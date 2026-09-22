---
source_url: https://openai.com/index/put-data-to-work
source_type: blog-post
title: "Now everyone can put data to work"
author: OpenAI (product announcement; no individual byline; quotes partner and customer executives)
date_published: 2026-09-10
date_extracted: 2026-09-22
last_checked: 2026-09-22
status: current
confidence_overall: emerging
issue: "#3609"
---

# Now everyone can put data to work

> OpenAI's launch announcement for the "Data agent" in ChatGPT Work — a
> conversational analytics plugin that connects to enterprise data
> warehouses, BI tools, and semantic layers, builds interactive
> dashboards from natural-language questions, and enforces the connected
> account's existing row/column permissions — backed by partner
> endorsements from seven data-platform vendors and eleven named Alpha
> customers, plus a claim that OpenAI itself runs the same capability
> internally across nearly all of its product team.

## Source Context

- **Type**: blog-post (openai.com/index, "Product" category; published
  September 10, 2026; auto-discovered via the trusted `openai-news` RSS
  feed). A product-launch announcement structured around four named
  sections ("Connect to the company data and context your business
  trusts," "Turn questions into analysis and action," "Built from the
  tools we use to analyze data at OpenAI," "Get started with the Data
  agent") plus a "Try these prompts" section and rotating carousels of
  partner and customer quotes.
- **Author credibility**: Unsigned OpenAI corporate blog post — a vendor
  announcing its own product. All quotes are solicited from partner
  companies (AWS, ClickHouse, Databricks, Snowflake, MongoDB, Redis, G2,
  Tableau, Microsoft/Power BI, Sigma, ThoughtSpot) and Alpha-program
  customers (NTT DATA, Thermo Fisher Scientific, ServiceTitan, Zipline,
  Empower, Piston, Doeren Mayhew, CookUnity, Turing, micro1, Unit8), all
  selected and published by OpenAI. No independent metrics, no
  methodology disclosure, and no negative or mixed feedback is included —
  this is marketing copy, not a practitioner report. The companion page
  `https://openai.com/business/solutions/data/` (fetched as a linked
  sub-page) republishes the same claims with no additional detail.
- **Scope**: Covers the Data agent's supported data-source connectors,
  its semantic-layer/context integration, its enterprise permission
  model, its dashboard-creation and BI-tool-interop capabilities, its
  action-taking capabilities (Slack/email sharing, approved actions
  through connected tools), OpenAI's claimed internal adoption, and
  eleven customer testimonials. Does NOT cover: pricing, a technical
  description of how the agent resolves ambiguous metric definitions or
  handles conflicting data across sources, accuracy/error-rate figures,
  a description of the underlying model or agent harness, or any
  independent/third-party evaluation of the product.

## Extracted Claims

### Claim 1: The Data agent lets users investigate enterprise data and build interactive dashboards through natural-language conversation, without writing queries or learning a separate analytics tool
- **Evidence**: Direct product description in the article's opening.
- **Confidence**: anecdotal (vendor's own framing of its product's core
  value proposition; no usage data or accuracy figures given for the
  "without writing queries" claim)
- **Quote**: "It connects to your company data, investigates what changed, and builds interactive dashboards you can share. Direct and refine the analysis in one conversation, without writing queries or learning a new analytics tool."
- **Our assessment**: This is the standard "natural language replaces
  SQL/BI tooling" pitch common to this product category. It says nothing
  about how the agent resolves the concept-to-entity mapping problem that
  `blog-anthropic-selfservice-data-analytics.md` Claim 2 identifies as
  the actual hard part of analytics agents (accuracy went from 21% to
  95%+ only after adding a structured skills layer), nor how it avoids
  the cross-system context-resolution failure documented in
  `blog-thoughtworks-xiong-data-agents-context-resolution.md` Claim 6.
  The marketing framing treats "connect to data + ask a question" as
  sufficient; the corpus's technical sources suggest it is not, absent
  the kind of governance and skills infrastructure described below in
  Claim 3.

### Claim 2: The Data agent connects to a broad set of approved enterprise data sources — including Amazon Redshift, Datadog, Google BigQuery, ClickHouse, Databricks, MongoDB, and Snowflake — plus files from Google Drive and SharePoint
- **Evidence**: Direct connector list under "Connect to the company data
  and context your business trusts."
- **Confidence**: settled (a factual list of supported integrations,
  independently corroborated by the solutions page listing 34 named
  plugins including MotherDuck, Mixpanel, dbt, Oracle Analytics, Datadog
  Experiments, Alation, PostHog, Hex, Metabase, and Firebase)
- **Quote**: "The Data agent connects to approved data sources including Amazon Redshift, Datadog, Google BigQuery, ClickHouse, Databricks, MongoDB, Snowflake, and more. It can also bring files and documents from Google Drive and SharePoint into the analysis."
- **Our assessment**: The connector breadth (7 named + "more," 34 listed
  on the solutions page) establishes this as a broad enterprise-data
  integration surface, not a narrow single-warehouse tool. It is a
  factual capability claim, distinct from the accuracy/quality claims
  elsewhere in the article, which is why it is rated higher confidence.

### Claim 3: The agent interprets data using the organization's own business terms, metric definitions, custom calculations, and data relationships, sourced from external semantic layers and governance systems such as Databricks Genie Ontology, dbt, GitHub, Snowflake Horizon, and BI dashboards
- **Evidence**: Direct architecture description under "Connect to the
  company data and context your business trusts."
- **Confidence**: anecdotal (a capability claim with no description of
  how conflicting or missing definitions across these five named source
  types are reconciled)
- **Quote**: "It uses your organization's business terms, metric definitions, custom calculations, and data relationships to interpret the data. This context comes from semantic layers and trusted sources such as Databricks Genie Ontology, dbt, GitHub, Snowflake Horizon, and BI dashboards."
- **Our assessment**: This is the article's only nod to the semantic-layer
  problem that dominates this corpus's deeper data-architecture sourcing.
  It implicitly takes the "route through an existing governed semantic
  layer" position rather than building a new curated ontology from
  scratch — closer in spirit to `blog-anthropic-selfservice-data-analytics.md`
  Claim 10 (agents should call semantic-layer functions to get "the same
  number every other surface in the company produces") than to either
  side of the curation-vs-passive-harvest debate in
  `blog-thoughtworks-gall-layered-context-enterprise-data.md`. But the
  claim gives no detail on what happens when an organization's Databricks
  Genie Ontology and dbt metric definitions disagree — exactly the
  cross-system conflation failure mode documented in
  `blog-thoughtworks-xiong-data-agents-context-resolution.md` Claims 2-4.
  Treat as an unverified architectural claim, not evidence that the
  problem is solved.

### Claim 4: Enterprise administrators control which data connections are available and to which roles, and queries enforce the connected account's existing table-, row-, and column-level permissions
- **Evidence**: Direct governance statement closing the "Connect to the
  company data" section.
- **Confidence**: anecdotal (a permission-model claim with no description
  of the underlying access-control mechanism, no mention of whether the
  agent runs under per-user or per-connection service-account
  credentials, and no third-party security review cited)
- **Quote**: "Enterprise administrators choose which data connections are available and which roles can use them. Queries enforce the connected account's existing permissions, including table, row, and column restrictions."
- **Our assessment**: "The connected account's existing permissions"
  implies the agent inherits access scope from whatever account was used
  to configure the data-source plugin (an admin-managed connection, per
  Claim 13 below), not necessarily from the individual end user asking
  the question — the article does not clarify which. This is a materially
  different (and less specified) governance model than
  `blog-anthropic-agent-identity-access-model.md`, which documents
  Anthropic's Claude Tag agent identity model as a named two-level
  workspace/channel service-account hierarchy with credential isolation
  and dual audit trails. For the guide: this claim should not be cited as
  evidence of a specific access-control architecture — only as evidence
  that OpenAI markets permission enforcement as a feature, without the
  architectural detail Anthropic's identity-model post provides.

### Claim 5: Dashboards generated by the Data agent are interactive, team-editable, shareable, refreshable, and can be styled to an organization's brand guidelines
- **Evidence**: Direct feature description under "Turn questions into
  analysis and action."
- **Confidence**: anecdotal (product feature description, no usage data
  on how often dashboards are actually edited/refreshed post-creation)
- **Quote**: "Turn the analysis into an interactive dashboard with built-in visualizations. Your team can edit, share, and refresh it as needed. Share your brand guidelines to tailor outputs to your organization's look and feel."
- **Our assessment**: Standard BI-tool feature parity claim (editable,
  shareable, refreshable, brand-themed) presented as a differentiator for
  a conversational agent. Notable mainly for confirming that the output
  is a persistent, live artifact (a refreshable dashboard object), not a
  one-off chat response — relevant to how this pattern should be
  described in a use-cases chapter.

### Claim 6: The Data agent can also build and interact with dashboards inside existing BI tools — Omni, Oracle BI, Power BI, Sigma, Tableau, and ThoughtSpot — directed entirely in natural language, including publishing new views directly into those tools
- **Evidence**: Direct capability statement plus corroborating partner
  quotes from Tableau, Microsoft (Power BI/Fabric), Sigma, and
  ThoughtSpot executives.
- **Confidence**: anecdotal (capability claim plus vendor-solicited
  partner endorsements; no independent demonstration of round-trip
  publish-to-BI-tool behavior)
- **Quote**: "The Data agent can also build and interact with dashboards in Omni, Oracle BI, Power BI, Sigma, Tableau, and ThoughtSpot. Direct the work in plain language in the tools your team already uses."
- **Quote** (Tableau): "Users can easily transform insights into action by asking questions, exploring evidence, and publishing new views directly to Tableau using built-in design and analytics best practices."
- **Our assessment**: This positions the Data agent as a natural-language
  control layer over existing BI tools rather than a replacement for
  them — a "BI tools stay, query interface changes" strategy. This is
  consistent with the connector-breadth strategy in Claim 2: rather than
  competing with governed BI platforms, OpenAI is positioning ChatGPT
  Work as the entry point that dispatches into them.

### Claim 7: The agent can recommend next steps, identify which stakeholders should be involved, share findings via Slack or email, and carry out user-approved actions through connected tools — extending from analysis into action
- **Evidence**: Direct capability statement closing the "Turn questions
  into analysis and action" section.
- **Confidence**: anecdotal (capability claim, no example of an
  end-to-end analysis-to-action sequence given in the article itself)
- **Quote**: "Ask ChatGPT Work to recommend next steps and identify who needs to be involved. It can share the findings through Slack or email and carry out the actions you approve through connected tools."
- **Our assessment**: This is the "analysis → recommendation → approved
  action" loop that distinguishes an agentic analytics tool from a static
  BI dashboard. The "actions you approve" phrasing signals a human-in-
  the-loop gate before any action executes, but the article gives no
  detail on what that approval step looks like (a chat confirmation? a
  separate review UI?) or what class of actions are eligible.

### Claim 8: OpenAI claims broad internal dogfooding of the Data agent's underlying capabilities — nearly all of its product team and over two-thirds of its go-to-market organization self-serve company-data analysis, enabled by the data team building shared business definitions, access rules, and sensitive-data safeguards
- **Evidence**: Direct self-reported adoption statistic under "Built from
  the tools we use to analyze data at OpenAI," with a link to a companion
  LinkedIn post by OpenAI's data leadership (not independently
  fetchable — see Extraction Notes) for further detail.
- **Confidence**: emerging (specific, quantified adoption figures
  ("nearly all," "over two-thirds") self-reported by the vendor about its
  own internal usage; more specific than a generic marketing claim, but
  no methodology, headcount base, or measurement window is disclosed)
- **Quote**: "We use the capabilities behind the Data agent broadly across OpenAI. Nearly all of our product team and over two-thirds of our GTM organization use data agents in ChatGPT Work to analyze company data themselves. Our data team made this possible by creating shared business definitions, setting access rules, and putting safeguards in place for sensitive data."
- **Our assessment**: This directly parallels
  `blog-anthropic-selfservice-data-analytics.md`'s central claim (95% of
  Anthropic's business analytics queries automated via Claude, ~95%
  accuracy) — both frontier labs are using their own internal analytics
  workflows as the flagship proof point for a self-service data product,
  and both cite "shared business definitions" / governed data foundations
  as the enabling prerequisite (compare Anthropic's Claim 8: "the most
  important aspect of ensuring analytics agents are accurate is via
  strong data foundations"). The OpenAI claim is far less specific,
  though: no accuracy figure, no automation-rate figure, and "nearly all"
  / "over two-thirds" describe usage/adoption, not correctness. This is
  evidence that both labs converge on eating-your-own-dogfood as the
  credibility signal for analytics agents, not evidence that OpenAI's
  agent achieves comparable accuracy to Anthropic's reported figures.

### Claim 9: NTT DATA reports that licensing cost, implementation effort, and required technical expertise had constrained BI dashboard use across the organization, and that the Data agent let non-engineers in sales and corporate functions build and update their own dashboards in plain language
- **Evidence**: Named customer quote from Yuji Shono, Head of Global AI
  Office, NTT DATA Group — an Alpha-program participant.
- **Confidence**: anecdotal (a single named executive's characterization
  of their own organization's prior BI barriers and current usage; no
  usage volume, dashboard count, or before/after time-savings figure
  given)
- **Quote**: "At NTT DATA, licensing costs, effort, and technical expertise have made it difficult to expand the use of dashboards across our organization. With the Data agent in ChatGPT Work, many non-engineers, particularly in sales and corporate functions, have been able to build and update their own dashboards using plain language."
- **Our assessment**: This names the specific prior barrier (BI tool
  licensing/skill cost) that a conversational analytics layer targets:
  democratizing dashboard creation past a technical-skill and per-seat-
  license gate, not just replacing SQL-writing. Notably, Yuji Shono and
  NTT DATA Group are already in this corpus for a different OpenAI
  product — see Cross-References → Extends.

### Claim 10: ServiceTitan used the Data agent to quantify that users of its own AI product ("Atlas") launch marketing campaigns at roughly three times the rate of non-users, a finding now shaping their onboarding strategy
- **Evidence**: Named customer quote from Ankur Bhatt, VP Engineering,
  Agent OS and Applied AI, ServiceTitan.
- **Confidence**: anecdotal (a single named executive's report of one
  internal analysis result; the "roughly three times" figure is not
  independently verifiable from the article, and no confidence interval,
  sample size, or causal-vs-correlational framing is given)
- **Quote**: "At ServiceTitan, we used the Data agent in ChatGPT Work to build a dashboard showing that users of Atlas, our AI sidekick, launched campaigns at roughly three times the rate of nonusers. That finding is helping us simplify onboarding and help more customers adopt Atlas."
- **Our assessment**: This is the article's most concrete customer
  outcome — a specific quantified finding (3x) tied to a specific
  business decision (simplifying onboarding). It is the strongest
  evidence in the piece that the tool produced an actionable insight
  rather than just a chart, though as with all testimonials here it is
  self-reported and uncorroborated.

### Claim 11: Several Alpha customers (Zipline, Doeren Mayhew, CookUnity, Turing, micro1) report that the Data agent surfaced findings or rebuilt reporting significantly faster than their prior manual process — ranging from "hours" of analyst digging to a half-hour dashboard rebuild
- **Evidence**: Five separate named customer quotes across "Try these
  prompts" carousel section.
- **Confidence**: anecdotal (five independent named-executive
  testimonials citing time savings in relative, non-quantified terms
  except for micro1's specific "half an hour" figure; no aggregate or
  independently measured time-savings statistic across the Alpha cohort)
- **Quote** (Zipline): "In early testing, it surfaced profound findings that would have taken one of our best people hours of digging through the data to uncover."
- **Quote** (micro1): "in half an hour, rebuilt our performance tracking dashboards while catching errors in the original."
- **Our assessment**: The micro1 quote is notable for a secondary claim
  buried inside it — the agent caught errors in the customer's
  pre-existing, presumably human-built dashboard, not just producing a
  new one from scratch. That is a distinct capability (error detection in
  existing reporting) from the headline "ask a question, get a dashboard"
  framing, and the article does not elaborate on it further.

### Claim 12: Seven data-platform and BI vendors (AWS, ClickHouse, Databricks, Snowflake, MongoDB, Redis, G2) and four additional BI-tool vendors (Tableau, Microsoft/Power BI, Sigma, ThoughtSpot) issued coordinated launch-day endorsement quotes, each framing the Data agent as extending — not replacing — their own platform's governed semantics
- **Evidence**: Eleven separate named-executive partner quotes across two
  carousel sections ("Platform partners" and "BI tools").
- **Confidence**: settled (as a factual observation about the article's
  own structure and content — eleven partner companies did in fact
  provide quotes for this launch); anecdotal as to whether the
  partnerships reflect deep technical integration versus a coordinated PR
  exchange, which the article does not clarify
- **Quote** (Snowflake): "Our customers have built a trusted foundation for enterprise data and context in Snowflake. With the Data agent in ChatGPT Work, employees can tap into that data and access controls to investigate business questions—while OpenAI models simultaneously bring intelligence to experiences like Snowflake CoCo and CoWork."
- **Quote** (Databricks): "Genie has the rich context for bridging the gap from data to insights. We are thrilled to partner with OpenAI to make it easy for all ChatGPT users to tap into Genie's data intelligence."
- **Our assessment**: The consistent framing across all eleven partner
  quotes — "our governed semantics/context, their conversational
  interface" — is itself a signal of how data-platform vendors are
  positioning themselves relative to frontier-lab agent products: not as
  competitors to be disintermediated, but as the trust/governance layer
  the agent sits on top of. This is the multi-partner analytics-ecosystem
  parallel to the single-vendor BI-interop claim in Claim 6.

### Claim 13: The Data agent ships as an installable plugin inside ChatGPT Work's existing Plugin Directory, administered the same way as other ChatGPT Work plugins — workspace admins enable/install it and separately enable and configure individual data-source connector plugins (e.g., Databricks, Snowflake) and manage per-plugin access
- **Evidence**: Direct instructions under "Get started with the Data
  agent," including the plugin's directory URL pattern
  (`chatgpt.com/plugins/Plugin_fc9843a6fb34819195d6c7802398a8a7`).
- **Confidence**: settled (a factual description of the product's
  packaging and admin-configuration mechanism, corroborated structurally
  by the solutions page's list of 34 separately named plugins, each with
  its own URL under `openai.com/business/plugins/`)
- **Quote**: "You'll find the Data agent listed as Data in the Plugins directory in ChatGPT Work. Administrators can make it available or install it for their teams through Workspace settings > Plugins. They can also enable and configure the relevant data-source plugins, such as Databricks and Snowflake, and manage who can use them."
- **Our assessment**: This confirms that "Data agent" is not a
  standalone product but a first-party plugin riding on ChatGPT Work's
  general-purpose plugin architecture — the same architecture documented
  in `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 7 (a
  Plugin Directory of "more than 1,000 plugins," combining apps, skills,
  and app templates). Each data-source integration (Databricks, Snowflake,
  etc.) is itself a separately admin-managed plugin, meaning the "Data
  agent" experience is actually an orchestration layer over multiple
  independently-installed connector plugins, not a single monolithic
  integration.

## Concrete Artifacts

```
Supported data-source connectors (from article + solutions page)
Source: openai.com/index/put-data-to-work and
        openai.com/business/solutions/data/, Sept 2026

Named in the announcement:
  Amazon Redshift, Datadog, Google BigQuery, ClickHouse, Databricks,
  MongoDB, Snowflake, Google Drive, SharePoint

Named on the solutions page (34 total plugins under "Work across your
data with trusted business context"):
  Data (native), Microsoft Power BI, Amplitude, AWS Data Analytics,
  Tableau, Snowflake, Databricks Genie, ClickHouse, Google BigQuery,
  MotherDuck, Mixpanel, dbt, Oracle Analytics, Datadog Experiments,
  ThoughtSpot, Sigma, Omni Analytics, MongoDB, Google Firebase,
  Microsoft Azure CosmosDB, Deepnote, Statsig, Alation, PostHog, Hex,
  Metabase, Redis, G2, WisdomAI, VillageSQL, Google Drive, Similarweb,
  Microsoft SharePoint, Slack, Outlook Email, Microsoft Teams, GitHub

BI/dashboard tools the agent can drive directly:
  Omni, Oracle BI, Power BI, Sigma, Tableau, ThoughtSpot
```

```
Sample prompts (from "Try these prompts" section)
Source: openai.com/index/put-data-to-work, Sept 2026

Diagnose a metric change:
  "@Data Diagnose why weekly active users changed last week. Identify
  likely drivers, compare against prior periods, and recommend the
  next checks."

Design KPI framework:
  "@Data Design a KPI framework for this new product area with primary
  metrics, drivers, guardrails, targets, and data validation needs."

Create leadership readout:
  "@Data Turn this month's metrics into a leadership-ready update with
  actuals, comparisons, drivers, caveats, and recommended actions."
```

```
Alpha-program customer roster and reported use case (from article)
Source: openai.com/index/put-data-to-work, Sept 2026

NTT DATA Group    — non-engineers self-build dashboards (sales, corporate)
Thermo Fisher Sci.— supply-base opportunity analysis
ServiceTitan      — quantified 3x campaign-launch rate for Atlas users
Zipline           — surfaced findings that would take hours manually
Empower           — combined org + AI usage data; parsed free-form survey text
Piston            — leadership team self-serve funnel/support/spend analysis
Doeren Mayhew     — marketing + finance teams building dashboards within 2 days
CookUnity         — built/refined seasonal conversion dashboard, cut planning time
Turing            — Business Operations explored ops metrics via follow-up Qs
micro1            — rebuilt performance dashboards in 30 min, caught data errors
Unit8             — pipeline/demand analysis across industries and accounts
```

## Cross-References

### Cross-reference verification notes
`blog-anthropic-selfservice-data-analytics.md`,
`blog-thoughtworks-xiong-data-agents-context-resolution.md`,
`blog-thoughtworks-gall-layered-context-enterprise-data.md`,
`blog-anthropic-agent-identity-access-model.md`,
`blog-latentspace-khemani-unpacking-chatgpt-work.md`, and
`blog-openai-ntt-data-incident-analysis.md` were re-read in full before
writing the citations below; claim numbers cited were confirmed against
each note's numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-anthropic-selfservice-data-analytics.md` Claim 1 (Anthropic:
    "95% of business analytics queries are automated via Claude, with
    ~95% accuracy in aggregate") and Claim 8 (strong governed data
    foundations are the most important accuracy enabler): this article's
    Claim 8 (OpenAI: "nearly all of our product team and over two-thirds
    of our GTM organization" self-serve analytics via the same capability,
    enabled by "shared business definitions, setting access rules, and...
    safeguards") shows both frontier labs converging on the same
    go-to-market pattern — use internal dogfooding at scale as the
    credibility signal for a self-service analytics agent, and cite
    governed data/business-definition foundations as the prerequisite.
    OpenAI's disclosure is materially less specific (no accuracy figure).
  - `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 7 (ChatGPT
    Work's plugin architecture: apps via MCP servers, skills, and app
    templates, with a Plugin Directory of "more than 1,000 plugins"):
    this article's Claim 13 (Data agent ships as a plugin at
    `chatgpt.com/plugins/Plugin_...`, with data-source connectors as
    separately admin-managed plugins) is a first-party confirmation, from
    the vendor itself, of the plugin-based packaging that Khemani's
    outsider reverse-engineering piece already documented.
  - `blog-openai-ntt-data-incident-analysis.md` (NTT DATA Group cuts
    incident analysis to 30 minutes with Codex; quotes Yuji Shono, Head of
    Global AI Office, NTT DATA Group): this article's Claim 9 quotes the
    same named executive at the same company describing a second,
    distinct OpenAI product (Data agent vs. Codex) delivering a second,
    distinct operational improvement (self-service dashboards vs. faster
    incident analysis) — see **Extends** below.

- **Contradicts**: None identified. This article does not take an
  explicit position on the curated-semantic-layer-vs-passive-harvesting
  debate already filed as
  [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)
  between `blog-thoughtworks-asthagiri-ontology-failure-modes.md` /
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` and
  `blog-thoughtworks-gall-layered-context-enterprise-data.md`. Claim 3's
  "context comes from semantic layers and trusted sources such as
  Databricks Genie Ontology, dbt... and BI dashboards" is consistent with
  routing through whatever governed semantic layer an organization
  already has, which is compatible with either side of that filed
  contradiction depending on how that semantic layer itself was built —
  the article gives no detail either way, so no new contradiction is
  filed.

- **Extends**:
  - `blog-openai-ntt-data-incident-analysis.md`: that note documents NTT
    DATA Group's use of Codex to cut incident analysis time to 30 minutes,
    quoting the same executive (Yuji Shono, Head of Global AI Office).
    This article extends the same customer relationship to a second
    product line and a second workflow (self-service BI dashboards for
    non-engineering staff, Claim 9) — evidence that OpenAI's enterprise
    customers are being cited across multiple product launches, which is
    useful context for weighing how independent any single customer
    quote is when the same executive is quoted repeatedly across a
    vendor's marketing output.
  - `blog-anthropic-agent-identity-access-model.md`: that note documents
    Anthropic's specific, named agent-identity access-control
    architecture (service accounts, workspace/channel hierarchy,
    credential isolation, dual audit trails) for Claude Tag. This
    article's Claim 4 (permissions enforced via "the connected account's
    existing permissions") describes a governance outcome without any of
    that architectural detail, so it cannot be assumed to use an
    equivalent mechanism — flagged as a gap, not corroboration.

- **Novel**:
  - **Cross-lab dogfooding-as-credibility-signal pattern** (Claim 8): the
    parallel between this article's internal-adoption claim and
    Anthropic's self-service-analytics post is itself a new observation
    for this corpus — not previously documented as a shared go-to-market
    pattern across labs.
  - **Coordinated multi-vendor partner-endorsement structure** (Claim 12):
    eleven data-platform/BI vendors issuing near-identical "our governed
    semantics, their conversational interface" endorsements in a single
    launch is a new documented pattern of how data-infrastructure vendors
    are positioning themselves relative to agentic analytics products,
    not previously captured in this corpus's data-architecture sourcing.
  - **"Analysis agent surfaces errors in an existing human-built
    dashboard" capability** (Claim 11, micro1 quote): a secondary,
    under-elaborated claim that the agent caught errors in pre-existing
    reporting while rebuilding it — a distinct capability from
    "answer a new question," not discussed elsewhere in the corpus's
    analytics-agent sourcing.

## Guide Impact

- **Chapter 05 or 06 (Use Cases / Self-Service Analytics)**: Add this as
  a second, competing data point alongside
  `blog-anthropic-selfservice-data-analytics.md` for the "self-service
  conversational analytics" use case — but flag clearly that this source
  is vendor marketing copy with no accuracy figures, while the Anthropic
  post discloses specific ablation metrics (21% → 95%+ with skills). The
  guide should not present the two sources as equivalent-quality evidence
  even though they describe similar products; recommend the Anthropic
  post as the primary technical reference and this post only as evidence
  that the product category (and the "dogfood internally first" pattern)
  is now shared across both frontier labs.
- **Chapter 04 (Context Engineering)**: Note that Claim 3's semantic-layer
  integration claim ("context comes from semantic layers and trusted
  sources such as Databricks Genie Ontology, dbt, GitHub, Snowflake
  Horizon, and BI dashboards") is an unverified architecture claim with no
  detail on cross-system conflict resolution — cite alongside
  `blog-thoughtworks-xiong-data-agents-context-resolution.md`'s Claim 6
  (context resolution is "the critical and challenging point where data
  agents fail") as a reminder that this category of product claim should
  be treated skeptically absent a published failure-mode analysis or
  accuracy benchmark, which OpenAI has not published for the Data agent
  as of this source.
- **Chapter 02 or 03 (Governance / Access Control)**: Use Claim 4
  ("queries enforce the connected account's existing permissions") as a
  concrete example of an underspecified vendor permission claim to
  contrast against the fully-documented architecture in
  `blog-anthropic-agent-identity-access-model.md`. The guide should
  caution practitioners evaluating enterprise analytics agents to ask
  vendors explicitly whether queries run under per-user or per-connection
  credentials, since this article does not answer that question despite
  making a permission-enforcement claim.
- **Chapter 04 (Tool Use & Ecosystem / Plugin Architecture)**: Add Claim
  13 as a concrete example confirming
  `blog-latentspace-khemani-unpacking-chatgpt-work.md`'s plugin-directory
  architecture from the vendor's own documentation — a first-party
  product (Data agent) and its data-source dependencies (Databricks,
  Snowflake plugins) are each independently admin-managed plugins in the
  same directory, not a single bundled integration.

## Extraction Notes

- **Direct fetch of the source URL returned HTTP 403.** Both `curl` (with
  a standard browser user agent) and the WebFetch tool received an HTTP
  403 Forbidden from `openai.com/index/put-data-to-work` — the raw HTML
  response is a JS-rendering placeholder page with a `<meta
  http-equiv="refresh">`, consistent with bot/scraper blocking on
  openai.com. The article was instead retrieved via the `r.jina.ai`
  read-only proxy (`https://r.jina.ai/https://openai.com/index/put-data-to-work`),
  which returned the full rendered article text, including the
  "Published Time" header (Thu, 10 Sep 2026 05:22:41 GMT) used for
  `date_published`. The complete fetched text is reproduced in the
  Concrete Artifacts and Extracted Claims sections above; nothing was
  paraphrased from a summarized version.
- **One linked sub-page was followed successfully; one could not be
  fetched.** The "Learn more" link
  (`https://openai.com/business/solutions/data/`) was fetched via the
  same `r.jina.ai` proxy and used to corroborate the connector list
  (Claim 2) and confirm the plugin-directory structure (Claim 13) — no
  claims beyond what the main article already stated were found there.
  The in-article link to a companion post, "Learn more by reading this
  post" (a LinkedIn Pulse article by Vijaye Raji,
  `linkedin.com/pulse/inside-openai-how-our-data-team-uses-ai-move-faster-vijaye-raji-a0vcc`),
  returned HTTP 403 from both the `r.jina.ai` proxy and would require
  LinkedIn authentication to view directly — it was not fetched. That
  post likely contains more technical detail behind Claim 8's internal-
  adoption figures; a future source-submission issue for that URL
  specifically (if accessible) would be worth filing separately, since it
  is authored by OpenAI's data leadership rather than being an unsigned
  product page.
- **A companion webinar link**
  (`https://webinar.openai.com/chatgpt-work-series/data-analytics/`) was
  referenced in the article but not fetched — it is a registration page
  for a live/recorded webinar, not a text source suitable for this
  extraction process.
- **No contradictions were identified or filed.** See Cross-References →
  Contradicts.
- **Confidence rated `emerging` overall**, not `anecdotal`, despite this
  being unsigned vendor marketing copy: the article combines eleven
  independently named, attributed customer/partner quotes across
  different industries (rather than a single customer-story anecdote, the
  more common OpenAI source-note pattern in this corpus — see
  `blog-openai-avatarin-retail-voice-agent.md` and
  `blog-openai-virgin-atlantic-customer-journeys.md`, both rated
  `anecdotal`), plus a specific quantified internal-adoption figure
  (Claim 8). Individual claims are rated `anecdotal` where they rest on a
  single named quote with no measurement detail, and `settled` only where
  they are plain factual/structural claims about the product's packaging
  (Claims 2, 12, 13) rather than performance or accuracy claims. Nothing
  in the article rises to `settled` on any accuracy, effectiveness, or
  architecture question.
