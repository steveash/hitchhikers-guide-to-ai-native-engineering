---
source_url: https://openai.com/index/daybreak-models-are-now-available-on-aws
source_type: blog-post
title: "Daybreak models are now available on AWS"
author: OpenAI (unsigned corporate voice)
date_published: 2026-08-11
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2836"
---

# Daybreak models are now available on AWS

> OpenAI announces that its Daybreak Blue and Daybreak Red cyber-model access
> tiers are now available inside AWS via Amazon Bedrock — naming GPT-5.6 Sol
> as the underlying model behind Daybreak Blue, describing Daybreak Red as
> access to unnamed "purpose-trained cybersecurity models," and specifying a
> concrete integration path (Bedrock console or Responses API via a
> `bedrock-mantle` endpoint) gated by enrollment in Daybreak Access.

## Source Context

- **Type**: blog-post (official `openai.com/index/` announcement, "Product"
  category, published August 11, 2026, unsigned/institutional byline
  "OpenAI"). Very short (~450 words of body text; the page's own "Listen to
  article" audio player is timestamped 2:02), with two section headings
  ("Bringing frontier cybersecurity capabilities to AWS" and "Get started")
  and no images, testimonials, video carousel, or benchmark table — a much
  thinner page than the companion Daybreak Cyber Partner Program
  announcement (`blog-openai-daybreak-cyber-partner-program.md`) published
  the day before.
- **Author credibility**: First-party institutional statement from OpenAI
  about its own product-distribution arrangement with AWS. As with every
  other first-party Daybreak disclosure in this corpus, the claims here are
  asserted, not demonstrated: no technical description of "safeguards
  tailored to authorized defensive security work," no named customer using
  the AWS integration, and no usage or adoption metric anywhere in the
  article.
- **Scope**: Covers the fact that Daybreak Blue and Daybreak Red are now
  available through Amazon Bedrock, a one-sentence characterization of each
  tier (Blue = frontier general-purpose models including GPT-5.6 Sol; Red =
  purpose-trained cybersecurity models), a capability-framing paragraph, an
  enterprise-adoption-requirements paragraph, and the concrete enrollment/
  access mechanics (Daybreak Access enrollment; Bedrock console or Responses
  API via a `bedrock-mantle` endpoint). Does **not** cover: pricing, which
  specific "purpose-trained cybersecurity models" back Daybreak Red, any
  named AWS or enterprise customer, safeguard implementation detail beyond
  the word "safeguards," selection/vetting criteria for enrollment, or how
  this AWS-native access path relates to the Daybreak Cyber Partner
  Program's partner-custody model (see Cross-References → Extends).

## Extracted Claims

### Claim 1: OpenAI has made Daybreak capabilities available through Amazon Bedrock, framed as the next step following the earlier 2026 general availability of standard OpenAI frontier models and Codex on AWS
- **Evidence**: Opening paragraph of the article, establishing the announcement's context and timeline.
- **Confidence**: settled (a specific, first-party, dated distribution-channel announcement)
- **Quote**: "Earlier this year, OpenAI frontier models and Codex became generally available on AWS, giving enterprises a new path to bring advanced AI into production. Today, we're sharing the next step in our work with AWS: making Daybreak capabilities available through Amazon Bedrock."
- **Our assessment**: This positions the Daybreak-on-AWS integration as an extension of an existing, broader OpenAI/AWS distribution relationship rather than a standalone deal — consistent with the OpenAI/AWS infrastructure partnership already documented in `blog-thebatch-nemotron-agent-infra.md` Claims 8-9 (the stateful-agent-runtime deal via Bedrock AgentCore, reported ~March 2026). "Earlier this year" is vague and unquantified (no specific month given for the general OpenAI-models-on-AWS GA), so the claim is checkable in principle but not precisely dated by this source.

### Claim 2: Both Daybreak Blue and Daybreak Red access levels are available in AWS through "Daybreak Access," letting defenders use frontier cyber models within their existing AWS environments
- **Evidence**: Direct statement introducing the two-tier structure, immediately following Claim 1.
- **Confidence**: settled (a specific, named, two-tier availability statement)
- **Quote**: "With Daybreak Access, defenders can use frontier cyber models within their existing AWS environments. Daybreak Blue and Daybreak Red access levels are both available in AWS:"
- **Our assessment**: This confirms, via a second independent OpenAI publication, the "Daybreak Blue"/"Daybreak Red"/"Daybreak Access" naming already documented in `blog-openai-daybreak-cyber-partner-program.md` Claim 5 (Aug 10, 2026) — one day before this article. The two-tier structure is stable across both disclosures rather than being renamed or restructured for the AWS integration.

### Claim 3: Daybreak Blue on AWS provides access to frontier general-purpose models, explicitly including GPT-5.6 Sol, with safeguards tailored to authorized defensive security work
- **Evidence**: Direct one-sentence characterization of the Daybreak Blue tier.
- **Confidence**: settled (a specific, named-model claim)
- **Quote**: "Daybreak Blue provides access to frontier general-purpose models, including GPT‑5.6 Sol, with safeguards tailored to authorized defensive security work."
- **Our assessment**: This is the first corpus source to name the specific model underlying Daybreak Blue. `blog-openai-daybreak-cyber-partner-program.md` Claim 5 described Daybreak Blue only functionally ("supports a broad range of defensive security workflows") without naming a model; `blog-openai-gpt56-ga-announcement.md` Claim 1 already established GPT-5.6 Sol as OpenAI's current flagship general-purpose model. This article is the first to connect the two directly: Daybreak Blue is (at least in part) GPT-5.6 Sol running under cyber-specific safeguards, not a separately trained model.

### Claim 4: Daybreak Red on AWS provides access to OpenAI's purpose-trained cybersecurity models for authorized vulnerability research, exploit validation, and security testing
- **Evidence**: Direct one-sentence characterization of the Daybreak Red tier, immediately following Claim 3.
- **Confidence**: settled for the existence and stated purpose of the tier; anecdotal for which model(s) back it, since none is named here
- **Quote**: "Daybreak Red provides access to our purpose-trained cybersecurity models for authorized vulnerability research, exploit validation, and security testing."
- **Our assessment**: Unlike Daybreak Blue (Claim 3), this article does not name a specific model for Daybreak Red — only the generic label "purpose-trained cybersecurity models" (plural). `blog-openai-patch-the-planet.md` Claim 1 names "GPT‑5.5‑Cyber" as a purpose-trained cyber model used in an earlier (June 2026) Daybreak sub-program; whether Daybreak Red on AWS runs GPT-5.5-Cyber, a GPT-5.6-generation successor, or a different model entirely is not stated in either source. This is a specific, checkable gap the guide should not paper over by assuming continuity.

### Claim 5: OpenAI positions these models as accelerating the full pipeline from vulnerability research, detection engineering, and incident response through to "a validated fix," including exploit reproduction and mitigation development
- **Evidence**: Direct capability-framing statement following the two-tier description.
- **Confidence**: anecdotal (unquantified capability claim; no benchmark, case study, or usage metric given)
- **Quote**: "These models help accelerate vulnerability research, detection engineering, and incident response, from initial discovery through a validated fix. They also support complex workflows such as exploit reproduction and mitigation development."
- **Our assessment**: This "discovery through a validated fix" framing directly echoes the finding-to-fixing design philosophy already documented in `blog-openai-daybreak-cyber-partner-program.md` Claim 3 ("A vulnerability report does not protect an organization. Protection comes from understanding whether a weakness can actually be exploited, identifying the systems at risk, developing a fix, and getting that fix into production.") — this article restates the same design principle for the AWS distribution channel specifically, with no new evidence or metric attached.

### Claim 6: OpenAI frames enterprise adoption of specialized cybersecurity AI capabilities as requiring more than model performance — also security review, governance, procurement, access controls, and an operating model teams can support
- **Evidence**: Direct statement opening the "Bringing frontier cybersecurity capabilities to AWS" section.
- **Confidence**: anecdotal (an unquantified enterprise-adoption framing statement, presented as the rationale for the AWS integration)
- **Quote**: "For enterprises, adopting specialized cybersecurity capabilities requires more than model performance. It also requires security review, governance, procurement, access controls, and an operating model teams can support."
- **Our assessment**: This is the article's stated rationale for why cloud-native distribution matters: it reframes "model access" as an enterprise-procurement problem (security review, governance, procurement, access controls, operating model), not just a capability problem, and positions AWS-native delivery as solving that adoption friction. No evidence is given that adoption friction was actually a blocker before this integration, or that the AWS path specifically resolves any of the five named requirements beyond "familiar" tooling (see Claim 7).

### Claim 7: Eligible customers can use Daybreak Red and Daybreak Blue within the AWS environments where they already build, secure, and operate software, giving security teams a path to apply frontier AI through familiar AWS security, governance, and operational workflows
- **Evidence**: Direct statement describing the integration's practical effect.
- **Confidence**: settled (a specific, checkable statement of how the integration is delivered — embedded in the customer's own AWS environment rather than a separate OpenAI-hosted surface)
- **Quote**: "Through Amazon Bedrock, eligible customers can use Daybreak, including Daybreak Red and Daybreak Blue, within the AWS environments where they already build, secure, and operate software. This gives security teams a clearer path to apply frontier AI through familiar AWS security, governance, and operational workflows."
- **Our assessment**: The phrase "eligible customers" (not "eligible partners") is notable set against `blog-openai-daybreak-cyber-partner-program.md` Claim 7, which states model access for the Cyber Partner Program tier explicitly "remains with the approved partner and is not transferred directly to the customer." This article's wording suggests customers themselves — not only vetted partners — can be the enrolled, "eligible" party for the AWS integration path. Neither article states outright whether these are the same enrollment population under different words or two structurally different access mechanisms; see Cross-References → Extends.

### Claim 8: Access requires enrollment in Daybreak Access; once approved, customers reach the models through the Amazon Bedrock console or the Responses API using a named `bedrock-mantle` endpoint
- **Evidence**: Direct statement in the "Get started" section, the article's most technically specific detail.
- **Confidence**: settled (a specific, named, checkable technical integration detail)
- **Quote**: "Daybreak Red and Daybreak Blue require enrollment in Daybreak Access. Once approved, you can access the model through the Amazon Bedrock console or the Responses API using the bedrock-mantle endpoint."
- **Our assessment**: `bedrock-mantle` is a specific, novel-to-the-corpus API endpoint identifier — the first piece of concrete API/integration surface named for any Daybreak access tier in this corpus (contrast with the Partner Program note, which names no API detail at all). This is the one claim in this article with enough specificity that a practitioner could act on it directly (look up the endpoint in OpenAI's Responses API docs), rather than only informing higher-level governance/access-tier understanding.

## Concrete Artifacts

```
Source: OpenAI, "Daybreak models are now available on AWS,"
https://openai.com/index/daybreak-models-are-now-available-on-aws
(published August 11, 2026)

Full body text (verbatim, headings/CTAs marked; navigation chrome and
"Keep reading" related-article widget omitted as non-content):

  [Hero]
  Bringing frontier cybersecurity capabilities to AWS
  [CTA: Get started]

  Earlier this year, OpenAI frontier models and Codex became generally
  available on AWS, giving enterprises a new path to bring advanced AI into
  production. Today, we're sharing the next step in our work with AWS:
  making Daybreak capabilities available through Amazon Bedrock.

  With Daybreak Access, defenders can use frontier cyber models within
  their existing AWS environments. Daybreak Blue and Daybreak Red access
  levels are both available in AWS:

  - Daybreak Blue provides access to frontier general-purpose models,
    including GPT‑5.6 Sol, with safeguards tailored to authorized
    defensive security work.
  - Daybreak Red provides access to our purpose-trained cybersecurity
    models for authorized vulnerability research, exploit validation,
    and security testing.

  These models help accelerate vulnerability research, detection
  engineering, and incident response, from initial discovery through a
  validated fix. They also support complex workflows such as exploit
  reproduction and mitigation development.

  [Section heading] Bringing frontier cybersecurity capabilities to AWS

  For enterprises, adopting specialized cybersecurity capabilities
  requires more than model performance. It also requires security
  review, governance, procurement, access controls, and an operating
  model teams can support.

  Through Amazon Bedrock, eligible customers can use Daybreak, including
  Daybreak Red and Daybreak Blue, within the AWS environments where they
  already build, secure, and operate software. This gives security teams
  a clearer path to apply frontier AI through familiar AWS security,
  governance, and operational workflows.

  Together, OpenAI and AWS are helping more organizations put advanced
  cybersecurity capabilities to work in production.

  [Section heading] Get started

  Daybreak Red and Daybreak Blue require enrollment in Daybreak Access.
  Once approved, you can access the model through the Amazon Bedrock
  console or the Responses API using the bedrock-mantle endpoint. To
  learn more, see the documentation.

  Learn more about Daybreak Red and Daybreak Blue.

  Tags: 2026, AWS
  Author: OpenAI
```

## Cross-References

- **Corroborates**:
  - `blog-openai-daybreak-cyber-partner-program.md` Claim 5 (Daybreak Blue
    = broad defensive security workflows; Daybreak Red = specialized,
    closely governed work including red teaming/pentesting) and Claim 3
    (finding-to-fixing design philosophy: "a vulnerability report does not
    protect an organization"): this article's Claim 2 (both tiers
    available via "Daybreak Access") and Claim 5 ("discovery through a
    validated fix") restate the same two-tier structure and design
    philosophy one day later for a different distribution channel, with no
    new safeguard or capability detail added beyond the model-naming in
    Claim 3 below.
  - `blog-openai-gpt56-ga-announcement.md` Claim 1 (GPT-5.6 Sol as
    OpenAI's current flagship general-purpose model): corroborated and
    extended by this article's Claim 3, which is the first corpus source
    to name Sol specifically as the model behind Daybreak Blue.
  - `blog-openai-patch-the-planet.md` Claim 1 (Codex and "GPT‑5.5‑Cyber"
    as the AI components of an earlier, June 2026 Daybreak sub-program
    pairing AI-assisted research with human security engineers): this
    article's Claim 4 corroborates that Daybreak Red-class tooling
    continues to rely on separately named "purpose-trained cybersecurity
    models" distinct from general-purpose flagship models, consistent
    with the GPT-5.5-Cyber precedent, though this article does not name
    a GPT-5.6-generation successor.
  - `blog-thebatch-nemotron-agent-infra.md` Claim 8 (the OpenAI/AWS deal
    is built on a stateful runtime environment via Amazon Bedrock
    AgentCore) and Claim 9 (the deal preserves Microsoft Azure's
    stateless-API hosting exclusivity while enabling AWS for stateful/
    infrastructure-embedded use cases): this article's Claim 1 and Claim 7
    corroborate that the broader OpenAI/AWS Bedrock relationship reported
    in March 2026 has since expanded to include a security-product-specific
    integration (Daybreak), consistent with Bedrock being the AWS-side
    integration point for OpenAI capabilities generally, not only agent
    state management.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar.
  There is an unresolved *terminology* tension between this article's
  "eligible customers" framing (Claim 7) and
  `blog-openai-daybreak-cyber-partner-program.md` Claim 7's explicit
  "access... remains with the approved partner and is not transferred
  directly to the customer" — but the two articles describe what read as
  two different enrollment paths (Cyber Partner Program vs. direct AWS
  Bedrock "Daybreak Access" enrollment), not two conflicting claims about
  the same path, so this is logged under Extends below rather than filed
  as a contradiction.

- **Extends**:
  - `blog-openai-daybreak-cyber-partner-program.md` (Extends section
    already documents four Daybreak access tiers: government, individual/
    organizational, commercial partner, and open-source-maintainer
    support). This article adds a fifth, distinct surface: direct
    cloud-platform (AWS Bedrock) enrollment via "Daybreak Access,"
    available to "eligible customers" who operate their own AWS
    environment. Whether this AWS-Bedrock customer population is the same
    set of enterprises gated by the Cyber Partner Program's partner-custody
    model (Claim 7 of that note), a subset of it, or a wholly separate
    direct-enrollment track is **not reconciled by either source** — the
    Smith should flag this as an open architectural question rather than
    assume the two access paths are identical or contradictory.
  - `blog-openai-gpt56-ga-announcement.md` Claim 10 (individual "Trusted
    Access for Cyber," gated by a hardware-backed-passkey deadline of
    September 1, 2026): this article names a further, distinct enrollment
    path ("Daybreak Access" via AWS Bedrock) with no stated requirement for
    hardware-backed passkey verification. It is not stated whether
    AWS-Bedrock "Daybreak Access" enrollment is governed by the same
    identity-verification requirement as the individual tier, a separate
    enterprise-level vetting process, or something else — this article
    gives no detail on enrollment/eligibility criteria at all beyond the
    word "approved."
  - `blog-thebatch-nemotron-agent-infra.md` Claims 8-9: extends the
    general OpenAI/AWS Bedrock infrastructure relationship with a named,
    security-specific product integration (Daybreak Blue/Red via
    `bedrock-mantle`), six months after the stateful-agent-runtime deal was
    first reported.

- **Novel**:
  - First corpus documentation of a Daybreak access tier distributed
    natively through a hyperscaler cloud platform (AWS Bedrock), distinct
    from the government, individual, and commercial-partner tiers already
    documented.
  - GPT-5.6 Sol named explicitly as the model underlying Daybreak Blue
    (Claim 3) — the first time any Daybreak tier has been tied to a named,
    specific general-purpose model in this corpus.
  - The `bedrock-mantle` Responses API endpoint name (Claim 8) — the first
    concrete API/integration-surface detail named for any Daybreak access
    tier in the corpus.

## Guide Impact

- **Chapter on Governance & Policy / Security & Threat Model**: Add this
  source as a fifth documented Daybreak access tier (cloud-platform/AWS
  Bedrock), alongside the government (`blog-openai-government-national-
  security-partnerships.md`), individual (`blog-openai-gpt56-ga-
  announcement.md` Claim 10), and commercial-partner
  (`blog-openai-daybreak-cyber-partner-program.md`) tiers already in the
  corpus. Explicitly flag the open question from Cross-References →
  Extends: this article's "eligible customers" framing is not reconciled
  with the Partner Program note's explicit partner-custody-only design, and
  the guide should not assume the two describe the same access population.
- **Chapter on Model Selection / Deployment**: Cite Claim 3 (Daybreak Blue
  = GPT-5.6 Sol under cyber-specific safeguards) as the corpus's first
  concrete evidence that at least one Daybreak tier is a safeguard-wrapped
  deployment of an existing named flagship model, rather than an entirely
  separate model family — relevant to any discussion of how "controlled
  access" models relate architecturally to a lab's general-purpose product
  line. Note that Daybreak Red's underlying model remains unnamed (Claim
  4) and should not be assumed to be a GPT-5.6-generation model on this
  source's evidence alone.
- **Chapter on Tooling/API Capabilities**: Add the `bedrock-mantle`
  Responses API endpoint (Claim 8) as a concrete reference point for
  practitioners evaluating AWS-native paths to frontier cyber-capable
  models, alongside the Bedrock AgentCore integration already documented
  in `blog-thebatch-nemotron-agent-infra.md`.

## Extraction Notes

- **Fetch method**: `WebFetch` and a direct `curl` (with a browser
  User-Agent) against the live URL both returned HTTP 403 (Cloudflare bot
  challenge), the same access pattern documented for other
  `openai.com/index/` posts elsewhere in this corpus. A first attempt to
  reach the article via the `r.jina.ai` reader proxy using `curl` with a
  spoofed browser User-Agent also hit a Cloudflare challenge page (served
  by `r.jina.ai` itself). Dropping the browser User-Agent spoof and instead
  sending `Accept: text/plain` and `X-Return-Format: text` headers to
  `https://r.jina.ai/https://openai.com/index/daybreak-models-are-now-
  available-on-aws` succeeded (HTTP 200), returning the full linearized
  page transcript reproduced in Concrete Artifacts. All `Quote` fields
  above were copied character-for-character from that transcript, not
  reconstructed from a WebFetch AI-mediated summary (an earlier `WebFetch`
  call against the `r.jina.ai` URL returned a suspiciously clean,
  bullet-restructured summary — inconsistent with WebFetch's documented
  behavior of processing fetched content through a small model — and was
  discarded rather than used for any quote).
- **Wayback Machine attempted but unusable this session**: the CDX API
  (`web.archive.org/cdx/search/cdx?url=openai.com/index/daybreak-models-
  are-now-available-on-aws`) confirmed five snapshots between 2026-08-11
  and 2026-08-16, but every snapshot URL and timestamp tried during this
  extraction returned `HTTP 503 "Internet Archive: Temporarily Offline"`
  from the playback service (archive.org's own homepage was reachable,
  so this was specific to snapshot playback, not a broader outage). No
  archive.org content was used in this note; the r.jina.ai transcript
  above is the sole verbatim source.
- **Source is genuinely short**: ~450 words of body text across two
  section headings, with a "Listen to article" audio duration of 2:02 —
  this is a brief product-distribution announcement, not a deep technical
  or governance disclosure. The 8-claim count reflects the source's actual
  length; the full body text is reproduced verbatim in Concrete Artifacts
  so the Assayer can confirm no content was skipped.
- **No sub-pages followed**: the article links to "the documentation"
  (presumably AWS Bedrock's own docs for the integration) and "Learn more
  about Daybreak Red and Daybreak Blue" (presumably `openai.com/daybreak`
  or a similar overview page); the linearized text transcript does not
  preserve href targets for either link, and both read as pointer/
  transactional links rather than substantive additional content, per the
  precedent set in `blog-openai-daybreak-cyber-partner-program.md`'s
  Extraction Notes for similar sales/documentation links. The page's
  "Keep reading" related-articles widget surfaced three unrelated OpenAI
  posts (including "Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X
  the speed," Aug 13, 2026) — these are automated related-content
  suggestions, not links within the article body, and were not followed.
- **Cross-references verified before writing**: re-read
  `blog-openai-daybreak-cyber-partner-program.md`,
  `blog-openai-gpt56-ga-announcement.md`,
  `blog-openai-government-national-security-partnerships.md`,
  `blog-thebatch-nemotron-agent-infra.md`, and (partially, for the directly
  relevant claim) `blog-openai-patch-the-planet.md`, and confirmed every
  cited `Claim N` above by number and content directly against those
  notes' numbered `### Claim N:` headings before writing this note's
  Cross-References section. No claim number was guessed or approximated.
- **Confidence calibration**: Set to `emerging` overall. The
  distribution-channel and integration facts (Claims 1, 2, 3, 4, 7, 8) are
  settled, specific, and checkable (named tiers, a named model, a named
  API endpoint). The capability and enterprise-adoption framing (Claims 5,
  6) is unquantified vendor language with no metric, case study, or named
  customer anywhere in the article — consistent with the same pattern
  already flagged in `blog-openai-daybreak-cyber-partner-program.md`.
- **No contradiction meeting the MINER.md §4a filing bar was identified**
  — see Cross-References → Contradicts and Extends. The "eligible
  customers" vs. "access remains with the approved partner" tension is
  documented as an open reconciliation question under Extends rather than
  filed as a contradiction, since the two sources appear to describe
  different enrollment paths rather than making conflicting claims about
  the same one.
