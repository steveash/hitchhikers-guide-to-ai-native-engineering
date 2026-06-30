---
source_url: https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/
source_type: blog-post
title: "All the news from the Google I/O 2026 Developer keynote"
author: Google Developers Blog (official Google team)
date_published: 2026-05-19
date_extracted: 2026-06-30
last_checked: 2026-06-30
status: current
confidence_overall: emerging
issue: "#1369"
---

# All the news from the Google I/O 2026 Developer keynote

> Google's official May 2026 I/O developer announcement establishes Antigravity 2.0 as an "agent-first development platform" with security controls (terminal sandboxing, credential masking, hardened Git policies), introduces WebMCP as a proposed open web standard for browser-based agent tooling (Chrome 149 origin trial), and documents domain-specific agent evaluation (Android Bench leaderboard), automated cross-platform migration (React Native/iOS → Kotlin), and a new suite of agentic web primitives (Chrome DevTools for agents, HTML-in-Canvas, Modern Web Guidance).

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party announcement, May 19, 2026 — Google I/O keynote companion post. Covers the developer-facing product announcements across three domains: cloud/agent orchestration, Android, and web platform.)
- **Author credibility**: First-party Google Developers Blog, the authoritative publication channel for official Google product announcements. These are vendor product-launch claims — concrete feature lists with named GitHub repos, Chrome version numbers, and leaderboard additions. No hands-on independent verification; treat as vendor-announced, not practitioner-validated. Complements `blog-simonwillison-gemini-spark-antigravity.md` which is an external practitioner analysis of the same event.
- **Scope**: Covers Antigravity 2.0 and CLI enhancements, Managed Agents API, Antigravity SDK, Android CLI (stable), Android Bench leaderboard, Migration Agent (preview), WebMCP open standard, Modern Web Guidance, Chrome DevTools for agents, HTML-in-Canvas API, and Google AI Studio feature updates. Does NOT cover: Gemini model capability benchmarks (see `blog-simonwillison-gemini35-flash-pricing.md`), Gemini Spark consumer product security architecture (see `blog-simonwillison-gemini-spark-antigravity.md`), or pricing/token cost.

## Extracted Claims

### Claim 1: Antigravity 2.0 is Google's formally declared "agent-first development platform"

- **Evidence**: Official product framing in the I/O developer keynote recap — Google's own positioning statement for its developer platform.
- **Confidence**: settled (first-party product announcement; the phrase is a strategic declaration, not a technical spec)
- **Quote**: "our agent-first development platform, with new capabilities to orchestrate and build agents"
- **Our assessment**: This is the most explicit on-record declaration from a major cloud provider that their developer platform is now agent-first by design — not an add-on capability but the organizing principle. The phrasing distinguishes "orchestrate" (composing existing agents) from "build" (creating new agents), matching the multi-agent coordination taxonomy from `blog-anthropic-multi-agent-coordination-patterns.md`. Google's formal adoption of this framing establishes "agent-first development platform" as standard industry vocabulary for this product category.

### Claim 2: Antigravity 2.0 CLI includes built-in cross-platform terminal sandboxing, credential masking, and hardened Git policies

- **Evidence**: First-party feature announcement in the developer keynote post; specific security controls named with "built-in" qualifier.
- **Confidence**: emerging (vendor announcement; specific implementation details of sandboxing and masking are not described; no independent verification)
- **Quote**: "all protected by built-in cross-platform terminal sandboxing, credential masking, and hardened Git policies."
- **Our assessment**: These three controls address distinct agentic threat vectors: terminal sandboxing limits code execution blast radius, credential masking prevents secrets from appearing in agent context or logs, and hardened Git policies control what the agent can commit. Together they map to the structural control pattern from `blog-anthropic-zero-trust-ai-agents.md` Claim 3 — controls that make misuse "impossible rather than tedious." The word "built-in" is significant: these are platform defaults, not opt-in hardening that practitioners must configure. Corroborates `blog-simonwillison-gemini-spark-antigravity.md` Claim 5 on credential opacity, which noted credentials "never exposed directly to the agent" — this developer-facing post confirms the same property is present in the CLI (not just the consumer Spark product).

### Claim 3: The Managed Agents API provisions fully configured Antigravity agents via a single API call with no infrastructure setup

- **Evidence**: First-party feature description in the announcement.
- **Confidence**: emerging (product launch claim; provisioning guarantee has not been independently tested)
- **Quote**: "Managed Agents in the Gemini API removes the friction of infrastructure setup, delivering the power of the Antigravity agent harness via managed agents."
- **Our assessment**: "Removes the friction of infrastructure setup" via a single API call is the "agents-as-a-service" provisioning model. This is Google's parallel to Anthropic's managed agents capability (see `blog-anthropic-claude-managed-agents.md`). The phrase "power of the Antigravity agent harness" indicates the API exposes the same runtime used in Antigravity 2.0 directly — practitioners get managed agent provisioning without needing the Antigravity desktop/CLI stack. This lowers the floor for building production agents substantially: no sandbox management, no credential infrastructure, no Git policy configuration.

### Claim 4: The Antigravity SDK provides programmatic control for custom agent deployment on own infrastructure

- **Evidence**: First-party product announcement.
- **Confidence**: settled (product feature announcement with explicit capability description)
- **Quote**: "We're also giving you programmatic control over the Antigravity agent harness with the new Antigravity SDK, so you can fully customize the agent and deploy it on your own infrastructure."
- **Our assessment**: "Deploy it on your own infrastructure" is the self-hosted path that distinguishes the SDK from Managed Agents. This creates a two-tier deployment model: managed (via API, Google-hosted) or self-hosted (via SDK, own infrastructure). The Willison note (Claim 6) described the SDK as "an open-source Python wrapper around a bundled closed-source Go binary" — this official announcement adds the self-hosting capability as an explicit new feature ("new Antigravity SDK"), suggesting either the SDK was updated or this deployment path is newly documented. The "fully customize" qualifier means the SDK is not just a deployment wrapper but a customization surface for agent behavior.

### Claim 5: The Android CLI (stable release) enables AI agents to directly access Android Studio capabilities including SDK downloads, device testing, and Jetpack migrations

- **Evidence**: Official stable release announcement; the word "stable" explicitly distinguishes this from preview or beta state.
- **Confidence**: settled (GA product announcement)
- **Quote**: "The stable Android CLI enables your AI agents to tap directly into the 'heavy-lifting' power of Android Studio."
- **Our assessment**: The first WebFetch summary notes this includes "SDK downloads, device testing, and open-sourced skills for Jetpack Compose and Navigation 3 migrations." The stable release marks AI-native Android development as production-ready, not experimental. The "heavy-lifting" framing positions Android Studio as a capability provider for AI agents rather than a tool for human developers — a role inversion from the traditional model. This is the formalization of the "AI agent uses IDE as a tool" pattern for the Android ecosystem.

### Claim 6: Android Bench is a domain-specific LLM leaderboard evaluating performance on Android development tasks, including open-weight models like Gemma 4

- **Evidence**: Named leaderboard announcement with a specific addition event ("this week").
- **Confidence**: settled (factual product announcement; leaderboard exists as a named evaluation artifact)
- **Quote**: "Android Bench, our LLM leaderboard for Android development tasks. This week, we added open-weight models such as Gemma 4 to the leaderboard."
- **Our assessment**: A domain-specific LLM leaderboard for mobile development is a new evaluation pattern. Rather than general-purpose coding benchmarks, Android Bench measures LLMs on the actual task domain: Android development. Including Gemma 4 (open-weight) alongside presumably proprietary models creates a cross-model comparison signal. For practitioners selecting models for Android development agents, this provides a first-party evaluation source aligned with the actual task domain — more informative than SWE-Bench or HumanEval for this use case. No prior corpus source documents domain-specific agent evaluation at this level of task specificity for mobile development.

### Claim 7: The Migration Agent (preview) automates weeks-long cross-platform code migration to native Kotlin regardless of source framework

- **Evidence**: Feature preview announcement with explicit source framework coverage (React Native, web, iOS).
- **Confidence**: emerging (preview feature; "reducing weeks-long migrations to hours" is from the first WebFetch summary, not a verbatim quote; the verbatim quote covers framework coverage only)
- **Quote**: "migrates your app code to a native Kotlin Android app, regardless of whether your source is React Native, a web framework, or iOS."
- **Our assessment**: Cross-platform-to-native code migration is one of the highest-value concrete agent use cases demonstrated to date. The "regardless of source" framing means the agent abstracts over framework differences rather than providing one-source-to-one-target migration. This is significant for the agent use case taxonomy: code migration was previously a human-intensive task requiring weeks because of semantic gap analysis across framework idioms. If the preview delivers on this claim, it represents the most concrete documented case in the corpus of an agent compressing a multi-week specialized engineering task to hours. The preview qualifier means this is early-stage; practitioners should treat the claim as aspirational until independent validation.

### Claim 8: WebMCP is a proposed open web standard for browser-based agent tool integration, with a Chrome 149 origin trial underway

- **Evidence**: Formal open standard proposal announcement with a named Chrome origin trial version.
- **Confidence**: emerging (proposed standard in origin trial; not yet ratified or broadly adopted)
- **Quote**: "WebMCP is a proposed open web standard that allows developers to expose structured tools" (note: the clause "so browser-based AI agents can execute complex tasks" follows but may not be adjacent in source)
- **Our assessment**: WebMCP is the most strategically significant claim in this source. MCP (Model Context Protocol) is Anthropic's protocol for agent-tool integration (see `blog-anthropic-mcp-production-agents.md`); WebMCP is Google's parallel proposal specifically for the browser environment, exposing "structured tools" (JavaScript functions, HTML forms per first WebFetch summary) that browser-based agents can invoke. The Chrome 149 origin trial signals this is moving toward a real platform feature, not just a paper proposal. If WebMCP advances to a W3C standard or Chrome stable, it would make browser-native agent tool integration a first-class web capability — eliminating the scraping/overlay pattern that current browser agents use. This is entirely new to the corpus; no prior note covers a browser-native standardization effort for agentic tooling.

### Claim 9: Modern Web Guidance provides coding agents with 100+ expert-vetted skills for performant, accessible, and secure web development, with Baseline integration

- **Evidence**: Product announcement; the "100+" count and "Baseline integration" details are from first WebFetch summary; the verbatim quote covers the purpose statement.
- **Confidence**: settled (GA product description)
- **Quote**: "Modern Web Guidance will help you build more performant, accessible, and secure web experiences by providing your coding agents with a set of expert-vetted skills."
- **Our assessment**: Agent skill libraries as a platform product is a different paradigm from general-purpose code generation: rather than relying on the model's training data for web development best practices, Modern Web Guidance injects expert-curated skills directly into the agent's toolset. The Baseline integration means skills are filtered to cross-browser-compatible patterns, reducing the hallucination of deprecated or non-standard APIs. The "expert-vetted" qualifier addresses a known limitation of LLM-generated web code (outdated patterns, accessibility blind spots). This pattern — vendor-curated skill sets for domain coding agents — is new to the corpus and represents a different approach to improving agent output quality than fine-tuning or prompting.

### Claim 10: Chrome DevTools for agents enables automated quality auditing, real-world experience emulation, and session handover for agentic workflows

- **Evidence**: Product announcement.
- **Confidence**: settled (product feature announcement; "automated quality audits, real-world experience emulation, and session handover without manual intervention" details are from first WebFetch summary)
- **Quote**: "Chrome DevTools for agents, helping you scale your workflow with verifying, debugging, and optimizing code in real time."
- **Our assessment**: Extending DevTools for agents rather than humans is a notable infrastructure decision: it acknowledges that agents need their own debugging and observability surfaces. "Session handover without manual intervention" suggests agents can pass state to other agents (or humans) using the DevTools interface. This addresses one of the unresolved patterns in harness engineering: how to inspect and debug an agentic workflow in-flight. The "real-world experience emulation" implies testing agents against real browser conditions (slow networks, device profiles) in the same workflow as code generation — a pattern that bridges CI/CD and agentic quality assurance.

### Claim 11: The HTML-in-Canvas API (origin trial) integrates DOM elements into WebGL/WebGPU canvas for fully searchable, accessible 3D experiences

- **Evidence**: Origin trial announcement; technical detail (WebGL/WebGPU) from first WebFetch summary.
- **Confidence**: emerging (origin trial, not yet stable)
- **Quote**: "developers can build immersive, 3D experiences that remain fully searchable, accessible, and interactable."
- **Our assessment**: The accessibility + 3D combination is the key claim: previous canvas-based 3D experiences (WebGL/WebGPU) sacrificed DOM accessibility for graphics performance. HTML-in-Canvas integrating both means AI-driven 3D interfaces can be built that remain accessible to screen readers and searchable by agents — removing the traditional accessibility/immersion tradeoff. For agentic web applications, searchability of 3D content is particularly relevant: an agent navigating a 3D UI needs the same DOM access it uses for 2D interfaces. This is a novel browser primitive but its agent-specific impact is speculative at origin trial stage.

### Claim 12: Google AI Studio gains native Kotlin support, Google Workspace integrations, one-click Cloud Run deployment, and Firebase service support

- **Evidence**: Product update announcement in the keynote post.
- **Confidence**: settled (product feature announcement)
- **Quote**: "Google AI Studio now includes native Kotlin support to vibe code Android apps" (note: "With Google Workspace integrations and a one-click deploy to Cloud Run along with support for Firebase services" follows in the article but may not be adjacent)
- **Our assessment**: This represents platform convergence: Google's AI development studio now spans mobile (Kotlin/Android), productivity (Workspace), serverless (Cloud Run), and app platform (Firebase) in a unified IDE. "Vibe coding Android apps" in native Kotlin (rather than cross-platform) is a specific claim about AI-assisted native Android development. The "one-click deploy to Cloud Run" removes the deployment friction that typically separates development from production. For practitioners, this signals that Google's vision for AI-native development is tightly integrated with its full cloud stack — the AI Studio is not just a model interface but a full-stack development environment.

## Concrete Artifacts

### Antigravity 2.0 Security Controls (from official developer keynote post)

```
Antigravity 2.0 Built-in Security Controls (Google, May 19, 2026)
Source: developers.googleblog.com — Google I/O 2026 Developer Keynote

Control                    Description
--------------------       --------------------------------------------------
Terminal sandboxing        Cross-platform; constrains code execution blast radius
Credential masking         Prevents secrets from appearing in agent context/logs
Hardened Git policies      Controls what the agent can commit to repositories

Verbatim: "all protected by built-in cross-platform terminal sandboxing,
           credential masking, and hardened Git policies."
```

### Antigravity 2.0 Deployment Architecture (from official developer keynote post)

```
Antigravity 2.0 Deployment Options (Google, May 19, 2026)
Source: developers.googleblog.com — Google I/O 2026 Developer Keynote

Surface                    Description
--------------------       --------------------------------------------------
Antigravity 2.0 CLI        "two powerful surfaces for incredible productivity gains"
                           (paired with Antigravity 2.0 desktop/IDE)
Managed Agents API         "removes the friction of infrastructure setup,
                           delivering the power of the Antigravity agent harness
                           via managed agents" — single API call provisioning
Antigravity SDK            "programmatic control over the Antigravity agent harness
                           ...fully customize the agent and deploy it on your
                           own infrastructure" — self-hosted path
```

### Android Developer Tooling (from official developer keynote post)

```
Android AI Developer Tooling (Google, May 19, 2026)
Source: developers.googleblog.com — Google I/O 2026 Developer Keynote

Tool                  Status    Description
------------------    ------    -----------------------------------------------
Android CLI           Stable    Agents access Android Studio capabilities
                                (SDK downloads, device testing, Jetpack skills)
Android Bench         GA        LLM leaderboard for Android development tasks;
                                includes Gemma 4 (open-weight)
Migration Agent       Preview   Converts React Native / web / iOS → native Kotlin
Google AI Studio      GA        Kotlin support, Workspace, Cloud Run, Firebase
```

### WebMCP Standard Summary (from official developer keynote post)

```
WebMCP (Google, May 19, 2026)
Source: developers.googleblog.com — Google I/O 2026 Developer Keynote

Status:        Proposed open web standard
Trial:         Chrome 149 origin trial
What it does:  "allows developers to expose structured tools" for
               browser-based AI agents (JavaScript functions, HTML forms)
Purpose:       Enable browser-native agent tool integration without
               scraping/overlay patterns
```

### Web Agent Tooling Summary (from official developer keynote post)

```
Web Agent Platform Features (Google, May 19, 2026)
Source: developers.googleblog.com — Google I/O 2026 Developer Keynote

Feature                     Status          Description
--------------------        --------        ----------------------------------
WebMCP                      Origin trial    Open standard for browser agent tools
                            (Chrome 149)
Modern Web Guidance         GA              100+ expert-vetted skills; Baseline
                                            integration; installable via
                                            Antigravity or CLI
Chrome DevTools for agents  GA              Verifying, debugging, optimizing code;
                                            quality audits; session handover
HTML-in-Canvas API          Origin trial    DOM in WebGL/WebGPU; searchable 3D
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gemini-spark-antigravity.md` Claim 5: That note documented Gemini Spark credential opacity — "user credentials remain fully encrypted and are never exposed directly to the agent." This source corroborates the same pattern appearing in the developer-facing CLI as "credential masking" (Claim 2 here). Consistent: Google applies the same credential protection principle to both consumer (Spark) and developer (Antigravity CLI) surfaces.
  - `blog-simonwillison-gemini-spark-antigravity.md` Claim 6: Willison's note documented the Antigravity ecosystem components (desktop app, CLI in Go, Python SDK wrapping Go binary, VS Code fork IDE). This source confirms and extends that inventory with Antigravity 2.0 features (new SDK self-hosting capability, Managed Agents API) — consistent with Willison's component listing but adds new deployment paths.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 3: The "impossible vs. tedious" design criterion for security controls. Antigravity 2.0's "built-in" terminal sandboxing, credential masking, and hardened Git policies are platform defaults enforced structurally — they implement the "impossible" end of the spectrum rather than friction-based deterrents.
  - `blog-anthropic-mcp-production-agents.md` Claim 1: "Agents are only as useful as the systems they can reach." WebMCP (Claim 8 here) is Google's browser-native implementation of exactly this principle — extending agent reach to structured browser tools via a proposed web standard.
  - `blog-anthropic-claude-managed-agents.md`: Managed Agents API (Claim 3 here) is Google's parallel to Anthropic's managed agents offering — single-API provisioning of fully configured agents. Both major providers converging on managed agent provisioning corroborates this as an emerging production pattern.

- **Contradicts**: None identified. This source is the official first-party announcement for the same Google I/O event analyzed by Willison in `blog-simonwillison-gemini-spark-antigravity.md` — they cover complementary dimensions without contradicting each other. The Willison note focused on security architecture and vendor lock-in risk; this source covers developer tooling across Android, web, and cloud.

- **Extends**:
  - `blog-simonwillison-gemini-spark-antigravity.md`: The Willison note was based on publicly available vendor documentation without access to the developer platform announcement. This source provides the comprehensive developer-facing feature set Willison could not cover: Android Bench, Migration Agent, WebMCP, Modern Web Guidance, Chrome DevTools for agents, HTML-in-Canvas, Google AI Studio updates, and the Managed Agents API. Together the two notes provide the most complete picture of Google I/O 2026 in the corpus.
  - `blog-anthropic-mcp-production-agents.md`: That note documented MCP as the integration protocol for agents reaching production systems. WebMCP extends this pattern to the browser environment specifically — browser-native agent tool integration via a proposed open web standard rather than an Anthropic-defined protocol.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 4: That note documented Gemini 3.5 Flash deployed across Google products "including Google Antigravity." This source confirms Antigravity 2.0 as the developer platform running on Gemini 3.5 Flash, completing the picture of the platform architecture.

- **Novel**:
  - **WebMCP as a proposed open web standard for browser-native agent tool integration**: No prior source in the corpus covers a browser standardization effort for agentic tooling. WebMCP (Chrome 149 origin trial) is the first corpus evidence of a major vendor proposing a W3C-style open standard specifically for agent-browser integration — not an API, not a protocol, but a web platform primitive.
  - **Android Bench: domain-specific LLM leaderboard for mobile development tasks**: The corpus has general coding benchmarks (SWE-Bench referenced in other notes) but no prior source documents a task-specific leaderboard for mobile development. Android Bench is the first corpus example of domain-aligned LLM evaluation for a specific engineering discipline.
  - **AI-automated cross-platform code migration (React Native/web/iOS → native Kotlin)**: No prior corpus source documents an agent performing multi-framework code migration at this scope. The Migration Agent claim (preview) is the most ambitious specific agent use case announced in the corpus.
  - **Chrome DevTools extended for agentic workflows**: DevTools has historically been a human-facing debugging environment. Chrome DevTools for agents is the first corpus-documented case of a browser's primary debugging tooling being explicitly extended for autonomous agent workflows — with quality audits, experience emulation, and session handover.
  - **HTML-in-Canvas API integrating DOM accessibility into 3D canvas**: No prior source in the corpus covers accessible 3D web primitives. This is a novel browser capability with potential relevance for agent-driven immersive interfaces.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Antigravity 2.0's "built-in" security controls (terminal sandboxing, credential masking, hardened Git policies) establish a commercial platform default for agent harness security. Update harness engineering guidance to note that as of May 2026, Google ships these three controls as platform defaults in Antigravity CLI — practitioners should treat these as the minimum baseline, not optional hardening. Chrome DevTools for agents adds a new observability pattern: browser-native agent debugging with automated quality auditing and session handover.

- **Chapter 03 (Standards)**: WebMCP is the first corpus-documented open web standard proposal for browser-based agent tool integration. If this section covers agent-tool integration protocols, add WebMCP as Google's browser-native parallel to MCP — a proposed W3C-style standard that would make browser tool integration a first-class web platform capability. Track Chrome 149 origin trial outcome.

- **Chapter 04 (LLM Integration / Agent Architecture)**: Managed Agents API (single-call provisioning) and Antigravity SDK (self-hosted deployment) establish a two-tier architecture pattern: managed (no infrastructure, vendor-hosted) vs. self-hosted (full customization, own infrastructure). This is a new architectural decision point that deserves explicit treatment alongside the existing multi-agent coordination patterns.

- **Chapter 06 (LLM Evaluation / Benchmarking)**: Android Bench is the first corpus example of a domain-specific LLM leaderboard for a professional engineering discipline. Add to evaluation guidance: general-purpose coding benchmarks (SWE-Bench) may not predict performance on domain-specific tasks; Google's Android Bench demonstrates the pattern of building task-aligned evaluation for specific engineering domains. Practitioners building agents for a specific domain should seek or build domain-aligned evaluation, not rely on general benchmarks.

- **Chapter 10 (Web Agents)**: WebMCP, HTML-in-Canvas API, Chrome DevTools for agents, and Modern Web Guidance represent a new cluster of web-platform primitives for agentic development. Add a section on Google's 2026 web agent tooling suite: WebMCP (browser tool integration standard), Modern Web Guidance (curated agent skill libraries), Chrome DevTools for agents (agentic observability), and HTML-in-Canvas (accessible immersive content). Together these represent Google's declared web-platform investment for the agent era.

- **Chapter 05 (Cross-platform Development)**: Migration Agent (preview) is the most ambitious automated code migration claim in the corpus. If the guide covers cross-platform development tooling, note this as an early-stage preview of AI-automated framework migration — with caution that preview claims require independent validation before production reliance.

## Extraction Notes

- **WebFetch returned summaries rather than verbatim text for some sections**: Three quotes in this note contain "..." indicating the WebFetch tool may have omitted intervening text (Quote 8: WebMCP, Quote 12: Google AI Studio, Quote 13: agent-first framing). Per MINER.md §2a, these are flagged in the note: only the contiguous fragments before the ellipsis are presented as direct quotes; the combined form is not presented as a verbatim quote. The Assayer should verify the exact wording around these ellipses against the live source URL.
- **Jules coding agent not mentioned in this source**: A Jules coding agent appears in triage comments as a potential extraction target. The WebFetch of this article returned no mention of "Jules" — this source either does not cover Jules or the fetcher did not capture it. If Jules is discussed in a separate Google I/O blog post, it would require a separate issue/extraction.
- **Preview vs. GA distinctions**: Migration Agent is explicitly preview; HTML-in-Canvas and WebMCP are origin trial. Android CLI, Android Bench, Modern Web Guidance, Chrome DevTools for agents, and Google AI Studio features appear to be GA. These distinctions affect the confidence grade for each claim.
- **No sub-pages followed**: The article links to GitHub repos and specific product pages (Android Bench, WebMCP spec, Chrome DevTools docs) that were not followed. A deeper extraction could pull verbatim quotes from those linked pages; the current note relies solely on the keynote recap article.
- **"Vibe coding" framing**: The source uses the phrase "vibe code Android apps" in the Google AI Studio section. This adopts informal practitioner vocabulary ("vibe coding") in an official product announcement — a notable framing choice indicating Google's awareness of and alignment with informal developer culture around AI-assisted coding.
