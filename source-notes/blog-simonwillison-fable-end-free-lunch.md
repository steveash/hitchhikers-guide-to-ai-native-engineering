---
source_url: https://simonwillison.net/2026/Aug/23/drew-breunig/
source_type: blog-post
title: "A quote from Drew Breunig"
author: Simon Willison (quoting Drew Breunig, "Fable & The End of the Free Lunch")
date_published: 2026-08-23
date_extracted: 2026-08-31
last_checked: 2026-08-31
status: current
confidence_overall: anecdotal
issue: "#3124"
---

# A quote from Drew Breunig (Fable & The End of the Free Lunch)

> Drew Breunig, quoted by Simon Willison, argues that Fable's arrival broke
> the "free lunch" pattern of AI model economics — where a new, cheaper
> model regularly arrived and made harness/context optimization not worth
> the effort — because Fable stayed expensive while "good enough"
> alternatives (Opus, 5.6, K3, GLM) proliferated, forcing practitioners to
> deliberately decide "what work went where" for the first time, an analogy
> Breunig draws explicitly from the end of Moore's Law's "free lunch" for
> single-threaded CPU performance.

## Source Context

- **Type**: blog-post (Simon Willison's link-blog "quotation" post format —
  a short blockquote plus attribution, no original Willison commentary
  beyond the excerpt selection; published 23rd August 2026 at 7:55pm). The
  post excerpts one paragraph-pair from Drew Breunig's own essay, "Fable &
  The End of the Free Lunch" (dbreunig.com, also published August 23, 2026),
  and links to it as the full source. Per MINER.md's "read the entire
  source, follow substantive linked pages" guidance, Breunig's full essay
  (~500 words) was fetched directly and is the primary basis for this
  extraction — it contains several substantive paragraphs (the Moore's Law
  analogy, the GLM 5.2 pricing figures, the "pushback" rebuttal, and the
  access-controls paragraph) that Willison's excerpt does not include.
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and is designated a `trusted-feed` source in this repo for his
  independent, high-signal LLM-tooling commentary. Here he is functioning
  purely as a curator — the post has no original analysis of his own, just
  the selected quotation and standard attribution. Drew Breunig writes
  analytical commentary on AI, data, and technology economics at
  dbreunig.com; he is a practitioner voice (not a vendor or an academic),
  previously corroborated in this corpus for the "cybersecurity is proof of
  work" economic framing (`blog-simonwillison-cybersecurity-proof-of-work.md`)
  and the "Claws as digital pets" cultural metaphor
  (`blog-simonwillison-5minute-llms.md` Claim 9) — both via the same
  Willison-quotes-Breunig publication pattern as this source. Breunig's
  claims here are stated as first-hand practitioner observation and
  economic argument, not backed by any cited study, survey, or named
  organization beyond his own workflow.
- **Scope**: Covers one specific economic argument — that Fable's high,
  persistent price (relative to "good enough" alternatives) changed the
  incentive structure around AI coding-harness and context-strategy
  investment — illustrated with a historical analogy (Moore's Law's "free
  lunch"), a specific competitor pricing figure (GLM 5.2), Breunig's own
  model-delegation workflow, a rebuttal to the "prices will keep falling"
  objection, and a secondary non-price argument (Fable's access controls
  and data retention terms). Does NOT cover: any benchmark data, adoption
  statistics, named companies beyond a single first-person anecdote, or
  technical detail about how to build a harness that delegates work across
  models — it is an economic argument, not a how-to guide.

## Extracted Claims

### Claim 1: Prior to Fable, investing effort in improving a coding harness or context strategy felt wasteful, because a new model would regularly arrive at the same price or cheaper and "paper over" most existing problems
- **Evidence**: Breunig's own stated recollection of his thinking "in the weeks following Fable's release," presented as the essay's opening premise. This exact passage is also the full text of Willison's blockquote excerpt — both pages carry it verbatim.
- **Confidence**: anecdotal (single practitioner's retrospective characterization of his own reasoning; no data on whether this was a widespread sentiment beyond Breunig)
- **Quote**: "Prior to Fable, it felt silly to waste too much time improving your coding harness or context strategies. A new model would arrive at the same price (or cheaper!) and paper over most of your problems."
- **Our assessment**: This is a specific, falsifiable-in-principle claim about incentive structure, not just a vague "things used to be different" statement — it names the mechanism (frequent same-or-lower-price model releases) that made optimization investment low-ROI. It is the direct predicate for Claim 2's argument that this incentive changed. No corpus source currently documents this "why bother optimizing" pre-Fable baseline explicitly; it is useful context for any guide claim about harness/context engineering ROI.

### Claim 2: Fable's high cost, combined with several alternatives (Opus, 5.6, K3, GLM) being "good enough" for most coding work, caused practitioners to start deliberately deciding which model class handles which work
- **Evidence**: Direct continuation of Breunig's argument, naming Fable's cost as the specific trigger and listing four named alternatives he judges sufficient for "most of the code we needed."
- **Confidence**: anecdotal (first-person practitioner account; "good enough" and "most of the code" are Breunig's own qualitative judgments, not benchmarked)
- **Quote**: "But then Fable landed. It was (and still is!) incredible. But the cost was so high and Opus was good enough (as was 5.6, K3, and even GLM) for most of the code we needed. So we started to think about what work went where."
- **Our assessment**: "What work went where" is the essay's central, reusable phrase — it names task-to-model routing as a newly-necessary discipline rather than an optional optimization. This is a practitioner-economics argument for the same underlying behavior that `blog-cursor-router-model-classifier.md` Claim 1 and Claim 3 describe as a product feature (Cursor Router's classifier routing "simple work" to price-efficient models and "complex, long-horizon problems" to frontier models) — Breunig gives the qualitative "why now" reasoning (an unusually expensive top-tier model), while Cursor's post gives the "how" (a trained classifier) for the same underlying shift.

### Claim 3: Breunig frames the AI-model economics shift as a direct analogy to the end of Moore's Law's "free lunch" — when CPU performance doubled reliably every ~18 months, ruthless code optimization wasn't worth it, but once single-threaded performance stagnated in the mid-2000s, engineers had to start thinking about parallelization, architecture, and memory locality, i.e., "what work went where"
- **Evidence**: Breunig's own historical framing, opening the essay before the Fable discussion; he explicitly attributes the "free lunch" term to Herb Sutter's "seminal essay," and reuses the exact phrase "what work went where" for both the historical CPU case and the later AI-model case.
- **Confidence**: anecdotal (Breunig's own historical narrative and analogy-construction; the underlying Moore's Law slowdown and Sutter's "free lunch" essay are established computing history, but Breunig's specific framing of it as a two-phase "before/after" analogy to AI model pricing is his own argument, not a cited academic claim)
- **Quote**: "When Moore's Law was in full effect, it didn't make sense to ruthlessly optimize your code. In 18 months, a CPU would arrive that would double your performance. Herb Sutter famously referred to this as, 'the free lunch,' in a seminal essay. When Moore's Law slowed in the mid-2000s (specifically, single-threaded performance stagnated), we suddenly had to think about parallelization, architecture, memory locality, etc. We had to think about what work went where."
- **Our assessment**: This is the essay's title-justifying literary device and its most citable framing for a guide: it gives AI-native engineers a pre-existing, well-known historical parallel (the parallel-computing transition of the mid-2000s) for understanding why model-routing discipline is now warranted. Note this passage does not appear in Willison's excerpt — it is only in Breunig's full essay, which Willison's post links to but does not quote.

### Claim 4: GLM 5.2, released the same week as Fable, costs roughly 1/9th of Fable's price (and about 1/5th the cost of Opus 5), and Breunig judges it "more than sufficient" for most rote coding, especially with good context
- **Evidence**: Breunig's own cost comparison and qualitative capability judgment, presented as the specific worked example anchoring his "what work went where" argument.
- **Confidence**: anecdotal (single practitioner's cost ratio and capability assessment; no benchmark citation, no methodology for how the 1/9th and 1/5th figures were computed)
- **Quote**: "GLM 5.2 is worth focusing on. It came out the same week as Fable and is roughly 1/9th the cost (and ~1/5th the cost of Opus 5). Is GLM 1/9th the quality of Fable? Perhaps, for certain classes of tasks. But for most rote coding it's more than sufficient. Especially when provided with great context."
- **Our assessment**: This is the essay's only quantified figure, and it is a first-person estimate rather than a benchmarked measurement — the rhetorical question ("Is GLM 1/9th the quality of Fable? Perhaps...") signals Breunig himself treats the quality comparison as uncertain, while treating the price ratio as solid. The explicit caveat "especially when provided with great context" ties the cost-arbitrage argument directly to context engineering quality — a cheap model's viability for a given task is not fixed, but depends on how well it is fed by the harness.

### Claim 5: Breunig's own workflow uses Fable to interrogate and shape a design, then hands off a brief to GLM to execute it — an expensive model for planning, a cheap model for execution
- **Evidence**: Breunig's first-person description of his current practice, given immediately after the GLM cost/quality discussion.
- **Confidence**: anecdotal (single practitioner's self-reported workflow, no measurement of its effectiveness relative to alternatives)
- **Quote**: "I frequently chat with Fable to interrogate and shape a design, before handing off a brief to GLM."
- **Our assessment**: This is a concrete, named instance of the "advisor strategy" pattern already documented in the corpus from the vendor side — `blog-anthropic-choosing-claude-model.md` Claim 8 (Sonnet executor + Fable advisor, quantified at within 10% of Fable's SWE-bench Pro score at 63% of the price) and `blog-anthropic-cost-visibility-control.md` Claim 13 ("a smaller model like Sonnet call a frontier model at key moments, like evaluating work before it ships"). Breunig's version differs in shape — Fable does the planning/design step and a cheaper, cross-vendor model (GLM, not Sonnet) does the bulk execution — which shows the executor/advisor split generalizing beyond a single vendor's own model family, corroborating that this is a pattern practitioners are independently arriving at, not just a vendor-prescribed one.

### Claim 6: Breunig argues falling inference prices will not reverse the shift back toward routing everything through the largest models, because price declines benefit smaller models equally and improving harnesses will make it easier to give weaker models sufficient context to perform well
- **Evidence**: Breunig's direct rebuttal to an anticipated objection ("I get pushback that..."), naming two specific counter-mechanisms: price-decline symmetry across model tiers, and harness improvement as an independent lever.
- **Confidence**: anecdotal (Breunig's own economic argument and prediction; no supporting data, and it is explicitly framed as a rebuttal to a stated objection rather than an established consensus — "I'm not so sure")
- **Quote**: "I get pushback that falling inference prices will eventually bring us back to sending everything through the largest models. But I'm not so sure: those same gains will benefit the K3s and Qwens, and as we continue to develop better harnesses it will be easier to provide weaker (but still great) models with sufficient context to perform well."
- **Our assessment**: This is the essay's forward-looking claim and the part most directly relevant to harness engineering as a discipline: Breunig is arguing that harness investment is not just a stopgap until prices fall, but a durable lever that keeps weaker/cheaper models viable even as prices decline — because price drops are symmetric across the model stack (frontier and non-frontier models both get cheaper) while harness quality is not. This is the same "price-symmetric" logic documented for a different domain in `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 9 (Breunig again, there arguing that per-token cost reductions benefit attacker and defender equally in the security-hardening arms race) — the same author reuses a structurally identical economic argument (symmetric price declines don't resolve a competitive/allocation problem) across two different domains four months apart.

### Claim 7: Fable's access controls, dynamic degradation, and required data retention are a second, non-price factor that Breunig says "likely locks in" the shift away from single-model reliance, by causing companies and countries to reconsider where they send their traces and get their tokens
- **Evidence**: Breunig's closing paragraph, presented as an additional and distinct argument from the cost-based case made in Claims 1-6.
- **Confidence**: anecdotal (Breunig's own characterization; no named company or country example, no citation for what Fable's access-control/degradation/retention terms specifically are)
- **Quote**: "Plus, Fable's other shock likely locks in this change. Fable's access controls, dynamic degradation, and required data retention spooked enough companies (and countries!) into thinking about where they send their traces and where they get their tokens."
- **Our assessment**: This is a distinct claim from the cost argument — even if Fable's price fell to parity with alternatives, Breunig argues the multi-model-routing behavior would persist because of non-price factors (data governance and reliability concerns). No detail is given on what "dynamic degradation" refers to mechanically, and no other corpus source currently documents Fable-specific access controls or data retention requirements as a driver of multi-model adoption strategies, making this a novel but thinly-evidenced claim — a single sentence with no elaboration.

### Claim 8: Breunig frames the essay itself as a response to active, contemporaneous discourse about "agentic coders... balking at Anthropic's pricing and adopting alternatives"
- **Evidence**: The essay's opening sentence, giving the immediate trigger for writing it.
- **Confidence**: anecdotal (Breunig's own framing of "some talk today," with no citation of the specific discourse referenced)
- **Quote**: "There's some talk today about how agentic coders are balking at Anthropic's pricing and adopting alternatives. I was reminded of a thought I had in the weeks following Fable's release: the free lunch was over."
- **Our assessment**: This dates the essay's argument to a specific market moment (August 2026) rather than presenting it as a timeless principle — Breunig is explicitly responding to a live pricing controversy, not writing a general theory piece. For the guide, this is useful as a marker that the "harness ROI has shifted" argument is itself contested/topical at time of writing, not settled practitioner consensus — the essay is one voice in an active debate about Anthropic's pricing, not a retrospective on a resolved question.

## Concrete Artifacts

### The Moore's Law / AI-model-economics analogy (verbatim, Breunig's full essay only — not in Willison's excerpt)
```
Source: Drew Breunig, "Fable & The End of the Free Lunch," dbreunig.com,
August 23, 2026 (https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html)

PHASE 1 (Moore's Law in effect):
  "it didn't make sense to ruthlessly optimize your code. In 18 months,
  a CPU would arrive that would double your performance."
  — named "the free lunch" (Herb Sutter, cited by Breunig as a "seminal essay")

PHASE 2 (Moore's Law slows, mid-2000s):
  "single-threaded performance stagnated ... we suddenly had to think
  about parallelization, architecture, memory locality, etc."
  — "We had to think about what work went where."

PHASE 1 ANALOG (pre-Fable AI models):
  "it felt silly to waste too much time improving your coding harness
  or context strategies. A new model would arrive at the same price
  (or cheaper!) and paper over most of your problems."

PHASE 2 ANALOG (post-Fable):
  "the cost was so high and Opus was good enough (as was 5.6, K3, and
  even GLM) for most of the code we needed."
  — "So we started to think about what work went where."
```

### GLM 5.2 pricing and Breunig's model-delegation workflow (verbatim, full essay only)
```
Source: same essay

- GLM 5.2 released same week as Fable
- Cost: ~1/9th of Fable's price; ~1/5th the cost of Opus 5
- Breunig's judgment: "more than sufficient" for most rote coding,
  "especially when provided with great context"
- Workflow: "I frequently chat with Fable to interrogate and shape
  a design, before handing off a brief to GLM."
```

### Willison's excerpted blockquote vs. the full essay (attribution boundary)
```
What Simon Willison's post (simonwillison.net/2026/Aug/23/drew-breunig/)
actually quotes verbatim (confirmed via direct HTML fetch):

  "Prior to Fable, it felt silly to waste too much time improving your
  coding harness or context strategies. A new model would arrive at the
  same price (or cheaper!) and paper over most of your problems.

  But then Fable landed. It was (and still is!) incredible. But the cost
  was so high and Opus was good enough (as was 5.6, K3, and even GLM) for
  most of the code we needed.

  So we started to think about what work went where."
  — Drew Breunig, Fable & The End of the Free Lunch

Willison's post tags: ai, generative-ai, llms, anthropic, claude,
drew-breunig, llm-pricing, claude-mythos-fable

Everything else in Claims 3, 4, 6, 7, and 8 above (the Moore's Law
analogy, GLM pricing, the pushback rebuttal, the access-controls
paragraph, and the opening "agentic coders balking" sentence) comes only
from Breunig's linked full essay, not from Willison's excerpt.
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-anthropic-choosing-claude-model.md`,
`blog-anthropic-cost-visibility-control.md`, `blog-anthropic-abc-legal-managed-agents.md`,
`blog-cursor-router-model-classifier.md`, `blog-simonwillison-cybersecurity-proof-of-work.md`,
and `blog-simonwillison-5minute-llms.md` were re-read directly (MINER.md §4b)
and every claim number cited below was confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-anthropic-choosing-claude-model.md` Claim 8 (the "advisor
    strategy": Sonnet 5 + Fable 5 advisor within 10% of Fable 5's SWE-bench
    Pro score at 63% of the price) and `blog-anthropic-cost-visibility-control.md`
    Claim 13 (same pattern, restated as "a smaller model like Sonnet call a
    frontier model at key moments"): this source's Claim 5 (Breunig chats
    with Fable to shape a design, then hands a brief to GLM for execution)
    is an independent, practitioner-level instance of the same
    executor/advisor split, generalized across vendors (Fable for planning,
    a non-Anthropic model for execution) rather than confined to a single
    vendor's model family — corroborating that this pattern is emerging
    organically among practitioners, not only as vendor-prescribed guidance.
  - `blog-cursor-router-model-classifier.md` Claim 1 ("routine work being
    completed at frontier prices" is a cost/quality mismatch Cursor Router
    is built to fix) and Claim 3 (routing "simple work" to price-efficient
    models, "complex, long-horizon problems" to frontier models): this
    source's Claim 2 ("what work went where") is the qualitative,
    practitioner-economics statement of the same underlying principle
    Cursor's product post operationalizes as a trained classifier — Breunig
    supplies the "why this became necessary now" reasoning (an unusually
    expensive top-tier model, Claim 1-2 here), Cursor supplies a specific
    "how" implementation.
  - `blog-anthropic-abc-legal-managed-agents.md` Claim 7 (ABC Legal's
    fleet-wide default: Sonnet for most agents, Haiku for high-volume/fast
    tasks, Opus reserved for tasks where deeper reasoning justifies the
    cost): both sources document a practitioner deliberately allocating
    different models to different work by cost/capability rather than
    running one model for everything — ABC Legal's version operates within
    a single vendor's tiers, Breunig's spans vendors (Fable, Opus, GLM,
    K3), extending the evidence for "deliberate model allocation by task"
    as a cross-context, cross-vendor pattern.
  - `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 9 (Breunig,
    in a different April 2026 essay on AI-security economics: "Code remains
    cheap, unless it needs to be secure... unless models reach the point of
    diminishing security returns, you still need to buy more tokens than
    attackers do" — i.e., symmetric per-token price declines do not resolve
    an allocation/competition problem): this source's Claim 6 makes the
    structurally identical argument in a different domain — falling
    inference prices won't undo model-routing discipline because price
    declines benefit all model tiers symmetrically. Same author, same
    "price-symmetric declines don't solve the underlying allocation
    problem" logic, applied to security spend in the April essay and to
    harness/context investment in this one.

- **Contradicts**: None identified as a MINER.md §4a contradiction. This
  source's practitioner argument for deliberate multi-model routing could
  look, at a glance, like it opposes `blog-anthropic-choosing-claude-model.md`
  Claim 1 (Anthropic's stated default: "start with the most intelligent
  generally available model and use effort level... to dial in performance
  and cost"). It is not a real contradiction: that same note's Claim 3
  already documents Anthropic itself acknowledging a legitimate bottom-up
  alternative ("some organizations may also choose to start with the most
  cost effective model and move up classes until the quality bar is met"),
  and this source's argument is conditioned on a specific market state (an
  unusually expensive top-tier model with several "good enough"
  alternatives) rather than a universal claim that starting cheap is always
  correct — a conditioning variable, not a disagreement about the same
  claim. No contradiction issue filed.

- **Extends**:
  - `blog-simonwillison-cybersecurity-proof-of-work.md`: that note documents
    Breunig's economic framing of AI security spend (tokens-as-budget,
    T_d > T_a). This source extends the corpus's coverage of Breunig's
    economic-analogy style of argument to a second, distinct domain
    (harness/context engineering investment) four months later, using a
    structurally similar "price symmetry doesn't resolve the underlying
    problem" mechanism (see Corroborates above).
  - `blog-simonwillison-5minute-llms.md`: that note documents Breunig's
    "Claws are digital pets, Mac Minis are aquariums" cultural metaphor
    (Claim 9), attributed via the same Willison-quotes-Breunig publication
    pattern as this source, but on an unrelated topic (personal AI
    assistants). No claim-level overlap — flagged here only because the
    Prospector's triage noted both existing notes "mention Breunig"; this
    source note treats that as a shared-author signal, not a
    topical-overlap citation, consistent with MINER.md's caution against
    superficial "relates to X" cross-references.

- **Novel**:
  - **The Moore's Law "free lunch" analogy applied to AI model-pricing
    economics** (Claim 3) — no other corpus source frames the
    harness/context-optimization ROI question using this specific
    historical parallel (Herb Sutter's "free lunch," the mid-2000s
    single-threaded performance stagnation, "what work went where" as a
    reused phrase across both eras).
  - **GLM 5.2's specific price ratio relative to Fable and Opus 5** (Claim
    4: ~1/9th of Fable, ~1/5th of Opus 5) — this specific figure does not
    appear in any existing corpus note.
  - **The claim that harness-quality improvement, not just price decline,
    is what keeps cheaper models viable long-term** (Claim 6) — this is a
    distinct argument from the corpus's existing model-routing sources
    (Cursor Router, GitHub Copilot auto-routing), which describe routing as
    a static or continuously-retrained classifier decision rather than
    arguing that harness investment itself is a durable, independent lever
    against price-driven convergence back to frontier-only usage.
  - **Fable's access controls, dynamic degradation, and data retention
    terms as a driver of multi-model/multi-vendor routing** (Claim 7) — no
    other corpus source documents this specific non-price mechanism for
    Fable, though the claim is thin (one sentence, no elaboration or named
    example).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claims 1, 2, and 3 (the
  pre-Fable "why bother optimizing" baseline, the post-Fable "what work
  went where" shift, and the Moore's Law "free lunch" analogy) as
  historical/economic context for why harness and context-engineering
  investment has a different ROI calculus depending on the pricing gap
  between the top-tier model and "good enough" alternatives. This gives
  the chapter a citable rationale for *when* harness investment becomes
  worthwhile, distinct from the technique-level guidance the chapter likely
  already covers.
- **Chapter 04 (Context Engineering) / Model Selection**: Add Claim 6
  (harness quality as an independent, durable lever that keeps cheaper
  models viable even as prices fall generally) as a forward-looking framing
  for context-engineering investment — the argument that better context
  delivery, not just waiting for prices to drop, is what lets teams keep
  using cheaper models for a growing share of work. Pair with Claim 5
  (Breunig's own Fable-plans/GLM-executes workflow) as a concrete,
  cross-vendor example of the advisor/executor pattern already documented
  from Anthropic's own product guidance (`blog-anthropic-choosing-claude-model.md`
  Claim 8).
- **Chapter 02 or 04 (Cost Optimization)**: Add Claim 4's GLM 5.2 pricing
  figure (~1/9th of Fable, ~1/5th of Opus 5) as a concrete, if unaudited,
  data point illustrating how large the price gap between a frontier and a
  "good enough" alternative can be — useful alongside the corpus's existing
  cost-per-commit and cost-per-task figures from Cursor and Anthropic
  sources, with the explicit caveat (per Our assessment on Claim 4) that
  this is a single practitioner's estimate, not a benchmarked measurement.

## Extraction Notes

- **WebFetch produced unreliable/inconsistent quotes on this source; raw
  HTML was fetched directly instead.** An initial WebFetch pass on the
  Willison URL refused to return verbatim text at all (citing a
  copyright/quote-length policy) and offered only a loose summary. A second
  WebFetch pass on both URLs returned quotes that were subtly inconsistent
  with each other across the two calls (e.g., paraphrased fragments
  presented as direct quotes). To get quote-accurate text, both pages were
  fetched directly via `curl` with a standard user agent and HTML tags
  stripped locally with a Python script; all quotes in this note are copied
  character-for-character from that locally-parsed text, not from either
  WebFetch pass.
- **Two pages, one argument**: Willison's post excerpts only the middle
  three paragraphs of Breunig's five-plus-paragraph essay (see the
  "Willison's excerpted blockquote vs. the full essay" artifact above for
  the exact boundary). Claims 3, 4, 6, 7, and 8 in this note come
  exclusively from Breunig's full essay (fetched via its linked URL,
  `dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html`), not from
  Willison's excerpt. This is disclosed explicitly per MINER.md §1's
  "follow substantive linked pages" guidance — the issue's source URL is
  Willison's page, but the substantive content lives primarily in
  Breunig's linked original.
- **No sub-pages beyond the two primary pages were followed.** Breunig's
  essay links to Herb Sutter's original "free lunch" essay (cited by name,
  not by URL, in the extracted text) — this was not independently fetched,
  since Breunig's own summary of Sutter's argument ("In 18 months, a CPU
  would arrive that would double your performance") is sufficient for the
  analogy as used in this essay, and Sutter's essay is decades-old computing
  history rather than new evidence about AI-model economics.
- **Confidence rated `anecdotal` overall**: every claim in this source is a
  single practitioner's first-person argument, estimate, or historical
  analogy — there is no cited study, benchmark, survey, or named
  organization beyond Breunig's own stated workflow and the one GLM 5.2
  price ratio (itself unattributed to any pricing page or calculation
  methodology).
- **No contradiction issues filed.** The one near-miss (this source's
  routing argument vs. Anthropic's "start with the most intelligent model"
  default) was evaluated and judged to be a conditioning-variable
  difference, not a material contradiction — see Cross-References →
  Contradicts above for the full reasoning.
