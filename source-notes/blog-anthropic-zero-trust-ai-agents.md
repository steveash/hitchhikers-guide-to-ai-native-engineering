---
source_url: https://claude.com/blog/zero-trust-for-ai-agents
source_type: blog-post
title: "Zero Trust for AI Agents"
author: Anthropic (Claude Security team)
date_published: 2026-05-27
date_extracted: 2026-05-28
last_checked: 2026-05-28
status: current
confidence_overall: emerging
issue: "#976"
---

# Zero Trust for AI Agents

> Anthropic's first-party 35-page security framework for deploying autonomous AI agents in the enterprise — a comprehensive treatment of agentic threat taxonomy, a three-tier Zero Trust architecture (Foundation/Enterprise/Advanced) mapped to organizational maturity, an eight-phase implementation workflow, and a novel "Agentic SOAR" concept for defensive operations at the speed of autonomous threats.

## Source Context

- **Type**: blog-post + companion eBook PDF (Anthropic official, claude.com blog, May 27, 2026;
  the blog page is a teaser; all substantive content lives in a freely-accessible PDF at
  `https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a1611a04085d7cd3dadc924_Claude-eBook-Zero-Trust-for-AI-Agents-05182026.pdf`.
  The PDF was downloaded and read in full — all claims and quotes below are extracted verbatim
  from the PDF, not the blog teaser.)
- **Author credibility**: Anthropic first-party security guidance. The PDF is explicitly
  positioned as "Anthropic's current thinking on agent security architecture." The coverage
  is comprehensive (35 pages, 5 parts), cites OWASP, Microsoft Research, Anthropic's own
  research (250-document LLM backdoor finding), and links to live government frameworks (NIST,
  NSA ZIGs, CISA). Unlike marketing materials, the document acknowledges limitations ("offered
  as a framework for your own evaluation, not as legal, compliance, or security assurance for
  any particular environment"). Authority is very high for claims about Claude-specific tooling
  (Claude Code pro-tips throughout); emerging for claims about third-party threat research
  (attributed but not independently reviewed by this corpus).
- **Scope**: Covers Zero Trust principles and their application to agentic AI specifically:
  (1) security properties unique to agentic systems, (2) agentic threat taxonomy (prompt
  injection, tool poisoning, identity abuse, memory poisoning, supply chain attacks), (3)
  three-tier architecture with per-capability Foundation/Enterprise/Advanced tables, (4) an
  eight-phase implementation workflow, (5) defensive operations including Agentic SOAR, MITRE
  ATT&CK mapping, and tabletop exercises. Does NOT cover: specific product pricing, deployment
  timelines, or code-level SDK guidance beyond pro-tips. Regulated industry guidance (HIPAA,
  FINRA, GDPR, FedRAMP, EU AI Act) is mentioned but not detailed within the PDF.

## Extracted Claims

### Claim 1: Frontier AI compresses the vulnerability-to-exploit timeline from months to hours, making the threat acceleration relevant to both infrastructure and agent deployment

- **Evidence**: Anthropic's first-party framing as the opening thesis of the document, consistent
  with their April 2026 Project Glasswing research (referenced in blog-anthropic-ai-accelerated-offense.md).
- **Confidence**: emerging (authoritative first-party claim from the model maker; no independently
  published timeline data cited in this document)
- **Quote**: "Frontier AI models are compressing the timeline between vulnerability and exploit
  from months to hours, at a marginal cost measured in dollars."
- **Our assessment**: This matches the April 2026 blog post's "24-month countdown" framing,
  but with a more acute formulation: months-to-hours rather than months-to-soon. The
  "marginal cost measured in dollars" clause is significant — it removes the economic barrier
  that limited sophisticated attacks to nation-state actors. For guide purposes: this is the
  opening threat claim that justifies the urgency of the entire framework.

### Claim 2: AI agents face dual exposure — they run on infrastructure exposed to AI-accelerated attack AND introduce new autonomous decision-making risks that traditional controls cannot address

- **Evidence**: Central structural claim of the eBook's introduction; no single empirical backing,
  but supported throughout the document with specific threat categories.
- **Confidence**: settled (logically derived from agent properties; first-party Anthropic framing)
- **Quote**: "This speed-up matters twice for any organization deploying agents. First, the
  infrastructure your agents run on is exposed to AI-accelerated offense like the rest of your
  estate. Second, the agents themselves introduce autonomy to interpret goals, select tools, and
  execute multi-step operations. Traditional access controls won't prevent agents from misusing
  legitimate permissions, and monitoring needs to account for attacks designed to succeed through
  persistence rather than exploitation."
- **Our assessment**: The "twice" framing is new to the corpus. Prior notes (blog-anthropic-ai-accelerated-offense.md)
  addressed the infrastructure side; this document is the first to provide a comprehensive
  treatment of both together. "Attacks designed to succeed through persistence rather than
  exploitation" is a particularly sharp observation — agent compromise succeeds by patient
  accumulation of legitimate actions, not by triggering security alerts.

### Claim 3: The "impossible vs. tedious" test is the definitive design criterion — controls whose value comes only from friction fail against agentic attackers

- **Evidence**: Stated as a design principle applied to every capability in the document's
  tier tables. Supported by the observation about agentic attacker properties.
- **Confidence**: emerging (sound security engineering principle; first-party framing for agentic
  context; no empirical validation data cited)
- **Quote**: "When you evaluate any control in this document, ask a single question: does this
  make the attack impossible, or just tedious? Mitigations whose value comes from friction rather
  than a hard barrier — including extra pivot hops, rate limits, non-standard ports, and SMS-based
  MFA — degrade significantly against an adversary that can grind through tedious steps at scale.
  Agentic attackers have unlimited patience and near-zero per-attempt cost."
- **Our assessment**: This is the most actionable single design heuristic in the document. It
  directly disqualifies a large class of commonly recommended controls (rate limits, non-standard
  ports, SMS MFA) as insufficient in the agentic threat model. For the guide: use this test as
  the evaluative standard in any security architecture section. Friction-based controls buy time;
  they cannot be the primary defense.

### Claim 4: The controls that survive the "impossible vs. tedious" test share a pattern: hardware-bound credentials, expiring tokens, cryptographic identity, and network paths that do not exist

- **Evidence**: Derived from Claim 3's principle; the specific pattern is stated as the design
  implication.
- **Confidence**: settled (established security engineering best practices; not novel, but clearly
  articulated in the agentic context)
- **Quote**: "The controls that survive this test share a pattern: hardware-bound credentials,
  expiring tokens, cryptographic identity, and network paths that do not exist rather than paths
  that are merely inconvenient. This test informs every tier recommendation in this document.
  When in doubt, prefer a control that removes a capability over a control that throttles it."
- **Our assessment**: "Prefer a control that removes a capability over a control that throttles
  it" is a memorable formulation of the principle that should anchor guide recommendations on
  security architecture. This directly implies: block network paths by not creating them, not
  by rate-limiting them; issue tokens that expire in minutes, not tokens that rotate weekly.

### Claim 5: "Least agency" (OWASP-coined term) extends least privilege specifically to agentic systems — constraining what each agent tool can do, how often, and where

- **Evidence**: Attributed to OWASP; described as "a new term coined by OWASP." Used throughout
  the document's architecture tables.
- **Confidence**: settled (OWASP attribution; the concept is sound and well-illustrated)
- **Quote**: "Least agency, a new term coined by OWASP, extends least privilege to agentic
  applications. Where least privilege constrains what users and systems can access, least agency
  goes further, restricting what each agent tool can do, how often, and where. In practice: a
  database tool gets read-only queries, an email summarizer gets no send/delete rights, an API
  gets minimal CRUD operations."
- **Our assessment**: This is the correct conceptual extension of least privilege for agentic
  contexts, and the term "least agency" is specific enough to anchor guide content. The three
  concrete examples (database read-only, email summarizer no-send, API minimal CRUD) are exactly
  the implementation-level specificity that practitioners need. This should be a named concept
  in any harness engineering chapter.

### Claim 6: A compromised MCP stack enables data theft, malicious code execution, and sabotage — the first documented in-the-wild malicious MCP server impersonated a legitimate email service

- **Evidence**: Two distinct evidence points: (a) first-party architectural assessment of MCP
  compromise risk; (b) citation of a documented real-world case.
- **Confidence**: emerging (first-party risk framing; real-world case cited but not linked to
  a named CVE or published report)
- **Quote**: "Tool access allows agents to interact with APIs, databases, file systems, and
  external services. This includes Model Context Protocol (MCP), which standardizes how agents
  connect to these resources. A compromised MCP stack can lead to data theft, malicious code
  execution, and sabotage."
- **Quote** (in-the-wild case): "The first documented in-the-wild malicious MCP server
  impersonated a legitimate email service and secretly copied all sent emails."
- **Our assessment**: The in-the-wild MCP server compromise is the first concrete production
  threat case for MCP in this corpus. Its mechanism (impersonation + silent exfiltration) is
  harder to detect than direct attack: the agent performed a legitimate-looking action (sending
  email) while the malicious server silently copied it. For guide purposes: MCP server
  provenance verification belongs in any production MCP deployment guidance.

### Claim 7: Indirect prompt injection is more insidious than direct injection because LLMs cannot reliably distinguish between informational context and actionable instructions

- **Evidence**: Attributed to Microsoft Research.
- **Confidence**: settled (attributed to Microsoft Research; widely corroborated in academic
  literature on prompt injection)
- **Quote**: "Indirect prompt injection presents the more insidious threat. Attackers embed
  malicious instructions in external data sources that agents process, such as web pages or
  emails. Microsoft Research confirms that LLMs cannot reliably distinguish between informational
  context and actionable instructions. The user never sees the malicious payload, and the agent
  executes it as if it were a legitimate request."
- **Our assessment**: The "user never sees the malicious payload" clause is the key threat
  property: indirect injection bypasses all user-review-based defenses because the malicious
  instruction is in the data, not in the user's message. Combined with agents that process web
  pages, documents, and emails autonomously, this makes indirect injection the dominant threat
  surface. Guides that recommend "have a human review agent inputs" as the primary defense
  are inadequate.

### Claim 8: Algorithmic direct prompt injection approaches can achieve 100% attack success rates with prompts that transfer across multiple model families

- **Evidence**: "Research shows" — source not named but cited as a known result.
- **Confidence**: emerging (cited as established research finding but no specific paper named;
  plausible given published adversarial suffix research)
- **Quote**: "Research shows algorithmic approaches can achieve 100% attack success rates with
  prompts that transfer across multiple model families."
- **Our assessment**: "100% attack success rates" is alarming and, if accurate, implies that
  any agent receiving unconstrained user input is fully exploitable by a motivated attacker.
  The "transfer across model families" clause is particularly concerning because it means defenses
  trained on one model provide no protection when switching models. This motivates the
  environmental control priority over model-layer defenses (consistent with
  blog-anthropic-how-contain-claude.md Claim 3).

### Claim 9: Tool chaining attacks combine legitimate tools in harmful sequences — host-centric monitoring cannot detect them because every command executes through trusted binaries under valid credentials

- **Evidence**: Described as a threat pattern with a specific example.
- **Confidence**: emerging (well-described threat pattern; specific example provided; no
  independently cited published research)
- **Quote**: "Tool chaining attacks present a more subtle threat. Attackers trick agents into
  combining legitimate tools in harmful sequences: chaining a secure internal CRM tool with an
  external email tool to exfiltrate customer data that neither tool would expose alone. Because
  every command executes through trusted binaries under valid credentials, host-centric monitoring
  sees no malware and the misuse goes undetected."
- **Our assessment**: "Host-centric monitoring sees no malware" is the critical observation:
  tool chaining attacks are invisible to traditional security monitoring. The agent is doing
  exactly what it's authorized to do — each individual tool call is legitimate — but the
  sequence is malicious. This motivates behavioral monitoring and traceability (connecting
  individual actions into complete sequences) rather than just action logging.

### Claim 10: Injecting 250 malicious documents can backdoor LLMs ranging from 600M to 13B parameters, with backdoors persisting through safety training including supervised fine-tuning and RLHF

- **Evidence**: Attributed to "Anthropic research" — first-party.
- **Confidence**: emerging (first-party Anthropic research finding; specific numbers cited; not
  linked to a published paper in this document, but corroborates known published Anthropic
  safety research)
- **Quote**: "Anthropic research demonstrates that injecting just 250 malicious documents can
  successfully backdoor LLMs ranging from 600 million to 13 billion parameters, and these
  backdoors persist through safety training including supervised fine-tuning and RLHF."
- **Our assessment**: The 250-document threshold is remarkably low — it suggests that model
  supply chain poisoning doesn't require compromising the training pipeline at scale. A
  relatively small RAG corpus poisoning or training data contamination event could introduce
  persistent backdoors that survive standard mitigation (RLHF, SFT). For teams using RAG
  systems or building custom fine-tuned models: this result implies that corpus integrity
  verification is a security-critical practice, not just a data quality concern.

### Claim 11: The three-tier Zero Trust framework (Foundation/Enterprise/Advanced) maps to organizational maturity, with the Foundation floor explicitly raised above friction-only controls due to AI-accelerated offense

- **Evidence**: Core structural claim of Part III; the tier definitions and their rationales
  are stated explicitly.
- **Confidence**: settled (first-party Anthropic framework design; tier definitions are clear
  and internally consistent)
- **Quote**: "Foundation represents the minimum viable security appropriate for smaller deployments
  or initial implementations. Because AI-accelerated offense has compressed exploitation timelines,
  the Foundation floor has been raised: friction-only controls no longer qualify."
- **Quote** (Enterprise): "Enterprise is where most organizations should aim. This tier takes
  the Foundation controls and adds the depth needed to handle real-world complexity: larger
  teams, multiple agentic deployments, and environments where a single compromise carries
  meaningful business impact."
- **Quote** (trajectory): "Expect the Advanced tier to become Enterprise standard as the space
  evolves, and Enterprise to become Foundation."
- **Our assessment**: The explicit upward pressure on the Foundation floor is important for
  guide framing: what was aspirational in 2024 is now the minimum for 2026. "Friction-only
  controls no longer qualify" directly disqualifies commonly recommended practices (SMS MFA,
  rate limits, non-standard ports) from the minimum bar. The tier progression ("Advanced
  becomes Enterprise becomes Foundation") establishes that this is a moving baseline, not a
  fixed standard.

### Claim 12: Static API keys and shared service-account passwords are no longer a legitimate Foundation posture — short-lived tokens are now the minimum baseline

- **Evidence**: Directly stated in the service authentication section.
- **Confidence**: settled (first-party prescriptive guidance; consistent with industry direction)
- **Quote**: "Static API keys and shared service-account passwords are among the first things
  an attacker with model-assisted code analysis will find; they are no longer a legitimate
  entry point, not even at Foundation. Short-lived, narrowly-scoped tokens issued by an identity
  provider are the new baseline."
- **Quote** (extended): "If you are running API keys with rotation policies today, treat it
  as a known gap rather than a legitimate Foundation posture. Rotating a credential that can
  be grepped out of a lockfile does not raise the cost to an AI-assisted attacker meaningfully.
  Move to short-lived tokens first, and bind credentials to hardware wherever you can."
- **Our assessment**: "A credential that can be grepped out of a lockfile does not raise the
  cost to an AI-assisted attacker meaningfully" is a precise and accurate statement. API key
  rotation creates an ongoing operational burden while providing minimal security benefit
  against an automated attacker that can recheck credentials continuously. This is the most
  concrete and immediately actionable security advice in the document.

### Claim 13: Microsoft's Spotlighting technique reduces indirect prompt injection attack success from over 50% to under 2%

- **Evidence**: Attributed to Microsoft's Spotlighting technique.
- **Confidence**: emerging (attributed to Microsoft Research; specific efficacy numbers cited;
  not linked to a specific published paper in this document)
- **Quote**: "Microsoft's Spotlighting technique reduces indirect injection attack success from
  over 50% to under 2% by clearly delimiting untrusted content."
- **Our assessment**: A 25x reduction in attack success rate (>50% → <2%) is the most
  concrete mitigation efficacy claim in the document. Spotlighting works by clearly marking
  the boundaries between trusted instructions and untrusted external content, allowing the
  model to treat external content as data rather than instructions. For guide purposes: this
  is the single input-isolation technique with the strongest published efficacy data.

### Claim 14: Anthropic's constitutional classifiers blocked 95% of jailbreak attempts in testing with minimal increase in over-refusal rates

- **Evidence**: Attributed to Anthropic's own research on constitutional classifiers.
- **Confidence**: emerging (first-party Anthropic claim; specific efficacy number cited;
  "minimal increase in over-refusal rates" is an important qualifier)
- **Quote**: "Constitutional classifiers provide an additional detection layer. These AI-based
  systems scan prompts and responses for manipulation attempts. Anthropic's approach blocked
  95% of jailbreak attempts in testing with minimal increase in over-refusal rates."
- **Our assessment**: 95% jailbreak blocking is high but not 100% — meaning 1 in 20 attempts
  passes through. For high-volume agents (processing thousands of messages daily), 5% pass-through
  represents meaningful attack exposure. The "minimal over-refusal" qualifier is important:
  it means the classifier doesn't simply refuse everything, which would make the agent
  useless. The combination of constitutional classifiers (catch sophisticated attacks) and
  Spotlighting (delimit untrusted content) provides complementary coverage.

### Claim 15: "Automate the bookkeeping around incidents, not the decisions" — models handle evidence collection and documentation, humans retain containment and disclosure decisions

- **Evidence**: Stated as an explicit design rule for automated incident response.
- **Confidence**: settled (first-party Anthropic design principle; consistent with the human/AI
  work-split pattern documented across the corpus)
- **Quote**: "A clear rule applies here: automate the bookkeeping around incidents, not the
  decisions. Models should take notes, capture artifacts, pursue parallel investigation tracks,
  and draft the postmortem. Humans should make the containment calls, the disclosure calls, and
  the customer-comms calls."
- **Quote** (related): "Human decision speed during an incident should never be rate-limited
  on evidence collection or write-ups."
- **Our assessment**: This is the clearest articulation of the human/AI work split for incident
  response in the corpus — more specific than prior sources. "Containment calls, disclosure calls,
  and customer-comms calls" are the three categories reserved for human judgment. This maps
  directly to the automated response tier table (Foundation: alerting + model-drafted triage
  context; Enterprise: automatic containment for high-confidence threats; Advanced: SOAR with
  graduated escalation).

### Claim 16: Agentic SOAR extends traditional SOAR with adaptive capabilities that respond to novel situations and can directly address malicious AI-driven attacks within seconds

- **Evidence**: Described in Part V as the "next generation of SOAR."
- **Confidence**: emerging (forward-looking description of an emerging category; no named
  Agentic SOAR products are cited; the concept is coherent and architecturally sound)
- **Quote**: "The next generation of SOAR is Agentic SOAR, which adds adaptive capabilities
  that respond to novel situations. This allows flexibility beyond existing playbooks and the
  adaptability to directly address malicious AI-driven attacks within seconds."
- **Our assessment**: "Within seconds" vs. the days or hours of traditional SOAR response is
  the key claim. Agentic SOAR achieves speed by removing human-in-the-loop from the detection-
  and-initial-response steps, while keeping humans on consequential decisions (containment,
  disclosure). The document explicitly requires applying the same Zero Trust principles to
  defensive agents as to production agents — "organizations should not blindly trust defensive
  automation any more than they trust other autonomous systems."

### Claim 17: The US requires all federal agencies to adopt Zero Trust by 2027, with aligned guidance from Australia, UK, and US governments

- **Evidence**: Direct statement about government mandates.
- **Confidence**: settled (verifiable government policy; consistent with known CISA/NSA/OMB
  Zero Trust requirements)
- **Quote**: "The United States, United Kingdom, and Australian governments have already
  published Zero Trust guidance, with the US requiring all federal agencies to adopt Zero
  Trust by 2027."
- **Our assessment**: The 2027 federal mandate creates regulatory urgency. For the guide's
  enterprise audience, this means Zero Trust adoption is not optional for federal contractors
  and government-adjacent organizations. The compliance alignment section (HIPAA, FINRA,
  GDPR, FedRAMP, EU AI Act) makes clear that Zero Trust framework adoption satisfies a broad
  range of regulatory requirements simultaneously.

### Claim 18: The eight-phase implementation workflow provides a repeatable process for deploying agents securely, from requirements through measurement

- **Evidence**: Detailed in Part IV across eight explicitly named phases.
- **Confidence**: settled (first-party Anthropic prescriptive guidance; each phase is
  substantively described)
- **Quote**: "Successful agent implementation requires a defined, repeatable process built on
  the security architecture above. Each phase addresses specific security controls while
  mitigating the identified threats."
- **Our assessment**: The eight-phase structure is a novel contribution to the corpus — no
  other source provides an ordered implementation workflow at this level of specificity for
  agentic security deployment. The phases are ordered by dependency: you cannot scope access
  (Phase 3) until you have identified requirements (Phase 1) and managed supply chain risks
  (Phase 2); you cannot protect credentials (Phase 6) until you have secured tool access
  (Phase 5). The ordering matters as much as the content.

### Claim 19: Identity-based isolation is the primary control for resource boundaries — network segmentation is a backstop, not the primary boundary

- **Evidence**: Explicitly stated as an architectural design decision in the resource boundaries section.
- **Confidence**: settled (first-party architectural guidance; consistent with Zero Trust
  principles generally)
- **Quote**: "Identity-based isolation is the primary control. Network segmentation can still
  reduce blast radius and noise, but it is a backstop: an attacker who can reach a segment
  boundary will pivot through it if the services on the other side accept any caller from
  that network. Enforce isolation at the receiving end — every workload carries its own
  cryptographic identity, and each service accepts connections only from the specific callers
  its policy names."
- **Our assessment**: This inverts the traditional security priority (network segmentation
  first) for agentic deployments. Network segmentation stops network-level attackers; it
  does not stop a compromised agent that already has legitimate network access. Identity-based
  isolation stops the compromised agent from reaching services it isn't authorized to call,
  even if it's on the same network. For harness designers: implement cryptographic service
  identity before or in parallel with network segmentation, not after it.

### Claim 20: The two metrics that matter most for agent security — dwell time and coverage — are exactly where AI automation has the greatest leverage

- **Evidence**: Stated as a priority principle before the behavioral monitoring sections.
- **Confidence**: emerging (sound operational principle; no published benchmark data cited
  comparing AI-augmented vs. human-only on these specific metrics)
- **Quote**: "Before investing anywhere else in detection, instrument two things: dwell time
  (how long between an anomaly occurring and a human becoming aware of it) and coverage (the
  fraction of alerts that actually get investigated). These are the two metrics AI-assisted
  automation has the greatest leverage to move, and they matter most when exploit windows
  shorten."
- **Our assessment**: This provides a decision framework for where to apply AI in security
  operations. Dwell time and coverage are the correct top-level metrics because they
  measure both speed of response and completeness of investigation — the two dimensions
  most affected by the AI threat acceleration. For guide impact: these two metrics should
  anchor any chapter section on security operations instrumentation.

## Concrete Artifacts

### Zero Trust Three-Tier Architecture (Foundation/Enterprise/Advanced)

```
Zero Trust for AI Agents — Three-Tier Framework (Anthropic, May 2026)
Source: PDF pp. 13-21

FOUNDATION — Minimum viable security for smaller deployments/initial implementations.
"The Foundation floor has been raised in response to AI-accelerated offense:
friction-only controls no longer qualify."
  Identity: Unique cryptographic identifiers per agent instance
  Service auth: Short-lived tokens (OAuth 2.0, minutes-expiry); NEVER embedded credentials
  Permissions: RBAC with deny-by-default
  Privilege: Static least-privilege roles per agent function
  Isolation: Identity-based isolation backed by network segmentation
  Logging: Comprehensive logs with timestamps and context
  Tracing: Request IDs linking agent actions to triggering events
  Baselines: Manually documented expected behavior patterns
  Anomaly: Threshold-based alerts with automated first-pass triage
  Response: Alerting to security teams with model-drafted triage context
  Input: Basic validation and length limits
  Output: Pattern-based sensitive data filtering
  Config: Version-controlled agent configurations
  Recovery: Documented rollback procedures
  Governance: Documented acceptable use and incident response policies

ENTERPRISE — Target maturity for most organizations with significant deployments.
  Identity: X.509 certificate-based with full lifecycle management
  Service auth: Mutual TLS with certificate pinning
  Permissions: ABAC with context-aware policies (time, location, data sensitivity, risk score)
  Privilege: Dynamic privilege adjustment per task (elevate → baseline → return)
  Isolation: Sandboxed execution environments (containers, gVisor syscall filtering)
  Logging: Immutable audit trails with cryptographic integrity verification
  Tracing: OpenTelemetry distributed tracing across multi-agent workflows
  Baselines: Automated baseline learning from normal operations
  Anomaly: Statistical anomaly detection with tunable sensitivity
  Response: Automatic containment for high-confidence threats (session termination, revocation)
  Input: Content filtering with known attack pattern detection
  Output: Semantic analysis before delivery
  Config: Signed configurations with deployment verification
  Recovery: Automated rollback with health checks
  Governance: Formal governance framework with cross-functional committee (security, legal,
               compliance, business)

ADVANCED — Aspirational for most; baseline for high-risk/regulated environments.
  Identity: HSM/TPM-backed with remote attestation; confidential computing enclaves
  Service auth: Hardware-bound credentials with attested issuance
  Permissions: Continuous authorization with real-time policy evaluation at each action
  Privilege: Just-In-Time (JIT) / Just-Enough-Administration (JEA) with automatic expiration
  Isolation: Hardware isolation (AMD SEV, Intel TDX); microVM architectures
  Logging: Real-time streaming to SIEM with correlation capabilities
  Tracing: Full provenance chains from input to output with intermediate steps
  Baselines: Continuous baseline refinement with drift detection
  Anomaly: ML-based behavioral analysis with contextual awareness
  Response: Orchestrated SOAR playbooks with graduated escalation
  Input: Multi-layer validation with constitutional classifiers and spotlighting
  Output: Human-in-the-loop approval for high-risk actions
  Config: Immutable infrastructure with attestation
  Recovery: Self-healing systems with automatic remediation
  Governance: Continuous policy enforcement with automated compliance checking
```

### Eight-Phase Agent Implementation Workflow

```
Zero Trust Agent Implementation Workflow (Anthropic, May 2026)
Source: PDF pp. 22-30

Phase 1: IDENTIFY REQUIREMENTS
  - Regulatory requirements (HIPAA, FINRA, GDPR, FedRAMP, EU AI Act)
  - Operational goals and constraints
  - Stakeholder alignment: security, legal, compliance, business — before you build

Phase 2: MANAGE SUPPLY CHAIN RISKS
  - AI Bill of Materials (AI-BOM): model provenance, training dataset lineage, fine-tuning params
  - OpenSSF Scorecard: automated dependency health scoring in CI
  - Dependency tree audit: frontier model reviewing lockfile for redundant libraries
  - Reachability analysis: remediate only vulnerable code that is actually reachable
  - AI vendoring: for unmaintained deps that score poorly, have a frontier model reimplement
    the subset of functionality actually used — "Treat this as a standard response to an
    unhealthy dependency, not an exotic workaround."
  - Cryptographic signing: sign models and software at every stage through production deployment
  - Vendor assessments: explicitly ask suppliers how they are preparing for AI-accelerated
    exploit timelines and whether they are scanning their own code
  - Pro-tip for MCP: "Run/host the MCP server yourself, on an immutable platform, after you
    have verified the code. Cryptographically sign it yourself."

Phase 3: DEFINE AGENT BOUNDARIES
  - Assign unique cryptographically rooted identity per agent instance
  - Document approved/prohibited actions explicitly (write it down, not implied)
  - Define escalation triggers: high-value transactions, sensitive data categories,
    external party communications
  - Apply scope limits / least agency: deny-by-default at all times
  - Identify blast radius with "impossible vs. tedious" test: "If your containment plan
    relies on friction — assume it will fail."
  - Compartmentalization: "break up some of the functions/goals of an agent into multiple
    agents" — each with unique ID and own credentials

Phase 4: DEFEND AGAINST PROMPT INJECTION
  - Input isolation: treat all natural-language inputs as untrusted
  - Microsoft Spotlighting: reduces indirect injection from >50% to <2%
  - Constitutional classifiers: additional detection layer (Anthropic: 95% jailbreak blocking)
  - Limit attack surfaces: limit who or what can interact with the agentic system

Phase 5: SECURE TOOL ACCESS
  - Tool allow-listing: explicit lists of permitted tools per agent function; deny unlisted tools
  - Require tool authentication: certificate-based or short-lived tokens bound to calling
    agent identity; "Static API keys are not acceptable for tool authentication, even at Foundation"
  - Capability restrictions: limit what permitted tools can do
  - Parameter validation: validate tool call arguments before execution (on both agent and tool side)
  - Sandbox execution: container sandboxes and/or microVMs with restricted network, limited
    filesystem, syscall filtering
  - Approval escalation: pause and require human review for high-risk tool invocations

Phase 6: PROTECT AGENT CREDENTIALS
  - Short-lived, identity-provider-issued credentials as baseline (expiring in minutes)
  - Certificate-based identity with CA enrollment, short-lived certs, CRL/OCSP validation
  - Hardware-bound credentials for production: phishing-resistant FIDO2/passkeys for human auth;
    "SMS-based codes do not meet the Foundation bar"
  - Credential isolation: per-agent unique credentials; inject at runtime from secrets management
    "Credentials should never appear in code or configuration files"
  - Explicit trust boundaries in multi-agent systems: verify identity and authorization of
    other agents before accepting delegated tasks; log all inter-agent communications
  - JIT access: "Token lifetimes should be measured in minutes rather than hours or days"

Phase 7: SAFEGUARD AGENT MEMORY
  - Memory isolation: strict session/user boundaries; "Each session starts with fresh context"
  - Context integrity validation: cryptographic hashes detect unauthorized modification;
    source attribution tracks origin; validate at every retrieval, not just storage
  - Retention policies: time-to-live values; shorter for high-risk context (external inputs,
    unverified tool outputs); versioned memory stores for rollback to known-good states
  - When poisoning detected: quarantine suspected content; test rollback procedures before incidents

Phase 8: MEASURE WHAT MATTERS
  - Instrument first: dwell time (anomaly to human awareness) and coverage (fraction investigated)
  - Explainability: "would we know within an hour if an agent went rogue?"
  - Behavioral conformance: establish baselines during controlled deployment; measure drift
  - Key indicators: tool usage patterns, output characteristics, decision distributions
  - Detection speed target: "within an hour for critical systems"
```

### Threat Taxonomy for Agentic Systems (Part II)

```
Agentic Threat Taxonomy (Anthropic, May 2026)
Source: PDF pp. 9-11

PROMPT INJECTION
  Direct: Instruction overrides, Base64/hex encoding to bypass filters, adversarial suffixes
          — algorithmic approaches achieve 100% attack success rates, transfer across model families
  Indirect: Malicious instructions in web pages, emails, external data
          — Microsoft Research: LLMs cannot reliably distinguish context from actionable instructions
          — User never sees the payload; agent executes as if legitimate

TOOL AND RESOURCE MISUSE
  Tool poisoning: Compromise MCP tool descriptors/schemas/metadata; agent invokes based on
                  falsified capabilities
  Rug pull attacks: Legitimate tool secretly replaced with malicious version
  In-the-wild case: "The first documented in-the-wild malicious MCP server impersonated
                     a legitimate email service and secretly copied all sent emails."
  Tool chaining: Combining legitimate tools in harmful sequences (CRM + email = data exfiltration)
                 — host-centric monitoring sees no malware because commands use trusted binaries
  Resource exhaustion: Loop amplification causes repeated costly API calls

IDENTITY AND PRIVILEGE ABUSE
  Unscoped privilege inheritance: High-privilege manager passes full access context to worker agents
  Confused deputy: Compromised low-privilege agent relays instructions to high-privilege agent
  Memory-based privilege retention: Agents cache credentials; attacker exploits cached secrets
                                    from prior secure sessions across session boundaries

SUPPLY CHAIN RISKS
  Model supply chain: Poisoned weights, compromised fine-tuning data — 250 documents can backdoor
                       LLMs from 600M to 13B parameters, persisting through SFT and RLHF
  Tool/framework supply chain: PyTorch dependency confusion attack; ~100 malicious AI models
                                 discovered on major platforms including reverse shell models
  Dependency accumulation: Multiple libraries doing the same job, each adding attack surface

MEMORY AND CONTEXT POISONING
  RAG poisoning: Malicious data in vector databases through poisoned sources or direct uploads
  Shared context poisoning: Multi-tenant environments where one session's poisoned context
                              affects later sessions
  Long-term memory drift: Gradual shift in stored knowledge or goal weighting — "difficult to
                            detect because no single change appears malicious"
```

### Agentic SOAR Rollout Pattern

```
Practical Agentic SOAR Implementation (Anthropic, May 2026)
Source: PDF p. 32

Step 1: Start with one high-noise, high-false-positive rule
Step 2: Wire a frontier model into its alert stream with read-only access to underlying data
Step 3: Have the model produce a structured disposition (query → think → report) for every firing
Step 4: Measure agreement against a human reviewer for two weeks
Step 5: If agreement rate is tolerable, expand to the next rule
        "Do not try to automate the whole queue at once."

Automated response categories (executed through identity-based isolation and short-lived credentials):
  - Automated quarantine or isolation (network or system level)
  - Dynamic access control adjustments (user or resource level)
  - Session termination
  - Credential revocation

Trust requirements for defensive agents (same Zero Trust as production agents):
  - Verified integrity of SOAR systems themselves
  - Limited blast radius: "Even trusted defensive systems should operate with least privilege"
  - Clear escalation paths: "High-impact responses should require human approval even when
    automated systems recommend them"
```

### Claude Code Zero Trust Pro-Tips (as shipped features)

```
Claude Code Zero Trust Feature Map (Anthropic, May 2026)
Source: PDF pp. 16-21 (Pro-tip boxes)

Resource Boundaries / Sandboxing:
  - Deny-by-default permissions requiring explicit approval for every write and execute operation
  - OS-level filesystem and network isolation
  - Write access restrictions confining modifications to the project directory
  - Managed settings: administrators enforce organization-wide permission policies users cannot override

Traceability:
  - OpenTelemetry metrics for tracking and auditing agent activity
  - Audit logging for all operations in cloud environments
  - Natural language descriptions of complex commands for human-readable traceability
  - ConfigChange hooks that audit or block settings changes during sessions
  - Unique session.id per session, with user.account_uuid and organization.id on all telemetry events

Behavioral Monitoring:
  - Command injection detection flagging suspicious commands even when matching allowlisted patterns
  - Fail-closed matching defaulting unrecognized commands to manual approval
  - Context-aware analysis detecting potentially harmful instructions by analyzing the full request

Input/Output Controls:
  - Input sanitization preventing command injection
  - Command blocklist blocking risky commands (curl, wget) by default
  - Isolated context windows processing web content in a separate context
  - Network request approval gating all outbound connections

Credential Protection:
  - OAuth 2.0 authentication with automatic token refresh for MCP server connections
  - Session-scoped permissions for "ask"-configured tools, expiring at session end
  - API credentials stored in OS credential store rather than configuration files
  - apiKeyHelper setting executing a script at runtime to retrieve secrets from external vaults

Memory Safeguards:
  - Session isolation by default: each session starts with fresh context
  - Sub-agents operate in their own isolated context windows without parent history access
  - cleanupPeriodDays setting controlling local transcript retention
  - Checkpoints capturing state before each edit; rewind (Esc+Esc or /rewind) for rollback

Governance:
  - Managed settings enforcing organization-wide policies
  - allowManagedPermissionRulesOnly preventing users from defining own permission rules
  - Server-managed settings deliverable through MDM or OS-level policies
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-ai-accelerated-offense.md` Claim 11: That note's Claim 11 documents
    zero-trust architecture with short-lived tokens and identity-based isolation as the correct
    response to AI-accelerated threats. This eBook provides the comprehensive implementation
    framework that Claim 11 prescribes in one sentence, expanding it to 35 pages of actionable
    guidance across eight capability domains and eight implementation phases.
  - `blog-anthropic-ai-accelerated-offense.md` Claim 7: "Place a model at the front of your
    alert queue, so that every alert gets at least some investigation." Verbatim equivalent
    appears in Part V of this eBook: "Every inbound alert should get an automated first-pass
    investigation before a human sees it." Both sources use the same architectural pattern
    with near-identical language, corroborating this as an Anthropic-endorsed design principle.
  - `blog-anthropic-ai-accelerated-offense.md` Claim 12: "Human decision-speed should never
    be rate-limited on aspects that would be better handed to an AI, like evidence collection."
    This eBook's Part V states: "Human decision speed during an incident should never be
    rate-limited on evidence collection or write-ups." — verbatim corroboration. Together
    they confirm this as a settled Anthropic-endorsed human/AI work-split principle.
  - `blog-anthropic-ai-accelerated-offense.md` Claim 10: "AI vendoring" (LLM reimplementation
    of unmaintained dependencies). This eBook's Phase 2 provides the same recommendation with
    the same name: "AI vendoring for small unmaintained dependencies." The eBook adds that it
    should be treated "as a standard response to an unhealthy dependency, not an exotic
    workaround" — a normalization of what the earlier note flagged as novel and high-risk.
  - `blog-anthropic-how-contain-claude.md` Claim 3: That note establishes "environmental
    containment should be the primary design priority — model-layer defenses will never achieve
    100% effectiveness." This eBook's three-tier architecture consistently places identity-based
    isolation and sandboxed execution at the Foundation and Enterprise levels, with model-layer
    controls (constitutional classifiers, spotlighting) as later layers. Both sources place
    environmental controls first.
  - `blog-anthropic-how-contain-claude.md` Claim 11: The 96% success rate on AWS credential
    phishing via prompt injection provides empirical grounding for this eBook's claim that
    "Traditional access controls won't prevent agents from misusing legitimate permissions."
    The phishing test is the concrete evidence for what this eBook states as a design principle.
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 6: Cloudflare sandboxes provide
    "zero-trust secrets injection" and "customizable egress proxy" — a production implementation
    of this eBook's Phase 6 (protect agent credentials) and Phase 5 (secure tool access sandbox
    execution) principles. The eBook provides the design rationale; the self-hosted sandboxes
    note documents the production implementation via a named provider.
  - `blog-anthropic-compliance-api-security-partners.md` Claim 5: The 28 security integration
    partners (DLP, SASE, SIEM, identity, eDiscovery) are the concrete tooling that implements
    this eBook's Enterprise and Advanced tier requirements for real-time SIEM streaming,
    behavioral correlation, and governance. The eBook defines what integration is needed; the
    Compliance API note documents the available integrations.

- **Extends**:
  - `blog-anthropic-ai-accelerated-offense.md`: That April 2026 post documented the threat
    landscape (24-month window, 7 defensive recommendations). This May 2026 eBook extends
    that into a structured implementation framework specific to agents. The relationship is
    strategic context (April post) → technical implementation (this eBook). The eBook's
    conclusion explicitly cross-links to the April post: "For broader org-wide readiness
    against AI-accelerated offense, check out our blog article, Preparing your security
    program for AI-accelerated offense."
  - `blog-anthropic-how-contain-claude.md`: That May 25 post documents Anthropic's production
    containment architecture for three products (claude.ai, Claude Code, Claude Cowork) with
    real incident reports. This eBook's eight-phase workflow and three-tier architecture provide
    the prescriptive framework that the containment post's engineering decisions implement.
    Read together: the containment post shows what Anthropic built; the eBook shows how any
    organization should build similar systems.

- **Contradicts**: No material contradictions identified with existing corpus source notes.
  The AI vendoring recommendation appears in both this eBook (Phase 2) and blog-anthropic-ai-accelerated-offense.md
  Claim 10, with slightly different framing: the earlier note flagged it as "novel strategy
  with no published adoption data" while this eBook normalizes it as "standard response to
  an unhealthy dependency." This is a maturation of framing over 6 weeks, not a contradiction
  — the eBook reflects evolved Anthropic positioning.

- **Novel**:
  - **Least agency** as the OWASP-coined term for extending least privilege to agentic systems:
    new named concept not previously in the corpus, with three concrete examples.
  - **"Impossible vs. tedious" design test**: Named heuristic for evaluating whether a control
    actually raises the cost to an agentic attacker or merely adds friction. No prior corpus
    source provides this evaluation framework.
  - **Complete eight-phase agent implementation workflow**: No prior corpus source provides an
    ordered, phase-based security implementation workflow for agentic systems. This is the first
    such prescriptive sequence.
  - **Agentic SOAR as a named category**: Extension of SOAR with adaptive capabilities for
    AI-accelerated threats. The term and concept are new to this corpus, though the underlying
    pattern (AI at alert queue front) was established by the April 2026 post.
  - **Spotlighting efficacy data** (>50% → <2% indirect injection): The specific efficacy
    numbers for the Microsoft mitigation technique are new to the corpus.
  - **Constitutional classifier efficacy data** (95% jailbreak blocking at minimal over-refusal):
    First-party Anthropic efficacy number for a specific defensive AI technique, new to the corpus.
  - **250-document LLM backdoor threshold**: Specific Anthropic research finding that 250
    malicious documents can backdoor LLMs from 600M to 13B parameters, persisting through RLHF
    and SFT — new to the corpus and alarming for any team using RAG or fine-tuning.
  - **Tabletop exercise for five simultaneous incidents**: The specific recommendation to rehearse
    for concurrent incidents (not one CVE at a time) is a novel operational practice recommendation.
  - **"Foundation floor has been raised" framing**: Explicit statement that what counted as
    minimum viable security in prior years no longer qualifies due to AI-accelerated offense.
    This is a significant calibration update with no prior equivalent in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "least agency" (OWASP term) as the named design
  principle for agent permissions alongside "least privilege." Include the three concrete examples
  from the document (database tool: read-only queries; email summarizer: no send/delete; API:
  minimal CRUD). Currently the corpus uses "least privilege" language; this document provides
  a more specific term calibrated to agentic tool use.

- **Chapter 02 (Harness Engineering) / Credential security**: Establish that static API keys
  and shared service-account credentials "are no longer a legitimate entry point, not even at
  Foundation." Update any guide content that presents API key rotation as an adequate security
  posture. The guide should recommend short-lived tokens (minutes expiry, identity-provider-issued)
  as the minimum baseline, with hardware-bound credentials as the target for production systems.

- **Chapter 04 or 05 (Security / Multi-agent systems)**: Add the agentic threat taxonomy from
  Part II as the named threat categories: prompt injection (direct + indirect), tool and resource
  misuse (tool poisoning, tool chaining, resource exhaustion), identity and privilege abuse
  (unscoped inheritance, confused deputy, memory-based retention), supply chain risks (model +
  tool + dependency), and memory/context poisoning (RAG poisoning, shared context, long-term drift).
  These are more specific and agent-relevant than generic security threat taxonomies.

- **Chapter 04 or 05 (Security)**: Add the "impossible vs. tedious" design test as a standing
  evaluation heuristic for security controls in agentic systems. Explicitly name the controls
  that fail this test (SMS MFA, rate limits, non-standard ports) and the controls that pass
  (hardware-bound credentials, expiring tokens, cryptographic identity, network paths that
  don't exist).

- **Chapter 04 or 05 (Security)**: Add Spotlighting (Microsoft, >50% → <2% indirect injection
  success rate) and constitutional classifiers (Anthropic, 95% jailbreak blocking) as the two
  highest-evidence input control techniques. Current guide content (if any) on prompt injection
  mitigation lacks efficacy data; these provide concrete benchmarks.

- **Chapter 05 (Multi-agent orchestration)**: Add explicit trust boundary design for multi-agent
  systems: each agent needs its own cryptographic identity and credentials; high-privilege agents
  must verify identity of callers before accepting delegated tasks; credential sharing between
  agents eliminates the compartmentalization benefit. The confused deputy pattern (low-privilege
  agent relays instructions to high-privilege agent) should be the canonical example of why
  per-agent credential isolation matters.

- **Chapter 06 (Production / Security operations)**: Add the Agentic SOAR concept and the
  practical rollout pattern: start with one noisy rule, wire a frontier model with read-only
  SIEM access, measure agreement for two weeks, expand if tolerable. Add the two key metrics
  (dwell time and coverage) as the measurement framework. Add the human/AI work split rule:
  AI handles evidence collection and documentation; humans retain containment, disclosure, and
  customer communications.

- **Chapter 06 or governance chapter**: Add the three-tier framework (Foundation/Enterprise/Advanced)
  as a maturity model for agent security. Frame Foundation not as "beginner level" but as "the
  floor that AI-accelerated offense has raised" — organizations that have not yet met Foundation
  requirements have a known gap, not a starting point. The Enterprise tier (ABAC, dynamic privilege,
  sandboxed execution, immutable audit trails, signed configs) should be positioned as the target
  for any production agentic deployment.

## Extraction Notes

- **Source is a blog post linking to a freely-accessible PDF eBook**: The blog page
  (claude.com/blog/zero-trust-for-ai-agents) is a teaser with ~500 words; all substantive
  content is in the 35-page PDF (published May 18, 2026, created 9 days before the blog post's
  May 27 date). The PDF was downloaded directly and read page-by-page. All claims and quotes
  in this note are extracted verbatim from the PDF pages as read by this extraction process.
- **All quotes are verbatim from PDF text**: The PDF was read as a document, providing
  character-for-character access to the source text. Quotes have been verified against the
  rendered PDF pages.
- **Claude Code pro-tips**: Throughout the eBook, Claude Code is cited as implementing each
  capability described. These pro-tips serve a dual purpose: they demonstrate that Claude Code
  implements Zero Trust patterns, and they provide implementers specific Claude Code features
  to reference. The pro-tips are extracted in the Concrete Artifacts section.
- **No empirical evidence for tier efficacy**: The eBook prescribes practices across three
  tiers but provides no before/after data on what security outcomes each tier achieves (no
  "Foundation reduces incident rate by X%"). The efficacy evidence it provides is for specific
  techniques (Spotlighting, constitutional classifiers) rather than the tier system as a whole.
- **Research citations**: The document cites "Microsoft Research," "Anthropic research," and
  "research shows" without linking to specific papers. Claims based on these citations are
  rated "emerging" rather than "settled" to account for the lack of direct verifiable links.
- **Compliance section is thin**: The document mentions HIPAA, FINRA, GDPR, FedRAMP, and
  EU AI Act as aligning with Zero Trust but does not detail the mapping. Organizations in
  regulated industries will need supplementary compliance mapping resources beyond this eBook.
- **Overall confidence**: The three-tier framework, eight-phase workflow, threat taxonomy, and
  design principles are rated "settled" as first-party Anthropic prescriptive guidance. Claims
  citing third-party research without named papers (Microsoft Research, "research shows 100%
  attack success rates") are rated "emerging." The overall note confidence is "emerging" because
  the framework's efficacy is asserted rather than empirically demonstrated at the system level.
