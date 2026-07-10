---
source_url: https://www.thoughtworks.com/insights/articles/governing-autonomous-enterprise-agentic-scope-authority-framework
source_type: blog-post
title: "Governing the autonomous enterprise: The Agentic Scope of Authority Framework"
author: Jeremy Gordon and Matt Kamelman
date_published: 2026-06-18
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: emerging
issue: "#1713"
---

# Governing the Autonomous Enterprise: The Agentic Scope of Authority Framework

> Thoughtworks proposes the "Agentic Scope of Authority Framework" — a legal/
> operational governance blueprint built on the corporate-law distinction between
> actual and apparent authority, operationalized through a three-tier oversight
> structure (manual, semi-automated, automated) and applied to data privacy,
> contractual guardrails, and explainability/drift review — motivated by the
> April 2026 Andon Labs autonomous-retail-agent failure.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published June 18, 2026; from the
  trusted feed `thoughtworks`. Co-authored by Jeremy Gordon (bio line:
  "Head of Legal, Americas") and Matt Kamelman (bio line: "Innovation
  Choregrapher" — job title as it appears on the page, unedited). Framework/
  thought-leadership piece structured around a single motivating case study
  followed by a named, numbered framework.)
- **Author credibility**: Jeremy Gordon is credited in-article as Thoughtworks'
  "Head of Legal, Americas," giving the legal/agency-law content first-party
  legal-practitioner authority within the firm rather than outside academic or
  regulatory authority. Matt Kamelman (credited as "Innovation Choregrapher")
  is a repeat author in this corpus — see
  `blog-thoughtworks-kamelman-ai-governance-category-error.md` and
  `blog-thoughtworks-kamelman-token-crisis.md` — established as a
  trusted-feed voice, though prior notes on his solo work found his claims
  frequently unsourced/unlinked within the article itself (see Cross-References
  and Extraction Notes below for how that pattern recurs here). No case-study
  outcome data, adoption metrics, or named enterprise deployments of the
  framework itself are provided — the framework is presented as newly proposed,
  not validated in production.
- **Scope**: Covers a legal/governance framework for constraining what an AI
  agent is authorized to commit an enterprise to, built around agency law
  (actual vs. apparent authority) and operationalized through a three-tier
  oversight structure. Also covers three "legal and ethical minefield" areas:
  data privacy (GDPR/CCPA), contractual guardrails (an NLP-scanned "never"
  list), and explainability/drift mitigation (XAI logging + scheduled "drift
  review" red-teaming). Mentions but does not detail: the EU AI Act (cited
  only as background pressure), a "nine blocks" interactive assessment tool
  (referenced but the nine blocks are not enumerated in the article body —
  see Extraction Notes). Does NOT cover: specific vendor tooling, model-layer
  technical security controls (prompt injection, tool poisoning, credential
  isolation — see `blog-anthropic-zero-trust-ai-agents.md` for that), or any
  quantitative outcome/incident data beyond the single Andon Labs case study.

## Extracted Claims

### Claim 1: The Andon Labs autonomous retail agent (April 2026) — given a three-year commercial lease, $100,000 in capital, and the single directive "make a profit" — successfully performed several complex, high-autonomy business functions (branding, inventory, AI-generated art, hiring, later ratified by a human) but made two concrete operational errors, and the underlying governance failure was structural: no governance document, no designated principal, no clear liability chain
- **Evidence**: The article's opening case study, presented as fact without an external citation link within the article text.
- **Confidence**: anecdotal (single case study; no independent verification link provided in the article itself; the specific "$100,000" and "three-year lease" figures and the "attempting to hire a painter in Afghanistan" detail are stated as fact but not sourced to a report, filing, or interview)
- **Quote**: "In April 2026, an autonomous AI agent in San Francisco was given a three-year commercial lease, a business bank account with $100,000 and a single directive: make a profit. Without human direction or intervention, it opened a store, designed the brand's aesthetic, purchased inventory, decorated with its own AI-generated art and hired human staff (a move later ratified by a human)."
- **Quote** (failure and governance gap): "But when the agent made operational errors, attempting to hire a painter in Afghanistan due to a botched vendor form and failing to schedule staff for opening day, there was no governance document, no designated principal and no clear liability chain."
- **Our assessment**: This is the strongest concrete artifact in the article and the motivating case for the entire framework. The two named failures are illustrative rather than catastrophic (a mis-routed hiring form, a scheduling gap) — the article's point is not that the failures were severe, but that *no governance structure existed to catch, own, or answer for them*. This is a good example for the guide of a real deployed-agent governance gap, though the Miner could not independently verify the case details beyond this article's own account — the guide should flag it as reported, not independently confirmed, if cited.

### Claim 2: The legal frameworks needed to govern AI agents already exist (centuries-old agency law); the challenge is not writing new law but creatively and defensively applying existing legal principles to AI's digital reality
- **Evidence**: Stated as the article's central operating premise, used to justify why the proposed framework does not wait for new regulation.
- **Confidence**: anecdotal (single-author/co-author legal-practitioner assertion; no citation to case law, statute, or legal scholarship supporting the specific claim that existing agency law doctrine transfers cleanly to autonomous AI agents)
- **Quote**: "There is a common misconception that society must wait for regulatory bodies to invent entirely new legal systems to govern AI. In reality, the legal frameworks we need have existed for centuries. The challenge is not writing new laws; it's creatively and defensively applying the established principles of agency law to our digital reality."
- **Our assessment**: This premise is doing significant argumentative work — the entire framework's legitimacy rests on the assumption that agency law (built for human agents with human judgment, titles, and legal capacity) maps onto autonomous software agents without requiring new institutional response. **This directly contradicts a claim in this corpus's other Kamelman-associated piece** — see Cross-References → Contradicts, and the filed contradiction issue #1730. The guide should not treat this premise as settled; it is a contestable legal-strategy stance from one legal practitioner, not an adjudicated legal conclusion (no court case establishing actual/apparent authority doctrine applies to autonomous AI agents is cited).

### Claim 3: Corporate agency law divides authority into two categories — actual authority (what the principal explicitly permits) and apparent authority (what a third party reasonably believes is authorized based on the agent's title/presentation/behavior) — and the gap between these two is an underappreciated source of enterprise exposure for AI agents specifically
- **Evidence**: Direct legal-doctrine description, applied to AI agents by extension.
- **Confidence**: settled (actual vs. apparent authority is an established doctrine in corporate/agency law generally) / emerging (the specific claim that this doctrine applies "identically" to AI agents carrying titles or logos is the article's extension, not independently adjudicated)
- **Quote**: "In corporate law, authority is divided into two categories. Actual authority is what the agent is explicitly permitted to do by its principal. Apparent authority is what a third party reasonably believes the agent is authorized to do based on its title and behavior. The disconnect between the actual and apparent authority of an AI agent is perhaps the most underappreciated source of enterprise exposure."
- **Quote** (extension to AI): "Under agency law and electronic signature regulations a company can be legally bound by actions that fall entirely outside an agent's actual authority if a third party reasonably assumed those actions were authorized... It applies identically to AI agents that carry corporate logos, respond on company letterhead, or present themselves with titles like 'Procurement Director.'"
- **Our assessment**: The actual/apparent authority distinction itself is well-established law; the "applies identically" extension to AI agents is the article's own legal-strategy argument, not a cited precedent. For guide purposes, this is a useful framing vocabulary (actual vs. apparent authority) for discussing agent-authority risk, but the guide should present the AI-specific application as an interpretive legal position from a Thoughtworks legal practitioner, not settled case law.

### Claim 4: An agent's public-facing title and visual identity are legal design decisions, not UX decisions — a "Junior Clerk"-styled agent carries fundamentally different apparent authority than a "VP of Procurement"-styled agent even under identical technical constraints, and these must be made explicit, documented, and enforced at the infrastructure layer
- **Evidence**: Direct statement of the framework's identity-styling design principle.
- **Confidence**: emerging (logically coherent extension of Claim 3; no empirical or legal-case data on whether courts would actually treat AI agent titling as apparent-authority evidence)
- **Quote**: "An agent styled as a 'Junior Clerk' carries a fundamentally different apparent authority than one styled as a 'VP of Procurement,' even if both operate under identical technical constraints. The public-facing title, the visual identity and the presence of a 'subject to human validation' disclaimer are not UX decisions. They are legal design decisions."
- **Quote** (enforcement mechanism): "Our framework requires that these be made explicitly, documented and enforced at the infrastructure layer — for instance, through metadata, authorization policies, constrained prompts and platform-level enforcement controls."
- **Our assessment**: This is the article's most actionable, specific claim — it reframes a product/UX decision (what to call an agent, how to present it) as carrying legal weight, and prescribes infrastructure-layer enforcement (metadata, authorization policies, constrained prompts) rather than documentation alone. This corroborates and extends `blog-anthropic-agent-identity-access-model.md` Claim 5 (Claude Tag agents present as distinct, named identities — "Claude app," "Claude GitHub App" — per connected system), though the two sources address different audiences for that identity: Anthropic's note is about internal/system-facing identity (which service account touched what), while this claim is about external/third-party-facing identity (what a vendor or customer reasonably infers about the agent's authority from its title). See Cross-References → Extends.

### Claim 5: The framework's core innovation is categorizing oversight into three tiers, clarifying which parts of agent governance must be human-authored policy versus platform-enforced code: manual oversight (designated principal + human-written core mandate), semi-automated oversight (dynamic escalation + identity styling/disclaimers), and automated oversight (financial constraints, contractual "forbidden clause" scanning, failsafes/kill switches)
- **Evidence**: Stated as the framework's central structural claim, elaborated with three named, numbered subsections.
- **Confidence**: emerging (coherent, actionable taxonomy from a credible practitioner source; no case study demonstrating this specific three-tier split was tested against a real governance failure)
- **Quote**: "A key innovation of the framework is its categorization of oversight into three distinct levels, clarifying exactly which parts of the governance document must be drafted by human leaders and which must be enforced by your agentic platform."
- **Quote** (Tier 1, manual): "The framework mandates that every deployed agent must have a 'designated principal' — a specific human executive legally and operationally accountable for the agent's outcomes. Furthermore, humans must explicitly write the agent's core mandate (e.g., 'Autonomously source and procure eco-friendly office supplies within Western Europe'). AI cannot define its own legal and operational purpose."
- **Quote** (Tier 2, semi-automated — dynamic escalation): "If an agent is authorized to negotiate purchases up to $10,000, any negotiation exceeding this limit is automatically paused by the platform and routed to a human supervisor for manual sign-off."
- **Quote** (Tier 3, automated — financial/contractual/failsafe): "Financial constraints: Hard limits on budget consumption, transaction sizes and daily spending caps. Contractual boundaries: 'Forbidden clause' lists scanned via natural language processing (NLP) to instantly flag and block negotiations containing unfavorable terms. Failsafes and kill switches: Automatic, soft pauses triggered by system-level anomalies, such as high API error rates or rapid market volatility."
- **Our assessment**: This three-tier taxonomy (manual/semi-automated/automated) is a legal-governance-oriented parallel to the technical three-tier maturity model in `blog-anthropic-zero-trust-ai-agents.md` (Foundation/Enterprise/Advanced), but organized by *who enforces it* (human vs. platform) rather than by *organizational maturity*. It also corroborates `blog-jetbrains-agentic-ai-governance.md` Claim 3 (chain of command — a specific person with authority over outcomes) and Claim 8 (intentional checkpoints with risk scoring for high-impact actions) — the "designated principal" and "$10,000 dynamic escalation" concepts are concrete operationalizations of both. See Cross-References → Corroborates for full mapping.

### Claim 6: The framework establishes technical "Data No-Go Zones" using role-based access controls to prevent agents from reading or processing sensitive repositories (HR records, customer PII, protected health data) for GDPR/CCPA compliance, and separately requires organizations to explicitly decide whether an agent may learn/fine-tune from data it processes or must be siloed to prevent IP contamination
- **Evidence**: Direct statement under the "Data privacy and integrity" subsection.
- **Confidence**: emerging (RBAC as a technical control for data-boundary enforcement is well-established generally; the specific "Data No-Go Zones" terminology and its sufficiency for GDPR/CCPA compliance is the article's own framing, not a compliance-certified claim)
- **Quote**: "To comply with global frameworks like the EU's General Data Protection Regulation and the California Consumer Privacy Act, the framework establishes technical 'Data No-Go Zones'. Using role-based access controls, these zones prevent agents from reading or processing sensitive repositories, such as employee HR records, customer personally identifiable information (PII), or protected health data."
- **Quote** (secondary use): "Organizations must programmatically decide whether an agent is allowed to learn and fine-tune its models from the data it processes, or if strict, temporary technical silos must be enforced to prevent intellectual property contamination and ensure compliance with regulatory purpose-limitation principles."
- **Our assessment**: "Data No-Go Zones" is a specific, memorable term for RBAC applied to agent data-access boundaries — directly corroborates `blog-anthropic-zero-trust-ai-agents.md`'s "least agency" concept (Claim 5 in that note: restrict what each agent tool can access) applied specifically to the compliance/privacy dimension rather than the security dimension. The secondary-use/fine-tuning question ("should this agent learn from what it processes?") is a distinct and, per this Miner's review, novel framing in this corpus — no other source explicitly poses data governance as a question of whether an agent's *learning* (not just its access) must be scoped.

### Claim 7: Contractual guardrails require an NLP-scanned "never" list of forbidden terms (e.g., foreign arbitration clauses, unlimited liability, IP assignment) that immediately halts vendor negotiations and triggers human-in-the-loop escalation
- **Evidence**: Direct statement under "Contractual guardrails: The 'never' list."
- **Confidence**: emerging (coherent technical/legal design; no data on false-positive/false-negative rates for the NLP scanning approach, no named product implementing this)
- **Quote**: "When negotiating with third-party vendors, agents must be constrained by an unyielding list of forbidden terms. If a counterparty's contract draft attempts to slip in foreign arbitration clauses, demand unlimited liability or assign away your intellectual property, the agent's NLP scanning engine must immediately halt negotiations and trigger a human-in-the-loop escalation."
- **Our assessment**: This is the most concrete technical control specified for the "automated oversight" tier (Claim 5) and gives specific example forbidden-clause categories (arbitration jurisdiction, liability caps, IP assignment) that a real implementation could use as a starting checklist. No accuracy/reliability data is given for the NLP scanning mechanism itself — this should be flagged if cited as a specific implementation recommendation, since NLP-based clause detection is a nontrivial reliability problem the article does not address.

### Claim 8: Explainability requires logging every agent decision alongside its context, prompts, tool usage, data sources, and execution trace, and organizations must run scheduled "drift review" red-team exercises (human engineers + legal specialists) to verify the agent still operates within its originally granted actual authority
- **Evidence**: Direct statement under "Explainability (XAI) and drift mitigation."
- **Confidence**: emerging (audit-logging requirement is consistent with established practice elsewhere in the corpus; the specific "drift review" red-team cadence is the article's own proposed practice, with no stated frequency, staffing ratio, or case data on effectiveness)
- **Quote**: "Explainability (XAI) logging: Every decision made by the agent must be logged alongside the decision context, prompts, tool usage, data sources utilized and execution trace, ensuring an audit trail for legal defense."
- **Quote** (drift review): "The 'drift review': Regular, scheduled red team exercises where human engineers and legal specialists run adversarial testing against the agent to verify it still operates within its original actual authority."
- **Our assessment**: The logging specification here (decision context, prompts, tool usage, data sources, execution trace) is narrower than the seven-element audit trail in `blog-jetbrains-agentic-ai-governance.md` Claim 7 (which additionally specifies initiator, policy-violation status, duration, and cost) — this article's version is oriented toward legal defensibility specifically, while JetBrains' is oriented toward operational governance broadly. The "drift review" pairing legal specialists with engineers in a joint red-team exercise is, per this Miner's cross-reference check, a novel practice not named elsewhere in the corpus — prior sources describe technical drift detection (`blog-jetbrains-agentic-ai-governance.md` Claim 6 on LLM non-determinism) but not a joint legal+engineering adversarial review cadence tied specifically to verifying the agent stayed within its *originally granted legal authority* (as opposed to its technical/behavioral baseline).

### Claim 9: Thoughtworks positions its value proposition as bridging Legal and Platform Engineering teams to translate legal governance policy into running code (event-driven architectures, metadata tagging, cryptographic validation in CI/CD), on the premise that "if your legal constraints cannot be translated into running code, they do not exist"
- **Evidence**: Stated in the "Thoughtworks advantage" section as the firm's positioning/service pitch.
- **Confidence**: anecdotal (vendor self-positioning/marketing claim; no named client engagement or outcome data provided)
- **Quote**: "At Thoughtworks, we know that a governance policy sitting in a static corporate slide deck is practically useless when dealing with autonomous AI. If your legal constraints cannot be translated into running code, they do not exist."
- **Quote** (service description): "Our unique expertise lies in bridging the gap between the Legal and the Platform Engineering team. We help organizations build guardrail architectures that wrap around AI agents. We translate legal limits into event-driven software architectures, secure metadata tagging and cryptographic validation protocols that sit within your automated CI/CD pipelines."
- **Our assessment**: This is vendor self-promotion embedded in the article (Thoughtworks describing its own consulting services) rather than an independent technical or legal claim — flag as marketing content if cited. The underlying principle ("governance that isn't enforced in code doesn't exist") is directionally consistent with `blog-jetbrains-agentic-ai-governance.md` Claim 12 ("Governance is not a bolt-on. It belongs in the architecture") and worth citing for that principle, but the specific Thoughtworks service claims should not be cited as independent evidence of effectiveness.

### Claim 10: Thoughtworks has built an interactive assessment tool covering "nine blocks" of the framework that evaluates enterprise readiness and generates a customized "Scope of Authority" blueprint
- **Evidence**: Stated as a concrete deliverable/tool the firm offers.
- **Confidence**: anecdotal (marketing claim for a specific tool; the article's own body text does not enumerate what the nine blocks are, so this cannot be independently checked against the framework content actually described in the article)
- **Quote**: "To help organizations kickstart this process, we have developed an interactive assessment tool that walks teams through all nine blocks of the framework, evaluates your enterprise readiness and generates a customized, exportable Scope of Authority blueprint."
- **Our assessment**: This is a notable internal inconsistency worth flagging rather than resolving: the article's body describes at most six to seven named framework components across the three-tier structure (designated principal, core mandate, dynamic escalation, identity styling, financial constraints, contractual "never" list, failsafes) plus three "minefield" areas (data privacy, contractual, explainability) — it does not name or enumerate "nine blocks" anywhere in the visible article text. Either the nine-block structure exists only inside the (paywalled/interactive, not fetched by this Miner) assessment tool itself, or this is imprecise marketing copy. Do not cite "nine blocks" as a specific enumerable framework element in the guide without independently accessing the assessment tool.

### Claim 11: The EU AI Act's transparency, risk-management, and logging requirements (alongside similar rules being adopted globally) are ending the viability of "black box" agent deployments — the operative question for enterprises is no longer whether an AI agent can act on the organization's behalf, but whether its authority has been explicitly defined in advance
- **Evidence**: Stated as the article's closing framing, tying regulatory pressure (EU AI Act) to the article's central "define authority before it acts" thesis.
- **Confidence**: emerging (the EU AI Act's transparency/logging requirements are real and verifiable independently of this article; the causal framing — that this specific pressure is what "ends" black-box deployment — is the author's own rhetorical synthesis)
- **Quote**: "As sweeping legal requirements, such as the stringent transparency, risk management and logging requirements of the EU AI Act are adopted increasingly around the world, the sun is setting on black box agent deployments."
- **Quote** (closing thesis): "The question is not whether an AI agent can act on behalf of your organization; it is whether you have effectively defined the agent's authority before it does."
- **Our assessment**: This closing framing is the article's most quotable single line and a good candidate for a chapter epigraph on agent governance — it crisply states the shift from "can it act" (capability question) to "is its authority defined" (governance question), echoing the same capability-vs-accountability reframe in `blog-jetbrains-agentic-ai-governance.md` Claim 1 ("the question is no longer whether it's useful, but what happens when something goes wrong"). Both sources independently converge on this reframe from capability to accountability, though this article ties it specifically to regulatory (EU AI Act) pressure while JetBrains ties it to general production-deployment risk.

## Concrete Artifacts

### Case Study: Andon Labs Autonomous Retail Agent (April 2026)

```
Source: Jeremy Gordon & Matt Kamelman, Thoughtworks Insights, June 18, 2026

SETUP:
  - Three-year commercial lease (San Francisco)
  - Business bank account with $100,000
  - Single directive: "make a profit"
  - No human direction or intervention during operation

ACTIONS TAKEN AUTONOMOUSLY:
  - Opened a physical store
  - Designed brand aesthetic
  - Purchased inventory
  - Decorated with its own AI-generated art
  - Hired human staff (later ratified by a human)

FAILURES:
  - Attempted to hire a painter in Afghanistan (botched vendor form)
  - Failed to schedule staff for opening day

GOVERNANCE GAP (the article's point):
  "there was no governance document, no designated principal and no clear
   liability chain"
```

### Three-Tier Oversight Structure

```
Agentic Scope of Authority Framework — Three Tiers of Oversight
Source: Jeremy Gordon & Matt Kamelman, Thoughtworks Insights, June 18, 2026

TIER 1 — MANUAL OVERSIGHT (Setting human intent)
  - Every deployed agent must have a "designated principal": a specific human
    executive legally and operationally accountable for the agent's outcomes
  - Humans must explicitly write the agent's core mandate, e.g.:
    "Autonomously source and procure eco-friendly office supplies within
     Western Europe"
  - "AI cannot define its own legal and operational purpose."

TIER 2 — SEMI-AUTOMATED OVERSIGHT (Blended human-in-the-loop control)
  - Dynamic escalation: e.g., an agent authorized to negotiate purchases up
    to $10,000 has any negotiation above that limit auto-paused and routed
    to a human supervisor for sign-off
  - Identity styling: platform auto-injects headers/disclaimers stating the
    agent is a "digital assistant with limited capacity," managing and
    limiting its apparent authority to third parties

TIER 3 — AUTOMATED OVERSIGHT (Technical infrastructure guards)
  - Financial constraints: hard limits on budget consumption, transaction
    sizes, daily spending caps
  - Contractual boundaries: "forbidden clause" lists scanned via NLP to
    flag/block negotiations with unfavorable terms
  - Failsafes and kill switches: automatic soft pauses triggered by
    system-level anomalies (high API error rates, rapid market volatility)
```

### Legal and Ethical Minefield Areas

```
Source: Jeremy Gordon & Matt Kamelman, Thoughtworks Insights, June 18, 2026

DATA PRIVACY AND INTEGRITY (GDPR, CCPA)
  - "Data No-Go Zones" via role-based access control
  - Prevents agents from reading/processing: employee HR records, customer
    PII, protected health data
  - Separate question: can the agent learn/fine-tune from data it
    processes, or must strict temporary technical silos apply (IP
    contamination / purpose-limitation compliance)?

CONTRACTUAL GUARDRAILS ("the never list")
  - NLP scanning engine halts negotiations immediately on detecting:
    foreign arbitration clauses, demands for unlimited liability, IP
    assignment clauses
  - Triggers human-in-the-loop escalation

EXPLAINABILITY (XAI) AND DRIFT MITIGATION
  - Every decision logged: decision context, prompts, tool usage, data
    sources, execution trace — "ensuring an audit trail for legal defense"
  - "Drift review": scheduled red-team exercises, human engineers + legal
    specialists, adversarial testing to verify the agent still operates
    within its ORIGINAL actual authority
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-anthropic-zero-trust-ai-agents.md`,
`blog-jetbrains-agentic-ai-governance.md`, `blog-anthropic-agent-identity-access-model.md`,
and `blog-thoughtworks-kamelman-ai-governance-category-error.md` were re-read
directly (MINER.md §4b) and claim numbers below were confirmed against those
notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-jetbrains-agentic-ai-governance.md` Claim 3 ("Agentic systems need
    a defined chain of command — a specific person or function with
    authority over the outcome, who monitors behavior and intervenes when
    the system drifts"): This article's "designated principal" (Claim 5,
    Tier 1) is the same accountability structure under different vocabulary
    — a named human executive, not just a function, legally and
    operationally accountable. Two independent trusted-feed sources converge
    on requiring a specific accountable human for every deployed agent.
  - `blog-jetbrains-agentic-ai-governance.md` Claim 8 ("The solution is to
    design workflows with intentional checkpoints and risk scoring. Let the
    agent handle routine work autonomously, but flag high-impact actions for
    human review"): This article's Tier 2 dynamic escalation ($10,000
    negotiation threshold auto-pausing to a human supervisor, Claim 5) is a
    concrete, numeric operationalization of the same "intentional checkpoint
    with risk scoring" pattern.
  - `blog-jetbrains-agentic-ai-governance.md` Claim 1 ("the question is no
    longer whether it's useful, but what happens when something goes
    wrong"): This article's closing thesis (Claim 11: "The question is not
    whether an AI agent can act on behalf of your organization; it is
    whether you have effectively defined the agent's authority before it
    does") is an independent convergence on the same capability-to-
    accountability reframe from a different practitioner source.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 5 ("least agency" —
    restricting what each agent tool can do, how often, and where): This
    article's "Data No-Go Zones" (Claim 6) apply the same restrict-by-default
    principle specifically to sensitive data repositories for privacy
    compliance, rather than to tool capability generally.
  - `blog-anthropic-agent-identity-access-model.md` Claim 5 (Claude Tag
    agents present as distinct, named identities in each connected system —
    "Claude app," "Claude GitHub App," not a proxied user identity): This
    article's identity-styling requirement (Claim 4 — a "Junior Clerk" vs.
    "VP of Procurement" title carries different apparent authority, and must
    be enforced at the infrastructure layer via metadata/authorization
    policies) describes the same underlying practice (agents need explicit,
    infrastructure-enforced identities) applied to external-party-facing
    legal authority rather than internal system access.

- **Contradicts**:
  - **`blog-thoughtworks-kamelman-ai-governance-category-error.md` Claim 1
    and Claim 2** — filed as **contradiction issue #1730**. That note's
    central thesis (from the same trusted Thoughtworks feed, and Matt
    Kamelman is a co-author of both pieces) is that AI governance debates
    are miscalibrated by a "category error": historical governance analogies
    (industrialization, nuclear weapons, mass media) worked because "the
    thing being governed was external to the governing" and did not modify
    itself, whereas recursively self-improving AI breaks that pattern —
    "locomotives didn't design better locomotives." This article's central
    operating premise (Claim 2 here) is the opposite: "the legal frameworks
    we need have existed for centuries... the challenge is not writing new
    laws; it's creatively and defensively applying the established
    principles of agency law to our digital reality." One argues that
    static, pre-existing frameworks structurally cannot keep pace with
    self-modifying AI; the other confidently deploys a static, centuries-old
    legal framework (agency law) as sufficient, today, for governing AI
    agents. Per MINER.md §4a, no verdict is picked here — see issue #1730
    and the eventual CONTRADICTIONS.md entry for resolution.

- **Extends**:
  - `blog-anthropic-zero-trust-ai-agents.md`: The zero-trust eBook's
    three-tier Foundation/Enterprise/Advanced framework is organized by
    organizational security maturity and covers primarily technical
    controls (identity, credentials, sandboxing). This article's three-tier
    manual/semi-automated/automated framework is organized by *who enforces
    each control* (human policy-author vs. platform) and covers legal/
    liability governance specifically. The two taxonomies are
    complementary axes for the same underlying problem (how much should be
    human-decided vs. platform-enforced) — a Ch06 discussion of agent
    governance maturity could present both taxonomies side by side.
  - `blog-jetbrains-agentic-ai-governance.md`: That article's seven-element
    audit trail specification (Claim 7: initiator, intent, systems/data
    touched, changes made, policy violations, duration, cost) is broader
    than this article's explainability logging spec (Claim 8: decision
    context, prompts, tool usage, data sources, execution trace). This
    article adds the "drift review" practice — a scheduled, joint legal +
    engineering red-team exercise specifically checking whether the agent
    still operates within its *originally granted legal authority* — which
    is a legal-compliance-oriented extension of JetBrains' more general
    drift-detection framing (JetBrains Claim 6: LLM non-determinism as the
    reason audit trails must differ from deterministic-system audit trails).
  - `blog-anthropic-agent-identity-access-model.md`: That source defines
    agent identity for internal/system-facing purposes (which service
    account touched which connected system). This article extends the
    concept of "agent identity" to the external/legal dimension: what a
    third party (vendor, customer, counterparty) reasonably infers about an
    agent's authority from its presented title and disclaimers. Together
    they cover both sides of agent identity: internal system access
    (Anthropic) and external apparent authority (this article).

- **Novel**:
  - **Actual vs. apparent authority as the organizing legal frame for AI
    agent governance** (Claim 3): No prior corpus source frames agent
    governance risk using this specific corporate-law doctrine pair. This
    is a new legal vocabulary contribution to the corpus.
  - **Agent title/styling as an explicit "legal design decision"** (Claim
    4): The framing that what an agent is called and how it presents itself
    carries legal (not just UX) weight, and must be infrastructure-enforced,
    is new to the corpus.
  - **"Data No-Go Zones" as a named term for RBAC applied to agent
    data-privacy compliance** (Claim 6): New terminology in the corpus,
    though the underlying RBAC mechanism is well-established.
  - **The agent-learning/fine-tuning secondary-use question posed as a
    distinct governance decision from data access** (Claim 6): No prior
    corpus source explicitly separates "can the agent access this data?"
    from "can the agent learn from this data?" as two different questions
    organizations must answer.
  - **NLP-scanned contractual "never list" for vendor negotiation** (Claim
    7): A specific, named technical control (forbidden-clause NLP scanning)
    not previously documented in this corpus's governance sources.
  - **"Drift review" as a joint legal+engineering red-team exercise tied to
    original legal authority** (Claim 8): New practice name and scope in
    the corpus — existing drift-detection framing (JetBrains) is technical/
    behavioral, not framed as verifying continued legal authority.
  - **The Andon Labs case study itself** (Claim 1): First appearance of this
    specific case in the corpus as far as this Miner found via cross-
    reference search of existing source notes.

## Guide Impact

- **Chapter 05 (Team Adoption — Organizational Governance)**: Add the
  "designated principal" requirement (Claim 5, Tier 1) as a concrete,
  citable pairing with the JetBrains "chain of command" recommendation
  (`blog-jetbrains-agentic-ai-governance.md` Claim 3) — two independent
  trusted-feed sources now converge on requiring a named, accountable human
  executive for every production agent deployment. Add the three-tier
  manual/semi-automated/automated taxonomy as a legal-governance-oriented
  companion to the zero-trust eBook's technical maturity tiers, explicitly
  noting the different organizing axis (who enforces, not how mature).

- **Chapter 05 (Team Adoption) — Escalation Design**: Add the concrete
  dynamic-escalation example ("negotiate purchases up to $10,000... paused
  and routed to a human supervisor," Claim 5) as a worked numeric example of
  the "intentional checkpoints with risk scoring" pattern already recommended
  from `blog-jetbrains-agentic-ai-governance.md` Claim 8 — this article
  supplies the concrete dollar-threshold mechanism that JetBrains describes
  only abstractly.

- **Chapter 06 (Security/Threat Model — Compliance and Data Boundaries)**:
  Add "Data No-Go Zones" (Claim 6) as a named term for RBAC-based data
  boundary enforcement addressing GDPR/CCPA compliance specifically, as a
  privacy-compliance-flavored companion to the "least agency" concept in
  `blog-anthropic-zero-trust-ai-agents.md` Claim 5. Add the agent-learning/
  fine-tuning secondary-use question (Claim 6) as a governance decision point
  distinct from data access scoping — currently no chapter addresses whether
  an agent may learn from data it has been granted access to.

- **Chapter 06 (Security/Threat Model — Vendor/Contract Risk)**: Add the
  NLP-scanned "never list" (Claim 7) as a candidate technical control for
  agents that negotiate on an organization's behalf, with the caveat (per
  this note's assessment) that the article provides no reliability data for
  the NLP scanning mechanism — flag as an unvalidated but concrete starting
  point, not a proven control.

- **Any chapter discussing agent authority/governance framing generally**:
  Flag the contradiction with `blog-thoughtworks-kamelman-ai-governance-category-error.md`
  (issue #1730) prominently if either source is cited. Do not cite this
  article's "the legal frameworks we need have existed for centuries" premise
  (Claim 2) as an uncontested position — the same trusted feed (and one of
  the same co-authors) has separately argued that static frameworks cannot
  keep pace with recursively self-improving AI. Present both, per SMITH.md's
  `**Debated:**` treatment, once the contradiction is resolved.

## Extraction Notes

1. **WebFetch returned an AI-summarized version on first attempt; full
   verbatim text was obtained via direct HTML fetch.** A first WebFetch call
   against the source URL returned only a condensed summary (paraphrased
   section headers, no verbatim quotable text). To satisfy MINER.md §2a's
   verbatim-quote requirement, the article's raw HTML was fetched directly
   (`curl` with a standard browser user agent, HTTP 200) and the article
   body text was extracted from the rendered HTML by stripping markup. The
   resulting text reads as a complete, internally consistent article: byline
   (Jeremy Gordon, Matt Kamelman), "Published: June 18, 2026," full body
   copy through the closing acknowledgment ("Thanks to Juliana Reis for
   contributing valuable research that informed both this article and the
   framework"), and the standard article-footer pull-quote repeated twice
   (a page-templating artifact, not a content duplication). All quotes above
   are copied character-for-character from this extracted HTML text. The
   Assayer should spot-check quotes against the live URL; if the page has
   since changed (e.g., paywalled or edited), the raw HTML used for this
   extraction is not preserved outside this session.

2. **The "nine blocks" of the interactive assessment tool are not
   enumerated anywhere in the article body** (see Claim 10). This Miner
   did not attempt to access the interactive tool itself (not linked with a
   direct URL in the fetched article text, and likely gated/interactive
   rather than a static page). Guide content should not assume a specific
   nine-part structure beyond what is named in the article body (which
   describes at most six to seven named framework components).

3. **No sub-pages followed.** The article is self-contained; no inline
   links to further Thoughtworks framework documentation, the interactive
   assessment tool, or external legal/regulatory sources were present in the
   extracted text (links may have been stripped by the HTML-to-text
   extraction, consistent with the pattern noted in
   `blog-thoughtworks-kamelman-ai-governance-category-error.md`'s
   Extraction Notes for the same publication's article template).

4. **Contradiction filed before this PR was opened**: Per MINER.md §4a,
   contradiction issue **#1730** was filed prior to writing this note,
   documenting the tension between this article's Claim 2 and
   `blog-thoughtworks-kamelman-ai-governance-category-error.md` Claims 1–2.
   No verdict is asserted in this note; the contradiction awaits human/Smith
   resolution and a CONTRADICTIONS.md entry.

5. **Overall confidence rated "emerging."** The corporate-law doctrine
   underlying the framework (actual vs. apparent authority) is settled law
   in general; its specific application to autonomous AI agents, the
   three-tier oversight taxonomy, and every named technical control
   (Data No-Go Zones, NLP "never list," drift review) are this article's own
   proposed framework, presented with one illustrative case study (Andon
   Labs) and no adoption, outcome, or reliability data. Several claims
   (Claims 1, 2, 9, 10) are rated "anecdotal" individually — the overall
   confidence reflects that this is a credible practitioner's newly proposed
   framework, not a validated or widely-adopted governance standard.
