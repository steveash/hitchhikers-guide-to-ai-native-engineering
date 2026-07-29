---
source_url: https://www.latent.space/p/ainews-codex-usage-up-10x-in-6-months
source_type: blog-post
title: "[AINews] Codex usage up >10x in 6 months to 7M users, +1M in the past ~day; did Codex overtake Claude Code??"
author: swyx / smol.ai (AINews aggregation, published under Latent Space)
date_published: 2026-07-14
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2300"
---

# [AINews] Codex usage up >10x in 6 months to 7M users, +1M in the past ~day; did Codex overtake Claude Code??

> A daily AINews aggregation digest (covering 7/11–7/13/2026) assembles a
> Codex user-count timeline from named OpenAI executives' own tweets —
> ~550k-700k (Jan 1, 2026) → 2M (March) → 6M (Jul 10-12) → 7M (Jul 13),
> a claimed 10x growth in six months — and juxtaposes it against Claude
> Code's last public disclosure (~2M users, $2.5B ARR, February 2026),
> posing the open question of whether Codex has overtaken Claude Code
> while explicitly flagging that Anthropic's silence since February makes
> the comparison difficult to make cleanly.

## Source Context

- **Type**: blog-post (daily news-aggregation digest, "AINews" — a section
  of Latent Space / smol.ai, published 2026-07-14 for the 7/11-7/13 news
  cycle, spanning a holiday weekend gap). Editorially, this is swyx's own
  synthesis and commentary built around a curated set of tracked tweets,
  not original reporting or an interview — the digest explicitly frames
  itself as "a quiet day lets us fact check some numbers against the sound
  of silence of Claude Code reporting."
- **Author credibility**: swyx (Shawn Wang) co-founded Latent Space, a
  well-regarded AI engineering publication already represented in this
  corpus (`blog-latentspace-databricks-agent-clouds.md`,
  `blog-latentspace-ainews-meta-harness-summer.md`). AINews itself
  states its own methodology in a standard footer: "AI News for
  7/11/2026-7/13/2026. We checked 12 subreddits, 544 Twitters and no
  further Discords." Unlike the meta-harness-summer digest (which mostly
  paraphrases third-party reactions), this post's core numeric claims
  trace to two named, directly relevant primary sources: Fidji Simo
  (OpenAI's CEO of Applications, who disclosed the Jan 1 and March
  figures on X) and a person identified in the post only as "Tibo," who
  posted the 6M (Jul 12) and 7M (Jul 13) milestone tweets. This is
  stronger sourcing than an anonymous Twitter reaction, but the digest
  itself performs the arithmetic and interpretation (the "10x" framing,
  the "similar trajectory" extrapolation, the "did Codex overtake Claude
  Code" question) — those synthesis steps are swyx's own, not sourced to
  either OpenAI or Anthropic directly.
- **Scope**: Covers, in the free-preview portion read for this note: (1)
  the Codex user-growth timeline and its arithmetic; (2) Claude Code's
  last disclosed user/revenue figures and Anthropic's subsequent silence
  on the metric; (3) a "charitable interpretation" of that silence
  (Claude Tag); (4) the headline "did Codex overtake Claude Code"
  question, left explicitly unresolved. Does NOT cover (behind this
  post's paywall, not reached in this extraction): the "AI Twitter Recap"
  and "AI Reddit Recap" sections that the post's own table of contents
  lists as covering agent infrastructure, coding agents, GPT-5.6 Sol
  updates, open models, security/privacy, and continual-learning
  research — none of that material was read for this note (see
  Extraction Notes).

## Extracted Claims

### Claim 1: Codex grew from an estimated 550k-700k users on January 1, 2026 to 7 million users by July 13, 2026 — roughly 10x growth in six months
- **Evidence**: The Jan 1 figure and the March 2M figure are both attributed to Fidji Simo (OpenAI's CEO of Applications) via a linked X/Twitter post; the July milestones are attributed to a second named source ("Tibo") via two linked tweets (6M on Jul 12, 7M on Jul 13). The "10x" figure is the digest's own arithmetic (7M ÷ 700k ≈ 10x) presented as the post's headline claim.
- **Confidence**: emerging (the endpoint figures trace to named, directly-relevant individuals — OpenAI's own applications CEO and a Codex-team-adjacent poster — rather than anonymous reactions, but none of the four data points (550k-700k, 2M, 6M, 7M) is drawn from an audited OpenAI report; they are individual tweets aggregated and interpolated by the digest into a single trajectory)
- **Quote**: "Fidji [puts the Jan 1 number at around 550k-700k users](https://x.com/fidjissimo/status/2033537381907710092)"
- **Our assessment**: This is a more granular and more recent timeline than any single-snapshot figure elsewhere in the corpus — it adds two waypoints (Jan 1, March) that predate `blog-openai-codex-knowledge-work.md`'s June 2 disclosure of "5M weekly active users" and two waypoints (Jul 10-12, Jul 13) that postdate it. The two sets of figures are consistent with a single continuous growth curve (700k → 2M → ~5M → 6M → 7M across Jan-Jul 2026) rather than contradicting one another — see Cross-References. Treat the *shape* of the trajectory (steady, fast growth all year) as reasonably well-evidenced by four independent tweets from relevant sources; treat the precise "10x" multiplier as the digest's own rounding of a Jan 1 estimate that is itself a range (550k-700k), not a single audited number.

### Claim 2: A named individual ("Tibo") announced the 7 million active-user milestone on July 13, 2026, framing it explicitly as spanning both Codex and "ChatGPT Work," and OpenAI gave users a "banked reset" to mark the occasion
- **Evidence**: Direct quote of the milestone tweet, as relayed by the digest.
- **Confidence**: emerging (a specific, named, dated product announcement quoted directly, though only relayed via the digest rather than independently fetched from the primary tweet)
- **Quote**: "Thank you to the 7M active users who are now using Codex and ChatGPT Work. We have added a banked reset to everyone's account to celebrate the milestone."
- **Our assessment**: This is the most concrete, checkable claim in the source — a named product milestone with a specific user-facing action (a "banked reset," i.e., a usage-quota reset) taken to mark it. Notably, the 7M figure explicitly spans two products ("Codex and ChatGPT Work"), not Codex alone — this is a scope caveat the digest's own headline ("Codex usage up >10x... to 7M users") does not carry forward, and it means the 7M figure is not a clean apples-to-apples comparison to a Codex-only user count. This matters for how the guide should cite the number: it is an OpenAI-product-family figure, not a pure "Codex" figure, even though the source headlines it that way.

### Claim 3: Claude Code's most recent public disclosure — roughly 2 million users and $2.5B ARR — was made in February 2026, and Anthropic has not updated these figures since
- **Evidence**: Digest's own framing statement, linking to Anthropic's own funding-announcement press release as the source of the February figures.
- **Confidence**: emerging (the February figures trace to Anthropic's own announcement, linked directly by the digest; the claim that Anthropic has not updated them "since" is the digest's own observation of an absence, which is harder to verify independently than a positive claim)
- **Quote**: "the last update we got about Claude Code is the roughly 2M users and $2.5B ARR in Feb"
- **Our assessment**: This is the first source note in the corpus to record a Claude-Code-specific (not company-wide) user count and ARR figure. It is a different metric from the company-wide run-rate revenue trajectory in `blog-simonwillison-anthropic-47b-revenue.md` (which documents Anthropic's total run-rate revenue reaching $30B around April 6, 2026 and $47B in May 2026) — that note's figures are company-wide, not product-specific to Claude Code, so the two should not be conflated even though both cite large dollar figures in a similar timeframe. No existing corpus note previously captured a Claude-Code-specific 2M-users/$2.5B-ARR figure; this fills that gap, at emerging confidence since it is a single secondhand relay of Anthropic's own February disclosure, not independently re-verified in this extraction.

### Claim 4: The digest offers a "charitable interpretation" for Claude Code's silence on updated metrics — that Anthropic shifted the bulk of its coding-agent user growth to "Claude Tag" (a Slack-based agent) rather than continuing to report Claude Code CLI numbers — while leaving the comparison to Codex's growth explicitly unresolved
- **Evidence**: The digest's own editorial interpretation, presented as one possible (charitable) explanation rather than a confirmed fact.
- **Confidence**: anecdotal (explicitly labeled by the source itself as an interpretation — "the charitable interpretation... of course" — not a confirmed fact; no Anthropic statement is cited to support it)
- **Quote**: "The charitable interpretation on Claude Code's comparative silence on reporting, of course, is that they moved the bulk of coding to Claude Tag months ago and are now focusing users there."
- **Our assessment**: "Claude Tag" here refers to Anthropic's Slack-native team agent (Claude in Slack), previously documented in `blog-latentspace-ainews-meta-harness-summer.md` (Claims 3, 5-6) as a distinct product surface from the Claude Code CLI — that note quotes @random_walker describing it as "a coworker that remembers everything and bills by the thought." If the "moved reporting focus to Claude Tag" interpretation is correct, it would mean any Codex-vs-Claude-Code user-count comparison is comparing a single OpenAI product family against only part of Anthropic's coding-agent user base, understating Anthropic's true agentic-coding reach. The digest itself does not resolve whether this interpretation is correct — it is offered as the *charitable* reading, implying an uncharitable alternative (that Claude Code's growth has genuinely slowed and Anthropic is declining to publicize it) exists but is not spelled out or evidenced in the source. Treat this claim as speculation, not evidence, when citing it.

### Claim 5: The digest poses, but does not answer, the question of whether Codex has overtaken Claude Code, concluding only that Codex's growth rate itself is a notable number regardless of the comparison's resolution
- **Evidence**: The post's own headline framing and closing editorial line.
- **Confidence**: anecdotal (an explicitly open, unresolved editorial question — the source's own framing, not a factual claim)
- **Quote**: "But 10x growth in 6 months is an impressive number to beat nonetheless."
- **Our assessment**: This is a deliberately hedged conclusion. The headline question ("did Codex overtake Claude Code??") is double-question-marked in the source's own title, signaling the author's own uncertainty rather than a settled verdict. The guide should not cite this source as evidence that "Codex overtook Claude Code" — it explicitly does not claim that. It should be cited only for the narrower, better-evidenced claim: Codex's user count grew roughly 10x from Jan 1 to Jul 13, 2026 (Claim 1), while the most recent comparable Claude-Code-specific figure available to the public dates to February 2026 (Claim 3).

## Concrete Artifacts

```
Codex user-count timeline (as assembled by the AINews digest,
July 14, 2026, from tweets by Fidji Simo and "Tibo"):

  Jan 1, 2026   ~550,000-700,000 users   (Fidji Simo, via X)
  March 2026    2,000,000 users          (Fidji Simo, via X)
  Jul 10-12     6,000,000 users          ("Tibo," via X — gained in the
                                          prior 48 hours)
  Jul 13, 2026  7,000,000 active users   ("Tibo," via X — spans "Codex
                                          and ChatGPT Work"; +1M in ~1 day
                                          from the Jul 12 figure)

  Digest's own headline framing: ">10x growth in 6 months"

Claude Code, last public disclosure per this digest:
  Feb 2026      ~2,000,000 users, $2.5B ARR
                (Anthropic funding-announcement press release, linked by
                the digest; no update to this figure reported since)

Source: "[AINews] Codex usage up >10x in 6 months to 7M users, +1M in
the past ~day; did Codex overtake Claude Code??", Latent Space/AINews,
2026-07-14.
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in those
notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**: `blog-openai-codex-knowledge-work.md` Claim 1 ("Codex
  now has more than 5 million weekly active users, up more than 6x since
  the launch of the desktop app in February," dated June 2, 2026) — that
  note's 5M-weekly-active-users figure sits chronologically and
  numerically between this source's March waypoint (2M) and its July
  waypoints (6M, 7M), forming a single consistent growth curve across
  four independent disclosures (Fidji Simo's March tweet, OpenAI's own
  June 2 report, and Tibo's July 10-12 and July 13 tweets) rather than
  conflicting figures. This strengthens confidence in the overall
  direction (fast, roughly continuous Codex growth through H1 2026) even
  though none of the individual snapshots is independently audited.
- **Extends**: `blog-latentspace-ainews-meta-harness-summer.md` (Claims
  3, 5-6) — that note documents "Claude Tag" (Claude in Slack) as a
  distinct product surface from Claude Code, including named practitioner
  critiques of it. This source's Claim 4 relies on that same "Claude
  Tag" product to explain Claude Code's reporting silence, but does not
  itself establish what Claude Tag is — this note supplies that missing
  context via the earlier extraction.
- **Extends**: `blog-simonwillison-anthropic-47b-revenue.md` Claim 1
  (Anthropic's company-wide run-rate revenue trajectory: $9B Dec 2025 →
  $14B Feb 12, 2026 → $30B Apr 6, 2026 → $47B May 2026) — this source
  adds a Claude-Code-*specific* figure (2M users, $2.5B ARR, Feb 2026)
  that is a different metric (product-level, not company-wide) from the
  same general period. The two should be cited separately: the $47B-note
  figures describe all of Anthropic's revenue (API, Claude.ai, Claude
  Code, enterprise, etc. combined), while this source's $2.5B ARR figure
  is specifically attributed to Claude Code by the digest.
- **Contradicts**: None identified. This source does not make a claim
  that opposes any existing corpus note — its central tension (Codex's
  disclosed growth vs. Claude Code's reporting silence) is a *gap in
  available evidence* about Claude Code's current trajectory, not a
  factual disagreement with anything already in the corpus. Per
  MINER.md §4a, an absence of contradicting data is not itself a
  contradiction, so no contradiction issue was filed.
- **Novel**: The Jan 1, 2026 (550k-700k) and March 2026 (2M) Codex
  user-count waypoints (Claim 1) are new to the corpus — no prior note
  documents Codex's user count before the June 2, 2026 "5M weekly active
  users" disclosure. The Claude-Code-specific 2M-users/$2.5B-ARR
  disclosure (Claim 3) is also new — no prior corpus note isolates a
  Claude-Code-specific (as opposed to company-wide Anthropic) user or
  revenue figure. The explicit "Codex vs. Claude Code" competitive
  framing (Claim 5) is itself novel — prior corpus adoption sources
  report each vendor's numbers independently without directly comparing
  growth rates between the two leading coding agents.

## Guide Impact

- **Chapter 01 (Market Adoption)**: Add the assembled Codex growth
  timeline (Claim 1: ~700k Jan 1 → 2M March → 6-7M July 2026) as a more
  granular data point than the single June 2 snapshot already cited from
  `blog-openai-codex-knowledge-work.md`, with the explicit caveat (Claim
  2) that the July figures span "Codex and ChatGPT Work" jointly, not
  Codex alone — the guide should not present "7M" as a clean Codex-only
  count. Add Claim 3 (Claude Code: ~2M users, $2.5B ARR, last disclosed
  February 2026) as the most recent Claude-Code-specific adoption figure
  in the corpus, explicitly flagged as five months stale relative to
  this source's July 2026 publication date — any guide comparison of
  Codex vs. Claude Code adoption should note that the two vendors are not
  disclosing on comparable cadences, which makes a "who's winning"
  framing (the source's own headline question) currently unanswerable
  from public data.
- **Chapter 03 (Tool Evaluation & Market Positioning)**: Do not cite this
  source as evidence that "Codex overtook Claude Code" — per Claim 5, the
  source itself explicitly declines to make that claim. If the guide
  discusses competitive positioning between the two agents, cite the
  asymmetry in disclosure transparency (OpenAI publishing frequent
  milestone updates via named individuals' social posts; Anthropic not
  having updated its Claude-Code-specific figures since February) as the
  more defensible, better-evidenced point, rather than a growth-rate
  comparison built on non-comparable, non-contemporaneous snapshots.

## Extraction Notes

- **Paywall encountered, partially worked around**: Like
  `blog-latentspace-ainews-meta-harness-summer.md` (same publication),
  this post is a paid-tier Substack post with a free preview. Multiple
  targeted WebFetch calls recovered the free-preview portion — the
  opening framing, the full Codex-vs-Claude-Code growth analysis, and
  the section's concluding lines — but the post's table-of-contents
  indicates additional sections (an "AI Twitter Recap" covering agent
  infrastructure, coding agents, GPT-5.6 Sol, open models,
  security/privacy, and continual learning, plus an "AI Reddit Recap")
  that were not reached; WebFetch reported a "Keep reading with a 7-day
  free trial" / "Subscribe to Latent.Space to keep reading this post"
  paywall marker beyond the Codex/Claude Code section. Unlike the
  meta-harness-summer extraction, this note's Prospector-assigned focus
  (Codex/Claude Code adoption and competitive positioning) was fully
  contained within the free-preview portion that was successfully
  recovered, so the paywall did not prevent extracting the claims most
  relevant to this issue's triage guidance — but the other topics listed
  in the table of contents were not mined and may warrant a separate
  source submission if judged independently valuable.
- **First WebFetch pass returned a summary, not verbatim text**: as
  documented in several other AINews/Latent Space source notes in this
  corpus, the first WebFetch call against this URL returned an
  AI-summarized paraphrase rather than exact source text. Four
  additional, narrowly-scoped WebFetch calls (each asking for a specific
  short passage, under ~125 characters where possible, per MINER.md
  §2a.3) were used to recover verbatim quotes for each Claim above. All
  `Quote` fields were cross-checked for consistency across at least two
  separate fetch calls before inclusion.
- **No day-level dates for the Jan 1 or March Codex figures beyond what
  is quoted**: the source itself only gives "Jan 1" (an exact date) and
  "March" (month-only, no day) for the two earlier Codex waypoints; no
  more precise date was fabricated for the March figure.
- **"Similar trajectory" sentence flagged as ambiguous**: the source
  contains the sentence "Codex has followed a similar trajectory and is
  now around 10x user growth year to date," but the antecedent of
  "similar trajectory" is not unambiguous from the surrounding text
  recovered via WebFetch — it most plausibly refers to Codex's own
  implied growth curve extrapolated from its three known waypoints
  (Jan 1, March, July), not a comparison to Claude Code's separately
  discussed trajectory, but this note does not assert a confident reading
  of that sentence's referent and Claim 1 does not rely on it.
- **No sub-pages followed**: beyond the linked X/Twitter posts cited
  inline (which were not independently opened — their content is quoted
  as relayed by the digest), the post has no other substantive outbound
  links within the free-preview portion.
