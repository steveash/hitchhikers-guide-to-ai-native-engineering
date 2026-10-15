---
source_url: https://claude.com/resources/articles/agent-observability-on-the-claude-platform
source_type: blog-post
title: "Agent observability on the Claude Platform"
author: Anthropic (no individual byline; customer quotes from Foxglove, Ramp, Sterling Labs, and an unnamed accounting-software company)
date_published: 2026-10-14
date_extracted: 2026-10-15
last_checked: 2026-10-15
status: current
confidence_overall: emerging
issue: "#4127"
---

# Agent observability on the Claude Platform

> First-party announcement (public beta) that Claude Managed Agents, the Messages API, and the Claude SDKs can export OpenTelemetry GenAI-convention traces to any OTLP tool, filling the agent-level tracing gap left by earlier Managed Agents and connector-observability coverage.

## Source Context

- **Type**: blog-post (vendor product announcement, ~3 min read; the page title is "Trace agents with OpenTelemetry on the Claude Platform")
- **Author credibility**: Anthropic, as the platform vendor. Authoritative on what the feature does, not independent evidence that it works well. The four customer quotes are vendor-curated testimonials.
- **Scope**: Covers the capability, the partner tool list, the two setup paths, and beta status. It has no config or code. For technical detail I also read the linked docs page (https://platform.claude.com/docs/en/manage-claude/opentelemetry), which supplies the content modes, span names, and limits recorded below. I did not follow the docs sub-pages ("Get Claude SDK spans", "Get Claude API spans", span reference), so per-attribute names beyond those on the overview page are not verified.

## Extracted Claims

### Claim 1: Managed Agents, the Messages API, and the Claude SDKs can now export OpenTelemetry traces to any OTel tool
- **Evidence**: Product announcement (public beta). The docs page gives a coverage matrix: the SDK and the API each cover Messages API requests, Managed Agents turns, and token usage, with different coverage for tools.
- **Confidence**: emerging (first-party, beta, no independent verification)
- **Quote**: "You can now send OpenTelemetry (OTel) traces from Claude Managed Agents, the Messages API, and Claude SDKs to any OTel tool, and follow each step your agents take."
- **Our assessment**: Credible, and it extends the OTel story from Claude Code and Cowork to the API and Managed Agents layer. The post says nothing about reliability, sampling, or overhead.

### Claim 2: Trace scope is every agent turn, model call, and tool use (including MCP server calls), carrying latency, tokens, and IDs
- **Evidence**: Stated in the post. The docs describe `anthropic.session.turn`, `anthropic.model_request`, `anthropic.tool_use <name>`, and `anthropic.custom_tool_use <name>` spans, plus a span per outcome evaluation.
- **Confidence**: emerging
- **Quote**: "every agent turn, model call, and tool use arrives in your observability tool as a standard OpenTelemetry trace, with latency, tokens, and IDs."
- **Our assessment**: This is the concrete answer to the gap recorded in `blog-anthropic-claude-managed-agents.md` Claim 7, which says granularity "is not described in the announcement". The docs list some tool cases where API spans are not emitted ("except in the cases listed in the tool span reference"), so "every" should not be taken as exhaustive. I did not read that reference.

### Claim 3: Traces follow the OpenTelemetry GenAI semantic conventions, so Claude and other providers share dashboards
- **Evidence**: Stated in the post and the docs. The docs name `gen_ai.system_instructions`, `gen_ai.input.messages`, and `gen_ai.output.messages` as the content-bearing attributes on the `anthropic.messages.create` server span.
- **Confidence**: emerging
- **Quote**: "Claude traces follow the OpenTelemetry GenAI semantic conventions, so data from Claude and other providers works in the same tools and dashboards."
- **Our assessment**: Useful for teams running multi-provider stacks. The span names are `anthropic.*`-prefixed, so only attributes, not span names, follow the shared convention. The GenAI conventions were still evolving when this was written, so portability is likely partial.

### Claim 4: There are two export paths. SDKs export automatically, while Managed Agents and the Messages API need a destination added in the Claude Console
- **Evidence**: Post, plus the docs setup table. SDK tracing needs no permission but requires registering a tracer provider in code. API tracing needs the Admin permission in the Console and works for any client. Both together put SDK and API spans in one trace.
- **Confidence**: emerging
- **Quote**: "Managed Agents and the Messages API need a destination in the Claude Console, while Claude SDKs export traces automatically."
- **Our assessment**: The post's "automatically" is loose. The docs say to "Install the SDK and register a tracer provider", so the SDK path is one setup step in code, not zero. The API path is an org-level admin control, which matters for who can turn it on. For Claude Platform on AWS, the API spans land in their own traces rather than joining the SDK trace.

### Claim 5: Trace content defaults to metadata only. Prompts and responses require opting in to Full content
- **Evidence**: Docs only (not in the post). Content modes are `metadata_only` (default) and `content`. Full content spans cap at 0.75 MB by default, and truncation sets `anthropic.content.truncated` to true. Organizations with HIPAA/FERPA/K-12 restrictions export only metadata from destinations. Managed Agents is not eligible for zero data retention.
- **Confidence**: emerging (first-party docs)
- **Quote**: "Your observability platform stores this content under its own access and retention settings, so check that they meet your organization's requirements."
- **Our assessment**: This is the most security-relevant detail and the post omits it. Enabling Full content moves prompts, tool results, and conversations into a third-party store with its own access controls. That is a data-handling decision, not just a debugging toggle.

### Claim 6: Tracing is positioned as a precondition for granting agents more access: review traces, then widen access as the agent proves reliable
- **Evidence**: Assertion in the post, with no data. The Foxglove, Ramp, and accounting-firm testimonials describe use, not a graduated-access result.
- **Confidence**: anecdotal
- **Quote**: "Review its traces, then widen its access as it proves reliable."
- **Our assessment**: This is a reasonable trust-ladder pattern that aligns with the guide's verification theme. No evidence is given that teams do this, or what "proves reliable" means in measurable terms.

### Claim 7: Real traces can be turned into evals and used to measure whether a change helped
- **Evidence**: Post lists eval-oriented partners. Ramp's testimonial says its Reflect system scores Langfuse traces, finds recurring failures, and proposes fixes, with reported token cuts of 10-20% and 30% faster sessions "on some agents".
- **Confidence**: anecdotal (vendor-curated customer quote; numbers unverified and not attributed specifically to OTel export)
- **Quote**: "you can turn real traces into evals, catch quality issues, and measure whether a change helped."
- **Our assessment**: The trace-to-eval loop is plausible and matches the guide's verification chapter. Treat Ramp's numbers as a testimonial. They come from a separate in-house system, not from the export feature.

### Claim 8: Platform and security teams can use exported traces for per-team token attribution and unusual-activity flags (Databricks Unity Gateway)
- **Evidence**: One sentence in the post. No detection logic or thresholds are described.
- **Confidence**: anecdotal
- **Quote**: "Send traces to Databricks Unity Gateway so platform and security teams can see token usage by team and flag unusual activity."
- **Our assessment**: The anomaly detection is Databricks' feature, not Anthropic's. Claude's role is supplying the telemetry. It does show OTel traces as an input to org-wide cost visibility and security monitoring, but it provides no tested pattern.

### Claim 9: Traces let a team answer an auditor about what an agent did from a single timeline, including prompt version, tool calls, latency, and token spend
- **Evidence**: Customer testimonial (Head of Infrastructure at an accounting-software company, Grafana Cloud). The company is named only in the page's testimonial attribution as a title; I did not capture the company name.
- **Confidence**: anecdotal
- **Quote**: "so when an auditor asks what an agent did and why, we can answer from one timeline."
- **Our assessment**: Illustrates the audit use case. The claim that "prompt version" is in the trace is the customer's, and I could not confirm from the docs I read which attribute carries it (possibly a customer-set attribute).

## Concrete Artifacts

Span hierarchy for a Messages API tool-runner request, from the docs page (https://platform.claude.com/docs/en/manage-claude/opentelemetry), source column as published:

```
answer_question                         (your code)  starts the trace
  anthropic.messages.tool_runner        (SDK)
    anthropic.messages.create CLIENT    (SDK)
      anthropic.messages.create SERVER  (API)
        anthropic.model_request         (API)
        anthropic.tool_use web_search   (API)
        anthropic.model_request         (API)
    anthropic.custom_tool_use get_weather (SDK)
    anthropic.messages.create CLIENT    (SDK)
      anthropic.messages.create SERVER  (API)
        anthropic.model_request         (API)
```

Managed Agents session spans named in the docs: `anthropic.sessions.events.stream`, `anthropic.sessions.events.list`, `anthropic.sessions.events.send` (each with CLIENT and SERVER variants), `anthropic.session.turn` (the stop reason `requires_action` ends a turn when a custom tool is requested), and `anthropic.custom_tool_use <name>`.

Docs content-mode and limit settings: `metadata_only` (default) vs `content` in the SDK; `traces.max_content_bytes` in the SDK; "Maximum content size in MB" under Advanced settings in the Console; `anthropic.content.truncated` attribute.

Partner tools listed in the post: Grafana Cloud, Honeycomb, Sentry, Splunk; Arize AI, Braintrust, Datadog, Langfuse, LangSmith by LangChain, New Relic, PostHog; Databricks Unity Gateway; any OTLP endpoint.

## Cross-References

- **Corroborates**: `blog-anthropic-cowork-enterprise.md` Claim 3 (Cowork emits OTel events that feed SIEM pipelines). This post says Claude Code and Cowork traces and the new platform traces can land in the same tool. `blog-anthropic-claude-apps-gateway.md` Claim 6 (Claude Code telemetry relayed over OTLP to an operator-run collector): same export standard.
- **Contradicts**: None found. No filed contradiction.
- **Extends**: `blog-anthropic-claude-managed-agents.md` Claim 7, which says execution tracing is in the Console but its granularity is "not described in the announcement". This post and its docs partly fill that gap with span names, content modes, and export. It does not contradict that note's assessment. It also extends `blog-anthropic-connector-observability.md`, which covers connector-developer dashboards and not agent-level tracing. `blog-ghaw-agent-observability.md` is a different product (GitHub Agentic Workflows).
- **Novel**: The content-mode data-handling model (metadata by default, opt-in full prompts, truncation, ZDR and HIPAA interactions); the SDK-span vs API-span split with joined traces; the "trace first, widen access later" framing; the eval-from-traces loop as a first-party-supported workflow.

## Guide Impact

- **Chapter 03 (verification)**: Add a short pointer that production OTel traces (turn, model-call, and tool-use spans) can be exported to eval tools such as Braintrust or Langfuse and converted into evals. Cite this note, labeling Ramp's numbers as a vendor testimonial.
- **Chapter 06 (security)**: Add tracing of tool and MCP calls as a monitoring control, and warn that enabling Full content sends prompts and tool results to a third-party store (Claim 5). Cite docs-derived details, not the post.
- **Chapter 05 (team adoption)**: Per-team token attribution via exported traces (Claim 8) is a candidate mention for org visibility. It is thinly evidenced.
- **Chapter 02 (harness engineering)**: Note that the managed agent loop now exposes turn-level spans, which resolves the open question recorded under `blog-anthropic-claude-managed-agents.md` Claim 7.

## Extraction Notes

- Fetched the article page directly and read its full text, including all four testimonials. The WebFetch summary tool paraphrased the page, so every quote above was re-verified against the raw page text and the docs page text.
- Read the docs overview page (get-started table, content modes, limits, two example traces). Did not follow the SDK/API span reference sub-pages.
- Post is thin on technical detail, so most claim-grade detail comes from the docs page. Testimonials are treated as vendor-curated, not independent practitioner evidence.
- Public beta as of 2026-10-14; details may change.
