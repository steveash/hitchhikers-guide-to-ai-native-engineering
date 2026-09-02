---
source_url: https://simonwillison.net/2026/Aug/26/qwen38-flash-next/
source_type: blog-post
title: "Qwen3.8-Flash-Next"
author: Simon Willison
date_published: 2026-08-26
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: anecdotal
issue: "#3153"
---

# Qwen3.8-Flash-Next

> A very short "link post" (7 short paragraphs, no timing/benchmark figures)
> in which Simon Willison relays Qwen's own description of Qwen3.8-Flash-Next
> as an early Qwen4-architecture preview, reports trying two Unsloth GGUF
> quantizations (72.5GB and 78.9GB) on a DGX Spark, and shares his favorite
> pelican-riding-a-bicycle SVG output — with no quality comparison, no
> tokens/second figure, and no reasoning-cost measurement of the kind his
> companion Qwen 3.8 27B post ten days earlier provided in depth.

## Source Context

- **Type**: blog-post (simonwillison.net, personal technical blog; explicitly
  self-labeled by the site as "a link post" — the shortest, lowest-effort
  post format Willison uses, distinct from his longer first-person
  evaluation posts).
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this corpus (creator of Django, Datasette, and the `llm` CLI
  tool) with an established track record of hands-on local-model testing
  already documented at depth in `blog-simonwillison-qwen38-27b-overthinking.md`
  (same author, same "pelican riding a bicycle" benchmark, same DGX Spark
  hardware, published ten days earlier). This particular post, however, is
  explicitly thinner than that companion post: it is one paragraph of vendor
  description, one paragraph of parameter counts, one paragraph naming the
  two quantizations tried, and one paragraph naming a favorite output — no
  timing data, no token counts, no side-by-side quality comparison between
  the two quantizations, and no explicit recommendation.
- **Scope**: Covers Qwen's own one-sentence self-description of
  Qwen3.8-Flash-Next, a one-sentence total/active-parameter figure, which
  two Unsloth GGUF quantizations Willison tried on a DGX Spark, and which
  single output (from the larger of the two, at `xhigh` reasoning effort) he
  preferred. Does NOT cover: throughput (tokens/second), latency, reasoning
  token counts, VRAM/RAM requirements actually observed on the DGX Spark,
  any coding-agent or non-image-generation task, any comparison against
  Qwen3.8-27B or Qwen3.8-Max, or independent verification of the "early
  preview of the architecture used in Qwen4" framing (the Qwen blog post
  Willison links to, `qwen.ai/blog?id=qwen3.8-flash-next`, did not render
  retrievable content for this Miner — see Extraction Notes).

## Extracted Claims

### Claim 1: Qwen3.8-Flash-Next is described (by Qwen, relayed by Willison in quotation marks) as "a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4"
- **Evidence**: Willison's opening paragraph, presenting the description in
  quotation marks as a relayed characterization rather than his own words.
- **Confidence**: emerging (a vendor self-description relayed by a credible
  practitioner, but not independently verified by this Miner against Qwen's
  own announcement — the linked `qwen.ai` blog page returned no retrievable
  body text on fetch)
- **Quote**: "Another open weights model from Qwen. This one is "a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4"."
- **Our assessment**: This is the post's only forward-looking architectural
  claim — that Qwen4 will share architectural DNA with this release — and it
  comes with no elaboration of what specifically previews Qwen4 (which
  layers, which routing scheme, etc.). Treat as a vendor teaser claim, not a
  technical specification; the actual architecture detail available to this
  Miner came from the linked Unsloth quantization page (Claims 5-8 below),
  not from Qwen's own post or from Willison's summary.

### Claim 2: Willison states the model is "125B tokens, but only 6B active" — likely a token/parameter terminology slip, since the same paragraph's framing ("performance boost" from a small active fraction) only makes sense if "125B" and "6B" refer to parameters, not tokens
- **Evidence**: Willison's second paragraph, a single unqualified sentence
  with no supporting figures or link for this specific number.
- **Confidence**: anecdotal (a single, unelaborated sentence from a
  non-benchmark blog post; likely a wording error rather than a deliberate
  claim about token counts)
- **Quote**: "It's pretty big: 125B tokens, but only 6B active which means it gets a significant performance boost."
- **Our assessment**: We read "125B tokens" as almost certainly meant to say
  "125B parameters" — MoE models are conventionally described by total vs.
  active *parameters*, not tokens, and the Unsloth model card linked from
  this same post (Claim 5) independently states "125B" as a parameter count
  ("125B with 6B activated, plus 51B n-gram embedding and 4B MTP"), not a
  token count. We flag this as a probable slip in the primary source rather
  than silently correcting it, per MINER.md's verbatim-quoting rule — the
  Assayer and Smith should read "125B tokens" in the quote above as sourced
  exactly as written, with this caveat attached.

### Claim 3: Willison tried two Unsloth GGUF quantizations of the model on a DGX Spark: the 72.5GB UD-IQ1_S and the 78.9GB UD-Q2_K_XL
- **Evidence**: Direct first-person statement naming both quantizations, file
  sizes, and the hardware used, with links to example outputs from each.
- **Confidence**: anecdotal (a single practitioner's in-progress exploration,
  explicitly flagged by the author as incomplete: "I'm still exploring the
  model")
- **Quote**: "I've been trying it out on a DGX Spark using these Unsloth quantized models. I'm still exploring the model - so far I've tried the 72.5GB UD-IQ1_S one (producing these pelicans) and the 78.9GB UD-Q2_K_XL (producing these)."
- **Our assessment**: Notably, both quantizations tried sit at the *bottom*
  of Unsloth's full-model GGUF ladder for this model — UD-IQ1_S is the
  smallest of the eleven and UD-Q2_K_XL the third smallest, with UD-IQ1_M
  (74.5GB) between them (see Claim 8's complete size table, running up to
  354GB for BF16) — consistent with fitting comfortably within a single
  DGX Spark's memory, though Willison
  does not state a memory ceiling or explain the choice explicitly. No
  timing, token/second, or side-by-side quality comparison is given between
  the two quantizations, unlike the companion Qwen 3.8 27B post's detailed
  before/after timing pairs (`blog-simonwillison-qwen38-27b-overthinking.md`
  Claims 2-3).

### Claim 4: Willison's favorite output so far came from the larger UD-Q2_K_XL quantization, generated with `xhigh` reasoning effort
- **Evidence**: Direct first-person preference statement, immediately
  preceding an embedded pelican-riding-a-bicycle illustration.
- **Confidence**: anecdotal (a single subjective preference between two
  unquantified example outputs, no stated methodology for the comparison)
- **Quote**: "My favorite so far was this xhigh reasoning effort one from UD-Q2_K_XL:"
- **Our assessment**: This confirms `xhigh` exists as a reasoning-effort
  setting on Qwen3.8-Flash-Next specifically (consistent with the
  `xhigh`/`medium`/`low` naming scheme already documented for Qwen3.8-Max
  and Qwen3.8-27B — see Cross-References), but gives no information about
  whether `xhigh` is this model's *default* the way it is for Qwen3.8-27B
  (`blog-simonwillison-qwen38-27b-overthinking.md` Claim 1), nor any cost
  figure for using it. The favorited image's alt text (Concrete Artifacts
  below) is the only description of output quality in the entire post — no
  prose critique of either quantization's output is given.

### Claim 5: Per the linked Unsloth GGUF model card, Qwen3.8-Flash-Next totals 125B parameters, described as "6B activated, plus 51B n-gram embedding and 4B MTP," with a native context length of 262,144 tokens extensible to 1,000,000
- **Evidence**: Unsloth's own published model card for the GGUF quantizations
  Willison links to and tested from — a third-party quantization provider's
  page, not Qwen's own primary documentation (which did not render for this
  Miner) or Willison's own words.
- **Confidence**: emerging (a named, specific architecture claim from a
  well-established quantization community project, itself presumably
  relaying Qwen's own model card, but not independently cross-checked by
  this Miner against Qwen's primary HuggingFace repository)
- **Quote**: "Number of Parameters: 125B with 6B activated, plus 51B n-gram embedding and 4B MTP"
- **Quote (context length)**: "Context Length: 262,144 natively and extensible up to 1,000,000 tokens."
- **Our assessment**: This is background architecture detail supporting
  Claim 2's "125B... 6B active" figure from Willison's own post, sourced to
  the page he links to rather than the post's own prose — attributed
  separately here per MINER.md's rule that cited material from a linked page
  is not the same as a claim made by the primary author. Note the component
  figures do not obviously sum in a simple total/active split (6B + 51B +
  4B = 61B, not 125B), which we do not attempt to resolve here; a future
  Miner reading Qwen's own primary model card directly would be better
  positioned to reconcile this.

### Claim 6: Per the Unsloth model card, the model routes to 10 of 512 experts per token plus one always-on shared expert ("10 Routed + 1 Shared")
- **Evidence**: Unsloth's GGUF model card, architecture section.
- **Confidence**: emerging (same sourcing caveat as Claim 5 — a
  quantization-provider page, not independently checked against Qwen's own
  primary documentation)
- **Quote**: "Number of Experts: 512" / "Number of Activated Experts: 10 Routed + 1 Shared"
- **Our assessment**: This 512-expert, 10-routed-plus-1-shared configuration
  is architecturally comparable in shape (though not scale) to Qwen
  3.5-397B's documented MoE layout (`blog-google-qwen35-ironwood-moe-optimization.md`
  Claim 3: "512 experts, top-10 routing, plus one always-on shared expert"),
  suggesting Qwen has kept a consistent 512-expert/top-10-plus-shared MoE
  routing shape across at least two model generations at very different
  total-parameter scales (397B vs. 125B) — a useful architecture-family data
  point, though sourced here to a third party (Unsloth) rather than Qwen
  directly for this specific model.

### Claim 7: Per the Unsloth model card, recommended sampling parameters differ sharply between Thinking mode (temperature 1.0, top_p 0.95, presence_penalty 0.0) and Instruct/Non-Thinking mode (temperature 0.7, top_p 0.80, presence_penalty 1.5)
- **Evidence**: Unsloth's GGUF model card, recommended-settings section.
- **Confidence**: emerging (same third-party sourcing caveat as Claims 5-6)
- **Quote (Thinking)**: "temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0"
- **Quote (Instruct/Non-Thinking)**: "temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0"
- **Our assessment**: The large swing in `presence_penalty` (0.0 in Thinking
  mode vs. 1.5 in Non-Thinking mode) is a concrete, actionable detail for any
  practitioner deploying this model — running Non-Thinking mode with the
  Thinking-mode `presence_penalty` (or vice versa) would deviate substantially
  from the vendor-recommended configuration. Neither the primary blog post
  nor this Miner's fetch of Qwen's own blog page describes or corroborates
  this recommendation directly; it is sourced solely to Unsloth's page.

### Claim 8: Per the Unsloth model card, the full-model GGUF quantization ladder for this model runs from 72.5GB (UD-IQ1_S, 1-bit) up to 354GB (BF16, full precision), with nine intermediate sizes in between
- **Evidence**: Unsloth's GGUF model card, quantization file listing.
- **Confidence**: settled (a directly observable repository file listing,
  independently checkable at the linked URL)
- **Quote**: (no direct quote; see the complete size table reproduced in
  Concrete Artifacts below)
- **Our assessment**: This places the two variants Willison tried (Claim 3)
  at the bottom of the ladder — the smallest and third-smallest of the eleven
  full-model quantizations Unsloth offers. He has not yet, as of this post,
  tried anything from UD-IQ3_XXS (82GB) upward.
  For a DGX Spark, that stops well short of the 192GB Q8_0 or 354GB BF16
  ceiling, so this post gives no evidence about how the model performs at
  higher-precision quantizations on that hardware.

## Concrete Artifacts

### Full body text of the source post (verbatim, in order)

```
"Another open weights model from Qwen. This one is "a multimodal MoE model
that also serves as an early preview of the architecture used in Qwen4"."

"It's pretty big: 125B tokens, but only 6B active which means it gets a
significant performance boost."

"I've been trying it out on a DGX Spark using these Unsloth quantized
models. I'm still exploring the model - so far I've tried the 72.5GB
UD-IQ1_S one (producing these pelicans) and the 78.9GB UD-Q2_K_XL
(producing these)."

"My favorite so far was this xhigh reasoning effort one from UD-Q2_K_XL:"

Source: simonwillison.net/2026/Aug/26/qwen38-flash-next/ (2026-08-26)
```

### Favorited pelican image alt text (verbatim)

```
"Flat vector illustration: a white pelican with an orange beak and orange
legs rides a red bicycle along a sandy path, a wicker basket on the
handlebars holding a blue fish, with green rolling hills, a small tree and
bushes, white clouds and a bright yellow sun in a blue sky behind it"

Source: image alt text on simonwillison.net/2026/Aug/26/qwen38-flash-next/,
the UD-Q2_K_XL / xhigh reasoning effort output referenced in Claim 4
```

### Unsloth GGUF quantization size table (complete listing, from the linked model card)

```
Bits     Variant       Size
1-bit    UD-IQ1_S      72.5 GB
1-bit    UD-IQ1_M      74.5 GB
2-bit    UD-Q2_K_XL    78.9 GB
3-bit    UD-IQ3_XXS    82 GB
3-bit    UD-Q3_K_XL    90 GB
4-bit    UD-IQ4_XS     93.7 GB
4-bit    MTP Q4_K_M    2.79 GB
4-bit    MTP Q4_K_M    1.91 GB
4-bit    UD-Q4_K_XL    111 GB
5-bit    UD-Q5_K_XL    158 GB
6-bit    UD-Q6_K_XL    169 GB
8-bit    Q8_0          192 GB
8-bit    MTP Q8_0      2.79 GB
16-bit   BF16          354 GB
16-bit   MTP BF16      7.77 GB
16-bit   MTP BF16      5.23 GB

Source: huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF, linked from
simonwillison.net/2026/Aug/26/qwen38-flash-next/ as "these Unsloth
quantized models"

Miner's note: every row the model card lists is reproduced above, with the
card's own bit-width grouping preserved. The rows prefixed `MTP` are the
separate small multi-token-prediction module files (1.91-7.77 GB), not
full-model quantizations; the eleven remaining rows are the full-model
ladder discussed in Claims 3 and 8.
```

### Links referenced by the post (verbatim anchor text / destination)

```
"these Unsloth quantized models" -> huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF
"Qwen3.8-Flash-Next" (implicit source of the quoted description) -> qwen.ai/blog?id=qwen3.8-flash-next
"these pelicans" (UD-IQ1_S output) -> tools.simonwillison.net/markdown-svg-renderer#url=...gist.github.com/simonw/f9c69ebdab90d8a45b8de4742cc7b840
"these" (UD-Q2_K_XL output) -> tools.simonwillison.net/markdown-svg-renderer#url=...gist.github.com/simonw/6ba7cbfc1a9336986703b41f7fccd73a
Hacker News discussion -> news.ycombinator.com/item?id=49448210

Source: simonwillison.net/2026/Aug/26/qwen38-flash-next/
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-qwen38-27b-overthinking.md`,
`blog-latentspace-ainews-qwen38-max-27b-launch.md`,
`blog-google-qwen35-ironwood-moe-optimization.md`, and
`blog-google-qwen3-embedding-tpu-precision.md` were each re-read directly
and the specific claim numbers cited below were confirmed against each
note's numbered `### Claim N:` headings in document order before writing
this section, per MINER.md §4b. The corpus was additionally keyword-searched
for "Qwen3.8", "Qwen 3.8", "DGX Spark", and "reasoning effort" across
`source-notes/*.md` to catch same-model and same-hardware notes a
topic-only scan would miss.

- **Corroborates**:
  - `blog-simonwillison-qwen38-27b-overthinking.md` Claim 1 (Qwen 3.8 27B
    exposes an `xhigh`/`medium`/`low` `reasoning_effort` scheme, defaulting
    to `xhigh`): Claim 4 here confirms `xhigh` also exists as a
    reasoning-effort setting on this separate, newer Qwen3.8-Flash-Next
    model, extending the naming scheme to a third Qwen model generation
    within this corpus (Qwen3.8-Max, Qwen3.8-27B, now Qwen3.8-Flash-Next).
    This note cannot confirm whether `xhigh` is Qwen3.8-Flash-Next's
    *default* the way the companion note establishes for Qwen3.8-27B — the
    source simply doesn't say.
  - `blog-google-qwen35-ironwood-moe-optimization.md` Claim 3 (Qwen
    3.5-397B: "512 experts, top-10 routing, plus one always-on shared
    expert"): Claim 6 here (Unsloth's "512" experts, "10 Routed + 1 Shared"
    for Qwen3.8-Flash-Next) corroborates the same 512-expert,
    top-10-plus-shared MoE routing shape carrying across at least two Qwen
    generations at very different total-parameter scales.

- **Contradicts**: None filed. No candidate tension was identified between
  this source and any existing note — the "125B tokens" wording flagged in
  Claim 2 is treated as an apparent terminology slip within the source
  itself (reconciled against the same post's own linked quantization page,
  Claim 5), not a substantive disagreement between two sources or two claims
  that would lead to different guide advice, so MINER.md §4a's
  contradiction-filing bar is not met.

- **Extends**:
  - `blog-simonwillison-qwen38-27b-overthinking.md` (the corpus's detailed,
    ten-days-earlier hands-on Qwen 3.8 27B evaluation by the same author, on
    the same DGX Spark hardware, using the same pelican-riding-a-bicycle
    benchmark prompt): this note is a much thinner companion data point for
    a different, newer Qwen3.8 model (Flash-Next, MoE, multimodal) rather
    than the 27B dense model covered there. Where that note supplies timed,
    token-counted, multi-task evidence (reasoning-cost measurements,
    bounding-box vision tests, a Pi coding-agent session, throughput
    figures), this note supplies none of those for Flash-Next — only two
    named quantizations tried and one favored image output. Practitioners
    should not read this note as providing Flash-Next-specific performance
    or cost evidence comparable to the 27B post's depth.
  - `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 11
    (TeortaxesTex's speculation about a route "from flagship capability to
    laptop-deployable specializations" via the Qwen3.8-27B release): this
    note's Flash-Next model is a separate, third release in the same Qwen
    3.8 family (alongside Max and 27B), and Claim 1 here (Qwen framing it as
    "an early preview of the architecture used in Qwen4") suggests Qwen's
    3.8-generation releases are serving partly as architecture previews for
    the next generation, not purely as standalone products — a framing not
    previously present in this corpus's Qwen coverage.

- **Novel**:
  - **Qwen3.8-Flash-Next's existence and self-described positioning as an
    "early preview of the architecture used in Qwen4"** (Claim 1): entirely
    new to the corpus — no prior note documents this specific model or any
    forward reference to Qwen4.
  - **The specific Unsloth GGUF quantization ladder and architecture
    breakdown for this model** (Claims 5-8): new to the corpus at this level
    of Flash-Next-specific detail, though architecturally similar in shape
    (512-expert MoE) to the already-documented Qwen 3.5-397B.
  - **The near-total absence of performance/timing/quality evidence in a
    Willison Qwen post**: worth flagging as a pattern break rather than a
    claim — every other Willison Qwen source note in this corpus
    (`blog-simonwillison-qwen38-27b-overthinking.md`) includes concrete
    timing, token-count, or throughput figures; this one includes none,
    consistent with the site's own "link post" categorization of this
    particular entry (see Concrete Artifacts, final paragraph of the post).

## Guide Impact

- **No direct chapter update recommended from this source alone.** Unlike
  `blog-simonwillison-qwen38-27b-overthinking.md`, which supplied concrete,
  citable figures for Chapter 02 (reasoning-effort defaults) and Chapter 04
  (local throughput expectations), this post supplies no comparable
  measurement for Qwen3.8-Flash-Next: no reasoning-effort default confirmed,
  no timing, no token/second figure, no task-completion evidence. The one
  Chapter 04 (Model Selection & Cost)-relevant fact worth a citation if the
  guide ever surveys the current open-weight MoE model landscape is the
  quantization-ladder data point in Claim 8 (a 125B-total/6B-active MoE
  model quantizes down to 72.5GB, fitting a single DGX Spark-class machine)
  — but this alone does not justify a standalone guide addition; it is
  better folded into a future, more substantive Flash-Next-specific source
  (e.g. if Willison or another practitioner publishes a follow-up with
  actual throughput/quality measurements) rather than cited from this thin
  post in isolation.

## Extraction Notes

- **Fetch method and its limits**: `simonwillison.net` was fetched via
  WebFetch (this Miner did not have `curl` access in this run). WebFetch's
  own small-model summarizer initially declined to reproduce the page
  verbatim (citing copyright concerns) on a first attempt; targeted
  follow-up prompts asking for specific short passages (the opening
  sentence, the quantization-and-file-size sentence, the "favorite" sentence,
  and a full paragraph-by-paragraph listing) succeeded and are cross-checked
  against each other for consistency above — the paragraph-by-paragraph
  listing and the targeted single-sentence quotes agree word-for-word on
  every overlapping passage, giving reasonable confidence these are genuine
  verbatim extracts rather than paraphrases, though this Miner could not
  independently verify byte-for-byte against raw HTML the way prior notes in
  this corpus did via direct `curl` access.
- **Sub-pages followed**: the linked Unsloth GGUF model card
  (`huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF`) was fetched and is the
  source for Claims 5-8 and the quantization-size table, clearly attributed
  to Unsloth rather than to Willison or Qwen directly. The linked Qwen
  announcement (`qwen.ai/blog?id=qwen3.8-flash-next`) was attempted but
  returned no retrievable body content (the fetch tool reported only the
  single word "Qwen," consistent with a JavaScript-rendered page WebFetch
  could not execute) — Claim 1's "early preview of the architecture used in
  Qwen4" framing could not be independently verified against Qwen's own
  primary announcement as a result, and is sourced here only as relayed by
  Willison. The linked Hacker News discussion
  (`news.ycombinator.com/item?id=49448210`) returned HTTP 429 (rate-limited)
  on two separate attempts and was not read; no community-reaction claims
  are extracted from it as a result. Per MINER.md §1's up-to-5-linked-page
  budget, 2 of the post's linked pages were successfully fetched (Unsloth,
  attempted-but-empty Qwen blog) and 1 was attempted and blocked (Hacker
  News); the two linked pelican-SVG-output gists/renderer pages were treated
  as supporting image artifacts already covered via the alt-text extraction
  in Concrete Artifacts, not as separate substantive pages to mine.
- **Source is genuinely thin — not a skimming artifact.** This note's small
  claim count relative to the corpus's densest Qwen notes
  (`blog-simonwillison-qwen38-27b-overthinking.md`, 11 claims;
  `blog-latentspace-ainews-qwen38-max-27b-launch.md`, 12 claims) reflects the
  primary source's actual length (7 short paragraphs total, one of which is
  a sponsorship pitch) rather than incomplete extraction — all four
  substantive paragraphs of the post are represented as Claims 1-4, with
  Claims 5-8 supplying independently-sourced background architecture detail
  from the one linked page that rendered successfully.
- **Triage inconsistency observed on the source issue.** Issue #3153 carries
  three separate Prospector "Triage Assessment" comments with differing
  novelty ratings (high, low, medium) and differing lists of overlapping
  existing notes — apparently duplicate triage runs rather than a single
  assessment. This Miner proceeded per the task instructions (extract
  regardless) and independently arrived at an assessment closest to the
  "low novelty" comment's characterization ("a very brief 'link blog' post
  ... primarily a model announcement rather than practitioner insight or
  failure pattern"), for the reasons detailed throughout this note. Flagged
  here for the Assayer in case the triage duplication itself is worth
  reporting upstream.
- **Confidence rationale**: rated `anecdotal` overall. Claims 1-4 (from
  Willison's own post) are single-practitioner, single-session, largely
  unelaborated observations with no measurement methodology — the weakest
  tier of evidence this corpus uses. Claims 5-8 (from the linked Unsloth
  page) are individually more concrete and independently checkable
  (`settled` for the directly observable file-size table, `emerging` for
  the architecture/sampling-parameter claims relayed from a third-party
  quantization provider rather than Qwen's own primary documentation), but
  do not lift the note-level rating given the primary source itself
  (Willison's post, which this issue was filed to extract) contributes only
  anecdotal-tier claims.
