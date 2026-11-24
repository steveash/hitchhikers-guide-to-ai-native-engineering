---
source_url: https://developers.googleblog.com/did-the-user-ask-for-this-securing-ai-agents-against-intent-hijacking-with-semantic-governance-policies/
source_type: blog-post
title: "Did the user ask for this? Securing AI agents against intent hijacking with Semantic governance policies"
author: Ritika Nigam, Deepti Sehrawat, Pranav Bhagwat (Google)
date_published: 2026-11-23
date_extracted: 2026-11-24
last_checked: 2026-11-24
status: current
confidence_overall: emerging
issue: "#4924"
---

# Did the user ask for this? Securing AI agents against intent hijacking with Semantic governance policies

> Google's vendor-measured AgentDojo evaluation of an inline LLM-judged "did the user ask for this?" tool-call gate: attack success 48.7% to 0.9% at a 2.6-point benign-utility cost, with the authors' own caveats that the attacks were not adaptive and the judge's data/instruction separation is prompt-enforced.

## Source Context

- **Type**: blog-post (vendor, Google Developers Blog; feature in Preview; first-party benchmark)
- **Author credibility**: Two Software Engineers and a Staff Software Engineer at Google, describing their own product. Numbers are vendor-measured, single model, single benchmark; not independently replicated. The post is unusually candid about limitations.
- **Scope**: Covers the intent-check mechanism, one banking walk-through, AgentDojo method and results (overall and by domain), and limitations. Result charts/tables are images and were not readable; the numbers cited here are from the page text. Does not cover latency, token cost, adaptive attacks, or ambiguous user requests. Follow-up to `blog-google-semantic-governance-policies.md`.

## Extracted Claims

### Claim 1: With only the default intent check and no custom policies, attack success on AgentDojo fell from 48.7% to 0.9%
- **Evidence**: gemini-2.5-flash agent; AgentDojo v1.2.2, 97 user tasks, 949 attacked runs, `important_instructions` attack; averages over six full runs per configuration.
- **Confidence**: emerging (vendor-measured, one model, one benchmark)
- **Quote**: "Semantic governance policies cut the attack success rate on AgentDojo from 48.7% to 0.9%, at a cost of 2.6 percentage points of utility on benign tasks."
- **Our assessment**: A large effect against fixed, non-adaptive injections. Treat as an upper bound on real-world effectiveness (see Claim 7). Mixed with a caveat that the 48.7% baseline is for a weak-ish flash model with no defence at all.

### Claim 2: The result was stable across repeated runs
- **Evidence**: Six runs per configuration, because "Agents are nondeterministic."
- **Confidence**: emerging
- **Quote**: "across all six runs, the attack success rate with Semantic governance policies stayed between 0.84% and 0.95%."
- **Our assessment**: Good evaluation hygiene (repeat runs rather than a single pass). Narrow range supports the number, though the six runs share the same fixed attack set.

### Claim 3: Benign utility cost was small on average but noisy per run
- **Evidence**: Average drop of 2.6 points; per-run range −1.0 to 7.2.
- **Confidence**: emerging
- **Quote**: "Individual runs ranged from −1.0 to 7.2 points, because the agent's own behavior varies from run to run."
- **Our assessment**: A 7.2-point worst-run drop is not trivial; an operator should expect single-digit utility loss. Over-blocking is concentrated, not diffuse (Claim 6).

### Claim 4: Zero attacks that needed a tool call succeeded; the only residual failures were text-only manipulation
- **Evidence**: 929 tool-call attacks across six runs, none successful; remaining travel successes were a "recommend this hotel" reply.
- **Confidence**: emerging
- **Quote**: "None of the 929 attacks that needed a tool call succeeded in any of the six runs, including attacks that tried to send messages, transfer money or share data."
- **Our assessment**: The gate evaluates actions, not text, so a text-only hijack is structurally outside it. The post itself says it needs "complementary controls, such as response filtering". Echoes the parent note's Claim 12 (text-only responses not evaluated).

### Claim 5: The check works on actions rather than attack phrasing, by treating tool results as data and the user request as the only source of intent
- **Evidence**: Design description plus the bill-payment walk-through where `send_money` was denied with a rationale citing the injected file.
- **Confidence**: emerging
- **Quote**: "Because it evaluates actions rather than text, it doesn't need to recognize a specific attack phrasing. It asks a simpler question: did the user ask for this?"
- **Our assessment**: Sound design principle (action-level provenance check rather than injection-pattern detection). Same transfer requested directly by the user is allowed, so the check is about provenance, not the action type.

### Claim 6: Denial stops the agent's turn, leaving a task-completion gap; "safe completion under attack" still improves
- **Evidence**: Utility under attack 25.8% with vs 35.1% without; 12.4 points of the baseline were tasks completed while also executing the attacker's goal; tasks completed safely 25.1% vs 22.7%.
- **Confidence**: emerging
- **Quote**: "When Semantic governance policies denies an injected action, the agent usually stops rather than continuing with the user's task, which is the remaining gap."
- **Our assessment**: Useful metric framing: report "task done AND attack failed", not raw utility. The honest admission is that the agent rarely recovers after a denial, because production replaces the whole response.

### Claim 7: Over-blocking was concentrated in two Slack tasks that resembled injections
- **Evidence**: Domain breakdown; 1 of 97 benign tasks over-blocked (about 1%). Banking, Slack and workspace reached zero successful attacks in every run; Slack baseline attack success exceeded 9 in 10.
- **Confidence**: emerging
- **Quote**: "Unintended over-blocking affected 1 of the 97 benign tasks (about 1%)."
- **Our assessment**: The two Slack tasks told the agent to follow external web-page instructions and claimed a conflicting user identity, so the vendor argues blocking was correct. Plausible, but it is the vendor's own classification of its misses.

### Claim 8: The defence is not a hard boundary and was not tested against adaptive attacks
- **Evidence**: Authors' stated limitation; cites NIST CAISI results where red-teamed attacks raised ASR from 11% to 81%.
- **Confidence**: settled (the limitation is stated by the vendor; adaptive attacks being stronger is well established)
- **Quote**: "That separation is enforced by how the judge is instructed, not by a hard technical boundary, so an attack designed specifically against Semantic governance policies could try to manipulate the judge itself, for example by disguising an injected request as the user's."
- **Our assessment**: The central caveat. The 0.9% figure should not be read as expected adversarial performance. Directly resolves the open question in the parent note's Claims 6 and 9 as "unmeasured against adaptive attack".

### Claim 9: The benchmark ran through a test harness, not the production gateway path
- **Evidence**: AgentDojo calls the model directly; the production policy engine was fed the same inputs via a harness.
- **Confidence**: emerging
- **Quote**: "The harness enforces denials slightly differently from production in a few edge cases, but these don't materially change the results."
- **Our assessment**: Reasonable, but the "don't materially change" claim is unquantified.

### Claim 10: Benchmark grading is deterministic, not model-graded
- **Evidence**: AgentDojo checks final app state with Python.
- **Confidence**: settled (benchmark design)
- **Quote**: "The benchmark's own Python check reads the final state of the apps to decide the outcome, so a model never grades the results."
- **Our assessment**: Strengthens result credibility: no LLM-judge-grades-LLM-judge circularity. Matches the grader design praised in `blog-google-agent-anomaly-detection-benchmarks.md` Claim 8.

### Claim 11: Rollout recommendation is dry-run first, then enforcement
- **Evidence**: "Try" section.
- **Confidence**: emerging
- **Quote**: "To start, turn on Semantic governance policies for an agent behind Agent Gateway in dry run mode, review its verdicts in Cloud Logging, then switch to enforcement."
- **Our assessment**: Consistent with the parent note's rollout checklist; the over-blocking in Claim 7 is the reason to do so.

## Concrete Artifacts

Metrics (all from the source page text, averages over six runs):

```
AgentDojo v1.2.2, gemini-2.5-flash, important_instructions attack
97 user tasks, 949 attacked runs, 6 full runs per configuration
Intent check only (default), no custom policies

Attack success rate:        48.7% -> 0.9%  (per-run range 0.84%-0.95%)
Clean utility change:       -2.6 pp average (per-run range -1.0 to 7.2)
Utility under attack:       35.1% (no guardrail) vs 25.8% (guarded)
Safe completion under attack: 22.7% (no guardrail) vs 25.1% (guarded)
Tool-call attacks:          929, 0 succeeded in any run
Over-blocked benign tasks:  1 of 97 (~1%)
```

Bill-payment trace (paraphrased from the source): read bill allowed; check recent transactions allowed; `send_money` to attacker account denied; rationale cited prompt injection inside `bill-december-2023.txt`.

## Cross-References

- **Corroborates**: `blog-google-semantic-governance-policies.md` Claim 3 (two-check design) and Claim 4 (response replaced wholesale on denial): this post confirms the replace-the-whole-response behavior and adds that it ends the agent's turn. Its Claim 12 (text-only responses not evaluated) is borne out by the residual travel failures here. `blog-google-agent-anomaly-detection-benchmarks.md` Claim 10 (defense in depth).
- **Contradicts**: None filed. This post resolves, rather than opposes, the parent note's Claim 9 ("effectiveness against adaptive injection is unvalidated"): it provides non-adaptive numbers and explicitly leaves adaptive untested.
- **Extends**: `blog-google-semantic-governance-policies.md` Claims 6 and 9 (probabilistic judge; intent check effectiveness) gain measured evidence. `blog-google-adk-zero-trust-agents.md` Claim 8 (deterministic gateway): this is the LLM-judged alternative, now with a measured number. `blog-google-agent-anomaly-detection-benchmarks.md` Claims 1-2 (detector figures are conditional on how you count) parallels this post's utility-under-attack versus safe-completion reframing.
- **Novel**: First measured effectiveness figure for an inline LLM-judge tool-call gate in the corpus; the "task completed AND attack failed" metric; the gap that denial usually halts the agent; the NIST CAISI 11% to 81% adaptive-attack figure.

## Guide Impact

- **Chapter 06**: In the intent-check row of the preventive-controls table (guide/06-security-threat-model.md), add the AgentDojo figures as vendor-measured and non-adaptive (48.7% to 0.9%, 2.6 pp utility cost, 0 of 929 tool-call attacks), and pair them with the adaptive-attack caveat (11% to 81% per NIST CAISI). State that text-only manipulation is outside such a gate and needs response filtering.
- **Chapter 03**: Cite the "task completed AND attack failed" metric as a better way to evaluate security controls than raw utility or raw ASR.
- **Chapter 02**: Use as evidence that action-level, out-of-agent gating is measurable, with the caveat that the gate's trust boundary is prompt-enforced.

## Extraction Notes

- Fetched the full article HTML via curl and read all text. The results tables and domain charts are images; per-domain numbers beyond those stated in prose were not extracted. Linked pages (adversarial benchmarking method, overview docs) were not followed.
- WebFetch only returned a summary, so quotes were taken from the raw HTML-to-text conversion and copied verbatim.
- No contradiction filed.
