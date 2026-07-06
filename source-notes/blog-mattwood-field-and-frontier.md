---
source_url: https://mattwood.blog/essays/2026/06/the-field-and-the-frontier/
source_type: blog-post
title: "The Field and The Frontier"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-06-23
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: emerging
issue: "#1571"
---

# The Field and The Frontier

> Matt Wood (AWS Chief AI & Technology Officer) argues that two AI cost
> dynamics run simultaneously — frontier budgets keep rising because ambition
> expands to fill each efficiency gain, while the price of any *fixed*
> capability level collapses by 9x-40x per year — and that most enterprise
> value over the next few years will come from "field-first" deployment
> (systematically instrumenting known-capability workflows against local data)
> rather than frontier exploration, because most organizations are
> over-indexed on the latter.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays"
  collection; short-form, single-author, no comments/citations infrastructure
  beyond inline prose attribution; ~1,000 words, no images, tables, or
  hyperlinked citations — the two named data sources, Epoch AI and Artificial
  Analysis, are named in prose but not linked).
- **Author credibility**: Matt Wood returned to AWS in 2026 as "Chief AI &
  Technology Officer" after nearly 15 years at AWS earlier in his career and,
  most recently, leading commercial technology and innovation at PwC (per the
  site's About page). He holds a PhD in machine learning and did a
  postdoctoral fellowship in NLP/bioinformatics at Weill Cornell Medicine.
  This gives him direct, senior-executive visibility into enterprise AWS/AI
  customer deployments — the essay's central claims (customer-question shift,
  organizational over-indexing) read as drawn from that vantage point, but are
  asserted rather than evidenced with named customer examples or a citable
  survey. This is a `trusted-feed` source (per the triage issue), meaning it
  already passed an author-worth-listening-to bar, but the essay itself is an
  opinion/strategy piece, not a data report — the one quantitative claim with
  a named source (Claim 3, price-decline rates) cites Epoch AI and Artificial
  Analysis by name without a link or specific benchmark citation this note
  could independently follow.
- **Scope**: Covers the frontier-vs-field cost-dynamics framework, quantified
  price-decline rates for fixed-capability inference, a "materials vs. tools"
  metaphor for when cheap AI becomes infrastructure, the shift in customer
  questions from model selection to model orchestration, a Forrester
  orchestration statistic, three enterprise AI postures (frontier exploration,
  frontier-first development, field-first deployment), and where competitive
  advantage moves once model access is commoditized. Does NOT cover: specific
  tooling, vendor recommendations, a named customer case study, how to
  implement routing/evaluation/cost-control infrastructure, or a rebuttal to
  the argument (the essay is single-voice, no counter-perspective addressed).

## Extracted Claims

### Claim 1: Two AI cost dynamics run simultaneously and look contradictory only because they're measured on different axes — frontier budgets rising vs. fixed-capability prices collapsing
- **Evidence**: Author's opening framing, presented as the essay's thesis before any supporting data.
- **Confidence**: anecdotal (interpretive framing claim, not a measured finding)
- **Quote**: "Two dynamics are running simultaneously in AI, and they are easy to confuse because they are measured on different axes."
- **Our assessment**: This is the essay's organizing device and its main contribution to the guide's vocabulary — a named distinction (cost-to-push-the-frontier vs. price-of-fixed-capability) that the corpus does not currently have as an explicit framework. It is presented as an observation, not backed by a dataset showing both trends on the same chart, but the two component claims it introduces (Claims 2 and 3 below) are separately more concrete.

### Claim 2: Frontier budgets don't shrink even as fixed-capability prices fall, because the definition of "frontier work" keeps expanding to absorb every efficiency gain
- **Evidence**: Author's own mechanism argument, no external citation.
- **Confidence**: anecdotal (asserted causal mechanism, no measured frontier-lab budget data cited)
- **Quote**: "The frontier never holds capability fixed; it spends every efficiency gain on greater ambition."
- **Our assessment**: This is a plausible mechanism (frontier labs redirect saved compute toward more reasoning/context/tool-use rather than banking the savings) but it is asserted, not demonstrated with frontier-lab R&D spend figures. Useful as a framing device for why "AI is getting cheaper" and "frontier AI spend keeps rising" are not in tension — but the guide should present it as the author's interpretive model, not settled fact.

### Claim 3: Fixed-capability inference price has fallen by roughly 9x/year (GPT-3.5-level general knowledge) to roughly 40x/year (GPT-4-level PhD-science questions), per Epoch AI and Artificial Analysis benchmark price-tracking, with GPT-4-level PhD-science-question performance falling from $30/M tokens (early 2023) to under $1/M (mid-2024) to under $0.10/M (early 2025)
- **Evidence**: Named third-party benchmark-tracking sources (Epoch AI, Artificial Analysis), cited by name but not linked or given a specific report title.
- **Confidence**: emerging (specific, named data sources and concrete dollar figures, but this note could not independently follow a link to the underlying Epoch AI/Artificial Analysis data — the essay does not hyperlink to it, and no URL was recoverable from the page's HTML)
- **Quote**: "GPT-4 level performance on PhD-level science questions has fallen at roughly 40x per year: models that cost $30 per million tokens in early 2023 had equivalents below $1 by mid-2024, and below $0.10 by early 2025."
- **Our assessment**: This is the essay's most concrete, checkable claim and the one the Prospector specifically flagged for extraction. It is directionally consistent with `blog-thoughtworks-kamelman-token-crisis.md` Claim 6's Concrete Artifacts figure ("GPT-4-equivalent performance now costs roughly $0.40 per million tokens, down from $20 per million in late 2022... a 98% reduction," sourced to TheNextWeb/FinOps Foundation) — both sources document dramatic fixed-capability price collapse — but the two give different numbers for a similar comparison (this essay: $30→<$0.10 by early 2025, a >300x drop over roughly two years, using Epoch AI/Artificial Analysis benchmark curves; Kamelman/TheNextWeb: $20→$0.40, a 98%/50x drop over a similar window, from real-world enterprise pricing data). This is not a MINER.md §4a contradiction — both cite different data sources measuring different things (benchmark-threshold price curves vs. observed enterprise billing) over overlapping-but-not-identical time windows — but the guide should not average or reconcile the two figures; cite each to its own source and note that "9x-40x/year" and "98% since 2022" are two independently-sourced quantifications of the same broad phenomenon, not two measurements of the same number.

### Claim 4: Below a capability-usefulness threshold, cheap AI is a curiosity; above it, cheap AI becomes a "material" that gets embedded in infrastructure rather than picked up and put down like a tool
- **Evidence**: Author's own metaphor/argument, illustrated with the claim that the threshold was crossed "somewhere around GPT-4-class usefulness" for professional knowledge work (summarization, drafting, classification, synthesis, coding assistance, analysis, decision support).
- **Confidence**: anecdotal (metaphorical framing, no measurement of "material vs. tool" adoption behavior)
- **Quote**: "Below the threshold, cheap AI is a curiosity. Above it, cheap AI is a material."
- **Our assessment**: The tool-vs-material distinction is a useful rhetorical device for explaining why falling price suddenly matters after a long period of "interesting and practically irrelevant" decline (the essay's own phrase for the pre-GPT-4-class era). It is not a novel empirical claim, but it packages the threshold-effect argument memorably, and it is a plausible complement to the corpus's existing infrastructure-commoditization discussions.

### Claim 5: "The field" is the broad space behind the frontier where capabilities are no longer novel but are cheap and available enough to be built into ordinary work, and Forrester's 2025 automation predictions estimate that genAI orchestrates less than 1% of core business processes despite broad experimentation
- **Evidence**: Author's own definition, paired with a cited (but not linked) Forrester statistic.
- **Confidence**: emerging for the Forrester statistic (named research firm, specific figure, but not independently followed or linked in the source — this note could not verify it against Forrester's original report); anecdotal for the definitional framing itself
- **Quote**: "Forrester's 2025 automation predictions estimate that genAI will orchestrate less than 1% of core business processes, even as it affects process design, development, and data integration."
- **Our assessment**: This is the single most guide-relevant statistic in the essay — a quantified "gap between experimentation and production orchestration" claim from a named analyst firm. It is new to the corpus (no existing source note cites a Forrester orchestration statistic). It should be flagged for independent verification before being cited as settled, since this note only has the essay's restatement of the figure, not the original Forrester report.

### Claim 6: The hard problem has shifted from model access to economic viability — when inference was expensive the model was the system, but now that it's cheap the model is a component and the system is the surrounding work
- **Evidence**: Author's own argument, no external citation.
- **Confidence**: anecdotal (interpretive claim)
- **Quote**: "When capable inference was expensive, the model was the system. Now that it is cheap and getting cheaper, the model is a component, and the system is the work."
- **Our assessment**: This directly corroborates `blog-latentspace-satya-loopcraft-frontier-ecosystems.md` Claim 2 (Nadella: "the real opportunity is not in picking the best model but instead in building a learning loop on top of models") and Claim 7 (practitioner "model neutrality" consensus requiring harness, context, memory, and routing built into the application layer) — three independent voices (an AWS exec, a Microsoft CEO, and a cluster of named practitioners) converging on "the model is becoming a commoditized component, not the differentiator." This essay adds the economic argument (falling fixed-capability price) for *why* that shift is happening now, which neither the Nadella nor the practitioner-consensus source explains mechanistically.

### Claim 7: The question customers ask has shifted from "which model is best?" to "how do I select and chain models so the right one meets the right workload?"
- **Evidence**: Author's own observation, framed as something heard directly from customers ("you can hear the shift in what customers ask"), but no named customer or transcript is quoted.
- **Confidence**: anecdotal (first-person practitioner observation from an AWS executive with direct customer exposure, but unattributed to any specific customer or survey)
- **Quote**: "The question used to be: which model is best? The question now is: how do I select and chain models so the right one meets the right workload?"
- **Our assessment**: Given the author's role (AWS Chief AI & Technology Officer, direct customer-facing position), this carries more weight than a random commentator's guess, but it remains a first-person anecdotal claim rather than data (no survey, no named customer quotes, no count of how many customers ask which question). Useful as a qualitative signal that model routing/orchestration questions are becoming more common than single-model-selection questions, consistent with the broader "model neutrality" architecture trend documented elsewhere in the corpus (Claim 6 above).

### Claim 8: Falling inference cost changes which workflows are worth automating because the return calculation shifts non-linearly as the model-cost line item shrinks — illustrated with a hypothetical (a workflow saving an analyst fifteen minutes isn't worth $5 in inference cost, but the calculation changes at $0.05, and changes again at $0.005)
- **Evidence**: Author's own illustrative example; not an empirical case study.
- **Confidence**: anecdotal (hypothetical numbers, not drawn from a real workflow or customer)
- **Quote**: "A workflow that saves an analyst fifteen minutes is not worth $5 in inference cost. At $0.05, the calculation changes. At $0.005, it changes again."
- **Our assessment**: This is a clean illustrative device for explaining why cost curves matter to ROI decisions even when the underlying task (saving 15 minutes) never changes — but it is a made-up example, not a real cost breakdown, and the essay is explicit that "model cost was only one line in a budget that also included integration, exception handling, and ownership," so falling model cost alone does not automatically make a workflow worth building. The guide should present this as an illustrative heuristic, not a proven ROI formula.

### Claim 9: Organizations should pursue three distinct postures — frontier exploration (probing what's newly possible), frontier-first development (building at frontier prices assuming price follows capability down), and field-first deployment (surveying and instrumenting already-run workflows where the return is real) — and most organizations are over-indexed on the first two, leaving field-first deployment as where the untapped value sits
- **Evidence**: Author's own strategic framework, presented as the essay's central prescriptive claim; no data on the actual distribution of organizational effort across the three postures beyond the Forrester statistic (Claim 5) offered as indirect support.
- **Confidence**: anecdotal (prescriptive framework, not tested against a named organization's resource-allocation data)
- **Quote**: "Most organizations are over-indexed on the first two. The third is where the untapped value sits."
- **Our assessment**: This "three postures" framework is the essay's most directly actionable contribution and the one the Prospector's triage comment specifically flagged for extraction. It is new to the corpus — no existing source note names "frontier exploration / frontier-first development / field-first deployment" as a triad. It is presented as the author's own strategic judgment rather than backed by a survey of where organizations actually allocate AI investment (only the indirect Forrester <1%-orchestration statistic supports the "under-indexed on field" half of the claim); the "over-indexed on frontier" half is asserted without a comparable citation.

### Claim 10: Once the model is a commoditized component, competitive advantage moves to two kinds of "machinery" — technical (routing, evaluation, observability, cost controls) and organizational (proprietary data, process knowledge, clear ownership, and the authority to change how work gets done) — with the organizational kind being harder to buy and the real differentiator between orgs that pull ahead and those that only run pilots
- **Evidence**: Author's own framework, extending directly from Claim 6.
- **Confidence**: anecdotal (strategic framework, not benchmarked against named organizations that have or haven't built this machinery)
- **Quote**: "The second is organizational, and harder to buy off a shelf: proprietary data, process knowledge, clear ownership, and the authority to change how work actually gets done. The first is necessary. The second is what separates the organizations that pull ahead from the ones that run impressive pilots."
- **Our assessment**: This two-part "technical machinery vs. organizational machinery" decomposition is a sharper, more specific version of generic "avoid vendor lock-in" or "build your own harness" advice already in the corpus (e.g., the four-layer model-neutrality decomposition in `blog-latentspace-satya-loopcraft-frontier-ecosystems.md` Claim 7 — harness, context, memory, routing). The novel piece here is naming *organizational authority to change work* as a distinct, harder-to-acquire competitive asset, separate from technical infrastructure — a dimension the practitioner "model neutrality" consensus (which focuses on harness/context/memory/routing) does not explicitly name.

### Claim 11: The frontier and the field don't compete — the frontier creates capability, the price curve makes that capability ordinary, and "today's frontier is next year's field"
- **Evidence**: Author's own closing synthesis.
- **Confidence**: anecdotal (rhetorical conclusion, ties together Claims 1-10 without new evidence)
- **Quote**: "None of these compete. The frontier creates capability; the price curve makes that capability ordinary. Today's frontier is next year's field."
- **Our assessment**: This closing line is the essay's most quotable synthesis and directly supports the guide's likely framing that frontier-chasing and field-deployment are sequential/complementary phases of the same technology, not competing strategies for organizational attention — useful for resolving any perceived tension between "watch the frontier closely" and "deploy known capabilities widely" advice elsewhere in the guide.

## Concrete Artifacts

### The essay's core numeric claims (as stated in prose; no table, chart, or linked source in the original)

```
Source: Matt Wood, "The Field and The Frontier," mattwood.blog, 2026-06-23
(https://mattwood.blog/essays/2026/06/the-field-and-the-frontier/)

- GPT-3.5 Turbo-level performance (general knowledge): ~9x price decline/year
  (stated as "the slowest rate in the data")
- GPT-4-level performance (PhD-level science questions): ~40x price decline/year
  - $30/M tokens (early 2023) -> below $1/M (mid-2024) -> below $0.10/M (early 2025)
  - Cited sources (named, not linked): Epoch AI, Artificial Analysis
- Forrester's 2025 automation predictions: genAI orchestrates <1% of core
  business processes, despite broad experimentation
- Illustrative ROI thresholds (hypothetical, not a real case study):
  a 15-minute-saved workflow "is not worth $5 in inference cost. At $0.05,
  the calculation changes. At $0.005, it changes again."
```

### Author bio (from the site's About page, `https://mattwood.blog/about/`, fetched directly)

```
"I returned to AWS as Chief AI & Technology Officer in 2026, after almost 15
years here earlier in my career and most recently leading commercial
technology and innovation at PwC."

"Earlier: a PhD in machine learning, medical school at the University of
Nottingham, and a postdoctoral fellowship at Weill Cornell Medicine, where I
worked on natural language processing and bioinformatics back when that was
still a niche."

Source: https://mattwood.blog/about/
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-satya-loopcraft-frontier-ecosystems.md` Claim 2 ("the
    real opportunity is not in picking the best model but instead in building
    a learning loop on top of models where human capital and token capital
    compound") and Claim 7 (practitioner "model neutrality" consensus: harness,
    context, memory, routing built into the application layer): this essay's
    Claim 6 ("the model is a component, and the system is the work") makes the
    same "model commoditization shifts advantage elsewhere" argument as a
    third independent voice (AWS exec, alongside a Microsoft CEO and a cluster
    of named practitioners), and supplies the economic mechanism (fixed-
    capability price collapse, Claim 3) that the other two sources assert but
    don't explain.
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 6 (TheNextWeb-sourced:
    "per-token API prices fell 98%... from $20 to $0.40 per million tokens
    since late 2022... while enterprise AI bills rose an estimated 320%"):
    both sources document dramatic fixed-capability price collapse over
    a similar 2022-2025 window, though with different specific figures from
    different data sources (see Claim 3's "Our assessment" for why this is
    not treated as a contradiction).
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 7 (frontier
    per-token list prices have continued rising release-over-release: Opus
    4.6 -> Opus 4.7 (+46%) -> Fable 5 (+100%)): this is the frontier-budget
    half of this essay's Claim 1/Claim 2 argument in concrete pricing-table
    form — top-tier list prices rising even as fixed-capability-tier prices
    fall is exactly the "two axes" distinction this essay's Claim 1 makes.

- **Contradicts**: None identified as a MINER.md §4a contradiction. The
  different price-decline figures between this essay (Claim 3: $30->under
  $0.10/M, ~40x/year via Epoch AI/Artificial Analysis benchmark curves) and
  `blog-thoughtworks-kamelman-token-crisis.md` (98% / $20->$0.40 via
  TheNextWeb/FinOps Foundation enterprise pricing data) are two independently
  sourced quantifications of the same broad phenomenon using different
  methodologies and time windows, not two claims about the same measurement
  that disagree — see Claim 3's "Our assessment" for the full reasoning. No
  contradiction issue filed.

- **Extends**:
  - `docs-ghaw-cost-management.md` and `blog-simonwillison-agentsview-custom-model-price.md`:
    both cover organizational and individual-practitioner cost *tracking*
    tooling. This essay extends that with a strategic *why it matters*
    argument — falling fixed-capability price is what makes previously
    marginal workflows worth instrumenting in the first place (Claim 8),
    which is the economic precondition for needing the cost-tracking tooling
    those notes describe.
  - `blog-latentspace-satya-loopcraft-frontier-ecosystems.md`: extends
    Nadella's "frontier ecosystem, not just a frontier model" framing (that
    note's Claim 4) with a named three-posture taxonomy (Claim 9 here: frontier
    exploration / frontier-first development / field-first deployment) that
    gives practitioners a more granular vocabulary than Nadella's single
    ecosystem-vs-model dichotomy.

- **Novel**:
  - The explicit "field vs. frontier" framework and definition (Claim 1,
    Claim 5) — no existing corpus source names this distinction.
  - The three-posture taxonomy (frontier exploration / frontier-first
    development / field-first deployment) and the claim that most
    organizations are over-indexed on the first two (Claim 9) — new
    vocabulary and a new prescriptive framework for the corpus.
  - The Forrester <1%-of-core-business-processes-orchestrated statistic
    (Claim 5) — the corpus's first citation of this specific figure.
  - The "material vs. tool" metaphor for the usefulness threshold at which
    falling AI price starts to matter (Claim 4) — a new framing device, not
    previously in the corpus.
  - The two-part "technical machinery vs. organizational machinery"
    competitive-advantage decomposition, specifically naming "authority to
    change how work actually gets done" as a distinct organizational asset
    (Claim 10) — sharper than the corpus's existing harness/context/memory/
    routing decomposition because it separates technical infrastructure from
    organizational authority as two independently necessary conditions.

## Guide Impact

- **Chapter 02 (Building Blocks & Infrastructure / Model Selection)**: Add the
  "field vs. frontier" distinction (Claim 1) as framing for why falling
  fixed-capability prices (Claim 3) don't contradict rising frontier-model
  list prices (already documented via `blog-simonwillison-agentsview-custom-model-price.md`
  Claim 7's Opus 4.6->4.7->Fable 5 pricing escalation) — these are the same
  phenomenon Wood's essay names as two axes, not a pricing inconsistency in
  the corpus's own data.

- **Chapter 03 (Operationalization)**: Add the illustrative ROI-threshold
  example (Claim 8: $5 vs. $0.05 vs. $0.005 per workflow-run) as a heuristic
  for when previously-marginal workflows become worth instrumenting as
  fixed-capability inference cost falls, alongside the existing cost-
  management docs (`docs-ghaw-cost-management.md`). Flag it explicitly as
  illustrative, not a validated formula.

- **Chapter 04 (Organizational Patterns)**: Add the three-posture taxonomy
  (Claim 9: frontier exploration / frontier-first development / field-first
  deployment) as a named framework for auditing where an organization's AI
  investment is actually going, paired with the Forrester <1%-orchestration
  statistic (Claim 5) as the indirect evidence that most orgs are under-
  invested in the field-first posture. Add the technical-vs-organizational
  "machinery" decomposition (Claim 10) as a sharper, complementary framing to
  the existing harness/context/memory/routing "model neutrality" checklist
  from `blog-latentspace-satya-loopcraft-frontier-ecosystems.md` Claim 7 —
  specifically the "authority to change how work actually gets done" as a
  distinct organizational asset not currently named in the guide.

- **Chapter 01 (Concepts)**: Consider the "model is a component, not the
  system" reframing (Claim 6) as a concept-level anchor, since it is now
  corroborated by three independent voices in the corpus (this essay, Nadella
  via `blog-latentspace-satya-loopcraft-frontier-ecosystems.md`, and the
  practitioner "model neutrality" cluster in the same note).

## Extraction Notes

1. **WebFetch's summarizer refused verbatim full-article reproduction** (a
   copyright-appropriate response to a "reproduce the whole article verbatim"
   prompt) and, on a follow-up targeted-quote prompt, returned quotes that
   could not be trusted as character-for-character without independent
   verification. Per MINER.md §2a, this note does not rely on either
   WebFetch response for quotes. The full article HTML was instead retrieved
   directly via `curl` (with a browser user-agent, HTTP 200) and parsed to
   plain text by stripping script/style tags and HTML markup. All quotes in
   this note were copied character-for-character from that locally-parsed
   text.
2. The article contains no outbound hyperlinks in its body (confirmed by
   inspecting the raw HTML's `<a>` tags — the only links are two navigation
   links to the site root). The essay's two named data sources for Claim 3
   (Epoch AI, Artificial Analysis) and the Forrester statistic in Claim 5 are
   named in prose only, with no link this note could follow to verify the
   underlying figures directly — flagged as a limitation in each claim's
   confidence rating.
3. The site's About page (`https://mattwood.blog/about/`) was also fetched
   directly via `curl` to establish author credibility (Concrete Artifacts
   section), since the essay itself carries no byline/bio.
4. No contradiction issues filed. The closest candidate (differing price-
   decline figures vs. `blog-thoughtworks-kamelman-token-crisis.md`) was
   evaluated against MINER.md §4a and judged not to qualify — see Claim 3 and
   Cross-References → Contradicts for the full reasoning.
5. This note did not follow any sub-pages beyond the About page (the essay
   itself has no linked sub-pages to follow, per MINER.md §1's "up to 5 linked
   pages" guidance — there were none to follow).
