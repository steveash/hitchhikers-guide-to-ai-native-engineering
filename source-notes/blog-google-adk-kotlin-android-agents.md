---
source_url: https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/
source_type: blog-post
title: "Announcing ADK for Kotlin and ADK for Android 0.1.0: Building AI Agents on Android and Beyond"
author: Guillaume Laforge (Developer Advocate) and Jolanda Verhoef (Android Developer Relations Engineer), Google Developers Blog
date_published: 2026-05-21
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: emerging
issue: "#1457"
---

# Announcing ADK for Kotlin and ADK for Android 0.1.0: Building AI Agents on Android and Beyond

> Google's first-party 0.1.0 launch of Agent Development Kit (ADK) for Kotlin and a
> companion ADK for Android library, whose headline feature is explicit hybrid
> orchestration — a cloud model acts as the top-level agent and offloads specific
> sub-tasks (e.g., local document retrieval) to sub-agents that run entirely on-device
> against Gemini Nano, with code-level controls (`disallowTransferToPeers`,
> `disallowTransferToParent`) for constraining the resulting multi-agent hierarchy.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party framework/SDK launch
  announcement with inline code samples, May 21, 2026)
- **Author credibility**: Guillaume Laforge (Developer Advocate) and Jolanda Verhoef
  (Android Developer Relations Engineer) are named Google staff writing on Google's own
  developer blog, announcing a Google-authored open-source library (`google/adk-kotlin`
  on GitHub). This is a first-party vendor announcement, not independent practitioner
  analysis — treat feature descriptions and code samples as accurate representations of
  what shipped in 0.1.0, but treat the maturity/production-readiness framing as
  vendor-optimistic. The post explicitly says this is "our first experimental version."
- **Scope**: Covers the ADK for Kotlin 0.1.0 and ADK for Android launch: the rationale
  (edge AI shift, Gemini Nano device reach), four headline features (hybrid
  orchestration, on-device sequential agents, local retrieval, flexible tooling), a
  narrated real-world trip-assistant example, Gradle setup instructions, two runnable
  Kotlin code samples (a `disallowTransferToPeers`/`disallowTransferToParent`-gated
  root/sub-agent pair, and an "Improbability Drive" tool-based example), the full 0.1.0
  feature set table, and the three Android model-access paths (ML Kit GenAI/AICore,
  Firebase AI Logic, Google GenAI). Does NOT cover: benchmark numbers for Gemini Nano
  quality or latency, pricing, enterprise deployment/compliance guidance, or a
  comparison against ADK for Python/Java/Go feature parity beyond the one-line mention
  that those are already at 1.0.0/beta.

## Extracted Claims

### Claim 1: Hybrid orchestration lets a cloud model act as the top-level orchestrator while offloading specific tasks to on-device sub-agents, with ADK auto-adapting the API surface
- **Evidence**: First-party feature description under the "Feature Highlights" section, presented as the first and lead feature of the release.
- **Confidence**: emerging (vendor feature description of a 0.1.0/"first experimental version" release; no independent verification of the auto-adaptation behavior)
- **Quote**: "Hybrid Orchestration: You can use a cloud model as your main orchestrator, which can then offload specific tasks to sub-agents that run fully on-device. The ADK library takes care of adapting generic agent implementations to the correct cloud or on-device APIs."
- **Our assessment**: This is the structurally novel claim in the source: the same `LlmAgent` abstraction is reused for both cloud-backed and fully on-device sub-agents, and ADK — not the developer — handles the API translation between a cloud model call (e.g., Gemini via Firebase AI Logic) and an on-device call (e.g., Gemini Nano via AICore). If accurate, this removes a meaningful integration burden: a developer composing a multi-agent hierarchy does not need to hand-write two different calling conventions for cloud vs. edge sub-agents. This is the first source in the corpus describing a shipped framework where cloud/edge model choice is a configuration detail behind a uniform agent abstraction, rather than an architectural fork.

### Claim 2: On-device local retrieval agents access and parse documents entirely on-device so data never leaves the hardware
- **Evidence**: First-party feature description under "Feature Highlights."
- **Confidence**: emerging (vendor privacy claim for a 0.1.0 release; not independently audited)
- **Quote**: "Local Retrieval: By utilizing on-device models like Gemini Nano, you can create retrieval agents that access and parse documents locally, ensuring data never has to leave the hardware."
- **Our assessment**: This is a concrete instance of using an on-device model specifically to avoid a network round-trip for privacy-sensitive data — not just for latency or cost. Combined with Claim 4 (the trip-assistant example), the pattern is: keep the reasoning/orchestration step in the cloud (where model quality is presumably higher) but keep the data-touching step on-device (where privacy exposure is a concern). This is a specific, actionable architectural split that a privacy/security-threat-model discussion of agent design could cite directly.

### Claim 3: Sub-agents can be defined as sequential agents specifically for on-device multi-step task execution
- **Evidence**: First-party feature description under "Feature Highlights."
- **Confidence**: emerging (vendor feature description, 0.1.0 release)
- **Quote**: "On-Device Sequential Agents: You can define sub-agents as sequential agents, perfect for multiple tasks that need to run one after the other."
- **Our assessment**: This confirms ADK's existing workflow-agent primitives (sequential/parallel agents, part of the shared ADK family per the "ADK feature set" section) apply on-device, not just in cloud deployments. It is a thin claim on its own — mostly restating a workflow-agent primitive already documented in the broader ADK ecosystem — but it matters because it establishes that on-device sub-agents are not limited to single-shot tool calls; they can run local multi-step pipelines.

### Claim 4: The trip-assistant example demonstrates a full cloud-orchestrator-to-on-device-subagent-to-validation pipeline where private documents never leave the device
- **Evidence**: Narrated real-world usage example from Google's I/O session, described in prose (no code shown for this specific example).
- **Confidence**: emerging (vendor-narrated demo scenario, not a customer case study with independent verification)
- **Quote**: "If a user encounters an issue while traveling, the cloud-based orchestrator interacts with the user to understand the problem. However, when it needs to verify a booking confirmation, it delegates the task to an on-device subagent. Various retrieval agents use the on-device Gemini Nano model to extract data from the user's locally stored documents. Finally, a validation agent compares the data coming from these analyses. This keeps private data offline while leveraging the reasoning capabilities of the cloud orchestrator."
- **Our assessment**: This is the most concrete end-to-end illustration of Claims 1 and 2 combined into a working pipeline shape: cloud orchestrator (conversation) → on-device retrieval sub-agents (document extraction) → on-device validation agent (cross-checking extracted data) → results surfaced back to the cloud orchestrator. It is a three-tier hybrid pipeline, not just a two-tier cloud/edge split — the validation step is itself a distinct on-device agent, suggesting ADK expects on-device sub-agent hierarchies of more than one level, not just a flat cloud-to-edge handoff.

### Claim 5: ADK for Kotlin exposes explicit code-level flags to block a sub-agent from transferring control back to its parent or sideways to peer agents
- **Evidence**: Verbatim code sample under "Getting Started with ADK for Android," defining a `genius_orchestrator` `LlmAgent` with `disallowTransferToPeers = true` and `disallowTransferToParent = true` set on the orchestrator relative to its `subAgents`.
- **Confidence**: settled (this is a direct code artifact from the source, not an interpretive claim — the parameters and their names are shown verbatim in the sample)
- **Quote**: (parameter names copied verbatim from the code sample; see Concrete Artifacts for the full block) — the source does not describe these flags in prose beyond the code sample itself, so no separate prose quote exists.
- **Our assessment**: This is a directly useful multi-agent topology control primitive: rather than relying on prompt instructions to keep control flow one-directional (parent → children only, no escalation back up or sideways), ADK for Kotlin exposes it as a boolean constructor argument on the agent definition. This is a stronger guarantee than prompt-based instruction and maps onto the "structural control, not prompted control" pattern this corpus has already identified for security controls (see Cross-References). It is new to the corpus specifically as a *multi-agent coordination-topology* lockdown, as distinct from a *tool-permission* lockdown.

### Claim 6: Gemini Nano has been available on Android since its introduction and now runs on over 140 million devices
- **Evidence**: First-party scale claim in the "Why ADK for Kotlin?" section, presented as the market-reach justification for building on-device agent tooling.
- **Confidence**: emerging (vendor-reported device count; no methodology or date range given for how "140 million" was measured or over what period)
- **Quote**: "The AI ecosystem is experiencing a massive shift toward the edge, since the introduction of Gemini Nano as a model on Android, it has become available on over 140 million devices."
- **Our assessment**: This is the deployment-scale justification for treating on-device inference as a first-class target rather than a niche one. 140 million devices is a large enough install base that "on-device sub-agent" stops being a hypothetical edge case and becomes a mainstream mobile-agent design consideration — but the claim is unaudited (no source data, no time window specified for how the count was reached), so it should be treated as a directional signal of scale, not a precise, sourced statistic.

### Claim 7: Android apps have three distinct SDK paths to reach a model — on-device Gemini Nano via ML Kit GenAI/AICore, cloud Gemini via Firebase AI Logic, or Google GenAI for quick prototyping
- **Evidence**: First-party "Android Models" subsection of the "ADK feature set" table, listing exactly three named integration paths.
- **Confidence**: settled (this is a direct enumeration from the source's own feature table, not an inference)
- **Quote**: "ML Kit GenAI to access on-device Gemini Nano via AICore" / "Firebase AI Logic to access Gemini models running in the cloud" / "Google GenAI for quick prototyping"
- **Our assessment**: This three-way split formalizes the hybrid architecture at the SDK level, not just the conceptual level: on-device (ML Kit GenAI/AICore), managed-cloud (Firebase AI Logic), and prototyping (Google GenAI) are each separate, named integration surfaces rather than one unified client with a model-selection flag. For a developer building the hybrid pattern in Claim 1, this means picking which SDK backs each agent in the hierarchy is an explicit, per-agent architectural decision — it is not abstracted away at the SDK level, even though ADK's agent abstraction hides the difference at the orchestration level.

### Claim 8: This is explicitly the first, experimental release of ADK for Kotlin, positioned behind the already-1.0/beta releases of ADK for Java, Go, and Python
- **Evidence**: First-party maturity framing in both the opening paragraph and the closing "What's Next?" section.
- **Confidence**: settled (direct vendor statement about release maturity, not an inference)
- **Quote**: "Following the recent 1.0.0 releases of ADK for Java and Go, as well as the beta of ADK for Python 2.0, we are thrilled to announce the launch of version 0.1.0 of Agent Development Kit (ADK) for Kotlin!" / "This 0.1 release is our first experimental version of the library, currently featuring default agents for the ML Kit GenAI APIs and direct connections to Gemini in the Cloud. But we are just getting started!"
- **Our assessment**: This directly caps the confidence practitioners should place in the Kotlin/Android surface specifically: Google's own framing is "first experimental version," well behind the 1.0.0 Java/Go releases and the Python 2.0 beta. Practitioners evaluating ADK for a hybrid-agent Android project should expect API churn and treat the 0.1.0 Kotlin/Android layer as less stable than the same ADK concepts on other languages. This tempers Claims 1–7: the hybrid-orchestration feature set is real and shipped, but on the least mature of the four ADK language surfaces.

### Claim 9: The GitHub repository for ADK for Kotlin carries an explicit Pre-GA disclaimer and has already advanced past the 0.1.0 version announced in this post
- **Evidence**: Followed the "project on GitHub" link (`github.com/google/adk-kotlin`) referenced at the end of the blog post; fetched the repository page directly (not via the blog post itself) and read the embedded README text.
- **Confidence**: settled (directly observed repository state as of the extraction date, 2026-07-03, six weeks after the blog post's May 21, 2026 publication)
- **Quote**: "An open-source, code-first Kotlin toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control." / "This feature is subject to the \"Pre-GA Offerings Terms\" in the General Service Terms section of the Service Specific Terms. Pre-GA features are available \"as is\" and might have limited support."
- **Our assessment**: This is a follow-up-page finding, not from the blog post text itself: at extraction time the repository's latest tagged release is v0.4.0 (up from the 0.1.0 announced here), and the README's own "Preview" section repeats the "as is"/"limited support" Pre-GA disclaimer. This corroborates Claim 8's "first experimental version" framing with independent evidence from the project's own repository rather than relying solely on the announcement post's self-description — the project is iterating quickly (0.1.0 → 0.4.0 in about six weeks) but Google itself has not removed the Pre-GA caveat as of this writing.

## Concrete Artifacts

### Root/sub-agent code sample with explicit transfer-control flags (verbatim from source, "Getting Started with ADK for Android")

```kotlin
val orchestrator = LlmAgent(
name = "genius_orchestrator",
model = Gemini(apiKey = apiKey, name = MODEL_NAME),
instruction = Instruction("""
You are a travel genius assistant.
First, use `get_trip_details` to get the full itinerary of the trip and
understand what events are scheduled.
Then, respond with a welcome message tailored to the trip state.
""".trimIndent()),
tools = listOf(GetTripDetailsTool(tripId)),
subAgents = listOf(carRentalPipeline, hotelPipeline),
disallowTransferToPeers = true,
disallowTransferToParent = true,
)
```
Source: developers.googleblog.com, "Announcing ADK for Kotlin and ADK for Android 0.1.0" (2026-05-21)

### Tool-annotation + multi-agent delegation sample (verbatim from source, "Getting Started with ADK for Kotlin")

```kotlin
class ImprobabilityDriveService {
    /** Calculates the improbability of a given event. */
    @Tool
    fun calculateImprobability(
        @Param("The event to calculate the improbability for, e.g., 'A cup of tea materializing'")
        event: String
    ): String {
        return "The improbability of '$event' is approximately 42 to 1 against."
    }
}

val heartOfGoldAgent =
    LlmAgent(
        name = "HeartOfGold",
        description = "The Heart of Gold ship computer. Handles improbability drive queries.",
        model = Gemini(apiKey = apiKey, name = "gemini-2.5-flash"),
        instruction =
            Instruction(
                """
                You are the ship computer of the Heart of Gold. You are cheerful, helpful, and slightly annoying.
                You have access to the Infinite Improbability Drive.
                Use real facts about yourself if asked, but keep it funny.
                """
                    .trimIndent()
            ),
        tools = ImprobabilityDriveService().generatedTools()
    )

val rootAgent =
    LlmAgent(
        name = "MissionControl",
        description = "The central router for space queries. Routes to HeartOfGold.",
        subAgents = listOf(heartOfGoldAgent),
        model = Gemini(apiKey = apiKey, name = "gemini-2.5-flash"),
        instruction =
            Instruction(
                """
                You are Mission Control. You are the central hub for all communications.
                Your main job is to route the user's query to the most appropriate agent.
                - If the query is about improbability, the Infinite Improbability Drive, or the Heart of Gold, transfer to `HeartOfGold`.
                - Otherwise, respond directly with a professional but stressed persona.
                """
                    .trimIndent()
            )
    )
```
Source: developers.googleblog.com, "Announcing ADK for Kotlin and ADK for Android 0.1.0" (2026-05-21)

### Gradle dependency setup (verbatim from source)

```
# For Android apps (build.gradle.kts)
implementation("com.google.adk:google-adk-kotlin-core-android:0.1.0")

# For backend/JVM projects (build.gradle.kts)
dependencies {
    // Implementation dependency for ADK Core
    implementation("com.google.adk:google-adk-kotlin-core:0.1.0")
    // KSP processor for generating @AdkTools
    ksp("com.google.adk:google-adk-kotlin-processor:0.1.0")
}
```
Source: developers.googleblog.com, "Announcing ADK for Kotlin and ADK for Android 0.1.0" (2026-05-21)

### Full 0.1.0 feature set table (verbatim list items from source, "ADK feature set")

```
Agents:
  - LLM-based, workflow-based, custom agents
  - Multi-agent systems

Tooling & Integrations:
  - Function tools
  - Long-running function tools
  - MCP Tools
  - A2A
  - Plugins

Runtime & Observability:
  - Session state for short-term memory
  - Memory service for long-term memory
  - Telemetry (OpenTelemetry)

Developer Experience:
  - Web interface for development and experimentation

Android Models:
  - ML Kit GenAI to access on-device Gemini Nano via AICore
  - Firebase AI Logic to access Gemini models running in the cloud
  - Google GenAI for quick prototyping
```
Source: developers.googleblog.com, "Announcing ADK for Kotlin and ADK for Android 0.1.0" (2026-05-21)

## Cross-References

- **Corroborates**:
  - `blog-anthropic-agent-identity-access-model.md` Claim 4 ("Agent identity replaces the per-user access question with a per-compartment agent access model") and Claim 8 ("Credentials are stored independently, mapped to channel identity, and injected at the network boundary at request time — never attached to individual users"): both sources independently converge on structural, code/config-level access control rather than prompt-based control. ADK's `disallowTransferToPeers`/`disallowTransferToParent` (Claim 5 here) is the multi-agent-topology analog of Anthropic's per-compartment credential injection — both use a declared, non-negotiable boundary rather than an instruction the model could ignore.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3 ("Orchestrator-subagent's core failure mode is information bottleneck when subagents discover cross-cutting insights"): the trip-assistant example here (Claim 4) is a concrete orchestrator-subagent instance with a *validation* sub-agent inserted specifically to reconcile findings from multiple retrieval sub-agents before they reach the orchestrator — a specific mitigation shape for the cross-cutting-insight problem that Anthropic's taxonomy names abstractly.
  - `blog-anthropic-mcp-production-agents.md` Claim 4 ("MCP is the recommended integration layer for production cloud agents..."): ADK's feature table (Concrete Artifacts, "Tooling & Integrations") lists "MCP Tools" as a first-class, shipped integration surface alongside "A2A" — external corroboration from a competing vendor's framework that MCP has become a expected integration point for production agent frameworks, not an Anthropic-only convention.

- **Contradicts**: None identified. No existing source note makes a claim about hybrid cloud/on-device agent orchestration that this post disagrees with; this is a novel architecture pattern rather than a competing claim about an existing one.

- **Extends**:
  - `blog-google-io-2026-developer-keynote.md`: That note's Claim 5 documents the stable Android CLI as "AI agent uses IDE as a tool" for Android *development* tooling (agents building Android apps). This source is a distinct, narrower claim: an SDK for building agents that run *inside* Android apps as a runtime feature (agents as a product capability for end users), not a developer-tooling agent. The two sources cover adjacent but separate parts of Google's May 2026 Android/AI push — dev-tooling agents vs. in-app agents — and should not be conflated.
  - `blog-ronacher-local-models-focus-polish.md` Claim 14 ("The local model vision is explicitly framed as an alternative to hyperscaler lock-in..."): Ronacher's definition of "local" (full offline capability, no hyperscaler dependency) is a useful contrast case for this source's on-device claims (Claims 2, 6, 7). ADK's on-device path still depends on Google's AICore/ML Kit GenAI stack and Gemini Nano being present on the device — it is "on-device execution within a hyperscaler-controlled model and OS stack," not the fully independent local-model vision Ronacher describes. This is a definitional contrast worth flagging in guide text, not a contradiction (the two sources describe different products for different audiences: mobile app developers vs. individual coding-agent practitioners).

- **Novel**:
  - **Shipped, code-level multi-agent transfer-topology locks** (`disallowTransferToPeers`, `disallowTransferToParent`, Claim 5): no prior corpus source documents a framework exposing agent-hierarchy control-flow restrictions as typed constructor parameters on the agent definition itself.
  - **A named three-tier hybrid pipeline shape** (cloud orchestrator → on-device retrieval sub-agents → on-device validation agent, Claim 4): the corpus has cloud/edge splits in the abstract (multi-agent coordination patterns) but no prior worked example of a validation agent specifically inserted at the on-device layer to reconcile multiple on-device retrieval results before surfacing them to a cloud orchestrator.
  - **A named three-way Android model-access SDK split** (ML Kit GenAI/AICore, Firebase AI Logic, Google GenAI, Claim 7): no prior source documents this specific three-path taxonomy for how a mobile app developer chooses between on-device, managed-cloud, and prototyping model access within one platform's SDK ecosystem.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the `disallowTransferToPeers`/`disallowTransferToParent` pattern (Claim 5) as a concrete example of structural (code-level, not prompt-level) control over multi-agent delegation topology, alongside the existing generator-verifier/orchestrator-subagent taxonomy from `blog-anthropic-multi-agent-coordination-patterns.md`. This is a specific implementation mechanism the chapter currently lacks: a way to guarantee a sub-agent cannot escalate control back to its parent or hand off to a peer, enforced by the framework rather than by instruction.

- **Chapter 06 (Security Threat Model)**: Add the on-device-retrieval-for-privacy pattern (Claims 1, 2, 4) as a concrete architectural mitigation for "keep sensitive data out of the cloud reasoning loop": route the orchestration/reasoning step through a cloud model, but route any step that touches locally-stored sensitive documents through an on-device sub-agent so that data never crosses the network boundary. Caveat this with Claim 9's finding: the on-device execution still runs on a Google-controlled stack (AICore/Gemini Nano), so this is a network-boundary privacy control, not an independence-from-vendor control (contrast with `blog-ronacher-local-models-focus-polish.md`'s narrower, non-hyperscaler definition of "local").

- **Chapter 04 (Context Engineering)**: If a future revision covers cross-agent state sharing in hybrid cloud/on-device systems, flag that this source's blog text does not itself document how session state is shared across the cloud/on-device boundary in the trip-assistant example — the "Session state for short-term memory" feature is listed in the 0.1.0 feature table (Concrete Artifacts) but not explained in prose in this post. This would need a separate, deeper extraction from the ADK docs site (`adk.dev/sessions/state/`) before citing specific session-sharing mechanics in the guide.

## Extraction Notes

- Primary source fetched directly via `curl` and parsed to plain text (not through the WebFetch small-model summarizer) specifically so that every `Quote` field above could be verified character-for-character against the raw HTML. The first WebFetch pass on this URL returned a paraphrased summary (e.g., "Hybrid Orchestration: Cloud models can serve as main orchestrators while delegating specific tasks to on-device sub-agents, with automatic API adaptation") that does not match the source's own wording — that summary was discarded and only the raw-fetched text was used for quotes.
- Followed 4 linked pages from the announcement per MINER.md §1: `github.com/google/adk-kotlin` (fetched raw; used for Claim 9, verified verbatim from the embedded README JSON), `adk.dev/sessions/state/`, `adk.dev/a2a/`, and `adk.dev/agents/multi-agents/` (this last one 404-redirected to `adk.dev/workflows/` and was not usable). The `adk.dev/sessions/state/` and `adk.dev/a2a/` pages were only fetched via WebFetch (summarized, not raw-parsed) — their content is deliberately *not* quoted anywhere in this note (per MINER.md §2a.4, synthesis from those pages is confined to the "Guide Impact" caveat about session state, not presented as a direct quote).
- No contradiction issue filed. This source describes a new architecture pattern (hybrid cloud/on-device multi-agent orchestration for mobile apps) rather than disputing a claim already in the corpus; the closest adjacent source (`blog-ronacher-local-models-focus-polish.md`) addresses a different "local" definition for a different audience (individual coding-agent practitioners vs. mobile app end-users), which is a scope difference, not a contradiction per MINER.md §4a's "when NOT to file" guidance.
- Confidence graded `emerging` overall: this is a first-party vendor announcement of a library the vendor itself calls "our first experimental version" (Claim 8), corroborated by the GitHub repo's own Pre-GA disclaimer persisting six weeks later (Claim 9). The code samples and feature-table enumeration (Claims 5, 7, and Concrete Artifacts) are `settled` as factual descriptions of what shipped, but the qualitative claims about ease-of-use, API auto-adaptation, and privacy guarantees (Claims 1, 2, 6) are vendor framing that has not been independently practitioner-verified in this corpus.
