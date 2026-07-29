---
source_url: https://simonwillison.net/2026/Jul/25/boris-cherny/
source_type: blog-post
title: "Quoting Boris Cherny"
author: Simon Willison (quoting Boris Cherny)
date_published: 2026-07-25
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: anecdotal
issue: "#2288"
---

# Quoting Boris Cherny

> A single-sentence quotation post — Simon Willison highlighting Boris
> Cherny's claim that Claude Opus 5 is "our least prompt injectable model
> yet," sourced to page 73 of Anthropic's Opus 5 System Card — with no
> independent commentary, testing, or quantified figures reproduced by
> Willison himself.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus a citation line, no surrounding editorial commentary;
  posted 25th July 2026 at 12:42 am). Auto-discovered via the
  `simon-willison` trusted feed.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo and maintains the corpus's most-cited index of
  prompt-injection incidents. For this post he is purely a curator — he
  adds no original analysis, testing, or framing beyond the blockquote and
  its citation (the same pattern as `blog-simonwillison-sam-altman-quote.md`
  in this corpus). The quoted individual, Boris Cherny, is not described in
  the post itself — no role, title, or employer is stated in the page text.
  The post is tagged `anthropic` and `claude` on Willison's site (a
  classification tag, not an in-post statement), consistent with Cherny
  being an Anthropic-affiliated source, but this note's own verification of
  that affiliation stops at the tag; it was not independently confirmed
  against an Anthropic staff page or the linked tweet (which returned HTTP
  402 to unauthenticated fetch — see Extraction Notes).
- **Scope**: Covers exactly one thing — a single sentence attributed to
  Boris Cherny about Claude Opus 5's resistance to prompt injection,
  quoted by Willison, with a citation pointing to Cherny's original
  X/Twitter post and to page 73 of Anthropic's Claude Opus 5 System Card
  PDF. Does NOT cover: the System Card's actual page-73 content (the PDF
  could not be fetched in full for this extraction — see Extraction
  Notes), the original tweet's full text or any eval scores it may have
  referenced, or any comparison to other vendors' models.

## Extracted Claims

### Claim 1: Boris Cherny states that, more than any of the eval scores associated with its release, what excites him most about Claude Opus 5 is that it is "our least prompt injectable model yet"
- **Evidence**: A single X/Twitter post by Cherny, block-quoted in full by
  Willison, with a citation linking to page 73 of the Opus 5 System Card as
  the underlying source of the claim.
- **Confidence**: anecdotal (a single vendor-affiliated individual's
  first-person social-media statement; no attack-success rate, red-team
  methodology, or other quantified figure is given in the quoted text
  itself — any such figure would live on the cited System Card page, which
  this extraction could not independently verify; see Extraction Notes)
- **Quote**: "More than any of these eval scores, what is most exciting to me is something else: Opus 5 is our least prompt injectable model yet."
- **Our assessment**: This is a comparative superlative relative only to
  Anthropic's own prior model lineage ("least prompt injectable model
  *yet*") — it makes no claim about standing relative to competitor models
  (GPT, Gemini) and supplies no attack-success-rate number itself. The
  phrase "more than any of these eval scores" indicates Cherny's original
  post referenced specific eval results that are not reproduced in
  Willison's excerpt, so the strength of the underlying evidence cannot be
  assessed from this source alone. It should be read as a vendor-employee's
  own characterization of a training/eval outcome, not as an
  independently-verified capability claim.

### Claim 2: The claim is explicitly sourced to page 73 of Anthropic's Claude Opus 5 System Card, rather than presented as an unattributed marketing statement
- **Evidence**: Willison's citation line pairs the quote with a direct
  hyperlink to Cherny's original X/Twitter post and a second hyperlink
  targeting a page-73 anchor within the Opus 5 System Card PDF hosted on
  Anthropic's own CDN.
- **Confidence**: settled (the existence of both links, and that the
  second one targets a `#page=73` anchor within a specifically-named PDF
  on an `anthropic.com`-controlled CDN domain, is directly checkable from
  the page's own HTML, independent of whether this extraction verified
  page 73's actual content)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the
  exact wording of the citation line itself was returned inconsistently
  across separate fetch attempts and is not reproduced verbatim here; the
  underlying URLs, not the surrounding prose, are the verified artifact)
- **Our assessment**: Citing a specific page number in a named, vendor-
  published System Card gives the claim a nominally checkable location,
  which is more specific than an unattributed marketing statement would be.
  However, a page citation is only as strong as the cited content, and this
  extraction was unable to fetch the System Card PDF directly (it exceeded
  the fetch tool's content-size limit — see Extraction Notes), so this note
  cannot confirm what evidence page 73 actually presents (eval numbers,
  red-team methodology, comparison baseline, etc.). The guide should treat
  the page-73 citation as a pointer for a future, dedicated mining pass of
  the Opus 5 System Card, not as content already verified in this note.

### Claim 3: Willison's post consists solely of the blockquoted sentence and a citation line, with no independent testing, scrutiny, or commentary added by Willison himself
- **Evidence**: Direct observation of the page's content structure (a
  single blockquote, a citation/byline line, and standard site
  navigation/tag furniture — no additional prose).
- **Confidence**: settled (a direct observation of what is and is not
  present on the page, not a claim requiring external verification)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the page
  contains no editorial sentence by Willison beyond the blockquote and its
  citation)
- **Our assessment**: This matters for how much evidentiary weight the
  source itself carries. Unlike Willison's hands-on coverage elsewhere in
  this corpus (e.g., his own testing of Fable 5's proactive behavior in
  `blog-simonwillison-fable-relentlessly-proactive.md`), this post adds no
  independent scrutiny of Cherny's claim — Willison is functioning purely
  as an aggregator, structurally identical to his "sam-altman-quote" post
  (`blog-simonwillison-sam-altman-quote.md`). The guide should treat this
  source as a pointer to a citable primary document (the System Card), not
  as an independently-vetted practitioner assessment of Opus 5's actual
  prompt-injection resistance.

## Concrete Artifacts

```
Source: Simon Willison, simonwillison.net/2026/Jul/25/boris-cherny/
Posted: 25th July 2026 at 12:42 am
Tags: ai, prompt-injection, generative-ai, llms, anthropic, claude, boris-cherny

Blockquoted text (attributed to Boris Cherny):
"More than any of these eval scores, what is most exciting to me is
something else: Opus 5 is our least prompt injectable model yet."

Citation links (as embedded in the page):
  - Boris Cherny's original post:
    https://twitter.com/bcherny/status/2080713091688583312
  - Anthropic Claude Opus 5 System Card, page 73:
    https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=73
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-hack-my-ai-assistant.md` Claim 1 (zero of ~6,000
    prompt-injection attempts succeeded against an Opus 4.6-powered
    deployment) — this source's claim that the *next* model generation
    (Opus 5) is Anthropic's "least prompt injectable model yet" is
    directionally consistent with that prior result and with the
    downward-trend-by-model-generation observation already recorded in
    `CONTRADICTIONS.md` entry C-007's resolution. This source adds no
    quantified figure of its own, so it corroborates the *direction* of the
    trend, not a specific number.
  - `blog-simonwillison-prompt-injection-role-confusion.md` Claim 5 (Opus
    4.5 failed 11% of the time against automated role-confusion attacks as
    of May 2026) — Cherny's superlative claim about Opus 5 is consistent
    with a continuation of that trendline one generation forward, but this
    source gives no comparable automated-attack failure rate for Opus 5 to
    compare directly against the 11% figure.
- **Contradicts**: None identified directly. Practitioners should note
  that `CONTRADICTIONS.md` entry **C-007** (debated, resolved 2026-07-02)
  already tracks an unresolved tension between near-100% human-red-teamer
  success against frontier models (per the role-confusion paper) and the
  0/6,000 hackmyclaw result against Opus 4.6. This source's claim is a
  vendor characterization with no red-team methodology or attempt count of
  its own, so it neither resolves nor adds new data to that debate — it
  should not be read as evidence that prompt injection is "solved" for
  Opus 5. No new contradiction issue filed: this source's claim is a
  directional, unquantified vendor statement, not a specific figure that
  materially opposes either side of C-007.
- **Extends**:
  - `blog-simonwillison-introducing-opus-5.md` Claim 6 (Opus 5 improved at
    *detecting* vulnerabilities via general capability gains but remains
    "substantially behind Mythos 5" at *exploiting* them, per Anthropic's
    own disclosure) — that note documents Opus 5's offensive-capability
    restraint; this source adds a complementary defensive-hardening claim
    (prompt injection resistance) for the same model, rounding out Opus
    5's security profile across both axes documented so far in the corpus.
  - `blog-anthropic-choosing-claude-model.md` (Opus 5 launched the same
    week as Anthropic's model-selection guidance, positioning Opus for
    "reasoning-intensive enterprise tasks") — this source adds a specific
    security-property data point for the Opus tier not covered in that
    note's model-class descriptions.
- **Novel**: First corpus source attributing a named Anthropic-affiliated
  individual's (Boris Cherny's) personal characterization of a specific
  model's prompt-injection resistance, and the first corpus pointer to the
  Opus 5 System Card's page 73 specifically (as distinct from general
  system-card citations elsewhere in the corpus, e.g. the Fable 5 system
  card page cited in `blog-simonwillison-fable-silent-interventions.md`).

## Guide Impact

- **No chapter should cite the "least prompt injectable model yet" claim
  as a verified capability fact on its own.** It is a single, unquantified,
  vendor-employee social-media statement whose supporting evidence (page
  73 of the System Card) was not independently accessible to this
  extraction. Its guide value is as a **pointer to a primary document**,
  not as citable evidence of Opus 5's actual security properties.
- **Chapter on Model Selection / Security (wherever the guide discusses
  Ch06-equivalent prompt-injection material)**: If the guide adds a
  running list of vendor claims about model-generation improvements in
  prompt-injection resistance (alongside the Opus 4.5/GPT-5.4 automated-
  attack figures from `blog-simonwillison-prompt-injection-role-confusion.md`
  and the Opus 4.6 hackmyclaw result), this source can be cited as the
  Opus 5 data point in that list — explicitly flagged as `[anecdotal]` and
  unquantified, per Claim 1's assessment above, pending a dedicated mining
  pass of the Opus 5 System Card itself (page 73 specifically) to obtain
  the actual eval/red-team figures Cherny's post references but does not
  reproduce.

## Extraction Notes

1. **Source is a single-sentence quotation post**: this is the same
   Willison post type as `blog-simonwillison-sam-altman-quote.md` — one
   blockquote, one citation line, no editorial commentary. Per MINER.md's
   "aim for 5-15 claims... if you only found 1-2, you probably didn't read
   deeply enough" guidance: this note extracts 3 claims, which is the full
   substantive content available. The two Prospector triage comments
   rating this "low novelty" / "thin curation of a single quote" concur
   with this assessment; a third comment rated it "medium" citing the
   System Card as traceable evidence, which this note treats as a citation
   pointer rather than verified content (see Claim 2).
2. **System Card PDF not independently fetched**: an attempt to fetch
   `https://www-cdn.anthropic.com/.../Claude%20Opus%205%20System%20Card.pdf#page=73`
   directly failed with a tool-side "maxContentLength exceeded" error (the
   PDF is too large for the fetch tool). Page 73's actual content — the
   eval scores, red-teaming methodology, or any quantified figure backing
   Cherny's claim — is NOT verified in this note. This is a strong
   candidate for a dedicated future source-submission issue targeting the
   Opus 5 System Card directly (ideally a specific page range or section,
   given the full-document fetch failure here).
3. **Original tweet not independently verified**: both
   `twitter.com/bcherny/status/2080713091688583312` (redirects to
   `x.com`) and the redirected `x.com` URL were attempted; the `x.com`
   fetch returned HTTP 402 Payment Required, consistent with X's paywall
   for unauthenticated automated access (the same failure mode
   encountered for the `@techemails` tweet cited in
   `blog-simonwillison-sam-altman-quote.md`). This Miner did not have
   access to an authenticated X/Twitter client. Confidence for Claim 1 is
   set to `anecdotal` rather than `emerging` for this reason, combined with
   the fact that no quantified figure appears in the reproduced text
   itself.
4. **Verbatim quote verified via repeated, narrowly-targeted fetches**:
   the one-sentence blockquote in Claim 1 was independently re-requested
   with differently-worded prompts across two separate fetch calls and
   returned character-for-character identical wording both times. The
   surrounding citation-line prose (Claim 2) was NOT consistent across
   fetch attempts (different phrasing was returned each time), so it is
   deliberately not presented as a verbatim quote — only the underlying
   URLs, which do not vary between fetches, are treated as verified.
5. **No sub-pages followed beyond the two citation links**: both were
   attempted (System Card PDF, original tweet) and both failed for the
   reasons above (size limit; paywall). The page's "Recent articles"
   sidebar links (unrelated launch-week posts) were not followed, as they
   are standard site furniture rather than links the post itself relies on
   for its claim.
6. **Cross-reference verification**: before writing citations above,
   `blog-simonwillison-hack-my-ai-assistant.md`,
   `blog-simonwillison-prompt-injection-role-confusion.md`,
   `blog-simonwillison-introducing-opus-5.md`, and
   `CONTRADICTIONS.md` entry C-007 were re-read directly (MINER.md §4b),
   and all claim numbers cited above were confirmed against those notes'
   numbered `### Claim N:` headings in document order.
7. **No contradiction filed**: this source's claim is a directional,
   unquantified vendor statement about a newer model generation. It does
   not supply a specific figure that materially opposes either side of the
   already-filed and already-resolved (`debated`) C-007 contradiction, so
   no new contradiction issue was filed. See Cross-References — 
   Contradicts above.
8. **`confidence_overall` set to `anecdotal`**: all three claims rest on a
   single vendor-employee social-media statement (Claims 1 and the framing
   observations in Claims 2-3) with no independently-verifiable
   quantitative backing accessible to this extraction (the System Card PDF
   and original tweet were both unreachable). This is weaker than the
   `emerging` rating given to `blog-simonwillison-sam-altman-quote.md`,
   which rests on a specific primary-document quotation with more concrete,
   checkable textual content, even though that note's provenance chain was
   also not fully independently verified.
