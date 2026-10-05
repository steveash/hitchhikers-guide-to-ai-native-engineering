---
source_url: https://www.latent.space/p/ainews-xiaomi-mimo-v26-pro-1t-a42b
source_type: blog-post
title: "[AINews] Xiaomi MiMo-V2.6-Pro 1T-A42B: the new top Open Weights model, trained for $3M"
author: Latent Space / AINews (daily digest; no individual byline; aggregates tweets/Reddit)
date_published: 2026-09-22
date_extracted: 2026-10-05
last_checked: 2026-10-05
status: current
confidence_overall: emerging
issue: "#3911"
---

# [AINews] Xiaomi MiMo-V2.6-Pro 1T-A42B: the new top Open Weights model, trained for $3M

> Latent Space's AINews digest on Xiaomi's MIT-licensed MiMo-V2.6-Pro (1.02T total / 42B active), the top open-weights model on the Artificial Analysis Intelligence Index (46), with the headline data point that the RL run behind it reportedly cost ~$2.6M (130 hours, 75B tokens) and that Xiaomi plans to open-source its RL environments and training code — plus a Jev "decision model" thread and inference-engineering roundups.

## Source Context

- **Type**: blog-post (AINews weekday roundup; "Paid" post — only the free preview was readable, see Extraction Notes). Discovered via the trusted `latent-space` feed; published 22 Sep 2026.
- **Author credibility**: No individual byline. As established for this publication elsewhere in the corpus (e.g. `blog-latentspace-ainews-much-ado-open-weights.md`), AINews relays attributed third-party tweets and benchmark posts; it is not independent testing. Primary sources named here: Xiaomi's launch post/technical report, Artificial Analysis (independent evaluator), and individual commentators (@zephyr_z9, @tianjun_zhang, @eliebakouch, @xeophon, @victormustar) — none re-fetched by this Miner.
- **Scope**: Hand-written intro (Xiaomi launch, RL scaling axes, open-sourced tooling list), then the "AI Twitter Recap" (open models/China gap; MiMo-V2.6 and RL; Jev decision models; inference/tooling; agent security; top tweets) and one Reddit section (Qwen-Image 2.1) before the paywall. The "$3M" in the title is not itself substantiated in the readable body; the only cost figure in the body is the **$2.6M RL run** (a tweet-sourced number the digest hedges with "If these numbers hold up"). Pretraining cost and compute are not given in the readable portion.

## Extracted Claims

### Claim 1: MiMo-V2.6-Pro debuts as the top open-weights model on the Artificial Analysis Intelligence Index at 46, on the Intelligence-vs-Cost-per-Task Pareto frontier
- **Evidence**: Embedded Artificial Analysis tweet (Sep 21, 2026); AA is a third-party evaluator. Cost figure of $0.13 per Intelligence Index task.
- **Confidence**: emerging
- **Quote**: "MiMo-V2.6-Pro debuts as the top open weights model on the Artificial Analysis Intelligence Index (46). At $0.13 per Intelligence Index task, it lands on the Intelligence vs. Cost per Task Pareto frontier"
- **Our assessment**: Credible as an index result (independent evaluator), but an index of 46 should be compared against the same-index figures in other notes (e.g. Kimi K3 at 57 in `blog-latentspace-ainews-kimi-k3-wiki-memory.md`, Claim 3) — "top open weights" here contrasts with that note's higher K3 number, a discrepancy this digest does not explain (possibly different index versions or K3 excluded; not verified).

### Claim 2: MiMo-V2.6-Pro is a 1.02T-total / 42B-active MoE, MIT licensed, with low per-token pricing
- **Evidence**: Digest summary of Artificial Analysis plus @victormustar for the license.
- **Confidence**: emerging
- **Quote**: "with 1.02T total / 42B active parameters and strong cost efficiency at $0.435/M input and $0.87/M output tokens."
- **Our assessment**: Concrete pricing/size data points useful as a cost anchor. MIT is more permissive than the "open weights, not open source" Kimi K3 terms in `blog-latentspace-ainews-much-ado-open-weights.md` (Claim 4).

### Claim 3: Xiaomi is an out-of-order entrant — a phone maker not among the "six Chinese AI Tigers" — shipping a natively omnimodal frontier-class model
- **Evidence**: Editorial framing by the digest; Xiaomi's launch quote (Pro / Flash / Pro-UltraSpeed tiers).
- **Confidence**: anecdotal
- **Quote**: "Xiaomi is not traditionally considered one of the"
- **Our assessment**: (Quote is a verbatim fragment; the sentence continues "six Chinese AI Tigers".) Mainly a landscape signal: frontier-scale open releases are no longer confined to the established labs.

### Claim 4: The RL run behind MiMo-V2.6-Pro reportedly took 130 hours, 75B tokens and $2.6M; the digest hedges that if the numbers hold, post-training/RL is a much cheaper route to frontier-adjacent gains
- **Evidence**: Single tweet source (@zephyr_z9); not verified against the technical report in this digest.
- **Confidence**: anecdotal
- **Quote**: "If these numbers hold up, the implication is that post-training/RL is becoming a far cheaper route to frontier-adjacent gains than many assumed."
- **Our assessment**: This is the source for the "$3M" headline (likely RL cost plus rounding; the title's figure is not decomposed in the readable text). Treat as an unverified cost figure that excludes pretraining. It is consistent with the "post-training scaling" thesis in `blog-latentspace-ainews-death-of-params-glm53.md` (Claims 4–5: GLM-5.3 gains from ~one month of extra RL on the same base), but should not be cited as "total cost to train a frontier model."

### Claim 5: Xiaomi scaled RL compute along three axes: batch/throughput, task/environment diversity, and grader compute
- **Evidence**: Digest summary of Xiaomi's technical report: 1,568 samples per update, up to 1M context, 3.5–3.7B tokens per step, fully asynchronous architecture; multi-task suite (coding, general agents, visual, cyber) across several harnesses; relative grading within groups.
- **Confidence**: emerging
- **Quote**: "large batches on a fully asynchronous architecture, with 1,568 samples per update, training at up to 1M context length, and 3.5 to 3.7B tokens per step."
- **Our assessment**: Specific and checkable against the tech report. Mixing "several harnesses" in training so gains transfer is directly relevant to harness-robustness arguments (a model trained across harnesses is less harness-fragile).

### Claim 6: Grader compute is used to give long-horizon RL tasks more precise reward signals, closes a self-improvement loop, and steers models toward fewer tokens per task
- **Evidence**: Digest summary of the technical report.
- **Confidence**: emerging
- **Quote**: "gives long-horizon RL tasks more precise and more diverse reward signals, closes a self-improvement loop, and steers the model toward shorter paths and fewer tokens per task."
- **Our assessment**: Token-efficiency as an explicit RL objective is notable for cost-conscious agent use; unverified beyond the digest.

### Claim 7: Xiaomi is open-sourcing RL environment code and training recipes (~7K tasks), but the full task datasets were not yet released
- **Evidence**: Digest lists environments (coding, ARVO cyber/vulnerability reproduction, general knowledge work, web-dev grading, music generation, composable mini-harnesses, "mimoagent" adapters); @xeophon on ~7K environments; @eliebakouch on shipping less than a week after the final RL run.
- **Confidence**: emerging
- **Quote**: "the complete 7k+ task datasets have not yet been released."
- **Our assessment**: Important caveat to the "ALL of this tooling … will be open sourced" claim: recipes and code ≠ full data. Open RL environments are a reproducible-eval asset.

### Claim 8: Open RL environments may now be as strategically important as pretraining corpora were in the last cycle
- **Evidence**: Interpretation attributed to @bertgodel and @Thom_Wolf; supporting paper on generating RL tasks from open repos with "agents in the loop" for robustness and anti-cheating (@eliebakouch).
- **Confidence**: anecdotal
- **Quote**: "high-quality open RL environments may now be as strategically important as pretraining corpora were in the last cycle."
- **Our assessment**: Plausible and consistent with the environment-driven gains in the GLM-5.3 note; opinion, not demonstrated.

### Claim 9: The MiMo family trains RL on JAX + TPU, where scaling is "mostly a config change, not a code rewrite"
- **Evidence**: Single tweet (@tianjun_zhang), a Xiaomi-adjacent claim.
- **Confidence**: anecdotal
- **Quote**: "mostly a config change, not a code rewrite."
- **Our assessment**: Self-reported infra anecdote; low relevance to the guide beyond cost-trajectory context.

### Claim 10: Open-vs-frontier disagreement: one camp says coding capability has plateaued since Opus 4.8 with open models 10–50x cheaper; another says the frontier has split into higher tiers
- **Evidence**: @Yuchenj_UW and @ClementDelangue vs. @teortaxesTex; ~10-week run of Chinese releases compiled by @Thom_Wolf (Kimi K3, Qwen3.8-Max, DeepSeek V4-Pro, GLM-5.3, Hy4 Preview, Atria Dawn); Bloomberg-sourced note that startups build custom models on open weights.
- **Confidence**: anecdotal
- **Quote**: "frontier coding capability has plateaued since"
- **Our assessment**: Opinion-level; the "plateau" claim is contested within the same paragraph and conflicts with the tiering view of `blog-latentspace-ainews-fable-mythos-51-launch.md` (not verified claim-by-claim; not filed as a contradiction because the digest itself presents both sides and both are tweet-level).

### Claim 11: Jev-style "decision models" are framed as classification/routing with modern intelligence and low latency/cost; fits are routing, approval gates, trace scoring, tool selection, and supervision inside agent loops
- **Evidence**: Karpathy, @willdepue, @ClementDelangue, LangChain's Jev-as-a-judge in LangSmith; @omarsar0's anecdote of retagging ~2.3K papers in 83 seconds for $0.14 with manual validation of disagreements.
- **Confidence**: anecdotal
- **Quote**: "retag ~2.3K papers in 83 seconds for $0.14"
- **Our assessment**: Extends the Jev coverage with a concrete cost anecdote and the sensible caveat that these are not standalone "smart agents." (Quote is a verbatim fragment of the digest's sentence.)

### Claim 12: Agent-security design for computer-use agents: assume prompt injection, keep real credentials from the model, isolate tools in containers, use an independent outbound-call gatekeeper
- **Evidence**: DeepLearningAI summary of Meta's design philosophy for Muse-like agents; contrasted with Patrick Wardle's reported local-hijack flaw in Muse.
- **Confidence**: emerging
- **Quote**: "assume prompt injection will happen, keep real credentials away from the model, isolate tools in containers, and use an independent outbound-call gatekeeper."
- **Our assessment**: A compact four-part security posture, worth noting for the guide's security material; second-hand summary.

### Claim 13: OpenAI reportedly automated parts of experimental-model training (kernel writing, code optimization), compressing some experiments from years to about a week
- **Evidence**: Widely shared @wallstengine summary; unverified.
- **Confidence**: anecdotal
- **Quote**: "compressing some experiments from years to about a week"
- **Our assessment**: Unverified secondhand claim; do not cite as fact.

## Concrete Artifacts

```
Artificial Analysis tweet (Sep 21, 2026), embedded in the digest:
"MiMo-V2.6-Pro debuts as the top open weights model on the Artificial Analysis
Intelligence Index (46). At $0.13 per Intelligence Index task, it lands on the
Intelligence vs. Cost per Task Pareto frontier"

Digest metrics (AINews, Sep 22, 2026):
- 1.02T total / 42B active parameters; MIT license
- $0.435/M input, $0.87/M output tokens
- RL run: 130 hours, 75B tokens, $2.6M (@zephyr_z9 citation)
- RL batch: 1,568 samples/update, up to 1M context, 3.5-3.7B tokens/step
- ~7K RL environments planned for release; full 7k+ task datasets not yet released
```

## Cross-References

- **Corroborates**: `blog-latentspace-ainews-death-of-params-glm53.md` (Claims 4–5) — frontier-adjacent gains from RL/post-training on long-horizon environments rather than parameter count. `blog-latentspace-glm52-open-frontier-parity.md` (Claim 4) — open-weight models as the cost-efficient end of the AA cost-per-task frontier.
- **Contradicts**: None filed. Mild tension on the "top open-weights model" label (46 here vs. Kimi K3 at 57 in `blog-latentspace-ainews-kimi-k3-wiki-memory.md`, Claim 3) is likely index/version/timing and unverified, so no contradiction issue was opened.
- **Extends**: `blog-latentspace-ainews-jev-system-one-model.md` (Claim 3 launch performance claims; this adds a cost anecdote and use-case list); `blog-latentspace-ainews-much-ado-open-weights.md` (Claims 2, 4: Kimi K3 open-weights package and license — MiMo adds an MIT-licensed, RL-environment-releasing counterpart).
- **Novel**: Xiaomi as a frontier open-weights lab; a published RL-run cost figure ($2.6M); the thesis that open RL environments are the new strategic open asset.

## Guide Impact

- **Chapter 02 (model selection)**: Could add MiMo-V2.6-Pro as a data point (AA index 46, $0.435/$0.87 per M tokens, MIT) in the open-weights options list; flag cost figures as vendor/tweet-reported.
- **Chapter 04 (cost-aware model choice)**: The $0.13 per Intelligence Index task figure is a usable cost-per-task anchor; do not cite "$3M" as total training cost — the readable source supports only an unverified $2.6M RL-run figure.
- **Chapter 05**: No change recommended; evidence is too thin for adoption advice.

## Extraction Notes

- The post is paywalled ("Keep reading with a 7-day free trial"); the free preview (intro, full AI Twitter Recap, first Reddit section) was read via raw HTML fetch. The remaining Reddit/Discord sections were not accessible.
- The "$3M" in the title is not decomposed in the readable text; the technical report and linked tweets were not followed (the digest is an aggregation; Prospector suggested tracing but the report was out of scope for this note).
- Claim 3's quote is intentionally a verbatim fragment that ends mid-sentence.
- Cross-reference claim numbers were checked against the cited notes' numbered claim headings. The `blog-latentspace-ainews-fable-mythos-51-launch.md` reference in Claim 10 was not claim-checked and is cited at note level only.
