---
source_url: https://claude.com/blog/claude-managed-agents
source_type: blog-post
title: "Claude Managed Agents: get to production 10x faster"
author: Anthropic (product announcement)
date_published: 2026-04-08
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: anecdotal
issue: "#205"
---

# Claude Managed Agents: get to production 10x faster

> Official Anthropic product announcement introducing Claude Managed Agents — a
> hosted platform that bundles sandboxing, checkpointing, credential management,
> scoped permissions, multi-agent coordination, and an outcome-based self-evaluation
> loop as composable APIs, claiming to reduce agent time-to-production from months
> to days, backed by eight named enterprise customer testimonials.

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com blog,
  April 8 2026; public beta launch of a new paid platform service)
- **Author credibility**: First-party Anthropic announcement — maximum authority
  on what the platform provides. Customer testimonials are from named individuals
  with full titles at named companies (Notion, Rakuten, Asana, Sentry, Atlassian,
  Vibecode, General Legal, Blockit), which raises them above generic marketing
  pull quotes. The performance benchmark ("+10 points task success") is Anthropic's
  own internal test, not independently replicated — treat it as a directional signal,
  not a settled result. The "10x faster" headline is a marketing claim supported by
  testimonials, not a controlled study. No independent engineering post accompanies
  this announcement.
- **Scope**: Covers what the platform provides (capability list), why to use it
  (vs. building your own harness), how it performs (one internal benchmark), what
  it costs ($0.08/session-hour), and how customers are using it (eight testimonials).
  Does NOT cover: API design specifics, SDK integration patterns, how sandboxing or
  checkpointing are implemented technically, how multi-agent coordination works
  mechanically (deferred to research preview access), or failure modes. The blog
  post is high-level marketing copy; the technical specifics live in the linked
  docs and Console quickstart that were not fetched for this extraction.

## Extracted Claims

### Claim 1: Building a production agent requires months of infrastructure work — sandboxing, checkpointing, credential management, scoped permissions, and end-to-end tracing — before users see anything

- **Evidence**: Vendor claim, corroborated by the concrete specificity of the
  infrastructure list (these are real problems every team hits) and by the
  Vibecode, Sentry, and Atlassian testimonials explicitly citing these as the
  pain points they no longer have to solve.
- **Confidence**: emerging
- **Quote**: "Until now, building agents meant spending development cycles on
  secure infrastructure, state management, permissioning, and reworking your
  agent loops for every model upgrade. Managed Agents pairs an agent harness
  tuned for performance with production infrastructure to go from prototype to
  launch in days rather than months."
- **Our assessment**: The infrastructure list is accurate — these are the same
  components every practitioner building a production agent must solve. Our corpus
  confirms this from the build-your-own side: Sentry's `.claude/settings.json`
  with 60+ permission allowlists (practitioner-getsentry-sentry), TTal's external
  state management via Taskwarrior/FlickNote (discussion-hn-ttal-multiagent-factory),
  and Kiln's GitHub Issues as session state (discussion-hn-kiln-orchestration) are
  all DIY answers to exactly the problems Managed Agents claims to solve. The
  reworking-agent-loops-for-every-model-upgrade problem is independently documented
  in our corpus as real and costly (blog-anthropic-harness-long-running).

### Claim 2: A built-in orchestration harness decides when to call tools, how to manage context, and how to recover from errors

- **Evidence**: Vendor description of the platform's orchestration layer. The
  Atlassian testimonial explicitly corroborates the "heavy lifting" framing.
- **Confidence**: anecdotal (vendor claim; no independent technical audit)
- **Quote**: "A built-in orchestration harness decides when to call tools, how
  to manage context, and how to recover from errors."
- **Our assessment**: This is the core architectural trade-off the platform embodies:
  practitioners give up explicit control of the orchestration loop in exchange for
  not having to build it. The phrase "tuned for performance" implies the harness
  incorporates the design decisions from Anthropic's own harness research
  (blog-anthropic-harness-long-running, blog-anthropic-harnessing-claude-intelligence)
  — but this is inference, not documented in the announcement. The "recover from
  errors" claim is significant because error recovery is one of the hardest parts
  of long-running agent design and is barely addressed in DIY practitioner sources.

### Claim 3: Long-running sessions operate autonomously for hours with progress and outputs persisting even through disconnections

- **Evidence**: Core product feature claim. Notion's Eric Liu (Product Manager)
  specifically validates this: "Agents can handle long-running sessions, manage
  memory, and deliver high-quality outputs over time." Rakuten's Yusuke Kaji
  (GM of AI for Business) references "managing long-running tasks across
  engineering, product, sales, marketing, and finance."
- **Confidence**: anecdotal (vendor claim + two customer corroborations)
- **Quote**: "Long-running sessions that operate autonomously for hours, with
  progress and outputs that persist even through disconnections."
- **Our assessment**: Session persistence across disconnections is the specific
  infrastructure gap that our failure corpus documents as painful. The decker
  4-hour session loss (failure-decker-4hr-session-loss) is the canonical example:
  context collapsed after a long session with no recovery mechanism. Managed Agents
  claims to solve this at the platform level. The claim is credible as a product
  feature; its reliability in practice is not independently documented.

### Claim 4: The self-evaluation outcome loop (define success criteria → Claude iterates until met) improves structured file generation task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems

- **Evidence**: Anthropic's own internal benchmark on structured file generation.
  This is the only quantitative performance claim in the post. The benchmark is
  Anthropic-run, not independently replicated. The "hardest problems" caveat is
  important — the gain is not uniform across task difficulty.
- **Confidence**: anecdotal (internal benchmark from the product team; no
  methodology details, no independent replication; treat as directional)
- **Quote**: "In internal testing around structured file generation, Managed
  Agents improved outcome task success by up to 10 points over a standard
  prompting loop, with the largest gains on the hardest problems."
- **Our assessment**: The "+10 points" figure is the only hard number in the
  announcement. Its interpretation requires context: (a) "up to" is a ceiling
  claim, not an average; (b) structured file generation is a specific task type
  with clear success criteria — the gain may not transfer to open-ended tasks;
  (c) the self-evaluation feature is in research preview, meaning most readers
  can't access it today. The pattern (define outcomes + iterate until met) is
  architecturally identical to the generator/evaluator architecture documented
  in blog-anthropic-harness-long-running, which also emphasizes Claude iterating
  against defined success criteria producing quality improvements at known cost.
  The "largest gains on hardest problems" qualifier is important: the outcome
  loop provides diminishing returns on easy tasks where a single-shot response
  already succeeds.

### Claim 5: The outcome-driven mode (define success criteria, let Claude self-evaluate and iterate) is an explicit architectural choice distinct from traditional prompt-and-response (tighter control) mode

- **Evidence**: The article explicitly presents both modes and frames them as
  design choices based on desired control level.
- **Confidence**: settled (explicit product feature distinction from first-party
  source)
- **Quote**: "With Managed Agents, you define outcomes and success criteria, and
  Claude self-evaluates and iterates until it gets there...It also supports
  traditional prompt-and-response workflows when you want tighter control."
- **Our assessment**: This is the most novel conceptual contribution of the
  announcement for practitioners. It names a pattern that the research literature
  (generator/evaluator architectures, Ralph loop) had established but not packaged
  as a user-facing choice. The framing is: if you can specify what success looks
  like, you can delegate the how to the model. The "tighter control" alternative
  is the familiar single-prompt-and-response mode that all existing practitioners
  already understand. The article is explicit that the outcome mode is the
  differentiating value; prompt-and-response is the compatibility mode.

### Claim 6: Multi-agent coordination — agents spawning and directing sub-agents to parallelize complex work — is available as a first-class platform feature

- **Evidence**: Product feature description. Currently in research preview with
  separate access request required.
- **Confidence**: anecdotal (research preview; no customer testimonials
  specifically citing multi-agent coordination in production)
- **Quote**: "Multi-agent coordination so agents can spin up and direct other
  agents to parallelize complex work (available in research preview)."
- **Our assessment**: The architecture described (agents spawning sub-agents to
  parallelize) is identical to what the TTal framework implements manually
  (Manager/Worker plane in discussion-hn-ttal-multiagent-factory) and what
  Osmani describes as experimental in Claude Code Agent Teams
  (blog-addyosmani-code-agent-orchestra, Claim 4). Managed Agents represents the
  fully hosted version of the same pattern: the orchestration infrastructure
  (how sub-agents communicate, how state is shared) is handled by the platform.
  The research preview status means practitioner reports of real-world use are
  not yet available to corroborate or refine the claim.

### Claim 7: Scoped permissions, identity management, and execution tracing are built into the governance layer, with full inspection via Claude Console

- **Evidence**: Product feature description. Atlassian's Sanchan Saxena (SVP,
  Head of Product) specifically calls out "sandboxing, sessions, and scoped
  permissions" as what the platform handles. Sentry's Indragie Karunaratne
  (SVP Engineering) explicitly cited "secure, fully managed agent runtime."
- **Confidence**: anecdotal (vendor claim + two customer corroborations)
- **Quote (platform)**: "Giving agents access to real systems with scoped
  permissions, identity management, and execution tracing built in."
- **Quote (console)**: "Session tracing, integration analytics, and
  troubleshooting guidance are built directly into the Claude Console, so you
  can inspect every tool call, decision, and failure mode."
- **Our assessment**: The execution tracing claim (inspect every tool call,
  decision, and failure mode) addresses one of the key deficits in DIY agent
  harnesses. Kiln had no tracing; TTal had Telegram as a human-readable log
  but no structured trace. The practitioner-getsentry-sentry source shows
  Sentry building MCP server integration to get event visibility — a problem
  Managed Agents claims to solve at the platform level. The actual tracing
  quality (granularity, latency, searchability) is not described in the
  announcement.

### Claim 8: Multiple enterprise teams built initial integrations in weeks rather than months

- **Evidence**: Six of eight customer testimonials explicitly reference weeks-
  vs-months timeframes or similar speed claims.
- **Confidence**: anecdotal (named customer testimonials; real companies with
  named individuals and titles; no independent audit)
- **Quote (Sentry)**: "Managed Agents not only allowed us to build the initial
  integration in weeks instead of months, but has also eliminated the ongoing
  operational overhead of maintaining bespoke agent infrastructure."
- **Quote (Atlassian)**: "With Claude Managed Agents, we can build agents for
  developers directly into the workflows teams already rely on in weeks instead
  of months."
- **Quote (Vibecode)**: "Before Claude Managed Agents, users would have to
  manually run LLMs in sandboxes, manage their lifecycle, equip them with
  appropriate tools, and oversee their execution, a process that could take
  weeks or months to set up. Now, with a few lines of code, users can spin up
  that same infrastructure at least 10x quicker than before."
- **Our assessment**: Eight companies with named executives all reporting the
  same order-of-magnitude improvement is strong testimonial evidence. The
  practitioner-getsentry-sentry profile gives us independent background on
  Sentry's AI engineering investment — they have a sophisticated internal AI
  setup (16 domain-specific skills, MCP server integration, 60+ permission
  allowlists), so their "weeks instead of months" is credible, not from a
  naive baseline. The time savings cluster around moving the infrastructure
  build off the critical path, not from the agent itself being faster.

### Claim 9: Dynamic tool generation — the agent codes up new tools on the fly for novel user queries — is enabled by the managed harness model

- **Evidence**: General Legal CTO Javed Qadrud-Din provides the clearest example:
  agents can handle any user query by generating the needed tool dynamically,
  rather than requiring pre-built tools for every anticipated query type.
- **Confidence**: anecdotal (single customer experience; no description of the
  mechanism enabling this)
- **Quote**: "Before Managed Agents, we would've had to anticipate every question
  our users might want to ask and build tools or prompt workflows for each one.
  Now, with Managed Agents it can code up any tool it needs on the fly, allowing
  it to handle virtually any user query."
- **Our assessment**: This is the most architecturally interesting customer claim.
  It implies the sandboxed code execution environment enables a pattern where the
  agent writes and executes its own tools as needed. This is a capability enabled
  by the sandbox — a DIY harness without sandboxed execution cannot safely allow
  agents to generate and run arbitrary code. The General Legal use case (document
  Q&A with arbitrarily variable query types) is a good illustration of where the
  pattern applies: domains where the query space is open-ended but the data source
  is bounded.

### Claim 10: Pricing is $0.08 per session-hour for active runtime, on top of standard Claude Platform token rates

- **Evidence**: Stated explicitly in the pricing section.
- **Confidence**: settled (as of April 8, 2026; subject to change)
- **Quote**: "Standard Claude Platform token rates apply, plus $0.08 per
  session-hour for active runtime."
- **Our assessment**: The session-hour pricing model is notable because it creates
  a non-token cost signal for long-running agents. A 6-hour build run (comparable
  to the retro game example in blog-anthropic-harness-long-running) would incur
  $0.48 in session-hour charges on top of token costs. The session-hour rate is
  small relative to token costs for typical agents — at Opus rates, 6 hours of
  heavy tool use would cost far more in tokens than $0.48. The more important
  pricing signal is the build-vs-buy comparison: $0.08/session-hour for the entire
  infrastructure stack vs. the engineering hours to build and maintain sandboxing,
  checkpointing, credential management, and tracing yourself.

### Claim 11: The Blockit meeting prep agent went from idea to production in days using Managed Agents, with MCP for external system integration

- **Evidence**: John Han (Co-founder, Blockit) provides the most implementation-
  rich testimonial: custom tools for calendar/contacts data, MCP for external
  systems (notetakers, CRMs), managed harness for sandboxed execution and built-in
  web search.
- **Confidence**: anecdotal (single company's experience)
- **Quote**: "Claude Managed Agents made it 3x faster to build a production-ready
  meeting prep agent. We went from idea to shipping in a matter of days. Our agent
  researches every participant ahead of a meeting to surface what matters for
  moving the conversation forward. Custom tools let us feed in our own calendar
  and contacts data, MCP made it simple to connect external systems like meeting
  notetakers, CRMs, etc., and the managed harness handled the heavy lifting,
  including sandboxed execution and built-in web search."
- **Our assessment**: The Blockit testimonial is the most technically specific and
  therefore the most useful for practitioners evaluating the platform. It shows
  the integration pattern: custom tools for proprietary data + MCP for external
  services + managed harness for execution infrastructure. This is the intended
  composition model. The "3x faster" claim is the most conservative speed-claim
  in the testimonials — and for context-managed assembly of existing integrations,
  it is plausible.

## Concrete Artifacts

### Platform Capability Matrix (from announcement)

```
Claude Managed Agents — Infrastructure Components:

EXECUTION LAYER:
  - Sandboxed code execution (for all agents)
  - Tool execution handled by platform
  - Built-in web search (mentioned in Blockit testimonial)

SESSION LAYER:
  - Long-running sessions (hours, autonomous)
  - Checkpointing (state persists through disconnections)
  - Credential management / authentication handled

ORCHESTRATION LAYER:
  - Built-in harness decides: when to call tools / how to manage context /
    how to recover from errors
  - Outcome mode: define success criteria → Claude self-evaluates + iterates
    (RESEARCH PREVIEW — requires separate access request)
  - Multi-agent coordination: agents spawn + direct sub-agents for parallel work
    (RESEARCH PREVIEW — requires separate access request)
  - Prompt-and-response mode: traditional workflow, tighter control (GA)

GOVERNANCE LAYER:
  - Scoped permissions
  - Identity management
  - Execution tracing (tool calls, decisions, failure modes via Claude Console)
  - Session tracing + integration analytics + troubleshooting guidance

OBSERVABILITY:
  - Claude Console: inspect every tool call, decision, failure mode
  - Integration analytics

INTEGRATION PATTERN (from Blockit testimonial):
  - Custom tools: inject proprietary data (calendar, contacts)
  - MCP: connect external systems (CRMs, notetakers, etc.)
  - Managed harness: sandboxed execution + built-in web search

PRICING:
  - Standard Claude Platform token rates (input + output)
  - + $0.08 per session-hour for active runtime
```

### Performance Benchmark (Anthropic internal)

```
Task: Structured file generation
Comparison: Managed Agents outcome loop vs. standard prompting loop
Result: Up to +10 points task success rate improvement
Condition: Largest gains on hardest problems
Source: Internal testing, Anthropic (not independently replicated)
Caveat: Outcome/self-evaluation feature is in research preview only
```

### Customer Deployment Timeline Evidence

```
Company         | Claim                                | Source
----------------|--------------------------------------|---------------------------
Sentry/Seer     | "weeks instead of months"            | Indragie Karunaratne, SVP Eng AI/ML
Atlassian/Jira  | "weeks instead of months"            | Sanchan Saxena, SVP Product
Vibecode        | "at least 10x quicker than before"   | Ansh Nanda, Co-founder
Rakuten         | "deploy each specialist agent within | Yusuke Kaji, GM AI for Business
                |  a week" (per domain)                |
Blockit         | "idea to shipping in a matter of days"| John Han, Co-founder
                | "3x faster to build"                 |
General Legal   | "cut development time by 10x"        | Javed Qadrud-Din, CTO
Asana           | "dramatically accelerated" shipping  | Amritansh Raghav, CTO
Notion          | handles "long-running sessions,      | Eric Liu, Product Manager
                |  manage memory, high-quality outputs"|
```

### Sentry/Seer Integration Pattern (most detailed technical testimonial)

```
Use case: Root cause analysis → automated fix → PR

Before Managed Agents:
  - Manual infrastructure: sandbox runtime + session management + credential
    scoping + custom agent loop

After Managed Agents:
  1. Seer identifies root cause (existing Sentry product)
  2. Claude-powered agent writes the fix + opens PR
  3. Platform handles: secure agent runtime + sandboxing + scoped permissions

What Sentry built: "seamless developer experience around the handoff"
What the platform handled: "secure, fully managed agent runtime"
Ongoing benefit: "eliminated the ongoing operational overhead of maintaining
                  bespoke agent infrastructure"

Source: Indragie Karunaratne, SVP Engineering AI/ML, Sentry
```

## Cross-References

- **Corroborates**:
  - **practitioner-getsentry-sentry**: Sentry is a named customer in this
    announcement. Indragie Karunaratne's quote about "secure, fully managed
    agent runtime" and "weeks instead of months" is first-party confirmation
    from a source already profiled in depth. The Sentry profile documented
    their sophisticated DIY agent configuration (16 skills, MCP server,
    granular permission allowlists); this announcement confirms they adopted
    Managed Agents for their Seer product rather than extending their DIY setup
    further. This is strong signal: even a team with one of the most mature
    DIY agent configurations in our corpus reached for the managed service for
    production deployment.
  - **blog-anthropic-harness-long-running**: The self-evaluation outcome loop
    ("define outcomes and success criteria, Claude iterates until it gets there")
    is architecturally identical to the generator/evaluator harness documented
    in that post — the platform productizes the same pattern. The "+10 points
    on structured file generation" benchmark is directionally consistent with
    that post's finding that the evaluator architecture "dramatically" improves
    quality on hard tasks. The session persistence claim also corroborates that
    post's Opus 4.6 finding of 2+ hour coherent sessions.
  - **blog-anthropic-harnessing-claude-intelligence**: The "built-in harness
    decides when to call tools, how to manage context" description is the
    productized version of that post's recommendations to delegate orchestration
    and context management to the model. The multi-agent coordination (agents
    spawning sub-agents) matches the subagent patterns documented there with
    benchmark evidence.
  - **discussion-hn-ttal-multiagent-factory**: Multi-agent coordination (agents
    spawning and directing sub-agents) is the same pattern as TTal's Manager/
    Worker plane architecture. Managed Agents is the fully-hosted version of
    what TTal implements as a local CLI: spawn worker agents, coordinate via a
    controller, parallelize complex tasks. The key difference is execution
    environment (cloud-hosted vs. local worktrees) and build-vs-buy tradeoff.
  - **blog-addyosmani-code-agent-orchestra**: The outcome-driven mode (define
    success criteria, iterate until met) is the productized version of Osmani's
    Ralph Loop and the "define outcomes + guardrails" design philosophy he
    describes. The multi-agent coordination matches his experimental Agent Teams
    feature. This announcement is the vendor's response to the orchestration
    patterns the practitioner community had been building independently.

- **Contradicts**: None filed. The most relevant tension is build-vs-buy
  (Managed Agents vs. DIY harness), but this is a design-space tradeoff on
  a control/convenience axis, not a factual contradiction. Specifically:
  - Kiln (discussion-hn-kiln-orchestration) advocated for self-hosted, locally-
    run orchestration with full control over state and dispatch. Managed Agents
    is the opposite design choice. Both are valid; the choice depends on
    whether the team values control or speed-to-production. The Sentry profile
    shows that even sophisticated DIY teams can reach for the managed service
    for specific use cases.
  - The DIY harness notes (blog-anthropic-harness-long-running,
    blog-anthropic-harnessing-claude-intelligence) give practitioners recipes
    for building their own. Managed Agents gives them an alternative to building.
    These are not contradictions — they are two answers to the same question
    with different tradeoffs.

- **Extends**:
  - **blog-anthropic-harness-long-running**: Managed Agents productizes the
    generator/evaluator and sprint-contract patterns from that post. Practitioners
    who read that post to understand harness design now have a hosted option that
    implements those designs without building them.
  - **practitioner-getsentry-sentry**: Adds the first documented case of a
    sophisticated DIY-agent-configured team adopting a managed service for
    production agent deployment (Seer + Managed Agents). Extends the Sentry
    profile from "how to configure a harness yourself" to "even well-configured
    teams reach for the managed service for production workloads."

- **Novel**:
  - **Infrastructure-as-product for agent deployment**: No existing source note
    describes a platform that bundles sandboxing + checkpointing + credential
    management + scoped permissions + execution tracing + multi-agent coordination
    as composable APIs. This is the first hosted agent infrastructure product
    to appear in our corpus.
  - **$0.08/session-hour pricing model**: The first concrete production pricing
    signal for agent runtime infrastructure in our corpus. The session-hour unit
    (not per-token, not per-request) is a novel pricing dimension that captures
    the "time alive" cost of long-running agents distinct from inference cost.
  - **Dynamic tool generation in production**: General Legal's pattern (agent
    generates tools on-the-fly for novel queries via sandboxed code execution)
    is not documented in any other source note. It implies a qualitatively
    different agent architecture than the tool-list-defined-at-design-time pattern
    that dominates our corpus.
  - **Outcome mode vs. prompt-and-response mode as a named design choice**:
    Framing the decision as "how much do you want to specify the how vs. the
    what" with the platform supporting both is new to our corpus as a first-class
    product design choice, even though the underlying patterns are documented
    elsewhere.
  - **Rakuten's cross-functional agent-per-domain deployment model**: "Deploy
    each specialist agent within a week" across engineering, product, sales,
    marketing, and finance. This is the first example in our corpus of
    organization-wide multi-domain agent deployment with a per-domain, per-week
    build cadence.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "Build vs. Buy" section that
  explicitly frames Managed Agents (and the emerging category of hosted agent
  platforms) as an alternative to DIY harness engineering. The tradeoff:
  - **Managed (Managed Agents)**: weeks-to-production, no infrastructure
    maintenance, no control over orchestration decisions, session-hour pricing
  - **Self-hosted (DIY with Claude Code + Agent SDK)**: full orchestration control,
    no session-hour overhead, weeks/months to build the same infrastructure,
    ongoing maintenance burden
  - The Sentry case study is the key evidence: even a team with one of the most
    mature DIY agent configurations in our corpus adopted the managed service
    for a specific production workload. DIY and managed are not mutually exclusive.

- **Chapter 02 (Harness Engineering)**: Document the "outcome mode vs.
  prompt-and-response mode" design choice as a first-class harness pattern.
  Current guide material focuses on prompt-and-response orchestration; this
  announcement introduces the outcome-loop pattern as a productized alternative
  where practitioners specify success criteria and delegate the iteration strategy
  to the model. This should sit alongside the generator/evaluator architecture
  (from blog-anthropic-harness-long-running) as the same underlying pattern at
  different abstraction levels.

- **Chapter 05 (Multi-Agent Orchestration)** or wherever multi-agent patterns
  land: Add Managed Agents' multi-agent coordination (agents spawning sub-agents
  to parallelize work) alongside TTal's Manager/Worker plane and Osmani's Agent
  Teams as three implementations of the same pattern at different points on the
  hosted/DIY spectrum. The convergence of independent practitioner tools (TTal),
  a vendor experimental feature (Agent Teams), and a production hosted service
  (Managed Agents) around the same architectural pattern is strong signal that
  this is the right abstraction.

- **Chapter 06 (Production Deployment)** or equivalent: The customer testimonials
  provide concrete deployment evidence for multiple agent use case patterns:
  - Coding agents: codebase → fix → PR (Sentry/Seer)
  - Productivity agents: join project, pick up tasks, deliver work (Asana AI Teammates)
  - Document intelligence: pull from documents + answer open-ended queries (General Legal)
  - Cross-functional domain agents: one specialist agent per business function
    deployed weekly (Rakuten)
  These are real production deployments from named companies, not speculative
  use cases. The guide should reference these as validated deployment patterns.

- **Chapter 08 (Governance / Permissions)**: The governance layer (scoped
  permissions + identity management + execution tracing) and the Claude Console
  visibility model (inspect every tool call, decision, failure mode) are
  enterprise-grade governance primitives that practitioners building DIY harnesses
  must replicate themselves. Document these as the production governance bar that
  any harness (DIY or managed) needs to meet.

## Extraction Notes

- The announcement is a marketing blog post, not an engineering post. Technical
  specifics live in the linked docs (platform.claude.com/docs/en/managed-agents/
  overview) and Claude Console (platform.claude.com/workspaces/default/agent-
  quickstart), which were not fetched for this extraction. A follow-up extraction
  of the Managed Agents documentation would provide the implementation-level detail
  missing here — specifically: API design, SDK integration patterns, how multi-agent
  coordination works mechanically, and what "scoped permissions" means in technical
  terms.
- **Glean is not mentioned in the article**. The Prospector's second triage comment
  listed Glean as a potential customer to look for; they are absent from the published
  announcement. Either the Glean integration was not ready for the launch post or it
  appeared in an earlier draft. Do not include Glean in any guide citations derived
  from this source.
- **Issue #132 (LangChain "Deep Agents Deploy")** is identified by the Prospector
  as a related counterpoint — an open-source alternative to Managed Agents that
  may have been written in direct response to this launch. That source has not been
  extracted yet. When it is extracted, the two notes should be cross-referenced to
  document the managed-vs-self-hosted architecture debate with both sides represented.
- The self-evaluation outcome loop and multi-agent coordination are both in research
  preview with separate access requests. Claims about these capabilities are forward-
  looking product descriptions, not generally available features at time of writing.
  The "+10 points task success" benchmark is specific to the self-evaluation feature
  (research preview), meaning most practitioners cannot reproduce or test this result
  today.
- The article cites Claude Code as a path to building with Managed Agents: "Developers
  can also use the latest version of Claude Code and built-in claude-api Skill to build
  with Managed Agents. Just ask 'start onboarding for managed agents in Claude API' to
  get started." This is the first mention in our corpus of a Claude Code skill that
  specifically targets a Claude Platform service. It suggests a tighter integration
  between Claude Code (the IDE/CLI tool) and Managed Agents (the platform service)
  than previously documented.
- Confidence is set to `anecdotal` overall because the performance claim is a single
  internal benchmark, the capability claims are vendor descriptions, and the customer
  testimonials — while from named individuals at real companies — have not been
  independently corroborated. Individual claims are rated at appropriate levels
  within the note.
