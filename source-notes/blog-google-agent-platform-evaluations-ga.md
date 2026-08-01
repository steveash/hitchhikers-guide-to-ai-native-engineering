---
source_url: https://developers.googleblog.com/agent-and-model-evaluations-in-gemini-enterprise-agent-platform-are-now-ga/
source_type: blog-post
title: "Agent and Model Evaluations in Gemini Enterprise Agent Platform are now GA"
author: Alex Martin (Product Manager), Dima Melnyk (Product Manager) — Cloud AI
date_published: 2026-07-31
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: emerging
issue: "#2389"
---

# Agent and Model Evaluations in Gemini Enterprise Agent Platform are now GA

> Google's GA announcement for a unified agent/model evaluation service —
> 20+ pre-built metrics, DeepMind-co-developed "adaptive rubrics" that
> generate case-specific pass/fail criteria instead of one fixed judge
> prompt, integrated user/environment simulators, and continuous online
> production monitoring — paired with a linked companion post describing
> an installable coding-agent skill (explicitly targeting Claude Code)
> that drives the whole eval-fix loop autonomously under human approval.

## Source Context

- **Type**: blog-post (official Google Developers Blog, GA/product
  announcement, published July 31, 2026). This note also follows one
  linked sub-page in depth — a companion post from the day before,
  "Driving the Agent Quality Flywheel from Your Coding Agent"
  (2026-06-30) — plus two Google Cloud reference-docs sub-pages
  ("Manage evaluation metrics" and "Continuous evaluation with online
  monitors") that the GA post links to for specifics the announcement
  itself only names in passing.
- **Author credibility**: Alex Martin and Dima Melnyk are named Google
  Product Managers for Cloud AI, writing first-party about a shipped,
  generally-available feature of a product Google sells and operates.
  The companion flywheel post is co-authored by Dima Melnyk and Jason
  Dai (Software Engineer), and states the underlying AutoRaters were
  "developed in close partnership with Google DeepMind." This is vendor
  content about a vendor's own product; no third-party or independently
  reproduced evidence is presented anywhere in either post — all metrics,
  workflows, and the one worked case study are Google's own account of
  its own system.
- **Scope**: Covers what shipped at GA (metrics, adaptive rubrics,
  experiments, simulators, online monitors, integration paths, pricing)
  and, via the linked flywheel post, a concrete worked example of the
  service driven end-to-end by an installable coding-agent skill against
  two real ADK sample agents. Does NOT cover: the underlying model or
  algorithm behind the AutoRaters, comparative benchmarks against other
  evaluation vendors, or any evaluation outcome independently verified
  outside Google. The GA post's own linked "regions and security
  features table," "Evaluate agents with the GenAI Client" tutorial, and
  full ADK evaluation docs were not fetched for this note (see Extraction
  Notes) — this note covers what was directly read, not the full doc tree.

## Extracted Claims

### Claim 1: Running the same evaluation metrics on local experiments and live production traffic means a production score drift signals a problem with the agent, not with how it was measured
- **Evidence**: Stated as the article's opening framing principle, immediately following the announcement of GA status.
- **Confidence**: emerging (first-party design rationale for why one engine spans both stages; no measured comparison against split dev/prod tooling is offered)
- **Quote**: "When you use consistent quality scoring on local experiments and live traffic, a drift in production points to a problem with the agent rather than with the way it was measured."
- **Our assessment**: This is the load-bearing argument for unifying dev-time and production-time evaluation on one engine — if the metrics themselves differ between stages, any drift is confounded with a measurement change, and teams can't tell whether the agent got worse or the yardstick moved. It's a clean, generalizable principle independent of Google's specific implementation.

### Claim 2: The service ships more than 20 pre-built metrics spanning quality, safety, grounding, agent tool use and trajectory, and reference-based scoring for tasks like summarization and translation
- **Evidence**: Stated directly under "What's generally available" as the first named capability.
- **Confidence**: settled (a specific, named count of shipped metrics in a GA product)
- **Quote**: "Start from more than 20 pre-built metrics spanning quality, safety, grounding, agent tool use and trajectory, and reference-based scoring for tasks like summarization and translation."
- **Our assessment**: This is a concrete inventory claim rather than a design principle — useful primarily as a citable "what ships out of the box" fact, distinguishing computation-based reference metrics (ROUGE, BLEU, MetricX, COMET, exact match — named later in the post) from the model-graded rubric metrics that are the more novel part of this source.

### Claim 3: Adaptive rubrics tailor the judging criteria to each individual case instead of applying one fixed LLM-as-judge prompt uniformly across inputs that don't deserve the same questions
- **Evidence**: Named as the service's headline evaluation mechanism, elaborated later in the "Evaluation metrics" section (Claim 8 below).
- **Confidence**: emerging (a named, shipped mechanism; the underlying rubric-generation model/algorithm is not described in this post beyond "co-developed with Google DeepMind")
- **Quote**: "Adaptive rubrics tailor the judging criteria to each case instead of applying one brittle llm-as-judge prompt across inputs that don't deserve the same questions."
- **Our assessment**: This directly names the failure mode of naive LLM-as-judge setups — a single static rubric applied indiscriminately across heterogeneous inputs — as the problem adaptive rubrics solve. It's the sharpest articulation in our corpus so far of *why* a fixed judge prompt is brittle, not just that alternatives exist.

### Claim 4: Experiments integrate with case generation, a user simulator for multi-turn cases, and an environment simulator that stands in for systems the agent calls, including simulating a failing or slow backend without touching production
- **Evidence**: Named directly in the "What's generally available" summary and elaborated in the "Case generation and simulation" section.
- **Confidence**: emerging (named, shipped capabilities; no data on simulator fidelity relative to real users/systems is given)
- **Quote**: "Experiments integrate with case generation to bootstrap an evaluation dataset, a user simulator to play out multi-turn cases without scripting each reply, and an environment simulator to stand in for the systems the agent calls, so you can emulate a failing or slow backend without affecting production."
- **Our assessment**: The environment simulator in particular is a distinct capability from anything else in our eval-tooling corpus: it lets a team inject a failure mode (slow/broken dependency) into an eval run without needing a real staging environment that actually fails. This is a chaos-engineering-adjacent pattern applied to agent evaluation specifically.

### Claim 5: Continuous evaluation grades production traces already being collected and produces score-over-time charts and drift alerts, without requiring custom data-processing pipelines
- **Evidence**: Named under "Online monitors and telemetry integrations" in the GA summary, elaborated later in the full "Online monitors and telemetry integrations" section.
- **Confidence**: emerging (named, shipped capability; alert-quality/false-positive-rate data is not given)
- **Quote**: "Continuous evaluation on live production traffic grades the traces you already collect and produces score-over-time charts and drift alerts, without needing to set up custom data processing pipelines."
- **Our assessment**: The "you already collect" framing matters — this is explicitly designed to piggyback on existing OpenTelemetry trace collection rather than requiring a parallel logging pipeline, which lowers the adoption cost relative to building bespoke production monitoring.

### Claim 6: Evaluations are reachable from four integration surfaces — the Agent Platform SDK, agents-cli, the Evaluation section of the Google Cloud console, and directly from ADK
- **Evidence**: Stated as a single summary sentence naming all four surfaces.
- **Confidence**: settled (a specific, named list of integration paths for a GA product)
- **Quote**: "You can reach evaluations from the Agent Platform SDK, agents-cli, the Evaluation section in Agent Platform Google Cloud console, and directly from ADK."
- **Our assessment**: Four distinct entry points (programmatic SDK, CLI, web console, and framework-native via ADK) signal that Google is positioning evaluation as a cross-cutting capability meant to be reachable from wherever a team already works, rather than a single dedicated tool teams must adopt separately.

### Claim 7: For large evaluation jobs, the system clusters failures into interpretable, actionable groups against a taxonomy of failure reasons, with a pre-built taxonomy available for adaptive rubrics covering common agent failure modes
- **Evidence**: Described in the "Experiments" section as "issue clustering," with an explicit fallback for teams without their own taxonomy.
- **Confidence**: emerging (named, shipped capability; the pre-built taxonomy's actual categories are not enumerated in this post)
- **Quote**: "For large evaluation jobs, the system supports issue clustering: it groups eval failures into interpretable, actionable clusters against your own taxonomy of failure reasons. If you haven't developed a taxonomy yet, you can use a pre-built one we have for adaptive rubrics, which covers the common ways agents go wrong."
- **Our assessment**: This addresses a scaling problem that individual case-by-case review can't: once you have hundreds or thousands of failing eval cases, someone still has to read all of them unless failures are pre-clustered into actionable groups. Providing a pre-built taxonomy lowers the bar for teams who haven't yet built their own failure-mode categorization.

### Claim 8: An adaptive rubric is an LLM-judge metric workflow, co-developed with Google DeepMind, that generates case-specific pass/fail tests from the eval case definition, the developer instruction, and the tool declarations, then grades traces against those rubrics with a verdict and rationale per rubric
- **Evidence**: Direct definitional statement in the "Evaluation metrics" section, the most detailed mechanism description in the GA post.
- **Confidence**: emerging (a specific, named mechanism attributed to a named research partnership; not independently audited, and no accuracy/reliability numbers are given in this post — see Claim 14 from the linked flywheel post for the caveat Google itself attaches)
- **Quote**: "an adaptive rubric is an advanced LLM-judge metric workflow co-developed with our research partners at Google DeepMind. It creates case-specific pass/fail tests (rubrics) from the eval case definition, the developer instruction, and the tool declarations. It then grades the traces against these rubrics, providing the verdict and rationale per rubric."
- **Our assessment**: This is the concrete mechanism behind Claim 3's headline claim — the rubric generator conditions on three inputs (the eval case, the developer's own instructions, and the tool schema) rather than a generic judge prompt, so the pass/fail bar for a given case is derived from what the agent was actually told to do and what tools it had, not a one-size-fits-all quality bar.

### Claim 9: Google names and defines six adaptive-rubric variants for common evaluation questions — Task Success, Tool Use Quality, Safety, Trajectory Quality, Final Response Quality, and Hallucination/Grounding — plus separate image/video quality metrics
- **Evidence**: Enumerated directly in the "Evaluation metrics" section of the GA post, and independently confirmed with fuller definitions on the linked "Manage evaluation metrics" docs sub-page (Concrete Artifacts below).
- **Confidence**: settled (named, shipped metric set, cross-confirmed across two first-party sources — the blog post and the docs page)
- **Quote**: "Task Success grades goal fulfillment across a conversation from observable outcomes and confirmations in the agent's responses." ... "Tool Use Quality evaluates tool selection, argument correctness, and schema compliance." ... "Safety scores the response against content policies spanning hate speech, harassment, dangerous content, sexually explicit material, and PII, returning the policies violated."
- **Our assessment**: Notably, per the docs sub-page (Concrete Artifacts below), Safety and Hallucination are implemented as **static** rubrics, not adaptive ones — the GA blog post itself doesn't draw this distinction explicitly, but the docs page does. This matters: Google is not claiming every metric benefits from per-case rubric generation; safety-policy violations and factuality-against-tool-output are checked against a fixed bar, while goal achievement, tool-use quality, and trajectory quality (things that genuinely vary case-to-case) get adaptive treatment.

### Claim 10: Server-side evaluation runs support any Model Garden model, including all Gemini and Anthropic models, for custom LLM-as-a-judge metrics
- **Evidence**: Stated in the "Evaluation metrics" section describing custom metric support.
- **Confidence**: settled (a specific, named vendor-inclusion claim for a GA product feature)
- **Quote**: "When running locally you can use any model from any provider, and server-side evaluation runs support any Model Garden model, including all Gemini and Anthropic models."
- **Our assessment**: This is directly relevant to our corpus: Google's own agent-evaluation infrastructure explicitly supports Claude/Anthropic models as the judge model for custom metrics in server-side runs, not just as a subject being evaluated. It signals that a team building on Claude could adopt this evaluation service without being locked into Gemini as the judge model.

### Claim 11: Pricing charges standard model-call rates for LLM-as-a-judge and other model-based metrics plus Cloud Storage for server-side run artifacts; code-based and computation metrics add no additional cost; datasets and traces stay in the customer's own project
- **Evidence**: Stated directly in the "Pricing and availability" section.
- **Confidence**: settled (a specific, first-party pricing-model statement for a GA feature)
- **Quote**: "You pay standard rates for the model calls behind LLM-as-a-judge and the other model-based metrics – plus Cloud Storage for the artifacts a server-side run keeps. Code-based and computation metrics add no additional cost. Your datasets and traces always stay in your project."
- **Our assessment**: The cost asymmetry (LLM-judge metrics cost model-call rates; code-based/computation metrics are free) is a concrete lever teams can use when designing an eval suite on a budget — prefer code-based checks (exact match, JSON-shape validation) where they suffice, and reserve LLM-judge metrics (including adaptive rubrics) for genuinely subjective or open-ended quality questions.

### Claim 12: A reusable, installable skill lets a coding agent (explicitly including Claude Code) drive the entire evaluation-and-fix loop on a developer's behalf, with the optimizer and evaluator kept architecturally decoupled so that whatever proposes a fix never grades its own work
- **Evidence**: Named in the GA post's closing section and elaborated in the linked companion post, "Driving the Agent Quality Flywheel from Your Coding Agent" (2026-06-30), which names Claude Code by name.
- **Confidence**: emerging (a shipped, installable skill described with one detailed worked example in the companion post; not independently used or verified by this Miner)
- **Quote**: "You can even run the loop straight from your coding agent: a reusable skill walks Claude Code and similar tools through the full agent-quality flywheel." (GA post) — "The optimizer and the evaluator stay decoupled: whatever proposes a fix (your coding agent, an automated optimizer, or you) never grades it. The Gemini Enterprise Agent Platform GenAI evaluation service scores it independently. An optimizer that grades itself learns to game the metric instead of improving the agent." (companion post)
- **Our assessment**: This is the single most directly relevant claim in this source for our guide's audience: Google is explicitly naming Claude Code as a supported driver for its evaluation skill, and the "optimizer never grades itself" architectural principle is a general anti-gaming safeguard applicable to any self-improving harness, not just Google's own tooling. It's the same underlying concern as `blog-langchain-better-harness-evals.md` Claim 6 ("agents are famous cheaters") but solved by a different structural mechanism — decoupling roles rather than holding out a test set (see Cross-References).

### Claim 13: The skill's five-stage loop (Prepare Data, Run Inference, Grade, Analyze Failures, Optimize & Iterate) runs the same way against both synthetic dev-time data and real production traces — grading production traces skips the "Run Inference" stage since those traces already exist
- **Evidence**: Described in the companion post's "The flywheel, zoomed in" and "From the inner loop to the production loop" sections.
- **Confidence**: emerging (a described, shipped workflow; not independently reproduced by this Miner)
- **Quote**: "Prepare Data: build an evaluation dataset from existing OTel traces, hand-crafted cases, or synthesized scenarios. Run Inference: execute the agent over the dataset to produce traces; skip this if you already have traces. Grade: score traces with Google's adaptive AutoRaters... This is the only stage that always runs." ... "The same skill runs against production traffic; you just point it at real traces instead of synthesized ones. Tell it to grade last week's production sessions, and because those traces are already complete, it skips Run Inference entirely and grades them in place with the same raters."
- **Our assessment**: The reuse of identical stages for dev and production evaluation is the practical instantiation of Claim 1's "same engine for both stages" principle — it's not just that the *metrics* are consistent between dev and prod (Claim 1), but that the *procedure* driving those metrics is literally the same code path with one stage conditionally skipped.

### Claim 14: The built-in AutoRaters are explicitly framed by Google as "a strong directional signal," not ground truth — the recommended practice is to trust the delta between before/after runs more than any single absolute score
- **Evidence**: Stated directly in the companion post's "What this skill is (and isn't)" section, as an explicit limitation the authors attach to their own model-based judges.
- **Confidence**: emerging (a first-party caveat about the reliability of the company's own judge system — notable specifically because it's a limitation the vendor volunteers rather than a claim of accuracy)
- **Quote**: "The built-in AutoRaters are more than just a model scoring an answer. For a multi-turn agent they extract the user's intent from the conversation, generate rubrics specific to that case, validate the trace against each criterion, and majority-vote across samples. Sophisticated, but still model-based: treat the scores as a strong directional signal, and trust the deltas between runs more than any single number as an absolute grade."
- **Our assessment**: This is a rare and valuable vendor self-limitation: Google is telling users not to treat its own flagship adaptive-rubric mechanism as ground truth, and to instead rely on relative comparison (did this change help or hurt) rather than absolute scores. This directly corroborates `docs-ghaw-measuring-impact.md` Claim 13 ("do not overreact to single numbers... trend data is usually more useful") — two different vendors (GitHub Agentic Workflows and Google Agent Platform) independently converge on trend/delta-over-absolute-number as the correct way to read agent-quality metrics.

### Claim 15: A single custom categorical rubric, promoted above the noisy adaptive built-ins, let a team isolate and quantify one specific concern (whether an agent honored a mid-conversation revision) that the adaptive metrics detected but diluted into a blended score
- **Evidence**: The companion post's worked case study on `travel-concierge`, an ADK sample multi-agent trip planner. The custom rubric `revision_honored` used a four-way categorical verdict (HONORED / IGNORED / PARTIAL / NO_REVISION), gated at "more than 20% come back IGNORED."
- **Confidence**: anecdotal (a single named worked example on a sample/demo agent, not a production system; presented by Google as illustrative)
- **Quote**: "multi_turn_task_success and multi_turn_trajectory_quality are adaptive: they'll generate a rubric for each case and will surface a revision miss inside it. But it lands as one criterion among several that are regenerated differently every run, folded into a blended score; there's no stable 'revision-honoring' number to threshold or trend. So I'll promote that one concern to its own metric: a custom rubric, revision_honored, with a categorical verdict (HONORED / IGNORED / PARTIAL / NO_REVISION) that I can count, gate on (act if more than 20% come back IGNORED), and track cycle over cycle." ... "That 21% cleared the skill's own action threshold."
- **Our assessment**: This is a concrete, reusable diagnostic pattern that generalizes beyond Google's tooling: when an adaptive/blended metric is sensitive enough to detect a specific failure but too noisy or too aggregated to *track* it reliably (the underlying rubric criteria regenerate every run), promote that one concern to its own fixed, countable, categorical metric. The failure itself is also notable on its own terms — in three of four IGNORED cases, "its internal state was correct... but its final message to the user echoed the stale value anyway," i.e., the agent's tool calls and memory were right but its final natural-language response contradicted its own state.

### Claim 16: On a different, unrelated agent, running the skill with no specific hypothesis ("find a real failure and fix it") surfaced that an agent silently stopped disclosing which tools it used in 14 of 15 cases; a one-paragraph instruction fix raised tool-disclosure compliance from 0% to 96% of responses in a single cycle
- **Evidence**: The companion post's second worked example, on `software-bug-assistant`, a bug-triage agent wired to a Postgres ticket database via an MCP toolbox plus web/StackExchange search.
- **Confidence**: anecdotal (a single named worked example on a sample/demo agent)
- **Quote**: "We tried exactly that on a different agent: software-bug-assistant from google/adk-samples, a bug-triage assistant wired to real tools (a Postgres ticket database behind an MCP toolbox, plus web and StackExchange search). With no hypothesis, the skill surfaced one cluster immediately: in 14 of 15 cases the agent did the work correctly but never told the user which tools it had called. Its own instruction asked for it, and the model had quietly treated it as optional. A one-paragraph fix mandating that every response now ends with a footer like "Tools used: search-tickets, get-ticket-by-id" took that from 0% to 96% of responses across all 15 cases, in a single cycle."
- **Our assessment**: This is a good illustration of "clustering failures without a taxonomy" (Claim 7) in practice, and of a distinct failure mode from Claim 15's: here the agent silently dropped a disclosure instruction it had been given, rather than contradicting its own correct internal state. Both cases in this post share a pattern worth naming: the agent *did the work correctly* in both, and the defect was purely in what it communicated about that work — task-success metrics alone would likely have missed both, since the underlying task outcomes (planning, ticket lookup) were fine.

### Claim 17: Online monitors run on a scheduled loop (typically every 10 minutes) that queries sampled production traces, evaluates them with configured metrics, and writes results to Cloud Logging and Cloud Monitoring; creating an `OnlineEvaluator` carries an explicit privilege-escalation risk the docs flag as a security disclosure
- **Evidence**: Detailed on the linked "Continuous evaluation with online monitors" docs sub-page, elaborating the GA post's higher-level "online monitors and drift alerts" claim (Claim 5).
- **Confidence**: settled (specific, documented operational mechanics and an explicit first-party security disclosure)
- **Quote**: "Online monitors run on a scheduled evaluation loop, typically every 10 minutes." ... "Query: Samples data from Cloud Trace and Cloud Logging based on your filters. Evaluate: Runs configured metrics using the Gemini Enterprise Agent Platform Evaluation Service. Report: Writes results back to Cloud Logging and exports numeric scores to Cloud Monitoring." ... "Security Disclosure: Online evaluation relies on the project-level service account (P4SA). Any user with permissions to create an `OnlineEvaluator` can attach it to any agent within the same project. To avoid potential privilege escalation, ensure that `OnlineEvaluator` creation is restricted to authorized administrators."
- **Our assessment**: The privilege-escalation disclosure is the most concrete safety-relevant fact in this source and is not mentioned anywhere in the GA announcement post itself — it only surfaces in the linked reference docs. Because `OnlineEvaluator` runs under a shared project-level service account (not a per-user identity), any user who can create one can attach continuous evaluation — and by implication, whatever access that service account carries — to *any* agent in the project, not just their own. This is a concrete access-control requirement (restrict `OnlineEvaluator` creation to admins) that teams adopting this feature need to apply explicitly; it is not a safe default.

### Claim 18: Online monitoring requires the agent to emit specific OpenTelemetry semantic-convention attributes (`gen_ai.agent.name`, `gen_ai.conversation.id`, `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.tool.definitions`), and ADK agents must opt in via two environment variables to emit them
- **Evidence**: Listed under "Telemetry requirements" on the "Continuous evaluation with online monitors" docs sub-page.
- **Confidence**: settled (a specific, documented technical requirement for a shipped feature)
- **Quote**: "Online monitoring requires your agent to export specific OpenTelemetry signals to provide the necessary context for evaluation... If you are using the Agent Development Kit, you must enable these telemetry capabilities by setting the following environment variables: OTEL_SEMCONV_STABILITY_OPT_IN='gen_ai_latest_experimental' OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT='EVENT_ONLY'"
- **Our assessment**: This confirms that online evaluation is not a passive, zero-instrumentation feature — it depends on a specific (and, per the flag name, still-experimental) OpenTelemetry GenAI semantic-convention profile, and ADK does not emit the required message-content events by default. Teams building agents on other frameworks would need to independently confirm they emit the same `gen_ai.*` attribute set before online monitors can score their traffic.

## Concrete Artifacts

### Metric Registry: three metric types (from linked docs sub-page, "Manage evaluation metrics")
```
Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/manage-metrics

Predefined Metrics: Managed metrics provided by Google, including multi-turn
  raters for task success, tool use quality, and trajectory compliance.
Custom LLM Metrics: Natural language rubrics where a "Judge LLM" evaluates
  an agent's response based on your specific criteria and rating scales.
Custom Code Metrics: Python functions that programmatically validate agent
  behavior, such as checking for a specific output format or verifying a
  tool response.
```

### Single-turn vs. multi-turn predefined metrics, with adaptive/static type per metric (verbatim table content, same doc)
```
Single-turn:
  Agent Final Response Quality  | Adaptive rubric | "Comprehensive evaluation
    that auto-generates rubric criteria based on the agent's configuration
    (system instructions and tool declarations) and the user's prompt."
  Agent Hallucination            | Static rubric   | "Checks factuality by
    segmenting the response into atomic claims and verifying each claim is
    grounded in the tool usage from intermediate events."
  Agent Tool Use Quality         | Adaptive rubric | "Evaluates the selection
    of appropriate tools, correct parameter usage, and adherence to the
    specified sequence of operations."
  Safety                         | Static rubric   | "Assesses whether the
    response violates safety policies, including PII and demographic data,
    hate speech, dangerous content, harassment, or sexually explicit
    content. Returns 1 for safe and 0 for unsafe."

Multi-turn:
  Agent Multi-turn Task Success       | Adaptive rubric | "Evaluates whether
    the agent successfully achieved the goal or goals of the conversation.
    This reference-free metric focuses on whether the goal was achieved,
    not how it was achieved."
  Agent Multi-turn Tool Use Quality   | Adaptive rubric | "Evaluates the
    quality of function calls made during a multi-turn conversation.
    Assesses whether the agent called the right tools with correct
    arguments at the right time."
  Agent Multi-turn Trajectory Quality | Adaptive rubric | "Evaluates the
    overall trajectory (path) of the conversation. Unlike Task Success,
    this metric assesses how the agent achieved the goal—whether the
    reasoning path was logical and efficient."
```

### The Quality Flywheel skill: five-stage loop (from linked companion post, "Driving the Agent Quality Flywheel from Your Coding Agent," 2026-06-30)
```
Source: https://developers.googleblog.com/driving-the-agent-quality-flywheel-from-your-coding-agent/

Prepare Data:      build an eval dataset from existing OTel traces,
                   hand-crafted cases, or synthesized scenarios
Run Inference:     execute the agent over the dataset to produce traces
                   (skipped if traces already exist, e.g. production)
Grade:             score traces with adaptive AutoRaters or custom metrics
                   — "This is the only stage that always runs."
Analyze Failures:  read rubric verdicts to understand why a case failed;
                   for 10+ failures, cluster with Automatic Loss Analysis
Optimize & Iterate: apply a targeted fix, re-run stages 2-4, compare
                   against the previous baseline

Install (two packages, same underlying GenAI evaluation service):
  npx skills add https://github.com/google/agents-cli --skill google-agents-cli-eval
  npx skills add https://github.com/google/skills --skill agent-platform-eval-flywheel
```

### `travel-concierge` worked example: one rater's actual verdict on one failing case (verbatim, companion post)
```
Source: same companion post, "One case, three raters: party_size_02" section

revision_honored (custom rubric)        -> IGNORED
  "The agent acknowledged the request but re-offered the earlier results
  instead of searching the revised criteria, and never memorized the new
  preference."

multi_turn_task_success (built-in, adaptive) -> 0.80
  Five generated criteria, four passed. Fifth failed:
  "provides dorm room options at 'Hostel World Amsterdam'":
  "the agent failed to provide the specific information requested ...
  because it claimed a lack of tool capability."

multi_turn_trajectory_quality (built-in, adaptive) -> 0.67
  Miss attributed to an eval-config artifact (tool schemas not surfaced
  to the rater), not a real agent defect.
```

### Online monitor operational loop and telemetry contract (verbatim, from linked docs sub-page, "Continuous evaluation with online monitors")
```
Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-online

Scheduled loop, "typically every 10 minutes":
  Query    -> samples data from Cloud Trace and Cloud Logging per filters
  Evaluate -> runs configured metrics via the Evaluation Service
  Report   -> writes results to Cloud Logging, exports scores to Cloud
              Monitoring

Required OTel attributes on the invoke-agent span:
  gen_ai.agent.name, gen_ai.agent.description, gen_ai.conversation.id
Required OTel inference-event fields:
  gen_ai.input.messages, gen_ai.output.messages,
  gen_ai.system_instructions, gen_ai.tool.definitions

ADK opt-in (not on by default):
  OTEL_SEMCONV_STABILITY_OPT_IN='gen_ai_latest_experimental'
  OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT='EVENT_ONLY'

Security Disclosure (verbatim):
  "Online evaluation relies on the project-level service account (P4SA).
  Any user with permissions to create an `OnlineEvaluator` can attach it
  to any agent within the same project. To avoid potential privilege
  escalation, ensure that `OnlineEvaluator` creation is restricted to
  authorized administrators."
```

## Cross-References

- **Corroborates** `docs-ghaw-measuring-impact.md` Claim 13 ("Do not
  overreact to single numbers. Trend data is usually more useful. Look
  for cost per successful run moving down, useful output rate and
  acceptance moving up, retries dropping, and system overlap
  decreasing"): this source's Claim 14 ("treat the scores as a strong
  directional signal, and trust the deltas between runs more than any
  single number as an absolute grade") is the same principle —
  distrust absolute single-run scores, trust trend/delta — independently
  reached by two different platform teams (GitHub Agentic Workflows and
  Google Agent Platform) for two different kinds of metric (workflow
  cost/outcome metrics vs. LLM-judge quality scores).
- **Corroborates** `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 5 (persona-based multi-turn simulation as a distinct evaluation
  layer with dedicated tooling — Snowglobe, Collinear, Rhesis named) and
  Claim 7 (operational observability as "the production safety net...
  bridging the gap between pre-deployment testing and real user
  behavior"): this source's user/environment simulators (Claim 4) and
  online monitors (Claim 5, Claim 17) are a concrete, named
  implementation of exactly those two layers from a different vendor
  (Google rather than the Snowglobe/Collinear/Rhesis and
  LangSmith/Langfuse/Helicone tools that source names). Read together,
  the Thoughtworks post's three-layer taxonomy (persona / unit /
  observability) generalizes across at least two independent platforms'
  concrete tooling, which raises confidence in the taxonomy itself even
  though neither vendor's specific tools were named by the other.
- **Contradicts**: None found, but this source sits in productive tension
  with `blog-langchain-better-harness-evals.md` Claim 6 ("agents are
  famous cheaters" — holdout sets are the structural check against an
  autonomous optimizer overfitting to visible evals) without disagreeing
  with it. This source's Claim 12 (optimizer/evaluator role decoupling —
  "whatever proposes a fix... never grades it") addresses the same
  underlying risk (an autonomous improvement loop gaming its own success
  metric) via a different structural mechanism: separating *who proposes*
  from *who grades*, rather than LangChain's *visible-set vs. holdout-set*
  split. Both are legitimate, non-conflicting mitigations for the same
  failure mode, and a guide section on autonomous harness improvement
  should probably recommend both together (decoupled roles *and* holdout
  validation) rather than treating them as alternatives. Not filed as a
  contradiction per MINER.md §4a — this is a conditioning/complementary
  relationship, not a disagreement about what works.
- **Extends** `blog-google-jules-insight-policy-eval.md`: that note
  documents Google/Jules's separate "insight policy" evaluation construct
  for *proactive* agents (grading whether an agent decided correctly
  whether to notify, question, draft, or stay silent), built on a
  bug-history-clustering ground-truth methodology and reporting Hit@K
  metrics from an internal 705-bug study. This source's adaptive rubrics
  and AutoRaters are a general-purpose evaluation *service* (Task
  Success, Tool Use Quality, Trajectory Quality, Safety, Hallucination)
  productized for any Agent Platform agent, not specific to proactive/
  diagnostic agents. The two sources describe complementary Google
  evaluation efforts: one is a published research methodology for a
  specific agent-behavior class (Jules/insight policy), the other is the
  shipped, general GA product (this source) — it is plausible, though not
  stated in either post, that a Jules-style insight-policy grader could be
  registered as a Custom LLM Metric (Claim 9 above) within this GA
  service, but neither source makes that connection explicitly.
- **Extends** `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`
  Claim 9 (single-trial evaluation designs overstate effect deltas by
  40-60% versus averaging at least three repeated trials): this source's
  AutoRaters "majority-vote across samples" (Claim 14) is a related but
  distinct mitigation for judge noise specifically — sampling the judge
  multiple times and voting, rather than Sourcegraph's practice of
  re-running the *task* itself multiple times and averaging. A rigorous
  eval setup arguably needs both: repeated task execution (controls for
  agent non-determinism) and repeated/majority-vote judging (controls for
  judge non-determinism), and neither source's practice alone covers the
  other's failure mode.
- **Novel**:
  - The Quality Flywheel skill explicitly naming **Claude Code** as a
    supported driver (Claim 12) is new to the corpus — no existing
    source note documents a Google-built, Anthropic-model-compatible
    evaluation skill installable into a coding agent's own workflow.
  - The optimizer/evaluator architectural decoupling principle ("whatever
    proposes a fix... never grades it," Claim 12) as an explicit,
    named anti-gaming safeguard is new — distinct from the holdout-set
    mechanism already in the corpus (see Contradicts/tension above).
  - The adaptive-vs-static rubric type distinction, cross-confirmed
    against the docs page (Claim 9, Concrete Artifacts), is new: no
    existing source note documents which specific evaluation dimensions
    a major vendor considers appropriate for per-case adaptive grading
    (goal achievement, tool use, trajectory) versus a fixed bar (safety
    policy compliance, factuality-against-tool-output).
  - The `OnlineEvaluator` privilege-escalation security disclosure
    (Claim 17) is new — no existing source note documents an access-
    control risk specific to agent-evaluation infrastructure itself
    (as opposed to the agent being evaluated).
  - Explicit confirmation that server-side custom-metric judge models
    include "all Gemini and Anthropic models" (Claim 10) is new — the
    corpus did not previously have a citation for Anthropic models being
    a supported judge-model choice in a major cloud vendor's evaluation
    service.
  - The environment simulator's ability to inject a specific failure mode
    (a forced error or added latency on a named tool) into an eval run
    without a real failing dependency (Claim 4) is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the Quality Flywheel skill
  (Claim 12, Claim 13) as a concrete example of an installable,
  Claude-Code-compatible evaluation-and-fix loop, alongside the existing
  Better-Harness (`blog-langchain-better-harness-evals.md`) content on
  autonomous harness hill-climbing. Specifically recommend citing the
  optimizer/evaluator decoupling principle (Claim 12) as a second,
  complementary anti-gaming safeguard to Better-Harness's holdout-set
  approach — a guide section on autonomous harness improvement should
  name both mechanisms rather than treating them as alternatives.
- **Chapter 03 (Verification)**: Add adaptive rubrics (Claims 3, 8, 9) as
  a named alternative to fixed LLM-as-judge prompts, with the
  adaptive-vs-static metric type distinction (Claim 9, Concrete
  Artifacts) as a concrete decision framework: use adaptive rubrics for
  case-varying quality dimensions (goal achievement, tool use,
  trajectory), and static/deterministic checks for fixed-bar dimensions
  (safety policy compliance, factuality). Add the "promote a diluted
  concern to its own categorical metric" pattern (Claim 15) as a concrete
  technique for when an adaptive/blended metric detects but doesn't
  reliably track a specific known failure mode.
- **Chapter 03 (Verification)**: Add "trust deltas over absolute scores"
  (Claim 14) to the trend-vs-single-number guidance already sourced from
  `docs-ghaw-measuring-impact.md` Claim 13 — this source is a second,
  independent vendor making the identical recommendation for LLM-judge
  scores specifically, strengthening the case for treating this as
  general practitioner consensus rather than one platform's idiosyncratic
  advice.
- **Chapter 06 (Security & Threat Model)**: Add the `OnlineEvaluator`
  privilege-escalation disclosure (Claim 17) as a concrete example of a
  security consideration specific to agent-evaluation infrastructure:
  when evaluation/monitoring tooling runs under a shared service account
  rather than per-user identity, restrict who can attach it to agents,
  since doing so can grant de facto access beyond the creator's own
  agents.
- **Chapter 01 (Daily Workflows)**: Note the two worked examples (Claims
  15-16) as illustrations of a recurring failure class worth naming:
  agents that perform the underlying task correctly but fail purely in
  what they communicate about it (a stale value restated in the final
  message; a silently-dropped disclosure instruction) — task-completion
  metrics alone would miss both, which is itself an argument for
  evaluating communication/response-quality as a distinct dimension from
  task success.

## Extraction Notes

- This note follows MINER.md §1's "follow up to 5 linked pages" guidance:
  from the GA post's ~20 outbound links, three were fetched and read in
  full — the companion post "Driving the Agent Quality Flywheel from Your
  Coding Agent" (chosen because it directly names Claude Code and
  contains the only concrete worked examples in either post), the
  "Manage evaluation metrics" docs page (chosen to resolve the
  adaptive-vs-static rubric type distinction the GA post gestures at but
  doesn't fully specify), and the "Continuous evaluation with online
  monitors" docs page (chosen to get the operational mechanics and
  security disclosure behind the GA post's "drift alerts" claim). Not
  fetched: the "regions and security features table," the ADK evaluation
  docs, the Agent Platform SDK tutorial pages, the "Evaluate agents with
  the GenAI Client" tutorial, the `view-results`/issue-clustering docs
  page, and the arXiv-adjacent Cloud Next '26 talk referenced in the
  companion post — these are flagged as natural follow-up sources if a
  future Miner wants deeper coverage of the ADK-native evaluation path or
  the full loss-analysis taxonomy.
- Both the main blog HTML and all three linked pages were fetched via
  direct `curl` (not the WebFetch tool's summarizing pass) and converted
  to plain text with a tag-stripping script, then read in full before any
  quote was selected, per MINER.md §2a. Every `Quote` field above was
  copied character-for-character from that extracted text; none were
  reconstructed or paraphrased into quote form.
- No sub-pages were paywalled or inaccessible; all four pages (main post
  + three linked pages) returned HTTP 200 and were read in full.
- Two duplicate Prospector triage comments were posted on the source
  issue (near-identical content, differing only in exact chapter
  numbering and wording) — both point at evaluation/measurement content
  and were treated as a single triage signal for this extraction.
- No contradictions requiring a filed issue were identified. The
  optimizer/evaluator-decoupling vs. holdout-set tension noted under
  Cross-References → Contradicts is a complementary-mechanisms
  relationship, not a disagreement about what works or a claim that one
  approach is correct where another is wrong, so no contradiction issue
  was filed per MINER.md §4a's "conditioning variable, not a
  contradiction" guidance.
