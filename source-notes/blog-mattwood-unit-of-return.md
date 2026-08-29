---
source_url: https://mattwood.blog/essays/2026/08/the-unit-of-return/
source_type: blog-post
title: "The Unit of Return"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-08-27
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: anecdotal
issue: "#3029"
---

# The Unit of Return

> Matt Wood (AWS Chief AI & Technology Officer) uses an 1875 international
> telegraph-tariff dispute over what counts as a "word" as an analogy for why
> token counts are precise for billing but deceptive for ROI, then proposes a
> three-question framework — what useful result will the system produce, what
> evidence shows it's good enough, what does the full path to that result
> cost — for defining a "unit of return" that lets investment and value be
> expressed and compared in the same terms, across models and providers.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays"
  collection; short-form, single-author, no comments or citation
  infrastructure; ~900 words; no images, tables, or hyperlinks — the raw HTML
  contains no outbound `<a>` tags in the article body, only a single
  navigation link back to the site root).
- **Author credibility**: Matt Wood is AWS's Chief AI & Technology Officer,
  having returned to AWS in 2026 after nearly 15 years there earlier in his
  career and, most recently, leading commercial technology and innovation at
  PwC (per the site's About page, `https://mattwood.blog/about/`, fetched
  directly for this extraction). He holds a PhD in machine learning and did a
  postdoctoral fellowship in NLP/bioinformatics at Weill Cornell Medicine.
  This is the same author and site as `blog-mattwood-barcode-bargain.md`,
  `blog-mattwood-field-and-frontier.md`, `blog-mattwood-half-life-assumption.md`,
  and `blog-mattwood-how-this-was-made.md`; the bio and credibility assessment
  in those notes applies unchanged here (re-verified by re-fetching the About
  page for this extraction — the bio text is identical to the version quoted
  in those sibling notes, though the About page's third paragraph, on the
  author's newsletter "Counterintuitive" and book "Both, And," was not quoted
  in any prior note and is included below for completeness). As with those
  essays, this is a `trusted-feed` source that has already passed an
  author-worth-listening-to bar, but the piece itself is a historical-analogy
  and prescriptive-framework essay, not a data report: it names no company,
  cites no study, and gives no measured figure anywhere in its text — every
  claim is either an unsourced historical description or the author's own
  argument.
- **Scope**: Covers the 1875 St. Petersburg International Telegraph Convention
  and its word-counting rules, the historical gap this created between what a
  telegraph network charged for and what a recipient actually received, an
  analogy to AI token billing, a diagnosis of why token price is a poor proxy
  for business return, a three-question framework for defining a "unit of
  return" (useful result / evidence of sufficiency / full cost of the path),
  worked-through guidance for each of the three questions (baseline value,
  Goodhart's-law-style evidence gaming, evidence latency, the components of
  "full cost"), the role of an evaluator in enabling cross-provider
  comparison, and a closing note that token counting still matters
  operationally even after this reframing. Does NOT cover: any named AI
  product, customer, vendor, or company; any citation, study, or figure for
  any of its claims; a description of how to build or operate an evaluator;
  or a worked numerical example of a "unit of return" calculation for any
  real system.

## Extracted Claims

### Claim 1: The 1875 international telegraph tariff negotiations had to define what counted as a "word" for billing purposes, and the resulting rules (character limits per word, cipher-word equivalences) let businesses compress complete instructions into codebook words the network billed as one word but the recipient received as a paragraph — separating the message from the charge
- **Evidence**: Historical description, presented as established fact but with no citation, source, or named historian in the essay itself.
- **Confidence**: anecdotal (unsourced historical claim, consistent with how this author's other essays treat historical analogies — see `blog-mattwood-barcode-bargain.md` Claim 3, `blog-mattwood-how-this-was-made.md` Claim 10 — neither independently verified against a primary historical source by their respective extractions)
- **Quote**: "The delegates responded with limits: no more than fifteen letters to a word in Europe, ten outside it, five characters of cipher counted as one word. [...] Businesses compiled codebooks in which a single word could represent a complete commercial instruction. The network counted one word. The recipient received a paragraph. The message and the charge had begun to separate."
- **Our assessment**: This is the essay's framing device and title justification — a concrete historical case of a billing unit (the word) diverging from the unit of value actually delivered (the instruction). Like this author's other historical analogies (barcode scanning, the Franklin Junto), it is asserted without citation and should be treated as illustrative narrative, not a verified historical record, if used in the guide.

### Claim 2: Two models can consume the same number of tokens and produce answers of very different quality — one finishes the task immediately, another needs a retry, a check from another model, or a person to fix what it produced — so tokens are useful for billing (because running models has a real cost) but become misleading when carried into an ROI calculation as if they measured what the business receives
- **Evidence**: Author's own definitional argument, drawing the direct parallel to Claim 1's telegraph-word problem.
- **Confidence**: anecdotal (asserted claim, no measured example of two models consuming equal tokens for materially different-quality outputs)
- **Quote**: "A token may be a word, part of a word, punctuation, or a space, and two models can consume the same number of tokens and produce answers of very different quality. One finishes the task immediately. Another needs a second attempt, a check from another model, or a person to fix what it produced. Tokens are useful for billing because running models has a real cost. They become less useful when carried into an ROI calculation as though they measure the thing a business receives."
- **Our assessment**: This is the essay's central diagnostic claim and the direct AI-era restatement of Claim 1's telegraph pattern. It is plausible and consistent with the corpus's existing token-cost material (see Cross-References) but is asserted rather than measured within this essay — no specific model pair or task is named as an example.

### Claim 3: Most AI business cases pair an exact, countable cost (licenses, model calls, tokens) against a return described only in broad, unmeasurable terms (productivity, better decisions, improved experience, transformation) — and the comparison between a precise number and a vague ambition is structurally meaningless even when the vague terms describe something real
- **Evidence**: Author's own diagnostic claim about how AI business cases are typically constructed.
- **Confidence**: anecdotal (asserted pattern, no survey or named example of an actual AI business case exhibiting this structure)
- **Quote**: "Most AI business cases start with a cost that's easy to count: licenses, model calls, tokens. The return sits opposite it as productivity, better decisions, improved experience, transformation. Those may all be real. They're also too broad to sit across from a number that precise. The calculation puts an exact measure of consumption next to a vague ambition and expects the comparison to mean something."
- **Our assessment**: This names a specific structural flaw (precision mismatch between the two sides of an ROI comparison) rather than just asserting "ROI is hard to measure" generically — it is the essay's setup for the three-question framework that follows, which is designed to give the "return" side comparable precision to the "cost" side.

### Claim 4: As capable models get cheaper, ROI comparison gets harder rather than easier, because more models become viable for the same task and each one's full path varies in cost, speed, and retry frequency — a model with cheaper tokens can cost more overall once it requires three attempts and a person to finish the job, since token price describes every charge along the way without indicating which path produced the better result
- **Evidence**: Author's own extension of Claim 2's diagnosis to a multi-model comparison scenario.
- **Confidence**: anecdotal (asserted mechanism, no named comparison of specific models' token price vs. total-path cost)
- **Quote**: "As capable models get cheaper, the comparison gets harder. More models become viable for the same task, and the path through each one varies — in cost, in speed, in how often it needs a second pass. A model with cheaper tokens can cost more overall when it requires three attempts and a person to finish the job. Token prices describe every charge along the way without saying which path produced the better result."
- **Our assessment**: This directly complicates a "just switch to the cheaper model" instinct with a specific, checkable mechanism (retry/second-pass cost can outweigh a lower per-token price) rather than a vague caution against model switching — see Cross-References for how this interacts with the corpus's existing token-price-deflation-vs-spend-inflation material.

### Claim 5: A useful ROI calculation needs a single unit both the investment side and the return side can use — the investment becomes the full cost of producing that unit, the return becomes the value created each time it is delivered — and every AI proposal should be able to answer three questions: what useful result will the system produce, what evidence will show it's good enough, and what will the full path to that result cost
- **Evidence**: Author's own central prescriptive framework, presented as the essay's thesis and structured with the three questions as section headers in the remainder of the essay.
- **Confidence**: anecdotal (prescriptive framework, not validated against any named organization's actual ROI calculation)
- **Quote**: "A useful ROI calculation needs a unit both sides can use. The investment becomes the full cost of producing that unit. The return becomes the value created each time it's delivered. Every AI proposal should be able to answer three questions."
- **Our assessment**: This is the essay's single most reusable artifact for the guide — a compact, three-question checklist that reframes "is this AI project worth it" from a token-cost-vs-vague-benefit comparison into a same-unit cost-per-result vs. value-per-result comparison. It is presented and immediately illustrated (Claims 6-8 below work through each question), which makes it more concrete than a bare assertion, but it remains untested against a real organization's numbers within the essay itself.

### Claim 6 (Question 1 — the result): A useful result must be defined narrowly enough to be observable (e.g., a resolved customer request means the correct policy was applied, the requested action completed, and the customer did not have to return the next day — not simply "answering questions"), must connect to a specific value driver (capacity created, cost avoided, revenue gained, or risk reduced), and must be measured against a baseline, because automating a request the team already resolves quickly and cheaply creates less return than the completed result alone suggests
- **Evidence**: Author's own worked-through elaboration of the first framework question, using a customer-request-handling example throughout.
- **Confidence**: anecdotal (illustrative worked example, not a named case study)
- **Quote**: "'Answering questions' is too broad to measure. A resolved request has observable conditions: the correct policy was applied, the requested action was completed, and the customer did not have to return the next day. [...] That value needs a baseline. If the team already resolves the same request quickly and cheaply, automating it creates less return than the completed result alone suggests."
- **Our assessment**: The baseline requirement is the sharpest, most guide-actionable detail here — it is a specific caution against a common ROI-inflation error (crediting an AI system with the full value of a result it produces, even when a cheap existing process already produced that same result). This is a concrete, checkable criterion a team could apply to its own proposal, not just a restatement of "define your goal clearly."

### Claim 7 (Question 2 — the evidence): Evidence that a result is "good enough" must include the underlying thing actually being protected, not just a proxy metric standing in for it, because a system rewarded only for a narrow metric (e.g., avoiding repeat contact) can learn to satisfy that metric while failing the actual goal (e.g., ending conversations fast while leaving people confused) — and how fast and cheaply that evidence arrives (a payment matched to an invoice vs. a market-entry decision that plays out over years) determines how confidently the result can be counted at all
- **Evidence**: Author's own worked-through elaboration of the second framework question, using a support-system example for the gaming risk and payment-matching/market-entry examples for evidence latency.
- **Confidence**: anecdotal (illustrative examples, not a named case of a support system actually exhibiting the "ends conversations fast while leaving people confused" failure mode)
- **Quote**: "A support system rewarded only for avoiding repeat contact can learn to end conversations fast while leaving people confused — so the evidence has to include the thing you were actually trying to protect, not just the metric standing in for it. [...] A recommendation to enter a new market depends on competitive responses that may take years to play out. How fast and how cheaply the evidence arrives determines how confidently the result can be counted at all."
- **Our assessment**: This is a Goodhart's-law-shaped warning applied specifically to evaluation design for the "unit of return" framework — it argues the evidence criterion itself must be resistant to gaming, not just present. The evidence-latency point (some results are cheap and fast to verify, others take years) is a distinct and separately useful claim: it means the framework's confidence, not just its cost, varies by domain.

### Claim 8 (Question 3 — the full cost): The full cost of a result includes more than the model call — a system may also search, use other software, check its own work, retry, or hand off to a person — plus one-time building/integration/process-change costs before the first result arrives and ongoing maintenance costs afterward, so a complete calculation requires an expected volume over a defined period rather than a single per-call price
- **Evidence**: Author's own elaboration of the third framework question.
- **Confidence**: anecdotal (framework elaboration, no worked numerical example or named system's actual full-cost breakdown given)
- **Quote**: "The model call is one part of the answer. A system may also search, use other software, check its own work, retry or hand off to a person. Building, integration and process change create costs before the first result arrives; maintenance adds more over time. Some costs occur once and others on every request, so the full calculation needs an expected volume over a defined period."
- **Our assessment**: This is the framework's explicit rejection of "the cost is the token price" — it names four categories (per-request compute, one-time build/integration, ongoing maintenance, and volume-over-time) that a token-only cost model omits entirely. It corroborates the corpus's existing build/run/maintenance budgeting material (see Cross-References) with an independent articulation of the same structure, framed here as a definitional requirement of the unit-of-return calculation rather than a budgeting best practice.

### Claim 9: Answering all three questions lets both sides of an ROI calculation be expressed in the same unit — value per accepted result and full cost per accepted result — and this common unit is what allows comparison across models and providers, since any model that applies the right policy, completes the action, and satisfies the definition of resolution delivers the same unit of work as any other model that does the same thing, letting a business move between providers while continuing to get resolved requests; an evaluator is what makes this possible, checking the result and routing failed, unusual, or high-stakes work down a different path
- **Evidence**: Author's own synthesis, connecting the three-question framework (Claims 5-8) to a cross-provider comparison capability and naming the evaluator as the enabling mechanism.
- **Confidence**: anecdotal (prescriptive synthesis; no named organization or evaluator implementation described)
- **Quote**: "Answer all three, and the two sides of ROI can be expressed in the same unit: value per accepted result and full cost per accepted result. [...] The common unit also lets you compare across providers. A model that applies the right policy, completes the action, and satisfies the definition of resolution delivers the same unit of work as any other model that does the same thing. The business can move between them and keep getting resolved requests. The work and the machinery that produced it begin to separate. An evaluator makes that possible. It checks the result and routes failed, unusual or high-stakes work down a different path."
- **Our assessment**: This is the essay's payoff claim — the three questions aren't just a measurement discipline, they're what makes model/provider substitution possible without losing the ability to compare outcomes. The claim that "the work and the machinery that produced it begin to separate" directly echoes Claim 1's telegraph pattern (the message separating from the charge) and Claim 2's opening diagnosis, closing the essay's own analogy loop. The "evaluator" is named as the enabling mechanism but not described mechanically (no architecture, tooling, or implementation detail is given — it is asserted as a role, not specified as a system).

### Claim 10: Token counting remains genuinely useful for operational purposes even after adopting the unit-of-return framework — developers still need it to manage cost, monitor response times, and catch runaway loops, and providers may reasonably continue usage-based billing since different requests require different amounts of work; businesses can still compare providers by cost per accepted result rather than by raw token price
- **Evidence**: Author's own closing qualification, explicitly avoiding an "ignore tokens entirely" overstatement of the essay's own argument.
- **Confidence**: anecdotal (author's own qualifying claim, not independently tested)
- **Quote**: "Developers will still count tokens to manage cost, monitor response times and catch runaway loops. Providers may continue charging by usage because different requests require different amounts of work. Businesses can still compare providers by cost per accepted result."
- **Our assessment**: This is a useful, self-limiting clarification that keeps the essay's central claim narrow and defensible: the argument is not "tokens are meaningless," it is "tokens are the wrong unit for an ROI conversation specifically." This distinction matters for how the guide should cite this source — it should not be used to argue against token-level cost monitoring (which the corpus's `docs-ghaw-cost-management.md` and related notes document as operationally necessary), only against using token price as a stand-in for business value.

### Claim 11: A proposal that cannot yet answer the three questions may still deserve funding as an experiment, with the next investment specifically aimed at identifying the useful unit, the evidence that proves it, and the real cost of producing it — discovering whether an ROI case exists rather than assuming one does
- **Evidence**: Author's own closing prescriptive claim.
- **Confidence**: anecdotal (prescriptive claim, not tested against a named organization's staged-funding practice)
- **Quote**: "A proposal that can't yet answer the three questions may still deserve funding as an experiment. The next investment should identify the useful unit, the evidence that proves it and the real cost of producing it, discovering whether an ROI case exists."
- **Our assessment**: This positions the three-question framework as a staged-discovery tool rather than a pre-funding gate that would block all early-stage AI experimentation — an unfunded proposal isn't necessarily rejected, but its next round of investment should be explicitly aimed at answering the three questions rather than building further capability. This is a specific, actionable distinction (experiment-to-define-the-unit vs. experiment-to-build-the-feature) not elaborated further in the essay.

## Concrete Artifacts

### The three-question "unit of return" framework (verbatim, as structured by the article's own section headers)

```
Source: Matt Wood, "The Unit of Return," mattwood.blog, 2026-08-27
(https://mattwood.blog/essays/2026/08/the-unit-of-return/)

"Every AI proposal should be able to answer three questions."

1. What useful result will the system produce?
2. What evidence will show the result is good enough?
3. What will the full path to that result cost?

"Together, those three answers define the unit of return."
```

### The telegraph word-counting rules (as stated in prose; no citation or link in the original)

```
Source: Matt Wood, "The Unit of Return," mattwood.blog, 2026-08-27

- June 1875: delegates from twenty countries meet in St. Petersburg to settle
  the rules of international telegraphy
- Word-length limits set: no more than fifteen letters to a word in Europe,
  ten outside it
- Cipher equivalence: five characters of cipher counted as one word
- Businesses responded by compiling codebooks where a single billed "word"
  represented a complete commercial instruction
```

### The essay's closing synthesis (verbatim)

```
Source: Matt Wood, "The Unit of Return," mattwood.blog, 2026-08-27

"The delegates in St. Petersburg needed to know how many words crossed the
wire. The sender needed the instruction to be understood and acted upon.
Each measure answered a different question.

Leaders evaluating an AI proposal need the same separation. What useful
result will the system produce? What evidence will show it's good enough?
What will the full path to that result actually cost?

Together, those three answers define the unit of return."
```

### Author bio (from the site's About page, `https://mattwood.blog/about/`, fetched directly)

```
"I returned to AWS as Chief AI & Technology Officer in 2026, after almost 15
years here earlier in my career and most recently leading commercial
technology and innovation at PwC."

"My work is about helping turn AI from possibility into production. I work
with customers, builders, partners, and AWS teams to understand where the
technology is going, how customers can put it to work now, and what it takes
to build something durable on top of it rather than something that demos
well and fades."

"I think the next era will be shaped by inventors and builders who use AI to
reinvent products, services, and experiences, not just bolt it onto what they
already have. I write about that, and the counterintuitive parts most takes
miss, in my newsletter, Counterintuitive. My book, Both, And, is about
holding two true things at once, which turns out to be most of the job."

"Earlier: a PhD in machine learning, medical school at the University of
Nottingham, and a postdoctoral fellowship at Weill Cornell Medicine, where I
worked on natural language processing and bioinformatics back when that was
still a niche."

Source: https://mattwood.blog/about/ (fetched 2026-08-29; the "returned to
AWS," "Earlier," and closing lines are unchanged from the versions quoted in
blog-mattwood-barcode-bargain.md, blog-mattwood-field-and-frontier.md,
blog-mattwood-half-life-assumption.md, and blog-mattwood-how-this-was-made.md;
the "My work is about..." and "I think the next era..." paragraphs were not
previously quoted in any sibling note)
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-faros-claude-code-roi.md`,
`paper-miller-speed-cost-quality.md`, `blog-thoughtworks-kamelman-token-crisis.md`,
`blog-thoughtworks-vega-token-billing-lockin.md`, `docs-ghaw-cost-management.md`,
and `blog-mattwood-field-and-frontier.md` were re-read directly (MINER.md §4b)
and claim numbers below were confirmed against those notes' numbered
`### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 1 ("no one owns the
    aggregate" — token spend has expanded into a finance, engineering,
    delivery-governance, and strategic-liability problem simultaneously) and
    Claim 6 (the 98%-per-token-price-drop-vs-320%-enterprise-spend-increase
    paradox): this essay's Claim 4 (as models get cheaper, ROI comparison
    gets *harder*, because cheaper tokens don't guarantee a cheaper full
    path) independently arrives at the same underlying "falling price does
    not mean falling cost" paradox from the ROI-framework angle rather than
    the industry-spend-data angle — two different authors, two different
    kinds of evidence (Kamelman's named-company figures vs. Wood's
    definitional argument), same structural conclusion.
  - `paper-miller-speed-cost-quality.md` Claim 1 (Cursor adoption produces a
    281% velocity spike in month 1 that decays to zero by month 3) and Claim
    4 (velocity gains disappear entirely by month 3, with quality
    degradation as the likely mechanism): this essay's Claim 2 (two models
    can consume equal tokens but one "finishes the task immediately" while
    another "needs a second attempt, a check from another model, or a person
    to fix what it produced") is the same underlying phenomenon Miller et
    al. measure empirically — a system's *apparent* per-unit cost hides
    downstream rework cost that erodes the visible gain. Miller et al.
    supply the peer-reviewed measurement; this essay supplies the framework
    (define the "full path" cost explicitly, per Claim 8) that would have
    caught the gap Miller et al. document.
  - `blog-faros-claude-code-roi.md` Claim 4 (three measurement layers:
    usage/adoption, code trust/acceptance, team-level performance) and Claim
    5 (vanity metrics to avoid: lines of code, raw PR counts, autocomplete
    acceptance percentages): this essay's Claim 6 (a result must be defined
    narrowly enough to be observable, with a baseline, not just "answering
    questions") and Claim 7 (evidence must include the thing actually being
    protected, not a gameable proxy) make the same "don't measure the proxy,
    measure the outcome" argument from the ROI-definition angle that Faros
    makes from the measurement-methodology angle. Faros tells a team *how*
    to instrument a rollout once the unit is defined; this essay tells a
    team how to define the unit in the first place — the two are
    sequential, not overlapping, contributions.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  existing corpus note argues that token price is a sufficient or
  appropriate stand-in for business value in an ROI calculation, nor that
  full-path cost (retries, human review, integration) should be excluded
  from a cost comparison — so this essay's central claims do not conflict
  with prior source notes. No contradiction issue filed.

- **Extends**:
  - `blog-mattwood-field-and-frontier.md` (same author): that essay argues
    frontier AI budgets keep rising because ambition expands to fill each
    efficiency gain, while the price of any *fixed* capability level
    collapses by 9x-40x per year, and recommends "field-first" deployment
    (instrumenting known-capability workflows against local data) as where
    most near-term value lies. This essay supplies the missing measurement
    discipline for that recommendation: field-first deployment only
    demonstrates value if the deploying team can first answer this essay's
    three questions for the workflow being instrumented — otherwise "we
    deployed AI against a known-capability workflow" is exactly the kind of
    unmeasured claim this essay's Claim 3 warns against (a precise cost next
    to a vague, unmeasured "productivity" return).
  - `docs-ghaw-cost-management.md` Claim 1 (gh-aw workflow cost is the sum of
    Actions minutes and inference charges) and Claim 12 (common scenario
    cost estimates in Actions-minutes and premium-requests-per-month): this
    essay's Claim 8 (full cost includes search, tool use, self-checking,
    retries, and handoffs, not just the model call, plus one-time and
    ongoing components over an expected volume) is the framework-level
    argument for why a platform's per-run billing breakdown is necessary but
    not sufficient for an ROI calculation — gh-aw's cost reference documents
    *how to measure* the pieces of "full cost" for one specific platform;
    this essay explains *why* all those pieces (not just token/inference
    spend) belong in the denominator of a return-on-investment comparison.
  - `blog-thoughtworks-vega-token-billing-lockin.md` Claim 1 (the AI cost
    model has shifted from flat subscription to variable, consumption-based
    billing) and Claim 3 (enterprise token exposure scales through
    qualitatively different risk tiers): this essay's Claim 10 (token
    counting remains useful for managing cost, monitoring response time, and
    catching runaway loops, even after adopting the unit-of-return
    framework) is a narrower, complementary claim — it agrees token-level
    monitoring matters operationally while explicitly denying that token
    price alone answers the ROI question Vega's essay is otherwise concerned
    with (bill size and vendor lock-in, not value delivered per dollar).

- **Novel**:
  - The three-question "unit of return" framework itself (Claim 5, with
    Claims 6-9 as its worked elaboration) — a new, named, three-part checklist
    for defining a common measurement unit before comparing AI investment to
    AI return. No existing corpus source proposes this specific
    result/evidence/cost triad as a pre-ROI-calculation discipline.
  - The 1875 international telegraph tariff analogy (Claim 1) — a new
    historical framing device for the corpus, distinct from this author's
    other analogies already extracted (barcode scanning, the Franklin
    Junto, nautical charts) and distinct from any non-mattwood source in the
    corpus.
  - The explicit baseline requirement for defining a "result" (Claim 6:
    automating an already-cheap, already-fast process creates less return
    than the completed result alone suggests) — a specific, checkable
    anti-inflation criterion for ROI claims not previously named this way in
    the corpus's cost/ROI material.
  - The "the work and the machinery that produced it begin to separate"
    framing for cross-provider comparability (Claim 9) — a new, reusable
    articulation of *why* a common measurement unit enables model/provider
    substitution, going beyond the corpus's existing vendor-lock-in material
    (which addresses switching cost and dependency risk, not measurement
    comparability specifically).

## Guide Impact

- **Chapter 02 (Economics) / wherever the guide discusses AI cost-benefit
  analysis**: Add the three-question "unit of return" framework (Claim 5:
  what useful result, what evidence of sufficiency, what full-path cost) as
  a structured discipline for constructing an AI business case, positioned
  upstream of any specific measurement methodology already covered
  (`blog-faros-claude-code-roi.md`'s cohort design and vanity-metric list).
  Add Claim 3 (precise cost vs. vague return is a structurally meaningless
  comparison, even when the vague terms describe something real) as the
  explicit failure mode this framework is designed to fix — a sharper
  diagnostic than a generic "measure your ROI" recommendation.

- **Chapter 03 (Evaluation & Validation)**: Add Claim 7's evidence-gaming
  warning (a metric standing in for the actual goal can be satisfied while
  the goal itself fails, e.g. a support system optimizing for reduced repeat
  contact while leaving customers confused) as a Goodhart's-law-shaped
  caution specifically for evaluator design, alongside the corpus's existing
  anti-gaming-metric cases (Uber's "tokenmaxxing leaderboard," Duolingo's
  reversed AI-activity performance policy — both documented in
  `blog-thoughtworks-kamelman-token-crisis.md`). Add Claim 7's evidence
  latency point (some results verify in seconds — a payment matched to an
  invoice — others take years — a market-entry recommendation) as a
  criterion for how much confidence a team should place in an early ROI
  read, tied to how fast the chosen evidence actually arrives.

- **Chapter 04 (Cost of Validation in Loops) or wherever build/run/maintenance
  cost budgeting is discussed**: Add Claim 8's full-cost taxonomy (model
  call, search, other software, self-checking, retries, human handoff, plus
  one-time build/integration/process-change cost and ongoing maintenance,
  sized against an expected volume over a defined period) as the definitional
  argument for why a token-only or per-call cost model understates the true
  cost of an AI-driven result — this corroborates and gives a first-principles
  rationale for the corpus's existing build/run/maintenance budgeting material
  (`blog-thoughtworks-omahony-feature-token-budgets.md`, referenced via
  `blog-thoughtworks-kamelman-token-crisis.md` Claim 9's extension of it).

- **Chapter 05 (System Design) / model-and-provider selection guidance**: Add
  Claim 9 (a common unit of measurement — value per accepted result, full
  cost per accepted result — is what allows meaningful comparison and
  substitution across models and providers) as the measurement-layer
  precondition for any "compare providers by cost" recommendation already in
  the guide. Explicitly note Claim 9's own gap: the essay names "an
  evaluator" as the mechanism that makes this comparison possible but does
  not describe how to build or operate one — pair this claim with any
  existing corpus guidance on evaluator/harness design rather than treating
  it as self-sufficient.

## Extraction Notes

1. The full article was retrieved via a direct `curl` request with a browser
   user-agent (HTTP 200) and parsed to plain text by stripping `<script>` and
   `<style>` tags from the raw HTML, following the same method used in the
   sibling `blog-mattwood-*.md` notes. This is a from-scratch direct fetch,
   not a WebFetch summarization pass, so all quotes in this note are taken
   directly from the locally-parsed verbatim HTML.
2. The article contains no outbound hyperlinks in its body (confirmed by
   inspecting the raw HTML's `<a>` tags — only a single navigation link back
   to the site root). No sub-pages were followed beyond the About page, per
   MINER.md §1's "up to 5 linked pages" guidance — there were none in the
   essay itself to follow.
3. The site's About page (`https://mattwood.blog/about/`) was fetched
   directly via `curl` to confirm the bio text against the four prior
   mattwood.blog extractions; the previously-quoted passages are unchanged.
   This note additionally quotes two paragraphs (on the author's newsletter
   and book) not previously extracted in any sibling note, included here for
   completeness since they bear on author credibility (a named newsletter
   and a named book add two more independently checkable claims of
   expertise, though this Miner did not independently verify the newsletter
   or book's existence/content beyond the About page's own description).
4. This note found three of Prospector's overlap suggestions
   (`blog-mattwood-for-your-information.md`, `blog-mattwood-how-this-was-made.md`,
   `blog-mattwood-barcode-bargain.md`) to be same-author sibling essays on
   different topics (information-sharing norms, spreading adoption through
   process notes, and trust-in-adoption respectively) with no claim-level
   overlap with this essay's cost/ROI-measurement content, so they are not
   cited above as Cross-References beyond the shared-authorship note in
   Source Context — citing them as topical overlaps would be the kind of
   superficial "same author, so related" citation MINER.md's quality bar
   flags as insufficiently specific. `blog-mattwood-field-and-frontier.md`
   was the one same-author note found to have genuine claim-level overlap
   (AI cost dynamics and where value comes from) and is cited under Extends.
5. No contradiction issues filed. This essay's central claims (token price
   is a poor proxy for ROI; full cost includes more than the model call;
   ROI requires a common measurement unit) were checked against the corpus's
   existing token-cost and measurement-methodology notes; none argues the
   opposite — see Cross-References → Contradicts for the full reasoning.
6. `confidence_overall` is rated `anecdotal`, consistent with three of this
   author's four sibling notes (`blog-mattwood-barcode-bargain.md`,
   `blog-mattwood-half-life-assumption.md`, `blog-mattwood-how-this-was-made.md`;
   only `blog-mattwood-field-and-frontier.md` is rated `emerging`, on the
   strength of a specific quantified cost-decline figure not present in this
   essay). Every claim in this essay is either an unsourced historical
   narrative or the author's own prescriptive/definitional argument
   illustrated with hypothetical, unnamed examples — there is no named
   company, study, survey, or measured figure anywhere in the source.
