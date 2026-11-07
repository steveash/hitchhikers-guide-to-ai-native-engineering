---
source_url: https://latent.space/p/ainews-kimi-31/
source_type: blog-post
title: "[AINews] Kimi 3.1 Pro 104BA-2.8T: Fable-5.1-Class Open Weights narrows Closed-AI lead to 1 month... and Pro Highspeed API with 2-3× speed"
author: swyx / Latent Space AINews (daily digest aggregating tweets and Reddit for 10/22/2026-10/23/2026)
date_published: 2026-10-24
date_extracted: 2026-11-07
last_checked: 2026-11-07
status: current
confidence_overall: emerging
issue: "#4579"
---

# [AINews] Kimi 3.1 Pro 104BA-2.8T: Fable-5.1-Class Open Weights narrows Closed-AI lead to 1 month...

> A digest of the Kimi K3.1 Pro launch that supplies concrete cost-per-completed-task figures (Artificial Analysis, Arena) showing a one-third list-price cut did not translate into cheaper work on every workload, plus a careful separation of vendor claims, independent evals, and unverified allegations.

## Source Context

- **Type**: blog-post (AINews daily digest; "Top Story" section is an LLM-assisted, heavily hedged synthesis of tweets, with Reddit recaps and "Other topics" following)
- **Author credibility**: swyx / Latent Space is a well-known AI-engineering publication. The digest relays other people's claims and explicitly labels what is vendor-stated, independently measured, or speculation. The benchmark numbers originate with Artificial Analysis (AA) and Arena, not with the digest.
- **Scope**: Covers the K3.1 Pro launch (2026-10-22/23): release status, AA and Arena evals, pricing and per-task cost, the cyber-training-data intervention, interactive/3D results, benchmark-interpretation caveats, and paid-promotion allegations. Does not include the underlying tweets or charts (the AA K3-vs-K3.1 comparison table did not survive in the fetched text). I did not follow the linked tweets; primary sources were not independently checked.

## Extracted Claims

### Claim 1: Lower per-token prices did not make completed work uniformly cheaper; cost per task depends on token consumption
- **Evidence**: AA/Arena per-task figures relayed from tweets: AA Intelligence Index $1.98/task (roughly unchanged from K3), Arena WebDev $1.23 median/task (29% below K3), AA Cyber Index $2.81/task (15% above K3). Output tokens per Intelligence Index task rose from 48K to 55K.
- **Confidence**: emerging
- **Quote**: "On the Intelligence Index, K3.1 Pro generated"
- **Our assessment**: Strongest takeaway for Ch02. The quote is only the opening fragment; the figures are in Concrete Artifacts. The pattern (token price down, tokens per task up) is plausible and matches how reasoning models behave. Figures are second-hand via the digest, so cite as "AA reported" and not as our measurement.

### Claim 2: Standard K3.1 Pro list pricing is one-third below K3; Highspeed is claimed 2–3× faster at 2× price
- **Evidence**: Pricing from AA and Moonshot-affiliated Chinese account (Zhihu Frontier) via tweets.
- **Confidence**: emerging (vendor-stated)
- **Quote**: "down one-third from K3’s $3/$15/$0.30"
- **Our assessment**: Straightforward vendor pricing. The speed claim is Moonshot's; no independent latency test is reported.

### Claim 3: List-price comparisons against other labs are not cost-per-success comparisons
- **Evidence**: The digest notes launch commentary compared per-token rates (50% below Opus 5.5's $4/$20, 80% below Astra's $10/$50). Arena's per-task view separately puts K3.1 Pro 74% below Opus 5 Max, 24% below GPT-6 Sol Max, 47% below Qwen3.8-Max at median task cost, with small preference-point differences.
- **Confidence**: emerging
- **Quote**: "Those comparisons concern per-token list prices, not measured cost per successful task."
- **Our assessment**: Good methodological caveat. Note Arena's comparison is on one workload (WebDev) and Arena's task-cost numbers still are not "cost per successful task" in the strict sense.

### Claim 4: Terminal-Bench cost claims for K3.1 Pro were inconsistent across commentators
- **Evidence**: One reaction said better than Opus 5.5 at about one-third the cost; Cline said near-parity at half the cost. Another researcher cited 65.7% vs AA's rounded 67%.
- **Confidence**: anecdotal
- **Quote**: "Terminal-Bench cost claims were inconsistent across reactions"
- **Our assessment**: Illustrates that harness, settings and cost accounting change the answer; supports recommending teams measure on their own tasks.

### Claim 5: AA ranks K3.1 Pro 4th on its Intelligence Index (55), with gains concentrated in agentic rather than knowledge tasks
- **Evidence**: AA, via tweet. Opus 5.5 58; Sonnet 5.5 and Muse Wonder Full 56. AA-Omniscience accuracy 48%→51%, hallucination rate 53%→44%. AA says that once weights are published the open-vs-proprietary gap would narrow from 12 points to three.
- **Confidence**: emerging (independent evaluator, but second-hand)
- **Quote**: "Its strongest improvements were agentic rather than uniformly distributed across knowledge and science tests."
- **Our assessment**: The title's "narrows Closed-AI lead to 1 month" is a framing; the digest's own body is more cautious. The 9-point hallucination drop is explicitly distinguished from Moonshot's separate "65% fewer hallucinations" finance claim.

### Claim 6: "Open weights" was unfulfilled at launch; license, precision and serving requirements were unknown
- **Evidence**: API available at launch, weights promised by 2026-11-04. Illustrative arithmetic: 2.8T params ≈ 5.6 TB at 16-bit or 1.4 TB at 4-bit.
- **Confidence**: settled for status at time of writing; the later release is unverified here
- **Quote**: "At launch, "
- **Our assessment**: The full relevant sentence spans a formatting break in the page ("the API was available; the weights were not"). Treat the 2026-11-04 release as unverified; check before citing. The digest's distinction "Self-hostable and consumer-device-local are different properties" aligns with the Thoughtworks note.

### Claim 7: K3.1 Pro is a post-train of K3 with much more RL compute, not a new pretrain
- **Evidence**: Moonshot's own statement, quoted in the digest.
- **Confidence**: emerging (vendor-stated)
- **Quote**: "Kimi K3.1 Pro is a post-trained version of Kimi K3, with substantially larger post-training compute."
- **Our assessment**: Notable evidence that large agentic gains can come from post-training scale alone. Spec figures (2.8T/104B/1M) duplicate existing notes.

### Claim 8: Moonshot removed cyber data from mid-training and RL, yet K3.1 Pro posted the highest publicly accessible AA Cyber Index result
- **Evidence**: Moonshot report (via tweets): internal cyber score fell 90.5%→81%. AA: 64% on Cyber Index, second to trusted-access GPT-6 Sol Daybreak Blue at 69%; +23 index points over K3's 41%; CyberGym 58%→95%; no safety refusals observed.
- **Confidence**: emerging (internal score vendor-stated; AA score independent)
- **Quote**: "Despite deliberately reducing cyber-related training, it subsequently scored"
- **Our assessment**: The digest separates training-time capability reduction from API refusal policy. Key lesson: data-removal mitigation did not prevent strong public defensive/offensive benchmark results; relevant to open-weight risk framing in Ch05.

### Claim 9: Provider deployment fidelity varies; the same model name can perform very differently across hosts
- **Evidence**: Vals study: Kimi K3 (not K3.1) scored 60.6% on legal tasks via Baseten vs 75.8% via Moonshot.
- **Confidence**: emerging
- **Quote**: "This does not establish a K3.1 provider gap, but explains why identical model names do not guarantee identical agent performance."
- **Our assessment**: Practical and actionable for anyone routing to third-party hosts; applies to K3, not K3.1.

### Claim 10: Vendor benchmark tables are not independent replication; harness and provenance questions remain
- **Evidence**: Critics noted heavy use of the Claude Code harness in Moonshot's results and mixed data sources (DeepSeek's self-reported 42.3 Terminal-Bench vs tbench.ai/AA for others).
- **Confidence**: anecdotal (allegations about provenance)
- **Quote**: "Moonshot’s benchmark table is not an independent replication."
- **Our assessment**: Reasonable caution; the provenance inconsistency is an unreconciled allegation.

### Claim 11: Independent results outside conventional coding are mixed, and workload-specific anecdotes disagree
- **Evidence**: AA-3D early preferences below its coding standing (voting incomplete); RuneScape Bench comparable to DeepSeek V4.1 Flash and about Opus 5.0 at comparable cost to Argon; a compiler-development user found no alternative matched Fable 5.1/Opus 5.5.
- **Confidence**: anecdotal
- **Quote**: "These are workload-specific anecdotes, not population-level results."
- **Our assessment**: Supports "task-dependent competitiveness" rather than blanket frontier parity.

### Claim 12: Serving economics are the central business objection to a ~3T open model
- **Evidence**: A commentator estimated 30×+ the serving cost of DeepSeek Flash; the digest labels this unverified.
- **Confidence**: anecdotal
- **Quote**: "These are unverified estimates and strategic judgments—not measured infrastructure costs."
- **Our assessment**: Do not cite the 30× figure as fact.

### Claim 13: Paid-promotion allegations are reported but unauthenticated
- **Evidence**: A commentator alleged Moonshot sought undisclosed positive reviews (instruction quoted as "do not put on the paid partnership label"); no briefing, provenance or Moonshot response in the digest.
- **Confidence**: anecdotal
- **Quote**: "No Moonshot response or independent authentication of the alleged briefing appears in this collection."
- **Our assessment**: Record as an allegation only. Useful, generalizable lesson: influencer enthusiasm at launch is not independent validation.

## Concrete Artifacts

```
Per-task cost table (Latent Space AINews digest, citing AA and Arena):
Workload/source          Reported K3.1 Pro cost   Comparison
AA Intelligence Index    $1.98/task               Roughly unchanged from K3
Arena WebDev             $1.23 median/task        29% below K3
AA Cyber Index           $2.81/task               15% above K3; much more than DeepSeek 1017

Tokens: Intelligence Index 55K output tokens/task (K3: 48K, ~14% more);
Cyber suite: roughly twice the input-token consumption.

Pricing (per M tokens): K3.1 Pro $2 input / $10 output / $0.20 cached input
(K3: $3 / $15 / $0.30). Highspeed: described as 2x standard price, 2-3x output speed.
Cline: ClinePass $9.99/month plan advertising discounted open-weight access.

AA Intelligence Index: Opus 5.5 58; Sonnet 5.5 and Muse Wonder Full 56; K3.1 Pro 55.
Arena Code Arena WebDev: #8, 1,692 points (K3: #17, 1,655).
```

## Cross-References

- **Corroborates**: `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 3 (self-hosting a 2.8T MoE needs serious infrastructure; the digest's 5.6 TB / 1.4 TB arithmetic and the "local" caveat agree). `blog-latentspace-ainews-much-ado-open-weights.md` Claim 16 (hardware sizing for the ~1.4TB checkpoint).
- **Contradicts**: None filed. No existing claim materially opposes this note.
- **Extends**: `blog-simonwillison-kimi-k3-pelican-benchmark.md` Claim 3 (K3 pricing $3/$15, which this note shows cut to $2/$10) and Claim 10 (AA results for K3). `blog-latentspace-ainews-much-ado-open-weights.md` Claim 2 (K3 specs) and Claim 10 (K3 agentic/coding evals): K3.1 adds a version delta and per-task costs. `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 10 ("insurance and pricing power") gains concrete per-task cost data.
- **Novel**: Per-task cost vs per-token price evidence for an open-weight frontier model; the training-data-removal cyber intervention paired with strong public cyber scores; provider-fidelity gap (Vals); the paid-promotion allegation.

## Guide Impact

- **Chapter 02**: Add (hedged, attributed to AA/Arena) that token price cuts do not guarantee cheaper completed work: K3.1 Pro's list price fell one-third while AA Intelligence Index cost per task stayed ~$1.98 and Cyber Index cost rose 15%, because token use rose. Recommend measuring cost per completed task on the team's own workload.
- **Chapter 05**: When evaluating open-weight models, note (a) weights/license may lag the API launch, so verify before planning around them, (b) hosted providers can score materially differently from the vendor endpoint (Vals K3 example), (c) vendor benchmark tables and influencer reviews are not independent evidence.
- **Chapter 00**: Optional: one-line pointer that AA placed an open-weight-promised model 4th, 3 points behind the top closed model, with the caveat that the "1 month lag" is a headline framing.

## Extraction Notes

- Read the full article text (about 36 min read) including Top Story, recaps, and Other topics; Reddit and non-Kimi sections were skimmed and judged out of scope. Linked tweets and the AA/Arena primary sources were not followed, so figures are second-hand.
- The in-article AA K3 vs K3.1 comparison table was not present in the fetched text.
- Whether weights were released on 2026-11-04 was not verified.
- Quotes are contiguous fragments copied from the fetched page text; some are short because the page splits sentences across bolded spans.
- Prior issue #4358 (Simon Willison link post, same launch) was rejected as low novelty; this note covers different content.
