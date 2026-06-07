---
source_url: https://lucumr.pocoo.org/2026/6/6/communities-of-not/
source_type: blog-post
title: "Communities of Not"
author: Armin Ronacher
date_published: 2026-06-06
date_extracted: 2026-06-07
last_checked: 2026-06-07
status: current
confidence_overall: anecdotal
issue: "#1099"
---

# Communities of Not

> Armin Ronacher argues that LLM-skeptical developer communities develop an
> "identity from opposition" that turns legitimate critique into tribal mob
> behavior against developers who change their positions — and offers a
> de-escalation framing for individuals navigating that pressure.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~400 words; five
  paragraphs plus one substantive footnote; opinion/philosophical reflection;
  published 2026-06-06)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent. His blog is a
  designated `trusted-feed` source in this repo. This post is personal
  reflection with self-confession ("I have done versions of this myself in the
  past") — not a practitioner analysis of technical patterns. Claims carry
  anecdotal confidence throughout; the post is direct observation and normative
  argument, grounded in one named concrete incident (rsync mob, footnote) and
  analogy to similar dynamics in other communities. Ronacher occupies an
  unusual position in AI-skeptic discourse: a long-time OSS practitioner who
  uses AI tools daily (Earendil, Pi) while critically analyzing their social
  consequences (see his earlier posts on content flooding, terminology, and
  local models).
- **Scope**: Covers the sociological pattern of opposition-based community
  identity, the specific form this takes in LLM-skeptical developer spaces,
  mob behavior against individuals who change positions, the inevitability of
  LLM exposure in modern developer environments, and a de-escalation
  prescription for individuals. Does NOT cover: specific technical critiques of
  LLMs, organizational or management strategies for AI rollout, or quantitative
  evidence of any kind. The post is short and prescriptive rather than
  analytical.

## Extracted Claims

### Claim 1: LLM-skeptical developer communities develop "identity from opposition" — the thing being rejected (LLMs) gradually becomes the primary subject of the community's identity, displacing the legitimate underlying concerns

- **Evidence**: Ronacher's cross-community observation: childfree spaces
  (autonomy/choice → identity around not having children), anti-car spaces
  (safer streets/transit → identity around not driving), LLM-skeptical spaces
  (labor, code quality, slop → identity around not using LLMs). The underlying
  legitimate concerns named for LLM-skeptics — "the future of labor, code
  quality and slop" — are real; the claim is about what happens to those
  concerns over time within the community.
- **Confidence**: anecdotal
- **Quote**: "There is a strange thing that happens in communities that gather
  around abstinence from something: identity from opposition. At their best
  these communities are not *just* negative: childfree spaces can be about
  autonomy, choice and acceptance, anti-car spaces about safer streets and
  transit, and LLM-skeptical developer spaces about the future of labor, code
  quality and slop. But the thing being refused often does not go away and
  instead becomes the main subject of the community's identity."
- **Our assessment**: The pattern Ronacher identifies has a specific
  implication for AI-native engineering teams and those leading adoption: the
  substantive concerns of LLM-skeptical colleagues (labor, quality, slop) may
  be legitimate entry points for discussion — but if those colleagues are also
  embedded in opposition-identity communities, the actual barrier to engagement
  may be social identity rather than the technical concerns they articulate.
  Understanding the distinction helps team leads calibrate: addressing the
  stated technical concern is necessary but may not be sufficient if group
  identity is the underlying driver.

### Claim 2: When a respected developer publicly tries LLMs after being seen as LLM-skeptical, opposition communities treat it as tribal betrayal and mobilize collective punishment — even though the person never agreed to be a community member

- **Evidence**: Ronacher's direct observation pattern, anchored by the rsync
  maintainer mob incident (named in the footnote as "the LLM version that
  prompted this post" with two linked external references). Parallel examples
  from childfree and anti-car communities confirm the pattern is not unique to
  AI discourse.
- **Confidence**: anecdotal (one named incident; pattern confirmed by analogy)
- **Quote**: "a respected developer tries LLMs, and the community feels
  betrayed because it assumed they were members of the same tribe."
- **Our assessment**: The key insight here is "assumed they were members of the
  same tribe" — the target never opted into tribal membership. This is the
  mechanism that makes the resulting punishment feel disproportionate to the
  observer: the community is enforcing norms against someone who never accepted
  them. For teams rolling out AI tools: when a visible skeptic publicly tries an
  AI tool, they should be prepared for this pattern from within their network —
  and team culture should explicitly not reinforce tribal expulsion dynamics by
  treating adoption as personal endorsement of any political or social position.

### Claim 3: The "punishment" communities unleash for position-changing is concrete and coordinated — pile-ons, quote mining, and retroactive character attacks — even though the "expulsion" itself is imaginary

- **Evidence**: Ronacher's direct description of the mechanics; consistent with
  the rsync incident referenced in the footnote.
- **Confidence**: anecdotal
- **Quote**: "The expulsion of that person (who never signed up to be a
  community member) is entirely imaginary but the punishment that the community
  unleashes is not: people pile on and shame them, quote them out of context and
  turn their weakest moments into proof that the person was always unserious, a
  sharlatan or should not be listened to."
- **Our assessment**: The specific mechanics are worth noting for team adoption
  guidance: quote mining and "turning weakest moments into proof" are
  information-warfare patterns that produce real reputational harm. A developer
  who publicly shares nuanced observations about AI tools (what works, what
  doesn't) is providing exactly the kind of content that quote mining can weaponize
  into a "proof" of either uncritical enthusiasm or hypocritical adoption. This
  has a chilling effect: practitioners with the most grounded experience may stay
  quiet rather than risk becoming targets. See also Ronacher's April 2026 post
  "The Center Has a Bias" (not yet mined) which explores why the most credible
  critics of AI tools are also often adopters — and why they are easily
  mischaracterized.

### Claim 4: LLMs appear in developer work environments (editors, issue trackers, hiring, management pressure, code reviews) whether individual developers opted in or not — making complete abstinence practically impractical

- **Evidence**: Ronacher's observation of the current state of developer
  tooling and organizational dynamics. This is an assertion of fact about the
  2026 development environment, not a prescription.
- **Confidence**: emerging (the claim is increasingly observable; no quantitative
  data cited, but consistent with broader corpus evidence of AI tool penetration
  in developer environments)
- **Quote**: "For us developers, LLMs show up in editors, issue trackers, hiring
  conversations, management pressure and code reviews whether we asked for them
  or not."
- **Our assessment**: This claim does significant work in Ronacher's argument:
  it decouples "using LLMs" from "choosing to use LLMs," and thereby establishes
  that LLM-skeptical identity is partly a response to a perceived imposition, not
  purely a free choice. For AI-native engineering teams: the framing "whether we
  asked for them or not" describes how many engineers experience AI tool rollout —
  as something happening to them rather than something they selected. This
  perception gap (adoption leaders seeing voluntary uptake; resisters experiencing
  imposition) is a concrete team dynamics problem, separate from the technical
  merits of any particular tool.

### Claim 5: Legitimate resistance to LLM adoption exists, but it does not justify using that rejection as a basis for mob behavior against others

- **Evidence**: Ronacher's explicit normative argument; self-positioned as
  coming from someone who has done "versions of this" himself and understands
  the impulse.
- **Confidence**: anecdotal
- **Quote**: "Resisting that can be legitimate but that is no excuse for using
  one's rejection to justify shitty mob behavior."
- **Our assessment**: The explicit acknowledgment that "resisting that can be
  legitimate" is significant — Ronacher is not dismissing LLM criticism as
  irrational, which would undermine the broader argument. He is disaggregating
  substantive critique from tribal enforcement behavior. For teams navigating
  adoption: this framing provides a principled response to the common charge that
  "you just want to silence critics." The line is not between critics and
  non-critics, but between substantive critique and collective shaming of
  individuals. Teams can explicitly honor the first while not tolerating the
  second.

### Claim 6: Shared-insecurity communities are psychologically comforting but create a pathway from personal skepticism to collective harassment that is easy to slide into without noticing

- **Evidence**: Ronacher's personal confession that he has "done versions of
  this myself in the past" and required deliberate work to become "more
  accepting of other people's worldviews." The mechanism is self-reinforcing:
  the comfort of shared negativity makes the transition to harassment feel
  natural.
- **Confidence**: anecdotal
- **Quote**: "Whatever insecurities we have, finding a group of others sharing
  them can be comforting. The danger is that being part of a crowd of negativity
  can easily make us part of collective harassment."
- **Our assessment**: The personal confession gives this claim unusual weight —
  Ronacher is not describing other people's bad behavior but his own past
  susceptibility. The mechanism named is specific: insecurity → shared community
  → crowd negativity → collective harassment, with each step feeling like a
  natural extension of the last. For engineering teams: this suggests that
  opposition dynamics do not require bad actors — they emerge from ordinary human
  psychology around belonging and validation. Team culture guidance that addresses
  these dynamics needs to account for how natural it feels from the inside.

### Claim 7: The recommended individual response to tribal pressure and mob dynamics in LLM-skeptical spaces is to breathe, slow down, de-escalate, and default to openness rather than assuming catastrophic interpretations

- **Evidence**: Ronacher's normative prescription, framed as personal
  encouragement rather than policy. Links to his April 2026 post "The Center
  Has a Bias" for context on what "open to new things" means practically
  (requiring genuine engagement rather than performative neutrality). The
  prescription is addressed at individuals observing or participating in these
  dynamics, not at organizational decision-makers.
- **Confidence**: anecdotal
- **Quote**: "I can only encourage you to breathe, slow down, de-escalate when
  given the chance, and resist the temptation to always assume the most
  catastrophic reading. Default to being open to new things. Being negative
  towards something, and making that ones identity, is an easy trap to fall
  into."
- **Our assessment**: The prescription is deliberately individual-scale and
  modest — Ronacher says "I can only encourage you," not "here is the policy."
  The "most catastrophic reading" framing is specific: it addresses the
  interpretive escalation mechanism where ambiguous actions (a colleague trying
  an AI tool) get read through the most hostile possible lens ("proof they were
  always a fraud"). For teams: this is a plausible microculture intervention —
  explicitly naming the "default to catastrophic reading" pattern and modeling
  de-escalation from leadership can interrupt the pile-on dynamic before it
  starts.

## Concrete Artifacts

### The rsync mob incident — the triggering LLM-specific event (from footnote)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/6/communities-of-not/
        (footnote [1] to "LLM-skeptical developer spaces about the future of
        labor, code quality and slop")

Footnote text (verbatim):
  "These examples are not meant as equivalents. The recent
  mob [against rsync] is the LLM version that prompted this post.
  I picked the others because I'm familiar with those communities
  and they all show similar cases of personal choices being
  interpreted as betrayal."

Linked external references in footnote:
  - https://github.com/RsyncProject/rsync/issues/929
  - https://mastodon.gamedev.place/@JeremiahFieldhaven/116654345332213390

Context: Ronacher describes this as the concrete incident that prompted
         the post — a mob targeting the rsync project in the context of
         LLM use.
```

### The "opposition identity" pattern across analogous communities

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/6/communities-of-not/

Three parallel community patterns cited:
  Childfree spaces:
    Original positive aim:   "autonomy, choice and acceptance"
    Opposition drift target: not having children → policing those who become parents

  Anti-car spaces:
    Original positive aim:   "safer streets and transit"
    Opposition drift target: not driving → policing those who buy cars

  LLM-skeptical developer spaces:
    Original positive aim:   "the future of labor, code quality and slop"
    Opposition drift target: not using LLMs → policing developers who try them

Author's note: "These examples are not meant as equivalents" — the
               communities and underlying issues differ in moral weight;
               the structural pattern is what is shared.
```

### The de-escalation prescription (verbatim)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/6/communities-of-not/

Individual prescription (final paragraph, verbatim):
  "I can only encourage you to breathe, slow down, de-escalate when given
  the chance, and resist the temptation to always assume the most
  catastrophic reading. Default to being open to new things. Being negative
  towards something, and making that ones identity, is an easy trap to fall
  into."

Linked context: "open to new things" links to Ronacher's April 2026 post
  "The Center Has a Bias" (https://lucumr.pocoo.org/2026/4/11/the-center-has-a-bias/)
  which argues that genuinely informed criticism of AI tools requires direct
  engagement with them, not just secondhand accounts.
```

## Cross-References

- **Corroborates**: `blog-ronacher-clanker-terminology.md` Claim 11 — "The
  goal is not a specific word but a clear boundary — humans on one side with
  responsibility, machines on the other as tools — and this position is
  explicitly not anti-AI." Quote: "Whatever word we use, I want it to preserve
  a clear division: humans on one side with responsibility, machines on the
  other as a boring tool." Both posts establish Ronacher's position as nuanced:
  he embraces AI utility while rejecting both anthropomorphization (clanker
  post) and opposition-identity tribalism (this post). The current post is the
  social/community-dynamics counterpart to the clanker post's
  responsibility/language argument.

- **Extends**: `blog-ronacher-clanker-terminology.md` Claim 8 — "Real harms
  from AI to actual humans — copied works, data labelers, data center neighbors,
  buried OSS maintainers, people with AI psychosis — deserve the moral
  attention." Quote from that note: "Open Source maintainers buried under
  generated slop." The rsync mob incident in the current post's footnote is
  a concrete instance of exactly this harm category: OSS maintainers facing
  organized social pressure in the context of AI-generated content dynamics. The
  clanker note names OSS maintainers as a human harm category; this post
  provides a named incident.

- **Extends**: `blog-ronacher-content-for-contents-sake.md` Claim 6 —
  "The inability to distinguish human from LLM-generated text erodes trust in
  people you know, not just strangers." Quote from that note: "The moment I
  start distrusting people I otherwise trust, because they have started picking
  up LLM phrasing, it erodes trust all over society." That post addresses trust
  erosion at the interpersonal/team level (distrust of colleagues who use LLM
  phrasing). The current post extends the same trust-erosion dynamic to the
  community level: the mechanism changes from "I distrust your text" to "I
  distrust your identity," but both reflect the same breakdown in social trust
  around AI adoption. Together they describe a layered picture: trust erodes
  first at the text level (content-for-contents-sake), then at the tribal
  identity level (communities-of-not).

- **Extends**: `blog-ronacher-pi-oss.md` — The pi-oss post documents
  AI-generated "slop issues" misdirecting OSS maintainers and AI volume pressure
  fragmenting OSS collaboration. The current post's rsync incident (footnote) is
  a social-pressure complement to those technical pressures: OSS projects face
  both AI-generated issue volume (pi-oss) and organized community mob pressure
  (communities-of-not). Both posts document forms of harm from AI dynamics to
  OSS infrastructure that predate the current post.

- **Contradicts**: None identified. No existing corpus source makes claims
  that would lead to directly opposing guide advice about opposition-community
  dynamics or LLM-skeptical tribal behavior. No contradiction issue filed.

- **Novel**:
  - **Sociological analysis of "communities of not" pattern applied to
    LLM-skeptical developer spaces**: No other corpus source identifies or names
    the opposition-identity mechanism as a distinct sociological pattern
    affecting AI adoption dynamics. Existing corpus notes address adoption
    resistance as tactical/practical (code quality, security, economics) but not
    as tribal identity enforcement.
  - **De-escalation framing for individual developers navigating tribal
    pressure**: No other corpus source offers de-escalation guidance for
    individual practitioners facing community hostility over their AI tool use.
    The prescription is modest but named.
  - **"Identity from opposition" as distinct from substantive critique**:
    The explicit disaggregation — "resisting that can be legitimate" but
    opposition identity is a different and more dangerous thing — is not present
    in any other corpus source. This framing allows teams to honor legitimate
    critique while not enabling tribal enforcement dynamics.
  - **Imposition framing of AI tool exposure**: The claim that LLMs "show up in
    editors, issue trackers, hiring conversations, management pressure and code
    reviews whether we asked for them or not" names the developer perception of
    AI adoption as unwilled imposition. This framing is not found in any other
    corpus source; other sources describe adoption from the perspective of teams
    choosing to adopt, not individuals experiencing it as something imposed on them.

## Guide Impact

- **Chapter 05 (Team Adoption — Understanding Resistance)**: This is the
  primary contribution. Current chapter coverage (inferred) likely treats
  adoption resistance as primarily technical skepticism or legitimate concern.
  Claim 1 and Claim 2 add a distinct and harder-to-address category: social
  identity resistance, where the barrier is tribal belonging rather than
  technical objection. Teams should be advised to distinguish between (a) a
  colleague who has substantive concerns about code quality or labor effects,
  and (b) a colleague whose skepticism is also a community identity marker —
  they require different engagement approaches. The Claim 5 framing ("resisting
  that can be legitimate") provides language for honoring the first without
  capitulating to mob dynamics from the second.

- **Chapter 05 (Team Adoption — Change Management Microculture)**: Claim 7
  (de-escalation prescription) and Claim 6 (psychological pathway to collective
  harassment) together suggest a concrete team culture intervention: explicitly
  name the "default to catastrophic reading" pattern, model de-escalation from
  leadership, and not treating a colleague's decision to try an AI tool as a
  political act requiring comment. This is below the level of formal policy and
  operates at team-norm level.

- **Chapter 04 (Organizations — Adoption Dynamics)**: Claim 4 (LLMs show up
  whether developers opted in or not) is a structural observation relevant to
  organizational adoption strategy. If engineers experience AI tool integration
  as imposition rather than choice, adoption resistance becomes a grievance
  dynamic rather than a technical evaluation dynamic. Organizational adoption
  strategy should include explicit acknowledgment of this perception and create
  genuine opt-in paths where possible — not because opt-in is always feasible
  but because the perception of imposition amplifies opposition-identity
  formation (Claim 1).

- **Chapter 01 (Daily Workflows — Environmental Context)**: The Claim 4
  enumeration of where LLMs now appear (editors, issue trackers, hiring,
  management pressure, code reviews) is useful as a concise statement of the
  current development environment. A section describing what AI-native
  engineering means in 2026 could anchor on this observation: AI tools are no
  longer a deliberate add-on but an environmental baseline that practitioners
  navigate whether they chose to or not.

## Extraction Notes

- Full markdown source fetched directly from
  `https://lucumr.pocoo.org/2026/6/6/communities-of-not.md`. All quotes
  verified character-for-character against the markdown source.
- The post is very short (~400 words, five paragraphs) with one substantive
  footnote. The footnote names the rsync incident as the direct trigger and
  provides two external links (GitHub issue #929 on RsyncProject/rsync; a
  Mastodon post). The external links were not fetched; the claim is attributed
  to the footnote text itself.
- The final paragraph links to Ronacher's April 2026 post "The Center Has a
  Bias" (https://lucumr.pocoo.org/2026/4/11/the-center-has-a-bias/) for the
  phrase "open to new things." That post was fetched and found to be substantive
  (develops the argument that informed criticism of AI tools requires direct
  engagement; explores why people with the most grounded views appear as
  adopters). It has no existing source note in this repo and would warrant
  independent mining.
- Confidence rated anecdotal overall: the post is pure opinion and personal
  reflection, with one named incident (rsync) as the only external anchor. The
  cross-community pattern argument (childfree, anti-car, LLM-skeptic) provides
  structural support but is itself observational. No quantitative data, studies,
  or independent verification.
- The Prospector's triage identifies the first comment as medium-novelty,
  the second and third as high-novelty. All three identify Ch04/Ch05 (team
  adoption, organizational dynamics) as primary targets. The extraction covers
  all three angles: the sociological pattern (Claim 1), mob mechanics
  (Claims 2-3), adoption environment (Claim 4), ethical framing (Claim 5),
  psychological pathway (Claim 6), and individual prescription (Claim 7).
