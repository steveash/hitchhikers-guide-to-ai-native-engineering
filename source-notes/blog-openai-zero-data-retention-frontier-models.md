---
source_url: https://openai.com/index/offering-zero-data-retention-for-frontier-models
source_type: blog-post
title: "Offering Zero Data Retention for frontier models"
author: OpenAI
date_published: 2026-08-19
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: anecdotal
issue: "#3058"
---

# Offering Zero Data Retention for frontier models

> OpenAI's reaffirmation of Zero Data Retention (ZDR) for eligible API
> customers, paired with a preview of "Private Safety Processing" — a new
> mechanism designed to detect cross-interaction misuse patterns (multi-turn
> probing, coordinated abuse, agentic tasks drifting from user intent) using
> encrypted customer content and narrow automated signals, without giving
> OpenAI personnel access to underlying prompts or responses. Four named
> enterprise CISOs/CTOs (Glean, Databricks, Abridge, Microsoft) endorse the
> approach; full rollout and a technical white paper are promised for
> September 2026. The post positions this as a technical answer to the
> exact tradeoff JetBrains described accepting with Anthropic in
> `blog-anthropic-jetbrains-fable5-evaluation-deployment.md` Claim 8.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`, "Company /
  Safety" category, published August 19, 2026; unsigned/house-authored
  product-safety announcement with an embedded customer-testimonial
  carousel, auto-discovered via the `openai-news` trusted RSS feed).
- **Author credibility**: First-party OpenAI vendor content, unsigned (no
  named individual author on OpenAI's side). Four named external
  individuals are quoted with title and company: Sunil Agrawal (CISO,
  Glean), Hanlin Tang (CTO of Neural Networks, Databricks), Zach Powers
  (CISO, Abridge), and Sarah Bird (Chief Product Officer of Responsible AI,
  Microsoft) — all OpenAI-selected, OpenAI-published endorsements of
  OpenAI's own data-handling posture, not independent third-party
  verification of how Private Safety Processing actually behaves in
  production (it is explicitly still in early-customer testing, not GA).
- **Scope**: Covers what ZDR promises today (no prompt/response retention
  after processing, no personnel review of customer content, no training
  use without opt-in), why OpenAI says single-interaction safety evaluation
  is insufficient for longer/more-complex agentic tasks, the two-part
  mechanism of Private Safety Processing (encrypted-content pattern
  detection + narrow signal-only alerts), the two storage models it
  supports (customer-controlled infrastructure vs. OpenAI-provided
  storage encrypted with customer-controlled keys), the customer
  investigation/appeal path, four customer endorsement quotes, and a
  September 2026 rollout/white-paper commitment. Does NOT cover: a
  definition of what makes an API customer "eligible" for ZDR, any
  technical detail of the pattern-detection algorithm or model used to
  generate "narrow signals," a false-positive/false-negative rate for the
  signal system, pricing or contractual terms, which specific frontier
  models (GPT-5.6 family, etc.) this applies to, or any named case in which
  Private Safety Processing actually caught or missed a real misuse
  pattern during its early-customer testing period.

## Extracted Claims

### Claim 1: Zero Data Retention gives eligible API customers a guarantee that OpenAI does not retain prompts or model responses after a request is processed, that customer content is not available to OpenAI personnel for review, and that enterprise customer data is not used for model training unless the customer explicitly opts in
- **Evidence**: The article's opening definitional statement of what ZDR currently provides.
- **Confidence**: settled (a specific, checkable vendor policy statement, though "eligible" is left undefined in this source — see Extraction Notes)
- **Quote**: "Zero Data Retention gives eligible API customers a clear promise: OpenAI does not retain their prompts or model responses after a request is processed. Customer content is not available to OpenAI personnel for review, and enterprise customer data is not used to train our models unless customers explicitly opt-in."
- **Our assessment**: This is a reaffirmation, not a new policy — the article's own framing ("reaffirms Zero Data Retention") and its structure (one paragraph restating ZDR, followed by a much longer section previewing Private Safety Processing) indicate ZDR itself already existed; the news content of this post is the new safety-monitoring mechanism, not the retention guarantee. This directly parallels `blog-anthropic-legal-industry-deploy.md` Claim 14 (Anthropic's ZDR is available on the Platform API and Claude Code but explicitly NOT on Claude.ai or Cowork) in naming ZDR as a scoped, product-specific guarantee rather than a blanket company policy — this OpenAI post similarly scopes ZDR to "eligible API customers" without stating which products or plans qualify.

### Claim 2: The most serious AI safety risks are not always visible in a single interaction — potentially harmful intentions often become clear only when multiple interactions are viewed together, including bad actors repeatedly probing safeguards, coordinating across accounts, disguising threats as routine research, or an agentic task drifting out of alignment with user intent by continuing to act after being told to stop
- **Evidence**: The article's stated rationale for why existing ZDR-compatible safety systems (which evaluate each interaction individually) are insufficient going forward.
- **Confidence**: anecdotal (a stated threat model and design rationale, not a measured finding — no data is given on how often single-interaction evaluation actually misses a risk that multi-interaction evaluation would catch)
- **Quote**: "The most serious AI safety risks are not always visible in a single interaction. Often, potentially harmful intentions become clear only when multiple interactions are viewed together. Similar risks can arise when bad actors repeatedly probe safeguards, coordinate across accounts, or disguise threats as routine research. Risks can also develop over the course of an agentic task—for example, if a system becomes misaligned with the user's intent by continuing to act after being told to stop."
- **Our assessment**: The "agent continues acting after being told to stop" example is a concrete, specific instance of the agentic-misalignment risk category — directly relevant to any guide discussion of agent stop-conditions and runaway-task risk (adjacent to `blog-openai-managing-ai-investments-agentic-era.md` Claim 9's "explicit stopping conditions... reduce loops," though that claim is about cost/waste, not safety). This is OpenAI's own stated justification for why it is building cross-interaction safety infrastructure rather than staying with per-interaction evaluation.

### Claim 3: Some recent frontier-model deployments have required customers to allow their AI provider to retain sensitive content for safety monitoring, and for many organizations such requirements conflict with their security obligations or commitments to the people they serve
- **Evidence**: A direct statement in the "Why safety systems need to evolve" section, positioned immediately before the article states "Private Safety Processing is designed so we can continue to offer ZDR."
- **Confidence**: anecdotal (no named competitor, no citation, no data on how many organizations were affected or declined a deployment over this requirement)
- **Quote**: "Some recent frontier-model deployments have required customers to allow their AI provider to retain sensitive content for safety monitoring. For many organizations, such requirements conflict with their security obligations or commitments to the people they serve."
- **Our assessment**: No competitor is named, but this reads as a direct, if unattributed, response to exactly the kind of mandatory-retention-for-safety requirement documented in `blog-latentspace-fable-5-mythos-launch.md` Claim 5 — Anthropic's own June 2026 announcement that it "will require 30-day retention for all traffic on Mythos-class models" for safety purposes, not training. This is not a formal MINER.md §4a contradiction (OpenAI does not name Anthropic, and the two posts are not making opposing factual claims about the same fact — one states a policy for a named model tier, the other states a general architectural design goal), but the juxtaposition is worth flagging prominently: OpenAI is implicitly positioning Private Safety Processing as solving the exact problem Anthropic's Mythos-class retention requirement represents, without going so far as to name Anthropic or provide evidence that its own new system achieves comparable safety coverage.

### Claim 4: Private Safety Processing extends automated, ZDR-compatible safety evaluation from per-interaction analysis to analysis across related interactions, and is designed so OpenAI can continue offering ZDR while gaining that broader detection capability
- **Evidence**: Direct architectural framing statement, the article's core new-feature claim.
- **Confidence**: emerging (a specific, named mechanism with a described design goal, currently in early-customer testing rather than GA — no performance data on detection accuracy is given)
- **Quote**: "Private Safety Processing builds on the automated protections already used in ZDR and other deployments. Existing ZDR-compatible safety systems evaluate interactions individually. Private Safety Processing extends those protections across related interactions, allowing automated systems to identify patterns without OpenAI personnel having access to retained customer content."
- **Our assessment**: This is the article's headline technical claim and the one the Prospector's triage question targets most directly. It names a specific architectural tradeoff — retain the "no human ever sees raw content" guarantee of ZDR while adding cross-session pattern detection — that no existing corpus source describes for any vendor. It should be read as a preview-stage design goal, not a shipped, audited capability: the article itself says it is "currently being tested with early customers," with full rollout and a technical white paper not promised until September 2026.

### Claim 5: Private Safety Processing works over customer content regardless of where it is stored — either on infrastructure the customer controls (ZDR deployments) or in OpenAI-provided storage encrypted with keys controlled by the customer, where OpenAI personnel do not have a copy of the encryption keys and therefore cannot access the underlying content
- **Evidence**: Direct mechanism description in the "How Private Safety Processing works" section.
- **Confidence**: emerging (a specific, named technical architecture — customer-held encryption keys as the access-control mechanism — described by the vendor but not independently verified or audited in this source)
- **Quote**: "Private Safety Processing utilizes customer content regardless of where it is stored—whether in infrastructure customers control (ZDR deployments) or in storage provided by OpenAI. With OpenAI-provided storage, customer content is encrypted using keys controlled by the customer. OpenAI personnel do not have a copy of those keys, so they cannot access the underlying content."
- **Our assessment**: "OpenAI personnel do not have a copy of those keys" is a specific, falsifiable technical claim (as opposed to a policy promise not to look) — if true, it is a stronger guarantee than a purely procedural "we promise not to access this" policy, since it removes technical capability rather than relying on internal access controls alone. The source gives no detail on key management, rotation, or what happens if a customer loses their key, so this should be treated as a described design intent pending the promised September white paper.

### Claim 6: When Private Safety Processing identifies a risk, OpenAI receives only a narrowly defined signal indicating the type of activity involved — not the underlying content — and that signal is used to determine whether enforcement is necessary; OpenAI personnel do not receive access to the flagged content even when an alert fires
- **Evidence**: Direct description of the alert/enforcement mechanism, following the storage-architecture description in Claim 5.
- **Confidence**: emerging (a specific claim about what information does and does not reach human reviewers; no example of an actual signal or enforcement action is given)
- **Quote**: "When a risk is identified, OpenAI receives a narrowly defined signal indicating the type of activity involved, similar to our existing safety systems today. That signal can be used to determine whether enforcement is necessary. OpenAI personnel do not receive access to the customer content even when it is flagged."
- **Our assessment**: This directly addresses the exact tension JetBrains' CTO described accepting in `blog-anthropic-jetbrains-fable5-evaluation-deployment.md` Claim 8 — JetBrains told Anthropic "I don't see any other way for you to understand what was asked and where a classifier may have worked incorrectly," accepting limited data retention on the condition that human review stays scoped to "the most serious cases flagged." OpenAI's claim here is that its own architecture avoids that tradeoff entirely: enforcement decisions are made from a signal alone, with no human review of the underlying flagged content at all — a stronger (if here still preview-stage and unaudited) version of the "flagged-case-only" limited-review compromise JetBrains described accepting from Anthropic.

### Claim 7: Customers can investigate Private Safety Processing alerts and enforcement decisions using information available in their own systems, and if they want to appeal, clarify legitimate activity, or support an investigation into verified abuse, they can choose to voluntarily share relevant information with OpenAI
- **Evidence**: Direct description of the customer-side recourse path, immediately following the enforcement-signal mechanism in Claim 6.
- **Confidence**: settled (a described, specific product/process commitment, though not yet independently tested since the system is still preview-stage)
- **Quote**: "Customers can investigate alerts and enforcement decisions using information available in their own systems. If they want to appeal, clarify legitimate activity, or support an investigation into verified abuse, they can choose to share relevant information with OpenAI."
- **Our assessment**: This makes information-sharing with OpenAI opt-in and customer-initiated rather than automatic — the default state after an enforcement action is that OpenAI still has no access to the underlying content; the customer must actively choose to disclose it to appeal. This is a meaningful design detail for any guide discussion of enterprise-side incident response when a ZDR-style vendor flags suspected misuse: the customer, not the vendor, holds the content needed to investigate a false positive.

### Claim 8: Like other frontier model providers, OpenAI is legally required to report apparent child sexual abuse material (CSAM), and images flagged for potential CSAM continue to be retained for manual review and reporting even in Zero Data Retention deployments, unchanged from current practice
- **Evidence**: A footnote attached to the ZDR promise in Claim 1, disclosing a specific carve-out to the "no retention" guarantee.
- **Confidence**: settled (a specific, legally grounded exception, explicitly scoped and disclosed by the vendor)
- **Quote**: "Like other frontier model providers, OpenAI is required by law to report apparent child sexual abuse material (CSAM). Images flagged for potential CSAM will continue to be retained for manual review and reporting purposes, even in Zero Data Retention deployments, as they are today."
- **Our assessment**: This is the one unambiguous, legally-mandated exception to the ZDR promise disclosed in this source — practitioners evaluating ZDR for a compliance-sensitive image-handling workflow should not read "Zero Data Retention" as an absolute guarantee without this carve-out. No existing corpus source documents this specific CSAM-reporting exception for any vendor's ZDR offering; it is a concrete, novel scope boundary worth citing wherever the guide discusses what ZDR actually covers.

### Claim 9: Private Safety Processing is currently being tested with early customers, not yet generally available; OpenAI plans to begin rolling it out and to share a technical white paper in September 2026, and states it will keep customers informed throughout the process
- **Evidence**: Direct, dated commitment in the article's closing paragraph.
- **Confidence**: settled (a specific, dated, checkable forward-looking commitment from the vendor, though it is a promise about future disclosure, not yet-delivered technical detail)
- **Quote**: "Private Safety Processing is currently being tested with early customers. We are sharing this preview now because we've heard our customers loud and clear that they need predictability about how their content will be protected as AI systems become more capable." ... "We plan to start rolling out Private Safety Processing, and share a technical white paper, in September. We'll keep customers informed every step of the way, sharing updates early, explaining what they mean for existing commitments, and providing the time and support customers need to plan ahead."
- **Our assessment**: Every mechanism claim in this note (Claims 4–7) should be read through this dating: as of the August 19, 2026 publication date, Private Safety Processing is an announced design and early-customer pilot, not an audited, generally available system. The promised September 2026 technical white paper is the artifact that would let a practitioner or the Assayer actually verify the encryption/signal-extraction mechanics described in Claims 5–6 rather than taking the vendor's architectural description on faith.

### Claim 10: Four named enterprise security/product executives — from Glean, Databricks, Abridge, and Microsoft — publicly endorse OpenAI's ZDR/no-training commitments and its collaborative approach to shaping Private Safety Processing, citing regulatory obligations, customer trust, and competitive advantage as reasons data control matters to their organizations
- **Evidence**: Four named, titled customer-testimonial quotes in a carousel section titled "Privacy and safety built with and for our customers."
- **Confidence**: anecdotal (OpenAI-selected, OpenAI-published endorsements; no customer describes actually using Private Safety Processing in production or reports a measured outcome from it — the quotes praise OpenAI's process/collaboration and general ZDR/no-training posture, not a tested result)
- **Quote (Glean)**: "Enterprise AI adoption depends solely on customer control of data, with no direct or derivative use beyond the chosen service. OpenAI's no-training commitment and ZDR give Glean confidence to build with OpenAI. As models become more capable, OpenAI shows safety can advance without compromising the privacy and control that sustain enterprise trust." — Sunil Agrawal, Chief Information Security Officer, Glean
- **Quote (Databricks)**: "Our customers rely on Databricks to access powerful AI models within the data and governance environment they already trust. OpenAI's continued support for Zero Data Retention and their collaborative approach to AI safety help us make their increasingly capable models available while preserving the privacy protections our customers expect. We appreciate the opportunity to help shape safeguards that respect how enterprises actually deploy AI." — Hanlin Tang, CTO of Neural Networks, Databricks
- **Quote (Abridge)**: "In healthcare, protecting massive amounts of sensitive data and ensuring its accuracy and integrity are fundamental to earning the trust of clinicians and patients. Having the chance to work directly with OpenAI's product, engineering, policy, and leadership teams to help shape those practices has made for an unparalleled partnership. That level of collaboration on trust and security is uncommon. They listen, they take action, and that gives us confidence in OpenAI. That level of partnership on trust and security is just not common." — Zach Powers, Chief Information Security Officer, Abridge
- **Quote (Microsoft)**: "Privacy and safety are both essential to enterprise AI adoption and balancing them is a significant challenge. At Microsoft and GitHub, we've been working through many of these same issues ourselves, and we appreciate OpenAI's approach to helping organizations maintain control of their data while preserving important security protections." — Sarah Bird, Chief Product Officer of Responsible AI, Microsoft
- **Our assessment**: The Microsoft quote is notable in that Microsoft is simultaneously a major OpenAI investor/infrastructure partner and, via GitHub Copilot, a distributor of Anthropic models (Claude Sonnet 5 operates under ZDR in Copilot per `docs-github-copilot-sonnet5-ga.md` Claim 9) — Sarah Bird's framing that "we've been working through many of these same issues ourselves" reads as a vendor-agnostic statement about the general privacy/safety tradeoff Microsoft manages across both AI providers it ships, not an exclusive OpenAI endorsement. None of the four quotes describes a concrete before/after outcome from Private Safety Processing specifically (unsurprising, since it is still in early testing) — they endorse OpenAI's general ZDR/no-training posture and its process of soliciting customer input while shaping the new system.

## Concrete Artifacts

### Private Safety Processing architecture, as described (verbatim structure)

```
Source: OpenAI, "Offering Zero Data Retention for frontier models,"
https://openai.com/index/offering-zero-data-retention-for-frontier-models
(August 19, 2026)

Existing ZDR-compatible safety systems:
  -> evaluate each interaction individually
  -> no cross-interaction pattern detection

Private Safety Processing (preview, testing with early customers):
  -> extends automated protections across RELATED interactions
  -> works over customer content wherever stored:
       (a) customer-controlled infrastructure (ZDR deployments), OR
       (b) OpenAI-provided storage, encrypted with customer-controlled
           keys (OpenAI personnel hold no copy of the keys)
  -> on risk detection: OpenAI receives a narrowly defined SIGNAL
     (activity type only) -- not the underlying content
  -> signal used to decide whether enforcement is necessary
  -> OpenAI personnel never see flagged content, even post-alert
  -> customer can investigate using their own systems; may VOLUNTARILY
     share content with OpenAI to appeal/clarify/support an abuse
     investigation

Rollout commitment: begins + technical white paper, September 2026
```

### ZDR/CSAM exception (footnote, verbatim)

```
"Like other frontier model providers, OpenAI is required by law to report
apparent child sexual abuse material (CSAM). Images flagged for potential
CSAM will continue to be retained for manual review and reporting
purposes, even in Zero Data Retention deployments, as they are today."

Source: https://openai.com/index/offering-zero-data-retention-for-frontier-models
(footnote 1)
```

## Cross-References

### Cross-reference verification notes
`blog-anthropic-jetbrains-fable5-evaluation-deployment.md`,
`blog-latentspace-fable-5-mythos-launch.md`,
`blog-anthropic-legal-industry-deploy.md`,
`blog-anthropic-claude-code-self-hosted-environments.md`,
`blog-openai-managing-ai-investments-agentic-era.md`,
`blog-openai-gpt56-ga-announcement.md`, and
`docs-github-copilot-sonnet5-ga.md` were re-read directly (MINER.md §4b)
and the claim numbers cited above were confirmed against each note's
numbered `### Claim N:` headings in document order before writing this
section.

- **Corroborates**:
  - `blog-anthropic-legal-industry-deploy.md` Claim 14 (Anthropic's ZDR is
    available on Claude Platform API and Claude Code, but explicitly NOT
    on Claude.ai or Cowork): this source's Claim 1 similarly scopes ZDR to
    "eligible API customers" without stating which OpenAI products or
    plans qualify — both vendors treat ZDR as a scoped, product-specific
    guarantee rather than a blanket company policy, though neither source
    gives a full eligibility matrix.
  - `blog-openai-gpt56-ga-announcement.md` Claim 3 (Programmatic Tool
    Calling is "Zero Data Retention (ZDR) compatible") and
    `blog-openai-managing-ai-investments-agentic-era.md` Claim 6 (a bare
    pointer to "Zero Data Retention options" as part of OpenAI's
    enterprise privacy controls): both prior OpenAI sources mention ZDR as
    an existing capability without describing its mechanics; this source
    is the first in the corpus to actually define what the ZDR promise
    covers (Claim 1) and to disclose its one legally-mandated exception
    (Claim 8, CSAM).

- **Contradicts**: None filed as a formal MINER.md §4a contradiction. One
  substantive tension is flagged instead, per the precedent set in
  `blog-openai-managing-ai-investments-agentic-era.md`'s Cross-References
  for non-opposing-but-tension-worthy claims: this source's Claim 3
  ("some recent frontier-model deployments have required customers to
  allow retention for safety monitoring," positioned as the problem
  Private Safety Processing solves) sits opposite
  `blog-latentspace-fable-5-mythos-launch.md` Claim 5 (Anthropic requiring
  30-day retention for all Mythos-class model traffic, explicitly for
  safety purposes). OpenAI does not name Anthropic, and the two sources
  are not making opposing claims about the same fact — one states a
  policy for a specific named model tier (Anthropic, Mythos-class,
  mandatory), the other states a general, unaudited architectural design
  goal still in early-customer testing (OpenAI, Private Safety
  Processing). No contradiction issue filed, but the guide should present
  this as two different vendors making two different bets on whether
  robust cross-interaction safety monitoring requires data retention,
  rather than treating either claim as settled.

- **Extends**:
  - `blog-anthropic-jetbrains-fable5-evaluation-deployment.md` Claim 8
    (JetBrains: "We'd prefer zero data retention. But I don't see any
    other way for you to understand what was asked and where a classifier
    may have worked incorrectly. As long as reviews are only to
    investigate the most serious cases flagged, I'm okay with it."): this
    source's Claims 4–6 describe an architecture explicitly designed to
    eliminate the exact tradeoff JetBrains described accepting — instead
    of scoping human review to "the most serious flagged cases," OpenAI
    claims its personnel never see flagged content at all, working only
    from a narrow activity-type signal. This is the strongest single
    cross-reference in this note: a named customer's stated compromise
    with one vendor (Anthropic) is directly answered, in architecture if
    not yet in independently-verified practice, by a different vendor's
    (OpenAI) new preview feature.
  - `blog-anthropic-claude-code-self-hosted-environments.md` Claim 7
    (Anthropic: self-hosted environments and Zero Data Retention are
    mutually exclusive, because self-hosting still requires Anthropic to
    process and store session transcripts for cross-surface resume): this
    is a second, independent example of a vendor stating that some
    capability (there: session resume; here: cross-interaction safety
    monitoring) is in tension with a strict no-retention guarantee. This
    source's Private Safety Processing is presented as OpenAI's attempt to
    resolve that exact category of tension (retain the capability, keep
    the ZDR guarantee) via encryption and signal-only alerting rather than
    accepting the trade-off Anthropic's self-hosted product accepts.
  - `docs-github-copilot-sonnet5-ga.md` Claim 9 (Claude Sonnet 5 operates
    under ZDR within GitHub Copilot): gives independent, third-party
    (Microsoft/GitHub) confirmation that ZDR-style guarantees are already
    a live purchasing consideration for enterprise coding-tool deployments
    — relevant context for why Microsoft's CPO of Responsible AI (Claim
    10 of this note) is quoted endorsing a second frontier-model vendor's
    ZDR/safety approach on the same general topic.

- **Novel**:
  - **Private Safety Processing itself** (Claims 4–7): no existing corpus
    source describes a mechanism for cross-interaction misuse detection
    that operates on encrypted content via customer-held keys and returns
    only narrow, content-free signals. This is the first documented
    attempt in the corpus at technically reconciling "zero retention" with
    "multi-interaction safety visibility" rather than choosing one over
    the other.
  - **The CSAM-reporting carve-out to ZDR** (Claim 8): the first corpus
    source to disclose a specific, legally-mandated exception to any
    vendor's zero-retention guarantee.
  - **"Agentic task drifting from user intent by continuing to act after
    being told to stop" as a named safety-risk category** (Claim 2): a
    specific, concrete framing of runaway-agent risk tied directly to a
    vendor's stated rationale for building new safety infrastructure, not
    previously framed this way in the corpus's existing agent-safety
    material.
  - **Customer-controlled encryption keys as the access-control mechanism
    for vendor-side safety processing** (Claim 5): a specific technical
    design (key custody, not just a policy promise) not previously
    documented in the corpus for any vendor's data-handling architecture.

## Guide Impact

- **Chapter 06 (Security & Threat Model)**: Add Claims 4–7 (Private Safety
  Processing's encrypted-content-plus-narrow-signal architecture) as a
  concrete, named example of a vendor attempting to reconcile zero data
  retention with cross-interaction misuse detection — cite alongside
  `blog-anthropic-jetbrains-fable5-evaluation-deployment.md` Claim 8 to
  show a customer's stated compromise with one vendor being directly
  answered (architecturally, though not yet independently verified) by a
  different vendor's new preview feature. Flag explicitly that this is a
  preview-stage, early-customer-testing capability as of August 2026, not
  an audited or GA system — the promised September 2026 white paper is the
  artifact to watch for independent verification.
- **Chapter 06 (Security & Threat Model — Compliance Scoping)**: Add
  Claim 8 (the CSAM-reporting exception to ZDR) as a concrete example that
  "Zero Data Retention" is not an absolute guarantee even when a vendor
  states it as one — any guide checklist for evaluating a vendor's ZDR
  claim should include "what legally-mandated exceptions exist" as a
  question to ask, since this is the first corpus source to name one
  specifically.
  Add Claim 1's "eligible API customers" framing as a scope gap to flag
  — practitioners should confirm exactly which product/plan combinations
  qualify for ZDR before assuming it applies uniformly, mirroring the
  guidance already recommended for Anthropic's ZDR scoping in
  `blog-anthropic-legal-industry-deploy.md` Claim 14's Guide Impact.
- **Chapter 04 (Context Engineering / Agent Stop Conditions)**: Add
  Claim 2's specific example of agentic-misalignment risk ("a system
  becomes misaligned with the user's intent by continuing to act after
  being told to stop") as a named vendor-stated risk category worth
  citing wherever the guide discusses explicit stopping conditions or
  runaway-agent safeguards.
- **Chapter 05 (Team Adoption / Vendor Evaluation)**: When comparing
  vendor data-retention postures for a compliance-sensitive deployment
  decision, present this source's Claim 3/Cross-References tension
  alongside `blog-latentspace-fable-5-mythos-launch.md` Claim 5 as two
  different vendor bets on the same underlying question (does robust
  safety monitoring require data retention) — do not present either as
  settled; OpenAI's alternative is unaudited and preview-stage, while
  Anthropic's mandatory retention is a shipped, GA policy for a named
  model tier.

## Extraction Notes

1. **Live URL returned HTTP 403** (`https://openai.com/index/offering-zero-data-retention-for-frontier-models`,
   confirmed via both `WebFetch`-style access and a direct `curl` with a
   standard browser user-agent, `cf-mitigated: challenge` header present)
   — the same Cloudflare bot-challenge pattern already documented for
   `openai.com/index/` posts in multiple prior source notes in this corpus
   (e.g. `blog-openai-managing-ai-investments-agentic-era.md`,
   `blog-openai-gpt56-ga-announcement.md`,
   `blog-openai-asana-codex-case-study.md`). Retrieved instead via the
   Internet Archive Wayback Machine snapshot dated 2026-08-22
   (`web.archive.org/web/20260822115111/https://openai.com/index/offering-zero-data-retention-for-frontier-models/`,
   three days after the August 19 publication date, HTTP 200 via direct
   `curl`).
2. **Two-pass extraction to recover the full customer-testimonial
   carousel**: the archived page's rendered `<article>`/`<main>` HTML,
   stripped of scripts/styles/tags and linearized, surfaced only one of
   the four customer quotes (Glean/Sunil Agrawal) plus a bare row of four
   company logos ("GleanDatabricksAbridgeMicrosoft") with no accompanying
   text — the other three testimonials are rendered client-side from a
   JSON payload embedded in a `<script>` tag (a Next.js RSC data blob)
   that the linearized-tag-stripping pass discarded along with all other
   script content. A second pass searched the raw, un-stripped archived
   HTML directly for quoted string literals (`\"..."\"` patterns) and
   recovered the Databricks, Abridge, and Microsoft quotes verbatim from
   that embedded JSON, matching them against the visible logo row. All
   four quotes in Claim 10 were verified character-for-character against
   this raw-HTML string-literal source, not against any AI-summarized or
   paraphrased rendering.
3. **Two link-affordance/markup artifacts were elided as formatting
   noise, consistent with precedent in
   `blog-openai-managing-ai-investments-agentic-era.md`'s Extraction
   Notes**: (a) the footnote-1 CSAM text as embedded in the raw HTML
   included a trailing, unrelated CSS-class/SVG-icon fragment
   immediately after the sentence ("...as they are today.svg]:opacity-60
   ms-[10px] scale-inline-100\" href=\"#citation-top-1\">...") — this is
   rendering markup for a footnote-anchor icon, not body prose, and was
   excluded from the quoted text in Claim 8; (b) the literal
   "(opens in a new window)" accessibility text attached to the CSAM
   footnote's outbound link to the US Code was elided as link-affordance
   markup, not body prose. Neither elision changes the meaning of the
   quoted passage.
4. **No sub-pages followed.** The article's "Keep reading" footer links to
   three unrelated OpenAI posts ("ChatGPT Ads expands across Europe,"
   "Partnering with CodeAI to prepare the first AI generation," "Pacing
   model development in an era of cyber-critical capabilities"), none of
   which concern ZDR or Private Safety Processing, and were not followed.
   The CSAM footnote's outbound link (to 18 U.S.C. § 2258A on
   uscode.house.gov) is a legal-citation link, not a substantive
   OpenAI-authored page, and was not followed as a separate source.
5. **No independent verification of the encryption/signal-detection
   architecture is possible from this source alone.** Claims 4–7 describe
   a system still in early-customer testing; the promised September 2026
   technical white paper (Claim 9) is the artifact that would allow
   independent assessment of whether the "OpenAI personnel cannot access
   the underlying content" and "narrowly defined signal" claims hold up
   to scrutiny. This note should be revisited (`last_checked` updated, and
   a new source note opened) once that white paper or the GA rollout
   itself is published.
6. **Confidence calibration: anecdotal (overall).** While several
   individual claims are rated settled (Claim 1's ZDR definition, Claim 8's
   CSAM carve-out, and Claim 9's dated rollout commitment are unambiguous
   vendor policy/commitment statements), the article's central new-content
   claim — that Private Safety Processing actually achieves
   content-invisible cross-interaction misuse detection in practice — is
   an unaudited, preview-stage design description with no performance
   data, no named early-customer account of it working, and no
   independent technical review. The four customer testimonials (Claim 10)
   endorse OpenAI's general posture and collaborative process, not a
   tested outcome from the new system specifically. The overall "anecdotal"
   rating reflects that this source's primary news content — the new
   safety mechanism — is not yet independently verifiable, even though
   several surrounding policy facts are settled.
7. **No contradiction issue filed.** The tension between this source's
   Claim 3 and `blog-latentspace-fable-5-mythos-launch.md` Claim 5 was
   considered per MINER.md §4a but does not rise to a formal contradiction
   — see Cross-References → Contradicts for the full reasoning. The
   Assayer or Smith may weigh in if they read this differently, especially
   once the September 2026 white paper allows a more concrete comparison
   of the two vendors' actual safety-monitoring coverage.
