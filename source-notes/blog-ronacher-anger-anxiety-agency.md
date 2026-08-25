---
source_url: https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/
source_type: blog-post
title: "Anger, Anxiety and Agency"
author: Armin Ronacher
date_published: 2026-08-24
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: anecdotal
issue: "#2931"
---

# Anger, Anxiety and Agency

> Armin Ronacher argues that anxiety — not anger — is the appropriate emotional
> response to AI-driven disruption, because anxiety does not require a target
> to blame while anger does; he warns that AI's diffuse, structural disruption
> makes it easy to pick the wrong villain, and prescribes curiosity and
> experimentation as the path to earning the right to decide when resistance
> is actually warranted.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~900 words; single
  untitled essay, no section headers; first-person reflective/opinion piece
  published 2026-08-24)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent. His blog is a
  designated `trusted-feed` source in this repo. This post is personal
  emotional/psychological reflection — not practitioner analysis of technical
  patterns (contrast with `blog-ronacher-the-coming-loop.md` or
  `blog-ronacher-pi-oss.md`) and not political/structural analysis (contrast
  with `blog-ronacher-ai-nationalism-americans-only.md`, though it touches the
  same European-dependency concern in one aside). It is written explicitly as
  a response to another author's post (Sean Goedecke, "You should never be
  angry at work") and to a Lobsters comment thread, and discloses Ronacher's
  own dual position as both a working programmer and a company owner. Claims
  are pure first-person opinion and self-report; no data, study, or named
  third-party evidence beyond the two linked posts and one linked news article.
- **Scope**: Covers the emotional distinction between anger and anxiety in
  response to AI disruption, the "who is the villain" framing of tech-industry
  anger, the observation that both individual contributors and leadership
  experience uncertainty without foresight, curiosity/excitement as productive
  alternatives to anger, and a closing normative claim about where legitimate
  anger should be directed (society, climate, geopolitical power balance) and
  how to earn the standing to act on it. Does NOT cover: specific technical
  workflows, harness engineering, team rollout mechanics, or any quantitative
  evidence. This is the most purely psychological/emotional-register piece by
  this author in the corpus so far.

## Extracted Claims

### Claim 1: Ronacher agrees that anger at work rarely improves outcomes, and specifically warns against starting an internal "mutiny" when you disagree with a company's shared vision but lack the power to change it
- **Evidence**: Direct endorsement of Sean Goedecke's linked post ("You should
  never be angry at work"), plus Ronacher's own first-person lesson learned
  ("I did learn that lesson, but it did not come naturally").
- **Confidence**: anecdotal
- **Quote**: "Anger can be a useful signal, but being angry at work rarely improves the situation. More often, it makes life worse for the people around you, many of whom have no more power over the source of your anger than you do."
- **Additional quote**: "in a company there is a shared vision, and if you don't agree with it and are not in a position to change it, you should not start a mutiny, not even a small-scale one. Nothing good comes from that."
- **Our assessment**: This is the framing premise the rest of the post builds on, not the post's distinctive contribution (that credit goes to Goedecke's linked essay). The "mutiny" language is specific and useful as team-adoption vocabulary: it names the failure mode of an individual contributor who disagrees with an AI-adoption decision escalating to covert resistance rather than either accepting the decision or leaving. It presupposes the disagreeing party lacks the standing to change the decision — the advice does not extend to people who do have that standing.

### Claim 2: In response to the question "How can you work in tech right now and not be angry?", Ronacher's answer is that the appropriate emotional register for AI-driven disruption is disorientation and anxiety, not anger
- **Evidence**: Direct response to a specific, quoted Lobsters comment from the
  discussion thread under Goedecke's post, explicitly connected to AI and
  agents by Ronacher.
- **Confidence**: anecdotal
- **Quote**: "How can you work in tech right now and not be angry?"
- **Additional quote**: "In the context of the thread, this was clearly also about AI and agents. For me, the emotions I would expect in tech vis-a-vis these new developments are disorientation and anxiety, but not anger."
- **Our assessment**: This reframes a common adoption-resistance question (implicitly: "isn't anger the rational response to AI disruption?") as a category error — the question assumes anger is the only available register. The reframing is useful for team leads fielding this exact objection from engineers, since it supplies a named alternative emotional vocabulary (disorientation, anxiety) rather than just "calm down."

### Claim 3: Anxiety and anger are mechanistically different emotions — anxiety does not require a target to blame, while anger inherently needs to be directed at someone or something
- **Evidence**: Ronacher's own definitional distinction, offered as the
  analytical core of the post.
- **Confidence**: anecdotal
- **Quote**: "Anxiety as an emotion does not require someone to blame. Right now, I find it reasonable to feel anxious about an uncertain future. Who knows what our professions will turn into and what kind of world my kids will find themselves in when they enter the workplace? And if you've been in the industry for a long time, will the skills you've spent years acquiring still matter?"
- **Additional quote**: "anger is different from anxiety because anger needs to be directed somewhere. The feeling of anger suggests that somebody or something is doing something to you."
- **Our assessment**: This is the post's central analytical claim and its most reusable piece of vocabulary. The blame-requirement distinction gives team leads and individual practitioners a diagnostic question to ask when someone reports being "angry about AI": is there an actual identified actor doing something to you, or is the underlying feeling actually anxiety (uncertainty) misread as anger because anger feels more actionable (see Claim 4)? The claim is asserted, not empirically tested, but it is internally coherent and matches ordinary usage of both terms.

### Claim 4: Anger is more emotionally "actionable" than anxiety because it converts an admission of "I don't know" into a comforting narrative with a villain — but AI's disruption is diffuse enough that it is easy to pick the wrong villain, including blaming managers or leaders who are themselves uncertain and merely projecting confidence
- **Evidence**: Ronacher's own mechanism argument, extended to a specific
  named risk: misdirected anger at immediate superiors.
- **Confidence**: anecdotal
- **Quote**: "Anxiety is an uncomfortable emotion because it acknowledges that you do not know what will happen and might not be able to stop it. On the other hand, anger can feel more actionable because, instead of saying 'I don't know,' you already have someone to blame. It turns a loss of control into a comforting story with a villain. But I feel that particularly when it comes to AI, it's easy to pick the wrong villain because of how disruptive the change is for everyone."
- **Additional quote**: "Your engineering manager or leadership team might themselves feel uncertain about their future and just try to bolster their own confidence by projecting clarity and certainty."
- **Our assessment**: This is the most directly actionable claim for team-adoption guidance: it names a specific misattribution risk (blaming a manager who is themselves anxious and performing confidence) that plausibly drives a real category of workplace conflict during AI rollouts. It corroborates and gives an individual-psychology mechanism for the mob/scapegoating dynamics documented at the community level in `blog-ronacher-communities-of-not.md` (see Cross-References).

### Claim 5: Ownership and leadership positions provide agency but not foresight — many people who project public confidence about AI are privately far less certain, and are placing bets while trying to keep their businesses afloat
- **Evidence**: Ronacher's first-person observation from his own position
  engaging with founders and leaders ("I engage with plenty of people who
  project confidence in public and are much less certain in private").
- **Confidence**: anecdotal
- **Quote**: "The fact that this is happening shows us that owners and founders don't necessarily know what will happen. Ownership comes with agency, but it does not provide foresight, and this change is disorienting for everybody."
- **Additional quote**: "Many of them are placing bets, but they are talking with confidence about those bets, trying to keep their business afloat while the ground moves under them. They experience that uncertainty from a position where they can act on it, and they are often standing somewhere with a megaphone to get others on their side to improve their odds."
- **Our assessment**: This directly supports Claim 4's "wrong villain" warning with a structural reason: leaders project confidence not because they know more, but because their position gives them agency to act on uncertainty and a platform to rally others — public confidence is a function of position, not of superior knowledge. For team-adoption guidance, this suggests leadership communication that overclaims certainty about AI's trajectory is itself a (perhaps unintentional) contributor to the wrong-villain dynamic in Claim 4, since it invites employees to read confident messaging as knowledge rather than as bet-placing.

### Claim 6: Ronacher reports experiencing the same contradiction he describes — simultaneously excited and uncertain, unsure what programming will mean in the future or where competitive advantage will settle even as a company owner, oscillating between feeling liberated and feeling like "the ground is crumbling"
- **Evidence**: First-person self-report, offered as evidence that the
  emotional split he describes is not merely theoretical.
- **Confidence**: anecdotal
- **Quote**: "I feel that contradiction myself: I am simultaneously tremendously excited, but I am also unsure what will happen next. I do not know what it will mean to be a programmer in the future, and, as the owner of a company, I am also not sure where the high ground will be when this all settles."
- **Additional quote**: "Some days that feels liberating, but on others I wake up feeling like the ground is crumbling beneath me."
- **Our assessment**: This is a credibility-building self-disclosure rather than a new analytical claim — Ronacher applies his own framework to himself, including in his capacity as an owner (the group he otherwise describes as agency-but-not-foresight in Claim 5). It reinforces that the anxiety/curiosity framing is not advice from a position of certainty but a description of how to hold genuine, ongoing uncertainty.

### Claim 7: The "AI gains will benefit companies rather than employees" narrative is real and has direct evidence (a named Meta executive statement), but it is complicated by the fact that many leaders themselves distrust AI vendors — worried about cost capture by AI labs, data exposure, and vendors becoming competitors rather than partners
- **Evidence**: Ronacher names a specific external example (linked article
  about a Meta executive) as evidence for the pro-company-capture narrative,
  then immediately complicates it with his own observation of leadership
  anxiety about vendor dependency.
- **Confidence**: anecdotal (the Meta example is a specific, externally
  verifiable data point; the leadership-anxiety observation is Ronacher's own
  unquantified impression)
- **Quote**: "One narrative that is pretty pervasive is that if AI will usher in productivity gains, those gains are going to benefit companies rather than employees. And well at least someone at Meta wants that."
- **Additional quote**: "Yet I also find that plenty of people in leadership positions express doubt about AI. They see that an increasing share of their costs is being funneled directly to some large AI labs. They express worries about what will happen to their data and whether these large companies will step into their space instead of being partners."
- **Our assessment**: This is a useful corrective to a one-sided "management wants AI, workers don't" framing that team-adoption guidance can lean on too easily. Ronacher's point is not that the labor-capture narrative is false, but that it coexists with a distinct and separate leadership anxiety (vendor/platform dependency risk) that is not about labor at all. For guide purposes, this suggests two independent anxieties in the same rollout — employees worried about value capture, leaders worried about vendor capture — that can be mistaken for each other or used to talk past one another.

### Claim 8: Uncertainty is a more productive emotional state than anger because it can lead to curiosity, and much of AI's realized value is currently showing up as individually-owned side projects rather than as company-captured productivity gains
- **Evidence**: Ronacher's own prescriptive argument and observation about
  where AI-enabled output is currently landing.
- **Confidence**: anecdotal (the side-projects observation is asserted, not
  measured — no count, survey, or platform data is cited)
- **Quote**: "instead of being angry, you can simply be unsure. The feeling of uncertainty is a much more productive emotional state because it can lead to curiosity. Even if you don't find what's happening right now exciting, you can at least find it interesting. We have access to magic machines, and we can poke at them and see what happens."
- **Additional quote**: "A lot of the gains from AI aren't turning into productivity gains that are reflected in company profits but they're showing up instead in the number of side projects shipped by everybody not on their company's time."
- **Our assessment**: The curiosity-as-productive-uncertainty framing is the post's main prescriptive contribution at the individual level. The side-projects claim is asserted without evidence (no data on side-project volume is cited or linked) and should be treated as an anecdotal impression, not a documented trend — the guide should not cite the specific "gains are showing up in side projects, not company profits" claim as established without independent corroboration.

### Claim 9: Legitimate villains do exist, but Ronacher locates them at the societal/geopolitical scale — the impact on society, climate, and global power balance, including Europe's dependence on other countries — rather than at the level of individual colleagues or managers
- **Evidence**: Ronacher's own closing normative claim, naming specific
  categories of harm.
- **Confidence**: anecdotal
- **Quote**: "That does not mean there are no villains. When this all plays out, some will profit and many will not. I'm afraid we're completely ignoring the impact this has on society at large, the climate, and the balance of the world as a whole. As excited as I am about the technology, I worry about Europe's lack of ambition and growing dependence on other countries."
- **Our assessment**: This directly echoes the structural European-dependency concern developed at length in `blog-ronacher-ai-nationalism-americans-only.md` (see Cross-References), compressed here into a single aside. Its guide-relevant function is to draw a scale boundary: Ronacher is not arguing anger is never warranted, only that its target should be commensurate with the disruption's actual (structural/societal) scale rather than displaced onto an individual coworker or manager who is themselves uncertain (Claim 4).

### Claim 10: The prescribed response to feeling angry and looking for a villain is to redirect that impulse into curiosity and experimentation first, and only from what is learned that way to earn the right to decide when and where resistance is actually warranted
- **Evidence**: Ronacher's closing normative conclusion, stated as direct
  advice.
- **Confidence**: anecdotal
- **Quote**: "I don't know what the future of this industry will look like, and I don't know who will benefit from it and I don't think I'm alone with that. However I can only urge anyone who feels anger and looks for a villain right to instead remain curious instead. To be curious enough to understand what is changing, excited enough to experiment with it. And then, from what we learn, earn the right to decide when resistance is warranted and where to direct it."
- **Our assessment**: This is the post's terminal prescription and ties Claims 1–9 together: curiosity and direct engagement are framed as a prerequisite for legitimate resistance, not an alternative to it — the sequence is understand/experiment first, decide on resistance second. This closely parallels the individual-level prescription in `blog-ronacher-communities-of-not.md` Claim 7 ("default to being open to new things") and the organizational-level conclusion in `blog-ronacher-the-coming-loop.md` Claim 13 (retain judgment rather than abdicating it within an inevitable change), applied here specifically to the emotional register rather than to community behavior or harness architecture.

## Concrete Artifacts

### The triggering Lobsters comment and its context

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/
        citing a comment on https://lobste.rs/s/mbmn1f/you_should_never_be_angry_at_work
        (the Lobsters discussion of Sean Goedecke's post
        https://www.seangoedecke.com/you-should-never-be-angry-at-work/)

The quoted comment, verbatim:
  "How can you work in tech right now and not be angry?"

Ronacher's framing of scope: "In the context of the thread, this was clearly
also about AI and agents."
```

### Ronacher's implicit emotional-register taxonomy (reconstructed from the prose; not presented as a table in the original)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/

Emotion      | Requires a target to blame? | Ronacher's framing
-------------|------------------------------|----------------------------------
Anger        | Yes                          | "feels more actionable"; converts
             |                              | loss of control into "a comforting
             |                              | story with a villain"; risk of
             |                              | targeting the wrong villain
Anxiety      | No                           | "does not require someone to
             |                              | blame"; acknowledges "you do not
             |                              | know what will happen and might
             |                              | not be able to stop it"
Uncertainty/ | No                           | "a much more productive emotional
curiosity    |                              | state"; "we can poke at them and
             |                              | see what happens"
Excitement   | No                           | "a newfound feeling of power and
             |                              | freedom", reached by "mov[ing]
             |                              | beyond curiosity"

Note: this taxonomy is this note's synthesis of the post's argument, not a
table or list format used by Ronacher himself — the underlying quotes above
are each verbatim from the source.
```

## Cross-References

- **Extends**: `blog-ronacher-communities-of-not.md` Claim 6 — that note
  documents the community-level mechanism by which shared insecurity becomes
  collective harassment: "Whatever insecurities we have, finding a group of
  others sharing them can be comforting. The danger is that being part of a
  crowd of negativity can easily make us part of collective harassment." The
  current post's Claim 4 (anger's need for a target, and the risk of choosing
  the wrong one) supplies the individual-level emotional mechanism that
  precedes and feeds the community-level mob dynamic documented there: an
  individual first converts uncertainty into blame-seeking anger (this post),
  and that blame-seeking, when shared with others holding the same
  insecurity, can escalate into the tribal punishment behavior described in
  `communities-of-not`. The two posts describe adjacent stages of the same
  underlying dynamic — individual emotional mechanism here, group social
  mechanism there.

- **Extends**: `blog-ronacher-communities-of-not.md` Claim 7 — that note's
  individual prescription is "breathe, slow down, de-escalate when given the
  chance, and resist the temptation to always assume the most catastrophic
  reading. Default to being open to new things." The current post's Claim 10
  (curiosity and experimentation as a prerequisite for earning the right to
  decide on resistance) is a more fully developed version of the same
  "default to openness" prescription, now framed specifically around the
  anger/anxiety distinction rather than around catastrophic-reading bias.

- **Corroborates**: `blog-ronacher-ai-nationalism-americans-only.md` Claims 4
  and 8 — that note documents Europe's layered structural dependency on US
  technology infrastructure ("We depend on American cloud providers, operating
  systems, developer platforms and now AI models...") and argues a stronger EU
  is "at best, a temporary defense against a darker world." The current post's
  Claim 9 names the same concern in a single compressed aside: "I worry about
  Europe's lack of ambition and growing dependence on other countries." The
  current post does not develop the argument further — it is a corroborating
  restatement by the same author, not new evidence — but it confirms the
  concern is a standing, recurring position for Ronacher rather than a
  one-off argument specific to the export-control post.

- **Extends**: `blog-ronacher-the-coming-loop.md` Claim 13 — that note's
  organizational conclusion is that "the question is not whether we will loop
  because clearly we will. Maybe the question is that in a future of loops,
  how do we don't abdicate judgment..." The current post's Claim 10 makes a
  structurally identical move at the individual-emotional level: the question
  is not whether disruption is happening (it is), but how to retain enough
  judgment and agency (via curiosity and direct engagement) to decide when
  resistance is actually warranted, rather than either freezing in anxiety or
  discharging it as misdirected anger.

- **Contradicts**: No specific existing source note makes a claim that
  directly opposes this post's core anger/anxiety distinction or its
  villain-displacement warning. No contradiction issue filed.

- **Novel**:
  - **The anger-requires-blame / anxiety-does-not distinction as a named
    diagnostic**: No existing corpus source draws this specific mechanistic
    line between the two emotions, or uses it to explain why anger is
    experienced as more "actionable" than anxiety. This is new vocabulary for
    the corpus.
  - **"Wrong villain" as a named risk in AI-adoption conflict**: No existing
    corpus source names the specific failure mode of employees directing
    anger at managers or leaders who are themselves anxious and merely
    projecting confidence. This is a new, concrete adoption-conflict pattern.
  - **Leadership's "agency without foresight" framing**: No existing corpus
    source makes the specific claim that ownership/leadership positions
    confer the ability to act on uncertainty (agency) without conferring
    superior knowledge of outcomes (foresight), and that public confidence is
    therefore a function of position rather than of insight. This is a novel,
    reusable framing for team-adoption communication guidance.
  - **The dual-anxiety framing (labor value capture vs. vendor/platform
    capture)**: No existing corpus source explicitly separates "employees
    worried AI's gains will benefit the company, not them" from "leaders
    worried AI vendors will capture their margin/data/market" as two distinct,
    coexisting anxieties in the same organization. This is new to the corpus.
  - **Curiosity/experimentation as a precondition for "earning the right" to
    resist**: While `blog-ronacher-communities-of-not.md` prescribes openness
    generally, no existing corpus source frames direct engagement and
    experimentation specifically as something that must happen *before* a
    person has standing to decide whether and where resistance is warranted.

## Guide Impact

- **Chapter 05 (Team Adoption) — "Common Objections and Real Answers,"
  Objection 6 ("I don't want to be forced to use AI")**: The chapter's
  existing objection-handling framing can be sharpened with Claim 3's
  anger/anxiety distinction: when an engineer expresses hostility toward
  mandated AI adoption, the guide could suggest team leads first check
  whether the underlying feeling is actually undirected anxiety (about skill
  relevance, job security, or how the work will change) being expressed as
  anger because anger feels more actionable (Claim 4). Treating the two
  differently — anxiety needs acknowledgment and information, anger needs a
  correctly identified target or it misfires onto colleagues — is a concrete,
  actionable addition this source supplies that the chapter does not
  currently have.

- **Chapter 05 (Team Adoption) — rollout communication guidance (adjacent to
  "Pulling It Together: A Rollout Playbook")**: Claim 5 (leaders project
  public confidence that outstrips their private certainty) is a specific
  risk for whoever authors rollout communication: overclaiming certainty
  about AI's trajectory invites employees to read confident messaging as
  superior knowledge rather than as bet-placing, which plausibly worsens the
  "wrong villain" dynamic in Claim 4 when those bets do not pan out as
  described. The guide could recommend that rollout messaging be explicit
  about what leadership does and does not actually know, rather than
  projecting uniform certainty.

- **Chapter 05 (Team Adoption) — same section as
  `blog-ronacher-communities-of-not.md`'s existing Guide Impact entry on
  "Understanding Resistance"**: This post adds an individual-psychology layer
  underneath that note's social-identity layer. Team leads distinguishing
  "substantive concern" from "tribal identity resistance" (per
  `communities-of-not`) can use this post's anger/anxiety mechanism (Claim 3)
  as the earlier diagnostic step — before resistance has hardened into group
  identity, it often starts as individual blame-seeking anger standing in for
  unexpressed anxiety.

- No addition is recommended for Chapter 00 (Principles) or Chapter 01 (Daily
  Workflows): this post's content is about the emotional/interpersonal
  register of AI disruption, not about verification practice, harness design,
  or daily workflow mechanics, and neither existing chapter has a natural
  section for individual-practitioner psychological framing.

## Extraction Notes

- Full post HTML was fetched directly via `curl` from
  `https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/` (the post has no
  section headers and is short enough — twelve paragraphs, one blockquote —
  that the entire body was read and transcribed paragraph-by-paragraph; all
  quotes above were checked character-for-character against that transcription
  after decoding HTML entities, e.g. `&#8217;` → `'`).
- The post's central premise links to and directly responds to Sean
  Goedecke's "You should never be angry at work"
  (https://www.seangoedecke.com/you-should-never-be-angry-at-work/), which was
  also fetched in full via `curl` for context (it has no existing source note
  in this repo). Goedecke's post is workplace-anger advice generally, not
  AI-specific — Ronacher explicitly narrows the "how can you not be angry"
  question to the AI/agents context himself, and this note extracts only
  Ronacher's post, not Goedecke's, per the issue's scope (Goedecke is not the
  submitted source and could be separately mined if the Prospector queues it).
  The Lobsters thread (https://lobste.rs/s/mbmn1f/you_should_never_be_angry_at_work)
  was not fetched beyond the single quoted comment reproduced in Ronacher's
  post; the comment thread itself was not read.
- The linked Meta/Bosworth article
  (https://thenextweb.com/news/meta-bosworth-ai-productivity-more-work-not-time-off)
  was not fetched; Claim 7 attributes the "someone at Meta wants that" framing
  to Ronacher's own characterization, not to a verified quote from the linked
  article.
- Confidence rated anecdotal overall: every claim in this post is first-person
  opinion, self-report, or unquantified observation. There is no data,
  survey, or named study anywhere in the source. This is consistent with how
  this corpus rates other purely reflective Ronacher posts (e.g.
  `blog-ronacher-communities-of-not.md`, also anecdotal overall).
- Cross-references verified: all four `Claim N` citations to
  `blog-ronacher-communities-of-not.md`, `blog-ronacher-ai-nationalism-americans-only.md`,
  and `blog-ronacher-the-coming-loop.md` were checked against the actual
  numbered claims and verbatim quotes in those notes before writing (all four
  notes were re-read in full for this extraction, not recalled from memory).
- No contradiction issue filed: this post's claims are compatible with every
  existing Ronacher-authored note in the corpus and do not oppose any
  non-Ronacher source note's claims on adoption psychology or team dynamics.
- Two Prospector triage comments were included on the issue, with differing
  chapter guesses (Ch01/Ch03/Ch05 in the first; Ch01/Ch05 in the second, with
  more specific "Notes for Miner" guidance pointing at emotional-regulation
  framing for team adoption and morale). This extraction maps Guide Impact
  against the actual `guide/*.md` chapter files and their real section
  headings rather than the triage comments' chapter numbering, and finds the
  best fit is Chapter 05 (Team Adoption) specifically, not Chapter 00 or 01.
