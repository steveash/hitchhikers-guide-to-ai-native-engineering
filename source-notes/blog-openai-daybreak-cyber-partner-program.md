---
source_url: https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands
source_type: blog-post
title: "Putting frontier cyber models in more trusted hands"
author: OpenAI (unsigned corporate voice)
date_published: 2026-08-10
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: emerging
issue: "#2779"
---

# Putting frontier cyber models in more trusted hands

> OpenAI announces its Daybreak Cyber Partner Program, naming 16 security,
> services, and technology partners (Accenture, IBM, Capgemini, Cognizant,
> EY, KPMG, PwC, NCC Group, SpecterOps, Palo Alto Networks, CrowdStrike,
> Cisco, Sophos, Akamai, Fortinet, Cloudflare) who can embed OpenAI's
> controlled-access frontier cyber models — via two named product tiers,
> Daybreak Blue and Daybreak Red — into their own security services, with
> model access kept at the partner level (not transferred to the partner's
> customers) and safeguards described only at the category level (identity
> verification, defined testing scopes, logging, monitoring, human
> oversight).

## Source Context

- **Type**: blog-post (official `openai.com/index/` announcement, "Security"
  category, published August 10, 2026, unsigned/institutional byline
  "OpenAI"). Short (~600 words), four headed sections ("From finding
  vulnerabilities to fixing them," "Bringing frontier models into existing
  security operations," "More access, with the safeguards to match,"
  "Closing the defense gap together"), plus a partner-logo image and a
  "Hear from Daybreak partners" video carousel with no accompanying
  transcript text on the page.
- **Author credibility**: First-party institutional statement from OpenAI
  about its own commercial partner program. This is the authoritative
  source for *what OpenAI says the program's structure and named partners
  are*, but — as with every other first-party OpenAI Daybreak disclosure in
  this corpus (`blog-openai-astra-critical-cyber-capabilities.md`,
  `blog-openai-government-national-security-partnerships.md`,
  `blog-openai-patch-the-planet.md`) — the safeguards described ("logging,
  monitoring, human oversight") are asserted, not demonstrated: no
  technical implementation, audit mechanism, or independent verification of
  any named partner's actual practice is given. No named individual is
  quoted in body text; the "Hear from Daybreak partners" section is a video
  carousel, not a transcript.
- **Scope**: Covers the name and stated purpose of the Daybreak Cyber
  Partner Program, its 16 named partners (split into "security & services"
  and "technology" categories), the class of engagement work partners can
  perform, two named access-tier products (Daybreak Blue, Daybreak Red),
  a category-level list of safeguards, and an explicit statement that model
  access is not transferred to the partner's end customer. Does **not**
  cover: pricing, selection/vetting criteria for becoming a partner, any
  named government agency or AI safety organization (contrast with the
  companion Astra disclosure's Claim 8 testing-partner commitment — see
  Extends below), technical detail on how Daybreak Blue differs from
  Daybreak Red beyond the one-sentence characterization each gets, how
  "logging" or "monitoring" are technically implemented, or any metric,
  case study, or named vulnerability finding produced through the program
  (contrast with `blog-openai-patch-the-planet.md`'s per-CVE findings from
  a different, narrower Daybreak sub-program).

## Extracted Claims

### Claim 1: OpenAI's Daybreak Cyber Partner Program includes named security & services partners (Accenture, IBM, Capgemini, Cognizant, EY, KPMG, PwC, NCC Group, SpecterOps) and named technology partners (Palo Alto Networks, CrowdStrike, Cisco, Sophos, Akamai, Fortinet, Cloudflare)
- **Evidence**: Direct enumeration in the article's second paragraph, immediately following the partner-logo image.
- **Confidence**: settled (a specific, named, first-party partner list)
- **Quote**: "Our Daybreak Cyber Partner program includes leading security & services partners such as Accenture, IBM, Capgemini, Cognizant, EY, KPMG, PwC, NCC Group, and SpecterOps along with technology partners Palo Alto Networks, CrowdStrike, Cisco, Sophos, Akamai, Fortinet and Cloudflare." (the source renders each partner name as a hyperlink with a screen-reader-only "(opens in a new window)" label immediately after; these labels are omitted here as non-content formatting noise, per the precedent set in `blog-openai-astra-critical-cyber-capabilities.md`'s Claim 1 footnote-omission handling)
- **Our assessment**: This is the first corpus source to name the Daybreak Cyber Partner Program specifically and to enumerate its 16 partners. Four of these names — Accenture, Palo Alto Networks, CrowdStrike, and PwC — also appear as named Claude/Opus security partners in `blog-anthropic-opus-cybersecurity-partners.md` (that note's Claims 4, 5, 9, and 10 respectively). That is a concrete, checkable overlap: at least four major security/consulting vendors are simultaneously building AI-driven cybersecurity offerings on top of both OpenAI's and Anthropic's frontier models, a multi-vendor-frontier-model strategy not previously documented explicitly in this corpus. Whether this reflects genuine dual-sourcing for resilience/leverage, or simply that a short list of enterprise security vendors has fully saturated its "add a frontier-lab AI partnership" quota with both major U.S. labs, is not something either source addresses.

### Claim 2: OpenAI frames the motivation for the program as: AI is changing cybersecurity faster than most organizations can respond, with attackers gaining speed and scale while too many defenders lack access to the frontier models that could help them determine which vulnerabilities pose a real threat and fix them
- **Evidence**: Full opening paragraph of the article body (following the introductory sentence and partner-logo image), stated as the article's framing problem statement.
- **Confidence**: anecdotal (unquantified motivational framing; no cited statistic, incident count, or named study backs the "faster than most organizations can respond" claim)
- **Quote**: "AI is changing cybersecurity faster than most organizations can respond. Attackers can identify vulnerabilities, develop exploits, and move through complex systems with increasing speed and scale. At the same time, security teams are confronting a growing volume of weaknesses across the software and infrastructure they protect. Finding those vulnerabilities is only the beginning. The harder challenge is determining which ones pose a real threat and fixing them before they can be exploited. Too many defenders still lack access to the frontier models that can help them do that."
- **Our assessment**: This is standard frontier-lab "defense must keep pace with offense" framing, structurally identical to the register already documented from Anthropic (`blog-anthropic-opus-cybersecurity-partners.md` Claim 12: "As attackers weaponize frontier models to automate cyberattacks, the defense must move faster," quoting Palo Alto Networks' Sam Rubin) and from OpenAI itself in the companion Astra post (`blog-openai-astra-critical-cyber-capabilities.md` Claim 10: "We believe advanced cyber-capable models should help defenders identify and address vulnerabilities before attackers do"). The specific new element here is naming the access gap itself — "too many defenders still lack access to the frontier models" — as the problem this program is designed to solve, rather than a capability gap in the models.

### Claim 3: OpenAI states that a vulnerability report alone does not protect an organization — protection instead requires understanding whether a weakness can actually be exploited, identifying at-risk systems, developing a fix, and getting that fix into production
- **Evidence**: Opening statement of the "From finding vulnerabilities to fixing them" section, presented as the program's underlying design philosophy.
- **Confidence**: emerging (a specific, falsifiable-in-principle four-step framing of what "protection" requires, though not independently tested or measured against any incident data in this article)
- **Quote**: "A vulnerability report does not protect an organization. Protection comes from understanding whether a weakness can actually be exploited, identifying the systems at risk, developing a fix, and getting that fix into production."
- **Our assessment**: This four-step chain (exploitability assessment → at-risk-system identification → fix development → production deployment) is a reusable framing for evaluating any AI-cyber tool's actual value proposition: a tool that only produces vulnerability reports addresses step zero, not the harder downstream steps. It corroborates the finding-to-fixing gap already documented from Anthropic's side (`blog-anthropic-opus-cybersecurity-partners.md` Claim 7: Deloitte's "the gap helps determine whether attackers or defenders win the window," and Claim 6: TrendAI's 96-day virtual-patching lead time) — both labs' partner ecosystems are explicitly positioned around closing the same discovery-to-remediation gap, not just discovery volume.

### Claim 4: Depending on the engagement, Daybreak Cyber Partners can help with vulnerability discovery and validation, red teaming, penetration testing, incident response, and remediation across complex enterprise systems
- **Evidence**: Direct statement under "From finding vulnerabilities to fixing them," describing the scope of work partners perform.
- **Confidence**: settled (a direct, specific first-party enumeration of program scope)
- **Quote**: "Depending on the engagement, partners can help with vulnerability discovery and validation, red teaming, penetration testing, incident response, and remediation across complex enterprise systems."
- **Our assessment**: This is a broader service scope than any single Anthropic partner offering documented in this corpus — it spans both offensive (red teaming, pentesting) and defensive/reactive (incident response, remediation) work under one program, whereas `blog-anthropic-opus-cybersecurity-partners.md` organizes its seven partners into three narrower named areas (offensive testing, finding-to-fixing, governed production deployment). Whether OpenAI's broader single-program framing reflects genuinely broader partner capability, or simply a less granular public description of the same underlying partner specialization, cannot be determined from this article alone.

### Claim 5: Approved partners can access one of two named product tiers — Daybreak Blue or Daybreak Red — through "Daybreak Access," where Daybreak Blue supports a broad range of defensive security workflows and Daybreak Red is designed for more specialized, closely governed work including red teaming and penetration testing
- **Evidence**: Direct statement under "Bringing frontier models into existing security operations," naming the two access-tier products.
- **Confidence**: settled (a specific, named, two-tier product structure, stated directly)
- **Quote**: "Partners can access Daybreak Blue or Daybreak Red through Daybreak Access, depending on their needs and the work involved. Daybreak Blue supports a broad range of defensive security workflows, while Daybreak Red is designed for more specialized, closely governed work, including red teaming and penetration testing."
- **Our assessment**: "Daybreak Blue," "Daybreak Red," and "Daybreak Access" are new names to this corpus — no prior mined OpenAI Daybreak source (`blog-openai-astra-critical-cyber-capabilities.md`, `blog-openai-government-national-security-partnerships.md`, `blog-openai-patch-the-planet.md`, or `blog-openai-gpt56-ga-announcement.md` Claim 10's individual "Trusted Access for Cyber" tier) names these specific product tiers. The Blue/Red split maps roughly onto a defense/offense capability split (Blue = general defensive workflows, Red = red-teaming/pentesting specifically), which is consistent with the general pattern that offensive-capable cyber tooling gets a narrower, more closely governed access tier than defensive tooling — the same graduated-access logic seen in `blog-openai-gpt56-ga-announcement.md` Claim 10's individual-tier hardware-passkey gate, just applied at the partner-product level instead of the individual-account level. This article gives no further technical detail (model version, capability differences, or specific governance mechanism) distinguishing the two beyond this one sentence each.

### Claim 6: Safeguards for Daybreak Cyber Partner engagements can include identity verification, defined testing scopes, logging, monitoring, and human oversight, depending on the specific work
- **Evidence**: Direct statement opening the "More access, with the safeguards to match" section.
- **Confidence**: anecdotal (a category-level list of safeguard types, stated as things that "can include" — not a commitment that all five apply to every engagement, and no detail on how any of the five is technically implemented or audited)
- **Quote**: "Daybreak Cyber Partners use OpenAI's controlled-access models within trusted, governed engagements. Depending on the work, safeguards can include identity verification, defined testing scopes, logging, monitoring, and human oversight."
- **Our assessment**: This is thinner than the corresponding safeguards disclosure in the Astra post, which itemized five specific, more concrete internal security-control steps (isolated testing environments, restricted network/tool access, weight encryption, universal Chain-of-Thought monitoring, activity pausing — `blog-openai-astra-critical-cyber-capabilities.md` Claim 5 and Concrete Artifacts). Here the five safeguard categories are named but not described mechanically, and the hedge "can include" (rather than "we require") leaves open whether any specific engagement actually implements all five. This should be read as evidence a governance framework exists in name, not evidence of its operational strength.

### Claim 7: Access to the underlying Daybreak models remains with the approved partner and is not transferred directly to the partner's customer; the partner defines engagement boundaries, reviews findings, and applies its own expertise before any action is taken
- **Evidence**: Direct statement immediately following Claim 6's safeguards list, in the same "More access, with the safeguards to match" section.
- **Confidence**: settled (a specific, structural governance claim about who holds model access)
- **Quote**: "Access to the underlying models remains with the approved partner and is not transferred directly to the customer. Partners work with organizations to define the boundaries of each engagement, review findings, and apply their expertise before action is taken."
- **Our assessment**: This is the most concrete, portable governance pattern in the article: a capability-gated model is deployed to end customers only through a vetted intermediary who retains custody of the access itself, rather than the model credentials being handed to the customer directly. This is architecturally the same custody pattern already documented for Anthropic's partner ecosystem in `blog-anthropic-opus-cybersecurity-partners.md` (e.g. Wiz Red Agent, PwC's "Secure AI Adoption," CrowdStrike's Frontier AI Readiness — in every case the vendor runs the AI-powered service and delivers validated findings, rather than handing raw model access to the customer), though that note did not extract an equally explicit "access is not transferred" statement from Anthropic. This article is the first in this corpus to state that non-transferability explicitly and as a named design principle, not just an implicit product architecture.

### Claim 8: OpenAI closes the article stating that attackers are moving faster than many security teams can respond, and that closing this gap requires frontier models, experienced security practitioners, and trusted partners capable of bringing those capabilities into real-world environments
- **Evidence**: Direct statements in the closing "Closing the defense gap together" section.
- **Confidence**: anecdotal (aspirational closing framing with no new specific commitment, metric, or named partner attached)
- **Quote**: "Attackers are moving faster than many security teams can respond. Closing that gap means getting stronger defenses to the organizations that need them. Meeting this moment requires frontier models, experienced security practitioners, and trusted partners capable of bringing those capabilities into real-world environments."
- **Our assessment**: Standard closing mission-register rhetoric, consistent with the pattern already noted in `blog-openai-astra-critical-cyber-capabilities.md` Claim 10's assessment (frontier-lab posts closing a specific disclosure with sweeping "defense/benefit of all" framing). No example of a specific vulnerability found and fixed through the Daybreak Cyber Partner Program is given anywhere in this article — contrast with `blog-openai-patch-the-planet.md`, whose Claims cite specific CVEs (e.g. CVE-2026-8390) and per-project findings counts from a different, narrower Daybreak sub-program.

### Claim 9: Organizations can bring Daybreak capabilities into their security operations by contacting their cybersecurity provider or OpenAI's sales team, and cybersecurity companies, service providers, and consultancies interested in joining the program can apply via a named partners page
- **Evidence**: Final paragraph of the article, the operational call-to-action closing the piece.
- **Confidence**: settled (a direct, checkable statement that an open enrollment/contact channel exists, independent of whether any given applicant would be accepted)
- **Quote**: "To bring Daybreak capabilities into your security operations, contact your cybersecurity provider or speak with our sales team. Cybersecurity companies, service providers, and consultancies interested in joining the program can learn more at openai.com/daybreak/partners."
- **Our assessment**: This confirms the partner list in Claim 1 is not presented as closed or final — the program has an open application channel for additional security companies, service providers, and consultancies. No selection or vetting criteria are given (contrast with `blog-openai-government-national-security-partnerships.md`'s more detailed eligibility framework for government partners, Claims 7–8 of that note), so it is not possible to assess from this article alone how selective the partner-approval process actually is.

## Concrete Artifacts

```
Source: OpenAI, "Putting frontier cyber models in more trusted hands,"
https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands
(published August 10, 2026)

Daybreak Cyber Partner Program — named partners (verbatim list, link/
accessibility-label markup stripped per Claim 1's Quote note):

Security & services partners:
  - Accenture
  - IBM
  - Capgemini
  - Cognizant
  - EY
  - KPMG
  - PwC
  - NCC Group
  - SpecterOps

Technology partners:
  - Palo Alto Networks
  - CrowdStrike
  - Cisco
  - Sophos
  - Akamai
  - Fortinet
  - Cloudflare

Access tiers (verbatim):
  "Daybreak Blue supports a broad range of defensive security workflows,
  while Daybreak Red is designed for more specialized, closely governed
  work, including red teaming and penetration testing."

Safeguard categories (verbatim, "can include"):
  - identity verification
  - defined testing scopes
  - logging
  - monitoring
  - human oversight

Enrollment / contact channels (verbatim):
  "To bring Daybreak capabilities into your security operations, contact
  your cybersecurity provider or speak with our sales team. Cybersecurity
  companies, service providers, and consultancies interested in joining
  the program can learn more at openai.com/daybreak/partners."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-opus-cybersecurity-partners.md`: four of this article's
    16 named partners — Accenture, Palo Alto Networks, CrowdStrike, and PwC
    — are also named partners in Anthropic's Opus cybersecurity partner
    ecosystem (that note's Claims 5, 4, 10, and 9 respectively). This is a
    specific, checkable overlap establishing that at least four major
    security/consulting vendors are simultaneously building AI-driven
    cybersecurity offerings on both OpenAI's and Anthropic's frontier
    models — see Claim 1's assessment above.
  - `blog-anthropic-opus-cybersecurity-partners.md` Claim 7 (Deloitte's
    "the gap helps determine whether attackers or defenders win the
    window") and Claim 6 (TrendAI's 96-day virtual-patching lead time):
    both corroborate this article's Claim 3 finding-to-fixing framing —
    both labs' partner ecosystems are explicitly built around closing the
    same discovery-to-remediation gap.
  - `blog-openai-astra-critical-cyber-capabilities.md` Claim 10 ("We
    believe advanced cyber-capable models should help defenders identify
    and address vulnerabilities before attackers do") and
    `blog-anthropic-opus-cybersecurity-partners.md` Claim 12 (Sam Rubin:
    "As attackers weaponize frontier models to automate cyberattacks, the
    defense must move faster"): both corroborate this article's Claim 2
    "defense must keep pace with offense" framing — the same rhetorical
    register appears across both labs' cyber-partnership disclosures.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Daybreak's partner structure, access tiers, or safeguards that
  opposes what this article states. No contradiction issue filed.

- **Extends**:
  - `blog-openai-astra-critical-cyber-capabilities.md`: that note's
    Extraction Notes explicitly flagged this exact article ("Putting
    frontier cyber models in more trusted hands," Aug 10, 2026) as a
    "strong candidate future Miner target" tied to that note's Claim 8
    (OpenAI's unnamed commitment to work with "relevant government
    agencies and select AI safety organizations" to test Astra). **Having
    now read this article directly, it does not resolve that open
    question**: this article names commercial security/services and
    technology partners (Claim 1 above), not any government agency or AI
    safety organization, and never mentions Astra by name. The Prospector's
    routing note for this issue ("this Aug 10 companion post likely
    supplies those details") should be treated as not borne out by the
    source text — the government/safety-org testing-partner question
    raised by `blog-openai-astra-critical-cyber-capabilities.md` Claim 8
    remains open and unresolved in the corpus.
  - `blog-openai-government-national-security-partnerships.md` Claim 4
    (Daybreak's government-level "Trusted Access for Cyber" partnerships
    with nine named allied governments/institutions) and
    `blog-openai-gpt56-ga-announcement.md` Claim 10 (Daybreak's
    individual/organizational "Trusted Access for Cyber" tier, gated by a
    hardware-backed-passkey deadline): this article documents a third,
    distinct Daybreak access tier — the commercial partner-program tier —
    naming 16 enterprise partners rather than allied governments or
    individual accounts. Together with `blog-openai-patch-the-planet.md`
    (a fourth, open-source-maintainer-support Daybreak sub-program with
    Trail of Bits), the corpus now documents four concurrently running,
    differently-gated Daybreak access tracks: government, individual/
    organizational, commercial partner, and open-source-maintainer
    support. No single source describes all four together or explains how
    they relate operationally to one another.

- **Novel**: The name "Daybreak Cyber Partner Program" and its 16-partner
  list (Claim 1); the named product tiers "Daybreak Blue" and "Daybreak
  Red" and the access mechanism "Daybreak Access" (Claim 5); and the
  explicit, named statement that underlying model access "remains with the
  approved partner and is not transferred directly to the customer"
  (Claim 7) are all first appearances in this corpus.

## Guide Impact

- **Chapter on Governance & Policy / Security & Threat Model**: Add Claim 7
  (access-custody-stays-with-the-vetted-intermediary pattern) as a named,
  reusable governance pattern for deploying capability-gated or dual-use
  models: the vendor/partner, not the end customer, holds model access and
  is accountable for defining engagement scope and reviewing output before
  action. Pair with the architecturally similar (but less explicitly
  stated) pattern already documented from Anthropic's partner ecosystem in
  `blog-anthropic-opus-cybersecurity-partners.md`, to show this is a
  cross-lab convergent design choice for AI-driven offensive/defensive
  security tooling, not an OpenAI-specific idiosyncrasy.
- **Chapter on Governance & Policy**: Cite the four-tier Daybreak access
  structure now documented across this note, `blog-openai-government-
  national-security-partnerships.md`, `blog-openai-gpt56-ga-announcement.md`,
  and `blog-openai-patch-the-planet.md` as a worked example of how one
  frontier lab operationalizes "controlled access" for a model class it has
  separately flagged as approaching its highest internal risk threshold
  (`blog-openai-astra-critical-cyber-capabilities.md`). Flag explicitly
  that no single OpenAI source ties these four tracks together or explains
  their relationship — the guide should present them as four separately
  disclosed tiers, not as a documented, unified architecture.
- **Do not cite this source as identifying which government agencies or AI
  safety organizations will test Astra's cyber capabilities** — see Extends
  above. That question, raised by `blog-openai-astra-critical-cyber-
  capabilities.md` Claim 8, remains open.

## Extraction Notes

- **Fetch method**: `WebFetch` and direct `curl` (with a browser
  user-agent) against the live URL both returned HTTP 403 (Cloudflare bot
  challenge, `cf-mitigated: challenge`), consistent with the access pattern
  already documented for other `openai.com/index/` posts in this corpus.
  The article was successfully retrieved via the `r.jina.ai` reader proxy
  (`https://r.jina.ai/https://openai.com/index/putting-frontier-cyber-
  models-in-more-trusted-hands`), which returned the full linearized page
  text (HTTP 200) including all section headings and body paragraphs. All
  `Quote` fields above were copied character-for-character from that
  extracted text (after stripping markdown hyperlink syntax and
  screen-reader-only "(opens in a new window)" labels around partner
  names, per the precedent documented in Claim 1's Quote note), not
  reconstructed from a WebFetch AI-mediated summary.
- **Video carousel not transcribed**: The page includes a "Hear from
  Daybreak partners" section with a "1 of 4" video carousel and a second
  "1 of 3" carousel under "Bringing frontier models into existing security
  operations" / "More access, with the safeguards to match." The reader
  proxy extraction returned only the carousel position markers ("1 of 4",
  "1 of 3"), not video transcripts or captions — no video content was
  available to extract as text. This is flagged as a gap: any spoken
  partner testimonials in those videos are not represented in this note.
- **No sub-pages followed**: The article links to `openai.com/daybreak/
  contact-cyber-sales/` (a sales contact form) and `openai.com/daybreak/
  partners-new/` (partner application page), plus each named partner's own
  homepage. None were fetched — the sales-contact and partner-application
  links are transactional pages with no substantive editorial content
  relevant to this note's extraction, and the individual partner homepages
  are third-party sites outside this article's own scope.
- **Cross-references verified before writing**: re-read
  `blog-openai-astra-critical-cyber-capabilities.md`,
  `blog-openai-government-national-security-partnerships.md`,
  `blog-openai-gpt56-ga-announcement.md`, `blog-openai-patch-the-planet.md`,
  and `blog-anthropic-opus-cybersecurity-partners.md` in full and confirmed
  every cited `Claim N` by number and content before writing this note's
  Cross-References section. No claim number was guessed or approximated.
  The partner-name overlap in Claim 1 (Accenture, Palo Alto Networks,
  CrowdStrike, PwC) was checked against `blog-anthropic-opus-cybersecurity-
  partners.md`'s partner deployment map and confirmed against that note's
  numbered claims directly, not against the summary table alone.
- **Confidence calibration**: Set to `emerging` overall. The partner list,
  program name, and access-tier names (Claims 1, 4, 5, 7, 9) are settled,
  specific, checkable facts. The motivational framing and safeguards
  description (Claims 2, 3, 6, 8) are unquantified, category-level, or
  aspirational, with no independently verifiable detail on how safeguards
  are technically implemented or audited. The overall rating reflects that
  mix rather than treating the whole article as either fully settled or
  purely anecdotal.
- **No contradiction meeting the MINER.md §4a filing bar was identified**
  — see Cross-References → Contradicts. No contradiction issue was filed.
  Note that the Extends section above does flag a discrepancy between the
  Prospector's routing expectation for this issue and what the source
  actually contains (it does not name Astra's government/safety-org
  testing partners) — this is a routing/expectation mismatch, not a
  claim-level contradiction between two sources, so it is documented under
  Extends rather than filed as a contradiction issue.
