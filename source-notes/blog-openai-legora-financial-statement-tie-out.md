---
source_url: https://openai.com/index/legora-financial-statement-review-with-astra
source_type: blog-post
title: "Legora reviewed 41 documents in minutes with GPT-6 Astra"
author: OpenAI (customer case study, featuring Percevale Perks, Legal Engineer, Legora)
date_published: 2026-09-03
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: anecdotal
issue: "#3403"
---

# Legora reviewed 41 documents in minutes with GPT-6 Astra

> An OpenAI customer case study describing how Legora, a legal-and-professional-work
> agentic platform, used GPT‑6 Astra to complete a 41-document financial-statement
> tie-out in minutes instead of "an entire evening, sometimes days," and evaluated the
> model with its own planted-error benchmark (Legora BAR), reporting that Astra found
> all four intentionally planted errors — including a hidden £500,000 revenue-note gap
> — while retaining every check the previous model passed and completing roughly 50
> more.

## Source Context

- **Type**: blog-post (OpenAI `openai.com/index/` customer-story vertical; a very
  short (~330-word) case study with two section headers and one pull quote — no
  benchmark table, no methodology appendix, no code or architecture diagram).
- **Author credibility**: Written and published by OpenAI as promotional
  customer-success content — OpenAI has a direct commercial incentive to present
  GPT‑6 Astra favorably. The only named individual quoted is Percevale Perks,
  identified as a "Legal Engineer" at Legora. No auditor, client, or independent
  third party is named or quoted. No methodology is disclosed for the "nearly 40%"
  improvement figure, the "about 3%" average BAR improvement figure, what the
  "previous model" specifically was, or how the four planted errors were selected
  or verified as representative of real tie-out defects.
- **Scope**: Covers the financial-statement tie-out workflow (checking every figure
  in draft accounts against trial balances, a consolidation schedule, and prior-year
  accounts), a single description of the Agent completing that workflow across 41
  documents in one run, the human-in-the-loop framing (Agent does exhaustive
  comparison, human makes the judgment call), Legora's internal "Benchmark for
  Agentic Reasoning" (BAR) results comparing GPT‑6 Astra to an unnamed previous
  model, and the four-planted-error validation result. Does NOT cover: which model
  Astra is being compared against ("the previous model" is never named — likely but
  not confirmed to be GPT‑5.6 Sol, the immediately preceding OpenAI flagship per
  `blog-simonwillison-gpt6-astra-launch.md`), the BAR benchmark's task composition,
  scoring methodology, or task count, the size/complexity of the 41 documents, any
  latency or cost figures for the run, or any detail of Legora's underlying
  orchestration/agent architecture beyond the word "Agent."

## Extracted Claims

### Claim 1: Legora is an agentic operating system for legal and professional work used by more than 100,000 professionals across more than 1,800 in-house legal departments and law firms in over 50 markets
- **Evidence**: Company-background statement opening the article.
- **Confidence**: anecdotal (self-reported, first-party adoption figures with no independent audit, survey date, or definition of "used by")
- **Quote**: "Legora is an agentic operating system for legal and professional work, used by more than 100,000 professionals across more than 1,800 in-house legal departments and law firms in over 50 markets."
- **Our assessment**: This is a vendor-reported adoption ceiling in the same evidentiary class as other self-reported enterprise-scale figures already in the corpus (e.g. Polimill's "1,050 municipalities," `blog-openai-polimill-japan-public-ai-infrastructure.md` Claim 1) — treat as an upper-bound reach figure, not a measured active-usage rate. Legora previously appeared in the corpus only as a named, undescribed customer-session presenter at Code w/ Claude London (`blog-anthropic-code-w-claude-london-2026.md` Claim 5); this is the first source with any substantive description of what Legora actually does.

### Claim 2: Financial-statement tie-out — checking every figure in draft accounts against trial balances, a consolidation schedule, and the previous year's accounts until each item agrees — is described by a Legora Legal Engineer as one of the more tedious workflows, taking "an entire evening, sometimes days"
- **Evidence**: Direct attributed quote describing the pre-AI baseline for the workflow.
- **Confidence**: anecdotal (single practitioner's characterization of task tedium and duration, no timed baseline measurement given)
- **Quote**: "the work 'can take an entire evening, sometimes days.'"
- **Our assessment**: This is the article's only quantified (if vague) baseline for the "before" state, and it is stated as a quote-within-the-article rather than a directly block-quoted passage — the source itself renders it as a partial quotation embedded in a sentence, not a full pull-quote. This baseline is the reference point against which the "minutes" claim in Claim 3 should be read; no more precise time figure (e.g., exact hours) is given for either the before or after state.

### Claim 3: Using GPT‑6 Astra, Legora's Agent completed the tie-out across 41 documents in a single run, within minutes, checking every balance against its supporting schedule, surfacing breaks in the amounts, and recording each check
- **Evidence**: Direct statement under the "Processing complex financial context at scale" section header — the article's headline result.
- **Confidence**: anecdotal (a single vendor-selected, self-reported task-completion example; no independent timing measurement, no disclosure of document length/complexity, and "minutes" is not given as an exact figure)
- **Quote**: "Using GPT‑6 Astra, Legora's Agent completed the tie-out across 41 documents in a single run. Legora says the Agent did the work within minutes: checking every balance against its supporting schedule, surfacing breaks in the amounts, and recording each check."
- **Our assessment**: This is the article's title claim and its only concrete task-scale figure (41 documents, one run). Structurally this is the same self-reported "hours/days → minutes" compression pattern already documented across multiple OpenAI customer case studies in the corpus (e.g. Notion's "2 Weeks → 3 hours," `blog-openai-polimill-japan-public-ai-infrastructure.md` Claim 6's 3-5x figure) — directionally consistent with, not independent confirmation of, those other multipliers. No baseline hours figure is given to compute an exact multiplier against Claim 2's "entire evening, sometimes days."

### Claim 4: Percevale Perks attributes the change to processing power — the ability to ingest a large number of documents and digest complex information across many line items and figures at once
- **Evidence**: Direct attributed pull-quote, the only full block quote in the article.
- **Confidence**: anecdotal (single practitioner's causal attribution, not a technical explanation of the mechanism)
- **Quote**: "I think what changed before and after is the processing power, the ability to ingest such a large number of documents, digest really complex information, and get all of those different line items and figures."
- **Our assessment**: This is a practitioner-facing but non-technical explanation — "processing power" is not a specific mechanism (no mention of context window size, retrieval strategy, or agentic tool-calling pattern). It is the closest the source comes to explaining *why* Astra can do this and *why* the previous model apparently could not to the same degree, but it stays at the level of a felt capability jump rather than a named architectural cause.

### Claim 5: The Agent handles the exhaustive comparison while the expert remains responsible for the judgment call on each result — a human-in-the-loop approach central to Legora's expansion beyond legal work into audit, tax, compliance, and risk
- **Evidence**: Direct statement following the pull quote, framing the division of labor and Legora's stated platform-expansion strategy.
- **Confidence**: anecdotal (stated design philosophy and forward-looking business strategy, not a demonstrated or audited practice)
- **Quote**: "The Agent handles the exhaustive comparison, while the expert remains responsible for the judgment call on each result. That approach of keeping a human in the loop is central to how Legora is extending its platform beyond legal work into audit, tax, compliance, and risk."
- **Our assessment**: This is a specific, named human-in-the-loop division of labor (agent: exhaustive comparison / human: judgment call) tied explicitly to a stated multi-domain expansion strategy (audit, tax, compliance, risk) — more concrete than a generic "humans stay in the loop" statement because it names the exact task split and the business rationale for it. No detail is given on how the "judgment call" review step is structured, timed, or audited in practice.

### Claim 6: Legora evaluated GPT‑6 Astra using its own "Legora Benchmark for Agentic Reasoning" (BAR), measuring performance on end-to-end legal tasks drawn from real-world use cases; Astra improved performance by nearly 40% over the previous model on the financial-statement workflow specifically, versus about 3% average improvement across all BAR tasks
- **Evidence**: Direct statement under "Improving accuracy, completeness, and reliability," naming the benchmark and giving two contrasting improvement figures.
- **Confidence**: anecdotal (a proprietary, vendor-internal benchmark with no published task list, scoring rubric, task count, or third-party audit; "the previous model" is never named)
- **Quote**: "Legora evaluated GPT‑6 Astra with the Legora Benchmark for Agentic Reasoning (BAR), which measures performance on end-to-end legal tasks drawn from real-world use cases. Legora reports that GPT‑6 Astra improved performance by nearly 40% over the previous model on this financial-statement workflow. Across all tasks in the BAR, the improvement averaged about 3%."
- **Our assessment**: This is the most specific, checkable-in-principle claim in the source — a named benchmark (BAR) with two distinct figures (task-specific ~40% vs. all-task-average ~3%) — but it is entirely opaque as evaluation infrastructure: no public task list, no scoring methodology, no sample size, and no independent replication exist anywhere the Miner could find. The large gap between the workflow-specific figure (~40%) and the all-task average (~3%) is itself notable and should be preserved together whenever this claim is cited — it signals that financial-statement tie-out is an unusually large point of improvement relative to Legora's other benchmarked legal tasks, not a representative one. "The previous model" is not named; per `blog-simonwillison-gpt6-astra-launch.md` Claim 1 (Astra launched September 3, 2026, following GPT‑5.6 Sol as OpenAI's immediately prior flagship), GPT‑5.6 Sol is the most likely referent, but this is inference, not a stated fact in this source.

### Claim 7: In the tie-out task specifically, GPT‑6 Astra found all four errors Legora had planted in the accounts, including a £500,000 gap hidden in the revenue note
- **Evidence**: Direct statement describing a planted-error validation exercise, attributed to Legora's own testing (not independently audited).
- **Confidence**: anecdotal (a vendor-run, unaudited planted-error test with a very small n=4 error set; no description of how the four errors were chosen, whether they were chosen to be findable, or what error types the remaining BAR average-3% figure in Claim 6 reflects)
- **Quote**: "GPT‑6 Astra found all four errors Legora had planted in the accounts, including a £500,000 gap hidden in the revenue note."
- **Our assessment**: This is a concrete, specific artifact (a £500,000 planted gap, specifically located in a "revenue note") rather than an abstract accuracy percentage, which makes it more legible as an example even though the underlying test (4 planted errors, presumably in one accounts set) is far too small a sample to generalize an error-detection rate from. See Cross-References → Corroborates for a directly parallel planted-defect verification methodology already documented in the corpus for a different domain (software test-suite validation via mutation testing).

### Claim 8: GPT‑6 Astra retained every check the previous model got right and completed around 50 more checks in the same tie-out exercise
- **Evidence**: Direct statement immediately following Claim 7, describing coverage/completeness gains relative to the unnamed previous model.
- **Confidence**: anecdotal (a specific-sounding "around 50 more" figure with no stated total check count, so the relative magnitude of the improvement cannot be assessed — 50 more checks out of 60 total is a very different result than 50 more out of 2,000)
- **Quote**: "And it retained every check the previous model got right as well as completed around 50 more."
- **Our assessment**: "Around 50 more" is presented without a denominator (total checks performed, or total line items across the 41 documents), which makes this figure impossible to contextualize as a percentage improvement — it should not be cited in the guide without flagging that the total check count is undisclosed. Combined with Claim 7, this frames Astra's improvement over the previous model as strictly additive (no regressions, only new coverage) rather than a tradeoff, but that framing is asserted by the vendor, not demonstrated with a before/after check-by-check comparison the reader can inspect.

## Concrete Artifacts

### Full article text (verbatim, via reader-proxy retrieval — see Extraction Notes)

```
Source: https://openai.com/index/legora-financial-statement-review-with-astra
(OpenAI, published on or before September 3, 2026)

Legora is an agentic operating system for legal and professional work, used
by more than 100,000 professionals across more than 1,800 in-house legal
departments and law firms in over 50 markets. Its legal engineers work
directly with customers to understand how they operate and adapt Legora to
their end-to-end workflows, from contract and agreement review to legal
research.

One of the more tedious workflows is financial-statement tie-out: checking
every figure in draft accounts against trial balances, a consolidation
schedule, and the previous year's accounts until each item agrees. As
Legora Legal Engineer Percevale Perks says, the work "can take an entire
evening, sometimes days."

## Processing complex financial context at scale

Using GPT‑6 Astra, Legora's Agent completed the tie-out across 41
documents in a single run. Legora says the Agent did the work within
minutes: checking every balance against its supporting schedule, surfacing
breaks in the amounts, and recording each check. The result gives the
legal professional a granular record of every line item and figure to
review.

"I think what changed before and after is the processing power, the
ability to ingest such a large number of documents, digest really complex
information, and get all of those different line items and figures."
—Percevale Perks, Legal Engineer, Legora

The Agent handles the exhaustive comparison, while the expert remains
responsible for the judgment call on each result. That approach of keeping
a human in the loop is central to how Legora is extending its platform
beyond legal work into audit, tax, compliance, and risk.

## Improving accuracy, completeness, and reliability

Legora evaluated GPT‑6 Astra with the Legora Benchmark for Agentic
Reasoning (BAR), which measures performance on end-to-end legal tasks
drawn from real-world use cases. Legora reports that GPT‑6 Astra improved
performance by nearly 40% over the previous model on this
financial-statement workflow. Across all tasks in the BAR, the improvement
averaged about 3%.

In the tie-out, Legora saw gains across what Percevale describes as
accuracy, completeness, and reliability. GPT‑6 Astra found all four errors
Legora had planted in the accounts, including a £500,000 gap hidden in the
revenue note. It checked every balance against its supporting schedule and
recorded each check. And it retained every check the previous model got
right as well as completed around 50 more.

The result is a more complete and faster first pass and a clearer record
to review, while the final decision stays with the legal expert.
```

## Cross-References

- **Corroborates**:
  - `guide/03-verification.md` (Example: mutation testing that found two
    holes in the tests, citing `blog-simonwillison-condense-json-1-1` Claim
    10): that example validates a Hypothesis test suite by planting three
    named bug classes and confirming the suite caught all three — the same
    "plant a small number of known defects, verify the system catches all
    of them" evaluation pattern this source's Claim 7 uses (four planted
    errors, all four found) to validate an agent's tie-out checking, just
    applied to a financial-review agent rather than a software test suite.
    This is a cross-domain corroboration of planted-defect validation as a
    recognizable, reusable evaluation technique — worth citing in Chapter
    03 as a second, independent domain instance of the same technique.
  - `blog-simonwillison-gpt6-astra-launch.md` Claim 8 (GPT‑6 Astra scores
    100% on ExploitBench vs. Sol's 78.5%, 42.4% on ExploitGym vs. Sol's
    30.3%, and 99.2% on SRE-Bench reverse engineering vs. Sol's 68.7% —
    large, quantified capability jumps over the immediately prior OpenAI
    flagship on precision-detection benchmarks) and Claim 4 (on Artificial
    Analysis's Intelligence Index, Astra scores equal to Sol, trailing both
    Claude Fable 5.1 and Meta Muse Spark 1.3): this source's Claim 6 (~40%
    improvement on the tie-out task specifically, vs. only ~3% average
    across all BAR tasks) is directionally consistent with that note's
    finding that Astra's gains over Sol are highly task-dependent rather
    than a uniform across-the-board improvement — both sources independently
    show Astra posting large gains on tasks requiring precise,
    exhaustive detection/comparison work (security exploit detection;
    financial figure reconciliation) while showing much smaller or no gains
    on general/aggregate measures (BAR all-task average; Artificial
    Analysis Intelligence Index).
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 11
    (auditability, not accuracy, is the irreducible trust requirement in
    regulated financial AI — derived from discovery with 147 financial
    firms and anchored on the quote "How am I supposed to trust something
    I can't audit?"): this source's Claim 5 (Agent does the exhaustive
    comparison, expert keeps the judgment call) corroborates that framing
    from the opposite vendor stack (OpenAI rather than Anthropic), and
    does so in what the workflow actually ships rather than as a stated
    principle. The article's described deliverable is not a verdict but a
    reviewable record — "recording each check" (Claim 3) producing
    "a granular record of every line item and figure to review," and
    closing on "a clearer record to review, while the final decision stays
    with the legal expert." That is Kepler's auditability-first requirement
    expressed as an output artifact. **The two sources differ in the
    strength of the guarantee, and this is the useful distinction for the
    guide, not a contradiction**: Kepler derives auditability
    *architecturally* — the model is structurally excluded from producing
    any final auditable number (Kepler Claim 3) and provenance is designed
    in from inception (Kepler Claim 9, "Provenance has to shape the entire
    system, not get added at the end"). Legora's case study describes no
    such separation: the Agent itself performs the checks and generates the
    record the human reviews, so auditability here rests on the
    completeness and honesty of the agent's own log, not on a
    deterministic layer the model cannot bypass. Legora never denies a
    provenance architecture — the source simply says nothing about its
    orchestration internals (see Source Context → Scope) — so this is a
    weaker instance of the same principle, not an opposing claim.
    Cite them together in Chapter 03 with that asymmetry stated
    explicitly: human-in-the-loop review of an agent-generated record
    (Legora) is a strictly weaker verifiability guarantee than
    human review of deterministically-produced numbers with
    designed-in provenance (Kepler).
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8 (automated
    evaluation pipelines testing every prompt change, model upgrade, and
    context modification against known-correct answers at every stage,
    with failures attributed to reasoning / context / execution): this
    source's Claim 7 (four planted errors, all four found) is the *other*
    approach to verifying financial-AI output correctness, and the contrast
    is instructive. Kepler's is **continuous and stage-attributable**:
    standing evaluation infrastructure run against every change, designed
    to localize which layer regressed. Legora's planted-error exercise is
    **one-off and end-to-end**: a single whole-workflow pass/fail on n=4
    defects, with no stage attribution and no indication it re-runs on
    model or prompt changes. Legora's BAR benchmark (Claim 6) is the
    closer analogue to Kepler's discipline — a repeatable internal
    benchmark of end-to-end tasks — but Legora discloses no task list,
    scoring rubric, or task count, where Kepler at least describes the
    attribution structure and the within-hours new-model benchmarking
    cadence. Neither is third-party audited, so this is two vendors
    independently treating internal-eval infrastructure as the correctness
    story in regulated financial AI; the pairing is worth citing as
    evidence the *practice* is converging even though neither instance is
    externally verifiable.
  - `blog-openai-polimill-japan-public-ai-infrastructure.md` Claim 6 (Codex
    "3-5x" development-speed multiplier, self-reported, no baseline
    methodology) and Claim 1 (self-reported adoption scale with no audit):
    this source's Claim 1 (100,000+ professionals, 1,800+ firms, 50+
    markets) and Claim 3 (41-document tie-out completed "within minutes")
    are structurally the same kind of unaudited, vendor-published
    scale/speed figures as that note's headline claims — both are OpenAI
    customer case studies following an identical template (named
    individual quote, headline speed/scale figure, "Results"-style closing
    framing).

- **Contradicts**: None identified. No existing corpus source makes a
  claim about Legora, financial-statement tie-out, or the Legora BAR
  benchmark that opposes what this post states. This source's Claim 6
  (task-specific ~40% vs. all-task ~3% BAR improvement) is an internal
  contrast within the same source, not a contradiction between sources —
  both figures are presented by Legora as compatible, simply describing
  different scopes (one task vs. all tasks). No contradiction issue filed.
  The closest candidate considered and rejected: this source's Claim 5
  (human-in-the-loop review of an agent-produced record) versus
  `blog-anthropic-kepler-verifiable-ai-financial.md` Claims 3, 9, and 11
  (auditability must be enforced architecturally, with the model excluded
  from producing final auditable numbers). These are not opposing claims —
  they are the same auditability-first principle at two different strengths
  of guarantee, and Legora's source is silent on orchestration internals
  rather than asserting that no deterministic layer is needed. Per
  MINER.md §4a, a difference in the strength or scope of a claim is a
  conditioning variable, not a contradiction; both positions are captured
  in Cross-References → Corroborates above.

- **Extends**:
  - `blog-anthropic-code-w-claude-london-2026.md` Claim 5: that note names
    Legora as an undescribed customer-session presenter at Code w/ Claude
    London (May 2026) and explicitly flags "no extractable patterns from
    this source" for Legora, recommending a dedicated extraction "if
    individual session recaps or recordings become available." This source
    is that dedicated extraction — the first substantive description in
    the corpus of what Legora's platform actually does (financial-statement
    tie-out via an agentic workflow) and, notably, on OpenAI's GPT‑6 Astra
    rather than Claude — meaning Legora is a corpus-documented customer of
    at least two frontier-lab platforms (Anthropic, per the May 2026 event
    presence, and OpenAI, per this September 2026 case study), though this
    source gives no indication of whether Legora's production tie-out
    workflow itself runs on Astra specifically or was evaluated on it as
    one of several supported models.
  - `blog-simonwillison-gpt6-astra-launch.md`: extends that note's
    benchmark-only view of Astra's security/precision-detection gains
    (ExploitBench, ExploitGym, SRE-Bench) with a real (if small and
    unaudited) applied-workflow example in a different high-precision
    domain — financial figure reconciliation — showing a similar
    "large gains on exhaustive/precise comparison tasks" pattern outside
    of formal benchmarks.

- **Novel**:
  - **The Legora Benchmark for Agentic Reasoning (BAR)** is not previously
    documented anywhere in this corpus — this is the first source
    describing a legal-domain, company-internal, end-to-end agentic-task
    benchmark distinct from the general-purpose or security benchmarks
    (Artificial Analysis Intelligence Index, ARC-AGI-3, ExploitBench, etc.)
    already tracked for GPT‑6 Astra.
  - **Financial-statement tie-out as a named, described legal/audit
    workflow** — not previously documented in the corpus. This is a
    concrete instance of an agent performing exhaustive cross-document
    reconciliation with human sign-off, distinct from the contract-review
    and legal-research use cases more commonly associated with legal AI in
    the corpus.
  - **A planted-error validation exercise (n=4) applied to an agentic legal/
    financial-review workflow**, with one concrete example (a £500,000
    hidden revenue-note gap) — the first corpus instance of this specific
    evaluation technique (see Corroborates above for the parallel software
    mutation-testing instance) applied to a non-software, financial-review
    domain.

## Guide Impact

- **Chapter 03 (Verification)**: Add this source's Claim 7 (Legora planted
  four known errors in a set of accounts, including a £500,000 revenue-note
  gap, and confirmed GPT‑6 Astra's Agent found all four) as a second,
  independent domain instance — alongside the existing mutation-testing
  example (`blog-simonwillison-condense-json-1-1` Claim 10, already in
  `guide/03-verification.md`'s "Example: mutation testing that found two
  holes in the tests") — of the general "plant known defects, verify the
  system catches all of them" evaluation technique. Flag clearly that n=4
  is far too small a sample to support a general error-detection-rate
  claim, and that no detail is given on how the four errors were selected
  or whether they were representative of real-world tie-out defect types.
  **Placement and sequencing** (Chapter 03 already cites
  `blog-anthropic-kepler-verifiable-ai-financial` in two places, so this
  addition must not land as a disconnected third financial-AI block):
  1. Put the planted-error material where the technique already lives —
     immediately after the existing `#### Example: mutation testing that
     found two holes in the tests` subsection in `guide/03-verification.md`
     (~line 812) — as a short second instance showing the same
     plant-known-defects technique in a non-software domain. It does
     **not** belong in the `## Architectural Verification: Separate
     Reasoning from Computation` section (~line 1055), which is about
     removing the model from the path that produces the final number;
     Legora describes no such separation.
  2. Where Claim 5 is used (Chapter 03's human-review material and
     Chapter 05, below), add an explicit forward pointer to the existing
     Architectural Verification section stating the asymmetry from
     Cross-References above: Legora's human reviewing an
     agent-generated record is a strictly weaker verifiability guarantee
     than Kepler's human reviewing deterministically-produced numbers with
     designed-in provenance. Sequence Kepler first (the stronger
     architectural guarantee) and Legora second (the weaker,
     record-based form), so the chapter reads as a gradient of
     verifiability strength rather than two competing vendor anecdotes.
  3. If the guide adds evaluation-discipline guidance, pair this source's
     one-off n=4 planted-error check with Kepler's Claim 8 continuous,
     stage-attributable evaluation pipeline as the two ends of that
     spectrum — again Kepler first, Legora as the lighter-weight
     acceptance-test form.
- **Chapter 05 (Team Adoption)**: Add Claim 5 (Legora's explicit "Agent
  does exhaustive comparison, human makes the judgment call" division of
  labor, stated as central to expanding the platform into audit, tax,
  compliance, and risk) as a named example of a human-in-the-loop design
  pattern being used as an explicit business-expansion enabler into
  adjacent, higher-stakes domains — not just a safety afterthought.
- **No chapter should cite Claim 1's adoption figures, Claim 3's "within
  minutes" timing, Claim 6's "nearly 40%" / "about 3%" BAR figures, or
  Claim 8's "around 50 more" checks figure as independently verified or
  as generalizable accuracy/speed statistics** — all are first-party,
  unaudited, vendor-published figures with no disclosed methodology,
  no named comparison model, and (for Claim 8) no disclosed denominator,
  consistent with every other OpenAI customer case study already in this
  corpus.

## Extraction Notes

1. **Direct fetch blocked (Cloudflare challenge)**: Both `WebFetch` and a
   direct `curl` (with standard and mobile browser user-agents) against
   `https://openai.com/index/legora-financial-statement-review-with-astra`
   returned an HTTP 403 Cloudflare bot-challenge page (confirmed by
   inspecting the returned HTML, which contained
   `cdn-cgi/challenge-platform` script tags rather than article content) —
   the same access pattern already documented for `openai.com/index/`
   pages in `blog-openai-polimill-japan-public-ai-infrastructure.md` and
   other corpus notes. No Wayback Machine snapshot existed for this URL at
   extraction time (`archive.org/wayback/available` returned an empty
   `archived_snapshots` object) — likely because the article is very
   recent. The article was retrieved via the `r.jina.ai` reader-proxy
   (`https://r.jina.ai/https://openai.com/index/legora-financial-statement-review-with-astra`,
   HTTP 200), which returned clean Markdown-converted article text. This
   fetch was performed once; the retrieved Markdown is short (~330 words),
   internally coherent, and its section headers and quote structure match
   the sentence-level detail given in the two Prospector triage comments on
   the source issue (e.g. "41 documents," "GPT-6 Astra," "financial
   statement review"), which corroborates that the retrieval is accurate
   and not a paraphrase or hallucination.
2. **Entire article captured, nothing truncated**: The retrieved
   `r.jina.ai` output is 27 lines / ~2.8KB and ends on a clear closing
   sentence ("while the final decision stays with the legal expert.")
   with no indication of truncation. All extractable claims (Claims 1-8)
   were drawn from this single, complete retrieval — the full text is
   reproduced verbatim in Concrete Artifacts above.
3. **No sub-pages followed**: The retrieved article text contained no
   inline links to further substantive pages (no linked PDF, no "related
   posts" footer, no companion technical post) in the `r.jina.ai` Markdown
   output. This is consistent with the article's short, single-page
   customer-story format. Per MINER.md §1, no linked pages existed to
   follow.
4. **Cross-reference verification**: Before writing citations above,
   `blog-anthropic-code-w-claude-london-2026.md`,
   `blog-openai-polimill-japan-public-ai-infrastructure.md`,
   `blog-simonwillison-gpt6-astra-launch.md`,
   `blog-anthropic-kepler-verifiable-ai-financial.md`, and
   `blog-latentspace-meurer-agent-engineer-fde.md` were re-read directly
   (MINER.md §4b), and `guide/03-verification.md` was checked directly for
   the mutation-testing example cited above. All claim numbers cited above
   were confirmed against those notes' numbered `### Claim N:` headings in
   document order.
   The initial overlap pass searched the corpus on Legora-, Astra-, and
   benchmark-related terms and missed the corpus's other
   financial-verification source; a second pass searching on "financial,"
   "audit," "auditab," and "verification" surfaced
   `blog-anthropic-kepler-verifiable-ai-financial.md`, now cited above
   under Corroborates (Claims 8 and 11) with its Claims 3 and 9 referenced
   for the architectural contrast. `guide/03-verification.md` was also
   re-checked for where Kepler is already cited (the
   `## Architectural Verification: Separate Reasoning from Computation`
   section, citing Kepler Claims 3 and 9) so the Guide Impact
   recommendation below sequences this source against that existing
   material rather than proposing an unrelated addition. `blog-openai-gpt56-sol-ultrafast-mode.md` and
   `blog-latentspace-meurer-agent-engineer-fde.md` were also read in full
   during the overlap-check pass but are not cited above — neither
   contains any claim materially connected to this source's content beyond
   general OpenAI-customer-case-study or agent-engineering-role framing
   already captured via the other cross-references.
5. **No contradiction filed**: Checked this source's content against the
   cross-referenced notes above, including
   `blog-anthropic-kepler-verifiable-ai-financial.md` on the second pass;
   no material opposition to any existing claim was found — see
   Cross-References → Contradicts for the Legora/Kepler candidate that was
   considered and rejected as a strength-of-guarantee difference rather
   than a contradiction. Open `contradiction`-labeled issues and
   `CONTRADICTIONS.md` were checked for an existing entry on financial-AI
   verifiability; none covers this pairing.
6. **Confidence rated `anecdotal` overall**: every claim in this source is
   a first-party, vendor-published figure or characterization from a
   single customer case study, with no disclosed benchmark methodology, no
   named comparison model, no independent audit, and no second independent
   source confirming any of the specific figures (adoption scale, timing,
   BAR percentages, or check counts). This matches the `anecdotal` rating
   already applied to the corpus's other single-company vendor case
   studies (e.g. Polimill, Asana, Notion) rather than the `emerging` rating
   applied to sources with named, independently-checkable benchmark
   aggregators (e.g. Artificial Analysis, ARC Prize) as in
   `blog-simonwillison-gpt6-astra-launch.md`.
7. **Source is short and thin**: at ~330 words with two section headers,
   one pull quote, and no benchmark table, this is one of the shortest
   OpenAI customer-case-study sources in the corpus (shorter than the
   Polimill case study). All eight claims above exhaust the article's
   substantive content — there was no additional depth to extract beyond
   what is captured here, and the "previous model" comparison point (Claim
   6) and the undisclosed check-count denominator (Claim 8) are genuine,
   unresolvable gaps in the source itself, not extraction omissions.
