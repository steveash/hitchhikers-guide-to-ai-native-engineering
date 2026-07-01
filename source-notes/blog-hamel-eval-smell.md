---
source_url: https://hamel.dev/blog/posts/eval-smell/
source_type: blog-post
title: "\"It's Hard to Eval\" Is a Product Smell"
author: Hamel Husain
date_published: 2026-06-29
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: emerging
issue: "#1384"
---

# "It's Hard to Eval" Is a Product Smell

> Hamel Husain argues that when practitioners say a product is "hard to eval,"
> the real problem is a design smell: if an AI artifact is hard for the builder
> to verify, it is usually hard for the end user to verify too — so products
> should be designed for ease of verification *before* evals are built, not after.

## Source Context

- **Type**: blog-post (personal blog, hamel.dev, June 29, 2026)
- **Author credibility**: Hamel Husain has spent "the past 3 years" with AI
  evals as his "professional focus." He co-teaches an "AI Evals for Engineers &
  PMs" course, co-authored the O'Reilly book "Evals for AI Engineers," and has
  previously published "Your AI Product Needs Evals" and "A Field Guide to
  Rapidly Improving AI Products" (referenced in the article's own footnote).
  He writes as an advisor who worked directly with the three companies described
  — not as a detached commentator. No controlled experiments or quantitative
  outcomes are reported; the evidence is advisory case experience across three
  named-but-anonymized engagements.
- **Scope**: Covers three product redesigns Husain advised on (an internal AI
  data agent for business questions, a K-12 PE lesson-plan generator, and a
  workers'-compensation medical-report tool), then generalizes to a four-question
  design framework and situates the whole argument as an application of
  pre-existing product/UX design principles to AI products. Does NOT cover eval
  harness mechanics, metrics, annotation tooling, or model selection — it is
  explicitly upstream of eval-building, not a treatment of eval design itself.

## Extracted Claims

### Claim 1: "Hard to eval" is a product design smell, not an inherent property of the task — because outputs hard for the builder to verify are usually hard for users to verify too
- **Evidence**: Stated as the article's opening thesis, generalized from the objection Husain says he hears most often from teams building AI products.
- **Confidence**: emerging (practitioner generalization from advisory experience across many engagements, not a single case; no counter-examples or boundary conditions discussed)
- **Quote**: "This objection is a product smell. Artifacts that are hard for you to verify are often hard for users too. In the worst case, users have to redo the work from scratch to verify the output. More importantly, designing your product for ease of verification should come before building evals."
- **Our assessment**: This is the load-bearing reframe of the whole post: "hard to eval" is treated as a signal to inspect the product's information architecture rather than a property to route around with more sophisticated eval tooling. The ordering claim ("verification design should come before building evals") is the most actionable part — it argues for a design-first sequence rather than eval-tooling-first.

### Claim 2: Making the AI's final answer the only visible output is a common design mistake, because it leaves nothing for the user (or evaluator) to check
- **Evidence**: First case study — an internal AI data agent that answers business questions (e.g., "what was net revenue for Product A last quarter") by finding data sources, running queries, and returning an answer.
- **Confidence**: emerging (single case, but consistent with the general information-hiding failure mode described across all three case studies)
- **Quote**: "A common mistake when building AI data agents is to make the answer the only output" ... "Since the only output is the answer, there is nothing here to check."
- **Our assessment**: This names the specific architectural failure — collapsing a multi-step reasoning process down to a single scalar/text answer — as the root cause of "hard to eval." It's a concrete, checkable anti-pattern rather than a vague complaint about AI opacity.

### Claim 3: Domain experts already have concrete, nameable techniques for verifying answers manually — and a product should expose the artifacts those techniques need
- **Evidence**: Husain lists five specific verification techniques he uses personally to check a data-agent's answer: comparing against a trusted source, confirming the metric definition, sanity-checking a related quantity, inspecting the distribution beneath an aggregate, and reading the underlying query.
- **Confidence**: emerging (first-person practitioner technique list; presented as Husain's own verification workflow, not surveyed across multiple experts)
- **Quote**: "Compare the quantity and any intermediate calculations against a trusted source, like a vetted dashboard or report, or a similar analysis a colleague has already vetted." ... "Read the query. For an important number I look at the SQL to confirm it does what I think, and I tweak it and rerun to test my assumptions."
- **Our assessment**: This is the concrete bridge between "verification" as an abstract goal and "verification" as a specific set of user actions a product must support. It reframes the design question from "how do we show our work?" to "which of these five specific check types does our UI need to make possible?"

### Claim 4: The redesigned data agent should retrieve from vetted prior analyses and disclose provenance (source, author) rather than compute from scratch and hide its process
- **Evidence**: The "after" design for the data agent: the agent optionally retrieves from vetted analyses and the interface shows which one was used and who authored it.
- **Confidence**: emerging (single design sketch from an advisory engagement; not a shipped/measured product)
- **Quote**: "The agent optionally performs retrieval from vetted analyses, and the interface shows which one was used along with who authored it."
- **Our assessment**: This ties provenance directly to trust transfer — the agent borrows credibility from a human-vetted analysis and makes that borrowing visible, rather than asking the user to trust a fresh computation with no history.

### Claim 5: Progressive disclosure — a short answer with high-value details visible by default and full context available on demand — resolves the tension between concise answers and verifiability
- **Evidence**: The redesigned data agent's chat reply, described as showing high-value items (sources, assumptions, issues) by default, with an optional interactive notebook exposing full context.
- **Confidence**: emerging (design pattern from a single advisory case; no user-testing data on whether the disclosure levels are the right ones)
- **Quote**: "There is progressive disclosure of details. The chat reply shows high value items like sources, assumptions, and issues. The user can optionally open an interactive notebook to see the full context."
- **Our assessment**: This is a specific, implementable UI pattern (chat-first, notebook-on-demand) rather than a general appeal to "transparency." It's directly reusable as a design template for other agent products that summarize computed results.

### Claim 6: Anchoring AI-generated work to something a user already trusts, and showing only the diff, converts "judge the whole artifact" into "judge a small set of changes"
- **Evidence**: Second case study — a PE lesson-plan generator for K-12 teachers. Redesign anchors new plans to a vetted plan already used by a similar teacher and surfaces only the diff.
- **Confidence**: emerging (single advisory engagement; founder-facing product, not confirmed at scale)
- **Quote**: "When the tool generates a plan, it shows which vetted plan it started from, who uses that plan, and a diff of what it changed for this teacher's constraints." ... "Next, the teacher can check a small set of changes against a plan they already trust, instead of judging a whole plan from scratch."
- **Our assessment**: This generalizes Claim 4's "anchor to something trusted" pattern into an explicit review-unit-size reduction technique: the verification burden scales with the diff size, not the artifact size. This is the same principle code review relies on (small diffs are more reviewable than whole-file rewrites), applied to AI-generated content review.

### Claim 7: Social proof — "a teacher like them already uses this plan" — is the fastest trust-building signal available, faster than the user re-verifying the content themselves
- **Evidence**: Stated directly in the PE curriculum-builder case study as the rationale for anchoring to existing vetted plans.
- **Confidence**: anecdotal (single stated design rationale, not tested against alternative trust signals)
- **Quote**: "The fastest way to trust a plan is to see that a teacher like them already uses it."
- **Our assessment**: This is a distinct trust mechanism from provenance-as-traceability (Claim 4) — it's provenance-as-social-proof. Both reduce verification burden, but through different mechanisms (traceable evidence vs. peer validation), and a product may need both depending on whether the user's remaining doubt is about correctness or about applicability.

### Claim 8: For research-heavy, high-stakes documents, redesigning the product as a "research assistant" that surfaces facts, sources, and contradictions — rather than a "report generator" that outputs a finished document — makes incremental verification possible during the work instead of exhaustive verification after
- **Evidence**: Third case study — a workers'-compensation medical-report tool. Original design required the doctor to re-read the entire chart and check every claim in the generated report, "which can take as long as writing the report from scratch." Redesign: extract facts with source links, surface contradictions between exams, let the doctor resolve gaps, then assemble the final report from what's already been checked.
- **Confidence**: emerging (single advisory case in a regulated, high-stakes domain; no outcome data on doctor time saved)
- **Quote**: "To trust it, the doctor has to re-read the whole chart and check every claim, which can take as long as writing the report from scratch." ... "I advised the founder to make the product work like a research assistant instead of a report generator." ... "For example, the product could read every record and pull out relevant facts, with a link back to the page so the doctor can check each one." ... "Where two exams disagree, or the chart leaves a question open, the product should surface that." ... "The doctor can then resolve any contradictions and fill in the gaps." ... "Finally, the product can assemble the final report from what they have already checked."
- **Our assessment**: This is the strongest of the three case studies for showing *why* verification-first design matters economically: without redesign, verifying the AI's report costs as much effort as not using the AI at all, which erases the product's value proposition. The redesign moves verification earlier and distributes it across smaller units (per-fact links, flagged contradictions) so the final assembly step requires no additional trust — everything in it was already checked.

### Claim 9: Designing for verification requires asking what the user needs to check, what trusted reference they can check it against, what heuristics domain experts already use, and what smaller units of work they can accept/edit/reject
- **Evidence**: The "Generalizing the pattern" section distills the three case studies into a four-question design framework, explicitly framed as applicable beyond the three examples given.
- **Confidence**: emerging (framework synthesized from three cases; not validated against a broader sample of products)
- **Quote**: "What does the user actually need to check?" ... "What trusted thing can they compare it against?" ... "Are there signals or heuristics that experts use to aid in verification?" ... "What smaller units can they accept, edit, or reject?"
- **Our assessment**: This is the most directly reusable artifact in the post — a checklist a team can apply during product design, independent of domain. Each question maps onto one of the three case studies (verification target ↔ data agent's "nothing to check" problem; trusted comparison ↔ vetted plan/analysis anchoring; expert heuristics ↔ the five data-verification techniques in Claim 3; smaller acceptable units ↔ the diff-based lesson-plan review and per-fact medical report review).

### Claim 10: Provenance — showing where information originated, with links for deeper inspection — is the common thread across all three redesigns
- **Evidence**: Explicitly named as the connecting pattern across the data agent (source/author of retrieved analysis), the curriculum builder (source plan and diff), and the medical report tool (link back to the source page for each extracted fact).
- **Confidence**: emerging (pattern synthesis across three cases by the author; not independently tested)
- **Quote**: "A common thread across these examples is provenance."
- **Our assessment**: Provenance-as-connective-thread is consistent with the pattern Anthropic's Kepler case study describes (see Cross-References) but Husain's framing is narrower and more UI-specific: provenance here means a visible, clickable link from an AI-asserted fact back to its origin, not an architectural guarantee that outputs are computed deterministically.

### Claim 11: What a user needs to verify changes as their trust in the product grows — verification requirements are not static
- **Evidence**: Stated in the "Generalizing the pattern" section as a qualifier on the four-question framework.
- **Confidence**: anecdotal (single stated observation, not elaborated with a concrete example of how verification needs shift over time)
- **Quote**: "What needs verifying also changes as the user's trust grows."
- **Our assessment**: This is a thin but important caveat: a verification-first design that never adapts risks over-verifying for experienced users (adding friction after trust is established) or under-verifying for new users (before trust is established). The post does not elaborate on how to detect or design for this trust curve, which is a gap — the guide should flag this as an open design question rather than a solved pattern.

### Claim 12: These verification-design principles are not new — they are standard product design principles, applied to AI because verification is now the bottleneck
- **Evidence**: The closing section, "None of this is new," explicitly frames the whole post as a restatement of established design principles rather than a novel discovery, with the AI framing added because verification is newly the constraint.
- **Confidence**: settled (as an observation about pre-AI design principles, e.g., progressive disclosure, diffs, provenance links, are all well-established UX/software patterns; presented as such by the author, not as an emerging or contested claim)
- **Quote**: "Evals thinking is aligned with good product design." ... "All of these ideas stem from well-established design principles." ... "Even though these ideas are well established, a reminder is due in the age of AI." ... "With AI, verification is the bottleneck."
- **Our assessment**: This framing matters for how the guide should present the claim: not as a novel AI-specific technique, but as an argument that the bottleneck AI products face is disproportionately a verification bottleneck, which makes long-standing UX principles (progressive disclosure, diffing, provenance links, small reviewable units) newly load-bearing rather than nice-to-have.

## Concrete Artifacts

```
Four-question verification design framework
Source: "Generalizing the pattern" section, hamel.dev/blog/posts/eval-smell/

1. What does the user actually need to check?
2. What trusted thing can they compare it against?
3. Are there signals or heuristics that experts use to aid in verification?
4. What smaller units can they accept, edit, or reject?
```

```
Five manual verification techniques (data-agent case study, first-person)
Source: hamel.dev/blog/posts/eval-smell/, "Example 1: the AI data agent"

1. Compare against a trusted source (vetted dashboard/report, or a
   colleague-vetted analysis).
2. Confirm the metric definition precisely (e.g., does "net revenue"
   include or exclude returns/discounts).
3. Sanity-check a related quantity that should move with the target
   number (e.g., units sold, unique customers).
4. Look at what's beneath the aggregate — break a total down by
   dimension (region, time period) and sanity-check the distribution.
5. Read the underlying query (SQL) for an important number, and tweak/
   rerun it to test assumptions.
```

```
Three case-study redesigns (before -> after), condensed
Source: hamel.dev/blog/posts/eval-smell/

1. AI data agent
   Before: answer only, "nothing here to check"
   After:  retrieval from vetted analyses + visible source/author +
           progressive disclosure (chat summary -> notebook detail)

2. PE curriculum builder
   Before: lesson plan generated from scratch, judged as a whole
   After:  plan anchored to a vetted plan already used by a similar
           teacher, with a diff of what changed for this teacher

3. Workers'-comp medical report tool
   Before: full report generated, doctor must re-read entire chart to
           verify (as much work as writing it from scratch)
   After:  "research assistant" mode — extract facts with source links,
           surface contradictions between exams, doctor resolves gaps,
           report assembled last from already-checked facts
```

## Cross-References

- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9
  ("Provenance must be designed in from day one — full traceability to source
  SEC filings, page numbers, and line items is an architectural constraint, not
  a compliance feature added after the fact"): both sources converge on
  provenance-first design, though at different altitudes. Kepler's claim is
  architectural (a deterministic execution layer that makes model output
  structurally incapable of becoming the final auditable number); Husain's
  claim is UI/product-design-level (visible source links and diffs). The two
  are complementary: Kepler shows how to guarantee provenance is *true*
  end-to-end; Husain shows how to make that provenance *visible and checkable*
  to the end user in the interface. Neither source alone covers both layers.
- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 11
  ("Discovery with 147 financial firms before founding revealed that
  auditability is the irreducible trust requirement — not accuracy"): Husain's
  workers'-comp case study makes the same point from the opposite direction —
  a report the doctor cannot cheaply audit is not trustworthy regardless of its
  accuracy, because verifying it costs as much as not using the AI at all.
- **Extends** `blog-langchain-better-harness-evals.md`: that source treats evals
  as the object to optimize (holdout sets, eval-as-regression-test, six-step
  hill-climbing recipe) and is entirely internal-facing — it assumes the team
  already has a way to check outputs. Husain's post is explicitly upstream of
  that entire discipline: his claim is that if the team is struggling to build
  the evals blog-langchain-better-harness-evals.md describes, the fix may be to
  redesign the *product* (expose provenance, shrink review units, add
  progressive disclosure) rather than to invest further in eval tooling. This
  source should be read as a precondition-setting companion to the eval-harness
  note, not a competing one.
- **Contradicts**: None found. No existing source note stakes out a position
  that hard-to-eval products should be evaluated harder rather than redesigned,
  so there is no direct conflict to file.
- **Novel**:
  - **"Hard to eval" reframed as a product design smell** (Claim 1) — no
    existing corpus note treats eval difficulty as a diagnostic signal about
    product architecture rather than a property of the task or a gap in eval
    tooling sophistication.
  - **The four-question verification-design framework** (Claim 9) — a
    reusable, domain-agnostic design checklist not present elsewhere in the
    corpus. Existing verification-related notes (Kepler, Carta) describe
    specific architectures; none provide a generalizable question set for
    designing verification into a product from scratch.
  - **Review-unit-size reduction via anchoring + diffing** (Claims 6-7) — the
    specific mechanism of anchoring AI output to something already trusted and
    showing only the diff, as a way to shrink the verification unit from
    "whole artifact" to "small change set," is new to the corpus. It is
    conceptually related to code review practice but not previously connected
    to AI product design in any existing note.

## Guide Impact

- **Chapter 03 (Verification)**: Add "hard to eval is a product smell" (Claim 1)
  as a named diagnostic heuristic: when a team reports that a task is hard to
  evaluate, the guide should recommend first asking whether the product exposes
  enough intermediate structure to check, before investing further in eval
  tooling or human annotation capacity. Pair with the four-question framework
  (Claim 9) as the concrete design exercise to run.
- **Chapter 03 (Verification)**: Add progressive disclosure (Claim 5) and
  anchor-and-diff (Claims 6-7) as two named, reusable UI patterns for making AI
  output verifiable, with the data-agent and curriculum-builder case studies as
  worked examples. Position alongside the Kepler note's deterministic-layer
  pattern as the UI-level counterpart to Kepler's architecture-level provenance
  guarantee — the guide should note that visible provenance (this source) and
  guaranteed provenance (Kepler) are both needed and address different failure
  modes (users doubting a true answer vs. an architecturally unverifiable one).
- **Chapter 02 (Harness/Product Design)**: Add the "research assistant, not
  report generator" reframe (Claim 8) as a named pattern for high-stakes
  document-generation products: decompose the task into fact-extraction with
  provenance links, contradiction surfacing, and human gap-resolution, before a
  final assembly step — rather than generating the finished artifact first and
  asking the human to audit it after the fact whole-cloth.
- **Chapter 03 (Verification)**: Flag Claim 11 (verification needs shift as
  user trust grows) as an open design question the corpus does not yet resolve
  — worth watching for a future source that addresses how to detect or design
  for the trust curve explicitly.

## Extraction Notes

- The article was fetched via multiple targeted WebFetch passes (title/opening,
  each of the three case-study sections, the "Generalizing the pattern" and
  "None of this is new" sections, and the four design questions specifically)
  because the tool's default behavior returns a paraphrased summary rather than
  verbatim text. Quotes in this note were assembled from passes that explicitly
  requested word-for-word reproduction, and repeated across passes for
  consistency where the same passage was requested more than once.
- The article has one footnote (marked `[1]`) on the opening sentence,
  referencing Husain's prior work ("Your AI Product Needs Evals," "A Field
  Guide to Rapidly Improving AI Products," the "AI Evals for Engineers & PMs"
  course, and the "Evals for AI Engineers" O'Reilly book). This is background
  on the author's credibility, not a separate claim, and is folded into Source
  Context above rather than extracted as its own claim.
- No sub-pages were linked from the article that warranted following — it is a
  single self-contained post.
- All three case studies are advisory engagements Husain does not name (company
  names are not given for any of the three), so confidence is capped at
  "emerging" throughout: the mechanisms described are plausible and consistent
  with established design principles, but none are independently verified,
  outcome-measured, or attributable to a checkable production system (contrast
  with the Kepler note, which names the company and reports production scale
  metrics).
- Three convergent Prospector triage comments were filed on the issue, all
  identifying the same core pattern (provenance, verifiability-by-design,
  Ch02/Ch03 relevance) and overlapping candidate notes (Kepler, LangChain
  better-harness). This extraction confirms and extends both cross-references
  suggested in triage.
