---
source_url: https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/
source_type: blog-post
title: "The solution might be cancelling my AI subscription"
author: Simon Willison (relaying David Wilson's experience + Hacker News commenters)
date_published: 2026-05-31
date_extracted: 2026-06-09
last_checked: 2026-06-09
status: current
confidence_overall: anecdotal
issue: "#1122"
---

# The Solution Might Be Cancelling My AI Subscription

> Simon Willison relays David Wilson's first-person experience of AI-induced project
> sprawl — 16+ projects spun up without follow-through — and Wilson's "thermonuclear ADHD
> amplifier" framing; the Hacker News discussion surfaces the opposite effect for people
> with ADHD: agents enabling project completion for the first time.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, May 31, 2026; a short reflective post
  (~26 sentences) relaying David Wilson's experience with AI-driven project sprawl and
  curating the Hacker News discussion thread at news.ycombinator.com/item?id=48345896.
  All "David Wilson" quotes below are Wilson's words as block-quoted within Willison's
  post. Wilson's original post was not separately fetched; quotes are attributed to the
  Willison page as the canonical citable URL.)
- **Author credibility**: Simon Willison is the creator of Django, one of the most
  widely-read independent AI tooling commentators, and a prolific daily practitioner
  maintaining 200+ tools. He opens by calling Wilson's experience "very relatable" — this
  is personal identification, not neutral relay. David Wilson is a practitioner whose
  16+ abandoned AI-assisted projects illustrate the named pattern. The three HN commenters
  are anonymous but self-identified as having ADHD; their accounts are individually
  anecdotal but collectively corroborate a mechanistically distinct outcome.
- **Scope**: Covers AI-agent-induced project proliferation and abandonment, the proposed
  solution of curtailing AI use, and the neurotype-conditional variation in outcomes.
  Does NOT cover: technical configurations for constraining session scope, maintenance
  cost economics (see `blog-simonwillison-james-shore-maintenance-costs.md`), team-level
  adoption dynamics, or code quality. This is a short personal-reflection post, not a
  systematic analysis.

## Extracted Claims

### Claim 1: Coding agents can produce a working, tested, documented project from a vague idea in less than one hour

- **Evidence**: Willison's first-person observation. He notes the output "looks like a
  carefully considered project evolved over the course of many weeks."
- **Confidence**: anecdotal (single practitioner self-report; consistent with the broader
  corpus's evidence on agentic coding throughput)
- **Quote**: "I'm finding that coding agents can take me from a vague idea to a working
  solution, one with tests and documentation and that _looks_ like a carefully considered
  project evolved over the course of many weeks... in less than an hour."
- **Our assessment**: This is the enabling mechanism for the anti-pattern. Sub-hour
  project scaffolding fundamentally changes the cost structure of starting projects —
  when starting is cheap and finishing is never required, the rational response to any
  itch is to start. The same productivity velocity claim appears in
  `blog-simonwillison-vibe-coding-agentic-engineering.md` from a different angle (SDLC
  disruption); this source adds the individual discipline consequence: each sub-hour start
  adds to an unbounded backlog.

### Claim 2: AI agents cause developers to build projects they did not intend to build, starting from trivial requests that balloon into unrequested solutions

- **Evidence**: David Wilson's direct self-report about 16+ projects, quoted by Willison.
  Willison identifies the experience as "very relatable."
- **Confidence**: anecdotal (two practitioners; consistent with the broader corpus)
- **Quote**: "I didn't mean to build most of these things. Usually the Claude session
  started with something like '_write a quick script for X_', and one hour later the
  result is not a _quick script for X_, nor in the usual case is my problem solved,
  whatever the original itch happened to be." (David Wilson, as quoted by Simon Willison)
- **Our assessment**: This is a specific named anti-pattern: scope creep driven by agent
  momentum rather than user intention. The agent, given a minimal prompt, builds toward
  a complete solution; the user, seeing progress, continues the session rather than
  stopping at the original scope. One hour later, the user has a project they didn't want
  and the original problem is unsolved. This is the attention-capture problem of agentic
  coding in its concrete form.

### Claim 3: For many users, AI agents function as a "thermonuclear ADHD amplifier" — cheap, low-friction rewards drive project sprawl and undermine sustained commitment

- **Evidence**: David Wilson's quoted characterization, corroborated by Willison finding
  it "very relatable." Wilson extends the observation to "every single one of my adult
  friends."
- **Confidence**: anecdotal (two practitioners' observations; no measured data; the
  neurological framing is imprecise but the behavioral description is specific)
- **Quote**: "It's a thermonuclear ADHD amplifier and I have seen the same effect in every
  single one of my adult friends. Folk running 3 screens simultaneously working on totally
  unrelated 'projects' they have little hope of maintaining, and such little commitment to
  the outcome that the time is obviously wasted." (David Wilson, as quoted by Simon Willison)
- **Our assessment**: The "thermonuclear ADHD amplifier" framing is vivid but technically
  imprecise — Wilson is not claiming the tool causes ADHD, but that it amplifies
  attention-fragmentation patterns that exist broadly in neurotypical users. The underlying
  mechanism is classic operant conditioning: variable-ratio reinforcement at low cost. Each
  session produces a satisfying artifact (the working prototype), rewarding the behavior
  of starting a new session; the reward is immediate, the cost (abandoned project debt) is
  deferred. This is structurally similar to social media engagement traps. For the guide:
  acknowledge the "ADHD" framing while noting the mechanism applies to neurotypical
  practitioners as a general attention pattern.

### Claim 4: Even technically excellent AI-generated code provides no value if the project is immediately abandoned

- **Evidence**: Willison's direct logical observation. The concession "even if the code is
  rock solid" explicitly accepts output quality and still finds the outcome valueless
  without maintenance commitment.
- **Confidence**: anecdotal (logical claim, not empirical; but the logic is sound and
  connects to the broader corpus's evidence on maintenance cost dynamics)
- **Quote**: "Even if the code is rock solid, there's a limit to how many projects like
  that I can sensibly care for - and if they're instantly abandoned, what value was there
  from creating them in the first place?"
- **Our assessment**: This is the crucial insight that separates this source from the
  "AI produces low-quality code" concern (already addressed by `paper-miller-speed-cost-quality.md`).
  This source adds a different dimension: even high-quality AI-generated code has zero
  realized value if the project is abandoned. Combined with Claim 1 (sub-hour scaffolding),
  this implies a productivity trap: fast creation of high-quality but abandoned projects
  is not productivity — it is waste with extra steps. The "AI makes coding 10x faster"
  claim is meaningless without commitment to completion and maintenance.

### Claim 5: The only proposed solution to AI-driven project sprawl is curtailing or cancelling AI use, because low-friction conditions make discipline unsustainable

- **Evidence**: David Wilson's explicit conclusion — "I have no idea how to manage AI at
  present except by curtailing use" — and Willison's admission that he's been trying to
  develop discipline "for decades."
- **Confidence**: anecdotal (practitioner prescription; other practitioners may have found
  different approaches not captured in this source)
- **Quote**: "I have no idea how to manage AI at present except by curtailing use, because
  a tool producing a cheap reward with minimal input and no friction can only be a
  liability, and achieving that realisation is probably the only real contribution of AI
  to date." (David Wilson, as quoted by Simon Willison)
- **Our assessment**: Wilson's framing is notably strong — not "curtailing use is one
  option" but "I have no idea how to manage AI except by curtailing use." The "cheap
  reward with minimal input and no friction can only be a liability" claim makes an
  implicit argument that some friction is load-bearing: it acts as a commitment filter,
  and removing it removes the filter. This suggests that effective AI workflow design may
  deliberately need to *add* friction as a countermeasure — explicit scope declarations
  before session start, project commitment rituals, time limits — rather than further
  optimizing for zero friction. Friction is a feature, not a bug, when managing attention
  and commitment.

### Claim 6: The critical skill for sustainable AI-assisted development is discipline — but this is persistently difficult to develop even for self-aware practitioners

- **Evidence**: Willison's self-report: he finds Wilson's experience "relatable" and
  admits he's been "trying to figure that one out for decades."
- **Confidence**: anecdotal (self-deprecating self-report from a credible practitioner
  with 25+ years of experience)
- **Quote**: "I'm hopeful that the critical skill to develop here is _discipline_. That's
  not great news for me: I've been trying to figure that one out for decades!"
- **Our assessment**: Willison's honesty is the signal. Discipline is the named solution,
  but he explicitly lacks confidence in his ability to develop it. If a highly analytical,
  self-aware senior practitioner finds discipline difficult to maintain in low-friction AI
  environments, the solution likely needs to be structural (workflow design, harness
  constraints, deliberate friction) rather than individual (personal resolve). "Develop
  discipline" is an inadequate guide recommendation; actionable structural patterns are
  needed.

### Claim 7: For people with ADHD, AI agents produce the opposite effect — enabling project completion before interest wanes, rather than amplifying distraction

- **Evidence**: Multiple HN commenters self-identifying as having ADHD, independently
  reporting positive focus and completion outcomes. Willison explicitly frames the HN
  discussion as "a number of comments from people with ADHD who are finding agents help
  them achieve the focus they've been missing."
- **Confidence**: anecdotal (anonymous self-reports on HN; multiple independent voices
  reporting the same outcome is meaningful despite the anecdotal ceiling)
- **Quote**: "... for me (also ADHD) it's kind of the opposite. I'm finishing side projects
  for the first time ever because I can actually get them working before I get bored of
  them." (HN commenter, as quoted by Simon Willison)
- **Our assessment**: The same low-friction, fast-reward property that Wilson identifies as
  harmful for neurotypical users appears beneficial for ADHD users, because it changes
  the temporal relationship between starting and finishing. For ADHD, the historical
  problem is losing interest before completion; AI agents collapse the completion timeline
  to within the interest window — the finishing happens before the boredom arrives. This
  is not merely an anecdotal exception; it is a mechanistically coherent difference in how
  the speed property interacts with different attention patterns.

### Claim 8: AI agents can replace external stimulation and focus mechanisms for neurodiverse users, enabling sustained engagement that previously required coping strategies

- **Evidence**: HN commenter's first-person account of replacing EDM music with agent
  conversation as a focus mechanism, with specific behavioral details (inbox zero, cross-
  team participation) suggesting genuine lived experience.
- **Confidence**: anecdotal (single HN commenter; richly described with concrete specifics)
- **Quote**: "As someone with ADHD I feel like AI is a salve for my mind. I used to listen
  to intense EDM while working. Now I sit in silence and talk to my agents. I maintain
  inbox zero. I absorb and comment across all relevant projects, even outside my team. I
  literally feel like I have a support team for the first time." (HN commenter, as quoted
  by Simon Willison)
- **Our assessment**: The mechanism described is: AI agent conversation provides continuous
  stimulation required for focus, replacing an EDM coping strategy. The commenter is not
  describing AI as a productivity tool in the conventional sense but as a cognitive
  environment — an ambient stimulation channel that enables sustained attention. For the
  guide: AI tools may be transformatively beneficial for neurodiverse team members in ways
  that are difficult to capture in standard productivity metrics, and difficult to predict
  from aggregate team-level data.

### Claim 9: The impact of AI agent use on attention, focus, and project completion varies fundamentally by neurotype — the same tool creates divergent outcomes

- **Evidence**: The full structure of the post: Wilson's (neurotypical) experience of
  distraction and sprawl, Willison's corroboration, and multiple independent ADHD-positive
  reports from the HN thread. Willison explicitly curates both sides.
- **Confidence**: anecdotal (practitioner observations; no controlled study; the divergence
  is mechanistically coherent and independently reported)
- **Quote**: (no direct quote captures this synthesis; see Our assessment)
- **Our assessment**: This is the most guide-relevant meta-claim in the source: one-size-
  fits-all productivity guidance for AI tools may be wrong. The "AI makes you more/less
  focused" framing is neurotype-conditional. For team adoption guidance: a team where
  some members have ADHD may show mixed aggregate productivity results while neurotypical
  members experience focus degradation — or vice versa. Team-level averages can mask
  structurally opposite individual experiences. The guide should name this explicitly:
  AI agent adoption outcomes are not universal and neurotype is a meaningful moderating
  variable.

## Concrete Artifacts

### David Wilson's Pattern Description (verbatim, block-quoted in Willison's post)

```
Simon Willison, simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/
Quoting David Wilson:

"I didn't mean to build most of these things. Usually the Claude session started with
something like '_write a quick script for X_', and one hour later the result is not a
_quick script for X_, nor in the usual case is my problem solved, whatever the original
itch happened to be."

"On that last point, this technology is horrific for attention."

"It's a thermonuclear ADHD amplifier and I have seen the same effect in every single one
of my adult friends. Folk running 3 screens simultaneously working on totally unrelated
'projects' they have little hope of maintaining, and such little commitment to the outcome
that the time is obviously wasted."

"This is a very real problem."

"I have no idea how to manage AI at present except by curtailing use, because a tool
producing a cheap reward with minimal input and no friction can only be a liability, and
achieving that realisation is probably the only real contribution of AI to date."
```

### Willison's Own Framing (verbatim)

```
Simon Willison, simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/

PROJECT VELOCITY OBSERVATION:
"I'm finding that coding agents can take me from a vague idea to a working solution,
one with tests and documentation and that _looks_ like a carefully considered project
evolved over the course of many weeks... in less than an hour."

VALUE QUESTION:
"Even if the code is rock solid, there's a limit to how many projects like that I can
sensibly care for - and if they're instantly abandoned, what value was there from
creating them in the first place?"

DISCIPLINE AS SOLUTION:
"I'm hopeful that the critical skill to develop here is _discipline_. That's not great
news for me: I've been trying to figure that one out for decades!"
```

### HN Commenters — ADHD-Positive Outcomes (verbatim, block-quoted in Willison's post)

```
Simon Willison, simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/
Quoting Hacker News thread: news.ycombinator.com/item?id=48345896

Commenter 1 (self-identified ADHD):
"... for me (also ADHD) it's kind of the opposite. I'm finishing side projects for the
first time ever because I can actually get them working before I get bored of them."

Commenter 2 (self-identified ADHD):
"As someone with ADHD I feel like AI is a salve for my mind. I used to listen to intense
EDM while working. Now I sit in silence and talk to my agents. I maintain inbox zero. I
absorb and comment across all relevant projects, even outside my team. I literally feel
like I have a support team for the first time."

Commenter 3 (prone to hyperfocus):
"For those of us prone to hyperfocus, working with AI can provide the kinds of stimulation
we crave. I can hardly remember a time when I've felt more engaged with my work, more
productive, and more badass."
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 1 ("Vibe-coding accelerates app
    development to the point where the release cadence becomes blog-post-like rather than
    product-launch-like"): Willison's sub-hour scaffolding observation (Claim 1 above)
    is the same underlying capability seen from a different angle. The RSS note documents
    the positive cadence framing (frequent tool production is a new cultural mode); this
    note documents the negative consequence of the same capability (the frequency without
    commitment creates abandoned project debt). Together they establish both sides of the
    high-velocity production dynamic.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5 ("Evidence of actual
    sustained use is now the primary quality signal for software, replacing artifact
    inspection"): Claim 4 above (abandoned projects are valueless despite high code quality)
    is the inverse framing. If sustained use is the new quality signal, immediately
    abandoned projects — however well-constructed — score zero on that quality metric.
    These two claims are structurally complementary: the vibe-coding note identifies what
    to look for as a quality proxy (use evidence); this note names the failure mode that
    scores zero on that proxy (no use because the project was never maintained).

- **Extends**:
  - `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1 ("AI coding agents only
    produce a net productivity benefit if they reduce maintenance costs by exactly the
    inverse of their productivity gain ratio"): This source adds a degenerate case Shore's
    framework doesn't cover — projects that are immediately abandoned generate no ongoing
    maintenance costs *and* no ongoing value. Wilson's pattern (16+ abandoned projects) is
    where Shore's model's productivity gain is effectively zero because the projects are
    never used. Shore addresses maintained-but-costly projects; this source addresses
    commitment-abandoned projects. Together they establish a two-risk axis: (1) maintained
    with accumulating maintenance debt (Shore's Hotel California), (2) abandoned with zero
    realized value (Wilson's anti-pattern).
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1 ("The boundary between
    vibe coding and responsible agentic engineering has begun to blur even for experienced
    professionals"): Wilson's pattern is a further extension of this blur into commitment
    behavior. In vibe coding, projects are started without review expectations; in
    responsible agentic engineering, projects are reviewed and maintained. Wilson describes
    a third mode: projects polished enough to look maintained, but abandoned — neither
    fully vibe-coded (no review) nor responsibly engineered (no maintenance commitment).
    This source extends Willison's own blur in a direction he didn't name in the
    vibe-coding note: the blur also affects *commitment*, not just *review standards*.

- **Contradicts**: None filed. The ADHD-positive perspective (Claims 7–8) does not
  contradict existing notes — no prior corpus source claims AI agents universally harm
  focus. It adds neurotype as a conditioning variable to claims stated more broadly
  elsewhere. The implicit Wilson tension ("no friction can only be a liability") with
  sources that frame friction reduction positively is not a contradiction at the claim
  level — those sources address technical execution friction, not commitment-gating
  friction; the friction types are distinct.

- **Novel**:
  - **Neurotype as a moderating variable for AI agent productivity outcomes**: No other
    corpus source documents that the same agent use pattern produces opposite outcomes
    (focus vs. distraction, completion vs. sprawl) depending on neurotype. This is the
    only corpus source that explicitly names neurotype as a conditioning variable in AI
    adoption outcomes. Any guide claim about AI's effect on developer attention or focus
    must acknowledge this conditionality.
  - **Low friction as a load-bearing feature**: Wilson's framing — "a tool producing a
    cheap reward with minimal input and no friction can only be a liability" — is a direct
    argument that zero-friction is not unconditionally good. No other corpus source makes
    this argument. Most sources treat friction reduction as unambiguously positive. This is
    the first to argue that commitment-gating friction serves a filtering function: removing
    it removes the filter.
  - **The "project I didn't mean to build" anti-pattern**: No prior corpus source names the
    specific failure mode where an agent session started for a minimal task produces an
    unrequested complete project, leaving the original problem unsolved. This is a specific,
    nameable anti-pattern — scope creep driven by agent momentum, not user intention.
  - **Discipline as a persistently unsolved structural challenge**: Willison's admission
    that he's been trying to develop discipline "for decades" frames this as structural,
    not individual. No prior corpus source discusses discipline as a persistent unsolved
    challenge for senior AI practitioners, with the implication that workflow and harness
    design solutions are needed rather than relying on individual resolve.

## Guide Impact

- **Ch01 (Daily Workflows — Session Scoping)**: Add the "project I didn't mean to build"
  anti-pattern (Claim 2) as a named failure mode. The specific shape — "quick script for
  X" → one hour later → unrequested full project → original problem unsolved — needs a
  concrete counter-workflow: state scope explicitly before session start, set a time
  limit, and notice when agent output has expanded beyond stated intent. This is
  immediately actionable.

- **Ch02 (Harness Engineering — Deliberate Friction Design)**: Claims 5 and 6 together
  imply that harness design should deliberately add commitment-gating friction before new
  project sessions begin. This is counterintuitive — most harness design aims to reduce
  friction — but the argument is that commitment-gating friction (explicit scope
  declaration, time commitment prompt, project registration) is a filter that prevents
  the Wilson anti-pattern. Guide should recommend friction-as-feature patterns for teams
  experiencing project sprawl, distinguishing clearly between execution friction (reduce)
  and commitment friction (preserve or add).

- **Ch04 / Ch05 (Adoption Guidance — Neurotype Considerations)**: Claim 9's neurotype-
  conditionality (Claims 7–8 as ADHD-positive evidence) directly implies that team-level
  adoption guidance should account for neurodiverse team members. Team-wide productivity
  surveys may mask structurally opposite individual experiences. Guide should recommend:
  (a) individual self-reports alongside aggregate metrics; (b) acknowledging that AI tools
  may be transformatively beneficial for neurodiverse members even when team numbers are
  neutral; (c) designing workflow constraints that address the discipline challenge for
  neurotypical users without undermining AI's effectiveness for ADHD users.

- **Ch04 (Productivity Claims Calibration)**: Claim 4 — rock-solid abandoned code has no
  value — directly challenges narratives focused on code generation speed as the primary
  productivity metric. Guide should note explicitly that the productivity benefit of AI
  tools is conditional on project maintenance commitment, not just code quality or
  generation speed. The unit of productivity measurement should be completed, used,
  maintained projects — not lines generated or time-to-scaffold.

## Extraction Notes

- **Short source**: The Willison post is approximately 26 sentences. All sentences were
  read in document order via WebFetch. No sub-pages were followed; the David Wilson post
  linked from the Willison page was not separately fetched — all Wilson quotes were already
  block-quoted in Willison's post.
- **HN thread**: The Hacker News thread (news.ycombinator.com/item?id=48345896) was not
  separately fetched. The three commenter quotes are drawn verbatim from Willison's post,
  which selected and reproduced them. These are exactly the quotes Willison chose to
  highlight.
- **Attribution of "David Wilson" quotes**: Sentences 4–9 and sentence 13 in the source
  appear in block-quoted sections introduced by Willison with "David lists 16+ projects
  he's spun up with AI tooling, and concludes:" and "David doesn't think this is
  sustainable at all:" respectively. All are clearly contextually attributed to Wilson
  within the post.
- **Confidence ceiling: anecdotal**: The source is short-form personal reflection with no
  measured data, no controlled comparison, and predominantly anonymous HN commentary. The
  neurotype-conditional finding (Claims 7–9) is directionally important but backed only
  by a handful of HN self-reports. Cite for named patterns and direction, not empirical
  frequency or magnitude.
- **Cross-reference verification**: All cited claim numbers verified against source notes
  by document-order count:
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 1 (line 45): "Vibe-coding
    accelerates app development to the point where the release cadence becomes
    blog-post-like rather than product-launch-like" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1 (line 48):
    "The boundary between vibe coding and responsible agentic engineering has begun to
    blur even for experienced professionals" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5 (line 124):
    "Evidence of actual sustained use is now the primary quality signal for software,
    replacing artifact inspection" — verified.
  - `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1 (line 50): "AI coding
    agents only produce a net productivity benefit if they reduce maintenance costs by
    exactly the inverse of their productivity gain ratio" — verified.
