---
source_url: https://cursor.com/blog/continually-improving-agent-harness
source_type: blog-post
title: "Continually improving our agent harness"
author: "Stefan Heule & Jediah Katz (Cursor / Anysphere)"
date_published: 2026-04-30
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#479"
---

# Continually improving our agent harness (Stefan Heule & Jediah Katz, Cursor)

> Cursor's first-party operational account of how they continuously improve a production
> agent harness: introducing the Keep Rate metric and LLM-as-judge satisfaction signal as
> novel online eval approaches, a five-category tool-call error taxonomy with per-tool
> per-model anomaly detection, model-specific tool format provisioning, and the ongoing
> evolution from heavy static context toward fully dynamic context retrieval.

## Source Context

- **Type**: blog-post (Cursor / Anysphere engineering blog, published April 30, 2026;
  two named engineers — Stefan Heule and Jediah Katz — writing about production systems
  they operate)
- **Author credibility**: First-party account from Cursor engineers describing their own
  production harness. Cursor has tens of thousands of active developer users and processes
  real-world agent sessions at scale, giving their operational observations substantial
  weight. This is vendor blog content (commercial incentive to present favorably), but
  the specificity of the error taxonomy, the named measurement approaches, and the candid
  discussion of failure modes (context anxiety, cache miss at model switch) are consistent
  with genuine engineering documentation. Treat as emerging: directionally reliable for
  the named patterns, but not independently audited.
- **Scope**: Covers six areas of harness operation — context window evolution, measuring
  harness changes via A/B testing, tracking and repairing degradations, model-specific
  customization, mid-chat model switching, and a forward-looking section on multi-agent
  systems. Does NOT cover training methodology, model architecture, or deployment
  infrastructure (those are in `blog-cursor-composer2-technical-report.md`). Does NOT
  describe implementation code for any of the patterns.

## Extracted Claims

### Claim 1: Keep Rate — fraction of agent-generated code changes remaining in the codebase after fixed time intervals — serves as an online proxy for agent quality

- **Evidence**: First-party description of a metric Cursor tracks in production. The
  metric measures whether users retain the code the agent wrote, using actual developer
  acceptance behavior as the quality signal rather than a correctness oracle.
- **Confidence**: emerging (described as a production metric; no published numbers or
  comparison against alternative eval approaches)
- **Quote**: "For a given set of code changes that the agent proposed, we track what
  fraction of those remain in the user's codebase after fixed intervals of time."
- **Our assessment**: Keep Rate is a behavioral proxy that requires no annotation and
  no ground-truth oracle: if developers keep the code, it was probably good. It is
  corroborated by the online-offline eval philosophy in `blog-cursor-cursorbench.md`
  (Claim 8), which describes online signals as necessary to catch regressions that
  offline graders miss. Keep Rate is the concrete instantiation of the "online signal"
  concept that CursorBench describes abstractly. The limitation: Keep Rate has a
  temporal lag (you need to wait to see if code persists) and can be confounded by
  developers leaving code in place for reasons unrelated to quality.

### Claim 2: LLM-as-judge reads user follow-up responses to detect satisfaction — "user moving on to next feature" as positive signal, "user pasting a stack trace" as negative

- **Evidence**: First-party description of a production signal. The LLM classifies
  user-session continuation behavior semantically to produce a satisfaction score.
- **Confidence**: emerging (described as operational; no published accuracy or
  correlation numbers)
- **Quote**: "we use a language model to read the user's responses to the agent's
  initial output in order to capture semantically whether the user was satisfied or not."
- **Our assessment**: This is a complement to Keep Rate. Keep Rate requires waiting;
  LLM-as-judge can surface a signal within the same session. The user behavior signals
  used — moving on to the next feature (positive) vs. pasting a stack trace (negative)
  — are clever because they require no annotation: the user's own behavior encodes
  quality judgment. The limitation: the LLM judge introduces its own error; the
  classification accuracy of "user pasting stack trace = agent failed" is not always
  correct (the user may be exploring, not debugging an agent error). As the post notes:
  "A user moving on to the next feature is a strong signal the agent did its job, while
  a user pasting a stack trace is a reliable signal that it didn't."

### Claim 3: "Context rot" — errors left in the agent's context window degrade the quality of subsequent model decisions and waste tokens

- **Evidence**: Named failure mode with a concrete mechanism: errors accumulate in
  context, the model reasons over that corrupted state, and downstream decisions
  degrade.
- **Confidence**: emerging (mechanism is stated; no quantitative measure of the
  degradation published)
- **Quote**: "errors remain in context, wasting tokens and causing 'context rot,'
  where accumulated mistakes degrade the quality of the model's subsequent decisions."
- **Our assessment**: Context rot is distinct from compaction-induced information loss
  (which is about forgetting). Context rot is about the *wrong information* persisting:
  failed tool calls, incorrect outputs, and error messages that accumulate and pollute
  the model's working memory. This is why Cursor treats "unknown errors" (see Claim 5)
  as harness bugs — they introduce context rot that cascades. Practitioners should
  design harnesses that actively clear error artifacts from context or treat unknown
  errors as bugs requiring immediate remediation.

### Claim 4: Tool-call errors fall into five categories: InvalidArguments, UnexpectedEnvironment, ProviderError, UserAborted, Timeout

- **Evidence**: Explicit taxonomy named in the source. The categories distinguish
  model-caused errors (InvalidArguments), environment-caused errors
  (UnexpectedEnvironment), provider-caused errors (ProviderError), and user/time
  interruptions (UserAborted, Timeout).
- **Confidence**: emerging (first-party taxonomy; no published category frequencies
  or relative importance)
- **Quote**: (no single direct quote names all five; the taxonomy is listed in the
  source as `InvalidArguments`, `UnexpectedEnvironment`, `ProviderError`,
  `UserAborted`, `Timeout`)
- **Our assessment**: This five-category taxonomy is the most actionable concrete
  artifact in the post for harness engineers. The categories have different causes and
  call for different responses: InvalidArguments points to a model reasoning failure;
  UnexpectedEnvironment points to environment brittleness; ProviderError is external
  and may require retry logic; UserAborted and Timeout are interruptions, not failures.
  Without a taxonomy, all failures look the same and trigger the same response. With
  it, you can instrument each category separately and alert on different thresholds.

### Claim 5: Any tool-call error not in the expected taxonomy is treated as a harness bug; expected errors are monitored with per-tool per-model anomaly detection

- **Evidence**: Explicit statement of the error classification philosophy. Unknown
  errors are treated as bugs specifically because they introduce context rot.
- **Confidence**: emerging (operational philosophy described; implementation details
  not published)
- **Quote**: "Any unknown error represents a bug in the harness, and we treat it
  accordingly. But many errors are 'expected,' for example the model occasionally
  proposing an incorrect edit or trying to read a file that doesn't exist."
- **Our assessment**: The "unknown error = harness bug" framing is disciplined
  engineering: it forces the team to explicitly classify every error mode, and any
  error that doesn't fit a known category triggers a bug investigation rather than
  being silently absorbed. This is the error-as-signal philosophy applied to agent
  harnesses. The practical implication: maintaining an explicit error taxonomy and
  treating unclassified errors as bugs is the mechanism that drives the harness toward
  higher reliability over time.

### Claim 6: Anomaly detection alerts fire when expected error rates significantly exceed per-tool per-model baselines — because different models fail at tool calls at different baseline rates

- **Evidence**: First-party description of a production monitoring system. The per-tool
  per-model baseline calibration is described as necessary because model baselines differ.
- **Confidence**: emerging (described as operational; thresholds and alert volumes not
  published)
- **Quote**: "We compute baselines per-tool and per-model, because different models may
  mess up tool calls at different rates." And: "we have anomaly detection alerts which
  fire when expected errors significantly exceed the baseline."
- **Our assessment**: The per-model-per-tool baseline design is important: a single
  global alert threshold would produce false positives (model A uses tool X poorly by
  nature) or miss real regressions (model B's poor use of tool Y is a bug, not the
  baseline). This is the same principle as establishing per-service SLOs rather than a
  global SLO. For practitioners: when building harness monitoring, calibrate error
  thresholds per model per tool rather than using a single global threshold.

### Claim 7: Cursor drove tool-call reliability to "at least 2 or often 3 9s" through focused improvement sprints

- **Evidence**: Specific reliability target stated as an achieved outcome of their
  degradation-tracking and repair process.
- **Confidence**: emerging (first-party claim; no external audit; specific number is
  notable)
- **Quote**: "We drove all tool calls to at least 2 or often 3 9s of reliability."
- **Our assessment**: 99–99.9% reliability per tool call is the production bar Cursor
  describes. In a multi-tool agent session with 20+ tool calls, even 99% reliability
  per call means ~18% of sessions hit at least one error. At 99.9%, that drops to
  ~2%. The gap between 2 9s and 3 9s matters at scale. The "focused sprints" framing
  suggests reliability is not a passive side-effect of good code — it requires active
  investment and measurement.

### Claim 8: Model-specific tool format provisioning — OpenAI models receive patch-based file editing tools; Anthropic models receive string-replacement tools — reduces reasoning cost and error rate

- **Evidence**: Direct description of a production harness customization. The rationale
  is explicit: each model was trained on a different tool format, and giving it the
  unfamiliar format costs extra reasoning tokens.
- **Confidence**: emerging (operational practice described with a stated rationale; no
  published delta in error rates between native and non-native formats)
- **Quote**: "OpenAI's models are trained to edit files using a patch-based format,
  while Anthropic's models are trained on string replacement." And: "Either model could
  use either tool, but giving it the unfamiliar one costs extra reasoning tokens and
  produces more mistakes. So in our harness, we provision each model with the tool
  format it had during training."
- **Our assessment**: This is the clearest statement in the corpus of the "give each
  model its native tool format" principle. It is transferable beyond file editing: any
  tool that admits multiple equivalent interface designs should be offered to each model
  in the format it was trained on. The reasoning-cost overhead from using an unfamiliar
  format is real but typically unobserved by teams that use a single-format harness.
  For teams working with multiple models: explicitly check what tool formats each model
  was trained with and provision accordingly.

### Claim 9: One model developed "context anxiety" — refusing work as its context window filled — mitigated via prompt adjustments in the harness

- **Evidence**: First-party observation of a model-specific behavioral quirk that
  required harness-level intervention. The model is not named. The mitigation was a
  prompt adjustment rather than a model fix.
- **Confidence**: anecdotal (one named behavior on an unnamed model; no published
  reproduction details)
- **Quote**: "As its context window filled up, it would start refusing work, hedging
  that the task seemed too big."
- **Our assessment**: This corroborates `blog-anthropic-harness-long-running.md`
  Claim 7, which documents the same failure mode ("context anxiety") on Opus 4.5 and
  required sprint decomposition as the architectural mitigation. The Cursor case uses
  a simpler fix (prompt adjustment rather than architectural change), suggesting the
  severity of context anxiety is model-specific: mild forms may be addressable with
  prompts; severe forms require architecture changes. The key harness design implication:
  monitor for context anxiety explicitly and have prompt-level and architecture-level
  mitigations ready.

### Claim 10: Mid-chat model switching invalidates provider-specific KV caches, causing a slower and more expensive first turn; Cursor mitigates by summarizing the conversation at switch time

- **Evidence**: First-party description of a design challenge and its mitigation.
  The cache-miss mechanism (provider-specific caches) and the summarization approach
  are both described.
- **Confidence**: emerging (mechanism described; tradeoff between summarization
  quality loss and cache miss cost acknowledged without published quantification)
- **Quote**: "Switching means a cache miss and a slower, more expensive first turn."
  And: "We have experimented with mitigating this by summarizing the conversation at
  switch time, which provides the model with a clean summary that reduces the cache
  penalty."
- **Our assessment**: The mid-chat switching design space has a fundamental tradeoff:
  summarization reduces the cache penalty but loses detail, particularly on complex
  tasks where the full context history is important. This extends
  `blog-cursor-composer-self-summarization.md` Claim 2 (self-summarization as a
  compaction technique) with a new application domain: switching context rather than
  compacting context. The underlying tension is the same: any form of lossy compression
  risks losing critical information. For practitioners: if you support model switching,
  design the summarization quality before enabling the feature for complex tasks.

### Claim 11: Subagents with fresh context windows are the alternative to mid-chat model switching, avoiding cache miss and context distribution challenges

- **Evidence**: Described as a design alternative Cursor explicitly considers.
- **Confidence**: emerging (stated as an alternative; no direct comparison of outcomes
  between mid-chat switching and subagent approaches)
- **Quote**: "Another way to sidestep the challenges of mid-conversation model switching
  is to instead use a subagent, which starts from a fresh context window."
- **Our assessment**: The subagent alternative trades one set of tradeoffs for another:
  no cache miss, but you lose the full conversation history (not just a summary). The
  fresh context window means the subagent must be given the relevant task context
  explicitly. For practitioners designing multi-model workflows: the subagent approach
  is cleaner architecturally (no mid-session state transfer), while switching preserves
  continuity at the cost of cache performance. Task complexity determines which matters
  more.

### Claim 12: The Cursor harness evolved from heavy static context (folder layouts, semantic code snippets, compressed files) toward almost entirely dynamic tool-fetched context as model capability increased

- **Evidence**: First-party description of a harness evolution over time. Earlier
  guardrails limiting tool calls were removed as models improved.
- **Confidence**: emerging (described direction of travel; specific timeline not given)
- **Quote**: "We've adapted to increasing model capability by knocking down guardrails
  and providing more dynamic context." And: "At various points, that included the folder
  layout of the codebase, code snippets that semantically matched the query, and
  compressed versions of files that the user manually attached. That is mostly long
  gone."
- **Our assessment**: This is a concrete example of the harness-simplification
  principle documented in `blog-anthropic-harness-long-running.md` Claim 9 ("every
  component in a harness encodes an assumption about what the model can't do on its
  own"). Static context components (folder layout, pre-fetched snippets) encode the
  assumption that models can't find context on their own via tools. As models improved
  their tool use, these guardrails became unnecessary overhead. For practitioners: any
  static context injection in your harness is a candidate for removal as models improve.
  Test whether removing it degrades quality before assuming it's still load-bearing.

### Claim 13: An automated "software factory" — weekly LLM-powered log scanning that surfaces new/spiked issues and creates Linear tickets, with Cloud Agents triggerable directly from Linear — closes the degradation-detection-to-remediation loop

- **Evidence**: Described as a production automation running weekly. The pipeline
  integrates log scanning, issue surface, ticket creation, and agent-triggered repair.
- **Confidence**: anecdotal (described at a high level; no volume figures, model
  identities, or precision metrics published)
- **Quote**: "We also run a weekly Automation equipped with a skill that teaches the
  model how to search through our logs, surface issues that are new or recently spiked,
  and create or update tickets in a backlog with an investigation." And: "This process
  is part of the way we're instantiating an automated 'software factory' for our agent
  harness." And regarding triggering agents from tickets: "can even trigger them
  directly from Linear"
- **Our assessment**: The "software factory" framing positions agent-driven maintenance
  as a named, intentional operational pattern rather than an ad-hoc debugging tool.
  The loop is: logs → LLM analysis → Linear ticket → Cloud Agent fix attempt. This
  is the log-analysis equivalent of the crash-to-PR pipeline in
  `blog-cursor-app-stability.md` Claim 7 — both use agentic automation to close the
  gap between degradation detection and remediation. The weekly cadence vs. daily
  cadence reflects the different urgency profiles: crashes demand daily response,
  tool-call degradations may tolerate weekly sweeps. For practitioners: design
  degradation loops to match the urgency of each failure class.

## Concrete Artifacts

### Tool-Call Error Taxonomy

```
# Cursor agent harness tool-call error taxonomy (April 2026)
# Source: "Continually improving our agent harness," Stefan Heule & Jediah Katz

EXPECTED ERRORS (classified; monitored with per-tool per-model baselines)
  InvalidArguments     — model proposed an incorrect edit or invalid parameters
  UnexpectedEnvironment — file doesn't exist, path wrong, environment not as expected
  ProviderError        — upstream model provider outage or transient failure
  UserAborted          — user interrupted the tool call explicitly
  Timeout              — tool call exceeded time limit

UNKNOWN ERRORS (unclassified)
  → Treated as bugs in the harness
  → Trigger investigation and remediation
  → Must NOT accumulate in context (causes "context rot")

MONITORING
  Baselines: per-tool AND per-model (different models fail at different rates)
  Alert: anomaly detection fires when expected errors significantly exceed baseline
  Target: at least 2 or often 3 9s of reliability per tool call
```

### Model-Specific Tool Format Provisioning

```
# Cursor harness model provisioning rules (April 2026)
# Source: "Continually improving our agent harness," Stefan Heule & Jediah Katz

OpenAI models   → patch-based file editing tools
                   (trained on patch format; unfamiliar format = more reasoning cost + errors)

Anthropic models → string-replacement file editing tools
                   (trained on string replacement; same reasoning applies)

Principle: "provision each model with the tool format it had during training"
Rationale: "giving it the unfamiliar one costs extra reasoning tokens and produces more mistakes"
Note: either model CAN use either format — the provisioning is a harness optimization,
      not a hard capability constraint
```

### Online Eval Signal Architecture

```
# Cursor online eval signals for harness quality (April 2026)
# Source: "Continually improving our agent harness," Stefan Heule & Jediah Katz

KEEP RATE
  Definition: fraction of agent-proposed code changes remaining in codebase after
              fixed time intervals
  Signal type: behavioral (developer acceptance as implicit quality judgment)
  Latency: delayed (must wait for "fixed intervals of time")
  Annotation required: none
  Limitation: temporal lag; confounders (code kept for reasons unrelated to quality)

LLM-AS-JUDGE SATISFACTION SIGNAL
  Definition: LLM reads user responses to agent output to classify satisfaction
  Positive signal: user moving on to next feature
  Negative signal: user pasting a stack trace
  Signal type: semantic behavioral classification
  Latency: within-session (faster than Keep Rate)
  Annotation required: none (user behavior is the signal)
  Quote: "A user moving on to the next feature is a strong signal the agent did its
         job, while a user pasting a stack trace is a reliable signal that it didn't."

RELATIONSHIP TO OFFLINE EVALS (CursorBench, public benchmarks)
  Both Keep Rate and LLM-as-judge are online signals that cross-check offline eval
  verdicts; they catch regressions that look correct to a grader but feel worse to
  real users — same pattern described in blog-cursor-cursorbench.md Claim 8
```

### Harness Evolution: Static to Dynamic Context

```
# Context evolution in Cursor's agent harness (April 2026)
# Source: "Continually improving our agent harness," Stefan Heule & Jediah Katz

EARLIER HARNESS (heavy static context)
  - Folder layout of the codebase (injected as static context)
  - Code snippets that semantically matched the query
  - Compressed versions of user-attached files
  - Tool-call guardrails limiting model tool use
  Status: "That is mostly long gone"

CURRENT HARNESS (dynamic context)
  - Models fetch context via tool calls as needed
  - Guardrails removed as model capability increased
  - Static pre-injection replaced by model-driven retrieval
  Quote: "We've adapted to increasing model capability by knocking down guardrails
         and providing more dynamic context."

PRINCIPLE
  Each static context component encodes an assumption that the model can't retrieve
  that information on its own. Test periodically: if removing a static component
  doesn't degrade quality, the model has grown past the need for it.
```

### Mid-Chat Model Switching Design

```
# Mid-chat model switching architecture (Cursor, April 2026)
# Source: "Continually improving our agent harness," Stefan Heule & Jediah Katz

PROBLEM
  - KV cache is provider-specific; switching models invalidates the cache
  - Result: "a cache miss and a slower, more expensive first turn"

MITIGATION OPTION A: Conversation summarization at switch time
  - Summarize the conversation before switching
  - New model receives clean summary rather than full context
  - Reduces cache penalty
  - Risk: summary is lossy; complex tasks may lose important detail

MITIGATION OPTION B: Subagent with fresh context window
  - Start a new subagent rather than switching mid-conversation
  - No cache miss; no context transfer
  - Tradeoff: loses full conversation history (not even a summary)
  - Best for: tasks where the sub-task is sufficiently self-contained
```

## Cross-References

- **Corroborates**: `blog-cursor-cursorbench.md` Claim 8 ("The online-offline hybrid
  loop catches regressions where offline grading looks correct but the output feels
  worse to developers") — Keep Rate and LLM-as-judge described here are the concrete
  online signals that CursorBench Claim 8 describes abstractly. The two sources together
  give a complete picture of Cursor's eval architecture: CursorBench provides offline
  grading; Keep Rate and LLM-as-judge provide the online cross-check.

- **Corroborates**: `blog-anthropic-harness-long-running.md` Claim 7 ("Opus 4.5
  exhibited 'context anxiety' — premature task wrap-up as the context window filled")
  — this source independently documents the same named failure mode on a different
  unnamed model, with a different mitigation (prompt adjustment vs. sprint
  decomposition). The convergence of two independent teams naming the same failure
  mode strengthens confidence that context anxiety is a real, recurring model
  behavioral pattern tied to context filling.

- **Corroborates**: `blog-anthropic-harness-long-running.md` Claim 9 ("every
  component in a harness encodes an assumption about what the model can't do on its
  own, and those assumptions are worth stress testing") — the static-to-dynamic
  context evolution (Claim 12) is the concrete production example of this principle.
  Cursor removed static folder layouts, semantic snippets, and file compression as
  models grew capable enough to fetch context via tools. The principle is stated
  abstractly in the Anthropic post and demonstrated operationally here.

- **Extends**: `blog-cursor-cursorbench.md` — CursorBench covers offline eval
  methodology. This source adds the online eval layer (Keep Rate, LLM-as-judge A/B
  testing) that CursorBench does not cover. Together they form Cursor's complete
  measurement framework for harness quality.

- **Extends**: `blog-cursor-composer-self-summarization.md` Claim 2 (self-summarization
  5× more token-efficient than prompt-based baselines) — that post introduces
  summarization as a compaction technique for long contexts. This source adds a second
  use case: summarization at model-switch time to reduce cache penalty. The underlying
  mechanism and the information-loss risk are the same; the trigger condition differs.

- **Extends**: `blog-cursor-app-stability.md` Claim 7 (daily crash-stack-to-PR
  automation as an agent-in-the-loop maintenance loop) — the weekly software factory
  described here is a parallel agentic maintenance loop targeting a different failure
  domain (tool-call degradations vs. OOM crashes). Together these two posts establish
  that Cursor operates multiple cadenced agentic maintenance loops against distinct
  failure classes: daily for crash severity, weekly for tool-call reliability.

- **Novel**: The following patterns are new to the corpus:
  - **Keep Rate** as a named online eval metric using developer code-retention behavior
    as implicit quality signal — no other corpus source describes this pattern
  - **Context rot** as a named failure mode (errors accumulating in context degrade
    downstream decisions) — distinct from compaction-induced forgetting
  - **Five-category tool-call error taxonomy** (InvalidArguments, UnexpectedEnvironment,
    ProviderError, UserAborted, Timeout) with explicit unknown-error-as-bug treatment
  - **Per-tool per-model anomaly detection baselines** — different models have different
    baseline failure rates per tool; single-threshold alerting is insufficient
  - **Model-specific tool format provisioning** as an explicit harness engineering
    principle with stated rationale ("provision each model with the tool format it had
    during training")
  - **Mid-chat model switching with cache-miss mitigation** — the architecture of
    summarization at switch time and subagents as alternative
  - **"Software factory" framing** for agent-driven harness maintenance — weekly log
    scanning + ticket creation + agent-triggered remediation as a named operational
    pattern

## Guide Impact

- **Chapter 02 (Harness Engineering — monitoring and reliability)**: Add the five-category
  tool-call error taxonomy as the recommended classification scheme for harness error
  monitoring. The "unknown error = harness bug" principle and the per-tool per-model
  anomaly detection baseline design are actionable patterns for any team building agent
  monitoring. The 2-3 9s reliability target (Claim 7) provides a concrete production
  bar to aim for. Currently no chapter in the guide covers tool-call reliability
  monitoring at this level of specificity.

- **Chapter 02 (Harness Engineering — model-specific customization)**: Add Claim 8
  (model-specific tool format provisioning) as a concrete harness design principle:
  "Provision each model with the tool format it had during training to minimize reasoning
  overhead and error rate." This is the most directly actionable practitioner guidance
  in the post for multi-model harnesses.

- **Chapter 02 (Harness Engineering — harness simplification as models improve)**: Cite
  Claim 12 alongside `blog-anthropic-harness-long-running.md` Claim 9 as the dual-source
  evidence for the "strip harness components as models improve" principle. Cursor's
  static-to-dynamic context evolution is the concrete Cursor-side example; the Anthropic
  post provides the abstract principle with Opus 4.5 → 4.6 sprint decomposition removal
  as the Anthropic-side example.

- **Chapter 05 or 06 (Evaluation — online eval signals)**: Add Keep Rate (Claim 1)
  and LLM-as-judge satisfaction classification (Claim 2) as the two concrete online
  eval signals Cursor uses alongside CursorBench offline evals. The guide currently
  covers CursorBench (offline) via `blog-cursor-cursorbench.md`; this source provides
  the missing online eval layer. Together: offline CursorBench + online Keep Rate +
  online LLM-as-judge = Cursor's complete measurement architecture.

- **Chapter 04 (Context Engineering — context rot and static vs dynamic context)**:
  Add "context rot" (Claim 3) as a named failure mode distinct from compaction-induced
  forgetting — errors accumulate in context and corrupt downstream reasoning. Add the
  static-to-dynamic context evolution (Claim 12) as the positive pattern: prefer
  tool-fetched dynamic context over pre-injected static context as model tool use
  improves. Cite alongside `blog-anthropic-harness-long-running.md` Claim 9 as
  converging evidence from two different engineering teams.

- **Chapter 04 (Context Engineering — context anxiety)**: Add Claim 9 as a second
  data point for context anxiety (alongside `blog-anthropic-harness-long-running.md`
  Claim 7), noting that the same failure mode appears across models and can be
  mitigated at the prompt level (Cursor's approach) or architecture level (Anthropic's
  sprint decomposition). The prompt-level mitigation is the lighter-weight option for
  teams experiencing mild context anxiety.

- **Chapter 04 or 07 (Multi-agent — mid-chat model switching)**: Add Claim 10 (cache
  miss on model switching, summarization mitigation) and Claim 11 (subagents as
  alternative) as the design considerations for multi-model workflows. The two-option
  design space (summarize-and-switch vs. fresh-context subagent) is the practical
  framework for teams implementing model-selection features.

## Extraction Notes

- Article was fetched from cursor.com/blog/continually-improving-agent-harness and read
  in full. Multiple fetches were performed to extract verbatim quotes and verify
  specific technical claims. The full article includes six named sections (see below)
  covering all aspects of harness improvement.
- Section structure: (1) Evolving the context window, (2) Two ways of assessing harness
  changes, (3) Tracking and repairing degradations, (4) Customizing the harness for
  different models, (5) Facilitating mid-chat model switching, (6) The harness and the
  future of software development.
- The five error categories (Claim 4) are named explicitly in the source but not
  provided as a single quoted list; they are distributed across the "Tracking and
  repairing degradations" section.
- The article mentions a forward-looking multi-agent section anticipating specialized
  subagents for planning, editing, and debugging. This was not extracted as a primary
  claim (anecdotal/forward-looking) but is relevant context for the guide's multi-agent
  chapter.
- No contradictions to file: context anxiety is corroborated (not contradicted) by the
  Anthropic harness post; the static-to-dynamic evolution corroborates (not contradicts)
  the Anthropic harness simplification principle. No existing source note makes claims
  that this source opposes.
