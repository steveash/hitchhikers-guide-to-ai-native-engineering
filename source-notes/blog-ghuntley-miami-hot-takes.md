---
source_url: https://ghuntley.com/miami/
source_type: blog-post
title: "A couple of months ago in Miami, I sat down and dumped my brains. Here's the interview..."
author: Geoffrey Huntley
date_published: 2026-06-26
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: anecdotal
issue: "#1383"
---

# A couple of months ago in Miami, I sat down and dumped my brains. Here's the interview...

> Thirteen unstructured "hot takes" from an AI:Engineer Miami fireside chat, covering
> career risk from AI-driven commoditization, the coder/software-engineer distinction,
> SaaS per-seat economics instability, small AI-native team sizes, and a "play like a
> musical instrument" framing for building AI intuition — presented as opinion, not
> evidence-backed research.

## Source Context

- **Type**: blog-post (personal blog, ghuntley.com, June 26, 2026). The post is a
  short list of numbered observations framed as an interview transcript/recap of a
  fireside chat at AI:Engineer Miami, embedded with a YouTube clip of the chat
  ("Hot-takes at a fireside chat during AI:Engineer Miami").
- **Author credibility**: Geoffrey Huntley is the author; the post itself contains no
  biographical statement or credentials. Per the submitting issue's trusted-feed
  description, Huntley is tracked in this corpus's feed list for "deep agentic coding
  technique (Ralph loops, spec-driven autonomy)" — that characterization comes from
  the feed/Prospector metadata, not from the article body itself, and is noted here
  for context rather than treated as an in-article claim. The post itself is entirely
  first-person opinion ("hot takes"), with no data, citations, or named sources
  supporting any individual point.
- **Scope**: Thirteen numbered one- or two-sentence assertions about software-development
  commoditization, career risk, team economics, and how to build AI proficiency. No
  claim in the post is elaborated beyond a sentence or two — this is a bulleted opinion
  list, not an argued essay. One item (point 13, the "musical instrument" framing) is
  elaborated at length in a separate, directly-linked post (`ghuntley.com/play/`,
  embedded as a bookmark card), which was followed per extraction guidance. Does NOT
  cover: any methodology, data, case study, or named company beyond Huntley's own
  observations.

## Extracted Claims

### Claim 1: Software development is now a "dead-end profession" because AI has removed the barrier to writing code

- **Evidence**: Bare assertion, first item in the numbered list. No supporting argument or data in the post.
- **Confidence**: anecdotal
- **Quote**: "Software development is a dead-end profession because anyone can be a software developer now."
- **Our assessment**: Stated as a provocation rather than an argued position — the post immediately qualifies it in points 2–3 by distinguishing "software developer" from "software engineer." Taken alone, the headline claim is much stronger than what the rest of the list actually supports (which is closer to "the entry-level coding tier is commoditized," not "the whole profession is dead-end"). We read this as intentionally provocative framing for a fireside chat, not a considered forecast.

### Claim 2: Being able to use a coding tool (e.g., Cursor) to generate code is a different skill from being a software engineer

- **Evidence**: Bare assertion, second item in the list, immediately following Claim 1.
- **Confidence**: anecdotal
- **Quote**: "Anyone can use Cursor or any other tool and generate code. Being a coder and being a software engineer are different."
- **Our assessment**: This is the load-bearing distinction for the rest of the post — points 4, 9, and 10 all depend on a coder/engineer split where "coder" means "can produce code via a tool" and "engineer" means something more (see Claim 4 and Claim 10 for what Huntley says that "more" consists of). The post never fully defines "software engineer" beyond these adjacent points, so the distinction is asserted rather than operationalized.

### Claim 3: Computers used to be gated to specialists; AI has made them malleable to everyone, but that doesn't make everyone a software engineer

- **Evidence**: Bare assertion, third item in the list, restating and extending Claim 2 with a "gated vs. malleable" framing.
- **Confidence**: anecdotal
- **Quote**: "Computers used to be gated; now everyone has the power to make computers malleable. Everyone is a software developer now, but that does not mean they are software engineers"
- **Our assessment**: The "gated to malleable" framing is a specific and reusable metaphor for the accessibility shift — worth capturing verbatim if the guide wants a quotable line for the "coding is commoditized" narrative — but it is a restatement of Claim 2's distinction, not new evidence for it.

### Claim 4: If you cannot demonstrate how a coding agent works, you are a consumer, not an engineer, and you have capped your own career

- **Evidence**: Bare assertion, fourth item in the list.
- **Confidence**: anecdotal
- **Quote**: "If you cannot demonstrate how a coding agent works, you are just a consumer and have imposed an artificial glass ceiling on your career as a software engineer."
- **Our assessment**: This is the most concrete operational content in the post's coder/engineer distinction: the differentiator is being able to explain the agent's mechanism, not just operate it. This is compatible with — but more specific than — Fiona Fung's hiring philosophy in `blog-anthropic-ai-native-engineering-org.md` (Claim 9), which de-prioritizes "raw throughput" in favor of "deep systems expertise." Huntley's framing names understanding-of-mechanism as the specific gate; Fung's framing names systems expertise more broadly. Both agree that mechanical code-production ability is no longer the differentiator, but neither source defines a testable bar for "can demonstrate how a coding agent works."

### Claim 5: Curiosity, not experience or seniority, is now the primary determinant of career survival

- **Evidence**: Bare assertion, fifth item in the list.
- **Confidence**: anecdotal
- **Quote**: "If you are curious, you will have a job. If you have not been curious in the last two years, you are replaceable."
- **Our assessment**: This is a strong, unqualified claim with no criteria for what counts as "curious" or "replaceable," and no timeframe evidence beyond the two-year figure itself being asserted rather than derived. It pairs directly with Claim 13/the linked `/play/` post's "deliberate, intentional practice" framing — curiosity here appears to mean sustained hands-on experimentation with AI tools specifically, not general intellectual curiosity, based on how the linked post elaborates the same theme (see Concrete Artifacts and Claim 13).

### Claim 6: SaaS per-seat pricing economics may become unstable as customers need fewer people to achieve the same results, forcing founders to rethink unit economics

- **Evidence**: Bare assertion, sixth item in the list. No company names, no data, no timeframe given.
- **Confidence**: anecdotal
- **Quote**: "SaaS per-seat economics may become unstable as  customers need fewer people to achieve results, prompting founders to think about new unit economics" (double space before "customers" is verbatim from the source)
- **Our assessment**: This is framed as speculative ("may become") rather than observed. It is directionally consistent with — but distinct from — `blog-simonwillison-product-market-fit.md` (Claim 5), which documents that both Anthropic and OpenAI already shifted their own *AI vendor* enterprise pricing from flat/seat allocations to direct API/usage pricing in the Nov 2025–Apr 2026 window. Willison's claim is about AI labs' own pricing for AI products; Huntley's claim is a broader, unevidenced prediction about SaaS pricing generally (i.e., non-AI software vendors whose products require fewer human seats because AI increases per-person output). The two are adjacent but not the same claim — Willison's is a settled, sourced fact about two specific companies; Huntley's is speculation about an industry-wide effect with no company named. No existing corpus note makes Huntley's specific claim (customer-side seat reduction destabilizing vendor SaaS pricing), so this is novel as a hypothesis, not as a confirmed pattern.

### Claim 7: Most companies will take two to three years, or more, to complete their AI transformation

- **Evidence**: Bare assertion, seventh item in the list. No company examples or methodology.
- **Confidence**: anecdotal
- **Quote**: "Most companies will take two or three years (or more!) to figure out AI transformation."
- **Our assessment**: This is a bare timeline estimate with no stated basis (survey, case count, or reasoning). It is broadly consistent with the general "adoption takes time" pattern found elsewhere in the corpus (e.g., the Cowork deploy guide's multi-month maturity model in `blog-anthropic-cowork-deploy-guide.md`), but Huntley gives no specific mechanism for why 2–3 years is the right figure, so we treat it as an unsupported estimate rather than a calibrated one.

### Claim 8: Some companies are already building AI-native teams of five to ten people who build "with the grain of AI"

- **Evidence**: Bare assertion, eighth item in the list. No company named, no count of how many companies.
- **Confidence**: anecdotal
- **Quote**: "Some companies are already building AI native teams of five to ten people who can build with the grain of AI"
- **Our assessment**: This overlaps closely with `blog-thebatch-ng-aiteam-structure.md` (Claim 6), where Andrew Ng scopes his generalist-team argument explicitly to "AI-native teams with around 2-10 persons" — Huntley's 5–10 range sits inside Ng's broader 2–10 range. Both are anecdotal (editorial observation for Ng; unnamed "some companies" for Huntley) rather than survey-based, so this is convergent anecdote, not independent confirmation of a hard number. Neither source names which companies, so the convergence should be read as "two practitioners both landed on a similar small-team intuition," not as two independently measured data points.

### Claim 9: An explosion in the number of software developers is coming because software development is now essentially free and tokens are cheaper than human labor

- **Evidence**: Bare assertion, ninth item in the list.
- **Confidence**: anecdotal
- **Quote**: "There will be an explosion in the number of software developers. Software development is now essentially free, and tokens are cheaper than humans"
- **Our assessment**: The "tokens are cheaper than humans" framing is consistent with the economic-inversion argument in `blog-simonwillison-charity-majors-code-economics.md` (Claim 1: "the economics of code production were turned upside down... it became effectively free and instant"), though Majors frames the shift as being about code generation cost, while Huntley extends this specifically into a labor-market prediction (more developers, not just cheaper code). This is an extension of Majors' economic diagnosis into a headcount forecast that Majors' own note does not make.

### Claim 10: Not enough engineers understand what it means to be a "product engineer"

- **Evidence**: Bare assertion, tenth item in the list. No definition of "product engineer" is given in this post.
- **Confidence**: anecdotal
- **Quote**: "Not enough engineers know what it means to be a product engineer"
- **Our assessment**: This gestures at the same role-blurring theme as Claim 2/Claim 4 (engineer vs. coder) but introduces a third undefined term ("product engineer") without connecting it explicitly to the rest of the list. It is directionally consistent with Andrew Ng's claim in `blog-thebatch-ng-aiteam-structure.md` (Claim 3) that "the fastest-moving teams... tend to have engineers who know how to do some product work," and with Fiona Fung's hiring emphasis on "creative builders with product sense" in `blog-anthropic-ai-native-engineering-org.md` (Claim 9). Both of those sources define the concept in more operational detail than this post does; Huntley's point is asserted without elaboration.

### Claim 11: Engineers whose job is purely executing pre-defined tickets ("JIRA ticket monkeys") are now obsolete

- **Evidence**: Bare assertion, eleventh item in the list, phrased as a slang dismissal.
- **Confidence**: anecdotal
- **Quote**: "JIRA ticket monkeys are cooked"
- **Our assessment**: No definition of "JIRA ticket monkey" or supporting reasoning is given beyond the phrase itself. Read alongside Claim 10 (product engineer) and Claim 2 (coder vs. engineer), the implied argument is that pure ticket-execution is now within reach of AI tooling and no longer a viable standalone role — but the post does not make this connection explicit; we are inferring it from adjacency in the list, not from stated logic.

### Claim 12: If your employer has banned AI tools, you should quit

- **Evidence**: Bare assertion, twelfth item in the list.
- **Confidence**: anecdotal
- **Quote**: "If your company has banned AI, you should quit that company"
- **Our assessment**: Presented as unconditional career advice with no discussion of the reasons a company might restrict AI tools (e.g., the security/compliance concerns covered extensively elsewhere in the corpus, such as `blog-anthropic-zero-trust-ai-agents.md` or `blog-anthropic-compliance-api.md`). This is the most one-sided claim in the post — it does not engage with legitimate reasons for AI restrictions (regulated industries, client contractual requirements, unresolved data-handling risk) and should not be repeated in the guide without that caveat.

### Claim 13: AI tools are better understood as an instrument to be played through deliberate, intentional practice than as a tool to be picked up and immediately judged

- **Evidence**: Bare assertion in the main post's numbered list, substantially elaborated in a separate, directly-linked post (`ghuntley.com/play/`, "deliberate intentional practice," embedded as a bookmark card at the end of the numbered list).
- **Confidence**: anecdotal
- **Quote** (main post): "AI is more like a musical instrument than just a tool. Play with it, make discoveries, build intuition, learn where AI is good and where it fails"
- **Quote** (linked `/play/` post, elaborating the same point): "In the circles around me, the people who are getting the most out of AI have put in deliberate, intentional practice. They don't just pick up a guitar, experience failure, and then go, \"Well, it got the answer wildly wrong,\" and then move on and assume that that will be their repeated experience."
- **Our assessment**: This is the most developed idea in either post, and it directly supplies the missing mechanism behind Claim 5's curiosity claim: "curious" appears to specifically mean "willing to put in repeated, deliberate practice with AI tools rather than judging them off one bad result." The `/play/` post also raises a caveat not present in the Miami post: engineers whose only AI experience is inside "a large, proprietary codebase" with "extensive proprietary patterns that AI simply doesn't have the training data for" may reasonably conclude AI doesn't work for them in that context — a nuance that softens Claim 1's blanket framing. Both posts remain anecdotal: no measurement of what "deliberate practice" produces, only an assertion that it correlates with better outcomes among people "in the circles around me."

## Concrete Artifacts

### Full numbered list, verbatim (main post, `ghuntley.com/miami/`)

```
Source: Geoffrey Huntley, "A couple of months ago in Miami, I sat down and
dumped my brains. Here's the interview...", ghuntley.com, June 26, 2026.
Intro line: "Some personal hot takes from AI: Engineer Miami follows..."
Embedded video title: "Hot-takes at a fireside chat during AI:Engineer Miami"

1. Software development is a dead-end profession because anyone can be a
   software developer now.

2. Anyone can use Cursor or any other tool and generate code. Being a coder
   and being a software engineer are different.

3. Computers used to be gated; now everyone has the power to make computers
   malleable. Everyone is a software developer now, but that does not mean
   they are software engineers

4. If you cannot demonstrate how a coding agent works, you are just a
   consumer and have imposed an artificial glass ceiling on your career as
   a software engineer.

5. If you are curious, you will have a job. If you have not been curious in
   the last two years, you are replaceable.

6.  SaaS per-seat economics may become unstable as  customers need fewer
   people to achieve results, prompting founders to think about new unit
   economics

7. Most companies will take two or three years (or more!) to figure out AI
   transformation.

8. Some companies are already building AI native teams of five to ten
   people who can build with the grain of AI

9. There will be an explosion in the number of software developers.
   Software development is now essentially free, and tokens are cheaper
   than humans

10. Not enough engineers know what it means to be a product engineer

11. JIRA ticket monkeys are cooked

12. If your company has banned AI, you should quit that company

13. AI is more like a musical instrument than just a tool. Play with it,
    make discoveries, build intuition, learn where AI is good and where it
    fails
```

(Numbering and internal spacing — including the double spaces in point 6 —
are verbatim from the live page as of 2026-07-01.)

### Elaboration of point 13, verbatim (linked post, `ghuntley.com/play/`)

```
Source: Geoffrey Huntley, "deliberate intentional practice", ghuntley.com
(linked directly from the Miami post as a bookmark-card embed)

"Something I've been wondering about for a really long time is, essentially,
why do people say AI doesn't work for them? What do they mean when they say
that?"

"From which identity are they coming from? Are they coming from the
perspective of an engineer with a job title and sharing their experiences in
a particular company, in that particular codebase? Or are they coming from
the perspective that they've tried at home and it hasn't worked for them
there?"

"Now, this distinction is crucial because there are companies out there with
ancient code bases, and they've extensive proprietary patterns that AI
simply doesn't have the training data for. That experience is entirely
understandable."

"However, I do worry about engineers whose only experience with AI is using
it in a large, proprietary codebase. Have they tried AI at home? Are they
putting in deliberate, intentional practice? Have they discovered the beauty
of AI?"

"You see, there is a beauty in AI. And the way I like to describe it these
days, they are kind of like a musical instrument."

"Let's take a guitar as an example. Everyone knows what a guitar is, and
everyone knows that if you put deliberate, intentional practice into it, you
can become good at the guitar. Still, it takes time, effort and
experimentation."

"In the circles around me, the people who are getting the most out of AI
have put in deliberate, intentional practice. They don't just pick up a
guitar, experience failure, and then go, "Well, it got the answer wildly
wrong," and then move on and assume that that will be their repeated
experience."

"What they do is they play" [blockquote in original]
```

(This page is gated after this point by a "This post is for subscribers
only" paywall banner; the text above is everything accessible without a
subscription.)

## Cross-References

- **Corroborates**: `blog-thebatch-ng-aiteam-structure.md` (Claim 6) — Andrew
  Ng's "AI-native teams with around 2-10 persons" scoping overlaps with
  Claim 8 here ("five to ten people"). Both are anecdotal practitioner
  observations naming no specific companies; this is convergent intuition
  between two practitioners, not independently measured data.

- **Corroborates**: `blog-anthropic-ai-native-engineering-org.md` (Claim 9)
  — Fiona Fung's hiring philosophy ("What I index on less... is raw
  throughput; the models handle that") is consistent with Claim 4 here
  (demonstrating how a coding agent works, not just using it, is the
  differentiator) and Claim 2 (coder vs. engineer). Fung's account is a
  first-party, named organizational practice; Huntley's is an unelaborated
  personal assertion — the corroboration is directional, not equal in
  evidentiary weight.

- **Extends**: `blog-simonwillison-product-market-fit.md` (Claim 5) —
  Willison's note documents that Anthropic and OpenAI already shifted their
  own enterprise pricing away from flat/seat allocations toward direct API
  pricing (settled, sourced, company-specific). Claim 6 here speculates
  about a broader, unevidenced second-order effect: that AI-driven headcount
  reduction at *customer* companies could destabilize *SaaS vendors'*
  per-seat pricing generally. These are related but distinct economic
  claims — one is a confirmed fact about AI labs' own pricing; the other is
  an unconfirmed hypothesis about the wider SaaS market. No existing corpus
  note makes Huntley's specific customer-side hypothesis, so it extends
  rather than duplicates Willison's finding.

- **Extends**: `blog-simonwillison-charity-majors-code-economics.md` (Claim
  1) — Majors' claim that code generation became "effectively free and
  instant" in 2025 is the economic premise Claim 9 here extends into a labor-
  market prediction ("explosion in the number of software developers").
  Majors' note stops at the production-cost claim; Huntley's post is the
  first corpus source to extend it into a headcount forecast.

- **Contradicts**: None found requiring a contradiction filing. The post's
  claims are broad, unelaborated opinions rather than specific, falsifiable
  positions that clash with an existing source note's specific claim. The
  closest tension is internal to this source's own linked pages: Claim 1's
  blanket "dead-end profession" framing is softened by the `/play/` post's
  own caveat that engineers in large proprietary codebases with
  training-data-poor patterns may reasonably experience AI as not working —
  this is a self-qualification within Huntley's own writing, not a claim
  that materially opposes a claim in an existing source note, so it does not
  meet the bar in MINER.md §4a for filing a contradiction issue.

- **Novel**:
  - The specific claim that SaaS *vendor* per-seat pricing (as distinct from
    AI-lab API pricing) may become unstable because *customers* need fewer
    seats (Claim 6) is not present in any existing corpus note.
  - The "gated vs. malleable" framing for computing accessibility (Claim 3)
    is a new metaphor not used elsewhere in the corpus.
  - "JIRA ticket monkeys are cooked" (Claim 11) is a distinctly-phrased
    claim about the obsolescence of pure ticket-execution roles; no existing
    note uses this framing, though the underlying idea (mechanical execution
    roles are most exposed) is present elsewhere (e.g., the Zapier posting
    in `discussion-hn-agentic-coding-jobs.md`).
  - The "AI as musical instrument, played through deliberate practice" framing
    (Claim 13) is a new, reusable metaphor for the guide's discussion of how
    practitioners build AI intuition — no existing corpus note frames skill-
    building this way.

## Guide Impact

- **Chapter 01 (Daily Workflows — building AI intuition)**: Consider adding
  the "AI as musical instrument" framing (Claim 13) as a named metaphor for
  why one-shot judgments of AI tools ("it got the answer wildly wrong, so it
  doesn't work") are an unreliable basis for adoption decisions, contrasted
  with the "deliberate, intentional practice" pattern from the linked
  `/play/` post. Pair this with the `/play/` post's caveat about large
  proprietary codebases with training-data-poor patterns — this is a fairer,
  more complete version of the claim than the bare "musical instrument" line
  alone, since it acknowledges legitimate reasons AI may underperform in a
  given environment.

- **Chapter 05 (Team Adoption — team sizing)**: Claim 8 ("teams of five to
  ten people") can be cited as a second, convergent anecdotal data point
  alongside Andrew Ng's "2–10 persons" scoping in
  `blog-thebatch-ng-aiteam-structure.md`, but the guide should flag both as
  practitioner intuition rather than measured team-size optimization — no
  source in the corpus, including this one, provides a methodology for why
  a given team size is optimal.

- **Chapter 05 (Team Adoption — economics)**: Claim 6 (SaaS per-seat
  economics instability) is worth flagging as an open, unconfirmed
  hypothesis distinct from the settled AI-vendor pricing shift documented in
  `blog-simonwillison-product-market-fit.md`. If the guide discusses vendor
  pricing risk, it should keep these two claims separate: one is sourced and
  company-specific: (Willison); the other is speculative and industry-wide
  (Huntley).

- **Chapter 05 (Team Adoption — career framing)**: Claim 4 (agent-mechanism
  understanding as the coder/engineer differentiator) is a specific,
  quotable formulation the guide could pair with Fung's hiring-philosophy
  claim in `blog-anthropic-ai-native-engineering-org.md` (Claim 9) — but the
  guide should not present Claim 4 as a settled competency bar, since
  Huntley does not define what "demonstrate how a coding agent works" means
  in practice (no rubric, no test, no example).

- **Not recommended for inclusion without heavy caveats**: Claim 1 ("dead-end
  profession"), Claim 5 ("replaceable" if not curious), and Claim 12 (quit
  if AI is banned) are unqualified, one-sided assertions with no supporting
  argument in the source. If cited at all, the guide should attribute them
  explicitly as one practitioner's provocative framing, not as consensus or
  established fact — the source itself supplies no evidence for any of the
  three.

## Extraction Notes

- The source is a short, unstructured list of 13 one- or two-sentence "hot
  takes" — there is no argued essay to extract beyond the list itself. This
  note extracts each numbered point individually, which produces a claim
  count on the high end of typical for how little total text the post
  contains; several claims (e.g., 2, 3, 10, 11) are closely related
  restatements rather than fully independent arguments, and this is noted
  explicitly in each claim's "Our assessment" rather than papered over.
- Per MINER.md §1, one substantively linked page was followed: the bookmark-
  card embed at the end of the numbered list links directly to
  `ghuntley.com/play/`, which elaborates point 13 (the musical-instrument /
  deliberate-practice framing) at length. That page is paywalled after six
  paragraphs ("This post is for subscribers only"); all text quoted from it
  above is from the freely accessible portion only. A second-order link
  from within `/play/` (to `ghuntley.com/ngmi/`, an older Feb 2025 post about
  career risk from non-adoption) was checked but not extracted from in
  depth, since it is two hops from the submitted source URL and covers
  ground (career risk from not adopting AI tools) already represented by
  Claim 5 and Claim 12 in this note.
- Both pages were fetched directly via HTTP (not through a summarizing
  fetch tool) specifically so that all quotes above are verified
  character-for-character against the live HTML, including the verbatim
  double-spacing artifacts in point 6 of the main post.
- Cross-reference verification: all cited claim numbers were confirmed by
  re-reading the actual source notes before writing this note —
  `blog-thebatch-ng-aiteam-structure.md` Claim 6 (line 133: "In small
  AI-native teams (2–10 persons), generalists excel..."), Claim 3 (line 79:
  "the fastest-moving teams I see tend to have engineers who know how to do
  some product work") — verified; `blog-anthropic-ai-native-engineering-org.md`
  Claim 9 (line 82: "Hiring now prioritizes two profiles over raw
  throughput...") — verified; `blog-simonwillison-product-market-fit.md`
  Claim 5 (line 110: "Both Anthropic (Nov 2025) and OpenAI (Apr 2026) shifted
  enterprise pricing from flat/seat allocations to direct API pricing") —
  verified; `blog-simonwillison-charity-majors-code-economics.md` Claim 1
  (line 47: "In 2025, the economics of code production were turned upside
  down...") — verified.
- Confidence is set to `anecdotal` overall: every claim in the source is an
  unsupported personal assertion from a single practitioner at a fireside
  chat, with no data, named companies, or methodology behind any individual
  point. This is consistent with the Prospector's own triage assessment
  ("Claims are stated as hot takes / opinions rather than evidence-backed
  studies").
