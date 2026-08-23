---
source_url: https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams
source_type: blog-post
title: "Turning conversation into knowledge: how Slack builds human-agent teams"
author: Jaime DeLanghe (Slack CPO), interviewed by Anthropic staff
date_published: 2026-08-19
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: anecdotal
issue: "#2882"
---

# Turning conversation into knowledge: how Slack builds human-agent teams

> First-person interview with Slack's Chief Product Officer describing how
> Slack treats conversation history as reusable organizational knowledge,
> structures a human-agent "handoff cycle" around Claude in Slack, and
> spreads adoption through peer demonstration rather than mandate — while
> warning that activity metrics (messages, token usage) do not prove agent
> value.

## Source Context

- **Type**: blog-post (interview format, published on claude.com/blog,
  August 19, 2026; conversation between Anthropic staff and Jaime DeLanghe).
- **Author credibility**: Jaime DeLanghe is Slack's Chief Product Officer,
  speaking in first person about practices inside her own product
  organization and about how Slack (the product) is used internally at
  Slack. This is a single-company, single-executive account rather than an
  aggregated or audited study — comparable in evidentiary weight to the
  ABC Legal CTO account in `blog-anthropic-abc-legal-managed-agents.md`.
  It is also promotional by construction: published on Anthropic's own blog
  as a partner/customer story about a product ("Claude in Slack") Anthropic
  sells. Treat concrete practices and quotes as credible first-hand
  description of Slack's internal norms; treat the framing as advocacy for
  those norms rather than an independently validated methodology.
- **Scope**: Covers organizational and cultural practices for human-agent
  collaboration at Slack — public-by-default channels, a handoff-cycle
  model for dividing work between agents and humans, agent role
  specialization, peer-driven adoption, and a caution against activity-based
  measurement. Does NOT cover: technical harness details (no CLAUDE.md,
  hooks, or permission configuration), specific agent architectures, cost
  or ROI figures, or any quantified adoption metrics (the piece names
  "thousands of members" in one internal channel but gives no percentages,
  headcounts, or before/after numbers).

## Extracted Claims

### Claim 1: Slack defaults shared work channels to public specifically so that AI agents (not just humans) can build shared context from conversation history
- **Evidence**: Direct quote from DeLanghe describing the purpose of public
  channels in terms of both human and agent context-building.
- **Confidence**: emerging (first-person practitioner account of an
  internal norm; the underlying mechanism — agents can only read what is
  written down and visible — is a settled technical fact echoed elsewhere
  in the corpus)
- **Quote**: "You're building a shared understanding, a shared context for
  all of the work that's going to come next."
- **Our assessment**: This reframes "work in public" from a
  transparency/culture value (the usual framing) into an explicit
  agent-context-engineering practice: the channel's public visibility is
  treated as an input to what agents can learn and reuse, not just a norm
  for human collaboration. It is a practitioner-level restatement of the
  same mechanism named more formally in `blog-anthropic-human-agent-teams.md`
  Claim 3 ("if it's not written down and accessible, it doesn't exist" for
  agents).

### Claim 2: A private channel is invisible to every agent that would otherwise report on that work, making privacy-by-default a hidden cost for agent-assisted teams
- **Evidence**: Direct quote, stated as the specific downside of defaulting
  to private channels.
- **Confidence**: emerging (stated as a categorical practitioner claim, not
  measured, but logically follows from how LLM agents consume only visible
  text)
- **Quote**: "A private channel is a blind spot for every agent that
  reports on it."
- **Our assessment**: This is a sharper, more quotable version of the same
  point as Claim 1, framed as a cost rather than a benefit. It directly
  corroborates `blog-simonwillison-tobias-lutke-lehrwerkstatt.md` Claim 2
  (Shopify's River agent refuses DMs and pushes users to public channels so
  every conversation is searchable) — two independent companies converging
  on the same "public by default, private by exception" norm specifically
  because of agent visibility, not just human transparency culture.

### Claim 3: The core organizational unit for human-agent collaboration at Slack is a repeating "handoff cycle": agents do production work, a human reviews and decides, then hands work back for the next step
- **Evidence**: Direct quote defining the cycle explicitly, naming "Claude
  in Slack" as the mechanism powering it.
- **Confidence**: emerging (first-party description of an internal working
  pattern; the human-review-then-redirect structure matches recommended
  practice, not just Slack's private choice)
- **Quote**: "The core rhythm of a human-agent team is a cycle of
  handoffs. Powered by Claude in Slack, agents handle the production
  work—drafting, summarizing, monitoring, preparing—and pass the results to
  a person. The person reviews, decides, and redirects, then hands the work
  back for agents to carry out the next step."
- **Our assessment**: This names the same generator-then-human-review shape
  as the "Doer-Verifier" pattern in `blog-anthropic-human-agent-teams.md`
  Claim 8, but as a continuous *cycle* (agent → human → agent → human)
  rather than a one-shot check. The four verbs named for agent-side work
  (drafting, summarizing, monitoring, preparing) are a useful concrete
  enumeration of what "production work" means in this model, distinct from
  the decision-making retained by the human.

### Claim 4: DeLanghe's own workflow illustrates the handoff cycle concretely: her Monday routine opens with an agent-built daily briefing covering workshop recaps, flagged escalations, an AI news report, meeting prep, and a rewritten bio
- **Evidence**: First-person anecdote, given as a concrete example rather
  than an abstract description.
- **Confidence**: anecdotal (single executive's personal routine, offered
  as illustration, not a documented team-wide practice)
- **Quote**: "It's Monday morning, and I've just had my daily briefing that
  an agent has built for me."
- **Our assessment**: This is the most concrete artifact in the source —
  a specific bundle of agent-produced outputs (recap, escalations, news
  report, meeting briefings, a rewritten bio) waiting for one person's
  review each morning. It operationalizes Claim 3's abstract "drafting,
  summarizing, monitoring, preparing" into a template other teams could
  copy directly: a standing daily-briefing agent that aggregates several
  distinct content types for human review.

### Claim 5: Agents work best treated as specialized coworkers with distinct, clearly-felt roles rather than as general-purpose chatbots, and mandated (rather than felt) agent value causes teams to lose track of what the agent is for
- **Evidence**: Direct quote from DeLanghe on role clarity and adoption
  motivation.
- **Confidence**: emerging (practitioner opinion, consistent with role-
  definition guidance elsewhere in the corpus, but not independently
  measured)
- **Quote**: "I like to think that agents are kind of like coworkers."
- **Quote** (mandated vs. felt value): "if the value of the agent feels
  mandated rather than very clearly felt and understood by the people using
  it, it's really hard to remember what the thing is for."
- **Our assessment**: The "coworker" framing corroborates the role-roster
  recommendation in `blog-anthropic-human-agent-teams.md` Claim 5 (teams
  without defined agent roles fragment into duplicated shadow-AI usage).
  The "mandated vs. felt" distinction adds a genuinely new angle: it is a
  claim about adoption psychology, not architecture — value that is
  imposed top-down erodes because users lose the felt reason for using the
  tool, which argues for bottom-up, demonstrated value (see Claim 7) over
  top-down rollout mandates.

### Claim 6: Message and token-usage volume are necessary but insufficient signals of AI value; teams should measure business outcomes, not activity
- **Evidence**: Three direct quotes stacked together, explicitly contrasting
  activity metrics with outcome measurement.
- **Confidence**: emerging (practitioner methodological claim; directionally
  consistent with general measurement best-practice, not backed by a named
  study or dataset in this source)
- **Quote**: "Do we want people to send more messages?" ... "Maybe not.
  Sending messages might not actually mean that they're getting more out of
  Slack."
- **Quote**: "Token usage tells you the lights are on, but while that's
  important to know, it's not sufficient."
- **Quote**: "Activity tells you adoption is happening, not that it's
  working."
- **Our assessment**: This is a specific, quotable caution against a
  measurement failure mode common in AI rollout reporting: treating volume
  metrics (messages sent, tokens consumed) as proxies for value delivered.
  It doesn't propose a replacement metric or methodology — it names the
  trap without providing the fix — which limits how directly actionable
  this claim is on its own; it functions better as a warning to pair with
  other sources' concrete measurement frameworks.

### Claim 7: Adoption at Slack spread organically after one PM documented his agent workflow in a canvas that other PMs copied and adapted, rather than through a top-down mandate
- **Evidence**: Concrete anecdote naming the specific artifact (a Slack
  canvas) and the propagation mechanism (copying/adapting by peers).
- **Confidence**: anecdotal (single named example of one PM's workflow
  spreading; no data on how many people adopted it or measured impact)
- **Quote**: "One PM got the developer experience lead to help him get set
  up, then he wrote up a canvas showing what he did and how he did it.
  Other PMs copied the format."
- **Quote** (general principle): "The fastest way to learn a new way of
  working is to watch a teammate do it."
- **Our assessment**: This is a concrete instance of "show, don't mandate"
  adoption — a specific artifact type (a short "what I did and how" canvas)
  that turned one person's ad hoc setup into a reusable team template. It
  complements Claim 5's "felt not mandated" point with a mechanism: peer
  documentation is the actual vehicle by which felt value spreads, rather
  than staying locked in one person's workflow.

### Claim 8: Slack maintains a company-wide public channel, "How I Slackbot," with thousands of members, where practices from one function (e.g. sales) get picked up and adapted by a different function (e.g. engineering)
- **Evidence**: Named channel with a specific (if uncounted) scale claim
  ("thousands of members," "by her count").
- **Confidence**: anecdotal (self-reported membership count, no
  independent verification, and no measure of how often cross-functional
  transfer actually happens)
- **Quote**: "a company-wide channel called _How I Slackbot_, which by her
  count has thousands of members. In that channel, which is public by
  default, a trick from a sales process can end up reshaping an
  engineering process."
- **Our assessment**: This is the clearest concrete artifact for
  cross-functional knowledge transfer in the source — a single named,
  public, opt-in channel functioning as a company-wide pattern library for
  agent workflows. It is the scaled-up version of the one-PM canvas in
  Claim 7: the canvas is the unit of documentation, the channel is the
  distribution mechanism. Worth flagging for a guide adoption-playbook
  section as a copyable structural pattern (a standing public "how I use
  the agent" channel), independent of whether Slack's specific membership
  figure is verifiable.

### Claim 9: Human-agent teams require reimagining workflows for collaboration, not simply using agents to accelerate existing processes
- **Evidence**: Direct quote framing the distinction explicitly as a
  closing/synthesizing point.
- **Confidence**: emerging (framing claim, consistent with the rest of the
  source's examples, but stated as assertion rather than demonstrated with
  a before/after case)
- **Quote**: "We're going to have to figure out how to change the ways
  that we're working, not just do more of the same kind of work faster."
- **Our assessment**: This is the source's thesis statement, and it is
  consistent with — but adds no new mechanism beyond — the handoff-cycle
  (Claim 3) and role-clarity (Claim 5) claims already extracted. It is
  useful primarily as a framing device for a guide section, similar to how
  `blog-anthropic-human-agent-teams.md` Claim 11 ("agents just make it even
  more important not to skip [good team practices]") functions as that
  note's closing frame.

## Concrete Artifacts

```
Slack CPO Jaime DeLanghe's Monday "handoff cycle" briefing bundle
Source: claude.com/blog, "Turning conversation into knowledge:
how Slack builds human-agent teams," Aug 19, 2026

Agent-produced, waiting for human review each Monday morning:
  - A recap of the previous week's product workshops, with flagged
    escalations
  - A report on AI developments across the web
  - Briefings for the day's meetings
  - A stale bio, handed to an agent to rewrite

Handoff cycle definition (verbatim):
"The core rhythm of a human-agent team is a cycle of handoffs.
Powered by Claude in Slack, agents handle the production
work—drafting, summarizing, monitoring, preparing—and pass the
results to a person. The person reviews, decides, and redirects,
then hands the work back for agents to carry out the next step."
```

```
Peer-driven adoption artifact: the "what I did and how" canvas
Source: same article

Mechanism: One PM got help from the developer experience lead to
set up an agent workflow, then wrote a Slack canvas documenting
what he did and how. Other PMs copied the format.

Distribution channel: company-wide public channel "How I Slackbot"
(thousands of members per DeLanghe's count) — cross-functional
transfer of agent workflow tricks (e.g. sales → engineering).
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-human-agent-teams.md` (Claim 3): Both sources make the
    identical technical claim — agents can only build context from written,
    visible text — as the reason for public-by-default channels. This
    source states it as a practitioner quote ("You're building a shared
    understanding..."; "A private channel is a blind spot for every agent
    that reports on it"); the other states it as prescriptive Anthropic
    guidance ("if it's not written down and accessible, it doesn't exist").
    Independent framing (practitioner account vs. first-party prescriptive
    post), same underlying mechanism.
  - `blog-simonwillison-tobias-lutke-lehrwerkstatt.md` (Claim 2): Shopify's
    River agent enforces public channels and refuses DMs specifically to
    keep all agent conversation searchable. Slack's "public by default, go
    private on purpose" norm (Claim 2 here) is the same practice observed
    at a second, independent company — this strengthens the case that
    "public channels for agent visibility" is an emerging cross-company
    pattern rather than one company's idiosyncratic choice.
  - `blog-anthropic-human-agent-teams.md` (Claim 8, "Doer-Verifier"): The
    handoff cycle here (Claim 3) — agent produces, human reviews/decides,
    agent executes next step — is structurally the same human-in-the-loop
    review shape as Doer-Verifier, but framed as a continuous cycle rather
    than a single verification step.
  - `blog-anthropic-human-agent-teams.md` (Claim 5, role rosters / "fleets
    of personal AIs"): The "agents as coworkers" / role-clarity claim here
    (Claim 5) corroborates the need for defined agent roles named in that
    note, from an independent company's practitioner perspective rather
    than first-party Anthropic guidance.

- **Contradicts**: None filed. No claim here materially opposes an existing
  source note; the overlap with `blog-anthropic-human-agent-teams.md` is
  corroborating (same mechanisms, independent voices), not conflicting.

- **Extends**:
  - `blog-anthropic-human-agent-teams.md` — that post gives first-party
    Anthropic *prescriptive* guidance (four lessons, a five-question
    self-assessment); this source gives a single practitioner's *lived*
    account of the same territory, adding concrete artifacts the other post
    lacks: a specific daily-briefing content bundle (Claim 4), a named
    peer-adoption artifact and channel (Claims 7-8), and an explicit
    warning against activity-based measurement (Claim 6) that the other
    post does not address at all.
  - `blog-simonwillison-tobias-lutke-lehrwerkstatt.md` — extends the public-
    channel-for-agent-visibility pattern from a single-agent (River) case
    study to a company-wide, multi-agent norm at a second company.

- **Novel**:
  - **"Mandated vs. felt" value as an adoption-psychology distinction**: No
    prior corpus source frames agent adoption failure in terms of whether
    users *feel* the value versus having it imposed. This is a new lens for
    diagnosing stalled adoption (Claim 5).
  - **Activity-vs-outcome measurement warning**: The specific "token usage
    tells you the lights are on... not sufficient" / "activity tells you
    adoption is happening, not that it's working" framing is new to the
    corpus — a named measurement anti-pattern without a prior citation.
  - **The "How I Slackbot" channel as a scaled peer-documentation
    mechanism**: A standing, company-wide, public channel purpose-built for
    people to document and share their agent workflows is a concrete,
    copyable organizational artifact not previously named in the corpus
    (the closest prior artifact, the team roster in
    `blog-anthropic-human-agent-teams.md`, documents *roles*, not
    *how-to workflows*).
  - **Handoff cycle as a named, repeating rhythm** (vs. a one-time
    verification step): framing human-agent collaboration as a continuous
    loop of handoffs, rather than a single generate-then-check pass, is a
    distinct framing from the corpus's existing Doer-Verifier / generator-
    verifier language.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the concrete "daily briefing bundle"
  (Claim 4 / Concrete Artifacts) as a worked example of a standing agent
  workflow: a single agent (or agent set) that aggregates several distinct
  content types (metrics recap, escalations, external news, meeting prep,
  routine rewrites) into one artifact for a single daily human review pass.
  This is more concrete than the existing "work in public" guidance in
  `blog-anthropic-human-agent-teams.md` and can serve as a template readers
  can copy directly.

- **Chapter 05 (Team Adoption)**: Add two specific, actionable adoption
  mechanisms currently missing from the guide's team-adoption material:
  (1) the "what I did and how" canvas as the minimum-viable artifact for
  turning one person's ad hoc agent setup into a team template (Claim 7),
  and (2) a standing company-wide public channel purpose-built for sharing
  these artifacts across functions (Claim 8, "How I Slackbot"). Pair with
  the "mandated vs. felt" distinction (Claim 5) as the rationale for why
  peer-demonstration adoption outperforms mandated rollout — this gives the
  chapter's adoption-strategy section a concrete "why" alongside the "what."

- **Chapter 05 (Team Adoption — Measurement)**: Add the activity-vs-outcome
  measurement warning (Claim 6) as a named anti-pattern: token usage and
  message volume prove adoption is happening, not that it is delivering
  value. Currently the guide's adoption material (per the existing
  `blog-anthropic-human-agent-teams.md` note) does not address measurement
  pitfalls at all — this is a genuinely new addition, though it is a
  warning without a prescribed alternative metric, so it should be paired
  with a source that does propose one if such a source exists in the
  corpus.

## Extraction Notes

- WebFetch declined to reproduce the article verbatim in full (standard
  copyright-safe summarization behavior) on the first pass. All quotes in
  this note were obtained through five separate targeted WebFetch calls,
  each asking for verbatim text on a specific sub-topic; the returned
  quotes were consistent in wording across calls where topics overlapped
  (e.g. the handoff-cycle definition was returned identically twice). No
  sub-pages were linked from the article to follow.
- The article gives no quantified adoption metrics beyond the unverified
  "thousands of members" figure for the "How I Slackbot" channel — this
  limits how strongly the adoption claims (7, 8) can be weighted; they are
  marked anecdotal accordingly.
- Confidence is set to `anecdotal` overall: every claim in this source rests
  on a single executive's first-person account of practices inside one
  company, with no independent metrics, audit, or multi-company validation
  within the source itself. Individual claims are marked `emerging` where
  the underlying mechanism (e.g., agents cannot see private channels) is
  independently well-established elsewhere in the corpus, and `anecdotal`
  where the claim is a specific unverified example (the daily briefing
  routine, the PM canvas, the channel membership count).
