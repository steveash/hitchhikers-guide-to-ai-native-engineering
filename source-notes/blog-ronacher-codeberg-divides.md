---
source_url: https://lucumr.pocoo.org/2026/7/24/codeberg-divides/
source_type: blog-post
title: "Codeberg Divides"
author: Armin Ronacher
date_published: 2026-07-24
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: anecdotal
issue: "#2215"
---

# Codeberg Divides

> Armin Ronacher critiques Codeberg's new terms-of-use rule excluding projects
> "mostly" written by generative AI as democratically legitimate but
> operationally unenforceable, arguing that a platform hosting Open Source
> infrastructure needs predictability and neutrality more than it needs
> democratic process, and that the ambiguous middle-ground policy risks
> fracturing the Open Source community rather than helping it engage with an
> AI-assisted future.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~600 words; eight
  paragraphs; practitioner/political commentary on a specific platform policy
  change; published 2026-07-24)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent. His blog is a
  designated `trusted-feed` source in this repo. He writes as a long-time
  Open Source maintainer who wants GitHub to face real competition (he links
  to his own April 2026 post making that case) and who has previously written
  about corporate access restrictions (`blog-ronacher-gaslighting-openness.md`)
  and community fracture over AI (`blog-ronacher-communities-of-not.md`). He
  discloses no direct affiliation with Codeberg; this is outside-practitioner
  commentary on a competitor-to-GitHub platform he wants to succeed. Claims
  are anecdotal/normative — no metrics, surveys, or enforcement data are
  cited, only Ronacher's reading of the policy text and his own inability to
  self-assess authorship percentages on his projects.
- **Scope**: Covers Codeberg's new Terms of Use clause excluding "mostly"
  AI-generated projects, the tension between democratic legitimacy and good
  policy outcomes, enforcement ambiguity of the word "mostly," a proposed
  alternative (either full LLM prohibition or narrowly targeting spam/abuse),
  the Open Source/Free Software community's fracture over LLMs and agents, and
  Codeberg's strategic choice between a smaller ideologically-bounded
  community and a broad European GitHub alternative. Does NOT cover: technical
  detection methods for AI-generated code, Codeberg's internal deliberation
  process, other platforms' AI policies, or quantitative data on how many
  projects the policy affects.

## Extracted Claims

### Claim 1: Codeberg's exclusion of AI-heavy projects is procedurally legitimate (a democratic association decision) but democratic process does not guarantee a good or inclusive outcome for people already depending on the platform

- **Evidence**: Ronacher's direct characterization of Codeberg's governance
  structure (member association with a democratic process) set against the
  outcome for existing users and projects.
- **Confidence**: anecdotal
- **Quote**: "Codeberg is entirely within its rights to do this. It is an
  association with members and a democratic process, and that process
  produced a result. But democracy is a way of making a decision, not a
  guarantee that the decision is inclusive, wise, or even good for the people
  already depending on it. A majority can still decide that certain projects
  and people no longer belong."
- **Our assessment**: This is the post's framing move: separating procedural
  legitimacy (the vote happened correctly) from substantive quality (the
  result may still harm dependents). It is a useful distinction for any team
  evaluating a platform or vendor's governance model — a "democratic" process
  does not by itself de-risk a policy change for people who already built on
  the platform. This is a general point about infrastructure governance, not
  specific to AI.

### Claim 2: Infrastructure needs predictability and neutrality toward legal Open Source software more than it needs democratic governance — a democratic provider without a clear constitution can be worse at that than a corporation

- **Evidence**: Ronacher's explicit comparison between GitHub (non-democratic,
  disliked in some respects) and Codeberg (democratic), arguing the axis that
  matters for infrastructure dependents is not governance style but
  predictability.
- **Confidence**: anecdotal
- **Quote**: "GitHub's governance has never been democratic and there is
  plenty about the platform that I dislike. Yet democracy is not the main
  property I need from infrastructure. I need it to be predictable,
  dependable, and reasonably neutral towards the legal Open Source software
  hosted on it. A democratic provider without a clear constitution can be
  worse at those things than a corporation."
- **Our assessment**: This is the core normative claim of the post and the
  one most directly named by the Prospector's triage question. It reframes
  "which governance model is better" as the wrong question for infrastructure
  dependents; the right question is "which model produces predictable,
  neutral treatment of legally-compliant content." For teams evaluating
  hosting platforms (not just GitHub alternatives, but any shared
  infrastructure with a governance layer — package registries, CI providers,
  forges), this suggests weighting policy stability and content-neutrality
  commitments alongside or above governance structure.

### Claim 3: The policy's "mostly" threshold for AI-generated code is unenforceable in practice because authorship percentage cannot be reliably assigned in an actively developed codebase — even by the codebase's own maintainer

- **Evidence**: Ronacher's self-report: he could not reliably assign
  authorship percentages to his own recent projects. This is first-person
  testimony from someone with direct visibility into his own commit history
  and AI tool usage.
- **Confidence**: anecdotal (single practitioner's self-assessment, but
  directly falsifiable — if the creator of the policy's target behavior
  cannot self-classify, the ambiguity claim is strongly supported)
- **Quote**: "The actual wording makes this more difficult. The terms
  prohibit projects that mostly consist of code written by generative AI
  tools. In an actively developed codebase, what does 'mostly' mean, and who
  can still tell? I could not reliably assign authorship percentages to many
  of my own recent projects."
- **Our assessment**: This is the most concrete and falsifiable claim in the
  post. A policy threshold that its most sympathetic, most technically
  literate potential subject cannot self-apply is a strong signal of
  enforcement failure — the burden shifts entirely to moderators making
  after-the-fact judgment calls with no reliable measurement method. This is
  directly relevant to any team or project writing AI-usage policy language
  ("substantially AI-generated," "primarily AI-assisted," etc.): if the
  policy's own target audience cannot self-classify against the threshold, the
  policy is not enforceable as written and will be enforced unevenly or by
  proxy (social reputation, style suspicion) instead.

### Claim 4: Ambiguous, hard-to-classify positions near a policy's threshold ("the center") will be treated worse than clearer positions on either side, because the center is structurally underrepresented in judgment about it

- **Evidence**: Ronacher's cross-reference to his own earlier post ("The
  Center Has a Bias," linked in-line) applied to the specific enforcement
  dynamic of the "mostly" threshold.
- **Confidence**: anecdotal
- **Quote**: "The line is open to interpretation precisely where it needs to
  be enforceable. In practice the center will probably lose out, as it has a
  bias."
- **Our assessment**: This connects the Codeberg policy critique to a broader
  Ronacher argument (from "The Center Has a Bias," not separately mined here)
  that people with moderate, mixed AI usage are judged more harshly or more
  suspiciously than either committed non-users or open enthusiasts, because
  the observers forming judgment are themselves selected from people willing
  to engage deeply with the tools. Applied here: a project with moderate,
  genuinely mixed human/AI authorship is the hardest case for moderators to
  classify fairly, and is the case most likely to be treated unfavorably
  under social pressure even when technically compliant.

### Claim 5: A harsher, unambiguous line — either prohibiting all LLM involvement, or narrowly targeting autonomous repository spam and abusive resource consumption — would be preferable to the current vague middle ground

- **Evidence**: Ronacher's direct policy alternative, proposed as a binary
  choice between two enforceable extremes rather than the current
  percentage-based rule.
- **Confidence**: anecdotal
- **Quote**: "A harsher line would probably be preferable. If Codeberg wants
  no LLM involvement, it should say so. If it wants to prevent autonomous
  repository spam and abusive resource consumption, it should write rules for
  those instead."
- **Our assessment**: This is a concrete, actionable policy-design principle
  for any organization writing an AI-usage rule: pick an axis that is
  mechanically checkable (was any LLM used at all — checkable via a
  disclosure requirement; is this an autonomous bot generating high-volume,
  low-quality submissions — checkable via volume/behavior signals) rather
  than a threshold requiring proportion-of-authorship estimation, which
  cannot be checked by anyone, including the author. This generalizes past
  Codeberg to any team or platform drafting contribution or acceptable-use
  policies that reference AI involvement.

### Claim 6: The current middle-ground policy delegates enforcement to moderators and community norms, and Ronacher expects the community's informal social boundary to be harsher than the letter of the rule

- **Evidence**: Ronacher's prediction about downstream enforcement behavior,
  stated as an assumption rather than an observed fact.
- **Confidence**: anecdotal (explicitly framed as his own assumption, not a
  reported observation)
- **Quote**: "The current middle ground delegates too much of the policy to
  moderators and community norms. I'm currently assuming the community around
  it draws a much harsher social boundary, making projects and maintainers
  unwelcome even when they technically comply."
- **Our assessment**: This is a specific enforcement-gap prediction: technical
  compliance with a vague written rule does not protect a maintainer from
  informal social exclusion if the surrounding community's actual norm is
  stricter than the codified policy. For teams thinking about how their own
  internal AI-usage guidelines will actually be enforced, this is a caution
  that the written policy and the lived social norm can diverge, and the gap
  falls hardest on people operating near the ambiguous threshold (Claim 4).

### Claim 7: The Open Source and Free Software communities are fracturing deeply over LLMs and agents despite real, legitimate underlying concerns (copyright, labor, energy use, slop, maintainer burden), and this division is a missed opportunity rather than a resolution

- **Evidence**: Ronacher's direct assessment of the state of OSS/FLOSS
  discourse, naming the legitimate concerns explicitly before criticizing the
  response to them.
- **Confidence**: anecdotal
- **Quote**: "It is a real shame that the Open Source and Free Software
  communities are splitting this deeply over LLMs and agents. There are
  serious questions about copyright, labor, energy use, slop, and maintainers
  drowning in generated contributions. But these tools are also becoming part
  of how software is made. The Open Source world needs to figure out how to
  engage with that future, not just divide into camps."
- **Our assessment**: As with `blog-ronacher-communities-of-not.md`, Ronacher
  explicitly validates the underlying concerns before criticizing the
  community-level response to them — he is not dismissing critics. The
  specific claim here is that fracturing into camps (accept-all-AI vs.
  exclude-all-AI platforms/projects) forecloses the harder, more useful work
  of building norms and tooling for the mixed-authorship reality that already
  exists (Claim 3). For a guide chapter on team or community adoption, this
  names camp-formation itself, not just individual resistance, as a dynamic
  that blocks progress on legitimate concerns.

### Claim 8: LLMs, if built and used well, represent a potential tool for reclaiming control and power away from large corporations and institutions — not just a threat to be excluded

- **Evidence**: Ronacher's normative claim, stated as a corrective to the
  framing implicit in exclusionary AI policies.
- **Confidence**: anecdotal
- **Quote**: "More importantly, LLMs if done and used well, should be welcome
  to all of us. They could be used to reclaim control and power, away from
  large corporations and institutions."
- **Our assessment**: This is a notable pivot: Ronacher's critique of
  Codeberg's policy is not that AI-skepticism is wrong, but that a blanket
  exclusion forecloses a version of AI adoption he considers desirable —
  community-controlled, locally-run, or otherwise not concentrated in large
  vendors' hands. This connects to his open-source/local-model advocacy
  elsewhere in the corpus (see Cross-References) but is stated here without
  elaboration on mechanism; it is an assertion, not a developed argument, in
  this post.

### Claim 9: Codeberg faces a strategic choice between being a smaller community with a stronger political identity and being a broad, dependable European alternative to GitHub — these are different ambitions, and the current policy pursues the former

- **Evidence**: Ronacher's direct framing of Codeberg's strategic options,
  stated in the context of his stated preference (from his linked "before
  GitHub" post) that GitHub face real competition, ideally from an
  association rather than another corporation.
- **Confidence**: anecdotal
- **Quote**: "It can choose to be a smaller community with a stronger
  political identity, but that is a different ambition from being a broad
  and dependable European alternative to GitHub."
- **Our assessment**: This is the post's strategic conclusion, distinct from
  the enforceability critique (Claims 3–6). Even if the policy were perfectly
  enforceable, Ronacher argues it still represents a choice to narrow
  Codeberg's addressable community rather than broaden it — a trade-off
  Codeberg is entitled to make but one with real cost to Ronacher's stated
  goal of competitive pressure on GitHub. For teams evaluating platform
  dependencies, this names a general trade-off: platforms that adopt
  ideologically narrower policies to satisfy their existing community may
  become less viable as neutral, broad-based infrastructure for projects
  outside that community's specific position.

### Claim 10: Ronacher wants Codeberg to be forward-looking enough to host the Open Source software of tomorrow, not only software made in the ways its current community approves of — while explicitly affirming Codeberg's right to choose otherwise

- **Evidence**: Ronacher's closing normative statement, paired with an
  explicit acknowledgment of Codeberg's legitimate authority to decide
  differently.
- **Confidence**: anecdotal
- **Quote**: "I wish Codeberg were more forward-looking here: willing to host
  the Open Source software of tomorrow, not only software made in the ways
  its community approves of today. It has every right to make the choice it
  made, but I just do not think it is a good one."
- **Our assessment**: This closing line is consistent with Claim 1: Ronacher
  never disputes Codeberg's authority to set this policy, only its wisdom.
  The distinction between "software of tomorrow" and "software made in ways
  the community approves of today" is a useful framing for any platform or
  organization writing forward-facing acceptable-use policy around a
  fast-changing practice — a policy anchored to today's community consensus
  about method (how code is produced) rather than to durable, checkable
  properties (licensing, safety, spam behavior) risks obsolescence as the
  practice shifts.

## Concrete Artifacts

### Codeberg's actual Terms of Use clause (fetched directly from Codeberg's repository, not just Ronacher's characterization)

```
Source: Codeberg e.V., TermsOfUse.md, § 2 (1) 7
https://codeberg.org/Codeberg/org/src/branch/main/TermsOfUse.md
(fetched 2026-07-25 via raw file at
 https://codeberg.org/Codeberg/org/raw/branch/main/TermsOfUse.md)

"You must not share projects that mostly consist of code written by
'generative AI'-tools (including services such as Claude, OpenAI Codex).
Such projects having an unclear copyright status (see requirements
§ 2 (1) 1 and § 2 (1) 3) and furthermore have little safeguards to ensure
that they do not include harmful code (c.f. § 2 (1) 5)."

Enforcement clause, § 2 (2):
"Failure to comply with the rules in § 2 (1) leads to immediate removal of
the content together with a warning; further violations might result in
immediate account suspension. In non-obvious cases, decisions about account
suspensions and content removal are made by the presidium, and require a
simple majority."

Note: the clause's stated rationale is copyright-status ambiguity and
insufficient harmful-code safeguards, not a categorical objection to AI
involvement per se — Ronacher's post does not quote or engage with this
stated rationale directly, only the "mostly" threshold and the community
reaction he expects around it.
```

### Ronacher's proposed alternative framing (verbatim, paragraph 5)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/7/24/codeberg-divides/

"A harsher line would probably be preferable. If Codeberg wants no LLM
involvement, it should say so. If it wants to prevent autonomous repository
spam and abusive resource consumption, it should write rules for those
instead. The current middle ground delegates too much of the policy to
moderators and community norms."
```

### Linked context (not independently mined as separate sources)

```
- https://lobste.rs/s/ax914v/protecting_our_floss_commons_from_llms
  (the community discussion thread Ronacher links to as the origin of the
  policy change; not fetched — a discussion thread, not a primary source
  for this note)
- https://lucumr.pocoo.org/2026/4/28/before-github/ (Ronacher's own post,
  linked for "I want GitHub to face competition"; fetched for context —
  documents his motivation for wanting a credible non-corporate GitHub
  alternative to succeed, grounded in concerns about GitHub's role as OSS
  archival infrastructure. Not separately mined; no existing source note
  covers it.)
- https://lucumr.pocoo.org/2026/4/11/the-center-has-a-bias/ (Ronacher's own
  post, linked for the "center has a bias" reference in Claim 4; fetched
  for context — argues that people in the "informed center" of any new-
  technology debate are self-selected toward engagement/experimentation,
  which biases how ambiguous middle positions get judged. Not separately
  mined; no existing source note covers it, though it is referenced as
  linked context in `blog-ronacher-communities-of-not.md`'s Extraction Notes.)
```

## Cross-References

- **Extends**: `blog-ronacher-communities-of-not.md` Claim 1 — "There is a
  strange thing that happens in communities that gather around abstinence
  from something: identity from opposition... LLM-skeptical developer spaces
  about the future of labor, code quality and slop... the thing being refused
  often does not go away and instead becomes the main subject of the
  community's identity." The current post's Claim 7 (OSS/FLOSS community
  "splitting this deeply over LLMs and agents" despite legitimate underlying
  concerns) is the platform-policy-level manifestation of the same dynamic
  that post describes at the individual/mob level. Where communities-of-not
  documents informal social punishment of individuals (the rsync mob), this
  post documents the same fracture crystallizing into formal platform policy
  (Codeberg's Terms of Use) — a harder-to-reverse, institutional version of
  camp formation.

- **Extends**: `blog-ronacher-communities-of-not.md` Claim 5 — "Resisting that
  can be legitimate but that is no excuse for using one's rejection to justify
  shitty mob behavior." The current post's Claim 7 performs the identical
  move at the platform level: naming the legitimate concerns (copyright,
  labor, energy use, slop, maintainer burden) explicitly before arguing that
  the community's chosen response (excluding rather than engaging) is not the
  right way to act on them.

- **Extends**: `blog-ronacher-gaslighting-openness.md` Claim 5 — "Democratized
  access to technology, including AI, is in everyone's interest... Disliking
  the EU, China, or any other large government should not make us forget that
  true democratized access to technology including AI is in all our
  interest." That post argues for keeping access gates open against corporate
  and regulatory gatekeepers (Anthropic, Apple, national governments). The
  current post's Claim 2 and Claim 8 apply the identical "keep the gates
  open" instinct to a different kind of gatekeeper: a nonprofit, member-
  governed Open Source platform excluding AI-assisted projects. Ronacher's
  position is consistent across gatekeeper type — corporate, governmental, or
  community-democratic access restrictions all draw the same "this narrows
  who gets to participate" objection from him, even though the current post's
  gatekeeper is ideologically aligned with the Open Source values he
  otherwise shares.

- **Extends**: `blog-ronacher-ai-nationalism-americans-only.md` Claim 4 — "We
  depend on American cloud providers, operating systems, developer platforms
  and now AI models and internet from satellites... If access to frontier AI
  becomes a matter of American national security policy, Europe is not a peer
  in that conversation and might not even be a market." That note names
  "developer platforms" (i.e., GitHub) as one of five layers of European
  dependency on US infrastructure. The current post's Claim 9 (Codeberg as a
  potential "broad and dependable European alternative to GitHub") is
  Ronacher's candidate mitigation for exactly that dependency layer — and his
  central complaint is that the new AI-exclusion policy makes Codeberg less
  likely to succeed at filling that role, because it narrows Codeberg's
  addressable community rather than broadening it.

- **Contradicts**: None identified. No existing corpus source note argues
  that platform-level AI-authorship thresholds are enforceable, or that
  community-democratic exclusion policies are a low-risk way to resolve OSS
  AI-adoption tension. The Codeberg ToS text itself is a primary artifact
  (extracted above), not a corpus source note, so no contradiction issue was
  filed against it — this note reports Ronacher's critique of that policy
  without asserting the Assayer/Smith should treat the policy itself as
  refuted.

- **Novel**:
  - **Platform terms-of-use as a distinct AI-adoption friction category**: No
    existing corpus source documents a formal, democratically-adopted
    platform policy excluding AI-authored projects, or the specific
    enforcement mechanics (moderator discretion, presidium majority vote on
    non-obvious cases) of such a policy. Prior corpus sources on adoption
    friction cover individual tribal dynamics (communities-of-not) and
    corporate/governmental access restriction (gaslighting-openness,
    ai-nationalism); this is the first to cover a community-governed
    platform's own contribution policy.
  - **Self-inapplicable percentage thresholds as a policy design failure
    mode**: The specific argument — that a proportion-based AI-authorship
    threshold fails because even a technically sophisticated author cannot
    self-classify against it — is not documented elsewhere in the corpus and
    is directly actionable for any team drafting similar policy language.
  - **"The center has a bias" applied to policy enforcement at an ambiguous
    threshold**: This is the first corpus note to connect that framing
    (previously only referenced as unmined linked context in
    `blog-ronacher-communities-of-not.md`) to a concrete enforcement
    prediction: that projects near a policy's ambiguous middle are treated
    worse than clear cases on either side.
  - **The verbatim Codeberg ToS clause and its stated rationale**: No
    existing corpus source has extracted the actual text of an OSS platform's
    AI-exclusion policy. This note is the first to include the primary
    document alongside Ronacher's commentary on it.

## Guide Impact

- **Chapter 05 (Team Adoption — Model Deprecation Is a Recurring Governance
  Event, line ~560)**: That section frames vendor/model deprecation as a
  governance event teams must plan for. This source extends the same
  "governance event" framing to platform-level policy changes around AI
  authorship — a project's hosting platform (or, by extension, a package
  registry, CI provider, or internal engineering platform) can unilaterally
  change what kinds of AI-assisted contributions it will accept, and that
  change can arrive via a democratic process that is procedurally legitimate
  but substantively disruptive (Claim 1). Recommend adding platform
  acceptable-use policy changes as a named category of governance risk
  alongside model deprecation.

- **Chapter 05 (Team Adoption — Common Objections and Real Answers, line
  ~1117)**: Claim 7 (legitimate concerns — copyright, labor, energy, slop,
  maintainer burden — being real even when the community's chosen response is
  counterproductive) provides language for distinguishing valid objections to
  AI adoption from unproductive camp-formation, directly usable alongside the
  existing "communities-of-not" framing already recommended for this
  chapter. Recommend citing Claim 3 and Claim 5 as a concrete policy-design
  lesson for any internal team writing its own AI-usage guidelines: prefer
  binary, checkable rules (disclosure required / not required; bot-behavior
  thresholds) over proportion-of-authorship thresholds, because the latter
  fails even when self-applied by a good-faith, technically sophisticated
  author.

- **Chapter 00 (Principles) or Chapter 05 — Vendor/Platform Evaluation**: If
  the guide develops general guidance on evaluating shared infrastructure
  (hosting platforms, registries, forges) for AI-native teams, Claim 2 (
  predictability and neutrality matter more than governance model) is a
  reusable evaluation lens: a platform's stated AI-usage policy and how
  mechanically enforceable it is should be assessed independently of whether
  the platform is corporate or community-governed. Democratic governance does
  not guarantee predictable outcomes for platform dependents, and non-
  democratic governance does not guarantee poor ones.

## Extraction Notes

- Full article HTML was fetched directly via `curl` from
  `https://lucumr.pocoo.org/2026/7/24/codeberg-divides/` after WebFetch
  repeatedly returned summarized/paraphrased content rather than verbatim
  text despite explicit anti-summarization instructions (tried the page URL,
  the site's `.md` mirror, and an explicit "reproduce verbatim" prompt three
  times; all three attempts returned condensed prose). All quotes in this
  note were verified character-for-character against the raw HTML paragraph
  text.
- The actual Codeberg Terms of Use text was independently fetched via `curl`
  from `https://codeberg.org/Codeberg/org/raw/branch/main/TermsOfUse.md`
  (the canonical source Ronacher links to) rather than relying on his
  paraphrase, so the Concrete Artifacts section quotes Codeberg's own policy
  language, not Ronacher's characterization of it.
- Two linked Ronacher posts were fetched for context and are noted in
  Concrete Artifacts → "Linked context": `/2026/4/28/before-github/` (his
  stated motivation for wanting GitHub to face competition) and
  `/2026/4/11/the-center-has-a-bias/` (the argument behind the "center has a
  bias" reference in Claim 4). Neither was deep-mined as an independent
  source in this note; both remain candidates for independent mining.
- The linked lobste.rs discussion thread
  (`https://lobste.rs/s/ax914v/protecting_our_floss_commons_from_llms`) that
  Ronacher cites as the origin of the policy change was not fetched — it is a
  discussion aggregator thread, not a primary source, and the primary policy
  document (Codeberg's own ToS) was fetched directly instead.
- The post is short (~600 words, eight paragraphs) with no code examples,
  metrics, or session transcripts of its own; the only concrete artifact
  internal to the post is the paraphrased policy line, which this note
  supplements with the actual verbatim policy text fetched independently.
- Confidence rated anecdotal overall: every extracted claim is Ronacher's
  normative argument or first-person self-assessment (Claim 3). The one
  verifiable, settled fact in this note — the literal text of Codeberg's
  Terms of Use clause — is reported directly from the primary source in
  Concrete Artifacts rather than folded into the anecdotal claims about its
  wisdom or enforceability.
- Three Prospector triage comments were included in the issue, naming
  slightly different chapter targets (Ch06/Ch02; Ch05; Ch01/Ch02). Given the
  guide's actual current chapter files (00-principles, 01-daily-workflows,
  02-harness-engineering, 03-verification, 04-context-engineering,
  05-team-adoption, 06-security-threat-model — confirmed by directly listing
  `guide/`), this extraction maps Guide Impact to Chapter 05 (Team Adoption),
  which already contains directly relevant sections ("Model Deprecation Is a
  Recurring Governance Event," "Common Objections and Real Answers"), rather
  than to the Prospector's Ch06 suggestion, since the current Chapter 06 is
  "Security Threat Model" and not an adoption/community chapter. No chapter
  in the guide currently covers open-source community governance as a
  standalone topic.
- Cross-references verified: all `Claim N` citations from
  `blog-ronacher-communities-of-not.md`, `blog-ronacher-gaslighting-openness.md`,
  and `blog-ronacher-ai-nationalism-americans-only.md` were checked against
  the actual numbered claims and verbatim quotes in those notes before
  writing this note.
- No contradiction issue filed. No existing corpus source note makes a claim
  that this source directly opposes in a way that would change guide advice
  in conflicting directions.
