---
source_url: https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/
source_type: blog-post
title: "Reverse-engineering is cheap now"
author: Simon Willison
date_published: 2026-07-20
date_extracted: 2026-07-26
last_checked: 2026-07-26
status: current
confidence_overall: anecdotal
issue: "#2240"
---

# Reverse-Engineering Is Cheap Now

> Willison argues that coding agents shift the ROI calculus for reverse-engineering
> undocumented home-device APIs: not by removing the maintenance risk, but by making
> the initial effort and the cost of failed attempts cheap enough that the future
> maintenance burden (including discarding the work and starting over) carries
> much less psychological weight than it used to.

## Source Context

- **Type**: blog-post (a short-form "note" on Willison's link-blog, not a full
  entry — the page itself is labeled "This is a note by Simon Willison." The
  entire substantive content is four paragraphs; there are no embedded links to
  external anecdotes, case studies, or the "people" Willison references, and no
  sub-pages to follow.)
- **Author credibility**: Simon Willison is the creator of Django and one of the
  highest-signal independent commentators on practical LLM/agentic tooling; he is
  already a heavily cited source in this corpus (dozens of existing source notes).
  This particular post is not a report of his own experiment — it is a reflective
  observation prompted by secondhand anecdotes ("I keep hearing anecdotes from
  people who used coding agents..."). He does not name the people, the devices,
  or the automations involved.
- **Scope**: Covers a single, narrow economic observation: how coding agents
  change the ROI calculation for reverse-engineering undocumented, unstable APIs
  on personal home devices. Does NOT cover: specific tools, specific devices,
  concrete before/after cost figures, or professional/production software
  maintenance economics. Willison explicitly frames this as an "illustration"
  of a broader pattern (the reduced cost of writing code), not a study.

## Extracted Claims

### Claim 1: People are increasingly using coding agents to reverse-engineer and automate home devices
- **Evidence**: Author's secondhand anecdotal observation ("I keep hearing
  anecdotes from people who used coding agents..."); no named individuals,
  devices, or specific automations are given.
- **Confidence**: anecdotal
- **Quote**: "I keep hearing anecdotes from people who used coding agents to reverse-engineer and automate devices in their homes."
- **Our assessment**: This is the weakest-evidenced claim in the post — it is a
  vague trend observation with zero named examples, dates, or verifiable
  instances. It functions as the premise for the economic argument that follows
  (Claims 2-4), not as a standalone finding. Treat as color/context, not as
  evidence of scale or prevalence.

### Claim 2: Prior to coding agents, reverse-engineering home devices was technically possible but usually not worth the ROI, because undocumented APIs are unstable and create a future maintenance burden
- **Evidence**: Author's own reasoning about pre-agent cost/benefit tradeoffs,
  presented as a general truth about experienced programmers' judgment.
- **Confidence**: anecdotal
- **Quote**: "Prior to agents, it was entirely possible to reverse-engineer home devices. The problem was the ROI - was it really worth all of that effort? More importantly, any experienced programmer knows that undocumented, unstable APIs like that may well change or break in the future. Is that initial work worth the effort if you're committing yourself to a frustrating cycle of maintenance in the future?"
- **Our assessment**: This is a plausible, widely-shared engineering intuition
  (undocumented/reverse-engineered integrations are fragile) rather than a
  documented case. It sets up the "before" state for the argument: the barrier
  wasn't technical feasibility, it was a rational unwillingness to take on
  open-ended maintenance risk for uncertain future benefit.

### Claim 3: Coding agents lower both the effort required to build a working automation and the cost of a failed attempt
- **Evidence**: Author's direct assertion, no measurement or example given.
- **Confidence**: anecdotal
- **Quote**: "Coding agents change that equation entirely. The effort to get a simple automation working has dropped, as has the cost of trying and failing to get it to work."
- **Our assessment**: This is consistent with the broader corpus claim that
  code generation cost has collapsed (see Cross-References), but Willison
  supplies no quantification here — no time-to-working-automation figures, no
  before/after comparison. The claim is directionally credible given corpus
  corroboration but should not be cited as an independently measured result.

### Claim 4: Because the code itself is now cheap, the prospect of having to maintain it later — or discard it and start over — carries much less psychological weight than it used to
- **Evidence**: Author's concluding inference, framed as the practical
  consequence of Claim 3.
- **Confidence**: anecdotal
- **Quote**: "Since the code is so cheap, the idea of having to maintain it in the future - or throw it away and start again - carries way less psychological baggage."
- **Our assessment**: This is the post's central, most citable claim, but it is
  explicitly about *psychological* cost (the practitioner's willingness to
  start a project despite an uncertain future), not about actual maintenance
  economics. It should not be read as a claim that maintenance costs
  themselves have gone down — only that the up-front decision to accept future
  maintenance risk (or the option of discarding the work entirely) is now an
  easier one to make for low-stakes, personal, single-owner projects. See
  Cross-References for why this framing does not extend to production
  software maintained by a team.

## Concrete Artifacts

```
Full text of the post (verbatim, https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/,
posted 20th July 2026 at 7:24pm; confirmed via direct HTML fetch):

"I keep hearing anecdotes from people who used coding agents to reverse-engineer
and automate devices in their homes.

I think this is an interesting illustration of the impact of the reduced cost
of writing code.

Prior to agents, it was entirely possible to reverse-engineer home devices.
The problem was the ROI - was it really worth all of that effort? More
importantly, any experienced programmer knows that undocumented, unstable
APIs like that may well change or break in the future. Is that initial work
worth the effort if you're committing yourself to a frustrating cycle of
maintenance in the future?

Coding agents change that equation entirely. The effort to get a simple
automation working has dropped, as has the cost of trying and failing to get
it to work. Since the code is so cheap, the idea of having to maintain it in
the future - or throw it away and start again - carries way less
psychological baggage."

Tags on the post: reverse-engineering, ai, generative-ai, llms,
ai-assisted-programming, coding-agents
```

## Cross-References

- **Corroborates**: `blog-simonwillison-charity-majors-code-economics.md`
  Claim 1 ("In 2025, the economics of code production were turned upside
  down — generation shifted from expensive and time-consuming to effectively
  free and instant") and Claim 3 ("Code's epistemic status shifted from
  capital asset...to consumable"). Majors names the general economic
  inversion (code as regenerable/disposable consumable rather than curated
  capital); this post is a concrete, narrow instance of exactly that
  inversion applied to a specific low-stakes use case (home-device
  automation), where "disposable and regenerable" literally means "throw it
  away and start again" with low psychological cost.

- **Corroborates**: `blog-addyosmani-intent-debt.md` Claim 9 ("Software's
  scarce resource shifted from the ability to produce correct implementation
  (now cheap) to intent"). Willison's claim that the *effort* to build the
  automation has dropped is the generation-cost side of the same shift Osmani
  names; both sources treat "cheap to write" as the new baseline condition,
  though Osmani's post is about what remains scarce (intent) rather than
  about willingness to start throwaway projects.

- **Contradicts**: None filed. This source's Claim 4 (less psychological
  baggage about future maintenance) could superficially seem to conflict with
  `blog-simonwillison-james-shore-maintenance-costs.md` Claim 4 ("stopping AI
  agent use does not remove the accumulated maintenance debt — teams are
  'permanently indentured'") and Claim 5 (current agents tend to increase,
  not decrease, maintenance costs). On inspection this is a conditioning-
  variable difference, not a genuine contradiction (per MINER.md §4a "when
  NOT to file"): Shore's claims are about production codebases maintained by
  a team, where the code stays in service and discarding it is not a real
  option — the maintenance debt compounds because the system must keep
  running. Willison's claim is scoped to personal, single-owner, low-stakes
  home automations where "throw it away and start again" is a literally
  available and low-cost option. The two sources describe different stakes
  (disposable hobby script vs. load-bearing production system), not opposing
  claims about the same situation. No contradiction issue filed.

- **Extends**: `blog-simonwillison-charity-majors-code-economics.md` — Majors
  names the supply-side economic shift in the abstract; this post supplies a
  concrete, if anecdotal, illustration of that shift changing a specific
  category of real-world decision (whether to attempt a reverse-engineering
  project at all).

- **Novel**: The specific application of "cheap code" economics to
  reverse-engineering undocumented, unstable home-device APIs is new to the
  corpus — no existing source note addresses this use case (verified via
  keyword search across `source-notes/` for "reverse-engineering," "home
  automation," "IoT," and "undocumented API"; no matches). The framing of the
  effect as primarily *psychological* ("less psychological baggage") rather
  than purely economic is also a distinct angle not previously named this way
  in the corpus, though it is closely related to the disposable/regenerable
  framing in the Majors source.

## Guide Impact

- **Chapter 00 (Principles)**: The guide's existing framing at
  `guide/00-principles.md` line 231 ("AI makes code cheap to generate. It
  does not make understanding cheap to skip.") is corroborated by this
  source but should NOT be extended using it to claim that maintenance
  actually gets cheaper — this source is about the psychological threshold
  for *starting* low-stakes work, not about maintenance cost itself. If the
  guide adds a discussion of when "cheap to write" changes practitioner
  behavior, this source is a citable example of the effect being scoped to
  low-stakes, easily-discarded projects — pair with the Shore source's
  warning (via the Cross-References note above) that the same reasoning does
  not hold for production systems a team is committed to keeping running.

- **Chapter 01 (Daily Workflows)**: This source is a good candidate for a
  brief callout on personal/exploratory automation as a legitimate use case
  for agentic coding — projects previously not worth attempting due to
  maintenance risk are now reasonable to attempt precisely because failure
  and abandonment are cheap. This is a narrower and more defensible claim
  than a general ROI framework, and should be presented as anecdotal
  color, not as an established pattern.

## Extraction Notes

- The source is unusually short: a four-paragraph "note" (Willison's site
  distinguishes "notes" from full "entries"), confirmed via direct HTML fetch
  of the page. There are no sub-pages, linked case studies, or named
  anecdotes to follow — the post's own text states Willison is relaying
  secondhand anecdotes without naming sources. This limits the note to 4
  extracted claims rather than the usual 5-15; a shallow-looking claim count
  here reflects the source's actual length, not incomplete reading. The full
  verbatim text is reproduced in Concrete Artifacts for verification.
- All quotes were checked against the raw HTML fetched directly from
  https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/ (not the
  WebFetch AI-summarized version, which paraphrased some sentences).
- Considered filing a contradiction issue against the James Shore maintenance-
  costs source but concluded, per MINER.md §4a, that the difference is a
  conditioning variable (personal/disposable projects vs. team-maintained
  production systems), not a real contradiction. See Cross-References for the
  full reasoning.
- Cross-reference verification: claim numbers cited above were confirmed by
  re-reading the actual source notes in this session —
  `blog-simonwillison-charity-majors-code-economics.md` Claim 1 (line 47) and
  Claim 3 (line 89); `blog-addyosmani-intent-debt.md` Claim 9 (line 93);
  `blog-simonwillison-james-shore-maintenance-costs.md` Claim 4 (line 111)
  and Claim 5 (line 130).
