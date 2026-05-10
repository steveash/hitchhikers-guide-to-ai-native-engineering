---
source_url: https://www.anthropic.com/engineering/managed-agents
source_type: blog-post
title: "Scaling Managed Agents: Decoupling the Brain from the Hands"
author: Anthropic Engineering
date_published: 2026-04-08
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#388"
---

# Scaling Managed Agents: Decoupling the Brain from the Hands

> First-party Anthropic engineering deep-dive explaining the architectural
> design of the Managed Agents platform: three virtualized components
> (session, harness, sandbox), the "pets vs. cattle" motivation for
> decoupling, a 60%/90% TTFT improvement from stateless harnesses, and a
> security boundary that keeps credentials out of Claude-generated code.

## Source Context

- **Type**: blog-post (Anthropic Engineering Blog, April 8, 2026; same day as
  the product launch announcement on claude.com)
- **Author credibility**: First-party Anthropic engineering post explaining
  internal architectural decisions. The engineering blog is distinct from the
  marketing/product blog (claude.com) — it describes design rationale, failure
  modes, and tradeoffs from the team that built the system. The companion
  product announcement (blog-anthropic-claude-managed-agents.md) covers the
  user-facing capability list; this post covers the internal architecture
  decisions. Maximum authority for claims about why Managed Agents was designed
  this way.
- **Scope**: Covers the architectural transformation from a coupled
  (brain+hands+session in one container) to a decoupled design, the session
  model, the security boundary for credentials, and the multi-brain/multi-hand
  scalability design. Frames the design philosophy through the OS abstraction
  analogy. Does NOT cover: SDK integration, pricing, or the self-evaluation/
  outcomes feature. The article has five sections: introduction, "Don't adopt a
  pet," "Decouple the brain from the hands," "The session is not Claude's
  context window," "Many brains, many hands," and conclusion.

## Extracted Claims

### Claim 1: Harnesses encode assumptions about model limitations that go stale as models improve — the canonical example is context-anxiety resets that became dead weight on Opus 4.5

- **Evidence**: Named example with model version: Sonnet 4.5 exhibited context
  anxiety (premature task wrap-up as context window filled); harness added
  context resets as a fix; Opus 4.5 no longer exhibited the behavior; the
  resets became dead weight. This is not a benchmark — it is an architectural
  observation from the team running Managed Agents in production.
- **Confidence**: emerging (first-party observation with named model versions;
  see Contradicts for an existing corpus disagreement on which model version
  eliminated context anxiety)
- **Quote**: "In prior work we found that Claude Sonnet 4.5 would wrap up tasks
  prematurely as it sensed its context limit approaching—a behavior sometimes
  called 'context anxiety.' We addressed this by adding context resets to the
  harness. But when we used the same harness on Claude Opus 4.5, we found that
  the behavior was gone. The resets had become dead weight."
- **Our assessment**: This directly corroborates the meta-principle in
  blog-anthropic-harness-long-running.md (Claim 9: "every component in a
  harness encodes an assumption about what the model can't do on its own, and
  those assumptions are worth stress testing") and blog-anthropic-harnessing-
  claude-intelligence.md (Claim 15: context resets became "dead weight" by
  Opus 4.5). The specific claim that Opus 4.5 eliminated context anxiety
  conflicts with blog-anthropic-harness-long-running.md (Claims 7–8), which
  attributes the elimination to Opus 4.6. This is the existing contradiction
  filed as issue #232 (C-004 pending). See Cross-References.

### Claim 2: Managed Agents virtualizes three components — session, harness, sandbox — with stable interfaces that outlast the implementations behind them

- **Evidence**: Architectural description of the platform design, framed
  explicitly as the OS-abstraction parallel. The three components are named with
  their roles: session (append-only log of everything that happened), harness
  (the loop that calls Claude and routes Claude's tool calls to infrastructure),
  sandbox (execution environment where Claude can run code and edit files).
- **Confidence**: settled (first-party architectural description; this is what
  the platform does by design)
- **Quote**: "We virtualized the components of an agent: a session (the
  append-only log of everything that happened), a harness (the loop that calls
  Claude and route Claude's tool calls to the relevant infrastructure), and a
  sandbox (an execution environment where Claude can run code and edit files)."
- **Our assessment**: The virtualization framing is the key architectural
  contribution. By defining stable interfaces between session, harness, and
  sandbox, each layer can fail independently and be replaced without affecting
  the others. The OS analogy is explicitly made: process, file, and other
  abstractions outlasted the underlying hardware. The session/harness/sandbox
  interfaces are intended to outlast specific Claude models and harness designs.

### Claim 3: The original coupled design (brain+hands+session in one container) was a "pet" — failure cost the entire session and required manual recovery

- **Evidence**: First-person description of the original Managed Agents
  architecture and its failure mode, before the decoupling redesign.
- **Confidence**: settled (first-party retrospective; describes what was built
  and why it failed)
- **Quote**: "If a container failed, the session was lost. If a container was
  unresponsive, we had to nurse it back to health."
- **Quote (pets/cattle)**: "A pet is a named, hand-tended individual you can't
  afford to lose, while cattle are interchangeable."
- **Our assessment**: The "pets vs. cattle" framing is borrowed from
  infrastructure engineering (Urs Hölzle's original cattle metaphor for data
  center servers) and applied here to agent infrastructure. The coupled design
  created a pet problem: each agent session was a named, stateful unit that
  required human intervention on failure. The insight driving the redesign is
  that the session (state) and the harness (compute) should be separated so
  that harness failures are recoverable by booting a new, stateless harness
  from the durable session log.

### Claim 4: Decoupling the harness from the container dropped p50 TTFT by ~60% and p95 TTFT by over 90%

- **Evidence**: Specific latency metrics from the production Managed Agents
  deployment. The mechanism: in the coupled design, inference could not start
  until the container was provisioned; in the decoupled design, inference starts
  while the container is being provisioned, eliminating the provisioning wait
  from the critical path.
- **Confidence**: emerging (first-party metrics from production deployment; no
  independent replication; numbers are specific and directionally plausible)
- **Quote**: "Using this architecture, our p50 TTFT dropped roughly 60% and p95
  dropped over 90%."
- **Our assessment**: The p95 improvement (>90%) is more dramatic than p50
  (~60%), suggesting that tail latency was dominated by occasional slow container
  provisioning in the coupled design. Decoupling eliminates this tail by running
  inference before provisioning completes. This is a pure architectural win
  with no capability tradeoff — the decoupled design is faster, more resilient,
  AND more flexible. The numbers are from Anthropic's own infrastructure; no
  benchmark methodology is disclosed, but the mechanism makes them plausible.

### Claim 5: Stateless harnesses recover from failure by calling wake(sessionId) — they re-read the event log and resume without any per-harness state

- **Evidence**: Architectural description of the harness API and recovery
  mechanism. The harness exposes: `wake(sessionId)` to resume from an existing
  session, `getSession(id)` to retrieve session state, `emitEvent(id, event)`
  for durable event logging.
- **Confidence**: settled (first-party architectural description of the shipping
  API design)
- **Quote**: "The harness leaves the container." / "The container became cattle."
- **Our assessment**: The key insight is that "harness" is redefined from a
  stateful long-lived process to a stateless recovery function. Any new harness
  instance can call `wake(sessionId)` and pick up exactly where a crashed
  harness left off. This is the architectural enabler of the cattle model: since
  harnesses carry no state, any harness instance is interchangeable. The session
  event log is the source of truth; the harness is ephemeral compute that reads
  from it.

### Claim 6: The session is a context object that lives outside Claude's context window, enabling flexible retrieval via getEvents() rather than irreversible context trimming

- **Evidence**: Architectural description comparing the session to Claude's
  context window. The session stores all events durably; Claude can retrieve
  them flexibly via `getEvents()` rather than having stale context trimmed
  irreversibly by compaction.
- **Confidence**: settled (first-party architectural design description)
- **Quote**: "The session provides this same benefit, serving as a context
  object that lives outside Claude's context window."
- **Our assessment**: This is the architectural answer to context compaction
  failures documented in the corpus (failure-claudemd-ignored-compaction,
  failure-decker-4hr-session-loss). Instead of fighting the context window
  limit by trying to preserve content through compaction, the session model
  keeps the authoritative record outside Claude's context entirely. The model
  can then choose what to retrieve — "pick up from wherever it last stopped
  reading, rewind a few events before a specific moment to see the lead up,
  or reread context before a specific action" — rather than working with
  whatever survives compaction. This is a fundamentally different approach:
  compaction manages what fits in context; the session model separates context
  from record.

### Claim 7: The security boundary design ensures credentials are never accessible from the sandbox where Claude's generated code runs

- **Evidence**: Architectural design description with two specific credential
  patterns named.
- **Confidence**: settled (first-party security design description)
- **Quote**: "The structural fix was to make sure the tokens are never reachable
  from the sandbox where Claude's generated code runs. We used two patterns to
  ensure this. Auth can be bundled with a resource or held in a vault outside
  the sandbox."
- **Our assessment**: The motivation for this design is explicit: "In the
  coupled design, any untrusted code that Claude generated was run in the same
  container as credentials—so a prompt injection only had to convince Claude to
  read its own environment." The fix is architectural: the execution environment
  (where Claude-generated code runs) is structurally separated from credential
  storage. The two patterns — bundle auth with resource (e.g., Git clone token
  wired into local git remote at sandbox initialization) vs. vault + MCP proxy
  (OAuth tokens in a vault, accessed via a proxy that fetches credentials; the
  harness is never made aware of credentials) — give practitioners two templates
  for different credential types.

### Claim 8: Each sandbox exposes a uniform execute(name, input) → string interface, making any execution environment a swappable "hand" — containers, phones, and Pokémon emulators are all equivalent

- **Evidence**: Architectural description of the hands abstraction. The
  interface is a single function signature; the implementation behind it can
  be anything. The article explicitly names containers, phones, and Pokémon
  emulators as examples.
- **Confidence**: settled (first-party architectural description)
- **Quote**: (no single verbatim quote captures the full claim; paraphrase in
  Our assessment draws on: "whether the sandbox is a container, a phone, or a
  Pokémon emulator")
- **Our assessment**: The uniform tool interface is what enables the
  "many hands" design. Each hand exposes `execute(name, input) → string` and
  nothing else. Claude treats all hands identically; the harness routes tool
  calls to whichever hands are available. This is the same abstraction that
  makes MCP servers interchangeable in a harness — the interface stays constant;
  the implementation varies. The Pokémon emulator example is not whimsical: it
  references Anthropic's own experiments running Claude inside game environments,
  which appear in other corpus notes as qualitative memory benchmarks.

### Claim 9: Multiple brains (harness instances) can access multiple hands (sandboxes) — brains can pass hands to one another, enabling flexible multi-agent topologies

- **Evidence**: Architectural design description. Since harnesses are stateless
  and each sandbox is a uniform tool, multiple harnesses can connect to any
  combination of sandboxes. "Brains can pass hands to one another" is the
  mechanism for subagent tool delegation.
- **Confidence**: settled (first-party architectural description of the shipping
  design)
- **Quote**: "brains can pass hands to one another"
- **Our assessment**: This is the architectural foundation for the Managed
  Agents multi-agent coordination feature (public beta as of May 6, 2026 per
  blog-anthropic-managed-agents-dreaming-outcomes.md). "Brains passing hands"
  means an orchestrator agent can provision a sandbox and pass the tool
  reference to a subagent, rather than requiring subagents to provision their
  own execution environments. This enables the lead-agent-plus-specialists
  pattern with shared filesystem described in the dreaming-outcomes note without
  additional coordination overhead.

### Claim 10: The design philosophy is "opinionated about interfaces, unopinionated about implementations" — modeled on OS abstractions that outlasted the hardware they virtualized

- **Evidence**: Architectural philosophy stated explicitly in the article,
  backed by the OS analogy (process, file abstractions outlasted disk packs
  and SSDs). The conclusion frames Managed Agents as a "meta-harness" designed
  to accommodate harnesses "as yet unthought of."
- **Confidence**: settled (explicit design philosophy statement from first-party
  source)
- **Quote**: "Operating systems solved this problem by virtualizing hardware
  into abstractions—_process, file_—general enough for programs that didn't
  exist yet. The abstractions outlasted the hardware. The `read()` command is
  agnostic as to whether it's accessing a disk pack from the 1970s or a modern
  SSD."
- **Quote (conclusion)**: "Managed Agents is a meta-harness in the same spirit,
  unopinionated about the _specific_ harness that Claude will need in the
  future."
- **Our assessment**: This philosophy is the most durable claim in the article.
  The OS analogy is precise: Anthropic is betting that the three-way split
  (session/harness/sandbox) is the right level of abstraction — not too
  high-level (which would preclude unanticipated use cases) and not too
  low-level (which would require re-architecting for each model improvement).
  The "programs as yet unthought of" framing is a direct homage to Ken
  Thompson/Dennis Ritchie era OS design — the claim is that Managed Agents is
  to agent infrastructure what Unix was to computing infrastructure.

## Concrete Artifacts

### Harness API Signatures

```
# Managed Agents harness API (from engineering article, 2026-04-08)
# Source: https://www.anthropic.com/engineering/managed-agents

SESSION OPERATIONS:
  wake(sessionId)         — resume a session on a new stateless harness instance
  getSession(id)          — retrieve session metadata
  emitEvent(id, event)    — append an event to the session log (durable)
  getEvents()             — retrieve events from the session log (flexible retrieval)

SANDBOX OPERATIONS:
  provision({resources})  — initialize a sandbox with bundled auth/resources
  execute(name, input)    — uniform tool interface for all sandbox types
                            return type: string

ARCHITECTURE INVARIANT:
  The harness is never made aware of any credentials.
  Credentials are bundled with resources at provision() time or held in a vault
  accessed via a proxy — never accessible from the sandbox where Claude's
  generated code runs.
```

### Three-Component Virtualization Model

```
# Managed Agents: three virtualized components
# Source: https://www.anthropic.com/engineering/managed-agents

SESSION (append-only event log):
  - Lives outside Claude's context window
  - Durable: harness crash does not lose session
  - Retrieval: Claude calls getEvents() to read specific event ranges
  - Recovery: new harness calls wake(sessionId) to resume from log

HARNESS (agent loop):
  - Stateless: carries no session state between invocations
  - Calls Claude; routes Claude's tool calls to sandboxes
  - Connects to sandboxes on demand (no persistent pairing)
  - Scalable: multiple harness instances can connect to multiple sandboxes

SANDBOX (execution environment):
  - Uniform interface: execute(name, input) → string
  - Implementations: container, phone, Pokémon emulator, etc.
  - Security: credentials never accessible from sandbox
  - Cattle: interchangeable, provisioned on-demand

DECOUPLING BENEFIT:
  - Inference starts before container provisioning (eliminates provisioning
    from TTFT critical path)
  - p50 TTFT: -60% vs. coupled design
  - p95 TTFT: >-90% vs. coupled design
```

### Credential Security Patterns

```
# Two credential patterns for Managed Agents sandboxes
# Source: https://www.anthropic.com/engineering/managed-agents

PATTERN 1 — Bundle auth with resource:
  Example: Git repository access
  Mechanism: provide each repository's access token to clone the repo during
             sandbox initialization and wire it into the local git remote
  Security: token is consumed at provision() time; not accessible post-init

PATTERN 2 — Vault + MCP proxy:
  Example: OAuth tokens for external services
  Mechanism: OAuth tokens stored in a secure vault outside the sandbox;
             Claude calls MCP tools through a dedicated proxy that fetches
             credentials; the harness is never made aware of any credentials
  Security: credentials never traverse the sandbox boundary

THREAT MODEL ADDRESSED:
  In the original coupled design: "any untrusted code that Claude generated
  was run in the same container as credentials—so a prompt injection only
  had to convince Claude to read its own environment."
  In the decoupled design: structural separation ensures credentials are
  unreachable from Claude-generated code even under prompt injection.
```

### Pets vs. Cattle Evolution

```
# From "pets" to "cattle": Managed Agents infrastructure evolution
# Source: https://www.anthropic.com/engineering/managed-agents

COUPLED DESIGN (pet):
  - Session, harness, and sandbox co-located in one container
  - Container failure = session loss
  - Unresponsive container = manual recovery required
  - Scaling required maintaining many distinct, named, long-lived containers
  - TTFT: container provisioned before inference starts

DECOUPLED DESIGN (cattle):
  - Session: durable event log (outside any container)
  - Harness: stateless, recoverable via wake(sessionId)
  - Sandbox: provisioned on-demand, uniform interface
  - Container failure = boot new harness, call wake(sessionId), resume
  - TTFT: inference starts while container provisioning runs in parallel
  - p50 TTFT: -60%; p95 TTFT: >90% improvement
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-harness-long-running.md** (Claim 9): "every component in
    a harness encodes an assumption about what the model can't do on its own,
    and those assumptions are worth stress testing." This article's context-
    anxiety example (Claim 1 here) is a direct illustration of exactly that
    principle: context resets were a component encoding a Sonnet 4.5 limitation
    that became dead weight on Opus 4.5. Both sources are first-party Anthropic
    posts making the same meta-argument from different angles.
  - **blog-anthropic-harnessing-claude-intelligence.md** (Claim 15): That note
    documents the same context-anxiety example — "Earlier agent versions needed
    context-reset logic to handle 'context anxiety,' but Opus 4.5 exhibited no
    such behavior, making the resets 'dead weight.'" The managed-agents
    engineering article corroborates this: Opus 4.5 eliminated context anxiety.
    Both are consistent on model version (Opus 4.5). **This is Side A of the
    existing contradiction issue #232 (C-004 pending)** — do not cite as settled
    until that contradiction is resolved.
  - **blog-anthropic-claude-managed-agents.md**: The product announcement
    describes what Managed Agents does; this engineering article describes *why*
    it was designed that way. Together they form the complete picture: capability
    list (product note) + architectural rationale (this note). The product
    announcement's session persistence claim (Claim 3 there: "long-running
    sessions that operate autonomously for hours, with progress and outputs that
    persist even through disconnections") is the user-facing expression of the
    session-as-durable-event-log design (Claim 6 here).
  - **blog-anthropic-managed-agents-dreaming-outcomes.md** (Claim 7): "events
    are persistent and every agent remembers what it's done." This is the same
    session/event-log architecture described here — the dreaming-outcomes note's
    multiagent mid-workflow check-in capability is built on the durable event
    log whose design this article explains.
  - **failure-decker-4hr-session-loss.md**: Decker's session loss is the
    user-side symptom of the failure mode this article's decoupled session
    design addresses architecturally. The decker failure occurred because
    session state was coupled to a single process; the Managed Agents session
    log is designed so that no harness crash can lose session state.
  - **failure-claudemd-ignored-compaction.md**: The session-as-context-object
    design (Claim 6 here, `getEvents()` for flexible retrieval) is a structural
    alternative to compaction. Where that failure note documents compaction as
    lossy and unreliable, this article shows that Managed Agents sidesteps the
    problem by keeping the authoritative record outside Claude's context window
    entirely.

- **Contradicts**:
  - **blog-anthropic-harness-long-running.md** (Claims 7–8) on which model
    eliminated context anxiety: That post attributes context-anxiety elimination
    to Opus 4.6 (and claims Opus 4.5 still exhibited it). This article and
    blog-anthropic-harnessing-claude-intelligence.md both attribute elimination
    to Opus 4.5. This is the existing **contradiction issue #232 (C-004
    pending)**. Do not cite either side as settled until resolved. Note: this
    source adds a third first-party Anthropic source agreeing that Opus 4.5
    eliminated context anxiety, strengthening Side A of that contradiction.

- **Extends**:
  - **blog-anthropic-claude-managed-agents.md**: Adds the engineering
    architecture rationale behind the product features. The "why decoupled?"
    question is not answered in the product announcement; this article answers
    it with the pets-vs-cattle failure analysis, the TTFT metrics, and the OS
    abstraction philosophy.
  - **blog-anthropic-harness-long-running.md**: That post documents the
    principle of pruning stale harness components at model upgrades; this
    article shows the same principle applied at the platform level — building
    Managed Agents' interfaces to be stable even as the harnesses and models
    behind them change.

- **Novel**:
  - **Three-way virtualization (session/harness/sandbox) as an architecture
    pattern**: No prior corpus source names this three-way split as the
    canonical decomposition for agent infrastructure. This is the first
    Anthropic-published architectural taxonomy for what a production agent
    platform must virtualize.
  - **Stateless harness recovery via wake(sessionId)**: The specific recovery
    API design — boot a new harness, call wake(sessionId), resume from durable
    event log — is not documented in any prior corpus source. This is a concrete
    pattern for building crash-resilient agent harnesses without stateful
    containers.
  - **TTFT improvement metrics from architectural decoupling**: The -60%/−90%
    TTFT improvement from decoupling harness from container is the first corpus
    benchmark showing latency impact from an agent infrastructure architecture
    decision (vs. model choice or prompt engineering decisions).
  - **Credential security design pattern for agent sandboxes**: The two-pattern
    credential isolation design (bundle with resource vs. vault+proxy) and its
    threat model (prompt injection → credential read in coupled design) is the
    most specific security architecture guidance for agent sandboxing in the
    corpus.
  - **OS abstraction analogy applied to agent platform design**: The explicit
    framing of agent infrastructure in OS-abstraction terms ("programs as yet
    unthought of," session/harness/sandbox as process/file equivalents) is a
    design philosophy statement not present in other corpus sources.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The three-way virtualization
  (session/harness/sandbox) should be added as the canonical architectural
  decomposition for production agent infrastructure. The design principle —
  "opinionated about interfaces, unopinionated about implementations" — gives
  practitioners a durable framework for evaluating both DIY and managed
  harness designs. Add alongside the product announcement note (blog-anthropic-
  claude-managed-agents.md) as the engineering rationale that explains the
  product choices.

- **Chapter 02 (Harness Engineering)**: The `wake(sessionId)` recovery pattern
  (boot stateless harness, resume from durable session log) should be presented
  as the architectural answer to session persistence failures documented in
  failure-decker-4hr-session-loss.md and failure-claudemd-ignored-compaction.md.
  The specific API signatures (`wake`, `getSession`, `emitEvent`, `getEvents`)
  are concrete design vocabulary for practitioners building their own stateless
  harnesses.

- **Chapter 02 (Harness Engineering)**: The credential security patterns
  (Claim 7, bundle-with-resource vs. vault+proxy) should anchor any section
  on agent security design. The threat model statement — "a prompt injection
  only had to convince Claude to read its own environment" in the coupled design
  — is the clearest articulation in the corpus of why credential isolation is
  structurally required, not optionally desirable.

- **Chapter 04 (Context Engineering)**: Claim 6 (session as durable context
  object outside Claude's window, `getEvents()` for flexible retrieval) should
  be presented as a structural alternative to compaction-based context
  management. The contrast: compaction manages what *fits* in context (lossy,
  irreversible); session log keeps the authoritative record *outside* context
  (lossless, flexible). The guide currently covers compaction strategies; this
  is the architectural design option that sidesteps the problem entirely.

- **Chapter 02 or Chapter 05 (Multi-Agent / Scalability)**: Claim 9 (brains
  can pass hands to one another) should be noted as the platform mechanism
  behind Managed Agents' multi-agent coordination feature. Practitioners
  building DIY multi-agent systems can implement an analogous pattern: orchestrator
  provisions a sandbox, passes the tool reference to a subagent; subagent
  calls `execute(name, input)` without managing the sandbox lifecycle.

- **Chapter 02 (Harness Engineering)** — TTFT and latency: The -60%/−90%
  TTFT improvement from decoupling should be cited wherever the guide discusses
  agent latency optimization. The mechanism (inference starts before container
  provisioning) is generalizable: any harness that can separate "start thinking"
  from "provision execution environment" will see similar TTFT improvements.

## Extraction Notes

- This article is from Anthropic's engineering blog (anthropic.com/engineering),
  distinct from the consumer/product blog (claude.com/blog). The engineering
  blog is the primary vehicle for Anthropic's technical architecture
  documentation. The product announcement for the same day (blog-anthropic-
  claude-managed-agents.md, from claude.com/blog) and this engineering post
  together form a complementary pair; neither is complete without the other.
- Author attribution: the article's byline and acknowledgements section were
  not extracted verbatim. The article is attributed to "Anthropic Engineering"
  as the institutional author; individual author names were not confirmed in
  the fetch.
- The context-anxiety quote (Claim 1) names Sonnet 4.5 and Opus 4.5
  specifically. This is the third first-party Anthropic source consistent
  with the Opus 4.5 resolution (alongside blog-anthropic-harnessing-claude-
  intelligence.md Claim 15). It does not resolve contradiction issue #232
  (C-004 pending) because both this source and harnessing-claude-intelligence
  could be wrong — the corpus needs the contradiction resolved against the
  harness-long-running data. The issue is noted but no new contradiction filed.
- The `execute(name, input) → string` interface and the five API signatures
  (`wake`, `getSession`, `emitEvent`, `getEvents`, `provision`) appear to be
  simplified conceptual representations of the actual API, not necessarily
  exact SDK method names. They are reproduced as stated in the article.
- The Pokémon emulator example in Claim 8 references the same Pokémon memory
  benchmark used in blog-anthropic-harnessing-claude-intelligence.md (Claim 9
  there: Pokémon game memory quality comparison at 14,000 steps). The managed-
  agents article uses it as a hands abstraction example; the harnessing article
  uses it as a memory quality illustration. They draw on the same internal
  experiment in different contexts.
