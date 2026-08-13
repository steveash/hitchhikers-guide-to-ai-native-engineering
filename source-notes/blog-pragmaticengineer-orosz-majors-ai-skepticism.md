---
source_url: https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for
source_type: blog-post
title: "Stop being skeptical about AI for development with Charity Majors"
author: Gergely Orosz, featuring Charity Majors (The Pragmatic Engineer podcast)
date_published: 2026-08-12
date_extracted: 2026-08-13
last_checked: 2026-08-13
status: current
confidence_overall: anecdotal
issue: "#2673"
---

# Stop being skeptical about AI for development with Charity Majors (The Pragmatic Engineer)

> A podcast episode/newsletter post in which Gergely Orosz interviews Charity Majors
> (CTO/co-founder of Honeycomb) about her evolution from March 2025 "try vibe coding"
> skepticism to a November 2025 conviction that AI (specifically Claude Code) is a
> generational infrastructure shift comparable to cloud computing in 2010 — landing on a
> contrarian claim that "code review is overrated," a "pets to cattle" metaphor for code
> generation, a verdict that 20 years of DevOps failed to close the code-to-production
> feedback loop, and tactical advice that non-deterministic AI-generated code demands
> *more* engineering discipline (testing, evals, conformance checking), not less.

## Source Context

- **Type**: blog-post / podcast episode page. The Pragmatic Engineer newsletter
  (`newsletter.pragmaticengineer.com`, Gergely Orosz) publishes a written companion post
  for each podcast episode. This post is not a full transcript — it is Orosz's own
  written framing ("In this episode" intro), a curated numbered list of "13 parts I
  found especially interesting" (the "Takeaways from the conversation with Charity"
  section, several containing direct pull-quotes from Majors), a timestamp index of the
  ~82-minute audio/video episode (also on YouTube, `HC8T1OlgYi0`), a "References" list of
  people/things mentioned, and links to related Pragmatic Engineer deep-dives. No
  full transcript of the audio/video conversation was found published alongside this
  post — only Orosz's curated digest and the direct quotes embedded in it are
  extractable as verbatim text.
- **Author credibility**: Gergely Orosz writes The Pragmatic Engineer, a widely-read
  software-engineering newsletter/podcast (`newsletter.pragmaticengineer.com` is a
  `trusted-feed` in this corpus, source of `survey-pragmaticengineer-ai-tooling-2026.md`
  and multiple `blog-pragmaticengineer-orosz-*` notes). Charity Majors is CTO and
  co-founder of Honeycomb (observability platform) and co-author of *Database
  Reliability Engineering* and *Observability Engineering* (2nd edition just released at
  time of this episode). She has an extensive existing presence in this corpus as one of
  the highest-credibility voices on the "balanced skeptic" position — see
  `blog-simonwillison-charity-majors-enthusiast-skeptic.md` (June 4, 2026) and
  `blog-simonwillison-charity-majors-code-economics.md` (June 17, 2026), both excerpts of
  her own Substack writing via Simon Willison. This episode is a direct interview, not a
  third-party excerpt, recorded roughly two months after those Substack pieces.
- **Scope**: Covers Majors' personal AI-skepticism timeline (March 2025 → November 2025
  inflection), her "2025 was for AI what 2010 was for cloud" framing, the "pets to
  cattle" metaphor for code generation, her "code review is overrated" position, her
  verdict on 20 years of DevOps, her argument that non-deterministic AI code requires
  more (not less) engineering discipline, career advice for anxious engineering
  directors, AI-fatigue coping tactics (Honeycomb's "no AI on Wednesdays" norm), a call
  for both AI camps to "tell the whole story," and a personal rule about not sending
  unread AI-drafted messages. Does NOT cover (from the accessible written content):
  the full audio conversation on Parse/Honeycomb history, individual productivity
  metrics, observability tooling specifics, or the leadership/engineering-management
  segments of the episode (these are listed only as timestamped topics, not digested
  into prose the way the AI-adoption "takeaways" are).

## Extracted Claims

### Claim 1: In March 2025, Majors publicly urged even AI skeptics to try vibe coding, while still doubting AI would have generational impact
- **Evidence**: First item in Orosz's 13-point takeaways list, describing a specific dated event (Majors speaking at SREcon).
- **Confidence**: anecdotal
- **Quote**: "In March 2025, Charity told the audience at SREcon to try vibe coding, and back then, the response was grumbling. Charity's point was that people who are skeptical of AI should still learn to use it, because you can complain better if you've learned it. At this time, Charity still saw AI having a bigger impact than a new programming language, but was skeptical that it would have a generational impact."
- **Our assessment**: This establishes the pre-inflection baseline for the rest of the episode's narrative arc — Majors was already advocating hands-on trial for skeptics eight months before she says her own view shifted (Claim 2), which is a useful data point that "try it before judging it" and "become a believer in generational impact" are separable positions, not the same claim.

### Claim 2: Majors' turning point toward seeing AI as a generational change came in November 2025, driven more by the Claude Code harness than by the underlying Opus 4.5 model
- **Evidence**: Second takeaway item; Majors explicitly separates model capability from harness maturity as the causal driver.
- **Confidence**: anecdotal
- **Quote**: "Charity's turning point in seeing AI as a generational change was in November 2025. This was due to Opus 4.5, but Charity argues that the coding harness (Claude Code) made the bigger difference. Because thanks to Claude Code, harnesses went from being more of a shell script to serious infrastructure."
- **Our assessment**: The "harness, not model" attribution is the most specific and checkable claim in this section — it names a mechanism (harness maturity) rather than a vague "the models got better." It corroborates a corpus theme (harness engineering as a distinct discipline from model capability) but is here stated as a personal causal attribution by one practitioner, not measured.

### Claim 3: Majors frames AI's 2025 industry impact as comparable in scale to cloud computing's 2010 impact
- **Evidence**: Third takeaway item, an explicit historical analogy drawn by Majors.
- **Confidence**: anecdotal
- **Quote**: "The impact of AI on the industry in 2025 was similar to the impact of the cloud in 2010. Looking back, Charity is comfortable saying this: in 2010, it became clear that cloud computing was certainly going mainstream and would change the infra-layer. After 2025, it's also clear that AI will have a similar impact on the infrastructure of building software."
- **Our assessment**: This is a rhetorical/historical framing claim, not an empirical one — no data is cited for either the 2010 cloud comparison point or the AI claim. Its value is as a credibility signal (a former skeptic committing publicly to a strong analogy) rather than as evidence.

### Claim 4: Pre-2025 AI skepticism was rational, because prior technologies (COBOL, neural nets, no-code/low-code) made similar transformation promises and fell short
- **Evidence**: Fourth takeaway item, listing specific prior-technology examples Majors cites as grounds for skepticism having been reasonable.
- **Confidence**: anecdotal
- **Quote**: "Engineers who were skeptical of AI up to 2025: they had good reason to be so. This was because we've seen plenty of technologies and innovations in the past that all promised to transform the software industry, but later fell short. Examples include COBOL (a technology promising that programmers would no longer be needed to create software), neural nets, no-code and low-code tools."
- **Our assessment**: This directly answers the Prospector's key question about temporal framing of when skepticism became irrational. Majors is explicit that skepticism was rational *through* 2025 given the base rate of prior over-promised technologies, and that her own position changed because of a specific event (Claim 2), not because skepticism was always unreasonable. This is a more measured framing than the episode's title ("Stop being skeptical") implies on its own.

### Claim 5: Majors believes it is a "when," not an "if," that professional engineers will ship AI-generated code to production without ever having read it, and that engineering's job is to build the systems that make that safe
- **Evidence**: Fifth takeaway item, framed as the central question of the episode.
- **Confidence**: anecdotal
- **Quote**: (no direct quote for the framing sentence; direct quote for the underlying question) "The question engineers need to answer: what would it take for you to be fully comfortable shipping code you have not read?"
- **Our assessment**: This reframes "verification" as a system-design problem rather than a human-reading-effort problem — the goal isn't faster human review, it's building validation infrastructure trustworthy enough that human reading becomes optional. This is a stronger and more specific claim than generic "AI will write more code" framing found elsewhere in the corpus.

### Claim 6: Majors proposes code may undergo a "pets to cattle" transition analogous to server infrastructure in the 2010s — broken code gets regenerated, not repaired
- **Evidence**: Sixth takeaway item, drawing an explicit parallel to the Terraform/Kubernetes-era shift from manually-repaired servers to disposable, re-created infrastructure.
- **Confidence**: anecdotal
- **Quote**: "AI could have the software industry go through the 'pets' to 'cattle' change that compute infra went through in the 2010s. Up to now, writing software from scratch was far more expensive than editing existing software. But now, generating hundreds of variants of a function can be done faster than how long it would take you to hand-write it once. Charity believes that we might be at the beginning of the transition from 'pets' to 'cattle' that happened at the hardware infrastructure layer. Before the 2010s, configuring and repairing individual servers was commonly done. But with tools like Terraform and Kubernetes, individual servers having issues are no longer fixed up: they are re-created instead. Charity thinks the same might happen with code, sooner rather than later. When there's an issue with the code, generate new code that solves it, and is verifyably correct."
- **Our assessment**: The "pets to cattle" framing is a novel, specific metaphor not present elsewhere in the corpus (checked below). It is a stronger and more mechanistic version of the capital-asset-to-consumable shift Majors already named in her June 17, 2026 Substack piece (see Cross-References) — here she names the *replacement mechanism* (regenerate rather than patch) rather than just the change in code's economic status.

### Claim 7: Majors' contrarian take: code review is overrated and the least valuable part of what humans contribute to software engineering, because humans are better at conversations and build decisions than at correctness-checking
- **Evidence**: Seventh takeaway item, stated as an explicit "contrarian take."
- **Confidence**: anecdotal
- **Quote**: "Her contrarian take: code review is overrated, and the least valuable part of what humans add to software engineering. Charity says that humans are good at conversations and deciding what to build, not reading code to check for correctness, syntax and bugs."
- **Our assessment**: This is presented by Orosz himself as contrarian, and it is worth checking against corpus consensus rather than accepting at face value. It does not, on inspection, contradict the existing corpus finding in `blog-anthropic-ai-native-engineering-org.md` (Claim 6) that code review has "bifurcated" — Claude catches bugs/style/tests while humans retain legal, security, and product-taste judgment. Majors' claim that humans are "not good at" reading code for correctness/syntax/bugs is consistent with ceding exactly that portion of review to AI, which is what Fung already describes doing at Anthropic. The novelty here is Majors' explicit value judgment ("least valuable part") rather than a new practice — see Cross-References for why this reads as corroboration/extension, not contradiction.

### Claim 8: Majors' verdict on 20 years of DevOps: the "ops people learn to code" half succeeded, but the "software engineers understand your code in production" half failed
- **Evidence**: Eighth takeaway item, an explicit two-part verdict distinguishing which half of the DevOps movement's feedback-loop goal succeeded.
- **Confidence**: anecdotal
- **Quote**: "Charity's verdict of 20 years of DevOps: it failed. The DevOps feedback was about trying to create a feedback loop that connected people writing the code to the code running in production. She thinks that the 'ops people: learn to code!' wave worked, but the 'software engineers: understand your code in production' failed, to this day."
- **Our assessment**: This is a specific, falsifiable historical claim from a co-author of *Database Reliability Engineering* and *Observability Engineering* — an author whose career is explicitly built on trying to close this exact feedback loop. It is a notably harsh self-assessment of her own field (observability), which lends it more credibility than a triumphalist framing would. It is entirely novel to the corpus (no existing note assesses DevOps as a movement) and sets up Claim 9 as her explanation for why AI-generated code makes this gap more urgent, not less.

### Claim 9: Non-deterministic AI-generated code requires more engineering discipline (testing, evals, conformance checking), not less, because trust shifts from the code's authorship to its validation
- **Evidence**: Ninth takeaway item, an explicit causal argument linking reduced trust in authorship to increased need for validation infrastructure.
- **Confidence**: anecdotal
- **Quote**: "Non-deterministic systems require more engineering discipline versus before. With code written by AI, we're reducing the trust in the code (because we no longer wrote it), so we need to increase trust at the other part of the development process. Specifically, at validation: with things like tests, evals, and conformance testing."
- **Our assessment**: This directly corroborates the June 17, 2026 Majors Substack claim (via Willison) that "AI demands more engineering discipline. Not less" (`blog-simonwillison-charity-majors-code-economics.md`, Claim 4) — here Majors names the specific mechanism (trust displaced from authorship to validation) that the June piece's title asserted without full elaboration in the accessible excerpt. This is an extension, not new evidence: same author, same thesis, more specific mechanism eight weeks later.

### Claim 10: Majors' career advice to anxious engineering directors is to consider returning to individual-contributor work, because agency (not the change itself) determines whether uncertainty is experienced as anxiety or excitement
- **Evidence**: Tenth takeaway item, including a direct quote framing the urgency of gaining AI experience.
- **Confidence**: anecdotal
- **Quote**: "The next time you'll have a job interview, you'll be filtered out if you don't have AI experience."
- **Our assessment**: This is tactical career advice rather than an engineering-practice claim — narrower scope than the rest of the episode's claims, but concrete and quotable. The "agency determines anxiety vs. excitement" framing is a psychological claim asserted without citation; treat as an anecdotal opinion, not a validated finding.

### Claim 11: Majors recommends small, deliberate acts of reclaiming control from AI tools as a countermeasure to AI fatigue, citing Honeycomb's team norm of not using AI on Wednesdays
- **Evidence**: Eleventh takeaway item, naming a specific team practice at Majors' own company.
- **Confidence**: anecdotal
- **Quote**: "Charity finds small acts of taking control back in your work from AI tools help. For example, none of the Honeycomb team uses AI on Wednesdays."
- **Our assessment**: This is a concrete, replicable organizational practice (a designated no-AI day) attributed to a named company (Honeycomb) by its CTO — more specific and actionable than generic "avoid AI fatigue" advice, and novel to the corpus (see Cross-References).

### Claim 12: Majors argues both the "AI-pilled" and "anti-AI" camps under-report the costs alongside the wins, and calls for both sides to tell the whole story
- **Evidence**: Twelfth takeaway item, with an extended direct quote from Majors.
- **Confidence**: anecdotal
- **Quote**: "There are some really incredible things happening in software right now, for example, with rewrites and with automating away toil. Not a single person that I've talked to would give up using AI. But half of the people are seeing the _wins,_ and they're not connecting it to the _cost_, which makes them think that their coworkers are just afraid of getting automated out of existence. So that's my beg to everyone who listens to this: tell the whole story! Talk about the costs as well. We're all in it together."
- **Our assessment**: This restates, in interview form and with new supporting language ("Not a single person that I've talked to would give up using AI"), the "both are not wrong" epistemological stance Majors already established in her June 4, 2026 Substack piece (see Cross-References). It is corroborating continuity of position, not a new claim — but the added detail (universal continued usage despite complaints) is a small new data point about her own informal observation of colleagues.

### Claim 13: Majors' personal rule for AI-assisted writing: never send a message or email to a human that you have not read in full yourself, because it will take the reader longer to read than it took you to produce it
- **Evidence**: Thirteenth takeaway item, a stated personal practice with an explicit rationale.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; paraphrase from the takeaways list) "Charity's rule on AI writing: do not send any message/email to a human that you yourself have not read in full. She also says that it would take them longer to read whatever you send than it took you to produce it: it's probably slop!"
- **Our assessment**: A narrow, tactical personal-practice claim rather than an engineering claim. Useful as a specific, quotable heuristic for a guide section on AI-assisted writing etiquette, but it is a personal rule, not a measured or widely-adopted norm.

## Concrete Artifacts

```
Source: The Pragmatic Engineer newsletter/podcast, Gergely Orosz interviewing Charity
Majors, "Stop being skeptical about AI for development with Charity Majors"
https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for
Published: August 12, 2026

Episode framing (from "In this episode"):
"In 2025, it was rational to be skeptical about AI, but in 2026 it's clear that AI is
changing all of the industry, and there's less and less place for skepticism."

"We explore how AI is changing the economics of code generation, why reliability and
verification are increasingly the bottlenecks, and why the rise of non-deterministic
systems requires more engineering discipline. Charity shares her views on code reviews,
observability, DevOps, leadership, and why both AI skeptics and enthusiasts are getting
important things right."

Timestamp index (topic labels only, ~82-minute episode, YouTube video ID HC8T1OlgYi0):
00:00 Intro
02:56 How Parse led to Honeycomb
06:00 The limits of individual productivity metrics
09:08 How Charity's perspective on AI has evolved
13:50 Rewriting code vs. editing code
19:20 Production as a stage of development
22:14 Code reviews
26:56 Non-deterministic systems
31:11 Sensible uses of AI
37:41 The two AI camps
44:40 Why AI works so well for building software
49:42 DevOps
55:13 Modern observability
1:00:40 Handling context overload
1:01:56 What's new in Observability Engineering's 2nd edition
1:07:45 What effective leadership looks like
1:10:25 Engineering management: what is changing?
1:16:31 Junior engineers
1:18:01 AI fatigue
1:21:39 Book recommendations
```

## Cross-References

- **Corroborates**: `blog-simonwillison-charity-majors-code-economics.md` (Claim 4 —
  "The article title indicates that engineering discipline should increase, not
  decrease, in response to the economic inversion," title-only claim: "AI demands more
  engineering discipline. Not less"): this episode's Claim 9 supplies the specific
  mechanism the June 17 Substack title asserted but that note could not access the body
  text for — trust shifts from code authorship to validation infrastructure (tests,
  evals, conformance testing), so discipline must increase at the validation layer even
  as it is no longer needed at the authorship layer.
- **Corroborates**: `blog-simonwillison-charity-majors-enthusiast-skeptic.md` (Claim 1 —
  "AI enthusiasts are not wrong... real, non-imaginary, discontinuous leaps in
  capabilities," and Claim 3 — "AI skeptics are also not wrong... shipping code faster
  than engineers can read it... depletes institutional trust"): this episode's Claim 12
  restates the same "both are not wrong" stance eight weeks later, adding the informal
  observation that "not a single person" she has talked to would give up AI despite the
  costs — continuity of position, same author, same core thesis.
- **Extends**: `blog-simonwillison-charity-majors-code-economics.md` (Claim 3 — "Code's
  epistemic status shifted from capital asset... to consumable... 'disposable and
  regenerable, practically overnight'"): this episode's Claim 6 ("pets to cattle")
  gives that capital-to-consumable shift a concrete mechanism and an explicit historical
  analogy (server infrastructure's 2010s shift from manual repair to Terraform/Kubernetes
  regeneration) that the June 17 excerpt's accessible text did not include.
- **Extends**: `blog-anthropic-ai-native-engineering-org.md` (Claim 6 — "Code review has
  bifurcated — Claude handles style, linting, bug-catching, test addition; humans retain
  domain expertise in legal, security, and product sense"): this episode's Claim 7
  ("code review is overrated... humans are good at conversations and deciding what to
  build, not reading code to check for correctness, syntax and bugs") is consistent with,
  not contradictory to, Fung's bifurcation — Majors' framing supplies the value judgment
  (why the human-correctness-checking portion of review is "the least valuable part")
  that Fung's first-person account describes practicing without editorializing on. Not
  filed as a contradiction: both sources agree on the specific allocation (AI catches
  bugs/correctness; humans do judgment work), they differ only in how strongly they
  editorialize about the human-correctness-checking portion's value, which is a framing
  difference, not an opposing recommendation.
- **Novel** (not present in any existing corpus note):
  - **"Pets to cattle" as a metaphor for code generation** (Claim 6): the corpus has
    prior claims about code becoming disposable/regenerable, but no prior source names
    the specific infrastructure-management analogy (Terraform/Kubernetes-era server
    regeneration vs. manual repair) or uses this specific metaphor.
  - **A dated, two-part verdict on DevOps as a 20-year movement** (Claim 8): no existing
    corpus note assesses DevOps's success or failure as a named historical movement, or
    distinguishes which half of its stated feedback-loop goal succeeded vs. failed.
  - **"2025 was for AI what 2010 was for cloud" as an explicit historical analogy**
    (Claim 3): the corpus has velocity/adoption timelines but no prior source frames
    2025 specifically against the 2010 cloud-computing mainstreaming moment.
  - **Honeycomb's "no AI on Wednesdays" team norm** (Claim 11): a specific, named,
    company-level AI-fatigue countermeasure not present elsewhere in the corpus.
  - **The "harness, not model" causal attribution for Majors' November 2025 inflection**
    (Claim 2): a specific practitioner's causal claim isolating harness maturity
    (Claude Code) from underlying model capability (Opus 4.5) as the more important
    driver of a generational-impact judgment.

## Guide Impact

- **Chapter 05 (Team Adoption — Framing AI Skepticism)**: Claim 4 (pre-2025 skepticism
  was rational given COBOL/neural-nets/no-code precedent) gives the guide a specific,
  named list of prior over-promised technologies to cite when validating skeptic
  concerns, rather than treating "skepticism was reasonable" as an unsupported
  assertion. Recommend citing this alongside the existing `blog-simonwillison-
  charity-majors-enthusiast-skeptic.md` "both are not wrong" framing.
- **Chapter 03 (Safety and Verification — Trust Displacement)**: Claim 9's specific
  mechanism (trust moves from code authorship to validation infrastructure — tests,
  evals, conformance testing — when authorship is no longer human) is a more precise,
  actionable framing than "AI demands more discipline" alone. Recommend adding this as
  the mechanistic explanation in any section that currently cites the June 17, 2026
  Majors piece's title without its reasoning.
- **Chapter 04 (Engineering Patterns — Code Review Reconsidered)**: Claim 7's contrarian
  framing ("code review is overrated... least valuable part") should be presented
  alongside, not instead of, Fung's bifurcation account (`blog-anthropic-ai-native-
  engineering-org.md` Claim 6) — the guide can use Majors' framing to explain *why* the
  bifurcation makes sense (humans are comparatively weak at correctness-checking) while
  using Fung's account for the concrete allocation (what specifically humans retain).
- **Chapter 05 (Team Adoption — Sustaining Adoption / AI Fatigue)**: Claim 11
  (Honeycomb's "no AI on Wednesdays" norm) is a concrete, citable example for a section
  on preventing AI fatigue or maintaining engineer skill/judgment under heavy AI use —
  currently the corpus has no similarly specific organizational countermeasure for this
  concern.
- **Chapter 00 (Principles)**: Claim 6's "pets to cattle" metaphor is a strong,
  memorable framing device the guide could adopt when explaining why code
  disposability changes engineering practice — pairing well with the existing
  capital-asset-to-consumable vocabulary already sourced from Majors' June 17 piece.

## Extraction Notes

- This post is a podcast-episode companion page, not a full transcript. WebFetch was
  used with several distinct, targeted prompts to reconstruct the page's actual text
  content section by section (an initial broad request returned only an AI-generated
  summary rather than verbatim text, so it was discarded and re-fetched with narrower,
  explicit "reproduce verbatim" prompts per section: "Takeaways from the conversation
  with Charity," "In this episode," "Timestamps," "References," and "The Pragmatic
  Engineer deepdives relevant for this episode"). All 13 items in the "Takeaways"
  section and all direct quotes in this note were captured this way.
- No paywall was encountered; the "Takeaways," "In this episode," "Timestamps," and
  "References" sections are fully accessible without a subscription. A "Discussion
  about this episode" comments section exists but returned no visible comment text or
  commenter names in the fetched content — not extracted.
- The full ~82-minute audio/video conversation (also on YouTube, video ID HC8T1OlgYi0)
  was not separately transcribed or fetched; this note is limited to Orosz's written
  digest and the direct quotes embedded within it. Topics visible only in the timestamp
  index (Parse/Honeycomb history, individual productivity metrics, observability
  tooling specifics, leadership/engineering-management segments, junior engineers, book
  recommendations) are named in Concrete Artifacts but not extracted as claims, since no
  verbatim prose describing their content was found on the page.
- No contradiction with existing corpus notes was found that meets the MINER.md §4a bar
  (a claim that materially opposes an existing source note's claim on the same topic in
  a way that would lead to different guide advice). Claim 7 ("code review is overrated")
  was checked closely against `blog-anthropic-ai-native-engineering-org.md` Claim 6
  because it is presented by Orosz himself as "contrarian" — see Cross-References for
  why it was assessed as an extension/framing difference rather than a contradiction.
- Cross-reference verification: all cited claim numbers were verified by re-reading the
  actual source notes before writing this note:
  - `blog-simonwillison-charity-majors-code-economics.md` Claim 4 (line 111): "The
    article title indicates that engineering discipline should increase, not decrease"
    — verified.
  - `blog-simonwillison-charity-majors-code-economics.md` Claim 3 (line 89): "Code's
    epistemic status shifted from capital asset... to consumable" — verified.
  - `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 1 (line 50): "AI
    enthusiasts are not wrong... real, non-imaginary, discontinuous leaps" — verified.
  - `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 3 (line 87): "AI
    skeptics are also not wrong... depletes institutional trust" — verified.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 6 (line 61): "Code review has
    bifurcated — Claude handles style, linting, bug-catching, test addition; humans
    retain domain expertise in legal, security, and product sense" — verified.
- Confidence is rated `anecdotal` (not `emerging`) despite Majors' high credibility as an
  authority, because every claim in this note is a personal, in-conversation assertion
  from a curated digest of a single interview, without the additional
  written-essay precision or independent corroboration that earned the June 2026
  Substack excerpts an `emerging` rating. Several claims here (Claims 9, 12) do
  corroborate those `emerging`-rated prior claims, which somewhat strengthens confidence
  in the recurring themes, but the episode-specific novel claims (DevOps verdict, "pets
  to cattle," Wednesday no-AI norm) are single-source anecdotes.
