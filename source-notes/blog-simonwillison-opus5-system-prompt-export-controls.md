---
source_url: https://simonwillison.net/2026/Aug/9/claude-opus-5-system-prompt/
source_type: blog-post
title: "A quote from Claude Opus 5 system prompt"
author: Simon Willison
date_published: 2026-08-09
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: settled
issue: "#2774"
---

# A quote from Claude Opus 5 system prompt

> Simon Willison quotes, verbatim, the passage in Claude Opus 5's public system
> prompt that tells the model how to talk about the June 2026 Fable 5/Mythos 5
> export-control suspension — a concrete, verifiable example of Anthropic
> instructing a model to acknowledge a specific post-training-cutoff event
> factually, cite an authoritative source, and actively check for newer
> information rather than deny or hedge.

## Source Context

- **Type**: blog-post (Willison link-blog "quotation" format — a single
  blockquote plus a short attribution line, no independent commentary beyond
  the citation gloss; published August 9, 2026, ~11:31pm)
- **Author credibility**: Simon Willison is the creator of Django and a
  `trusted-feed` source in this corpus with extensive prior coverage of Claude
  system prompts, including a full diff of the Opus 4.6→4.7 system prompt
  (`blog-simonwillison-opus47-system-prompt.md`) and the original Fable
  5/Mythos 5 export-control directive (`blog-simonwillison-fable-mythos-access-directive.md`).
  His contribution here is curation and quotation, not analysis: he surfaces
  a specific passage from Anthropic's own publicly published system prompt
  archive (`platform.claude.com/docs/en/release-notes/system-prompts#claude-opus-5`)
  and adds a one-line editorial gloss. This extraction independently verified
  the quoted text against that archive page directly (see Extraction Notes);
  the wording matches character-for-character across both sources.
- **Scope**: Covers only the single `<product_information>` passage in the
  Opus 5 system prompt that addresses the Fable 5/Mythos 5 export-control
  suspension and restoration. Does NOT cover the rest of the Opus 5 system
  prompt (tool list, other behavioral sections, safety instructions), does
  not diff Opus 5's prompt against Opus 4.8's the way the prior 4.6→4.7 note
  did, and does not cover the underlying export-control incident itself
  (already covered by `blog-simonwillison-fable-mythos-access-directive.md`
  and `blog-simonwillison-fable-5-export-controls.md`).

## Extracted Claims

### Claim 1: The Opus 5 system prompt states the exact dates of the Fable 5/Mythos 5 release, suspension, and restoration, framed as facts Claude would not otherwise know from training data

- **Evidence**: Verbatim quote from the system prompt, independently confirmed
  against Anthropic's public system prompt archive.
- **Confidence**: settled (verbatim, cross-verified against two independent
  fetches of Anthropic's own published archive page)
- **Quote**: "Claude Fable 5 and Claude Mythos 5 were first released on June 9, 2026. On June 12, 2026, Anthropic suspended access to both models to comply with U.S. Department of Commerce export controls; the Department lifted those controls on June 30, 2026, and Anthropic restored access on July 1, 2026 (Anthropic's statement: https://www.anthropic.com/news/fable-mythos-access)."
- **Our assessment**: This is a system prompt functioning as an explicit factual patch for a specific, dated real-world event — not a general "you may be out of date" disclaimer, but the exact dates, the exact regulatory mechanism (Department of Commerce export controls), and a citable link to Anthropic's own statement. This matches and independently confirms the incident timeline already documented in `blog-simonwillison-fable-mythos-access-directive.md` Claims 1 and 8 (directive received, suspension, and Anthropic's compliance-while-disputing posture) — Anthropic appears to have taken the incident it publicly described in June and baked a condensed factual summary directly into the following model generation's system prompt.

### Claim 2: The prompt explicitly states these events are after Claude's training-data cutoff and that Claude knows about them "only from this notice"

- **Evidence**: Verbatim quote, same passage.
- **Confidence**: settled (verbatim, cross-verified)
- **Quote**: "These events are after Claude's training-data cutoff, so Claude knows about them only from this notice."
- **Our assessment**: This is a rare piece of direct, machine-readable evidence about the boundary between what a model "knows" from training vs. what it is told at inference time via the system prompt. It confirms a specific architectural fact: Anthropic patches post-cutoff, high-salience current events into the system prompt itself rather than relying solely on retraining or a general web-search fallback. For practitioners building harnesses around Claude, this is a directly transferable pattern for injecting known-critical, time-sensitive facts (e.g., a company's own recent incident, a policy change, a product rename) that the model would otherwise hallucinate or deny.

### Claim 3: The prompt instructs Claude to confirm the suspension "accurately and matter-of-factly" and explicitly not deny that it happened

- **Evidence**: Verbatim quote, same passage.
- **Confidence**: settled (verbatim, cross-verified)
- **Quote**: "If asked, Claude confirms them accurately and matter-of-factly — it doesn't deny the suspension happened — and otherwise treats the export controls like any other current political topic: it gives a fair, accurate account rather than sharing personal opinions, and points to the linked statement for anything further."
- **Our assessment**: The explicit "it doesn't deny the suspension happened" clause is notable — it suggests Anthropic anticipated (or observed) a failure mode where a model, uncertain about a negative or embarrassing event concerning its own vendor, might default to denial or evasion rather than confirmation. Instructing the model to affirmatively confirm an event that reflects negatively on Anthropic's own product (a forced government suspension) is a specific, verifiable design choice toward accuracy over self-serving hedging. The instruction to treat the topic "like any other current political topic" (fair, accurate account, no personal opinions, defer to the linked source) generalizes the pattern beyond this one incident to a reusable template for handling any politically sensitive current event.

### Claim 4: The prompt instructs Claude to actively check for newer information via search when possible, and otherwise to suggest the user check Anthropic's site directly

- **Evidence**: Verbatim quote, same passage.
- **Confidence**: settled (verbatim, cross-verified)
- **Quote**: "Things may have developed since this notice, so Claude checks for newer information when it can search, and otherwise suggests checking Anthropic's site."
- **Our assessment**: This closes the loop on staleness: the system-prompt-injected fact is explicitly marked as time-bound and superseded by search results when search is available, with a fallback pointer when it is not. This is the delegation pattern referenced in the Prospector's triage comment — the system prompt does not just supply a static fact, it also tells the model how to detect that the fact might now be stale and what to do about it (search, or defer to an external authoritative source). Practitioners injecting time-sensitive facts into their own system prompts should consider including this same two-tier fallback (live tool check, then pointer to an authoritative external source) rather than a bare fact injection with no staleness handling.

### Claim 5: The passage lives inside the `<product_information>` tag of the Opus 5 system prompt, alongside descriptions of Claude's model lineup and products — not in a dedicated safety or current-events tag

- **Evidence**: Confirmed via direct fetch of Anthropic's public system prompt archive page for Claude Opus 5, cross-checked against the Willison blog quote (which does not show the surrounding XML tag, since Willison's blockquote excerpts only the prose).
- **Confidence**: emerging (the tag name and surrounding placement were confirmed via a single independent fetch of the archive page, not independently re-verified with a second fetch the way the prose quote was; see Extraction Notes)
- **Quote**: (no direct quote from Willison's post for the tag name itself; see paraphrase above — the tag name comes from the independently-fetched archive page, not from Willison's post)
- **Our assessment**: Placing an export-control/regulatory-suspension disclosure inside the general `<product_information>` block (rather than, say, a dedicated `<current_events>` or `<safety>` tag) suggests Anthropic treats "which of our models are currently available and why" as part of routine product-lineup information rather than as an exceptional safety disclosure. This is a minor but useful structural data point for practitioners studying how Anthropic organizes system prompt content by category.

## Concrete Artifacts

### Full quoted passage (verbatim, from the Claude Opus 5 system prompt, `<product_information>` section)

```
Claude Fable 5 and Claude Mythos 5 were first released on June 9, 2026. On
June 12, 2026, Anthropic suspended access to both models to comply with U.S.
Department of Commerce export controls; the Department lifted those controls
on June 30, 2026, and Anthropic restored access on July 1, 2026 (Anthropic's
statement: https://www.anthropic.com/news/fable-mythos-access). These events
are after Claude's training-data cutoff, so Claude knows about them only from
this notice. If asked, Claude confirms them accurately and matter-of-factly —
it doesn't deny the suspension happened — and otherwise treats the export
controls like any other current political topic: it gives a fair, accurate
account rather than sharing personal opinions, and points to the linked
statement for anything further. Things may have developed since this notice,
so Claude checks for newer information when it can search, and otherwise
suggests checking Anthropic's site.
```

*Source: Simon Willison, simonwillison.net, August 9, 2026, quoting the
Claude Opus 5 system prompt at
`platform.claude.com/docs/en/release-notes/system-prompts#claude-opus-5`.
Independently confirmed verbatim against a direct fetch of that archive page
during this extraction.*

### Willison's attribution/citation line (his own words, not part of the quoted prompt)

```
— Claude Opus 5 system prompt, ensuring Claude doesn't provide incorrect
  answers about the export controls situation
```

*Source: Simon Willison, simonwillison.net, August 9, 2026.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-fable-mythos-access-directive.md` Claims 1, 2, and 8 —
    that note documents the original June 12, 2026 incident (directive
    received 5:21pm ET, access suspended by 9:59pm ET, Anthropic complying
    while disputing the rationale). This source's Claim 1 confirms the same
    dates (June 9 release, June 12 suspension, June 30 controls lifted, July 1
    access restored) from an entirely independent source (the Opus 5 system
    prompt itself, published roughly two months later) — cross-corroboration
    between Anthropic's contemporaneous public statement and the persistent
    factual summary later embedded in the next model's system prompt.
  - `blog-simonwillison-fable-5-export-controls.md` — that note (Moussouris/
    Willison, June 16, 2026) covers the technical and policy dispute over
    the underlying "jailbreak" that triggered the directive. This source
    does not touch that dispute at all; the system prompt passage is
    scrupulously neutral on the merits ("gives a fair, accurate account
    rather than sharing personal opinions"), which is a notable contrast
    with the strongly-argued practitioner framing in that note.

- **Contradicts**: None identified. No existing corpus note makes a claim
  about Opus 5's system prompt or the export-control timeline that conflicts
  with this source. No contradiction issue filed.

- **Extends**:
  - `blog-simonwillison-opus47-system-prompt.md` — that note diffed the
    Opus 4.6→4.7 system prompt and documented (Claim 13) a knowledge-cutoff
    date bump with no accompanying explanatory mechanism beyond the date
    change itself, plus (Claims 1 and 9) two examples of *stateful,
    within-conversation* behavioral constraints (child safety, disordered
    eating). This source documents a different mechanism entirely: a
    *static, pre-written* factual patch for a specific named event beyond
    the cutoff, with explicit instructions on how to talk about it and how
    to detect staleness. Together the two notes establish that Anthropic
    uses at least two distinct system-prompt techniques for handling
    information beyond the knowledge cutoff — (a) simply move the cutoff
    date forward, and (b) explicitly inject a dated, sourced fact plus
    handling instructions when a specific event is important enough to
    address directly. Neither corpus note previously documented technique
    (b) with a full verbatim example.
  - `blog-simonwillison-introducing-opus-5.md` — that note covers the July 24,
    2026 Opus 5 launch (pricing, leaderboard position, the FreeCAD anecdote,
    the vulnerability-detection-vs-exploitation disclosure) but does not
    mention the system prompt at all. This source, published two weeks
    later, is the corpus's first look at Opus 5's actual system prompt text.

- **Novel**:
  - **First verbatim, cross-verified example in the corpus of a system
    prompt explicitly telling a model not to deny an event that reflects
    negatively on its own vendor.** The "it doesn't deny the suspension
    happened" clause is a specific, checkable instruction not documented
    in any prior corpus source about system-prompt design.
  - **First documented example of a two-tier staleness-handling pattern**:
    inject a dated fact, then instruct the model to actively search for
    newer information when possible and defer to an authoritative external
    URL when not. Prior corpus coverage of knowledge-cutoff handling
    (`blog-simonwillison-opus47-system-prompt.md` Claim 13) documented only
    a bare cutoff-date change, with no equivalent "how to detect this fact
    may now be stale" instruction.
  - **First confirmation that Anthropic files this kind of disclosure under
    `<product_information>` rather than a dedicated safety/current-events
    tag** — a minor structural data point new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — System Prompt Design)**: Add this
  passage as a concrete, reusable template for injecting a specific,
  time-sensitive, potentially-reputationally-awkward fact into a system
  prompt: (1) state the fact with exact dates and a citable authoritative
  URL; (2) explicitly flag it as beyond the model's training cutoff; (3)
  instruct the model to confirm it factually rather than deny or hedge; (4)
  instruct the model to treat contested/sensitive angles neutrally and defer
  to the linked source; (5) instruct the model to check for newer information
  via search when available, and point to the authoritative source otherwise.
  Cite this source alongside `blog-simonwillison-opus47-system-prompt.md` as
  two distinct, verbatim-documented mechanisms Anthropic uses to handle
  post-cutoff information.

- **Chapter 03 (Reliability and Accuracy Beyond Training Cutoff)**: Use
  Claim 2 ("Claude knows about them only from this notice") as direct,
  quotable evidence for the guide's discussion of how vendors patch
  known-critical facts into models between training runs, distinct from
  retraining or general web-search grounding. Practitioners building
  internal harnesses for fast-moving domains (e.g., a company's own recent
  incidents, policy changes, product renames) can use this as a template
  worth adapting for their own system prompts.

## Extraction Notes

- The core quoted passage was verified via two independent methods: (1)
  multiple narrowly-scoped WebFetch calls against Willison's post itself,
  each requesting a short verbatim continuation of the quote (the tool
  truncates or summarizes on broad requests, consistent with the pattern
  noted in prior Willison extractions in this corpus); (2) a separate
  WebFetch of Anthropic's own public system prompt archive page at
  `platform.claude.com/docs/en/release-notes/system-prompts#claude-opus-5`.
  Both independently returned character-for-character identical prose for
  the full passage, which is why `confidence_overall` is set to `settled`
  rather than `emerging` despite this being a single-source blog post — the
  underlying fact (the exact system prompt wording) was independently
  cross-verified against the primary vendor document, not just against the
  secondary blog post.
- The `<product_information>` tag name and its surrounding placement (Claim
  5) come only from the single archive-page fetch, not from Willison's post
  (his blockquote strips XML tags), and were not re-verified with a second
  independent fetch the way the prose was — hence `emerging` confidence on
  that specific claim rather than `settled`.
- Willison's post itself is extremely short (one blockquote plus a one-line
  citation gloss) — there is no additional editorial commentary from him to
  extract beyond the attribution line captured in Concrete Artifacts. The
  post's "Recent articles" sidebar links were not followed as substantive
  content; they are auto-generated related-post suggestions, not part of
  the article body. A sponsor link ("auth.md by WorkOS") appears at the top
  of the page — this is a standard ad on Willison's blog, unrelated to the
  article content, and is not extracted as a claim.
- No linked sub-pages beyond the two already covered (Anthropic's statement
  at `anthropic.com/news/fable-mythos-access`, already extracted in
  `blog-simonwillison-fable-mythos-access-directive.md`; and the system
  prompt archive page itself, fetched directly for this note) warranted
  independent extraction.
- No contradictions identified against the existing corpus; none filed.
