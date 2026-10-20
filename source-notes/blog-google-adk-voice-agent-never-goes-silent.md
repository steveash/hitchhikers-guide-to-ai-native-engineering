---
source_url: https://developers.googleblog.com/step-by-step-guide-build-a-voice-agent-that-never-goes-silent-using-adk/
source_type: blog-post
title: "Step by Step guide: Build a Voice Agent That Never Goes Silent using ADK"
author: Stephen Allen (Solutions Architect, AI Apps and Platforms) and Kaz Sato (Staff Developer Advocate), Google
date_published: 2026-10-19
date_extracted: 2026-10-20
last_checked: 2026-10-20
status: current
confidence_overall: emerging
issue: "#4229"
---

# Step by Step guide: Build a Voice Agent That Never Goes Silent using ADK

> Google's first-party tutorial on non-blocking tool calls in live voice sessions: turning a tool's `return` into `yield` (streaming tools), or setting `response_scheduling` (`WHEN_IDLE` / `INTERRUPT` / `SILENT`), so a slow tool no longer blocks the model's turn, plus production cautions (single-flight, `stop_streaming`, barge-in does not cancel tools).

## Source Context

- **Type**: blog-post (Google Developers Blog, first-party how-to with code, published Oct. 19, 2026)
- **Author credibility**: A Google Solutions Architect and a Staff Developer Advocate writing about Google's own framework (ADK) and model (`gemini-3.8-live`). Authoritative on API mechanics; the performance claim is vendor-reported.
- **Scope**: ADK `run_live` bidirectional sessions only: streaming tools, background execution, scheduling of tool results. Does not cover evaluation, non-live (text) agents, or non-Google stacks. Model ID and ADK version numbers (2.8, 2.10) were not verified against release notes.

## Extracted Claims

### Claim 1: In a live voice session a blocking tool produces dead air, and prompting cannot fix it because the model turn is blocked on the function response
- **Evidence**: Explanation of the `run_live` execution loop plus a baseline `async def` tool with a single `return`; an architectural argument, no measurement of the baseline beyond the benchmark in Claim 2.
- **Confidence**: emerging
- **Quote**: "Prompting instructions such as \"tell the user you are working on it\" cannot resolve this, because the model's turn is blocked waiting for the function response payload."
- **Our assessment**: Plausible and important: the failure is in harness control flow, not instructions. It generalizes beyond ADK to any loop that awaits tool results before the next model turn. Mechanism is asserted, not demonstrated.

### Claim 2: Switching from a blocking to a streaming tool cut time to the agent's first words from 14.4 s to 1.2 s
- **Evidence**: Self-reported benchmark on one sales-report workflow on `gemini-3.8-live`; no methodology, run count, or variance published.
- **Confidence**: anecdotal
- **Quote**: "In our benchmark sales-report workflow on gemini-3.8-live, switching from a blocking tool to a streaming tool cut the time to the agent's first words from 14.4 seconds to 1.2 seconds."
- **Our assessment**: Directionally believable (an immediate acknowledgement vs. waiting ~13 s) but it is a single vendor-run workflow; cite only as illustrative. The post itself notes that backend time is unchanged.

### Claim 3: A streaming tool needs only `return` changed to `yield`; ADK then marks the declaration `NON_BLOCKING` and sends an immediate acknowledgement
- **Evidence**: Code example (full sales-analyst agent) in the post.
- **Confidence**: emerging
- **Quote**: "In ADK, turning a standard tool into a streaming tool requires changing only return to yield. By defining the function as an AsyncGenerator, ADK automatically marks the tool declaration as NON_BLOCKING and returns an immediate status acknowledgement to the model."
- **Our assessment**: A low-friction API design: the sync/async shape of the tool function is the control signal. Not independently verified against ADK source.

### Claim 4: Each `yield` is a partial function response that the model paraphrases, but narration can lag the tool by several seconds, and the user can ask unrelated questions meanwhile
- **Evidence**: Description of behavior in the "How It Works in Practice" section; no trace shown.
- **Confidence**: anecdotal
- **Quote**: "Each yield sends a partial function response upstream. The model paraphrases each update as it arrives (\"Connecting to the warehouse...\", \"Aggregating product line data...\"), though narration can trail the tool by several seconds."
- **Our assessment**: The candid latency caveat is useful: streamed progress is delivered through the model, so it is not real-time. The progress text is also model-context content, which has a token and attention cost.

### Claim 5: Streaming tools are not single-flight by default; the model may re-invoke them, so use a "Call this ONCE" directive and an in-memory latch or idempotency key
- **Evidence**: Production-considerations list; no failure rate given.
- **Confidence**: emerging
- **Quote**: "Because streaming tools push updates across multiple turns, models may occasionally attempt to call the tool again if prompted repeatedly."
- **Our assessment**: A real hazard of any async tool that outlives a turn. The docstring directive is a prompt-level mitigation; the latch/idempotency key is the real fix, and the post only "consider[s]" it. Echoes classic idempotency practice for agent tools.

### Claim 6: Cancellation is by model-callable `stop_streaming(function_name)`, which cancels the underlying `asyncio.Task` and raises `CancelledError` for cleanup
- **Evidence**: API description in the post; no code sample for the cleanup path.
- **Confidence**: emerging
- **Quote**: "ADK intercepts the call and cancels the generator's underlying asyncio.Task, raising asyncio.CancelledError within your function so you can cleanly close database connections or file handles."
- **Our assessment**: Cancellation is a tool the model must choose to call, not a harness-level reaction to user speech; this gives resource cleanup a defined hook but depends on model judgment.

### Claim 7: User barge-in does not cancel running tools; their results are still delivered
- **Evidence**: Stated behavior of ADK/Live API (`interrupted=True` event stops audio playback only).
- **Confidence**: emerging
- **Quote**: "Running streaming or background tools are not cancelled, and their results are still delivered."
- **Our assessment**: Counter-intuitive safety-relevant semantics: interrupting speech is a UI event, not a task cancel. Side-effecting tools (writes, payments) in voice agents need explicit cancel handling.

### Claim 8: Two patterns: stream when "the wait has a story"; otherwise run quietly in the background and let the result land when idle
- **Evidence**: Design rule of thumb; reasoning that continuous commentary can feel intrusive if the user pivots.
- **Confidence**: emerging
- **Quote**: "The rule of thumb: If the wait has a story, stream it. If the wait is just a wait, run it in the background and let the result land when idle."
- **Our assessment**: A usable decision heuristic, UX-based rather than empirically tested.

### Claim 9: A single-yield async generator is the fastest route to immediate acknowledgement without progress chatter
- **Evidence**: Code example (`yield report` once upon completion).
- **Confidence**: emerging
- **Quote**: "Because this is an async generator, ADK issues an immediate pending response."
- **Our assessment**: Neat trick: uses the streaming machinery solely for its acknowledgement side effect.

### Claim 10: A `FunctionTool` with `response_scheduling` and a return-once coroutine gives no payload until the function finishes, so the model typically does not acknowledge first
- **Evidence**: Trade-off explanation; ADK 2.10+ also offers `behavior = types.Behavior.NON_BLOCKING`.
- **Confidence**: emerging
- **Quote**: "When using response_scheduling with a return-once coroutine, the model receives no payload until the entire function completes."
- **Our assessment**: Clarifies that delivery timing and acknowledgement are separate concerns; choose this when the user is expected to keep talking.

### Claim 11: `response_scheduling` has three modes controlling when a tool result enters the conversation: `WHEN_IDLE` waits for a pause, `INTERRUPT` cuts in, `SILENT` adds to history without announcing
- **Evidence**: Benchmark sessions on `gemini-3.8-live` described qualitatively (WHEN_IDLE waited out a 20-second answer; INTERRUPT cut off speech mid-sentence; SILENT added the result to history). The mode table from the original page was not captured in extraction.
- **Confidence**: emerging
- **Quote**: "Under SILENT, the result was added to the conversation history, available for subsequent turns without prompting an unrequested announcement."
- **Our assessment**: An explicit context-engineering knob: when tool output enters the model's context and whether it triggers a turn. Observations are demo-grade, not a systematic test.

### Claim 12: Execution shape and delivery timing are independent and composable; from ADK 2.8, a streaming tool can set scheduling per update by yielding `types.FunctionResponse`
- **Evidence**: Code example yielding a `SILENT` progress update then a `WHEN_IDLE` final result.
- **Confidence**: emerging
- **Quote**: "Execution shape (streaming vs. single-return) and delivery timing (response_scheduling) are independent and can be composed."
- **Our assessment**: Lets a tool update context quietly during work and speak only for the result. Version numbers come from the post.

### Claim 13: Non-blocking tools change conversational presence, not backend latency
- **Evidence**: Authors' framing in the conclusion.
- **Confidence**: settled
- **Quote**: "Non-blocking tools do not reduce backend execution time: a 13-second query still takes 13 seconds."
- **Our assessment**: Honest and correct; perceived latency is a harness/UX property distinct from compute latency.

## Concrete Artifacts

Streaming tool (from the post, "Pattern 1"):

```python
async def query_sales_database(region: str) -> AsyncGenerator[str, None]:
    """Runs the quarterly sales report. Call this ONCE; it pushes updates automatically.
    ...
    """
    stages = [
        ("Connecting to the sales warehouse...", 1.5),
        ("Scanning order records...", 3.5),
        ("Aggregating revenue by product line...", 3.5),
        ("Formatting the report...", 1.5),
    ]
    for message, delay in stages:
        yield f"PROGRESS: {message}"
        await asyncio.sleep(delay)
    yield f"DONE: {region} Q2 revenue reached $4.81M, up 12.4% year over year."
```

Scheduling on a plain coroutine (post, "Approach B"):

```python
sales_tool = FunctionTool(query_sales_database)
sales_tool.response_scheduling = types.FunctionResponseScheduling.WHEN_IDLE
# ADK 2.10+: sales_tool.behavior = types.Behavior.NON_BLOCKING
```

Per-update scheduling (post, ADK 2.8+):

```python
yield types.FunctionResponse(
    response={"stage": "aggregating"},
    scheduling=types.FunctionResponseScheduling.SILENT,
)
yield types.FunctionResponse(
    response={"report": final_data},
    scheduling=types.FunctionResponseScheduling.WHEN_IDLE,
)
```

Requirements (post): `google-adk >= 2.10.0`, model `gemini-3.8-live` on Gemini Enterprise, bidirectional `run_live` sessions.

## Cross-References

- **Corroborates**: `blog-simonwillison-gptlive-voice-delegation.md` Claim 1: GPT-Live also keeps conversing while slow work runs in the background and merges the result later. Same architectural idea (decouple slow work from the conversational turn) in a different vendor stack.
- **Contradicts**: none found.
- **Extends**: `blog-google-adk-live-voice-agent-evaluation.md` (same ADK live-voice toolkit; that note covers evaluation, this one covers runtime tool execution and scheduling, no claim overlap). `blog-google-adk-recipes-three-layers.md` is a related ADK note without claim overlap.
- **Novel**: Non-blocking/streaming tool semantics in a live session; the `response_scheduling` trio as a control over when tool output enters context; barge-in not cancelling tools; model-callable `stop_streaming`.

## Guide Impact

- **Chapter 02 (harness engineering)**: Add a short section on tool-call blocking semantics in real-time loops: a tool that is awaited before the next model turn cannot be fixed by prompting (Claim 1); async/streaming tools plus single-flight/idempotency guards (Claim 5) and explicit cancellation semantics (Claims 6-7). Cite as vendor-documented, ADK-specific.
- **Chapter 04 (context engineering)**: Use `response_scheduling` (Claim 11) as a concrete example of controlling when tool results enter context (wait / interrupt / silent append).
- **Chapter 05**: Optional mention under voice agents; the 14.4 s -> 1.2 s figure must be attributed as a single-workflow vendor benchmark.

## Extraction Notes

- Fetched the full page via curl and read it end to end. The page's scheduling-mode table and architecture-summary table did not survive HTML-to-text conversion; Claim 11 relies on the surrounding prose.
- Linked reference pages (Streaming Tools, Live API Toolkit, Function tools docs) were not followed.
- Model ID `gemini-3.8-live` and ADK version numbers (2.8, 2.10) are taken from the post and not verified against release notes.
