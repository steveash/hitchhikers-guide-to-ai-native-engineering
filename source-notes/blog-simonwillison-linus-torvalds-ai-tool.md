---
source_url: https://simonwillison.net/2026/Jul/16/linus-torvalds/
source_type: blog-post
title: "Quoting Linus Torvalds"
author: Simon Willison (link-blog curation); quoted subject Linus Torvalds (Linux kernel creator and top-level maintainer)
date_published: 2026-07-16
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: anecdotal
issue: "#2058"
---

# Quoting Linus Torvalds

> Simon Willison's link-blog "quotation" post relays a Linux Media Mailing List message
> in which Linus Torvalds, as top-level Linux kernel maintainer, declares Linux is "not
> one of those anti-AI projects," frames continued objection as an individual's problem
> to solve by forking or leaving, and states that "is it useful" is a settled question
> about AI as of mid-2026 — directly at odds with the Zig Software Foundation's
> published anti-LLM contribution ban.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog "quotation" post format — a short
  attributed excerpt with minimal Willison commentary; the post consists almost
  entirely of the Torvalds quote itself, framed as a standalone quotation entry, not
  an essay)
- **Author credibility**: The quote is attributed directly to Linus Torvalds, creator
  of Linux and Git, and the Linux kernel's top-level maintainer — one of the most
  consequential decision-makers in open-source software governance. The quote is
  sourced to a message on the Linux Media Mailing List (linked by Willison to
  `lore.kernel.org`, the canonical kernel mailing-list archive), which is Torvalds'
  normal venue for maintainer rulings on kernel development policy. Willison's own
  role here is pure curation — he is a `trusted-feed` source in this repo, but the
  substantive authority is Torvalds', not Willison's.
- **Scope**: Covers only Torvalds' stated personal/maintainer position that Linux
  will not be an "anti-AI project" and his framing of AI as a settled-useful tool.
  Does NOT cover: any specific kernel policy on AI-generated patch submissions,
  attribution requirements for AI-assisted contributions, sign-off/DCO handling for
  AI-authored commits, or any discussion of *how* AI tools are or aren't used in
  kernel development in practice. The quote is a broad philosophical/governance
  stance, not a technical contribution policy document (contrast with Zig's CoC,
  which is a specific contribution-channel ban — see Cross-References).

## Extracted Claims

### Claim 1: Torvalds asserts unilateral, non-negotiable authority as "the top-level maintainer" to settle the question of whether Linux tolerates AI

- **Evidence**: Direct quote, first sentence of the message.
- **Confidence**: anecdotal (single first-person maintainer statement, but Torvalds'
  authority over kernel governance is not in dispute — he has held this role since
  Linux's founding)
- **Quote**: "I realize that some people really dislike AI, but this is an area where I'm willing to absolutely put my foot down as the top-level maintainer."
- **Our assessment**: This is a governance-power move, not an argument. Torvalds is
  explicit that he is not building consensus — he is exercising the authority
  structure of kernel maintainership to foreclose the debate. This is a useful data
  point for the guide's discussion of how large OSS projects actually resolve
  contentious tooling questions: not always by community vote or RFC process, but
  sometimes by BDFL-style fiat from whoever holds top-level maintainer status.

### Claim 2: Torvalds explicitly positions Linux as not one of the "anti-AI projects" — implying such projects exist and are a known category

- **Evidence**: Direct quote, second sentence.
- **Confidence**: anecdotal
- **Quote**: "Linux is not one of those anti-AI projects, and if somebody has issues with that, they can do the open-source thing and fork it."
- **Our assessment**: The phrase "one of those anti-AI projects" treats anti-AI OSS
  policy as an established, nameable category by mid-2026 — consistent with this
  corpus's own documentation of Zig's explicit anti-LLM Code of Conduct
  (`blog-simonwillison-zig-anti-ai.md`). Torvalds does not name Zig or any other
  project, but the existence of the category is presupposed rather than argued for.
  This is corpus-relevant evidence that OSS AI-adoption policy has bifurcated into
  recognizable camps by this point, not that every project is still deciding.

### Claim 3: Torvalds frames "fork it or walk away" as the correct open-source mechanism for resolving disagreement with his AI policy, rather than continued in-project debate

- **Evidence**: Direct quote, continuing the same sentence and the next.
- **Confidence**: anecdotal
- **Quote**: "if somebody has issues with that, they can do the open-source thing and fork it. Or just walk away."
- **Our assessment**: This is a specific and citable articulation of a governance
  principle: in a BDFL-style project, dissent over a foundational policy decision is
  not resolved by escalation or persuasion — it is resolved by the dissenter either
  forking the codebase (rare and costly for something as large as the Linux kernel)
  or exiting the community. This is a harder-line version of open-source's
  "exit over voice" governance option than most adoption-policy discussions in this
  corpus have documented. It also sets a high bar for anyone hoping to change the
  policy through argument.

### Claim 4: Torvalds asserts AI is categorically "just" a tool like other tools already in use, not a special case requiring separate governance treatment

- **Evidence**: Direct quote.
- **Confidence**: anecdotal (a normative framing claim, not an empirical one)
- **Quote**: "AI is a tool, just like other tools we use. And it's clearly a useful one."
- **Our assessment**: This "AI is just a tool" framing is a recurring rhetorical move
  across pro-adoption sources in this corpus (compare the general "why fight the
  tool" framing implicit in enterprise adoption case studies such as
  `blog-openai-bbva-banking-transformation.md` and `blog-cursor-nab-legacy-migration.md`).
  It is doing real argumentative work here: by categorizing AI with "other tools,"
  Torvalds forecloses arguments that AI-generated contributions deserve a distinct
  governance category (the exact opposite of Zig's stance, which treats LLM
  authorship as categorically different from any other tool-assisted contribution
  regardless of output quality — see Cross-References, Contradicts).

### Claim 5: Torvalds explicitly marks a change over time — AI's usefulness was not "clearly" true even a year prior, but is no longer in question as of mid-2026

- **Evidence**: Direct quote.
- **Confidence**: anecdotal (single individual's retrospective judgment, not a
  measured trend)
- **Quote**: "It may not have been that \"clearly\" even just a year ago, but it's no longer in question today."
- **Our assessment**: This is a dated claim from a specific, credible technical
  authority that AI coding/tooling utility crossed a legibility threshold sometime in
  the roughly 2025-to-2026 window, in his own assessment. It is not a measurement,
  but it is a useful anecdotal marker for the guide's narrative of when "is AI useful
  for engineering" stopped being a live question for skeptical, technically rigorous
  audiences. Worth pairing with harder evidence elsewhere in the corpus rather than
  citing standalone.

### Claim 6: Torvalds separates "is AI useful" (settled, in his view) from "what will AI's economics look like" (still open)

- **Evidence**: Direct quote.
- **Confidence**: anecdotal
- **Quote**: "There are other questions around AI (like what the economy of it will actually look like in the end), but \"is it useful\" is no longer one of those questions."
- **Our assessment**: This is a useful analytical move for the guide to reuse:
  separating the *utility* question from the *economics* question lets a source be
  simultaneously pro-adoption and agnostic-to-skeptical about AI business models,
  compute costs, or vendor sustainability. It is consistent with plenty of this
  corpus's other content (e.g., cost-anxiety material in
  `blog-fowler-fragments-2026-07-06.md`) which treats AI's usefulness as given while
  still treating token economics as an open and anxious topic.

### Claim 7: Torvalds asserts that anyone who still doubts AI's usefulness has not actually used it

- **Evidence**: Direct quote, closing line of the substantive part of the message.
- **Confidence**: anecdotal (an ad hominem-adjacent rhetorical closer, not evidence)
- **Quote**: "Anybody who doubts that clearly hasn't actually used it."
- **Our assessment**: This is the most dismissive line in the quote and is worth
  flagging as rhetoric rather than argument — it forecloses the possibility of an
  informed skeptic. For the guide, this is useful as an example of how pro-adoption
  rhetoric can slide into dismissiveness toward critics, which is the mirror image of
  the anti-AI "communities of not" tribal dynamics documented in
  `blog-ronacher-communities-of-not.md` (Claim 2: mobilizing collective punishment
  against position-changers). Both camps, per this corpus, contain leadership figures
  willing to treat the opposing view as not worth engaging on the merits.

## Concrete Artifacts

### Full quoted message (Linux Media Mailing List, via Willison's post)

```
Source: Linus Torvalds, Linux Media Mailing List, quoted in full by Simon
Willison at https://simonwillison.net/2026/Jul/16/linus-torvalds/
(posted 16th July 2026 at 1:26pm; original at
https://lore.kernel.org/linux-media/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com/)

I realize that some people really dislike AI, but this is an area where
I'm willing to absolutely put my foot down as the top-level maintainer.

Linux is not one of those anti-AI projects, and if somebody has issues
with that, they can do the open-source thing and fork it.

Or just walk away.

AI is a tool, just like other tools we use.  And it's clearly a useful
one.

It may not have been that "clearly" even just a year ago, but it's no
longer in question today.

There are other questions around AI (like what the economy of it will
actually look like in the end), but "is it useful" is no longer one of
those questions. Anybody who doubts that clearly hasn't actually used it.
```

## Cross-References

- **Contradicts**: `blog-simonwillison-zig-anti-ai.md` (Claims 1–5, 9, 11) — filed as
  contradiction issue [#2078](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2078).
  Zig's Code of Conduct imposes a comprehensive, ratified ban on LLM-generated
  content in issues, PRs, and bug-tracker comments, defended by ZSF VP of Community
  Loris Cro as game-theoretically rational regardless of code quality ("contributor
  poker"). Torvalds' statement takes the opposite institutional stance for Linux:
  AI use is settled-acceptable, treating it as "just" a tool, and dissenters are told
  to fork or leave rather than be accommodated by policy carve-outs. Both are
  top-level, on-the-record leadership statements from major foundational OSS
  infrastructure projects. The scope is not identical (Torvalds' statement is a
  broad philosophical stance; Zig's is a specific contribution-channel ban), which is
  exactly why this is filed as `debated` rather than a clean either/or — see the
  filed issue for the full framing. Do not resolve the verdict in this note; the
  issue tracks that decision.

- **Corroborates**: `blog-openai-bbva-banking-transformation.md` and
  `blog-cursor-nab-legacy-migration.md` — both document large, credible
  institutions (BBVA, a Fortune-Global-500 bank; NAB, a Fortune-500 bank) treating AI
  tool adoption as a settled strategic direction driven by leadership, not a live
  debate at the point of the case study. Torvalds' statement is the first corpus
  source to document this same "leadership settles the adoption question" dynamic
  inside a volunteer open-source governance structure rather than a corporate
  hierarchy — a different power structure reaching a structurally similar outcome
  (top-down, non-negotiable direction-setting).

- **Extends**: `blog-ronacher-communities-of-not.md` — Ronacher documents
  LLM-skeptical developer communities mobilizing tribal punishment against
  developers who change their AI stance (Claim 2), and argues legitimate resistance
  exists but shouldn't justify mob dynamics (Claim 5). Torvalds' post is a live
  instance of a maintainer publicly and pre-emptively closing off exactly the kind of
  in-project argument Ronacher describes — except from the pro-AI side, using
  maintainer authority rather than social pressure. The guide can use these two
  sources together to show that both "anti-AI" and "pro-AI" camps contain leadership
  voices willing to end debate by fiat/dismissal rather than engagement.

- **Novel**: This is the first source in the corpus documenting an explicit,
  attributed AI-adoption policy stance from the top-level maintainer of the Linux
  kernel specifically — the largest and most consequential piece of collaboratively
  maintained infrastructure software in existence. No existing note addresses kernel
  or Linux Foundation-level AI governance. The "fork it or walk away" framing as the
  correct dispute-resolution mechanism for a foundational tooling-policy
  disagreement is also new to the corpus — prior OSS-governance sources
  (Zig/contributor-poker) frame the ban as a considered institutional policy, not an
  individual maintainer's foreclosure of debate.

## Guide Impact

- **Chapter 02 (Industry adoption patterns)**: Add Torvalds' statement as evidence
  that AI-adoption legitimacy questions have reached the top of even the most
  conservative, technically rigorous corners of open source (the Linux kernel).
  Pair explicitly with the Zig contradiction (issue #2078) rather than presenting
  Torvalds' view as the settled consensus of OSS leadership — the guide should show
  both positions and flag that this is a live, unresolved split among credible
  maintainers, not cite Torvalds alone as proof AI adoption in OSS is uncontested.

- **Chapter 05 (Team Adoption / organizational legitimacy)**: Use Claim 1 and
  Claim 3 (unilateral maintainer authority; "fork it or walk away") as a case study
  in how governance structure shapes how AI-adoption disputes actually get resolved
  in practice — sometimes not through argument or evidence but through whoever holds
  decision-making authority exercising it. Contrast with BBVA/NAB's more
  process-driven ("trust, governance, structured learning") corporate adoption
  frameworks, which invest much more visible process in bringing skeptics along
  rather than telling them to leave.

- **Chapter 02 or 05, "handling skeptics" framing**: Claim 7 (dismissive framing of
  doubters) should be flagged as a rhetorical pattern to avoid recommending, even
  while citing the substantive claim (AI utility is broadly no longer contested
  among rigorous practitioners) as useful evidence. Pair with
  `blog-ronacher-communities-of-not.md` to show the guide takes a symmetric stance:
  dismissiveness and mob tribalism are both discouraged regardless of which side
  they come from.

## Extraction Notes

- The primary source (Willison's blog post) was fetched directly via `curl` and
  parsed from raw HTML; all quotes above are verbatim from that fetch.
- The post links to the original message on `lore.kernel.org`
  (`linux-media` mailing list archive). That page was attempted twice (via `curl`
  and via WebFetch) and both times returned an Anubis anti-bot proof-of-work
  challenge page (HTTP 403, "Making sure you're not a bot!") rather than the actual
  mailing-list content. The original could not be read directly; this note relies
  entirely on Willison's blog post, which reproduces the quote in full as a
  blockquote and is itself the `source_url` designated in the triaged issue. No
  discrepancy between the two is suspected — Willison's site has a strong track
  record in this corpus of verbatim quotation — but the Assayer should note that the
  primary mailing-list post itself was not independently verified due to the
  bot-wall.
- The source is extremely short (a single short paragraph-per-line quotation with
  almost no surrounding Willison commentary), so claim count is lower than the
  5–15 target range suggested in MINER.md; all substantive sentences in the quote
  have been extracted as individual claims, and Claims 1–7 exhaust the quoted text.
  This reflects the source's actual length, not incomplete reading.
- Confidence rated `anecdotal` overall: this is a single quotation from a single
  individual, however authoritative, with no accompanying kernel policy document,
  mailing-list thread discussion, or corroborating maintainer statements fetched or
  reviewed.
- Filed contradiction issue #2078 against `blog-simonwillison-zig-anti-ai.md` per
  MINER.md §4a before writing this note. No verdict is asserted here; see the issue.
