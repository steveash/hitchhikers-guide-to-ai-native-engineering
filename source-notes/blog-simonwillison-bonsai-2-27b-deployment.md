---
source_url: https://simonwillison.net/2026/Sep/17/hn-49747390/
source_type: blog-post
title: "Comment: Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint"
author: Simon Willison (comment), with linked material from Prism ML (vendor) and named Hacker News commenters
date_published: 2026-09-17
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: emerging
issue: "#3718"
---

# Bonsai 2 27B: Deployment Instructions, Measured Throughput, and Practitioner Pushback on "Near-Lossless" Compression

> Simon Willison's cross-posted Hacker News comment gives a tested, reproducible
> recipe for running Prism ML's ternary Bonsai 2 27B GGUF via Prism's own
> llama.cpp fork, with a measured ~20-44 tok/s on an Apple M5 Pro. Read
> alongside the linked Hugging Face model card (Prism ML's detailed 14-benchmark
> "98.2% of FP16 intelligence retained" claim) and the wider Hacker News thread
> it lives in, the source also surfaces direct practitioner pushback — multiple
> independent testers reporting real quality and agentic-task failures the
> vendor's benchmark suite does not capture.

## Source Context

- **Type**: blog-post (simonwillison.net "beat" — Willison's site republishes
  his own Hacker News comments as short standalone posts under the `Comment`
  label; this one is explicitly tagged as "My comment" on HN item 49746618,
  titled "Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint").
  Published 2026-09-17 at 10:13pm per the post's own footer. The post itself
  is three short paragraphs: a link to the Hugging Face GGUF repo with a
  warning that Prism's llama.cpp fork is required, a shell recipe, and one
  throughput/anomaly observation.
- **Author credibility**: Simon Willison is a designated `trusted-feed` source
  in this corpus (creator of Django, Datasette, and the `llm` CLI tool) and a
  frequent hands-on local-model tester (`blog-simonwillison-qwen38-27b-overthinking.md`,
  `blog-simonwillison-georgi-gerganov.md`). This entry is first-person,
  tested deployment instructions and a directly measured throughput figure —
  not a vendor announcement or a controlled benchmark.
- **Scope**: Willison's own post covers only deployment mechanics (the fork
  requirement, download/build/serve commands, one throughput reading, one
  startup warning). It does **not** cover model quality, benchmark scores, or
  agentic-task performance. Because the post itself is extremely thin, this
  Miner followed three substantive linked/adjacent pages per MINER.md §1,
  all reachable from Willison's post or the HN thread it lives in: (1) the
  full Hacker News discussion thread (news.ycombinator.com/item?id=49746618,
  589 points / 200 comments at time of extraction), which the post's own "My
  comment" link points into and which contains both corroborating and
  strongly critical practitioner reports; (2) the linked Hugging Face model
  card (huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf), Prism ML's
  detailed first-party compression methodology and 14-benchmark comparison
  table; (3) Prism ML's own launch blog post (prismml.com/news/bonsai-2-27b),
  the original HN submission target, which makes the vendor's "near-lossless"
  and agentic-capability-preservation claims in marketing prose. Does NOT
  cover the linked GitHub release binaries, the linked whitepaper PDF, the
  Bonsai-demo repository's run scripts, or comments beyond roughly the first
  20 (of 200) and a keyword-directed sweep of the remainder (see Extraction
  Notes).

## Extracted Claims

### Claim 1: Prism ML's Bonsai 2 27B GGUF files require Prism's own llama.cpp fork — stock llama.cpp either rejects the quantization types outright or silently produces garbage output
- **Evidence**: Willison's own tested warning, corroborated and given a root cause by the Hugging Face model card's explicit "Stock llama.cpp will not run these files" section.
- **Confidence**: settled (directly reproduced by Willison's own working recipe, and independently explained in Prism ML's own model card documentation)
- **Quote**: "If you want to try out out the GGUFs from https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf#these-files-need-our-llamacpp-build be aware that you need Prism's llama.cpp fork to get them to work, from https://github.com/PrismML-Eng/llama.cpp/releases/tag/prism-b10685-7dffb15" (simonwillison.net, 2026-09-17)
- **Quote (model card, mechanism)**: "The ternary hybrid-attention kernels live in the [PrismML-Eng/llama.cpp](https://github.com/PrismML-Eng/llama.cpp) fork. **Stock llama.cpp will not run these files.** It rejects `PQ2_0` and `PTQ1_0` as unknown types, and it loads `Q2_0` without any warning and produces garbage, because it has no Hadamard activation runtime." (huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf README)
- **Our assessment**: This is a concrete, actionable deployment hazard that extends the corpus's existing quantization thread. `blog-latentspace-ainews-harness-drift-quantization.md` Claim 4 recorded the *predecessor* Bonsai 27B's existence and size figures without any deployment detail; this source is the first in the corpus to document that Prism's ternary format is not merely "a GGUF file" but requires a non-standard, fork-specific runtime — and that the standard runtime's failure mode is not a loud error but *silent garbage output* for one of the two packing formats (`Q2_0`, a different quant tag than the fork's own `PQ2_0`/`PTQ1_0`). For a team evaluating self-hosted quantized models, "does this require a vendor-specific inference binary, and does the wrong binary fail loudly or silently" is a more decision-relevant question than raw compression ratio.

### Claim 2: Willison measured Bonsai 2 27B running at ~20 tokens/second on an Apple M5 Pro via Prism's llama-server, jumping to 44 tokens/second after a server restart for reasons he could not explain, alongside a Metal backend warning that a required tensor API was unsupported
- **Evidence**: Willison's own direct, first-person throughput measurement and observed startup log line.
- **Confidence**: anecdotal (single practitioner, single machine, single session, unexplained 2.2x speed variance between runs)
- **Quote**: "That's running at ~20 token/second for me on an M5 Pro (after a server restart I got 44 token/second, not sure why), but I'm pretty sure something isn't working right, on startup the server said \"ggml_metal_device_init: - the tensor API is not supported in this environment - disabling\"." (simonwillison.net, 2026-09-17)
- **Our assessment**: The unexplained restart-triggered doubling, paired with the explicit "something isn't working right" self-assessment, is a useful practitioner-honesty signal: Willison is flagging his own measurement as suspect rather than reporting the higher number as representative. Claim 3 below (a named HN commenter's follow-up) resolves exactly this anomaly, which is a rare case in this corpus of a specific technical mystery in a source note being closed out within the same source thread.

### Claim 3: A named commenter (francisjp) identified the root cause of Willison's Metal "tensor API is not supported" warning as a missing `MTLCompileOptions.languageVersion` declaration in llama.cpp's Metal backend, and reported that a fix he proposed was merged upstream
- **Evidence**: A specific, named technical explanation posted directly in reply to Willison's comment in the same HN thread, with a link to the merged upstream diff.
- **Confidence**: emerging (a specific, named, checkable technical claim — a real GitHub PR link is given — but not independently verified by this Miner by opening the PR itself)
- **Quote**: "Commenting because the fix I proposed was merged in roughly 49 commits after the PrismML Fork. The \"tensor API is not supported\" warning occurred because llama.cpp's startup probe fails to compile a matmul2d kernel: Metal's tensor headers require language version 4.0, but ggml-metal-device.m previously omitted MTLCompileOptions.languageVersion, disabling the API universally." (francisjp, news.ycombinator.com/item?id=49746618, reply to Willison's comment)
- **Our assessment**: This directly resolves Claim 2's mystery and supplies a specific, actionable fact for any practitioner following Willison's recipe after this fix landed: the "tensor API not supported" warning on Apple Silicon was a startup-probe bug, not a hardware limitation, and Willison's ~20 tok/s reading was very likely running without the disabled tensor-API path's "prefill gains" (the commenter's own phrase) — meaning practitioners applying an updated fork build should expect faster prompt processing than Willison's original numbers, though this Miner has not independently measured the delta.

### Claim 4: Independent practitioners reproduced deployment success at broadly comparable throughput on both other Apple Silicon hardware (M1 Pro, ~14 tok/s) and consumer NVIDIA GPUs with as little as 8GB VRAM (RTX 3070: ~40.6 tok/s generation; RTX 3060 12GB: ~26.5 tok/s generation), using Willison's or the model card's own recipe with minor flag adjustments
- **Evidence**: Three separate named HN commenters (rahimnathwani, wombat23, zepearl) posting their own measured results using the same or a closely adapted command line, in direct reply to Willison's and each other's comments in the same thread.
- **Confidence**: emerging (three independent, named, hardware-specific reproductions with concrete numbers, though none are controlled or repeated-trial measurements)
- **Quote (rahimnathwani, M1 Pro)**: "M1 Pro, same prompt, same cli options: 32,706 tokens 38min 19s 14.22 t/s"
- **Quote (wombat23, RTX 3070 8GB)**: "I managed to run it with RTX 3070 (8GB VRAM) following the \"Quickstart\" on HF model card with minor modifications (modify the architecture 86 for your own hardware)... the parameters were suggested by gpt-5.6-luna to reduce memory footprint, as the defaults ran OOM on my gpu. result looks good: [ Prompt: 165.6 t/s | Generation: 40.6 t/s ]"
- **Quote (zepearl, RTX 3060 12GB)**: "Exact same test executed on my RTX 3060 (12 GiB VRAM, PCIe 3.0 4x slot): [ Prompt: 95.0 t/s | Generation: 26.5 t/s ]"
- **Our assessment**: This is the strongest corroborating evidence in the source: three named practitioners, three different hardware classes (an older Apple M1 Pro and two prosumer/entry-datacenter-adjacent NVIDIA cards, one with only 8GB VRAM), all successfully running the same model with only minor flag tuning (batch size reduction to avoid OOM on the 3070). This extends `blog-simonwillison-georgi-gerganov.md` and `blog-simonwillison-qwen38-27b-overthinking.md`'s local-model-viability evidence to a meaningfully lower hardware floor — 8GB VRAM is well below the M2 Ultra/RTX 5090/DGX Spark class of hardware documented elsewhere in this corpus's local-model thread, though wombat23's need for community-sourced flag tuning (via an LLM, not the vendor's own docs) to avoid OOM suggests the low-VRAM path is not yet a documented, first-party-supported configuration.

### Claim 5: One practitioner (wombat23) found that serving Bonsai 2 27B through the `pi` coding-agent harness capped usable context at 64K tokens (against the model's nominal 262K) and caused the harness's `/thinking` level to be silently reset to off, degrading output quality
- **Evidence**: Direct first-person report of a specific `llama-server` + `pi` harness configuration and its observed limitation, posted as a follow-up ("UPDATE") in the same HN thread.
- **Confidence**: anecdotal (single practitioner, single harness, unresolved at time of posting — "haven't figure out a way to fix that")
- **Quote**: "UPDATE: I did more experiments - this time with llama-server and pi harness... the max context size i could serve is 64K on GPU only (the -ngl 99 setting). tested with pi harness and it is very fast. the /thinking level always gets reset to off though and it is not very smart like this. haven't figure out a way to fix that." (wombat23, news.ycombinator.com/item?id=49746618)
- **Our assessment**: This is a specific, novel harness-integration failure mode — not a model-quality problem per se, but a config/serving-layer bug where the coding-agent harness cannot keep the model's reasoning mode engaged, which the same commenter directly links to the model being "not very smart like this" in practice. This pairs directly with `blog-simonwillison-qwen38-27b-overthinking.md` (the base model's `xhigh` reasoning-effort default and its measured cost/quality tradeoffs): if a harness silently disables thinking mode for the quantized derivative of that same model lineage, teams evaluating Bonsai 2 27B for agentic coding should verify the harness is actually invoking reasoning mode before attributing any capability gap to the quantization itself.

### Claim 6: Prism ML's Hugging Face model card claims Bonsai 2 27B retains 98.2% of full-precision (FP16) Qwen3.8-27B's aggregate benchmark performance (84.78 vs. 86.32 average across 14 thinking-mode benchmarks) at ~1.72-1.75 effective bits per weight, roughly a 9.3x size reduction, using a ternary {-1,0,+1} weight representation with a blockwise Hadamard rotation applied before quantization
- **Evidence**: Prism ML's own first-party model card, with a full methodology write-up and a benchmark comparison table (FP16 vs. UD-Q4_K_XL vs. IQ2_XXS vs. Bonsai 2 27B) evaluated "with EvalScope + vLLM on NVIDIA H100 under identical infrastructure, decoding, and scoring."
- **Confidence**: emerging (a specific, detailed, first-party benchmark methodology and result table — a substantial upgrade in evidentiary detail over the predecessor Bonsai 27B's release, which this corpus's existing note flagged as having no accompanying quality benchmark at all — but vendor-published and not independently reproduced by this Miner or, per Claims 9-10 below, corroborated by several independent testers' real-world experience)
- **Quote**: "**98.2% of FP16 intelligence retained**: 84.78 average across 14 thinking-mode benchmarks — far above the conventional IQ2_XXS build (72.59) at about 82% of its footprint, and within 0.4 points of UD-Q4_K_XL at three times the footprint" (Hugging Face model card)
- **Quote (weight format)**: "Each weight takes a value from {−1, 0, +1}, with one shared FP16 scale factor for every group of 128 weights... The weights are stored in a **rotated basis**: each matrix is transformed blockwise by an orthogonal Hadamard rotation before the ternary assignment, and the runtime applies the matching transform to activations." (Hugging Face model card)
- **Our assessment**: This directly extends and partially resolves the open question flagged in `blog-latentspace-ainews-harness-drift-quantization.md` Claim 4, which noted the original Bonsai 27B's "preserving agentic workflows" framing was unaccompanied by any quality benchmark and should be read as marketing pending verification. Prism ML has since published one (here, for the successor model) — a meaningfully more evidence-backed claim than the July 2026 release. However, "far above IQ2_XXS" is a comparison against a conventional low-bit baseline the vendor itself characterizes as collapsing at sub-4-bit, not against a neutral or independently chosen baseline, and Claims 9-10 below document specific, named practitioner reports that the aggregate 98.2% figure does not match their hands-on experience — so this claim should be cited as "the vendor's own detailed, methodologically-described benchmark result," not as independently confirmed quality parity.

### Claim 7: The vendor's own per-category breakdown shows the retention gap is uneven — math (96.57 vs. 97.06 FP16) and coding (89.42 vs. 89.07 FP16, i.e. no measured loss) are preserved almost exactly, while knowledge & reasoning (79.86 vs. 85.55) and vision (66.19 vs. 71.36) show the largest drops
- **Evidence**: The model card's "By Skill Category" table, a first-party breakdown of the same 14-benchmark suite by skill area.
- **Confidence**: emerging (specific, itemized first-party benchmark numbers, not independently reproduced by this Miner)
- **Quote**: "The reasoning backbone comes through intact: math falls only from 97.06 to 96.57, coding is level with the baseline, and instruction following is slightly ahead of it. The remaining gap is concentrated in the most demanding categories — knowledge and reasoning, and vision." (Hugging Face model card)
- **Our assessment**: This is a more nuanced and more useful claim than the single aggregate "98.2%" headline: it tells a practitioner *where* to expect degradation (broad world-knowledge recall and vision) versus where not to (math, coding, instruction-following) — a genuinely actionable calibration if it holds up. It is worth flagging that this same model card elsewhere shows an IQ2_XXS baseline whose *aggregate* score (72.59) looks respectable but which "falls to 57.5 on AIME26 and 56.4 on LiveCodeBench" (a documented instance of aggregate scores masking selective collapse) — the vendor names this exact phenomenon as a reason casual testing misses degradation, which makes it directly relevant to weigh against the vendor's own aggregate claim for Bonsai 2 27B itself, since the same masking risk could in principle apply to categories the 14-benchmark suite does not cover (see Claim 10).

### Claim 8: Prism ML's separate launch blog post frames Bonsai 2 27B's key achievement as preserving capability specifically in agentic and long-horizon tasks, explicitly because "small errors can compound over many steps" in those workflows, and separately describes the compression level as making the release "practically 'lossless'"
- **Evidence**: Prism ML's own marketing/announcement blog post (a different first-party document from the Hugging Face model card, published the same day), read in full by this Miner.
- **Confidence**: anecdotal for the framing/marketing language (vendor's own promotional prose, not itself a benchmark methodology); emerging for the underlying retention percentage it restates (98.2%, consistent with the model card)
- **Quote**: "Coding agents, tool-use systems, multimodal workflows, and long-horizon tasks are particularly sensitive to model degradation because small errors can compound over many steps. Bonsai 2 27B preserves much of the full-precision model's performance in exactly these areas while operating at a fraction of the memory footprint." (prismml.com/news/bonsai-2-27b)
- **Quote ("practically lossless")**: "Compared to Ternary Bonsai 27B, the new Ternary Bonsai 2 27B has closed the retention gap between the full precision model from 95% to over 98%. This is a significant improvement that makes the current release practically \"lossless\"." (prismml.com/news/bonsai-2-27b)
- **Our assessment**: This is the specific claim that Claims 9-10 below directly contest with independent evidence. Notably, this vendor blog post's own benchmark table (83.9 overall for Bonsai 2 27B vs. 85.4 for Qwen3.8-27B) uses a *different* benchmark suite and reports different absolute numbers than the Hugging Face model card's table (84.78 vs. 86.32) — both claim "98.2%" retention, but from two non-identical first-party evaluations. This internal inconsistency across the vendor's own two publications (not a contradiction with an external source, so not filed as a corpus contradiction issue per MINER.md §4a) is worth the Assayer/Smith noting: a headline retention percentage that is stable across two different benchmark suites could reflect a robust result, or could reflect the number itself being the fixed target the marketing copy was built around — this Miner cannot distinguish the two from the published material alone.

### Claim 9: A named practitioner benchmarker's independent agentic-coding comparison against the full-precision base model reportedly showed the "near-lossless" claim "should be taken with a grain of salt," and a second commenter independently corroborated a gap between the model's benchmark scores and its real-world usefulness as a coding agent
- **Evidence**: A named HN commenter (verytrivial) relaying a third party's (Bijian Bowen's) agentic coding-challenge comparison, with a second, independent commenter (Aurornis) agreeing based on their own separate usage experience.
- **Confidence**: anecdotal (a relayed third-party comparison not directly linked or independently verified by this Miner, corroborated by one independent first-person account with no further detail given)
- **Quote**: "There's a chap called Bijian Bowen who does very quick agentic coding challenges for new models (very soon after release!) mainly for toy games or websites. He just did one for this model and included a comparison with the base model Qwen 3.8 which shows the \"near-lossless\" claim should be taken with a grain of salt. It is an interesting model if you are GPU starved and want local, but you might have trouble finding things it is good at." (verytrivial, news.ycombinator.com/item?id=49746618)
- **Quote (Aurornis, corroborating)**: "I agree. I don't know how they get such good results on these benchmarks because using them gives a very different experience. They're kind of cool for doing short free form outputs in memory constrained systems, but I don't think they're useful as coding agents." (Aurornis, same thread)
- **Our assessment**: This is the single highest-value finding in this source for the guide: two independent commenters, converging on the same specific gap — vendor benchmark scores vs. real coding-agent usefulness — with one citing a named third party's direct base-model comparison. Neither comment supplies reproducible numbers, so this should not be cited as a quantified refutation of Claim 6, but as a concrete signal that the benchmark suite's coverage (Claim 7's math/coding/instruction-following strength) may not transfer to sustained, multi-turn agentic coding work — exactly the workload category the vendor's own launch post (Claim 8) singles out as its key achievement.

### Claim 10: Additional independent commenters reported specific, concrete quality failures not visible in the vendor's benchmark suite: one found the ternary and even fp8 variants failed a memorization/recitation test that the bf16 version nearly passed; another found the model looped with clearly wrong reasoning that the non-quantized 27B did not exhibit; a third found it out-right failed on an actual agentic task; a fourth argued the vendor's benchmark selection avoids long-context and long-horizon multi-turn evaluation specifically
- **Evidence**: Four separate named HN commenters (raylad, redox99, v3ss0n, anana_) posting independent, specific failure reports and critiques in the same thread.
- **Confidence**: anecdotal (four independent but informal, unreplicated, non-benchmarked reports; none give a reproducible transcript in the comment itself)
- **Quote (raylad, recitation test)**: "For my \"Please recite Jabberwocky\" test the bf16 almost passes but the ternary and even fp8 versions fail badly."
- **Quote (redox99, looping)**: "I tried their WebGPU version and it immediately started looping. Yeah \"near lossless\" my ass. Plus the reasoning that it looped on was clearly wrong and unlike the non quantized 27B"
- **Quote (v3ss0n, agentic failure)**: "On actual agentic task , it just fail."
- **Quote (anana_, benchmark-selection critique)**: "The benchmarks they chose are rather cherry picked to not include long context or difficult ones that involve long horizon work or many agent turns, as I suspect this is where the model shows more differences compared to the full fat one"
- **Our assessment**: Taken together with Claim 9, this is a five-commenter convergence (verytrivial/Bijian Bowen, Aurornis, raylad, redox99, v3ss0n) plus one structural critique (anana_) on the same underlying pattern: the vendor's detailed, methodologically-described benchmark suite (Claim 6) does not appear to predict real-world quality on the workloads (agentic coding, sustained reasoning, exact recitation/memorization) that practitioners actually tried. anana_'s critique is the most actionable of the group because it names a specific, checkable gap in the benchmark suite itself (no long-context or many-turn agentic tasks in the published 14-benchmark table) rather than only reporting an anecdote. None of this rises to a controlled A/B study, and it should not be cited as proof the model is broadly unusable (wombat23's and rahimnathwani's successful deployments in Claim 4 show it does run and produce output), but it is strong enough, multi-source, and specific enough to warrant citing the vendor's "near-lossless"/"preserves...agentic...performance" framing (Claim 8) as contested, not settled, pending an independent agentic benchmark (e.g. SWE-bench-style or long-horizon multi-turn evaluation) that this source does not itself provide.

## Concrete Artifacts

### Willison's tested deployment recipe (verbatim, simonwillison.net, 2026-09-17)
```
cd /tmp

# Get the Prism macOS runtime
curl -fL https://github.com/PrismML-Eng/llama.cpp/releases/download/prism-b10685-7dffb15/llama-prism-b10685-7dffb15-bin-macos-arm64.tar.gz -o bonsai-runtime.tar.gz
tar -xzf bonsai-runtime.tar.gz

# Get the ~5.95 GB GGUF model:
curl -fL https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/resolve/main/Ternary-Bonsai-2-27B-PTQ1_0.gguf -o Ternary-Bonsai-2-27B-PTQ1_0.gguf

# Run the server, I used port 8331
./llama-prism-b10685-7dffb15/llama-server \
  -m Ternary-Bonsai-2-27B-PTQ1_0.gguf \
  --port 8331 -ngl 99 -fa on -c 32768
```
Query via the OpenAI-compatible endpoint (verbatim):
```
uvx llm openai endpoint http://127.0.0.1:8331/v1 \
  --model bonsai-2-27b --responses hi
```

### Prism ML's own quickstart command (Hugging Face model card, differs from Willison's — uses PQ2_0 pack and llama-cli, not llama-server)
```
hf download prism-ml/Ternary-Bonsai-2-27B-gguf Ternary-Bonsai-2-27B-PQ2_0.gguf --local-dir .

./bin/llama-cli -m Ternary-Bonsai-2-27B-PQ2_0.gguf \
    -ngl 99 -fa on -c 32768 \
    --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.05 \
    -p "Explain quantum computing in simple terms." -n 16384
```

### Vendor benchmark table (Hugging Face model card, "Benchmarks" section, EvalScope + vLLM on H100, thinking mode)
```
Variant                          True bpw   Footprint   Thinking avg   vs FP16
Qwen3.8-27B FP16                 16.0       54 GB       86.32          100%
Qwen3.8-27B UD-Q4_K_XL ("4-bit") 5.2        17.6 GB     85.18          98.7%
Qwen3.8-27B IQ2_XXS ("2-bit")    2.16       7.27 GB     72.59          84.1%
Bonsai 2 27B                     1.72       5.95 GB     84.78          98.2%

By skill category (FP16 -> Bonsai 2 27B):
  Knowledge & reasoning (MMLU-Redux, MuSR): 85.55 -> 79.86
  Math (GSM8K, MATH-500, AIME25, AIME26):    97.06 -> 96.57
  Coding (HumanEval+, MBPP+, LiveCodeBench): 89.07 -> 89.42
  Instruction following (IFEval, IFBench):   81.25 -> 82.66
  Agentic / tool calling (BFCL v3):          76.74 -> 74.92
  Vision (MMMU-Pro, OCR Bench v2):           71.36 -> 66.19
```

### Vendor's own launch post benchmark table (prismml.com/news/bonsai-2-27b — a different, non-identical suite from the HF model card above, both reporting "98.2%")
```
Capability                     Bonsai 2 27B   Qwen3.8 27B   Qwen3.6 27B
Agentic & Tool Calling          77.57          79.74         80.05
Coding                          81.58          82.17         82.57
Instruction Following           82.66          81.25         74.53
Knowledge & Reasoning           83.95          86.66         84.71
Math                            96.57          97.06         94.64
Vision                          78.59          81.64         79.82
Overall                         83.9           85.4          83.6
```

### Practitioner throughput reports (Hacker News item 49746618, named commenters)
```
Willison (M5 Pro, Metal):        ~20 tok/s (44 tok/s after restart, "not sure why")
rahimnathwani (M1 Pro):          14.22 tok/s (32,706 tokens, 38min 19s)
wombat23 (RTX 3070, 8GB VRAM):   Prompt 165.6 t/s | Generation 40.6 t/s (reduced batch size to avoid OOM)
zepearl (RTX 3060, 12GB VRAM):   Prompt 95.0 t/s | Generation 26.5 t/s

Vendor's own figures (HF model card cross-platform table, PQ2_0 pack):
  RTX 5090 (32GB):  TG128 129.9 tok/s
  M5 Max (Metal):   TG128 47.0 tok/s
  M5 Pro (Metal):   TG128 28.7 tok/s
```

### Root-cause explanation for Willison's Metal warning (francisjp, same HN thread)
```
"The 'tensor API is not supported' warning occurred because llama.cpp's
startup probe fails to compile a matmul2d kernel: Metal's tensor headers
require language version 4.0, but ggml-metal-device.m previously omitted
MTLCompileOptions.languageVersion, disabling the API universally."
Fix reportedly merged upstream; linked diff:
https://github.com/ggml-org/llama.cpp/pull/27461/changes
```

## Cross-References

### Cross-reference verification notes
`blog-latentspace-ainews-harness-drift-quantization.md`,
`blog-simonwillison-georgi-gerganov.md`, and
`blog-simonwillison-qwen38-27b-overthinking.md` were each re-read in full
during this extraction, and claim numbers cited below were confirmed by
position (top-to-bottom, document order) in each note before citing, per
MINER.md §4b.

- **Corroborates**:
  - `blog-simonwillison-georgi-gerganov.md` Claim 1 and
    `blog-simonwillison-qwen38-27b-overthinking.md` Claim 8 (Qwen-family
    27B-class models are viable local coding-agent models on prosumer
    hardware): Claim 4 here extends this pattern down to a lower hardware
    floor — three independent testers running the ternary derivative
    successfully on an M1 Pro and on NVIDIA cards with as little as 8GB
    VRAM, well below the M2 Ultra/RTX 5090/DGX Spark-class hardware those
    notes document.
  - `blog-latentspace-ainews-harness-drift-quantization.md` Claim 4's own
    caution ("no quality benchmark accompanies this claim... should be read
    as vendor marketing framing, not measured evidence, pending a future
    Miner locating PrismML's own eval numbers"): Claims 9-10 here are
    exactly that follow-up, and they confirm the predecessor note's
    skepticism was warranted — even with a published, detailed benchmark
    suite now available (Claim 6), independent practitioners report the
    "near-lossless"/agentic-preservation claim does not hold up in
    real-world agentic use.

- **Contradicts**: No formal contradiction issue filed. The clearest tension
  in this source is internal to the source bundle itself, not against an
  existing corpus note: Prism ML's own launch post (Claim 8) explicitly
  claims agentic and long-horizon task performance is specifically
  preserved ("particularly sensitive to model degradation... Bonsai 2 27B
  preserves much of the full-precision model's performance in exactly these
  areas"), while five independent, named commenters in the same Hacker News
  thread the source lives in (Claims 9-10: verytrivial/Bijian Bowen,
  Aurornis, raylad, redox99, v3ss0n) report the opposite on agentic coding,
  sustained reasoning, and exact recitation tasks specifically. Per
  MINER.md §4a, this was not filed as a cross-corpus contradiction because
  no existing source note stakes out the opposing position being contested
  here (the closest existing note, `blog-latentspace-ainews-harness-drift-quantization.md`,
  already treats the predecessor model's agentic-preservation claim as
  unverified marketing, so there is no established corpus claim to file
  *against* — this source is direct evidence *for* that existing caution,
  not a new conflict). The Assayer/Smith should nonetheless treat the
  vendor-claim-vs-practitioner-reports gap documented in Claims 8-10 as the
  single most guide-relevant tension in this note.

- **Extends**:
  - `blog-latentspace-ainews-harness-drift-quantization.md` Claim 4 (the
    original Bonsai 27B: 5.9GB/1.71 effective bits, based on Qwen 3.6 27B,
    no accompanying quality benchmark): this source covers the *successor*
    release (Bonsai 2 27B, based on the newer Qwen3.8-27B, 5.95GB/1.72-1.75
    effective bits), with, for the first time in this corpus's Bonsai
    coverage, a detailed vendor benchmark methodology (Claims 6-7) and
    independent deployment/quality evidence (Claims 1-5, 9-10) that the
    predecessor note lacked entirely.
  - `blog-simonwillison-qwen38-27b-overthinking.md` (Qwen 3.8 27B's `xhigh`
    reasoning-effort default causes measured over-thinking, and disabling
    reasoning trades quality for speed in a task-dependent way): Claim 5
    here (a coding-agent harness silently resetting `/thinking` to off when
    serving the *quantized derivative* of the same base model) is a
    directly relevant, unresolved practical complication for any team
    trying to reproduce that note's reasoning-effort guidance against
    Bonsai 2 27B specifically, since the harness-level thinking-mode bug
    could confound any quality comparison between the quantized and
    full-precision models.
  - `blog-simonwillison-georgi-gerganov.md` (Qwen3.6-27B viable for daily
    coding-agent maintainer work at full precision): this source's
    throughput and deployment data (Claims 2, 4) provide a second-generation,
    quantized data point on the same Qwen-27B model lineage's local
    deployability, at a much smaller (5.95GB vs. ~54GB) footprint but with
    contested quality parity (Claims 9-10) that Gerganov's full-precision
    account does not need to address.

- **Novel**:
  - **A tested, reproducible deployment recipe for a shipped sub-2-bit
    ternary model, with a documented non-standard-runtime hazard** (Claim 1):
    no existing corpus note gives step-by-step, verified commands for
    running a Bonsai-family model, or documents that the wrong runtime
    silently produces garbage rather than erroring.
  - **A specific root-cause explanation and merged upstream fix for a
    startup-time inference bug, contributed by a named third party directly
    in response to the source author's post** (Claim 3): a new pattern for
    this corpus — a technical mystery raised in one comment resolved by
    name in a later comment in the same thread.
  - **A detailed, first-party 14-benchmark quality methodology for a
    Bonsai-family model** (Claims 6-7): the predecessor Bonsai 27B note has
    no benchmark data at all; this is the corpus's first per-category
    breakdown of where sub-2-bit quantization degrades a specific model
    (knowledge/reasoning and vision) versus where it does not (math,
    coding, instruction-following).
  - **Direct, multi-commenter practitioner contestation of a vendor's
    "near-lossless"/agentic-preservation marketing claim, on the same
    workload category (agentic coding) the vendor's own materials single
    out** (Claims 8-10): this specific vendor-claim-vs-practitioner-reports
    pattern, with this level of convergence (five independent commenters)
    and this much first-party benchmark detail to contrast against, is new
    to the corpus's quantization coverage.
  - **A documented harness-level bug where a coding-agent harness silently
    disables a served model's reasoning/thinking mode** (Claim 5): novel
    failure mode, not previously documented in this corpus's harness or
    local-model material.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 1 (Bonsai-family GGUF
  files require Prism's non-standard llama.cpp fork, and the standard
  runtime silently produces garbage for one of the two pack formats rather
  than erroring) as a concrete example of a vendor-specific-runtime
  deployment hazard practitioners should check for before adopting any
  novel low-bit quantization format — "does this need a fork, and does the
  wrong binary fail loudly" is a specific due-diligence question this
  source makes actionable. Add Claim 5 (a coding-agent harness silently
  resetting `/thinking` to off when serving this model) as a specific
  verification step: teams should confirm a harness is actually invoking a
  served local model's reasoning mode before attributing any capability gap
  to the model or its quantization.
- **Chapter 04 (Model Selection & Cost) — local/quantized model viability**:
  Cite Claim 4 (successful reproduction on an 8GB-VRAM RTX 3070 and a 12GB
  RTX 3060, alongside Apple Silicon) as evidence that sub-2-bit quantization
  is lowering the local-deployment hardware floor for 27B-class models
  meaningfully below what `blog-simonwillison-georgi-gerganov.md` and
  `blog-simonwillison-qwen38-27b-overthinking.md` document for full/near-full
  precision. Pair this immediately with Claims 6-10: the vendor's detailed
  98.2%-retention benchmark claim (Claims 6-7) should be presented alongside
  the independent practitioner reports contesting it on agentic-coding and
  sustained-reasoning tasks specifically (Claims 9-10) — the guide should
  not cite "9x smaller, 98.2% capability retained" as a settled, transferable
  fact for coding-agent use cases without this caveat, since that is
  precisely the workload category multiple independent testers report the
  claim not holding up for.
- **Chapter 03 (Verification)**: anana_'s specific critique (Claim 10) — that
  the vendor's published benchmark suite excludes long-context and
  many-turn agentic evaluation, which is exactly where independent testers
  report the largest gaps — is a reusable due-diligence heuristic for
  evaluating *any* vendor-published model benchmark suite, not just this
  one: check what task categories and context lengths a benchmark suite
  does *not* cover before trusting an aggregate retention/quality claim.

## Extraction Notes

- **Fetch method**: Willison's own post was fetched via direct `curl` (raw
  HTML, no preload JSON needed — simonwillison.net serves static
  server-rendered HTML for this page type) rather than relying on WebFetch's
  AI-summarized pass, which paraphrased rather than preserved the source
  text verbatim. All `Quote` fields attributed to simonwillison.net were
  copied character-for-character from that raw HTML (tags stripped, no
  wording changed), including the source's own typo ("try out out").
- **Linked pages followed** (3, within MINER.md's up-to-5 budget): (1) the
  Hacker News discussion thread the post's "My comment" link points into,
  fetched via direct `curl` and parsed comment-by-comment from the raw HTML
  (`<div class="commtext">` blocks), preserving HTML entities decoded to
  their literal characters (`&#x27;` to apostrophe, `&quot;` to `"`, `&gt;`
  to `>`) with no other wording changes; roughly the first 20 of 200
  comments were read in full document order, plus a keyword sweep (terms
  including "benchmark", "quality", "hallucin", "marketing", "agentic",
  "lossless") across the remaining 180 to surface substantive threads not
  in the first 20 — this surfaced the Claims 9-10 material. (2) The Hugging
  Face model card README, fetched directly via its `raw/main/README.md`
  URL (plain Markdown, no HTML parsing needed) — the single most reliable
  source of verbatim vendor text in this note. (3) Prism ML's own launch
  blog post (the original HN submission target), fetched via `curl` and
  HTML-stripped to plain text. The linked whitepaper PDF, the
  `PrismML-Eng/Bonsai-demo` repository's run scripts, and the merged GitHub
  PR referenced by francisjp (Claim 3) were not independently fetched or
  verified by this Miner.
- **Comment coverage caveat**: with 200 comments in the HN thread, this
  Miner's coverage is deep-but-partial (documented above) rather than
  exhaustive. The keyword sweep specifically targeted quality-skepticism and
  benchmark-critique language per this issue's Prospector-flagged "tested
  vs. theoretical" key question; a different keyword set (e.g. focused on
  license terms, comparisons to other vendors' quantization methods, or
  further hardware reports) would likely surface additional material a
  future Miner could add if this source is revisited.
- **No contradiction issue filed** — see Cross-References → Contradicts
  above for the reasoning: the tension identified (vendor agentic-capability
  claim vs. practitioner reports) is evidence *for* an existing note's
  already-stated caution, not a new conflict against an established corpus
  position, so it does not meet MINER.md §4a's filing bar. It is instead
  surfaced prominently in Claims 8-10 and the Guide Impact section for the
  Smith's attention.
- **Confidence rated `emerging` overall**: the source bundle mixes a
  `settled`-quality first-person tested deployment recipe (Claim 1) with a
  first-party benchmark methodology of real but vendor-published,
  unreplicated evidentiary weight (Claims 6-8), multiple independent but
  informal practitioner corroborations (Claim 4) and contestations (Claims
  9-10) of varying specificity, and one unresolved anecdotal harness bug
  (Claim 5). No single controlled study exists in this source; the
  aggregate signal is stronger and more specific than a single anecdotal
  report (multiple independent named commenters converging on the same
  quality-gap pattern) but well short of settled, replicated fact.
