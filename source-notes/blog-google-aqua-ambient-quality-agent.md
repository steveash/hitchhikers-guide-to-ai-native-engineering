---
source_url: https://developers.googleblog.com/the-outer-loop-insights-first-an-ambient-quality-agent-that-diagnoses-your-production-agent/
source_type: blog-post
title: "The Outer Loop, Insights First: An Ambient Quality Agent That Diagnoses Your Production Agent"
author: Dima Melnyk (Product Manager, Cloud AI), Elia Secchi (Solutions Specialist)
date_published: 2026-10-08
date_extracted: 2026-10-09
last_checked: 2026-10-09
status: current
confidence_overall: emerging
issue: "#4014"
---

# The Outer Loop, Insights First: An Ambient Quality Agent That Diagnoses Your Production Agent

> Google announces AQuA, an open reference implementation of a production "outer loop": a sidecar agent that samples live sessions, reviews, clusters, independently verifies and tracks failure patterns, then diagnoses root causes against an immutable deploy-time source snapshot.

## Source Context

- **Type**: blog-post (vendor announcement of an open-source reference implementation, `google/adk-recipes`)
- **Author credibility**: Product manager and solutions specialist on the Google Cloud AI / Gemini platform team that built AQuA. First-hand knowledge of the design; vendor framing. Credits list a large engineering team.
- **Scope**: Architecture of the five-stage sweep, trust/verification design rules, a worked scripted-replay example on `travel-concierge`, cost figures, and open problems. Does not give independent production data; all numbers are vendor-run (scripted replays and an internal benchmark).

## Extracted Claims

### Claim 1: After launch, agent quality can regress silently while every infrastructure health check stays green, because usage drifts and the harness/model/tool/skill layer changes underneath
- **Evidence**: Argument plus two illustrative failures (seat 3A "confirmed" without asking the seat sub-agent; vegan traveler sent a steakhouse). Figures 1-2 (not reproduced). No measured prevalence.
- **Confidence**: emerging
- **Quote**: "when you upgrade a model, update your harness, or change a tool or skill, everything still runs and health checks stay green (Figure 2), but conversation quality and task success may shift in ways a standard deploy pipeline never warns you about."
- **Our assessment**: Plausible and consistent with practitioner experience; extends the inner-loop eval story into production. The "first 80% / last 20%" framing is narrative, not evidence.

### Claim 2: Diagnosing a bad session requires separating model, harness, tool-contract, and instruction/skill failures, which have different owners, and that requires reading trajectories alongside the exact code revision that produced them
- **Evidence**: Four-layer taxonomy given in the post; reasoning, no data.
- **Confidence**: emerging
- **Quote**: "A raw trajectory records what happened next to what, not what caused what. Telling those layers apart requires reading the failing trajectories alongside the exact code revision that produced them."
- **Our assessment**: A useful, reusable failure taxonomy for the harness chapter. The causal claim (need the code revision) is sound; it is the justification for the deploy-time snapshot design.

### Claim 3: A five-stage sweep pipeline (Sample → Review → Cluster → Verify → Track) turns raw production sessions into verified, tracked insights
- **Evidence**: Pipeline description plus the travel-concierge walk-through (see Concrete Artifacts).
- **Confidence**: emerging
- **Quote**: "Each run reads a sample of recent sessions and puts it through a five-stage pipeline:"
- **Our assessment**: The most reusable artifact. Stage details: random sample of up to 1,000 sessions; nine-point checklist (procedure, tool selection and arguments, grounding, task completion, others) producing actual/expected findings; cluster by shared failure mechanism; verifier; tracking. Pipeline shape is portable beyond Google Cloud.

### Claim 4: Clusters must be verified by a separate model against full transcripts before they enter the queue; unverified hypotheses must never look like verified findings
- **Evidence**: Verifier checks each cluster against up to three full transcripts and sub-agent definitions. In the worked example it rejected 3 of 9 clusters (two where the user explicitly asked to skip a step; one where clustering merged unrelated mismatches from two sub-agents). On an "87-trace internal benchmark" it rejected 4 of 24 candidate clusters (not independently reproducible).
- **Confidence**: emerging
- **Quote**: "Clusters are claims until verified against full transcripts."
- **Our assessment**: Strong design rule. The false-positive categories are informative (legitimate user override; over-merging). Note the verifier checks up to three transcripts per cluster, so trace count is a priority signal, not a verified count, which the post states itself. No false-negative rate is reported.

### Claim 5: Insights should be their citations, not a self-reported confidence score; root-cause citations are machine-validated against the snapshot
- **Evidence**: Schema design claim: no confidence field; each occurrence links session IDs; root causes cite `<path>:<start>-<end>` validated server-side against the revision's snapshot; citations to nonexistent files/lines are rejected.
- **Confidence**: emerging
- **Quote**: "An insight is its citations, not a self-reported confidence score."
- **Our assessment**: Good transferable pattern (grounding via validated citations rather than model-stated confidence). Vendor-described; implementation is open so checkable.

### Claim 6: Insights are tracked across runs as NEW / RECURRING / auto-RESOLVED after 14 days unseen, with permanent dismissal for by-design behavior
- **Evidence**: Stage 5 description; "Dismiss" behavior described under trust rules. Run records also explicitly record rejected clusters, clusters past the 50-cluster cap, rubric errors, and empty/uncaptured trace windows.
- **Confidence**: emerging
- **Quote**: "Matches surviving clusters against open insights (verified issues tracked across runs) in BigQuery as NEW, RECURRING, or auto-RESOLVED after 14 days unseen."
- **Our assessment**: Turns one-off audits into a queue with lifecycle, which is what makes on-call triage workable. The 14-day window is an arbitrary default and will not suit low-traffic agents.

### Claim 7: The quality agent runs outside the request path and never writes back to the agent or applies fixes itself
- **Evidence**: Architecture statement; root-cause stage "never applies an edit or opens a pull request on its own"; for out-of-repo faults it attributes to a trajectory step without a diff.
- **Confidence**: emerging
- **Quote**: "AQuA never sits in the request path or writes back to your agent."
- **Our assessment**: Clear human-in-the-loop boundary; the fix path goes through a human or a separate coding agent. Compare the anomaly-detection note, where findings can optionally gate tool calls via callback (that note, Claim 9) — a deliberate contrast in posture.

### Claim 8: Root-cause diagnosis is anchored to the immutable source snapshot captured at deploy time, keyed by deployment revision
- **Evidence**: `agents-cli deploy` writes a snapshot to Cloud Storage keyed by revision. Worked example: 33-file snapshot; the diagnosis agent traced the seat bypass to `travel_concierge/sub_agents/planning/prompt.py` line 93 and the vegan bug to `inspiration/prompt.py` line 23.
- **Confidence**: emerging
- **Quote**: "AQuA reads the failing trajectories alongside the immutable source snapshot captured at deploy time"
- **Our assessment**: Novel and practical: avoids diagnosing live traces against drifted `main`. Applicable to any harness by tagging traces with a revision and archiving the source.

### Claim 9: Multi-agent failures cluster at sub-agent boundaries (dropped context across handoffs; prompt/toolset contradictions)
- **Evidence**: Worked example of 6 verified issues: seat check bypass (15 of 32 sessions), vegan constraint dropped across `inspiration_agent → place_agent` (7), `poi_agent` prompt requires map/place fields but is declared with `tools=[]` so it fabricates `https://example.com/...` URLs (5). Scripted replay of four journeys, not real traffic.
- **Confidence**: anecdotal
- **Quote**: "place_agent is wrapped as an isolated tool whose prompt never receives that profile."
- **Our assessment**: Concrete, believable failure patterns for sub-agent design (isolated sub-agents need explicit context passing; lint prompts against declared tools). Sample is synthetic, so frequencies mean nothing.

### Claim 10: Fixing two one-line prompt defects found by the pipeline improved the replayed sessions (vendor-run)
- **Evidence**: After fixes and a Revision 2 deploy, replaying the same 32 sessions: seat bypass 15→2 sessions (stated as 87% drop), vegan omissions 7→0, full-session pass 5/32→13/32.
- **Confidence**: anecdotal
- **Quote**: "Full-session pass count more than doubles, from 5/32 to 13/32."
- **Our assessment**: Demonstrates the closed loop, but the replay uses the same sessions that surfaced the bugs (no held-out set), the judge is the same family, and n=32. Treat as illustration. (The triage comment expected no measured results; this one small before/after exists and is flagged here.)

### Claim 11: Running the sweep is cheap enough to schedule, but cost scales with trajectory depth
- **Evidence**: Reported: 96-session single-agent sweep cost $0.70 (~$0.007/session); 32-session travel-concierge sweep $3.76 (~$0.12/session, ~50 spans/session); root-cause diagnosis $0.33 to $2.47 per investigated insight. Caps: 1,000 sessions sampled, 50 clusters verified, 3 transcripts per cluster.
- **Confidence**: emerging
- **Quote**: "Root-cause diagnosis (Gemini 3.8 Flash) runs only on demand and costs $0.33 to $2.47 per investigated insight, depending on how many full trajectories it pulls."
- **Our assessment**: Useful order-of-magnitude numbers, at standard Gemini pricing. Whole-transcript review will not scale to hundreds-of-turn coding agents, as the authors concede.

### Claim 12: Open problems: session selection at scale, judge/SME calibration, long-horizon compaction, replay without environment state, and what generalizes across products
- **Evidence**: Authors' own "hard problems" list; reasoning only.
- **Confidence**: emerging
- **Quote**: "outer-loop workflows are often bespoke to a product's tools, domain invariants, data pipelines, and orchestration harness."
- **Our assessment**: Honest limits. Random sampling can miss a regression that breaks 1% of a critical workflow; anomaly-only filtering over-samples duplicates. Static `adk run --replay` diverges when external state changes, so a replay-verified fix is weaker evidence than it looks.

## Concrete Artifacts

Developer goal steering the review (from the post, step 1):

```
Goal: Help travelers move from trip inspiration to a concrete itinerary and confirmed bookings across our sub-agents, with every confirmed flight, hotel, seat, and recommendation grounded in tool results and the traveler's profile.
Failure modes to make sure we cover:
- Mid-conversation changes (a weak spot in pre-launch testing): if a user updates destination, dates, or flight/hotel choices after an initial plan, make sure subsequent sub-agent tool calls and state updates reflect the change.
- Dropped context when handing off or delegating across inspiration_agent, planning_agent, and booking_agent (such as traveler profile preferences or prior selections).
Ignore: tone, greetings, small talk, or sessions where the user browses options and leaves without booking.
```

Structured finding format (actual / expected), from the post:

```
actual: When the user selected outbound flight UA204 and requested seats 3A and 3B in the same turn, planning_agent saved those seat numbers directly to session state without calling flight_seat_selection_agent to check whether 3A and 3B were available.
expected: planning_agent should call flight_seat_selection_agent to verify seat availability and pricing before saving outbound or return seat numbers to session state.
```

Headless coding-agent loop (from the post, step 4):

```
# 1. Pull new insights affecting >= 10 sessions without a root cause
agents-cli aqua list-insights --status NEW --root-cause false \
  | jq -r '.insights | sort_by(-.trace_count) | .[] | select(.trace_count >= 10) | "\(.insight_id)  \(.label)"'
# 2. Trigger root-cause analysis headlessly and fetch the anchored edit + evidence traces
agents-cli aqua run 'Diagnose insight 220d9209e27d4e16a73b4ad4741caa81. What is the root cause, and how would you fix it?'
agents-cli aqua get-insight 220d9209e27d4e16a73b4ad4741caa81 > insight.json
# 3. Extract the user turns from the attached trace in insight.json for local replay (or add to your eval set)
jq '{state: {}, queries: [.occurrences[0].rubrics[0].trace[] | select(.role == "user") | .content]}' \
  insight.json > ./b4b38471-inputs.json
adk run --replay ./b4b38471-inputs.json travel_concierge
```

Worked-example funnel (vendor-run, scripted replay): 32 sessions (1,583 spans) → 5 pass, 27 fail → 42 findings → 9 candidate clusters → verifier rejects 3 → 6 verified issues.

## Cross-References

- **Corroborates**: `blog-ghaw-agent-observability.md` Claim 3 (meta-agent pattern: agents auditing other agents are viable in production) and Claim 5 (observability closing the loop into downstream fixes); AQuA is a more rigorous, verification-gated version of the same idea. `blog-google-agent-anomaly-detection.md` Claim 3 (analysis runs asynchronously, out of band from the live request path) and Claim 7 (layered pipeline, cheap first pass then LLM reasoning on a subset; AQuA instead samples randomly then verifies).
- **Contradicts**: None filed. Terminology: this post uses "inner loop" for pre-launch eval/fix and "outer loop" for production monitoring, which differs from `blog-addyosmani-own-the-outer-loop.md` Claim 1/Claim 2, where the outer loop is the human-owned verdict/accountability layer. This is the terminology divergence tracked in #1943; no `C-NNN` entry exists in CONTRADICTIONS.md, so it is noted here rather than filed again. The two sources are not opposed on substance: AQuA's outer loop produces evidence for a human triager.
- **Extends**: `blog-addyosmani-own-the-outer-loop.md` (supplies a concrete implementation of evidence-producing outer-loop machinery, where that note is conceptual). `blog-google-jules-insight-policy-eval.md` Claim 5 (clustering real history to form ground truth; AQuA clusters live findings by failure mechanism).
- **Novel**: Verify-then-track pipeline with NEW/RECURRING/auto-RESOLVED lifecycle; deploy-time immutable source snapshot with validated line-range citations; "no confidence field" schema rule; sub-agent-boundary failure examples; per-session cost figures for LLM-judge sweeps.

## Guide Impact

- **Chapter 03 (Verification)**: Add a production/"outer loop" subsection describing the Sample → Review → Cluster → Verify → Track pipeline as a pattern, with the rule that clusters are unverified until a separate model confirms them against full transcripts. Mark the effectiveness numbers as vendor-run illustrations.
- **Chapter 02 (Harness Engineering)**: Add the four-layer failure taxonomy (model / harness / tool contract / instructions-skills) and the practice of archiving a source snapshot per deploy revision so traces can be diagnosed against the code that produced them. Add the sub-agent isolation lesson (profile constraints not passed across an isolated sub-agent; prompt demanding fields from an empty toolset).
- **Chapter 05 (Team Adoption)**: Mention a quality-rotation model where an ambient agent prepares case files for the on-call human, and the dismiss/auto-resolve lifecycle that keeps the queue manageable.
- **Terminology (#1943)**: Record this post's usage of inner/outer loop as a third meaning to reconcile.

## Extraction Notes

- Read the full post (fetched raw HTML, stripped to text) and extracted every section. Did not follow the linked repo, "Driving the Agent Quality Flywheel" post, or docs pages; implementation details beyond the post are unverified.
- Figures (1-8) are images and were not inspected; claims rely on the surrounding text only.
- All quotes were copied verbatim from the fetched text. The cross-referenced claim numbers were checked against the headings of the cited notes.
- All results (13/32 pass, 87% drop, cost figures, 4-of-24 rejection) are vendor-asserted and not independently reproducible from the post alone.
