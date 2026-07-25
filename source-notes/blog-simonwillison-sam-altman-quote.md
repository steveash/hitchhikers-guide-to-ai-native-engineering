---
source_url: https://simonwillison.net/2026/Jul/20/sam-altman/
source_type: blog-post
title: "A quote from Sam Altman"
author: Simon Willison (quoting Sam Altman's October 2022 email to OpenAI's board)
date_published: 2026-07-20
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: emerging
issue: "#2213"
---

# A quote from Sam Altman

> A single primary-source quotation — Sam Altman's October 1, 2022 email to
> OpenAI's board, exposed in *Musk v. Altman* (2026) litigation discovery —
> in which Altman proposes releasing a locally-runnable, GPT-3-capability
> open-weight model for explicitly competitive reasons (pre-empt Stability
> AI, discourage rival releases, reduce funding for competing efforts), with
> no mention of user access or public benefit as a motivation.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus citation, no surrounding editorial commentary; ~90 words
  total including the quote). Auto-discovered via the `simon-willison`
  trusted feed.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo, but for this post he is purely a curator — he adds no
  original analysis, only the blockquote and its citation. The underlying
  primary source is Sam Altman's own email, addressed to OpenAI's board on
  October 1, 2022, entered into the public record via discovery in the
  *Musk v. Altman* litigation (referenced by Willison as "*Musk v. Altman
  (2026)*") and first circulated publicly via the `@techemails` account on
  X/Twitter (`https://twitter.com/techemails/status/2078854346683678927`,
  linked as the blockquote's `cite` attribute in the page's HTML). This
  Miner could not independently verify the `@techemails` post (X returned
  HTTP 402 to automated fetch), so authenticity rests on Willison's citation
  chain (blog post → tweet → litigation exhibit) rather than on this note's
  own direct inspection of the underlying court filing.
- **Scope**: Covers exactly one thing — the text of one email, quoted in
  full as reproduced by Willison. Does not cover any other part of the
  *Musk v. Altman* case, any other exposed OpenAI internal document, any
  OpenAI response to the email's disclosure, or any framing/analysis beyond
  the bare citation ("Sam Altman, Email to OpenAI's board, October 1, 2022 -
  exposed in Musk v. Altman (2026)").

## Extracted Claims

### Claim 1: In an October 1, 2022 email to OpenAI's board, Sam Altman proposed that OpenAI create and release a language model with roughly GPT-3's capability that could run locally on consumer hardware
- **Evidence**: Direct primary-source quote (the full body of the email, as
  reproduced by Willison from the litigation-exposed document).
- **Confidence**: emerging (a specific, quoted primary document with a
  stated provenance chain, but not independently verified by this Miner
  against the original court filing or the `@techemails` source post)
- **Quote**: "We have been having extensive discussions around open source strategy. We will discuss it more at our next board meeting, but one thing we'd like to do soon is to create a language model with the approximate capability of GPT-3 that can run locally on consumer hardware and release that."
- **Our assessment**: This is a concrete, dated, internal planning statement — notably from three years before this note's extraction date and roughly six months before ChatGPT's public GPT-3.5 debut context, i.e., from the same period OpenAI was already running GPT-3 as a hosted API product. The proposal is specifically for a *locally-runnable* open-weight model, distinct from OpenAI's hosted-API business — a strategic category OpenAI has, as of this corpus's other OpenAI-sourced notes, not actually shipped as of the 2026 present (see Cross-References).

### Claim 2: Altman stated the release should happen soon, explicitly "before Stability or someone else does" — i.e., timed as a pre-emptive competitive move against Stability AI and other potential open-model releasers
- **Evidence**: Direct quote, same email.
- **Confidence**: emerging (same provenance caveat as Claim 1 — single
  quoted document, not independently cross-verified)
- **Quote**: "We'd like to do it soon, before Stability or someone else does."
- **Our assessment**: This frames the proposed release as a timing race against a named competitor (Stability AI, which had released Stable Diffusion earlier in 2022), not as a response to user demand or an access gap. The urgency is competitive, not altruistic.

### Claim 3: Altman's stated general rationale for OpenAI releasing a locally-runnable, GPT-3-capability model is that doing so discourages other organizations from releasing similarly-powerful models and makes it harder for competing AI efforts to secure funding
- **Evidence**: Direct quote, same email — the explicit "why" clause
  attached to the release proposal.
- **Confidence**: emerging (same provenance caveat — this is the single
  most consequential sentence in the source, and it rests entirely on the
  authenticity of one litigation-exposed email)
- **Quote**: "In general, we think this helps discourage others from releasing similarly-powerful models, and makes it harder for new efforts to get funded."
- **Our assessment**: This is the source's highest-value sentence for the guide: it is a first-party, internal (not public-facing) statement of *why* a frontier lab might release an "open" model — not to broaden access or benefit the public, but to suppress the competitive and financial viability of rivals. Internal board communications are less subject to PR-audience pressure than a company blog post, which is part of what makes this evidence notable despite being a single document. See Cross-References — Contradicts for the direct tension with OpenAI's later public mission framing.

### Claim 4: The email entered the public record via discovery in *Musk v. Altman*, litigation identified by Willison only as "(2026)" with no further case detail given in this post
- **Evidence**: The blockquote's citation line and Willison's post date
  (July 20, 2026).
- **Confidence**: anecdotal (no case number, court, filing date, or docket
  reference is given in this source — this Miner did not attempt to locate
  the underlying litigation record, which is out of scope for a single
  90-word quotation post)
- **Quote**: "Sam Altman, Email to OpenAI's board, October 1, 2022 - exposed in Musk v. Altman (2026)"
- **Our assessment**: This establishes *how* a 2022 internal email became public in 2026 (litigation discovery, not voluntary disclosure or a leak), which matters for weighing the document's authenticity and OpenAI's lack of control over its release — but the guide should not treat "exposed in Musk v. Altman (2026)" as a verified case citation without independent confirmation, since this source gives no docket or filing detail.

## Concrete Artifacts

```
Full text of the quoted email (Sam Altman to OpenAI's board, October 1, 2022,
as reproduced verbatim in the page HTML at
simonwillison.net/2026/Jul/20/sam-altman/):

"We have been having extensive discussions around open source strategy.
We will discuss it more at our next board meeting, but one thing we'd
like to do soon is to create a language model with the approximate
capability of GPT-3 that can run locally on consumer hardware and
release that. We'd like to do it soon, before Stability or someone else
does. In general, we think this helps discourage others from releasing
similarly-powerful models, and makes it harder for new efforts to get
funded."

Citation line: "— Sam Altman, Email to OpenAI's board, October 1, 2022 -
exposed in Musk v. Altman (2026)"

Cited primary link (blockquote's `cite` attribute, not independently
verified by this Miner — X returned HTTP 402 to automated fetch):
https://twitter.com/techemails/status/2078854346683678927
```

## Cross-References

- **Corroborates**: No existing source note documents this specific 2022
  email or the general pattern it illustrates (competitive rather than
  access-driven motivation for an open-model release) with primary-document
  evidence; nothing in the corpus corroborates this claim independently.
- **Contradicts**: **See filed contradiction issue #2235** (not resolved in
  this note per MINER.md §4a — no verdict is assigned here). Claim 3 here
  (OpenAI's 2022 internal rationale for releasing an open-weight model was
  to "discourage others from releasing similarly-powerful models" and
  "make it harder for new efforts to get funded") is in direct tension with
  `blog-openai-built-to-benefit-everyone.md` Claim 3 ("give everyone on
  Earth a personal AGI") and Claim 7 ("we believe the safer future is one
  where power is broadly distributed... more of the world can participate
  in building a resilience ecosystem"). Both sources concern the same
  underlying question — what actually motivates OpenAI's openness-adjacent
  decisions — but Side A here is a contemporaneous internal document giving
  a competitive-strategy rationale, and Side B is a 2026 public mission
  statement giving an access/benefit rationale. This is a distinct
  mechanism from the already-filed issue #1597 (nationality-gated export
  controls vs. universal-access rhetoric, also contradicting
  `blog-openai-built-to-benefit-everyone.md`) — #1597 is about *who gets
  access*, this new issue is about *why an open release decision gets made
  in the first place*. Contradiction filed for human resolution; see
  CONTRADICTIONS.md once resolved.
- **Extends**: `blog-simonwillison-open-source-ai-gap-map.md` and
  `blog-simonwillison-inkling-open-weights.md` both document the current
  (2026) open-weights ecosystem and lab openness practices in detail, but
  neither addresses lab *motivation* for releasing open models — this
  source adds a rare data point on stated internal motivation (competitive
  suppression of rivals), three-plus years earlier than either of those
  notes' subject matter, from the specific lab (OpenAI) most central to
  this corpus's frontier-lab coverage.
- **Novel**: The specific claim that a frontier lab's internal (not public)
  rationale for a proposed open-weight release was explicitly to suppress
  competitors' ability to release comparable models and to reduce their
  funding prospects is new to this corpus. No other source note documents
  an internal strategic memo of this kind for any lab.

## Guide Impact

- **No chapter should currently cite this source as a general claim about
  how frontier labs think about open-sourcing today** — it is a single,
  unaudited, 2022-dated email about a model OpenAI never actually shipped
  (OpenAI's flagship 2022–2023 releases were GPT-3.5/ChatGPT and GPT-4, both
  closed/hosted-API products, not a locally-runnable open-weight release;
  this corpus's other OpenAI-sourced notes do not document OpenAI having
  since released a GPT-3-class open-weight consumer model). The claim's
  guide value is as a **historical caution about mission-statement
  interpretation**, not as evidence of current OpenAI practice.
- **Chapter 00 (Principles), if/where the guide discusses how much weight
  to give a frontier lab's public "open" or "benefit everyone" framing**:
  Cite Claim 3 alongside the filed contradiction (issue #2235) as a concrete
  historical instance — from the lab's own internal communication, not a
  critic's inference — where a plausible-sounding "open source strategy"
  decision was reasoned about in explicitly competitive terms internally,
  while the same lab's later public statements (`blog-openai-built-to-
  benefit-everyone.md`) frame comparable strategic territory in
  access/benefit terms. Recommend framing this as "internal board
  communications and public mission statements can describe the same
  strategic territory very differently — weight primary internal documents
  higher than mission copy when they're available and don't over-generalize
  from one 2022 email to 2026 intent."

## Extraction Notes

1. **Source is unusually thin**: this is Simon Willison's "quotation" post
   type — a single blockquote and a one-line citation, with zero surrounding
   editorial commentary. Per MINER.md's "aim for 5-15 claims... if you only
   found 1-2, you probably didn't read deeply enough" guidance: this note
   extracts 4 claims, which is the full substantive content of the source.
   Padding further would require either fabricating claims not present in
   the source or splitting the single email into artificially finer-grained
   sub-claims; neither was done. This matches the second and third
   Prospector triage comments' framing of the source as "a single
   historical quotation" with "minimal concrete guidance."
2. **Verbatim text obtained via direct `curl`, not an AI-summarizing fetch
   tool**: a first WebFetch attempt against the page returned a paraphrased
   reconstruction, not verbatim source text, and a follow-up WebFetch
   attempting to request raw text was refused as a copyright concern by the
   fetch tool's underlying model. Per MINER.md §2a, all quotes in this note
   were instead obtained by fetching the raw HTML directly with `curl`
   (browser user-agent) against `simonwillison.net`, and copied
   character-for-character from the `<blockquote>` element in that HTML.
3. **`@techemails` primary source not independently verified**: the
   blockquote's `cite` attribute points to
   `https://twitter.com/techemails/status/2078854346683678927`. Both an
   unauthenticated WebFetch of the `twitter.com` URL (redirected to
   `x.com`) and a direct fetch of the `x.com` URL failed (the `x.com` fetch
   returned HTTP 402 Payment Required, consistent with X's paywall for
   unauthenticated automated access). This Miner did not have access to an
   authenticated X/Twitter client and did not attempt to locate the
   underlying *Musk v. Altman* court filing directly. Confidence is set to
   `emerging` rather than `settled` for this reason — the quote is specific
   and plausible (Willison is a credible curator with no evident motive to
   fabricate a quote), but this note's own verification chain stops at
   Willison's blog post rather than reaching the original litigation
   exhibit or tweet.
4. **No sub-pages followed**: the source page contains no substantive
   inline links beyond the citation link to the (inaccessible) `x.com`
   post and standard site navigation/tag links. Per MINER.md §1, none were
   followed beyond the one attempted (and failed) fetch of the citation
   link itself.
5. **Contradiction filed**: per MINER.md §4a, filed issue #2235 ("OpenAI's
   2022 open-weight release rationale: competitive-blocking strategy
   (internal email) vs. 'power broadly distributed' mission framing (2026
   public statement)") before writing this note, contrasting this source's
   Claim 3 against `blog-openai-built-to-benefit-everyone.md` Claims 3 and
   7. No verdict is assigned in this note; see the issue and (once
   resolved) CONTRADICTIONS.md. Checked for and did not duplicate the
   already-filed, related-but-distinct issue #1597.
6. **Cross-reference verification**: before writing citations above,
   `blog-openai-built-to-benefit-everyone.md`,
   `blog-simonwillison-open-source-ai-gap-map.md`, and
   `blog-simonwillison-inkling-open-weights.md` were re-read directly
   (MINER.md §4b) and all claim numbers above were confirmed against those
   notes' numbered `### Claim N:` headings in document order.
7. **Overall confidence set to `emerging`**: all four claims rest on a
   single primary-document quotation with a plausible but not
   independently-verified provenance chain (per Extraction Note 3). This is
   stronger than a bare editorial opinion (`anecdotal`) because it is a
   quoted primary document with specific, checkable text, not weaker than
   `settled` only because this note could not independently confirm the
   underlying litigation exhibit or original tweet.
