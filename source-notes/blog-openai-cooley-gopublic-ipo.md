---
source_url: https://openai.com/index/cooley-gopublic
source_type: blog-post
title: "How Cooley is accelerating IPO work with ChatGPT"
author: OpenAI (customer-story vertical; quoted subjects David Wang — Chief Innovation Officer, and Dave Peinsipp — Partner and Co-Chair, Global Capital Markets, both Cooley LLP)
date_published: 2026-09-17
date_extracted: 2026-09-28
last_checked: 2026-09-28
status: current
confidence_overall: anecdotal
issue: "#3766"
---

# How Cooley is accelerating IPO work with ChatGPT

> An OpenAI customer-story case study describing GO Public, a proprietary
> agentic AI offering that international law firm Cooley built on top of
> ChatGPT Work to accelerate IPO preparation — shifting the traditional
> starting point for deal work from a precedent-company template to the
> client itself, and reframing the goal as "speed to quality" (reaching a
> strong first draft sooner) rather than raw task-completion speed. The
> article contains zero quantified metrics — no time-savings figure, no
> adoption percentage, no deal-count acceleration number — making it one of
> the thinnest-evidenced case studies of its kind in the corpus.

## Source Context

- **Type**: blog-post (OpenAI `openai.com/index/` customer-story vertical;
  a short (~470-word) case study with three section headers, two named
  quoted executives, and two pull quotes; no metrics box, no benchmark
  table, no code or architecture diagram). Published September 17, 2026;
  auto-discovered via the `openai-news` trusted RSS feed per the source
  issue's auto-filed body.
- **Author credibility**: House-authored OpenAI customer-story copy built
  around quotes from two named Cooley executives: David Wang (Chief
  Innovation Officer) and Dave Peinsipp (partner and co-chair, global
  capital markets group). Cooley is a real, named international law firm
  with a verifiable public track record in IPO work. This is a vendor case
  study — OpenAI selected the customer and the quotes, and frames the
  narrative promotionally — not an independent report with disclosed
  methodology. Unlike most OpenAI customer case studies already in the
  corpus (e.g. Gilbert + Tobin's 87% active-seat figure, Legora's 41
  documents / nearly-40%-BAR-improvement figures), this article contains
  **no quantified metric of any kind** tied to GO Public's performance —
  no before/after time figure, no adoption percentage, no deal-count or
  revenue figure attributable to the tool. The only numbers in the source
  are firm-scale background stats (180 deals, $51.5 billion in 2025 deal
  volume) that describe Cooley's business generally, not GO Public's effect
  on it.
- **Scope**: Covers what GO Public is (a proprietary agentic harness built
  on ChatGPT Work), how it changes the starting point for IPO preparation
  (client-first rather than precedent-first), how it was built (legal
  engineers, innovation counsel, and practitioners translating firm
  know-how into the harness, in partnership with OpenAI), the human-review
  structure of the harness, and two named executives' framing of the
  "speed to quality" value proposition and its extension beyond IPOs to
  capital markets work more broadly. Does NOT cover: any quantified
  performance metric, the harness's technical architecture (models used,
  context sources, agent count, tool integrations), a specific IPO
  transaction where GO Public was used, client-side or associate-level
  testimony (both named speakers are senior executives — CIO and
  partner/co-chair — not associates or clients who used the tool
  first-hand), a rollout timeline or adoption figure within the firm, or
  pricing/commercial terms of the OpenAI partnership.

## Extracted Claims

### Claim 1: Cooley is a top-tier IPO law firm — it advised on 180 deals globally in 2025 totaling more than $51.5 billion in deal volume, and has advised on more venture-backed IPOs than any other firm over the past 20-plus years
- **Evidence**: Firm-background statement opening the article, establishing Cooley's credibility as the case-study subject.
- **Confidence**: anecdotal (self-reported firm-scale figures with no independent audit or citation to a league-table source)
- **Quote**: "In 2025, the firm advised on 180 deals globally, totaling more than $51.5 billion in deal volume. Cooley has a decade-long track record at the top of the US issuer-side IPO market and has advised on more venture-backed IPOs than any other firm over the past 20-plus years."
- **Our assessment**: This is scale/credibility framing for the case study, not a claim about GO Public's effect — none of these figures are attributed to AI adoption; they describe Cooley's pre-existing market position. Should be cited only as background context establishing that the customer is a credible, high-volume practice, not as evidence the tool works.

### Claim 2: GO Public is a proprietary AI product offering, built on ChatGPT Work, whose agentic harness analyzes information so lawyers can review and validate the work, producing a tailored starting point for an IPO
- **Evidence**: Direct description of the product in the article's opening framing.
- **Confidence**: anecdotal (first-party product description with no technical detail on the harness's architecture)
- **Quote**: "Cooley developed GO Public, a proprietary AI product offering built on ChatGPT Work. Its agentic harness analyzes information so lawyers can review and validate the work. The workflow comes together into a tailored starting point for an IPO."
- **Our assessment**: This is a law firm building its own proprietary agentic product on top of a general-purpose enterprise AI platform (ChatGPT Work), rather than buying a separately vetted domain-specific legal-AI platform. This is a build-vs-buy contrast worth flagging against `blog-openai-gilbert-tobin-legal-ai-governance.md` Claim 7, where Gilbert + Tobin instead uses ChatGPT only for "the operational side" of lawyers' work while routing legal-specific workflows through a separately vetted third-party platform, Harvey. Cooley's GO Public is the opposite strategic choice for the same underlying need (domain-specific AI for legal-substance work): build a proprietary harness on the general-purpose platform rather than buy a vetted vertical product. See Cross-References → Extends.

### Claim 3: Before GO Public, Cooley teams typically began IPO work with a precedent from a comparable company and adapted it; GO Public instead begins with the client itself, combining client-provided information, relevant public sources, and curated precedents into a more tailored starting point for lawyer review
- **Evidence**: Direct narrative description contrasting the old and new starting points for deal preparation.
- **Confidence**: anecdotal (a described workflow shift with no example transaction, no time comparison, and no description of how "curated precedents" are selected or weighted)
- **Quote**: "Before GO Public, teams often began with a precedent from a comparable company and adapted it to fit the client's circumstances. GO Public allows Cooley to begin with the client itself, bringing together the information provided, relevant public sources, and carefully curated precedents to create a more tailored starting point for lawyer review."
- **Our assessment**: This is the article's clearest concrete mechanism claim — a described shift from a "closest analogous precedent, adapted" starting point to a "client-first, precedent-informed" starting point. It is structurally similar to a retrieval-augmented drafting pattern (pull relevant context, synthesize a tailored first draft) but the source gives no detail on how "the information provided" by the client is ingested, what "relevant public sources" means concretely, or how conflicts between curated precedents are resolved — this is a qualitative workflow description, not a technical one.

### Claim 4: Cooley's legal engineers, innovation counsel, and practitioners worked together to translate the firm's capital markets experience into GO Public's proprietary agentic system, partnering closely with OpenAI to combine subject-matter expertise and AI engineering knowledge
- **Evidence**: Direct narrative description of the build process, paired with a supporting quote from David Wang.
- **Confidence**: anecdotal (a described cross-functional build process with no team size, timeline, or detail on the specific division of labor between Cooley's legal engineers and OpenAI's engineers)
- **Quote**: "Cooley's legal engineers, innovation counsel, and practitioners worked together to translate the firm's capital markets experience into a proprietary agentic system. ... 'With GO Public and the agentic harness that we built using OpenAI's technology, we were able to bring this forward into the AI era,' Wang says. ... Cooley partners closely with OpenAI to combine subject-matter expertise and AI engineering knowledge to ensure the right processes produce the right outcomes."
- **Our assessment**: This names a specific internal role — "legal engineer" — already documented in the corpus for other firms (e.g. Percevale Perks, "Legal Engineer, Legora," in `blog-openai-legora-financial-statement-tie-out.md` Claim 2) as the practitioner-technologist hybrid role responsible for translating domain expertise into an AI workflow. Here the role appears at a law firm building its own tool (Cooley) rather than at a vendor selling a platform to firms (Legora) — a third instance in the corpus of "legal engineer" as a named, recurring role title for this kind of work, this time inside the customer rather than the vendor. The close-partnership framing with OpenAI ("Cooley partners closely with OpenAI to combine subject-matter expertise and AI engineering knowledge") suggests deeper co-engineering than a typical enterprise-tier deployment, but the article gives no detail on what that partnership consisted of concretely (co-located engineers, a dedicated OpenAI account team, model fine-tuning, etc.).

### Claim 5: Information curated from previous analyses provides "baked-in know-how"; the harness lays out which steps agents can perform automatically, where lawyers must review or validate the work, and how it all comes together
- **Evidence**: Direct narrative description of the harness's controlled-workflow structure.
- **Confidence**: anecdotal (a described control structure with no example of a specific automated step versus a specific human-review step, and no detail on how "baked-in know-how" is captured, stored, or updated over time)
- **Quote**: "The harness provides a controlled workflow for agents that lays out which steps agents can perform automatically, where lawyers must review or validate the work, and how it all comes together. Information curated from previous analyses provides what Wang calls 'baked-in know-how.'"
- **Our assessment**: This is a human-in-the-loop harness design — a fixed division between agent-automated steps and lawyer-review steps — in the same structural family as the AML/KYC compliance workflow in `blog-openai-gilbert-tobin-legal-ai-governance.md` Claim 11 ("completes research and processing steps, then produces a report for human review and sign-off") and the tie-out workflow in `blog-openai-legora-financial-statement-tie-out.md` Claim 5 ("The Agent handles the exhaustive comparison, while the expert remains responsible for the judgment call on each result"). All three sources describe the same shape: an agent handles breadth/exhaustiveness, a named human step handles judgment, and the boundary between the two is fixed rather than described as narrowing over time. Cooley's contribution to this pattern is the phrase "baked-in know-how" for the curated-precedent-and-analysis layer feeding the harness — a specific naming of the institutional-knowledge-encoding mechanism that the other two sources describe without naming.

### Claim 6: The goal of GO Public is "speed to quality," not raw task-completion speed — reaching a strong starting point sooner so lawyers can spend more time applying judgment, challenging the disclosure, and thinking strategically about what matters most to the company
- **Evidence**: Direct attributed quote from Dave Peinsipp, framing the value proposition explicitly against a "just do the same work faster" alternative.
- **Confidence**: anecdotal (a stated design philosophy from a senior partner, not a measured outcome)
- **Quote**: "'That's what we mean by speed to quality,' Peinsipp says. 'The point isn't simply to do the same work faster. It's to get to a strong starting point sooner, so our lawyers can spend more time applying judgment, challenging the disclosure and thinking strategically about the issues that matter most to the company.'"
- **Our assessment**: "Speed to quality" is a specific, quotable reframing of the "concentrate human effort on the highest-value surface areas" pattern already present in this same article (Claim 7 below) and elsewhere in the corpus's professional-services case studies — the explicit rejection of "same work, faster" as the goal is a sharper articulation than most case studies offer, which more often report a bare time-savings multiplier without addressing what the freed-up time is redirected toward, or whether speed itself was ever the intended benefit. This is a directly reusable, quotable framing device for the guide.

### Claim 7: Bringing intelligence to a large array of information that previously had to be manually sorted lets Cooley "really concentrate the human effort and expertise on the highest value surface areas"
- **Evidence**: Direct attributed quote from David Wang, describing the mechanism behind the "speed to quality" outcome named in Claim 6.
- **Confidence**: anecdotal (a stated causal mechanism from a senior executive, not demonstrated with a specific before/after example)
- **Quote**: "'The amazing thing about integrating ChatGPT Work into GO Public is that it brings intelligence to this very large array of information that had to be manually sorted before,' Wang says. 'Once you do that first cut, you're able to really concentrate the human effort and expertise on the highest value surface areas.'"
- **Our assessment**: "Once you do that first cut" names a specific mechanism — an AI-performed first pass over a large information set — that precedes the human-judgment step described in Claim 5's harness structure and Claim 6's "speed to quality" framing. This is the same "AI does the exhaustive/broad pass, human applies judgment to the narrowed set" mechanism documented in Claim 5's cross-references (Gilbert + Tobin's AML/KYC workflow, Legora's tie-out agent), stated here in the specific vocabulary of "first cut" and "highest value surface areas" rather than "exhaustive comparison" or "research and processing steps."

### Claim 8: For management teams, GO Public's benefit extends beyond the legal work itself — it gives valuable time back to executives who are also running fast-moving businesses, since IPO preparation competes for their attention
- **Evidence**: Direct narrative statement plus a supporting pull quote from Dave Peinsipp.
- **Confidence**: anecdotal (a stated benefit to a third party — client executives — not the primary subject of the case study, with no example or figure attached)
- **Quote**: "IPO preparation competes for the attention of executives who are also running fast-moving businesses." ... "ChatGPT Work allows us to move more quickly through intensive preparation and give valuable time back to management. We want their attention focused where only they can add value — on the business, the story and the decisions that will ultimately shape the offering." — Dave Peinsipp, Partner and Co-Chair, Global Capital Markets
- **Our assessment**: This extends the "speed to quality" framing (Claim 6) from the law firm's own lawyers to the client's management team — the stated beneficiary of freed-up time is not only Cooley's own staff but also the client executives who would otherwise be consumed by IPO logistics. No source in the corpus reviewed for this note documents a professional-services AI tool whose value proposition explicitly targets the *client's* executive attention as a named beneficiary, rather than only the professional-services firm's own staff efficiency — see Cross-References → Novel.

### Claim 9: The legal industry has traditionally been "relatively change-averse," but AI gives Cooley an opportunity to rethink how capital markets work gets done while preserving the professional judgment and accountability clients depend on
- **Evidence**: Direct attributed quote from David Wang under the "Transforming an industry" section header, paired with narrative framing about professional duties.
- **Confidence**: anecdotal (a characterization of an entire industry by one executive at one firm, and a stated intention to preserve judgment/accountability with no independent verification of how that preservation is enforced beyond the review-and-validate harness structure described in Claim 5)
- **Quote**: "'Traditionally, the legal industry has been relatively change-averse,' Wang says." ... "'As attorneys, we have professional duties and obligations to make sure that the best, most legally defensible outcome occurs for our clients, and that just takes a lot of work,' Wang explains. GO Public, powered by OpenAI, is designed to help lawyers consider more information while directing their expertise toward the decisions that matter most."
- **Our assessment**: The "change-averse industry" framing corroborates the same characterization already present in `blog-openai-gilbert-tobin-legal-ai-governance.md`'s broader narrative about law firms needing deliberate governance groundwork (contractual protections, role-based access, approved-task guidance) before expanding AI access — both articles frame law as a profession where trust and accountability norms slow adoption relative to other industries, and both pair that framing with an explicit design choice (Cooley's review-and-validate harness; Gilbert + Tobin's governance-before-scale sequencing) meant to address the underlying concern rather than dismiss it.

### Claim 10: Dave Peinsipp frames GO Public as the beginning of a broader shift in how capital markets work is delivered, with the collaboration seen as having "enormous potential" for capital markets transactions more broadly, not just IPOs
- **Evidence**: Direct attributed quote closing the article.
- **Confidence**: anecdotal (a forward-looking aspiration stated by a senior partner, not a described or committed expansion plan)
- **Quote**: "'GO Public is our vision for the future of capital markets practice,' Peinsipp says. 'Our collaboration with OpenAI has allowed us to rethink how this work gets done. We see enormous potential not only for IPOs but for capital markets transactions more broadly.'"
- **Our assessment**: This is a stated aspiration for horizontal expansion of the same agentic-harness pattern (client-first synthesis, curated institutional know-how, fixed human-review gate) to other capital-markets transaction types (e.g. M&A, secondary offerings — neither named specifically). No committed timeline, transaction type, or resourcing detail is given; this should be read as closing-quote aspiration rather than a roadmap.

## Concrete Artifacts

### Full article text (verbatim, via reader-proxy retrieval — see Extraction Notes)

```
Source: https://openai.com/index/cooley-gopublic
(OpenAI, published September 17, 2026)

Cooley is an international law firm with a reputation for helping companies
navigate capital markets and initial public offerings (IPOs). In 2025, the
firm advised on 180 deals globally, totaling more than $51.5 billion in deal
volume. Cooley has a decade-long track record at the top of the US
issuer-side IPO market and has advised on more venture-backed IPOs than any
other firm over the past 20-plus years.

Capital markets involve huge amounts of information that need to be
synthesized and analyzed. "For our lawyers, it's always very busy," explains
David Wang, Chief Innovation Officer at Cooley. "When there's an IPO, there
are thousands of things that need to be done constantly."

Cooley developed GO Public, a proprietary AI product offering built on
ChatGPT Work. Its agentic harness analyzes information so lawyers can review
and validate the work. The workflow comes together into a tailored starting
point for an IPO.

"ChatGPT Work is changing legal work by bringing intelligence to every step
of the process faster, more effectively, and more democratically."
— David Wang, Chief Innovation Officer

## Synthesizing legal expertise into an AI product offering

"An IPO is one of the most consequential moments in a company's life, and it
can consume enormous management attention," says Dave Peinsipp, partner and
co-chair of Cooley's global capital markets group. "GO Public helps us move
through the intensive preparation faster so lawyers and management teams can
spend more time on the decisions that shape the transaction — where
judgment, market experience and strategic thinking matter most."

Before GO Public, teams often began with a precedent from a comparable
company and adapted it to fit the client's circumstances. GO Public allows
Cooley to begin with the client itself, bringing together the information
provided, relevant public sources, and carefully curated precedents to
create a more tailored starting point for lawyer review.

"Everybody understands that as the leading capital markets firm, we know
what to do in an IPO," Wang says. Cooley's legal engineers, innovation
counsel, and practitioners worked together to translate the firm's capital
markets experience into a proprietary agentic system. "With GO Public and
the agentic harness that we built using OpenAI's technology, we were able to
bring this forward into the AI era," Wang says.

The harness provides a controlled workflow for agents that lays out which
steps agents can perform automatically, where lawyers must review or
validate the work, and how it all comes together. Information curated from
previous analyses provides what Wang calls "baked-in know-how." Cooley
partners closely with OpenAI to combine subject-matter expertise and AI
engineering knowledge to ensure the right processes produce the right
outcomes.

## Concentrating human effort where it's most impactful

With GO Public, Cooley can redirect more lawyer and management time toward
the substantive work that drives an IPO. "The amazing thing about
integrating ChatGPT Work into GO Public is that it brings intelligence to
this very large array of information that had to be manually sorted
before," Wang says. "Once you do that first cut, you're able to really
concentrate the human effort and expertise on the highest value surface
areas."

"That's what we mean by speed to quality," Peinsipp says. "The point isn't
simply to do the same work faster. It's to get to a strong starting point
sooner, so our lawyers can spend more time applying judgment, challenging
the disclosure and thinking strategically about the issues that matter most
to the company."

For management teams, the benefit extends beyond the legal work itself. IPO
preparation competes for the attention of executives who are also running
fast-moving businesses.

"ChatGPT Work allows us to move more quickly through intensive preparation
and give valuable time back to management. We want their attention focused
where only they can add value — on the business, the story and the
decisions that will ultimately shape the offering."
— Dave Peinsipp, Partner and Co-Chair, Global Capital Markets

## Transforming an industry

"Traditionally, the legal industry has been relatively change-averse," Wang
says. But AI is giving Cooley an opportunity to rethink how capital markets
work gets done while preserving the professional judgment and accountability
clients depend on.

"As attorneys, we have professional duties and obligations to make sure
that the best, most legally defensible outcome occurs for our clients, and
that just takes a lot of work," Wang explains. GO Public, powered by OpenAI,
is designed to help lawyers consider more information while directing their
expertise toward the decisions that matter most.

Peinsipp sees GO Public as the beginning of a broader shift in how capital
markets work is delivered.

"GO Public is our vision for the future of capital markets practice,"
Peinsipp says. "Our collaboration with OpenAI has allowed us to rethink how
this work gets done. We see enormous potential not only for IPOs but for
capital markets transactions more broadly."
```

### Article metadata (from page source, not visible in rendered body text)

```
Source: raw page metadata for https://openai.com/index/cooley-gopublic
(retrieved via HTML fetch of the rendered Next.js page data, September 28, 2026)

publicationDateText: "September 17, 2026"
subhead: "Cooley's GO Public offering uses ChatGPT Work to surface issues
  earlier, focus expertise, and help clients reach market faster."
tags: Enterprise, North America, Services, ChatGPT
```

## Cross-References

### Cross-reference verification notes
`blog-openai-gilbert-tobin-legal-ai-governance.md`,
`blog-openai-legora-financial-statement-tie-out.md`, and
`blog-anthropic-claude-legal-industry.md` were each re-read directly
(MINER.md §4b). Every `Claim N` citation above was confirmed against those
notes' actual numbered `### Claim N:` headings in document order, and every
passage quoted from them was copied character-for-character from the cited
file.

- **Corroborates**:
  - `blog-openai-gilbert-tobin-legal-ai-governance.md` Claim 11 (Codex-built
    AML/KYC/conflict workflow: "completes research and processing steps,
    then produces a report for human review and sign-off") and
    `blog-openai-legora-financial-statement-tie-out.md` Claim 5 ("The Agent
    handles the exhaustive comparison, while the expert remains responsible
    for the judgment call on each result"): this source's Claim 5 (GO
    Public's harness lays out "which steps agents can perform automatically,
    where lawyers must review or validate the work") and Claim 7 ("Once you
    do that first cut, you're able to really concentrate the human effort
    and expertise on the highest value surface areas") are a third,
    independent instance of the same fixed agent-breadth /
    human-judgment-gate design across three different professional-services
    AI deployments (a law firm's own product, a vendor platform used by a
    law firm, and a coding agent used by a law firm) — all three retain a
    permanent human sign-off step with no stated trajectory toward reduced
    review over time.
  - `blog-openai-gilbert-tobin-legal-ai-governance.md`'s broader narrative
    of law-firm AI governance requiring deliberate groundwork before
    expanding access: this source's Claim 9 ("Traditionally, the legal
    industry has been relatively change-averse") independently names the
    same industry characteristic that motivates Gilbert + Tobin's
    governance-before-scale sequencing (approved-task guidance,
    contractual protections, role-based access — that note's Claim 3), from
    a second, unrelated law firm.
  - `blog-openai-legora-financial-statement-tie-out.md` Claim 2 (Percevale
    Perks, "Legal Engineer, Legora"): this source's Claim 4 names "legal
    engineers" as part of the team that built GO Public at Cooley — a
    second, independent instance of "legal engineer" as a specific,
    recurring named role title for practitioners who translate domain
    expertise into AI-workflow design, this time on the customer/law-firm
    side rather than the vendor side.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Cooley, GO Public, IPO-preparation AI workflows, or the
  "speed to quality" framing that this source disagrees with. The
  build-a-proprietary-harness-on-ChatGPT-Work choice described in Claim 2
  is a conditioning variable (a strategic build-vs-buy choice) relative to
  Gilbert + Tobin's buy-a-vetted-platform choice (Harvey) for
  legal-substance work — not a disagreement about what either tool can do
  or should be trusted to do. Per MINER.md §4a, no contradiction issue was
  filed.

- **Extends**:
  - `blog-openai-gilbert-tobin-legal-ai-governance.md` Claim 7 (Gilbert +
    Tobin lawyers use ChatGPT for "the operational side" of their work
    while legal-specific workflows go through the separately vetted Harvey
    platform): this source's Claim 2 extends the corpus's record of how law
    firms draw the line between general-purpose AI platforms and
    legal-substance work, but with the opposite strategic choice. Gilbert +
    Tobin keeps ChatGPT away from legal-substance work and buys a
    separately vetted vertical platform (Harvey) for it; Cooley instead
    builds its own proprietary agentic harness (GO Public) directly on top
    of ChatGPT Work and uses it for legal-substance work (IPO document
    preparation) itself. The guide should present these as two distinct,
    documented strategies for the same underlying "which tool for
    legal-substance work" question — buy a vetted vertical product vs.
    build a proprietary harness on a general-purpose platform — rather than
    assuming one is more common or more advisable than the other; the
    corpus now has one clean example of each.
  - `blog-openai-legora-financial-statement-tie-out.md`: both sources
    describe an agent performing an exhaustive first pass over a large
    information set so a human expert can apply judgment to a narrowed
    output, but at different points in the value chain. Legora is a
    third-party vendor selling an agentic platform that a law firm uses;
    Cooley is a law firm that built its own proprietary product using
    OpenAI's underlying platform. This is the same build-vs-buy contrast
    named above, applied to the vendor-relationship dimension rather than
    the platform-selection dimension.

- **Novel**:
  - **"Speed to quality" as an explicit rejection of "same work, faster" as
    the goal** (Claim 6): no prior corpus source this note's author
    reviewed states this framing as directly — most case studies report a
    bare time-savings multiplier (e.g. "4 hours to 20 minutes") without
    addressing what the freed time is redirected toward or explicitly
    denying that raw speed was the point.
  - **Client executive attention, rather than only the professional-services
    firm's own staff time, named as a beneficiary of the AI tool** (Claim
    8): "ChatGPT Work allows us to move more quickly through intensive
    preparation and give valuable time back to management" — a
    professional-services AI deployment whose stated value proposition
    explicitly includes redirecting the *client's* executives' attention,
    not only the law firm's own lawyers' time.
  - **A law firm building its own proprietary agentic product on a
    general-purpose enterprise AI platform, rather than buying a vetted
    vertical platform, for legal-substance work** (Claim 2): the corpus's
    first clean "build" case to contrast against Gilbert + Tobin's "buy"
    case (Harvey) for the same underlying need.
  - **"Baked-in know-how" as a named term for curated-prior-analysis context
    feeding an agentic harness** (Claim 5): a specific naming of the
    institutional-knowledge-encoding mechanism that other corpus sources
    describe (e.g. Legora's and Gilbert + Tobin's human-review-gated
    workflows) without a comparable name.

## Guide Impact

- **Chapter 02 (Harness Engineering — build vs. buy for domain-specific
  work)**: Add Claim 2 (Cooley builds its own proprietary agentic harness,
  GO Public, on top of ChatGPT Work, rather than adopting a separately
  vetted vertical legal-AI platform) as a documented "build" case,
  contrasted directly with `blog-openai-gilbert-tobin-legal-ai-governance.md`
  Claim 7's "buy" case (Harvey for legal-substance work, ChatGPT for
  operational work). The guide currently has no explicit build-vs-buy
  framing for domain-specific AI harnesses in regulated professional
  services; this pairing gives it one, with both cases from the same
  vendor ecosystem (OpenAI) and industry (law), which controls for vendor
  and industry as confounding variables.
- **Chapter 05 (Team Adoption) or wherever the guide discusses
  human-in-the-loop design**: Add Claim 5 and Claim 7 (GO Public's harness:
  agents perform automatable steps and a "first cut" over a large
  information set, lawyers review/validate and apply judgment to "the
  highest value surface areas") as a third named instance of the
  fixed-agent-breadth/human-judgment-gate pattern, alongside Gilbert +
  Tobin's AML/KYC workflow and Legora's tie-out agent (see
  Cross-References → Corroborates). Recommend citing Claim 6's "speed to
  quality" framing as a reusable, quotable articulation of why this
  pattern's benefit is not raw throughput.
- **This source should not be cited for any quantified before/after
  performance claim** — unlike nearly every other OpenAI customer case
  study in the corpus, it contains no time-savings figure, adoption
  percentage, or deal-count acceleration number. If the guide needs a
  quantified IPO-or-capital-markets AI example, this is not that source;
  it should be cited only for its qualitative framing (starting-point
  shift, "speed to quality," build-vs-buy) and the named human-in-the-loop
  harness design.

## Extraction Notes

1. **Direct fetch blocked (bot protection)**: Both `WebFetch` and a direct
   `curl` (with a standard desktop-browser user agent) against
   `https://openai.com/index/cooley-gopublic` returned HTTP 403 — consistent
   with the Cloudflare-style bot-protection behavior already documented for
   the `openai.com/index/` domain across prior OpenAI-sourced notes in this
   corpus (e.g. `blog-openai-gilbert-tobin-legal-ai-governance.md`,
   `blog-openai-legora-financial-statement-tie-out.md`). The article was
   retrieved via the `r.jina.ai` reader-proxy
   (`https://r.jina.ai/https://openai.com/index/cooley-gopublic`, HTTP 200),
   which returned a clean Markdown extraction of the full rendered article
   (46 lines, ~470 words). A second fetch of the raw rendered-page HTML
   (also via the same reader proxy, requesting HTML rather than Markdown)
   was used only to confirm the publication date (September 17, 2026), the
   subhead, and page tags via the page's embedded JSON metadata — this did
   not surface any body content beyond what the Markdown extraction already
   captured; a targeted search of that HTML for percentage/multiplier
   figures ("N%", "Nx faster", "reduced by N%") found only CSS/design-token
   values with no article-content context, confirming the article truly
   contains no quantified performance metric anywhere on the page.
2. **Entire article captured, nothing truncated**: The retrieved Markdown
   ends on a clear closing quote ("We see enormous potential not only for
   IPOs but for capital markets transactions more broadly.") with no
   indication of truncation. All ten claims above are drawn from this
   single, complete retrieval, reproduced verbatim in Concrete Artifacts.
3. **No sub-pages followed**: The retrieved article contains no inline
   links to further substantive pages (no linked PDF, no companion
   technical post, no "related stories" footer content within the article
   body). Per MINER.md §1, no linked pages existed to follow beyond the
   generic site navigation/footer, which is not Cooley- or GO
   Public-specific.
4. **Confidence rated `anecdotal` overall**: every claim is a first-party,
   vendor-published characterization or quote from a single customer case
   study, with zero quantified metrics of any kind, no independent audit,
   and no second independent source (a client, an associate, a press
   account of a specific Cooley-advised IPO) confirming any claim. This is
   a strictly thinner evidentiary basis than the corpus's other OpenAI
   legal-vertical case studies (Gilbert + Tobin's 87% adoption figure and
   named time-savings figures; Legora's 41-document run and BAR percentages),
   both of which at least offer some quantified, if unaudited, figures.
5. **No contradiction filed**: Checked this source's content against
   `blog-openai-gilbert-tobin-legal-ai-governance.md` and
   `blog-openai-legora-financial-statement-tie-out.md`; no material
   opposition to any existing claim was found. The build-vs-buy strategic
   difference from Gilbert + Tobin (Claim 2, Cross-References →
   Contradicts) is a conditioning variable — a different firm making a
   different strategic choice — not a disagreement about what either
   platform or design choice can achieve. Open `contradiction`-labeled
   issues and `CONTRADICTIONS.md` were checked; none covers this pairing.
