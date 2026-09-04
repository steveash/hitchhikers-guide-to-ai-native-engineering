---
source_url: https://mattwood.blog/essays/2026/08/the-wicked-frontier/
source_type: blog-post
title: "The Wicked Frontier"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-08-31
date_extracted: 2026-09-04
last_checked: 2026-09-04
status: current
confidence_overall: anecdotal
issue: "#3217"
---

# The Wicked Frontier

> Matt Wood (AWS Chief AI & Technology Officer) applies Rittel and Webber's
> 1973 tame/wicked problem distinction to AI adoption: AI advances fastest on
> "tame" problems (checkable, no need to reopen the goal) and stalls on
> "wicked" problems (no stopping rule, resolution requires *standing* — the
> authority to decide and the accountability to own the outcome — which AI
> cannot establish for itself); most real work is neither, but a "sweet spot"
> of wicked-looking tasks that decompose into tame, AI-automatable substeps
> plus an irreducible judgment residue, and the practical adoption discipline
> is repeatedly separating the two at the level of a single task, not once in
> a strategy document.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays"
  collection; short-form, single-author, no comments or citation
  infrastructure; ~1,000 words; no images, tables, or outbound hyperlinks in
  the article body — confirmed by inspecting the raw HTML's `<a>` tags, which
  contain only navigation links back to the site root).
- **Author credibility**: Matt Wood is AWS's Chief AI & Technology Officer,
  having returned to AWS in 2026 after nearly 15 years there earlier in his
  career and, most recently, leading commercial technology and innovation at
  PwC (per the site's About page, `https://mattwood.blog/about/`, fetched
  directly for this extraction). He holds a PhD in machine learning and did a
  postdoctoral fellowship in NLP/bioinformatics at Weill Cornell Medicine.
  This is the same author and site as the six prior mattwood.blog notes in the
  corpus — `blog-mattwood-field-and-frontier.md`,
  `blog-mattwood-unit-of-return.md`, `blog-mattwood-barcode-bargain.md`,
  `blog-mattwood-half-life-assumption.md`,
  `blog-mattwood-for-your-information.md`, and
  `blog-mattwood-how-this-was-made.md`;
  the bio and credibility assessment in those notes apply unchanged here
  (re-verified by re-fetching the About page for this extraction — the text
  is byte-for-byte identical to the version quoted in those sibling notes).
  As with those essays, this is a `trusted-feed` source that has already
  passed an author-worth-listening-to bar, but the piece itself is a
  conceptual/strategy essay, not a data report: it names no company, customer,
  or study, and gives no measured figure anywhere in its text. Its one
  external citation — Rittel and Webber's 1973 wicked-problems theory — is a
  real, independently verifiable academic framework (Rittel & Webber,
  "Dilemmas in a General Theory of Planning," *Policy Sciences*, 1973), named
  by author and year but without a formal citation or link; everything else
  in the essay is the author's own application of that framework to AI
  adoption, argued rather than measured.
- **Scope**: Covers the tame/wicked distinction via a bridge-construction
  example, Rittel and Webber's 1973 definition of wicked problems, the claim
  that AI advances unevenly across the tame/wicked divide, the concept of
  "standing" as what AI cannot establish, the "sweet spot" of decomposable
  wicked-looking work illustrated with a market-entry-decision example, an
  estimate that the sweet-spot category is "rarely a sliver" of a typical
  week's knowledge work, a critique of uniform "AI adoption" strategy
  ("adoptioneering"), a repeatable task-level procedure for finding the sweet
  spot, and a closing claim about how the three zones evolve as tame
  execution becomes infrastructure. Does NOT cover: any named company,
  product, or customer example; any measured figure for how large the sweet
  spot actually is in any real organization; a citation or link for the
  Rittel and Webber reference; any tooling, workflow, or implementation
  detail for how a team would actually build decomposition capability; or a
  counter-perspective (single-voice essay).

## Extracted Claims

### Claim 1: A consequential problem can split into an objective, checkable part and a subjective, unresolvable-by-analysis part — illustrated with a bridge: engineering constraints (span, traffic, budget, safety) are testable, but whether to build it, where it should land, and whose idea of improvement counts cannot be made objective by analysis
- **Evidence**: Author's own illustrative example, opening the essay.
- **Confidence**: anecdotal (illustrative framing device, not a measured claim)
- **Quote**: "Analysis can inform those choices, but it cannot make them objective. Each possible answer gives different weight to different interests, trade-offs, and preferences."
- **Our assessment**: This is the essay's entry point into the tame/wicked distinction and does real work: it shows the same project (one bridge) contains both problem types simultaneously, rather than presenting tame and wicked as separate categories of *projects*. That framing — one piece of work, two kinds of question braided together — is what later licenses the "sweet spot" claim (Claim 6) that most real tasks are mixed rather than purely one type.

### Claim 2: Rittel and Webber (1973) named "wicked problems" as those that resist formal resolution because different people experience different parts of the problem, there is no agreed stopping rule, and possible answers are better-or-worse rather than true-or-false — the opposite is "tame," where the result is knowable and objective
- **Evidence**: Named academic citation (Rittel & Webber, 1973), given by author/year in prose with no link or formal reference.
- **Confidence**: settled, for the underlying academic theory itself (Rittel and Webber's 1973 wicked-problems framework is a well-established, independently citable concept in planning theory, not an invention of this essay); anecdotal for the essay's own application of the theory to AI adoption, which is Wood's argument, not Rittel and Webber's
- **Quote**: "In 1973, planning theorists Horst Rittel and Melvin Webber gave this second set a name: wicked problems. Wicked did not mean negative, or even exceptionally complicated - but a problem which resists formal resolution. There is no single, definitive account of the problem, because different people are experiencing different parts of it. There is no agreed stopping rule."
- **Our assessment**: The distinction itself is borrowed, not novel — but its use as an operating vocabulary for *AI adoption* specifically is new to this corpus. The essay does not enumerate Rittel and Webber's original ten properties of wicked problems (confirmed by re-reading the full text); it only carries forward the "no stopping rule, better-or-worse not true-or-false" core, which is the part most directly useful for the guide's purposes.

### Claim 3: AI is not advancing at the same rate through both problem types — it moves fastest through tame problems, where an answer can be checked without reopening the goal each time and every attempt provides feedback for the next
- **Evidence**: Author's own causal claim, stated as the essay's central thesis before elaboration.
- **Confidence**: anecdotal (asserted mechanism, no benchmark or measured capability-growth-rate comparison given)
- **Quote**: "A proof can be verified. Code can be run against a test suite. A structural design can be checked against stated limits. These problems may be ferociously hard, but their difficulty has a shape. An answer can be checked without reopening the goal each time. Where answers are cheap to check and new problems cheap to create, progress can compound quickly. I call this the tame frontier."
- **Our assessment**: This is a specific mechanistic claim (cheap verification → compounding progress) rather than a vague "AI is good at technical work" observation, and it gives the guide's existing verification-as-bottleneck thesis (`guide/03-verification.md`) an explanatory frame at the capability-growth level, not just the workflow-design level — see Guide Impact.

### Claim 4: The tame frontier covers software, engineering, physics, and materials science, especially where strong simulations or automated experiments exist; most knowledge work, by contrast, is "wicked work" because the target cannot be inferred from the problem itself
- **Evidence**: Author's own taxonomy, listing named domains for the tame frontier.
- **Confidence**: anecdotal (categorical claim, no data on what share of "knowledge work" is wicked vs. tame)
- **Quote**: "Tasks related to software, engineering, physics, and materials science sit inside it, especially where strong simulations or automated experiments exist. [...] However, most knowledge work does not have that shape. Knowledge work is wicked work."
- **Our assessment**: The domain list is a concrete, checkable claim about *where* the tame frontier currently sits — useful for grounding the more abstract tame/wicked distinction in named fields rather than leaving it purely conceptual. The "most knowledge work is wicked" half is a sweeping generalization asserted without measurement; Claim 6 below partly walks this back by arguing wicked-*looking* work is often internally mixed.

### Claim 5: What current AI capability cannot establish is "standing" — the right to make the call and the responsibility to own what follows — and this gap does not close as models get more capable; it relocates to wherever the next consequential definition hasn't been made yet
- **Evidence**: Author's own definitional and structural claim, the essay's most quoted line per the earlier Prospector triage comments.
- **Confidence**: anecdotal (asserted claim about the limits of AI capability, not derived from a benchmark or a case where capability gains were tracked against standing specifically)
- **Quote**: "What today's AI capabilities cannot establish is standing — the right to make the call and the responsibility to own what follows: whose interests should prevail, who had the authority to define the objective, who remains accountable afterward. [...] That gap doesn't close as models get more capable. It relocates, to wherever the next consequential definition hasn't been made yet."
- **Our assessment**: This is the essay's sharpest and most guide-relevant claim — it reframes "AI can't do wicked work yet" (a capability statement, which model progress could falsify) as "AI can't hold standing" (a structural statement about authority and accountability, which model progress cannot address by definition). This directly corroborates `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 4 (a core unresolved question is who owns the consequences when an agent acts correctly within its instructions and the organization still suffers harm) and Claim 2 (guardrails can prevent rule violations but cannot catch judgment failures) — three independent authors converging on accountability/authority, not raw capability, as the limiting factor for agentic autonomy over judgment work.

### Claim 6: No real job sits purely at either extreme — a single week mixes genuinely tame work worth automating outright, wicked work where judgment must stay visible, and wicked-*looking* work that is tame underneath and worth decomposing; this last category is the "sweet spot" for AI
- **Evidence**: Author's own categorical claim, introducing the essay's central "sweet spot" concept.
- **Confidence**: anecdotal (categorical claim, no measured distribution of a real team's work across the three categories)
- **Quote**: "No real job sits perfectly inside these two extremes. A single week moves through work that's genuinely tame and worth automating outright, some that's wicked all the way down, where the judgment must remain visible and someone must own it, and some that's wicked-looking but tame underneath and worth decomposing. For AI, that's often the sweet spot."
- **Our assessment**: This is the essay's operational payoff — it converts the tame/wicked binary into a three-way categorization (tame / sweet spot / wicked) that maps directly onto a differentiated adoption strategy in Claim 9. Still asserted rather than measured, but it is a specific, three-part taxonomy rather than a restatement of the binary.

### Claim 7: A market-entry decision looks wicked at first glance (risk appetite, competitive response, what success means) but decomposes into individually plain substeps — pulling market data, modeling pricing scenarios, summarizing comparable-company precedent, drafting framings — none of which require the underlying decision to already be made
- **Evidence**: Author's own worked example, the essay's single concrete illustration of sweet-spot decomposition.
- **Confidence**: anecdotal (a single hypothetical, unnamed example, not a real case study)
- **Quote**: "Pull the relevant market data. Model a few pricing scenarios. Summarize how three comparable companies handled a similar entry. Draft two or three framings of the decision so a leader can react to something concrete instead of a blank page. None of those steps require anyone to have already decided what the company should do."
- **Our assessment**: This is the essay's only worked example, and it is doing real conceptual work: each named substep (data pull, scenario modeling, precedent summary, framing draft) has a checkable target once separated from "should we enter this market," which is exactly the "reopening the goal" distinction from Claim 3 applied to a single task rather than a whole problem class. No real organization or outcome is named, so this remains illustrative rather than evidenced.

### Claim 8: The sweet-spot category — decomposable, wicked-looking work — is large enough across an ordinary week of knowledge work (research, drafting, checking numbers, coordinating logistics, preparing materials for someone else's decision) to plausibly change the economics of most jobs, though the exact balance varies by role
- **Evidence**: Author's own estimate, reasoning from an enumerated list of common knowledge-work activities rather than from measured task-time data.
- **Confidence**: anecdotal (an estimate reasoned from an unweighted list of activity types, not a time-and-motion study or survey)
- **Quote**: "The exact balance differs by role, but it is rarely a sliver. It could be large enough to change the economics of most jobs."
- **Our assessment**: This is the essay's most aggressive quantitative-sounding claim and its weakest-evidenced one — "rarely a sliver" and "could be large enough" are hedged, non-numeric language, not a measured percentage. The guide should cite this as the author's directional judgment (the sweet spot is probably substantial) rather than as a sized estimate, and should flag that no organization-level measurement of decomposable-task share currently exists in this source or, to this note's knowledge, elsewhere in the corpus.

### Claim 9: Treating "AI adoption" as one uniform push is imprecise because the three zones want different things — the tame zone wants automation, the sweet spot wants decomposition and tooling, and the wicked zone wants people empowered to keep making calls nothing upstream can make for them, with that empowerment increasing as the other two zones free up attention
- **Evidence**: Author's own prescriptive framework, directly following from Claim 6's three-way taxonomy.
- **Confidence**: anecdotal (prescriptive framework, not tested against a named organization's adoption strategy)
- **Quote**: "The tame zone wants automation. The sweet spot wants decomposition and the tooling to do it well. And the wicked zone wants something different from either: people empowered to keep making the calls nothing upstream can make for them, and increasingly empowered as the other two zones improve and free up the time and attention to do it properly."
- **Our assessment**: This gives the guide a differentiated adoption vocabulary sharper than a generic "roll out AI carefully" recommendation — it names three distinct target states (automate / decompose+tool / empower) rather than treating adoption as a single dial to turn up. It also makes an interesting, unverified prediction: that automating the tame and sweet-spot zones *increases* — not decreases — the attention available for wicked-zone judgment, rather than simply eliminating headcount. No evidence is given for that specific redistribution effect.

### Claim 10: The sweet spot is found by a repeatable, task-level procedure — take a wicked-looking request, find the substeps with a clear checkable target once isolated, do those with AI, and keep the residue (the part that still needs a person to decide something) — performed constantly by whoever is closest to the work, not as a single top-down strategy decision
- **Evidence**: Author's own operational procedure, presented as the answer to "how does the sweet spot actually get found."
- **Confidence**: anecdotal (prescriptive procedure, not validated against a named team's actual practice)
- **Quote**: "Take a request that arrives wicked-looking. Find the substeps inside it that are actually tame — the parts with a clear, checkable target once isolated. Do those with AI. Keep the residue: the part that still needs a person to decide something. That act of separating — this part can just be done, this part still needs a call — is itself a small piece of authorship, and it happens at the size of a single task, not once at the top of a strategy document. [...] It happens constantly, at every size of task, performed by whoever is closest to the work."
- **Our assessment**: This is the essay's most directly actionable claim for the guide — a four-step, repeatable procedure rather than an abstract principle, and it explicitly locates the decomposition skill at the individual-task level rather than as a one-time organizational strategy exercise. It directly corroborates `blog-addyosmani-human-judgment-relocates.md` Claim 15 ("human judgment is being relocated" rather than eliminated) and Claim 4 (a human can shape work early, steer mid-implementation, or stop shipping at multiple points, not just at a final review gate) — both sources argue human involvement is redistributed to specific decision points rather than removed wholesale, though Osmani's evidence is first-hand factory-operation anecdotes and Wood's is a single hypothetical example.

### Claim 11: Whatever doesn't decompose does not disappear — it rises to whoever holds the next layer of judgment, "which is exactly where it belongs"
- **Evidence**: Author's own closing claim to the decomposition procedure (Claim 10), asserting where irreducible judgment work should land.
- **Confidence**: anecdotal (normative claim about where residual judgment should route, not a description of any measured escalation practice)
- **Quote**: "And whatever doesn't decompose, no matter how far down the attempt is pushed, doesn't disappear. It rises to whoever is holding the next layer of judgment, which is exactly where it belongs."
- **Our assessment**: This closes the loop between Claim 5 (standing as the un-automatable residue) and Claim 10 (the task-level decomposition procedure) — undecomposable work is not a failure of the process, it is the process correctly routing judgment to whoever currently holds standing over it. The claim that this routing is "exactly where it belongs" is a value judgment, not a description of how escalation actually happens inside any named organization — the essay gives no mechanism (tooling, process, or governance structure) for how "rising to the next layer" would actually be implemented.

### Claim 12: As the tame frontier keeps advancing and turning more work into infrastructure, the sweet spot widens (creating more decomposition-driven acceleration), while the wicked frontier does not move simply because capability does — it instead comes into sharper focus as tame execution recedes into the background
- **Evidence**: Author's own closing synthesis, projecting the essay's three-zone taxonomy forward in time.
- **Confidence**: anecdotal (predictive/rhetorical closing claim, no trend data on zone boundaries shifting over time)
- **Quote**: "The tame frontier will keep advancing, turning more work into infrastructure. The sweet spot will widen with it, creating real acceleration for anyone willing to decompose the work. The wicked frontier will not move simply because capability does. It will come into sharper focus as the tame execution around it recedes into the background."
- **Our assessment**: This is the essay's forward-looking claim and its clearest statement that decomposition skill, not any specific tool or model generation, is the durable asset — "focusing on building those decomposition skills will be rewarded over and over, even as the capabilities of AI change" (essay's final line, not separately quoted above as its own claim since it restates this claim's conclusion). It is consistent with, but independently argued from, `blog-mattwood-half-life-assumption.md`'s general thesis that capability-dependent decisions decay fast while durable skills and judgment-routing structures should be built to last.

## Concrete Artifacts

### The three-zone taxonomy (author's own framework, reconstructed as a table from the prose)

```
Source: Matt Wood, "The Wicked Frontier," mattwood.blog, 2026-08-31
(https://mattwood.blog/essays/2026/08/the-wicked-frontier/)

Zone         | Character                          | What it wants
-------------|-------------------------------------|---------------------------
Tame         | Answer is checkable, no need to     | Automation
             | reopen the goal each time           |
Sweet spot   | Looks wicked, decomposes into tame  | Decomposition + tooling
             | substeps plus a judgment residue    |
Wicked       | No agreed stopping rule; answers    | People empowered to keep
             | are better/worse, not true/false    | making the calls
```

### The sweet-spot-finding procedure (verbatim, condensed from prose)

```
Source: same essay

"Take a request that arrives wicked-looking. Find the substeps inside it
that are actually tame -- the parts with a clear, checkable target once
isolated. Do those with AI. Keep the residue: the part that still needs a
person to decide something."

"It isn't a single decision made by a leader and rolled out. It happens
constantly, at every size of task, performed by whoever is closest to the
work."
```

### The market-entry decomposition example (verbatim)

```
Source: same essay

Wicked-looking request: "prepare a view on whether to enter a new market."

Decomposable substeps identified by the author:
- Pull the relevant market data.
- Model a few pricing scenarios.
- Summarize how three comparable companies handled a similar entry.
- Draft two or three framings of the decision so a leader can react to
  something concrete instead of a blank page.

"None of those steps require anyone to have already decided what the
company should do."
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

Source: https://mattwood.blog/about/ (re-fetched 2026-09-04; text unchanged
from the version quoted in all six prior mattwood.blog notes —
blog-mattwood-field-and-frontier.md, blog-mattwood-unit-of-return.md,
blog-mattwood-barcode-bargain.md, blog-mattwood-half-life-assumption.md,
blog-mattwood-for-your-information.md, and blog-mattwood-how-this-was-made.md)
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-kamelman-delegation-architecture.md`,
`blog-addyosmani-human-judgment-relocates.md`, `blog-thoughtworks-kamelman-unbundling-expertise.md`,
`blog-mattwood-field-and-frontier.md`, `blog-mattwood-unit-of-return.md`, and
`blog-mattwood-half-life-assumption.md` were re-read directly (MINER.md §4b)
and claim numbers below were confirmed against those notes' numbered
`### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 1 (the right
    analytic question is "bounded autonomy" — what an agent may decide, under
    what conditions, with what observability and accountability), Claim 2
    (guardrails prevent rule violations but cannot catch judgment failures),
    and Claim 4 (a core unresolved question is who owns the consequences when
    an agent acts correctly within its instructions and the organization
    still suffers harm): this essay's Claim 5 ("standing" — the right to
    decide and the responsibility to own what follows — as what AI capability
    cannot establish, and a gap that relocates rather than closes as models
    improve) is the same underlying limitation, named independently by a
    different author from a different angle (organizational-management-theory
    framing here vs. delegation-architecture framing there). Three
    independent voices converge on accountability/authority, not raw
    capability, as the durable constraint on agentic autonomy over judgment
    work.
  - `blog-addyosmani-human-judgment-relocates.md` Claim 15 ("human judgment is
    being relocated," not eliminated, as the share of human-typed code falls)
    and Claim 4 (a human participates at multiple points — shaping work
    early, steering mid-implementation, handoff, stop-shipping — not just a
    single final review gate): this essay's Claim 10 (the sweet-spot
    decomposition procedure happens "constantly, at every size of task,
    performed by whoever is closest to the work") and Claim 11 (undecomposable
    residue "rises to whoever is holding the next layer of judgment") describe
    the same redistribution-not-elimination pattern for human involvement,
    independently argued from software-factory operations (Osmani, first-hand
    anecdotes) versus organizational-adoption strategy (Wood, a single
    worked example).

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  existing corpus note argues that AI adoption should be pursued as a single
  uniform strategy regardless of task type, nor that AI capability alone
  (without an accountability/authority structure) is sufficient to resolve
  judgment-dependent decisions — so this essay's central claims do not
  conflict with prior source notes. No contradiction issue filed.

- **Extends**:
  - `blog-mattwood-half-life-assumption.md` (same author): that essay argues
    organizational decisions decay at different rates and that capability
    assumptions are now among the fastest-decaying — with a durable-vs-flexible
    taxonomy of what should stay stable (purpose, accountability, security
    boundaries) versus what can be held lightly (models, configs, workflow
    designs). This essay's Claim 12 (the wicked frontier "will not move
    simply because capability does," while the tame frontier keeps advancing)
    supplies a structural reason *why* that asymmetry exists: standing-dependent
    work (Claim 5) does not decay the way capability-dependent assumptions do,
    because its constraint is accountability, not what a model can currently
    do.
  - `blog-mattwood-field-and-frontier.md` (same author): that essay argues
    AI capability advances fastest where answers are cheap to check (the
    "tame frontier" concept in embryonic form, though not named as such
    there) and that most near-term enterprise value comes from field-first
    deployment of known capability. This essay names and formalizes that same
    "cheap to check" dynamic as the tame frontier (Claim 3) and adds the
    sweet-spot/wicked-frontier vocabulary the earlier essay does not have.
  - `guide/03-verification.md`'s Verification-as-Bottleneck Thesis: this
    essay's Claim 3 (AI compounds fastest where answers are cheap to check
    and the goal need not be reopened) supplies an explanatory frame, at the
    level of what makes a problem tractable for AI at all, for why the guide
    already treats verification cost as the binding constraint on safe
    autonomy — the guide's existing thesis is about workflow design; this
    essay's claim is about why that design choice tracks a deeper
    tame/wicked property of the underlying problem.

- **Novel**:
  - The tame/wicked/sweet-spot three-zone taxonomy itself (Claims 4, 6) and
    the explicit naming of "standing" (the right to decide plus the
    responsibility to own the outcome) as the specific thing AI capability
    cannot establish (Claim 5) — no existing corpus note uses Rittel and
    Webber's wicked-problems framework, or this specific standing-based
    account of AI's limits, in this form.
  - The repeatable, task-level sweet-spot-finding procedure (Claim 10) and
    the claim that undecomposable residue correctly "rises to whoever is
    holding the next layer of judgment" (Claim 11) — a new, concrete
    operational vocabulary for how decomposition-as-adoption-strategy would
    actually be practiced day to day, distinct from this corpus's existing
    factory/harness-design material, which addresses how work gets executed
    once judgment calls have already been made rather than how the judgment
    boundary itself gets located.
  - The claim that automating the tame and sweet-spot zones should *increase*
    the attention available for wicked-zone judgment rather than simply
    reduce headcount (Claim 9) — a specific, testable prediction about
    attention redistribution not previously made this way in the corpus.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 3 (AI compounds fastest on
  problems where an answer is cheap to check without reopening the goal) as
  an explanatory frame for the existing Verification-as-Bottleneck Thesis —
  the guide's argument that verification cost gates safe autonomy is a
  workflow-design instance of this essay's more general claim about what
  makes a problem tractable for AI at all. Add the tame/sweet-spot/wicked
  taxonomy (Concrete Artifacts) as vocabulary for classifying *which* tasks
  are candidates for the guide's autonomy-ramp material in the first place —
  the ramp only applies within the tame and sweet-spot zones; the wicked zone
  is explicitly out of scope for autonomous execution per Claim 5.

- **Chapter 05 (Team Adoption)**: Add the three-zone "adoptioneering" claim
  (Claim 9: automation for tame, decomposition+tooling for the sweet spot,
  empowerment for wicked) as a differentiated-strategy alternative to any
  implicit single-dial "roll out AI" framing. Add the sweet-spot-finding
  procedure (Claim 10) and the market-entry worked example (Claim 7,
  Concrete Artifacts) as a concrete technique teams can apply to their own
  wicked-looking requests, alongside the existing verification-ramp and
  license-allocation-by-verification-capacity material — decomposition
  capability is the skill that determines how much of a team's work can move
  into the ramp at all. Add Claim 5's "standing" framing as the reason a
  verification-capacity gate is necessary but not sufficient: even a fully
  verified tame substep does not confer standing over the wicked judgment
  it was extracted from.

- **Chapter 00 (Principles)**: Consider Claim 5 ("standing" — authority to
  decide plus accountability for the outcome — as what AI capability cannot
  establish, and a gap that relocates rather than closes) as a
  principles-level anchor for the guide's accountability material, now
  corroborated by three independent sources
  (`blog-thoughtworks-kamelman-delegation-architecture.md`,
  `blog-addyosmani-human-judgment-relocates.md`, and this essay).

## Extraction Notes

1. WebFetch's summarizer refused a "reproduce the whole essay verbatim"
   prompt on copyright grounds, and a follow-up structured-quote prompt
   returned quotes that could not be trusted as character-for-character
   without independent verification (consistent with the pattern already
   documented in `blog-mattwood-field-and-frontier.md`'s Extraction Notes).
   Per MINER.md §2a, this note does not rely on either WebFetch response for
   any quote. The full essay HTML was instead retrieved directly via `curl`
   (browser user-agent, HTTP 200) and parsed to plain text by stripping
   `<script>`/`<style>` tags and HTML markup. All quotes in this note were
   copied character-for-character from that locally-parsed text.
2. The article contains no outbound hyperlinks in its body (confirmed by
   inspecting the raw HTML's `<a>` tags — only navigation links to the site
   root). The site's homepage (`https://mattwood.blog/`) and About page
   (`https://mattwood.blog/about/`) were both fetched directly via `curl` —
   the homepage to confirm the essay's place in the author's publication
   list and the author's one-line self-description, the About page to
   confirm the fuller bio text used in Source Context and Concrete Artifacts
   is unchanged from prior mattwood.blog extractions. No further sub-pages
   were followed, per MINER.md §1's "up to 5 linked pages" guidance — there
   were none in the essay itself to follow.
3. The essay's one external citation (Rittel and Webber, 1973) is named by
   author and year only, with no link, journal name, or formal reference in
   the source text. This note independently identifies the likely reference
   (Rittel & Webber, "Dilemmas in a General Theory of Planning," *Policy
   Sciences*, 1973) as background context in Claim 2's confidence rating, but
   did not fetch or verify the original 1973 paper itself — the confidence
   split in Claim 2 (settled for the theory's existence as an academic
   framework, anecdotal for its application to AI) reflects that the
   underlying academic citation was not independently retrieved and checked
   against this essay's characterization of it.
4. No contradiction issues filed. This essay's central claims (AI advances
   unevenly across tame/wicked work; AI cannot establish standing regardless
   of capability; most real work is a decomposable mix rather than purely one
   type) were checked against the corpus's existing accountability,
   delegation, and judgment-relocation material; none argues the opposite —
   see Cross-References → Contradicts for the full reasoning.
5. `confidence_overall` is rated `anecdotal`, consistent with four of this
   author's six prior sibling notes (`blog-mattwood-barcode-bargain.md`,
   `blog-mattwood-half-life-assumption.md`, `blog-mattwood-unit-of-return.md`,
   and `blog-mattwood-how-this-was-made.md`). The other two are rated
   `emerging`: `blog-mattwood-field-and-frontier.md`, on the strength of a
   specific quantified cost-decline figure not present here, and
   `blog-mattwood-for-your-information.md`, whose claims were independently
   verified against the live site's API endpoints rather than resting on the
   author's assertion alone. Neither kind of support exists in this essay.
   Every claim in this essay beyond the borrowed Rittel-and-Webber definition
   is the author's own argument, illustrated with a single hypothetical,
   unnamed example (the market-entry decomposition) — there is no named
   company, survey, or measured figure anywhere in the source.
