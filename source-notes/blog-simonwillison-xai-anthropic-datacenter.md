---
source_url: https://simonwillison.net/2026/May/7/xai-anthropic/
source_type: blog-post
title: "Notes on the xAI/Anthropic data center deal"
author: Simon Willison
date_published: 2026-05-07
date_extracted: 2026-05-16
last_checked: 2026-05-16
status: current
confidence_overall: emerging
issue: "#755"
---

# Notes on the xAI/Anthropic Data Center Deal

> Simon Willison's analysis of Anthropic's compute-constrained infrastructure
> choice to lease xAI's Colossus 1 data center: documents the specific
> environmental violations (unpermitted gas turbines, hospital admissions),
> the governance risk from Musk's unilateral "reclaim" clause, and the
> supply chain risk pattern illustrated by xAI's same-week deprecation of
> multiple Grok models with two weeks' notice.

## Source Context

- **Type**: blog-post (Simon Willison's blog, May 7, 2026 — a standalone
  analysis post following his live blog of the May 6 Code w/ Claude event.
  This is Willison's own considered commentary, not live event coverage.
  Published one day after the announcement.)
- **Author credibility**: Simon Willison is the creator of Django, one of the
  most widely-read independent AI tooling commentators, and a 25-year software
  engineering practitioner. No vendor affiliation. His commentary on the
  environmental record and supply chain risk is independent practitioner
  analysis, not vendor-provided framing. He was among the first to name the
  Colossus environmental concerns in public AI commentary.
- **Scope**: Covers the Anthropic/xAI Colossus 1 data center deal announced
  May 6, 2026. Includes: compute constraint context, Colossus 1 vs Colossus 2
  distinction, specific environmental violations (permits, gas turbines, air
  quality), a named expert critique (Andy Masley), Musk's approval and
  governance clause, and the xAI Grok model deprecation event as a concrete
  supply chain risk illustration. Does NOT cover product feature announcements
  from the Code w/ Claude event — this post focuses entirely on the
  infrastructure deal and its risks.

## Extracted Claims

### Claim 1: Anthropic is "severely compute-constrained" and struck the Colossus deal primarily out of capacity need, not strategic preference

- **Evidence**: Willison's direct editorial framing in the post, named
  explicitly as his interpretation of Anthropic's motivation.
- **Confidence**: anecdotal (Willison's inference, not an Anthropic statement;
  consistent with the 17x YoY API growth context in
  `blog-simonwillison-code-w-claude-2026.md` Claim 4)
- **Quote**: "I get that Anthropic are severely compute-constrained"
- **Our assessment**: The phrase "severely compute-constrained" is Willison's
  characterization, not an official Anthropic statement, but it fits the
  available evidence — Anthropic secured full capacity of an existing facility
  rather than building new infrastructure, and the deal was the "biggest"
  announcement at their developer event, signaling it addressed a material
  operational bottleneck. The framing matters for guide advice: this is an
  infrastructure decision made under constraint, not a strategic partnership
  chosen for its attributes.

### Claim 2: Anthropic receives access to Colossus 1; xAI retains the larger Colossus 2 for their own AI development

- **Evidence**: Specific factual clarification in the article, addressing
  misconceptions that xAI surrendered their compute advantage.
- **Confidence**: settled (factual distinction about which facility was leased;
  independently verifiable)
- **Quote**: "Anthropic are getting Colossus 1, but xAI are keeping their
  larger Colossus 2 data center for their own work."
- **Our assessment**: The Colossus 1 / Colossus 2 distinction matters for
  assessing the deal's scale. xAI did not hand over their primary development
  infrastructure. Anthropic gained access to significant capacity, but the
  deal does not represent xAI deprioritizing their own AI development. This
  also means the governance risk (Claim 5 below) applies to an asset xAI does
  not depend on for its own work — they can afford to reclaim or restrict it.

### Claim 3: The Colossus facility's gas turbines ran without Clean Air Act permits by classifying them as "temporary" installations

- **Evidence**: Specific factual claim about the environmental regulatory
  history of the facility, cited with concrete regulatory details.
- **Confidence**: emerging (Willison states this as fact; independently
  reported by others but sourced here through Willison's commentary)
- **Quote**: "The gas turbines installed to power the facility initially ran
  without Clean Air Act permits or pollution control devices, which they got
  away with by classifying them as 'temporary'."
- **Our assessment**: This is not a general environmental criticism — it
  describes a specific regulatory strategy (classify as "temporary" to avoid
  permitting) with a specific violation type (Clean Air Act, no pollution
  control devices). For practitioners evaluating AI infrastructure vendors,
  this pattern signals that the facility operator is willing to use regulatory
  loopholes to accelerate deployment. Whether this rises to a material business
  risk depends on organizational values and sustainability commitments.

### Claim 4: Credible reports link the Colossus facility to increased hospital admissions from air quality degradation

- **Evidence**: Willison cites "credible reports" without specific attribution
  in the post; the underlying health reports exist independently.
- **Confidence**: emerging (Willison characterizes the reports as "credible"
  but does not name the specific studies or reports; the claim is not
  independently verified through this source)
- **Quote**: "Credible reports link it to increases in hospital admissions
  relating to low air quality."
- **Our assessment**: This is the most serious claim in the source: not just
  an environmental compliance failure but a documented public health impact
  near the facility. Without named citations, the "credible reports" framing
  should be treated as emerging evidence. For practitioners with health,
  environmental, or ESG commitments, this claim warrants independent
  verification before acting on it.

### Claim 5: Choosing the Colossus facility "is a really bad look" given the current political scrutiny of AI data centers

- **Evidence**: Willison's direct editorial judgment, with specific political
  context (AI infrastructure as "red-hot political issue").
- **Confidence**: anecdotal (Willison's opinion; not a factual claim but a
  practitioner assessment worth noting)
- **Quote**: "in a world where the very existence of 'AI data centers' is a
  red-hot political issue...signing up with this particular data center is a
  really bad look."
- **Our assessment**: The political risk framing adds a dimension beyond
  environmental compliance: reputational and regulatory risk from selecting
  an infrastructure partner with a documented violation history at a time of
  heightened public scrutiny. For enterprise practitioners evaluating AI
  infrastructure, this is a governance and communications risk, not just
  a technical one. The claim also reflects Willison's broader skepticism of
  AI-infrastructure rhetoric versus actual infrastructure quality.

### Claim 6: A prominent data center critic stated they "would simply not run" their compute at this specific facility

- **Evidence**: Direct named quote from Andy Masley, identified as a data
  center critic familiar with the Colossus facility's record.
- **Confidence**: settled (direct attributed quote from a named expert;
  independently verifiable)
- **Quote**: "I would simply not run my computing out of this specific data
  center"
- **Our assessment**: Andy Masley's statement is the strongest expert signal
  in the source. A data center specialist — not an AI policy advocate — who
  has specific knowledge of this facility's record making an unambiguous
  "would not use" statement is meaningful signal. The quote doesn't
  distinguish between the environmental record as the reason and reputational
  risk as the reason; it's a direct operational judgment. For guide purposes,
  this is the single most actionable expert claim: a named domain expert
  explicitly advising against this infrastructure choice.

### Claim 7: Elon Musk personally reviewed Anthropic's approach before approving the deal

- **Evidence**: Musk's own Twitter post, quoted in the article.
- **Confidence**: settled (Musk's stated claim on Twitter; independently
  verifiable as a public post)
- **Quote**: "I spent a lot of time last week with senior members of the
  Anthropic team to understand what they do to ensure Claude is good for
  humanity and was impressed."
- **Our assessment**: Musk's personal approval framing positions the compute
  lease as a conditional relationship — Anthropic must satisfy Musk's
  assessment of Claude's humanity-benefit stance to use the infrastructure.
  This is unusual for a data center lease, where infrastructure is typically
  provided as a utility without content conditions. The governance implication
  is that Anthropic's infrastructure access is contingent on ongoing external
  approval by a single individual.

### Claim 8: Elon Musk reserved the right to reclaim Colossus compute if Claude "engages in actions that harm humanity," with criteria apparently set by Musk alone

- **Evidence**: Musk's own Twitter post, quoted directly in the article.
- **Confidence**: settled (Musk's stated claim on Twitter; independently
  verifiable as a public post — the risk is real and documented)
- **Quote**: "We reserve the right to reclaim the compute if their AI engages
  in actions that harm humanity."
- **Our assessment**: This is the most significant governance risk in the
  source. The clause gives Musk unilateral authority to terminate Anthropic's
  compute access based on subjective criteria ("harm to humanity") that Musk
  defines. There is no arbitration mechanism, no SLA protection, and no
  mutually-agreed definition of the trigger condition. For practitioners
  building on Claude: if Musk exercises this clause, Anthropic faces a
  sudden compute capacity reduction that could affect rate limits, model
  availability, and pricing. This is infrastructure supply chain risk made
  explicit in contractual form. Willison's characterization of this as "a new
  form of supply chain risk" (Claim 9) captures the practitioner consequence.

### Claim 9: The Colossus deal introduces "a new form of supply chain risk" for Anthropic from its compute dependency on a single external provider with unilateral governance rights

- **Evidence**: Willison's direct editorial framing, synthesizing the
  governance clause (Claim 8) and overall deal structure.
- **Confidence**: anecdotal (Willison's analytical judgment, not a factual
  claim — but well-reasoned from the documented evidence)
- **Quote**: "Sounds like a new form of supply chain risk for Anthropic to me!"
- **Our assessment**: This is the most important analytical contribution of
  the source. Willison names a pattern: when AI model providers depend on
  external compute controlled by a party with independent interests and
  unilateral governance rights, that compute dependency becomes a supply chain
  risk for the model provider's customers. The pattern generalizes beyond this
  specific deal: any AI service provider relying on a single external
  infrastructure partner who can change terms, deprecate capacity, or restrict
  access becomes a supply chain dependency for downstream practitioners. This
  is the primary novel concept in the source for guide purposes.

### Claim 10: xAI issued two-week deprecation notices for eight Grok models on the eve of the Anthropic announcement, affecting developers who had recently migrated to those models

- **Evidence**: Specific documented event: the xAI deprecation notice with
  a named list of models, a specific deadline, and a quoted practitioner
  complaint. The notice was issued "the night before the Anthropic
  announcement" (May 6, 2026).
- **Confidence**: settled (specific deprecation event with documented notice
  and deadline; independently verifiable)
- **Quote**: "Effective May 15, 2026 at 12:00pm PT, the following models will
  be retired from the xAI API: grok-4-1-fast-reasoning,
  grok-4-1-fast-non-reasoning, grok-4-fast-reasoning,
  grok-4-fast-non-reasoning, grok-4-0709, grok-code-fast-1, grok-3,
  grok-imagine-image-pro."
- **Our assessment**: Eight models deprecated simultaneously with two weeks'
  notice is an unusually aggressive deprecation timeline. The affected models
  include Grok 4.1 Fast, which practitioners had been actively migrating to.
  This deprecation event is Willison's primary concrete illustration of the
  supply chain risk pattern (Claim 9): the same operator who controls
  Anthropic's compute infrastructure also deprecates customer-facing models
  with minimal notice. For practitioners: xAI's deprecation behavior is the
  clearest available evidence of what compute-supplier governance risk looks
  like in practice — and that evidence comes from the same entity controlling
  Anthropic's infrastructure.

### Claim 11: Practitioners who had just invested in migrating to Grok 4.1 Fast were given no migration alternatives and less than two weeks to move off

- **Evidence**: Direct quoted practitioner complaint in the article.
- **Confidence**: anecdotal (single quoted complaint; the claim about lack of
  migration alternatives is from the developer perspective, not confirmed
  by xAI documentation)
- **Quote**: "This is terrible @xai. I just spent time and money to migrate
  to grok 4.1 fast, and you're disabling it with less than two weeks notice"
- **Our assessment**: The practitioner complaint illustrates the concrete
  operational impact of supply chain risk: investment in migration to a
  vendor's model (time, money, integration work) followed by sudden
  deprecation without replacement paths. This pattern — migrate to a new
  model, then face deprecation before recovering migration costs — is a
  real operational risk for AI-dependent systems. The quote's specificity
  (named model, named vendor, named consequence) makes it useful evidence
  for guide advice about vendor selection and migration risk.

## Concrete Artifacts

### xAI Grok Deprecation Notice (May 6, 2026)

```
Source: Willison quoting the xAI API deprecation notice

"Effective May 15, 2026 at 12:00pm PT, the following models will be
retired from the xAI API:
  - grok-4-1-fast-reasoning
  - grok-4-1-fast-non-reasoning
  - grok-4-fast-reasoning
  - grok-4-fast-non-reasoning
  - grok-4-0709
  - grok-code-fast-1
  - grok-3
  - grok-imagine-image-pro"

Notice issued: night of May 6, 2026 (the night before Anthropic's
announcement)
Deadline: May 15, 2026 at 12:00pm PT
Notice period: ~9 days from issue to first publication of this article
(May 7), ~2 weeks from announcement
```

### Supply Chain Risk Pattern: Compute-Constrained Provider + Unilateral Governance

```
Source: Willison, "Notes on the xAI/Anthropic data center deal" (May 7, 2026)

Pattern: AI model provider dependent on external compute with unilateral
         governance rights = supply chain risk for downstream practitioners

Mechanism:
  1. AI provider (Anthropic) is compute-constrained
  2. Provider leases capacity from infrastructure operator (xAI/SpaceX)
  3. Infrastructure operator retains unilateral rights:
     - Can reclaim compute if provider's AI "harms humanity" (Musk's terms)
     - Criteria defined unilaterally by operator, not by contract or SLA
  4. Infrastructure operator independently makes model/API decisions:
     - Deprecated 8 models with 2 weeks' notice on May 6, 2026
  5. Downstream practitioners inherit this dependency transitively:
     - Anthropic rate limits, availability, pricing all affected by (3)/(4)

Willison's framing: "Sounds like a new form of supply chain risk for
Anthropic to me!"

Expert signal: Andy Masley (data center critic): "I would simply not run
my computing out of this specific data center"
```

### Colossus Environmental Record Summary

```
Source: Willison, "Notes on the xAI/Anthropic data center deal" (May 7, 2026)

Facility: Colossus 1, Memphis (xAI/SpaceX operated)
Anthropic access: Colossus 1 only; xAI retains Colossus 2

Environmental record:
  - Gas turbines ran WITHOUT Clean Air Act permits or pollution control
    devices
  - Regulatory workaround: classified as "temporary" installations
  - Health impact: "Credible reports link it to increases in hospital
    admissions relating to low air quality."
  - Political context: "in a world where the very existence of 'AI data
    centers' is a red-hot political issue...signing up with this particular
    data center is a really bad look."
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-code-w-claude-2026.md` Claim 5: That note captured the
    surface-level announcement ("We're partnering with SpaceX to use all of the
    capacity of their Colossus data center") and Willison's parenthetical note
    about the environmental record ("That's the same Colossus data center in
    Memphis with the particularly bad environmental record."). This May 7 post
    is Willison's full analysis; the May 6 live blog is where he first flagged
    the concern.
  - `blog-simonwillison-code-w-claude-2026.md` Claim 4: The 17x YoY API
    growth metric from the same event explains the compute constraint context
    (Claim 1 here). Rapid adoption creating capacity pressure is why Anthropic
    needed the deal.

- **Extends**:
  - `blog-simonwillison-code-w-claude-2026.md` Claim 5: The live blog note
    captures the announcement; this note adds the full governance analysis:
    specific environmental violations, named expert critique, Musk's approval
    process, the reclaim clause text, and the Grok deprecation evidence for
    the supply chain risk pattern. The May 7 post substantially extends the
    May 6 surface mention.

- **Contradicts**: None filed. No claims in this source materially oppose
  claims in any existing corpus note. The supply chain risk framing and model
  deprecation pattern are new to the corpus.

- **Novel**:
  - **Compute vendor supply chain risk pattern**: No prior corpus source
    documents the pattern where AI model providers' compute dependencies
    create transitive supply chain risks for downstream practitioners. Willison
    names this pattern explicitly ("a new form of supply chain risk").
  - **Model deprecation as operational risk**: The xAI Grok deprecation event
    — 8 models, 2-week notice, no migration alternatives — is the first
    concrete documented model deprecation event in the corpus and provides
    specific evidence for the operational risk of building on external model
    providers without deprecation protections.
  - **Governance clause in compute contracts**: Musk's "reclaim compute" clause
    with unilateral harm-definition authority is the first documented example in
    the corpus of content-conditional infrastructure supply — where compute
    access depends on the provider's ongoing approval of the customer's
    AI behavior.
  - **Named data center expert critique**: Andy Masley's direct "would not
    run computing there" statement is the first named domain expert
    infrastructure critique in the corpus.
  - **Environmental violation specifics**: Unpermitted gas turbines classified
    as "temporary" to avoid Clean Air Act requirements — more specific than
    the general "bad environmental record" mention in the May 6 live blog.
  - **Hospital admissions link**: The air quality / hospital admissions claim
    is the first public-health-framed infrastructure concern in the corpus.

## Guide Impact

- **Chapter 03 (Economics, Governance, Supply Chain)**: This source provides
  the primary evidence base for a new section on compute vendor supply chain
  risk. Currently no chapter covers the pattern where AI provider compute
  dependencies become transitive risks for practitioners. Recommend adding:
  (1) the compute-constrained provider pattern (Anthropic's situation),
  (2) the governance clause risk (Musk's reclaim right as a case study),
  (3) the model deprecation timeline pattern (8 Grok models, 2-week notice)
  as operational evidence, and (4) the practitioner mitigation heuristic:
  evaluate your AI provider's compute dependencies and governance arrangements
  as part of vendor selection.

- **Chapter 04 (Infrastructure & Operations)**: Add the environmental and
  reputational risk dimension to infrastructure selection guidance. Currently
  no chapter covers how to evaluate the AI data center choices your providers
  are making on your behalf. Recommend citing Willison's summary of the
  Colossus record as evidence that practitioners with ESG or reputational
  commitments need to understand their AI providers' infrastructure choices,
  not just their APIs.

- **Chapter 03 (Model Deprecation Risk)**: The Grok deprecation event (Claim
  10, 11) is concrete evidence for a model deprecation risk section that the
  corpus currently lacks. Recommend framing: when building production systems
  on external model APIs, deprecation with short notice and no migration path
  is a real operational risk. Mitigation patterns: model abstraction layers,
  multi-provider fallbacks, and negotiated deprecation notice periods in SLAs.

- **Chapter 02 (Vendor Selection Criteria)**: Add governance clause inspection
  as a vendor selection criterion. The Musk reclaim clause (Claim 8) is the
  first documented case in the corpus of a compute provider attaching
  behavioral conditions to infrastructure access. Practitioners should ask:
  what conditions does my AI provider's infrastructure supplier attach to
  compute access, and what happens to my service if those conditions are
  exercised?

## Extraction Notes

- Source is a standalone post published the day after the Code w/ Claude event
  live blog. It is shorter and more analytical than the live blog. No sub-pages
  were followed; the post is self-contained.
- WebFetch processed the source and returned summaries on first pass. Quotes
  were extracted via targeted follow-up prompts asking for verbatim passages.
  All quotes in this note were confirmed across at least two WebFetch calls
  requesting verbatim text. The environmental violation quote (Claim 3), the
  hospital admissions quote (Claim 4), the political risk quote (Claim 5),
  Andy Masley's quote (Claim 6), Musk's meeting quote (Claim 7), the reclaim
  clause quote (Claim 8), and the supply chain risk quote (Claim 9) were each
  confirmed by direct verbatim extraction requests.
- The political risk quote (Claim 5) contains an ellipsis (...) representing
  text in the original source between "red-hot political issue" and "signing
  up" — this is an elision, not a splice of non-adjacent sentences. The
  two fragments are from the same passage.
- The developer complaint (Claim 11) is a quoted tweet or social media post
  embedded in Willison's article, not Willison's own words.
- Andy Masley's quote (Claim 6) is quoted by Willison from a third-party source
  (likely a tweet or post by Masley). Willison is the source of record for
  our corpus; Masley's original post is not directly cited.
- No contradictions were found with existing source notes. The supply chain
  risk pattern and model deprecation event are new territory in the corpus.
- Confidence overall is set to `emerging`: the specific environmental claims
  and hospital admissions report are cited by Willison but not attributed to
  named primary sources in this article; the governance clause and deprecation
  event are directly documented (settled on those specific facts); the supply
  chain risk framing is Willison's editorial judgment (anecdotal).
