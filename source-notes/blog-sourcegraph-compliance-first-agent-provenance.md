---
source_url: https://sourcegraph.com/blog/compliance-first-ai-proving-agent-provenance
source_type: blog-post
title: "Compliance-first AI: Proving Agent Provenance for Regulated Engineering Teams"
author: Justin Dorfman (Sourcegraph); six additional Sourcegraph staff credited as contributors in the post footer
date_published: 2026-07-27
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: emerging
issue: "#2355"
---

# Compliance-first AI: Proving Agent Provenance for Regulated Engineering Teams

> Sourcegraph vendor blog post arguing that the real blocker to agentic AI adoption in
> regulated engineering teams isn't model capability but "agent provenance" — the
> missing record of which files an agent read and why before it changed anything — and
> proposing scoped, citation-backed retrieval (via Sourcegraph Deep Search and its MCP
> server) as the mechanism that turns agent context into an exportable audit trail.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published July 27, 2026;
  auto-discovered via the `sourcegraph` trusted feed). Argumentative/explainer piece:
  opens with a CISO/CTO framing question, develops the "agent provenance" concept
  across three sections, then walks through Sourcegraph Deep Search and its MCP server
  as the proposed implementation, closes with a compliance-category FAQ block (Change
  Management, GDPR/CCPA, SOC 2/ISO 27001, PCI-DSS, SOX, HIPAA) and a "Schedule a demo"
  call-to-action.
- **Author credibility**: Bylined **Justin Dorfman (Sourcegraph)** directly beneath the
  title and publish date. Six further Sourcegraph staff are credited separately in a
  footer note — "A special thanks to André Eleuterio, Dora Neumeier, Jamie Lindsay,
  Makenna Freauf, Matt Tanner, and Stephanie Jarmak for their contributions to this blog
  post" — as contributors, not co-authors. This is Dorfman's **second** post in the
  corpus; he is also the author of `blog-sourcegraph-dorfman-repo-security-posture.md`
  (published 2026-07-10). That matters when weighing how much independent vendor
  perspective Sourcegraph's corpus entries represent: two of the three Sourcegraph notes
  are the same author's recurring voice, and both advance a closely related thesis
  (org-wide, queryable code visibility as the load-bearing security/compliance control)
  toward the same product line. Treat the two Dorfman notes as one vendor argument
  developed across two posts, not as two independent corroborating vendor sources.
  This is company content advancing Sourcegraph's own commercial product (Deep Search,
  the Sourcegraph MCP server) as the solution to the problem it names. The central claim — that engineering
  and security leaders across banking, healthcare, and large software organizations cite
  "proof," not model capability, as the adoption blocker — is attributed to
  Sourcegraph's own customer conversations, not to any named survey, study, or
  third-party report. Treat as informed vendor commentary with a direct commercial
  interest in the conclusion, not independently verified industry research.
- **Scope**: Covers the conceptual argument for "agent provenance" as a compliance
  requirement, the auditing rationale (accuracy/completeness assertions applied to
  agent retrieval), a description of Sourcegraph Deep Search's citation-backed output
  and the Sourcegraph MCP server's discrete-operation design, and a list of
  regulation-specific example questions (SOC 2, ISO 27001, PCI-DSS, GDPR, SOX, HIPAA)
  the product is positioned to answer. Does NOT cover: any named customer case study
  with before/after audit-time metrics, Deep Search's or the MCP server's technical
  implementation details, independent verification of the claimed customer sentiment,
  or a comparison against competing code-intelligence/audit tooling.

## Extracted Claims

### Claim 1: The primary blocker to agentic AI adoption cited by engineering and security leaders in banking, healthcare, and large software organizations is proof, not model capability — the ability to verify an agent looked at the right things before it acted, and to demonstrate that after the fact
- **Evidence**: Stated as the article's opening framing, attributed to Sourcegraph's own conversations with executives across these sectors, not to a named survey.
- **Confidence**: anecdotal (vendor's characterization of unnamed customer conversations; no survey methodology, sample size, or named sources given)
- **Quote**: "We talk to engineering and security leaders across banking, healthcare, and large software organizations and the hesitation about agentic development rarely comes down to model capability. What we are told is it comes down to proof."
- **Our assessment**: This reframes the enterprise adoption barrier away from the "is the model good enough" question that dominates most of the corpus and toward a verification/evidentiary question. It is plausible and consistent with regulated-industry compliance culture generally, but it is a vendor's secondhand paraphrase of unnamed conversations, not a citable data point — should be presented in the guide as a framing claim, not a measured finding.

### Claim 2: A clean audit trail of an agent's reasoning is not sufficient on its own — an agent can document its reasoning perfectly and still patch the symptom instead of the root cause; what has to be verifiable is that the agent had the right context before it acted
- **Evidence**: Stated directly in the article's opening paragraph as a qualification on the "proof" framing in Claim 1.
- **Confidence**: anecdotal (the author's own conceptual distinction, not backed by a named incident or study)
- **Quote**: "A clean audit trail still isn't enough: an agent can document its reasoning perfectly and still patch the symptom instead of the vulnerability. What matters is that it had the right context before it acted, and that you can verify it did."
- **Our assessment**: This is a sharper and more specific claim than a generic "log everything" recommendation — it draws a line between explanation (an agent narrating its reasoning after the fact) and provenance (evidence of what informed the decision before the fact). For a guide chapter on agent audit trails, this distinction is worth preserving explicitly: a well-written post-hoc justification is not the same evidence as a record of what was actually consulted.

### Claim 3: With AI agents, the audit "process" that determines whether accuracy and completeness assertions can be trusted is the retrieval step itself — a transparent record of exactly which files an agent read, and why, lets an auditor reverse-engineer the agent's logic and confirm both assertions
- **Evidence**: Stated as the article's core auditing-theory argument, explicitly naming the "accuracy" and "completeness" management assertions as the foundational concepts being applied.
- **Confidence**: emerging (a specific, structured argument connecting standard audit theory — management assertions — to agent retrieval mechanics; the audit-theory framing itself is a settled external concept, but its application to agent retrieval is this article's own synthesis, not independently corroborated)
- **Quote**: "In auditing, two foundational management assertions, accuracy and completeness, determine whether you can rely on evidence at all, and they're verified by stress-testing the process behind it. With AI agents, the process is the retrieval. A transparent record of exactly which files an agent read, and why, lets an auditor reverse-engineer the agent's logic and confirm both assertions: the agent acted on the complete set of requirements, using only relevant, authorized code context."
- **Our assessment**: This is the article's most technically substantive claim and the clearest candidate for direct guide citation — it gives a specific mechanism (retrieval-as-the-auditable-process) rather than a vague call for "more logging." It reframes retrieval scoping from a quality/cost concern (as it's typically discussed in the corpus's context-engineering material) into a compliance control with a named theoretical grounding.

### Claim 4: When a human engineer ships a change, the PR record (diff, approvals, review comments, CI checks) is normally sufficient for audit purposes, and deeper file-level scrutiny is reserved for high-blast-radius artifacts; nobody expects a list of every file a human read
- **Evidence**: Stated as a direct comparison point, specifically referencing SOC 2 review practice.
- **Confidence**: anecdotal (a generalization about typical SOC 2 audit practice, not cited to a specific audit standard document or named auditor)
- **Quote**: "In a SOC 2 review, auditors may pull individual PRs to confirm the promised scans and approvals actually ran, and deeper, file-level scrutiny tends to be reserved for high-blast-radius artifacts like the Terraform applied to customer environments."
- **Our assessment**: This establishes the baseline the article contrasts agents against — the claim is that the human audit bar is already low (PR record suffices; nobody logs every file a person reads) precisely because there's a person to ask follow-up questions of later. This is useful context for readers who might otherwise assume agents need to clear some new, unusually strict compliance bar; the article's actual point is closer to "an agent has to meet the standard humans already meet, but can't rely on the same shortcut (asking the engineer)."

### Claim 5: The provenance gap opens specifically because there is no one to ask why an agent made a change the way it did — the context that informed an agent's decision disappears at the end of the session unless it is deliberately captured, and reconstructing it after the fact is largely manual for most teams today
- **Evidence**: Stated as the article's central definition of "agent provenance," directly following the human-engineer PR-record comparison (Claim 4).
- **Confidence**: anecdotal (a definitional/conceptual claim, not backed by a named case study of a specific reconstruction effort or its cost)
- **Quote**: "The gap appears when the 'engineer' is an agent. The PR still shows the diff and the approval, but there's no one to ask why the change was made the way it was. ... That missing record is agent provenance: the evidence of which files an agent read, and why, before it changed anything. That gap, more than any model limitation, is what keeps AI from scaling in regulated environments."
- **Our assessment**: This is the article's defining term and its headline claim ("more than any model limitation"). It is a strong, falsifiable framing — but it is asserted, not measured; no comparison is offered against how much model-capability limitations vs. this provenance gap actually block adoption in practice. Worth citing as the article's thesis while flagging that it is a vendor's own diagnostic claim about the market it sells into.

### Claim 6: Model context access (via MCP and agentic tooling) solved the capability problem, but made a different problem visible — getting an agent to act accountably, not just to act, is now the harder engineering problem
- **Evidence**: Stated as the article's historical framing under "Capability Was Never the Hard Part," contrasting early autocomplete-style assistants against MCP-enabled agentic tooling.
- **Confidence**: emerging (a historical narrative claim about the sequencing of the field's problems; broadly consistent with the corpus's general MCP/agentic-tooling adoption narrative, though not independently cited to external sources)
- **Quote**: "That's what made agentic coding practical. It also made one thing very clear: getting an agent to act is increasingly easy. Getting it to act accountably is much harder."
- **Our assessment**: This is a clean, quotable line that reframes MCP's contribution — not as solving the accountability problem, but as removing the capability constraint that had been masking it. Consistent with the corpus's broader theme that harness/governance concerns emerged only once raw agent capability stopped being the bottleneck.

### Claim 7: An agent that retrieves broadly — pulling in whole repositories, guessing at context, hallucinating when it can't find what it needs — produces output that cannot be vouched for, and "the model decided" is not an answer that survives a compliance review of a security-critical change
- **Evidence**: Stated as the article's direct consequence of the capability/accountability distinction (Claim 6), specifically in the context of security-critical changes.
- **Confidence**: anecdotal (an assertion about compliance-review outcomes, not backed by a named audit failure or rejected finding)
- **Quote**: "An agent that retrieves broadly, pulling in whole repositories, guessing at context, and hallucinating when it can't find what it needs, produces output no one can vouch for. When that output is a security-critical change, 'the model decided' is not an answer that survives a compliance review."
- **Our assessment**: This is the article's normative claim connecting retrieval breadth directly to compliance risk, not just answer quality — a distinct framing from most of the corpus's context-engineering material, which discusses retrieval scoping mainly as a quality/cost lever (see Cross-References). Here, narrow retrieval is argued to be a compliance requirement in its own right, independent of whether broad retrieval happens to produce a correct answer.

### Claim 8: Scoped, deliberate retrieval ("scope the problem first, then reason") makes an agent's behavior legible — you can see what it asked, what it found, and what it read — and that legibility, not the token-cost savings, is the more important enterprise benefit
- **Evidence**: Stated as the article's central design-pattern claim under "Focused Retrieval Is a Control."
- **Confidence**: emerging (a specific, actionable design claim; internally consistent with Claim 3's audit-theory argument, though not independently benchmarked or compared against broad-retrieval approaches in this article)
- **Quote**: "The engineering community has been converging on a pattern: scope the problem first, then reason. Narrow, deliberate retrieval keeps token costs down, but the more important benefit for the enterprise is that it makes an agent's behavior legible. ... That trail is the difference between an AI workflow you can put in front of an auditor and one you have to quietly keep out of regulated systems."
- **Our assessment**: This is the article's reusable thesis statement for a governance chapter: scoped retrieval should be justified to enterprise stakeholders as an audit control first and a cost optimization second. This inverts the usual framing (cost/quality justification for scoping, with auditability as a side benefit) and is worth flagging as a distinct argument, not just a restatement of "narrow context windows are cheaper."

### Claim 9: Sourcegraph Deep Search returns an explicit, citable list of every search it ran and every file it read to reach its conclusion, functioning as an evidence trail rather than a debugging aid
- **Evidence**: First-party product description of Sourcegraph's own Deep Search feature.
- **Confidence**: emerging (first-party product capability description; not independently verified by this Miner against the actual product output)
- **Quote**: "Sourcegraph's Deep Search returns an explicit list of sources with every answer: a record of which searches it ran and which files it read to reach its conclusion. That source list isn't a debugging nicety; it's an evidence trail. When an agent's reasoning is questioned, you can point to exactly what it consulted."
- **Our assessment**: This is the concrete product mechanism underlying the abstract "legibility" claim in Claim 8. It is worth noting that this is a first-party description of Sourcegraph's own product with an obvious motivation to characterize it favorably — the Miner did not independently test Deep Search's citation behavior.

### Claim 10: The Sourcegraph MCP server exposes discrete, named operations (read a file, search by keyword, jump to a definition) instead of an opaque "do the thing" interface, and access is governed by the same repository permissions and scoped tokens the user already has — with processing happening inside the customer's own instance and the only external call going to the model
- **Evidence**: First-party architectural description of the Sourcegraph MCP server.
- **Confidence**: emerging (first-party architecture claim; the permissioning and data-residency claims are specific and checkable in principle, but not independently verified by this Miner)
- **Quote**: "Underneath that, the Sourcegraph MCP server exposes discrete, named operations (read a file, search by keyword, jump to a definition) rather than an opaque 'do the thing' interface. Every action an agent takes is a legible, individually observable event. Access is governed by repository permissions and scoped tokens: agents can only read the repositories a user is already permitted to see. Processing happens inside your own instance; the only external call is to the model itself."
- **Our assessment**: This bundles three distinct claims worth separating when citing: (a) discrete named tool operations as a legibility mechanism, echoing the "explicit verbs, not opaque actions" design pattern already documented elsewhere in the corpus for a different vendor's tooling; (b) permission inheritance (agent bounded by the user's existing repo ACLs, not elevated); (c) a data-residency claim (only the model call itself leaves the customer's instance). Each is independently useful for a security/compliance chapter, but (b) and (c) in particular are architecture claims about deployment topology, not about the retrieval-as-audit-trail thesis, and should be attributed as Sourcegraph's own self-hosted deployment characteristics rather than a general principle for all agent tooling.

### Claim 11: Deep Search sessions export as a PDF an auditor can be handed directly, tying cited commit history, file paths, and code context to the reasoning behind a change — shortening the audit because the auditor doesn't have to reconstruct what informed the change themselves
- **Evidence**: First-party product description, framed as the article's closing "what audit-ready looks like today" claim.
- **Confidence**: emerging (first-party product feature description; not independently verified)
- **Quote**: "The record is a concrete artifact: every conversation exports as a PDF you can hand to an auditor instead of asking them to take the agent's word for it. That does more than satisfy the control; it shortens the audit. The auditor doesn't have to poke around your environment piecing together what informed a change, because the sources and context are already laid out in a traceable line."
- **Our assessment**: This is the most concrete, actionable artifact-level claim in the source: a specific deliverable format (exportable PDF, citation-backed) that a compliance program could point to as evidence. It's also the clearest illustration of Claim 3's audit-theory argument made tangible — this is what "a transparent record an auditor can reverse-engineer" looks like as a shipped feature rather than an abstract requirement.

### Claim 12: The article frames the retrieval/context layer as the audit and compliance layer for agentic development, not merely a developer-productivity tool — arguing that regulated organizations that can produce provenance evidence are the ones cleared to deploy AI in their highest-stakes systems
- **Evidence**: Stated as the article's closing thesis under "From Productivity Tool to System of Record."
- **Confidence**: anecdotal (a closing strategic reframing/prediction, not backed by a named example of an organization being "cleared" or blocked on this basis)
- **Quote**: "For a security or platform leader, the context layer is also the audit and compliance layer for agentic development. It serves as the system of record for agent provenance, answering the questions regulators and risk teams actually ask: what did the agent read, and why did it act the way it did. ... The teams that can produce it are the ones that get cleared to use AI where the stakes are highest."
- **Our assessment**: This is the article's summary framing and should be read as a positioning statement for Sourcegraph's own product category (context/code-search engine) rather than a neutral industry observation — it directly serves Sourcegraph's commercial interest in being seen as compliance infrastructure, not just a search tool. Still useful for the guide as an articulated example of how a vendor is choosing to position retrieval/search tooling to security buyers.

## Concrete Artifacts

### "Ask Deep Search the Questions Your Auditors Ask You" — compliance-category question bank (verbatim from the article)
```
Source: sourcegraph.com/blog/compliance-first-ai-proving-agent-provenance

Change Management / Access Control
  - "Show me all commits touching the authentication service in the last audit period."
  (Deep Search groups every commit touching the authentication service by theme,
   with SHA, date, and author for each one.)

Data Privacy / GDPR / CCPA
  - "When did we implement the 'right to be forgotten' / user data deletion endpoint?"
  - "Where is PII encrypted at rest, and when was that encryption added?"
  - "Do we have code that logs or stores IP addresses without consent checks?"

Security Controls (SOC 2 / ISO 27001)
  - "When was MFA enforcement added to the admin login flow?"
  - "Where do we validate that access tokens expire, and what's the expiration window?"
  - "Show me all places where secrets/API keys might be hardcoded instead of pulled
    from a vault."

PCI-DSS (Payment Data)
  - "When was the last change to the payment processing module, and who approved it?"
  - "Where does credit card data touch our codebase, and is it tokenized before storage?"
  (Deep Search traces credit card data from entry point to storage in the public
   gitlab-org/gitlab repository, naming the files and the fields that get hashed.)

SOX (Financial Controls)
  - "Where is revenue recognition logic implemented, and when did it last change?"

HIPAA (Healthcare)
  - "Where is PHI access logged, and when was audit logging added?"
  - "Do we have role-based access control gating PHI fields, and when was it introduced?"

Primary sources cited by the article for these frameworks: SOC 2, ISO/IEC 27001,
PCI-DSS, GDPR Article 17, HIPAA 45 CFR 164.312, SOX Section 404.
```

### Sourcegraph MCP server + Deep Search architecture stack (as described)
```
Source: sourcegraph.com/blog/compliance-first-ai-proving-agent-provenance

1. Sourcegraph MCP server: discrete named operations (read file, search by
   keyword, jump to definition) — not an opaque "do the thing" tool call.
2. Access control: repository permissions + scoped tokens — agent can only
   read what the invoking user is already permitted to see.
3. Data residency: processing happens inside the customer's own Sourcegraph
   instance; the only external network call is to the model itself.
4. Deep Search: returns an explicit source list per answer (searches run,
   files read) — the evidence trail layer on top of the MCP server's
   individually observable operations.
5. Export: every Deep Search conversation exports as a PDF, citing commit
   history, file paths, and code context tied to the reasoning for a change.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-ciso-guide-agentic-ai.md` Claim 2 (the four-question risk
    framework's fourth question — "What observability do I have? ... Does it land in
    your SIEM?"): this article's provenance argument (Claims 3, 5) sharpens that
    observability question specifically for the retrieval/context dimension — not just
    "can you tell agent actions from user actions" but "can you show which files
    informed a specific decision and why." Same underlying observability concern,
    narrower and more retrieval-specific framing here.
  - `blog-thebatch-fde-agents-aiact-issue355.md` Claim 9 (EU AI Act delay to
    December 2027 for high-risk systems, with sector-specific compliance deadlines):
    that note documents the regulatory timeline pressure; this article's FAQ block
    names the specific compliance frameworks (SOC 2, ISO 27001, PCI-DSS, GDPR, SOX,
    HIPAA) that regulated engineering teams are already operating under today,
    independent of the EU AI Act's newer AI-specific requirements. The two sources
    together give both the emerging AI-specific regulatory timeline and the
    already-in-force general compliance frameworks agent provenance has to satisfy.
  - `blog-latentspace-databricks-agent-clouds.md` Claim 6 (Omnigent's stateful
    "contextual policies" tracking cumulative session risk, e.g. how many confidential
    documents an agent has read): both sources treat "what has the agent actually
    accessed this session" as the load-bearing governance signal, though they propose
    different mechanisms — Databricks tracks cumulative risk state to gate future
    actions, while this article emphasizes a citable retrieval record for after-the-fact
    audit. Complementary layers: one is preventive (block risky next actions), the other
    is evidentiary (prove what already happened).

- **Extends**:
  - `blog-anthropic-compliance-api.md` Claim 4 (Anthropic's Claude Platform Compliance
    API explicitly does NOT log inference activities — "user interactions with the
    model or model activities" are excluded by design, per that note's Enterprise
    Compliance Gap Matrix, which lists "What were the model's recommendations?" as
    "NOT COVERED"): this is the single most direct and valuable cross-reference for
    this source. The Anthropic note documents, from the platform vendor's own
    admission, a compliance gap — no first-party record of what a model was asked or
    what informed its output. This Sourcegraph article is a different vendor's proposed
    fix for exactly that gap, at the tool/retrieval layer rather than the platform layer:
    Deep Search's citation trail and exportable PDF are one concrete answer to "what did
    the agent read and why," which is precisely the class of question the Compliance API
    explicitly disclaims responsibility for. Worth pairing these two notes directly in
    any guide section on compliance architecture: platform-level audit logging (access,
    resource, config changes) plus tool-level retrieval provenance (this source) together
    address a fuller compliance surface than either alone — though neither, on its own,
    logs the literal token-by-token model conversation.
  - `docs-github-copilot-chat-agent-sessions.md` Claim 2 ("Get agent logs" — a Copilot
    Chat tool that pulls PR-scoped cloud agent session logs into chat for natural-language
    querying): that source documents post-hoc log retrieval as a forensics/debugging
    primitive. This article extends the same underlying need (post-hoc access to what an
    agent did and why) into an explicit compliance-artifact framing — a citation-backed,
    exportable PDF positioned for auditors, not just an in-chat NL query for engineers
    debugging a PR. The Copilot tool is retrieval of raw session logs; Deep Search's
    output is described as a structured, pre-cited evidence trail generated as part of
    normal operation, not fetched after the fact from raw logs.
  - `docs-ghaw-audit-with-agents.md` (the `gh aw audit` JSON schema and regression
    thresholds for agent workflow monitoring): that source's "audit" concerns
    operational health (cost deltas, token usage, MCP error rates) — performance and
    reliability monitoring for agent *workflows* running in CI. This article's "audit"
    concerns a different and non-overlapping question: not "did this agent run cost
    more than the baseline" but "which specific files did this agent read before making
    this specific change, and can that be shown to a compliance auditor." Both are
    legitimately called "audit" in their respective sources but address distinct
    layers — worth noting explicitly in the guide so the two "audit" senses aren't
    conflated: operational audit (is the agent behaving efficiently/reliably) vs.
    compliance/provenance audit (can we prove what informed this specific decision).

- **Contradicts**: No material contradiction identified against existing corpus source
  notes. The closest adjacent claim — that scoped/narrow retrieval is preferable to
  broad retrieval (Claims 7–8) — is a conditioning-variable distinction (compliance
  auditability vs. answer completeness), not a contradiction: no existing source note
  argues that broad, unscoped retrieval is preferable specifically for audit/compliance
  purposes. Checked directly against `blog-anthropic-compliance-api.md`,
  `blog-anthropic-ciso-guide-agentic-ai.md`, `blog-thebatch-fde-agents-aiact-issue355.md`,
  `docs-ghaw-audit-with-agents.md`, `docs-github-copilot-chat-agent-sessions.md`,
  `blog-latentspace-databricks-agent-clouds.md`, `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`,
  and `blog-sourcegraph-dorfman-repo-security-posture.md`.

- **Novel**:
  - **"Agent provenance" as a named, distinct compliance concept** (Claims 1, 5): no
    prior corpus source names or defines this specific gap — evidence of which files an
    agent read and why, before it acted — as its own compliance category distinct from
    general "observability" or "audit logging."
  - **Audit management assertions (accuracy, completeness) applied explicitly to agent
    retrieval as "the process"** (Claim 3): the corpus has general audit/compliance
    material (Compliance API, CISA directives, EU AI Act) but no prior source connects
    formal audit theory (management assertions) to what specifically must be
    stress-tested for an agentic system (the retrieval step).
  - **Scoped retrieval reframed as a compliance control first, cost/quality
    optimization second** (Claim 8): inverts the usual corpus framing of context
    scoping as a token-cost or answer-quality lever.
  - **Sourcegraph Deep Search's citation-backed, exportable-PDF audit artifact**
    (Claims 9, 11): first documentation in the corpus of a specific vendor shipping
    a per-conversation, auditor-handoff-ready export tied to file-level citations.
  - **The compliance-category question bank mapped to specific regulatory
    frameworks** (Concrete Artifacts): the specific SOC 2 / ISO 27001 / PCI-DSS /
    GDPR / SOX / HIPAA example-question mapping to a single code-search product is new
    to the corpus.

## Guide Impact

- **Chapter 06 (Security / Threat Model / Compliance)**: Add "agent provenance"
  (Claim 5) as a named term distinct from general observability — the specific
  requirement is a record of which files an agent read and why, before it acted,
  not just a log of what actions it eventually took. Pair directly with
  `blog-anthropic-compliance-api.md` Claim 4 to show the gap (platform-level compliance
  logging explicitly excludes model/inference activity) and this source's proposed
  fill (tool-level retrieval citation trail) as two halves of a fuller compliance
  architecture.

- **Chapter 06**: Add Claim 3's audit-theory framing (accuracy/completeness management
  assertions applied to agent retrieval) as a concrete argument for why scoped,
  citable retrieval should be treated as a compliance control, not merely a
  cost-optimization technique — cite alongside Claim 8's "legibility, not just token
  cost" reframing.

- **Chapter 06**: Add the compliance-category question bank (Concrete Artifacts) as a
  self-assessment tool: teams building regulated-industry agent systems should be able
  to answer SOC 2/ISO 27001/PCI-DSS/GDPR/SOX/HIPAA-style questions about their own
  agent's file access history, not just about the code changes it produced.

- **Chapter 02 (Harness Engineering)**: Add the Sourcegraph MCP server's
  discrete-named-operations design (Claim 10) as a reusable harness pattern — expose
  tools as individually observable verbs (read file, search, jump to definition) rather
  than an opaque composite action — cross-referencing this against any existing
  corpus material on legible/auditable tool design.

## Extraction Notes

1. **Full article read via WebFetch**: The article is short (~1,400 words) and was
   retrieved in full via a single WebFetch request that returned complete, apparently
   verbatim section text including the compliance-category question bank and the
   contributor credits footer. No paywall or truncation was encountered. No sub-pages
   were followed — the article's only outbound links are to a "Book a demo" CTA and a
   generic "Schedule a demo" footer link, neither of which contains substantive content
   to extract.
2. **Byline is Justin Dorfman — same author as an existing corpus note**: The post
   carries a single byline (Justin Dorfman) beneath the title and publish date. The six
   names in the footer (André Eleuterio, Dora Neumeier, Jamie Lindsay, Makenna Freauf,
   Matt Tanner, and Stephanie Jarmak) are credited "for their contributions to this blog
   post" — contributors, not co-authors. Dorfman already appears in the corpus as the
   author of `blog-sourcegraph-dorfman-repo-security-posture.md`, so the corpus's
   `blog-<author>-<topic>.md` convention for single-byline Sourcegraph posts would give
   this note the slug `blog-sourcegraph-dorfman-compliance-first-agent-provenance.md`.
   The file retains the `<type>-<source>-<topic>.md` slug it was opened under because the
   PR, branch, and issue #2355 all key off it; **flagged here for a maintainer rename**
   rather than renamed unilaterally during rework. Analytically, the consequence is that
   this note and the repo-security-posture note are one author's successive arguments for
   the same product category and should be weighted as a single vendor voice, not two
   independent vendor sources (see Source Context → Author credibility).
3. **Vendor content, no independent verification of product claims**: Claims 9–11
   (Deep Search's citation behavior, the MCP server's permission inheritance and data
   residency, and the PDF export feature) are first-party descriptions of Sourcegraph's
   own shipping product. This Miner did not test Deep Search or the MCP server directly
   and could not independently verify these behaviors — they are graded `emerging`
   throughout rather than `settled`, consistent with the `emerging` grading already
   applied to the corpus's other two Sourcegraph vendor-blog notes.
4. **No contradictions filed**: Cross-referenced against all source notes covering
   compliance, audit, agent observability, and Sourcegraph's own prior blog posts (see
   Cross-References → Contradicts for the full list checked). No material contradiction
   found; this source instead fills a gap the corpus had already surfaced
   (`blog-anthropic-compliance-api.md`'s explicit inference-logging exclusion) rather
   than disputing an existing claim.
5. **Overall confidence set to `emerging`**: The article's central conceptual argument
   (agent provenance as a distinct, real compliance requirement, grounded in standard
   audit theory) is well-reasoned and consistent with the corpus's broader compliance
   material, so it is not graded `anecdotal` overall. However, the customer-sentiment
   claims (Claims 1, 2) are unnamed and unverifiable, and the product-capability claims
   (Claims 9–11) are first-party vendor descriptions not independently tested — so the
   note is graded `emerging` rather than `settled`, consistent with the other two
   Sourcegraph vendor posts already in the corpus.
