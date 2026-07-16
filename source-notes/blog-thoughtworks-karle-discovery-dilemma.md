---
source_url: https://www.thoughtworks.com/insights/blog/product-innovation/Using-AI-to-focus-research-in-product-discovery
source_type: blog-post
title: "The discovery dilemma: Using AI to focus research where it matters"
author: Aditya Karle
date_published: 2026-07-03
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: anecdotal
issue: "#1923"
---

# The Discovery Dilemma: Using AI to Focus Research Where It Matters

> Thoughtworks case study of a single greenfield loyalty-proposition project
> for an unnamed global travel retailer, in which the author used Claude as a
> "thinking partner" to pressure-test twenty workshop-generated concepts
> against traveler behavioral archetypes — narrowing to concrete scenarios
> before spending a fixed 8-user research budget — and reports that the
> tensions Claude surfaced (privacy concerns, narrow-appeal concepts, an
> airport-security-driven shift in traveler interface preference) reappeared
> unprompted in the subsequent real user sessions.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Product innovation" vertical,
  published July 3, 2026; auto-discovered via the trusted feed
  `thoughtworks`). First-person practitioner narrative structured around
  eight named sections: "The discovery dilemma" (unheaded intro), "Starting
  with uncertainty", "Using AI as a thinking partner", "From concepts to
  scenarios", "Validating with users", "What actually changed", "Where this
  works and where it doesn't", "The real opportunity".
- **Author credibility**: Aditya Karle. No bio, title, or credentials are
  given anywhere in the article body (no byline pull-quote of the kind seen
  in Kamelman's Thoughtworks pieces in this corpus). The entire evidentiary
  basis is the author's own first-person account of a project he says he
  personally led ("I led discovery for a greenfield loyalty proposition with
  a global travel retailer"). Neither the client, the specific loyalty
  product, nor any teammates are named — this is a single, unverifiable
  practitioner anecdote, not a client-attributed or third-party-audited case
  study.
- **Scope**: Covers one project's discovery-phase methodology end to end
  (workshop concept generation → CVP/BVP prioritization → AI-assisted
  archetype/scenario pressure-testing → 8-user prototype validation) and the
  author's generalized claims about where AI helps and doesn't help in
  product discovery. Does NOT cover: any quantitative outcome metric (no
  conversion, retention, or revenue figures — the only concrete numbers in
  the piece are "twenty concepts," "five" shortlisted, "five" archetypes,
  and "eight users"), the actual prompts or Claude conversation transcripts
  used, how CVP/BVP scoring was weighted, or what happened to the loyalty
  proposition after the 8-user round (no ship/launch outcome is reported).

## Extracted Claims

### Claim 1: Research budget is one of the first things cut when delivery timelines tighten, which shifts team focus from exploring opportunities to picking what to build next
- **Evidence**: Author's opening framing, presented as the general problem the rest of the article addresses.
- **Confidence**: anecdotal (a general industry observation asserted without data, functioning as the article's motivating premise)
- **Quote**: "Research is one of the most valuable parts of product discovery, and one of the first to be compressed when timelines tighten."
- **Our assessment**: A plausible, commonly-cited pressure in product organizations, but unsupported by any cited data here — it is scene-setting rhetoric rather than a claim the article defends. Its value is as framing for the more concrete methodology that follows, not as an independent finding.

### Claim 2: When research gets compressed, the operative question shifts from "which opportunities should we explore?" to "which of these can we start building?"
- **Evidence**: Author's own characterization of the typical failure mode this article's methodology is meant to counter.
- **Confidence**: anecdotal (rhetorical framing, not measured)
- **Quote**: "Before long, the conversation shifts from 'Which opportunities should we explore?' to 'Which of these can we start building?'"
- **Our assessment**: This is the article's diagnostic hook — a two-question contrast used to motivate the discovery-dilemma framing. It has no independent evidentiary weight but is a clean, quotable statement of the problem the rest of the piece claims to solve.

### Claim 3: In a real project (a greenfield loyalty proposition for a global travel retailer), a handful of focused workshops produced around twenty concepts spanning shopping, utility, personalization, airport navigation, local discovery, and travel assistance
- **Evidence**: Author's first-person account of a specific, named-context (unnamed client) project he says he led.
- **Confidence**: anecdotal (single-project, single-narrator account; no client name, no corroborating source)
- **Quote**: "Through a handful of focused workshops, the team generated around twenty concepts spanning shopping, utility, personalization, airport navigation, local discovery and travel assistance."
- **Our assessment**: This is the concrete case study the rest of the article's claims are anchored to. Twenty concepts across six categories is a specific, checkable-in-principle number, but nothing beyond the author's own account corroborates it. Treat the entire case study as a single illustrative anecdote, not a validated methodology.

### Claim 4: Claude was integrated as a "thinking partner" to explore assumptions and model traveler behaviors, after the twenty concepts were narrowed to five using Consumer Value Proposition (CVP) and Business Value Proposition (BVP) prioritization lenses
- **Evidence**: Direct practitioner account of the workflow step and the named prioritization framework used before AI was introduced.
- **Confidence**: anecdotal (single-project workflow description)
- **Quote**: "I integrated Claude as a thinking partner to explore assumptions and model behaviors." / "After prioritizing via CVP (consumer value proposition) and BVP (business value proposition) lenses, we shortlisted five concepts."
- **Our assessment**: This establishes the specific sequencing that matters for guide purposes: AI is not used to generate or prioritize the initial twenty concepts — that step used a conventional two-axis (consumer value / business value) framework first. AI enters only after human prioritization has already cut the field from 20 to 5, to pressure-test the survivors rather than to do the initial triage. This sequencing detail is more specific than the Prospector's triage summary, which described AI as inserted into "the assumption-validation phase" generally without naming where in the funnel it entered.

### Claim 5: The team built five traveler behavioral archetypes (frequent business travelers, leisure explorers, last-minute buyers, pre-planners, Gen Z digital-first travelers) and used Claude to model how each archetype would respond to the five shortlisted concepts
- **Evidence**: Author's account of the archetype-construction step, immediately following Claim 4.
- **Confidence**: anecdotal (single-project methodology)
- **Quote**: "frequent business travelers, leisure explorers, last-minute buyers, pre-planners and Gen Z digital-first travelers."
- **Our assessment**: Naming five archetypes explicitly gives the guide a concrete, reusable pattern (behavioral archetype construction as an intermediate artifact between "concept" and "user scenario"), distinct from generic "build a persona" advice — these archetypes are built specifically to be argued against by the AI, not just described.

### Claim 6: Providing Claude with context it could not infer on its own — specifically, airport psychology and traveler-journey moments — was what made the archetype modeling valuable, not the modeling itself
- **Evidence**: Author's own explanation of what made the technique work, given in the "What actually changed" section.
- **Confidence**: anecdotal (author's own causal attribution, not independently tested against a version of the exercise that omitted this context)
- **Quote**: "The real value came from providing context Claude couldn't infer on its own: airport psychology."
- **Our assessment**: This is the article's clearest mechanistic claim, and it converges with `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 3 (success with AI correlates with the ability to externalize a coherent mental model, not with domain knowledge itself) and Claim 6 (expertise isn't the multiplier for AI-assisted work — transmissibility is). Both articles independently argue that the human's job is to supply the specific, non-inferable context/mental model; the AI's value is downstream of that input, not a substitute for it. Karle's version is a concrete instance (airport psychology as the input) of Kamelman's abstract claim (externalized context as the multiplier).

### Claim 7: Under time pressure before airport security, business travelers preferred a conversational interface that helped them decide quickly; once through security, they shifted into exploration mode and preferred a browsable interface
- **Evidence**: A specific output the AI-assisted archetype modeling produced, presented as a discovery surfaced during the exercise.
- **Confidence**: anecdotal (single-project AI-generated hypothesis; per Claim 10 below, this specific tension is reported as having later reappeared in real user sessions, which is the article's only corroborating evidence for it)
- **Quote**: "Under time pressure, business travelers preferred a conversational interface that helped them reach a decision quickly. Once through security, however, they shifted into exploration mode and preferred a browsable experience."
- **Our assessment**: This is the article's single most concrete example of an AI-surfaced insight, and it is a genuinely specific, falsifiable-sounding behavioral claim (interface preference flips at a named physical/temporal transition point — airport security). Its credibility rests entirely on the self-reported later confirmation in Claim 10; there is no independent measurement of business traveler behavior cited.

### Claim 8: The team replaced abstract concept validation ("Would you use this?") with concrete scenario-based questioning ("What would you do here?"), turning each concept into a journey scenario tied to a specific traveler, moment, and decision
- **Evidence**: Author's description of the methodological shift in the "From concepts to scenarios" section.
- **Confidence**: anecdotal (methodology description, no comparison data between the two question framings)
- **Quote**: "Instead of asking 'Would you use this?' and started asking 'What would you do here?'"
- **Our assessment**: This is a reusable prompting/research-design pattern independent of whether AI is involved — converting abstract preference questions into concrete situated-decision questions. It is presented as an effect of using AI to generate scenarios (the archetype/scenario work made concrete situations available to test), but the underlying research-design principle (situated over abstract questions) is a general one the article doesn't claim to have invented.

### Claim 9: Scenario testing surfaced a privacy concern — a concept recommending products using social media signals — that abstract concept testing would not have revealed
- **Evidence**: Named example of a problem the scenario-based approach surfaced.
- **Confidence**: anecdotal (single example, no comparison against what abstract testing of the same concept would have shown)
- **Quote**: "A concept that recommended products using social media signals immediately raised privacy concerns."
- **Our assessment**: A concrete, specific instance of the general claim that situated scenario-testing surfaces issues abstract concept-testing misses. Useful as a worked example for a guide section on AI-assisted concept pressure-testing, but it is one example from one project.

### Claim 10: Of the five shortlisted concepts, some were eliminated at the scenario-testing stage for having narrow appeal that didn't justify investment, or for being compelling once but offering no reason for a traveler to return
- **Evidence**: Author's account of what the AI-assisted scenario exercise eliminated before the concepts reached real users.
- **Confidence**: anecdotal (single-project account, exact number of eliminated concepts not stated)
- **Quote**: "Other concepts revealed different weaknesses: appeal that was too narrow to justify investment, or experiences that felt compelling once but offered nothing to bring a traveler back."
- **Our assessment**: This names two specific, reusable failure modes for product concepts (narrow appeal; no repeat value) that a guide section on AI-assisted concept triage could use as a checklist, though the article gives no detail on which of the five concepts these applied to or how many were cut.

### Claim 11: Eight users, tested via a mix of Maze sessions and in-person interviews, provided directional (not statistical) validation, and themes that had surfaced during the AI-assisted simulation reappeared in real user sessions without the team prompting for them
- **Evidence**: Author's account of the final validation step and its outcome, the article's only claim of external (human) corroboration for the AI-surfaced findings.
- **Confidence**: anecdotal (self-reported outcome by the same author who ran both the AI exercise and the user sessions; no independent observer or blinded comparison confirms that the "themes" genuinely reappeared unprompted rather than being pattern-matched after the fact by someone who already expected them)
- **Quote**: "We tested a prototype with eight users, a mix of Maze sessions and in-person interviews." / "Themes that had surfaced during the AI-assisted simulation reappeared in real sessions without prompting."
- **Our assessment**: This is the article's central evidentiary claim — that the AI-generated hypotheses (Claims 7, 9, 10) were validated by real users — but it is self-reported by the same practitioner who designed both the AI exercise and interpreted the user sessions, with no blinding, no named researcher other than the author, and n=8 (explicitly framed by the author as directional, not statistically significant). This should be presented in the guide as a single practitioner's account of AI-hypothesis-then-human-confirmation, not as demonstrated proof that AI reliably predicts user research outcomes.

### Claim 12: Work that would traditionally span multiple synthesis sessions and rounds of internal alignment happened in hours, letting the team reach user research faster and with sharper questions
- **Evidence**: Author's own before/after comparison of process speed, given in the "What actually changed" section.
- **Confidence**: anecdotal (comparison to an implied but unspecified baseline — "traditionally" — not a measured time-on-task comparison within this project)
- **Quote**: "Work that would traditionally span multiple synthesis sessions and rounds of internal alignment happened in hours, which meant we arrived at user research faster, and with sharper questions."
- **Our assessment**: This is a speed claim with no baseline measurement (no stated number of hours, no stated number of "traditional" sessions it's being compared against) — it is a qualitative impression, not a benchmark. Should be cited in the guide as illustrative language ("compressed from sessions to hours"), not as a quantified efficiency gain.

### Claim 13: AI is useful in product discovery for expanding idea spaces, exploring alternative perspectives, building and refining behavioral archetypes, stress-testing concepts, and generating hypotheses — but is not useful for predicting adoption, replacing user research, or making strategic decisions
- **Evidence**: Author's explicit boundary-setting list in the "Where this works and where it doesn't" section, presented as the article's generalized takeaway beyond the single case study.
- **Confidence**: anecdotal (a generalized prescriptive claim extrapolated from one project's experience, not tested against counterexamples or other projects)
- **Quote**: "Expanding idea spaces. Exploring alternative perspectives. Building and refining behavioral archetypes. Stress-testing concepts. Generating hypotheses." / "Predicting adoption. Replacing user research. Making strategic decisions."
- **Our assessment**: This is the article's most guide-actionable claim — an explicit "AI helps with X, not Y" boundary for product discovery work. It is consistent with the general corpus pattern of AI augmenting rather than replacing judgment-heavy human work (see Cross-References), but as a generalization from a single project it should be presented as the author's own considered opinion, not an industry-validated rule.

## Concrete Artifacts

```
Source: Aditya Karle, "The discovery dilemma: Using AI to focus research
where it matters," Thoughtworks Insights, published July 3, 2026.

Project methodology funnel (as described in the article):
  ~20 concepts (workshop-generated, spanning shopping, utility,
    personalization, airport navigation, local discovery, travel assistance)
    -> CVP (consumer value proposition) + BVP (business value proposition)
       prioritization
    -> 5 shortlisted concepts
    -> 5 traveler archetypes built (frequent business travelers, leisure
       explorers, last-minute buyers, pre-planners, Gen Z digital-first
       travelers), Claude used to model archetype responses to each concept
    -> concept-to-scenario conversion ("Would you use this?" ->
       "What would you do here?")
    -> 8-user prototype validation (mix of Maze sessions + in-person
       interviews)

Article's explicit "works / doesn't work" list (verbatim, from the
"Where this works and where it doesn't" section):
  Works for:
    - Expanding idea spaces
    - Exploring alternative perspectives
    - Building and refining behavioral archetypes
    - Stress-testing concepts
    - Generating hypotheses
  Doesn't work for:
    - Predicting adoption
    - Replacing user research
    - Making strategic decisions

Section headings, in order:
  (unheaded intro: "The discovery dilemma: Using AI to focus research
    where it matters")
  Starting with uncertainty
  Using AI as a thinking partner
  From concepts to scenarios
  Validating with users
  What actually changed
  Where this works and where it doesn't
  The real opportunity
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-kamelman-unbundling-expertise.md`,
`blog-anthropic-jessyan-pm-agentic-era.md`, and `blog-openai-endava-frontiers.md`
were re-read directly (MINER.md §4b) and claim numbers below were confirmed
against those notes' numbered `### Claim N:` (or `### Claim:`) headings in
document order.

- **Corroborates**:
  - `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 3 (success
    with AI is primarily a measure of a person's capacity to externalize a
    coherent internal model so another intelligence can act on it) and
    Claim 6 (expertise isn't the multiplier for AI-assisted work —
    transmissibility is): this article's Claim 6 (the value came from
    providing Claude context it couldn't infer — airport psychology, not
    from the modeling exercise itself) is a concrete, single-project
    instance of Kamelman's abstract thesis. Kamelman argues the mechanism
    in the general case; Karle reports living it on one project.
  - `blog-anthropic-jessyan-pm-agentic-era.md` Claim 6 (the PM's workflow
    splits cleanly between Claude/Cowork for "open-ended research and
    discovery — the murky, early-stage exploration" and Claude Code for
    building, once "greater clarity on the job to be done" exists): both
    sources independently place AI-assisted exploration *before* a
    commitment point (Yan: before writing a custom agent; Karle: before
    committing user-research budget to specific concepts), using AI to
    resolve murkiness cheaply so the more expensive/committed step that
    follows is better-targeted. Different roles (PM tooling workflow vs.
    product discovery methodology) and different AI use (agent-building
    prep vs. concept pressure-testing), but the same underlying "cheap AI
    exploration narrows what's worth the expensive step" structure.
  - `blog-openai-endava-frontiers.md` Claim 5 (AI is "embedded throughout
    the entire DavaFlow lifecycle — from meeting preparation and business
    planning to **product discovery**, software engineering, and
    deployment"): Endava's article names product discovery as one phase
    among many where AI is used company-wide, but — as the Prospector's
    triage comment for this issue also noted — gives no methodology detail
    for that phase. This article supplies the concrete methodology
    (concept funnel, archetype modeling, scenario conversion, validation
    loop) that the Endava piece's one-word "product discovery" mention
    lacks.

- **Contradicts**: No contradiction issue filed. This article's central
  boundary claim (Claim 13: AI helps with expanding/stress-testing concepts,
  not with predicting adoption or replacing research) does not oppose any
  existing corpus claim found during this extraction — it is consistent
  with the corpus's general pattern of treating AI as augmenting rather
  than replacing judgment-heavy validation work (e.g., the
  verification-as-bottleneck claims corroborated across
  `blog-addyosmani-code-agent-orchestra.md`, `blog-anthropic-ai-native-engineering-org.md`,
  and `blog-openai-endava-frontiers.md`, though those concern engineering
  delivery rather than product research specifically).

- **Extends**:
  - `blog-anthropic-jessyan-pm-agentic-era.md`: extends Yan's abstract
    two-tool workflow split ("Cowork for discovery... Claude Code for
    building") with a concrete, step-by-step methodology for what
    "discovery" work with AI actually looks like inside a product-research
    context specifically (concept funnel, archetype construction, scenario
    conversion, validation loop) — Yan's note names the phase boundary but
    does not describe a research methodology within the discovery phase
    itself.
  - `blog-thoughtworks-kamelman-unbundling-expertise.md`: extends
    Kamelman's abstract "externalized context is the multiplier" thesis
    with a concrete example of what that context looks like in a specific
    professional discipline (product discovery: airport psychology,
    traveler journey moments) rather than Kamelman's own more abstract
    software-engineering-adjacent illustrations (the accountant/junior-
    developer example).

- **Novel**:
  - **The CVP/BVP-then-AI-archetype-modeling funnel** as a named,
    step-by-step product discovery methodology: no existing corpus source
    describes a specific sequence for where AI enters a concept-narrowing
    funnel (after human prioritization, before user research) in this much
    procedural detail.
  - **"What would you do here?" vs. "Would you use this?" as a scenario-
    design principle for AI-assisted concept testing**: not present
    elsewhere in the corpus's product-workflow coverage.
  - **The self-reported AI-hypothesis-then-user-confirmation loop** (Claim
    11: AI-surfaced themes "reappeared in real sessions without prompting")
    is a distinct evidentiary pattern from the corpus's existing AI-adoption
    case studies, which generally report either AI output alone or human
    outcomes alone, not a claimed before/after match between the two within
    a single project.

## Guide Impact

- **Chapter 02 / product-and-discovery-workflow sections**: Add the
  CVP/BVP → AI-archetype-modeling → scenario-conversion → user-validation
  funnel (Claim 4, 5, 8, Concrete Artifacts) as a concrete, reusable
  discovery-phase pattern, explicitly citing this as a single practitioner's
  account (n=1 project, n=8 users) rather than a validated methodology.
  Currently the guide's product-workflow material (via
  `blog-openai-endava-frontiers.md`) only names "product discovery" as a
  phase without procedural detail — this source fills that gap.
- **Chapter 04 / effective prompting or context-provision sections**: Add
  Claim 6 (the value came from providing Claude context it couldn't infer —
  airport psychology, not the archetype-modeling technique itself) as a
  second, domain-different illustration of the "externalized context is the
  multiplier, not the tool" principle already sourced from
  `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 3/6. Recommend
  presenting the two sources together: Kamelman for the abstract mechanism,
  Karle for a concrete non-engineering domain instance of it.
- **Chapter 06 / AI-assisted research and evaluation sections**: Add Claim
  13's explicit "works for / doesn't work for" boundary list as a
  discovery-specific instance of the augment-not-replace framing already
  present in the corpus for engineering delivery — flag it as one
  practitioner's generalization from a single project, not an
  industry-validated boundary.
- **Any chapter cautioning about self-reported validation claims**: Claim 11
  (AI-surfaced themes "reappeared... without prompting" in user testing) is
  a useful example of a claim that sounds like independent validation but is
  actually self-reported by the same person who ran both halves of the
  comparison, with no blinding and n=8 — worth flagging as a pattern to
  watch for when practitioners report "AI predicted what users later said."

## Extraction Notes

- **WebFetch declined full verbatim reproduction**, citing copyright
  concerns (consistent with other Thoughtworks extractions in this corpus,
  e.g. `blog-thoughtworks-kamelman-unbundling-expertise.md`). Rather than
  retry with a raw-HTML fetch, this note was built from a sequence of five
  targeted WebFetch calls, each asking for a detailed structural
  summary/outline (author, date, section-by-section paraphrase with
  specific numbers) plus short, explicitly verbatim (under-40-word) quotes
  for specific named passages. Every `Quote` field in this note comes from
  one of those targeted verbatim-quote requests, not from the initial
  summary-only response. This is a slightly different verification method
  than the direct-`curl`-plus-HTML-strip approach used in some other
  Thoughtworks notes in this corpus; it was not independently cross-checked
  against a raw HTML fetch, so there is a residual (believed low) risk that
  a quote reflects the fetch model's close paraphrase rather than the
  page's exact wording. Flagging this for the Assayer's spot-check.
- **No sub-pages were followed.** The article contains no internal links to
  other substantive Thoughtworks pages beyond standard site navigation/
  author-bio boilerplate (checked via the structural-outline fetch); this
  is a standalone, self-contained article.
- **The client and product are never named.** "A global travel retailer"
  and "a greenfield loyalty proposition" are the only identifying details
  given; this is consistent with typical consulting-firm case-study
  anonymization and was not treated as evasive, but it does mean none of
  this article's claims can be independently corroborated against a named
  company's public statements, unlike (for contrast) the corpus's Uber,
  Microsoft, or Duolingo token-cost case studies, which name the company
  and are corroborated via independently followed third-party reporting.
- **No contradiction issues filed.** See Cross-References → Contradicts for
  reasoning — this article's claims are consistent in direction with the
  existing corpus's augment-not-replace framing, and no existing note argues
  the opposite about AI's role in product discovery specifically.
