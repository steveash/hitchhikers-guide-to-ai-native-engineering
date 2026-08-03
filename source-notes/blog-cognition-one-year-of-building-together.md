---
source_url: https://cognition.com/blog/one-year-of-building-together
source_type: blog-post
title: "One Year of Building Together"
author: Scott Wu & Jeff Wang (Cognition)
date_published: 2026-07-14
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: emerging
issue: "#2454"
---

# One Year of Building Together

> Cognition co-founders Scott Wu and Jeff Wang's one-year retrospective on the
> Cognition/Windsurf merger, combining a founding-story narrative with a
> month-by-month product changelog (July 2025-July 2026), headline growth
> metrics (team 44→350, revenue run rate $73M→$500M+, 20M+ lines of code
> written), and a capability-progression claim ("Devin has matured from a
> junior engineer to operating at a mid-to-senior level: launching,
> scheduling, and managing other Devins") that ties together several
> previously-documented product features under one narrative arc.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, byline "By Scott
  Wu & Jeff Wang," published "07.14.26" per the page's own byline format —
  the same MM.DD.YY convention used across this corpus's other Cognition
  posts). Both authors are named individually and are Cognition's/Windsurf's
  co-founders/CEOs (Scott Wu, Cognition; Jeff Wang, ex-Windsurf), giving this
  a stronger individual-attribution standard than the anonymous "Cognition
  Team" byline used on several other posts in this corpus (e.g.
  `blog-cognition-devin-schedule-devins.md`, `blog-cognition-auto-triage.md`).
- **Author credibility**: First-party founder retrospective, published on the
  one-year anniversary of Cognition's acquisition/merger with Windsurf. This
  is not a technical or methodology post — no benchmark, no customer quote, no
  named engineering detail — but it is dense with quantified business metrics
  (team size, revenue run rate, lines of code) that are checkable in
  direction even if not independently audited, and it discloses the founding
  story (a 72-hour acquisition timeline) in specific, dated terms rather than
  vaguely. As with other Cognition first-party posts in this corpus, treat
  favorable framing and headline numbers as vendor-reported and unaudited.
- **Scope**: Covers the Cognition/Windsurf merger origin story (July 2025),
  a capability-progression narrative for Devin over the following year, a
  month-by-month product changelog from July 2025 through July 2026, three
  headline growth metrics (team size, revenue run rate, lines of code
  written), the company's global office footprint, and a closing
  forward-looking statement about "self-driving software development." Does
  **not** cover: any accuracy, reliability, or session-level metric for any
  named feature; per-feature adoption numbers; the methodology behind any of
  the three headline growth figures; or technical detail for any of the
  ~30 named product releases in the changelog (each of which is named only
  by title, not described).

## Extracted Claims

### Claim 1: Cognition frames Devin's one-year capability arc as a progression from "junior engineer" to "mid-to-senior level," specifically naming self-scheduling, orchestration of other Devins, and cross-Devin learning from prior agent history as the defining new capabilities
- **Evidence**: Direct progression statement under the "The world has changed
  in a year" heading, contrasting Devin's capabilities "a year ago" against
  "today."
- **Confidence**: emerging (first-party retrospective capability claim with
  no benchmark or metric attached, but naming specific, checkable mechanisms
  — scheduling, managing other Devins, cross-agent learned history — rather
  than a vague "Devin got better" statement)
- **Quote**: "Today, Devin has matured from a junior engineer to operating at a mid-to-senior level: launching, scheduling, and managing other Devins, with each new Devin learning from the history of the agents before it."
- **Our assessment**: This is the single most guide-relevant sentence in the
  post — it is Cognition's own framing device for tying together two
  separately-documented product features (self-scheduling, per
  `blog-cognition-devin-schedule-devins.md`; manager-child delegation, per
  `blog-cognition-multi-agents-working.md` Claim 12) under one narrative of
  agent-lifecycle maturation. The specific phrase "each new Devin learning
  from the history of the agents before it" is new to this corpus: neither
  of those two more detailed feature-level sources describes cross-session,
  cross-*agent* (not just cross-run, same-agent) history transfer — this is
  a broader memory claim than `blog-cognition-devin-schedule-devins.md`
  Claim 3's same-schedule state persistence ("Devin carries state between
  runs... reads and writes its own notes across sessions"), which is scoped
  to one recurring schedule, not to newly-spawned Devins inheriting history
  from prior, distinct agent instances. No mechanism is disclosed for how a
  "new Devin" accesses "the history of the agents before it" — this should
  be read as an aspirational/summary framing, not a documented architecture.

### Claim 2: The same progression narrative names self-testing via computer use, self-verification, and autofixes as the other defining capability shift over the year, alongside the orchestration capabilities in Claim 1
- **Evidence**: Direct continuation of the same progression statement,
  immediately following Claim 1's quote.
- **Confidence**: emerging (first-party summary claim, restating capabilities
  documented at implementation depth elsewhere in this corpus)
- **Quote**: "Not only writing code, but testing its own work with computer use, self-verification, and autofixes."
- **Our assessment**: This is the marketing-summary-level restatement of the
  self-verification workflow already documented in full implementation
  detail by `blog-cognition-verifying-agentic-development.md` (test-plan
  grounding, in-session annotation, deterministic "skills," structured test
  reports, and two named failure modes). This source adds no new mechanism
  detail beyond that note; its value here is only in confirming that
  Cognition itself frames self-verification as one of the year's two
  headline capability shifts (alongside orchestration, Claim 1), rather than
  as one feature among many in the changelog.

### Claim 3: Cognition explicitly positions itself as "the Switzerland of AI" and cites two specific mechanisms — Arena Mode and a public leaderboard — as evidence of vendor-neutral model evaluation
- **Evidence**: Direct self-positioning statement under "The future arrived"
  heading, in the same paragraph describing Cognition's own SWE-1.x model
  line.
- **Confidence**: anecdotal (a stated self-positioning claim/slogan, not a
  measured or independently-audited neutrality claim; the post gives no
  detail on how many non-Cognition models Arena Mode or the leaderboard
  cover, or how "neutral" evaluation is operationally ensured)
- **Quote**: "We like to call ourselves the Switzerland of AI, so we put model evaluation in the open with Arena Mode and a public leaderboard."
- **Our assessment**: This is a novel synthesis for this corpus: it
  explicitly frames two previously-documented but separately-covered
  Cognition mechanisms — Windsurf Arena mode (internal blind subjective
  preference testing, documented in `blog-cognition-swe16-preview.md` Claim
  11: "Windsurf Arena mode was a first step towards this, by measuring blind
  subjective preference on real coding tasks") and the public FrontierCode
  leaderboard (documented in full in `blog-cognition-frontiercode.md`, whose
  Claim 10 shows Cognition's own SWE-1.7 ranking below several competitor
  models on that leaderboard, "a data point that argues against dismissing
  FrontierCode as pure self-serving marketing") — as a single, named
  "Switzerland of AI" positioning strategy. Neither of those two more
  detailed sources uses this framing language; this post is the only place
  in the corpus that names the neutrality positioning explicitly and ties
  the two mechanisms together as evidence for it. The changelog (see
  Concrete Artifacts) separately dates "Arena Mode" to January 2026, which
  is consistent with the swe16-preview post (published 2026-03-01)
  referring to Arena mode as already-existing at that time.

### Claim 4: Cognition reports team growth from 44 to 350 people and revenue run rate growth from $73M to $500M+ "since merging the brands," alongside 20M+ lines of code written by the team "locally" over the year
- **Evidence**: Direct statement of three headline metrics in a single
  closing sentence of "The future arrived" section.
- **Confidence**: anecdotal (self-reported, unaudited business metrics with
  no stated measurement window boundaries beyond "since merging the
  brands," no definition of what counts as revenue run rate, and no
  clarification of what "wrote 20M+ lines of code locally" measures — e.g.
  whether it includes agent-generated code, is limited to the combined
  team's own commits, or excludes customer-side Devin usage entirely)
- **Quote**: "Along the way, our team wrote 20M+ lines of code locally, grew from 44 to 350 people, and grew revenue run rate from $73M to $500M+ since merging the brands."
- **Our assessment**: These three figures are new to this corpus — no
  existing source note reports Cognition's team size or revenue run rate.
  They should be cited as unaudited, vendor-reported business-viability
  evidence (a ~6.8x revenue run-rate increase and ~8x headcount increase in
  roughly one year), useful as directional evidence that AI-native coding
  tooling has commercial traction at scale, but not verifiable from this
  source alone — no third-party financial disclosure, funding-round
  valuation, or customer count accompanies these numbers. The "20M+ lines
  of code" figure is also notable for what it does *not* claim: the
  sentence attributes the lines specifically to "our team," not to Devin,
  making this a claim about combined Cognition+Windsurf engineering output
  rather than an AI-generated-code volume metric — a distinction the guide
  should preserve if citing this figure, since it is easy to misread as an
  "AI wrote 20M lines" statistic.

### Claim 5: Cognition's post-merger global footprint spans five named offices — San Francisco, New York, London, Singapore, and Tokyo — with further international expansion stated as planned
- **Evidence**: Direct statement under "The future arrived" heading, naming
  the five cities and a forward-looking expansion statement.
- **Confidence**: settled (a direct, checkable factual statement about
  current office locations, not a projected or estimated figure)
- **Quote**: "And we became a global company: Cognition's offices now span San Francisco, New York, London, Singapore, and Tokyo. Our teams are on the ground in even more places, and we'll be opening even more international offices soon."
- **Our assessment**: A minor but concrete data point on organizational
  scale one year post-merger, useful mainly as supporting context for Claim
  4's headcount and revenue figures — a five-city footprint is consistent
  with, though does not independently verify, a 350-person combined team.

### Claim 6: The merger was completed within a single 72-hour window (a Friday-evening call to a signed agreement by Monday morning and a same-day public announcement), driven by the founders' assessment that the two companies' organizational strengths were exactly complementary — Cognition's engineering org paired with Windsurf's GTM org
- **Evidence**: Direct origin-story narrative in the article's opening
  section, including a specific timeline and an explicit statement of the
  complementarity rationale.
- **Confidence**: settled for the timeline (a specific, dated, checkable
  historical account of a publicly-announced transaction); anecdotal for
  the complementarity framing (the founders' own retrospective
  characterization of why the deal made sense, not an independently
  audited assessment)
- **Quote**: "One year ago today capped off the craziest 72 hours of our lives. The story of how Cognition and Windsurf came together has been told many times: a first call after 5 p.m. on a Friday, a flurry of texts and emails, almost no sleep, a signed definitive agreement by Monday morning, an announcement tweet that afternoon."
- **Quote (complementarity)**: "Cognition had built one of the best engineering orgs in Silicon Valley and was looking for a GTM org; Windsurf had built one of the best GTM orgs and was looking for engineering. Our products didn't even overlap: one of us had been building a cloud agent, the other an IDE."
- **Our assessment**: This is company-history narrative rather than an
  engineering or product claim, and its direct guide relevance is limited —
  but it is a concrete, dated example of a fast, decisive organizational
  merger specifically motivated by complementary capabilities (engineering
  vs. go-to-market) rather than overlapping product lines, which the guide
  could cite as a real-world instance if it ever discusses organizational
  integration patterns in AI-native companies. The article also discloses
  the human cost on the Windsurf side ("many members of the Windsurf team
  had just left for Google, recruiters were reaching out to everyone who
  remained, and customers were calling to understand what was happening"),
  which is a candid, non-flattering detail about the acquisition's
  immediate aftermath that a purely promotional retrospective could have
  omitted.

### Claim 7: Cognition explicitly frames uninterrupted product shipping cadence through the merger's organizational disruption as a deliberate signal, shipping a named release ("Wave 11," internally titled "Just Keep Shipping") only three days after the deal closed
- **Evidence**: Direct statement naming the specific release and its
  internal title, immediately following the merger-completion narrative.
- **Confidence**: settled (a specific, named, dated internal claim — a
  release name and a stated timing relative to a publicly dated event)
- **Quote**: "Three days after the deal closed, we shipped Wave 11. We called it 'Just Keep Shipping' and it set the tone for the year."
- **Our assessment**: This is a specific, citable example of a stated
  practice — treating uninterrupted release cadence through organizational
  upheaval (a merger, team departures, customer uncertainty per Claim 6) as
  a deliberate cultural signal rather than a side effect. It is presented
  only as a single anecdote from one company's own retrospective, not as a
  general recommendation, but it is a concrete instance the guide could use
  if discussing how engineering teams maintain momentum through
  organizational change.

### Claim 8: The article's own month-by-month product changelog (July 2025-July 2026) names roughly 30 individual feature releases, several of which correspond to and independently date features already documented elsewhere in this corpus
- **Evidence**: A full dated changelog list under "Just keep shipping,"
  reproduced verbatim in Concrete Artifacts.
- **Confidence**: settled (a first-party, dated list of the vendor's own
  named product releases — directly checkable against this corpus's
  existing per-feature source notes, several of which independently confirm
  the same month)
- **Quote**: "March 2026. New token-based plans, including Max. Devin can Manage Devins. Schedule Devins." / "May 2026. Android emulator support. Devin gets a Windows PC. Auto-Triage." / "June 2026. Security in Devin Review. FrontierCode. Devin Fusion." / "July 2026. Devin Security Swarm. Devin Security Vulnerability Remediation Program."
- **Our assessment**: This changelog is the most concretely useful artifact
  in the post for cross-checking this corpus's existing date attributions.
  Three entries independently corroborate existing source notes' own
  publish dates: "Schedule Devins" under March 2026 matches
  `blog-cognition-devin-schedule-devins.md` (published 2026-03-20); "Auto-Triage"
  under May 2026 matches `blog-cognition-auto-triage.md` (published
  2026-05-18); and "Devin Fusion" and "FrontierCode" under June 2026 match
  `blog-cognition-devin-fusion.md` (published 2026-06-29) and
  `blog-cognition-frontiercode.md` (original launch post published
  2026-06-08), respectively. No date conflict was found between this
  changelog and any existing corpus source note's own publish date. The
  changelog also names several features with no existing corpus source
  note (e.g. "Devin can Manage Devins," "Devin gets a Windows PC," "Devin
  Security Swarm," "Devin Security Vulnerability Remediation Program" — the
  latter two do have dedicated notes per a `source-notes/` directory
  listing, `blog-cognition-devin-security-swarm-launch.md` and
  `blog-cognition-devin-security-vulnerability-remediation-program.md`,
  though this extraction did not re-read those two notes to verify their
  dates against this changelog's "July 2026" placement).

### Claim 9: The SWE model line progressed through three named versions over the year — SWE-1.5 (served at ~1000 tokens/second), SWE-1.6, and SWE-1.7 — with SWE-1.7 described as launched "just last week" (i.e., roughly the week of 2026-07-07) and as "the most capable and efficient model we've trained to date"
- **Evidence**: Direct statement under "The future arrived" heading.
- **Confidence**: emerging (a first-party model-lineage and performance
  claim; the ~1000 tok/s figure for SWE-1.5 is stated approximately, and
  SWE-1.7's superiority is asserted without an accompanying benchmark score
  in this post)
- **Quote**: "We built our own models: SWE-1.5, served at ~1000 tokens per second, then SWE-1.6, then SWE-1.7, launched just last week — the most capable and efficient model we've trained to date."
- **Our assessment**: The "~1000 tokens per second" figure for SWE-1.5 here
  is a rounded approximation of the more precise "950 tok/s" figure this
  corpus already has for SWE-1.5 from two independent, more technical
  Cognition sources (`blog-cognition-swe16-preview.md` Claim 1: "SWE-1.6...
  runs equally as fast at 950 tok/s" as SWE-1.5; and
  `blog-cognition-multi-agents-working.md` Concrete Artifacts: "SWE-1.5: 950
  tok/sec"). This is not a contradiction meeting the MINER.md §4a bar — a
  retrospective post rounding 950 to "~1000" is an approximation, not a
  conflicting factual claim about the same measurement — but the guide
  should cite the more precise 950 tok/s figure from those two sources
  rather than this post's rounded figure. SWE-1.7 itself has no dedicated
  source note in this corpus at time of writing (confirmed via directory
  search of `source-notes/` — the corpus's SWE-model coverage currently
  stops at `blog-cognition-swe16-preview.md`), so this is currently the only
  place in the corpus that names SWE-1.7 or its "most capable and efficient
  model we've trained to date" claim; a future source mining a dedicated
  SWE-1.7 launch post (if one exists) would supersede this post as the
  primary citation for that model.

### Claim 10: The article closes by framing Cognition's forward direction as a shift toward "self-driving software development," in which engineers become "super engineers" and people who have never coded gain access to development capabilities previously unavailable to them
- **Evidence**: Direct closing statement under "What's next," referencing an
  unspecified "latest fundraise" announcement as the source of this framing.
- **Confidence**: anecdotal (a forward-looking vision/positioning statement,
  not a shipped capability or measured claim; the referenced "latest
  fundraise" announcement itself is not linked or fetched as part of this
  extraction)
- **Quote**: "As we shared when announcing our latest fundraise, we're now shifting to a world of self-driving software development." / "Engineers are becoming super engineers, and people who never coded before are able to leverage themselves in ways they never imagined."
- **Our assessment**: "Self-driving software development" is new phrasing to
  this corpus's Cognition coverage — prior sources use "self-verifying,"
  "autonomous," and "asynchronous" to describe Devin's trajectory, but not
  this specific automotive-autonomy analogy. It should be treated as a
  positioning statement for where Cognition says it is headed, not a
  description of a shipped capability — the post gives no concrete feature,
  metric, or example illustrating what "self-driving software development"
  means operationally beyond the "super engineers" framing, which itself is
  asserted without a supporting anecdote in this post (contrast with
  `blog-anthropic-cognition-fable5-frontier-trust.md`, which supports
  similar autonomy claims with a specific eight-hour unattended session
  anecdote).

## Concrete Artifacts

### Full month-by-month product changelog, verbatim
```
Source: cognition.com/blog/one-year-of-building-together, "Just keep shipping"

July 2025. Voice Mode. Named Checkpoints. @-mention past conversations.
Deeper Browser integration. Planning Mode on by default. Workflows and
Rules on JetBrains. Devin's MCP Marketplace.

August 2025. DeepWiki in the IDE. Vibe and Replace. Smarter Cascade. Faster
Tab. Dev Containers support. 100+ bug fixes in a single wave.

September 2025. Queued Messages.

October 2025. SWE-grep and SWE-grep-mini. IL6-ready.

November 2025. Windsurf Codemaps.

December 2025. Parallel agents. Git worktree support. Multi-pane Cascade.
Cascade Dedicated Terminal. Context Window Indicator. Cascade Hooks.
System-level Rules and Workflows for enterprise.

January 2026. Plan Mode. Megaplan. Agent Trace. Arena Mode.

February 2026. Tab v2. Variable Aggression. Autofix for review comments.

March 2026. New token-based plans, including Max. Devin can Manage Devins.
Schedule Devins.

April 2026. Adaptive. Per-message token counts. Daily limits removed.
Self-serve Devin plans. SWE-check.

May 2026. Android emulator support. Devin gets a Windows PC. Auto-Triage.

June 2026. Security in Devin Review. FrontierCode. Devin Fusion.

July 2026. Devin Security Swarm. Devin Security Vulnerability Remediation
Program.
```

### Headline growth and capability statements, verbatim
```
Source: cognition.com/blog/one-year-of-building-together, "The future arrived"

"We built our own models: SWE-1.5, served at ~1000 tokens per second, then
SWE-1.6, then SWE-1.7, launched just last week — the most capable and
efficient model we've trained to date. We like to call ourselves the
Switzerland of AI, so we put model evaluation in the open with Arena Mode
and a public leaderboard.

We launched Devin Review, Devin CLI, Devin 2.2, and Cognition for
Government.

Windsurf 2.0 brought every agent into a single command center. Then, we
finally unified into one brand with the launch of Devin Desktop, your home
for software engineering. Now Devin is available on every surface with any
agent and any model.

We put our money where our mouth is with the AI Productivity Guarantee. We
entered new industries and partnered with new teams like automakers and
systems integrators.

And we became a global company: Cognition's offices now span San
Francisco, New York, London, Singapore, and Tokyo. Our teams are on the
ground in even more places, and we'll be opening even more international
offices soon."

"Along the way, our team wrote 20M+ lines of code locally, grew from 44 to
350 people, and grew revenue run rate from $73M to $500M+ since merging
the brands."
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-devin-schedule-devins.md` Claim 3 (Devin "carries state
    between runs. It reads and writes its own notes across sessions") —
    corroborated at a summary level by this note's Claim 1 ("each new Devin
    learning from the history of the agents before it"), though this
    source's framing is broader (cross-*agent* history, not just
    cross-*run* state within one recurring schedule) and no mechanism is
    given here, so this should be read as a marketing-level restatement,
    not additional mechanism detail.
  - `blog-cognition-multi-agents-working.md` Claim 12 (manager-child
    delegation: "a manager Devin can break a larger task into pieces, spawn
    child Devins to work on them, and coordinate their progress through an
    internal MCP") — corroborated by this note's Claim 1 ("managing other
    Devins") as the same orchestration capability referenced at summary
    level in a company retrospective, one year (this post) after the
    original April 2026 practitioner deep-dive.
  - `blog-cognition-verifying-agentic-development.md` (Devin's computer-use
    self-testing workflow, documented at full implementation depth) —
    corroborated by this note's Claim 2 ("testing its own work with
    computer use, self-verification, and autofixes") as one of the
    company's own two headline capability shifts for the year, confirming
    that Cognition itself treats self-verification as a defining 2025-2026
    milestone rather than one feature among many.
  - `blog-cognition-swe16-preview.md` Claim 11 (Windsurf Arena mode as
    "blind subjective preference" testing) and
    `blog-cognition-frontiercode.md` (the public FrontierCode leaderboard,
    including Claim 10's observation that Cognition's own SWE-1.7 ranks
    below several competitors on it) — this note's Claim 3 ("Switzerland of
    AI... Arena Mode and a public leaderboard") is the first source in this
    corpus to name both mechanisms together under one explicit
    vendor-neutrality positioning claim; neither cited source uses this
    framing language independently.
  - `blog-cognition-devin-fusion.md`, `blog-cognition-frontiercode.md`,
    `blog-cognition-devin-schedule-devins.md`, and
    `blog-cognition-auto-triage.md` — this note's Claim 8 changelog
    independently corroborates each of those notes' own publish-date
    attributions (Schedule Devins/March 2026; Auto-Triage/May 2026; Devin
    Fusion and FrontierCode/June 2026), with no date discrepancy found.

- **Contradicts**: None filed. One near-miss was evaluated and rejected:
  this note's Claim 9 states SWE-1.5 was "served at ~1000 tokens per
  second," while `blog-cognition-swe16-preview.md` Claim 1 and
  `blog-cognition-multi-agents-working.md` Concrete Artifacts both give a
  more precise "950 tok/s" figure for the same model. This does not meet
  the `agents/MINER.md` §4a bar for a filed contradiction: "~1000" is an
  explicitly approximate figure ("~") in a non-technical retrospective post
  rounding a number two independent, more technical sources state precisely
  as 950 — a rounding/precision difference, not an opposing factual claim
  about the same measurement.

- **Extends**:
  - `blog-anthropic-cognition-fable5-frontier-trust.md` (Cognition SVP of
    Research Silas Alberti's account of Claude Fable 5 enabling ~8-hour
    unattended Devin sessions, and Cognition's founding bet that "agents
    should run in the cloud for hours at a time") — this note's Claim 6
    (the Cognition/Windsurf merger origin story) and Claim 10 ("self-driving
    software development," "super engineers") supply the company-history
    and forward-vision framing around the same underlying capability
    trajectory that source documents at the model-capability level; neither
    source overlaps on a specific claim, but together they place the
    Fable-5-enabled capability jump within Cognition's own one-year
    narrative arc.
  - `blog-cognition-devin-productivity-estimation.md` (Cognition's
    LLM-judge system for estimating "human-equivalent engineering hours"
    per Devin session, validated against 126 users across eight
    deployments) — this note's Claim 4 mentions "the AI Productivity
    Guarantee" by name (in the Concrete Artifacts verbatim passage) as a
    named commercial offering, without describing its mechanism. The
    productivity-estimation source is a plausible measurement basis for
    such a guarantee, but this post does not state that connection
    explicitly, and the productivity-estimation source note itself does
    not mention "AI Productivity Guarantee" by name — this is a plausible,
    not confirmed, link between the two sources, flagged here rather than
    asserted as fact.

- **Novel**: The three headline growth metrics (Claim 4: team 44→350,
  revenue run rate $73M→$500M+, 20M+ lines of code written) are new to this
  corpus — no existing source note reports Cognition's team size or revenue
  figures. The "Switzerland of AI" self-positioning framing (Claim 3) and
  the specific phrase "each new Devin learning from the history of the
  agents before it" (Claim 1) are also new. The merger origin story (Claim
  6, including the specific 72-hour timeline and the disclosed detail that
  departing Windsurf staff had "just left for Google") and the "Just Keep
  Shipping" continuity-through-disruption anecdote (Claim 7) are new
  business-history material not previously in this corpus's Cognition
  coverage, which has focused almost entirely on product/technical posts.
  "Self-driving software development" (Claim 10) as a named forward-looking
  framing is also new.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 1 as a citable, company-level
  framing statement tying together `blog-cognition-devin-schedule-devins.md`
  (self-scheduling) and `blog-cognition-multi-agents-working.md` Claim 12
  (manager-child delegation) under a single "agent lifecycle maturation"
  narrative — useful as a section-opening summary quote, but flag explicitly
  that "each new Devin learning from the history of the agents before it" is
  an unsubstantiated aspirational claim with no mechanism disclosed anywhere
  in this corpus's Cognition coverage, broader than the documented
  same-schedule state-persistence mechanism.

- **Chapter 03 (Verification)**: Add Claim 3 ("Switzerland of AI," Arena
  Mode + public leaderboard) as a named vendor-neutrality positioning claim
  when discussing `blog-cognition-frontiercode.md` — note explicitly that
  this framing is Cognition's own marketing language, and that the
  strongest evidence *for* it in this corpus remains FrontierCode's own
  Claim 10 (Cognition's SWE-1.7 ranking below competitors on its own
  leaderboard), not this post's slogan itself.

- **Chapter 05 (Team Adoption)**: Add Claim 4's growth metrics (team and
  revenue growth) as a business-viability data point when discussing
  whether AI-native engineering tooling has demonstrated commercial
  traction — flag clearly as self-reported and unaudited, with no
  methodology disclosed, consistent with how this corpus treats other
  vendor-reported business metrics (e.g. `blog-cognition-devin-productivity-estimation.md`'s
  more rigorously-disclosed figures by contrast). Add Claim 6 and Claim 7
  (the 72-hour merger timeline; shipping "Wave 11" three days after close)
  as a concrete example of maintaining engineering cadence through
  organizational disruption, if the guide ever covers how AI-native
  engineering orgs navigate M&A or team restructuring.

- **Chapter 01 (Daily Workflows) / Chapter 04 (Context Engineering)**: Add
  Claim 2 only as a corroborating summary reference alongside the
  implementation-depth source (`blog-cognition-verifying-agentic-development.md`)
  — this post adds no new technique detail and should not be cited as a
  primary source for self-verification mechanics.

## Extraction Notes

- WebFetch's default summarizing pass on this URL returned only a
  condensed ~200-word paraphrase that dropped the merger origin-story
  detail, the exact growth figures' framing sentence, and the full
  month-by-month changelog — consistent with the verbatim-extraction
  difficulty already documented for this vendor's site elsewhere in this
  corpus (e.g. `blog-cognition-devin-in-windsurf.md`,
  `blog-cognition-multi-agents-working.md` Extraction Notes). The full
  article was instead fetched via `curl` with a browser user-agent, the
  `<article>` element isolated from the raw HTML, and HTML tags stripped
  with a Python regex-based tag stripper. All quotes above were taken from
  that raw-text extraction and checked against the shorter WebFetch summary
  for consistency — no discrepancy was found beyond the expected loss of
  direct quotes and the full changelog in the summary.
- The article is short (~700 words across an intro, "The world has changed
  in a year," "The future arrived," "Just keep shipping" — which contains
  the 13-month changelog — and "What's next"). No outbound hyperlinks
  requiring follow-up were present in the extracted article body (the
  fetched `<article>` element contained no inline anchor tags to other
  Cognition posts); the "latest fundraise" reference in Claim 10 is
  unlinked in the fetched text and was not independently tracked down or
  fetched separately for this extraction, consistent with MINER.md §1's
  guidance to follow substantive linked pages, not unlinked references.
- Searched `source-notes/` for existing coverage before writing
  Cross-References and Novel: confirmed no existing source note reports
  Cognition's team size, revenue run rate, or "Switzerland of AI"
  framing; confirmed no dedicated SWE-1.7 source note exists (the corpus's
  SWE-model-line coverage currently stops at
  `blog-cognition-swe16-preview.md`, covering SWE-1.6-Preview). Re-read
  `blog-cognition-devin-schedule-devins.md` in full and confirmed Claim 3
  by number and content; re-read `blog-cognition-multi-agents-working.md`
  in full and confirmed Claim 12 by number and content; re-read
  `blog-cognition-swe16-preview.md` in full and confirmed Claim 1 and Claim
  11 by number and content; re-read `blog-cognition-frontiercode.md` in
  full and confirmed Claim 10 by number and content; re-read
  `blog-cognition-devin-in-windsurf.md`,
  `blog-cognition-verifying-agentic-development.md`,
  `blog-cognition-devin-productivity-estimation.md`, and
  `blog-anthropic-cognition-fable5-frontier-trust.md` in full for
  cross-referencing context. No claim number was guessed or approximated.
- The three separate Prospector triage comments on the source issue
  (#2454) list mutually inconsistent chapter-numbering guesses (one
  references "Ch02 Multi-Agent Patterns," another "Ch01 Daily Workflows,
  Ch02 Harness Engineering," a third adds "Ch03 Verification") — none
  matches the guide's actual chapter files exactly. This note's Guide
  Impact section cites the guide's actual chapter numbers and titles as
  read directly from the `guide/` directory
  (`00-principles.md` through `06-security-threat-model.md`), not the
  numbering used in any of the three triage comments.
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References → Contradicts for the one candidate (SWE-1.5 tokens/sec
  rounding) considered and rejected as an approximation, not a same-claim
  conflict. No contradiction issue filed.
- Confidence is rated `emerging` overall: this is a first-party founder
  retrospective with several specific, quantified business metrics (team
  size, revenue run rate, lines of code, a dated 72-hour merger timeline,
  a dated month-by-month changelog) that exceed pure marketing framing —
  but none of the headline figures has a disclosed methodology, no external
  or audited source corroborates the revenue or headcount numbers, and the
  post's forward-looking claims (Claim 10, "self-driving software
  development") are vision statements rather than shipped, measured
  capabilities. This is consistent with the confidence tier already
  assigned to this corpus's other Cognition retrospective/announcement
  posts (e.g. `blog-cognition-multi-agents-working.md`,
  `blog-cognition-devin-fusion.md`).
