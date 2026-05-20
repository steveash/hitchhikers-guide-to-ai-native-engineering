---
source_url: https://simonwillison.net/2026/May/12/mitchell-hashimoto/
source_type: blog-post
title: "Quoting Mitchell Hashimoto"
author: Mitchell Hashimoto (quoted by Simon Willison)
date_published: 2026-05-12
date_extracted: 2026-05-20
last_checked: 2026-05-20
status: current
confidence_overall: anecdotal
issue: "#816"
---

# Quoting Mitchell Hashimoto: TDM Risk Aversion and Analyst-Driven Adoption

> Mitchell Hashimoto explains why 90% of technical decision makers are motivated
> primarily by job security, leading them to follow analyst consensus (Gartner,
> McKinsey) rather than technical merit — a dynamic that directly shapes how
> enterprise AI tooling categories emerge, get funded, and become mandatory.

## Source Context

- **Type**: blog-post (Simon Willison link-blog quotation, May 12, 2026; a single
  blockquote attributed to a Lobsters discussion about Redis homepage design, with
  Willison's only commentary being the sourcing attribution: "a conversation about
  the design of the Redis homepage." Tags on the Willison post: marketing, redis,
  mitchell-hashimoto. The Lobsters discussion thread was followed as a substantive
  linked source per MINER.md §1 — Hashimoto's full comment there provides the
  credentials claim and additional TDM-dynamics arguments not included in the
  Willison excerpt.)
- **Author credibility**: Mitchell Hashimoto is the co-founder and former CEO of
  HashiCorp (Terraform, Vagrant, Vault), which he grew from an open-source project
  to a company with hundreds of millions in revenue, an IPO, and ultimately a
  multi-billion dollar acquisition by IBM. He also executed HashiCorp's 2023 license
  change away from open source. He writes from direct, rare first-person experience
  on the OSS-to-commercial transition, enterprise software pricing, and TDM behavior
  at scale. Simon Willison is the creator of Django and one of the most widely-cited
  independent AI tooling commentators; his selection of this quote for his curated
  link-blog is itself a relevance signal. The Lobsters discussion is about a blog
  post by Charles Leifer titled "Redis and the Cost of Ambition," critiquing Redis
  Inc.'s strategic shift toward enterprise/AI positioning.
- **Scope**: One excerpt from Hashimoto's longer Lobsters comment, surfaced by Simon
  Willison on his link-blog. The Willison page presents a blockquote without
  additional editorial commentary beyond the source attribution. The context is
  enterprise database software (Redis), not AI tooling specifically — but the
  structural argument about TDM behavior applies directly to enterprise AI tool
  procurement. Does NOT cover: empirical data, controlled studies, AI tooling
  specifics, or any claim that is purely Redis-context-specific.

## Extracted Claims

### Claim 1: Most technical decision makers are motivated primarily by not getting fired, not by technical merit

- **Evidence**: Hashimoto's first-person observation from his experience building
  open source to scale, starting HashiCorp, and growing it through IPO and
  acquisition. The "90%" figure is Hashimoto's estimate, not a survey result; the
  framing is explicit and stated as a practitioner generalization.
- **Confidence**: anecdotal (one practitioner's synthesis from his career; no
  survey or empirical basis; but rare authority — few people have sat on both the
  OSS and commercial enterprise sides at this scale)
- **Quote**: "The thing about 90% of TDMs is that they're motivated primarily by
  NOT GETTING FIRED. These aren't people who browser Lobsters or push to GH on
  the weekend. These are people that work 9 to 5, get paid, go home, and NEVER
  THINK ABOUT WORK AGAIN."
  — Mitchell Hashimoto, as quoted on simonwillison.net/2026/May/12/mitchell-hashimoto/
- **Our assessment**: This is the load-bearing framing for all the claims that
  follow. Hashimoto distinguishes between practitioners (who browse Lobsters,
  push to GitHub on weekends) and TDMs (who optimize for not being blamed for
  bad decisions). If this framing is correct, technical arguments for novel
  tooling will systematically fail to persuade TDMs — because TDMs are not
  evaluating technical merit; they are evaluating personal risk exposure. The
  "browser" typo (should be "browse") is preserved from the source.

### Claim 2: TDMs follow analyst consensus as a proxy for defensible technology decisions, not independent technical evaluation

- **Evidence**: Hashimoto's direct explanation of TDM behavior, immediately
  following the risk-aversion claim. He names specific analyst firms (Gartner,
  McKinsey) as the validation mechanism.
- **Confidence**: anecdotal (first-person practitioner observation; consistent
  with widely-observed enterprise procurement patterns but not independently
  verified by survey data)
- **Quote**: "So to achieve all that, they follow secular trends supported by
  analysts and broad public sentiment."
  — Mitchell Hashimoto, as quoted on simonwillison.net/2026/May/12/mitchell-hashimoto/
- **Our assessment**: "Secular trends" is the operative phrase. A TDM does not
  need to understand Gartner's reasoning — they need to be able to say "Gartner
  says this is important" to their manager or board. The analyst citation is a
  liability shield, not a technical evaluation. This explains why AI adoption in
  enterprises often follows the pattern: analyst covers it → analyst puts it on
  the hype cycle → executives mandate evaluation → procurement. The quality of
  the analyst's reasoning is less relevant than the analyst's brand authority as
  a defensibility signal.

### Claim 3: Analyst-validated buzzwords create procurement-defensible product categories, enabling purchase decisions based on label-matching rather than technical evaluation

- **Evidence**: Hashimoto provides a concrete example of the mechanism: a Gartner
  "AI strategy" finding + McKinsey "context" recommendation → "Context Engine for
  AI Apps" becomes a purchasable product category, regardless of what it actually
  does.
- **Confidence**: anecdotal (one practitioner's account; the example is
  illustrative, not a documented case study; but the mechanism is consistent with
  how enterprise software marketing actually operates)
- **Quote**: "Oh, Gartner said that 'AI strategy' is most important? McKinsey said
  'context' needs to be managed? Well, 'Context Engine for AI Apps' is going to be
  defensible. Buy it."
  — Mitchell Hashimoto, as quoted on simonwillison.net/2026/May/12/mitchell-hashimoto/
- **Our assessment**: The "Context Engine for AI Apps" example is specifically
  relevant to this corpus — "context" and "context engineering" are central to
  guide Chapter 04. Hashimoto's observation predicts that whatever vocabulary
  analysts attach to AI capability management will become a self-fulfilling
  procurement category label. This is not a technical prediction; it is a
  sociological one. For practitioners: the vocabulary that analysts validate for
  AI tooling shapes which vendor pitches will succeed, which use cases get funded,
  and which patterns get mandated — independent of whether the underlying
  technology is the best available approach.

### Claim 4: TDMs actively want to pay for software as a mechanism for transferring liability

- **Evidence**: Hashimoto's explanation of TDM commercial software preferences,
  from his Lobsters comment (the full comment, not the Willison excerpt).
- **Confidence**: anecdotal (first-person practitioner observation from the
  Lobsters source)
- **Quote**: "TDMs absolutely do NOT want to be liable for technical decisions,
  they actually WANT to pay for software."
  — Mitchell Hashimoto, lobste.rs/s/oznirn/redis_cost_ambition#c_dzrja0
- **Our assessment**: This inverts the common practitioner assumption that
  open-source is the obvious choice (free + technically superior). From the TDM
  perspective, "free" can be worse than "paid" because it removes the contractual
  liability transfer. When TDMs pay a vendor, they can say "we used the vendor's
  recommended configuration and it failed — the vendor is liable." When they use
  free/open-source, there is no one to blame. The willingness to pay is not about
  ROI; it is about blame attribution. For the guide: this explains why some
  enterprises will pay for enterprise AI tooling even when free alternatives are
  technically equivalent or superior.

### Claim 5: The switching cost to adopt new technology is fundamentally higher than expanding existing vendor relationships

- **Evidence**: Hashimoto's procurement dynamics explanation, from the Lobsters
  comment.
- **Confidence**: anecdotal (Hashimoto's observation from his commercial software
  experience; widely acknowledged in enterprise sales but not empirically measured
  here)
- **Quote**: "The cost (cognitive, time, risk, money, etc.) of adopting a new thing
  is significantly higher than expanding an old thing."
  — Mitchell Hashimoto, lobste.rs/s/oznirn/redis_cost_ambition#c_dzrja0
- **Our assessment**: Hashimoto enumerates the switching cost components explicitly:
  cognitive (learning new API, new vendor), time (evaluation, procurement, training),
  risk (the new thing might fail), and money (procurement process overhead). Each of
  these is a separate TDM exposure. For AI tooling adoption: this explains why
  enterprises often prefer to add AI capabilities to existing tools (GitHub Copilot
  inside an existing GitHub Enterprise contract) over adopting best-in-class
  specialist tools (Cursor, Claude Code) that require a new procurement relationship.
  The incumbency advantage in enterprise AI adoption is structural, not technical.

### Claim 6: Customers routinely choose technically inferior options for non-technical reasons

- **Evidence**: Hashimoto's generalization about enterprise technology choices,
  from the Lobsters comment.
- **Confidence**: anecdotal (one practitioner's observation; consistent with
  enterprise technology adoption history but not an empirical study)
- **Quote**: "Customers choose shittier options all the time for non-technical
  reasons."
  — Mitchell Hashimoto, lobste.rs/s/oznirn/redis_cost_ambition#c_dzrja0
- **Our assessment**: This is the bluntest statement in Hashimoto's comment and
  the most useful for calibrating expectations. Practitioners who assume that the
  technically superior AI tool will win enterprise adoption are likely to be
  surprised. The non-technical reasons Hashimoto implies include: existing vendor
  relationship (Claim 5), analyst endorsement (Claims 2–3), procurement simplicity
  (Claim 4), and organizational risk tolerance (Claim 1). For the guide: the
  message for practitioners advocating for AI-native patterns in enterprise contexts
  is that the technical merits argument alone is insufficient — the organizational
  incentives argument must also be addressed.

### Claim 7: Hashimoto speaks from rare practitioner authority on the business dynamics of open source commercialization — credentials that make his TDM framing unusually credible

- **Evidence**: Hashimoto's self-disclosure in the Lobsters comment, listing his
  career trajectory. HashiCorp's history is independently verifiable.
- **Confidence**: settled (the credentials are public record; the IBM acquisition
  price and HashiCorp's IPO are documented)
- **Quote**: "I'm probably one of the few people around here -- at least publicly
  posting -- that has sat on the side of building open source to some large-ish
  scale, starting a company, growing that company to hundreds of millions in
  revenue, IPO, and then a multi-billion dollar sale."
  — Mitchell Hashimoto, lobste.rs/s/oznirn/redis_cost_ambition#c_dzrja0
- **Our assessment**: The credentials claim is relevant because it determines how
  much weight to assign the other claims. Hashimoto's TDM observations are not
  armchair theorizing — they are first-person observations from someone who spent
  years navigating both the practitioner and the enterprise-sales sides of a
  major open-source-to-commercial transition. Few people in public tech discourse
  have simultaneously operated at the technical depth (Terraform) and the business
  depth (multi-billion dollar exit) that make his TDM framing credible from both
  sides of the table.

## Concrete Artifacts

### The Willison Blockquote (verbatim from https://simonwillison.net/2026/May/12/mitchell-hashimoto/)

```
Tags: marketing, redis, mitchell-hashimoto
Published: 12th May 2026
Source attribution (Willison's words): "a conversation about the design of the Redis homepage"
Linked source: https://lobste.rs/s/oznirn/redis_cost_ambition#c_dzrja0

[Blockquote, verbatim:]

"The thing about 90% of TDMs is that they're motivated primarily by NOT GETTING
FIRED. These aren't people who browser Lobsters or push to GH on the weekend.
These are people that work 9 to 5, get paid, go home, and NEVER THINK ABOUT WORK
AGAIN. So to achieve all that, they follow secular trends supported by analysts
and broad public sentiment. Oh, Gartner said that 'AI strategy' is most important?
McKinsey said 'context' needs to be managed? Well, 'Context Engine for AI Apps'
is going to be defensible. Buy it."

— Mitchell Hashimoto
```

### Hashimoto's TDM Procurement Model (synthesized from Willison page + Lobsters source)

```
Source: Mitchell Hashimoto, lobste.rs/s/oznirn/redis_cost_ambition#c_dzrja0
        (linked from simonwillison.net/2026/May/12/mitchell-hashimoto/)

DECISION DRIVER: NOT GETTING FIRED
  Primary motivation: personal risk avoidance, not technical optimization
  Decision heuristic: "what can I defend to my manager / board?"

VALIDATION MECHANISM: ANALYST CONSENSUS
  Gartner, McKinsey → defines what categories are "important"
  Analyst-endorsed label → defensible procurement decision
  Example: "Context Engine for AI Apps" (AI-era analog of "Enterprise Service Bus")

PAYMENT AS LIABILITY TRANSFER:
  Free/open-source = no one to blame if it fails
  Paid vendor = contract → vendor accountability → reduced personal exposure
  "TDMs actually WANT to pay for software"

SWITCHING COST STRUCTURE:
  Costs of adopting new technology: cognitive + time + risk + money
  All significantly higher than expanding existing vendor relationship
  → Incumbency advantage is structural, not technical

OUTCOME: Technical merit is not the primary adoption driver
  "Customers choose shittier options all the time for non-technical reasons."
```

## Cross-References

- **Corroborates**:
  - **blog-bvp-shopify-ai-playbook.md** Claim 7 ("Performance reviews evaluate
    'AI-reflexive' behavior"): Shopify's mandate that engineers demonstrate
    AI-reflexive behavior in performance reviews is an example of TDM-level
    organizational pressure to adopt AI tooling — consistent with Hashimoto's
    model where TDMs enforce adoption once the analyst consensus is established.
    The guide should note this: Shopify's AI performance review mandate is the
    TDM playbook in action at a technically sophisticated company.
  - **blog-cursor-paypal-enterprise-adoption.md** Claim 1 (PayPal adoption
    starting with high-impact teams, then spreading organically): PayPal's
    organic practitioner-spread strategy operates at the rollout level, not
    the procurement level. The TDM decision to acquire Cursor licenses for 8,000
    engineers preceded the organic rollout Hashimoto describes. These two levels
    are compatible: TDM decides to buy (analyst-endorsed, liability-transferred);
    practitioners decide how to roll out. PayPal's case shows the practitioner
    layer operating autonomously after the TDM gate is cleared.

- **Contradicts**: None filed. No existing corpus note makes claims that
  directly contradict Hashimoto's structural account of TDM behavior. The
  Shopify case (Farhan Thawar, a technically sophisticated VP Eng making
  deliberate tool choices) could superficially appear to contradict the
  "TDMs don't think about technical merit" framing — but Thawar's behavior
  is consistent with the 10% exception Hashimoto acknowledges, and Shopify's
  AI adoption is self-described as deliberate engineering leadership, not
  analyst-driven procurement.

- **Extends**:
  - **blog-thebatch-ng-aiteam-structure.md** Claim 1 (Andrew Ng on engineers
    playing product management, design, and marketing roles): Ng describes the
    practitioner-side consequence of AI-native engineering (role boundary blur
    for practitioners). Hashimoto's framing provides the organizational context
    for why this matters: if TDMs are making purchasing decisions based on
    analyst consensus, practitioners who understand the TDM/practitioner
    distinction can translate their technical work into analyst-legible language
    to navigate procurement more effectively.
  - **blog-simonwillison-james-shore-maintenance-costs.md** Claim 1 (AI coding
    agents only produce net benefit if maintenance costs decrease proportionally):
    Shore's maintenance cost framework and Hashimoto's TDM framing are
    complementary at the organizational level. Shore says: technical merit
    requires maintenance cost reduction to be real. Hashimoto says: but TDMs
    won't evaluate technical merit — they'll evaluate analyst endorsement and
    liability transfer. Together they describe an organizational trap: even if
    practitioners understand Shore's ROI criterion, TDMs may adopt AI tooling
    anyway because of analyst pressure, and the maintenance cost burden will
    accumulate regardless.

- **Novel**:
  - **The practitioner vs. TDM framing applied to AI tooling adoption**: No
    existing corpus source explicitly models the organizational dynamics of
    enterprise AI adoption from the perspective of TDM incentive structures.
    The BVP/Shopify note covers operational decisions; The Batch covers team
    structure; neither explains *why* enterprises adopt AI tools the way they
    do. Hashimoto's model is the first in the corpus that provides a causal
    mechanism: TDM risk aversion → analyst dependence → category-label-driven
    procurement → practitioners inherit the mandated tooling.
  - **"Context Engine for AI Apps" as the AI-era enterprise buzzword exemplar**:
    No other corpus source identifies a specific AI-era analyst-validated category
    label and traces its adoption logic. This is directly relevant to Chapter 04
    (Context Engineering) — the vocabulary of "context management" may be
    succeeding partly because it maps onto analyst-recognized terminology, not
    solely because it is the technically correct framing.
  - **Payment as liability transfer (TDMs want to pay)**: No existing corpus
    source explains why TDMs prefer paid commercial AI tooling over technically
    equivalent free alternatives. Hashimoto's liability-transfer framing is a
    novel addition to the corpus's account of enterprise AI adoption dynamics.

## Guide Impact

- **Chapter 05 (Team Adoption — Organizational Dynamics)**: This is the most
  important addition this source makes. Chapter 05 currently documents what
  organizations do when adopting AI tooling (Shopify, PayPal, NAB) but not
  *why* adoption decisions get made the way they do. Hashimoto's TDM model
  supplies the missing causal mechanism. Specific recommendation: add a section
  on "How AI tooling gets purchased in enterprises" that distinguishes the TDM
  procurement decision (analyst-driven, liability-oriented) from the practitioner
  adoption decision (technically-evaluated, workflow-driven). Practitioners
  advocating for AI-native patterns need to speak both languages: technical merit
  for peers, analyst-endorsed framing for TDM approval chains. Cite this source
  and `blog-bvp-shopify-ai-playbook.md` Claim 7 together as the organizational
  case for that distinction.

- **Chapter 05 (Team Adoption — Why Technically Inferior Tools Win)**: Add a
  short paragraph or callout acknowledging that enterprise AI tooling adoption
  will not always select the technically best tool. Hashimoto's "customers choose
  shittier options all the time for non-technical reasons" is the bluntest
  statement in the corpus of this dynamic. Practitioners who understand this can
  stop being surprised when their enterprise mandates Copilot over a technically
  superior alternative, and instead focus on improving the experience within
  whatever tool the TDM procurement process delivers.

- **Chapter 04 (Context Engineering — Vocabulary and Analyst Validation)**: The
  "Context Engine for AI Apps" example is directly relevant. Chapter 04 should
  note that "context engineering" as a vocabulary choice is not purely a
  technical description — it is also an analyst-legible label. The fact that
  McKinsey-level vocabulary like "context needs to be managed" maps onto what
  practitioners call context engineering is not a coincidence; it is the adoption
  mechanism Hashimoto describes. Teams building context engineering infrastructure
  can frame their work in analyst-legible terms to navigate enterprise procurement.

- **Chapter 01 (Daily Workflows — Advocating for AI-Native Approaches)**: Add a
  brief note on the organizational advocacy challenge for practitioners. Technical
  arguments alone are insufficient to secure TDM buy-in for novel AI-native
  patterns. Practitioners need a secondary argument that addresses TDM risk
  exposure: what analyst endorsements exist, what vendors support this pattern,
  what liability exists if it fails. Hashimoto's model predicts that without
  these arguments, technically superior approaches will lose to analyst-endorsed
  alternatives regardless of merit.

## Extraction Notes

- **Thin Willison page; Lobsters comment is the substantive source**: The Willison
  page is a minimal link-blog post — a single blockquote with a one-sentence
  attribution and no additional Willison commentary. The Lobsters page was
  followed as the substantive linked source, per MINER.md §1. Claims 1–3 quote
  the Willison page (the canonical source URL). Claims 4–7 quote the Lobsters
  comment directly and are attributed to that URL.
- **Source context is Redis, not AI**: Hashimoto's comment is explicitly about
  Redis's marketing strategy and enterprise database procurement, not about AI
  tooling. The guide relevance is structural (TDM behavior is the same regardless
  of technology category) and specific (the "Context Engine for AI Apps" example
  applies the same logic to AI).
- **Three Prospector triage comments**: Three separate triage assessments were
  submitted (pipeline artifact). Novelty ratings varied: "medium" (first, third
  comments), "high" (second comment). The second assessment identified the highest
  novelty in "the sociology of technical decision-making" — consistent with the
  novel cross-reference claims identified above.
- **"browser" is a typo in the source**: The word "browser" in "people who browser
  Lobsters" is a Hashimoto typo for "browse." Preserved verbatim per MINER.md §2a.
- **WebFetch returned summaries, not full verbatim text**: Multiple attempts were
  needed to recover verbatim quotes. The Willison blockquote was recovered in full
  from WebFetch on the fourth attempt; the Lobsters quotes were recovered via
  targeted single-paragraph requests. Quotes attributed to the Willison page were
  confirmed verbatim; Lobsters quotes were confirmed via targeted extraction of
  specific paragraphs with exact capitalization and punctuation matching Hashimoto's
  emphatic style (ALL CAPS on stressed terms). Treat Lobsters quotes as high-
  confidence verbatim but not cross-checked against raw HTML.
- **No sub-pages followed beyond Lobsters**: The Lobsters thread has many other
  comments; only Hashimoto's comment was extracted. The Charles Leifer Redis post
  linked in the Lobsters thread title was not followed — the guide-relevant content
  is entirely in Hashimoto's comment, not in Leifer's Redis critique.
