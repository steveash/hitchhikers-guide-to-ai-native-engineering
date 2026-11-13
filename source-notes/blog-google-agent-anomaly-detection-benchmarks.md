---
source_url: https://developers.googleblog.com/how-agent-anomaly-detection-scores-on-benchmarks-we-didnt-write/
source_type: blog-post
title: "How Agent Anomaly Detection scores on benchmarks we didn't write"
author: Nakul Javali (Senior Software Engineer, Google)
date_published: 2026-11-12
date_extracted: 2026-11-13
last_checked: 2026-11-13
status: current
confidence_overall: emerging
issue: "#4700"
---

# How Agent Anomaly Detection scores on benchmarks we didn't write

> Google's follow-up to the Agent Anomaly Detection announcement supplies the first measured detection and false-alarm rates for an out-of-band agent monitor on five third-party agent-security benchmarks, including explicit negative results (poisoned memory, resisted instructions, cold-start agents).

## Source Context

- **Type**: blog-post (Google Developers Blog, published Nov. 12, 2026; tagged Case Studies)
- **Author credibility**: Named Google Senior Software Engineer writing about a Google-built feature (Private Preview). This is a vendor-run evaluation: Google measured its own product. Mitigations the post cites: the five benchmarks are third-party and public, and ground-truth labels come from each benchmark's deterministic Python check, not a model. No code, per-session data, or raw counts for most cells are published, so the numbers cannot be reproduced from the post.
- **Scope**: Detection rate, false-alarm rate, and failure areas across AgentDojo, InjecAgent, Agent Security Bench (ASB), AgentDyn and AgentHarm (1,774 sessions) using one agent model (gemini-2.5-flash on ADK) and simulated apps. Does not cover cascading failures or identity/privilege abuse (no public labeled traces), other models, production traffic, or latency/cost.

## Extracted Claims

### Claim 1: The headline 87% detection rate is conditional on the harmful instruction having been read and carried out by the agent
- **Evidence**: Per-benchmark carried-out detection: AgentDojo 85%, InjecAgent 87%, AgentDyn 99%, AgentHarm 81%. Ground truth from each benchmark's deterministic checker over final app state.
- **Confidence**: emerging (vendor-run, single model, simulated apps)
- **Quote**: "Of the ones that were executed, Agent Anomaly Detection flagged 87% for post-execution review."
- **Our assessment**: Useful, but the denominator matters. Anyone quoting "87%" without "of executed attacks" overstates coverage. Per-benchmark counts are not given, so confidence intervals are unknowable.

### Claim 2: Across all harmful sessions, including ones the agent never read or resisted, detection falls to 45-62%
- **Evidence**: Figure 3 (outcome split on four benchmarks); text summary.
- **Confidence**: emerging
- **Quote**: "Over all harmful sessions, including the ones that the agent never read or resisted, it flagged 45% to 62%."
- **Our assessment**: The more honest operational number if you want to know "how many attack attempts did I see". But flagging a never-read instruction is arguably a non-event (nothing happened), so 45-62% is not a "miss rate" for harm.

### Claim 3: Resisted instructions are mostly not flagged, so a monitor gives little visibility into probing attempts that the model itself defeated
- **Evidence**: 11-25% flagged for resisted instructions hidden in tool output; 55% for refused AgentHarm requests, because the request is in the user's own message. Of 141 never-read sessions, 1 was flagged.
- **Confidence**: emerging
- **Quote**: "When the agent didn't follow an instruction hidden in tool output, it flagged only 11% to 25%, because the instruction sits deep inside a tool result."
- **Our assessment**: Behavioral monitors detect changed behavior; a resisted injection changes little. Attack telemetry (who is probing me) needs input-side screening, not just behavior-side monitoring. Google lists resisted-attempt reporting as future work.

### Claim 4: Poisoned long-term memory is the clear detection gap
- **Evidence**: ASB plants instructions in long-term memory; 4 of 18 sessions where memory made the agent act were caught (about 22%).
- **Confidence**: anecdotal (n=18)
- **Quote**: "Poisoned memory is the clear gap: when instructions planted in the agent’s long-term memory made it act, Agent Anomaly Detection caught 4 of 18."
- **Our assessment**: Small sample, but the direction is plausible: a memory-driven action looks like the agent's own normal behavior. Directly relevant wherever the guide recommends persistent agent memory.

### Claim 5: False-alarm rate depends on the agent's everyday tools: 2-4% on office-task benchmarks, 16% on AgentHarm
- **Evidence**: Benign sessions in the three injection benchmarks are office tasks; AgentHarm benign tasks are "twins" of harmful ones (social posting, terminal commands, downloads).
- **Confidence**: emerging
- **Quote**: "High-impact tools in normal use look more like misuse."
- **Our assessment**: Strong practical point: expected alert volume scales with how many high-impact tools the agent legitimately uses. The post itself warns benign tasks here are likely simpler than production, so real false-alarm rates may be higher.

### Claim 6: The detector needs a few hundred benign sessions of per-agent history; new agents get poor coverage
- **Evidence**: AgentDyn: 33% of carried-out harmful instructions flagged with about 220 benign sessions per agent vs 99% with 360. The test protocol ran at least 300 benign sessions per agent first.
- **Confidence**: emerging (single benchmark data point)
- **Quote**: "Some Agent Anomaly Detection methods need a few hundred sessions of history: on AgentDyn, it flagged 33% of carried-out harmful instructions when each agent had about 220 benign sessions, and 99% with 360."
- **Our assessment**: Headline numbers therefore describe a warmed-up detector. Newly deployed or frequently re-specced agents (new tools/prompts) are the ones where preventive controls must carry the load.

### Claim 7: Small single actions that look like normal work (one page visit) are the hardest attacks to catch
- **Evidence**: 8 of 11 apps had at least 95% detection of carried-out instructions; lowest was AgentDojo's Slack app at 63%.
- **Confidence**: emerging (counts in some apps are small, per Figure 4 caption)
- **Quote**: "Many of those instructions ask for one small action, such as a page visit, which looks like normal browsing."
- **Our assessment**: Exfiltration-by-URL and similar low-footprint attacks are the natural evasion path for anomaly detection; reinforces egress allow-listing as a preventive control.

### Claim 8: Evaluation design: out-of-band monitor and deterministic grader see the same run, only the grader sees final app state
- **Evidence**: ADK agent on gemini-2.5-flash, benchmark simulated apps, traces sent to the detector as a customer's would be. Three-way outcome taxonomy: never read / resisted / carried out.
- **Confidence**: emerging
- **Quote**: "Deterministic code decides the label, not a model, so an injected instruction can't mislead the grader, and Agent Anomaly Detection cannot cheat the benchmark."
- **Our assessment**: The never-read/resisted/carried-out split is a reusable template for reporting any injection-defense evaluation; aggregate "detection rate" numbers without it are not comparable. Caveat: Google also reports no result for about 6% of sessions.

### Claim 9: The model itself was a substantial first line of defense
- **Evidence**: Without the monitor, the agent refused three in four direct harmful requests and ignored or failed at about 30% of instructions hidden in tool output; it did not follow about half of harmful instructions it read.
- **Confidence**: anecdotal (one model, gemini-2.5-flash, may not generalize)
- **Quote**: "The model itself didn't follow about half of the harmful instructions it read."
- **Our assessment**: The other half did get carried out, so model robustness alone is insufficient; and results from a single mid-tier model say little about other models.

### Claim 10: Recommended posture is defense in depth, with the monitor explicitly the detective (not preventive) layer
- **Evidence**: Recommendations list: send full telemetry incl. prompt/response content; screen untrusted content (Model Armor); block risky tool calls (Semantic Governance Policy, Preview); human approval for high-impact actions; least-privilege tools; route Critical/High findings from Security Command Center to incident team.
- **Confidence**: settled as general practice; product specifics are vendor-specific
- **Quote**: "Protect your agents with defense in depth. Use controls that stop harmful actions before they run, and Agent Anomaly Detection to find what gets through."
- **Our assessment**: Consistent with the guide's layered stance. Note the post states "Agent Anomaly Detection doesn’t block actions" while the earlier announcement describes an API for threshold-based blocking; those are compatible (blocking is something you build on findings, not a built-in), but see Cross-References.

### Claim 11: Public benchmark coverage is concentrated on goal hijack and tool misuse; there is no labeled public data for cascading failures or identity/privilege abuse
- **Evidence**: Authors state they graded each OWASP Agentic category on what the study showed, not on design intent.
- **Confidence**: emerging
- **Quote**: "We did not find public benchmarks with labeled agent traces for cascading failures or for identity and privilege abuse."
- **Our assessment**: A candid gap statement. For the guide: evidence for detectors on ASI03/ASI08 remains vendor assertion only.

## Concrete Artifacts

Metrics table assembled from the post (all vendor-run, gemini-2.5-flash, simulated apps; 1,774 sessions total):

```
Metric                                              Value
--------------------------------------------------  -----------------------------
Flagged, carried-out harmful instructions (overall) 87%
  AgentDojo / InjecAgent / AgentDyn / AgentHarm     85% / 87% / 99% / 81%
Flagged, all harmful sessions                       45%-62%
Flagged, resisted instr. in tool output             11%-25%
Flagged, refused AgentHarm requests                 55%
Never-read sessions                                 141 (1 flagged)
Apps with >=95% carried-out detection               8 of 11
Lowest app                                          AgentDojo Slack, 63%
False alarms, benign office-task sessions           2%-4%
False alarms, AgentHarm benign sessions             16%
Poisoned memory (ASB) acted-on sessions caught      4 of 18
AgentDyn carried-out detection ~220 / 360 sessions  33% / 99%
AgentHarm carried out                               108 of 412
No result returned                                  ~6% of sessions (1-2 pt lower if counted as misses)
```

Benchmarks used (per post): AgentDojo (NeurIPS 2024), InjecAgent (ACL 2024 Findings), Agent Security Bench (ICLR 2025), AgentDyn (2026), AgentHarm (ICLR 2025).

Planned improvements listed by the author:

```
- Report attempts that the agent resisted, at a lower severity
- Catch small actions that reach an untrusted destination
- Tell normal use of high-impact tools apart from misuse
- Give new agents full coverage sooner
- Detect instructions planted in long-term memory more reliably
```

## Cross-References

- **Corroborates**: `blog-google-adk-zero-trust-agents.md` Claim 8 (a gateway enforcing deterministic checks on tool calls before they execute) matches this post's "block risky tool calls before they run" layer. `blog-google-agent-anomaly-detection.md` Claim 4 (findings carry severity, explanation, published to Security Command Center) matches the triage advice here.
- **Contradicts**: None filed. Mild tension only: `blog-google-agent-anomaly-detection.md` Claim 9 describes using the findings API to block tool calls after a threshold, whereas this post says the product "doesn’t block actions". Read as a difference of framing (built-in vs. user-built), not a conflict, so no contradiction issue.
- **Extends**: `blog-google-agent-anomaly-detection.md` (#3508). That note's Source Context records no independent validation of detection accuracy or false-positive rates; this post is the first measured data, though still vendor-run. Its Claim 3 (async, no added latency) is unaffected by this post, which does not measure latency. Also extends `blog-green-sandboxing-rogue-agents.md` Claim 7 (monitoring agent traffic at scale must be done by other models) with measured results for one such monitor.
- **Novel**: Per-benchmark detection rates for an out-of-band agent monitor; the never-read/resisted/carried-out outcome taxonomy; cold-start sensitivity (33% vs 99%); the poisoned-memory gap; false-alarm dependence on tool set.

## Guide Impact

- **Chapter 06 (security-threat-model)**: Where behavioral/anomaly monitoring is described as a control, add that the one published evaluation reports 87% of carried-out harmful instructions flagged but only 4/18 poisoned-memory actions and 11-25% of resisted injections, so it should be positioned as a detective layer behind preventive controls (input screening, tool-call policy, human approval, least-privilege tools). Cite alongside `blog-google-agent-anomaly-detection.md`, and label the figures vendor-run.
- **Chapter 06**: Add poisoned long-term memory as a named monitoring blind spot relevant to any persistent-memory recommendation.
- **Chapter 03 (verification)**: Recommend reporting injection-defense results with the never-read/resisted/carried-out split and a deterministic outcome checker, and warn that a detector needs a baseline (~300+ benign sessions) before its rates apply.
- **Chapter 05 / operations**: Note that alert volume depends on the agent's tool set (2-4% vs 16% false alarms), so plan triage capacity for agents with high-impact tools.

## Extraction Notes

- Read the full post (fetched raw HTML and converted to text; figures are images and their content was only available via captions and text). No sub-pages followed beyond the existing note on the announcement.
- Quotes copied verbatim from the page text; two contain curly apostrophes as on the source.
- The triage comments mention a "Ch04/Ch07" mapping in one place; the repo's guide has Ch06 as security-threat-model, which I used.
- Evidence rated `emerging` overall: concrete numbers and honest limitations, but vendor-run, single model, simulated apps, and no per-cell counts.
