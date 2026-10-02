---
source_url: https://simonwillison.net/2026/Sep/24/datasette/
source_type: blog-post
title: "datasette 1.0a41"
author: Simon Willison
date_published: 2026-09-24
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: anecdotal
issue: "#3851"
---

# datasette 1.0a41

> A two-sentence release "beat" announcing OpenTelemetry support in Datasette (contributed by Alex Garcia) and a shared modal-dialog Web Component for plugins; the Datasette changelog supplies the only substantive detail, and none of it concerns AI-agent usage directly.

## Source Context

- **Type**: blog-post (a "beat", Simon Willison's short release-announcement format). The post body is two sentences with no code, metrics, or rationale. The Datasette changelog entry for 1.0a41 was also read for detail.
- **Author credibility**: Creator and maintainer of Datasette; first-party release announcement. The OpenTelemetry work is credited to Alex Garcia.
- **Scope**: Announces two changes. Does NOT discuss how the telemetry is used with AI agents, design rationale, or any coding-agent workflow. This source is thin; the Pre-screen comment on the issue flagged it as a tool announcement with little extractable guidance.

## Extracted Claims

### Claim 1: Datasette gained OpenTelemetry support in 1.0a41
- **Evidence**: Release announcement; changelog says traces cover HTTP requests, database queries and startup (including time waiting for SQL threads and queued writes), and metrics cover query latency, time-limit interruptions, SQL thread usage, write queues and open connections.
- **Confidence**: settled (first-party release fact)
- **Quote**: "Alec Garcia added"
- **Our assessment**: Quote is only a fragment; the blog post spells the name "Alec Garcia" while the changelog says "Alex Garcia" (likely a typo in the post, unverified). Factual release information; useful only as a data point that a small, agent-adjacent data tool exposes standard OTel traces/metrics. No evidence here of agent-specific use.

### Claim 2: Datasette's modal dialogs were consolidated into one documented Web Component for plugins
- **Evidence**: Changelog: "New DatasetteModal JavaScript API for plugins to create dialogs with Datasette's shared styles, keyboard behavior and focus handling. Datasette's built-in dialogs use the same API."
- **Confidence**: settled (first-party release fact)
- **Quote**: "I've also refactored all of Datasette's modal dialogs to a single Web Component"
- **Our assessment**: Plugin-extensibility detail ("dogfooding" the plugin API for built-ins). Not relevant to AI-native engineering guidance on its own.

## Concrete Artifacts

```
From the Datasette changelog (https://docs.datasette.io/en/latest/changelog.html), 1.0a41 (2026-09-24):
"To collect telemetry, configure an OpenTelemetry SDK and exporter, then run Datasette using opentelemetry-instrument."
```

## Cross-References

- **Corroborates**: none.
- **Contradicts**: none.
- **Extends**: `blog-simonwillison-datasette-1-0a39.md` and `blog-simonwillison-datasette-1-0a38.md` (earlier releases in the same 1.0 alpha series; this note adds only release-level facts). Note: no `1.0a40` note exists in the corpus at time of writing.
- **Novel**: Nothing substantive; first corpus mention of Datasette's OpenTelemetry support.

## Guide Impact

- No chapter change recommended. The triage suggested Ch02/Ch04/Ch05 observability relevance, but the source provides no agent-specific observability guidance. If a chapter on observability cites Datasette as an example of OTel adoption, this note can serve as a pointer only.

## Extraction Notes

- The post itself is two sentences; extraction depth is limited by the source. The changelog page was read for supporting detail; the full OpenTelemetry docs page was not followed.
- Recommend the Assayer/Smith treat this as low value; it is filed for completeness since the issue was triaged for mining.
