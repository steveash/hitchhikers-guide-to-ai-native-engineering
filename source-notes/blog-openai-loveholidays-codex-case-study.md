---
source_url: https://openai.com/index/loveholidays
source_type: blog-post
title: "How loveholidays is making everyone a builder with Codex"
author: OpenAI (customer case study, featuring Dmitri Lerko, Head of Engineering, and Mike Jones, CTO, loveholidays)
date_published: 2026-08-26
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: anecdotal
issue: "#3194"
---

# How loveholidays is making everyone a builder with Codex

> An OpenAI customer case study describing how loveholidays, a European online
> travel agent, built Codex-backed self-service platforms (a "Search
> Playground" for customer-experience prototyping and codified workflows for
> Data Platform/infrastructure changes) that let product managers, designers,
> and commercial staff ship code and deployments directly — headlined by
> AI-assisted code changes growing from 7% to 79% of all changes in a year
> with engineering headcount held flat, alongside concrete Data Platform
> success-rate and cost-savings figures.

## Source Context

- **Type**: blog-post (OpenAI customer case study, `openai.com/index/loveholidays`,
  published August 26, 2026; ~700 words). Structured identically to other
  OpenAI customer-story posts already in the corpus: a company metadata block
  (Company size: Enterprise, Region: Europe & UK, Industry: Travel,
  Technology, Products: Codex), a four-stat headline block, four named
  sub-sections, and two named-executive voices throughout the body. Not a
  technical or engineering blog post — no code, config, or architecture
  diagrams are shown.
- **Author credibility**: Written and published by OpenAI, not loveholidays,
  as promotional customer-success content — OpenAI has a direct commercial
  incentive to present Codex favorably. Two individuals are named and quoted:
  Dmitri Lerko, Head of Engineering at loveholidays (five quotes across the
  piece), and Mike Jones, CTO at loveholidays (four quotes). Both are senior,
  named practitioners at the featured company, which is a stronger sourcing
  posture than the single-vendor-quote pattern in
  `blog-openai-samsung-chatgpt-codex-deployment.md` (only an OpenAI employee
  quoted), but every quote was still selected by OpenAI for a promotional
  piece, and no other loveholidays employee (e.g., the marketing team member
  who built the "Crisps from Abroad" microsite, or a Data Platform engineer)
  is named or quoted directly.
- **Scope**: Covers loveholidays' company profile (eight European markets,
  "60 trillion package combinations" processed daily), the "Search Playground"
  internal platform for non-engineer prototyping of customer experiences, a
  Data Platform/infrastructure self-service workflow built on codified
  best-practices, four headline adoption/success metrics, two cost-savings
  figures, and closing framing around "Codex is becoming a single control
  plane." Does NOT cover: methodology for any percentage figure, the
  underlying prompt(s) or Codex configuration used to build Search Playground,
  headcount or team-size numbers (only "engineering headcount has remained
  broadly flat"), a rollout timeline, technical detail on how "best practices,
  instructions, and validations" are actually encoded into Codex-guided
  workflows, or any account from a non-engineer who used these tools
  first-hand.

## Extracted Claims

### Claim 1: AI-assisted code changes at loveholidays grew roughly 11x in a year — from about 7% to 79% of all code changes — while deployment frequency rose 73% and engineering headcount stayed broadly flat
- **Evidence**: Headline stat block (the "11x" figure) plus a restated, more precise version in the case study's "More software, without more engineers" section.
- **Confidence**: anecdotal (a single vendor-selected company's self-reported percentages; no definition given for what counts as an "AI-assisted code change," no absolute headcount or change-volume numbers, no independent audit)
- **Quote**: "A year ago, around 7% of its code changes were AI-assisted. Today, that figure is 79%." ... "Over the same period, deployments have increased 73%, while engineering headcount has remained broadly flat."
- **Our assessment**: This is the article's central adoption-trajectory claim, and the three numbers (79% AI-assisted changes, +73% deployment frequency, flat headcount) are internally consistent with a capacity-expansion story rather than a headcount-reduction story — the piece frames Codex as letting the same-sized team (plus newly-enabled non-engineers) ship more, not as enabling layoffs. As with the Asana and Notion case studies, the percentages are self-reported with no disclosed measurement methodology (what counts as "AI-assisted"?), so the direction (steep AI-assistance growth, flat headcount) should be trusted more than the precision of any single figure.

### Claim 2: loveholidays' Head of Engineering frames the shift as organizational, not just technical — "everybody is a builder," with making application/infrastructure changes and deploying code no longer restricted to engineers
- **Evidence**: Direct attributed quote from Dmitri Lerko, Head of Engineering, loveholidays, in the article's opening section.
- **Confidence**: anecdotal (a single executive's characterization of organizational change; no data given on what fraction of deployments are now made by non-engineers)
- **Quote**: "Everybody is a builder," says Dmitri Lerko, Head of Engineering at loveholidays. "Making changes to our applications, infrastructure, and deploying code is no longer an engineering-only activity. Product managers, designers, and commercial stakeholders are driving value and making deployments."
- **Our assessment**: This is the article's thesis statement, later illustrated with two concrete mechanisms (Search Playground, Claim 3; codified Data Platform workflows, Claim 5). The claim that product managers, designers, and commercial stakeholders are "making deployments" — not just requesting or reviewing changes — is a stronger and more specific claim than generic "AI empowers non-technical staff" framing found elsewhere in the corpus; it names deployment (a production action, not just prototyping) as something non-engineers now do directly.

### Claim 3: loveholidays' engineers built "Search Playground," an internal platform combining the company's design system, frontend technologies, and Codex, that has been used to develop more than ten new customer-facing search experiences — most built by non-engineers, with at least three shipped to the live website
- **Evidence**: Narrative description of the platform and its output, in the "From an idea to a live customer experience" section.
- **Confidence**: anecdotal (self-reported adoption count for a single internal platform, no total addressable count of experiments attempted, no failure/abandonment rate disclosed for the other "more than ten" not yet in production)
- **Quote**: "Its engineers created Search Playground using the company's design system, frontend technologies, and Codex. It gives people across the business a way to turn an idea into a working customer experience, gather feedback, and test whether it delivers value." ... "More than ten new search experiences have already been developed through the Playground. Most were built by non-engineers, and at least three are now running on the loveholidays website."
- **Our assessment**: This is the most concrete artifact in the piece — a named internal platform (not just "Codex" used ad hoc) purpose-built by engineers to give a governed self-service surface to non-engineers, combining an existing design system with Codex. It is structurally similar to the "paved roads" pattern (pre-audited, governed self-service platforms as the sustainable response to ad hoc AI usage) argued for in `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` — Search Playground is a concrete, shipped instance of exactly that pattern, built proactively by loveholidays' own engineers rather than described as a hypothetical governance response to shadow IT (see Cross-References).

### Claim 4: A marketing team used Codex and Search Playground to build an interactive competition microsite ("Crisps from Abroad") themselves in hours, work that previously would have gone to an external agency at added cost and time
- **Evidence**: Named example within the Search Playground section, describing a specific marketing activation.
- **Confidence**: anecdotal (single named example, self-reported build time — "in hours" — with no comparison baseline for how long the same microsite would have taken via the previous agency workflow)
- **Quote**: "For its recent Crisps from Abroad activation, the team wanted an interactive microsite to gather entries for a competition and share holiday inspiration. Previously, it would have relied on an external agency to design and develop a standalone digital experience, adding cost and time. Using Codex and Search Playground, the team built the experience itself in hours, while maintaining loveholidays' existing design system."
- **Our assessment**: This is a specific, named, checkable instance of Claim 3's broader pattern — a non-engineering business function (marketing) both building and shipping a customer-facing digital experience without engineering or external-agency involvement, while still conforming to the company's existing design system (i.e., the self-serve output was not a one-off, off-brand artifact). It is comparable in kind to the "insourcing work that used to go to an outside vendor/agency" pattern, though this is the only instance of that specific pattern in the corpus tied to a coding-agent tool rather than a general AI writing/design tool.

### Claim 5: loveholidays' engineering teams encode their best practices, instructions, and validations into Codex-guided workflows so that non-specialist employees can self-serve Data Platform and infrastructure changes with specialist expertise available "on tap, 24/7," rather than escalating to a specialist engineer
- **Evidence**: Narrative description of the mechanism plus a direct quote from Dmitri Lerko, in the "Putting specialist engineering expertise on tap" section.
- **Confidence**: anecdotal (mechanism description and single-executive characterization; no detail on what the encoded "best practices, instructions, and validations" actually consist of technically — no example workflow, skill file, or check is shown)
- **Quote**: "Engineering teams encode their best practices, instructions, and validations into workflows that Codex can guide other users through. Instead of needing to understand every underlying system, employees can focus on what they're trying to accomplish while Codex helps propose a change, run checks, and guide it through the release process." ... "We codify all the best practices. We codify validations, and continuously improve them as reality changes," says Lerko. "The expertise of our data and infrastructure engineers is available through Codex—so anybody self-serving their infrastructure or data needs gets that expertise on tap, 24/7."
- **Our assessment**: This describes a specific architectural pattern — encoding specialist procedural knowledge into agent-guided workflows so non-specialists can self-serve — that is conceptually the same mechanism `blog-anthropic-selfservice-data-analytics.md` documents in much greater technical depth for Anthropic's own internal analytics agents (skills as the decisive accuracy lever, a four-layer stack, canonical datasets). This source gives no comparable technical detail (no skill file structure, no accuracy ablation, no failure-mode taxonomy) — it should be read as a second vendor's customer confirming the same high-level pattern (codify specialist knowledge into agent-navigable workflows to enable safe non-specialist self-service) works in production, not as new technical detail on how to build it. See Cross-References.

### Claim 6: Successful AI-assisted changes to loveholidays' Data Platform rose from 58% to 93% over the past year, with four times as many Data Platform changes completed per support request; success across broader self-service infrastructure workflows rose from 63% to 90%
- **Evidence**: Two named before/after percentage metrics in the "Putting specialist engineering expertise on tap" section, plus the "93%" and "4x" figures repeated in the headline stat block.
- **Confidence**: anecdotal (self-reported before/after percentages with no disclosed definition of "successful" change, no absolute volume of changes or support requests, no independent audit)
- **Quote**: "Successful AI-assisted changes to loveholidays' Data Platform have risen from 58% to 93% over the last year. At the same time, the team is seeing four times as many Data Platform changes for every support request." ... "Across its broader self-service infrastructure workflows, success has increased from 63% to 90%."
- **Our assessment**: These are the most specific, quantified metrics in the source — two distinct before/after success-rate figures (Data Platform: 58%→93%; broader self-service infrastructure: 63%→90%) plus a support-request-deflection ratio (4x). Unlike Claim 1's aggregate "AI-assisted changes" figure, these numbers are scoped to a specific, named system (the Data Platform and adjacent self-service infrastructure workflows described in Claim 5), which makes them somewhat more checkable in principle, though still entirely self-reported with no methodology disclosed for how "success" is measured (deployment without rollback? no incident? user-reported satisfaction?).

### Claim 7: loveholidays' CTO frames the productivity gain as elevating engineers' work rather than replacing it — engineers move from being handed a solution to implement toward engaging directly with the underlying business problem
- **Evidence**: Direct attributed quote from Mike Jones, CTO, loveholidays, following the Data Platform metrics in Claim 6.
- **Confidence**: anecdotal (single executive's characterization of how engineers' day-to-day work has changed; no survey or data on engineer time allocation before/after)
- **Quote**: "The more work you can hand off to AI, the more your job elevates. Your job isn't to be handed a solution and implement it anymore. You have to get involved in the business problem."
- **Our assessment**: This is a specific, quotable articulation of the "role moves up the stack" pattern already documented from a different company and vendor in `blog-anthropic-ai-native-engineering-org.md` (Claim 1: verification, code review, and security replaced code-writing as the primary bottleneck) and `blog-openai-notion-codex-case-study.md` (Claim 8: an engineer's own time shifts from hand-writing code to writing specs). Jones' framing is more explicitly about problem ownership than either — "implement a handed-down solution" versus "get involved in the business problem" — a distinction about where in the problem-solving process the engineer's judgment is applied, not just what artifact they produce.

### Claim 8: loveholidays' CTO states the company deliberately measures AI usage against business outcomes rather than adoption alone, framing technology access as a means rather than the goal
- **Evidence**: Direct attributed quote from Mike Jones, CTO, loveholidays, in the "More software, without more engineers" section, immediately following the 7%→79% and deployment-growth figures.
- **Confidence**: anecdotal (a stated organizational philosophy from a single executive; no description of the specific outcome metrics tracked beyond the two cost-savings figures in Claim 9)
- **Quote**: "Technology is just a means to an end," says Jones. "It's not about the technology itself; it's about the impact it has. We're intentional about not just giving people access to tools, but helping them solve business problems—and measuring the impact."
- **Our assessment**: This is a self-aware caveat about how to read the article's own adoption statistics — the CTO explicitly warns against treating tool-access or usage-rate figures (like the 79% AI-assisted-changes figure) as the actual measure of success, and points instead to outcome measurement (of which Claim 9's cost-savings figures are the concrete example given). This is a notable, if brief, on-the-record instance of a vendor case study's own featured executive cautioning against exactly the kind of headline-adoption-number over-reading that this note's other claims require flagging.

### Claim 9: loveholidays' Data Engineering team reduced cloud storage costs by around £36,000 a year and is saving approximately another £100,000 annually by reducing data-processing waste, attributed to capacity freed up by the self-service Data Platform workflows
- **Evidence**: Two named dollar-figure outcomes, presented as the concrete instance of the outcome-measurement philosophy stated in Claim 8.
- **Confidence**: anecdotal (two specific, named cost figures — the most concrete financial claim in the piece — but self-reported, with no breakdown of how each figure was calculated, over what baseline, or independently audited)
- **Quote**: "With more capacity to tackle optimisation work that previously carried too high an opportunity cost, loveholidays' Data Engineering team has reduced cloud storage costs by around £36,000 a year and is saving approximately another £100,000 annually by reducing data-processing waste."
- **Our assessment**: This is the article's only hard financial figure (contrast the $12K-vs-$6M cost comparison in `blog-openai-asana-codex-case-study.md` Claim 2, which is a project-cost comparison, not a recurring operational savings figure). The framing — savings enabled by "capacity... freed up" from routine work — directly connects back to Claim 6's support-request-deflection ratio (4x more Data Platform changes per support request) and Claim 7's "job elevates" framing: less time on routine self-serve support translates into engineer time available for the kind of optimization work that produced these two savings figures. Still a single company's unaudited numbers, but concrete and specific rather than a bare percentage.

### Claim 10: loveholidays' Head of Engineering describes a shift in what the organization now considers achievable — "what used to be too hard is now ordinary" — framing this as a continuing trend rather than a one-time step change
- **Evidence**: Direct attributed quote from Dmitri Lerko, closing the "More software, without more engineers" section.
- **Confidence**: anecdotal (a qualitative, forward-looking characterization from a single executive; not a measured claim)
- **Quote**: "We're noticing that what used to be too hard is now ordinary," says Lerko. "The implication is that what's too hard now will become more ordinary."
- **Our assessment**: A qualitative companion to Claim 1's quantitative growth figures — the claim is explicitly framed as an expectation of continued acceleration ("what's too hard now will become more ordinary"), not just a description of gains already banked. This is closer to a forward-looking belief than an evidenced trend; treat it as color illustrating how the company's own leadership narrates the trajectory, not as an independent data point.

### Claim 11: loveholidays' Head of Engineering describes Codex as becoming a "single control plane" — one shared interface across engineers, data scientists, and business users, removing the need to train each group on a different tool
- **Evidence**: Direct attributed quote from Dmitri Lerko in the closing "Building the general intelligence for travel" section.
- **Confidence**: anecdotal (a single executive's architectural characterization of the tool's role in the organization; no detail on what other tools this "single interface" is replacing, or how many distinct tools different roles previously had to learn)
- **Quote**: "Codex is becoming a single control plane—a single interface shared by engineers, data scientists and the business," says Lerko. "There's a lot of power in that, because you no longer need to teach everyone a different tool."
- **Our assessment**: This is a distinct claim from Claim 2's "everybody is a builder" — that claim is about who can act (deploy, build), while this claim is about tooling consolidation (one interface instead of many role-specific tools). The "single control plane" framing is a specific, quotable metaphor worth tracking if it recurs in other vendor case studies, but here it is asserted without detail on what the prior, fragmented tooling landscape looked like.

### Claim 12: loveholidays frames its platform strategy as building "the general intelligence for travel" by combining its existing technology and its people's expertise, and using AI/Codex specifically to make both more broadly accessible across the business
- **Evidence**: Direct attributed quote from Mike Jones, CTO, loveholidays, presented early in the article as the strategic frame for everything that follows, and restated in the closing section.
- **Confidence**: anecdotal (a stated company strategy/vision from a single executive; a marketing framing more than a falsifiable claim)
- **Quote**: "At loveholidays, our platform vision is to build the general intelligence for travel. That's bringing together the great technology we have with our people's expertise—and democratising that with AI and Codex."
- **Our assessment**: This is the article's overarching strategic frame, into which every other claim in this note slots as a supporting example (Search Playground democratizes customer-experience-building expertise; the Data Platform workflows democratize infrastructure/data expertise). It is company messaging rather than an independently checkable claim, but it is useful as the explicit organizing thesis a reader should recognize before weighing the more specific claims above — the article is structured to build toward this line, not to report it as a discovered finding.

## Concrete Artifacts

### Case study metadata and headline stat block

```
Source: https://openai.com/index/loveholidays (August 26, 2026)

Company size: Enterprise
Region:       Europe & UK
Industry:     Travel, Technology
Products:     Codex

Headline stats:
  11x   AI-assisted code changes have grown from 7% to 79% in a year
  73%   increase in AI-assisted deployment frequency without growing the
        engineering team
  93%   Data Platform change success, up from 58%
  4x    More Data Platform changes per support request
```

### Company description — verbatim

```
Source: https://openai.com/index/loveholidays (August 26, 2026)

"loveholidays is a leading online travel agent operating across eight
European markets, using its technology to process 60 trillion package
combinations every day to help millions of people find their perfect
holiday. Behind that scale is a technology platform the company has spent
years building to make finding and booking a holiday faster and more
flexible."
```

### Dmitri Lerko quotes (Head of Engineering, loveholidays) — verbatim, in order of appearance

```
Source: https://openai.com/index/loveholidays (August 26, 2026)
Attribution: Dmitri Lerko, Head of Engineering, loveholidays

1. "Everybody is a builder. Making changes to our applications,
   infrastructure, and deploying code is no longer an engineering-only
   activity. Product managers, designers, and commercial stakeholders are
   driving value and making deployments."

2. "We wanted to decouple our ability to trial new ideas from actual
   engineering time."

3. "We codify all the best practices. We codify validations, and
   continuously improve them as reality changes. The expertise of our data
   and infrastructure engineers is available through Codex—so anybody
   self-serving their infrastructure or data needs gets that expertise on
   tap, 24/7."

4. "We're noticing that what used to be too hard is now ordinary. The
   implication is that what's too hard now will become more ordinary."

5. "Codex is becoming a single control plane—a single interface shared by
   engineers, data scientists and the business. There's a lot of power in
   that, because you no longer need to teach everyone a different tool."
```

### Mike Jones quotes (CTO, loveholidays) — verbatim, in order of appearance

```
Source: https://openai.com/index/loveholidays (August 26, 2026)
Attribution: Mike Jones, CTO, loveholidays

1. "At loveholidays, our platform vision is to build the general
   intelligence for travel. That's bringing together the great technology
   we have with our people's expertise—and democratising that with AI and
   Codex."

2. "The more work you can hand off to AI, the more your job elevates. Your
   job isn't to be handed a solution and implement it anymore. You have to
   get involved in the business problem."

3. "Technology is just a means to an end. It's not about the technology
   itself; it's about the impact it has. We're intentional about not just
   giving people access to tools, but helping them solve business
   problems—and measuring the impact."
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-openai-asana-codex-case-study.md`,
`blog-openai-notion-codex-case-study.md`,
`blog-anthropic-ai-native-engineering-org.md`,
`blog-anthropic-selfservice-data-analytics.md`, and
`blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-openai-codex-knowledge-work.md` Claim 2 ("Knowledge workers now
    represent about 20 percent of Codex users and are adopting it more than
    3 times as fast as developers") and Claim 5 (72% of knowledge-worker
    Codex users produce artifacts weekly; role boundaries between "developer"
    and "knowledge worker" task categories have blurred): this source's
    Claim 2 ("everybody is a builder") and Claim 3 (Search Playground built
    mostly by non-engineers) are a single named enterprise customer's
    concrete illustration of that aggregate, self-reported OpenAI usage
    trend — one company describing the same developer/non-developer
    boundary dissolution that OpenAI's own telemetry report claims is
    happening in aggregate.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 8 ("Roles blurred in
    the AI-native team — PMs now code, engineers do content and design; the
    traditional technical/non-technical division is dissolving") and
    `blog-openai-notion-codex-case-study.md` Claim 4/Claim 10 (a Notion
    manager returning to hands-on coding after 5+ years): this source's
    Claim 2 and Claim 3 are a third, independently-tooled company (Anthropic
    and its own team using Claude Code; Notion using Codex; loveholidays
    using Codex) making structurally similar claims about role boundaries
    dissolving between engineers and non-engineers — strengthening the case
    that this is a cross-vendor, cross-company organizational pattern rather
    than one vendor's narrative.
  - `blog-anthropic-selfservice-data-analytics.md` (four-layer "agentic data
    stack" — data foundations, sources of truth, skills, validation —
    reaching 95% automation at ~95% accuracy for Anthropic's own internal
    analytics agents; Claim 6: skills, not raw retrieval, are the decisive
    accuracy lever): this source's Claim 5 (loveholidays codifying "best
    practices, instructions, and validations" into Codex-guided workflows so
    non-specialists can self-serve Data Platform changes) is a second
    vendor's customer confirming the same high-level architectural pattern —
    encode specialist procedural knowledge so an agent can guide
    non-specialists through it — in production. This source gives far less
    technical detail than the Anthropic post (no skill-type taxonomy, no
    accuracy ablation, no failure-mode analysis), so it should be read as
    corroborating evidence that the pattern generalizes across companies and
    vendors, not as adding new technical depth to how it is built.
  - `blog-openai-asana-codex-case-study.md` Claim 3 ("Asana's engineering
    organization already uses Codex routinely for large codebase changes,
    following a review-and-approve workflow, as standing practice") and
    `blog-openai-notion-codex-case-study.md` Claim 9 (engineers moving from
    one task at a time to running multiple tasks in parallel): this source
    extends the "Codex as standing organizational practice, not a one-off
    pilot" pattern with a fourth OpenAI customer case study, and its Claim 6
    (4x more Data Platform changes per support request) is a concrete,
    quantified instance of capacity reallocation similar in kind to Notion's
    parallel-task-execution claim, though measuring deflected support
    requests rather than concurrent agent sessions.

- **Extends**: `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` Claim 11
  (the sustainable response to AI-accelerated shadow IT is building "paved
  roads" — hardened, pre-audited self-service platforms, embedded automated
  quality checks, and risk-based prioritization by use case — because
  shadow tools are structurally faster than gatekept processes). Ryan's
  article is a governance/security practitioner's prescriptive framework
  argued in the abstract, with no named implementation. This source's Claim
  3 (Search Playground: a governed, engineer-built platform combining the
  existing design system, frontend stack, and Codex, explicitly built so
  non-engineers can prototype and ship without going through an engineering
  queue) and Claim 5 (codified best-practices-and-validations workflows
  gating Data Platform self-service) are a concrete, shipped instance of
  exactly the "paved roads" pattern Ryan describes — a company proactively
  building the sanctioned self-serve platform rather than being described as
  a governance response to already-occurring shadow IT. Neither source
  mentions the other; the guide can now pair Ryan's abstract governance
  argument with a real production example of the same architecture.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about non-engineer self-service, Codex adoption, or Data Platform/
  infrastructure governance that this source disagrees with. Per MINER.md
  §4a, no contradiction issue was filed.

- **Novel**:
  - **A named, shipped internal platform purpose-built for non-engineer
    self-service** (Claim 3: Search Playground, combining an existing design
    system, frontend stack, and Codex) — the first source in the corpus
    describing a company-built, named internal tool specifically designed to
    let non-engineers prototype and ship customer-facing experiences, rather
    than describing ad hoc use of a coding agent by an individual
    non-engineer.
  - **A marketing team building and shipping a customer-facing microsite
    itself, insourcing work that previously went to an external agency**
    (Claim 4) — the first source in the corpus describing a coding agent
    displacing an external design/development agency relationship, as
    opposed to displacing internal engineering time.
  - **Two distinct before/after success-rate metrics for a specific
    self-service infrastructure system** (Claim 6: Data Platform 58%→93%;
    broader self-service infrastructure 63%→90%) plus a support-request
    deflection ratio (4x) — a more granular, system-scoped quantification
    than the corpus's other OpenAI case studies, which tend to report either
    a single project's time/cost comparison (Asana) or aggregate,
    company-wide usage percentages (Samsung, Notion).
  - **Two named recurring operational cost-savings figures** (Claim 9:
    ~£36,000/year cloud storage cost reduction; ~£100,000/year from reduced
    data-processing waste) — distinct from Asana's one-time project-cost
    comparison ($12K actual vs. ~$6M staffing estimate); this is the first
    source in the corpus reporting ongoing, recurring operational savings
    attributed to AI-enabled capacity reallocation rather than a one-time
    migration cost comparison.
  - **"Single control plane" framing for a coding agent as a
    cross-functional shared interface** (Claim 11) — a distinct metaphor
    from the "24/7 intern" framing in `blog-openai-notion-codex-case-study.md`
    Claim 11 or the "control tower"/orchestrator framings elsewhere in the
    corpus; worth tracking if this specific "control plane" language recurs
    in future OpenAI customer case studies.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 3 (Search Playground) and
  Claim 5 (codified Data Platform workflows) as concrete, shipped examples of
  the "paved roads" architecture already argued for abstractly in
  `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` — a governed,
  engineer-built self-service platform combining existing infrastructure
  (design system, frontend stack) with a coding agent, specifically designed
  to let non-engineers build without bypassing engineering into ungoverned
  shadow tooling. Recommend citing this source as the "here is what a paved
  road actually looks like in production" companion to Ryan's prescriptive
  framework.
- **Chapter 05 (Team Adoption)**: Add Claim 2 ("everybody is a builder,"
  non-engineers making deployments directly) and Claim 4 (marketing team
  insourcing agency work) as a fourth, independently-tooled corroboration of
  the role-blurring pattern already documented from Anthropic
  (`blog-anthropic-ai-native-engineering-org.md`) and Notion
  (`blog-openai-notion-codex-case-study.md`). Cite Claim 8 (CTO Mike Jones'
  explicit "measure outcomes, not adoption" caution) as a citable,
  vendor-published example the guide can point to when cautioning readers
  against over-indexing on headline usage-percentage figures — notably, this
  caveat comes from the featured customer's own executive, not from the
  guide's own editorial voice.
- **Chapter 01 (Daily Workflows)**: Cite Claim 7 (Jones: "your job isn't to
  be handed a solution and implement it anymore — you have to get involved
  in the business problem") alongside the similar "role moves up the stack"
  framing already sourced from `blog-anthropic-ai-native-engineering-org.md`
  Claim 1 and `blog-openai-notion-codex-case-study.md` Claim 8, as a third
  company's version of the same claim, phrased specifically around problem
  ownership rather than artifact type.
- **Chapter 06 (or wherever the guide discusses ROI/outcome measurement)**:
  Cite Claim 9's two recurring cost-savings figures (~£36K/year cloud
  storage, ~£100K/year data-processing waste) as a concrete example of
  outcome-based measurement distinct from adoption-rate or time-savings
  metrics — worth pairing with Asana's one-time project-cost comparison
  (`blog-openai-asana-codex-case-study.md` Claim 2) to give the guide both a
  one-time-migration and a recurring-operational-savings example of AI-driven
  cost impact.

## Extraction Notes

- The live OpenAI URL (`https://openai.com/index/loveholidays`) returned a
  Cloudflare interstitial challenge page (HTTP 403 via WebFetch; a
  JavaScript-challenge shell via direct `curl` with a browser user agent),
  consistent with the Cloudflare bot-blocking behavior already documented for
  `openai.com` across every prior OpenAI-sourced note in this corpus
  (`blog-openai-notion-codex-case-study.md`, `blog-openai-asana-codex-case-study.md`,
  `blog-openai-codex-knowledge-work.md`,
  `blog-openai-samsung-chatgpt-codex-deployment.md`). The WebFetch tool also
  refuses `web.archive.org` URLs directly in this environment (same
  limitation documented in the sibling notes above). Retrieved instead via
  the Wayback Machine snapshot `http://web.archive.org/web/20260826161804/https://openai.com/index/loveholidays`
  (crawled August 26, 2026, the same day as publication), fetched with `curl`
  and parsed by stripping `<script>`/`<style>` blocks and remaining HTML tags
  with a local Python script rather than through an AI-summarization pass,
  specifically to guarantee the `Quote` fields above are copied
  character-for-character rather than paraphrased, per MINER.md §2a. Every
  quote in this note was copied directly from that stripped-tag text extract.
- The source is short (~700 words) with no linked sub-pages containing
  further substantive content about this specific case study — the "Inspire
  Me" link points to a loveholidays product page (not a source of additional
  case-study detail) and was not followed as a source-note lead. The page's
  "Keep reading" footer links to three unrelated OpenAI posts ("The full
  stack behind abundant intelligence," "Jalapeño's first results show
  industry-leading speed and efficiency in AI inference," "Disrupting a new
  covert influence campaign from Russia"), none of which concern loveholidays
  or this case study, and were not followed.
- This is a single-source, single-company, vendor-published case study with
  exactly two named individuals (Head of Engineering and CTO) and no quote
  from any non-engineer who actually used Search Playground or the Data
  Platform self-service workflows first-hand. Every claim above should be
  read with that ceiling in mind: OpenAI selected which quotes and metrics to
  publish, loveholidays did not publish an independent account, and none of
  the percentage or currency figures (79% AI-assisted changes, 93%/90%
  success rates, £36K/£100K savings) is independently audited or
  methodologically explained.
- No contradictions were filed; see the Cross-References `Contradicts` entry
  for confirmation that no existing corpus source disagrees with any claim
  extracted here.
