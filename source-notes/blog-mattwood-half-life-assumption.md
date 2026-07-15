---
source_url: https://mattwood.blog/essays/2026/07/the-half-life-of-an-assumption/
source_type: blog-post
title: "The Half-Life of an Assumption"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-07-14
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: anecdotal
issue: "#1892"
---

# The Half-Life of an Assumption

> Matt Wood (AWS Chief AI & Technology Officer) argues, via a nautical-chart
> and "Notices to Mariners" analogy, that every consequential organizational
> decision has a half-life — the conditions that made it sound erode at
> different rates, AI is accelerating that erosion for capability-related
> assumptions specifically, and the operational fix is to record why a
> decision was made (as testable, re-checkable conditions) rather than only
> what was decided, with AI agents themselves standing the watch for
> threshold crossings.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays"
  collection; short-form, single-author, no comments or citation
  infrastructure; ~1,300 words; no images, tables, data, or outbound
  hyperlinks in the article body — confirmed by inspecting the raw HTML's
  `<a>` tags, which contain only two navigation links to the site root).
- **Author credibility**: Matt Wood is AWS's Chief AI & Technology Officer,
  having returned to AWS in 2026 after nearly 15 years there earlier in his
  career and, most recently, leading commercial technology and innovation at
  PwC (per the site's About page, fetched directly). He holds a PhD in
  machine learning and did a postdoctoral fellowship in NLP/bioinformatics at
  Weill Cornell Medicine. This is the same author and site as
  `blog-mattwood-field-and-frontier.md` (published three weeks earlier,
  2026-06-23); the bio and credibility assessment there apply unchanged here
  (verified by re-fetching the About page for this extraction — text is
  identical). As with that essay, this is a `trusted-feed` source that has
  already passed an author-worth-listening-to bar, but the piece itself is a
  strategy/framework essay, not a data report: it contains zero named
  customer examples, zero benchmarks, and zero citations of any kind — every
  claim is the author's own argument or metaphor, not third-party evidence.
- **Scope**: Covers the "half-life of an assumption" framework (organizational
  decisions decay because the conditions that made them sound change, not
  because the original analysis was wrong), the nautical-chart / Notices to
  Mariners analogy for why authoritative and current are different
  properties, the observation that AI capability assumptions are now among
  the fastest-decaying beliefs an organization holds, the practice of
  recording decision conditions as testable triggers, the idea of AI agents
  continuously re-testing old decisions against new models, a decay-rate-based
  cadence for different assumption types, the distinction between
  "corrections" (small fixes) and "new editions" (rebuilds), and a durable-
  vs-flexible taxonomy of what should and shouldn't be held loosely. Does
  NOT cover: any named company, product, or customer example; any
  quantitative measurement of decay rates, threshold-crossing frequency, or
  rebuild cost; any counter-perspective or rebuttal (single-voice essay); or
  implementation mechanics for the "AI agents re-run the old evaluation"
  proposal (no tooling, workflow, or architecture is described beyond the
  one-paragraph concept).

## Extracted Claims

### Claim 1: Every consequential organizational decision has a half-life — an unmeasurable but real decay rate at which the conditions that made it reliable erode, and AI is raising the rate at which the underlying "territory" changes
- **Evidence**: Author's central thesis, stated directly; no external data.
- **Confidence**: anecdotal (framing/thesis claim, not a measured finding)
- **Quote**: "Every consequential decision has a half-life. Not a number anyone can calculate, but a decay rate all the same: the conditions that made it reliable erode, and some erode far faster than others."
- **Our assessment**: This is the essay's organizing metaphor and its main contribution to the guide's vocabulary — a named concept ("half-life of an assumption") that generalizes a single anecdote already in the corpus (see Cross-References) into a claimed universal property of organizational decisions. It is presented as an observation, not derived from any dataset of decision lifespans, so the guide should treat "half-life" as a useful framing device rather than a measured quantity.

### Claim 2: A nautical chart is authoritative yet goes out of date almost immediately, and navigation as a discipline is built around a structured correction system (Notices to Mariners, issued weekly since 1890) rather than around either treating charts as permanently valid or reprinting a new edition for every change
- **Evidence**: Historical description of chart-making and the British Admiralty's Notices to Mariners system, presented as established maritime practice, not cited to a specific historical source.
- **Confidence**: anecdotal (historical analogy, unsourced beyond the author's own description)
- **Quote**: "A nautical chart is as authoritative as an official document gets: surveyed, compiled, checked, and issued under a national hydrographic office. It is also out of date almost as soon as it is printed. [...] The British Admiralty began issuing Notices to Mariners in 1834, at first sent individually to the ships and squadrons that needed them; by 1890 they had become a regular weekly publication, and hydrographic offices around the world now issue their own."
- **Our assessment**: This is the essay's load-bearing analogy and its most concrete artifact — a real historical practice (a 190-year-old institutional correction system) used to argue that a structured, incremental-correction discipline, not perfect initial accuracy or wholesale reissue, is what keeps authoritative-but-decaying documents useful. The specific dates (1834, weekly by 1890) were not independently verified against a maritime-history source by this note; they are reported as the author's own claim.

### Claim 3: Being authoritative and being current are different properties — a decision can be entirely correct when made and still be wrong later, because the world changed after publication, not because the original analysis was flawed
- **Evidence**: Author's direct restatement of the chart analogy's implication, applied explicitly to organizational decisions.
- **Confidence**: anecdotal (interpretive claim built on the chart analogy)
- **Quote**: "Nothing in the original chart had to be wrong. The surveyors did their work; the cartographers drew what was true. The world changed after publication. Being authoritative and being current are different properties, and the notice system exists because the difference can put a ship on the rocks."
- **Our assessment**: This is a useful reframing for the guide because it separates two failure modes that are often conflated: "we made a bad call" versus "we made a good call whose conditions expired." The essay's prescriptive advice later (Claims 8-9) only makes sense once this distinction is granted — you don't need to blame the original decision-maker to justify revisiting the decision.

### Claim 4: Organizations produce decisions with the care of charts but preserve them like permanent monuments, rarely attaching what changes afterward — somewhere in every organization sits a document asserting an AI capability limit that is no longer true and has never been corrected
- **Evidence**: Author's own generalization, illustrated with an unnamed, hypothetical example (no named company or document is cited).
- **Confidence**: anecdotal (asserted pattern, no survey or named example)
- **Quote**: "Organizations produce decisions with the care of charts and preserve them like monuments. [...] Somewhere in your organization there is a document that says AI cannot do something it can now do, and no notice has ever been issued against it."
- **Our assessment**: This is a plausible but unverified generalization — it is stated as if self-evidently true of "your organization" without a named instance, survey, or audit. Useful as a rhetorical hook for a guide section, but the guide should present it as an illustrative claim, not a documented finding.

### Claim 5: The organizational impact of an AI capability improvement is non-linear relative to the size of the capability gain — a modest improvement can move an entire workload from impractical to routine, and several such threshold crossings landing together across functions feels like a "succession of surprises" to organizations that didn't expect their assumptions to expire
- **Evidence**: Author's own argument, with generic (unnamed) illustrative examples — a process needing less attention, automation that "suddenly" pays for itself, a previously-impossible product experience becoming buildable.
- **Confidence**: anecdotal (illustrative, no named workload or measured threshold)
- **Quote**: "The organizational impact does not rise smoothly with capability. A modest improvement can move an entire workload from impractical to routine. [...] Organizations that discover each change only when it interrupts an existing plan will experience the period as a succession of surprises. Those that expect their assumptions to expire will still need to adapt, but they will have made room for adaptation before knowing exactly what would change."
- **Our assessment**: The nonlinearity claim (small capability gain, large workload-viability shift) is a useful mechanism for why "we'll just track the roadmap of model releases" under-prepares organizations — the disruptive event is a threshold crossing in a specific workload, not a headline model release. This complements rather than duplicates the corpus's existing "roadmap half-life" anecdote (see Cross-References), which documents the after-the-fact symptom without explaining this mechanism for why it happens abruptly.

### Claim 6: Different classes of organizational assumption decay at very different rates — customer-value assumptions (reliability, price, ease of use) can hold for years, while assumptions about AI capability are now among the fastest-decaying beliefs an organization holds, with model-choice assumptions going stale in weeks and agent-configuration assumptions in days
- **Evidence**: Author's own claim, presented as a direct comparison; no measurement of "weeks" or "days" beyond the assertion itself.
- **Confidence**: anecdotal (specific time figures asserted without a named benchmark or audit trail)
- **Quote**: "An assumption that customers will continue to care about reliability, price, and ease of use can hold for years, while an assumption about what the technology can do is now among the fastest-decaying beliefs an organization holds: a view about which model is best for a workload can go stale in weeks, and the right agent configuration in days."
- **Our assessment**: This is the essay's most concrete, checkable-sounding claim (specific units: years / weeks / days) and the one most useful for calibrating a guide recommendation, but it is not backed by a named case, survey, or dataset — it reads as the author's professional judgment from an AWS customer-facing vantage point (consistent with his role, per `blog-mattwood-field-and-frontier.md`'s credibility assessment) rather than a measured decay curve. The guide should cite the relative ordering (capability assumptions decay fastest, customer-value assumptions decay slowest) as directionally useful while flagging the specific week/day figures as illustrative, not measured.

### Claim 7: Decisions acquire self-reinforcing authority from the artifact and investment built on top of them — a mature system, a large team, or a detailed roadmap becomes evidence for the correctness of the decision that produced it, independent of whether the original conditions still hold
- **Evidence**: Author's own mechanism argument, with generic illustrative examples (a system with years of investment, a large team, a detailed roadmap).
- **Confidence**: anecdotal (asserted mechanism, no named organizational case)
- **Quote**: "The more work that went into a decision, the more authority it acquires. Then the artifact built from it begins to reinforce it: a system with years of investment looks appropriate because it exists, a large team appears to prove that the problem requires a large team, a detailed roadmap makes the destination look understood. The artifact becomes evidence for the decision that produced it."
- **Our assessment**: This names a specific circularity (sunk investment mistaken for confirming evidence) that is a sharper, more mechanistic version of generic "sunk cost fallacy" framing — it explains *why* organizations resist reopening decisions (the artifact itself feels like proof), not just *that* they resist. Useful as a diagnostic for a guide section on why stale assumptions persist even when contradicting evidence is available.

### Claim 8: The practical response is to record why a decision was made — the specific, testable conditions that made it sound — not only what was decided, so the decision carries its own trigger for reconsideration
- **Evidence**: Author's own prescriptive argument, illustrated with a generic example (a workflow excluded from automation because computer use failed too often, supervision erased the economic benefit, or remaining errors carried too much risk).
- **Confidence**: anecdotal (prescriptive practice, not evaluated against a named organization's adoption)
- **Quote**: "That starts with recording why a decision was made, not only what was decided. A workflow excluded from automation was rarely judged inherently unsuitable; it was excluded because computer use failed too often, supervision erased the economic benefit, or the remaining errors carried too much risk. Those are testable conditions, and the decision can carry its own triggers for reconsideration."
- **Our assessment**: This is the essay's single most actionable recommendation and converges directly with `blog-addyosmani-intent-debt.md`'s Claim 8 recommendation to capture decision rationale via lightweight ADRs — two independent authors, writing about different problems (assumption decay vs. agent-generated-code rationale), arrive at the same operational practice: record the *why*, not just the *what*. Wood's essay adds a mechanism Osmani's does not: framing the recorded rationale specifically as *testable conditions* that can trigger automatic re-evaluation, rather than only as institutional memory for future readers.

### Claim 9: AI agents can serve as the "watch" for decision decay — continuously re-running an old decision's original test cases and exceptions against new models, and returning the question to its owner with evidence attached, rather than requiring humans to track general AI news
- **Evidence**: Author's own proposal, extending Claim 8; no implementation detail, tooling, or named example is given beyond the one-paragraph concept.
- **Confidence**: anecdotal (proposed practice, no evidence it has been built or tried anywhere)
- **Quote**: "Keeping the original test cases makes that retest cheap, and AI can stand the watch itself: agents can track new models against the old evaluation, attempt the same requests and the same exceptions, and return the question to its owner with evidence attached rather than a general stream of AI news. The organization never has to debate computer use in the abstract. It learns whether the result on its own work has crossed the threshold that made the original decision fail."
- **Our assessment**: This is the essay's most novel and most guide-actionable proposal — pairing a decision record (Claim 8) with retained test cases lets an agent mechanically check "has the condition that made us say no changed?" without a human having to relitigate the original debate. It is unimplemented and unevaluated in this source (no tooling, cost, or false-positive-rate discussion), so the guide should present it as a promising pattern to try, not a proven practice.

### Claim 10: The review cadence for a decision should follow its decay rate, not a uniform schedule — model selection should become continuous rather than ceremonial, workflow design should move more slowly and be driven by operational data, customer-need understanding should come from sustained customer contact, and organizational purpose should barely move at all
- **Evidence**: Author's own prescriptive framework, synthesizing Claims 6 and 8-9 into a cadence-per-assumption-type recommendation.
- **Confidence**: anecdotal (prescriptive framework, no named organization's review cadence cited as validation)
- **Quote**: "The point is not to keep every decision open; permanent uncertainty would make coordinated action impossible. The point is to know which decisions deserve to be reopened, and when. The cadence should follow the decay rate: model selection becomes continuous rather than ceremonial, workflow design moves more slowly on operational data, customer needs are read through sustained contact with customers, and purpose barely moves at all."
- **Our assessment**: This is a clean rebuttal to the "if everything might change, review everything constantly" misreading of the essay's thesis — it explicitly argues for tiered cadences, not universal openness. It is the essay's clearest actionable guidance for how an organization should structure its own re-evaluation practice, though it remains a prescriptive framework rather than a tested one.

### Claim 11: Not every expired assumption calls for the same kind of fix — some are cheap "handwritten corrections" (reassign a model, move a review point, update a threshold), others require a "new edition" (a rebuild), and AI is simultaneously invalidating more decisions and lowering the cost of rebuilding them, changing the calculus between patching and replacing even for large systems
- **Evidence**: Author's own framework, extending the chart-correction analogy (Claim 2) to organizational rebuild decisions.
- **Confidence**: anecdotal (framework claim, no named rebuild-vs-patch case study or cost comparison)
- **Quote**: "Not every expired assumption calls for the same response. Some are handwritten corrections: a review point moves, a model assignment changes, a threshold gets updated. Others call for a new edition [...] AI is changing that calculation. Prototyping a replacement, testing an alternative architecture, migrating a system: each is becoming cheap enough to change the choice between continued patching and replacement, and the same capability jump that invalidates an implementation also reduces the cost of replacing it."
- **Our assessment**: The observation that the same capability jump both invalidates old decisions *and* cheapens their replacement is the essay's sharpest structural point — it argues the two effects are coupled, not coincidental, which is a stronger claim than simply "rebuilding got cheaper." No cost figures or named migration are given, so the guide should treat the "coupling" argument as a plausible mechanism worth citing alongside, not in place of, any concrete cost data the corpus already has for AI-assisted migrations.

### Claim 12: What should stay durable versus what can be held lightly is itself a design choice — purpose, customer promises, accountability, security boundaries, and the evidence required to trust a result should be stable, while models, configurations, workflow designs, and implementation plans can change without that being read as abandoning the objective
- **Evidence**: Author's own closing framework, presented as a direct taxonomy.
- **Confidence**: anecdotal (prescriptive taxonomy, not derived from a named organization's governance model)
- **Quote**: "This is where stability belongs. Purpose, customer promises, accountability, security boundaries, and the evidence required to trust a result should be durable. Models, configurations, workflow designs, and implementation plans can be held more lightly, and a change of route should not be read as a retreat from the objective or a repudiation of the people who pursued it."
- **Our assessment**: This durable-vs-flexible taxonomy is the essay's most reusable artifact for a guide section on organizational design — it gives a concrete checklist of what to lock down (purpose, promises, accountability, security, trust-evidence) versus what to explicitly keep provisional (models, configs, workflow design, implementation plans). It is asserted rather than derived from a named case, but it is specific enough to be directly actionable as governance guidance.

## Concrete Artifacts

### The Notices to Mariners historical timeline (as stated in prose; no citation or link in the original)

```
Source: Matt Wood, "The Half-Life of an Assumption," mattwood.blog, 2026-07-14
(https://mattwood.blog/essays/2026/07/the-half-life-of-an-assumption/)

- 1834: British Admiralty begins issuing Notices to Mariners
         (initially sent individually to ships/squadrons that needed them)
- 1890: Notices to Mariners become a regular weekly publication
- Present: Hydrographic offices worldwide issue their own notices
- Chart reliability = (quality of original survey) + (whether corrections
  are up to date) — two independent properties, not one
```

### Decay-rate cadence table (author's own framework, not presented as a table in the original — reconstructed here from the prose in Claim 10)

```
Assumption type          | Recommended review cadence
--------------------------|----------------------------------
Model selection           | Continuous (not ceremonial)
Workflow design            | Slower, driven by operational data
Customer needs             | Read via sustained customer contact
Organizational purpose     | Barely moves at all
```

### Durable vs. flexible taxonomy (Claim 12)

```
Durable (should be stable):
  - Purpose
  - Customer promises
  - Accountability
  - Security boundaries
  - Evidence required to trust a result

Flexible (can be held lightly):
  - Models
  - Configurations
  - Workflow designs
  - Implementation plans
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

Source: https://mattwood.blog/about/ (re-fetched 2026-07-15; text unchanged
from the version quoted in `blog-mattwood-field-and-frontier.md`)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-ai-native-engineering-org.md` Claim 2 (the Claude Code
    team's six-month roadmap was "out of date by month three") is a concrete,
    named anecdote that this essay's Claim 1 ("every consequential decision
    has a half-life... AI is increasing the rate at which the territory
    changes") generalizes into a named framework. The Anthropic note documents
    the symptom (a specific roadmap decayed fast); this essay supplies the
    general mechanism and vocabulary ("half-life," conditions eroding at
    different rates) and extends it beyond planning documents to all
    organizational assumptions.
  - `blog-addyosmani-intent-debt.md` Claim 8 (four intent-debt paydown
    practices, including "capture decisions where they happen — lightweight
    decision logs (ADRs) are pure intent-debt paydown"): this essay's Claim 8
    (record *why* a decision was made, not only what) is the same operational
    practice — recording decision rationale — arrived at independently by two
    different authors solving different problems (Osmani: agents cannot
    fabricate-then-restore lost intent; Wood: decisions need testable
    triggers for re-evaluation). Two independent voices converging on
    "write down the why" strengthens the case for recommending it as a
    named practice in the guide.
  - `blog-mattwood-field-and-frontier.md` (same author, three weeks earlier):
    that essay's Claim 7 ("the question customers ask has shifted from
    'which model is best?' to 'how do I select and chain models'") is
    consistent with this essay's Claim 10 recommendation that model
    selection should become a "continuous" rather than "ceremonial" review —
    both describe model choice as a moving target requiring ongoing
    attention rather than a one-time decision.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  existing corpus note argues that organizational decisions should be
  treated as permanently fixed once made, so this essay's central thesis
  does not conflict with prior source notes. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-ai-native-engineering-org.md`: extends the "roadmap
    half-life" anecdote (a single team's planning-document experience) into
    a general organizational-decision framework with concrete operational
    practices (record testable conditions, use AI agents to monitor
    threshold crossings, tier review cadence by decay rate) that the
    Anthropic note does not itself propose.
  - `blog-addyosmani-intent-debt.md`: extends the "record the why, not just
    the what" recommendation with a specific downstream use — the recorded
    rationale becomes a *testable trigger condition* an agent can
    mechanically re-check against new models (Claim 9), rather than only
    institutional memory for future human readers.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 8
    (scheduled "drift review" red-team exercises to verify an agent still
    operates within its originally granted authority): a structurally
    similar idea — periodic re-verification against the *original* granting
    conditions — applied to a different domain (agent authority/permissions
    rather than capability-based business decisions). This essay's Claim 9
    (AI agents re-running old evaluations against new models) is the same
    "verify against original conditions, don't assume they still hold"
    discipline, generalized from a security/governance context to a
    planning/strategy context.

- **Novel**:
  - The "half-life of an assumption" framing itself, generalized beyond
    planning/roadmap documents to all organizational decisions (Claim 1) —
    no existing corpus note uses decay-rate/half-life vocabulary for
    organizational assumptions broadly.
  - The nautical-chart / Notices to Mariners historical analogy (Claim 2) and
    the "authoritative vs. current are different properties" distinction
    (Claim 3) — a new framing device not previously in the corpus.
  - The claim that AI capability assumptions are now among the
    fastest-decaying organizational beliefs, with specific (if unmeasured)
    week/day figures for model-choice and agent-configuration assumptions
    (Claim 6) — a new, if anecdotal, calibration point.
  - The "artifact becomes evidence for the decision that produced it"
    circularity (Claim 7) — a sharper mechanism than generic sunk-cost
    framing, not previously named this precisely in the corpus.
  - The proposal to use AI agents themselves as continuous monitors,
    re-running a decision's original test cases against new models and
    returning evidence to the decision's owner (Claim 9) — new to the
    corpus as a concrete (if unimplemented) pattern.
  - The decay-rate-tiered review cadence (Claim 10) and the durable-vs-
    flexible taxonomy (Claim 12) — both new, reusable frameworks not
    previously named in the corpus.
  - The "corrections vs. new editions" framing (Claim 11) and the specific
    argument that the same capability jump both invalidates old decisions
    and cheapens their replacement — a coupling argument not previously
    made in the corpus's existing migration/rebuild-cost material.

## Guide Impact

- **Chapter 02 (Planning)**: Extend the existing "JIT planning" /
  roadmap-half-life guidance (currently anchored only on the Anthropic
  Claude Code team's "out of date by month three" anecdote via
  `blog-anthropic-ai-native-engineering-org.md`) with this essay's concrete
  operational practice: record the *testable conditions* that made a
  planning decision sound (Claim 8), not just the decision, so the plan
  carries its own re-evaluation trigger. Add the decay-rate-tiered cadence
  (Claim 10 — continuous for model selection, slower for workflow design,
  slowest for purpose) as a specific recommendation for how often different
  categories of planning assumption should be revisited, replacing any
  implicit "review everything on the same schedule" default.

- **Chapter 03/04 (Organization)**: Add the durable-vs-flexible taxonomy
  (Claim 12: purpose, customer promises, accountability, security
  boundaries, and trust-evidence as durable; models, configs, workflow
  designs, and implementation plans as flexible) as explicit governance
  guidance for what an organization should lock down versus keep
  provisional. Pair this with the "artifact becomes evidence for the
  decision" circularity (Claim 7) as a named failure mode to watch for when
  auditing why a stale decision has persisted despite contradicting
  evidence.

- **Chapter 05/06 (Evaluation & Cost-of-Validation)**: Add the "AI agents
  standing the watch" proposal (Claim 9 — retaining a decision's original
  test cases so an agent can mechanically re-run them against new models and
  surface threshold crossings) as a concrete, if unproven, pattern to pilot
  for continuous re-validation of model-selection and automation-feasibility
  decisions. Flag it explicitly as an untested proposal from this source,
  not a validated practice — no tooling, cost, or false-positive data is
  given in the essay.

## Extraction Notes

1. The full article was retrieved directly via `curl` (browser user-agent,
   HTTP 200) and parsed to plain text by stripping script/style tags and
   HTML markup, per the same method used for
   `blog-mattwood-field-and-frontier.md` (that note documented WebFetch's
   summarizer refusing verbatim reproduction and untrustworthy quote
   fidelity on a follow-up prompt; this extraction did not attempt WebFetch
   at all and went straight to the direct-fetch method). All quotes in this
   note were copied character-for-character from that locally-parsed text.
2. The article contains no outbound hyperlinks in its body (confirmed by
   inspecting the raw HTML's `<a>` tags — only two navigation links to the
   site root). No sub-pages were followed beyond the About page, per
   MINER.md §1's "up to 5 linked pages" guidance — there were none in the
   essay to follow.
3. The site's About page (`https://mattwood.blog/about/`) was re-fetched
   directly via `curl` for this extraction (rather than reused verbatim from
   the companion note) to confirm the bio text had not changed since
   `blog-mattwood-field-and-frontier.md` was written on 2026-07-06; it is
   identical.
4. No contradiction issues filed. This essay's thesis (decisions should be
   provisional and periodically re-tested) was checked against the corpus
   for any note arguing the opposite (decisions should be treated as
   permanently fixed); none was found, so no MINER.md §4a contradiction
   applies.
5. The three separate Prospector triage comments on issue #1892 gave
   slightly different "relevant chapters" lists (Ch02/03/06; Ch01/04/02;
   Ch02/03/05) but converged on the same key question and the same
   assessment of novelty and existing-note overlap. This note's Guide Impact
   section synthesizes across all three rather than picking one.
