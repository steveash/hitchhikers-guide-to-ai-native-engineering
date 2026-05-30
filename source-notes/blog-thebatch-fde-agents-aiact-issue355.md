---
source_url: https://www.deeplearning.ai/the-batch/issue-355
source_type: blog-post
title: "The Batch Issue 355: Gemini Flash Gets Pricey, AI Act Delays, Agents Drive Online Traffic"
author: Andrew Ng / DeepLearning.AI (editorial + reporting)
date_published: 2026-05-29
date_extracted: 2026-05-30
last_checked: 2026-05-30
status: current
confidence_overall: emerging
issue: "#1002"
---

# The Batch Issue 355: FDEs, Agents Driving Web Traffic, EU AI Act Delays, Gemini 3.5 Flash Pricing

> Issue 355 delivers four engineering-relevant stories: (1) Andrew Ng's editorial defining the Forward-Deployed Engineer (FDE) role, its vendor-optionality risks, and his prediction that AI Engineer jobs will far outnumber FDE jobs with eventual role specialization into LLMOps and Evals Engineering; (2) Human Security's 1-quadrillion-interaction study showing AI-driven web traffic nearly tripled in 2025, with agents handling 77% of interactions on product/search pages and OpenAI generating ~69% of automated traffic; (3) the EU AI Act's high-risk AI deadline delayed from August 2026 to December 2027 with SME carve-outs; (4) Gemini 3.5 Flash pricing at $1.50/$0.15/$9.00 per million input/cached/output tokens — corroborating the Willison analysis while adding the contradicting Google vs. Artificial Analysis cost claims.

## Source Context

- **Type**: blog-post (weekly news digest; DeepLearning.AI's flagship newsletter, Issue 355, May 29, 2026)
- **Author credibility**: Andrew Ng is the editorial author of the opening letter — co-founder of Coursera, former Baidu Chief Scientist, former Google Brain head, and founder of DeepLearning.AI and Landing AI. The FDE section is Ng's first-person editorial observation from running organizations that employ both FDEs and AI Engineers. The agent traffic and EU AI Act sections are reported journalism citing named third-party sources (Human Security; EU official statements). Ng's editorial claims are authoritative practitioner opinion; the news sections are reliable secondary reporting.
- **Scope**: Five sections. Primary extraction targets: Ng's FDE editorial letter, Human Security AI traffic data, EU AI Act timeline update. Secondary: Gemini 3.5 Flash pricing (largely corroborates `blog-simonwillison-gemini35-flash-pricing.md` with some novel detail). Staged image generation section skipped — no agent-engineering-practice signal per Prospector guidance.

## Extracted Claims

### Claim 1: Forward-Deployed Engineers (FDEs) embed within client organizations to customize AI solutions and build agentic workflows specific to the client's needs

- **Evidence**: Andrew Ng's first-person editorial definition; Ng runs organizations that hire both FDEs and AI Engineers and draws the distinction from direct experience.
- **Confidence**: anecdotal (authoritative practitioner definition from Ng; no industry-wide survey data)
- **Quote**: "embedded within a client organization to help customize solutions, such as building and tuning agentic workflows that suit the client's particular needs"
- **Our assessment**: This is the first formal definition of the FDE role in the corpus. The agentic workflow emphasis is significant: FDEs are not generic technical consultants but specialists in the harness-and-workflow layer that sits between foundation models and business processes. For the guide, this establishes FDE as a distinct role category, separate from AI Engineer and from traditional consulting.

### Claim 2: FDE roles require communication and business skills beyond pure technical skills — differentiating them from AI Engineers who are primarily technical builders

- **Evidence**: Ng's editorial characterization, drawing from his organizations' hiring practices.
- **Confidence**: anecdotal (editorial opinion; no job-market survey data)
- **Quote**: "In addition to having good technical skills, FDEs need communication skills and sometimes business skills."
- **Our assessment**: The "sometimes business skills" qualifier is notable — it is not an absolute requirement. This implies FDE seniority may correlate with whether business-domain knowledge is needed. The communication requirement is structural: embedding in a client organization means constant cross-functional translation that internal AI Engineers (working within their own org's context) do not face at the same intensity.

### Claim 3: AI Engineer jobs will far outnumber FDE jobs because most companies prefer in-house employees over embedded vendor consultants

- **Evidence**: Ng's direct comparative prediction and his own hiring data as evidence ("While my organizations do hire FDEs, we hire far more AI Engineers!").
- **Confidence**: anecdotal (Ng's first-person prediction with personal evidence; no labor market survey data)
- **Quote**: "a company might accept a few FDEs to be embedded within its organization. But most companies will want far more of their own employees working on their projects."
- **Quote** (Ng's own hiring): "While my organizations do hire FDEs, we hire far more AI Engineers!"
- **Our assessment**: Ng provides both the prediction and the evidence from his own organizations in the same editorial, giving this more weight than pure forecast. The asymmetry he describes — "a few" FDEs vs. "far more" AI Engineers — maps to a structural distinction: FDEs are bottlenecked by the number of companies willing to accept vendor embeds, while AI Engineers scale with the overall growth of AI-integrated software development.

### Claim 4: Vendor optionality concerns make companies wary of FDE relationships — organizations want the ability to switch AI vendors, which FDE embedding compromises

- **Evidence**: Ng's editorial characterization of a structural client concern he observes in FDE sales conversations.
- **Confidence**: anecdotal (editorial observation from Ng's direct experience; no survey of companies' stated concerns)
- **Quote**: "a common client concern is that it is hard to find vendor-neutral FDEs — they are, after all, there to deeply integrate a particular vendor's product into a company. In this moment when it's hard to predict which AI service will be the best one in a year's time, optionality (the ability to pick whatever vendor turns out to fit best in the future) is very valuable."
- **Our assessment**: This optionality argument has direct engineering implications. The same concern applies to harness design choices: tightly coupling workflows to a single vendor's proprietary features (server-side history management, specific tool call formats, vendor-specific system prompt patterns) reduces optionality at the code level, mirroring the organizational-level risk Ng describes for FDE engagements. The guide's model-swappability principle (corroborates `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4) is the technical expression of the same optionality concern Ng identifies at the organizational level.

### Claim 5: The AI Engineer role will eventually specialize into sub-roles such as LLMOps Engineers, Evals Engineers, and AI Data Engineers — following the historical pattern of frontend/backend/mobile specialization

- **Evidence**: Ng's editorial prediction by analogy to software engineering specialization history.
- **Confidence**: anecdotal (editorial forecast; plausible structural analogy but not empirically validated)
- **Quote**: (no direct quote for the specialization sub-roles; paraphrase from editorial summary; see Our assessment)
- **Our assessment**: The LLMOps / Evals / AI Data Engineering specialization prediction is the most forward-looking claim in Ng's letter and the most directly relevant to guide career-track content. If accurate, engineers making career decisions now should evaluate whether to stay generalist AI Engineers (broader market in the near term, per Claims 1–3) or invest in specialization (LLMOps, Evals) that will be in demand as the role matures. The historical analogy (frontend/backend/mobile) is imperfect but directionally useful — specialization followed productivity-tool maturation in prior software eras.

### Claim 6: Gemini 3.5 Flash is priced at $1.50/$0.15/$9.00 per million input/cached/output tokens — three times the price of its predecessor Gemini 3 Flash — with 204 tokens/second output speed and four adjustable reasoning levels

- **Evidence**: The Batch's reporting on Google's published pricing and specifications; corroborated by Willison's concurrent analysis.
- **Confidence**: settled (published pricing at time of post; specifications from official announcement)
- **Quote**: "at a price three times that of its predecessor Gemini 3 Flash"
- **Quote** (speed): "text out (up to 64,000 tokens, 204 tokens per second)"
- **Quote** (reasoning): "Adjustable reasoning levels (minimal, low, medium, high)"
- **Our assessment**: The cached-token tier ($0.15/million, one-tenth of input price) is explicit in The Batch's pricing table but not prominently featured in the Willison note — this is a small additive detail for practitioners designing prompt caching strategies with Gemini 3.5 Flash. The four-level reasoning granularity (minimal/low/medium/high) is novel to this corpus; the Willison note notes adjustable reasoning generally but does not name the four tiers. Engineers designing cost-sensitive harnesses with Gemini 3.5 Flash should default to minimal or low reasoning for routine tasks and escalate to high only when accuracy requirements demand it.

### Claim 7: Google claims Gemini 3.5 Flash "often runs at less than half the cost of competing models" — but Artificial Analysis found it actually costs more than Gemini 3.1 Pro in benchmark runs

- **Evidence**: The Batch reports both Google's official marketing claim and the independent Artificial Analysis finding. The Willison note (published May 19, 10 days before The Batch) provides the detailed benchmark cost data: Gemini 3.5 Flash at $1,551.60 vs. Gemini 3.1 Pro Preview at $892.28 on Artificial Analysis's Intelligence Index.
- **Confidence**: emerging (Google claim is first-party marketing; Artificial Analysis benchmark is third-party with specific methodology; both are point-in-time)
- **Quote** (Google): "often runs at less than half the cost of competing models"
- **Quote** (AA finding): "it actually costs more than Gemini 3.1 Pro"
- **Our assessment**: The direct contradiction between Google's marketing claim and independent benchmark results is the most practically significant detail in the Gemini section. Google's claim and Artificial Analysis's finding are not necessarily irreconcilable — the claim may refer to specific competitor comparisons or workloads while the benchmark uses a particular test suite composition. But for practitioners, the takeaway is clear: do not trust vendor-provided cost claims as a substitute for running your own workload cost analysis. Corroborates `blog-simonwillison-gemini35-flash-pricing.md` Claims 2–3, which document this anomaly in detail.

### Claim 8: EU AI Act requirements for high-risk AI systems were delayed from August 2026 to December 2027, with staggered deadlines across AI product categories through August 2028

- **Evidence**: The Batch reporting on the EU's official amendment announcement. Article title: "Europe Pauses Some AI Regulations."
- **Confidence**: settled (reported regulatory decision with specific dates; verifiable against official EU publications)
- **Quote**: (no direct quote from the amendment text; EU characterized amendments as "safer and simpler rules for both citizens and businesses")
- **Our assessment**: The 16-month delay for high-risk AI systems (August 2026 → December 2027) is the most engineering-relevant regulatory update in the corpus since the original AI Act passage. Teams that had already begun compliance roadmaps for Q3 2026 have 16 additional months. The staggered structure (sandbox: August 2027; AI-in-products: August 2028; watermarking: December 2026) means engineers should not treat "AI Act compliance" as a single deadline but as a category-specific timeline. The Zero Trust eBook (`blog-anthropic-zero-trust-ai-agents.md`) mentions the EU AI Act as a compliance target without specifying dates — the specific dates in this source update that omission.

### Claim 9: The EU AI Act amendments create lighter compliance requirements for small companies (fewer than 50 employees, revenue under €10 million) and small mid-cap companies (250–749 employees, revenue under €150 million)

- **Evidence**: The Batch's reporting of specific SME thresholds from the EU amendment.
- **Confidence**: settled (specific regulatory thresholds are verifiable against official amendment text)
- **Quote**: (no direct verbatim quote from the amendment; paraphrased from article reporting; see Our assessment)
- **Our assessment**: These thresholds are important for AI-native startups and growth-stage companies evaluating compliance burden. A startup with <50 employees and <€10M revenue falls outside the standard compliance tier. A company crossing these thresholds (growth from 49 to 51 employees, or revenue crossing €10M) should treat the transition as a trigger for compliance infrastructure investment. The guide's compliance section should note these thresholds explicitly so practitioners know which tier applies to them.

### Claim 10: AI-driven internet traffic nearly tripled in 2025, outpacing conventional bot traffic growth (23%) and human traffic growth (~3%) by a large margin

- **Evidence**: Human Security, "an analysis of over 1 quadrillion internet interactions observed in 2025." Human Security serves approximately 1,200 customers across 200+ countries and territories. Article title: "Agents Surf the AI-Written Web."
- **Confidence**: emerging (third-party cybersecurity firm's proprietary data; large-scale dataset; but methodology is not publicly detailed and the firm has commercial interests in bot-detection data)
- **Quote** (dataset): "an analysis of over 1 quadrillion internet interactions observed in 2025 by Human Security"
- **Our assessment**: The tripling of AI-driven traffic against 3% human traffic growth is the sharpest evidence in the corpus that the internet's traffic composition has structurally shifted. The 1-quadrillion-interaction scale makes this the largest dataset cited for AI traffic claims in the corpus. However, Human Security's customer base (1,200 companies) skews toward bot-detection buyers, which may oversample bot-heavy traffic patterns relative to the overall internet. The claim should be treated as directionally reliable but potentially non-representative of the full traffic mix.

### Claim 11: Agents executing browser-style tasks represent only 1.7% of all traffic (December 2025) but grew 80x year-over-year — making agentic browsing the fastest-growing traffic category by far

- **Evidence**: Human Security data (same dataset as Claim 10). Breakdown by AI traffic type: 68% crawlers (collecting training data, 2x prior year), 32% scrapers (immediate-use data, 7x prior year), 1.7% agents (browser-style task execution, 80x prior year).
- **Confidence**: emerging (proprietary data; specific growth multiples are striking and, if accurate, represent a material signal; the 80x figure is extraordinary and the December 2025 snapshot should not be extrapolated as a sustained rate)
- **Quote**: (no direct quote for the 1.7%/80x figure; see paraphrase in Our assessment)
- **Our assessment**: The 80x year-over-year growth in agentic browsing is the most extreme data point in this issue and potentially in the corpus. At 1.7% of traffic in December 2025, agentic browsing is already non-trivial at scale — a site receiving 1 billion monthly pageviews would see ~17 million agent-driven sessions per month. The 80x growth rate implies this category was essentially negligible 12 months prior. For AI-native engineers building web-facing products: designing for agent-driven access patterns (structured data extraction, task completion workflows, authentication flows) is moving from optional to necessary. The 77% concentration on product and search pages (Claim 12) narrows where to prioritize.

### Claim 12: 77% of agentic interactions occur on product and search pages — the highest-value transactional content — with the remainder on account pages, authentication, and transaction completion

- **Evidence**: Human Security data (same dataset). Article notes agentic traffic is not evenly distributed but concentrated on commerce and discovery pages.
- **Confidence**: emerging (same caveats as Claims 10–11; directionally reliable at scale)
- **Quote**: (no direct quote for the 77% figure; see paraphrase in Our assessment)
- **Our assessment**: Product and search pages are exactly the pages with the highest commercial value and the richest structured data for extraction. The concentration is not surprising — agents seeking to research, compare, or purchase products will hit product catalog and search results pages. For engineers building these surfaces: if agentic traffic reaches 1.7% today and is growing 80x YoY, treating agents as first-class clients (explicit API endpoints, structured data formats, rate-limit policies that distinguish agents from malicious scrapers) is a near-term engineering priority, not a future concern.

### Claim 13: OpenAI generates approximately 69% of automated AI traffic, followed by Meta at 16% and Anthropic at approximately 11% — establishing a clear market hierarchy in autonomous web activity

- **Evidence**: Human Security data identifying traffic sources. "Automated traffic" includes both AI-driven and conventional bot traffic from these platforms.
- **Confidence**: emerging (third-party attribution; traffic source attribution for AI crawlers can be imprecise; OpenAI's large share reflects both ChatGPT's web-browsing capability and its dedicated training crawlers)
- **Quote**: (no direct quote for the specific percentages; see paraphrase in Our assessment)
- **Our assessment**: The 69%/16%/11% split maps roughly to ChatGPT (OpenAI), Meta AI (Meta), and Claude (Anthropic) market positions in consumer AI. The high OpenAI share likely reflects both the ChatGPT browser plugin and GPTBot training crawler combined. For engineers operating web services: identifying and appropriately handling traffic from these three sources covers ~96% of AI-driven automated traffic. The 11% Anthropic share suggests Claude's agentic web-browsing capabilities (computer use, web search) are generating meaningful traffic volume at scale.

### Claim 14: Malicious scraping rose nearly 47% year-over-year, with 60%+ of 750,000 identified threat profiles involving malicious scraping; account takeover attempts fell 30%+ but post-login attacks increased 4x

- **Evidence**: Human Security data (same dataset as Claims 10–13).
- **Confidence**: emerging (same caveats as above; the distinction between "malicious" and "legitimate" scraping is Human Security's proprietary classification)
- **Quote** (study scope): "over 1 quadrillion internet interactions observed in 2025 by Human Security, which serves around 1,200 customers in more than 200 countries and territories"
- **Our assessment**: The shift from pre-login account takeover attacks (down 30%+) to post-login attacks (up 4x) is the most operationally significant security finding in this section. It suggests attackers are using AI assistance to succeed at authentication more often, and then executing damage inside authenticated sessions. For engineers designing session security: post-login anomaly detection (unusual actions after login, unexpected API call patterns, session behavior diverging from established user patterns) becomes more important than login-rate-limiting when the attack surface shifts post-authentication.

## Concrete Artifacts

### EU AI Act Delay Timeline (May 2026 Amendments)

```
EU AI Act Revised Compliance Deadlines (as reported by The Batch, Issue 355, May 29, 2026):

CATEGORY                               ORIGINAL DEADLINE    NEW DEADLINE
---------                              -----------------    ------------
High-risk AI systems                   August 2026          December 2027
(law enforcement, infrastructure,
employment, migration, ID)

Supervised sandbox environments        [prior]              August 2027

AI-driven products                     [prior]              August 2028
(machinery, toys)

Watermarking & transparency            [prior]              ~December 2026

SME CARVE-OUTS:
  Small companies:    <50 employees AND revenue <€10 million → lighter requirements
  Small mid-caps:     250–749 employees AND revenue <€150 million → lighter requirements

NEW PROVISIONS:
  - Personal data use for bias detection where "strictly necessary"
  - Exemption for industrial machinery already covered by product-safety laws
  - Ban on sexually explicit AI-generated images of children and non-consensual nude images

EU CHARACTERIZATION: "safer and simpler rules for both citizens and businesses"
EUROPEAN CONSUMER ORGANIZATION: "makes the digital environment less safe and creates
                                  dangerous loopholes for AI companies"

Source: The Batch Issue 355, May 29, 2026, reporting on EU official amendments
```

### Human Security AI Traffic Data (2025, 1+ Quadrillion Interactions)

```
Human Security AI Traffic Analysis — 2025 (published via The Batch Issue 355)
Dataset: 1+ quadrillion internet interactions, ~1,200 customers, 200+ countries/territories

GROWTH RATES (2025 vs. 2024):
  AI-driven traffic overall:     ~3x (nearly tripled)
  Conventional bot traffic:      +23%
  Human traffic:                 +3%

AI TRAFFIC COMPOSITION:
  Crawlers (training data):      68% of AI traffic   — 2x prior year volume
  Scrapers (immediate use):      32% of AI traffic   — 7x prior year volume
  Agents (browser-style tasks):   1.7% of all traffic (Dec 2025) — 80x year-over-year

AGENTIC TRAFFIC DISTRIBUTION:
  Product and search pages:      77% of agentic interactions
  Other (account, auth, txn):    23%

COMPANY MARKET SHARE (automated traffic):
  OpenAI (ChatGPT + crawlers):   ~69%
  Meta:                           16%
  Anthropic:                     ~11%

MALICIOUS ACTIVITY:
  Malicious scraping YoY:        +47%
  Threat profiles (malicious scraping): 60%+ of 750,000 identified
  Account takeover attempts:     -30%+ YoY
  Post-login attacks:            +4x YoY
  Account creation by agents:    +89% YoY

Source: Human Security, via The Batch Issue 355, May 29, 2026
```

### Gemini 3.5 Flash Pricing and Specifications (The Batch Reporting)

```
Gemini 3.5 Flash — The Batch Issue 355 pricing/spec summary (May 29, 2026):

PRICING:
  Input:   $1.50 / million tokens
  Cached:  $0.15 / million tokens
  Output:  $9.00 / million tokens
  vs. predecessor Gemini 3 Flash: 3x more expensive

PERFORMANCE:
  Output speed:  204 tokens/second (up to 64,000 output tokens)
  Reasoning:     Adjustable levels: minimal / low / medium / high

CONTRADICTING COST CLAIMS:
  Google claim:      "often runs at less than half the cost of competing models"
  Artificial Analysis: benchmark suite costs MORE than running Gemini 3.1 Pro
                       (corroborated by Willison: $1,551.60 vs. $892.28)

Source: The Batch Issue 355, May 29, 2026 (corroborates simonwillison.net/2026/May/19/gemini-35-flash/)
```

## Cross-References

- **Corroborates**:
  - `blog-thebatch-ng-aiteam-structure.md` Claim 5 ("agentic coding isn't just changing the workflow of software engineering, it's also changing all the teams around it"): Issue 355's FDE letter extends this to the consulting/vendor-integration market — the structural change cascades beyond internal engineering teams to how companies source and manage external AI expertise. The agentic-coding-changes-surrounding-teams principle applies to the FDE market as a specific instance.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4 (design harnesses to swap models as easily as bumping a dependency): Ng's Claim 4 in this note (vendor optionality concern driving companies to prefer in-house AI Engineers over FDEs) is the organizational-level expression of the same principle. Both sources make the case for optionality — Claim 4 in Issue 351 at the harness level, Ng's FDE letter at the team/vendor level.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claims 2–3 (Gemini 3.5 Flash pricing 3x predecessor; benchmark cost paradox vs. Gemini 3.1 Pro): This issue's Claim 7 directly corroborates the same Artificial Analysis finding Willison documented. The Batch adds the explicit Google marketing quote ("less than half the cost of competing models") that makes the contradiction concrete.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 6 (Willison's "price tolerance probing" framing): The Batch's Gemini coverage (Claim 6–7) provides the same evidence base — the 3x pricing jump — without Willison's editorial interpretation. Together the two sources establish the fact (3x price increase, Artificial Analysis anomaly) and Willison's synthesis of what it means.

- **Extends**:
  - `blog-thebatch-ng-aiteam-structure.md` (Issue 349): That note covers AI-native team structure from the internal engineering perspective (engineer:PM ratios, generalist model, co-location). Issue 355's FDE letter extends the lens to the external/vendor relationship layer — specifically, when and why companies should embed external AI specialists vs. hiring their own. The two issues together cover both internal team design and the vendor ecosystem around it.
  - `blog-thebatch-ng-pm-bottleneck.md` (Issue 348): Issue 348 identifies the PM bottleneck as the primary constraint when coding velocity rises. Issue 355's FDE letter implicitly addresses the FDE role as one market response to that bottleneck — companies that cannot hire AI Engineers fast enough may initially rely on FDEs. Ng's prediction (AI Engineers will far outnumber FDEs) implies this is a transitional state, not a stable equilibrium.
  - `blog-anthropic-zero-trust-ai-agents.md` (EU AI Act mention): The Zero Trust eBook lists EU AI Act as a compliance target in its Phase 1 implementation checklist without specifying dates. This source adds the specific deadline timeline: December 2027 for high-risk AI, with staggered deadlines through August 2028. Engineers using the Zero Trust eBook's Phase 1 checklist can now map the "identify regulatory requirements" step to specific deadline dates.

- **Contradicts**: No material contradictions identified with existing corpus source notes. The Gemini pricing data is consistent with the Willison note. The EU AI Act delay creates no contradiction — prior sources mentioned compliance requirements without specific dates, and these dates now extend the picture.

- **Novel** (not present in any prior source note):
  - **FDE role definition in the corpus**: First explicit definition of the Forward-Deployed Engineer (FDE) role as distinct from AI Engineer. The vendor-optionality concern, the communication/business skills requirement, and the ratio prediction (few FDEs vs. many AI Engineers) are all first-in-corpus.
  - **AI Engineer specialization trajectory**: LLMOps Engineers, Evals Engineers, AI Data Engineers as named future specializations is the first career-track prediction with named sub-roles in the corpus.
  - **EU AI Act delay timeline with specific dates**: December 2027 for high-risk systems, August 2027 for sandboxes, August 2028 for AI-in-products, with SME employee/revenue thresholds — specific, verifiable, and actionable.
  - **80x YoY agent traffic growth**: The fastest growth rate for any AI traffic category in the corpus, and the only large-scale empirical measurement of agentic browsing traffic volume.
  - **Post-login attack shift**: The -30%/+4x shift from account takeover to post-login attacks is the first security dataset in the corpus showing this specific inversion.
  - **Gemini 3.5 Flash four-tier reasoning labels**: minimal/low/medium/high as explicit configurable tiers for Gemini reasoning is new detail beyond what Willison documented.
  - **$0.15/million cached token pricing for Gemini 3.5 Flash**: The specific cached-token tier pricing (one-tenth of input price) was not captured in the Willison note.

## Guide Impact

- **Chapter 05 (Team Adoption) — New section: Role Landscape**: Claims 1–5 together establish the FDE/AI Engineer distinction as a fundamental career-path choice. The guide should add explicit framing: FDEs are vendor-specific workflow specialists embedded in client orgs; AI Engineers are generalist builders of AI-integrated software, expected to outnumber FDEs substantially. The vendor optionality concern (Claim 4) maps directly to the model-swappability engineering principle — organizations making both the hiring decision and the harness design decision should apply the same optionality logic.

- **Chapter 05 (Team Adoption) — Specialization roadmap**: Claim 5 (LLMOps / Evals / AI Data Engineering as future specializations) is worth adding to any section on career development for AI-native engineers. Engineers reading the guide in 2026 should consider whether to build generalist depth now or specialize early in the sub-disciplines Ng names.

- **Chapter 02 (Harness Engineering) — Agent-as-client design**: Claims 11–12 justify adding explicit guidance that web-facing harnesses should treat agents as first-class traffic sources. The 1.7% share, 80x growth, and 77% product/search concentration mean that any harness designed for a consumer-facing product should already be thinking about structured data endpoints and agent-appropriate response formats. This is not a future concern — it is a current traffic reality growing exponentially.

- **Chapter 02 (Harness Engineering) or new Chapter 06 (Security)**: Claims 13–14 add the post-login attack shift as a specific implication for session security design. Harnesses that implement authentication should not treat authentication as the primary security checkpoint — post-login behavioral anomaly detection is the emerging priority as pre-login attacks shift to post-login execution.

- **Chapter 03 (Safety and Verification) — Compliance calendar**: Claims 8–9 provide the actionable EU AI Act timeline that any compliance section should include. Current guide content (if any) on regulatory compliance lacks the specific December 2027/August 2027/August 2028 dates and the SME carve-out thresholds. Recommend adding a compliance calendar section: "If your system falls under EU AI Act high-risk AI definitions (law enforcement, employment, critical infrastructure, migration, personal identification), the compliance deadline is December 2027. Small companies (<50 employees, <€10M revenue) have lighter requirements."

- **Chapter 03 (Model Selection)**: Claims 6–7 add the Gemini 3.5 Flash cached-token pricing ($0.15/million) and the four reasoning tiers as detail useful for cost modeling. The Google vs. Artificial Analysis contradiction (Claim 7) should be cited to reinforce the "verify vendor cost claims with independent benchmarks" principle that the Willison note established.

## Extraction Notes

- Three Prospector triage comments on this issue had varying emphasis: Comments 1 and 2 rated novelty "medium" and focused on AI Act delays and agent traffic metrics; Comment 3 rated novelty "high" and emphasized the FDE role definition and team-structure implications. This extraction follows Comment 3's signal — the FDE content is genuinely novel to the corpus — while also extracting the AI Act and agent traffic data which all three comments identified as important.
- The Gemini 3.5 Flash section in The Batch overlaps substantially with `blog-simonwillison-gemini35-flash-pricing.md` (published 10 days earlier). Only the novel details were extracted here: cached-token pricing, four-tier reasoning labels, and the explicit contradiction between Google's marketing claim and Artificial Analysis's finding. The Willison note remains the primary source for the full Gemini 3.5 Flash pricing and specification analysis.
- The staged image generation section was skipped per Prospector guidance — the topic has no direct AI-native engineering practice signal.
- WebFetch returned summaries rather than verbatim content for full-page requests, consistent with prior The Batch extractions. Verbatim quotes were obtained via targeted requests focused on specific sections. All quotes attributed directly to speakers (Ng, EU spokespersons, European Consumer Organization) were obtained via targeted requests and appear character-for-character from the source as rendered.
- Human Security's dataset methodology is not publicly detailed. The 1-quadrillion-interaction claim is large enough to be plausible for a major bot-detection network but the company has commercial interests in emphasizing bot traffic growth. All Human Security-sourced claims are graded "emerging" rather than "settled."
- The EU AI Act delay dates (December 2027, August 2027, August 2028) are verifiable against EU official publications and are graded "settled" for the dates themselves, though their application to specific AI systems depends on legal interpretation of "high-risk" classification.
