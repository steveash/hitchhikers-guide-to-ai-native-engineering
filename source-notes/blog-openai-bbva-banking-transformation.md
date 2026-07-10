---
source_url: https://openai.com/index/bbva
source_type: blog-post
title: "BBVA puts AI at the core of banking with OpenAI"
author: OpenAI (customer-story vertical; quoted subjects Carlos Torres Vila — Chair of BBVA, Antonio Bravo — Head of AI Transformation at BBVA, Elena Alfaro — Head of Global AI Adoption at BBVA)
date_published: 2026-06-11
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: emerging
issue: "#1707"
---

# BBVA puts AI at the core of banking with OpenAI

> An OpenAI customer-story case study documenting BBVA's ChatGPT Enterprise rollout from
> 3,000 to ~100,000 employees, the "trust, governance, structured learning" adoption
> framework BBVA used to scale generative AI inside a highly regulated global bank, a
> two-tier champion/"wizard" enablement network, >20,000 employee-built custom GPTs, and
> three named production GPT workflows (credit risk analysis, retail-banking legal
> assistance, customer-survey sentiment analysis) plus a Peru-market internal assistant
> with a concrete before/after efficiency metric.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/`, ~900 words;
  auto-discovered via the `openai-news` trusted feed, published June 11, 2026)
- **Author credibility**: House-authored OpenAI customer-story copy built around quotes
  from three named BBVA executives: Carlos Torres Vila (Chair), Antonio Bravo (Head of AI
  Transformation), and Elena Alfaro (Head of Global AI Adoption). BBVA is a Fortune-Global
  500 financial institution (founded 1857, operating across Europe, Mexico, South America,
  Turkey, and the U.S.). This is a vendor case study — OpenAI selected the customer, chose
  which quotes and metrics to publish, and frames the narrative promotionally (a "Results
  at a glance" bullet box, a "Leadership lessons" bullet list, a closing "Contact sales"
  call to action) — not an independent report with disclosed methodology. The named
  executives are credible primary-source voices for what happened inside BBVA, but no
  metric in the article has an accompanying measurement methodology (time window, sample,
  survey instrument).
- **Scope**: Covers BBVA's ChatGPT Enterprise adoption trajectory (2024 pilot to ~100,000
  employees), the three-pillar adoption strategy (trust, governance, structured learning),
  the champions/"wizards" enablement network, leadership training program, custom-GPT
  creation volume, three named production GPT use cases (credit risk, legal, customer
  experience) plus one named market-level deployment (Peru), and a six-item "Leadership
  lessons" list. Does NOT cover: technical implementation details of any GPT (prompts,
  data pipelines, model versions), cost or licensing terms, any failure mode or rollback,
  how "efficiency gains" or "weekly active usage" were measured, or any detail on
  "The Eight" roadmap's eight initiatives beyond the six areas named in prose (customer
  experience, commercial banking, risk, operations, software development, employee
  productivity).

## Extracted Claims

### Claim 1: BBVA and OpenAI formed a strategic alliance centered on "The Eight" — an AI transformation roadmap for redesigning banking end-to-end across customer experience, commercial banking, risk, operations, software development, and employee productivity
- **Evidence**: Direct article statement describing the scope and evolution of the partnership from an initial collaboration into a named roadmap by the end of 2025.
- **Confidence**: anecdotal (named strategic initiative with no detail on the two remaining named-but-uncounted areas of "The Eight," no timeline for individual initiatives, no measurable milestones)
- **Quote**: "By the end of 2025, that collaboration had evolved into a broader strategic alliance centered around \"The Eight,\" BBVA's AI transformation roadmap for redesigning banking end-to-end—from customer experience and commercial banking to risk, operations, software development, and employee productivity."
- **Our assessment**: "The Eight" is a named, branded transformation roadmap, but the article only enumerates six areas in this sentence despite the name implying eight distinct initiatives — the remaining two (or the precise eight-way breakdown) are never listed. This is the same pattern seen in `blog-openai-endava-frontiers.md` Claim 5 ("DavaFlow"): a branded internal methodology name asserted with sweeping scope but no phase-by-phase enumeration. Treat as evidence that a named, board-level roadmap exists, not as evidence of its internal structure or completeness.

### Claim 2: BBVA's ChatGPT Enterprise deployment grew from an initial 3,000-employee pilot in 2024 to more than 100,000 employees globally, described as one of the largest enterprise generative-AI deployments in the financial sector
- **Evidence**: Direct before/after figures with a named starting point (2024, multiple countries and business areas) and current state ("Today more than 100,000 employees globally use ChatGPT Enterprise").
- **Confidence**: emerging (specific named headcount figures at two points in time; single-company, self-reported, no independent verification of "one of the largest" claim)
- **Quote**: "The relationship between BBVA and OpenAI began in 2024 with an initial deployment of ChatGPT Enterprise to 3,000 employees across multiple countries and business areas." ... "Today more than 100,000 employees globally use ChatGPT Enterprise, making BBVA one of the largest enterprise adopters of generative AI in the financial sector."
- **Our assessment**: A ~33x headcount expansion (3,000 → 100,000) is the largest ChatGPT Enterprise scale-up figure in the corpus, larger than any Cursor/Claude enterprise case study documented so far (PayPal: 8,000 developers; Coinbase: 2,400 developers; Endava: ~11,000 total headcount with no ChatGPT-specific seat count given). Note this figure counts total ChatGPT Enterprise *seats* across an entire bank workforce (legal, risk, engineering, operations, finance, marketing, customer service — Claim 3), not engineering-only adoption, which is a different population than the coding-tool adoption metrics in the Cursor case studies.

### Claim 3: For a highly regulated global bank, BBVA built its AI adoption strategy around three pillars — trust, governance, and structured learning — aligning security, legal, compliance, and technology teams from the outset rather than allowing unauthorized use of consumer AI tools
- **Evidence**: Direct article statement describing BBVA's adoption strategy and the deliberate choice to provide secure enterprise access instead of tolerating shadow-IT consumer-tool use.
- **Confidence**: emerging (specific named strategy with a clear rationale; single company; no detail on how the three pillars were operationalized beyond team alignment)
- **Quote**: "For a highly regulated global bank, scaling AI required more than simply deploying licenses. BBVA built its AI adoption strategy around three core pillars: trust, governance, and structured learning." ... "Rather than allowing unauthorized experimentation with consumer AI tools, the bank chose to provide employees with secure enterprise-grade access and formal enablement programs."
- **Our assessment**: This is the clearest regulated-industry adoption framing in the article and the most guide-relevant claim: BBVA explicitly names shadow-IT prevention (blocking unauthorized consumer-tool use) as a driver of its enterprise rollout decision, not just a productivity goal. This corroborates the general pattern in `blog-anthropic-legal-industry-deploy.md` and `blog-anthropic-cowork-deploy-guide.md` that regulated-industry Foundation/Month-1 phases start with security and privilege review before user-facing rollout — BBVA names the same sequencing logic (governance before scale) from a banking rather than legal-services context, and from OpenAI's ecosystem rather than Anthropic's, which is a new vendor-independent data point for this pattern.

### Claim 4: BBVA built a two-tier enablement network — an organization-wide "AI champions" network plus a smaller cohort of advanced users called "wizards" — who run hands-on workshops and help colleagues integrate ChatGPT into workflows
- **Evidence**: Direct article statement naming both tiers and their function.
- **Confidence**: emerging (named organizational structure with a specific two-tier design; single company; no headcount given for either tier)
- **Quote**: "To support adoption at scale, BBVA created a structured enablement framework that included an organization-wide AI champions network, along with advanced users known internally as AI \"wizards.\" These teams lead hands-on workshops, help colleagues integrate ChatGPT into everyday workflows, and identify valuable use cases across the organization."
- **Our assessment**: This directly corroborates the "champion network" adoption mechanism already documented at length in `blog-anthropic-cowork-deploy-guide.md` (Claim 9: champion-authored skills as the leading pilot-success indicator) and `blog-anthropic-legal-industry-deploy.md` (the same champion pattern applied to legal). BBVA's contribution is novel within that pattern: a named *second tier* ("wizards") above general champions — the corpus previously documented only a single champion tier. This is independent, vendor-external (OpenAI ecosystem, not Anthropic) confirmation that champion networks are a general enterprise AI adoption mechanism, not something specific to Claude Cowork's prescribed rollout framework, and it adds a two-tier variant the guide has not yet captured.

### Claim 5: BBVA trained 250 leaders, including the CEO and chairman, and members of the executive committee are now among the company's most active ChatGPT users
- **Evidence**: Direct article statement naming a specific leadership-training headcount and describing current executive usage behavior.
- **Confidence**: emerging (specific named figure; single company; "most active users" is not quantified relative to the rest of the 100,000-employee base)
- **Quote**: "Leadership participation became a major accelerator for adoption. BBVA provided specific training to 250 leaders, including the CEO and chairman, and today members of the executive committee are among the company's most active ChatGPT users."
- **Our assessment**: This is the largest named leadership-training cohort (250 leaders) in the corpus for an enterprise AI rollout, and it names the CEO and chairman specifically as trained participants — a stronger executive-modeling claim than `blog-cursor-coinbase-agent-first-adoption.md` Claim 6 (a single named engineering executive, Turakhia, personally modeling daily tool use) or `blog-cursor-paypal-enterprise-adoption.md`'s general leadership framing. BBVA's claim operates at board/C-suite level (chairman, CEO) rather than engineering-leadership level, which is a new organizational altitude for the "leaders must use the tool themselves to drive adoption" pattern already established across the corpus.

### Claim 6: BBVA employees have built more than 20,000 custom GPTs across the organization, with approximately 4,000 used frequently by teams worldwide
- **Evidence**: Direct article statement with specific counts for total GPTs created versus frequently-used GPTs.
- **Confidence**: emerging (specific named figures; single company; no definition given for "used frequently," no time window for the 20,000 count)
- **Quote**: "As adoption expanded, employees across BBVA began building custom GPTs tailored to specialized workflows across legal, risk, customer service, finance, and marketing. To date, employees have created more than 20,000 GPTs across the organization, with approximately 4,000 used frequently by teams around the world."
- **Our assessment**: This is the first custom-GPT creation-volume metric in the corpus. The ratio is notable: roughly 1 in 5 employee-built GPTs (4,000 of 20,000+) sees frequent reuse, implying substantial one-off or abandoned tool creation alongside genuine reuse — the article does not explain this gap, and it is a plausible signal that bottom-up tool proliferation at this scale produces significant redundancy/waste alongside genuine value, a tension the article does not address. For the guide, this is useful as a scale calibration point (what "grassroots tool building" looks like at 100,000-employee scale) but the 20%-frequent-use ratio deserves a skeptical read rather than being cited as a pure success metric.

### Claim 7: BBVA's Credit Analysis Pro GPT accelerates credit risk assessments by extracting and analyzing unstructured data from annual reports, ESG disclosures, and media coverage, letting analysts focus on strategic analysis instead of manual data-gathering
- **Evidence**: Named production GPT with a specific function description and stated before/after shift in analyst time allocation.
- **Confidence**: anecdotal (named tool and function description; no adoption count, no time-savings figure, no accuracy/error-rate data for the extraction step)
- **Quote**: "In credit risk, BBVA developed Credit Analysis Pro GPT, which accelerates assessments by extracting and analyzing unstructured data from annual reports, ESG disclosures, and media coverage—work that was previously manual and time-intensive. By automating these tasks, analysts can focus more on strategic analysis and higher-value work, including how ESG factors are incorporated into risk models."
- **Our assessment**: This is a banking-specific instance of the "integrity layer / narrative on top" division of labor named in `blog-anthropic-fong-finance-narrative.md` Claim 5 — mechanical data extraction shifts to the tool, analytical judgment (how ESG factors feed risk models) stays with the human. It is a much thinner claim than Kepler's architecture in `blog-anthropic-kepler-verifiable-ai-financial.md`: Kepler describes a production system with an explicit deterministic-execution/reasoning-layer separation and provenance chain for auditability; BBVA's Credit Analysis Pro GPT is described only as an extraction-and-analysis tool with no architectural detail, no mention of how outputs are verified before entering a credit decision, and no auditability claim at all — a meaningful gap given that credit risk assessment is exactly the kind of regulated, auditable decision Kepler's architecture is built to support. The guide should not treat this GPT as evidence of verifiable/auditable AI in credit decisioning; it is evidence only of adoption breadth.

### Claim 8: BBVA's Retail Banking Legal Assistant GPT drafts responses to approximately 40,000 annual client-related legal inquiries from branch managers, pulling from multiple internal knowledge sources for a nine-person legal team
- **Evidence**: Named production GPT with a specific annual inquiry volume and a specific team size it serves.
- **Confidence**: anecdotal (named tool with specific volume and headcount figures; no accuracy, error-rate, or human-review-rate data for the drafted responses)
- **Quote**: "In legal services, BBVA created a Retail Banking Legal Assistant GPT to help respond to approximately 40,000 annual client-related legal inquiries received from branch managers. The GPT drafts responses by pulling from multiple internal knowledge sources, dramatically reducing manual research time for the nine-person legal team."
- **Our assessment**: The 40,000-inquiries/9-person-team ratio (≈4,444 inquiries per legal team member per year, ≈17 per business day per person) is the most concrete leverage metric in the article — it makes explicit how implausible the pre-GPT workload was for a team that size, which is itself evidence of the demand pressure driving adoption regardless of measured output quality. The article states the GPT "drafts responses" (not "sends responses"), implying a human-in-the-loop review step, but does not describe what that review consists of or how much time it still takes — the "dramatically reducing manual research time" claim is about the research step specifically, not the full response cycle. Compare to `blog-anthropic-legal-industry-deploy.md`'s prescribed legal-industry pilot metrics (cycle time reduction, draft-acceptance-without-rewrite rate): BBVA's case study does not report either of those metrics for this GPT, so it cannot be used as evidence of drafting quality, only of adoption scale.

### Claim 9: BBVA's Client Experience Assistant GPT in Mexico analyzes thousands of open-ended customer survey responses to accelerate sentiment analysis, surface key themes, and recommend actions
- **Evidence**: Named production GPT with a specific market (Mexico) and function description.
- **Confidence**: anecdotal (named tool and function; no volume-of-surveys figure beyond "thousands," no measurement of decision quality or action-adoption rate from the recommendations)
- **Quote**: "In Mexico, a Client Experience Assistant GPT analyzes thousands of open-ended customer survey responses, accelerating sentiment analysis, surfacing key themes, and recommending actions that help improve customer experience faster and at scale."
- **Our assessment**: This is a customer-facing (rather than internal-productivity) application of unstructured-text analysis at BBVA, distinct from the credit-risk and legal-assistant GPTs, which are both internal-employee-facing tools. It is the thinnest-evidenced of the three named GPTs in the article — no before/after timing, no volume beyond "thousands," and no description of what "recommending actions" means operationally (is the recommendation reviewed by a human before any customer-facing change is made?). Treat as a named use-case category (survey-to-action pipeline) rather than a measured outcome.

### Claim 10: In Peru, more than 3,000 employees use an internal AI assistant that reduced average query-handling time from approximately 7.5 minutes to around 1 minute — roughly an 80% efficiency improvement
- **Evidence**: Named market deployment with a specific before/after timing metric and headcount.
- **Confidence**: emerging (specific before/after timing figures and headcount for a named market; single deployment; no description of what "query handling" covers or how the timing was measured)
- **Quote**: "In Peru, more than 3,000 employees now use an internal AI assistant that has reduced average query handling times from approximately 7.5 minutes to around 1 minute—an efficiency improvement of roughly 80%."
- **Our assessment**: This is the single most concrete, quantified before/after metric in the article — most other claims (Credit Analysis Pro, Legal Assistant, Client Experience Assistant) give no timing data at all. The 7.5-minute-to-1-minute reduction (≈87% time reduction, which the article rounds to "roughly 80%") is directly comparable to `blog-cursor-coinbase-agent-first-adoption.md` Claim 2 (8 days → under 30 minutes for idea-to-first-PR) and `blog-anthropic-legal-industry-deploy.md`'s cycle-time pilot metric, in that all three name a specific task-completion-time reduction as the adoption evidence. This is the strongest single data point in the source and the one most defensible to cite for "efficiency gains from an AI assistant in a regulated financial-services task," though it remains single-market, self-reported, and without a stated measurement methodology.

### Claim 11: Six "Leadership lessons" are presented as principles that emerged from BBVA's AI rollout — treating AI as business transformation, building with domain expertise, scaling securely from day one, empowering employees, training leadership early, and shifting from reactive to proactive banking
- **Evidence**: Verbatim bulleted list under the "Leadership lessons" heading, each with a one- or two-sentence elaboration.
- **Confidence**: anecdotal (vendor-authored/vendor-curated lessons list; no detail on how these six were selected or whether other lessons were considered and excluded)
- **Quote**: "Treat AI as business transformation: BBVA approached AI as a redesign of customer experience, operations, and ways of working across the organization — not as a standalone innovation effort."
- **Our assessment**: This "lessons learned" bulleted-list format is structurally identical to `blog-openai-endava-frontiers.md`'s "Lessons learned from Endava" list (Concrete Artifacts there) — both OpenAI customer-story pages use the same template: named metrics box, quoted executives, a "Results at a glance" bullet list, and a closing lessons-learned bullet list. The "treat AI as business transformation, not a standalone innovation effort" lesson here is nearly identical in substance to Endava's "Treat AI adoption as a behavior change, not a software rollout" lesson — this is now two independent OpenAI customer case studies (different industries: banking vs. IT consulting) converging on the identical framing, which is more likely evidence of OpenAI's house editorial framing being applied consistently across customer stories than two companies independently arriving at the same conclusion. The guide should treat this as *OpenAI's preferred narrative frame* for enterprise case studies, corroborating but not independently strengthening the underlying "adoption is organizational change, not tooling" claim already well-established via Anthropic-ecosystem sources.

### Claim 12: Carlos Torres Vila, BBVA's Chair, frames the OpenAI alliance's goal as creating a "smarter, more proactive, and completely personalized banking experience" that anticipates client needs
- **Evidence**: Direct pull-quote attributed to the Chair of BBVA, presented as a standalone block quote near the top of the article.
- **Confidence**: anecdotal (single executive's strategic framing; aspirational language; not a description of a currently operating capability)
- **Quote**: "Our alliance with OpenAI accelerates the native integration of artificial intelligence across the bank to create a smarter, more proactive, and completely personalized banking experience, anticipating the needs of every client."
- **Our assessment**: This is board-chair-level strategic framing (the highest executive altitude quoted in this article, and higher than any single quote source previously in the corpus for an enterprise AI adoption case study — Endava's quotes are all from the CTO, PayPal's and Coinbase's from SVP/Director-level executives). The "anticipating the needs of every client" language is aspirational proactive-AI framing rather than a description of a deployed capability — the rest of the article's concrete evidence (Credit Analysis Pro, Legal Assistant, Client Experience Assistant, Peru assistant) describes reactive/assistive tools, not predictive/anticipatory ones. Treat this quote as leadership vision-setting, not as evidence that BBVA has deployed anticipatory/proactive banking AI.

## Concrete Artifacts

```
Source: OpenAI, "BBVA puts AI at the core of banking with OpenAI,"
https://openai.com/index/bbva (published June 11, 2026; retrieved via
Wayback Machine snapshot of the live page — see Extraction Notes)

"Results at a glance" (verbatim bulleted list):
  - 100,000 employees using ChatGPT Enterprise globally
  - 70%+ weekly active usage across deployed employees
  - ~3 hours saved per employee, per week
  - Up to 80% efficiency gains in selected workflows
  - 250 senior leaders trained, including the CEO and chairman
  - Security, legal, and compliance aligned from day one
  - Employee-led AI adoption across business functions
  - 8 major transformation initiatives under "The Eight"

"Leadership lessons" (verbatim bulleted list with elaborations):
  - Treat AI as business transformation: BBVA approached AI as a redesign of
    customer experience, operations, and ways of working across the
    organization — not as a standalone innovation effort.
  - Build with domain expertise: The collaboration combines OpenAI's frontier
    AI capabilities with BBVA's deep expertise in banking, risk, operations,
    and customer experience.
  - Scale securely from day one: Transforming a global financial institution
    with AI requires governance, data architecture, and security frameworks
    designed to scale across the organization.
  - Empower employees with AI: By extending AI capabilities broadly across
    the workforce, BBVA is enabling employees to become active participants
    in the bank's transformation.
  - Train leadership early: AI adoption accelerates when senior leaders
    actively use the technology themselves. Early training programs for
    executives — including the CEO and chairman — help establish AI as a
    strategic priority across the organization.
  - Move from reactive to proactive banking: The long-term ambition is not
    simply greater efficiency, but a more intelligent and personalized
    banking experience capable of anticipating customer needs.

Named production GPT workflows (verbatim, condensed):
  Credit Analysis Pro GPT (Credit Risk):
    "accelerates assessments by extracting and analyzing unstructured data
    from annual reports, ESG disclosures, and media coverage"
  Retail Banking Legal Assistant GPT (Legal, 9-person team):
    "help respond to approximately 40,000 annual client-related legal
    inquiries received from branch managers... drafts responses by pulling
    from multiple internal knowledge sources"
  Client Experience Assistant GPT (Mexico):
    "analyzes thousands of open-ended customer survey responses,
    accelerating sentiment analysis, surfacing key themes, and recommending
    actions"
  Peru internal AI assistant (3,000+ employees):
    "reduced average query handling times from approximately 7.5 minutes to
    around 1 minute—an efficiency improvement of roughly 80%"
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-deploy-guide.md` Claim 9 (champion-authored skills as the leading
    pilot-success indicator) and `blog-anthropic-legal-industry-deploy.md`'s champion-network
    material: BBVA's "AI champions network" (Claim 4) is independent, vendor-external
    (OpenAI, not Anthropic) confirmation that champion-driven enablement is a general
    enterprise AI adoption mechanism rather than an Anthropic/Cowork-specific prescription.
    BBVA adds a two-tier variant ("champions" plus a smaller "wizards" cohort) not previously
    documented in the corpus.
  - `blog-anthropic-legal-industry-deploy.md` and `blog-anthropic-cowork-deploy-guide.md`
    (Foundation/Month-1 phases begin with security and privilege review before user rollout):
    BBVA's three-pillar strategy (trust, governance, structured learning — Claim 3) and its
    explicit rationale of preventing "unauthorized experimentation with consumer AI tools"
    corroborates the governance-before-scale sequencing already documented for regulated
    industries, now from a banking context and a different vendor ecosystem.
  - `blog-cursor-coinbase-agent-first-adoption.md` Claim 6 and `blog-cursor-paypal-enterprise-adoption.md`
    (leaders modeling tool use drives adoption): BBVA's leadership-training claim (Claim 5 —
    250 leaders including CEO and chairman) corroborates this pattern at a higher executive
    altitude (board chair/CEO) than either Cursor case study, which quote engineering or
    business-unit executives, not the CEO/chair directly.
  - `blog-openai-endava-frontiers.md`: Both are OpenAI customer-story pages sharing an
    identical article template (metrics summary box, "Results at a glance" bullet list,
    named-executive quotes, closing "Lessons learned" bullet list). BBVA's "Treat AI as
    business transformation... not a standalone innovation effort" lesson (Claim 11) is
    substantively identical to Endava's "Treat AI adoption as a behavior change, not a
    software rollout" lesson — this is likely evidence of OpenAI's consistent house framing
    across customer stories, not independent convergence by two companies.
  - `blog-anthropic-fong-finance-narrative.md` Claim 5 ("integrity layer / narrative on top"
    division of labor): BBVA's Credit Analysis Pro GPT (Claim 7 — automating unstructured
    data extraction so analysts "focus more on strategic analysis") is a banking-specific
    instance of the same mechanical-work/judgment-work division documented in Fong's finance
    workflow note, though with far less operational detail.

- **Contradicts**: None filed. The article presents no claim that materially opposes an
  existing source note or disagrees with itself on guidance or claim direction (per
  MINER.md §4a), so no contradiction issue is warranted.

- **Extends**:
  - `blog-openai-endava-frontiers.md`: extends the corpus's small set of OpenAI enterprise
    customer-story sources with a second data point — banking rather than IT
    consulting/services, and with substantially more quantitative detail (named headcounts,
    before/after timing metrics, GPT-creation counts) than Endava's entirely metric-free
    article.
  - `blog-anthropic-cowork-deploy-guide.md` and `blog-anthropic-legal-industry-deploy.md`:
    extends the champion-network adoption pattern with a two-tier ("champions" + "wizards")
    variant and demonstrates it operating at a much larger scale (~100,000 employees) than
    any single deployment previously documented in the corpus.
  - `blog-anthropic-kepler-verifiable-ai-financial.md`: BBVA's Credit Analysis Pro GPT
    (Claim 7) sits at the opposite end of the architectural-rigor spectrum from Kepler's
    deterministic-execution/provenance architecture — both are financial-services credit/risk
    AI applications, but BBVA's case study gives zero architectural or verification detail,
    which sharpens the guide's ability to contrast "adoption breadth" evidence (BBVA) against
    "verifiable architecture" evidence (Kepler) as two distinct and non-substitutable kinds
    of financial-AI source material.

- **Novel**:
  - **Two-tier "champions" + "wizards" enablement structure** (Claim 4): No prior corpus
    source documents a second, more-advanced tier above general adoption champions.
  - **Custom-GPT creation-volume metrics at enterprise scale** (Claim 6 — >20,000 GPTs
    created, ~4,000 frequently used): This is the corpus's first quantified measure of
    bottom-up, employee-built-tool proliferation at large-enterprise scale, including the
    (unexplained) gap between tools created and tools reused.
  - **Named legal-team leverage ratio** (Claim 8 — 40,000 annual inquiries against a
    9-person legal team) is the most extreme headcount-to-volume ratio documented in the
    corpus for any AI-assisted knowledge-work function.
  - **Board-chair-level executive quote and leadership-training cohort** (Claims 5 and 12):
    BBVA is the first corpus source to name a company chair/CEO explicitly as a
    trained, active AI tool user, rather than a business-unit or engineering executive.
  - **BBVA/banking as a new regulated-industry vertical** in the corpus's growing set of
    financial-services AI sources (alongside Kepler's B2B fintech SaaS and Anthropic's
    internal finance-function usage) — BBVA is the first traditional, large-scale
    consumer/commercial retail bank documented.

## Guide Impact

- **Chapter 05 (Team Adoption) / Chapter 04 (Enterprise Integration Patterns)**: Add BBVA's
  three-pillar regulated-industry adoption strategy (Claim 3 — trust, governance, structured
  learning; explicit rationale of preventing shadow-IT consumer-tool use) as a second,
  vendor-independent data point alongside the Anthropic Cowork/legal-industry deployment
  guides' Foundation-phase security-first sequencing. Note both arrive at the same
  governance-before-scale principle from different vendor ecosystems.
- **Chapter 05 (Team Adoption)**: Add the two-tier "champions" + "wizards" enablement
  structure (Claim 4) as a named variant of the champion-network pattern already documented
  from Anthropic sources — the guide's champion-network material currently describes only a
  single tier; BBVA's cohort structure (broad champions network plus a smaller advanced
  "wizards" tier) is a concrete elaboration worth adding.
- **Chapter 05 (Team Adoption)**: Add BBVA's leadership-training program (Claim 5 — 250
  leaders including CEO and chairman) as the highest-executive-altitude instance of the
  "leaders must use the tool themselves" pattern documented in the corpus; pair with Carlos
  Torres Vila's Chair-level quote (Claim 12) as illustrative material, with the caveat that
  it is vision-setting rhetoric, not a description of a deployed capability.
- **Chapter 04 (Enterprise Integration Patterns)**: Add the custom-GPT creation-volume metric
  (Claim 6) as a scale calibration point for what grassroots, employee-built-tool adoption
  looks like at 100,000-employee scale, with the explicit caution that only ~20% of created
  GPTs see frequent reuse — the guide should present this as a real trade-off of bottom-up
  tool proliferation (broad experimentation vs. redundancy/waste), not as an unqualified
  success metric.
- **Chapter 03 (Safety and Verification), if discussing financial-services AI**: Use BBVA's
  Credit Analysis Pro GPT (Claim 7) as a contrast case against Kepler's deterministic
  execution/provenance architecture (`blog-anthropic-kepler-verifiable-ai-financial.md`):
  BBVA demonstrates adoption breadth in a credit-risk use case with zero architectural or
  auditability detail, which is a materially different (and weaker) form of evidence than
  Kepler's production verifiability architecture. The guide should not conflate "a bank is
  using AI for credit analysis" with "a bank has built auditable AI for credit analysis."
- **Any chapter citing headline usage figures**: The one usage-level figure in the article
  is "70%+ weekly active usage across deployed employees" (Results at a glance). Cite it as
  a weekly-active-usage level, and note it is a single self-reported figure with no stated
  measurement methodology (sample, window definition).

## Extraction Notes

- The live URL (`https://openai.com/index/bbva`) returned HTTP 403 to both the WebFetch tool
  and direct `curl` with a browser user-agent — the response body was a client-side loading
  shell (a JS-app loading spinner page), not the rendered article, consistent with prior
  OpenAI-domain extraction difficulties noted in `blog-openai-endava-frontiers.md`'s and
  `blog-openai-codex-knowledge-work.md`'s Extraction Notes. Unlike the Endava extraction
  (which succeeded via the `r.jina.ai` proxy), this source was retrieved via a Wayback
  Machine snapshot (`web.archive.org/web/2026/https://openai.com/index/bbva/`), which
  returned a full HTML capture of the rendered page (HTTP 200). The page text was extracted
  from that HTML with a local Python `HTMLParser`-based script (stripping `script`/`style`/
  `nav`/`header`/`footer` tags) rather than WebFetch, since WebFetch is blocked from fetching
  `web.archive.org` directly in this environment. All quotes in this note were copied
  character-for-character from that extracted text.
- The article contains a "Keep reading" footer linking to three unrelated OpenAI news posts
  (an agents-transforming-work piece, a Broadcom chip announcement, a global-affairs post) —
  none are substantively linked follow-on material for this case study, so none were
  followed as sub-pages.
- The article is genuinely metric-richer than `blog-openai-endava-frontiers.md` (which had
  zero quantitative outcome data): BBVA's version of the OpenAI customer-story template
  includes an eight-bullet "Results at a glance" list, and three named production GPT use
  cases plus one named market deployment (Peru) with a specific before/after timing metric.
  All twelve claims above are reflected in the
  article's ~900 words; this is not a case of shallow reading, but the source itself gives
  no methodology for any metric (measurement window, sample size, survey instrument), so
  confidence is capped at "emerging" for the better-evidenced claims and "anecdotal" for the
  named-GPT descriptions that lack any quantitative backing.
- No contradiction issue was filed: the article contains no claim that materially opposes an
  existing source note or disagrees with itself on guidance or claim direction — see
  Cross-References → Contradicts.
- All cross-reference claim numbers cited above (from `blog-openai-endava-frontiers.md`,
  `blog-anthropic-cowork-deploy-guide.md`, `blog-anthropic-legal-industry-deploy.md`,
  `blog-anthropic-fong-finance-narrative.md`, `blog-anthropic-kepler-verifiable-ai-financial.md`,
  `blog-cursor-coinbase-agent-first-adoption.md`, and `blog-cursor-paypal-enterprise-adoption.md`)
  were verified by re-reading each cited note's actual claim numbering and content before
  writing this note; none were guessed.
