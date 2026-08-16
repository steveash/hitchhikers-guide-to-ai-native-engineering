---
source_url: https://openai.com/index/hsp-gruppe
source_type: blog-post
title: "How HSP GRUPPE builds AI capabilities for tax advisory"
author: OpenAI (customer-story vertical; quoted subjects Carsten Schulz — CEO, HSP GRUPPE; Frank Heibel — Managing Partner; Magdalene Posnak — Partner; Marco Sell — Managing Director; Jan-Henrik Leifelt — lawyer and tax advisor)
date_published: 2026-08-07
date_extracted: 2026-08-16
last_checked: 2026-08-16
status: current
confidence_overall: emerging
issue: "#2734"
---

# How HSP GRUPPE builds AI capabilities for tax advisory

> An OpenAI customer-story case study documenting how HSP GRUPPE — a German
> network of legally independent tax advisory, auditing, and law firms —
> rolled out ChatGPT Enterprise as an organizational capability rather than
> a tool, standardized successful use cases into shared custom Agents,
> reports high self-reported adoption and productivity survey figures (84%
> weekly active usage, 98.6% reporting higher productivity), and frames the
> economic case explicitly as capacity redirection rather than headcount
> reduction.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/`,
  ~1,300 words; auto-discovered via the `openai-news` trusted feed,
  published August 7, 2026)
- **Author credibility**: House-authored OpenAI customer-story copy built
  around quotes from five named HSP GRUPPE professionals: Carsten Schulz
  (CEO), Frank Heibel (Managing Partner), Magdalene Posnak (Partner), Marco
  Sell (Managing Director), and Jan-Henrik Leifelt (lawyer and tax advisor).
  HSP GRUPPE is described as a network of legally independent tax advisory,
  auditing, and law firms with more than two decades of investment in
  digitizing and standardizing professional-firm processes. This is a
  vendor case study — OpenAI selected the customer, chose which quotes and
  metrics to publish, and frames the narrative promotionally (a "Results at
  a glance" bullet box, a "Leadership lessons" bullet list, a "Tips" bullet
  list) — not an independent report with disclosed methodology. The article
  itself discloses an important scope caveat in its opening italic note:
  "The usage figures in this story refer to the shared ChatGPT Enterprise
  workspace used by HSP GRUPPE and Kanzleipakt, covering 81 organizational
  groups" — meaning the headline usage/survey figures are not HSP GRUPPE
  alone but a combined workspace shared with a second, otherwise-unexplained
  entity (Kanzleipakt), which is a material scoping detail for any figure
  cited from this source.
- **Scope**: Covers HSP's ChatGPT Enterprise rollout philosophy (organizational
  transformation, not software rollout), governance/data-protection framing,
  named shared custom Agents (AI Client Communication, Booking Assistant
  SKR03 & SKR04), four named individual-practitioner use cases, a forward
  pilot of "ChatGPT Work" (agentic capabilities), an economic framing tied
  to capacity redirection rather than headcount reduction, a specific
  workflow-redesign vision for year-end accounting, an eight-bullet
  "Results at a glance" metrics box, a five-item "Leadership lessons" list,
  and a five-item "Tips" list. Does NOT cover: technical implementation
  details of any Agent (prompts, data pipelines, model versions, guardrail
  configuration), cost or licensing terms, any failure mode, rollback, or
  employee pushback, the survey's sample size or instrument design, how
  "88 opportunities for automation" were identified or by whom, or any
  detail on what Kanzleipakt is or how the shared workspace is governed
  between the two organizations.

## Extracted Claims

### Claim 1: HSP approached generative AI as an organizational transformation problem — "helping the organization absorb it" — rather than a software deployment problem, and named this the central challenge rather than introducing the technology itself
- **Evidence**: Direct pull-quote from the CEO, presented as the article's framing thesis near the top of the piece, followed by a structural section ("Inside the rollout") explicitly stating "HSP approached AI as an organizational transformation rather than a software rollout."
- **Confidence**: anecdotal (single executive's framing quote; no operational detail on what "organizational absorption" specifically required beyond the governance and forum mechanisms described elsewhere in the article)
- **Quote**: "Technology is moving faster than organizations can transform. Our challenge wasn't introducing AI—it was helping the organization absorb it." —Carsten Schulz, CEO, HSP GRUPPE
- **Our assessment**: This is the same "adoption is organizational change, not a software rollout" framing already well-established across the corpus's OpenAI customer-story sources (`blog-openai-bbva-banking-transformation.md` Claim 11's "treat AI as business transformation... not a standalone innovation effort," and by extension `blog-openai-endava-frontiers.md`'s "behavior change, not a software rollout"). This is now a third independent OpenAI customer story converging on identical framing language across three different industries (banking, IT consulting, tax advisory) — strengthening the read that this is OpenAI's consistent house editorial template for customer stories rather than three companies independently arriving at the same conclusion.

### Claim 2: HSP's AI governance model separates technical security controls (ChatGPT Enterprise's built-in features) from organizational data-protection policy (HSP's own internal confidentiality/governance rules), and explicitly preserves final professional responsibility with the human tax, legal, or accounting professional in every case
- **Evidence**: Direct statement in the "Inside the rollout" section, and repeated twice more in the article for the two named Agents (AI Client Communication and Booking Assistant SKR03 & SKR04), each restating that professional review and final responsibility remain with the human specialist.
- **Confidence**: emerging (a named, repeatedly-stated governance principle applied consistently to every AI-touching workflow described in the article; single company; no description of how "final responsibility" is enforced operationally — e.g., no described sign-off workflow, audit log, or review checklist)
- **Quote**: "ChatGPT Enterprise's security features provide an important technical foundation, while the use of client-related information is governed by HSP's internal data protection, confidentiality, and governance requirements. Professional review and final responsibility always remain with the relevant tax, legal, or accounting professional."
- **Our assessment**: This is a regulated-professional-services variant of the "keep a human in the loop for the actual decision, let AI handle mechanical work" pattern documented elsewhere in the corpus's financial-services sources (e.g., `blog-anthropic-hebbia-financial-diligence.md` Claim 6's covenant-analysis "flagging risks" framing, `blog-openai-bbva-banking-transformation.md` Claim 7's Credit Analysis Pro GPT). Unlike those sources, HSP's article states the human-responsibility principle three separate times across different Agents, which suggests this is a deliberately repeated compliance framing for a licensed-professional context (tax advisors, auditors, lawyers carry personal professional liability in Germany) rather than a generic AI-safety disclaimer. The article gives no operational detail on how this is enforced — it is a stated policy, not a described control.

### Claim 3: HSP standardized successful individual use cases into shared custom Agents available to every employee — named examples are "AI Client Communication" (drafts, structure, tone for client messages) and "Booking Assistant SKR03 & SKR04" (supports classification of accounting/booking questions) — explicitly to spread best practices beyond AI experts
- **Evidence**: Direct description of both named Agents with their functions, framed as an organizational-scaling mechanism distinct from individual experimentation.
- **Confidence**: emerging (two named, described production Agents with stated purpose; no adoption-count, usage-volume, or accuracy/quality metric given for either Agent specifically)
- **Quote**: "the organization also began standardizing successful use cases into custom Agents. One example is AI Client Communication, a shared Agent that supports first drafts, structure, clarity, and a more consistent, client-oriented tone... Another is the Booking Assistant SKR03 & SKR04, which supports the preparation and classification of specific booking questions... Together, these kinds of shared Agents reduce repetitive work while making best practices available to every employee—not just AI experts."
- **Our assessment**: "SKR03 & SKR04" are named German standard charts of accounts (Standardkontenrahmen) used in German bookkeeping — this is a concrete, domain-specific artifact naming a real regulatory/accounting standard the Agent is built around, which is more specific than most vendor case-study tool descriptions in the corpus. The "grassroots experimentation → standardized shared Agent" progression mirrors the champion-network-to-shared-tool pattern in `blog-openai-bbva-banking-transformation.md` Claim 6 (employee-built custom GPTs, with a minority seeing frequent reuse), but HSP's version is narrower and more deliberate: only two named Agents are described as having been formally standardized, versus BBVA's reported 20,000+ raw employee-built GPT count. This is a different point on the same "bottom-up experimentation, top-down curation" spectrum — HSP's approach is described as more curated/selective, BBVA's as broader and less filtered.

### Claim 4: Partner Magdalene Posnak reduced the time to evaluate multiple real estate investments from approximately nine hours to approximately two hours using ChatGPT, redirecting the saved time to client advisory
- **Evidence**: Direct pull-quote attributed by name and title, presented as a standalone block quote.
- **Confidence**: anecdotal (single named practitioner's self-reported before/after time estimate for one task type; no description of what the nine-hour or two-hour process specifically involved, no sample size beyond "several real estate investments," no accuracy/quality check on the AI-assisted output)
- **Quote**: "An analysis of several real estate investments used to take me around nine hours. With ChatGPT, I can prepare it in about two—and use the time saved for client advisory." —Magdalene Posnak, Partner, HSP GRUPPE
- **Our assessment**: A ~78% time reduction (9 hours → 2 hours) on a named financial-analysis task is directly comparable in kind to `blog-openai-bbva-banking-transformation.md` Claim 10's Peru query-handling metric (7.5 minutes → 1 minute, ~87% reduction) — both are single-practitioner or single-market, self-reported, before/after task-time claims with no stated measurement methodology. The explicit "use the time saved for client advisory" framing is notable: it names redirection toward higher-value work (not headcount reduction) as the stated purpose of the time savings, which is consistent with and reinforces Claim 7 below (the article's explicit organization-wide "not about reducing headcount" framing).

### Claim 5: HSP ran monthly AI forums as the mechanism for employees to share practical use cases and learn from each other, positioned as central to building AI as a scalable organizational capability rather than isolated individual experimentation
- **Evidence**: Direct statement in the "Inside the rollout" section, restated in the "Leadership lessons" and "Tips" sections at the close of the article ("Create a culture of continuous learning. Regular AI forums helped successful ideas spread quickly across the organization" and "Create regular forums where employees can share successful use cases across teams").
- **Confidence**: emerging (a named, recurring organizational mechanism repeated across three sections of the article for internal consistency; single company; no attendance figures, cadence-adherence data, or measured effect of the forums on adoption speed)
- **Quote**: "Monthly AI forums gave employees a place to share practical use cases and learn from one another."
- **Our assessment**: This is a lighter-weight, single-tier version of the champion/enablement-network pattern already well-documented in the corpus (`blog-openai-bbva-banking-transformation.md` Claim 4's two-tier "champions" + "wizards" network; `blog-anthropic-cowork-deploy-guide.md`'s champion-authored-skills pattern). HSP's forums are a recurring open venue rather than a designated champion role or headcount-backed program — no named "champions" or "wizards" role exists in this article. This is a third independent vendor-ecosystem data point (OpenAI, tax-advisory vertical) for the general claim that structured, recurring peer-knowledge-sharing venues are a recurring enterprise AI-adoption mechanism, but it documents a lighter-weight variant (an open monthly forum) than the role-based champion networks documented elsewhere.

### Claim 6: HSP is piloting "ChatGPT Work" (agentic AI capabilities) with a small group of developers and administrators before expanding it across the wider workspace, explicitly to understand how agentic AI can safely automate complex workflows while balancing governance, quality, and cost
- **Evidence**: Direct statement describing the pilot's scope, participant group, and stated purpose, in the "Preparing for the next wave with ChatGPT Work" section.
- **Confidence**: anecdotal (a stated pilot strategy and its rationale; no participant count, pilot duration, or any outcome/result reported yet — this is described as in-progress at the time of the article, "just weeks" after gaining access)
- **Quote**: "Just weeks after gaining access, the organization began piloting the platform with a small group of developers and administrators before expanding across the wider workspace. The goal is to understand how agentic AI can safely automate complex workflows while balancing governance, quality, and cost before broader rollout."
- **Our assessment**: This is a textbook staged-rollout pattern (small technical pilot group → wider rollout), consistent with the "Tips" section's own explicit fifth item ("Pilot new capabilities with small groups before expanding organization-wide"). Piloting with developers and administrators specifically — rather than with the tax/legal professionals who are the firm's primary knowledge workers — suggests HSP is treating agentic-AI governance and safety validation as a technical-operations concern to de-risk first, before extending agentic capabilities to client-facing regulated work. The article gives no outcome data from this pilot; it should be read as a stated intention/early-stage process, not a completed or measured rollout.

### Claim 7: HSP explicitly frames the economic benefit of AI adoption as capacity redirection, not headcount reduction — the firms in the network are described as already operating at capacity with substantial backlogs, so time saved is redirected toward additional client work, shorter turnaround times, and stronger client service
- **Evidence**: Direct statement in the "Preparing for the next wave with ChatGPT Work" section, presented as an explicit organizational stance on how efficiency gains are being used.
- **Confidence**: emerging (a clearly stated organizational framing tied to a described operational condition — capacity-constrained firms with backlogs — though no backlog size, turnaround-time figure, or headcount data is given to substantiate "already operating at capacity")
- **Quote**: "For HSP, the economic benefit is not about reducing headcount. The firms in the network are already operating at capacity and managing substantial backlogs. Time saved with ChatGPT can therefore be redirected toward additional client work, shorter turnaround times, more advisory capacity, and stronger client service."
- **Our assessment**: This is one of the more explicit and unambiguous "AI is not a headcount-reduction tool here" statements in the corpus's enterprise case-study material — most sources (BBVA, PayPal, Hebbia) discuss productivity/efficiency gains without directly addressing headcount, leaving the question implicit. HSP's article states the counterfactual directly: the firms are demand-constrained (backlogs), not supply-constrained by excess headcount, so the efficiency gain has an obvious redirection target (more billable work) rather than requiring a framing choice between "do the same work with fewer people" and "do more work with the same people." This is useful, concrete context for a guide passage on how to communicate the economic case for AI adoption to a workforce concerned about job displacement — professional-services firms with backlogs have a structurally different (and easier) economic story to tell than firms without a demand overhang.

### Claim 8: CEO Carsten Schulz frames the larger opportunity as redesigning entire workflows rather than automating existing tasks, illustrated by a concrete example: using ChatGPT Work to continuously review bookkeeping throughout the year and proactively request missing documents from clients, rather than discovering missing information only when annual accounts are prepared months later
- **Evidence**: A named, described workflow-redesign example (year-end accounting) contrasted explicitly with the current-state failure mode (missing information discovered late, months after bookkeeping), presented as an illustration of the article's stated broader thesis.
- **Confidence**: anecdotal (a described exploratory/aspirational use case — "HSP is exploring how ChatGPT Work could" — not a deployed or measured capability; single named example)
- **Quote**: "Today, accountants often discover missing information only when they begin preparing annual accounts months after bookkeeping has been completed. HSP is exploring how ChatGPT Work could continuously review bookkeeping, identify missing information throughout the year, and proactively request documents from clients—so that much of the preparation has already happened before an accountant even opens the file."
- **Our assessment**: This names a specific, concrete workflow-redesign target (continuous proactive review vs. batch end-of-year discovery) rather than a generic "redesign your workflows" exhortation — it is a genuine example of the "AI orchestrating work across entire processes" framing the article uses to distinguish this from simple task assistance. It is explicitly aspirational/exploratory (not yet built or measured), which distinguishes it from Claims 3-5 above (described as already operating). The guide should treat this as an illustrative target-state example for what agentic workflow redesign looks like in a specific professional-services task, not as evidence of a deployed capability.

### Claim 9: Schulz reports HSP identified 88 discrete opportunities for automation internally, but frames that count itself as "already thinking too small" — arguing the more valuable question is redesigning processes, not automating today's process as-is
- **Evidence**: Direct pull-quote attributed to the CEO, presented as a closing framing statement for the "Preparing for the next wave" section.
- **Confidence**: anecdotal (a specific named count with no description of how the 88 opportunities were identified, by whom, over what time period, or what methodology defined an "opportunity")
- **Quote**: "We identified 88 opportunities for automation. But I think that's already thinking too small. The real question isn't how we automate today's processes. It's how we redesign them. That's what opens the door to a completely new world." —Carsten Schulz, CEO, HSP GRUPPE
- **Our assessment**: The specific figure (88) gives the claim a veneer of rigor, but the article discloses zero methodology for how these opportunities were catalogued — it functions rhetorically (a concrete number immediately dismissed as insufficiently ambitious) rather than as a measurable inventory the guide could cite as evidence of anything beyond "leadership rhetoric favoring redesign over automation." This is the same "automate vs. redesign" distinction found broadly across the corpus's workflow-transformation sources (e.g., `blog-cursor-paypal-enterprise-adoption.md` Claim 6's linear-to-iterative SDLC shift), applied here specifically to professional-services back-office work (year-end accounting, per Claim 8).

### Claim 10: HSP's self-reported six-month survey results (Feb 1–Jul 14, 2026, shared workspace covering HSP GRUPPE and Kanzleipakt, 81 organizational groups) report 84% weekly active usage (755 weekly active users, 913 unique users), 500,000+ exchanged messages, 98.6% reporting higher productivity, 84.6% reporting improved quality of work, 95.9% reporting weekly time savings (63.5% at least two hours, 25.7% at least five hours), 79.7% reporting better client service, and 78.1% reporting higher job satisfaction
- **Evidence**: The article's "Results at a glance" bulleted metrics box, drawing on an employee survey and platform usage data over a stated six-month window.
- **Confidence**: anecdotal (multiple specific, precise percentages presented as a self-reported employee survey with no disclosed sample size, response rate, survey instrument, or independent verification; the article's own opening caveat states these figures cover a *shared* workspace across two organizations and 81 organizational groups, not HSP GRUPPE in isolation)
- **Quote**: "Achieved 84% weekly active usage, with 755 weekly active users and 913 unique users over six months (February 1 to July 14, 2026)... 98.6% of surveyed employees reported higher productivity, while 84.6% reported improved quality of work. 95.9% of respondents reported weekly time savings; 63.5% saved at least two hours per week, and 25.7% saved at least five hours... 79.7% reported better client service and 78.1% reported higher job satisfaction."
- **Our assessment**: The scoping caveat in the article's opening note — that these figures describe a *shared* ChatGPT Enterprise workspace between HSP GRUPPE and an entity called "Kanzleipakt," covering 81 organizational groups — is a material qualifier the guide should preserve whenever citing any headline number from this source: 913 unique users across 81 organizational groups is a small, mixed-population sample (averaging ~11 users per group), and it is not exclusively HSP GRUPPE's own employee base. The near-universal positive percentages (98.6% productivity, 95.9% time savings) are higher than most comparable self-reported figures elsewhere in the corpus and should be read with appropriate skepticism about self-selection in survey response (employees who use the tool enough to notice benefits are more likely to respond to a usage survey) — the article gives no response-rate figure to evaluate this risk.

### Claim 11: HSP's internal "deliberately conservative" capacity-planning scenario estimates approximately 40,000 hours of additional annual capacity from AI-supported work (≈28,000 hours in generally-billable specialist work, ≈12,000 hours in administration/client-service/support), translating at conservative hourly rates to an estimated theoretical annual revenue potential of approximately €3.8 million — explicitly framed as a capacity scenario, not realized or guaranteed revenue
- **Evidence**: The article's "Results at a glance" section, presented as an internal scenario model with an explicit self-applied "deliberately conservative" qualifier and an explicit disclaimer distinguishing the estimate from realized results.
- **Confidence**: anecdotal (an internal scenario/estimate, not a measured outcome; no disclosed hourly-rate assumptions, no description of the capacity-planning model's methodology, and the article states the firm "expects to assess the full financial impact later this year" — i.e., no actual financial impact has yet been measured at publication time)
- **Quote**: "A deliberately conservative internal scenario estimates approximately 40,000 hours of additional annual capacity. Around 28,000 hours could support productive, generally billable specialist work, while roughly 12,000 hours could support administration, client service, and support. Based on conservative hourly rates, HSP estimates a theoretical annual revenue potential of approximately €3.8 million. This is a capacity scenario—not realized or guaranteed revenue."
- **Our assessment**: This is the article's own most explicit hedge — the "not realized or guaranteed revenue" language is a self-imposed disclaimer rarely seen this directly stated in vendor case-study copy, which typically presents revenue-adjacent figures without such an explicit caveat (contrast with `blog-openai-bbva-banking-transformation.md`'s metrics, none of which carry an equivalent "not realized" disclaimer). The guide should cite the €3.8M figure only paired with this disclaimer, and should note the article separately states "the organization expects to assess the full financial impact later this year" — meaning, at time of publication, HSP has not yet reported an actual measured financial outcome, only capacity-hours projections.

### Claim 12: Schulz explicitly rejects the framing that AI will replace tax advisors, arguing instead that AI helps qualified professionals become "dramatically more effective," and separately frames the joint effort with Kanzleipakt as building a shared, documented, scalable reference-workflow team around AI, firm process, and development
- **Evidence**: A closing pull-quote from the CEO addressing the "AI replaces tax advisors" narrative directly, combined with the article's stated forward plan to establish a "joint DATEV-centric AI, firm process, and development team" with Kanzleipakt.
- **Confidence**: anecdotal (executive framing/opinion on a contested industry narrative; the joint-team plan is a stated forward intention, not a described or measured outcome)
- **Quote**: "Everyone talks about AI replacing tax advisors. I think that's the wrong conversation. The real opportunity is helping qualified professionals become dramatically more effective." —Carsten Schulz, CEO, HSP GRUPPE
- **Our assessment**: This is a direct, on-the-record executive rebuttal of the AI-displacement narrative specifically for a licensed-professional context (tax advisory, where displacement fears are especially salient given regulatory licensing requirements) — a more pointed and specific statement than the generic "AI augments rather than replaces" framing seen elsewhere in the corpus. Combined with Claim 7's explicit "not about reducing headcount" statement, this article is unusually consistent (three separate places: Claims 2, 7, 12) in explicitly naming and rejecting headcount-reduction/displacement as the economic driver, which is a notably stronger and more repeated version of this framing than found in the corpus's other enterprise-adoption sources.

## Concrete Artifacts

```
Source: OpenAI, "How HSP GRUPPE builds AI capabilities for tax advisory,"
https://openai.com/index/hsp-gruppe (published August 7, 2026; retrieved
via r.jina.ai reader proxy — see Extraction Notes)

Opening scope caveat (verbatim, italicized note at top of article):
  "The usage figures in this story refer to the shared ChatGPT Enterprise
  workspace used by HSP GRUPPE and Kanzleipakt, covering 81 organizational
  groups. HSP GRUPPE itself is a network of legally independent tax
  advisory, auditing, and law firms."

"Results at a glance" (verbatim bulleted list):
  - Achieved 84% weekly active usage, with 755 weekly active users and 913
    unique users over six months (February 1 to July 14, 2026).
  - During the evaluated period from February 1 to July 14, 2026, users
    exchanged more than 500,000 messages with ChatGPT.
  - 98.6% of surveyed employees reported higher productivity, while 84.6%
    reported improved quality of work.
  - 95.9% of respondents reported weekly time savings; 63.5% saved at
    least two hours per week, and 25.7% saved at least five hours. HSP is
    already seeing an operational leading indicator in its annual capacity
    planning, with professionals planning significantly more work than in
    previous years because employees recognize additional capacity created
    through AI-supported work. The organization expects to assess the full
    financial impact later this year.
  - 79.7% reported better client service and 78.1% reported higher job
    satisfaction.
  - A deliberately conservative internal scenario estimates approximately
    40,000 hours of additional annual capacity. Around 28,000 hours could
    support productive, generally billable specialist work, while roughly
    12,000 hours could support administration, client service, and
    support. Based on conservative hourly rates, HSP estimates a
    theoretical annual revenue potential of approximately €3.8 million.
    This is a capacity scenario—not realized or guaranteed revenue.

"Leadership lessons" (verbatim bulleted list):
  - Treat AI as an organizational capability, not an individual tool.
    Scale successful experiments into repeatable workflows that everyone
    can benefit from.
  - Invest in operational foundations first. Strong processes, governance,
    and quality systems accelerate AI adoption.
  - Create a culture of continuous learning. Regular AI forums helped
    successful ideas spread quickly across the organization.
  - Redesign workflows—not just tasks. The greatest value comes from
    rethinking end-to-end processes rather than automating isolated
    activities.
  - Build AI around professional judgement. The greatest value comes when
    AI enhances expertise rather than replacing it.

"Tips" (verbatim bulleted list):
  - Start with business problems—not AI features.
  - Create regular forums where employees can share successful use cases
    across teams.
  - Pair AI specialists with domain experts to turn successful experiments
    into scalable workflows.
  - Pilot new capabilities with small groups before expanding
    organization-wide.
  - Measure adoption and business impact—not just deployment—to
    understand where AI is creating real value.

Named shared custom Agents (verbatim, condensed):
  AI Client Communication:
    "supports first drafts, structure, clarity, and a more consistent,
    client-oriented tone. Professional review and final responsibility
    remain with the relevant tax, legal or accounting specialist."
  Booking Assistant SKR03 & SKR04:
    "supports the preparation and classification of specific booking
    questions. The final professional decision remains with the
    employee." (SKR03/SKR04 are named German standard charts of accounts.)
```

## Cross-References

- **Corroborates**:
  - `blog-openai-bbva-banking-transformation.md` Claim 11 ("Treat AI as
    business transformation... not a standalone innovation effort") and
    `blog-openai-endava-frontiers.md`'s "behavior change, not a software
    rollout" lesson: HSP's "Our challenge wasn't introducing AI—it was
    helping the organization absorb it" (Claim 1) is a third independent
    OpenAI customer story converging on identical "adoption is
    organizational transformation, not a software rollout" framing, now
    across three industries (banking, IT consulting, tax advisory). This
    strengthens the read that this is OpenAI's consistent house editorial
    template for customer stories.
  - `blog-openai-bbva-banking-transformation.md` Claim 4 (two-tier
    "champions" + "wizards" enablement network) and
    `blog-anthropic-cowork-deploy-guide.md`'s champion-authored-skills
    material: HSP's monthly AI forums (Claim 5) corroborate the general
    pattern that structured peer-knowledge-sharing venues drive enterprise
    AI adoption, though HSP's forums are a lighter-weight, role-free
    variant (an open recurring venue) rather than a designated
    champion/wizard tier.
  - `blog-anthropic-hebbia-financial-diligence.md` Claim 6 and
    `blog-openai-bbva-banking-transformation.md` Claim 7 (human review
    retained over AI-assisted financial/credit analysis output): HSP's
    repeated "professional review and final responsibility always remain
    with the relevant tax, legal, or accounting professional" (Claim 2)
    is the professional-services-licensing variant of the same
    human-in-the-loop pattern, restated three times in this article for a
    regulated-licensed-professional context.

- **Contradicts**: None filed. No claim in this source materially opposes
  an existing source note or disagrees with itself on guidance or claim
  direction (per MINER.md §4a). The article's own internal claims are
  consistent with each other.

- **Extends**:
  - `blog-openai-bbva-banking-transformation.md`: extends the corpus's
    small set of OpenAI enterprise customer-story sources with a third
    vertical (professional services / tax advisory, following banking and
    IT consulting), and with an unusually explicit "not about reducing
    headcount" economic framing (Claim 7) tied to a specific structural
    condition (demand-constrained firms with backlogs) not previously
    articulated this directly in the corpus's enterprise-adoption sources.
  - `blog-cursor-paypal-enterprise-adoption.md` Claim 6 (linear-to-iterative
    SDLC transformation) and Claim 7 (role-boundary blurring producing
    better outcomes, not just faster ones): HSP's "redesign workflows, not
    just tasks" framing (Claims 8-9) is the professional-services-back-office
    analog of the same "automate vs. redesign" distinction PayPal makes for
    software delivery — both name redesigning end-to-end processes as more
    valuable than automating existing tasks in place.

- **Novel**:
  - **Professional-services/tax-advisory as a new regulated-industry
    vertical** in the corpus's growing set of financial/professional-services
    AI sources (alongside BBVA's banking, Hebbia's financial diligence,
    Kepler's fintech, PayPal's fintech engineering) — HSP is the first
    licensed-professional-services (tax, audit, law) case study, where
    individual practitioners carry personal professional liability distinct
    from the corporate-employee context of the other sources.
  - **Explicit, repeated "not about reducing headcount" economic framing
    tied to a demand-constrained (backlog) operating condition** (Claim 7):
    No prior corpus source states this framing as directly or ties it this
    explicitly to a structural business condition (backlogs) rather than a
    values statement.
  - **Self-disclosed "capacity scenario—not realized or guaranteed revenue"
    caveat on a headline revenue-adjacent figure** (Claim 11): a more
    explicit self-hedge on a monetary estimate than typically seen in
    vendor case-study copy in this corpus.
  - **Shared cross-organization workspace usage figures** (Claim 10): the
    article's own disclosed caveat that headline usage numbers span a
    shared workspace between two organizations (HSP GRUPPE and Kanzleipakt)
    across 81 organizational groups is a scoping detail not seen in other
    single-company case studies in the corpus, where usage figures are
    presented as belonging to one clearly-bounded organization.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add HSP's explicit "not about reducing
  headcount" economic framing (Claim 7) as a concrete example of how to
  communicate the business case for AI adoption to a workforce concerned
  about displacement, specifically for demand-constrained (backlog-heavy)
  professional-services contexts — pair with Claim 12's direct executive
  rebuttal of the "AI replaces tax advisors" narrative as illustrative
  leadership-communication material.
- **Chapter 05 (Team Adoption)**: Add HSP's monthly AI forums (Claim 5) as
  a lighter-weight variant of the champion-network pattern already
  documented from BBVA and Anthropic Cowork sources — useful for guide
  material distinguishing role-based champion programs from open recurring
  knowledge-sharing venues as two different implementations of the same
  underlying adoption mechanism.
- **Chapter 03 (Verification) or wherever the guide covers regulated
  professional-services AI**: Add HSP's repeated professional-responsibility
  framing (Claim 2) — human professional review and final responsibility
  retained across every named AI-touching workflow — as an example of how
  licensed-professional contexts (as distinct from corporate-employee
  contexts) state human-in-the-loop requirements, though flag that the
  article gives no operational description of how this is enforced.
- **Any chapter citing headline adoption/survey metrics**: When citing
  this source's "Results at a glance" figures (Claim 10), preserve the
  article's own scope caveat that the usage figures cover a shared
  workspace between HSP GRUPPE and Kanzleipakt across 81 organizational
  groups, not HSP GRUPPE's employee base in isolation.

## Extraction Notes

- The live URL (`https://openai.com/index/hsp-gruppe`) returned HTTP 403 to
  both the WebFetch tool and direct `curl` with a browser user-agent —
  consistent with the same OpenAI-domain access difficulty documented in
  this corpus's other `openai.com/index/` extractions
  (`blog-openai-bbva-banking-transformation.md`,
  `blog-openai-endava-frontiers.md`,
  `blog-openai-codex-knowledge-work.md`). This source was retrieved
  successfully via the `r.jina.ai` reader proxy (`https://r.jina.ai/https://openai.com/index/hsp-gruppe`,
  HTTP 200), which returned the full rendered article as clean Markdown.
  All quotes in this note were copied character-for-character from that
  retrieved text.
- The article is self-contained — the only outbound link is to HSP
  GRUPPE's own corporate homepage (hsp-gruppe.de), which is not a
  substantive extraction target (a marketing homepage, not a related
  article or documentation page). No sub-pages were followed.
- The article does not name or describe "Kanzleipakt" beyond stating it
  shares the ChatGPT Enterprise workspace with HSP GRUPPE. This is a real
  gap in the source: the headline usage figures (84% WAU, 500,000+
  messages, 913 unique users) are not attributable to HSP GRUPPE alone,
  and the article gives no breakdown between the two organizations. This
  is flagged prominently in Claim 10 and should not be silently dropped
  when this source is cited elsewhere in the guide.
- Confidence overall set to "emerging": a first-party OpenAI case study
  with five named practitioner sources across multiple organizational
  levels (CEO down to individual tax advisor), specific and repeatedly
  self-hedged metrics (the article itself flags the revenue estimate as
  unrealized and the shared-workspace scoping caveat), but no independent
  verification, no disclosed survey methodology, and several claims
  (Claims 6, 8, 9, 11) describe pilots, explorations, or scenario
  estimates rather than completed, measured outcomes.
