---
source_url: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-ama
source_type: blog-post
title: "The Pragmatic Engineer AMA"
author: Gergely Orosz (The Pragmatic Engineer), with Volodymyr Giginiak (CTO, Wordsmith AI) reading subscriber questions
date_published: 2026-07-08
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: anecdotal
issue: "#1708"
---

# The Pragmatic Engineer AMA

> A podcast/video AMA episode's written companion page: three personal "origin story"
> narratives and three named "opinions of the week" from Gergely Orosz, touching on why
> LeetCode-style interviews persist, why MCP's adoption window has closed, and a
> self-diagnostic framing for AI-driven skill atrophy — while the episode's actual
> subscriber Q&A (on AI-native SDLC, hiring, engineering-manager types, tech debt, and
> career future-proofing) exists only as untranscribed audio/video, not as page text.

## Source Context

- **Type**: blog-post (podcast/video AMA episode show-notes page; The Pragmatic Engineer
  newsletter, Substack; published July 8, 2026)
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager and author of The
  Pragmatic Engineer, described elsewhere in this corpus as a ~750k+ subscriber engineering
  newsletter (see `survey-pragmaticengineer-ai-tooling-2026.md`,
  `blog-pragmaticengineer-neetcode-interview.md`). This episode is a subscriber-question AMA
  ("Ask Me Anything") with Volodymyr Giginiak (CTO of Wordsmith AI) reading questions aloud;
  the written page is Orosz's own first-person text, not a third party's summary.
- **Scope**: The episode runs roughly 78 minutes (per its final timestamp, 1:17:13) and its
  timestamped topic outline names 21 segments including "AI-native SDLC" (09:22), "AI and
  hiring" (14:00), "Types of engineering managers" (41:36), "Measuring AI productivity"
  (44:40), and "Future-proofing your career" (56:09) — precisely the topics the Prospector's
  triage flagged as relevant to Ch02–Ch04. None of that Q&A content is available as page text:
  the written page contains only (1) three "origin story" narratives about the newsletter's
  own history, (2) three named "opinions of the week," and (3) the bare timestamp list with no
  transcript body. This note is built entirely from that accessible written text, verified
  against the raw page HTML. See Extraction Notes for full detail on what could not be
  extracted.

## Extracted Claims

### Claim 1: LeetCode-style technical interviews persist industry-wide, in Orosz's view, because grinding to prepare for them selects for candidates who tolerate corporate busywork, not because the skills tested predict job performance
- **Evidence**: Orosz's own stated opinion, labeled "Opinion #1" in the article — his personal editorial view as newsletter author, not a survey or measured dataset.
- **Confidence**: anecdotal (one author's opinion, not backed by data or a cited study in this source)
- **Quote**: "a candidate who's willing to grind for weeks or months to prepare for an interview which bears little resemblance to the job, is likely to be someone who understands that sometimes it's necessary to do pointless work"
- **Our assessment**: This is a specific causal mechanism (grinding-as-corporate-tolerance-signal) rather than a vague "interviews are broken" complaint. It proposes a *different* mechanism than the one already in the corpus from NeetCode (`blog-pragmaticengineer-neetcode-interview.md` Claim 1: interviews persist because the format scales to training thousands of interviewers). The two are not contradictory — a hiring practice can persist for more than one reason simultaneously — but they are genuinely different proposed explanations from two people at the same publication within two weeks of each other, worth citing together rather than treating either as the single explanation.

### Claim 2: AI tools now solve LeetCode-style data-structures-and-algorithms puzzles easily enough that Orosz expects larger companies to shift back toward in-person interviewing while still keeping DSA-style questions
- **Evidence**: Orosz's own stated opinion, same "Opinion #1" section.
- **Confidence**: anecdotal (a specific, falsifiable prediction, but the author's own forecast, not a reported company policy in this source)
- **Quote**: "AI solves the puzzles with ease these days, and I expect larger companies to move back to in-person interviewing – all while keeping DSA interview questions."
- **Our assessment**: This is a prediction, not a report of a company decision — contrast with `blog-pragmaticengineer-neetcode-interview.md` Claim 2, which reports (secondhand, via NeetCode) that Google has *already* reinstated onsite whiteboard interviews specifically to counter AI-assisted cheating. Read together, the two sources corroborate the same directional trend (AI-solvable DSA puzzles pushing hiring back toward in-person, harder-to-automate formats): one names a specific company that has already acted, this one is the author's own forward-looking generalization about "larger companies."

### Claim 3: MCP achieved industry-standard adoption partly because of a timing window — when it launched in November 2024, Anthropic was not yet perceived as the leading AI lab, which reduced other companies' fear of lock-in to a dominant competitor's protocol
- **Evidence**: Orosz's own stated opinion, labeled "Opinion #2" in the article.
- **Confidence**: anecdotal (one author's causal explanation for an industry-adoption pattern, not data on actual adopter motivations)
- **Quote**: "When MCP launched in November 2024, Anthropic wasn't yet considered the leading AI lab."
- **Our assessment**: This is a specific, checkable-in-principle timing claim (MCP's November 2024 launch date, and a claim about market perception at that date) rather than a vague "MCP won because it's a good protocol" story. Orosz's framing implies the headline claim — "it couldn't pull this off today" — meaning a hypothetical dominant-lab-launched protocol today would face more lock-in resistance (he draws an explicit comparison to resistance faced by Google's Agent2Agent protocol, per the WebFetch summary of this section, though that comparison sentence itself was not independently verified against raw HTML for this note and so is not quoted directly). This is genuinely novel to the corpus: no existing source note offers a "why did MCP specifically win adoption" explanation tied to competitive-trust timing rather than technical merit.

### Claim 4: Orosz deliberately avoids using AI tools in his own writing (keeping Grammarly turned off too) to prevent his writing skill from degrading, while consciously accepting that his hand-coding ability will degrade because he does use AI for coding — treating this as a deliberate, skill-by-skill tradeoff rather than an all-or-nothing choice
- **Evidence**: Orosz's own stated personal practice, in the "AI at Pragmatic Engineer" / career-advice portion of the article's free text.
- **Confidence**: anecdotal (a single individual's self-reported personal workflow choice)
- **Quote**: "I don't want my writing skill to degrade, and would like to keep improving. On the other hand, with coding, I do use AI and accept my hand-coding ability will unavoidably degrade."
- **Our assessment**: This corroborates `research-anthropic-ai-transforming-work.md` Claim 8 ("Engineers explicitly identify skill atrophy and supervision-paradox risks," quoting an interviewee: "When producing output is so easy and fast, it gets harder to actually take time to learn something") — both sources treat AI-driven skill atrophy as a real, named risk rather than a hypothetical one. What this source adds that the interview-study claim doesn't: an explicit worked example of *choosing* which skills to protect (writing, which the author values and actively practices) versus which to knowingly let degrade (hand-coding, which he treats as an acceptable tradeoff) — a skill-by-skill triage framing, not a blanket "avoid AI" or "embrace AI" position.

### Claim 5: Orosz frames unusual ease from using AI as a potential warning sign rather than a pure win — proposing that if AI is making work noticeably easier, that may indicate the person isn't pushing themselves hard enough
- **Evidence**: Orosz's own stated view, immediately following Claim 4 in the same section.
- **Confidence**: anecdotal (a personal heuristic/framing, not a measured claim)
- **Quote**: "If you're using AI and life seems to be getting a lot easier, it raises the question: are you trying hard enough?"
- **Our assessment**: This is a specific, self-diagnostic framing — not simply "watch out for skill atrophy," but a concrete question a reader could ask themselves. It pairs with Claim 4's skill-by-skill triage as a practical individual heuristic. Because it's phrased as a rhetorical question rather than a rule, it's better cited as a prompt for reflection than as an actionable policy for a guide chapter.

### Claim 6: Orosz adopted an editorial policy of writing about "what works inside companies" rather than "what seems to be broken," after a message from an engineer credited a company (Bunq) he was about to publish a critical piece on for sponsoring their visa
- **Evidence**: Orosz's own account of a specific incident from early in the newsletter's history (Story #2 of the article's three origin stories).
- **Confidence**: anecdotal (single self-reported incident and resulting policy change)
- **Quote**: "I write about what works inside companies, instead of focusing on what seems to be broken."
- **Our assessment**: Not directly about AI-native engineering, but relevant background for weighing the credibility and editorial stance of a frequently-cited corpus author: The Pragmatic Engineer's own stated policy is to favor positive/functional case studies over critical exposés (with the Pollen investigation below being an explicit, self-acknowledged exception). Guide-relevant only as a caveat when citing Orosz's company case studies elsewhere in the corpus (e.g. the Uber, Anthropic, OpenAI, Cursor material in `blog-pragmaticengineer-orosz-slow-down-speed-up.md` and `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`) — those pieces should be read with the awareness that the author's own stated default is to write about what works, which could bias case-study selection toward success stories.

## Concrete Artifacts

```
Full timestamp outline (verbatim topic headers, from the article's show notes —
no transcript body accompanies any of these; each is a bare timestamp + title):

00:00 Intro
01:56 From Uber to writing
09:22 AI-native SDLC
14:00 AI and hiring
19:06 Engineers currently thriving
22:18 Junior roles
24:44 Meta's war mode
27:54 AI at Big Tech vs. startups
36:46 Tech debt
41:36 Types of engineering managers
44:40 Measuring AI productivity
48:30 The value of CS degrees
50:53 AI at Pragmatic Engineer
56:09 Future-proofing your career
1:01:36 The EU job market
1:03:55 Making money as a creator
1:08:20 What's next for The Pragmatic Engineer
1:09:27 Bunq and Pollen
1:13:38 Spotting trends
1:14:33 Book updates
1:15:20 Favorite books & tech products
1:17:13 What won't change in engineering

Source: newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-ama
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-neetcode-interview.md` Claim 2 (Google reinstated onsite
    whiteboard interviews specifically because AI-powered cheating tools make DSA interviews
    easy to pass): Claim 2 here (Orosz predicting a broader industry shift back to in-person
    interviewing because "AI solves the puzzles with ease") is the same directional trend
    stated as a general forecast rather than one company's already-completed policy change.
  - `research-anthropic-ai-transforming-work.md` Claim 8 (engineers explicitly identify skill
    atrophy as a risk, quoting "When producing output is so easy and fast, it gets harder to
    actually take time to learn something"): Claim 4 here is a second, independent voice
    naming the same risk and describing a concrete personal mitigation (protect the skills you
    value, accept degradation in the ones you don't).

- **Contradicts**: None found requiring a filed contradiction issue per MINER.md §4a. Claim 1
  here (LeetCode interviews persist as a corporate-tolerance filter) and
  `blog-pragmaticengineer-neetcode-interview.md` Claim 1 (interviews persist because the
  format scales to training many interviewers) propose different mechanisms for the same
  observed persistence, but both could be true simultaneously and neither source frames the
  other as wrong — this is two complementary explanations, not a genuine disagreement, so no
  contradiction issue was filed.

- **Extends**: `blog-pragmaticengineer-neetcode-interview.md` (hiring/interview-process
  commentary from the same publication) and `research-anthropic-ai-transforming-work.md`
  (skill-atrophy risk) both gain a second, differently-sourced data point from this AMA's
  opinions.

- **Novel**: The MCP-adoption-timing explanation (Claim 3 — Anthropic's not-yet-dominant
  status at MCP's November 2024 launch as a precondition for its industry-standard adoption)
  is not documented anywhere else in the corpus; no existing source note offers a "why did
  MCP specifically win" explanation tied to competitive trust rather than technical design.
  The explicit skill-by-skill triage framing in Claim 4 (protect writing, accept coding
  degradation) is also a new, concrete individual-practice pattern not present in the
  corpus's existing skill-atrophy source (`research-anthropic-ai-transforming-work.md`,
  which documents the *risk* being named by interview subjects but not a worked example of
  someone's chosen mitigation).

## Guide Impact

- **Chapter 04 (Hiring/Careers)**: Add Claim 1 (grinding-as-corporate-tolerance-signal) as a
  second, distinct proposed explanation for LeetCode-style interview persistence, to be cited
  alongside NeetCode's scaling-based explanation (`blog-pragmaticengineer-neetcode-interview.md`
  Claim 1) rather than in place of it — the guide should present both mechanisms rather than
  picking one, since neither source treats them as mutually exclusive.
- **Chapter 04 (Hiring/Careers)**: Add Claim 2 as a second, forward-looking data point (this
  time a prediction rather than a completed policy change) supporting the guide's existing
  claim that AI-solvable DSA puzzles are pushing companies back toward in-person interviewing —
  pair with the already-cited Google example for a "one company has already acted, and an
  industry observer expects more to follow" framing.
- **Chapter 02/03 (Individual Workflows)**: Add Claim 4 and Claim 5 as a concrete individual
  practice for managing AI-driven skill atrophy — deliberately choosing which skills to
  protect from AI assistance versus which to let degrade, plus a self-diagnostic question
  ("is this getting easier because I'm not trying hard enough?"). This is a specific,
  actionable individual heuristic distinct from the corpus's existing, more abstract skill-
  atrophy risk documentation in `research-anthropic-ai-transforming-work.md`.
- **No chapter currently covers MCP's adoption-timing dynamics**: If the guide ever discusses
  why MCP specifically became the dominant agent-tool protocol (as opposed to a general
  "MCP is the standard" statement), Claim 3 is the only corpus source offering a causal theory
  beyond technical merit — flag it explicitly as one author's opinion, not a documented
  decision-making account from adopting companies.

## Extraction Notes

- **The episode's actual subscriber Q&A is not accessible as text.** This is the central
  limitation of this extraction. The article's show-notes page lists 21 timestamped topics
  (see Concrete Artifacts) covering exactly the material the Prospector's triage comments
  flagged as most relevant — "AI-native SDLC," "AI and hiring," "Measuring AI productivity,"
  "Types of engineering managers," "Future-proofing your career" — but none of that content
  exists as page text. The page states "See the episode transcript at the top of this page,"
  but no transcript text follows that heading anywhere in the raw page HTML; the Q&A itself
  is delivered only via the embedded YouTube/Spotify/Apple Podcasts audio/video. This matches
  the same limitation documented in `blog-pragmaticengineer-neetcode-interview.md`'s
  Extraction Notes for a different Pragmatic Engineer podcast episode.
- **What was extractable**: the article's introduction, three "origin story" narratives (the
  newsletter's founding, the Bunq editorial-policy incident, the Pollen investigation), three
  named "opinions of the week" (LeetCode interviews, MCP adoption timing, AI skill atrophy),
  and the bare 21-entry timestamp list. This is the full extent of the page's text content —
  no paywall was encountered; this is simply all the written material the page offers.
- **Verification method**: The page was fetched via WebFetch three times (each pass returned a
  paraphrased summary rather than verbatim text, consistent with the WebFetch quote-drift risk
  flagged in `blog-pragmaticengineer-orosz-slow-down-speed-up.md` and
  `blog-pragmaticengineer-neetcode-interview.md`'s Extraction Notes), then the raw page HTML was
  fetched directly via `curl` and parsed locally. Every quote in this note was verified
  character-for-character against that raw HTML, not against any WebFetch summary.
- **One unverified detail flagged and excluded from quotes**: an early WebFetch pass mentioned
  Orosz drawing a comparison between MCP's adoption and resistance faced by "Google's
  Agent2Agent protocol" in the same Opinion #2 section. This detail is plausible and consistent
  with the rest of Claim 3, but was not independently re-confirmed against the raw HTML for
  this note, so it is mentioned only as unverified context in Claim 3's assessment and is not
  presented as a direct quote.
- **Thin source relative to episode length**: Given the ~78-minute episode length and the
  Prospector's specific interest in hiring/adoption/workflow content, this note extracts
  meaningfully fewer claims (6) than the corpus's per-source target of 5-15, because the
  overwhelming majority of the episode's substantive content (the Q&A itself) is not available
  as text. This should not be read as a shallow read of the *available* material — the
  accessible text (introduction, three stories, three opinions, timestamp list) was read in
  full, cross-checked against raw HTML, and is fully represented in the claims above.
