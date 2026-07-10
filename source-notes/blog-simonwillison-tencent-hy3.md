---
source_url: https://simonwillison.net/2026/Jul/6/hy3/
source_type: blog-post
title: "tencent/Hy3"
author: Simon Willison
date_published: 2026-07-06
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: emerging
issue: "#1717"
---

# tencent/Hy3

> Willison's short link-blog post on Tencent's Apache-2.0 Hy3 release (295B
> total / 21B active MoE, 256K context) is the entry point to two more
> substantive sources followed for this note: Tencent's own Hugging Face
> model card (concrete architecture, deployment recipes, and self-reported
> reliability/hallucination-rate improvements) and Max Woolf's independent
> economic investigation of the Hy3 *preview* model's mysterious OpenRouter
> popularity a full six weeks before Willison's post. Together they document
> a Chinese MoE release with an unusually high active-parameter ratio (~7.1%)
> for its size class, and a real-world case study in why stated LLM API
> prices are no longer a reliable proxy for effective cost.

## Source Context

- **Type**: blog-post (Willison's link-blog format, ~120 words of original
  commentary plus an inline pelican-SVG test image; auto-discovered via
  trusted feed `simon-willison`). Per MINER.md §1, this note follows two
  substantive linked pages: Tencent's own Hy3 model card on Hugging Face
  (`huggingface.co/tencent/Hy3/raw/main/README.md`, fetched directly, not
  paraphrased) and Max Woolf's `minimaxir.com` post on the Hy3 *preview*
  model's OpenRouter ranking, which Willison links as an "Update" appended to
  his post.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo (creator of Django, Datasette, `sqlite-utils`, `llm`).
  His "pelican riding a bicycle" SVG test is his recurring informal
  cross-model benchmark. For this post he is a curator/first-hand tester, not
  an independent benchmarker — the only original claim of his own is the
  pelican-SVG result and the "free on OpenRouter until July 21st" access
  note. Max Woolf, whose post Willison links, is a Senior Data Scientist at
  BuzzFeed who works with AI/ML tooling; his post is a data-driven
  investigation using OpenRouter's own published usage and pricing tables,
  not vendor marketing.
- **Scope**: Covers the Hy3 model's specs, benchmark claims, license,
  availability, and one anecdotal capability test (pelican SVG). Via the
  Hugging Face model card, also covers architecture detail, deployment
  recipes (vLLM/SGLang), and Tencent's self-reported reliability/
  hallucination improvements over the April "Hy3 Preview." Via Woolf's post,
  also covers the *preview* model's real-world OpenRouter usage and pricing
  economics (a different model checkpoint, six weeks earlier, not the
  Apache-2.0 release Willison covers). Does NOT cover independent
  third-party benchmark reproductions, safety evaluation, or any
  agentic-coding-harness integration beyond the SWE-bench numbers Tencent
  self-reports.

## Extracted Claims

### Claim 1: Hy3 is a 295B-parameter MoE model with 21B active parameters and 3.8B MTP-layer parameters, released by Tencent's Hy Team as a successor to an April "Hy3 Preview"
- **Evidence**: Stated identically in both Willison's post and Tencent's own Hugging Face model card (word-for-word — Willison appears to quote the model card directly).
- **Confidence**: settled (vendor-published model metadata, corroborated across two independent pages)
- **Quote**: "Hy3 is a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and 3.8B MTP layer parameters, developed by the Tencent Hy Team. Following the Hy3 Preview launch in late April, we gathered feedback from 50+ products and scaled up post-training with higher quality data."
- **Our assessment**: At 21B/295B (~7.1%), Hy3's active-parameter ratio is notably higher than other recent large MoE releases in this corpus: DeepSeek V4-Pro sits at 49B/1.6T (~3%, `blog-simonwillison-deepseek-v4.md` Claim 1) and Microsoft's MAI-Thinking-1 at 35B/1T (~3.5%, `blog-simonwillison-microsoft-mai-models.md` Claim 1). A higher active ratio at a smaller total size (295B vs. >1T) trades some of the extreme sparsity-driven inference-cost advantage for a more moderate total footprint (598GB full weights vs. 865GB+ for the largest models) — a different point on the size/cost/capability curve worth tracking as a landscape data point.

### Claim 2: Hy3 has 192 experts with top-8 activated, 80 transformer layers plus 1 MTP layer, 64 attention heads with GQA (8 KV heads, 128 head dim), a 4096 hidden size, 120832 vocabulary size, and 256K context length
- **Evidence**: Tencent's own model-card specification table (Hugging Face README.md, fetched directly).
- **Confidence**: settled (primary-source architecture specification)
- **Quote**: "| Number of Experts | 192 experts, top-8 activated |" / "| Context Length | 256K |" / "| Attention Heads | 64 (GQA, 8 KV heads, head dim 128) |"
- **Our assessment**: This is the first architecture-level (not just total/active parameter count) documentation of a Tencent Hunyuan-family model in this corpus. The 256K context is below the 1M-token windows now common in the largest 2026 open-weight releases (DeepSeek V4-Pro, per `blog-simonwillison-deepseek-v4.md`), positioning Hy3 as competitive on parameter efficiency but not on context length.

### Claim 3: Tencent reports Hy3's hallucination rate improved from 12.5% to 5.4%, and commonsense error rate from 25.4% to 12.7%, versus the Hy3 Preview, via "fine-grained data cleaning and training constraints"
- **Evidence**: Tencent's own model card, "More Reliable Product Experiences" section, self-reported internal evaluation — no external benchmark or methodology disclosure beyond the stated framing.
- **Confidence**: anecdotal (vendor self-reported internal evaluation; no independent verification, no disclosed methodology or sample size)
- **Quote**: "Guided by the ideal of \"answer when grounded, state when evidence is missing, do not conflate sources or fabricate data,\" we implemented fine-grained data cleaning and training constraints. In internal evaluations based on real-world scenarios, Hy3's hallucination rate dropped from 12.5% to 5.4%, and commonsense error rates fell from 25.4% to 12.7%."
- **Our assessment**: A greater-than-50% relative reduction in self-reported hallucination rate between a preview and GA release is a large claimed jump with zero external verification — treat as a vendor marketing signal, not a settled capability fact, following the same skepticism this corpus applies to Microsoft's "commercially licensed data" claim in `blog-simonwillison-microsoft-mai-models.md` Claim 4 (a vendor claim that did not survive scrutiny). Worth flagging for future verification if independent evals of Hy3 appear.

### Claim 4: Tencent reports Hy3 scored 78 on SWE-bench Verified and 57.9 on SWE-bench Pro, and that accuracy variance across agent scaffoldings (CodeBuddy, Cline, KiloCode) on SWE-bench Verified stays within 4%
- **Evidence**: Tencent's own model card benchmark section; the scaffolding-variance claim is presented as evidence of production reliability, not just raw capability.
- **Confidence**: anecdotal (vendor self-reported benchmark; no independent reproduction)
- **Quote**: "Hy3 also generalizes across different agent scaffoldings. On SWE-Bench Verified, accuracy variance across scaffoldings like CodeBuddy, Cline, and KiloCode remains within 4%."
- **Our assessment**: The scaffolding-generalization claim is a more practitioner-relevant signal than the raw SWE-bench score itself, since it speaks to whether a model's coding competence is scaffold-dependent (a known failure mode discussed elsewhere in this corpus re: agent harness sensitivity) — but again, self-reported with no named comparison baseline for what "normal" cross-scaffold variance looks like.

### Claim 5: Tencent ran a blind evaluation with 270 experts on real work tasks, scoring Hy3 at 2.67/4 versus GLM-5.1 at 2.51/4, with the largest advantage in frontend development, data & storage, and CI/CD tasks
- **Evidence**: Tencent's own model card, explicitly framed as a response to benchmark skepticism ("we don't think public benchmark scores tell the full story").
- **Confidence**: anecdotal (vendor-run comparative human evaluation; panel composition, task selection, and scoring rubric not disclosed beyond the headline numbers)
- **Quote**: "We don't think public benchmark scores tell the full story. So we ran a blind evaluation with 270 experts using tasks from their work, and Hy3 scored 2.67/4, outperforming GLM-5.1 at 2.51/4."
- **Our assessment**: This is a direct head-to-head claim against GLM-5.1 (documented in `blog-simonwillison-glm51.md`, a 754B MIT-licensed Z.ai model), a genuine comparison point rather than a self-serving benchmark cherry-pick, but it is still Tencent's own panel and rubric with no disclosed selection criteria for the "270 experts." A 2.67 vs. 2.51 margin on an unscaled 4-point rubric is a small absolute gap regardless of who ran the study.

### Claim 6: The full-precision Hy3 weights are 598GB on Hugging Face; the FP8-quantized version (Hy3-FP8) is 300GB; Hy3 requires 8 GPUs with large memory capacity (H20-3e recommended) to serve
- **Evidence**: Willison's post states the 598GB/300GB sizes directly (matching Hugging Face repo file sizes); Tencent's model card states the 8-GPU/H20-3e serving requirement.
- **Confidence**: settled (file sizes and vendor deployment guidance are directly checkable facts)
- **Quote**: "The full-sized model is 598GB on Hugging Face, and the FP8 quantized one is 300GB." / "Hy3 has 295B parameters in total. To serve it on 8 GPUs, we recommend using H20-3e or other GPUs with larger memory capacity."
- **Our assessment**: This is a self-hosting-infeasible model for all but well-resourced teams — 8 GPUs of H20-3e-class memory capacity is a materially higher bar than the single-machine local-model setups documented in `blog-fowler-boeckeler-local-models-viability.md` (which topped out at a Qwen3.6 35B MoE model on Apple Silicon). Hy3's practical accessibility for most practitioners is therefore via hosted inference (OpenRouter), not self-hosting, despite the Apache 2.0 license nominally permitting it.

### Claim 7: Hy3 ships with dedicated deployment recipes for vLLM (with MTP speculative decoding) and SGLang (with EAGLE-algorithm speculative decoding), including exact CLI flags for both
- **Evidence**: Tencent's model card provides copy-pasteable `vllm serve` and `python3 -m sglang.launch_server` commands with specific flags (`--speculative-config.method mtp`, `--tool-call-parser hy_v3`, `--speculative-algorithm EAGLE`, etc.).
- **Confidence**: settled (verbatim vendor-provided deployment commands)
- **Quote**: `vllm serve tencent/Hy3 --tensor-parallel-size 8 --speculative-config.method mtp --speculative-config.num_speculative_tokens 2 --tool-call-parser hy_v3 --reasoning-parser hy_v3 --enable-auto-tool-choice --port 8000 --served-model-name hy3`
- **Our assessment**: The presence of named tool-call and reasoning parsers (`hy_v3`/`hunyuan`) built into both serving frameworks at release, plus MTP/EAGLE speculative-decoding support, signals Tencent invested in production-serving ergonomics rather than shipping weights alone — a stronger production-readiness signal than the self-reported benchmark numbers.

### Claim 8: Hy3 is available for free on OpenRouter until July 21st (2026), and Willison's pelican-SVG test on it produced a materially better result than his earlier test of the Hy3 Preview
- **Evidence**: Willison's direct first-hand statement and comparison of two of his own test runs (linked images).
- **Confidence**: anecdotal (single first-hand test, informal creative-code benchmark, not a systematic evaluation)
- **Quote**: "It's available for free on OpenRouter until July 21st. I had it \"Generate an SVG of a pelican riding a bicycle\" there and got this... When I tried that one I got back this pelican which wasn't as good as today's but did have a \"Change Pelican Color\" button, a first from any model."
- **Our assessment**: Consistent with Willison's established pattern (`blog-simonwillison-glm51.md`, `blog-simonwillison-deepseek-v4.md`) of using the pelican-SVG test as a cheap first-look capability signal, not a rigorous evaluation. The "Change Pelican Color" button detail from the earlier preview is a notable emergent-behavior anecdote (unprompted interactive UI generation) but is not present in today's release per Willison's own comparison.

### Claim 9: A distinct, earlier "Hy3 preview" checkpoint (not the Apache-2.0 GA release covered above) unexpectedly topped OpenRouter's token-usage rankings by more than 50% over Claude, for reasons Max Woolf's investigation could not fully explain
- **Evidence**: Max Woolf's `minimaxir.com` post, using OpenRouter's own published AI Model Rankings and per-model usage/pricing data, retrieved May 25, 2026.
- **Confidence**: emerging (data-driven investigation using primary platform data, but the central question — *why* — is explicitly left unresolved by the author)
- **Quote**: "Two new models are now beating LLM darling Claude in terms of token usage and by more than 50%?... I've never heard of Hy3 or anyone talking about it." / "Overall, I still don't understand the popularity of Hy3 preview on OpenRouter."
- **Our assessment**: This predates and is separate from the Hy3 GA release Willison covers — the preview checkpoint Woolf investigated was pulled from its free OpenRouter SKU around May 8, 2026, well before Willison's July 6 post. It's included here because it's the source Willison himself links as necessary background, and because it surfaces two mechanisms (below, Claims 10-11) directly relevant to how practitioners should read any vendor/OpenRouter pricing and usage claim, including Hy3's own.

### Claim 10: Effective (cache-adjusted) API pricing can diverge sharply from stated per-token pricing — Hy3 preview's stated $0.066/1M input was cheaper than DeepSeek V4 Flash's $0.10/1M, but Hy3 preview's cache-adjusted effective price ($0.034/1M, at a 44% cache-read cost from provider SiliconFlow) was nearly double DeepSeek V4 Flash's effective price when served directly by DeepSeek ($0.018/1M, at a 2% cache-read cost)
- **Evidence**: Woolf's post directly comparing OpenRouter's published "effective pricing" tables (which account for cache-hit savings) against stated list prices for both models.
- **Confidence**: settled (published, checkable OpenRouter pricing data as of the post's May 25, 2026 retrieval date; subject to change as OpenRouter pricing updates hourly per the post)
- **Quote**: "Comparing apples to apples with Hy3 preview, the effective pricing for Hy3 preview as noted on its model page from SiliconFlow (a whopping 44% cache read cost) is $0.034/1M: nearly double DeepSeek V4 Flash from DeepSeek!"
- **Our assessment**: This is the single most practically important claim in the corpus this note contributes: stated LLM API prices are increasingly unrepresentative of actual cost once cache-hit economics are included, because (per Claim 11 below) 98% of tokens in typical agentic usage are now input tokens subject to caching. A practitioner comparing "sticker" prices across providers/models — including any future Hy3 pricing — should demand cache-adjusted effective pricing, and should also account for which specific provider serves a request when a model (like Hy3 or DeepSeek V4 Flash) is available through multiple OpenRouter providers with very different cache-read cost ratios.

### Claim 11: Aggregate LLM API token usage has shifted to roughly 98% input / 2% output tokens, driven by agentic workflows that resend full conversation history on every turn, making prompt-caching economics the dominant cost factor
- **Evidence**: Woolf's post derives this ratio from OpenRouter's own published usage breakdown for Hy3 preview and generalizes it with an explanation of why (stateless LLM calls resending full context each turn).
- **Confidence**: emerging (single-model derived statistic, but the underlying mechanism — full-context resend per turn in agentic loops — is a well-understood, verifiable property of how LLM APIs work, not specific to Hy3)
- **Quote**: "LLM calls are still stateless, which means that after every turn (including user messages to the LLM asking questions), all of the tokens in the current conversation thread are reprocessed, meaning that in the case of agents, the count of input tokens increases cumulatively with each successive message... if you do the math on the numbers presented here, the input-token-to-output-token breakdown on LLM API calls is now 98% input, 2% output in aggregate."
- **Our assessment**: This mechanistic point (full-context resend per agent turn) is the reason cache-read pricing dominates effective cost, and is a durable, model-agnostic fact about agentic LLM usage rather than an Hy3-specific finding — worth citing generally whenever this corpus discusses agent cost economics, not just in an Hy3-specific context.

## Concrete Artifacts

### Hy3 model card specification table (Tencent, Hugging Face `tencent/Hy3/README.md`, retrieved 2026-07-10)
```
| Property | Value |
|:---|:---|
| Architecture | Mixture-of-Experts (MoE) |
| Total Parameters | 295B |
| Activated Parameters | 21B |
| MTP Layer Parameters | 3.8B |
| Number of Layers (excluding MTP layer) | 80 |
| Number of MTP Layers | 1 |
| Attention Heads | 64 (GQA, 8 KV heads, head dim 128) |
| Hidden Size | 4096 |
| Intermediate Size | 13312 |
| Context Length | 256K |
| Vocabulary Size | 120832 |
| Number of Experts | 192 experts, top-8 activated |
| Supported Precisions | BF16 |
```

### vLLM deployment recipe (Tencent model card)
```bash
export VLLM_FLASHINFER_ALLREDUCE_BACKEND=trtllm
vllm serve tencent/Hy3 \
  --tensor-parallel-size 8 \
  --speculative-config.method mtp \
  --speculative-config.num_speculative_tokens 2 \
  --tool-call-parser hy_v3 \
  --reasoning-parser hy_v3 \
  --enable-auto-tool-choice \
  --port 8000 \
  --served-model-name hy3
```

### SGLang deployment recipe (Tencent model card)
```bash
python3 -m sglang.launch_server \
  --model tencent/Hy3 \
  --tp-size 8 \
  --tool-call-parser hunyuan \
  --reasoning-parser hunyuan \
  --speculative-num-steps 2 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 3 \
  --speculative-algorithm EAGLE \
  --port 8000 \
  --served-model-name hy3
```

### OpenAI-compatible client usage (Tencent model card, showing the `reasoning_effort` control)
```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="EMPTY")

response = client.chat.completions.create(
    model="hy3",
    messages=[
        {"role": "user", "content": "Hello! Can you briefly introduce yourself?"},
    ],
    temperature=0.9,
    top_p=1.0,
    # reasoning_effort: "no_think" (default, direct response), "low", "high" (deep chain-of-thought)
    extra_body={"chat_template_kwargs": {"reasoning_effort": "no_think"}},
)
```

### Self-reported reliability deltas, Hy3 vs. Hy3 Preview (Tencent model card, "More Reliable Product Experiences")
```
Hallucination rate:          12.5% -> 5.4%
Commonsense error rate:      25.4% -> 12.7%
Multi-turn intent issue rate: 17.4% -> 7.9%
SWE-bench Verified cross-scaffolding variance: within 4% (CodeBuddy, Cline, KiloCode)
```

### Effective vs. stated pricing, Hy3 preview vs. DeepSeek V4 Flash (Max Woolf, minimaxir.com, retrieved 2026-05-25)
```
                          Stated input price   Cache-read cost   Effective input price
Hy3 preview (SiliconFlow)   $0.066/1M              44%              $0.034/1M
DeepSeek V4 Flash (13 providers avg.) $0.10/1M     20-50%           (varies by provider)
DeepSeek V4 Flash (DeepSeek direct)    $0.10/1M     2%               $0.018/1M
DeepSeek V4 Pro (DeepSeek direct)      —            0.83%            —
Aggregate token mix (Hy3 preview usage): 98% input / 2% output
```

## Cross-References

- **Corroborates**: `blog-simonwillison-deepseek-v4.md` (MoE architecture trend with low active-parameter ratios at large total scale, though Hy3's ratio is notably higher); `blog-simonwillison-microsoft-mai-models.md` (pattern of vendor self-reported comparative claims against named competitor models, and the general caution that vendor reliability/quality claims need independent scrutiny — see Claim 3's parallel to MAI's "commercially licensed data" claim); `blog-simonwillison-glm51.md` (Chinese open-weights MoE model, OpenRouter + `llm` CLI access pattern, informal pelican-SVG evaluation).
- **Contradicts**: None identified. Note a temporal, non-contradictory license change worth flagging: Woolf's May 2026 post states in a footnote that "the license for Hy3 is very restrictive in a way that could potentially prevent providers from adopting the model" — describing the *preview* checkpoint's license. The GA release covered by Willison's post is Apache 2.0. This is a license change between preview and GA, not a factual disagreement between the two sources, so no contradiction issue was filed.
- **Extends**: `blog-fowler-boeckeler-local-models-viability.md` (this note's Claim 6 supplies a concrete high-end data point — 8×H20-3e-class GPUs — against which Böckeler's single-Mac local-model ceiling can be contrasted, sharpening the self-hosting-feasibility line for large MoE models generally).
- **Novel**: First corpus documentation of a Tencent Hunyuan-family model (Hy3) and its architecture specifics. First corpus documentation of OpenRouter's cache-adjusted "effective pricing" tables and the mechanism (98%-input token ratios in agentic usage) that makes stated per-token prices misleading — a durable, broadly applicable cost-accounting point uncovered incidentally by following the linked background source rather than in the primary Hy3 announcement itself.

## Guide Impact

- **Chapter on model selection / landscape** (per Prospector triage, Ch01-02): Add Hy3 as a landscape data point — an Apache 2.0, 295B/21B-active MoE model with a notably higher active-parameter ratio (~7.1%) than other large 2026 MoE releases (DeepSeek V4-Pro ~3%, MAI-Thinking-1 ~3.5%), 256K context (below the 1M-token ceiling of the largest peers), and vendor-claimed parity with 2-5x larger flagship models — while flagging that the hallucination-rate and blind-eval improvement claims (Claims 3, 5) are vendor-self-reported and unverified.
- **Chapter on cost & efficiency** (per Prospector triage, Ch04): This note's strongest guide-relevant contribution is not about Hy3 itself but about cost accounting generally (Claims 10-11): recommend the guide explicitly warn practitioners that stated per-token LLM prices are unreliable cost signals once prompt-caching is in play, since ~98% of tokens in typical agentic sessions are now input tokens subject to highly variable cache-read pricing (2%-50%+ of input cost depending on provider) — and that comparing "cheapest model" claims requires comparing effective, cache-adjusted pricing, ideally for the specific provider a request will actually route to.
- **Chapter on deployment/self-hosting options** (if such a chapter exists): Hy3's 8×H20-3e-class GPU serving requirement (Claim 6) and its bundled vLLM/SGLang recipes with named tool-call/reasoning parsers and speculative decoding (Claim 7) are concrete, checkable data points for a "when is self-hosting a large open-weights model actually feasible" discussion, in contrast with the single-Mac local-model ceiling documented in `blog-fowler-boeckeler-local-models-viability.md`.

## Extraction Notes

- Followed three sources beyond the trigger blog post, per MINER.md §1: (1) Tencent's Hugging Face model card, fetched as raw markdown (`huggingface.co/tencent/Hy3/raw/main/README.md`) rather than via a summarizing tool, specifically so that quotes and the specification table could be reproduced verbatim rather than paraphrased; (2) Max Woolf's `minimaxir.com` post, fetched and stripped to plain text directly from the page HTML for the same verbatim-quoting reason; (3) the underlying page HTML of Willison's own post, to confirm which words were live links (the "Sponsored by: Teleport" line at the top of the page is an unrelated ad insertion, not part of the Hy3 content — verified by inspecting the raw HTML around the `fandf.co` shortlink, which resolves to a Teleport white paper unrelated to Hy3).
- Did not follow the Hacker News comment thread link or the static pelican-preview HTML page linked in Willison's post — both are single-artifact tangents (one HN comment, one static image page) with no additional substantive claims beyond what Willison's own text already states.
- Did not independently verify Tencent's self-reported benchmark numbers (SWE-bench Verified/Pro, GPQA Diamond, the 270-expert blind eval) against any third-party leaderboard; none was found linked from either source. All vendor-reported performance claims are marked `anecdotal` accordingly.
- Woolf's post concerns the earlier "Hy3 preview" checkpoint (April–May 2026), not the Apache-2.0 GA "Hy3" release that is the nominal subject of the triggering issue. Both are documented in this single note because Willison explicitly links Woolf's post as necessary background for the same model lineage, but Claims 9-11 should be read as pertaining to the preview checkpoint and its OpenRouter listing specifically, not verified to still hold for the GA release's pricing/usage pattern.
