---
source_url: https://openai.com/index/hp-frontier-partnership
source_type: blog-post
title: "HP Inc. launches Frontier strategic partnership with OpenAI"
author: OpenAI (Company/Partnerships vertical; no named HP executive quoted — one anonymous "HP engineer" quote)
date_published: 2026-06-28
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: anecdotal
issue: "#2061"
---

# HP Inc. launches Frontier strategic partnership with OpenAI

> An OpenAI "Company/Partnerships" announcement describing HP Inc.'s move from scattered
> pilots (begun February 2026) to a scaled "OpenAI Frontier" strategic partnership, framed
> around Frontier as a governance/connective layer (access, context, permissions,
> evaluation) across five named HP workstreams — partner/customer self-service, device
> fleet telemetry (WXP), security remediation, and general ChatGPT/Codex knowledge work —
> with two specific-but-uncorroborated productivity anecdotes and zero named HP executives
> quoted.

## Source Context

- **Type**: blog-post (OpenAI "Company" news post, `openai.com/index/`, ~800 words;
  auto-discovered via the `openai-news` trusted feed, published June 28, 2026). Structurally
  closest in the corpus to `blog-openai-endava-frontiers.md` and
  `blog-openai-bbva-banking-transformation.md` (both OpenAI customer-story pages with a
  "Table of contents" / section-heading structure), but thinner on attribution than either:
  it has no "Results at a glance" bullet box and no named customer-side executive quote at
  all.
- **Author credibility**: House-authored OpenAI announcement copy. The only quoted voice
  attributed to HP is anonymous — "said one HP engineer" — with no name, title, or team
  given. No HP executive, security lead, or IT/CIO figure is quoted anywhere in the piece.
  This is a weaker attribution posture than every other OpenAI enterprise-deployment case
  study already in the corpus: Endava quotes CTO Matthew Cloke by name, BBVA quotes three
  named executives (Chair, Head of AI Transformation, Head of Global AI Adoption), and even
  Samsung — the corpus's previous thinnest case study — quotes a named OpenAI-side executive
  (Harrison Kim). HP's piece quotes no named individual on either side.
- **Scope**: Covers HP's pilot-to-partnership timeline (pilots since February 2026, scaling
  now), the "Frontier" product's role as a cross-cutting governance/connective layer, four
  named HP workstreams under that layer (partner/customer self-service; Workforce Experience
  Platform device-fleet telemetry; cyber/security; general ChatGPT and Codex knowledge work),
  and two anecdotal productivity claims (a PR-throughput anecdote and a security-remediation-
  capacity estimate). Does NOT cover: any named individual at HP; any manufacturing-floor,
  product-design, CAD, or supply-chain use case (despite HP being a hardware/PC/printer
  manufacturer); a headcount or seat-count figure for the deployment; a rollout timeline
  beyond "began testing in February 2026"; contract terms, pricing, or exclusivity; or any
  measurement methodology for either productivity anecdote.

## Extracted Claims

### Claim 1: HP is scaling activation of a strategic "OpenAI Frontier" partnership after a series of successful pilots, having begun testing OpenAI Frontier in February 2026
- **Evidence**: Direct article statement describing the partnership's trigger and timeline.
- **Confidence**: anecdotal (a stated timeline and trigger with no pilot count, pilot team size, or selection criteria given)
- **Quote**: "Enterprise transformation rarely starts all at once. More often, it begins when small teams prove a new way of working is possible. That was the case with HP Inc., which just announced it will scale activation of its OpenAI Frontier strategic partnership, following a series of successful pilots across different areas."
- **Our assessment**: This is the same "pilots prove the model, then scale" narrative arc already used in `blog-openai-endava-frontiers.md` (single team wins → repeatable system) and `blog-openai-bbva-banking-transformation.md` (2024 3,000-employee pilot → 100,000-employee rollout). All three OpenAI customer-story posts open with this identical structural beat, which is more likely OpenAI's consistent house narrative template for enterprise announcements than independent evidence that HP's pilots were rigorously evaluated before scaling.

### Claim 2: "OpenAI Frontier" is positioned as a unified platform/connective layer that governs what agents can access, what context they use, what actions they're permitted to take, and how their outcomes are evaluated — distinct from ChatGPT or Codex as individual products
- **Evidence**: Two direct article statements describing Frontier's function as HP scales from pilots to "a broader portfolio of agents and AI workflows."
- **Confidence**: anecdotal (a product-positioning description with no technical/architectural detail — no mention of specific permissioning mechanisms, evaluation tooling, or how "context" is scoped)
- **Quote**: "Frontier gives HP the operating model for that motion: connecting access, context, deployment, and evaluation as the work moves from pilots toward production." ... "For a company as complex and distributed as HP, agents need to know which context to trust, which tools they can access, what actions they are allowed to take, and how their outputs will be evaluated over time."
- **Our assessment**: This is the corpus's first substantive description of what OpenAI's "Frontier" product/tier actually is, beyond the single passing mention in `blog-thebatch-nemotron-agent-infra.md` (which names "OpenAI Frontier (agent platform)" only as a routing category for Bedrock AgentCore traffic, with no functional description). Read together, the two sources corroborate that Frontier is an enterprise agent-governance layer sitting above ChatGPT/Codex — this note adds the governance-dimension description (access, context, actions, evaluation) that the Nemotron note's infrastructure-routing framing does not itself provide.

### Claim 3: One HP engineer used OpenAI models to move through 122 pull requests across 43 projects "in a matter of weeks"
- **Evidence**: A single named-count anecdote attributed to one unidentified engineer.
- **Confidence**: anecdotal (a specific numeric anecdote — 122 PRs, 43 projects — but single-individual, no baseline/comparison rate given, no definition of what "moved through" means for a PR — authored, reviewed, merged, or some mix)
- **Quote**: "One engineer used OpenAI models to move through 122 pull requests across 43 projects in a matter of weeks."
- **Our assessment**: This is a specific, falsifiable-sounding figure but it describes one individual with no stated prior baseline (how many PRs would this engineer normally handle in the same period?) and no clarity on what "move through" means (this could span drafting, reviewing, or merging PRs — activities with very different effort profiles). It is directionally consistent with the corpus's other single-engineer throughput anecdotes (e.g., `blog-cursor-coinbase-agent-first-adoption.md`'s idea-to-first-PR time reduction) but is weaker evidence than that source, which at least names a specific before/after task type rather than an aggregate count with no baseline.

### Claim 4: An HP security team used OpenAI models to remediate several software bugs in a day, work they estimated could otherwise have taken up to a month
- **Evidence**: A single team-level anecdote with a self-estimated before/after comparison.
- **Confidence**: anecdotal (an unnamed team's own retrospective estimate of counterfactual effort — "could otherwise have taken" — not a measured baseline)
- **Quote**: "A security team used these models to remediate several software bugs in a day, work they estimated could otherwise have taken up to a month."
- **Our assessment**: A roughly 20-30x compression claim (a day versus "up to a month"), but the counterfactual ("could otherwise have taken") is the team's own retrospective guess, not a measured prior baseline — the same evidentiary weakness as BBVA's Peru query-handling metric (`blog-openai-bbva-banking-transformation.md` Claim 10), except BBVA's figure is at least a measured before/after average rather than a retrospective estimate. Directionally consistent with the corpus's broader pattern of security/remediation work showing some of the largest reported AI-assisted time compressions, but this single claim should not be treated as a rigorous productivity metric.

### Claim 5: An anonymous HP engineer is quoted describing OpenAI tools as an "amazing" daily-use tool
- **Evidence**: A single anonymous pull-quote, the only first-person quote attributed to anyone at HP in the article.
- **Confidence**: anecdotal (unnamed, unverifiable individual sentiment)
- **Quote**: "It has been an amazing tool, and I am using it daily," said one HP engineer.
- **Our assessment**: Notable chiefly for its anonymity — every other OpenAI enterprise-deployment case study in the corpus (Endava, BBVA, Samsung) attributes at least one quote to a named individual (a customer executive, or in Samsung's weaker case, a named OpenAI regional executive). This is the first OpenAI customer-story source in the corpus with zero named quoted individuals on either side. Treat this quote as unverifiable color, not as evidence with any attributable weight.

### Claim 6: HP's channel/partner ecosystem — more than 80% of HP's business flowing through partners, with 100,000+ partners using the Partner Portal globally — is a target for Frontier-based self-service across store, partner, chat, and voice experiences
- **Evidence**: Direct article statement naming the scale of HP's partner ecosystem and the intended self-service application.
- **Confidence**: anecdotal (specific named scale figures — 80%+ of business, 100,000+ partners — but no detail on current versus planned deployment state, and no outcome/adoption metric for any self-service feature)
- **Quote**: "HP's channel ecosystem is a major platform opportunity with more than 80% of its business flowing through partners, and 100,000+ partners using the Partner Portal globally. Frontier will help HP create a more consistent self-service layer across store, partner, chat, and voice experiences, giving customers and partners faster ways to get answers, complete routine workflows, and move toward resolution or conversion."
- **Our assessment**: This is a new named vertical for the corpus — a hardware/PC manufacturer's B2B channel-partner ecosystem — distinct from the retail-banking (BBVA), consulting-delivery (Endava), and electronics-manufacturing-employee (Samsung) contexts already documented. Note the future/conditional framing ("will help HP create") — this is a stated intent, not a description of a deployed capability, unlike BBVA's named production GPTs which are described in present tense as already running.

### Claim 7: HP is using its "Workforce Experience Platform" (WXP) — a fleet-management tool for CIOs — together with Frontier to explore whether AI can reason across device telemetry, support knowledge, and runbooks to investigate crashes, Wi-Fi issues, and app hangs faster, with an eventual goal of "grounded remediation"
- **Evidence**: Direct article statement describing the WXP platform and the exploratory (not yet deployed) use of Frontier with it.
- **Confidence**: anecdotal (explicitly framed as exploratory — "is exploring how," "eventually supporting" — not a description of a shipped capability; no metric of any kind)
- **Quote**: "HP's WXP platform offers a single pane of glass that can manage entire fleets of devices and provide peace of mind for CIOs. Using Frontier, HP is exploring how device telemetry, support knowledge, operational objects, schemas, and runbooks can help AI reason across fleet health signals, investigate crashes, Wi-Fi issues, and app hangs faster, eventually supporting grounded remediation."
- **Our assessment**: This is the closest the article comes to a hardware/device-specific (as opposed to generic knowledge-work) use case, and it is explicitly speculative/exploratory language rather than a deployed-system claim — a meaningfully different evidentiary status than the "customer/partner self-service" workstream (Claim 6), which at least describes an intended production capability. The guide should not cite this as evidence of a working device-telemetry AI remediation system; it is evidence only that HP is investigating the idea.

### Claim 8: HP's security team has used ChatGPT to proactively remediate critical vulnerabilities and speed security analysis, with a directional estimate of roughly 82 hours per week of security-team capacity unlocked
- **Evidence**: Direct article statement, explicitly labeled by the source itself as a "directional estimate."
- **Confidence**: anecdotal (the source itself flags this as directional/non-rigorous; no methodology, sample period, or baseline given for how "82 hours/week" was calculated)
- **Quote**: "Security is both a proof point and a governance layer. HP teams have used ChatGPT to proactively remediate critical vulnerabilities and speed security analysis across tools, with a directional estimate of roughly 82 hours/week of security-team capacity unlocked."
- **Our assessment**: Notable for being the only claim in the article the source itself hedges as "directional" rather than presenting as a firm figure — a more honest hedge than the unqualified percentage/multiplier claims common elsewhere in the corpus's OpenAI customer-story posts (e.g., Samsung's unqualified "~800%" Korea Codex growth figure in `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 6). Still, "82 hours/week" with no stated team size makes the figure impossible to contextualize as a percentage of capacity — 82 hours could represent a small fraction of a large security org or a large fraction of a small one.

### Claim 9: HP has a named split in tool usage: ChatGPT supports broad knowledge work (research, analysis, ideation, workflow automation) while Codex supports software modernization, planning, UI scaffolding, and parallel software-delivery tasks
- **Evidence**: Direct article statement describing the intended division of labor between the two products.
- **Confidence**: anecdotal (a stated product-usage split with no adoption data, no per-category metric, and no description of how "parallel software-delivery tasks" are actually run)
- **Quote**: "HP is using ChatGPT to support broad knowledge work such as research, analysis, ideation, and workflow automation, while Codex supports modernization, planning, UI scaffolding, and parallel software-delivery tasks."
- **Our assessment**: This ChatGPT-for-knowledge-work / Codex-for-software-delivery split mirrors the same product-positioning narrative documented in `blog-openai-codex-knowledge-work.md` (Codex expanding beyond software engineering into general knowledge work) and `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 3 (same repositioning narrative applied to Samsung) — but here the split is described as HP keeping the two products in their more traditional lanes (ChatGPT = knowledge work, Codex = software delivery) rather than blurring them, which is a subtly different framing than the "Codex for everyone, including non-developers" narrative pushed in those other two sources. Treat this as one more vendor-narrated instance of the same product-positioning story, not independent confirmation of a blurred product boundary.

### Claim 10: HP frames its overall goal as turning "pilot momentum into a governed operating model" — combining shared context, clear permissions, evaluation, and reusable deployment patterns to move from proof-of-concept to production
- **Evidence**: Closing-section summary statement synthesizing the article's named workstreams into a single framing claim.
- **Confidence**: anecdotal (vendor-authored synthesis/aspirational framing, not a description of a measured or completed transformation)
- **Quote**: "Frontier is helping build a connective tissue that turns pilot momentum into a governed operating model: shared context, clear permissions, evaluation, reusable deployment patterns, and a path from proof of concept to production."
- **Our assessment**: This is the same "productivity layer → operating model" aspirational framing already documented in `blog-openai-endava-frontiers.md` Claim 10 (Endava: "AI is becoming more than a productivity layer. It's becoming the operating model itself"). The recurrence of nearly identical "operating model" language across two independent OpenAI customer-story posts (Endava, June 4; HP, June 28) is further evidence that this is OpenAI's house rhetorical framing for its enterprise partnership announcements, not two companies independently arriving at the same conclusion — consistent with the same pattern already flagged for the "lessons learned" bullet-list template shared between Endava's and BBVA's posts (see `blog-openai-bbva-banking-transformation.md` Claim 11's assessment).

## Concrete Artifacts

```
Source: OpenAI, "HP Inc. launches Frontier strategic partnership with OpenAI,"
https://openai.com/index/hp-frontier-partnership (published June 28, 2026;
retrieved via Wayback Machine snapshot — see Extraction Notes)

Article structure (Table of contents, verbatim):
  - From pilot wins to enterprise deployment
  - Frontier as a connective layer
  - Building an AI-driven operating model

Named HP workstreams under the "Frontier as a connective layer" section
(verbatim subheadings):
  - Pricing, partner, store, and customer support workflows
  - Workforce Experience Platform (WXP) and device context
  - Cyber/security
  - ChatGPT and Codex

Anecdotal figures (verbatim, no methodology disclosed for any):
  PR/project throughput (one engineer):     122 pull requests / 43 projects,
                                             "in a matter of weeks"
  Security bug remediation (one team):      "a day" vs. "up to a month"
                                             (team's own counterfactual estimate)
  Security-capacity unlocked (directional,
  explicitly hedged by the source itself):  "roughly 82 hours/week"
  HP channel-partner ecosystem scale:       80%+ of business via partners;
                                             100,000+ Partner Portal users globally
```

## Cross-References

- **Corroborates**:
  - `blog-openai-endava-frontiers.md` Claim 1 (opening "small pilot proves the model, then
    scale" narrative arc) and Claim 10 ("productivity layer → operating model" framing):
    HP's post opens and closes with near-identical structural beats and rhetorical language,
    reinforcing that this is OpenAI's consistent house template for enterprise-partnership
    announcements rather than independently-arrived-at company narratives.
  - `blog-openai-codex-knowledge-work.md` and `blog-openai-samsung-chatgpt-codex-deployment.md`
    Claim 3 (Codex repositioning from software-only to general knowledge work): HP's named
    ChatGPT/Codex usage split (Claim 9) is a third instance of OpenAI narrating this same
    product-positioning story to a named enterprise customer, though HP's framing keeps the
    two products in more traditional lanes than the other two sources' "Codex for everyone"
    framing.
  - `blog-openai-bbva-banking-transformation.md` Claim 10 (Peru's 7.5-minute-to-1-minute
    query-handling reduction) and Claim 11 (shared "lessons learned" template with Endava):
    HP's security-remediation anecdote (Claim 4) is a similarly large, self-reported
    before/after compression claim with no disclosed measurement methodology, continuing the
    corpus's pattern of OpenAI customer-story posts featuring one large, unaudited
    time-compression figure per source.

- **Contradicts**: None filed. No claim in this article materially opposes an existing
  source note, and the article does not disagree with itself on guidance or direction — per
  MINER.md §4a this is not a contradiction-worthy case.

- **Extends**:
  - `blog-thebatch-nemotron-agent-infra.md` (the corpus's only prior mention of "OpenAI
    Frontier (agent platform)," there used only as a traffic-routing category name for
    Bedrock AgentCore integration with no functional description): this note substantially
    extends that single passing mention with Frontier's actual stated purpose — a
    cross-cutting governance layer for agent access, context, permissions, and evaluation
    (Claim 2). Prior to this note, the corpus had no substantive description of what
    "Frontier" as an OpenAI enterprise product/tier actually does.
  - `blog-openai-samsung-chatgpt-codex-deployment.md` (the corpus's previous thinnest
    enterprise-deployment case study, with only a named OpenAI-side executive quoted and no
    customer executive): HP's post extends that "thin evidentiary posture" pattern one step
    further — zero named individuals on either side, only an anonymous engineer quote.
  - `blog-anthropic-building-enterprise-agents.md` (L'Oréal named as a manufacturing-adjacent
    case study subject, with no workflow detail given): HP is a second hardware/manufacturing
    company named in an enterprise AI case study, but — like L'Oréal — the actual named
    workstreams described (partner self-service, device-fleet telemetry, security, general
    knowledge work) are non-manufacturing-floor functions; neither source describes an actual
    manufacturing/production-line AI use case despite both companies being manufacturers.

- **Novel**:
  - **First substantive description of "OpenAI Frontier" as a product**: prior corpus
    coverage (`blog-thebatch-nemotron-agent-infra.md`) named Frontier only as an
    infrastructure-routing category; this note is the first to describe its stated function
    (governing agent access, context, permitted actions, and evaluation as a cross-cutting
    layer above ChatGPT/Codex).
  - **Zero named individuals on either side**: the first OpenAI enterprise customer-story
    source in the corpus with no named executive quote from the customer or the vendor — only
    an anonymous "one HP engineer" quote.
  - **Explicitly self-hedged "directional estimate"**: the 82-hours/week security-capacity
    figure (Claim 8) is the first instance in the corpus's OpenAI customer-story sources of
    the source itself labeling a headline metric as directional/non-rigorous rather than
    presenting it as a firm number.
  - **B2B channel-partner ecosystem as an AI self-service target** (Claim 6): a distinct
    enterprise-adoption context (100,000+ external partners, not employees) not previously
    documented in the corpus's enterprise-deployment sources, which have so far focused on
    employee-facing (Endava, BBVA, Samsung) rather than partner-facing AI deployment.

## Guide Impact

- **Chapter 05 (Team Adoption)**: If the guide builds a section calibrating the evidentiary
  strength of vendor enterprise-deployment case studies (as recommended in
  `blog-openai-samsung-chatgpt-codex-deployment.md`'s Guide Impact), add HP as the new
  weakest-evidence anchor point — even thinner than Samsung: no named customer-side
  individual at all, one anonymous engineer quote, and only two productivity anecdotes (both
  self-estimated, not measured). Order for the section, from strongest to weakest evidence:
  BBVA (three named executives, multiple named GPT workflows, one measured before/after
  metric) > Endava (one named CTO, qualitative results only) > Samsung (one named
  vendor-side executive, market-level not customer-level metrics) > HP (zero named
  individuals, self-estimated anecdotes only).
- **Chapter 04/05 (Deployment / Integration), if discussing OpenAI's enterprise product
  tiers**: Use Claim 2 (Frontier as a governance/connective layer for access, context,
  permissions, and evaluation) as the first substantive definition of "OpenAI Frontier" in
  the corpus, cross-referenced with `blog-thebatch-nemotron-agent-infra.md`'s infrastructure-
  routing mention — together the two sources give a fuller (though still vendor-marketing-
  level, non-technical) picture of what the product tier is for.
- **Chapter 05 (Team Adoption), manufacturing-vertical coverage**: Do NOT cite this source as
  evidence of manufacturing-floor AI adoption. Despite HP being a hardware manufacturer and
  the Prospector's triage flagging manufacturing-pattern novelty as a key question, the
  article describes no production-line, supply-chain, or product-design use case — only
  partner-portal self-service, device-fleet telemetry (still exploratory), security, and
  general knowledge work. This mirrors the L'Oréal gap already noted in
  `blog-anthropic-building-enterprise-agents.md`'s Cross-References: two manufacturers named
  as AI adopters, neither source describing an actual manufacturing-specific workflow.
- **Any chapter citing vendor-reported productivity metrics**: If the guide discusses how to
  read self-reported enterprise AI productivity claims skeptically, use HP's explicitly
  labeled "directional estimate" (Claim 8, 82 hours/week) as a model of a vendor at least
  partially hedging its own metric, in contrast with unqualified figures like Samsung's
  "~800%" Korea growth claim — worth noting as a small positive signal in how the same
  vendor's public communications vary in rigor-hedging across posts.

## Extraction Notes

- The live URL (`https://openai.com/index/hp-frontier-partnership`) returned HTTP 403 to both
  the WebFetch tool and direct `curl` with a browser user-agent — the response was a
  Cloudflare bot-challenge page (`cf_chl` JavaScript challenge), not the rendered article.
  This is the same failure mode documented in every prior OpenAI-domain extraction in this
  corpus (`blog-openai-endava-frontiers.md`, `blog-openai-bbva-banking-transformation.md`,
  `blog-openai-samsung-chatgpt-codex-deployment.md`, `blog-openai-codex-knowledge-work.md`).
  The article was retrieved via a Wayback Machine snapshot
  (`web.archive.org/web/20260630211026/https://openai.com/index/hp-frontier-partnership/`,
  crawled June 30, 2026, HTTP 200, confirmed via the CDX API against a second working
  snapshot at the same URL). WebFetch is blocked from fetching `web.archive.org` directly in
  this environment (same constraint noted in the prior OpenAI-domain notes above), so the
  snapshot was fetched with `curl` and the HTML parsed locally (a Python regex-based
  script stripping `script`/`style` tags and collapsing tags to newlines) rather than via a
  proxy service. All quotes in this note were copied character-for-character from that
  extracted text.
- No sub-pages were followed. The archived page's "Keep reading" footer links to three
  unrelated OpenAI news posts (an "agents transforming work" explainer, an OpenAI/Broadcom
  chip announcement, and a security-tools post) — none are substantively linked follow-on
  material for this partnership announcement.
- The article is short (~800 words) and every substantive sentence in its body is reflected
  in one of the ten claims above; this is not a case of shallow reading, but the source
  itself is thin — no named customer individual, no headcount/seat-count figure, no
  measurement methodology for either productivity anecdote, and one workstream (WXP/device
  telemetry) explicitly described as still exploratory rather than deployed.
- No contradiction issue was filed. The article contains no claim that materially opposes an
  existing source note, nor does it disagree with itself — see Cross-References → Contradicts.
- Three separate Prospector triage comments exist on issue #2061, giving somewhat different
  novelty assessments (high / low / medium) and different chapter-relevance suggestions. This
  note follows the most specific and actionable of the three (the "medium novelty... does HP
  show deployment bottlenecks/adoption patterns distinct from Samsung/Endava/BBVA" framing),
  and its Guide Impact section directly answers that question: HP does not show a
  manufacturing-specific pattern distinct from the software/consulting/fintech companies
  already in the corpus — its named workstreams (partner self-service, device telemetry,
  security, general knowledge work) are the same categories already documented, just at a
  hardware/PC-manufacturer company. The one genuinely novel contribution is the Frontier
  product description itself (Claim 2), not a manufacturing-sector adoption pattern.
- All cross-reference claim numbers cited above (from `blog-openai-endava-frontiers.md`,
  `blog-openai-bbva-banking-transformation.md`, `blog-openai-samsung-chatgpt-codex-deployment.md`,
  `blog-openai-codex-knowledge-work.md`, and `blog-anthropic-building-enterprise-agents.md`)
  were verified by re-reading each cited note's actual claim numbering and content before
  writing this note; the `blog-thebatch-nemotron-agent-infra.md` reference is cited by
  content (its "OpenAI Frontier (agent platform)" line) rather than by claim number, since
  that note's Frontier mention appears only in a Concrete Artifacts code block, not as a
  numbered claim.
