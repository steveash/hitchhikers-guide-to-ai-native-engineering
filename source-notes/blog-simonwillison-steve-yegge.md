---
source_url: https://simonwillison.net/2026/Apr/13/steve-yegge/
source_type: blog-post
title: "Steve Yegge"
author: Simon Willison (link-blog note relaying Steve Yegge)
date_published: 2026-04-13
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: anecdotal
issue: "#247"
---

# Steve Yegge: AI Adoption Curve and Organizational Information Isolation

> A short Simon Willison link-blog note that surfaces Steve Yegge's 20/20/60 adoption-curve
> claim (20% agentic power users / 20% outright refusers / 60% still on chat/Cursor) and the
> hiring-freeze-as-information-isolation hypothesis — along with direct rebuttals from Addy
> Osmani and Demis Hassabis — making the note most useful to Ch05 not for its contested
> Google-specific claims but for the underlying pattern about how large orgs lose visibility
> into where they stand relative to the industry.

## Source Context

- **Type**: blog-post (Simon Willison "note" format — link-blog relay, ~200 words, embedding
  Yegge's tweet thread and responses from Osmani and Hassabis; NOT an original analysis by
  Willison)
- **Author credibility**: Simon Willison is the creator of Django and one of the most widely-
  cited LLM-tooling commentators. His link-blog notes do not endorse the embedded claims —
  they surface them for community attention. The primary source is Steve Yegge, ex-Google
  engineering lead, currently at Sourcegraph, credible on Google culture but working from a
  secondhand account ("my buddy at Google"). Addy Osmani is Director of Engineering at
  Google Chrome and is giving a first-party rebuttal. Demis Hassabis is Google DeepMind CEO.
  All named parties have track records and institutional affiliations; none are anonymous.
- **Scope**: Covers one Twitter exchange about AI adoption patterns inside Google specifically
  and the broader tech industry. Does NOT cover tool selection, harness design, productivity
  metrics, or team-level practices. The analytical payload is in the embedded quotes, not
  Willison's prose. The post is too short to carry independent research weight; its value is
  surfacing a credibility dispute over a specific adoption model.

## Extracted Claims

### Claim 1: The software industry has a consistent internal AI adoption curve of 20% agentic power users / 20% outright refusers / 60% still on chat/Cursor equivalents

- **Evidence**: Steve Yegge's claim, sourced from a conversation with a 20-year Google tech
  director. Presented as an industry-wide generalization, not Google-specific: "Most of the
  industry has the same internal adoption curve."
- **Confidence**: anecdotal — secondhand from a single named insider; not corroborated by
  any survey or instrumented data. Useful as a mental model, not as a data point.
- **Quote**: "Most of the industry has the same internal adoption curve: 20% agentic power
  users, 20% outright refusers, 60% still using Cursor or equivalent chat tool."
  — Steve Yegge, via Simon Willison, 2026-04-13
- **Our assessment**: The 20/20/60 framing is a specific, nameable model for enterprise AI
  adoption segmentation. Even if the percentages are wrong, the three-segment structure
  (power users / refusers / passive adopters) maps cleanly onto what Ch05 needs: not just
  "how many people use AI" but "what are the three types of adopters and what does each
  need from a team rollout strategy?" Treat as a hypothesis to design around, not a data
  point to cite without hedging. The passive-adopter majority (the 60%) is the least
  discussed in the literature and may be the highest-leverage segment for team adoption
  work.

### Claim 2: Google's engineering organization has an AI adoption footprint comparable to John Deere's (contested)

- **Evidence**: Steve Yegge's claim, attributed to a Google tech director contact. Directly
  and forcefully disputed by Addy Osmani (Google Chrome Director of Engineering) and Demis
  Hassabis (Google DeepMind CEO).
- **Confidence**: anecdotal on the Yegge side; first-party denial on the Osmani/Hassabis
  side. The Google-specific claim is unreliable — two named insiders with institutional
  standing directly contradict it.
- **Quote (Yegge)**: "Google engineering appears to have the same AI adoption footprint as
  John Deere, the tractor company."
- **Quote (Osmani)**: "On behalf of @Google, this post doesn't match the state of agentic
  coding at our company. Over 40K SWEs use agentic coding weekly here."
- **Quote (Hassabis)**: "Maybe tell your buddy to do some actual work and to stop spreading
  absolute nonsense. This post is completely false and just pure clickbait."
- **Our assessment**: Do NOT extract the Google-specific claim as a reliable data point.
  Yegge is working from a secondhand account of a single contact; Osmani and Hassabis are
  first-party insiders with reputational stakes in the rebuttal. The interesting guide-relevant
  observation is not who is right about Google, but that this public dispute exists at all —
  two named Google leaders treating the claim as serious enough to rebut by name signals that
  (a) the 20/20/60 framing is credible enough to draw fire, and (b) internal adoption data at
  large companies is opaque enough that outsiders cannot verify it. Both of those meta-
  observations are relevant to Ch05.

### Claim 3: Addy Osmani's counter-claim — Google has 40K+ SWEs using agentic coding weekly, with internal Gemini CLI, MCPs, orchestrators, and virtual SWE teams

- **Evidence**: First-party claim from Addy Osmani (Google Chrome Director of Engineering),
  tweeting directly in response to Yegge's post.
- **Confidence**: anecdotal (self-reported, not independently audited, but first-party)
- **Quote**: "Over 40K SWEs use agentic coding weekly here. Googlers have access to our own
  versions of @antigravity, @geminicli, custom models, skills, CLIs and MCPs for our daily
  work. Orchestrators, agent loops, virtual SWE teams and many other systems are actively
  available to folks."
  — Addy Osmani, April 2026
- **Our assessment**: If accurate, 40K weekly agentic users at Google is a significant data
  point — it exceeds the "20% of a large tech org" threshold that Yegge implies, though
  Google's total SWE headcount is not stated. The list of capabilities (custom Gemini CLI,
  MCPs, orchestrators, virtual SWE teams) is the more actionable extract: it describes the
  rough feature set of a mature internal agentic coding platform. Whether the headcount claim
  is inflated or the bar for "agentic" is looser than Yegge's "power user" definition is
  unresolvable from this source, but the existence of the platform is credible.

### Claim 4: An 18+ month industry-wide hiring freeze has cut information flow between companies, leaving lagging organizations unaware of how far behind they are

- **Evidence**: Steve Yegge's hypothesis, stated as an explanation for why low-adoption
  companies (in his framing) remain unaware of their status. Not directly disputed by Osmani
  or Hassabis, who focused their rebuttals on the Google-specific adoption claim.
- **Confidence**: anecdotal — plausible mechanism, not empirically tested; but the hiring
  freeze in tech (late 2022 onward) is a documented macro trend. The causal link to
  information isolation is Yegge's original hypothesis.
- **Quote**: "There has been an industry-wide hiring freeze for 18+ months, during which
  time nobody has been moving jobs. So there are no clued-in people coming in from the
  outside to tell Google how far behind they are, how utterly mediocre they have become
  as an eng org."
- **Our assessment**: This is the most extractable novel signal in the source and it is not
  contested. The mechanism is straightforward: job mobility carries tacit knowledge about
  tool usage and practices across company boundaries. When job mobility drops, companies lose
  the informal benchmarking signal that tells them where they stand relative to peers. This
  is particularly sharp for AI adoption, where the state of practice is evolving weekly and
  no single public survey captures ground truth. For Ch05, this claim motivates external
  engagement (open source contribution, conference attendance, peer learning networks) as a
  deliberate antidote to adoption isolation — if you cannot benchmark against incoming hires,
  you must benchmark through other channels. This claim stands regardless of whether the
  Google framing is accurate.

### Claim 5: The public dispute itself is evidence that large-org adoption data is opaque enough to support sharply divergent first-party claims

- **Evidence**: The Yegge/Osmani/Hassabis exchange. Two Google insiders with senior
  institutional standing publicly denied a claim about their own organization with unusual
  forcefulness (Hassabis: "pure clickbait"), yet the claim was vivid enough to draw their
  attention. This level of credibility dispute about *internal company data* is unusual.
- **Confidence**: anecdotal (inference from the exchange)
- **Quote**: (see Claim 2 quotes above)
- **Our assessment**: When named senior leaders at a company feel the need to publicly rebut
  a claim about their company's internal adoption, it is evidence that (a) the claim is
  circulating seriously enough to damage perception, and (b) the internal reality is opaque
  enough to outsiders that an unsubstantiated secondhand account can be taken seriously.
  Neither of those conditions holds for, say, a claim about a company's public API — which
  is verifiable. Adoption rates for internal tools are not verifiable from outside. This
  meta-observation is directly relevant to Ch05's "measuring adoption" section: any
  benchmark you use for your own organization's adoption will be similarly contested,
  similarly opaque to outsiders, and similarly shaped by who is doing the measuring and why.

## Concrete Artifacts

### The 20/20/60 Adoption Curve (Yegge's model)

```
Industry AI adoption segmentation (Steve Yegge, 2026-04-13):

  20% — Agentic power users
          (fully integrated agentic workflows; directing agents as primary
          development mode)

  60% — Chat/Cursor-equivalent users
          (AI assistance in the IDE or chat; not agentic; still
          primarily hand-writing code)

  20% — Outright refusers
          (not using AI tools at all; active or passive resistance)

Source: Steve Yegge tweet thread, as relayed by Simon Willison
        simonwillison.net/2026/Apr/13/steve-yegge/
Note: secondhand (Yegge's Google contact); percentages are Yegge's
      characterization, not instrumented survey data.
```

### Osmani's counter-description of Google's internal agentic platform (2026)

```
Reported internal Google agentic coding platform (Addy Osmani, April 2026):
  - Custom versions of "antigravity" (likely internal agent tooling)
  - Gemini CLI (command-line agent interface)
  - Custom models
  - Skills and CLIs
  - MCP integrations
  - Orchestrators
  - Agent loops
  - Virtual SWE teams
  - Active users: 40K+ SWEs using agentic coding weekly

Source: Addy Osmani, Twitter, April 2026 (via Willison's relay)
```

## Cross-References

- **Corroborates**:
  - `survey-pragmaticengineer-ai-tooling-2026.md` — the Pragmatic Engineer survey
    (staff+ at 63.5% agent use, regular engineers at 49.7%) does not map directly onto
    Yegge's 20% power-user ceiling, but both sources agree on segmentation: adoption is
    not uniform across the organization, and the senior cohort leads. The specific
    percentages diverge significantly (20% vs. 49–63%), likely because Yegge's "agentic
    power user" definition is stricter than "regularly uses AI agents." The Pragmatic
    Engineer data is more reliable (906-respondent survey vs. secondhand anecdote), so
    Ch05 should weight it more heavily — but Yegge's three-segment framing is a useful
    complement for the qualitative discussion of adoption types.
  - `failure-noemit-early-agentic-adoption.md` — Lesson 5 ("neutral on agentic coding is
    a valid outcome") maps onto Yegge's 60% passive-adopter segment. noemit's "it's a new
    modality, pros and cons" framing is the practitioner-level version of someone in that
    60% — using AI tools, not refusing them, but not transformed by them.
  - `discussion-hn-agentic-coding-jobs.md` — codingdave's "minor speed improvement plus
    more slop" (Claim 10) is another voice in the 60% segment: using AI tools, getting
    marginal rather than transformative returns, not refusing but not power-using.

- **Contradicts**: None filed. The tension between Yegge's 20% industry-wide power-user
  estimate and the Pragmatic Engineer's 49–63% staff-level agent adoption figures is
  real but stems from different metric definitions ("power user" vs. "regularly uses
  agents"), different populations (industry-wide anecdote vs. senior-engineer survey
  audience), and different time periods. This does not rise to a guide-advice-changing
  contradiction. The guide should present both figures with their definitions rather than
  treating them as contradictory. The Google-specific dispute (Yegge vs. Osmani/Hassabis)
  is contained within this source and does not contradict any existing source note.

- **Extends**:
  - `survey-pragmaticengineer-ai-tooling-2026.md` — adds the hiring-freeze hypothesis
    (Claim 4) as a mechanism that explains why company-to-company adoption variance can
    be large and self-reinforcing: the normal information-transfer vector (job mobility)
    is suppressed. The Pragmatic Engineer survey documents what the adoption distribution
    looks like; Yegge's hypothesis offers a causal mechanism for why laggards stay laggers.
  - `discussion-hn-agentic-coding-jobs.md` (Zapier posting on agentic-first hiring) —
    Yegge's 20% power-user ceiling and Zapier's explicit requirement for agentic workflow
    competency are complementary framing for Ch05: Zapier is selecting from that 20%, and
    the implication is that the remaining 80% are not yet candidates for agentic-first
    roles.

- **Novel**:
  - **The hiring-freeze-as-information-isolation hypothesis (Claim 4)**: No other source
    in the corpus identifies job mobility as the primary channel through which companies
    benchmark their AI adoption against peers, or names the hiring freeze as a mechanism
    that breaks this channel. This is a distinct causal claim about *why* adoption
    variance is large and sticky, not just that it is.
  - **Named three-segment adoption typology (20/20/60)**: The Pragmatic Engineer survey
    segments by role; the noemit and codingdave posts describe individual experiences.
    Yegge's three-type framing (power user / passive / refuser) is the first explicit
    named segmentation model in our corpus with attached rough percentages. Even if the
    numbers are wrong, the *typology* is usable for Ch05 without relying on the contested
    percentages.
  - **A named credibility dispute over internal adoption data at a top tech company**:
    No other corpus source documents a public, named, multi-party dispute over AI adoption
    claims. The Osmani/Hassabis rebuttals, combined with the Yegge claim, provide the
    corpus's clearest illustration that internal adoption data is essentially unverifiable
    from outside — a meta-point relevant to how teams should think about external benchmarks.

## Guide Impact

- **Chapter 05 (Team Adoption — Adoption Segmentation)**: The 20/20/60 typology (even
  treated as a rough hypothesis) is a useful planning model for team rollout strategy.
  Ch05 should name the three segments explicitly: power users, refusers, and passive
  adopters. Each segment requires different intervention. The passive majority (60%) is
  likely the highest-leverage group — they are not refusing, they just haven't restructured
  their workflow. Pair Yegge's typology with the Pragmatic Engineer survey's role-level
  data as a more reliable quantification of the same pattern.

- **Chapter 05 (Team Adoption — Why Adoption Variance Is Sticky)**: Add the
  hiring-freeze-as-information-isolation hypothesis (Claim 4) as a mechanism explaining
  why teams at low-adoption organizations may have no internal benchmark for how far
  behind they are. Practical implication: teams cannot rely solely on incoming hires to
  carry tacit knowledge about current best practices — they need deliberate external
  engagement (open source, conferences, peer communities) to close the information gap.
  This is a specific, actionable recommendation that currently has no equivalent in
  the corpus.

- **Chapter 05 (Team Adoption — Measuring and Benchmarking Adoption)**: Claim 5 (the
  opacity of internal adoption data) supports adding a note of caution to any section
  recommending that teams benchmark against industry peers: the Yegge/Osmani dispute
  illustrates that even first-party claims about major companies' internal adoption are
  contested. External benchmarks should be used to identify the direction of travel, not
  as precise comparisons. The Pragmatic Engineer survey (906 respondents, stated
  methodology) is a more reliable benchmark than any company's self-reported adoption
  narrative.

- **Chapter 01 (Current Landscape — Honest State of Adoption)**: The three-segment model
  provides a concrete framing for "where the industry is in early 2026" that goes beyond
  "adoption is high" — it names the distribution shape (majority still in the passive
  middle, not yet agentic). Pair with the Pragmatic Engineer stat (56% do ≥70% of work
  with AI) for the appropriate nuance: the high-adoption stat is real AND the passive
  majority is real, depending on how you define the question.

## Extraction Notes

- **Short source (link-blog note, ~200 words)**: The analytical payload is entirely in the
  embedded quotes from Yegge, Osmani, and Hassabis — Willison's own prose is minimal and
  non-analytic. The source does not link to Yegge's original tweet thread in extractable
  form; the quotes as relayed by Willison are the accessible text. Twitter/X requires login
  to read full threads; Willison's relay is the accessible version.
- **The Prospector filed three separate triage comments** (the issue ran through three
  triage cycles). All three converge on the same key signals: extract the 20/20/60 (or
  20/60/20) typology as a hypothesis, not a fact; flag the Google-specific claims as
  unreliable (named first-party rebuttal); and treat the hiring-freeze claim as the highest-
  confidence novel signal (undisputed, plausible mechanism).
- **The 20/20/60 vs. 20/60/20 framing discrepancy**: The Prospector comments use both
  orderings (20/20/60 and 20/60/20). Yegge's original quote lists it as "20% agentic
  power users, 20% outright refusers, 60% still using Cursor" — so 20/20/60 is the correct
  reading with the 60 in the middle (passive users), not at the end. The source note uses
  this ordering throughout.
- **No contradiction issue filed**: The tension between Yegge's 20% power-user estimate
  and the Pragmatic Engineer's 49–63% staff-level figures was assessed and deemed a
  metric-definition difference rather than a guide-advice-changing contradiction. If a
  future source provides population-matched data that directly contradicts either figure,
  a contradiction issue should be filed at that time.
- **Confidence ceiling**: anecdotal throughout. The primary value of this source is the
  named typology and the hiring-freeze mechanism hypothesis, not the specific percentages
  or the Google-specific claims.
