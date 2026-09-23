---
source_url: https://www.thoughtworks.com/insights/articles/the-quantum-countdown
source_type: blog-post
title: "The quantum countdown: Why post-quantum cryptography is a strategic imperative"
author: Rav Hayer (Managing Director UK and Ireland and Head of BFSI Europe, Thoughtworks)
date_published: 2026-09-22
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: emerging
issue: "#3635"
---

# The Quantum Countdown: Why Post-Quantum Cryptography Is a Strategic Imperative

> A Thoughtworks leadership article arguing post-quantum cryptography (PQC)
> migration is now a board-level compliance mandate, not a future IT concern
> — built on well-established security-literature material (Mosca's
> theorem, HNDL/TNFL threat models, DORA/NIS2/NCSC regulatory citations) plus
> one novel, entirely unsubstantiated claim that autonomous agentic systems
> and machine-to-machine interaction specifically escalate PQC risk.

## Source Context

- **Type**: blog-post (Thoughtworks Insights "Articles," Security/Emerging
  tech categories; published September 22, 2026; auto-discovered via the
  trusted feed `thoughtworks`). A ~1,400-word strategic/compliance essay
  structured in four numbered sections (collapse of classical encryption,
  technical debt and operational friction, regulatory mandates, a four-step
  roadmap) plus an executive summary and conclusion. Per Miner step 1, one
  substantive linked page was also followed: a companion Thoughtworks blog
  post, "Three steps to post-quantum cryptography" (by Gitanjali
  Venkatraman, published June 12, 2025,
  https://www.thoughtworks.com/insights/blog/emerging-tech/three-steps-to-post-quantum-cryptography),
  linked from this article's "Related content" rail. That companion piece is
  used here only for corroboration/concrete-artifact context (see Concrete
  Artifacts and Cross-References); its claims are not separately numbered as
  claims of *this* source note since it is a distinct article by a different
  author, not part of the primary source's own text.
- **Author credibility**: Rav Hayer identifies himself in the closing
  attribution as "Managing Director UK and Ireland and Head of BFSI Europe,
  Thoughtworks" — an executive, not a working cryptographer or security
  researcher. Hayer is a repeat corpus author: co-authored
  `blog-thoughtworks-singh-hayer-stranger-core.md`,
  `blog-thoughtworks-shah-hayer-commodities-trading-agentic-frontier.md`, and
  sole-authored `blog-thoughtworks-hayer-agentic-horizon.md` — all rated
  `emerging` or `anecdotal` in this corpus because they are executive
  strategic framing pieces that name technical/architectural requirements
  without developing the underlying mechanism. This article follows the same
  pattern: well-cited regulatory and mathematical background (Mosca's
  theorem, DORA/NIS2 text) sits alongside one headline technical-risk claim
  about agentic systems that has no citation, example, or case study behind
  it anywhere in the piece.
- **Scope**: Covers the HNDL/TNFL threat framing, Mosca's theorem as a
  timeline-risk formula, PQC migration technical debt (key size/latency,
  supply chain), EU/UK regulatory mandates (DORA, NIS2, NCSC), procurement
  pressure (CBOM), and a four-phase crypto-agility roadmap. Does NOT cover:
  any specific agentic system, deployment, or incident where "automated
  execution" actually caused a PQC-related failure; any named PQC algorithm
  implementation detail beyond passing mentions of ML-KEM/ML-DSA/ECDH; or any
  quantitative sourcing for the "87%/7%" adoption statistic (no survey name,
  publisher, or link is given in the article body).

## Extracted Claims

### Claim 1: Threat actors are conducting Harvest Now, Decrypt Later (HNDL) attacks today — intercepting and storing encrypted corporate data now so it can be decrypted once quantum computers mature
- **Evidence**: Stated as established fact in the executive summary, consistent with widely cited security-industry framing (also corroborated by the companion Thoughtworks piece, see Cross-References).
- **Confidence**: settled (HNDL is a well-established threat model in security literature, not a novel claim of this article)
- **Quote**: "Through Harvest Now, Decrypt Later (HNDL), threat actors are intercepting and storing encrypted corporate data today to decrypt retroactively the moment quantum capabilities mature."
- **Our assessment**: This is background, not a novel contribution — HNDL is a standard framing repeated across the security industry (see the companion piece's near-identical framing in Cross-References). Useful as a citable, concise restatement, not as new evidence.

### Claim 2: Trust Now, Forge Later (TNFL) is a second, distinct quantum threat vector — the risk that digital signatures could be forged retroactively, undermining legal agreements, API authentication, and software update integrity
- **Evidence**: Stated as established fact in the executive summary; no case study or example of a TNFL attack is given.
- **Confidence**: settled (TNFL/signature-forgery risk is a recognized companion threat model to HNDL in PQC literature, distinct from but parallel to Claim 1)
- **Quote**: "Trust Now, Forge Later (TNFL) threatens digital identity by undermining signature validation across legal agreements, API authentication and software updates."
- **Our assessment**: "API authentication" and "software updates" are the two elements of this claim most directly relevant to AI-native engineering practice (CI/CD signing, agent-to-service auth) — but the article never returns to elaborate on either beyond this one sentence.

### Claim 3: The rise of autonomous agentic systems and machine-to-machine interaction specifically escalates the risk of PQC failure, due to automated execution and expanded attack surfaces
- **Evidence**: A single unsupported assertion in the executive summary. No example, deployment, incident, or citation is given anywhere else in the article — sections 1 through 4 (encryption collapse, technical debt, regulatory mandates, the four-step roadmap) never mention agents, automation, or machine-to-machine interaction again.
- **Confidence**: anecdotal (this is the specific claim the Prospector's triage flagged as the novel contribution and asked to verify; extraction confirms it has zero supporting evidence in the source itself)
- **Quote**: "The rise of autonomous Agentic systems and machine-to-machine interactions further escalates the risk of PQC failure due to automated execution and expanded attack surfaces."
- **Our assessment**: This is asserted, not argued. The article gives no mechanism for *how* agentic execution specifically escalates PQC risk beyond what any high-volume, automated (non-agentic) machine-to-machine system would already face — nothing here is unique to LLM-driven agents versus, say, existing high-frequency-trading or IoT machine-to-machine traffic. This is the same pattern seen in this author's other corpus entry, `blog-thoughtworks-hayer-agentic-horizon.md` Claim 6, which names "cryptographic identity tokenization" as a requirement for agentic platforms without developing the mechanism (see Cross-References → Extends). The guide should not cite this claim as evidence that agentic systems create a *distinct* PQC risk category without flagging that no such evidence currently exists in the corpus.

### Claim 4: Mosca's Theorem formalizes when quantum risk becomes unacceptable — if data shelf life (X) plus migration time (Y) is greater than or equal to the time until a cryptographically relevant quantum computer exists (Z), the data is already compromised
- **Evidence**: Presented as an established security-industry risk-timing principle (attributed by name to Michele Mosca, though not directly cited to a paper); the article supplies illustrative figures (10-30 year data shelf life, five-year migration time).
- **Confidence**: settled (Mosca's Theorem is a widely cited, established framework in PQC risk literature, also independently corroborated by the companion piece — see Cross-References)
- **Quote**: "The strategic reality: If your organization's data must remain secure for 10 to 30 years ($X$) and your enterprise migration takes five years ($Y$), any system where $X + Y ≥ Z$ means your data is already compromised today."
- **Our assessment**: This is the most rigorously grounded claim in the article — it's a named, citable formula rather than a vague warning, and gives a concrete way to reason about urgency (organizations with long-lived sensitive data and slow migration capacity are already exposed, regardless of when quantum computers actually arrive). Directly reusable in guide text as a risk-framing tool independent of the article's other, weaker claims.

### Claim 5: Industry surveys show 87% of organizations are planning or piloting PQC, but only 7% have deployed quantum-safe cryptography across most of their certificate estate
- **Evidence**: Cited as "recent industry surveys" with no named survey, publisher, sample size, or link.
- **Confidence**: anecdotal (specific numbers given, but entirely unsourced within the article — no way to verify methodology or recency)
- **Quote**: "Recent industry surveys show that while 87% of organizations are planning or piloting PQC, only 7% have deployed quantum-safe cryptography across most of their certificate estate."
- **Our assessment**: The 87%/7% gap is a strong, quotable "planning-versus-doing" statistic, but its unsourced presentation means the guide should treat it as illustrative context rather than a citable data point on its own — verify against a named survey (e.g., a vendor or analyst PQC-adoption report) before repeating the precise figures.

### Claim 6: PQC migration creates real operational friction because ML-KEM/ML-DSA lattice-based keys are orders of magnitude larger than legacy ECC keys, causing network packet fragmentation, TLS handshake latency, and memory strain
- **Evidence**: Named specific algorithm families (ML-KEM, ML-DSA) and named specific failure symptoms (packet fragmentation, TLS handshake latency, memory strain).
- **Confidence**: settled (key-size growth from lattice-based PQC schemes versus ECC is a well-documented, measurable property of the NIST-standardized algorithms, not a speculative claim)
- **Quote**: "PQC algorithms require significantly larger key sizes and signature payloads. Standardized lattice-based keys (such as ML-KEM and ML-DSA, which are lattice-based, quantum-resistant algorithms) are orders of magnitude larger than legacy ECC keys, triggering network packet fragmentation, TLS handshake latency and memory strain across database schemas."
- **Our assessment**: This is the one claim in the article with a concrete, independently corroborated real-world instance already in this corpus — `blog-simonwillison-bun-webview-json-api.md` Claim 11 documents exactly this failure mode (a TLS-intercepting sandbox proxy unable to parse Chrome's TLS 1.3 ClientHello carrying a ~1.7 KB post-quantum X25519MLKEM768 key share, causing `ERR_CONNECTION_RESET`). That prior note treats it as a narrow, environment-specific sandbox quirk; this article frames the same underlying key-size phenomenon as a general enterprise migration risk. Together they give the guide both the abstract claim (this article) and a concrete, reproduced instance (the Willison note) — see Cross-References.

### Claim 7: Enterprise supply chains introduce PQC exposure that organizations cannot fully audit, because they lack complete visibility into vendor codebases and partner integrations
- **Evidence**: General assertion; no named vendor, incident, or audit example.
- **Confidence**: anecdotal (plausible and consistent with general supply-chain security literature, but no PQC-specific example is given)
- **Quote**: "Enterprise perimeters are inherently vulnerable to third-party dependencies. Without complete visibility into vendor codebases and partner integrations, third-party software supply chains introduce backdoor quantum vulnerabilities into production environments."
- **Our assessment**: "Backdoor quantum vulnerabilities" is evocative language but the claim reduces to "you don't control your vendors' crypto," a generic supply-chain risk restated with a PQC label rather than a PQC-specific finding.

### Claim 8: EU regulation has converted PQC readiness from guidance into enforceable law — NIS2 imposes fines up to 2% of global annual turnover (or €10M) plus direct personal liability for board members, while DORA enforces quantum readiness through supervisory expectations
- **Evidence**: Named specific regulations (DORA, NIS2) and a specific financial penalty figure.
- **Confidence**: settled (NIS2 and DORA are real, named EU regulations with the described scope; the specific 2%/€10M figure matches NIS2's general administrative-fine structure for essential entities)
- **Quote**: "NIS2 introduces explicit administrative fines reaching up to 2% of global annual turnover (or €10M) for essential entities along with direct personal liability for board members, while DORA enforces quantum readiness and crypto-agility through supervisory expectations and remediation requirements."
- **Our assessment**: This is the strongest "why should a board act now" evidence in the article — a named, checkable regulatory citation rather than a vague warning. Worth flagging that DORA and NIS2 mandate crypto-agility and ICT risk management generally; the article does not quote regulatory text that names "post-quantum cryptography" specifically, so the PQC-specific compliance obligation is the author's interpretation of broader crypto-agility requirements, not a direct regulatory quote.

### Claim 9: The UK National Cyber Security Centre (NCSC) mandates cryptographic discovery and inventory planning with strict migration horizons for critical national infrastructure and commercial enterprises
- **Evidence**: General assertion; no specific NCSC document, timeline, or milestone date is quoted.
- **Confidence**: emerging (NCSC has published PQC migration guidance, consistent with the general claim, but the article gives no specific timeline or citation to verify "strict migration horizons")
- **Quote**: "The UK National Cyber Security Centre mandates complete cryptographic discovery and inventory planning, setting strict migration horizons for critical national infrastructure and commercial enterprises."
- **Our assessment**: Directionally consistent with public NCSC PQC guidance, but too vague to extract a specific timeline or requirement from this article alone — would need the primary NCSC source to cite a specific date or milestone.

### Claim 10: Institutional buyers increasingly require a verified Cryptographic Bill of Materials (CBOM) during procurement, and organizations without a documented PQC roadmap face immediate disqualification from enterprise RFPs
- **Evidence**: General assertion; no named buyer, RFP, or procurement policy example.
- **Confidence**: anecdotal (plausible market pressure, but no concrete example of an actual disqualification is cited)
- **Quote**: "Institutional buyers are increasingly demanding a verified Cryptographic Bill of Materials (CBOM) during procurement. Organizations lacking a documented PQC roadmap face immediate disqualification from enterprise RFPs and vendor ecosystems."
- **Our assessment**: This is a specific, actionable claim for vendor-facing engineering organizations (having a CBOM matters for sales, not just security) but is asserted rather than evidenced — no named enterprise buyer or RFP requirement is quoted.

### Claim 11: PQC migration should be executed as a four-phase program — discover and map (build a CBOM), prioritize by data longevity, re-architect for crypto-agility via abstraction/gateway layers, and execute hybrid deployments pairing classical and PQC algorithms
- **Evidence**: Presented as the article's own recommended framework, not attributed to an external standard; each phase is given a one-sentence description (see Concrete Artifacts for full text).
- **Confidence**: emerging (a reasonable, generic migration-planning structure consistent with standard crypto-agility guidance, but presented without a track record, case study, or named adopter)
- **Quote**: "PQC migration must be executed as an enterprise-wide modernization program across four sequential phases"
- **Our assessment**: The most concrete, reusable artifact in the article for engineering teams — the "re-architect for crypto-agility" phase specifically calls out abstracting cryptographic logic behind gateway layers/wrappers so algorithms can be swapped via configuration, which is a directly applicable architectural pattern independent of whether the reader buys the article's regulatory-urgency framing.

## Concrete Artifacts

### Mosca's Theorem formula (as rendered in the article, section 1)
```
Source: thoughtworks.com/insights/articles/the-quantum-countdown, section
"1. The collapse of classical encryption"

[ X: Data Shelf Life ] + [ Y: Migration Time ] >= Z (Time to Quantum)

X (Shelf Life): The duration for which data must remain confidential (for
  example, patient records, core financial ledgers, trade secrets).
Y (Migration Time): The operational timeframe required to re-architect
  systems, eliminate cryptographic debt and deploy PQC standards.
Z (Time to CRQC): The estimated timeframe until a cryptographically
  relevant quantum computer becomes operational.
```

### Four-phase crypto-agility roadmap (verbatim, section 4)
```
Source: thoughtworks.com/insights/articles/the-quantum-countdown, section
"4. A four-step roadmap for crypto-agility"

1. Discover and map (CBOM): Deploy automated scanning across repositories,
   network traffic and certificate stores to build a dynamic Cryptographic
   Bill of Materials.

2. Prioritize by data longevity: Target high-value data with long
   retention mandates and internet-facing endpoints first (Tier 1). Align
   lower-priority internal systems with routine technology refresh cycles.

3. Re-architect for crypto-agility: Build crypto-agility by abstracting
   cryptographic logic away from application code via gateway layers and
   wrappers. This ensures algorithms can be swapped via configuration as
   standards evolve without breaking downstream systems.

4. Execute hybrid deployments: Deploy hybrid cryptographic schemes pairing
   classical algorithms (for example, ECDH) in parallel with PQC algorithms
   (for example, ML-KEM). This preserves current compliance while
   validating real-world performance under post-quantum parameters.
```

### Board-level due-diligence questions (verbatim, conclusion)
```
Source: thoughtworks.com/insights/articles/the-quantum-countdown, conclusion

Data exposure: Which of our core data assets must remain confidential for
  the next 10 to 30 years, and are they crossing public networks today?

Supply chain risk: Do our critical software and SaaS vendors provide a
  validated Cryptographic Bill of Materials (CBOM)?

Regulatory readiness: Does our ICT risk strategy satisfy mandatory DORA
  and NCSC requirements to protect board directors from personal
  liability?
```

### Closing attribution quote
```
Source: thoughtworks.com/insights/articles/the-quantum-countdown, conclusion

"The quantum threat is not a future event to monitor. It is an active
vulnerability today. Securing the enterprise for the quantum era demands
immediate, crypto-agile modernization."
— Rav Hayer, Managing Director UK and Ireland and Head of BFSI Europe,
  Thoughtworks
```

### Companion piece context: three-step migration plan and NIST algorithm list (for corroboration only — different author/URL, not claims of the primary source)
```
Source: "Three steps to post-quantum cryptography" by Gitanjali
Venkatraman, thoughtworks.com/insights/blog/emerging-tech/three-steps-to-post-quantum-cryptography
(published June 12, 2025), followed as a substantive linked page per
Miner step 1.

NIST-approved PQC schemes named: CRYSTALS-Kyber, CRYSTALS-Dilithium,
Sphincs+, Falcon, HQC.

Three-step plan: (1) prepare a cryptographic inventory, (2) assess the
impact and cost of (not) moving to PQC, (3) build resilience
(cryptoagility, layered defenses, recovery strategy, scaling resilience).

Quote: "PQC migration is a two CEO problem, because it takes that long."
— Ben Packman, PQShield (as quoted in Venkatraman's piece)

Quote (Mosca's theorem, independently restated in this 2025 companion
piece): "If X + Y approaches Z, it is time to act!"
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-bun-webview-json-api.md` (Claim 11): That note
    documents a concrete, reproduced instance of exactly the failure mode
    Claim 6 of this source describes in the abstract — larger post-quantum
    key sizes (there, a ~1.7 KB X25519MLKEM768 TLS 1.3 ClientHello) breaking
    network/TLS infrastructure that wasn't built to expect them. The
    Willison note frames it as a narrow sandbox-proxy quirk; this article
    frames the same underlying phenomenon (PQC key-size growth) as a general
    enterprise migration risk. Read together, they give the guide both the
    abstract claim and a concrete reproduction.
  - The companion Thoughtworks piece ("Three steps to post-quantum
    cryptography," see Concrete Artifacts) independently restates both the
    HNDL threat model (Claim 1) and Mosca's Theorem (Claim 4) — since both
    are Thoughtworks-published pieces a year apart from different authors
    making the same claims, this is weak corroboration (same publisher, not
    fully independent sources) but does show consistency in how the firm
    frames PQC risk across authors and time.

- **Contradicts**: None identified against existing corpus source notes. No
  prior note makes a claim about PQC adoption strategy, regulatory
  compliance timelines, or enterprise migration roadmaps that this source
  disagrees with — this is a novel topic area for the corpus (see Novel,
  below). No contradiction issue filed per MINER.md §4a.

- **Extends**: `blog-thoughtworks-hayer-agentic-horizon.md` (Claim 6): That
  note, by the same author, names "cryptographic identity tokenization" as
  a requirement for production-grade agentic platforms without developing
  the mechanism beyond a single rhetorical question — rated `emerging`
  there specifically because the claim is a bare due-diligence question
  with "no named cryptographic standard, protocol, or vendor." This
  source's Claim 3 (agentic systems escalate PQC risk) repeats the same
  pattern: Hayer naming a cryptography-plus-agents intersection as
  strategically important without ever supplying a mechanism, example, or
  citation. Two separate pieces by the same author, roughly three weeks
  apart, both gesture at "agents create new cryptographic risk" without
  substantiating it — this strengthens the case that it reflects the
  author's/Thoughtworks' current strategic messaging rather than a
  documented technical finding, and the guide should treat it accordingly
  if citing either piece on this topic.

- **Novel**:
  - **PQC as a named, citable board-compliance topic**: No existing corpus
    note documents post-quantum cryptography migration as a regulatory/
    governance topic (DORA, NIS2, NCSC, CBOM procurement pressure) — this is
    the first source in the corpus to address PQC from an adoption-strategy
    and compliance angle rather than an LLM-capability-to-break-cryptography
    angle (contrast with `blog-simonwillison-cryptographic-weaknesses-mythos.md`,
    which covers Claude Mythos finding an attack against the HAWK
    post-quantum signature scheme — a capability-research angle, not an
    enterprise-adoption angle; the two sources do not overlap in claims
    despite both concerning post-quantum cryptography).
  - **Mosca's Theorem as a reusable risk-framing formula** (Claim 4): first
    explicit statement of this formula in the corpus.
  - **The four-phase crypto-agility roadmap and CBOM concept** (Claim 11,
    Claim 10): first documentation of a structured PQC migration process and
    the "Cryptographic Bill of Materials" artifact in the corpus.
  - **The unsubstantiated "agentic systems escalate PQC risk" claim itself**
    (Claim 3) is novel to the corpus as an assertion, but — per the
    Prospector's triage question — extraction found no supporting evidence
    for it anywhere in the source; it should be treated as an open question
    flagged by a repeat-author's strategic messaging, not as a documented
    finding.

## Guide Impact

- **Chapter 06 (Security Threat Model)**: The guide currently has no PQC
  content. If Ch06 adds a PQC subsection, it should be built primarily on
  the well-sourced claims here (Claim 4's Mosca's Theorem framing, Claim 8's
  DORA/NIS2 citations, Claim 6's key-size/TLS friction claim paired with the
  concrete Willison-note reproduction) rather than on Claim 3. Claim 3
  ("agentic systems escalate PQC risk due to automated execution and
  expanded attack surfaces") should NOT be repeated in Ch06 as an
  established risk finding — it is an unsubstantiated assertion, and this
  extraction found the same author making a structurally identical
  unsubstantiated crypto-plus-agents claim in a separate piece three weeks
  earlier (`blog-thoughtworks-hayer-agentic-horizon.md` Claim 6). If Ch06
  wants to make a claim about agentic systems and cryptographic risk, the
  corpus's actual evidence for that intersection is
  `blog-simonwillison-cryptographic-weaknesses-mythos.md` (agentic systems
  being used to *attack* post-quantum cryptography, i.e., HAWK) — a
  different and better-evidenced risk than this article's vague "automated
  execution" framing.
- **Chapter 05 (Team Adoption)**: The four-phase crypto-agility roadmap
  (Claim 11) and the CBOM/RFP-disqualification claim (Claim 10) are
  reusable as an organizational-adoption checklist item — specifically the
  "re-architect for crypto-agility" phase's architectural guidance
  (abstract cryptographic logic behind gateway layers/wrappers so
  algorithms can be swapped via configuration) is a concrete,
  implementation-relevant pattern independent of the article's regulatory-
  urgency framing, and could be cited alongside other vendor-risk/
  procurement-readiness material if Ch05 covers that territory.

## Extraction Notes

- The primary article was fetched as raw HTML (not via WebFetch's
  summarization) and parsed with BeautifulSoup to obtain exact verbatim
  text for all quotes, after an initial WebFetch pass returned a
  paraphrased/summarized version unsuitable for direct quotation. The
  Mosca's Theorem quote (Claim 4) was specifically checked against the raw
  HTML to confirm it is one continuous sentence in the source (not two
  non-adjacent sentences spliced together) — the surrounding inline-math
  markup ($X$, $Y$, $Z$) in the rendered page briefly made this ambiguous
  during extraction.
- One linked page was followed per Miner step 1: the companion Thoughtworks
  piece "Three steps to post-quantum cryptography" (2025, different
  author), used only for corroboration context in Concrete Artifacts and
  Cross-References, not extracted as numbered claims of this source note.
  Three other "Related content" links on the page (a graph-neural-networks/
  fraud-prevention article, a "Thoughtworks at Sibos 2026" promo page, and
  the same companion piece linked twice) were not substantive enough to
  warrant following further.
- No paywall or access restriction encountered on either fetched URL.
- The article's "87%/7%" adoption statistic (Claim 5) and its "backdoor
  quantum vulnerabilities" supply-chain claim (Claim 7) could not be traced
  to a named underlying survey or incident within the article itself —
  flagged as anecdotal/unsourced rather than settled, consistent with
  MINER.md's instruction not to inflate confidence beyond what the source
  itself supports.
- No contradiction issue filed — see Cross-References "Contradicts" for
  reasoning.
