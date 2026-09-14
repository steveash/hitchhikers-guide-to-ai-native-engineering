---
source_url: https://simonwillison.net/2026/Sep/9/terence-tao/
source_type: blog-post
title: "A quote from Terence Tao"
author: Simon Willison (quoting Terence Tao, Fields Medalist, UCLA), primary source Terence Tao's Mastodon thread
date_published: 2026-09-09
date_extracted: 2026-09-14
last_checked: 2026-09-14
status: current
confidence_overall: emerging
issue: "#3427"
---

# A quote from Terence Tao

> Simon Willison's "quotation" post excerpts two non-adjacent paragraphs
> from a 4-post Mastodon thread in which Terence Tao argues that AI's
> ability to rapidly "flatten" open mathematical problems is turning
> problem *identification* into the scarce resource, creating an incentive
> for researchers to stop sharing promising directions publicly — and
> proposes a mitigation (explicit community standards on what counts as a
> valuable "solution") that Willison's excerpt omits entirely.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — two
  short blockquoted paragraphs plus a one-line citation, with a `[...]`
  elision marker between them and zero original commentary from
  Willison). Auto-discovered via the `simon-willison` trusted feed.
- **Author credibility**: Willison is a designated `trusted-feed` source
  in this repo, but here he is purely a curator. The underlying primary
  source is Terence Tao — UCLA mathematics professor and Fields Medalist
  — posting under his own verified Mastodon account (`@tao@mathstodon.xyz`,
  26,413 followers, profile fields independently verified against
  `math.ucla.edu/~tao` and `terrytao.wordpress.com`). Per MINER.md §1,
  this Miner followed the citation link and fetched Tao's full original
  4-post thread directly from the Mastodon API
  (`mathstodon.xyz/api/v1/statuses/117237320796901560/context`), not just
  Willison's excerpt — see Extraction Notes for why this matters.
- **Scope**: Covers a single connected argument, posted by Tao as a
  4-part thread on 8 September 2026: (1) open problems are a
  non-renewable resource despite infinite possible questions, (2) problem
  *selection* is a skilled, historically-informed judgment, and every
  technical advance "flattens" a field's difficulty landscape, (3) AI is
  unlike prior advances because it flattens landscapes without leaving a
  stable "AI-feasible" vs. "AI-hard" boundary, making problem
  identification itself the scarce resource and creating a disincentive
  to share research directions publicly, and (4) Tao's own proposed
  mitigation — not banning automated tools, but establishing explicit
  community norms about what counts as a valuable contribution, analogous
  to food-donation-drive standards. Does not cover: any specific AI lab,
  product, or technique; any quantitative measurement of the phenomenon
  Tao describes; or replies/reception in the thread (59 public replies
  exist but are third-party reactions, not part of Tao's own claims, and
  were not extracted).

## Extracted Claims

### Claim 1: Tao argues that good, fruitful open mathematical problems are being consumed in a non-renewable way and risk becoming scarce, even though the set of possible problems one could pose is infinite
- **Evidence**: Tao's own stated analogy (a water-scarce region surrounded by ocean), first paragraph of post 1/4 of his Mastodon thread.
- **Confidence**: anecdotal (a named expert's own framing/analogy for a trend he asserts, not a measured or independently checkable claim)
- **Quote**: "I wrote recently about how the collection of good, fruitful open problems is now being mined in a non-renewable fashion, leading to the potential scenario of these problems becoming scarce.  This may seem unintuitive at first, since the set of possible problems one could ask is infinite.  Perhaps the following analogy can help: a country or region can suffer a critical shortage of drinking water while simultaneously being surrounded by a massive ocean." (post 1/4, mathstodon.xyz/@tao/117237320796901560)
- **Our assessment**: This is the thread's opening premise, not itself argued for in this post (Tao references "I wrote recently about" an earlier, unlinked post as the actual argument for non-renewability — this thread assumes it as established). The water/ocean analogy is doing real work: it distinguishes "infinite possible questions" from "infinite *valuable* questions," which is the distinction the rest of the thread depends on.

### Claim 2: Tao states that determining whether a mathematical question is actually worth pursuing is a slow, deliberate, subjective judgment informed by historical experience of what earlier work on similar problems did or did not produce
- **Evidence**: Tao's own methodological claim about how mathematicians select problems, post 2/4.
- **Confidence**: anecdotal (a working mathematician's description of his field's judgment process, not a measured result)
- **Quote**: "Working out whether a question is actually worth highlighting is a lengthy, deliberate, and subjective process, often informed by historical experience on what good mathematics was generated (or not generated) while working on earlier problems of this type." (post 2/4)
- **Our assessment**: This establishes the skill Tao later argues AI is devaluing not by answering questions faster, but by removing the "difficulty landscape" that lets this judgment operate at all (Claim 3). It is a load-bearing premise for the rest of the argument, not a standalone finding.

### Claim 3: Tao argues every mathematical advance — technique, technology, or infrastructure — "flattens" a field's difficulty landscape, and this is usually offset by the same advance expanding the range of results researchers can reach, creating new frontiers to explore
- **Evidence**: Tao's own general claim about how mathematical progress has historically worked, post 2/4.
- **Confidence**: anecdotal (a named expert's generalization about the history of his field, not a specific measured case)
- **Quote**: "Every new advance in mathematics, whether it comes from technique, technology, or infrastructure (such as access to libraries of past literature) reduces the difficulty of solving problems.  This is generally a good thing; but it comes at the cost of flattening out the difficulty landscape of a field, to the point where one can no longer discern its geometry to the extent that promising questions can be extracted within the range of applicability of the tool.  Often this effect is counteracted by the ability of such a tool to enlarge the radius of the sphere of results one can plausibly reach, creating new boundaries to fruitfully explore." (post 2/4)
- **Our assessment**: This is the general pattern Claim 4 says AI breaks. Tao is explicit that "flattening the difficulty landscape" is not new or inherently bad — it is the normal mechanism of progress — which makes his subsequent claim about AI being different a comparative one, not a claim that flattening itself is harmful.

### Claim 4: Tao argues current AI tools are unlike prior advances because they flatten difficulty landscapes without leaving any stable boundary between "AI-feasible" and "AI-hard" problems, a situation he attributes partly to how fast the technology is changing and partly to AI companies' refusal to disclose negative results or their solution process
- **Evidence**: Tao's own comparative claim, post 3/4, explicitly contrasted against the general pattern described in Claim 3.
- **Confidence**: emerging (a specific, named causal claim — including an explicit accusation of non-disclosure by AI companies — from a domain expert with direct visibility into which problems AI has and hasn't solved, but not an independently audited or measured claim)
- **Quote**: "However, one notable feature of the current AI era is the absence of any definitive such boundaries.  While AI tools have flattened the difficulty landscape now in many areas of the subject, thus destroying the ability to locate promising new problems in that area, there are no clear frontiers that are separating the \"AI-feasible\" problems from the \"AI-hard\" problems (which certainly still exist, given that the difficulty level of problems are unbounded, and can even be undecidable).  This is in part due to the rapidly changing nature of the technology, but also compounded by the refusal of AI companies to disclose their negative results, or reveal the process towards obtaining their solutions." (post 3/4)
- **Our assessment**: The "refusal... to disclose negative results" half of this claim is a specific, checkable accusation, not just a framing device, and it echoes a pattern already documented elsewhere in the corpus (see Cross-References): vendors publish polished successes and withhold the failed-attempt denominator. Tao is extending that same observed pattern to open mathematical research specifically, with the added claim that the absence of failure data is itself what prevents the field from mapping a stable "AI-hard" boundary.

### Claim 5: Tao argues that identifying a promising problem, not solving it, is now the scarce resource — because even a rumor that someone is working on a problem can trigger a large-scale AI-powered effort to solve it before the original researcher can develop it fully
- **Evidence**: Tao's own claim, stated as an observed pattern ("we have now seen"), post 3/4.
- **Confidence**: emerging (a specific, falsifiable claim about observed behavior in the mathematical research community, stated by a domain insider, but reported anecdotally with no named instance, date, or count)
- **Quote**: "In fact, it is now the identification of a promising problem which is the scarce and precious resource.  We have now seen that even the rumor of someone working on a problem can trigger a massive amount of AI-powered effort to flatten it before the original research project has time to reach its full potential." (post 3/4)
- **Our assessment**: This is the thread's central empirical claim, and it is also its weakest-evidenced one: "we have now seen" asserts an observed pattern but names no specific incident, so it cannot be independently checked from this source alone. It is nonetheless the load-bearing claim for the incentive argument in Claim 6, and corroborates (as a research-domain-specific instance) the corpus's existing evidence that large amounts of agentic effort can now be mobilized very quickly (see Cross-References).

### Claim 6: Tao argues this dynamic creates an incentive to stop sharing promising research directions with the broader community, which would reverse centuries of open-science tradition and cause serious long-term damage to the field
- **Evidence**: Tao's own stated conclusion, following directly from Claim 5, post 3/4. This is the exact passage Willison's blog post quotes.
- **Confidence**: emerging (a specific, named risk with a clear causal mechanism from a domain expert, but a prediction about future researcher behavior, not an observed outcome)
- **Quote**: "The incentives may now be pointing in the direction of no longer sharing any promising research directions with the broader community, which would reverse centuries of traditions of open science and do serious long-term damage to the future of the field." (post 3/4)
- **Our assessment**: This is the claim the Prospector's triage flagged as high-novelty, and it holds up on full reading: it is a specific, game-theoretic mechanism (rumor → AI rush → original researcher loses the credit/opportunity → rational response is silence) rather than a vague "AI threatens open science" assertion. Whether it is *already happening* at scale is not established by this source (see Claim 5's evidentiary gap); it is presented as an emerging risk, not a settled trend.

### Claim 7: Tao argues that indiscriminate use of automated solution-extraction tools solves the immediate problem at hand but at the cost of sustaining the research ecosystem for future progress and of the community's understanding of how the progress was achieved
- **Evidence**: Tao's own summary judgment, post 4/4, opening the thread's concluding post.
- **Confidence**: anecdotal (a normative judgment/synthesis from a named expert, not a measured claim)
- **Quote**: "In short, the indiscriminate use of powerful solution-extraction tools can achieve the immediate short-term goal of solving problems at hand, but at the cost of sustaining the ecosystem for the next wave of progress, or in understanding the progress already obtained." (post 4/4)
- **Our assessment**: This reframes Claims 4-6 as a single tradeoff (short-term problem-solving vs. long-term ecosystem health and process-understanding) rather than a flat "AI is bad for math" position — a distinction the guide should preserve if it cites this source, since it is closer to a capacity/incentive-design critique than an anti-AI one.

### Claim 8: Tao proposes that rather than trying to prohibit automated solution-extraction tools (which he considers technically infeasible), the mathematical community should designate certain classes of problems as requiring a "careful analysis" that extracts insight and understanding of the difficulty landscape, not just a raw solution — analogous to how food donation drives reject "technically edible" contributions that don't meet explicit community standards
- **Evidence**: Tao's own proposed mitigation, post 4/4, closing the thread.
- **Confidence**: anecdotal (a named expert's own proposed policy/norm, not something tested or adopted)
- **Quote**: "While it may be technically infeasible to completely prohibit the use of automated tools to perform indiscriminate solution extraction, I believe that we can still designate many classes of problems as being desirous of a careful analysis that not only solves the problem, but identifies insights from the solution process, and learn more about the difficulty landscape for nearby problems, and for which raw solutions without such analysis would be of negligible or even negative value for these purposes.  This is analogous to how a modern food donation drive no longer accepts arbitrary contributions even when they are verified to be technically edible, but instead maintains explicit and socially accepted standards on what level of contributions are actually sought." (post 4/4)
- **Our assessment**: This is the thread's most guide-relevant claim and is the part Willison's excerpt drops entirely (see Extraction Notes) — Tao is not arguing against AI-assisted research, he is arguing for community-level *acceptance criteria* that value process/insight over raw output, which generalizes past mathematics: it is a specific instance of a broader "define what counts as a valid contribution, not just a correct one" pattern that the guide's verification chapter already addresses for code review (see Cross-References).

## Concrete Artifacts

### Full verbatim text of Tao's 4-post Mastodon thread (fetched directly from the Mastodon API, not from Willison's excerpt)
```
Source: https://mathstodon.xyz/@tao/117237320796901560 and its reply
chain, fetched via `mathstodon.xyz/api/v1/statuses/117237320796901560/context`,
posted by Terence Tao (@tao@mathstodon.xyz) starting 2026-09-08T20:32:28Z.

[1/4] I wrote recently about how the collection of good, fruitful open
problems is now being mined in a non-renewable fashion, leading to the
potential scenario of these problems becoming scarce.  This may seem
unintuitive at first, since the set of possible problems one could ask
is infinite.  Perhaps the following analogy can help: a country or
region can suffer a critical shortage of drinking water while
simultaneously being surrounded by a massive ocean.

One can easily generate any number of open problems in mathematics at
will, such as working out the 10^10^10th digit of pi.  But the vast
majority of such problems are not worth focusing attention on: they
show no particular propensity to reveal any further insights or
connections to other questions, or may either be too easy or too
impossible relative to known techniques to learn anything from the
exercise.

[2/4] Working out whether a question is actually worth highlighting is
a lengthy, deliberate, and subjective process, often informed by
historical experience on what good mathematics was generated (or not
generated) while working on earlier problems of this type. ... Every
new advance in mathematics, whether it comes from technique,
technology, or infrastructure (such as access to libraries of past
literature) reduces the difficulty of solving problems.  This is
generally a good thing; but it comes at the cost of flattening out the
difficulty landscape of a field ... Often this effect is counteracted
by the ability of such a tool to enlarge the radius of the sphere of
results one can plausibly reach, creating new boundaries to fruitfully
explore.

[3/4] However, one notable feature of the current AI era is the
absence of any definitive such boundaries. ... there are no clear
frontiers that are separating the "AI-feasible" problems from the
"AI-hard" problems ... This is in part due to the rapidly changing
nature of the technology, but also compounded by the refusal of AI
companies to disclose their negative results, or reveal the process
towards obtaining their solutions.

In fact, it is now the identification of a promising problem which is
the scarce and precious resource.  We have now seen that even the
rumor of someone working on a problem can trigger a massive amount of
AI-powered effort to flatten it before the original research project
has time to reach its full potential.  The incentives may now be
pointing in the direction of no longer sharing any promising research
directions with the broader community, which would reverse centuries
of traditions of open science and do serious long-term damage to the
future of the field.

[4/4] In short, the indiscriminate use of powerful solution-extraction
tools can achieve the immediate short-term goal of solving problems at
hand, but at the cost of sustaining the ecosystem for the next wave of
progress, or in understanding the progress already obtained. While it
may be technically infeasible to completely prohibit the use of
automated tools to perform indiscriminate solution extraction, I
believe that we can still designate many classes of problems as being
desirous of a careful analysis that not only solves the problem, but
identifies insights from the solution process ... This is analogous to
how a modern food donation drive no longer accepts arbitrary
contributions even when they are verified to be technically edible,
but instead maintains explicit and socially accepted standards on what
level of contributions are actually sought.

(Note: "..." marks this Miner's own elisions in this consolidated
artifact block, made for length only, each within a single post/
paragraph and never splicing non-adjacent posts together. Every
individual Claim's Quote field above is copied verbatim from a single
contiguous passage with no elision beyond a trailing thread-number
marker.)
```

### What Willison's blog post actually quotes, for comparison
```
Source: https://simonwillison.net/2026/Sep/9/terence-tao/, raw HTML
fetched directly via curl.

"I wrote recently about how the collection of good, fruitful open
problems is now being mined in a non-renewable fashion, leading to the
potential scenario of these problems becoming scarce. [...]
We have now seen that even the rumor of someone working on a problem
can trigger a massive amount of AI-powered effort to flatten it before
the original research project has time to reach its full potential.
The incentives may now be pointing in the direction of no longer
sharing any promising research directions with the broader community,
which would reverse centuries of traditions of open science and do
serious long-term damage to the future of the field."

— Terence Tao (citation links to mathstodon.xyz/@tao/117237320796901560)
Tags: mathematics, ai, ai-ethics
Posted: 9th September 2026 at 12:20 am
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-ten-advances-mathematics.md` and
`blog-simonwillison-research-acceleration-view-inside-openai.md` were
each re-read directly before writing this section, and every `Claim N`
cited below was located and confirmed by number and content against
that note's own `### Claim N:` headings in document order, per
MINER.md §4b.

- **Corroborates**:
  - `blog-simonwillison-research-acceleration-view-inside-openai.md`
    Claim 5 ("by mid-August 2026 the organization used the equivalent
    of 3.1 agent-workdays... for every one workday of human labor"):
    this note's Claim 5 (a rumor can trigger "a massive amount of
    AI-powered effort") is a qualitative, research-community-specific
    instance of the same underlying capacity fact this corpus already
    has a quantitative anchor for — large amounts of agentic labor can
    now be mobilized quickly against a single target once attention is
    drawn to it.
  - `blog-simonwillison-ten-advances-mathematics.md` Claim 3
    ("OpenAI... did not publish the prompts used to produce the
    results" — an editorial observation from Willison that OpenAI
    disclosed output artifacts but not process) corroborates this
    note's Claim 4 (Tao: AI companies' "refusal... to disclose their
    negative results, or reveal the process towards obtaining their
    solutions" prevents the field from mapping a stable capability
    boundary). Two independent sources, about the same general
    phenomenon (AI labs solving open math problems), both flag the same
    disclosure gap — one from a journalist/curator's observation, one
    from a domain expert's stated reason it matters.

- **Contradicts**: None filed as a formal contradiction issue. The
  Prospector's two triage comments on this issue disagree with each
  other on this point — the first comment frames this source as
  directly contradicting `blog-simonwillison-ten-advances-mathematics.md`
  ("this note documents Tao's optimistic 'big mathematics' vision...
  This source documents Tao's concern about the *opposite* problem"),
  while the second comment finds "no overlap" and treats it as a wholly
  novel concern. Having now read this source's full 4-post thread
  (not just Willison's two-paragraph excerpt), this Miner's assessment
  sides closer to the second comment, but as "Extends" rather than
  "no overlap" or "contradicts" — see below. Per MINER.md §4a, a
  contradiction issue is filed only when two claims "would lead to
  different guide advice" on the same axis; here, Tao's "big
  mathematics" optimism (`ten-advances-mathematics.md` Claims 6-7:
  decentralized human-AI collaboration works *because* formal
  verification gives cheap, low-trust checking) and this thread's
  concern (indiscriminate automated solution-extraction, absent
  community norms, erodes the incentive to share research) are not
  competing verdicts about whether AI helps or harms mathematics — they
  are the same person describing the conditions under which
  collaboration works (verification-backed trust) and warning what
  happens when those conditions are absent (norm-free "flattening").
  Claim 8 of this note (Tao's own proposed fix — explicit community
  standards for what counts as a valuable contribution) is structurally
  the same move as `ten-advances-mathematics.md` Claim 7 (verification
  as the trust mechanism that "filters out a lot of the rubbish"): both
  are Tao proposing a *governance/norms* layer as the answer to a
  trust or incentive problem, not a rejection of AI involvement. No
  contradiction issue filed.

- **Extends**: `blog-simonwillison-ten-advances-mathematics.md`
  Claims 6-7 (Tao's "big mathematics" vision: humans keep the creative
  layer, AI absorbs technical work, formal verification is the trust
  mechanism that makes decentralized collaboration safe) — this note
  adds the risk case that vision does not by itself address: what
  happens when AI-powered effort can be mobilized *before* any
  collaboration structure or verification norm is in place, i.e. a
  "rumor" alone, not a formally shared project. Claim 8's proposed
  mitigation (explicit community standards on what a valid contribution
  must include) is the missing governance piece that would let "big
  mathematics" absorb the risk this thread describes.

- **Novel**: The specific mechanism in Claim 5 — that a mere *rumor*
  of research activity, not a published result or an open
  collaboration, can now trigger a race to solve the problem via AI —
  is new to the corpus. No existing source note documents an
  attention-driven, pre-publication incentive effect of AI capability
  on research behavior. Claim 8's "food donation drive" analogy for
  designing acceptance criteria that value insight over raw output is
  also a novel framing device not present elsewhere in the corpus.

## Guide Impact

- **Chapter 00 (Principles) → "Verification Over Generation"**: This
  source's direct engineering applicability to a software-engineering
  guide is limited — it is about mathematical research culture, not
  coding practice. The closest genuine tie-in is Claim 4's point that
  AI labs' non-disclosure of negative results and process prevents
  observers from mapping a stable capability boundary ("AI-feasible"
  vs. "AI-hard"). This corroborates (not extends with new mechanism,
  see Cross-References) the guide's existing theme that vendor capability
  claims should be treated with the same "published outputs, not
  published process" skepticism already applied elsewhere in the corpus
  — cite alongside `blog-simonwillison-ten-advances-mathematics.md`
  Claim 3, not as a standalone addition.
- **No chapter should cite Claims 5-6 (the rumor-triggers-a-rush and
  disincentive-to-share mechanism) as an established engineering-team
  risk.** These are domain-expert predictions about the mathematics
  research community specifically, evidenced only anecdotally ("we have
  now seen," no named instance). If a future chapter on team-adoption
  risk or knowledge-sharing culture wants to raise "could rapid AI
  capability discourage engineers from sharing exploratory work
  internally," this source can be cited as an analogous concern *from a
  different domain*, not as direct evidence about software engineering
  teams — the guide should not conflate open mathematical research
  norms with internal engineering team dynamics without that caveat.
- **Chapter 05 (Team Adoption)**: No specific existing subsection is a
  strong fit. If the guide ever adds content on internal knowledge-
  sharing incentives under AI-accelerated work (a topic Chapter 05
  does not currently cover — see headings audited above), Claim 8's
  framing (explicit standards for what counts as a valuable
  contribution, not just a correct one) is a reusable governance pattern
  worth citing, paired with the caveat above.

## Extraction Notes

1. **This Miner fetched Tao's full 4-post thread, not just Willison's
   excerpt.** Willison's blog post quotes only part of post 1/4 and part
   of post 3/4, joined by a `[...]` elision marker, and omits posts 2/4
   and 4/4 entirely — including Tao's own proposed mitigation (Claim 8),
   which is arguably the most guide-relevant part of the thread. The
   issue's Prospector triage comments both worked from a characterization
   of the source that (based on their wording) appears to reflect only
   Willison's two-paragraph excerpt, not the full thread — see the
   Contradicts discussion above for how this changed this Miner's
   assessment. Per MINER.md §1 ("follow up to 5 linked pages that seem
   substantive"), the Mastodon `cite` link was treated as substantive and
   followed to its full reply-chain context via the Mastodon API
   (`/api/v1/statuses/{id}/context`), which returns each post's full text
   in a structured JSON field, avoiding the need to screen-scrape a
   JavaScript-rendered timeline.
2. **One reference in the source was not chased further**: post 1/4
   opens "I wrote recently about how the collection of good, fruitful
   open problems is now being mined in a non-renewable fashion" — this
   points to an earlier Tao post that is not hyperlinked anywhere in
   this thread's content (no `<a>` tag in the post HTML). This Miner did
   not search for or attempt to identify that earlier post; Claim 1 is
   extracted as Tao's own restated premise in this thread, not verified
   against whatever the original longer argument was.
3. **59 public replies exist on the thread's root post** (per the
   Mastodon API context) but were not extracted — MINER.md's extraction
   process is about the source's own claims, and replies are third-party
   reactions, not statements by Tao himself.
4. **Quote verification**: every Quote field above was copied
   character-for-character from the Mastodon API's JSON `content` field
   for the relevant post (HTML-tag-stripped, HTML-entity-unescaped) via
   direct `curl` + Python, not from an AI-summarizing fetch tool — an
   initial WebFetch pass against the Mastodon post page returned only a
   truncated page-title fragment and could not be used as a quote
   source. The two long, italic-free straight-quote passages ("difficulty
   landscape," "AI-feasible," "AI-hard") were confirmed present verbatim
   in the raw API JSON, not curly-quote artifacts of any rendering tool.
5. **Confidence calibration**: Claims 1-3, 7, and 8 are rated
   `anecdotal` (personal framing, methodological description, or
   proposed norm from a named expert, none independently checkable).
   Claims 4-6 are rated `emerging` — they are more specific and
   falsifiable (a named causal mechanism, an observed-but-unnamed
   pattern, a predicted incentive shift) but still rest on Tao's
   unelaborated personal assertion ("we have now seen") with no named
   instance, date, or count. Overall note confidence set to `emerging`
   to reflect that mix, consistent with
   `blog-simonwillison-ten-advances-mathematics.md`'s `anecdotal`
   rating for its comparably-sourced Tao claims and this note's slightly
   more specific causal claims (4-6) pulling the average up.
