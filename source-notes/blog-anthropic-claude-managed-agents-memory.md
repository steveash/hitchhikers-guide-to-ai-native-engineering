---
source_url: https://claude.com/blog/claude-managed-agents-memory
source_type: blog-post
title: "Built-in memory for Claude Managed Agents"
author: Anthropic (product announcement)
date_published: 2026-04-23
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: anecdotal
issue: "#370"
---

# Built-in memory for Claude Managed Agents

> The April 23, 2026 public beta launch announcement for Managed Agents memory:
> a filesystem-based, enterprise-ready cross-session learning layer with four
> named production customers and the most specific improvement benchmarks in the
> Managed Agents corpus (Rakuten: 97% fewer errors / 27% lower cost / 34% lower
> latency; Wisedocs: 30% speedup).

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com blog,
  April 23, 2026; public beta launch of the memory feature for Claude Managed
  Agents, which itself launched April 8, 2026)
- **Author credibility**: First-party Anthropic announcement — authoritative on
  what the platform provides and which features are in which access tier. Customer
  testimonials are from named companies (Rakuten, Wisedocs, Netflix, Ando) without
  individually named testimonial authors in the available text, which is slightly
  weaker than the April 8 announcement's eight named executives with titles. The
  production benchmarks (Rakuten, Wisedocs) are customer-reported, not
  Anthropic-internal, which is more credible than the self-evaluation benchmark
  in the April 8 note — but still unaudited single-company figures.
- **Scope**: Covers the memory public beta launch: filesystem storage architecture,
  enterprise governance features (scoped permissions, audit logs, version rollback,
  content redaction), concurrent multi-agent access guarantee, developer API control,
  Claude Console memory traceability, scoped sharing across agents, Opus 4.7
  model optimization for filesystem memory, and four customer deployments. Does
  NOT cover: pricing changes, API design specifics, SDK integration code, how
  the filesystem memory interacts with the harness or sandbox components described
  in blog-anthropic-scaling-managed-agents.md, or the dreaming feature (announced
  separately on May 6 in blog-anthropic-managed-agents-dreaming-outcomes.md).

## Extracted Claims

### Claim 1: Memory on Claude Managed Agents enters public beta as a filesystem-based intelligence-optimized layer that enables agents to learn across sessions

- **Evidence**: First-party product launch announcement. The "intelligence-optimized
  memory layer" framing distinguishes this from generic file storage. The "public
  beta" status means this is broadly available (not research preview).
- **Confidence**: settled (explicit product launch with GA access tier)
- **Quote**: "Memory on Managed Agents is available today in public beta. Your
  agents can now learn from every session, using an intelligence-optimized memory
  layer that balances performance with flexibility."
- **Our assessment**: The "intelligence-optimized" qualifier is doing real work —
  it implies the memory system has been tuned to align with Claude's context
  handling rather than being a generic key-value store. The "balances performance
  with flexibility" phrase signals a deliberate trade-off: this is not the
  highest-throughput memory design, nor the most flexible schema-free design,
  but a point in the design space chosen for agent workloads. Notably, the
  announcement says "public beta" (not research preview), meaning this is
  accessible to all Managed Agents developers on day one, unlike the outcomes
  and multiagent coordination features launched the same day in research preview.

### Claim 2: Memories are stored as files mounted directly onto a filesystem, so agents access them via the same bash and code execution capabilities used for all other agentic tasks

- **Evidence**: First-party architectural description. The design motivation is
  explicitly stated: agents are already effective at filesystem operations, so
  memory reuses that interface rather than introducing a new memory-specific API.
- **Confidence**: settled (explicit product design description from first-party source)
- **Quote**: "Memory on Managed Agents mounts directly onto a filesystem, so
  Claude can rely on the same bash and code execution capabilities that make it
  effective at agentic tasks."
- **Our assessment**: This is the defining architectural decision of the memory
  system. Filesystem-based storage has two key properties: (1) Claude reads and
  writes memories using the same tool interface as all other filesystem operations
  — no new capability required; (2) the memory store is directly inspectable
  and auditable by developers since it is just files. The choice trades the
  semantic retrieval capabilities of vector databases for operational simplicity
  and integration coherence with the sandbox execution environment described in
  blog-anthropic-scaling-managed-agents.md (Claim 2). The sandbox component
  ("execution environment where Claude can run code and edit files") is the
  same substrate that memory is mounted onto.

### Claim 3: Memories are exportable and independently manageable via the API, giving developers full programmatic control

- **Evidence**: First-party feature description with explicit developer control framing.
- **Confidence**: settled (explicit product feature announcement)
- **Quote**: "Memories are files that can be exported and independently managed
  via the API, giving developers full control."
- **Our assessment**: Developer-controlled memory export mitigates platform
  lock-in risk — if an organization's agents have accumulated institutional
  knowledge in a managed service, exportability ensures that knowledge is not
  trapped. "Independently managed" also supports compliance scenarios where
  organizations need to audit, redact, or delete specific learned content
  outside the normal agent workflow. This is the first corpus source to
  describe memory as an explicitly portable artifact rather than a platform-
  internal resource.

### Claim 4: Memory updates surface in Claude Console as session events, enabling developers to trace what an agent learned and from which session

- **Evidence**: First-party feature description. The audit trail property is
  explicit: both what was learned and the session provenance are visible.
- **Confidence**: settled (explicit product feature with specific metadata described)
- **Quote**: "Updates also surface in the Claude Console as session events, so
  developers can trace what an agent learned and where it came from."
- **Our assessment**: Memory traceability addresses an enterprise governance
  requirement that generic logging cannot easily satisfy: knowing not just
  *what* an agent knows, but *how* it came to know it. Session-level provenance
  for each memory item enables both debugging (why is the agent behaving this
  way?) and compliance (did the agent learn something from a session it should
  not have accessed?). This extends the general execution tracing claim from
  blog-anthropic-claude-managed-agents.md (Claim 7) into the memory domain.

### Claim 5: Memory stores can be shared across multiple agents with different access scopes — org-wide stores can be read-only while per-user stores allow reads and writes

- **Evidence**: First-party architectural description with a concrete two-tier
  scoping example.
- **Confidence**: settled (explicit product design with illustrative example)
- **Quote**: "Stores can be shared across multiple agents with different access
  scopes. For example, an org-wide store might be read-only, while per-user
  stores allow reads and writes."
- **Our assessment**: The scoped sharing model enables a layered institutional
  knowledge architecture: common knowledge (org-wide, read-only) that all
  agents see without risk of individual agents overwriting it, combined with
  per-user contextual memory (read-write) that individual agents accumulate
  from their own sessions. This is architecturally important for multi-agent
  deployments. It also mirrors how organizations manage institutional knowledge
  in practice: company policies are read-only for employees; personal notes
  are read-write for individuals. The model is the first concrete shared-memory
  design pattern in the corpus with named scoping semantics.

### Claim 6: Multiple agents can work concurrently against the same memory store without overwriting each other

- **Evidence**: First-party product guarantee. The concurrency safety mechanism
  (file locking, write queue, merge strategy) is not described.
- **Confidence**: settled (explicit product guarantee from first-party source)
- **Quote**: "Multiple agents can work concurrently against the same store
  without overwriting each other."
- **Our assessment**: Concurrent write safety is a prerequisite for multi-agent
  deployments where parallel agents contribute to a shared memory store. Without
  this guarantee, concurrent agents could produce race conditions. The
  announcement states the guarantee without describing the mechanism — a
  practical consideration for teams that need to understand the performance
  implications of concurrent writes at scale. The guarantee is important
  context for the multiagent orchestration feature (blog-anthropic-managed-agents-
  dreaming-outcomes.md, Claim 6), where parallel subagents running against the
  same memory store is a natural deployment pattern.

### Claim 7: Memory is built for enterprise deployments with scoped permissions, audit logs, and full programmatic control

- **Evidence**: First-party feature description with an explicit enterprise positioning.
  The three governance elements (scoped permissions, audit logs, programmatic control)
  are listed.
- **Confidence**: settled (explicit product feature list from first-party source)
- **Quote**: "Memory is built for enterprise deployments, with scoped permissions,
  audit logs, and full programmatic control."
- **Our assessment**: The enterprise framing signals that memory governance was
  designed as a first-class concern, not retrofitted. The three governance
  elements map to distinct enterprise requirements: access control (scoped
  permissions), auditability (audit logs), and operational management
  (programmatic control). This extends the general governance layer from
  blog-anthropic-claude-managed-agents.md (Claim 7) specifically to memory.
  Practitioners building DIY cross-session memory systems should treat this
  as the production governance bar: if their home-built memory solution lacks
  any of these three properties, it is not enterprise-ready.

### Claim 8: Memory includes version rollback and content redaction capabilities

- **Evidence**: First-party feature description. No detail on granularity (per-item
  rollback vs. full-store rollback) or redaction scope.
- **Confidence**: settled (explicit product feature)
- **Quote**: "You can roll back to an earlier version or redact content from history."
- **Our assessment**: Version rollback and redaction address two distinct production
  lifecycle concerns: (1) recovery from agent error or adversarial input that caused
  the agent to learn incorrect or harmful content (rollback); (2) compliance and
  privacy requirements to remove specific learned content (redaction). These features
  signal that the memory system is designed for long-lived production deployments
  where agents accumulate months of learned behavior — not just for prototypes.
  The combination with the audit trail (Claim 4) creates a full lifecycle management
  capability: observe what was learned, redact what should not persist, roll back
  when an error is detected.

### Claim 9: Opus 4.7 is specifically optimized for filesystem-based memory — it saves more comprehensive, well-organized memories and is more discerning about what to remember across long multi-session work

- **Evidence**: First-party claim with model-specific optimization detail. Opus 4.7
  is the only model version named. Two distinct behaviors are claimed: better
  organization (comprehensive, well-organized) and better selectivity (discerning).
- **Confidence**: emerging (vendor claim about model optimization; no independent
  benchmark; this is a product-matching claim from the vendor)
- **Quote (selectivity)**: "With filesystem-based memory, our latest models save
  more comprehensive, well-organized memories and are more discerning about what
  to remember."
- **Quote (Opus 4.7 specifically)**: "Opus 4.7 is better at using file system-based
  memory. It remembers important notes across long, multi-session work"
- **Our assessment**: The model-optimization claim establishes a tight coupling
  between the memory system design (filesystem-based) and Opus 4.7. Two behaviors
  are claimed: comprehensiveness (saves more relevant detail) and discernment
  (does not save everything indiscriminately). The selectivity behavior is
  architecturally significant — an agent that saves every observation creates a
  noisy memory store that degrades retrieval quality over time; an agent that
  discerns what is worth saving keeps the memory store signal-dense. This is the
  per-session analogue to dreaming's between-session curation
  (blog-anthropic-managed-agents-dreaming-outcomes.md, Claim 2). The "long,
  multi-session work" framing is important: the optimization target is extended
  engagements, not one-shot sessions.

### Claim 10: Rakuten agents using cross-session memory achieved 97% fewer first-pass errors with 27% lower cost and 34% lower latency

- **Evidence**: Customer testimonial from Rakuten (attributed to Rakuten in the
  "our agents" phrasing). Three simultaneous improvement dimensions. No methodology
  details or baseline description.
- **Confidence**: anecdotal (single company; no methodology; first-party testimonial
  without individual attribution; no independent replication)
- **Quote**: "Our agents distill lessons from every session, delivering 97% fewer
  first-pass errors at 27% lower cost and 34% lower latency"
- **Our assessment**: The three-dimensional improvement (errors, cost, latency)
  is unusual — typically there are trade-offs between these metrics. The
  simultaneous improvement on all three dimensions suggests the primary mechanism
  is reduced retry/rework cycles: fewer first-pass errors eliminates expensive
  follow-up correction calls, which reduces both token cost and wall-clock latency.
  The 97% reduction in first-pass errors is the most striking quality metric in
  the Managed Agents corpus. "Distill lessons from every session" describes the
  mechanism: agents that carry forward what they learned about specific tasks,
  tools, or data patterns avoid repeating mistakes. Note: Rakuten was also named
  in the April 8 announcement (blog-anthropic-claude-managed-agents.md) as an
  enterprise customer deploying specialist agents per business domain. This result
  provides the first concrete performance evidence for that deployment pattern.

### Claim 11: Wisedocs achieved a 30% speedup in document verification by using cross-session memory to identify and remember common issues — including issues designers did not anticipate

- **Evidence**: Customer testimonial from Wisedocs with explicit mechanism description.
  The "including ones we didn't think about" clause adds an unexpected-discovery
  dimension.
- **Confidence**: anecdotal (single company; no methodology; testimonial without
  named individual)
- **Quote**: "we used cross-session memory to let our agents identify and remember
  common issues — including ones we didn't think about. It's sped verification
  up 30%."
- **Our assessment**: The "including ones we didn't think about" clause is the
  most significant element of this testimonial. It implies memory enables emergent
  expertise accumulation — the agent discovers patterns that human designers did
  not anticipate and would not have encoded in a static system prompt. This is
  qualitatively different from memory as a configuration shortcut (encoding known
  rules) and positions memory as a capability-expansion mechanism. The 30% speedup
  is directionally consistent with fewer re-runs, reduced context reconstruction,
  and better tool selection informed by discovered patterns. Note: Wisedocs is also
  cited in blog-anthropic-managed-agents-dreaming-outcomes.md (Claim 4) in the
  context of the outcomes feature providing a 50% faster review workflow — a
  different 30%-50% range improvement from a different feature, suggesting Wisedocs
  uses multiple Managed Agents capabilities in combination.

### Claim 12: Netflix agents use cross-session memory to carry context across sessions

- **Evidence**: Single customer mention; no specific metrics or mechanism detail.
- **Confidence**: anecdotal (named customer; minimal detail)
- **Quote**: "Netflix agents carry context across sessions"
- **Our assessment**: The minimal detail makes this claim's primary value its
  confirmation that a major enterprise customer is using cross-session memory in
  production. Netflix is also cited in blog-anthropic-managed-agents-dreaming-
  outcomes.md (Claim 6) for multiagent orchestration — the same customer is using
  multiple Managed Agents capabilities. The "without manual prompt updates"
  implication — that memory automates what previously required manual prompt
  maintenance — is not stated explicitly here but is the logical contrast to
  the pre-memory workflow.

### Claim 13: Ando is building their workplace messaging platform on Managed Agents, using the managed memory layer instead of custom infrastructure

- **Evidence**: Single customer mention; no detail on the memory usage pattern.
- **Confidence**: anecdotal (named customer; minimal detail)
- **Quote**: "Ando is building their workplace messaging platform on Managed Agents"
- **Our assessment**: Ando is new to the corpus. The "instead of custom
  infrastructure" framing positions memory not as an add-on capability but as
  an infrastructure replacement — the reason they chose Managed Agents over
  building their own is the managed memory layer. This is consistent with the
  broader build-vs-buy argument from blog-anthropic-claude-managed-agents.md
  (Claim 1), now applied specifically to the memory/state management dimension.

## Concrete Artifacts

### Memory Architecture Design (April 23, 2026)

```
Claude Managed Agents — Memory System Design:

STORAGE:
  - Type: filesystem (files mounted onto sandbox)
  - Access: bash and code execution (same capabilities as other agent tasks)
  - Export: files exportable and independently managed via API
  - Control: full developer programmatic control

SCOPING MODEL:
  - Per-agent: default isolated store
  - Shared: stores shareable across agents
  - Access scopes: read-only OR read-write per store
  - Example: org-wide store = read-only; per-user store = read/write
  - Concurrency: multiple agents concurrent on same store without overwrites

ENTERPRISE GOVERNANCE:
  - Scoped permissions
  - Audit logs (session events visible in Claude Console)
  - Version rollback (to earlier snapshot)
  - Content redaction (from history)
  - Full programmatic API control

OBSERVABILITY:
  - Memory updates surface as session events in Claude Console
  - Trace: what an agent learned + which session it came from

MODEL OPTIMIZATION:
  - Opus 4.7: better at filesystem-based memory
  - Behaviors: more comprehensive, well-organized saves; more discerning
    about what to save
  - Target: long, multi-session work

ACCESS TIER: Public beta (April 23, 2026)
```

### Production Benchmarks (Customer-Reported)

```
Company    | Metric                        | Value         | Mechanism
-----------|-------------------------------|---------------|---------------------------
Rakuten    | First-pass errors             | -97%          | "distill lessons from
           | Cost                          | -27%          |  every session"
           | Latency                       | -34%          |
Wisedocs   | Document verification speed   | +30%          | Cross-session memory of
           |                               |               | common issues (incl.
           |                               |               | unanticipated ones)
Netflix    | Context carried across        | (deployed)    | (no metric)
           | sessions                      |
Ando       | Workplace messaging platform  | (deployed)    | Memory replaces custom
           | built on Managed Agents       |               | infrastructure

Source: Anthropic product announcement (2026-04-23)
All benchmarks: customer-reported, no independent audit, no methodology detail
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-claude-managed-agents.md** (Claim 7): The general enterprise
    governance layer (scoped permissions, identity management, execution tracing)
    from the April 8 announcement is corroborated and extended here with
    memory-specific audit logging, session event tracing for learned content,
    version rollback, and content redaction. The memory governance features
    implement the same principles at the memory layer.
  - **blog-anthropic-claude-managed-agents.md** (Claim 3): Long-running sessions
    with persistent state. Memory adds the learned-knowledge dimension to state
    persistence — state persistence keeps in-session work; memory persistence
    carries forward what the agent learned across sessions.
  - **blog-anthropic-scaling-managed-agents.md** (Claim 2): The sandbox component
    ("execution environment where Claude can run code and edit files") is the same
    substrate that memory is mounted onto. The filesystem memory architecture
    directly leverages the sandbox's file execution interface, confirming the
    architectural coherence of the two-layer design (session+harness+sandbox /
    memory).

- **Extends**:
  - **blog-anthropic-claude-managed-agents.md**: The April 8 announcement
    established the Managed Agents platform. This April 23 post is the first
    major feature addition: memory in public beta. It adds the cross-session
    learning capability that the April 8 note did not describe.
  - **blog-anthropic-scaling-managed-agents.md**: The session model (Claim 2:
    "append-only log of everything that happened") is extended by memory — session
    events now include memory updates, giving the session log a new category of
    structured learned-knowledge output. The memory filesystem mounts onto the
    sandbox that the engineering post describes as one of the three virtualized
    components.
  - **blog-anthropic-managed-agents-dreaming-outcomes.md** (Claim 3): The May 6
    dreaming announcement frames memory and dreaming as a two-layer system:
    "Memory lets each agent capture what it learns as it works. Dreaming refines
    that memory between sessions, pulling shared learnings across agents and
    keeping it up-to-date." This April 23 post is the foundational first layer
    of that two-layer design — the session-level write path that dreaming then
    curates.

- **Contradicts**: None found. The April 8 announcement did not describe a memory
  feature; the April 23 announcement introduces one. There is no prior corpus
  position on memory architecture for Managed Agents to contradict.

- **Novel**:
  - **Filesystem-based memory as an explicit architectural choice**: No prior corpus
    source describes storing agent memory as files accessed via bash/code execution.
    The design rationale (reuse existing agent capabilities rather than introducing
    a new memory API) is the first stated architectural reasoning for a memory storage
    choice in the corpus. Prior corpus sources mention memory abstractly or as an
    opaque platform feature.
  - **Cross-agent scoped sharing model (org-wide read-only + per-user read-write)**:
    The named two-tier scoping example is the first concrete shared-memory design
    pattern in the corpus with explicit access semantics. This is architecturally
    actionable for multi-agent design.
  - **Production benchmarks with three-dimensional improvement (Rakuten)**:
    97% fewer errors + 27% lower cost + 34% lower latency simultaneously from
    cross-session memory. No prior corpus source provides a memory-specific
    production benchmark at this specificity. The mechanism (fewer retries
    → lower cost + latency cascade) is the first documented production evidence
    for the claim that cross-session learning reduces retry costs.
  - **Memory as emergent expertise discovery (Wisedocs)**:
    "including ones we didn't think about" — the claim that cross-session memory
    enables the agent to discover patterns that human designers did not anticipate
    is qualitatively new. Prior corpus framing of memory is as a lookup mechanism
    for known facts; this frames memory as a capability-expansion mechanism.
  - **Version rollback and content redaction for agent memory**:
    No prior corpus source describes a production memory system with rollback
    and redaction capabilities. These are first documented here.
  - **Opus 4.7 model optimization claim for filesystem memory**:
    The first model-specific memory optimization claim in the corpus, naming
    both comprehensiveness and discernment as distinct target behaviors.

## Guide Impact

- **Chapter 03 (Long-Running Sessions & State)**: This source should be the
  primary reference for cross-session memory architecture in a hosted platform
  context. The filesystem-based design (Claim 2) is the reference implementation.
  The Rakuten (97%/27%/34%) and Wisedocs (30%) benchmarks quantify the production
  value of cross-session memory at a level of specificity not available elsewhere
  in the corpus. Add the scoped sharing model (Claim 5: org-wide read-only +
  per-user read-write) as the canonical multi-agent memory sharing pattern.

- **Chapter 02 (Harness Engineering)**: Extend the "Build vs. Buy" framing from
  blog-anthropic-claude-managed-agents.md to include the memory dimension. The
  Ando case (Claim 13: building on Managed Agents "instead of custom
  infrastructure") specifically positions managed memory as an infrastructure
  replacement. The governance features (Claim 7: scoped permissions, audit logs,
  programmatic control; Claim 8: version rollback, content redaction) define the
  enterprise governance bar that any DIY cross-session memory system must meet.
  Practitioners building their own should be aware that matching this bar DIY
  requires implementing four distinct capabilities.

- **Chapter 05 (Multi-Agent Orchestration)**: The scoped sharing model (Claim 5)
  and concurrency guarantee (Claim 6) address the shared-state management challenge
  for multi-agent systems. Current guide material on multi-agent coordination does
  not describe concrete shared-memory architectures with named access semantics.
  This source provides the first such pattern with explicit org-wide vs. per-user
  scoping. Add alongside the multiagent orchestration patterns from
  blog-anthropic-managed-agents-dreaming-outcomes.md.

- **Chapter 08 (Governance)**: The memory governance feature set (Claim 7 + Claim 8:
  scoped permissions + audit logs + programmatic control + version rollback +
  content redaction) is the most complete specification of production memory
  governance in the corpus. Use this as the reference bar for "what enterprise-grade
  agent memory governance looks like" — both for practitioners evaluating Managed
  Agents and for practitioners building equivalent DIY systems.

## Extraction Notes

- The WebFetch tool returned summaries rather than the full post HTML. All quotes
  were extracted by making multiple targeted WebFetch calls and verifying specific
  passages character-for-character. Quotes marked with (no direct quote) are not
  used; all quotes in the Extracted Claims section are from targeted WebFetch
  verification passes.
- Customer testimonials (Rakuten, Wisedocs, Netflix, Ando) do not have named
  individual attributions in the available text, unlike the April 8 announcement
  which provided executive names and titles for eight customers. This is a minor
  reduction in evidential weight — the examples are company-level testimonials.
- The blog post references documentation at platform.claude.com/docs. The
  documentation pages were not fetched for this extraction — the architectural
  and design details may have additional specificity there.
- The Wisedocs 30% speedup is from the memory feature (document verification
  pipeline). blog-anthropic-managed-agents-dreaming-outcomes.md also cites Wisedocs
  for a "50% faster" outcome from the outcomes feature. These are two separate
  benchmarks for two separate features on what appear to be different workflows.
  They are not contradictory but should not be conflated in citations.
- This is the foundational memory announcement that blog-anthropic-managed-agents-
  dreaming-outcomes.md explicitly references: "Together, memory and dreaming form a
  robust memory system for self-improving agents." This note should be read before
  the dreaming note for full architectural context.
