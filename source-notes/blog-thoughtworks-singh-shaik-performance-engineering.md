---
source_url: https://www.thoughtworks.com/insights/articles/Performance-engineering-in-agentic-AI-systems
source_type: blog-post
title: "Performance engineering in agentic AI systems"
author: Divye Singh and Limansha Safreen Shaik (Thoughtworks)
date_published: 2026-07-06
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1924"
---

# Performance Engineering in Agentic AI Systems

> A Thoughtworks practitioner article proposing nine concrete optimization
> techniques for moving orchestrated multi-agent systems from functional
> prototype to production-grade infrastructure — model right-sizing,
> key-value vs. semantic caching, fan-out/fan-in parallelization with
> hot/cold path splitting, replacing LLM calls with deterministic code where
> a schema is known, dynamic context-slot selection, KV-cache-aware prompt
> ordering, and semantic-similarity classification as an alternative to
> LLM-based routing — framed around a four-way "flexibility, determinism,
> latency, cost" design tension.

## Source Context

- **Type**: blog-post (Thoughtworks Insights "articles" vertical, published
  July 6, 2026, modified July 13, 2026 per the page's `dateModified` metadata;
  roughly 2,300-word technical/prescriptive piece with two data tables, no
  code blocks, and no cited external sources, case studies, or metrics from a
  named client engagement).
- **Author credibility**: Two named authors, both Thoughtworks employees.
  Divye Singh's Thoughtworks profile lists his job title as "Developer" and
  describes him as "an AI researcher who has been working predominantly in
  the collaborative robotics and life sciences domain within Thoughtworks
  Engineering for Research (e4r) team," with stated interests in
  "Artificial Intelligence, Reinforcement Learning, Modeling and Simulation
  and Optimization." Limansha Safreen Shaik's Thoughtworks profile describes
  her as "a Senior Consultant at Thoughtworks specializing in Generative AI,
  agentic AI, RAG solutions, cloud-native platforms and backend engineering."
  Neither profile nor the article itself cites a specific named client
  engagement, a benchmark suite, or measured before/after numbers for any of
  the nine techniques — this is a synthesis of engineering practice and
  reasoning about trade-offs, not a reported case study with outcome data.
  The "12 seconds → 3 seconds" parallelization example and the "cosine
  similarity > 0.85" threshold are illustrative worked examples, not
  measurements from a production system.
- **Scope**: Covers, in order: why naive multi-agent designs fail at scale
  (latency accumulation, token cost growth, reliability degradation, routing
  hallucinations); a measurement-first diagnostic principle; model
  right-sizing by task complexity (with a four-row complexity/tier/rationale
  table); prompt/API response caching (key-value vs. semantic, and what
  should vs. should not be cached); async parallelization via fan-out/fan-in
  (with a worked 6-step analytics-query example, three preconditions for safe
  parallelization, and a hot-path/cold-path split); replacing LLM calls with
  deterministic code across four named patterns (query modification, query
  reuse, tool-response transformation, schema-driven sample generation) under
  a structured-outputs discipline; context engineering as dynamic
  slot-filling rather than static inclusion; prompt ordering for KV-cache
  utilization (with an explicit combined rule tying it to context
  engineering); semantic similarity (KNN) vs. LLM classification (with a
  five-row comparison table and a practical confidence threshold); and a
  closing "durable design tension" framing (flexibility, determinism,
  latency, cost) that argues teams must treat agent graphs as distributed
  systems. Does NOT cover: specific vendor/tool names for any of the
  described techniques (no embedding model, vector database, or LLM gateway
  product is named); cost or latency benchmarks for any technique; a worked
  code example or config snippet for any pattern; or how these techniques
  interact with agent evaluation/testing (the article does not mention evals,
  personas, or test suites at all).

## Extracted Claims

### Claim 1: Naive multi-agent designs fail at enterprise scale in four specific, predictable ways — accumulating latency, token costs that grow with traffic rather than value, reliability degradation from unstructured outputs, and costly routing hallucinations
- **Evidence**: Opening framing paragraph of the article, presented as the
  motivating problem statement before any technique is introduced.
- **Confidence**: emerging (a structural diagnosis stated with conviction but
  without a named case, incident, or measured frequency for any of the four
  failure modes)
- **Quote**: "Naive designs scale poorly in predictable ways. Latency
  accumulates when independent steps run sequentially. Token costs grow with
  traffic instead of value. Reliability degrades when unstructured outputs
  break downstream parsers. And routing hallucinations invoke the wrong
  specialist, which is often costlier than a wrong final answer."
- **Our assessment**: This is a clean four-part taxonomy of failure modes
  that the rest of the article's nine techniques map onto one-to-one
  (parallelization → latency; caching/right-sizing → token cost; structured
  outputs → reliability; semantic-similarity classification → routing). It
  corroborates `blog-thoughtworks-kamelman-token-crisis.md` Claim 8's four
  named engineering anti-patterns (premium models on non-premium tasks,
  unbounded agent retry loops, verbose prepended context, over-generous RAG
  retrieval) — both sources independently converge on "unstructured/naive
  design choices, not model capability, cause agentic-system cost and
  reliability failures at scale," though Kamelman's piece names the
  organizational root cause (unrevisited prototyping-phase defaults) while
  this article stays at the technical-pattern level.

### Claim 2: Teams should measure latency, token consumption, and failure rates at every node before optimizing, because the actual bottleneck is often an external dependency rather than the LLM call itself
- **Evidence**: Stated as the article's foundational diagnostic principle,
  positioned immediately after the opening problem statement and before any
  of the nine techniques.
- **Confidence**: emerging (a plausible, widely-echoed practitioner principle;
  no data on what fraction of teams skip this step or what it costs them when
  they do)
- **Quote**: "Before optimizing any workflow, measure it. Teams often spend
  weeks tuning prompts or introducing caching only to discover that the real
  bottleneck is a slow database call or an external API."
- **Our assessment**: This "measure before optimizing" principle is the
  article's load-bearing methodological claim — every subsequent technique
  (right-sizing, caching, parallelization) is presented as a targeted fix for
  a specific bottleneck class, which only makes sense if the bottleneck has
  first been identified. This is a genuinely new framing angle for the
  corpus: `blog-thoughtworks-anand-agent-evaluation-framework.md` addresses
  evaluation methodology and `docs-ghaw-cost-management.md` addresses cost
  monitoring commands, but neither states "measure the graph node-by-node
  before touching prompts or caching" as an explicit anti-premature-optimization
  discipline for agentic workflows specifically.

### Claim 3: The single most impactful performance change is to stop using the frontier/best model for every step, and instead map distinct model tiers (including temperature/token-limit variants of the same base model) to distinct task types, externalized from the codebase so assignments change without a code deploy
- **Evidence**: Presented as "the first and most impactful change" in the
  "Right-sizing models for agent workflows" section, with an explicit
  operational recommendation (externalize the mapping, fetch at inference
  time).
- **Confidence**: emerging (a strong practitioner recommendation, consistent
  with named platform-level tooling elsewhere in the corpus, but this article
  gives no measured cost/latency delta from adopting it)
- **Quote**: "The first and most impactful change is deceptively simple: stop
  using your best model for everything. An agentic workflow is a pipeline of
  small decisions and large syntheses. Treating every step as \"call the
  frontier model\" works in demos. At enterprise scale, it becomes an
  expensive and slow default."
- **Our assessment**: This directly corroborates `docs-ghaw-cost-management.md`
  Claim 6, which names `gpt-4.1-mini` and `claude-haiku-4-5` as the specific
  lighter-model options gh-aw workflows can select in frontmatter for
  "routine" tasks — that source gives the concrete, named-model version of
  the principle this article states abstractly. The "externalize the mapping
  so it can be fetched at inference time, no code change required" detail is
  new to the corpus: gh-aw's model selection is a frontmatter (design-time)
  decision, whereas this article proposes a runtime-configurable mapping
  layer, which is architecturally more flexible but also not demonstrated
  with any named implementation.

### Claim 4: A practical task-complexity-to-model-tier mapping assigns low-complexity tasks (intent routing, label classification, cache slot fill, context rephrase) to small/fast models, medium-complexity tasks (RAG-grounded Q&A, summarization, fixed-schema code generation) to mid-tier models, safety/policy classification to mid-tier models at temperature 0, and high-complexity tasks (multi-step planning, open-ended orchestration, ambiguous long-context dialogue) to large/frontier models
- **Evidence**: A four-row table titled by "Task complexity | Task examples |
  Model tier | Rationale" columns, presented immediately after Claim 3's
  general principle.
- **Confidence**: emerging (an internally consistent, plausible taxonomy;
  presented as general guidance, not derived from a measured accuracy/cost
  study across the four tiers)
- **Quote**: "Constrained, schema-like outputs. A larger model adds cost and
  latency with no accuracy gain." (rationale given for the Low-complexity row
  of the table)
- **Our assessment**: The explicit inclusion of "safety and policy
  classification" as its own row — requiring mid-tier model at temperature 0
  specifically for deterministic, consistent policy enforcement rather than
  for capability reasons — is the most operationally specific detail in this
  taxonomy and is new to the corpus; no existing source note ties a
  temperature setting to a compliance/consistency requirement this explicitly.
  This table is the concrete instantiation practitioners can copy directly
  into a routing config, which the abstract principle in Claim 3 lacks on
  its own.

### Claim 5: Not all workflow steps should be cached — guardrail checks and intent classification can be short-circuited entirely because they produce the same result for semantically identical queries, structured-query-generation steps can be cached with placeholders for dynamic slots (dates, user IDs), and steps like summarizing freshly fetched data must run every time
- **Evidence**: Stated under the "What should be cached?" subsection, with a
  concrete enterprise example (near-identical rephrasing of a revenue-by-region
  query) motivating the need for caching in the first place.
- **Confidence**: emerging (a clear, internally consistent policy for what to
  cache and what not to; no measured hit-rate or cost-savings figure given for
  any of the three categories)
- **Quote**: "Steps like guardrail checks and intent classification produce
  the same result for semantically identical queries and can be short-circuited
  entirely... The goal isn't to cache everything but to avoid re-running what
  does not need to change."
- **Our assessment**: This extends `blog-anthropic-prompt-caching-everything.md`'s
  caching guidance into a different layer of the stack: the Anthropic article
  covers prefix/KV caching of the LLM's own attention computation across
  turns of one conversation, while this article covers application-level
  caching of entire workflow-step *outputs* (e.g., an intent-classification
  result) across different users' semantically similar queries. The two are
  complementary, not overlapping — a production agentic system would want
  both the Anthropic article's prefix-caching discipline within a single
  agent's calls and this article's step-output caching across different
  requests.

### Claim 6: Key-value caching (exact/near-exact string match) and semantic caching (embedding-based similarity match) are two distinct caching strategies that solve different problems — key-value caching breaks on any rephrasing, while semantic caching converts what would be a full generation task into a cheaper selection task
- **Evidence**: Two consecutive named subsections ("Key-value caching" and
  "Semantic caching") describing each mechanism's operating principle.
- **Confidence**: settled (this is a well-established caching-architecture
  distinction in the broader LLM-application engineering literature, not a
  novel claim by these authors)
- **Quote**: "Key-value caching works on exact or near-exact matches, which is
  the same query string hitting the same cached response. This handles strict
  repetition well but breaks down the moment a user rephrases the question
  even slightly." ... "Semantic caching addresses this by operating on meaning
  rather than string matching... Instead of looking for an exact match,
  retrieve the top-k semantically similar responses and use a lightweight
  model to select the best candidate. This shifts what would have been a full
  generation task into a selection task, which is significantly cheaper and
  faster."
- **Our assessment**: This is a distinct concept from Anthropic's *prompt*
  key-value caching (attention-computation reuse across a conversation's
  prefix, covered in `blog-anthropic-prompt-caching-everything.md`). The
  article's use of the term "key-value caching" here refers to
  exact-string-match *response* caching (a cache keyed on the literal query
  string), which is a different mechanism than the KV-cache the article
  itself discusses later under "Prompt structure and KV cache utilization"
  (Claim 14 below) — the article uses "KV cache" in two senses across its
  own sections (application-level response cache vs. provider-side attention
  cache) without explicitly flagging the terminology overlap. The Assayer and
  guide authors should preserve this distinction carefully if citing both
  sections, since conflating them would misstate the mechanism.

### Claim 7: A fan-out/fan-in pattern — dispatching independent downstream steps concurrently once their shared prerequisite (query generation) completes, then merging results at a barrier — reduces user-visible latency from the sum of the branches to the maximum of them, illustrated by a worked example reducing four sequential three-second steps (12 seconds total) to roughly three seconds
- **Evidence**: A worked example: a 6-step analytics workflow (intent
  classification → query generation → data fetch → code generation →
  explanation generation → follow-up suggestions) where the four steps after
  query generation have no dependency on each other.
- **Confidence**: emerging (the "roughly three seconds instead of 12" figure
  is an illustrative arithmetic example built on an assumed "roughly three
  seconds" per-step latency, not a measured production benchmark)
- **Quote**: "The solution is a fan-out/fan-in pattern with query generation
  as the shared prerequisite. Once the query is ready, all four independent
  steps are dispatched concurrently and their results are merged at a barrier
  before the final response is assembled. User-visible latency shifts from
  the sum of the four branches to the maximum of them: roughly three seconds
  instead of 12 in this example."
- **Our assessment**: This is architecturally consistent with
  `docs-ghaw-orchestration-patterns.md`'s orchestrator/worker fan-out model
  (Claim 1: "one workflow (the orchestrator) needs to fan out work to one or
  more worker workflows"), though the two sources describe fan-out at
  different granularities — gh-aw's pattern dispatches entire *workflows* as
  workers (via `dispatch-workflow` or `call-workflow`), while this article
  describes fan-out at the level of *steps within a single agent's
  workflow graph* (data fetch, code generation, etc., as concurrent branches
  of one request). The underlying principle — identify the true dependency
  graph and stop serializing independent work — is the same at both
  granularities, giving the guide two complementary worked examples at
  different scales of the same architectural idea.

### Claim 8: Reliable parallelization of agent-graph branches requires three preconditions: removing artificial sequential dependencies between steps that don't actually need to wait on each other, defining explicit merge rules for concurrent writes to shared state (additive for lists, last-write-wins for scalars), and giving each branch its own failure handling so one branch's error doesn't collapse the whole response
- **Evidence**: Stated as "Three things need to be in place for this to work
  reliably," presented as a bulleted checklist immediately after the
  fan-out/fan-in worked example.
- **Confidence**: emerging (a coherent, actionable checklist; no data on how
  often teams skip one of the three and what specifically breaks as a result,
  beyond the general warning in Claim 10)
- **Quote**: "Concurrent branches writing to shared state need explicit merge
  rules (additive merges for lists, last-write-wins for scalars), otherwise
  race conditions surface silently under load."
- **Our assessment**: The "additive for lists, last-write-wins for scalars"
  merge-rule taxonomy is a specific, reusable piece of guidance not found
  elsewhere in the corpus — most parallelization discussion in the corpus
  (e.g., `docs-ghaw-orchestration-patterns.md`'s correlation-ID + Project
  board coordination convention) addresses cross-*workflow* coordination via
  an external artifact (a Project board field), not in-process merge
  semantics for concurrent branches writing to the same in-memory state
  object. This is a finer-grained concern the gh-aw orchestration note does
  not cover.

### Claim 9: Parallelization surfaces a useful hot-path/cold-path distinction — the hot path is the minimal step set required for the primary answer, while the cold path (enrichment steps like follow-up suggestions, logging, or cache pre-warming) can be dispatched asynchronously after the hot-path response, adding no user-visible latency
- **Evidence**: Described immediately after the three parallelization
  preconditions, applied to the same analytics-workflow example (hot path:
  query generation, data fetch, rendering; cold path: follow-up suggestions,
  logging, recommendation-model updates, cache pre-warming).
- **Confidence**: emerging (a clear architectural distinction with a
  plausible example; the claim that this split "often yields more latency
  reduction than parallelizing within the hot path alone" is asserted without
  a comparative measurement between the two strategies)
- **Quote**: "Parallelization also opens up a useful distinction between hot
  and cold paths... Cold path work can be dispatched asynchronously after the
  hot path response is returned, running in the background without
  contributing to user-visible latency."
- **Our assessment**: This hot/cold path terminology and framing is novel to
  the corpus — no existing source note names a "hot path" vs. "cold path"
  split for agentic workflow steps specifically (as distinct from general
  systems-engineering use of the terms). It is a genuinely reusable design
  vocabulary: "is this step on the user's critical path, or can it run after
  the response is already returned?" is a concrete question practitioners can
  ask of every step in an agent graph.

### Claim 10: Fan-out should not be used when steps have genuine sequential dependencies, when per-branch observability is not in place, or when partial-failure policies are undefined — without a partial-failure policy, a failing branch silently passes incomplete state through the merge barrier, producing a broken response with no clear cause
- **Evidence**: Stated under the "When not to use fan-out" subsection as an
  explicit negative-case warning.
- **Confidence**: emerging (a clear failure-mode warning; no incident or named
  example of this specific silent-failure pattern occurring in production is
  given)
- **Quote**: "Do not parallelize when steps have genuine sequential
  dependencies, when per-branch observability is not in place or when
  partial-failure policies are not defined. Without a partial-failure policy,
  a branch that fails will pass incomplete state through the barrier
  silently, producing a broken response with no clear cause."
- **Our assessment**: This is the article's most safety-relevant single
  claim and complements Claim 8's positive checklist with the negative case:
  Claim 8 says what must be in place; this claim says what happens if it
  isn't (silent incomplete-state propagation, not a loud failure). For a
  guide chapter on multi-agent orchestration, this "silent partial failure at
  the merge barrier" failure mode is the specific risk practitioners should
  test for before shipping fan-out patterns, distinct from the more commonly
  discussed risk of one branch simply erroring out loudly.

### Claim 11: Beyond removing unnecessary latency, reducing the number of LLM calls altogether is a further optimization opportunity — the principle is to use LLMs only for genuine language understanding or reasoning, and handle everything else (query modification, query reuse, tool-response field extraction, schema-driven sample generation) in code
- **Evidence**: Stated as the opening principle of the "Partial deterministic
  flows and structured outputs" section, followed by four named patterns
  (query modification, query reuse, tool-response transformation,
  schema-driven sample generation) each with a one-paragraph mechanism
  description.
- **Confidence**: emerging (a clear architectural principle with four
  concrete named patterns; no data on what fraction of a typical workflow's
  LLM calls are eliminable this way)
- **Quote**: "Even after removing unnecessary latency, another optimization
  opportunity remains: reducing the number of LLM calls altogether. Not
  everything in an agentic workflow needs an LLM... The principle is to use
  LLMs for the parts that genuinely require language understanding or
  reasoning, and handle everything else in code." For the query-modification
  pattern specifically: "most structured query languages expose a parser: the
  filter can be injected by parsing the output and appending the clause in
  code, which is guaranteed to be placed correctly every time."
- **Our assessment**: This directly corroborates and extends
  `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` deterministic
  checks as the highest-ROI gh-aw cost-reduction strategy — "every condition
  that can be evaluated without an LLM call should be expressed as a
  `skip-if-match` condition," per that note's own Guide Impact framing).
  gh-aw's `skip-if-match` operates at the level of "should this entire
  workflow run at all," while this article's four patterns operate one level
  deeper — "given that the workflow is running, which individual steps
  within it can be replaced with parsing/code rather than a fresh LLM call."
  The two sources describe the same underlying principle (deterministic code
  is cheaper and more reliable than an LLM call wherever the logic is
  actually deterministic) applied at two different granularities.

### Claim 12: Structured outputs validated against a schema before being passed downstream are what makes the LLM/deterministic-code split in Claim 11 safe — without schema validation the LLM/code boundary is fragile and hard to trace; with it, the boundary is an explicit, independently testable contract
- **Evidence**: Stated as the connective principle tying together the four
  deterministic-flow patterns, at the end of the "Partial deterministic flows
  and structured outputs" section.
- **Confidence**: settled (schema validation as a reliability practice for
  LLM/code boundaries is a well-established pattern in the broader LLM
  application engineering literature; the specific framing here is a clear
  restatement of that consensus, not a novel claim)
- **Quote**: "When LLM outputs are validated against a schema before being
  passed downstream, deterministic code can operate on them safely. Without
  schema validation, the boundary between LLM and code becomes fragile: a
  slightly malformed field or an unexpected key breaks the downstream step in
  ways that are hard to trace. With it, the contract between LLM and code is
  explicit, and the deterministic parts of the flow can be tested
  independently of the model."
- **Our assessment**: This corroborates `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 3, which names "deterministic agent" (e.g., intent identification,
  guardrail agent) vs. "non-deterministic agent" (e.g., summarization,
  rewriting) as a design axis requiring different evaluation approaches —
  that note addresses how to *evaluate* the split; this article addresses how
  to *engineer* the boundary safely (schema validation) so the split is
  trustworthy in the first place. Together they cover engineering and
  evaluation of the same deterministic/non-deterministic architecture
  decision.

### Claim 13: Context should be treated as a dynamic selection problem rather than a static inclusion problem — prompt templates should define named, optional slots (system, tools, retrieved context, history, user message) that a lightweight routing step populates only as needed per query, with empty slots omitted entirely rather than filled with placeholder text
- **Evidence**: Stated under "Context engineering: Send less, get better
  results," with three named compounding costs of over-inclusion (latency,
  direct cost, quality dilution) and a concrete implementation description
  (named template slots, a routing step to decide which to fill).
- **Confidence**: emerging (a clear, actionable architecture; no measured
  quality or cost delta given for adopting slot-based selection vs. static
  full-context inclusion)
- **Quote**: "There's a tempting default in agentic AI systems: when in doubt,
  include more context... A question about data analytics does not need the
  HR policy tool definitions. A greeting does not need the last ten
  conversation turns. A routine lookup does not need the full user profile."
  And, on implementation: "Define your prompt as a template with named
  sections: {{system}}, {{tools}}, {{retrieved_context}}, {{history}},
  {{user_message}}. At request time, populate only the sections the query
  actually needs. Empty slots are omitted entirely, not filled with
  placeholder text."
- **Our assessment**: This corroborates `blog-bswen-mcp-token-cost.md`
  Claim 3 ("If you have a 200k context window and burn 100k on tool
  definitions, you've already lost half your capacity") and Claim 6 (a
  measured breakdown showing conversation content was only 4% of a real
  session's token budget, with system prompts/tools/MCP definitions
  dominating). Bswen's post measures the cost of *not* doing dynamic slot
  selection (tool definitions loaded unconditionally consume the majority of
  the context budget); this article prescribes the *fix* (a routing layer
  that fills only the tool-definition slot the current query actually needs)
  as a general architectural pattern rather than the MCP-specific server-pruning
  workaround Bswen recommends. The two sources are strongly complementary:
  Bswen shows the problem is real and large in a measured session; this
  article proposes the general mechanism (typed, optional prompt slots) that
  would prevent it architecturally rather than requiring manual server
  pruning.

### Claim 14: Prompts should be ordered with everything stable (system instructions, tool definitions, fixed few-shot examples) at the top and everything dynamic (selected context, user message) at the bottom to maximize provider-side KV-cache hits, and this compounds with context engineering (Claim 13) because a shorter dynamic tail means the cached stable prefix covers a larger fraction of the total prompt — shuffling the order of any static block between requests forfeits the cache hit entirely
- **Evidence**: Stated under "Prompt structure and KV cache utilization,"
  with an explicit "Combined rule" subsection tying it back to context
  engineering, and a named caveat about provider opt-in requirements
  (Anthropic's `cache_control` breakpoint, OpenAI's prompt caching).
- **Confidence**: settled (the underlying mechanism — providers skip
  recomputing attention for an exactly-matching prefix — is well-established
  and independently corroborated elsewhere in the corpus; the specific
  "static top, dynamic bottom" ordering rule is standard practice, not a
  novel claim by these authors)
- **Quote**: "The rule is straightforward: everything stable goes at the top,
  everything dynamic goes at the bottom... The moment you shuffle the order
  of any static block between requests, the prefix no longer matches and you
  forfeit the cache hit entirely." And the combined rule: "First: select only
  what the query needs. Then: order the prompt as system → tools → fixed
  examples → selected context → user message. The static prefix gets cached.
  The dynamic tail stays small. Both savings stack."
- **Our assessment**: This is essentially the same rule as
  `blog-anthropic-prompt-caching-everything.md` Claim 3 ("static content
  first, dynamic content last" — "the best way to do this is static content
  first, dynamic content last") and Claim 2 (the four-layer cache hierarchy:
  static system prompt & tools → CLAUDE.md/project-level → session context →
  conversation messages), independently stated by a different vendor's
  practitioners for a general audience rather than for Claude Code
  specifically. The Anthropic article is the authoritative first-party
  account of *why* this rule exists and what breaks it in one specific
  product (timestamps in the static prompt, non-deterministic tool ordering,
  mid-session tool/model changes); this article states the same rule as
  general cross-provider guidance and adds the explicit "combined rule" link
  to context-slot selection (Claim 13) that the Anthropic piece does not
  make as a named connection. Two independent sources — one first-party
  product-engineering account, one general consultancy guidance piece —
  converge on the identical ordering principle, which strengthens confidence
  that "static first, dynamic last" is settled practice rather than a
  single-vendor idiosyncrasy.

### Claim 15: For stable label spaces, semantic similarity (KNN over embeddings) often outperforms LLM-based classification on both cost and latency, trading an upfront example-curation cost for a classifier that improves with use (via logging low-confidence LLM-fallback outcomes back into the example store) rather than degrading via prompt drift — a practical starting threshold is a cosine similarity score above 0.85 for high-confidence acceptance, with lower scores routed to an LLM fallback
- **Evidence**: A five-row comparison table (cost per call, latency, accuracy,
  debuggability, updating) plus a described operational loop: start with a
  manually curated seed set, route low-confidence cases to an LLM, log
  confirmed outcomes back into the example store.
- **Confidence**: emerging (the mechanism and comparison are architecturally
  sound and internally consistent; the 0.85 threshold is explicitly flagged
  by the authors themselves as domain- and embedding-model-dependent, not a
  universal constant)
- **Quote**: "Intent classification and routing are everywhere in agentic
  systems. For stable label spaces, semantic similarity often outperforms
  LLM-based classification on both cost and latency." ... "A practical
  threshold to start with is a cosine similarity score above 0.85 for a
  high-confidence accept, and below this for a hard LLM fallback. These
  numbers shift with your embedding model, label space and domain, but the
  structure holds. The classifier gets better with use rather than degrading
  as label drift accumulates in a static prompt."
- **Our assessment**: This is genuinely novel to the corpus — no existing
  source note documents a KNN-vs-LLM-classification trade-off table with a
  concrete confidence threshold, or the specific "route low-confidence to
  LLM, log outcomes back into the example store" self-improving-classifier
  loop. It connects to Claim 1's "routing hallucinations invoke the wrong
  specialist" failure mode as a proposed structural fix — routing/intent
  classification via semantic similarity is both cheaper (per the cost/latency
  columns) and more debuggable ("show nearest neighbours; fully explainable"
  vs. LLM classification's "hard to know why a label was chosen") than the
  LLM-classification approach the article opens by warning against.

### Claim 16: The durable design tension in agentic systems is four-way — flexibility, determinism, latency, and cost — and platforms optimizing one dimension while ignoring the others tend to require re-platforming under incident load; teams that sustain production load treat agent graphs as distributed systems (with barriers, backpressure, failure domains, and observability) rather than as "prompt demos with extra steps," because visibility and control, not autonomous novelty, is what makes agentic AI systems operable at enterprise scale
- **Evidence**: Stated as the article's closing synthesis, under "The durable
  design tension" heading.
- **Confidence**: emerging (a thesis-level synthesis claim tying together the
  preceding nine techniques; not independently tested against a named
  organization's "re-platforming under incident load" failure, though it is
  consistent with the corpus's broader operational-risk-management coverage)
- **Quote**: "The durable tension is four-way: flexibility, determinism,
  latency and cost. Platforms that optimize one dimension while ignoring
  others routinely re-platform under incident load. The teams that sustain
  production load treat agent graphs as distributed systems — with barriers,
  backpressure, failure domains and observability — rather than as prompt
  demos with extra steps. Visibility and control, not autonomous novelty, is
  what makes agentic AI systems operable at enterprise scale."
- **Our assessment**: The explicit "agent graphs as distributed systems"
  framing is a strong, quotable synthesis device connecting this article's
  nine tactical techniques to the operational-risk-management themes already
  present across the corpus (circuit breakers, rate limiting, monitoring).
  It is consistent with — though phrased independently of —
  `blog-thoughtworks-kamelman-token-crisis.md` Claim 13's "you have to move
  the decisions that generate the cost upstream, to where they can actually
  be governed": both articles argue that ad hoc, prototype-era design
  decisions become structural liabilities at production scale, and both
  recommend treating agentic systems with the same architectural discipline
  as any other distributed system, rather than as an extension of prompt
  engineering.

## Concrete Artifacts

### Task-complexity-to-model-tier mapping table (verbatim from source)
```
Source: "Performance engineering in agentic AI systems," Singh & Shaik,
Thoughtworks, 2026-07-06 — "Right-sizing models for agent workflows" section

Task complexity | Task examples | Model tier | Rationale
----------------|----------------|------------|----------
Low | Intent routing, label classification, cache slot fill, context
      rephrase | Small / Fast | Constrained, schema-like outputs. A larger
      model adds cost and latency with no accuracy gain.
Medium | RAG-grounded Q&A, summarization, code generation with fixed
         schemas | Mid-tier | Grounding reduces hallucination risk. Capable
         enough for nuanced output without frontier pricing.
Medium, strict | Safety and policy classification | Mid-tier, temp 0 |
                 Consistent, deterministic enforcement. Temperature 0
                 removes variance from policy decisions.
High | Multi-step planning, open-ended orchestration, ambiguous
       long-context dialogue | Large / Frontier | Tasks require reasoning
       over long context, tool selection and handling genuine ambiguity.
       A smaller model here hurts reliability visibly.
```

### Worked fan-out/fan-in example (verbatim, from "Async parallelization in agent graphs")
```
Source: "Performance engineering in agentic AI systems," Singh & Shaik,
Thoughtworks, 2026-07-06

Analytics request flow:
  Intent classification -> Query generation -> Data fetch -> Code
  generation -> Explanation generation -> Follow-up suggestions

"In this example flow, the four steps after query generation (data fetch,
code generation, explanation and follow-up suggestions) have no dependency
on each other. They only depend on the query generated in the step before
them. Yet the naive implementation runs them sequentially. If each step
takes roughly three seconds, those four steps alone accumulate to about 12
seconds of wall-clock time, even though the true dependency graph would
allow all four to run simultaneously."

Fix: fan-out/fan-in with query generation as the shared prerequisite;
merge results at a barrier. Result: ~3 seconds (max of branches) instead
of ~12 seconds (sum of branches).

Three preconditions stated for safe parallelization:
  1. Remove artificial dependencies between steps.
  2. Concurrent branches writing to shared state need explicit merge
     rules (additive merges for lists, last-write-wins for scalars).
  3. Each branch needs its own failure handling.
```

### Semantic similarity vs. LLM classification comparison table (verbatim)
```
Source: "Performance engineering in agentic AI systems," Singh & Shaik,
Thoughtworks, 2026-07-06 — "Semantic similarity vs. LLM classification" section

                | LLM classification              | Semantic similarity (KNN)
----------------|----------------------------------|---------------------------
Cost per call   | Input tokens: system prompt +    | Embedding call only
                | examples + query                 | (fraction of cost)
Latency         | Full LLM inference time          | Embedding + vector search
                |                                   | (sub-10ms typical)
Accuracy        | Prompt-dependent; not guaranteed  | Example-dependent;
                |                                   | improves continuously
Debuggability   | Hard to know why a label was      | Show nearest neighbours;
                | chosen                            | fully explainable
Updating        | Rewrite prompt, redeploy          | Add labelled examples to
                |                                   | the store; no redeploy

Practical threshold: cosine similarity > 0.85 for high-confidence accept;
below that, hard LLM fallback. "These numbers shift with your embedding
model, label space and domain, but the structure holds."
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 8 (enterprise token
    waste follows an engineering pattern: premium models on non-premium
    tasks, unbounded agent retry loops, verbose prepended context, generous
    RAG retrieval): this article's Claim 1 (naive designs fail via latency
    accumulation, token cost growth, reliability degradation, and routing
    hallucinations) is a structurally similar four-part failure taxonomy from
    a different author at the same publisher, and Claim 3/4 (model
    right-sizing by task complexity) is a direct technical fix for Kamelman's
    "premium reasoning models for tasks that don't require premium reasoning"
    anti-pattern.
  - `docs-ghaw-cost-management.md` Claim 6 (naming `gpt-4.1-mini` and
    `claude-haiku-4-5` as gh-aw's concrete cheaper-model options for routine
    workflows): this article's Claim 3 states the same "stop using your best
    model for everything" principle in the abstract; the gh-aw reference
    supplies the concrete, named-model instantiation this article's own
    table (Claim 4) leaves at the tier-name level ("Small / Fast," "Mid-tier,"
    "Large / Frontier") without naming specific models.
  - `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` deterministic
    checks as the highest-ROI gh-aw cost-reduction strategy, eliminating
    inference cost entirely for qualifying runs): this article's Claim 11
    (replace LLM calls with parsing/code wherever the logic is genuinely
    deterministic) states the same principle at a finer grain — within a
    running workflow, per individual step — where gh-aw's mechanism operates
    at the level of whether the whole workflow runs at all.
  - `blog-anthropic-prompt-caching-everything.md` Claim 3 ("static content
    first, dynamic content last" as the foundational rule for prompt
    structure under prefix caching) and Claim 2 (the four-layer cache
    hierarchy by mutability): this article's Claim 14 ("everything stable
    goes at the top, everything dynamic goes at the bottom") states the
    identical ordering rule, independently, for a general cross-provider
    audience rather than for Claude Code specifically — two independent
    sources (first-party Anthropic engineering, general Thoughtworks
    consultancy guidance) converging on the same rule strengthens confidence
    it is settled cross-provider practice.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 3
    (deterministic vs. non-deterministic components in the same pipeline
    require different evaluation approaches, with intent-identification/
    guardrail agents named as the deterministic examples): this article's
    Claim 12 (schema-validated structured outputs make the LLM/deterministic-code
    boundary an explicit, independently testable contract) addresses the
    engineering discipline that makes that same deterministic/non-deterministic
    split safe to build, while the Anand note addresses how to evaluate it —
    complementary halves of the same architectural decision.
  - `blog-bswen-mcp-token-cost.md` Claim 3 ("If you have a 200k context
    window and burn 100k on tool definitions, you've already lost half your
    capacity") and Claim 6 (measured breakdown showing conversation content
    was only 4% of a real session's token budget): this article's Claim 13
    (treat context as a dynamic selection problem; a question about data
    analytics does not need the HR policy tool definitions) prescribes the
    general architectural fix — typed, optional prompt slots filled only as
    needed — for exactly the problem Bswen measured in a real Claude Code
    session.

- **Contradicts**: None identified. No claim in this article materially
  opposes an existing source note's claim on the same topic in a way that
  would drive different guide advice. See Claim 6's "Our assessment" for a
  terminology overlap (this article uses "key-value caching" for two
  different mechanisms across its own sections — exact-match response
  caching vs. provider-side attention-computation caching) that is worth
  flagging to the Assayer and Smith as a clarity risk if both sections are
  cited in the same guide passage, but this is an internal terminology
  ambiguity within the single source, not a factual disagreement between two
  source notes, so no contradiction issue was filed per MINER.md §4a.

- **Extends**:
  - `docs-ghaw-orchestration-patterns.md` Claim 1 (orchestrator/worker
    fan-out as the canonical gh-aw multi-agent architecture) and Claim 4
    (the `dispatch-workflow`/`call-workflow` decision rule): this article's
    fan-out/fan-in pattern (Claim 7) and its three parallelization
    preconditions (Claim 8) describe the same "identify the true dependency
    graph, stop serializing independent work" principle at a finer
    granularity — within a single agent's step graph, rather than across
    dispatched worker *workflows*. The gh-aw note's correlation-ID + Project
    board coordination convention addresses cross-workflow state sharing;
    this article's "additive for lists, last-write-wins for scalars" merge
    rules address in-process concurrent-write semantics that the gh-aw note
    does not cover.
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 13 ("when the
    constraint is physical and compounding, you cannot optimize your way out
    of it at the billing layer — you have to move the decisions that generate
    the cost upstream, to where they can actually be governed"): this
    article's closing "durable design tension" (Claim 16) makes a structurally
    similar argument at the technical-architecture level rather than the
    organizational-governance level — both conclude that ad hoc, prototype-era
    decisions must be replaced with deliberate, upstream architectural choices
    before a system can operate reliably at scale.

- **Novel** (not documented in any existing corpus source note):
  - **The four-row task-complexity-to-model-tier mapping table** (Claim 4),
    including the specific pairing of "safety and policy classification"
    with "mid-tier model at temperature 0" for deterministic-enforcement
    reasons rather than capability reasons.
  - **Hot-path/cold-path terminology for agentic workflow steps** (Claim 9):
    no existing source note names this specific split for agent-graph design.
  - **The "additive for lists, last-write-wins for scalars" merge-rule
    taxonomy** for concurrent branches writing to shared state (Claim 8):
    a specific, reusable piece of in-process concurrency guidance not found
    elsewhere in the corpus.
  - **The silent-partial-failure-at-the-merge-barrier risk** (Claim 10): the
    specific warning that an unhandled branch failure passes incomplete state
    through a fan-in barrier silently, rather than failing loudly, is a novel
    named failure mode for the corpus.
  - **Semantic similarity (KNN) vs. LLM classification comparison table with
    a concrete cosine-similarity confidence threshold (>0.85) and a
    self-improving classifier loop (route low-confidence to LLM, log
    confirmed outcomes back to the example store)** (Claim 15): entirely new
    to the corpus.
  - **The four named deterministic-flow-replacement patterns** (Claim 11):
    query modification via parser injection, query reuse via programmatic
    query mutation, tool-response field extraction to avoid large payloads in
    context, and schema-driven sample generation — no existing source note
    names this specific set of four patterns for reducing LLM call count.

## Guide Impact

- **Chapter 02 (Harness Engineering — cost and latency management)**: Add
  the four-row task-complexity-to-model-tier table (Claim 4) as a concrete,
  copyable routing template, cross-referenced against `docs-ghaw-cost-management.md`
  Claim 6's named-model instantiation (`gpt-4.1-mini`, `claude-haiku-4-5`) so
  practitioners see both the abstract tier structure and a concrete model
  pairing. Add the "measure before optimizing" principle (Claim 2) as the
  opening discipline for any cost/latency optimization section — before
  recommending caching or model right-sizing, tell practitioners to instrument
  every node first.

- **Chapter 02 / Chapter 04 (Harness Engineering / Context Engineering —
  caching)**: Add the key-value-vs-semantic response-caching distinction
  (Claim 6) as a new "application-level caching" subsection distinct from
  the existing prefix/attention-caching coverage sourced from
  `blog-anthropic-prompt-caching-everything.md`. Explicitly flag for guide
  authors that this article uses the term "key-value caching" for exact-match
  *response* caching, which is a different mechanism from the provider-side
  *prefix* KV-cache the same article discusses later (and which
  `blog-anthropic-prompt-caching-everything.md` covers in depth) — use
  distinct terminology in the guide text to avoid reader confusion between
  the two.

- **Chapter 04 (Multi-Agent Orchestration Patterns)**: Add the fan-out/fan-in
  worked example (Claim 7), the three parallelization preconditions (Claim 8),
  the hot-path/cold-path split (Claim 9), and the "when not to use fan-out"
  warning (Claim 10) as a complete parallelization design checklist,
  cross-referenced against `docs-ghaw-orchestration-patterns.md`'s
  workflow-level fan-out mechanisms as the "same principle, different
  granularity" companion pattern.

- **Chapter 04 (Context Engineering)**: Add the dynamic-slot-selection
  pattern (Claim 13) — named template slots, populate only what's needed,
  omit empty slots rather than placeholder-filling them — as the prescribed
  architecture, paired with `blog-bswen-mcp-token-cost.md`'s measured evidence
  that unmanaged context (particularly MCP tool definitions) can consume the
  majority of a session's token budget. Add the KV-cache prompt-ordering rule
  (Claim 14) immediately after, with the article's own "combined rule" (select
  only what's needed, then order system → tools → fixed examples → selected
  context → user message) as the synthesis of both techniques.

- **Chapter 04 / Chapter 06 (Context Engineering / Observability — routing
  and classification)**: Add the semantic-similarity-vs-LLM-classification
  table and the >0.85 cosine-similarity threshold (Claim 15) as a named
  alternative to LLM-based intent routing, directly addressing Claim 1's
  "routing hallucinations invoke the wrong specialist" failure mode with a
  concrete, cheaper, more debuggable mechanism.

- **Chapter 03 / Chapter 04 (Verification — deterministic vs. non-deterministic
  boundaries)**: Add the four deterministic-flow-replacement patterns (Claim 11)
  and the structured-outputs-as-contract framing (Claim 12) as engineering
  guidance for where and how to safely replace LLM calls with code, paired
  with `blog-thoughtworks-anand-agent-evaluation-framework.md`'s guidance on
  evaluating the same deterministic/non-deterministic split.

## Extraction Notes

1. **WebFetch returned a refusal/summary rather than verbatim text on the
   first attempt** — the tool responded with a copyright caveat and offered a
   summary instead of full text, and a follow-up "detailed section-by-section
   breakdown" prompt returned quotes that could not be verified as
   character-for-character without independent confirmation. Per MINER.md
   §2a, **no quote in this note is taken from the WebFetch output**. Instead,
   the live article HTML was fetched directly via `curl` with a browser
   user-agent, and the relevant `<div class="text-container">` content block
   (located by searching for known phrases from the WebFetch summary, e.g.
   "Enterprise AI has evolved") was extracted and converted to plain text
   locally (Python: strip `<script>`/`<style>`, convert block-level tags to
   newlines, HTML-unescape entities, collapse whitespace). Every quote in
   this note was copied from that locally-parsed, directly-fetched text.
   Two apostrophe/quote-character inconsistencies were verified directly
   against the raw HTML bytes before quoting: "isn't" (Claim 5) uses a
   straight apostrophe (encoded as `&#39;` in the source), while "There's"
   (Claim 13) and "it's active" (in the KV-cache section, not directly quoted
   in a Claim above) use a curly right single quotation mark (U+2019) — the
   source itself is inconsistent in which character it uses, and this note
   preserves each occurrence's actual character rather than normalizing them.
2. **Author bylines and dates were confirmed via the page's embedded
   `application/ld+json` structured-data block** (author names, `datePublished:
   2026-07-06`, `dateModified: 2026-07-13`), not from visible on-page text —
   the rendered page does not show a visible byline in the fetched HTML.
   Author job titles and bios were independently confirmed by fetching each
   author's Thoughtworks profile page directly and reading the embedded
   `jobTitle`/`description` (Divye Singh) and meta-description (Limansha
   Safreen Shaik) fields.
3. **The article has no sub-pages or deep links to follow** per MINER.md §1 —
   it is a single, self-contained page with no inline citations, footnotes,
   or hyperlinks to external sources within the body text (the only outbound
   links found were three unrelated "More Insights" related-article teasers
   at the bottom of the page, which do not bear on this article's claims and
   were not followed).
4. **No code blocks, terminal transcripts, or config snippets appear in the
   source** — the two data tables (task-complexity/model-tier mapping;
   semantic-similarity/LLM-classification comparison) are the only structured
   artifacts, both reproduced verbatim in Concrete Artifacts above. There is
   no CLAUDE.md content, YAML, or CLI output to extract, unlike several
   gh-aw and Anthropic first-party sources already in the corpus.
5. **No contradictions filed**: cross-referenced against the four notes named
   by the Prospector's triage comments (`blog-thoughtworks-kamelman-token-crisis.md`,
   `blog-thoughtworks-omahony-feature-token-budgets.md`,
   `blog-cursor-faire-cloud-agents.md`,
   `blog-thoughtworks-anand-agent-evaluation-framework.md`) plus several
   additional notes located via corpus search on caching, model-routing, and
   orchestration terms (`blog-anthropic-prompt-caching-everything.md`,
   `docs-ghaw-orchestration-patterns.md`, `docs-ghaw-cost-management.md`,
   `blog-bswen-mcp-token-cost.md`). No claim in this article materially
   opposes any claim in those notes in a way that would drive different
   guide advice; all relationships found are corroboration or extension. The
   one internal ambiguity noted (the article's own dual use of "key-value
   caching" for two different mechanisms — see Claim 6 and Cross-References
   → Contradicts) is a within-source terminology risk, not a cross-source
   contradiction, so no contradiction issue was filed per MINER.md §4a.
6. **Three separate Prospector triage comments exist on issue #1924**, each
   proposing a slightly different set of "relevant chapters" (Ch02/03/04 in
   varying combinations, plus one mentioning Ch05 and Ch08). This note's
   Guide Impact section addresses the union of all three framings rather than
   picking one — cost/latency management (Ch02), verification/deterministic
   boundaries (Ch03), context engineering and orchestration (Ch04), and
   observability/routing (Ch06) are all touched by at least one extracted
   claim.
