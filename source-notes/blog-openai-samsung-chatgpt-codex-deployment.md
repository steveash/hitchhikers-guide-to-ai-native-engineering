---
source_url: https://openai.com/index/samsung-electronics-chatgpt-codex-deployment
source_type: blog-post
title: "Samsung Electronics brings ChatGPT and Codex to employees"
author: OpenAI ("Company" news vertical; single named external quote from Harrison Kim, General Manager of OpenAI Korea — no named Samsung executive is quoted)
date_published: 2026-06-21
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: anecdotal
issue: "#1883"
---

# Samsung Electronics brings ChatGPT and Codex to employees

> A short OpenAI "Company" news post announcing a blanket ChatGPT Enterprise + Codex rollout to all Samsung Electronics employees in Korea and all Device eXperience (DX) division employees worldwide, framed as one of OpenAI's largest enterprise deployments to date, alongside a Korea-market Codex growth metric (~800% since Feb 1, 2026) and context on OpenAI's broader Korean enterprise/education footprint. Contains no Samsung-specific outcome or productivity metric.

## Source Context

- **Type**: blog-post (OpenAI "Company" news post, `openai.com/index/`, ~450 words; auto-discovered via the `openai-news` trusted feed, published June 21, 2026). This is a shorter, plainer template than the "Customer Stories" case-study pages already in the corpus (`blog-openai-bbva-banking-transformation.md`, `blog-openai-endava-frontiers.md`) — it has no "Results at a glance" bullet box and no "Lessons learned" list, and it is filed under OpenAI's "Company" category rather than a customer-story vertical.
- **Author credibility**: House-authored OpenAI announcement. The only direct quotes are from Harrison Kim, General Manager of OpenAI Korea — an OpenAI employee speaking about the deal, not a Samsung executive. No Samsung representative is quoted anywhere in the piece, which is a notable gap compared to BBVA (three named BBVA executives quoted) and Endava (CTO Matthew Cloke quoted at length). Samsung Electronics is a Fortune-Global-500 electronics/semiconductor manufacturer; the deployment scope (all Korea employees, all global DX-division employees) is stated as company policy, not attributed to any named Samsung individual.
- **Scope**: Covers deployment scope and eligibility (who gets access), high-level intended use cases (technical and non-technical work across software development, marketing, product development, manufacturing), ChatGPT Enterprise's named security/governance capabilities, two market-scale metrics (5M+ weekly Codex users globally; ~800% Korea Codex growth since Feb 1, 2026), the OpenAI-Samsung semiconductor supply relationship as prior context, and a roundup of other Korean organizations using OpenAI products. Does NOT cover: any Samsung-specific productivity, time-savings, or adoption-rate metric; a rollout timeline or phased schedule; how many Samsung employees are covered by headcount (only "all" by country/division); pricing or contract terms; or any named Samsung executive perspective.

## Extracted Claims

### Claim 1: ChatGPT Enterprise and Codex are being made available to all Samsung Electronics employees in Korea, and to all employees worldwide within Samsung's Device eXperience (DX) division — described as one of OpenAI's largest enterprise deployments to date
- **Evidence**: Direct statement of deployment scope and OpenAI's own characterization of its scale relative to other enterprise deployments.
- **Confidence**: emerging (a specific, named eligibility rule — all-Korea-employees plus all-DX-worldwide — though no absolute headcount is given, and "one of our largest to date" is OpenAI's own unaudited superlative)
- **Quote**: "Under the agreement, ChatGPT and Codex will be made available to all Samsung Electronics employees in Korea, and all employees worldwide in its Device eXperience (DX) division. This represents one of OpenAI's largest enterprise deployments to date."
- **Our assessment**: This is a scope-by-eligibility-rule deployment (all employees meeting a country/division criterion) rather than a scope-by-headcount deployment. That is a different measurement style from BBVA's explicit "3,000 → 100,000 employees" figure (`blog-openai-bbva-banking-transformation.md` Claim 2) or PayPal's "8,000 developers" (`blog-cursor-paypal-enterprise-adoption.md`). Samsung Electronics' total global workforce is in the hundreds of thousands, and the DX division alone (mobile, TVs, home appliances) is a large fraction of that — so "one of OpenAI's largest" is plausible in absolute terms even without a disclosed number, but the guide should not treat this as a comparable, benchmarkable headcount figure against BBVA's or PayPal's named numbers.

### Claim 2: Samsung Electronics plans to use ChatGPT and Codex across both technical and non-technical functions, explicitly naming software development, marketing, product development, and manufacturing
- **Evidence**: Direct statement naming the four function areas, plus a subheading repeating "R&D and manufacturing to marketing, corporate functions, and other areas of its business."
- **Confidence**: emerging (specific named functional scope from the company itself; no adoption data per function, no rollout sequencing across functions)
- **Quote**: "Samsung Electronics plans to use ChatGPT and Codex for technical and non-technical work, across a broad range of functions, including software development, marketing, product development, and manufacturing, to enhance employee productivity and problem-solving capabilities."
- **Our assessment**: Manufacturing is the notable new vertical here — the corpus's enterprise-adoption sources to date are concentrated in software/fintech/consulting (PayPal, Coinbase, Endava, BBVA) plus one manufacturing-adjacent consumer-goods mention (L'Oréal, named only in passing in `blog-anthropic-building-enterprise-agents.md` Claim 8 with no workflow detail). Samsung is the first source in the corpus naming manufacturing as an explicit target function for a coding-agent product (Codex), though — like the L'Oréal mention — no manufacturing-specific workflow, use case, or outcome is described here either. Treat as evidence that vendors are marketing coding agents into manufacturing contexts, not as evidence of what that looks like in practice.

### Claim 3: Codex is explicitly framed as expanding beyond its original software-development purpose into general non-technical productivity — "Codex started as a tool for software development, but it's increasingly useful for more kinds of work"
- **Evidence**: Direct statement of Codex's positioning, paired with a description of non-technical use: turning ideas into working software, internal tools, websites, and automated workflows.
- **Confidence**: emerging (a specific, quotable repositioning statement from OpenAI; consistent with, but not additional evidence beyond, OpenAI's own prior product-positioning claims)
- **Quote**: "Codex started as a tool for software development, but it's increasingly useful for more kinds of work." ... "employees can use Codex to turn ideas into working software, internal tools, websites, and automated workflows"
- **Our assessment**: This is the same "Codex for everyone" repositioning already documented at length in `blog-openai-codex-knowledge-work.md` (Claim 2: knowledge workers are ~20% of Codex users, growing 3x faster than developers), published June 2, 2026 — nineteen days before this Samsung post. This Samsung announcement functions as a named enterprise-deployment instance of that same repositioning narrative rather than new evidence for it; the guide should treat the two sources together as one vendor narrative (broad usage-data claim + one named large-customer deployment), not as two independent confirmations.

### Claim 4: ChatGPT Enterprise is used at Samsung for knowledge-based tasks (searching/analyzing information, drafting documents, developing ideas, interpreting data), positioned as operating within Samsung's existing security policies and governance framework via named enterprise controls (data protection, user/access management, security controls)
- **Evidence**: Direct statement describing ChatGPT use cases and the named enterprise-grade capabilities that make secure use possible.
- **Confidence**: anecdotal (generic use-case and capability description; no metric, no description of how governance controls were actually configured or audited at Samsung specifically)
- **Quote**: "ChatGPT Enterprise provides enterprise-grade capabilities that enable organizations to use AI securely and effectively, including data protection, user and access management, and security controls. These capabilities allow Samsung Electronics employees to use advanced AI within the company's security policies and governance framework."
- **Our assessment**: This is boilerplate enterprise-governance framing — the same three capability categories (data protection, access management, security controls) are standard ChatGPT Enterprise marketing language and are not described as configured or adapted for Samsung's specific regulatory or IP-protection needs (notable given Samsung's semiconductor and consumer-electronics IP sensitivity). Compare to BBVA's more specific three-pillar "trust, governance, structured learning" framework (`blog-openai-bbva-banking-transformation.md` Claim 3), which at least names a deliberate strategy; this Samsung post gives only generic product-capability language with no strategy description.

### Claim 5: More than 5 million people now use Codex every week for technical and non-technical workflows and roles — the same headline figure OpenAI reported in its June 2, 2026 knowledge-work report
- **Evidence**: A global (not Samsung-specific) usage figure, presented immediately after the Samsung deployment description as supporting context.
- **Confidence**: emerging (self-reported vendor telemetry; not Samsung-specific — this figure describes Codex's entire global user base, and reappears unchanged in wording from an OpenAI report published 19 days earlier)
- **Quote**: "More than 5 million people now use Codex every week for technical and non-technical workflows and roles."
- **Our assessment**: This is not a Samsung-attributable metric — it is OpenAI's global Codex weekly-active-user count, identical to the headline figure in `blog-openai-codex-knowledge-work.md` Claim 1 ("Codex now has more than 5 million weekly active users, up more than 6x since the launch of the desktop app in February"), minus the "6x since February" growth qualifier. The reuse of the same "5 million" figure without an updated multiplier across a 19-day gap is a mildly interesting data point in its own right: it suggests either (a) OpenAI's public messaging has not refreshed this number since the June 2 report, or (b) weekly-active-user growth has plateaued near 5M in the interim. The guide should not attribute this 5M figure to Samsung's deployment specifically — it is placed in the article as supporting scale context, not as a Samsung outcome.

### Claim 6: Codex weekly active users in Korea have grown nearly 800% since February 1, 2026
- **Evidence**: A Korea-market (not Samsung-specific) growth figure, presented in the same paragraph as the global 5M figure.
- **Confidence**: emerging (specific named percentage and start date; single self-reported figure with no baseline volume disclosed, no methodology, and — like Claim 5 — not attributable specifically to Samsung's deployment, since the Korea-wide figure also reflects any other Korean-company or individual adoption)
- **Quote**: "Codex weekly active users in Korea have grown nearly 800% since February 1, 2026."
- **Our assessment**: This is the article's single most concrete quantitative claim, but it measures the entire Korean market's Codex adoption, not Samsung's rollout specifically (the Samsung deployment itself is described in the present/future tense — "is deploying," "plans to use" — suggesting this growth figure substantially predates or is independent of the Samsung-wide rollout being announced). A large percentage on an undisclosed base (as with `blog-openai-codex-knowledge-work.md` Claim 4's "+110% week over week" data-analysis growth) is directionally suggestive of a hot regional market but not a rigorous adoption metric. Useful only as color establishing competitive intensity in the Korean market, not as evidence of Samsung-specific outcomes.

### Claim 7: Harrison Kim (General Manager, OpenAI Korea) frames the Samsung deployment's significance as Samsung adopting AI "not as a tool limited to certain teams or functions, but as a core platform" for how employees work and innovate company-wide
- **Evidence**: Direct attributed quote from the only named individual in the article.
- **Confidence**: anecdotal (a single OpenAI (not Samsung) executive's characterization of the deal's significance; not a Samsung-sourced statement)
- **Quote**: "This historic deployment for OpenAI is particularly significant because Samsung Electronics, a global leader in technology and manufacturing, is embracing AI not as a tool limited to certain teams or functions, but as a core platform for improving how employees around the world work and innovate."
- **Our assessment**: Notably, this framing quote — the article's only quoted perspective — comes from the vendor's own regional executive, not from any Samsung representative. This is a different evidentiary posture than every other enterprise-adoption case study in the corpus (BBVA, Endava, PayPal, Coinbase, NAB), all of which quote the customer's own executives directly. The guide should flag this article as OpenAI narrating a deal on Samsung's behalf, with no independent Samsung voice corroborating the "core platform, not siloed to certain teams" characterization.

### Claim 8: The Samsung ChatGPT/Codex deployment extends an existing OpenAI-Samsung relationship that began with Samsung supplying advanced memory semiconductors for OpenAI's AI infrastructure — the partnership is now expanding from infrastructure supply into workforce/software adoption
- **Evidence**: Direct statement describing the prior AI-infrastructure relationship and its expansion into workforce transformation.
- **Confidence**: emerging (a specific, named prior commercial relationship — semiconductor supply — is stated as fact, consistent with independently reported memory-chip market context; the "expanding into workforce transformation" framing is OpenAI's own characterization of the relationship's trajectory)
- **Quote**: "OpenAI and Samsung Electronics previously began collaborating in the field of global AI infrastructure. Samsung Electronics is working with OpenAI to supply advanced memory semiconductors required for next-generation AI infrastructure. With Samsung Electronics' adoption of ChatGPT Enterprise, the relationship between the two companies is expanding beyond AI infrastructure to encompass workforce transformation and company-wide AI adoption."
- **Our assessment**: This corroborates the memory-chip supply-side context already in the corpus via `blog-simonwillison-memory-shortage-repricing.md`, which names Samsung (alongside SK Hynix and Micron) as one of only three major memory manufacturers amid an AI-driven memory shortage. Read together, the two sources describe a single relationship from opposite ends: Willison's note covers the supply-chain/pricing pressure Samsung's memory business faces from AI infrastructure demand; this Samsung deployment post covers OpenAI positioning that same commercial relationship as now extending into software/workforce adoption. The Samsung post gives no detail on deal structure, exclusivity, or whether the software deployment is commercially linked (e.g., bundled pricing) to the semiconductor supply agreement — the "expanding beyond" language is a relationship-narrative claim, not a disclosed contractual link.

### Claim 9: Other major Korean organizations are also using OpenAI's enterprise products — named examples include Seoul National University (ChatGPT Edu to all 47,000 community members), Kakao (ChatGPT integrated into KakaoTalk group chats), and a list of twelve additional companies (LG Electronics, LG Uplus, LG CNS, GS E&C, Samsung SDS, TVING, Krafton, Toss, MUSINSA, Korea Zinc, Nexen Tire, HanaTour) using ChatGPT Enterprise, OpenAI APIs, and/or Codex
- **Evidence**: Direct roundup paragraph naming each organization and, for two of them, a specific scale detail.
- **Confidence**: anecdotal (a named-but-undetailed roundup list; no per-company adoption metric beyond the two called out — Seoul National University's 47,000-member figure and the Kakao product-integration description — and no detail on depth or scale of use for the other eleven companies)
- **Quote**: "Also in Korea, Seoul National University recently began providing ChatGPT Edu to all 47,000 members of its community, including students, faculty, and staff, as part of its transition toward becoming an AI-native campus." ... "Companies across a wide range of industries in Korea, including LG Electronics, LG Uplus, LG CNS, GS E&C, Samsung SDS, TVING, Krafton, Toss, MUSINSA, Korea Zinc, Nexen Tire, and HanaTour are also using ChatGPT Enterprise, OpenAI APIs, and Codex."
- **Our assessment**: This roundup functions as competitive-intensity color for the Korea-market growth figure (Claim 6) — a long list of unrelated Korean companies and institutions (electronics, construction, retail, mining, travel, gaming, fintech) suggests broad, cross-sector enterprise AI adoption in Korea rather than adoption concentrated in tech-native firms, but the list gives zero detail on any individual company's deployment scope or outcome. This is the corpus's first source naming a dozen-plus organizations in a single regional adoption roundup; treat as evidence of regional market breadth claims by the vendor, not as twelve independent case studies.

## Concrete Artifacts

```
Source: OpenAI, "Samsung Electronics brings ChatGPT and Codex to employees,"
https://openai.com/index/samsung-electronics-chatgpt-codex-deployment
(published June 21, 2026)

Subheading bullets (verbatim, as they appear at the top of the article):
- ChatGPT Enterprise and Codex available to all Samsung Electronics employees
  in Korea and all Device eXperience (DX) employees worldwide
- Samsung's global deployment is one of OpenAI's largest enterprise
  launches ever
- Samsung Electronics to use ChatGPT and Codex across its operations, from
  R&D and manufacturing to marketing, corporate functions, and other areas
  of its business

Headline metrics (article body):
  Codex weekly active users (global):  5,000,000+
  Codex weekly active user growth, Korea, since Feb 1, 2026:  ~800%
  Seoul National University ChatGPT Edu community members:  47,000

Named Korean organizations using OpenAI products, beyond Samsung
(article roundup paragraph):
  Seoul National University (ChatGPT Edu, campus-wide)
  Kakao (ChatGPT embedded in KakaoTalk group chats)
  LG Electronics, LG Uplus, LG CNS, GS E&C, Samsung SDS, TVING, Krafton,
  Toss, MUSINSA, Korea Zinc, Nexen Tire, HanaTour
  (ChatGPT Enterprise, OpenAI APIs, and/or Codex — no per-company detail)
```

## Cross-References

- **Corroborates**:
  - `blog-openai-codex-knowledge-work.md` Claim 2 ("Codex started as a tool for software development, but it's increasingly useful for more kinds of work" / knowledge workers now ~20% of Codex users, growing 3x faster than developers): Claim 3 here is OpenAI applying the identical repositioning narrative to a single named enterprise customer. Read together as one vendor narrative rather than independent confirmations — see Claim 3's assessment.
  - `blog-openai-bbva-banking-transformation.md` and `blog-openai-endava-frontiers.md`: all three are OpenAI-authored enterprise-deployment announcements citing named enterprise-grade governance capabilities (data protection, access management, security controls) as the mechanism that makes regulated/large-scale adoption possible. Samsung's version (Claim 4) is the thinnest of the three — no named strategy framework (contrast BBVA's "trust, governance, structured learning" three-pillar strategy) and no named champion/enablement program (contrast BBVA's champions/"wizards" network or Endava's DavaFlow integration).
  - `blog-simonwillison-memory-shortage-repricing.md` (Samsung, SK Hynix, and Micron named as the oligopoly of major memory manufacturers amid an AI-driven memory shortage): corroborates and extends the semiconductor-supply context in Claim 8 — read together, one source covers the supply-side pricing pressure on Samsung's memory business, the other covers OpenAI's framing of the same commercial relationship extending into software adoption.

- **Contradicts**: None filed. No existing corpus source makes a claim that materially opposes anything in this article, and the article does not disagree with itself. Per MINER.md §4a this is not a contradiction-worthy case — see Extraction Notes for the one candidate tension considered (the reused, non-updated "5 million" figure) and why it was not treated as a contradiction.

- **Extends**:
  - `blog-openai-codex-knowledge-work.md`: extends that report's aggregate "Codex is for everyone" usage-segmentation claims with a single, large, named enterprise deployment instance — but without any Samsung-specific usage-segmentation data of its own.
  - `blog-anthropic-building-enterprise-agents.md` (L'Oréal named as a manufacturing-adjacent, consumer-goods deployment example, Claim 8): extends the corpus's very thin manufacturing-vertical coverage with a second named manufacturer (Samsung Electronics) explicitly targeting AI at "R&D and manufacturing," though — as with L'Oréal — no manufacturing-specific workflow or outcome detail is given by either source.
  - `blog-openai-bbva-banking-transformation.md`: extends the corpus's set of OpenAI-authored enterprise-deployment announcements with a non-financial-services, manufacturing/consumer-electronics vertical, and with a materially thinner evidentiary posture (no named customer-side executive quote, no per-function or per-workflow outcome metric, no adoption-strategy framework) than BBVA's twelve-claim case study.

- **Novel**:
  - **Vendor-only quoted perspective**: this is the first enterprise-deployment source in the corpus where the only quoted individual works for the AI vendor (OpenAI's Harrison Kim), not the customer (Claim 7). Every other enterprise case study in the corpus (BBVA, Endava, PayPal, Coinbase, NAB) quotes at least one named customer executive.
  - **Eligibility-rule deployment scope instead of headcount**: Samsung's deployment is announced by eligibility criterion (all Korea employees + all global DX-division employees) rather than by a disclosed headcount figure, a measurement style not previously seen in the corpus's enterprise-deployment sources (Claim 1).
  - **Manufacturing named as an explicit target function for a coding-agent product** (Claim 2): the first source in the corpus where a coding-agent vendor explicitly names manufacturing as a target use-case vertical, alongside software development, marketing, and product development.
  - **Multi-organization regional adoption roundup** (Claim 9): the first source in the corpus naming a dozen-plus unrelated organizations in a single regional "also adopting" list, useful as color for regional competitive-intensity claims but not as individual case-study evidence.

## Guide Impact

- **Chapter 05 (Team Adoption)**: If the guide adds a section on enterprise-deployment case studies, Samsung should be included as a data point specifically illustrating the *weakest* end of the evidentiary spectrum in that section — a vendor announcement with a named deployment scope but zero customer-side quotes, zero outcome/productivity metrics, and generic (not company-specific) governance-capability language. Explicitly contrast against BBVA's twelve-claim case study (`blog-openai-bbva-banking-transformation.md`) so readers calibrate confidence correctly: not every "enterprise deployment" announcement carries the same evidentiary weight.
- **Chapter 05 (Team Adoption), manufacturing-vertical coverage**: If the guide begins discussing AI adoption in manufacturing/hardware contexts (currently only a passing L'Oréal mention exists in the corpus), cite Samsung's explicit "R&D and manufacturing" targeting (Claim 2) as a second, larger-scale example — but flag clearly that neither source describes an actual manufacturing workflow or outcome; both are only reach/scope announcements.
- **Any chapter citing global Codex/ChatGPT scale figures**: Do not double-count the "5 million weekly Codex users" figure (Claim 5) as fresh evidence of Samsung-driven growth — it is the same unchanged global figure OpenAI published on June 2, 2026 in `blog-openai-codex-knowledge-work.md`, reused verbatim 19 days later without an updated growth multiplier. Cite the two sources together, noting the figure's non-refresh, if the guide discusses how frequently vendors update public usage statistics.
- **Chapter 05 (Team Adoption), regional/competitive framing**: The Korea adoption roundup (Claim 9) is useful only as color establishing that generative-AI adoption in Korea is broad and cross-sector (electronics, construction, retail, mining, travel, gaming, fintech, higher education) — not as case-study evidence for any single company on the list besides Samsung.

## Extraction Notes

- The live URL (`https://openai.com/index/samsung-electronics-chatgpt-codex-deployment`) returned HTTP 403 to both the WebFetch tool and a direct `curl` with a browser user-agent (client-side loading-shell response), consistent with prior OpenAI-domain extraction difficulties noted in `blog-openai-bbva-banking-transformation.md` and `blog-openai-endava-frontiers.md`.
- Initial WebFetch attempts against an `r.jina.ai` proxy returned inconsistent, mutually contradictory text across repeated fetches of the same URL (different "exact quotes," different named-company lists, one response fabricating a stitched-together sentence combining fragments from two earlier fetches with an invented opening clause). This is a materially different failure mode than the clean, stable jina-proxy extractions used successfully in `blog-openai-endava-frontiers.md` — treat any resemblance between this note's draft quotes and those proxy outputs as coincidental; none of the proxy output was used in the final note.
- The article was ultimately retrieved via a Wayback Machine snapshot (`web.archive.org/web/20260622092048/https://openai.com/index/samsung-electronics-chatgpt-codex-deployment/`, crawled June 22, 2026, one day after publication), fetched with `curl` directly (not the WebFetch tool, which is blocked from fetching `web.archive.org` in this environment — same workaround documented in `blog-openai-codex-knowledge-work.md` and `blog-openai-bbva-banking-transformation.md`). The archived HTML was parsed with a local Python `HTMLParser`-based script stripping `script`/`style`/`nav`/`header`/`footer` tags. All quotes in this note were copied character-for-character from that extracted text, cross-checked against a second, independently-timestamped snapshot from the same CDX listing (`20260623175639`) for the headline figures — both snapshots agree.
- One candidate tension was considered and not filed as a contradiction (per MINER.md §4a): the article's "5 million weekly Codex users" figure (Claim 5) is identical, without an updated growth multiplier, to the same figure published 19 days earlier in `blog-openai-codex-knowledge-work.md`. This is a data-freshness observation about OpenAI's public communications, not a disagreement between two sources about a fact — no contradiction issue was filed.
- No sub-pages were followed. The archived page's "Keep reading" footer links to three unrelated OpenAI company posts (an Ona acquisition announcement, an Oracle cloud-commitment post, an SEC draft-S-1 submission note) — none are substantively linked follow-on material for this deployment announcement.
- The article is short (~450 words) and every sentence in its body is reflected in one of the nine claims above; this is not a case of shallow reading, but the source itself is thin — no Samsung-specific outcome metric, no customer-side quote, and no rollout timeline exist to extract.
