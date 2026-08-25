---
source_url: https://developers.googleblog.com/how-to-evaluate-live-voice-agents-in-adk/
source_type: blog-post
title: "How to Evaluate Live & Voice Agents in ADK"
author: Stephen Allen (Solutions Architect, AI Apps and Platforms, Google)
date_published: 2026-08-24
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: emerging
issue: "#2939"
---

# How to Evaluate Live & Voice Agents in ADK

> Google's first-party implementation guide for testing voice-based ADK
> agents: native audio-based user simulation, two decoupled test-case
> formats (persona-driven scenarios and scripted fixed conversations),
> rubric-based LLM judges scoring whole multi-turn trajectories, and a
> CI/CD-callable eval pipeline with a playable-audio-transcript debugging
> UI — all inside the same eval loop ADK already runs for text agents.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party
  technical how-to, published August 24, 2026)
- **Author credibility**: Stephen Allen, Solutions Architect on Google's AI
  Apps and Platforms team, writing on Google's own developer blog about a
  Google-authored framework (ADK). This is first-party vendor guidance
  walking through a feature Google itself built and ships in ADK — the code
  samples (agent definitions, eval-set JSON, `test_config.json`, the CLI
  invocation) describe the actual shipped API surface, not a third-party
  integration. No independent production deployment, benchmark, or
  adversarial test of the feature is reported in this post; it is a
  step-by-step "how it works" guide, not a case study with outcome metrics.
- **Scope**: Covers building a three-agent live voice workflow, authoring
  an eval set with two test-case formats, turning on live/audio mode via
  config, the rubric-based LLM-judge evaluation model, running evals from
  the CLI and programmatically, and reviewing results in ADK Web's
  transcript-with-audio UI. Does **not** cover: pricing, judge-model
  calibration methodology, false-positive/false-negative rates for the
  rubric judge, latency or cost of running live evals at scale, multi-agent
  eval sets beyond the one three-node example, or how personas are
  authored beyond naming `NOVICE` as one built-in example.

## Extracted Claims

### Claim 1: Production live-agent reliability requires repeatable evidence across real conversations because agent behavior can silently degrade — tools stop firing, context slips between turns, interjections go ignored — after a prompt tweak or model iteration that looked fine in a demo
- **Evidence**: Opening problem statement framing the motivation for the whole feature.
- **Confidence**: settled (a specific, named failure-symptom list, not a generic "agents are unreliable" claim)
- **Quote**: "Behavior that sounded perfect yesterday can quietly change on the next prompt tweak or model iteration. Tools stop firing. Context slips between turns. Interjections go ignored."
- **Our assessment**: This is a concrete three-symptom diagnosis (tool-calling regressions, context loss across turns, unhandled interjections) specific to *live, spoken* multi-turn agents — distinct from the corpus's existing text-agent failure taxonomies. It motivates why a demo is insufficient evidence for live agents specifically: none of these three symptoms is reliably visible from a single scripted walkthrough.

### Claim 2: ADK now supports driving a live, voice-based agent with a simulated user that speaks its turns as synthesized audio, scoring the spoken replies inside the same eval loop already used for text agents
- **Evidence**: First-party feature announcement.
- **Confidence**: settled (direct vendor description of a shipped capability, corroborated by the runnable code and config samples that follow)
- **Quote**: "You can now drive a live, voice-based agent with a simulated user that speaks its turns as audio, score the spoken replies, and do it all inside the same eval loop you already run for text agents."
- **Our assessment**: The key structural claim is "the same eval loop" — this is not a separate voice-testing product bolted alongside ADK's existing text-agent evals, but a mode switch on the identical eval-set/eval-runner pipeline (see Claim 6). That unification is what makes the feature practically adoptable: a team with an existing ADK eval suite does not need new tooling to add voice coverage.

### Claim 3: The example agent under test is a graph-based Workflow of three sequential single-purpose live agents (greeter, date-of-birth verifier, goals/appointment agent) all running on `gemini-live-2.5-flash-native-audio`, with the audio stream and accumulated session state carried forward across handoffs so the user never notices a transition
- **Evidence**: A full runnable Python code sample defining three `Agent` objects and a `Workflow` connecting them with `START`/edges.
- **Confidence**: settled (directly falsifiable code artifact)
- **Quote**: "As control moves between agents, the user never notices a handoff. The audio stream stays open across the entire interaction, and ADK carries the accumulated session state and conversation history forward so each agent picks up in context rather than starting cold."
- **Our assessment**: This reuses the exact `Workflow`/`START`/edges graph-orchestration API documented in `blog-google-adk-2-0-deterministic-workflows.md`, applied here to a live-audio pipeline rather than a text refund-processing pipeline — direct evidence that ADK's deterministic-workflow orchestration generalizes across text and voice agent types without a different graph API.

### Claim 4: ADK eval sets support two decoupled test-case formats — conversation scenarios, where a developer states a goal and persona and a simulator improvises the turns, and fixed conversations, where the user's turns are scripted verbatim in advance
- **Evidence**: Explicit statement plus two JSON eval-case examples, one of each format.
- **Confidence**: settled (directly falsifiable JSON config artifacts)
- **Quote**: "Test cases are decoupled from how they run, so you can mix two distinct styles: conversation scenarios and fixed conversations."
- **Our assessment**: This is a reusable test-authoring duality: persona-driven scenarios give broad, improvised coverage for exploratory testing of how well an agent handles an underspecified conversation, while fixed conversations give an exact, reproducible regression case. A team can mix both in one eval set rather than choosing one authoring style for the whole suite.

### Claim 5: The built-in `NOVICE` persona is prompt-driven (not hardcoded) and shapes the simulated user to share only high-level goals and wait for the agent to ask for specifics, deliberately testing the agent's ability to drive the conversation rather than the user volunteering information
- **Evidence**: Description of the `user_persona` field's effect, paired with the conversation-scenario JSON sample that sets `"user_persona": "NOVICE"`.
- **Confidence**: settled (a specific, falsifiable description of a shipped built-in persona's behavior)
- **Quote**: "NOVICE tells the simulator to share only high-level goals and wait for the agent to ask for specifics, testing how well the agent drives the conversation. Personas are prompt-driven rather than hardcoded, so you can extend the set with your own personas."
- **Our assessment**: This is a more specific instance of persona-based multi-turn simulation than the corpus's existing coverage: `blog-thoughtworks-anand-agent-evaluation-framework.md` (Claim 5) names persona-based testing as a distinct evaluation layer using third-party tools (Snowglobe, Collinear, Rhesis) without detailing how any specific persona shapes simulated behavior. This source is concrete about the mechanism — `NOVICE` is not just a label but a design that withholds information to stress-test the agent's own information-gathering behavior, and the persona set is extensible because personas are themselves prompts, not code.

### Claim 6: Dynamic conversation scenarios end on their own once the stated `conversation_plan` is satisfied, with `max_allowed_invocations` acting as a hard safety cap on the total number of turns for any given case
- **Evidence**: Direct statement of the termination and safety-bound mechanism for scenario-style test cases.
- **Confidence**: settled (directly falsifiable config field described alongside the JSON sample that sets no explicit invocation cap in the scenario example, but sets `"max_allowed_invocations": 10` in the later `test_config.json` sample)
- **Quote**: "The simulator ends a scenario on its own once the conversation_plan is satisfied, so you script the goal and let it decide when the call is finished. As a safeguard against run-off conversations, max_allowed_invocations caps the total number of turns, giving every dynamic case a predictable upper bound."
- **Our assessment**: This is the same "bounded retry/timeout" design instinct the corpus already sees applied to autonomous agent loops generally (bounding an open-ended process with a hard numeric ceiling) — here applied specifically to a *simulated user's* turn count in an eval, not to the agent-under-test's own tool-call loop. Without this cap, a persona/goal-driven scenario has no other structural guarantee of terminating.

### Claim 7: Turning on live, audio-based execution for an eval set is a config-only change — adding `live_model_config` and an `llm_audio` user-simulator config to `test_config.json` — and omitting that config runs the identical test cases in standard text mode
- **Evidence**: The `test_config.json` code sample plus an explicit statement of what happens without it.
- **Confidence**: settled (directly falsifiable config artifact)
- **Quote**: "live_model_config enables live mode. Omitting this runs the exact same test cases in standard text mode."
- **Our assessment**: This is the concrete mechanism behind Claim 2's "same eval loop" claim — the eval-set JSON itself (the scenarios and fixed conversations from Claim 4) does not change between text and voice execution; only the runner config does. A team's existing text-agent eval set becomes a voice-agent eval set by adding a config block, not by rewriting test cases.

### Claim 8: The user-simulator config separates the simulated user's turn-taking/conversational logic (`model`) from the model that synthesizes those turns into speech (`audio_model`), so voice and language can be varied independently of the simulated user's conversational behavior
- **Evidence**: Explicit config-field explanation alongside the `test_config.json` sample, which sets `"model": "gemini-3.7-flash"` and `"audio_model": "gemini-3.1-flash-tts-preview"` with a `voice_name`/`language_code` block.
- **Confidence**: settled (directly falsifiable config artifact)
- **Quote**: "model powers the simulated user's turn-taking logic, while audio_model synthesizes those turns into speech. Adjust voice_name and language_code to test agent performance against different voices and accents."
- **Our assessment**: This split lets a team test the same conversational logic (same simulated-user reasoning model) against many different synthesized voices/accents/languages without re-authoring the eval cases — a specific, reusable pattern for testing an agent's robustness to speech-recognition variation independent of conversational content.

### Claim 9: Evaluation criteria combine rubric-based LLM judges that score an entire multi-turn trajectory against natural-language criteria and a configurable pass/fail threshold, with optional per-turn metrics for scoring individual responses or tool executions
- **Evidence**: The `criteria` block of the `test_config.json` sample (`rubric_based_multi_turn_trajectory_quality_v1`, a `threshold: 0.7`, a named `judge_model`, and a `rubrics` list with natural-language `text_property` rubric content) plus explanatory text.
- **Confidence**: settled (directly falsifiable config artifact)
- **Quote**: "criteria configures metrics and pass/fail thresholds. Rubric-based LLM judges (like trajectory quality) evaluate the conversation end to end—ideal for multi-agent graphs. You can also attach per-turn metrics to score individual responses or tool executions."
- **Our assessment**: This is a whole-trajectory analogue to the corpus's existing "conversation as a unit" evaluation granularity from `blog-thoughtworks-anand-agent-evaluation-framework.md` (Claim 6), and a concrete, code-level instance of "LLM-as-judge" more specific than the corpus's existing single-turn satisfaction-classification example (`blog-cursor-continual-harness-improvement.md`, cited in `guide/03-verification.md` ~line 1089) — here the judge scores an entire multi-agent, multi-turn conversation against an explicit rubric with a named threshold and judge model, not a single follow-up-message classification.

### Claim 10: Natural-language rubrics are used instead of rigid pattern matching because a correct spoken reply can be phrased in hundreds of different ways, so the rubric captures the intent once and is applied automatically across every conversation in the suite
- **Evidence**: Direct rationale statement for the rubric-based judging approach.
- **Confidence**: emerging (a plausible, mechanism-consistent design rationale, but not independently tested against a rigid-pattern-matching baseline in this source — no false-positive/false-negative rate or judge-model agreement-with-human-reviewer figure is given)
- **Quote**: "A spoken reply can be correct in hundreds of different phrasings. Natural-language rubrics judge intent the way a human reviewer would, captured once and applied automatically across every conversation in your suite."
- **Our assessment**: This names the specific reason rigid string/regex matching (the kind used, for example, in `blog-google-adk-zero-trust-agents.md`'s Semantic Gateway rules) is unsuited to scoring open-ended spoken output — voice agents have a strictly larger surface-form variance than a deterministic tool call or a text field the a Semantic Gateway inspects. The claim is graded "emerging" rather than "settled" because the post asserts, but does not measure, that the rubric judge reliably tracks a human reviewer's judgment across that phrasing variance.

### Claim 11: The live-voice eval pipeline is runnable from the CLI via `adk eval` and callable programmatically via `AgentEvaluator`, explicitly positioned for dropping into a CI/CD pipeline to catch regressions before shipping
- **Evidence**: A runnable shell command plus a direct statement of the CI/CD use case.
- **Confidence**: settled (directly falsifiable CLI artifact; the CI/CD-suitability claim is a straightforward consequence of having a scriptable, non-interactive entry point, not a separately tested claim)
- **Quote**: "This same pipeline can be called programmatically via AgentEvaluator, making it easy to drop live voice evaluations into your CI/CD pipeline to catch regressions before shipping."
- **Our assessment**: This corroborates `blog-langchain-better-harness-evals.md`'s Claim 12 ("the eval becomes a regression test") and `blog-thoughtworks-anand-agent-evaluation-framework.md`'s Claim 6 ("catch regressions") from a third, independent vendor and, notably, for a modality (live audio) neither of those sources' eval frameworks addresses — this is the first corpus source describing regression-testing for *voice* agent behavior specifically, not just text-agent tool-selection or trajectory behavior.

### Claim 12: ADK Web's run-setup dialog now has a Standard/Live mode toggle exposing audio-vs-text input-modality and voice/language options, and a completed live-eval run renders as a transcript with a playable audio clip per turn so a developer can review how the agent sounded, not just what it said
- **Evidence**: Direct feature description of the ADK Web debugging UI.
- **Confidence**: settled (direct vendor description of a shipped UI feature)
- **Quote**: "Once the run completes, ADK rebuilds the live audio stream into a clean transcript. Each turn renders in a dedicated message bubble complete with transcript text and an inline playable audio clip, so you can evaluate how your agent sounded, not just what it said."
- **Our assessment**: This is a concrete answer to a verification problem specific to voice agents that none of the corpus's text-based eval/observability sources address: transcript text alone can hide problems audible in the actual synthesized/recognized speech (tone, mispronunciation, awkward pacing, TTS artifacts) — the playable-clip-per-turn UI is a debugging affordance with no text-only equivalent.

## Concrete Artifacts

### Three-agent live Workflow (verbatim from source)
```python
from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext
from google.adk.workflow import START, Workflow
from pydantic import BaseModel, Field

LIVE_MODEL = "gemini-live-2.5-flash-native-audio"

def validate_date_of_birth(dob: str, tool_context: ToolContext) -> dict:
    """Validate a confirmed date of birth against records (mocked)."""
    match = dob == "1985-07-12"
    tool_context.state["dob_verified"] = match
    return {"match": match}

greeter_agent = Agent(
    model=LIVE_MODEL,
    name="greeter_agent",
    mode="task",
    instruction="You are Sam, a friendly care-team assistant. Greet the caller "
    "and confirm you're speaking with John Doe before sharing anything else. "
    "Ask one question per turn, then complete your task with the confirmed name.",
)

dob_verifier_agent = Agent(
    model=LIVE_MODEL,
    name="dob_verifier_agent",
    mode="task",
    tools=[validate_date_of_birth],
    instruction="Ask for the caller's date of birth, read it back to confirm, "
    "then call validate_date_of_birth in YYYY-MM-DD format. Complete your task "
    "with 'verified' or 'unverified'.",
)

goals_agent = Agent(
    model=LIVE_MODEL,
    name="goals_agent",
    mode="task",
    instruction="Identity is verified. Proactively share the upcoming "
    "appointment on Tuesday, June 16th at 3 PM with Dr. Example, answer any "
    'questions, then wrap up warmly and end with "Goodbye."',
)

root_agent = Workflow(
    name="live_workflow",
    edges=[
        (START, greeter_agent),
        (greeter_agent, dob_verifier_agent),
        (dob_verifier_agent, goals_agent),
    ],
)
```
Source: developers.googleblog.com, "How to Evaluate Live & Voice Agents in ADK" (2026-08-24), "Step 1: The agent under test."

### Conversation-scenario eval case (verbatim from source)
```json
{
  "eval_id": "example_scenario_case",
  "conversation_scenario": {
    "starting_prompt": "Hello?",
    "conversation_plan": "You are John Doe. Confirm your name when greeted. When asked for your date of birth, give July 12th, 1985, and confirm it when read back. Listen to the appointment details, ask what you should bring to the visit, then say you have no other questions and let the call wrap up.",
    "user_persona": "NOVICE"
  },
  "session_input": {
    "app_name": "live_workflow",
    "user_id": "test_user_id",
    "state": {}
  }
}
```
Source: same post, "Step 2: Author the eval set."

### Fixed-conversation eval case (verbatim from source)
```json
{
  "eval_id": "example_fixed_case",
  "conversation": [
    {
      "user_content": {
        "role": "user",
        "parts": [{ "text": "Hi, yes, this is John Doe." }]
      }
    },
    {
      "user_content": {
        "role": "user",
        "parts": [{ "text": "My date of birth is July 12th, 1985." }]
      }
    }
  ]
}
```
Source: same post, "Step 2: Author the eval set."

### Live/audio + rubric-judge test_config.json (verbatim from source)
```json
{
  "criteria": {
    "rubric_based_multi_turn_trajectory_quality_v1": {
      "threshold": 0.7,
      "judge_model_options": { "judge_model": "gemini-3.7-flash" },
      "rubrics": [
        {
          "rubric_id": "verifies_identity_first",
          "rubric_content": {
            "text_property": "Across the call, the agent confirms the caller's name and validates their date of birth before disclosing any appointment details."
          }
        }
        // ... further end-to-end rubrics
      ]
    }
  },
  "live_model_config": {
    "timeout_seconds": 300
  },
  "user_simulator_config": {
    "type": "llm_audio",
    "model": "gemini-3.7-flash",
    "max_allowed_invocations": 10,
    "audio_model": "gemini-3.1-flash-tts-preview",
    "audio_model_configuration": {
      "response_modalities": ["AUDIO"],
      "speech_config": {
        "voice_config": {
          "prebuilt_voice_config": { "voice_name": "Kore" }
        },
        "language_code": "en-US"
      }
    }
  }
}
```
Source: same post, "Step 3: Turn on live and audio."

### CLI eval invocation (verbatim from source)
```
uv run adk eval \
  contributing/samples/live/live_workflow \
  contributing/samples/live/live_workflow/live_workflow.evalset.json \
  --config_file_path contributing/samples/live/live_workflow/test_config.json
```
Source: same post, "Step 4: Run it." The post notes the `eval` extras must be installed (`uv pip install -e ".[eval]"`) and API credentials configured for both the Live API and Gemini TTS.

## Cross-References

- **Corroborates**:
  - `blog-google-adk-2-0-deterministic-workflows.md` Claim 4 (`Workflow`/`START`/edges graph orchestration with sequential and conditional nodes) and Claim 6 (Strict State Boundaries / Programmatic Routing shielding node context): this source's three-agent `Workflow` (Claim 3 here) reuses the identical graph-orchestration API on a live/voice pipeline, and its "ADK carries the accumulated session state and conversation history forward so each agent picks up in context rather than starting cold" independently restates the same state-continuity mechanism that note documents for text workflows — evidence the graph engine and its context-shielding behavior are shared infrastructure across text and voice agent types, not separate implementations.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 5 (persona-based testing as a distinct evaluation layer, via third-party tools Snowglobe/Collinear/Rhesis): this source is the first corpus example of a framework vendor (Google/ADK) shipping persona-based multi-turn simulation as a *native* eval capability rather than a third-party tool integration, and is more mechanism-specific about what a persona actually does (Claim 5 here: `NOVICE` withholds information to test the agent's own information-gathering behavior) than the Thoughtworks post's tool-landscape-level treatment.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 6 ("conversation as a unit" — treating a complete interaction as the unit under test) and `blog-langchain-better-harness-evals.md` Claim 12 (evals become regression tests once an agent handles a case correctly): this source's rubric-based multi-turn trajectory judge (Claim 9 here) and its explicit CI/CD regression framing (Claim 11 here) independently restate both claims for a new modality — voice/live agents — that neither of those two sources' frameworks addresses.
  - `guide/03-verification.md`'s existing LLM-as-judge coverage (~line 1089, sourced from `blog-cursor-continual-harness-improvement.md` Claim 2, a single-turn satisfaction classifier): this source's rubric-based judge (Claim 9) is a more elaborate instance of the same underlying mechanism — a model classifying agent behavior against a criterion — scaled up from one classification per follow-up message to a named, thresholded rubric scored across an entire multi-agent conversation.

- **Contradicts**: No material contradictions identified with existing corpus source notes.

- **Extends**:
  - `blog-anthropic-voice-mode-tools-multilingual.md`: that note's Scope explicitly states it does "NOT cover... benchmarks or latency figures, how the underlying speech model works technically" for Claude's consumer voice mode. This source fills an adjacent but distinct gap — not benchmarking Claude's voice mode, but providing a first-party *methodology* for evaluating a different vendor's developer-built voice agents (ADK) before shipping. The two sources are not about the same product (a consumer chat app's voice feature vs. a framework for building custom voice agents), but together they cover both "how end-user voice mode works" (Anthropic) and "how to test a voice agent you build" (Google/ADK), neither of which the corpus had before this pairing.
  - `blog-google-adk-zero-trust-agents.md` Claim 9 ("treat security policies as software contracts... include unit tests in your CI/CD pipeline to ensure prompt updates or model migrations do not introduce security regressions"): this source extends the "CI-tested software contract" pattern from deterministic regex/rule-based security checks into a genuinely different regime — a non-deterministic, LLM-judged rubric scoring conversational quality — for a different guarantee (conversation-quality regression, not security-rule regression). Both sources converge on "wire the check into CI so a later change can't silently break behavior a team already verified," applied to two different kinds of checks (deterministic security rules vs. rubric-scored trajectory quality).

- **Novel**:
  - **Audio-based user simulation as a native (not third-party) evaluation capability**: TTS-synthesized simulated-user turns streamed directly to a live agent under test, scored by the same eval pipeline as text agents. No prior corpus source describes simulating a *voice* user for automated agent evaluation — the corpus's existing persona-simulation coverage (`blog-thoughtworks-anand-agent-evaluation-framework.md`) is text-based and relies on third-party tooling.
  - **Decoupling the eval-set format from the execution modality**: the identical JSON test cases (conversation scenarios and fixed conversations) run in either text or live/audio mode depending solely on the presence of a `live_model_config` block (Claim 7) — no prior corpus eval-framework source describes a single test-case format that transparently runs across two different interaction modalities via config alone.
  - **Splitting the simulated user's conversational-logic model from its speech-synthesis model** (`model` vs. `audio_model`, Claim 8), allowing voice/accent/language variation to be tested independently of the simulated user's reasoning — a specific mechanism not present in any other corpus evaluation source.
  - **A named, thresholded, rubric-based LLM judge for whole multi-turn/multi-agent trajectories** (`rubric_based_multi_turn_trajectory_quality_v1`, Claim 9), with an explicit rationale (Claim 10) that phrasing variance in spoken output specifically motivates natural-language rubrics over rigid pattern matching — more specific than the corpus's existing single-turn LLM-as-judge example.
  - **A playable-audio-clip-per-turn transcript UI for eval-run debugging** (Claim 12) — no other corpus verification/observability source describes a results UI that lets a reviewer listen to, not just read, an agent's evaluated conversation turns.

## Guide Impact

- **Chapter 03 (Verification)**: Add ADK's live/voice eval pattern as a concrete example of extending an existing eval loop to a new interaction modality without a new pipeline — same eval-set JSON, execution mode flipped by config (Claim 7). Cite the conversation-scenario vs. fixed-conversation duality (Claim 4) as a reusable general pattern for eval-set design: persona-driven goal simulation for exploratory/robustness coverage, paired with scripted fixed conversations for exact, reproducible regression cases — applicable beyond voice agents specifically.
- **Chapter 03 (Verification), LLM-as-judge section** (~line 1089, currently sourced from `blog-cursor-continual-harness-improvement.md`'s single-turn satisfaction classifier): add this source's rubric-based, thresholded, whole-trajectory judge (Claim 9) as a more elaborate instance of the same LLM-as-judge mechanism, with Claim 10's explicit rationale (natural-language rubrics needed because correct output has high surface-form variance) as a named justification for choosing rubric judging over deterministic pattern matching — directly transferable to any agent whose valid outputs are not exact-matchable (not just voice).
- **Chapter 03 (Verification)**: Add the "safeguard against run-off conversations" `max_allowed_invocations` pattern (Claim 6) as a specific, reusable technique for bounding *simulated-user* turn counts in dynamic/goal-driven eval scenarios, distinct from — but structurally similar to — the corpus's existing agent-loop bounding guidance (which bounds the agent-under-test's own actions, not the simulator driving it).
- **Chapter 02 (Harness Engineering) or Chapter 03**: If the guide adds voice/multimodal agent coverage, cite this source as the concrete "how do you actually test this before shipping" answer, paired with `blog-anthropic-voice-mode-tools-multilingual.md` for the end-user-facing side of voice agents — together they cover both consumer voice-mode behavior and developer-built voice-agent testing methodology.

## Extraction Notes

- The article was fetched via WebFetch first, which returned only a high-level paraphrased summary (headings and generalized bullet points, not verbatim body text) — consistent with prior extractions in this corpus noting the WebFetch summarizer is unsuitable for verbatim quoting. All `Quote` fields above were instead taken from a direct `curl` fetch of the raw HTML, converted to plain text with a Python script that preserved code-block and paragraph boundaries, and matched character-for-character against that raw-fetched text, not the WebFetch summary.
- The post is a single, short, self-contained how-to guide with no linked sub-pages carrying additional substantive detail — the only in-body links are to the ADK documentation site (generic, not followed per MINER.md's "substantive" bar) and the `live_workflow` sample directory path referenced in the CLI command (a repository path, not a fetchable web page from the post itself). No sub-pages were followed.
- No contradiction with any existing corpus source note was identified; none filed per MINER.md §4a.
- Confidence graded "emerging" overall rather than "settled": the code-level artifacts (agent definitions, eval-set JSON, `test_config.json`, CLI command) are directly falsifiable and settled, but the post's persuasive/rationale claims — the failure-mode diagnosis (Claim 1) and the rubric-vs-pattern-matching justification (Claim 10) — are vendor rationale asserted without measurement (no false-positive/false-negative rate, no judge-model-vs-human-agreement figure, no production deployment or benchmark reported), which is why the overall grade sits one notch below a fully "settled" first-party feature-launch post.
