---
source_url: https://openai.com/index/how-news-organizations-are-using-ai
source_type: blog-post
title: "How news organizations are using AI to advance their vital missions"
author: OpenAI
date_published: 2026-07-22
date_extracted: 2026-08-04
last_checked: 2026-08-04
status: current
confidence_overall: anecdotal
issue: "#2475"
---

# How news organizations are using AI to advance their vital missions

> An OpenAI customer-roundup post naming ~20 news organizations and their AI
> use cases across editorial, audience, and business functions, plus two
> linked sub-pages documenting a $10M Lenfest Institute/Microsoft/OpenAI
> local-newsroom AI fellowship and a dedicated "OpenAI Academy for News
> Organizations" training/governance program — the corpus's first
> journalism-vertical adoption source.

## Source Context

- **Type**: blog-post (OpenAI customer-story roundup, `openai.com/index/`,
  auto-discovered via the `openai-news` trusted feed, published July 22,
  2026). Two linked sub-pages were also read as substantive follow-ons: the
  Lenfest Institute AI Collaborative and Fellowship Program page
  (`openai.com/index/lenfest-institute/`) and the "Introducing OpenAI
  Academy for News Organizations" page
  (`openai.com/index/openai-academy-for-news-organizations/`).
- **Author credibility**: House-authored OpenAI customer-story copy. No
  individual byline. The roundup names ~20 organizations (Associated Press,
  POLITICO, Axios, The Philadelphia Inquirer, Axel Springer/Business
  Insider/WELT, Future, Le Monde, PRISA Media, The Daily Beast, American
  Journalism Project, Condé Nast/Bon Appétit, The Atlantic, Eater, The San
  Francisco Standard, BILD, Chicago Public Media, News Corp, The Seattle
  Times) but gives almost no per-organization methodology, sample size, or
  measurement window for any claim — this is a vendor-selected,
  vendor-framed showcase, not an independent survey of journalism AI
  adoption. The two linked sub-pages add named individual quotes (Jim
  Friedlich, Lenfest CEO; Tom Rubin, OpenAI; Teresa Hutson, Microsoft) and
  one disclosed dollar figure ($10M), which raises those two pieces above
  the roundup's baseline anecdotal grade.
- **Scope**: Covers three OpenAI-defined categories — "Empowering
  Journalism" (editorial/reporting tools), "Growing Audiences and Enhancing
  Reader Experiences" (reader-facing products), and "Strengthening the
  Business of News" (sales/business tooling) — with one to three sentences
  per named organization. Does NOT cover: technical implementation detail
  for any named tool, adoption/usage rates beyond BILD's single cumulative
  count, cost or licensing terms, any failure mode or rollback, or
  independent verification of any claim. The Lenfest sub-page covers
  funding structure and named recipient organizations but not individual
  fellow deliverables. The Academy sub-page covers the program's four
  stated components but not curriculum content (same gating pattern as the
  general Academy catalog documented in
  `blog-openai-academy-training-courses.md`).

## Extracted Claims

### Claim 1: OpenAI frames its news-organization partnerships around three goals — helping with time-consuming editorial tasks, enabling new reader experiences, and supporting sustainable news businesses
- **Evidence**: Opening framing statement for the entire roundup, setting up
  the article's three named sections.
- **Confidence**: anecdotal (vendor framing; not itself a falsifiable
  operational claim)
- **Quote**: "OpenAI has partnered with news organizations to explore AI's utility in journalism, helping with time-consuming tasks, enabling new reader experiences, and supporting sustainable businesses."
- **Our assessment**: This is a strategic positioning statement parallel in
  function to the "learning is part of deployment" framing OpenAI used for
  its general Academy announcement
  (`blog-openai-academy-training-courses.md` Claim 1) — a top-of-post
  house-framing sentence that organizes the rest of the piece rather than
  asserting a testable outcome.

### Claim 2: The Associated Press uses AI tools for reporting verification and newsroom workflow tasks while retaining journalist editorial control, including overnight-news scanning, image/video verification via upload tracing and geolocation, and converting Supreme Court filings into searchable text
- **Evidence**: Direct description of five distinct AP tool applications in
  a single paragraph.
- **Confidence**: anecdotal (named applications with no adoption count,
  accuracy rate, or time-savings figure for any of the five)
- **Quote**: "The Associated Press leverages OpenAI technology for reporting verification and newsroom workflows while maintaining journalist editorial control. Tools scan overnight news for reportable developments, verify images and videos through upload tracing and geolocation, and transform Supreme Court filings into searchable information."
- **Our assessment**: "Maintaining journalist editorial control" is the
  closest this article comes to naming a human-in-the-loop safeguard for a
  wire service (a use case where unreviewed AI error has outsized
  downstream reach, since AP content is redistributed by other outlets).
  No detail is given on what "editorial control" means operationally
  (does a human review every AI-flagged story lead before publication, or
  only spot-check?) — treat as a stated principle, not a documented
  process.

### Claim 3: Axios built narrow, task-specific custom GPTs for individual editorial functions rather than one general-purpose newsroom assistant — a "FOIA Refiner GPT" for open-records requests, "O Caption! My Caption!" for image optimization, and "Axiomizer" for headline/copy review
- **Evidence**: Three named, single-function custom GPTs with brief
  descriptions of each tool's purpose.
- **Confidence**: anecdotal (three named tools; no adoption count, usage
  frequency, or output-quality data for any of the three)
- **Quote**: "Axios developed custom GPTs including the \"FOIA Refiner GPT\" for crafting open-records requests, \"O Caption! My Caption!\" for image optimization, and \"Axiomizer\" for reviewing copy to suggest \"sharper headlines and clearer writing.\""
- **Our assessment**: This is a much smaller-scale, more curated version of
  the bottom-up custom-GPT pattern documented at BBVA
  (`blog-openai-bbva-banking-transformation.md` Claim 6: >20,000 employee-built
  GPTs, ~4,000 frequently used). Axios names exactly three GPTs, each
  mapped to a specific, narrow editorial task (records requests, image
  captioning, copy review) — this reads as a curated, newsroom-scale
  instance of the same "employees build narrow custom GPTs for recurring
  tasks" mechanism, but at a scale where each tool can be named individually
  rather than reported only as an aggregate count.

### Claim 4: The Philadelphia Inquirer's Scribe tool monitors public meetings across municipalities and school districts, and ranks the resulting summaries using a newsworthiness framework its own reporters and editors developed
- **Evidence**: Direct description of Scribe's function and the origin of
  its ranking methodology.
- **Confidence**: anecdotal (named tool and named methodology origin; no
  adoption count, meeting-volume figure, or accuracy/false-negative rate
  for missed newsworthy items)
- **Quote**: "The Philadelphia Inquirer created Scribe, an AI tool monitoring public meetings across municipalities and school districts. Scribe converts transcripts into summaries ranked using a newsworthiness framework developed by Inquirer reporters and editors."
- **Our assessment**: The notable detail here is not the AI application
  itself (transcript summarization is a well-documented use case elsewhere
  in the corpus) but that the *ranking heuristic* was authored by domain
  experts (the paper's own reporters and editors) rather than left to a
  generic relevance score — a concrete instance of subject-matter experts
  encoding their own judgment into a scoring rubric that an AI tool then
  applies at scale across more meetings than a newsroom could staff
  in person. No detail is given on the framework's actual criteria.

### Claim 5: BILD's AI assistant Hey_ has answered more than 250 million reader questions, helping readers understand news through chat and interactive article widgets
- **Evidence**: Single cumulative usage count for a named reader-facing
  product.
- **Confidence**: anecdotal (single self-reported cumulative figure; no
  time window given for how long Hey_ has been live, no definition of what
  counts as an "answered" question, no user-satisfaction or accuracy data)
- **Quote**: "BILD's AI assistant Hey_ has answered more than 250 million reader questions, helping readers understand news through chat and interactive article widgets."
- **Our assessment**: This is the single largest raw usage number in the
  article, but it is a cumulative count with no denominator (total readers,
  total articles, or time period) and no quality signal — comparable in
  kind (a large, undated cumulative count with no measurement methodology)
  to BBVA's ">20,000 custom GPTs" figure in
  `blog-openai-bbva-banking-transformation.md` Claim 6. Useful only as a
  scale indicator that a reader-facing news chatbot can reach very high
  cumulative interaction volume, not as evidence of answer quality.

### Claim 6: The Seattle Times developed an AI-powered prospecting agent using ChatGPT Enterprise that generates targeted lead lists, scores prospects, produces research reports, and checks CRM status, reducing prospecting time "from hours to minutes"
- **Evidence**: Direct description of the agent's four functions and a
  stated before/after time claim.
- **Confidence**: anecdotal (named tool and function list with a
  qualitative, not quantified, before/after claim — "hours to minutes" has
  no specific numbers, unlike BBVA's Peru assistant)
- **Quote**: "The Seattle Times developed an AI-powered prospecting agent using ChatGPT Enterprise, enabling sales representatives to generate targeted lead lists, score prospects, produce research reports, and check CRM status. The tool has \"reduced prospecting time from hours to minutes.\""
- **Our assessment**: This corroborates the "quantified-sounding but
  actually qualitative" before/after efficiency pattern seen across OpenAI
  customer stories — compare BBVA's Peru assistant
  (`blog-openai-bbva-banking-transformation.md` Claim 10: a specific
  "7.5 minutes to around 1 minute" figure) against this claim's vaguer
  "hours to minutes" framing with no actual numbers. Both describe a
  business-side (not editorial) use case: sales/revenue operations rather
  than journalism itself, which is worth flagging separately from the
  article's editorial claims when assessing what "news organizations using
  AI" actually covers — a meaningful fraction of the named examples
  (Seattle Times prospecting, News Corp Knowledge Agents, POLITICO's
  commercial-team tailoring) are business-operations use cases, not
  reporting or audience-facing ones.

### Claim 7: News Corp developed AI-powered "Knowledge Agents" that combine structured enterprise data with unstructured business knowledge, securely accessing a global data lake using OpenAI models and the Model Context Protocol
- **Evidence**: Direct description naming the specific integration protocol
  used.
- **Confidence**: anecdotal (named architecture pattern; no detail on
  which data sources are connected, how many employees use the Knowledge
  Agents, or what "securely" means operationally beyond the MCP reference)
- **Quote**: "News Corp developed AI-powered \"Knowledge Agents\" combining structured enterprise data with unstructured business knowledge, securely accessing the global data lake using OpenAI models and Model Context Protocol."
- **Our assessment**: This corroborates `blog-anthropic-mcp-production-agents.md`
  Claim 4 ("MCP is the recommended integration layer for production cloud
  agents, providing authentication, discovery, and rich semantics as a
  standardized protocol") with a concrete, named, cross-vendor production
  example — a large media enterprise using MCP (an Anthropic-originated,
  now cross-vendor protocol) inside an OpenAI-model-based agent to reach an
  internal data lake. This is independent evidence that MCP adoption for
  enterprise-data access is not Anthropic-ecosystem-specific, though the
  article gives no architectural detail (server design, tool grouping,
  auth mechanism) comparable to what the Anthropic MCP post documents.

### Claim 8: The Lenfest Institute for Journalism partnered with OpenAI and Microsoft to fund a two-year AI fellowship program at five (with three more planned) local news organizations, with OpenAI and Microsoft each contributing $2.5 million in direct funding plus $2.5 million in software credits — roughly $10 million total for the pilot
- **Evidence**: Named funding structure with specific dollar figures and
  named recipient organizations, from the linked Lenfest Institute sub-page.
- **Confidence**: emerging (specific, disclosed dollar figures and named
  recipient list from a joint OpenAI/Microsoft/Lenfest program page; single
  program, no outcome data yet since fellows are described as being
  onboarded for a two-year term)
- **Quote**: "Through these fellowships—and by sharing results with the broader news industry—we will help empower local newsrooms to explore, implement and advocate for AI business solutions."
- **Our assessment**: This is the most concrete financial-commitment figure
  in either the roundup or its sub-pages, and it is a novel mechanism for
  the corpus: a joint, cross-vendor (OpenAI + Microsoft), grant-funded
  *fellowship* structure — direct cash plus software credits paid to a
  nonprofit journalism foundation, which in turn places named two-year AI
  fellows inside five specific local newsrooms (Chicago Public Media,
  Newsday, The Minnesota Star Tribune, The Philadelphia Inquirer, The
  Seattle Times), with three more organizations to follow in a second
  round. This differs structurally from every enablement mechanism
  documented elsewhere in the corpus (BBVA's internal champions/wizards
  network, OpenAI Academy's self-serve courses) — those are enablement
  programs an organization runs on its own budget; Lenfest's fellowship is
  externally vendor-funded headcount placed inside recipient organizations
  specifically for local-news outlets that likely could not fund equivalent
  positions themselves.

### Claim 9: OpenAI launched a dedicated "OpenAI Academy for News Organizations," a vertical-specific spinoff of its general Academy with four components — training programs, practical-application guidance, shared open-source resources, and AI-governance-policy frameworks
- **Evidence**: Direct enumeration of the program's four components from
  the linked Academy-for-News sub-page.
- **Confidence**: emerging (first-party description of a named, structured
  program with four enumerated components; the components themselves are
  as-designed descriptions, not measured outcomes)
- **Quote**: "journalism is essential to a healthy democracy"
- **Our assessment**: This is a sector-specific extension of the general,
  three-course OpenAI Academy curriculum already documented in
  `blog-openai-academy-training-courses.md` — that note's Claims 2-5
  describe a generic, cross-industry three-course sequence (AI Foundations
  → Applied AI Foundations → Agents and Workflows); this journalism-vertical
  Academy adds a fourth component absent from the general curriculum
  description: explicit "governance guidance" for developing "responsible
  AI policies," named alongside acknowledgment of "trust, accuracy, and
  jobs" concerns specific to journalism. No curriculum content, session
  count, or enrollment figures are given — the same content-gating pattern
  documented in `blog-openai-academy-training-courses.md`'s Extraction
  Notes recurs here (the source page describes the program's existence and
  components, not its material).

### Claim 10: Le Monde incorporated its own translation style guide into ChatGPT models to accelerate English-language publication, explicitly to free journalists to focus on "core reporting and analysis missions"
- **Evidence**: Direct description of a domain-specific customization
  (embedding an internal style guide into the model) and its stated
  organizational purpose.
- **Confidence**: anecdotal (named customization approach and stated
  purpose; no detail on how the style book was incorporated — fine-tuning,
  system prompt, or retrieval — and no throughput or quality metric for
  the resulting translations)
- **Quote**: "Le Monde incorporated its translation style book into ChatGPT models to accelerate publication processes for English-language content, freeing journalists to focus on \"core reporting and analysis missions.\""
- **Our assessment**: This is a concrete instance of an organization
  encoding its own institutional voice/style rules into a model rather than
  relying on generic output, paired with an explicit "AI does mechanical
  translation, humans do reporting and analysis" division of labor — the
  same integrity-layer/narrative-layer split documented in
  `blog-anthropic-fong-finance-narrative.md` Claim 5 and echoed in BBVA's
  Credit Analysis Pro GPT (`blog-openai-bbva-banking-transformation.md`
  Claim 7), now in a translation/publishing context rather than finance.

### Claim 11: The Daily Beast's data team built "Data Scouts," AI-powered agents that identify opportunities and recommend next steps, with most interactions happening in Slack rather than a dedicated app
- **Evidence**: Direct description of the tool's function and its primary
  interaction surface.
- **Confidence**: anecdotal (named tool and stated interaction channel; no
  adoption count, usage frequency, or outcome data)
- **Quote**: "The Daily Beast data team built Data Scouts, AI-powered agents identifying opportunities and recommending next steps. Most interactions occur in Slack, integrating insights into existing workflows."
- **Our assessment**: The specific, checkable detail here is the choice to
  surface agent output inside an existing collaboration tool (Slack) rather
  than building a standalone interface — a low-friction integration pattern
  that avoids requiring staff to adopt a new tool to benefit from the
  agent's output. This is a design choice worth noting for the guide as a
  concrete example of "meet users in their existing workflow," though the
  article gives no detail on what Data Scouts actually analyzes or how
  "opportunities" are defined.

## Concrete Artifacts

```
Source: OpenAI, "How news organizations are using AI to advance their vital
missions," https://openai.com/index/how-news-organizations-are-using-ai
(published July 22, 2026; retrieved via the r.jina.ai reader proxy — see
Extraction Notes)

Three named Axios custom GPTs (verbatim names and descriptions):
  - "FOIA Refiner GPT" — for crafting open-records requests
  - "O Caption! My Caption!" — for image optimization
  - "Axiomizer" — for reviewing copy to suggest "sharper headlines and
    clearer writing"

Named organizations by section (verbatim section headings):
  Empowering Journalism: Associated Press, POLITICO, Axios, The
    Philadelphia Inquirer, Axel Springer (Business Insider, WELT), Future,
    Le Monde, PRISA Media (Diario AS, EL PAÍS), The Daily Beast, American
    Journalism Project (Centro de Periodismo Investigativo, Enlace Latino
    North Carolina)
  Growing Audiences and Enhancing Reader Experiences: Condé Nast (Bon
    Appétit), The Atlantic, Eater, Future, Le Monde, The San Francisco
    Standard, BILD, Chicago Public Media
  Strengthening the Business of News: News Corp, The Seattle Times
```

```
Source: OpenAI, "OpenAI and the Lenfest Institute AI Collaborative and
Fellowship Program," https://openai.com/index/lenfest-institute/
(retrieved via the r.jina.ai reader proxy)

Initial grant recipients (five news organizations, two-year AI fellows):
  - Chicago Public Media
  - Newsday (Long Island, NY)
  - The Minnesota Star Tribune
  - The Philadelphia Inquirer
  - The Seattle Times
(Three additional organizations to receive fellowships in a second funding
round.)

Financial commitment: OpenAI and Microsoft each provided $2.5 million in
direct funding plus $2.5 million in software credits — approximately $10
million total for the two-year pilot.

Named quotes:
  Jim Friedlich (CEO, The Lenfest Institute): "Through these
    fellowships—and by sharing results with the broader news industry—we
    will help empower local newsrooms to explore, implement and advocate
    for AI business solutions."
  Tom Rubin (OpenAI): "AI technology can help in the research,
    investigation, distribution, and monetization of important
    journalism."
  Teresa Hutson (Microsoft): "We hope these news organizations will be
    lighthouses for the industry, to provide examples of how AI can build
    a better future."

Project focus areas: transcription, summarization, translation, public
data analysis, content discovery, archival search interfaces, and
advertising analytics.
```

```
Source: OpenAI, "Introducing OpenAI Academy for News Organizations,"
https://openai.com/index/openai-academy-for-news-organizations/
(retrieved via the r.jina.ai reader proxy)

Four stated program components:
  1. Training Programs — "AI Essentials for Journalists" plus advanced
     sessions for technical/product teams
  2. Practical Applications — investigative research, multilingual
     reporting, data analysis, production efficiency
  3. Shared Resources — open-source projects for organizations to customize
  4. Governance Guidance — frameworks for developing responsible AI
     policies

Launch context: debuted at the AI and Journalism Summit, co-hosted with
the Brown Institute for Media Innovation and Hearst. Named partner outlets:
News Corp, Axios, the Financial Times, Condé Nast, Hearst — collectively
described as providing "content in more than 20 languages globally."
```

## Cross-References

- **Corroborates**:
  - `blog-openai-bbva-banking-transformation.md` Claim 6 (>20,000
    employee-built custom GPTs, ~4,000 frequently used): Axios's three
    named, single-function custom GPTs (Claim 3) is a smaller-scale,
    fully-named instance of the same bottom-up custom-GPT pattern —
    narrow, curated tool-building rather than BBVA's aggregate-count scale.
  - `blog-anthropic-fong-finance-narrative.md` Claim 5 (integrity-layer /
    narrative-layer division of labor) and `blog-openai-bbva-banking-transformation.md`
    Claim 7 (Credit Analysis Pro GPT automating extraction so analysts
    "focus more on strategic analysis"): Le Monde's translation-automation
    claim (Claim 10 — freeing journalists for "core reporting and analysis
    missions") is the same mechanical-work/judgment-work split applied to
    publishing rather than finance.
  - `blog-anthropic-mcp-production-agents.md` Claim 4 (MCP as the
    recommended standardized integration layer for production cloud
    agents): News Corp's Knowledge Agents (Claim 7) is a concrete,
    cross-vendor (OpenAI-model, MCP-protocol) production example
    corroborating that MCP adoption for enterprise-data access extends
    beyond the Anthropic ecosystem.
  - `blog-openai-bbva-banking-transformation.md` Claim 10 (Peru assistant:
    "7.5 minutes to around 1 minute," ~80% reduction): the Seattle Times
    prospecting agent's "reduced prospecting time from hours to minutes"
    (Claim 6) is the same qualitative before/after efficiency framing
    pattern, but notably less quantified — no specific numbers, unlike
    BBVA's Peru figure.

- **Contradicts**: None identified. No claim in this source materially
  opposes an existing source note or disagrees with itself; checked open
  `contradiction`-labeled issues and CONTRADICTIONS.md entries C-001
  through C-008 before finalizing — none cover journalism/media adoption.

- **Extends**:
  - `blog-openai-academy-training-courses.md`: the "OpenAI Academy for News
    Organizations" (Claim 9) is a vertical-specific spinoff of the general
    three-course Academy curriculum documented in that note (Claims 2-5),
    adding a fourth component — explicit AI-governance-policy guidance —
    not present in the general Academy's course descriptions.
  - `blog-openai-bbva-banking-transformation.md`: extends the corpus's
    OpenAI customer-story corpus into a new, previously undocumented
    regulated-adjacent vertical (journalism/media), with a much larger
    number of named organizations (~20) but far shallower per-organization
    detail than the single-company-deep BBVA case study.

- **Novel**:
  - **Journalism/media as a documented AI-adoption vertical** (entire
    note): No prior corpus source covers news-organization AI adoption;
    this is the first.
  - **Cross-vendor, grant-funded fellowship structure** (Claim 8 — Lenfest
    Institute, $10M from OpenAI + Microsoft jointly, placing named
    two-year AI fellows inside five to eight local newsrooms): No prior
    corpus source documents an externally vendor-funded headcount/fellowship
    mechanism as an AI-adoption lever, as distinct from internal champion
    networks or self-serve training courses.
  - **Domain-expert-authored ranking heuristic applied at AI scale** (Claim
    4 — the Inquirer's Scribe using a newsworthiness framework built by its
    own reporters and editors): a concrete example of subject-matter
    experts encoding judgment into a rubric an AI tool then applies across
    volume the humans could not cover directly.
  - **Existing-tool-surface integration pattern** (Claim 11 — Daily Beast's
    Data Scouts surfacing agent output primarily in Slack rather than a new
    app): a low-friction adoption design choice not previously named this
    explicitly in the corpus.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add journalism/media as a documented
  adoption vertical, citing this source's breadth (~20 named organizations)
  alongside the caveat that per-organization evidence here is far shallower
  than the guide's existing single-company deep-dives (BBVA, Endava). Use
  this source primarily for pattern breadth, not as a primary evidentiary
  source for any single claim.
- **Chapter 05 (Team Adoption)**: Add the Lenfest Institute fellowship
  structure (Claim 8) as a novel enablement mechanism distinct from
  internal champion networks and self-serve training: vendor-funded,
  externally-placed headcount inside recipient organizations. This is
  relevant specifically for guide discussion of how smaller organizations
  (without budget for dedicated AI roles) can access AI-adoption expertise
  through vendor-sponsored fellowship/grant programs rather than
  internal-only enablement.
- **Chapter 05 (Team Adoption)**: Add the OpenAI Academy for News
  Organizations (Claim 9) as a concrete example of a vendor tailoring its
  general training curriculum to a specific regulated-adjacent vertical by
  adding a governance/policy component — useful alongside the general
  Academy material in `blog-openai-academy-training-courses.md` to show
  how vertical-specific AI training programs differ from generic ones.
- **Chapter 03 (Verification), if discussing domain-specific customization**:
  Use Le Monde's style-guide-into-model approach (Claim 10) and the
  Inquirer's Scribe newsworthiness framework (Claim 4) as two concrete,
  contrasting examples of encoding institutional/domain judgment into an
  AI tool's behavior, though neither source gives implementation detail
  (fine-tuning vs. prompting vs. retrieval) precise enough to recommend a
  specific technique.
- **Any chapter citing large cumulative usage figures**: Flag BILD's ">250
  million reader questions answered" (Claim 5) the same way the guide
  should flag BBVA's ">20,000 custom GPTs" — a large, undated,
  methodology-free cumulative count useful only as a scale indicator, not
  as evidence of quality or per-user value.

## Extraction Notes

- **The live source URL and its two linked sub-pages all returned HTTP 403
  to WebFetch**, consistent with the prior Prospector triage comments on
  this issue noting OpenAI's bot protection blocks direct fetches, and
  consistent with the extraction difficulty already logged in
  `blog-openai-bbva-banking-transformation.md`'s and
  `blog-openai-academy-training-courses.md`'s Extraction Notes for other
  `openai.com/index/` pages. `web.archive.org` is also blocked from direct
  WebFetch access in this environment (confirmed again during this
  extraction), and the Wayback Machine's `archive.org/wayback/available`
  API confirmed a snapshot exists but its `note` field stated no article
  text was retrievable through that check endpoint. All three pages (the
  main roundup and the two linked sub-pages) were successfully retrieved
  through the `r.jina.ai` reader proxy, which renders the live page
  server-side and returns extracted text — the same recovery method noted
  as successful for `blog-openai-endava-frontiers.md`. All quotes in this
  note were copied character-for-character from the `r.jina.ai`-extracted
  text.
- **Two of the five sub-pages allowed by MINER.md §1 were followed**: the
  Lenfest Institute fellowship page and the OpenAI Academy for News
  Organizations page, both linked directly from the main article. Three
  other linked pages were identified (an Axios news article about the
  American Journalism Project partnership, a WAN-IFRA program announcement,
  and an Atlantic game page) but were judged less substantive for
  guide-relevant AI-adoption-pattern extraction than the two OpenAI-authored
  program pages, so were not followed in depth.
- **Confidence calibration**: The main roundup names ~20 organizations with
  one to three sentences each and almost no methodology, sample size, or
  time window for any claim — this is closer to a marketing showcase than
  a deep case study, and most individual claims are graded anecdotal
  accordingly. The two linked sub-pages (Lenfest's disclosed $10M funding
  figure and named recipient list; the Academy-for-News page's four
  enumerated program components) are graded emerging where they give
  specific, checkable structural detail. Overall confidence_overall is set
  to anecdotal because the bulk of the source's content (the ~20-organization
  roundup that gives the piece its title and primary content) is
  shallow and unmeasured, even though two sub-page claims individually
  clear the emerging bar.
- No contradiction issue was filed — see Cross-References → Contradicts.
- All cross-reference claim numbers cited above (from
  `blog-openai-bbva-banking-transformation.md`,
  `blog-openai-academy-training-courses.md`,
  `blog-anthropic-mcp-production-agents.md`, and
  `blog-anthropic-fong-finance-narrative.md`) were verified by re-reading
  each cited note's actual claim numbering and content before writing this
  note; none were guessed.
