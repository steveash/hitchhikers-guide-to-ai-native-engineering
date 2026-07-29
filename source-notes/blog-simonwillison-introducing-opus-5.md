---
source_url: https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/
source_type: blog-post
title: "Introducing Claude Opus 5"
author: Simon Willison
date_published: 2026-07-24
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2287"
---

# Introducing Claude Opus 5

> Simon Willison's same-day link post on Anthropic's Claude Opus 5 launch: a
> leaderboard-leading, same-priced-as-Opus-4.8 frontier model whose most
> notable anecdote is autonomously writing its own computer-vision pipeline to
> reconstruct a machine part it was deliberately prevented from viewing
> directly, paired with Anthropic's disclosure that Opus 5 improved at
> *finding* vulnerabilities but was deliberately not trained on *exploiting*
> them.

## Source Context

- **Type**: blog-post (simonwillison.net, July 24, 2026 — a same-day link
  post, ~250 words, written before Willison had run his own hands-on testing).
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  and the `llm` Python CLI, and a trusted-feed source in this corpus with
  extensive prior coverage of Claude releases, including Fable 5's launch
  (`blog-simonwillison-claude-fable-5.md`) and its proactive-agent behavior
  (`blog-simonwillison-fable-relentlessly-proactive.md`). No Anthropic
  affiliation. Unlike those two posts, this is explicitly *not* a hands-on
  evaluation: Willison states he had not yet tested the model himself and is
  relaying Anthropic's own announcement plus links to related material.
- **Scope**: Covers the Opus 5 launch announcement at a summary level —
  leaderboard position, pricing, the FreeCAD/computer-vision anecdote (quoted
  from Anthropic's post), the vulnerability-detection-vs-exploitation
  disclosure, and pointers to Anthropic's prompting guide and Thariq
  Shihipar's context-engineering post. Does NOT cover: Willison's own
  independent testing of Opus 5 (he explicitly had not done this yet), formal
  benchmark methodology behind the Artificial Analysis leaderboard position,
  or any detail on Opus 5's context window/output token specs (not
  mentioned in this post, unlike the Fable 5 launch post).

## Extracted Claims

### Claim 1: Willison had not yet tested Opus 5 himself at the time of writing, due to being offline for unrelated reasons
- **Evidence**: Willison's direct, first-person disclosure at the top of the post.
- **Confidence**: settled (a first-person statement of fact about the author's own activity, not a claim requiring external verification)
- **Quote**: "I've been offline kayaking with sea otters for much of today so I haven't had a chance to put Anthropic's new model Claude Opus 5 through its paces yet."
- **Our assessment**: This is an important scoping signal, not a substantive claim: it means the rest of the post reports Anthropic's own announcement and Willison's editorial framing of it, not independent hands-on verification of the kind he provided for Fable 5 (`blog-simonwillison-claude-fable-5.md`) two days after that launch. The guide should treat the capability claims in this post as vendor-asserted-plus-editorial-curation, not as independently replicated by Willison, and should watch for a follow-up hands-on post.

### Claim 2: Opus 5 is currently leading the Artificial Analysis leaderboard, ahead of Claude Fable 5
- **Evidence**: Willison's direct statement, linked to an Artificial Analysis social-media post as the source of the leaderboard claim.
- **Confidence**: emerging (a specific, checkable leaderboard-position claim, but sourced to a third-party benchmark aggregator's post rather than a named benchmark methodology reproduced in this article)
- **Quote**: "It's currently leading the Artificial Analysis leaderboard, in front of even Fable 5."
- **Our assessment**: This is a notable model-class-positioning data point: Opus 5, priced at the Opus 4.8 tier (see Claim 3), reportedly outranks Fable 5, which is priced at 2x Opus 4.8 (`blog-simonwillison-claude-fable-5.md` Concrete Artifacts). If accurate, this reshapes the price/performance frontier documented in `blog-anthropic-choosing-claude-model.md` Claim 4 (Opus positioned for "reasoning-intensive enterprise tasks," Fable/Mythos as the frontier tier) — a same-priced-as-Opus-4.8 model beating the 2x-priced Fable 5 on a general leaderboard would argue for defaulting to Opus 5 before reaching for Fable 5, pending task-specific eval confirmation per that note's Claim 9 (benchmark saturation caveat for powerful models).

### Claim 3: Opus 5 is priced the same as Claude Opus 4.8, and continues to offer a "fast mode" at twice the base price
- **Evidence**: Willison's direct statement of the pricing structure.
- **Confidence**: settled (a specific, first-party-sourced pricing fact, consistent with the established Anthropic fast-mode pricing pattern already documented in this corpus)
- **Quote**: "It's priced the same as Opus 4.8, and continues to offer a "fast mode" at twice the cost of the base model."
- **Our assessment**: This confirms Opus 5 did not introduce a new price tier over Opus 4.8, and that the fast-mode-at-2x-base-price convention (documented for Opus 4.8 in `blog-simonwillison-llm-anthropic-0251.md` Claim 5, and for its Copilot rollout in `docs-github-copilot-opus48-fast-mode-preview.md` Claim 6, both citing $10/$50 per MTok base pricing) carries forward unchanged into the Opus 5 generation. Combined with Claim 2 (leaderboard lead over the pricier Fable 5), this is a strong signal for the guide's model-selection chapter: no price increase accompanied this capability jump, unlike the Opus 4.6→4.7 and Opus 4.8→Fable 5 transitions, which did raise prices (`blog-simonwillison-gemini35-flash-pricing.md` Claim 5; `blog-simonwillison-claude-fable-5.md` Concrete Artifacts).

### Claim 4: Opus 5 was given a drawing of a machine part and asked to write code to rebuild it as a 3D FreeCAD model, but was deliberately given no way to directly view the drawing
- **Evidence**: Willison quotes (or closely paraphrases from) Anthropic's own announcement describing the task setup.
- **Confidence**: emerging (a specific anecdote relayed from Anthropic's announcement, not independently reproduced or verified by Willison in this post)
- **Quote**: "Opus 5 was given a drawing of a machine part and asked to write code to rebuild it as a 3D FreeCAD model."
- **Quote (constraint)**: "the model was intentionally given no way to directly view the drawing"
- **Our assessment**: The deliberate removal of direct visual access is the load-bearing detail — it converts this from a routine vision-to-CAD task into a test of whether the model would proactively work around a missing capability rather than fail or ask for help. This is the same behavioral signature Willison documented for Fable 5 in `blog-simonwillison-fable-relentlessly-proactive.md` Claim 2 (inventing a PyObjC/Quartz workaround when `osascript` was blocked) and Claim 3 (building its own CORS server rather than stopping to ask) — a pattern of autonomously constructing missing tooling to route around a blocked capability, now observed in the next model generation on a completely different task domain (CAD/vision vs. OS/browser debugging).

### Claim 5: Faced with no direct viewing access, Opus 5 wrote its own computer vision pipeline to extract geometry from the raw pixels, then reconstructed the full machine part
- **Evidence**: Willison's direct quote of the outcome, relayed from Anthropic's announcement.
- **Confidence**: anecdotal (a single vendor-supplied anecdote, relayed rather than independently tested by Willison in this post; no image, code, or reproducible artifact is included in this article)
- **Quote**: "Opus 5 responded by writing its own computer vision pipeline to pull the geometry from the raw pixels, then reconstructed the full machine part."
- **Our assessment**: This is the headline capability anecdote of the post and the clearest evidence of "proactive, self-directed problem solving" carrying forward into Opus 5. It directly extends the "relentlessly proactive" pattern established for Fable 5: the model treats a missing tool/capability as an obstacle to build around rather than a task-blocking constraint. Because this is a single vendor-supplied anecdote with no reproducible artifact (unlike the Fable 5 CORS-server code Willison reproduced verbatim in `blog-simonwillison-fable-relentlessly-proactive.md`), the guide should cite it as illustrative of a now-recurring pattern across two model generations, not as an independently verified benchmark result.

### Claim 6: Opus 5 improved at detecting security vulnerabilities through general capability gains, but remains substantially behind Claude Mythos 5 at exploiting those vulnerabilities
- **Evidence**: Willison's direct quote, relaying Anthropic's disclosure about the model's relative capability and the deliberateness of the training choice.
- **Confidence**: emerging (a specific, vendor-disclosed capability-and-training-choice claim; the "substantially behind" comparison to Mythos 5 is not quantified with a benchmark score in this post)
- **Quote**: "it remains substantially behind Mythos 5 on the _exploitation_ of those vulnerabilities—that is, in turning vulnerabilities into material cyber threats."
- **Our assessment**: This is the most consequential claim in the post for risk modeling and the least independently verifiable, since it rests entirely on Anthropic's own framing of what it chose not to train the model on. It is consistent with the model-class access-gating pattern already in the corpus — Mythos is restricted to organizations under "Project Glasswing" (`blog-anthropic-choosing-claude-model.md` Claim 6) — and with the general trend that vulnerability-finding capability rises with general model capability even in sub-frontier, publicly available models (`blog-anthropic-ai-accelerated-offense.md` Claim 2). The distinction between *finding* and *exploiting* vulnerabilities is the same framing Anthropic uses in its defensive-tooling case studies (`blog-anthropic-opus-cybersecurity-partners.md`, covering Opus-powered continuous pentesting deployments) — this claim extends that same finding/exploiting split to describe a deliberate capability gap engineered into the model itself, rather than a deployment-context restriction. The guide should flag that "deliberately not trained on exploitation" is a training-time policy choice asserted by the vendor, not something a practitioner can verify from outside, and should track whether independent red-teaming (e.g., a future AISI or third-party evaluation, per `blog-simonwillison-aisi-gpt55-cyber.md`) corroborates or contradicts the "substantially behind Mythos 5" framing.

### Claim 7: Anthropic published a dedicated prompting guide specifically for Claude Opus 5
- **Evidence**: Willison links to the guide with a one-sentence mention.
- **Confidence**: settled (a link to a first-party, publicly accessible artifact; existence is directly checkable)
- **Quote**: "Anthropic have published a prompting guide for Claude Opus 5."
- **Our assessment**: Willison offers no commentary on the guide's contents in this post — this is a pointer, not an extraction of the guide itself. The guide's URL (`platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5`) is a candidate for a dedicated future source-note mining pass; this note does not extract its contents since Willison's post does not summarize or quote from it.

### Claim 8: Thariq Shihipar (Anthropic) published a companion post on context engineering for Claude 5-generation models, which Willison links to without excerpting
- **Evidence**: Willison's one-sentence pointer to the companion post, published the same day.
- **Confidence**: settled (a link to a first-party artifact already independently mined in this corpus)
- **Quote**: "Thariq Shihipar has also written The new rules of context engineering for Claude 5 generation models."
- **Our assessment**: This companion post is already extracted in full in `blog-anthropic-context-engineering-claude-5.md` (issue #2218, also published 2026-07-24) — the same-day pairing confirms the two posts were part of a coordinated Opus 5 launch communication (product announcement + practitioner-facing prompting/context-engineering guidance). No new claims to extract here beyond confirming Willison treated it as launch-adjacent reading; readers should go to that note directly for the 14 claims it contains (system-prompt reduction, rules-to-judgment shift, `claude doctor`, etc.).

## Concrete Artifacts

### Opus 5 launch summary (from the article, as relayed/quoted by Willison)
```
Source: Simon Willison, simonwillison.net/2026/Jul/24/introducing-claude-opus-5/

- Leaderboard: "currently leading the Artificial Analysis leaderboard, in
  front of even Fable 5"
- Pricing: "priced the same as Opus 4.8, and continues to offer a 'fast
  mode' at twice the cost of the base model"
- FreeCAD anecdote: given a machine-part drawing, asked to rebuild it as a
  3D FreeCAD model, "intentionally given no way to directly view the
  drawing" -> "wrote its own computer vision pipeline to pull the geometry
  from the raw pixels, then reconstructed the full machine part"
- Cybersecurity: "it remains substantially behind Mythos 5 on the
  _exploitation_ of those vulnerabilities—that is, in turning
  vulnerabilities into material cyber threats" (vulnerability *detection*
  improved via general capability gains; exploitation capability was
  reportedly not trained for)
- Linked resources: official Anthropic announcement
  (anthropic.com/news/claude-opus-5), prompting guide for Claude Opus 5
  (platform.claude.com), "The new rules of context engineering for Claude 5
  generation models" (claude.com/blog, Thariq Shihipar)
```
*Source: Simon Willison, simonwillison.net/2026/Jul/24/introducing-claude-opus-5/*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-anthropic-0251.md` Claim 5 and
    `docs-github-copilot-opus48-fast-mode-preview.md` Claim 6 (fast mode
    priced at 2x the base model's rate): Claim 3 in this source confirms the
    same 2x fast-mode multiplier carries into the Opus 5 generation at the
    Opus 4.8 base price point.
  - `blog-simonwillison-fable-relentlessly-proactive.md` Claims 2 and 3
    (Fable 5 autonomously invented workarounds — a PyObjC/Quartz OS API
    substitute, and its own CORS server — when blocked from a direct
    approach): Claims 4–5 in this source document the same proactive
    workaround-construction pattern in Opus 5 on a distinct task domain
    (vision/CAD rather than OS/browser debugging), suggesting this is a
    cross-generation, cross-domain model behavior rather than a one-off.
  - `blog-anthropic-ai-accelerated-offense.md` Claim 2 (sub-frontier,
    publicly available models already find serious vulnerabilities missed by
    traditional code review): Claim 6 in this source is consistent with this
    — vulnerability-*detection* capability rising with general model
    capability, independent of any deliberate exploitation training.
  - `blog-anthropic-opus-cybersecurity-partners.md` (partner case studies of
    Claude Opus deployed for continuous vulnerability detection and
    remediation): Claim 6's finding/exploiting distinction is consistent
    with that note's framing of Opus as a detection-and-remediation tool
    rather than an offensive-exploitation tool, though that note covers an
    earlier Opus generation's deployment context rather than a
    training-time disclosure about the model itself.

- **Extends**:
  - `blog-anthropic-choosing-claude-model.md` Claim 6 (Mythos restricted to
    organizations under "Project Glasswing") and Claim 4 (Opus positioned
    for reasoning-intensive enterprise tasks, Fable/Mythos as the frontier,
    dual-use-gated tier): Claim 6 in this source adds a training-time
    mechanism to that access-gating story — Mythos's exploitation-capability
    edge over Opus 5 is presented as partly a deliberate training choice, not
    solely an access-control policy. Claim 2 (Opus 5 leading the leaderboard
    ahead of the pricier Fable 5) extends the price/performance
    considerations in that note's Claim 7 (effort level as a second cost
    axis) and Claim 8 (advisor-strategy cost/quality tradeoffs) with a new
    data point: a same-priced-as-4.8 model reportedly outperforming a
    2x-priced sibling.
  - `blog-anthropic-context-engineering-claude-5.md` (the companion post
    Willison links to, already fully extracted in this corpus): this source
    provides the launch-day framing and anecdotal capability evidence that
    contextualizes why Anthropic simultaneously published new context-
    engineering guidance for "models like Claude Opus 5 and Claude Fable 5"
    (that note's Claim 1) — a more capable, more autonomous model is the
    stated reason for trusting it with less explicit rule-based guidance.

- **Contradicts**: None identified. No existing source note makes a claim
  that materially conflicts with anything in this post. No contradiction
  issue required.

- **Novel**:
  - **First in-corpus coverage of Claude Opus 5 as a model.** No prior
    source note documents Opus 5's launch, capabilities, pricing, or
    leaderboard position.
  - **First documented instance of the "autonomous workaround construction"
    behavior pattern in a vision/CAD task.** Prior instances in this corpus
    (`blog-simonwillison-fable-relentlessly-proactive.md`) were confined to
    OS-level and browser-automation tasks; the FreeCAD anecdote shows the
    same pattern in a completely different domain (computer vision →
    parametric CAD reconstruction), suggesting the behavior is a general
    model disposition rather than domain-specific.
  - **First explicit vendor disclosure of a deliberate train-time
    finding/exploiting capability gap for a named model pair** (Opus 5 vs.
    Mythos 5). Prior corpus sources document either general vulnerability-
    finding capability trends (`blog-anthropic-ai-accelerated-offense.md`)
    or access-based gating (`blog-anthropic-choosing-claude-model.md`), but
    not a specific claim that a model was deliberately not trained on
    exploitation techniques while its sibling was.

## Guide Impact

- **Chapter 06 (Model Selection/Landscape)**: Add Opus 5 to the model
  comparison table at the Opus 4.8 price point, with the leaderboard
  positioning claim (Claim 2) flagged as third-party-sourced rather than a
  reproduced benchmark. Recommend practitioners currently defaulting to
  Fable 5 for frontier-tier tasks re-run their evals against Opus 5 given the
  no-price-increase, leading-leaderboard-position combination — this is the
  first Opus-tier release in the corpus that is not accompanied by a price
  increase over its predecessor (contrast with the Opus 4.6→4.7 and Opus
  4.8→Fable 5 transitions, both of which raised price).

- **Chapter 02/04 (Harness Engineering / Agent autonomy patterns)**: Add the
  FreeCAD anecdote (Claims 4–5) as a second, cross-domain data point for the
  "agents will autonomously construct missing tooling rather than stop when
  blocked" pattern already documented from Fable 5
  (`blog-simonwillison-fable-relentlessly-proactive.md`). Recommend framing
  this explicitly as a now-recurring model disposition across two
  generations and two task domains, strengthening the guide's existing
  guidance that tool-grant boundaries should assume the model may construct
  equivalent capability from whatever access it does have, rather than
  respecting an implicit "don't build new tools" boundary.

- **Chapter 03 (Verification / Security risk modeling)**: Add Claim 6 (Opus 5
  improved at vulnerability *detection* but was deliberately not trained on
  *exploitation*, unlike Mythos 5) as a data point for the guide's security
  threat-modeling section, explicitly flagged as a vendor-asserted,
  train-time policy claim that is not independently verifiable from this
  source alone. Recommend the guide track this claim for corroboration or
  contradiction from independent red-teaming sources (e.g., a future AISI-
  style evaluation) before treating "Opus-tier models can't meaningfully
  exploit vulnerabilities" as a load-bearing assumption in any risk model.

## Extraction Notes

- This is a short (~250-word) same-day link post, not a hands-on evaluation
  — Willison explicitly states he had not tested Opus 5 himself at the time
  of writing (Claim 1). This changes the epistemic status of the post
  relative to his Fable 5 coverage: the capability claims here are relayed
  from Anthropic's own announcement and are not independently replicated by
  Willison in this article. `confidence_overall` is set to `emerging` rather
  than `anecdotal` because the pricing and leaderboard-link facts are
  directly checkable/settled, while the FreeCAD anecdote and the
  exploitation-training claim are vendor-sourced and unverified by the
  author — a mixed evidence body that does not cleanly fit either `settled`
  or purely `anecdotal`.
- WebFetch returned only summarized paraphrases on unconstrained requests
  (consistent with the pattern noted in prior Willison source notes in this
  corpus); this note's quotes were obtained through multiple separate,
  narrowly targeted WebFetch calls, each requesting one short verbatim
  passage under the tool's ~125-character quote limit. Each quote used in
  this note was independently re-requested and returned with identical
  wording across at least two separate fetch calls before being included.
- This post links to Anthropic's official announcement
  (anthropic.com/news/claude-opus-5), the Opus 5 prompting guide
  (platform.claude.com), and Thariq Shihipar's context-engineering companion
  post (claude.com/blog) — the last of these is already fully mined in this
  corpus as `blog-anthropic-context-engineering-claude-5.md` (issue #2218).
  The official Anthropic announcement itself and the Opus 5 prompting guide
  are not yet mined as of this extraction and are candidates for separate
  future source-note issues; this note does not attempt to extract their
  contents since Willison's post does not quote or summarize them beyond a
  bare link.
- The post also mentions two "pelican riding a bicycle" SVG benchmark
  attempts with linked results ("The first pelican I got was missing the
  bicycle wheels" / "the second attempt was better") but gives no further
  quantified detail (no cost, no token count, no effort-level breakdown as
  in `blog-simonwillison-claude-fable-5.md` Claim 11) — this is not extracted
  as a standalone claim since it carries no assessable evidence beyond
  Willison's brief qualitative note, and the linked SVG outputs themselves
  were not independently viewable through this extraction process.
- Cross-references verified:
  - `blog-simonwillison-llm-anthropic-0251.md` Claim 5: confirmed at that
    note's pricing table for Opus 4.8 fast mode ($10/$50 base, 2x for fast
    mode).
  - `docs-github-copilot-opus48-fast-mode-preview.md` Claim 6: confirmed at
    lines 137–157 of that note (fast mode billed at a premium over standard
    Opus 4.8, 3x reduction vs. prior fast-mode generations).
  - `blog-simonwillison-fable-relentlessly-proactive.md` Claims 2 and 3:
    confirmed at lines 63–99 of that note (PyObjC/Quartz workaround; CORS
    server construction).
  - `blog-anthropic-ai-accelerated-offense.md` Claim 2: confirmed at line 62
    of that note (sub-frontier publicly available models already finding
    serious vulnerabilities).
  - `blog-anthropic-opus-cybersecurity-partners.md`: confirmed at lines
    14–19 and Claim 3 (Wiz Red Agent reasoning "like a human pentester" for
    detection, not exploitation) of that note.
  - `blog-anthropic-choosing-claude-model.md` Claims 4 and 6: confirmed at
    lines 71 and 83–85 of that note (model-class positioning; Project
    Glasswing gating for Mythos).
  - `blog-anthropic-context-engineering-claude-5.md`: confirmed as the
    companion post Willison links to, published the same day (2026-07-24),
    already extracted under issue #2218.
- No contradictions identified. No contradiction issue filed.
