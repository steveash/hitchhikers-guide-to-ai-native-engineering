---
source_url: https://www.deeplearning.ai/the-batch/issue-370
source_type: blog-post
title: "The Batch Issue 370: Shaping the Build; GPT-6 Astra vs Claude Fable 5.1; Transcription Battles; SelfCompact"
author: Andrew Ng and The Batch editorial team (DeepLearning.AI)
date_published: 2026-09-11
date_extracted: 2026-10-05
last_checked: 2026-10-05
status: current
confidence_overall: emerging
issue: "#3905"
---

# The Batch Issue 370: Shaping the Build; GPT-6 Astra vs Claude Fable 5.1; Transcription Battles; SelfCompact

> Andrew Ng names "shaping the build" as the fourth AI Engineering skill, and the issue's news section adds a cost-per-task framing for Astra vs Fable 5.1, volatile benchmark indices, and a rubric-driven compaction tool (SelfCompact).

## Source Context

- **Type**: blog-post (weekly newsletter issue: a letter from Andrew Ng plus four news stories)
- **Author credibility**: Andrew Ng is the founder of DeepLearning.AI; the news stories are written by The Batch staff and cite independent evaluators (Artificial Analysis, Vals AI, ARC Prize) and vendor announcements. The letter is opinion. The news sections are secondary reporting.
- **Scope**: Covers (1) Ng's letter on the "shaping the build" skill cluster, (2) GPT-6 Astra launch, (3) Claude Fable 5.1 / Mythos 5.1 launch, (4) speech-to-text releases from Google, Meta and Microsoft, (5) the SelfCompact paper (Johns Hopkins / Apple). It does not give primary data of its own; numbers are relayed from evaluators and vendors.
- **Access note**: The origin site blocked direct fetches (Cloudflare 403). Text was read in full via the r.jina.ai markdown mirror of the same URL; the RSS feed description matches the letter's opening.

## Extracted Claims

### Claim 1: Skilled AI engineers "shape the build" rather than implement someone else's spec, because developer/PM/designer roles are blurring
- **Evidence**: Argument by the author from general observation; no data cited.
- **Confidence**: emerging
- **Quote**: "When you’re skilled at AI Engineering, your best work won’t be merely implementing a product that someone else spec’ed out. Instead, you will actively shape the build."
- **Our assessment**: Consistent with other Ng pieces in the corpus. It's a framing claim, not an empirical one. Useful as the definition of skill 4 of Ng's AI Engineering skills map.

### Claim 2: Four sub-skills make up "shaping the build"
- **Evidence**: Author's taxonomy, illustrated with a skills-map graphic and examples.
- **Confidence**: emerging
- **Quote**: "The key skills for shaping the build are:" (followed by the list: Driving the build loop, Making product decisions, Communicating and leading, High-agency ownership)
- **Our assessment**: The list is a useful checklist. It is not validated, but it lines up with the job-posting analysis summarized in the Latent Space note.

### Claim 3: Driving the build loop means high-velocity, small-batch shipping and choosing the next step among prototype, MVP, features, or enterprise-grade
- **Evidence**: Author's description; no metrics.
- **Confidence**: anecdotal
- **Quote**: "You frequently ship in small batches to keep up velocity."
- **Our assessment**: Matches the agent-loop-as-product-loop idea. Note the explicit decision inputs ("product vision, stage of the project, technical feasibility, key risks, effort, and budget") are a reusable decision rubric.

### Claim 4: Developers will make product decisions the spec doesn't cover, and need product, design and basic business sense grounded in user empathy
- **Evidence**: Author's assertion, with methods for honing empathy listed (2-3 user interviews, surveys of hundreds, A/B tests, behavior analytics of thousands or millions).
- **Confidence**: anecdotal
- **Quote**: "Developers don’t have to become PMs, but you will make decisions the product spec doesn’t cover."
- **Our assessment**: Plausible and corroborated by the PM-bottleneck letter. The "developers don't have to become PMs" hedge is notable: it is a scope expansion, not a role merger.

### Claim 5: AI engineering skill opens an opening for high-agency work because many executives don't yet know what AI can do
- **Evidence**: Author's observation.
- **Confidence**: anecdotal
- **Quote**: "many people — including some executives — do not yet understand what AI can do and therefore do not know what are good project directions."
- **Our assessment**: Anecdotal but practically relevant for adoption advice in the guide (engineers as bridge between capability and org direction). No evidence of how common this is.

### Claim 6: GPT-6 Astra tops or nearly tops leaderboards at a fraction of the tokens/cost of the few models that beat it
- **Evidence**: Independent evaluators relayed: ARC-AGI-3 62.7% at $26,098 (standard harness) and 99.9% at $18,817 (Provider Adapter harness); Artificial Analysis Intelligence Index v4.2 55 vs Fable 5.1's 57; Vals Index 66.61% (third).
- **Confidence**: emerging
- **Quote**: "OpenAI’s new model tops or comes close to topping AI leaderboards, and it does so using a fraction of the tokens and at a fraction of the cost of the few models that outperform it."
- **Our assessment**: Numbers are evaluator-sourced and plausible, but the index versions moved during the week (see Claim 9), so absolute scores are perishable. The Provider Adapter result depends on two API settings (hidden reasoning retained, compaction), the subject of the existing ARC-AGI-3 note.

### Claim 7: Per-token price is a poor guide to cost; reasoning level and tokens-per-task matter, so measure cost per task on your own setup
- **Evidence**: Astra's per-token price is 2.5x GPT-5.6 Sol's, yet it completed Artificial Analysis' agentic coding tasks for about the same price using a third as many tokens; on ARC-AGI-3 higher reasoning levels cost less than lower ones because fewer moves were needed.
- **Confidence**: emerging
- **Quote**: "Developers should carefully measure models’ cost per task on their own setup."
- **Our assessment**: Strong, directly actionable, and supported by two independent data points in the same piece. Corroborated by Fable 5.1's opposite case (cheaper cache reads, higher per-task cost; Claim 10).

### Claim 8: Astra's Codex and API features (retained reasoning, compaction, notes-to-self, async tool calls, mid-turn steering, adjustable reasoning without cache invalidation) are part of the product surface
- **Evidence**: Feature list in the Astra section; the notes-to-self mode is described as experimental and off by default.
- **Confidence**: settled (vendor-documented feature list as relayed)
- **Quote**: "In Codex, Astra can record detailed notes that persist as a conversation nears its context limit, instead of compacting a long session into a single summary, making more information searchable."
- **Our assessment**: A concrete example of a vendor replacing lossy summary compaction with searchable notes. Experimental, so don't build guidance on it yet.

### Claim 9: Benchmark leaderboards have a shrinking shelf life; Artificial Analysis changed its index twice in one week
- **Evidence**: v4.2 on Sept 4 retired GPQA-Diamond and raised private-test share to 40%; v4.3 on Sept 7 upgraded Terminal-Bench to v4 and added AutomationBench-AA. After the changes Fable 5.1 and Astra tied (53).
- **Confidence**: settled (dated, specific changes)
- **Quote**: "A top score on a benchmark has an ever-shrinking shelf life, not only because new models arrive every week, but also because the evaluation that crowns a model this month may not exist by the next month — or even the next week!"
- **Our assessment**: Important caveat for any guide table quoting index scores. Explains why other notes cite different Intelligence Index numbers (66, 61) for the same models.

### Claim 10: Fable 5.1 fixed only one of three stated issues: per-task cost rose about 20% despite a 75% cache-read price cut
- **Evidence**: Independent testing as reported; Fable 5.1 AA v4.3 cost $7.63/task vs Astra $3.26; Vals $28.92 and 76 min vs Astra $19.09 and 25 min.
- **Confidence**: emerging
- **Quote**: "Cost per task rose about 20 percent over Claude Fable 5 even after a 75 percent cut to the price of cached input."
- **Our assessment**: Matches the Latent Space launch note (Claim 3 there). Together with Claim 7, the pattern is: Fable leads on long-running tool work, Astra leads on cost/time efficiency.

### Claim 11: Fable 5.1 leads long-running tool-use work but trails Astra on overall knowledge, computer use and terminal tasks
- **Evidence**: AA-Briefcase 1662 Elo and GDPval-AA v2 1,764 Elo lead for Fable; Astra leads GDP.pdf, AA-Omniscience, GPQA Diamond, MMMU-Pro, and (Vals) Code Migration and Terminal-Bench 2.1 (87.27%).
- **Confidence**: emerging
- **Quote**: "It leads in long-running work that uses tools, but it trails GPT-6 Astra on overall knowledge, computer use, and multistep tasks in terminal."
- **Our assessment**: Useful model-selection heuristic, but rankings differ between evaluators ("One independent evaluator ranked Claude Fable 5.1 and GPT-6 Astra as tied for first. Another evaluator placed Claude Fable 5.1 just above GPT-6 Astra.").

### Claim 12: Both frontier vendors now ship gated cyber capability with classifier-based safeguards that can interrupt agent work
- **Evidence**: Astra: classifiers review reasoning and actions on every tool call, can interrupt; API requests end and cannot resume; checks run alongside the model, so an action may finish before it is flagged. Fable 5.1: activation probe plus LLM classifier, fallback to Opus 4.8 / Opus 5 on dangerous tasks; ~4% of measured output tokens came from fallback models; Anthropic expects roughly 60% fewer cyber interventions per session in Claude Code.
- **Confidence**: emerging
- **Quote**: "The checks run alongside the model rather than ahead of it, and OpenAI warns users that an action may finish before it is flagged."
- **Our assessment**: Operationally important: benchmark results may silently include fallback-model output, and API-mode interruptions are not resumable, which affects agent harness design.

### Claim 13: Three vendors released speech-to-text models, all under 4% WER on Artificial Analysis, with differing positioning (Gemini 3.5 Transcribe, Muse Voice Transcribe, MAI-Transcribe-2)
- **Evidence**: Pricing: Gemini ~$0.005/min batch, $0.009/min streaming; Muse $0.18/hr; MAI-Transcribe-2 $0.10/hr through year end. Muse lowest WER among streaming models; MAI-Transcribe-2 lowest among non-streaming and 5.2% on FLEURS. Diarization: Google up to 8 speakers, Muse over 20.
- **Confidence**: emerging
- **Quote**: "Muse Voice Transcribe has the lowest word error rate among streaming models, and MAI-Transcribe-2 has the lowest among non-streaming models."
- **Our assessment**: Answers the Prospector's key question: choose Muse for real-time/many-speaker use, MAI-Transcribe-2 for batch accuracy/speed/price, Gemini for 85+ language coverage and filler-word removal. The "fastest/most accurate/cheapest" claim is Microsoft's own ("Microsoft claims"). Little here about architecture; Meta's description is the only technical detail.

### Claim 14: Meta's "adaptive delay" lets the transcriber wait for more audio context only when needed
- **Evidence**: 80-ms audio chunks (12.5 per second), each a soft token; at each chunk the model emits a text token or a special "next audio" token; trained with reward for correct words and penalty for delay.
- **Confidence**: anecdotal (vendor-described, no paper)
- **Quote**: "Meta calls this process “adaptive delay.”"
- **Our assessment**: Interesting latency/accuracy trade-off mechanism for voice agents; unverified without a technical paper (the issue lists "technical papers" as undisclosed).

### Claim 15: SelfCompact, a compaction tool plus invocation rubric, beats fixed-interval and no-compaction baselines without fine-tuning
- **Evidence**: Every 16,000 tokens a probe asks the model to judge whether a sub-task is complete or progress is clear; compaction condenses 50-100k tokens of traces to 1-3k. IMO-Answerbench: 52.1% vs 48.7% (fixed interval) vs 45.2% (none) with Qwen3-30B-A3B; BrowseComp-Plus: 54.1% vs 50.0% vs 45.6% with GLM-4.7-Flash. Six benchmarks total.
- **Confidence**: emerging
- **Quote**: "Replacing the rubric with a simpler prompt that simply asked the model whether it wanted to compact the context reduced SelfCompact performance to the level of fixed-interval summarization."
- **Our assessment**: The ablation is the useful part: timing criteria, not compaction itself, drove the gains. Small open models only, and results are reported through a newsletter summary of the paper (arXiv 2606.23525), which I did not open.

### Claim 16: "Expose a tool and give the model explicit criteria for using it" is a new agentic design pattern
- **Evidence**: Editorial interpretation of SelfCompact.
- **Confidence**: anecdotal
- **Quote**: "exposing a tool and giving the model explicit criteria for using it."
- **Our assessment**: Reasonable generalization, but one paper doesn't establish a pattern. Compare Claude Code-style compaction triggers that are purely threshold-based.

## Concrete Artifacts

```
Source: The Batch issue 370, "GPT-6 Astra Is a Star" — API pricing line
API $10/$1/$12.50/$50 per million input/cached input/cache write/output tokens,
requests greater than 272,000 input tokens cost 2 times input and cache rates and
1.5 times output rates, batch and flex cost half the standard price, fast mode costs
twice the standard price
```

```
Source: The Batch issue 370, "Fable Holds The Top Spot (For Now)" — pricing line
both models via API at $10/$0.25/$50 per million input/cached/output tokens, cache
writes $12.50/$20 per million tokens, batch processing $5/$25 per million
input/output tokens; both models require 30-day data retention
```

```
Source: The Batch issue 370 — per-task cost/time on Artificial Analysis Intelligence Index v4.3 (as reported)
Claude Fable 5.1 (max, fallback): 53, $7.63, 12.2 min per task
GPT-6 Astra (max):                53, $3.26,  8.2 min per task
Claude Opus 5 (max):              51, $5.86, 13.9 min per task
```

```
Source: The Batch issue 370 — SelfCompact procedure (paraphrased from "How it works")
every 16,000 tokens: append probe prompt -> model judges own state
  sub-task complete / clear progress -> allow compaction
  mid-step or stuck                 -> block compaction
on compaction: 50k-100k tokens of traces -> ~1k-3k token summary, written by the same model
```

```
Source: The Batch issue 370 — speech-to-text pricing as reported
Gemini 3.5 Transcribe: ~$0.005/min (~$0.30/hr) pre-recorded; $0.009/min (~$0.54/hr) streaming
Muse Voice Transcribe: $0.18/hr ($3 per 1,000 min)
MAI-Transcribe-2:      $0.10/hr through end of year
```

## Cross-References

- **Corroborates**: `blog-latentspace-ainews-andrew-ng-ai-engineering.md` Claim 5 (Skill 4, Shaping the build) — this is Ng's own text of that skill. `blog-thebatch-ng-pm-bottleneck.md` Claim 1 (deciding what to build is the new bottleneck) and Claim 9 (judgment over implementation). `blog-latentspace-ainews-fable-mythos-51-launch.md` Claim 3 (per-task cost rose ~20% despite cache-read cut) and Claim 5 (fallback routing inside Artificial Analysis evaluation). `blog-latentspace-ainews-reality-checks-gas-town-astra-cost.md` Claim 5 (per-task benchmark costs for top models several times the previous tier) bears on Claim 7 here. `blog-simonwillison-gpt6-astra-launch.md` Claim 7 (ARC-AGI-3 99.9% on Provider Adapter harness vs 62.7% default, $19K vs $26K) matches this issue's numbers.
- **Contradicts**: None filed. Score differences against other notes (e.g. Intelligence Index 66 in the Fable 5.1 launch note Claim 4 and 61 in the Willison Astra note Claim 4, versus 55/57 and 53 here) reflect different Artificial Analysis index versions (Claim 9), so they are a conditioning variable, not a contradiction.
- **Extends**: `blog-openai-arc-agi-3-two-settings.md` Claims 2 and 8 (retained reasoning plus compaction) — here the settings produce the 99.9% Astra result. `research-wasnotwas-context-compaction.md` Claims 1 and 3 (threshold-triggered, lossy LLM-summary compaction across harnesses) — SelfCompact is an alternative, state-triggered trigger; Astra's notes-to-self mode is an alternative to summary compaction.
- **Novel**: Rubric-gated compaction (SelfCompact) with its ablation; Meta's adaptive-delay speech-to-text design; three-way speech-to-text comparison with prices (first speech-to-text model comparison in these notes; existing voice notes cover voice agents, not transcription models); the explicit Artificial Analysis v4.2/v4.3 index change timeline.

## Guide Impact

- **Chapter 04 (Model Capabilities & Tradeoffs)**: Add a cost-per-task caveat citing Claims 7 and 10: Astra costs 2.5x Sol per token but about the same per agentic coding task; Fable 5.1 got cheaper cache reads but costlier tasks. Add a note that leaderboard scores are version-dependent (Claim 9) when any index numbers are quoted.
- **Chapter 05 (Vendor Landscape)**: Add a transcription subsection using Claim 13 (Gemini 3.5 Transcribe, Muse Voice Transcribe, MAI-Transcribe-2 with prices, language/speaker counts, streaming vs non-streaming winners). Flag vendor-claimed rankings as such.
- **Chapters on context management / compaction (if present)**: Cite SelfCompact (Claim 15) as evidence that when compaction fires matters more than whether it fires; pair with the research-wasnotwas note on threshold triggers.
- **Chapters on roles/skills (if present)**: Cite Ng's four shaping-the-build sub-skills (Claims 1-2) as the primary source for the existing Latent Space-derived summary.

## Extraction Notes

- Read the full issue (letter plus four stories) via a mirror, since the origin site returned 403 to direct fetches. Did not follow the linked vendor pages or the SelfCompact arXiv paper; all numbers are as reported by The Batch.
- The cybersecurity-related details (Hugging Face incident, Glasswing, Daybreak) appear in the Astra "Behind the news" section and are covered by existing Astra/Mythos notes; not extracted as separate claims.
- The issue title (set by the feed) lists only the model-ranking and transcription stories; the letter and SelfCompact items are the more guide-relevant content.
- No contradiction issue filed.
