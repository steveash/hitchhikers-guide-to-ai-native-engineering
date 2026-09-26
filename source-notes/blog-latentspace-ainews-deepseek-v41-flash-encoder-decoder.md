---
source_url: https://www.latent.space/p/ainews-deepseek-v41-flash-763b-p8b
source_type: blog-post
title: "[AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture with vision marks the Return of the Whale"
author: Latent Space / AINews (automated/editorial daily digest; no individual byline; aggregates tweets/Reddit for 9/9/2026-9/10/2026)
date_published: 2026-09-12
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: emerging
issue: "#3729"
---

# [AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture with vision marks the Return of the Whale

> DeepSeek's v4.1-Flash abandons the standard decoder-only transformer for a causal
> encoder-decoder split with asymmetric active parameters (8B for
> prefill/input, 16B for decode/output), pushing KV cache down to roughly
> 1/8 of the prior V4 Flash and enabling full-precision local inference via
> SSD-offloaded Engram tables — while independent benchmarks show it winning
> on cost-per-task and several agentic benchmarks despite scoring lower on
> Artificial Analysis's general Intelligence Index than the equivalent
> figure reported for the July V4-Flash-0731 checkpoint, and despite being
> the most verbose model AA has measured.

## Source Context

- **Type**: blog-post (Latent Space's "AINews" — a daily, largely
  automated/editorial digest that opens with a hand-written editorial essay
  on one headline topic, here DeepSeek v4.1-Flash, followed by an "AI
  Twitter Recap" of the same and unrelated same-day stories, then an "AI
  Reddit Recap" covering r/LocalLLaMA and r/localLLM). Published
  2026-09-12T05:56:05Z per the page's own JSON-LD, covering "AI News for
  9/9/2026-9/10/2026" ("We checked 12 subreddits, 544 Twitters and no
  further Discords"). This is the same recurring source format already in
  this corpus (`blog-latentspace-ainews-death-of-params-glm53.md`,
  `blog-latentspace-ainews-megakernels-dead-and-back.md`,
  `blog-latentspace-ainews-kimi-k3-wiki-memory.md`,
  `blog-latentspace-ainews-harness-drift-quantization.md`).
- **Author credibility**: No individual AINews byline (page metadata
  attributes it to the organization "Latent.Space"). Per the credibility
  caveat already established for this outlet elsewhere in the corpus,
  AINews-relayed claims should be read as attributed third-party statements
  the outlet curates and lightly synthesizes, not as Latent Space's own
  independent benchmarking. The opening editorial essay (architecture
  framing, DeepSeek's release history, the "Return of the Whale" framing)
  is Latent Space's own analysis; the specific numeric benchmark claims are
  attributed to named third parties (Artificial Analysis, Vals AI) whose
  results AINews reports but did not independently reproduce.
- **Scope**: Covers the v4.1-Flash architecture (causal encoder-decoder,
  asymmetric active parameters, KV cache mechanics), independent benchmark
  placements (Artificial Analysis, Vals AI), local-inference/SSD-offload
  reports, a post-training philosophy claim attributed to DeepSeek via a
  quoted tweet, a cluster of harness/agent-research paper summaries
  unrelated to DeepSeek, and a Reddit-sourced correction of the model's
  true parameter count. Does NOT independently verify any of the
  third-party benchmark numbers it reports, does NOT give a technical
  breakdown of the vision encoder or the "Engram" hash-table component
  beyond size figures, and does NOT cover training data or RLHF
  methodology for v4.1-Flash specifically (contrast with the post-training
  methodology detail already extracted for GLM-5.3 in
  `blog-latentspace-ainews-death-of-params-glm53.md`).

## Extracted Claims

### Claim 1: DeepSeek v4.1-Flash replaces the standard decoder-only transformer with a causal encoder-decoder architecture, using an asymmetric split of 8B active parameters for prefill (input) and 16B active parameters for decode (output) — extending DeepSeek's own MoE notation into "763B-P8B-D16B"
- **Evidence**: Latent Space's own editorial description of the architecture, plus an independent, separately attributed confirmation from Artificial Analysis in the Twitter Recap.
- **Confidence**: emerging (first-party architectural framing from DeepSeek's release, restated independently by a named third-party benchmarking org, but this Miner could not access the DeepSeek technical report's own architecture diagrams — only the AINews prose description)
- **Quote**: "what we are HUGE fans of is the prefill/decode separation introduced here, 8B in prefill (input tokens), 16B in decode (output tokens), causing our alphabet soup of "DeepSeek v4.1-Flash: 763B-P8B-D16B" if you extend the established notation for MoEs."
- **Our assessment**: This is the architectural headline of the release and the most novel item in this source for the corpus: no other model tracked in this corpus splits active-parameter count by prefill vs. decode phase. The practical implication is that the model's compute cost is genuinely asymmetric — a long-prompt, short-answer workload (e.g., document summarization) runs cheaper than a short-prompt, long-answer workload (e.g., extended reasoning or code generation), which is a new dimension for cost estimation beyond the input/output token-count multiplication used for symmetric decoder-only models elsewhere in the corpus.

### Claim 2: A tweet from Sebastian Raschka characterized v4.1 as a "big overhaul" and said DeepSeek "should have called it DeepSeek V5," explicitly citing the encoder-decoder setup as the key break from prior DeepSeek generations; nrehiew separately called the design "cleaner" than V4's HSA+CSA combination and "very clearly designed for inference," citing a ~890 bytes/token KV cache size
- **Evidence**: Two independently attributed reactions in the Twitter Recap from named technical commentators (Raschka, a well-known ML educator; nrehiew, a technical AI commentator already used as a source in this corpus for Kimi K3 analysis).
- **Confidence**: anecdotal (both are named individuals' qualitative technical opinions, not measured results, though the ~890 bytes/token figure is a specific number nrehiew attributes to "the benchmarked score regime")
- **Quote**: "Sebastian Raschka characterized V4.1 as a "big overhaul" and said they "should have called it DeepSeek V5,"" and separately "Nrehiew concluded that the design looks cleaner than the older HSA + CSA combination in V4, saying it was "very clearly designed for inference," and cited a striking ~890 bytes/token KV size for the benchmarked score regime"
- **Our assessment**: Two independent, credentialed technical commentators converging on "this is a bigger architectural change than the version number implies" is a stronger signal than either alone. The 890 bytes/token figure is the most concrete KV-cache-efficiency number in this source and is consistent with the broader KV-cache-reduction claims in Claim 3 — worth citing together as the same underlying efficiency story from two angles (aggregate cache-size reduction ratio vs. absolute per-token footprint).

### Claim 3: DeepSeek claims KV-cache/storage reductions of 4× HBM and 8× SSD versus the prior generation, and 437× versus its first-generation model; separately, AINews reports the new Sliding-Window Attention Bounded Replay mechanism plus the prefill/decode split gives v4.1-Flash a KV cache footprint "up to 1/8 that of V4 Flash"
- **Evidence**: The 4×/8×/437× figures are DeepSeek's own stated claims, reported in the Reddit Recap's summary of the model's HuggingFace/announcement page; the "1/8 of V4 Flash" figure is AINews's own editorial framing in the opening essay, referencing "new tweaks like Sliding-Window Attention Bounded Replay."
- **Confidence**: anecdotal (both are vendor-stated efficiency claims — DeepSeek's own comparison baselines "prior generation" and "first-generation model" are not independently defined or reproduced in this source, and AINews does not cite a specific benchmark methodology for the "1/8" figure either)
- **Quote**: "DeepSeek claims KV-cache/storage reductions of 4× HBM and 8× SSD vs the prior generation, and 437× vs its first-generation model" and, separately, "combined with new tweaks like Sliding-Window Attention Bounded Replay, makes for a KV cache footprint up to 1/8 that of V4 Flash"
- **Our assessment**: These are vendor-reported efficiency multipliers without disclosed methodology (what exactly counts as "prior generation" vs. "first-generation model" is not specified), so they should be treated as directional claims pending independent verification — consistent with how this corpus already treats DeepSeek's self-reported efficiency metrics in `blog-simonwillison-deepseek-v4.md` Claims 4–5 (V4-Pro/V4-Flash FLOPs and KV-cache reductions vs. V3.2, also paper-cited and unreproduced). The pattern across two releases (April V4, September v4.1-Flash) is that DeepSeek consistently reports large KV-cache reductions as its headline efficiency metric at each generation, which practitioners evaluating long-context/agentic deployment cost should track but not take as independently benchmarked.

### Claim 4: A Reddit thread inspecting the HuggingFace safetensors argues v4.1-Flash is actually ~748.5B parameters for backbone + engram (551.566B backbone MoE FFN + 196.929B engram), not the widely reported 552B, 305B, 485B, or 522B figures — with total stored size ~763.21B params / 511.76GB once optional DSpark/MTP (14.225B) and the vision encoder (0.485B) are included
- **Evidence**: A Reddit post (r/LocalLLaMA, "Deepseek V4.1 Flash is 748B, not 552B," Activity 575) that the Miner accessed via the AINews Reddit Recap summary, attributing the confusion to counting/metadata errors — an NVIDIA forum estimate undercounting the backbone, HuggingFace's 485B figure likely miscounting FP4-packed weights as bytes rather than two-params-per-byte (compared to a similar miscount pattern on GLM-5.3-Flash-NVFP4), and vLLM's own recipe page inconsistently listing 522B before correcting.
- **Confidence**: emerging (a named, methodologically-described community investigation directly inspecting released model files, not a vendor claim — but this Miner did not independently re-derive the parameter count from the safetensors files, only relayed the Reddit thread's reported methodology and figures via AINews's summary)
- **Quote**: "OP inspected the Hugging Face safetensors and argues DeepSeek V4.1 Flash is ~748.5B parameters for backbone + engram—not 284B, 305B, 485B, or 522B—with a 551.566B backbone and 196.929B engram; including optional DSpark/MTP (14.225B) and vision encoder (0.485B) brings the stored model to ~763.21B params / 511.76 GB."
- **Our assessment**: This is a genuinely useful, checkable data point: even a model's basic total-parameter count can be reported inconsistently across sources (NVIDIA forums, HuggingFace's own page, vLLM's recipe page) due to quantization-format miscounting (FP4-packed bytes vs. params-per-byte). This directly explains why the issue title's own headline figure ("763B-P8B-D16B") differs from the Reddit-sourced "552B-parameter MoE" figure quoted elsewhere in the same Reddit Recap section of this same article — both are present in this single source and are not reconciled by AINews itself. Practitioners citing this model's parameter count in the guide should cite the safetensors-derived 748.5B/763.21B figures (backbone+engram, or backbone+engram+DSpark+vision) rather than the earlier, lower community estimates, and should note that MoE-with-hash-table (Engram) architectures may need their own parameter-counting convention distinct from standard MoE backbones.

### Claim 5: Independent evaluators report mixed benchmark results: Artificial Analysis places v4.1-Flash at 40 on its Intelligence Index (below GLM-5.3-Flash, above V4 Pro 0813) but with strong specific-benchmark wins — AutomationBench-AA 69% (tying GPT-6 Astra, above Grok 4.6, +15 over V4 Flash 0731, +12 over V4 Pro 0813, +7 over GLM-5.3), GDPval-AA v2 gaining 164 Elo (1468→1632, overtaking Kimi K3 at 1584), and AA-LCR v1.1 at 84% (on par with GPT-5.6 Sol and Gemini 3.8 Flash) — while Vals AI separately ranks it #1 among open-weight models on its own index, ahead of Kimi K3
- **Evidence**: Named third-party benchmark orgs (Artificial Analysis, Vals AI) cited directly with specific scores in the Twitter Recap.
- **Confidence**: emerging (specific, named third-party benchmark results, not vendor self-report — but none of these are independently reproduced by this Miner, and Vals AI's own methodology note limits the eval to "1M context, 384 max output tokens, temperature 1, default top-p/top-k, and high reasoning effort," a narrow harness configuration that may not generalize)
- **Quote**: "Independent benchmark account Artificial Analysis reported that DeepSeek V4.1 Flash surpasses DeepSeek V4 Pro 0813 despite being much cheaper, scoring 40 on the Artificial Analysis Intelligence Index, just below GLM-5.3-Flash and above the latest V4 Pro" and "Vals called it the new #1 open-weight model on the Vals Index, ahead of Kimi K3, at just $0.30 per test, the cheapest model in the open-weight top 10"
- **Our assessment**: The general Intelligence Index score (40) is notably *lower* than the ~50 Intelligence Index score `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 5 reported for the July V4-Flash-0731 checkpoint on the same Artificial Analysis metric — an apparent regression on the aggregate index despite clear improvement on several named sub-benchmarks (AutomationBench, GDPval-AA v2, AA-LCR) versus V4 Flash 0731 and V4 Pro 0813 specifically. Neither this source nor the 0731 note specifies which version of Artificial Analysis's Intelligence Index suite was used at each measurement date, and AA is known to periodically revise its benchmark composition (the "GDPval-AA v2" naming in this same source shows AA versions its own sub-benchmarks explicitly). Per the precedent set in `blog-latentspace-ainews-death-of-params-glm53.md` Claim 7 for a similar cross-time AA Index comparison, this is flagged here as a discrepancy worth independent verification rather than filed as a MINER.md §4a contradiction — the two figures may simply be non-comparable across index versions rather than a genuine disagreement about the model's capability trajectory.

### Claim 6: Artificial Analysis reports v4.1-Flash is among the most verbose models it has measured, averaging 89k tokens per Intelligence Index task — 25% more than GLM-5.3, 29% more than GLM-5.3-Flash, 62% more than V4 Pro 0813, and even above Fable 5.1 and Claude Opus 5 — yet estimates just $0.27 per Intelligence Index task, roughly 7× below GLM-5.3/Kimi K3 and ~2.5× below V4 Pro 0813, thanks to ultra-cheap token pricing
- **Evidence**: Named third-party benchmark org (Artificial Analysis) figures reported directly in the Twitter Recap, alongside the model's stated API pricing ($0.30/1M input, $1.20/1M output, cached input $0.006/1M, plus a 50% off-peak discount).
- **Confidence**: emerging (specific, named third-party cost/verbosity measurement, not vendor self-report, but not independently reproduced by this Miner)
- **Quote**: "Artificial Analysis also says V4.1 Flash is among the most verbose models measured, averaging 89k tokens per Intelligence Index task—25% more than GLM-5.3 (71k), 29% more than GLM-5.3-Flash (69k), 62% more than V4 Pro 0813 (55k), and even above Fable 5.1 (78k) and Claude Opus 5 (73k)" and "Even with that verbosity, AA estimates just $0.27 per Intelligence Index task, roughly 7x below GLM-5.3 ($2.01) and Kimi K3 ($2.00), and ~2.5x below V4 Pro 0813 ($0.67)"
- **Our assessment**: This is the clearest cost-per-task data point in the source and the sharpest illustration of the asymmetric-parameter architecture's real-world payoff (Claim 1): extreme verbosity (highest of any model AA has measured) is fully absorbed by ultra-low per-token pricing, producing the lowest total task cost in its comparison set. This is the same cost-per-task metric type already established as novel-to-corpus in `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 5 (that note's V4-Flash-0731 sat at ~$0.028/task on a different chart, a number not directly comparable to this $0.27/task figure since the two sources use different benchmark-task definitions — "Cost per Task" on AA's scatter chart there vs. "per Intelligence Index task" here). For practitioners: a model that is dramatically more verbose is not automatically more expensive if its per-token price is low enough — total task cost is the decision-relevant number, not token count or per-token price alone.

### Claim 7: A cluster of local-inference reports describe full-precision v4.1-Flash running on commodity-ish hardware via SSD/NVMe offload of the "Engram" hash-table component — Fraser Price reported 200 TPS on 4 Max-Qs with 64GB system RAM (offloading a 200GB Engram table to NVMe), later improved to 300+ TPS on 4 RTX Pros with under 32GB peak system RAM; Antirez ran it via DwarfStar on a 128GB M5 Max with SSD streaming
- **Evidence**: Two named practitioners' hands-on reports (Fraser Price, Antirez — the latter is the well-known creator of Redis, already a credible technical voice) in the Twitter Recap, each with specific hardware configurations and throughput numbers.
- **Confidence**: anecdotal (individual practitioners' hands-on reports, not controlled benchmarks; no standardized task/workload is specified for the TPS figures)
- **Quote**: "Fraser Price reported full-precision DeepSeek 4.1 Flash + DSpark at 200 TPS on 4 Max-Qs with just 64GB system RAM, offloading a 200GB Engram/hash table to NVMe; he says this made keeping the full structure in RAM unnecessary and promised a vLLM recipe" and "He later improved that to 300+ TPS on 4 RTX Pros, still at full precision, with <32GB peak system RAM, using a custom vLLM fork and SSD support" and "Antirez showed DwarfStar running V4.1 Flash on a 128GB M5 Max, saying SSD streaming made it unexpectedly fast"
- **Our assessment**: This is a concrete, checkable local-deployment pattern distinct from anything else in the corpus: rather than quantizing a huge model to fit in RAM/VRAM (the approach documented for other large open models, e.g. `blog-simonwillison-deepseek-v4.md` Claim 8's "lightly quantized Flash" hope), the architecture here allows a specific *component* (the Engram hash table, ~200GB) to live on NVMe/SSD while the active compute path stays small (P8B/D16B active parameters per Claim 1), keeping full-precision weights usable on far less RAM than the model's total parameter count would suggest. This is a genuinely novel-to-corpus local-inference technique (component-selective SSD offload rather than whole-model quantization) worth flagging for any guide section on local/self-hosted model deployment.

### Claim 8: DeepSeek's post-training comments (via a quoted tweet from Jasper Lu describing the DeepSeek release thread) argue that, at this point, the ROI of improving data quality "far exceeds" that of working on novel post-training algorithms — which AINews explicitly frames as DeepSeek agreeing with Z.ai CEO Jie Tang's prior "Death of Params" argument
- **Evidence**: A quoted tweet (embedded in the article, full text captured via the page's own embed data) plus AINews's own editorial framing linking it directly to a prior AINews article about Jie Tang.
- **Confidence**: anecdotal (a third party's characterization of DeepSeek's position, quoting a tweet thread that is itself truncated mid-sentence in the embed; not a direct quote from DeepSeek's own technical report)
- **Quote**: "This is notable. DeepSeek, a lab usually first to pioneer novel algorithms and architectures, is saying that at this point, the ROI of improving data quality far exceeds that of working on novel post-training algorithms. I think this has already been true for some time for…"
- **Our assessment**: This directly corroborates `blog-latentspace-ainews-death-of-params-glm53.md` Claim 5 (Z.ai's Jie Tang framing GLM-5.3's gains as coming from ~1 month of extra RL on the *same* base architecture, not a scale jump) and that note's Claim 3 heuristic ("memorization prefers more parameters, reasoning prefers more post-training data and effective depth"). Two different frontier labs (Z.ai/GLM and DeepSeek), in the same roughly one-month window (August–September 2026), are independently reported as reframing their capability gains around data/training-recipe quality rather than novel algorithms or parameter scale — a pattern worth citing together as convergent, cross-lab evidence rather than a single vendor's rhetorical framing. The caveat from that note applies equally here: this is a vendor's own framing of its results (relayed third-hand through a quoted tweet, itself truncated), not an independently measured ablation.

### Claim 9: TeortaxesTex (a frequently-cited technical commentator already used elsewhere in this corpus) argued that V4 GA had benefited substantially from tool/skills harness access, whereas v4.1-Flash appears less dependent on harness scaffolding and performs comparatively better in "minimal harnesses"
- **Evidence**: A named individual's technical opinion in the Twitter Recap, presented as a direct comparison between the prior V4 GA release and v4.1-Flash.
- **Confidence**: anecdotal (single commentator's qualitative assessment, no controlled minimal-vs-full-harness benchmark cited)
- **Quote**: "They also argued that V4 GA had benefited massively from tool/skills harness access, whereas V4.1 appears less dependent on harness scaffolding and better in "minimal harnesses""
- **Our assessment**: This is directly relevant to harness engineering (Ch02): if accurate, it suggests v4.1-Flash's capability is less contingent on a well-built tool/skills scaffold than its predecessor — a meaningfully different practitioner consideration than raw benchmark scores, since a model that performs well "out of the box" in a minimal harness is cheaper to integrate and less brittle to harness misconfiguration than one that requires substantial scaffolding investment to reach its benchmarked capability. This is a single commentator's unverified impression, not a controlled test, so it should be flagged as a hypothesis for practitioners to check against their own harness, not cited as settled.

### Claim 10: In hands-on use, the same commentator reported that multi-agent "DSH agent teams" could degrade output quality unless a project has very clear modularity, with v4.1-Flash running solo outperforming team mode in at least one example because subagents produced "slop" or wasted tokens on unnecessary research
- **Evidence**: The same named commentator's hands-on usage report in the Twitter Recap, describing a specific failure mode (subagents producing low-value output or over-researching) rather than a generic complaint.
- **Confidence**: anecdotal (single practitioner's hands-on observation on unspecified project(s), no controlled solo-vs-team-mode benchmark)
- **Quote**: "In hands-on use, they reported that multi-agent "DSH agent teams" could degrade quality unless the project has very clear modularity, with V4.1 solo outperforming team mode in at least one example because subagents produced slop or wasted tokens on unnecessary research"
- **Our assessment**: This is a specific, concrete failure mode for multi-agent orchestration — not "multi-agent is bad" in the abstract, but "multi-agent team mode underperforms solo mode specifically when project modularity is unclear, because subagents waste tokens on unnecessary research or produce low-value output." This is a useful, falsifiable claim for the guide's multi-agent orchestration guidance: it implies a precondition (clear task/codebase modularity) for multi-agent decomposition to pay off, and names the specific failure symptom (wasted research tokens, "slop") to watch for when it doesn't. This is model/harness-specific (DeepSeek's own "DSH agent teams" feature) and a single practitioner's report, so it should be cited as an illustrative anecdote rather than a general multi-agent verdict.

### Claim 11: A separate cluster of same-day agent-research papers converges on "the harness is now a core optimization target": a Salesforce paper found training a weaker model on a stronger expert's full trajectories can hurt performance by 4–30 points after harness evolution (because the fine-tuned model adopts an incompatible planning style), with a proposed fix of rewriting only the failing turn in the weaker model's own rollout; ByteDance's HarnessDev has agents build and iteratively improve their own runnable harnesses, with only 34/64 changes transferring directionally to held-out tasks; Qwen's "Elastic Horizon" is a closed-loop controller tracking the 90th percentile of successful trajectory lengths to adjust the maximum interaction horizon, improving success while saving up to 25% of trajectory tokens; and PARSER replaces sequential chunk reading with parallel frozen subagents plus an RL-trained lead agent over scatter-gather rounds, reporting +12 points at 896K context and up to 11× lower latency
- **Evidence**: Four separately attributed paper/writeup summaries in the Twitter Recap (via named aggregator accounts omarsar0, Sumanth_077, dair_ai), each describing a distinct research result unrelated to DeepSeek specifically.
- **Confidence**: emerging (specific, named papers with reported quantitative results, but this Miner accessed only AINews's summary of each, not the underlying papers themselves, so the reported figures are third-hand and unverified against the primary sources)
- **Quote**: "Several papers pushed on a common theme: the harness is now a core optimization target. A widely shared Salesforce paper summary from omarsar0 showed that training a weaker model on a stronger expert's full trajectories can hurt performance by 4–30 points after harness evolution, because the fine-tuned model adopts an incompatible planning style. The proposed fix—rewrite only the failing turn in the weaker model's own rollout—preserves model-harness fit."
- **Our assessment**: This cluster is tangential to the DeepSeek v4.1-Flash headline but directly corroborates `blog-latentspace-ainews-megakernels-dead-and-back.md` Claim 6 (a separate paper finding 5–30× swings in cost-per-success attributable to harness/scaffolding choice alone) — two independent same-corpus sources now report large, harness-attributable performance swings (4–30 points here, 5–30× cost-per-success there) from different research groups within about a month of each other. The Salesforce finding is especially notable for the guide's harness-engineering material: it is a specific, mechanistic explanation (incompatible planning style transfer) for why naive distillation-by-trajectory-imitation can *hurt* a weaker model, plus a named mitigation (surgical single-turn rewriting rather than full-trajectory imitation) — this is new, actionable methodology not previously in this corpus's harness-distillation coverage.

### Claim 12: DeepSeek is reportedly "soft retiring" DeepSeek V4 Pro: V4 Pro traffic is being automatically routed to V4.1-Flash and billed at the cheaper Flash pricing until a V4.1 Pro launches, with commenters speculating V4 Pro's GA release "suffered from reward hacking and poor scaling" and was "not performing meaningfully better than the flash model despite being nearly 6 times the size"
- **Evidence**: A Reddit thread (r/LocalLLaMA, "Deepseek Has Soft Retired Deepseek V4 Pro," Activity 1598) summarized in the Reddit Recap, describing DeepSeek's own routing/pricing change plus commenter speculation about the cause.
- **Confidence**: anecdotal for the speculative cause (reward hacking, poor scaling — unattributed commenter opinion); the routing/billing change itself is reported as a direct observation of DeepSeek's own API behavior, though not confirmed by an official DeepSeek statement in this source
- **Quote**: "The image is a screenshot of a tweet saying DeepSeek is effectively "soft retiring" DeepSeek V4 Pro: V4 Pro traffic will be automatically routed to DS V4.1 Flash and billed at cheaper Flash pricing until V4.1 Pro launches." and "Several commenters argued DeepSeek V4 Pro GA underperformed relative to its size, with one claiming it showed a "high degree of reward hacking" and was not meaningfully better than the Flash model despite being nearly 6× larger."
- **Our assessment**: This directly extends `blog-vercel-deepseek-v4-pro-updated-weights.md`, which documented V4 Pro receiving an updated-weights refresh via Vercel AI Gateway as recently as August 12, 2026 — barely a month before this source reports DeepSeek routing V4 Pro traffic away from itself entirely in favor of the smaller, cheaper v4.1-Flash. Read together, the two notes show a fast reversal: an August weights update to V4 Pro, followed within weeks by DeepSeek deprioritizing V4 Pro in favor of a smaller Flash-class model that reportedly outperforms it — consistent with the "smaller Flash variant beats larger Pro variant" pattern the same Reddit Recap explicitly compares to a similar Google small-beats-large-model dynamic. Practitioners with pinned V4 Pro model IDs (per that Vercel note's dated-ID pinning pattern) should treat this as a signal that the V4 Pro line itself may be reaching end-of-life, independent of any specific weight-version pin.

## Concrete Artifacts

### DeepSeek's own launch tweet (verbatim, quoted in article)

```
DeepSeek@deepseek_ai

🚀 Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.

🔹 Introducing the smallest model in our new architecture family, with native visual understanding.
🔹 Designed for greater capability, faster inference, higher throughput, and scaling to larger models.

Source: https://x.com/deepseek_ai/status/2097930608790167907, via
Latent Space AINews, Sep 12, 2026
```

### Parameter-count breakdown (Reddit thread, via AINews Reddit Recap)

```
Backbone (MoE FFN, FP4):        551.566B params
Engram (hash-table component):  196.929B params
------------------------------------------------
Backbone + Engram:              ~748.5B params

Optional additions:
  DSpark/MTP:                   14.225B params
  Vision encoder:                0.485B params
------------------------------------------------
Full stored model:              ~763.21B params / 511.76 GB

Prior (disputed) estimates: 284B, 305B, 485B, 522B, 552B
Cause of confusion: FP4-packed weights miscounted as bytes
rather than two params/byte in some estimates (similar to
GLM-5.3-Flash-NVFP4); vLLM's own recipe page listed 522B
before correcting.

Source: Reddit r/LocalLLaMA, "Deepseek V4.1 Flash is 748B, not
552B" (Activity: 575), via Latent Space AINews, Sep 12, 2026
```

### Independent benchmark placements (Artificial Analysis, Vals AI — via AINews Twitter Recap)

```
Metric                          v4.1-Flash          Comparison
--------------------------------------------------------------------
AA Intelligence Index           40                  below GLM-5.3-Flash,
                                                      above V4 Pro 0813
AutomationBench-AA              69%                 ties GPT-6 Astra (69%),
                                                      above Grok 4.6 (67%),
                                                      +15 vs V4 Flash 0731,
                                                      +12 vs V4 Pro 0813 (57%),
                                                      +7 vs GLM-5.3 (62%)
GDPval-AA v2 (Elo)               1632 (+164)         from 1468; overtakes
                                                      Kimi K3 (1584)
AA-LCR v1.1                     84%                  on par with GPT-5.6 Sol,
                                                      Gemini 3.8 Flash (84%)
Verbosity (tokens/task, avg)    89k                  most verbose AA has
                                                      measured; +25% vs
                                                      GLM-5.3 (71k), +29% vs
                                                      GLM-5.3-Flash (69k),
                                                      +62% vs V4 Pro 0813 (55k)
Cost per Intelligence-Index task $0.27               ~7x below GLM-5.3
                                                      ($2.01)/Kimi K3 ($2.00),
                                                      ~2.5x below V4 Pro
                                                      0813 ($0.67)
API pricing                     $0.30/$1.20 per 1M   cached input $0.006/1M;
                                 input/output          +50% off-peak discount
Vals Index rank                 #1 open-weight        ahead of Kimi K3,
                                                       $0.30/test

Source: Latent Space AINews, Sep 12, 2026, attributed to
@ArtificialAnlys and @ValsAI
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-deepseek-v4.md` Claims 4–5 (DeepSeek's own paper-cited FLOPs/KV-cache reduction claims for V4-Pro/V4-Flash vs. V3.2, self-reported and unreproduced): this source's Claim 3 (4× HBM / 8× SSD / 437× KV-cache/storage reduction claims for v4.1-Flash) is the same pattern of vendor-reported, methodology-light efficiency multipliers at a new generation — DeepSeek consistently leads each release with large self-reported KV-cache-reduction figures.
  - `blog-latentspace-ainews-death-of-params-glm53.md` Claim 5 (Z.ai/Jie Tang: GLM-5.3's gains came from ~1 month of extra RL on GLM-5.2's unchanged base architecture, not a scale jump) and Claim 3 (the "memorization prefers parameters, reasoning prefers post-training data" heuristic): this source's Claim 8 (DeepSeek's own post-training comments, per a quoted tweet, that data-quality ROI now exceeds novel-algorithm ROI) is a second frontier lab, in the same roughly one-month window, independently reframing capability gains around data/training-recipe quality over architecture or parameter scale.
  - `blog-latentspace-ainews-megakernels-dead-and-back.md` Claim 6 (a paper finding 5–30× swings in cost-per-success attributable to harness/scaffolding choice alone): this source's Claim 11 (Salesforce's finding that trajectory-imitation distillation can hurt a weaker model 4–30 points due to incompatible planning style) is a second, independent paper-level finding that harness/scaffolding choices — not just model capability — drive large performance swings.
  - `blog-latentspace-ainews-kimi-k3-wiki-memory.md` Claim 6 (Kimi Delta Attention: a fast-weights mechanism maintaining fixed-size learned state instead of paying full attention cost at long context, claiming up to 6× faster/cheaper throughput at 1M context): this source's Claims 1 and 3 (v4.1-Flash's prefill/decode split and KV-cache reductions) is a second, architecturally distinct example of a frontier open-weights lab attacking long-context KV/attention cost directly rather than through raw parameter or compute scaling — corroborating a broader industry-wide shift toward attention/cache-efficiency architecture innovation.

- **Contradicts**: None filed as a formal MINER.md §4a contradiction. Claim 5 flags a discrepancy — this source's AA Intelligence Index score of 40 for v4.1-Flash is *lower* than the ~50 AA Intelligence Index score `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 5 reports for the July V4-Flash-0731 checkpoint on the same named metric, despite v4.1-Flash improving on several specific sub-benchmarks versus V4 Flash 0731 (AutomationBench-AA: +15 points). This is not filed as a contradiction because neither source specifies which version of Artificial Analysis's Intelligence Index suite was used at each measurement date, and AA is independently shown (via this same source's own "GDPval-AA v2" naming) to version its sub-benchmarks explicitly — the two figures may be non-comparable across index revisions rather than a genuine disagreement about the model's capability trajectory. This follows the same non-filing precedent set in `blog-latentspace-ainews-death-of-params-glm53.md` Claim 7 for a structurally identical cross-time AA Index comparison.

- **Extends**:
  - `blog-vercel-deepseek-v4-pro-updated-weights.md`: that note documented an August 12, 2026 updated-weights refresh for V4 Pro on Vercel AI Gateway, with a dated-ID pinning mechanism for reproducibility. This source's Claim 12 extends that timeline forward by about a month: DeepSeek is now reportedly routing V4 Pro traffic to v4.1-Flash entirely and billing it at Flash pricing, a "soft retirement" that post-dates and outpaces that note's weight-refresh announcement — practitioners who pinned a dated V4 Pro model ID per that note's guidance should now also check whether V4 Pro remains a supported inference target at all.
  - `blog-simonwillison-deepseek-v4-flash-0731.md`: that note documented the July V4-Flash-0731 checkpoint's specs (304B, 167GB, $0.14/$0.27 per M tokens) and an unverified "substantially enhanced agentic capabilities" vendor claim (its Claim 1). This source extends the DeepSeek Flash lineage two months further with a genuinely new architecture (not just a checkpoint refresh) and, unlike that note, provides multiple independently-attributed agentic-benchmark results (AutomationBench-AA, GDPval-AA v2) that at least partially substantiate an agentic-capability improvement claim for the v4.1 generation specifically.
  - `blog-simonwillison-deepseek-v4.md`: that note established V4-Pro (1.6T total/49B active) and V4-Flash (284B/13B active) as April 2026 baselines, both symmetric decoder-only MoE architectures. This source extends the DeepSeek model family's architectural history with a structural break (Claim 1's causal encoder-decoder split) that neither of DeepSeek's April 2026 models exhibited.

- **Novel**:
  - **Asymmetric prefill/decode active-parameter architecture** (Claim 1): the first model in this corpus to report different active-parameter counts for the input/prefill phase versus the output/decode phase of inference, rather than a single active-parameter figure applying uniformly.
  - **Component-selective SSD offload for a hash-table ("Engram") component while keeping full model precision** (Claim 7): distinct from the whole-model quantization-for-local-deployment pattern documented elsewhere in the corpus (e.g. `blog-simonwillison-deepseek-v4.md` Claim 8).
  - **A documented case of a model's basic total-parameter count being disputed and corrected via direct safetensors inspection, with a named root cause (FP4-packing miscounted as bytes)** (Claim 4): a concrete illustration that even fundamental model specs should be checked against a primary technical report or direct file inspection rather than early community estimates or a single vendor page.
  - **A specific, named multi-agent-team failure mode** (Claim 10): "subagents produced slop or wasted tokens on unnecessary research" as the concrete symptom of multi-agent decomposition underperforming solo-agent mode absent clear project modularity — more specific than the general multi-agent-coordination themes already in the corpus (`blog-latentspace-ainews-zawinskis-law-multiagents.md`).
  - **A named mitigation for harmful trajectory-imitation distillation** (Claim 11): "rewrite only the failing turn in the weaker model's own rollout" as a specific fix for the incompatible-planning-style failure mode, not previously documented in this corpus's harness/distillation coverage.

## Guide Impact

- **Chapter 03 (Model Serving & Routing) / Chapter 04 (Deployment Infrastructure)**: Add Claim 1 (asymmetric prefill/decode active-parameter architecture) as a new dimension for cost-estimation frameworks: for this model family, input-heavy vs. output-heavy workloads have genuinely different compute costs beyond simple token-count multiplication. Pair with Claim 6's cost-per-task data ($0.27/task despite highest-measured verbosity) as a worked example of why per-token price and token-count-per-task should be evaluated together, not separately, when comparing models — extending the cost-per-task metric framing already recommended from `blog-simonwillison-deepseek-v4-flash-0731.md`.

- **Chapter 04 (Deployment Infrastructure / Local Deployment Patterns)**: Add Claim 7 (component-selective SSD/NVMe offload of the Engram hash-table, keeping the small active-parameter compute path in RAM/VRAM) as a new local-deployment pattern distinct from whole-model quantization — recommend the guide note this as a technique to evaluate for large sparse/hash-augmented models specifically, separate from the "quantize everything to fit in unified memory" pattern already documented elsewhere in the corpus.

- **Chapter 02 (Harness Engineering)**: Add Claim 9 (reduced harness-dependency vs. prior DeepSeek generation) and Claim 10 (the specific multi-agent-team failure mode: subagents producing "slop" or wasting tokens on unnecessary research absent clear modularity) as illustrative, model-specific anecdotes for a section on when multi-agent decomposition helps vs. hurts. Add Claim 11's Salesforce trajectory-imitation-distillation finding (4–30 point regressions from incompatible planning-style transfer, with a named single-turn-rewrite mitigation) as concrete, actionable methodology for any guide section on distilling or fine-tuning smaller models from larger models' rollouts.

- **Chapter 02 (Model Selection / Vendor Claims)**: Use Claim 4 (the disputed, safetensors-corrected parameter count) as a worked example of why the guide should recommend verifying a model's basic specs against a primary technical report or direct file inspection rather than early press/community figures, and use Claim 12 (V4 Pro's rapid "soft retirement" a month after a weights refresh) as a caution that even a recently-updated model ID in a fast-moving open-weights family may be deprioritized on a timescale of weeks, not years.

## Extraction Notes

- **Fetch method**: WebFetch was not used for this extraction; the article was fetched directly via `curl` with a browser user-agent to obtain the raw page HTML, then the `<div class="body markup">` content div was isolated and tag-stripped to plain text (preserving link targets inline as `text (URL)`). All `Quote` fields in this note were located and copied character-for-character from that raw HTML (including em dashes and curly quotes/apostrophes), following the same approach used in `blog-latentspace-ainews-death-of-params-glm53.md` and `blog-vercel-deepseek-v4-pro-updated-weights.md` Extraction Notes. The Jasper Lu tweet quote (Claim 8) was extracted from the embedded tweet's own JSON `data-attrs` payload (`full_text` field) rather than the surrounding prose, since the tweet's full text is not otherwise rendered in the article body.
- **No paywall encountered**: unlike several other AINews digests already in this corpus (`blog-latentspace-glm52-open-frontier-parity.md`, `blog-latentspace-ainews-death-of-params-glm53.md`), this issue's raw HTML included the full "AI Reddit Recap" section (all four r/LocalLLaMA/r/localLLM subsections) with no "Keep reading with a 7-day free trial" gate text found anywhere in the fetched HTML, despite the page's own JSON-LD metadata stating `"isAccessibleForFree": false`. The full digest was read in its entirety.
- **Scope decisions**: This is an unusually long omnibus digest. Beyond the DeepSeek-focused claims and the harness-research cluster (Claim 11, judged sufficiently relevant to Ch02 to extract), several other same-day items were read in full but not extracted as standalone claims because they are unrelated to the Prospector's flagged focus and each is a short vendor/product announcement without benchmark depth tying it to DeepSeek or harness engineering specifically: OpenAI's GPT-Live-1 voice model and Agents API launch, OpenAI's ChatGPT Work Data agent, Cognition's SWE-2 release and Devin Voice, Cursor's "Projects" persistent-thread feature, and the safety/governance discussion (Anthropic's threat intelligence report, chain-of-thought monitorability debate, Hugging Face's Open Alignment team). A future Miner could mine any of these separately if they become a priority topic — they were noted but deliberately left unextracted here to keep this note focused on the issue's flagged DeepSeek architecture/efficiency/cost topic.
- **No contradiction issues filed.** The one discrepancy identified (Claim 5's AA Intelligence Index score appearing to regress from ~50 to 40 across two DeepSeek Flash releases) is reported inline with an explanation (likely non-comparable index versions) rather than filed as a MINER.md §4a contradiction, following the precedent in `blog-latentspace-ainews-death-of-params-glm53.md` Claim 7 for a structurally identical situation.
- **Confidence calibration: emerging.** The architectural claims (Claims 1–3) and the parameter-count correction (Claim 4) are independently corroborated by named third parties (Artificial Analysis, a methodologically-described Reddit investigation) and rated `emerging`; the benchmark placements (Claims 5–6) are `emerging` (named, credible third-party benchmarking orgs, not independently reproduced); the local-deployment reports (Claim 7), post-training framing (Claim 8), harness-dependency and multi-agent observations (Claims 9–10), and the V4-Pro-retirement Reddit thread's speculative cause (Claim 12) are `anecdotal` (individual practitioner reports or unverified community speculation). The note-level confidence reflects this mix: solid on independently-corroborated architecture and benchmark facts, weaker on the practitioner anecdotes and vendor framing.
