---
source_url: https://cursor.com/blog/continually-improving-agent-harness
source_type: blog-post
title: "Continually improving our agent harness"
author: Stefan Heule & Jediah Katz (Cursor / Anysphere)
date_published: 2026-04-30
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: emerging
issue: "#479"
---

# Continually improving our agent harness (Cursor / Anysphere)

> Cursor's engineering team describes nine concrete operational patterns for measuring
> harness quality, detecting degradations, and customizing agent behavior per model —
> introducing Keep Rate and LLM-as-judge as novel online quality signals, a named
> tool-call error taxonomy, and the principle that static guardrails should be replaced
> with dynamic retrieval as model capability increases.

## Source Context

- **Type**: blog-post (Cursor / Anysphere engineering post, April 30, 2026; two named
  authors, ~5-minute read, no paywall)
- **Author credibility**: Stefan Heule and Jediah Katz are writing from inside Cursor's
  harness engineering team. This is a first-party operational account of production
  systems they built and operate. As with all Cursor engineering posts, there is an
  incentive to present their approach favorably; however, the specificity of the claims
  (named error categories, per-tool/per-model baselines, description of a model behaving
  unexpectedly) is consistent with genuine engineering documentation rather than marketing.
  No external peer review; treat claims as authoritative for "what Cursor does" and
  directionally credible for general practitioners.
- **Scope**: Covers the Cursor agent harness lifecycle: context window evolution, online
  and offline quality measurement, tool-call error monitoring, model-specific harness
  customization, mid-chat model switching, and automated maintenance. Does NOT cover
  model training, Cursor's product pricing, or any prescriptive configuration for
  practitioners building on Claude Code or other third-party harnesses.

## Extracted Claims

### Claim 1: Keep Rate — fraction of agent-generated code remaining in the codebase after fixed intervals — is a production online quality signal that captures solution quality independently of correctness oracles

- **Evidence**: Described as a live A/B testing metric. Cursor tracks Keep Rate in online
  experiments alongside latency, token efficiency, tool call counts, and cache hit rates.
  The metric is behavioral: if developers keep the code, the agent's output was good enough
  to use; if they discard it, it was not. No annotation or grader required.
- **Confidence**: anecdotal (first-party operational claim; not independently replicated;
  no published numbers)
- **Quote**: "Beyond these technical metrics, they track 'Keep Rate' — the percentage of
  agent-generated code remaining in user codebases after set intervals — to assess
  solution quality."
- **Our assessment**: This is the most novel measurement claim in the corpus. Keep Rate
  is structurally elegant: it uses developer behavior as the quality signal rather than
  requiring an explicit correctness oracle or manual annotation. A model that produces
  code developers delete or heavily rewrite scores low on Keep Rate even if a grader
  would call the output "correct." This metric is closest in spirit to the Cursor Blame
  technique in `blog-cursor-cursorbench.md` (using committed code as implicit ground
  truth) — both use the same behavioral proxy: what developers actually keep and use.
  The difference is that Cursor Blame generates offline benchmark tasks, while Keep Rate
  is an online signal used in A/B experiments. Any team with AI coding tool session
  logs correlated to git history can implement a version of Keep Rate.

### Claim 2: LLM-as-judge for online conversation satisfaction classifies whether user follow-up signals success or failure without requiring explicit user ratings

- **Evidence**: Described as a second online signal used alongside Keep Rate. The mechanism
  is: after the agent responds, a language model reads the user's next message and
  classifies it as a satisfaction signal (moving on to the next feature) or a failure
  signal (pasting a stack trace, asking the agent to fix what it broke).
- **Confidence**: anecdotal (first-party operational practice; no precision/recall figures
  published)
- **Quote**: "language models analyze user responses semantically, distinguishing satisfaction
  signals like 'moving on to the next feature' from negative indicators such as 'pasting
  a stack trace.'"
- **Our assessment**: This is a practical complement to Keep Rate. Keep Rate requires
  waiting for a time interval after the coding session; the LLM-as-judge signal fires
  immediately within the conversation. Together they cover two latency regimes: in-session
  quality (LLM-as-judge) and post-session acceptance (Keep Rate). The signal definition is
  worth capturing precisely: "user moved to next feature" = success; "user pasted a stack
  trace" = failure. This is the operational version of what CursorBench calls the
  "online-offline hybrid loop" — the post confirms which specific signals Cursor uses in
  the online half.

### Claim 3: "Context rot" — errors left in the context window — degrades the quality of subsequent model decisions; treating unknown tool-call errors as bugs prevents context rot from accumulating

- **Evidence**: Authors describe this as the motivating principle behind their zero-tolerance
  policy on unknown tool-call errors. Tool call errors can block agent progress and introduce
  context rot: accumulated mistakes that degrade subsequent decisions.
- **Confidence**: anecdotal (named failure mode from operational experience; no quantified
  degradation rate published)
- **Quote**: "Tool call errors present particular challenges, potentially blocking agent
  progress and creating 'context rot' through accumulated mistakes degrading subsequent
  model decisions."
- **Our assessment**: "Context rot" is the first explicit naming and framing of this failure
  mode in the corpus. The concept is intuitive — a model reasoning over a context that
  includes previous failed tool calls has a degraded picture of state — but naming it is
  useful for the guide because it gives practitioners a mental model for why unknown errors
  are worth treating as bugs rather than expected variance. The operational implication:
  any tool error that appears in a category outside the expected taxonomy is an unexpected
  contaminant in the context and should trigger a bug report, not just a retry.

### Claim 4: Cursor's tool-call error taxonomy distinguishes expected errors (five named categories) from unknown errors (harness bugs) — unknown errors trigger bug reports; expected errors trigger baseline-relative anomaly detection

- **Evidence**: Described as production classification logic. The five expected error
  categories are: `InvalidArguments`, `UnexpectedEnvironment`, `ProviderError`,
  `UserAborted`, and `Timeout`. Any error outside these categories is classified as
  an unknown error — a harness bug — and triggers a bug report. Expected errors
  trigger anomaly detection alerts when they exceed per-tool, per-model baselines.
- **Confidence**: emerging (specific taxonomy from named operational system; mechanism
  described in production; no code published)
- **Quote**: "The team classifies errors into categories: unknown errors (representing
  harness bugs), and expected errors including `InvalidArguments`, `UnexpectedEnvironment`,
  and `ProviderError`."
- **Our assessment**: The taxonomy itself is the artifact worth extracting. The five-
  category classification (plus the unknown class) is a direct design recommendation:
  any harness monitoring system should enumerate the expected error classes first, then
  treat everything outside that set as a bug rather than noise. The "unknown error rate
  > fixed threshold → bug report" rule is the operational corollary. This taxonomy
  gives practitioners a starting template; the specific category names may vary by
  harness but the unknown/expected split is universally applicable.

### Claim 5: Anomaly detection for tool-call errors must use per-tool, per-model baselines because different models have different baseline error rates for the same tool

- **Evidence**: Authors describe maintaining separate expected error rate baselines for
  every (tool, model) pair. Alerts fire when a tool's expected error rate for a specific
  model significantly exceeds its established baseline for that model. The motivation is
  explicit: a global baseline would produce false positives for models with inherently
  higher error rates on specific tools.
- **Confidence**: emerging (first-party operational practice; baseline methodology not
  quantified)
- **Quote**: "employ anomaly detection for expected errors exceeding per-tool, per-model
  baselines"
- **Our assessment**: This is an important operational detail that practitioners implementing
  similar monitoring would discover by accident. A harness monitoring system that uses a
  single global error threshold across all models will fire false alerts every time a
  lower-capability model is in use. The per-tool/per-model baseline design is the correct
  approach and should be a design requirement for any harness monitoring system that
  supports multiple models. This directly extends the monitoring patterns described in
  `blog-cursor-app-stability.md` — that post covers app-level OOM monitoring with
  per-version baselines; this post applies the same per-baseline principle to tool-call
  errors at the agent level.

### Claim 6: Model-specific tool format provisioning — giving each model the tool format it was trained on — reduces reasoning overhead and error rate in production

- **Evidence**: Authors describe a concrete production practice: OpenAI models receive
  patch-based file editing tools; Anthropic models receive string replacement tools.
  Additionally, prompting philosophy differs: OpenAI models require literal precision
  while Claude demonstrates greater tolerance for imprecise guidance.
- **Confidence**: emerging (first-party practice; reasoning about training format
  alignment is plausible but the specific error rate improvement is not quantified)
- **Quote**: "Each model receives customized tool formats matching training methodologies —
  OpenAI models use patch-based file editing while Anthropic's Claude uses string
  replacement."
- **Our assessment**: This is a concrete, actionable harness design principle: before
  assigning tools to a model, check the model's training data distribution and match
  tool interfaces to it. The patch-vs-string-replacement split is a real observable
  difference in Claude vs. GPT behavior with file editing tools (Claude is more reliable
  with exact string matches; GPT-series models handle diffs and patches more naturally).
  The prompting tolerance difference is consistent with practitioner reports across the
  corpus. Practitioners building harnesses that support multiple model providers should
  implement model-specific tool schemas rather than a single shared schema.

### Claim 7: "Context anxiety" — a model behavioral quirk where rising context window fullness triggers refusal to continue work — is a harness-level concern mitigated via prompt adjustment

- **Evidence**: Authors describe one model developing this behavior in production and
  mitigating it via prompt adjustments rather than model replacement or architectural
  changes. The harness detects and compensates for model-specific pathologies.
- **Confidence**: anecdotal (described as a single incident; specific model not named;
  prompt fix not published)
- **Quote**: "addressing one model's 'context anxiety' phenomenon where rising context
  window fullness triggered refusal behaviors"
- **Our assessment**: "Context anxiety" as a named behavioral quirk is independently
  corroborated by `blog-anthropic-harness-long-running.md`, which describes Opus 4.5
  exhibiting the same behavior ("begin wrapping up work prematurely" as context fills)
  and required sprint decomposition as an architectural mitigation. The Cursor post
  demonstrates a lighter-weight remediation path: prompt adjustment rather than
  architectural change. Together these two sources confirm context anxiety is a real
  failure mode that appears across multiple models, that it is manageable at the harness
  level, and that prompt adjustment is the lower-cost mitigation if the behavior is mild.
  The Anthropic note adds that Opus 4.6 eliminated the behavior — suggesting context
  anxiety may be a model generation characteristic that disappears as models improve.

### Claim 8: Mid-chat model switching causes cache misses because KV caches are provider-specific; conversation summarization at switch time mitigates latency/cost but risks losing detail on complex tasks

- **Evidence**: Authors describe this as a production design constraint. When users switch
  models mid-conversation, Cursor automatically applies the appropriate harness for the
  new model, but the new model must process conversation history from outside its training
  distribution. Custom instructions guide the new model away from calling unavailable
  tools. The cache miss increases both cost and latency.
- **Confidence**: emerging (described as operational experience; the cache-miss mechanism
  is technically grounded; no quantified cost delta published)
- **Quote**: "Conversation summarization at switch time provides cleaner context but risks
  losing important details in complex tasks. The authors recommend model consistency
  throughout conversations except when justified, suggesting subagents as an alternative
  approach offering fresh context windows."
- **Our assessment**: This is a design triangle with three vertices: (1) full conversation
  history passed to new model → cache miss + high cost, but no information loss; (2)
  conversation summary passed → lower cost, but potential detail loss on complex tasks;
  (3) subagent with fresh context → no cache miss, no information loss, but loses
  conversational continuity. The recommended default ("model consistency throughout
  conversations") is the correct conservative position. This extends `blog-cursor-
  composer-self-summarization.md`, which covers compaction at context limits using
  trained summarization — here the motivation is different (cache-miss mitigation at
  model switch) and the technique is different (on-the-fly conversation summary, not
  trained self-summarization). The two scenarios are distinct and should be documented
  separately in the guide.

### Claim 9: Heavy static context from early harness designs (lint errors, forced file re-reads, tool call limits) has been replaced by minimal static context plus dynamic tool-fetched retrieval as model capability improved

- **Evidence**: Authors describe the evolution directly: "When we first developed our
  coding agent in late 2024, models were much worse at choosing their own context."
  Early guardrails included surfacing lint and type errors after every edit, rewriting
  file reads when the model requested too few lines, and limiting maximum tool calls per
  turn. Current approach: OS details and git status as static context; everything else
  is agent-retrieved dynamically.
- **Confidence**: emerging (first-party description of their own evolution; the direction
  is corroborated by other notes)
- **Quote**: "When we first developed our coding agent in late 2024, models were much
  worse at choosing their own context and we invested lots of context engineering work
  into creating guardrails — for example, surfacing lint and type errors to the agent
  after every edit, rewriting its file reads when it requested too few lines, and even
  limiting the maximum number of tools it could call in one turn."
- **Our assessment**: This is a first-party confirmation of the harness-lifecycle principle
  described in `blog-anthropic-harness-long-running.md` Claim 9: "every component in a
  harness encodes an assumption about what the model can't do. When the model gets better,
  those components become dead weight." The Cursor post names the specific components that
  were removed (lint injection, read-rewriting, tool count limits) and the direction of
  change (toward dynamic retrieval). The two posts together make a strong combined case
  that harness engineering is an ongoing lifecycle — not a one-time design — and that
  practitioners should schedule a harness audit at every major model upgrade to identify
  which guardrails can be pruned.

### Claim 10: A weekly automated "software factory" scans logs for new or spiked harness issues, creates investigation tickets in Linear, and can trigger Cloud Agents directly from Linear to kick off fixes

- **Evidence**: Authors describe this as a production system running weekly, equipped
  with "specialized skills" for log scanning. The connection between Linear tickets and
  Cloud Agents is described as a direct integration: agents can be triggered from the
  ticket system. The authors cite a "focused sprint earlier this year" where this approach
  drove unexpected tool call errors down by an order of magnitude.
- **Confidence**: anecdotal (described at architectural level; no implementation details,
  skill definitions, or volume published)
- **Quote**: "A weekly automation equipped with specialized skills searches logs for newly
  emerged or spiked issues, creating tickets for investigation. 'Over the course of a
  focused sprint earlier this year, we drove unexpected tool call errors down by an order
  of magnitude.'"
- **Our assessment**: The "order of magnitude" reduction in unexpected tool call errors
  is the quantitative anchor for this claim — it's a strong result even without knowing
  the baseline. The architecture (log-scanning agent → ticket → cloud agent for fix) is
  a third agentic maintenance loop pattern at Cursor, alongside the crash-to-PR pipeline
  in `blog-cursor-app-stability.md` and the security agent PR loop in `blog-cursor-
  security-agents.md`. The combined picture from these three posts is that Cursor runs
  parallel agentic maintenance loops against distinct failure domains (stability, security,
  harness quality). The log scanning + ticketing half of this loop is replicable today
  by any team with structured agent logs and a ticket system. The Cloud Agents direct
  trigger from Linear is a Cursor-specific integration.

### Claim 11: Harness engineering will become more critical, not less, as AI-assisted software development shifts to multi-agent systems where coordination logic lives in the harness

- **Evidence**: Authors' forward-looking assessment based on their operational experience.
  They project that subtasks will be delegated across specialized agents for planning,
  editing, and debugging — and that the harness, not any single agent, will own
  orchestration.
- **Confidence**: anecdotal (vendor forward-looking claim; consistent with multi-agent
  coordination literature but no production evidence for the specific multi-agent
  architecture projected)
- **Quote**: "The ability to orchestrate that kind of coordination will live in the harness
  rather than any single agent. This means that, while harness engineering has always been
  important for agent success, it's only going to be more critical going forward."
- **Our assessment**: This is a framing claim rather than an operational finding, but it
  is consistent with the direction described in `blog-cursor-multi-agent-kernels.md` and
  `blog-anthropic-multi-agent-coordination-patterns.md`. The specific implication for
  the guide: harness engineering content should not be framed as a "current workaround
  for model limitations." It should be framed as a durable engineering discipline that
  grows more important as agent systems grow more complex. The Cursor authors are well-
  positioned to make this projection given their operational experience building
  production multi-agent harnesses.

## Concrete Artifacts

### Online Quality Signal Definitions

```
# Cursor online A/B eval signals (Stefan Heule & Jediah Katz, April 2026)
# Used alongside offline CursorBench evaluations

KEEP RATE
  Definition: fraction of agent-generated code remaining in user codebases
              after a fixed time interval
  How measured: correlate agent-generated code blocks with subsequent git history
  Signal type: behavioral proxy (developer acceptance = quality proxy)
  Latency: post-session (requires waiting for the interval to elapse)
  Advantage: no annotation, no grader, no explicit correctness oracle needed

LLM-AS-JUDGE CONVERSATION SATISFACTION
  Definition: LLM reads user's follow-up message and classifies satisfaction
  Positive signal: user moves on to next feature / accepts the output
  Negative signal: user pastes a stack trace / asks agent to fix what it broke
  Signal type: in-session (fires during conversation)
  Latency: immediate
  Advantage: complements Keep Rate for short-horizon quality detection

COMBINED USE
  Keep Rate = post-session acceptance signal (output quality over time)
  LLM-as-judge = in-session failure signal (did this specific turn succeed?)
  Both used together in online A/B harness evaluation
```

### Tool-Call Error Taxonomy

```
# Cursor tool-call error taxonomy (April 2026)
# Two-class system: expected errors vs. unknown errors

EXPECTED ERRORS (alerting: per-tool, per-model anomaly detection)
  InvalidArguments   — model passed malformed or out-of-range tool arguments
  UnexpectedEnvironment — runtime conditions prevented tool execution
  ProviderError      — external API or service failure
  UserAborted        — user cancelled the tool call
  Timeout            — tool execution exceeded time limit

UNKNOWN ERRORS (alerting: any occurrence above threshold → bug report)
  Definition: any error not classifiable into the five expected categories
  Treatment: treated as a harness bug, not expected operational variance
  Rationale: unknown errors create "context rot" — degrading subsequent
             model decisions by leaving unresolved failures in context
  Threshold: not disclosed; exceeding it triggers an immediate bug report

ANOMALY DETECTION DESIGN PRINCIPLE
  Baselines are per-tool AND per-model (not global)
  Reason: different models have different baseline error rates for the same tool
  Alert fires when: expected error rate for (tool, model) pair > baseline
                    for that specific (tool, model) combination
```

### Model-Specific Harness Customization Matrix

```
# Cursor model-specific tool and prompt customization (April 2026)

                    OpenAI models           Anthropic models (Claude)
File editing tool   Patch-based             String replacement
Prompt precision    High literal precision  Tolerates imprecision
                    required

DESIGN PRINCIPLE
  Assign each model the tool format it was trained on
  Reason: reduces reasoning overhead and tool-call error rate
  Method: when gaining early access to a new model, start from nearest
          existing harness, run offline evals, iterate

MODEL QUIRK DETECTION AND MITIGATION
  Symptom: "context anxiety" — model begins refusing work as context fills
  Mechanism: harness detects refusal pattern
  Mitigation: prompt-level adjustment (specific prompt not published)
  Alternative if prompt fails: sprint decomposition (see blog-anthropic-harness-long-running.md)
```

### Mid-Chat Model Switching Design Triangle

```
# Mid-chat model switching tradeoffs (Cursor, April 2026)

OPTION 1: Full conversation history → new model
  Cache impact: MISS (KV caches are provider-specific)
  Cost/latency: HIGH (full context reprocessed at new provider)
  Information loss: NONE
  Use when: complex task where detail loss is unacceptable

OPTION 2: Conversation summary → new model
  Cache impact: reduced miss (shorter context)
  Cost/latency: MEDIUM
  Information loss: POSSIBLE on complex multi-step tasks
  Use when: simple handoff, task is mostly complete

OPTION 3: Subagent with fresh context window
  Cache impact: NONE (new session)
  Cost/latency: LOW for the switch itself
  Information loss: HIGH (subagent starts fresh)
  Use when: the new task is largely independent

RECOMMENDED DEFAULT
  Maintain model consistency throughout a conversation
  Switch only when clearly justified
  Custom handoff instructions required in all cases
  (instruct incoming model away from tools unavailable in its harness)
```

### Harness Lifecycle: Static to Dynamic Context Evolution

```
# Cursor context window evolution (late 2024 → current, April 2026)

EARLY HARNESS (late 2024)
  What models couldn't do: choose appropriate context autonomously
  Guardrails added:
    - Surface lint and type errors after every edit (proactive injection)
    - Rewrite file reads when model requested too few lines (compensatory expansion)
    - Limit maximum tool calls per turn (constraint enforcement)
    - Heavy static context at session start: folder layouts, semantic code
      snippets, compressed file versions

CURRENT HARNESS (2026)
  What models can now do: choose their own context via tool calls
  Retained static context: OS details, git status (minimal anchors)
  Everything else: dynamic retrieval via agent tool calls
  Guardrails removed: all of the above from early harness

META-PRINCIPLE (corroborated by blog-anthropic-harness-long-running.md)
  "Every harness component encodes an assumption about model limitations.
   As models improve, those assumptions go stale."
  Schedule a harness audit at each major model upgrade.
  Prune components that are no longer load-bearing.
```

## Cross-References

- **Corroborates**: `blog-cursor-cursorbench.md` — CursorBench note (Claim 8) describes
  the online-offline hybrid eval loop as catching regressions "where the agent's output
  looks correct to a grader but feels worse to a developer." The new post fills in the
  specific online signals Cursor uses: Keep Rate and LLM-as-judge. Together these two
  notes give the complete picture of Cursor's production eval architecture. The
  CursorBench note names the architecture; this post names the signal definitions.

- **Corroborates**: `blog-anthropic-harness-long-running.md` — Two independent
  corroborations in this post: (1) "context anxiety" as a named, real behavioral quirk
  is independently confirmed by the Anthropic post (Opus 4.5 "begin wrapping up work
  prematurely as context fills"); (2) the static-to-dynamic context evolution principle
  is independently confirmed by the Anthropic post's Claim 9 ("every harness component
  encodes an assumption about model limitations — prune them as models improve"). Both
  posts were written by different teams about different harnesses, making this the
  strongest cross-organization corroboration in the corpus for these two principles.

- **Extends**: `blog-cursor-composer-self-summarization.md` — that post covers trained
  context compaction when the context window fills (trained self-summarization via RL).
  The new post adds a second distinct use of conversation summarization: mitigating
  cache-miss cost when switching models mid-chat. The scenarios are different (end-of-
  context compaction vs. mid-chat model handoff), the techniques differ (trained model
  behavior vs. on-the-fly summary), and the failure modes differ (information loss on
  long sessions vs. information loss on complex multi-step tasks). Guide should treat
  these as separate patterns, not as variations of the same technique.

- **Extends**: `blog-cursor-app-stability.md` — the crash-stack-to-PR automation described
  there (daily) and the software factory log-scanning + ticket creation described here
  (weekly) are two instances of the same pattern: agentic maintenance loops that
  continuously harvest production signals and close the loop to remediation. Together
  these two posts (plus `blog-cursor-security-agents.md` for security) establish
  Cursor's multi-domain agentic maintenance loop architecture as a platform-level
  design commitment, not a feature-specific tactic.

- **Extends**: `blog-cursor-cursorbench.md` — the "shelving promising approaches that show
  negligible quality improvement" described here (expensive context summarization models
  tested and found unhelpful) is a direct application of the CursorBench A/B methodology.
  The new post demonstrates the evaluation loop in use, producing a negative result.

- **Novel**: The following patterns are new to the corpus and not covered by any existing
  source note:
  1. Keep Rate as a named online quality signal (first definition and operational
     description in the corpus; closest analogue is Cursor Blame in CursorBench note,
     but they are distinct mechanisms)
  2. LLM-as-judge for conversation satisfaction using follow-up message classification
     (the specific signal definition — "moved to next feature" vs. "pasted stack trace"
     — is not described elsewhere)
  3. "Context rot" as a named failure mode (first explicit naming and framing in the corpus)
  4. Tool-call error taxonomy with five named categories plus unknown/expected distinction
  5. Per-tool, per-model anomaly detection baselines (per-model differentiation is new)
  6. Software factory: weekly log-scanning agent + Linear ticket creation + Cloud Agent
     direct trigger (distinct from the daily crash-to-PR loop in app-stability note)
  7. Mid-chat model switching design triangle with the three-option analysis

## Guide Impact

- **Chapter on Harness Engineering (online eval signals)**: Add Keep Rate and LLM-as-judge
  as named production online quality signals. Currently the guide references online eval
  loops generically. This source provides the specific signal definitions practitioners
  can implement. Recommendation: "After deploying harness changes, instrument Keep Rate
  (fraction of AI-generated code remaining after N days) and LLM-as-judge satisfaction
  (classify follow-up messages by success/failure signal) as the two primary online
  signals. Wait for Keep Rate data before concluding a change is neutral."

- **Chapter on Harness Engineering (error monitoring)**: Add tool-call error taxonomy
  as a design requirement. Recommendation: "Define your expected error categories before
  you build your alerting system. Treat any error outside those categories as a harness
  bug. Use per-tool, per-model baselines — not global thresholds — for anomaly detection,
  because different models have different baseline error rates for the same tool."

- **Chapter on Harness Engineering (model-specific customization)**: Add model-specific
  tool format provisioning as a harness design principle. Recommendation: "When supporting
  multiple model providers, design model-specific tool schemas matched to each model's
  training format. OpenAI-family models handle patch-based file editing more naturally;
  Anthropic models handle exact string replacement more naturally. Do not use a single
  shared tool schema across all providers."

- **Chapter on Context Engineering (context rot)**: Add "context rot" as a named failure
  mode. Recommendation: "Unknown errors left in the context window degrade subsequent
  model decisions — this is 'context rot.' Treat unknown errors as bugs, not noise. Aim
  for zero unknown errors in your tool call error taxonomy."

- **Chapter on Context Engineering (static vs. dynamic)**: The Cursor evolution from
  heavy static context (lint injection, forced expansions, tool limits) to dynamic
  retrieval is the canonical example for the guide's discussion of context strategy.
  Recommendation: "Audit your static context at each model upgrade. Guardrails built
  for an earlier model generation are often load-bearing only if the model still needs
  them. Remove guardrails that compensate for limitations the new model no longer has."

- **Chapter on Multi-Agent / Model Switching**: Add the mid-chat model switching design
  triangle as a reference pattern. Recommendation: "Prefer model consistency within a
  conversation. When switching is necessary, choose between full history (no information
  loss, high cache-miss cost), conversation summary (medium cost, risk of detail loss on
  complex tasks), or subagent (no cache penalty, loss of continuity). Always include
  custom handoff instructions telling the incoming model which tools are unavailable in
  its harness."

- **Chapter on Harness Engineering (lifecycle / maintenance)**: Add the software factory
  pattern as the third agentic maintenance loop example (alongside crash-to-PR and
  security PR loops from other Cursor posts). Recommendation: "Production harnesses
  degrade continuously. Implement a weekly log-scanning agent that classifies tool-call
  errors by category, surfaces newly emerged or spiked error types, and creates
  investigation tickets. Connect the ticket system to your remediation agents to close
  the loop from detection to fix."

## Extraction Notes

- Article is approximately 5 minutes / ~1,400 words. Full content read. No paywalled
  sections. The article is organized under five main headings: Evolving the context
  window; Two ways of assessing harness changes; Tracking and repairing degradations;
  Customizing the harness for different models; Facilitating mid-chat model switching;
  and a closing section on the future of software development.
- The error taxonomy in the original post explicitly names `InvalidArguments`,
  `UnexpectedEnvironment`, and `ProviderError` as expected error categories. The
  Prospector's triage comment adds `UserAborted` and `Timeout` — these are described
  in the post but not in a single enumerated list; I have included all five per the
  triage guidance and the prose description in the source.
- The specific model exhibiting "context anxiety" is not named in the post. The Prospector's
  triage correctly notes this is a general pattern; the cross-reference to
  `blog-anthropic-harness-long-running.md` (which names Opus 4.5 specifically) provides
  the model identification for practitioners who need it.
- No contradictions to file: the static-to-dynamic context evolution claim is corroborated
  (not contradicted) by `blog-anthropic-harness-long-running.md`. The Keep Rate claim
  complements (not contradicts) the CursorBench offline evaluation methodology. No
  existing source note makes claims that this source opposes.
- The "order of magnitude" reduction in unexpected tool call errors from the focused sprint
  is the only quantified outcome in the post for the software factory claim. No baseline
  figure published; treat as directionally strong but not audited.
