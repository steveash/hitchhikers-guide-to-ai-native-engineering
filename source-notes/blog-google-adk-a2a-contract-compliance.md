---
source_url: https://developers.googleblog.com/build-cross-language-multi-agent-team-with-google-agent-development-kit-and-a2a/
source_type: blog-post
title: "Build Cross-Language Multi-Agent Team with Google's Agent Development Kit and A2A"
author: Shubham Saboo and Eric Dong, Google Developers Blog
date_published: 2026-06-22
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1675"
---

# Build Cross-Language Multi-Agent Team with Google's Agent Development Kit and A2A

> Google's first-party implementation guide for a working, open-source
> contract-compliance pipeline that chains a Python/Gemini extraction agent
> to a deterministic Go compliance validator via ADK's `RemoteA2aAgent` and
> the A2A protocol — the corpus's first source with a fully worked,
> checkpoint-based orchestrator-subagent/shared-state hybrid, an explicit
> tool-count decomposition rationale, and a named fail-safe state for
> unreachable downstream agents.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party
  implementation guide with inline code samples and a linked open-source
  GitHub repository, published June 22, 2026)
- **Author credibility**: Shubham Saboo and Eric Dong are named authors
  publishing on Google's own developer blog about a Google-authored
  framework (ADK) and a protocol Google co-stewards (A2A). Their specific
  job titles could not be independently confirmed from the raw page HTML
  (see Extraction Notes) — treat as Google-affiliated first-party technical
  content, not independent practitioner analysis. The post links a
  companion open-source repository
  (`github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline`),
  which makes the architectural claims independently checkable in principle,
  though this extraction did not clone or execute the repo.
- **Scope**: Covers one worked example end-to-end — a "Contract Compliance"
  pipeline combining a Python/Gemini extraction agent, a Go deterministic
  compliance validator exposed as a remote A2A agent, and a Python report
  generator, orchestrated by an ADK `SequentialAgent`/Coordinator. Explains
  the rationale for decomposing into multiple agents, the A2A discovery/
  handshake mechanics, a shared-state checkpoint enum (`ComplianceStep`), a
  MANUAL_REVIEW fail-safe for an unreachable downstream agent, and a
  three-panel operations UI for demoing fault injection. Does NOT cover:
  performance/latency numbers, cost, multi-tenant or multi-customer
  deployment concerns, authentication/authorization for the A2A endpoints,
  or a comparison against non-ADK cross-language integration approaches
  (e.g., hand-rolled gRPC or REST).

## Extracted Claims

### Claim 1: Beyond roughly 10-15 tools, a single LLM agent starts missing instructions, calling the wrong tool, or hallucinating parameters — named as the "context degradation" reason to decompose into multiple agents
- **Evidence**: First-party rationale given as the first of three named
  reasons (alongside blast radius and testability) for splitting a
  monolithic agent into a multi-agent pipeline.
- **Confidence**: emerging (a specific numeric threshold stated as fact by
  the vendor, but not accompanied by a benchmark, eval, or citation in this
  post — it reads as accumulated internal experience, not a measured result)
- **Quote**: "As tools multiply beyond 10-15, the model starts missing instructions, calling wrong tools, or hallucinating parameters."
- **Our assessment**: This is a specific, falsifiable numeric claim (a
  10-15 tool ceiling) rather than a vague "keep context small" platitude,
  which makes it more useful to a practitioner than most decomposition
  advice in the corpus. It is not new in kind — the corpus already has
  extensive context-window-scarcity coverage — but it is new in giving a
  concrete tool-count number as the specific symptom threshold, rather than
  a token-budget or agent-count threshold.

### Claim 2: A single unhandled exception in a minor feature of a monolithic agent crashes the entire agent turn — named "blast radius" as a second reason to decompose
- **Evidence**: Second of the three named decomposition reasons, presented
  as a bullet labeled "Blast radius."
- **Confidence**: emerging (architecturally plausible engineering claim,
  stated without a specific incident or reproduction in this post)
- **Quote**: "One unhandled exception in a minor feature crashes the entire agent turn."
- **Our assessment**: This reframes decomposition as a fault-isolation
  argument, distinct from Claim 1's context-budget argument. Splitting a
  Go compliance check into its own remote agent means a crash in that
  service produces a routable failure (see Claim 8's MANUAL_REVIEW
  fail-safe) rather than taking down the whole pipeline — the two claims
  are connected in this source: decomposition (Claim 2) is what makes the
  fail-safe state machine (Claim 8) possible in the first place.

### Claim 3: A monolithic agent with 50 entangled responsibilities cannot be cleanly unit tested — named "Untestable" as the third reason to decompose
- **Evidence**: Third of the three named decomposition reasons, presented
  as a bullet labeled "Untestable."
- **Confidence**: anecdotal (a general software-engineering assertion,
  illustrated with a round "50 entangled responsibilities" figure rather
  than a specific test-suite example from this project)
- **Quote**: "You can't cleanly unit test a system with 50 entangled responsibilities."
- **Our assessment**: This is the weakest-evidenced of the three
  decomposition reasons (no example test, no before/after comparison) but
  it is a distinct axis from Claims 1-2: testability is an engineering-process
  argument, not a runtime-behavior argument. Combined with Claims 1-2, this
  source's three-part decomposition rationale (context degradation, blast
  radius, untestability) is a more complete practitioner checklist than any
  single reason alone.

### Claim 4: A2A solves agent discovery by having agents advertise capabilities through Agent Cards — JSON metadata served at a well-known URL
- **Evidence**: First-party protocol description in the "why A2A" section
  of the post, naming discovery as one of three problems A2A solves.
- **Confidence**: settled (a direct, falsifiable protocol mechanism
  description, corroborated by the same discovery mechanism already
  documented in `blog-google-a2a-collaborative-agents.md`)
- **Quote**: "Agents advertise their capabilities through Agent Cards, JSON metadata served at /.well-known/agent.json."
- **Our assessment**: This is consistent with, and gives a concrete file
  path/mechanism for, the discovery layer that `blog-google-a2a-collaborative-agents.md`
  described only in the abstract. This source additionally shows the
  discovery mechanism paired with a concrete Go implementation file
  (`go-compliance-agent/internal/agentcard/card.go`, see Concrete
  Artifacts), which is the first corpus source to show A2A discovery at
  the file/code level rather than the protocol-description level.

### Claim 5: ADK's `RemoteA2aAgent` abstraction lets a Python developer treat a remote, cross-language A2A service as a local sub-agent, with the SDK handling the handshake, serialization, and network calls automatically
- **Evidence**: First-party feature description of the `RemoteA2aAgent`
  class, illustrated by wrapping the Go compliance validator as a Python
  sub-agent.
- **Confidence**: settled (a direct SDK-behavior description of a shipped
  class, though the "automatically" framing is vendor-stated ease-of-use
  language not independently verified by running the code in this
  extraction)
- **Quote**: "The SDK automatically handles the Agent Card handshake, parameter serialization, and JSON-RPC network requests behind the scenes."
- **Our assessment**: This is the single most actionable implementation
  detail in the post for a practitioner building a cross-language agent
  system today: it names the specific abstraction (`RemoteA2aAgent`) that
  removes hand-written HTTP/JSON-RPC glue code between a Python orchestrator
  and a non-Python service. It is the concrete "how" that complements the
  abstract "why A2A" framing already in the corpus.

### Claim 6: ADK's `ToolContext.state` provides a shared dictionary that all sub-agents in a pipeline read from and write to, acting as a data bus between agents
- **Evidence**: First-party description of the shared-state mechanism used
  to pass extracted contract data and pipeline status between the
  extraction, compliance, and report agents.
- **Confidence**: settled (a direct SDK-mechanism description; the shared
  dictionary is shown driving the pipeline's checkpoint transitions in the
  ComplianceStep enum, Claim 7)
- **Quote**: "ADK's ToolContext.state provides a shared dictionary that all sub-agents in a pipeline read and write to."
- **Our assessment**: This is a concrete, shipped implementation of the
  "shared state" coordination pattern named in
  `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 1 taxonomy;
  Claim 5 termination-condition failure mode) — but notably, it is used
  *inside* a `SequentialAgent`-orchestrated pipeline (Claim 9) rather than
  as a standalone, coordinator-free shared-state topology. This is a
  hybrid of two of that taxonomy's five named patterns, not a pure instance
  of either one (see Cross-References and Guide Impact).

### Claim 7: The compliance pipeline's state is modeled as an explicit seven-value checkpoint enum — INGESTED, EXTRACTED, COMPLIANCE_PENDING, COMPLIANCE_COMPLETE, MANUAL_REVIEW, REVIEW_READY, APPROVED
- **Evidence**: Direct enumeration of the `ComplianceStep` states, each
  described as mapping to a specific pipeline checkpoint.
- **Confidence**: settled (a direct, falsifiable code-level enumeration
  from the source)
- **Quote**: "Each step in our compliance pipeline maps to a specific checkpoint: INGESTED, EXTRACTED, COMPLIANCE_PENDING, COMPLIANCE_COMPLETE, MANUAL_REVIEW, REVIEW_READY, APPROVED."
- **Our assessment**: This is a concrete instance of exactly the kind of
  explicit termination/checkpoint condition that
  `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 5) argues a
  shared-state pattern needs to avoid reactive, unbounded loops — here
  realized as a fixed, finite enum rather than a time budget or a judge
  agent. Because the enum is finite and the pipeline is sequentially
  orchestrated (Claim 9), convergence is structurally guaranteed by the
  state machine design itself, which is a stronger guarantee than the
  three termination mechanisms (time budget, convergence threshold, judge
  agent) that Anthropic's post names as sufficient-but-not-guaranteed
  mitigations for free-form shared state.

### Claim 8: When the Go compliance agent is unreachable (server crash, network timeout, container not started), the pipeline does not fail outright — it transitions to a MANUAL_REVIEW state that routes the case to a human legal reviewer
- **Evidence**: First-party description of the pipeline's fail-safe
  behavior, explicitly called out as "worth highlighting" in the source.
- **Confidence**: settled (a direct, specific behavioral description of a
  shipped fail-safe state, illustrated with a named enum value from Claim
  7's checkpoint list)
- **Quote**: "If the Go compliance agent is unreachable for reasons like server crash, network timeout, container not started - the pipeline doesn't just fail. It transitions to MANUAL_REVIEW, routing the case to a human legal reviewer."
- **Our assessment**: This is the most concrete resilience pattern in the
  post and is novel to the corpus: a named, coded fail-safe state
  (MANUAL_REVIEW) that a cross-language multi-agent pipeline enters when a
  downstream service dependency is unreachable, rather than surfacing a raw
  error or retrying indefinitely. It is a specific instance of "graceful
  degradation to a human in the loop" scoped to infrastructure failure
  (a service being down), which is a different failure mode than the
  information-bottleneck or termination-condition failure modes already
  documented for multi-agent patterns in the corpus — this is an
  availability failure mode, not a coordination-logic failure mode.

### Claim 9: The pipeline is orchestrated by a Coordinator (`SequentialAgent`) that chains three specialized sub-agents — a Python extractor, the remote Go compliance validator, and a Python report generator — in a fixed sequence
- **Evidence**: First-party architecture description plus a verbatim code
  fragment listing the `sub_agents` array.
- **Confidence**: settled (direct code artifact from the source)
- **Quote**: "Coordinator: Chains them together sequentially"
- **Our assessment**: This is a textbook instance of the orchestrator-subagent
  pattern already named as the corpus's recommended default
  (`blog-anthropic-multi-agent-coordination-patterns.md`, Claim 7), but it
  is the first corpus source to show that pattern spanning a language
  boundary (Python orchestrator, Go sub-agent) via A2A rather than all
  sub-agents running in the same process/language. The `sub_agents=[extractor_agent, compliance_agent, report_agent]`
  array (see Concrete Artifacts) shows the orchestration is a fixed,
  three-step sequence, not a dynamic routing decision — closer to a
  pipeline than a general-purpose dispatcher.

### Claim 10: Go was chosen for the compliance validator specifically because it is fully deterministic and produces identical, reproducible policy verdicts for audit purposes, while Python/Gemini was kept for the ambiguous extraction step
- **Evidence**: First-party rationale for the language/component split,
  framed as a "cognitive reasoning vs. deterministic enforcement" division
  of labor.
- **Confidence**: settled (a direct, specific architectural rationale
  statement from the source; the underlying determinism claim about Go
  itself is a property of the validator's implementation choice — avoiding
  an LLM — not a property of the Go language)
- **Quote**: "By bridging Python's AI ecosystem and Go's runtime reliability using Google ADK and the open A2A protocol, you get the best of both worlds: cognitive reasoning where there is ambiguity, and deterministic enforcement where there is policy."
- **Our assessment**: This is the clearest articulation in the corpus of a
  specific decision rule for splitting a pipeline by language: put
  ambiguous, language-understanding work behind an LLM agent, and put
  policy/compliance-verdict work behind a deterministic, non-LLM service,
  regardless of which language each happens to be written in. The
  determinism benefit is actually a property of "no LLM in the loop," not
  of Go specifically — the post's own framing ("using all deterministic
  logic and no LLM") supports reading this as an LLM-vs-non-LLM split that
  happens to also be a Python-vs-Go split in this example, which a
  practitioner could replicate in a single language just as validly.

### Claim 11: The demo ships a three-panel operations UI — a contract selection panel, a live results panel, and a developer console with policy controls, network-fault simulation, and a real-time inspector of the request/response data crossing the Python-Go language boundary
- **Evidence**: First-party description of the "Three-panel operations
  cockpit" and "Live agent handoff inspector" features of the linked demo.
- **Confidence**: emerging (a feature description of a demo/reference UI,
  not evaluated for production-readiness or usability by anyone other than
  the vendor in this post)
- **Quote**: "The right panel is a developer console with policy controls, network simulation, and a real-time view of the data flowing between the two agents."
- **Our assessment**: This is a concrete example of purpose-built
  observability tooling for a cross-language agent pipeline: rather than
  requiring a developer to read logs to see what crossed the A2A boundary,
  the demo UI surfaces live request/response inspection and lets an
  operator simulate the network failure that triggers Claim 8's
  MANUAL_REVIEW fail-safe. This is a useful worked example of what
  "observability for multi-agent handoffs" can look like concretely, which
  the corpus has mostly discussed in the abstract (e.g., message-bus event
  logging in `blog-anthropic-multi-agent-coordination-patterns.md`, Claim
  6) rather than as a built operator-facing tool.

## Concrete Artifacts

### Three named reasons to decompose a monolithic agent (verbatim labels + sentences, from the "why decompose" section)
```
Context degradation: As tools multiply beyond 10-15, the model starts
missing instructions, calling wrong tools, or hallucinating parameters.

Blast radius: One unhandled exception in a minor feature crashes the
entire agent turn.

Untestable: You can't cleanly unit test a system with 50 entangled
responsibilities.
```
Source: developers.googleblog.com, "Build Cross-Language Multi-Agent Team
with Google's Agent Development Kit and A2A" (2026-06-22).

### ComplianceStep checkpoint enum (verbatim from source)
```
INGESTED, EXTRACTED, COMPLIANCE_PENDING, COMPLIANCE_COMPLETE,
MANUAL_REVIEW, REVIEW_READY, APPROVED
```
Source: same post, ComplianceStep description. The enum drives the
pipeline's state machine; MANUAL_REVIEW is entered when the Go agent is
unreachable rather than as a normal-path step (Claim 8).

### SequentialAgent Coordinator wiring (verbatim code fragment)
```python
sub_agents=[extractor_agent, compliance_agent, report_agent]
```
Source: same post, "Coordinator" section describing the three-agent chain
(Python extractor → Go compliance validator wrapped via RemoteA2aAgent →
Python report generator).

### A2A protocol/version and file-level implementation details (confirmed against raw fetched HTML, not just the WebFetch summarizer)
```
Protocol version:  "ProtocolVersion": "1.0"
Extraction model:  gemini-3.5-flash (Python extraction agent)
Go agent card impl: go-compliance-agent/internal/agentcard/card.go
Python agent impl:  python-extraction-agent/app/agent.py
GitHub repo:        https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline
Go sub-repo link:   https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline/go-compliance-agent
```
Source: same post; the GitHub URLs were confirmed as `href` attributes in
the raw HTML (not just the small-model WebFetch summary — see Extraction
Notes).

### MANUAL_REVIEW fail-safe trigger conditions (verbatim from source)
```
"If the Go compliance agent is unreachable for reasons like server
crash, network timeout, container not started - the pipeline doesn't
just fail. It transitions to MANUAL_REVIEW, routing the case to a
human legal reviewer."
```
Source: same post, section explicitly flagged by the authors as "worth
highlighting."

## Cross-References

- **Corroborates**:
  - `blog-google-a2a-collaborative-agents.md` (Claim 1, "black box" handoff
    to a specialized internal agent; general A2A framing): this source
    corroborates A2A's role as a cross-boundary delegation protocol and
    adds the concrete Agent Card discovery mechanism (Claim 4 here) at the
    file/code level, where the earlier note described discovery only in
    the abstract.
  - `blog-google-adk-kotlin-android-agents.md` (Concrete Artifacts, "Tooling
    & Integrations" feature table listing "A2A" as a first-class ADK
    integration surface): this source is a concrete, worked demonstration
    of that listed-but-unillustrated A2A integration capability, this time
    in ADK for Python rather than ADK for Kotlin.
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7, the
    explicit recommendation to default to orchestrator-subagent "for most
    use cases"): this source's `SequentialAgent` Coordinator (Claim 9) is a
    concrete, shipped, cross-language instance of exactly that recommended
    default pattern.

- **Contradicts**: None identified. No existing corpus note makes a claim
  about multi-agent decomposition rationale, A2A implementation mechanics,
  or fail-safe state design that this source disagrees with.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 5, "shared
    state requires first-class termination conditions... at minimum: a time
    budget, a convergence threshold, or a designated judge agent"; guide
    text at `guide/02-harness-engineering.md` lines 1281-1283 names
    "consider a shared-state hybrid" as the guard for orchestrator-subagent's
    information-bottleneck failure mode): this source's ComplianceStep enum
    (Claim 7) is a concrete, shipped instance of that named-but-unillustrated
    "shared-state hybrid" — a finite checkpoint enum used as shared state
    *within* a sequentially orchestrated pipeline, rather than a free-form
    shared-state topology with no central coordinator. This is a fourth,
    more structurally constrained termination mechanism (a finite state
    machine) beyond the three Anthropic's post names (time budget,
    convergence threshold, judge agent).
  - `blog-google-a2a-collaborative-agents.md`: extends that post's abstract
    "Zero Context Pollution" advantage (peer agents "handle their own
    massive dependencies and internal state") with a concrete illustration
    of what stays out of the caller's context: the Go compliance agent's
    deterministic policy logic and its entire runtime never enter the
    Python orchestrator's LLM context — only the pass/fail verdict and
    extracted fields cross the A2A boundary via `ToolContext.state`.

- **Novel**:
  - **A named, coded fail-safe state (MANUAL_REVIEW) for an unreachable
    downstream agent** (Claim 8): no existing corpus source documents this
    specific "route to human review on infrastructure failure, not just on
    low-confidence output" pattern for a multi-agent pipeline.
  - **A three-part, tool-count-specific decomposition rationale** (Claims
    1-3, especially the 10-15 tool numeric threshold in Claim 1): no prior
    corpus source gives a specific numeric tool-count ceiling as the
    concrete symptom that triggers decomposition.
  - **A cross-language orchestrator-subagent/shared-state hybrid, shown at
    the code level** (Claims 6, 7, 9): the corpus's existing multi-agent
    taxonomy names orchestrator-subagent and shared state as two of five
    distinct patterns; this source is the first to show them combined in a
    single shipped pipeline, with the checkpoint enum acting as the
    termination mechanism for the shared-state component.
  - **An explicit language-choice rule tied to determinism, not
    familiarity** (Claim 10): "put the ambiguous work behind an LLM, put
    the policy-verdict work behind deterministic non-LLM logic" is a
    specific, replicable decision rule not previously stated this
    concretely in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering), "Multi-Agent Coordination Patterns"
  section** (`guide/02-harness-engineering.md`, ~lines 1261-1349, currently
  sourced from `blog-anthropic-multi-agent-coordination-patterns`): add
  this source's three decomposition reasons (Claims 1-3: context
  degradation past 10-15 tools, blast radius, untestability) as a concrete
  "why decompose in the first place" checklist that precedes the existing
  "which pattern" taxonomy — the guide currently jumps straight to pattern
  selection without stating the symptom threshold that should trigger
  considering decomposition at all. Also add this source's ComplianceStep
  enum (Claim 7) as a worked example next to the existing orchestrator-subagent
  guard text "consider a shared-state hybrid" (line 1283) — currently that
  guard is stated but not illustrated with a shipped example; this source
  provides one, plus a cross-language (Python/Go) instance of the
  orchestrator-subagent default pattern (Claim 9) that the section
  currently only illustrates with single-language/single-process examples.

- **Chapter 06 (Security Threat Model)**: no existing content in this
  chapter covers fail-safe behavior when a downstream agent/service in a
  pipeline becomes unreachable (confirmed by search — no matches for
  "unreachable," "fallback," "fail-safe," or "human review" in the current
  chapter text). Add Claim 8's MANUAL_REVIEW pattern as a concrete
  resilience/degradation control: route to human review specifically on
  infrastructure failure (server crash, timeout, container not started),
  as distinct from routing to human review on low-confidence model output.
  This is a gap the chapter does not currently address at all, not an
  extension of existing text.

- **Chapter 04 (Context Engineering)**: the existing "sub-agents as context
  firewalls" framing (`guide/04-context-engineering.md`, ~lines 989-1012)
  could cite this source's Go compliance validator as a concrete example
  where the entire remote agent's runtime and internal logic never enter
  the calling agent's context — only the extracted fields and the pass/fail
  verdict cross via `ToolContext.state` (Claim 6) — extending the existing
  "context firewall" framing (currently illustrated with same-process
  Claude Code sub-agents) to a cross-language, cross-process A2A boundary.

## Extraction Notes

- Read the full post via two extraction methods: (1) the WebFetch tool's
  small-model summarizer, used first for an overview pass and for locating
  candidate quotes, and (2) a direct `curl` fetch of the raw HTML
  (converted to plain text with a Python HTML-stripping script), used to
  independently verify every `Quote` field above character-for-character
  and to confirm the GitHub repository URLs as literal `href` attributes in
  the raw markup. Every quote in this note was confirmed present verbatim
  in the raw-fetched text before being used, following the same
  discard-if-unverified approach documented in
  `blog-google-adk-kotlin-android-agents.md`'s Extraction Notes.
- Did not follow the linked GitHub repository
  (`GoogleCloudPlatform/generative-ai/.../contract-compliance-pipeline`)
  beyond confirming the URL resolves as a real link in the page markup —
  did not clone or read the actual `card.go` / `agent.py` implementation
  files. A deeper extraction of the repository's actual code (as opposed to
  the blog post's code excerpts) is a candidate for a future, separate
  mining pass if the repository itself becomes independently notable.
- Author job titles ("Senior AI Product Manager" for Shubham Saboo,
  "Developer Relations Engineer" for Eric Dong) were reported by the
  WebFetch summarizer but could not be independently confirmed in the raw
  HTML fetch (the byline markup exposed only author names and search-link
  URLs, not role text, likely because titles are rendered by client-side
  JavaScript not present in the static HTML). These titles are therefore
  omitted from the frontmatter/Source Context above rather than stated as
  verified fact.
- Confidence graded `emerging` overall: the code-level artifacts (Claims 4,
  5, 6, 7, 9, and the Concrete Artifacts section) are `settled` — direct,
  falsifiable enumerations and code fragments from a shipped, linked
  open-source demo. The decomposition rationale (Claims 1-3) and the
  operations-cockpit description (Claim 11) are vendor framing/feature
  description without independent benchmarking or third-party usability
  testing in this post, which pulls the overall grade down from `settled`
  to `emerging` — consistent with how the two related Google-first-party
  notes in the corpus (`blog-google-a2a-collaborative-agents.md`,
  `blog-google-adk-kotlin-android-agents.md`) were graded.
- No contradiction issue filed per MINER.md §4a: this source describes a
  new worked example and extends existing taxonomy/pattern coverage rather
  than disputing any claim already in the corpus.
