---
source_url: https://www.thoughtworks.com/insights/articles/context-challenge-ai-agents
source_type: blog-post
title: "Why context is the real bottleneck for AI agents"
author: Gaurav Patole
date_published: 2026-10-01
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: emerging
issue: "#3930"
---

# Why Context is the Real Bottleneck for AI Agents

> Thoughtworks argues that agents fail on "half-truths" — outputs built on accurate data but missing business context — and proposes continuous context lifecycle management (people / processes / technology) to capture tribal knowledge, with the PocketOS database deletion as its failure example.

## Source Context

- **Type**: blog-post (Thoughtworks Insights article, published 2026-10-01; short conceptual/advocacy piece, no original data beyond one cited survey statistic and one incident anecdote)
- **Author credibility**: Gaurav Patole, writing for Thoughtworks Insights (data strategy). Consultancy perspective: practitioner-informed, but the piece is framework-style and carries a vendor-neutral-but-advisory tone; no first-hand implementation results are reported.
- **Scope**: Covers enterprise business context for agents (tribal knowledge, definitions, verification, ownership, semantic layers). Does NOT cover token-level context-window management, concrete tooling/product names for a context layer (beyond Databricks/Salesforce as examples of siloed context), or measured outcomes of the proposed approach.

## Extracted Claims

### Claim 1: Context — not data accuracy or plausible answers — is what makes AI trustworthy, and it has three layers: technical, policy, and business, with business context being the hardest
- **Evidence**: Argument by definition; no empirical backing.
- **Confidence**: emerging
- **Quote**: "context is the knowledge that makes AI trustworthy"
- **Our assessment**: Useful taxonomy (technical = schemas/databases; policy = governance/compliance; business = tribal knowledge). It widens "context" beyond the token-budget sense used in many corpus notes; worth keeping the two senses distinct in the guide. The layering is asserted, not validated.

### Claim 2: "Half-truths" — outputs that blend accurate facts with subtle context gaps — are a more dangerous failure mode than obvious hallucination, because they look rational and defeat human review
- **Evidence**: Reasoning plus the PocketOS example; no measurements of how often reviewers miss such errors.
- **Confidence**: emerging
- **Quote**: "half-truths blend accurate facts with subtle context gaps"
- **Our assessment**: Plausible and consistent with the corpus (see Cross-References: Xiong's CHF readmission example). The named failure mode is a good vocabulary item. The strong form (human oversight is insufficient) is overstated without evidence; the article's own remedy is to give overseers better context.

### Claim 3: The PocketOS incident: an AI coding agent hit a permission error in a test environment, used a valid API token to clear the blocker — unaware the token granted blanket access to live systems — and deleted the production database and backups within nine seconds
- **Evidence**: Single anecdote told in two sentences; no link to an incident report in the fetched text.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The details here (test-environment permission error, token with live-system scope, nine seconds, backups also deleted) are the most specific account in the corpus so far. Note the framing differs from Marr's: Marr reads PocketOS as missing enforcement (permissions/pre-action checks); Patole reads it as missing context (the agent did not know the token's blast radius). These are compatible readings of one incident (scoped credentials is the enforcement answer; knowing token scope is the context answer), but the incident is still reported, not independently verified, by this Miner.

### Claim 4: Human oversight alone is insufficient against half-truths; overseers need real business context and the tacit knowledge that was never documented
- **Evidence**: Reasoning only.
- **Confidence**: anecdotal
- **Quote**: "half-truths produce outputs that look completely rational on the surface"
- **Our assessment**: Pairs with the supervisory-engineering framing: reviewing agent output requires domain expertise, so "human in the loop" is only as good as the human's context. Conditional on the reviewer being a generalist rather than a domain owner.

### Claim 5: Tribal knowledge stays locked away for cultural and behavioral reasons, not primarily technical ones — five barriers are named
- **Evidence**: Listed barriers (incentive problems, deliberate withholding, administrative burden, expertise gaps from decades of IT outsourcing, difficulty of tacit knowledge in hyper-specialized fields like oncology or stock trading). No survey data for these specifically.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The article's most original contribution for the corpus. In particular the incentive barrier — experts fear that sharing knowledge makes them dispensable when leadership says AI will "streamline the workforce" — is an adoption risk that most technical notes ignore. Practitioner-plausible; experience-based rather than evidence-based.

### Claim 6: Even captured context needs verification, because data silos create competing versions of truth and no shared context layer exists across systems
- **Evidence**: Examples: Finance and Sales may define "active customer" differently; context defined in Databricks stays isolated there, Salesforce context stays in that CRM.
- **Confidence**: emerging
- **Quote**: "Because these systems lack a shared context layer, data cannot be cross-referenced or verified in real-time."
- **Our assessment**: Matches the cross-system reconciliation failure Xiong documents in detail. The "active customer" example is a clear, quotable illustration of semantic conflict between departments.

### Claim 7: Context must be managed as a continuous lifecycle (governance, lineage, ownership, continual update) rather than a static documentation project
- **Evidence**: Prescriptive argument; no case study showing it working.
- **Confidence**: emerging
- **Quote**: "end-to-end governance, traces lineage, assigns ownership and continually updates context"
- **Our assessment**: Consistent with Asthagiri's "ontology as a product with an owner" and the staleness findings. Treat as a direction, not a validated method.

### Claim 8: The "People" pillar: assign departmental (not IT) accountability for business definitions, and reframe AI as "eager interns" shadowing experts to address job-security concerns
- **Evidence**: Prescription; ties to the barriers in Claim 5 and to a Thoughtworks 2026 CIO survey statistic that 89% of respondents agreed they are now more responsible for redesigning workforce workflows.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Ownership-by-domain agrees with other Thoughtworks notes (Gall's domain-bounded context). The "eager interns" framing is a change-management tactic with no tested outcome. The 89% figure is about workflow-redesign responsibility, not context capture, so it is weak support for this claim.

### Claim 9: The "Processes" pillar: establish lineage for agent decisions so they can be corrected immediately, build "agent-ready data products" with product-engineering discipline, and embed context capture into daily work via conversational AI features instead of manual forms
- **Evidence**: Prescription; addresses the administrative-burden barrier from Claim 5.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The "capture as a by-product of work" idea echoes Gall's passive relationship discovery and Mishra's confidence/trace markers. No implementation detail is given, so it is a principle rather than a recipe.

### Claim 10: The "Technology" pillar: invest in semantic/ontology tooling and shared semantic layers exposed through open interfaces so every system resolves to one governed definition — but "a semantic layer is the foundation, not the finished house", because humans must keep curating as meaning drifts
- **Evidence**: Prescription plus an explicit caveat that tooling alone does not keep definitions accurate.
- **Confidence**: emerging
- **Quote**: "a semantic layer is the foundation, not the finished house"
- **Our assessment**: The caveat is the valuable half and aligns with the corpus's skepticism of one-time semantic-layer builds. The "single governed location" aspiration is in mild tension with Gall's view that a complete enterprise semantic layer is illusory (see Cross-References); the difference is plausibly scope (domain-level vs. enterprise-wide), but the article does not address it.

### Claim 11: At scale (hundreds or thousands of concurrent agents) context determines whether agents multiply business value or compound failures; context should be treated as a "living operational asset"
- **Evidence**: Rhetorical conclusion; no scale data.
- **Confidence**: anecdotal
- **Quote**: "a living operational asset"
- **Our assessment**: Directionally sensible (errors replicate across agents sharing the same bad context) but unquantified. Use as framing only.

## Concrete Artifacts

```
Three-pillar context lifecycle framework (Patole, Thoughtworks Insights, 2026-10-01; paraphrased structure)
People      : departmental ownership of business definitions; "eager interns" framing for AI
Processes   : lineage for agent decisions; agent-ready data products; capture context
              in daily operations via conversational AI features
Technology  : semantic/ontology tooling; shared semantic layer via open interfaces
```

```
Barriers to tribal-knowledge capture (Patole, section "Why Tribal Knowledge Remains Locked Away"; paraphrased list)
1. Incentive problems
2. Deliberate withholding (business units use context as leverage)
3. Administrative burden (forms, manual logs)
4. Expertise gaps (decades of IT outsourcing)
5. Tacit knowledge difficulty (e.g., oncology, stock trading)
```

```
PocketOS incident as told in the article (paraphrased sequence)
permission error in test environment -> agent finds valid API token -> token has access to live systems
-> production database and backups deleted in nine seconds
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-xiong-data-agents-context-resolution.md` Claim 1 (agent failures stem from meaning that lives outside the data) and Claim 8 (turn tacit reconciliation knowledge into explicit rules). Patole's "half-truths" is the general name for what Xiong shows concretely with the CHF readmission case (Claim 2).
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 1 (LLMs read documents but do not hold operating logic), Claim 6 (shared ontology goes stale without a steward) and Claim 8 (ontology as a product with an owner) — match this article's ownership and "foundation, not finished house" points.
  - `blog-thoughtworks-mishra-ai-assisted-migration.md` Claim 9 (tribal knowledge converted into a systematic process) — a worked example of capturing tribal knowledge.
- **Contradicts**: None filed. Potential tension, not escalated because it looks like a scope/conditioning difference rather than opposed claims: `blog-thoughtworks-gall-layered-context-enterprise-data.md` Claim 2 says a complete enterprise semantic layer is "ultimately illusory" and Claim 6 says SME-curated graphs are "dead on arrival", whereas Patole recommends a single governed semantic layer with departmental owners (Claim 10 here). Patole's own caveat that curation must continue is closer to Gall than the headline suggests.
- **Extends**:
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 3 (PocketOS as "missing enforcement"): adds a second, complementary reading — missing context about the token's scope — plus the nine-second/backups-deleted detail.
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md` (delegation failure as a diagnostic category; see its PocketOS-related claim): adds the context-gap category to the same incident.
  - `blog-thoughtworks-gall-supervisory-engineering.md`: the need for reviewers to hold tacit domain context.
- **Novel**:
  - The "half-truths" label as a failure category distinct from hallucination.
  - The five cultural barriers to tribal-knowledge capture, especially the job-security incentive problem.
  - The "eager interns" change-management framing.
  - Explicit "Finance vs. Sales: active customer" example of competing definitions across departments.

## Guide Impact

- **Chapter 02 (Context and Knowledge)**: Add a short passage distinguishing token-level context management from organizational/business context, with "half-truths" as the failure name and the Xiong CHF case plus PocketOS as examples. Cite this note together with `blog-thoughtworks-xiong-data-agents-context-resolution.md`.
- **Chapter 04 (Governance and Accountability)**: Add the five tribal-knowledge barriers (especially incentives) as an adoption risk, and the "departmental ownership of definitions, not IT" recommendation, flagged as emerging/practitioner opinion.
- **Chapter 05 (System Reliability)**: In any PocketOS discussion, present both readings (missing enforcement per Marr; missing context about credential scope per Patole) and note the incident is single-source and unverified.

## Extraction Notes

- Read the full article (single page, no pagination). Related-content links (AI-ready data, "How data agents fail, and why it's a context problem", data products) were listed but not fetched; the middle one corresponds to the already-mined Xiong note.
- The page text was obtained through a summarizing fetch tool, so short quotes were taken only from phrases the tool returned inside quotation marks; the Assayer should spot-check them against the live page. Claims without a safe verbatim fragment use the "no direct quote" convention.
- The article is brief and prescriptive; no metrics for the proposed approach are given. The only quantitative statement (89% in the 2026 CIO survey) is tangential to context capture.
- No contradiction issue was filed (see Cross-References → Contradicts).
