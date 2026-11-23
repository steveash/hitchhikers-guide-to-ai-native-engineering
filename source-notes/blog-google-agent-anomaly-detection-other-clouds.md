---
source_url: https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds/
source_type: blog-post
title: "Agent Anomaly Detection: Safeguarding agents across other clouds"
author: Gopi Subburaja Alagar and Arvind Chaudhary (Software Engineers, Google)
date_published: 2026-11-20
date_extracted: 2026-11-23
last_checked: 2026-11-23
status: current
confidence_overall: anecdotal
issue: "#4910"
---

# Agent Anomaly Detection: Safeguarding agents across other clouds

> Google's follow-up showing that its out-of-band behavioral monitor can analyze ADK agents running on AWS Lambda and Microsoft Foundry by ingesting OpenTelemetry traces/logs via the Telemetry API with Workload Identity Federation, backed by two small single-run test scenarios (not benchmarks).

## Source Context

- **Type**: blog-post (first-party Google Developers Blog, Private Preview product follow-up)
- **Author credibility**: Two named Google software engineers describing a Google-built feature. Vendor-authored; no independent validation.
- **Scope**: Covers the telemetry requirements for off-Google-Cloud agents, the env-var setup, and two scripted test scenarios (AWS Lambda inventory agent; Foundry customer-service agent). Does NOT give false-positive rates, detection rates, or session counts beyond those quoted. Setup details are deferred to external docs.

## Extracted Claims

### Claim 1: Detection works wherever the agent runs, because it consumes traces and logs rather than runtime access
- **Evidence**: Architectural statement; demonstrated on AWS Lambda and Microsoft Foundry.
- **Confidence**: emerging
- **Quote**: "Agent Anomaly Detection works from an agent's traces and logs, so it doesn't need access to the agent's runtime."
- **Our assessment**: Plausible and consistent with the out-of-band design in the launch note. The only demonstrated platforms are Lambda and Foundry; on-prem is mentioned but not shown.

### Claim 2: Three telemetry requirements: Telemetry API ingestion, OpenTelemetry conventions with prompts/responses as log events, and a resource attribute naming the agent
- **Evidence**: Stated requirements list.
- **Confidence**: emerging
- **Quote**: "It arrives through the Telemetry API (telemetry.googleapis.com), which keeps the resource attributes that identify the agent."
- **Our assessment**: Useful concrete checklist. Message content must be exported, which has a privacy consequence (prompts/responses are shipped to a Google Cloud project) that the post only touches on.

### Claim 3: Off-cloud agents authenticate via Workload Identity Federation, so no service-account key is needed
- **Evidence**: Setup description; config file said to contain no secret.
- **Confidence**: emerging
- **Quote**: "With Workload Identity Federation, the agent trades its own identity, such as an AWS role or a Microsoft Entra identity, for short-lived Google credentials."
- **Our assessment**: Good security practice (short-lived credentials over long-lived keys). Note the env var `GOOGLE_APPLICATION_CREDENTIALS` still points at a credentials file; the post says that file "contains no secret".

### Claim 4: Only telemetry leaves the agent's cloud; model and tool calls stay put, and analysis does not slow the agent
- **Evidence**: Architecture statement; no latency measurements.
- **Confidence**: anecdotal
- **Quote**: "The agent's model and tool calls still run where the agent runs. Only telemetry, including the prompts and responses that Agent Anomaly Detection reads, goes to your Google Cloud project."
- **Our assessment**: The latency point is true by construction (out-of-band), but it is not a prevention layer. Data-residency teams should note that full prompt/response content crosses clouds.

### Claim 5: On Lambda, only the scraping session was flagged although no call failed
- **Evidence**: Two scripted sessions with one tool, `list_inventory`: a shopper checking a few items and a scraper requesting 100 items at increasing offsets. Both used permitted calls.
- **Confidence**: anecdotal (one run, two sessions, scripted by the vendor)
- **Quote**: "Of the two sessions, Agent Anomaly Detection flagged only the scraper's. No call failed, but the whole exchange showed systematic scraping."
- **Our assessment**: Illustrates that pattern-and-intent, not per-call validity, is the signal. n=2 and scripted, so it shows the mechanism can work, not how often.

### Claim 6: Detection is claimed to be model-agnostic; Amazon Nova Lite flagged 10 of 40 sessions, some with no errors
- **Evidence**: Same agent on Nova Lite via Bedrock; 10/40 flagged; some started as routine questions and the model paged the whole catalog until timeout.
- **Confidence**: anecdotal
- **Quote**: "Detection doesn't depend on the agent's model."
- **Our assessment**: One model, one run, no ground-truth labels, so 10/40 is not a detection rate and cannot be read as precision or recall. It also shows that the benign-user sessions can be anomalous because of the model's own behavior, i.e. the monitor catches model-induced resource exhaustion, not only attacks. Contrast the launch/benchmarks notes, which gave real accuracy figures.

### Claim 7: On Foundry, four of six sessions that pushed the agent past its role were flagged, including privilege abuse and prompt injection via an order note
- **Evidence**: Six scripted sessions (two normal, four adversarial). Agent was told to carry out every request without validation. Admin-impersonation session refunded 10x order totals ($1,784.90 total); "SYSTEM OVERRIDE" order note produced a $999 refund on a $15.99 order.
- **Confidence**: anecdotal
- **Quote**: "The other four pushed the agent past its role, and Agent Anomaly Detection flagged all four."
- **Our assessment**: Note the setup is deliberately permissive ("which we told to carry out every request without validation"), so the agent is a worst-case victim and the test shows detection after the fact, not that the agent was hard to attack. Triage framing of "4 of 6 flagged" is slightly off: all four adversarial sessions were flagged and neither normal session was, so it is 4/4 adversarial, 0/2 false positives, on a tiny sample.

### Claim 8: Recommendations returned are concrete mitigations (validate tool arguments, block override patterns, threshold-gate refunds, rate-limit tools)
- **Evidence**: Findings text for both scenarios.
- **Confidence**: anecdotal
- **Quote**: "It recommended validating issue_refund arguments to block override patterns in order notes, and requiring extra validation for refunds above a set threshold."
- **Our assessment**: The monitor is detective; the fixes are preventive controls the team must implement. Matches the defense-in-depth posture in the benchmarks note.

### Claim 9: Scope limits: ADK for Python only; findings for off-cloud agents appear only in the Agent Anomaly Detection console; Private Preview
- **Evidence**: Stated limitations.
- **Confidence**: settled (as a statement of current product scope)
- **Quote**: "Findings for agents outside Google Cloud appear only in the Agent Anomaly Detection console."
- **Our assessment**: Means off-cloud findings apparently do not feed Security Command Center, which weakens the SOC-integration story from the launch note (Claim 4 there). The post is silent on this beyond the console statement, so treat as inference.

## Concrete Artifacts

Environment variables, verbatim from the post's "Connect an agent from another cloud" section:

```
GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
GOOGLE_APPLICATION_CREDENTIALS=/path/to/gcp-credentials.json
# Capture prompts and responses in the format Agent Anomaly Detection reads.
OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental
OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=EVENT_ONLY
ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false
# Describe the agent and where it runs.
OTEL_SERVICE_NAME=<AGENT_NAME>
OTEL_RESOURCE_ATTRIBUTES=cloud.provider=<aws|azure>,cloud.platform=<PLATFORM>,cloud.region=<REGION>,faas.name=<AGENT_NAME>
```

Reported results (post's "What we tested"):

```
Scenario                     Platform / model        Sessions   Flagged
Inventory agent (list_inventory)  AWS Lambda          2          1 (scraper only)
Inventory agent               Lambda + Amazon Nova Lite (Bedrock)  40  10
Customer-service (get_order_status, issue_refund)  Microsoft Foundry  6  4 (all adversarial)
Discovery: agent appears in Monitored agents list within 30 minutes
```

## Cross-References

- **Corroborates**: `blog-google-agent-anomaly-detection.md` Claim 2 (analysis of reasoning traces/tool calls across a full session from existing OpenTelemetry data), Claim 3 (out-of-band, no added latency) and Claim 8 (inventory scraping worked example); `blog-google-agent-anomaly-detection-benchmarks.md` Claim 10 (monitor is the detective layer in defense in depth).
- **Contradicts**: None filed. Version discrepancy (not a substantive contradiction): the launch note Claim 10 and hands-on note state ADK 1.2+ for Google Cloud agents, whereas this post requires "ADK for Python, version 2.12.0 or later" for the other-cloud exporters. Likely different requirements for different paths (the hands-on note prefers 2.0+); unresolved and flagged for the Smith.
- **Extends**: `blog-google-agent-anomaly-detection-hands-on.md` Claim 3 (three env vars for telemetry/content capture) by adding the cross-cloud env set and WIF; Claim 4 there (discovery via telemetry only) is echoed by the 30-minute discovery window here.
- **Tension (mild)**: `blog-google-agent-anomaly-detection-benchmarks.md` Claim 5 reports a 2-4% to 16% false-alarm rate and Claim 2 says detection falls to 45-62% across all harmful sessions; this post's tidy 4/4 and 0/2 results come from scripted, obvious attacks and should not be weighed against those figures.
- **Related**: `blog-google-semantic-governance-policies.md` (the preventive counterpart published the same day).
- **Novel**: Cross-cloud telemetry path with Workload Identity Federation; a "no error, no blocked call" resource-exhaustion case caused by a weaker model's own behavior; an injection-via-data (order note) refund example.

## Guide Impact

- **Chapter 06 (security-threat-model)**: Where the runtime-monitoring layer is described, add that behavioral monitors can be run out-of-band over OpenTelemetry from agents on other clouds, and cite the "no error, no blocked call" Nova Lite sessions as an example of model-induced runaway behavior. Keep the claim labelled vendor-reported, single-run.
- **Chapter 06**: Use the "SYSTEM OVERRIDE" order-note refund as a concrete injection-via-tool-data example, noting the test agent was instructed to skip validation.
- **Chapter 03 (verification)**: Post-deployment session-level review complements per-call checks; cite the scraper-vs-shopper pair (same tool, same permitted calls, different pattern).
- **Do not** cite 10/40 or 4/6 as detection rates.

## Extraction Notes

- Fetched the page directly and read the full text (the WebFetch summarizer would not return verbatim text, so quotes were copied from the raw HTML-to-text extraction). Images (console screenshots) were not viewable; only their captions were read.
- Did not follow the external setup guide/docs links (not given as URLs in the page text).
- Triage described the Foundry result as "4 of 6 sessions flagged"; the post itself says two sessions were normal and the four adversarial ones were all flagged.
- No contradiction issue filed: the ADK version difference is a context difference, flagged above.
