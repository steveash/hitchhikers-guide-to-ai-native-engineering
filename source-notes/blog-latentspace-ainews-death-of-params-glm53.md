---
source_url: https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie
source_type: blog-post
title: "[AINews] Death of Params: Z.ai CEO Jie Tang on GLM 5.3 and the new Post-training Scaling Law"
author: Latent Space / AINews (automated/editorial daily digest; no individual byline; aggregates an X thread from Z.ai's Jie Tang plus tweets/Reddit for 8/18/2026-8/19/2026)
date_published: 2026-08-20
date_extracted: 2026-09-05
last_checked: 2026-09-05
status: current
confidence_overall: emerging
issue: "#3255"
---

# [AINews] Death of Params: Z.ai CEO Jie Tang on GLM 5.3 and the new Post-training Scaling Law

> Z.ai co-founder/CEO Jie Tang argues on X that raw parameter count is no
> longer a meaningful standalone metric for model capability, and that
> GLM-5.3's improvements over GLM-5.2 came entirely from about one month of
> additional RL on long-horizon, synthetically-generated production-workflow
> environments — not from any change to the base architecture or parameter
> count — reframing "scaling" around training-recipe and environment quality
> rather than model size.

## Source Context

- **Type**: blog-post (Latent Space's "AINews" — a daily, largely
  automated/editorial digest that opens with a hand-written editorial section
  on one headline topic, here Jie Tang's X thread, followed by an "AI Twitter
  Recap" of unrelated same-day stories, then a paywalled "AI Reddit Recap").
  Published 2026-08-20 per the page byline ("Aug 20, 2026"), covering "AI News
  for 8/18/2026-8/19/2026."
- **Author credibility**: No individual AINews byline. Per the credibility
  caveat already established in this corpus for the same publication
  (`blog-latentspace-glm52-open-frontier-parity.md`,
  `blog-latentspace-fable-5-mythos-launch.md`), AINews-relayed claims should be
  treated as attributed third-party statements curated by the outlet, not as
  Latent Space's own independent testing or analysis. The headline claims in
  this note, however, are primary-source: they are Jie Tang's own words from
  his X thread, quoted directly by AINews, rather than AINews's own
  assessment. Jie Tang is Z.ai's co-founder and CEO and a Tsinghua professor;
  he is speaking about his own company's model and training methodology, so
  his claims carry direct authority about *what Z.ai did* but should be read
  as a vendor's own framing of its results, not independently verified
  research.
- **Scope**: Covers Jie Tang's four-dimension reframing of "scaling" (data,
  compute allocation, deployment conditions, plus parameter count), the
  specific RL-environment methodology behind GLM-5.3's gains, a "5 knobs of
  scaling" claim (knobs themselves not enumerated in the accessible text
  beyond MoE sparsity notation), a corroborating second mention of the same
  GLM-5.3-via-one-month-RL claim from a different AINews subsection, and one
  open-weight-model benchmark placement for GLM-5.3 (ValsAI). Also touches,
  in the unrelated "AI Twitter Recap," an Ornith-1.5 release and a
  GLM-5.2-cost-routing data point from TrueForge, extracted here only because
  they extend existing GLM/Ornith source notes. Does NOT cover: the "AI
  Reddit Recap" beyond its first Qwen/DeepSeek quantization subsection
  (paywalled after that point — see Extraction Notes), an enumerated list of
  all "5 knobs of scaling," or any independently reproduced benchmark for
  GLM-5.3 beyond the single ValsAI placement.

## Extracted Claims

### Claim 1: Jie Tang argues parameter count alone is not a meaningful capability metric — it must be read alongside data volume, compute allocation, and deployment conditions
- **Evidence**: Direct quote from Jie Tang's own X post (embedded/quoted by AINews), presented as the article's central thesis and its "death of params" framing.
- **Confidence**: emerging (a specific, on-the-record claim from the CEO of the lab in question, but a framing argument rather than a measured result)
- **Quote**: "Parameter count is only meaningful alongside three others — how much data you have, where you intend to spend your compute, and who will run the model, under what conditions."
- **Our assessment**: This is a vendor CEO's rhetorical framing as much as a technical claim, and it conveniently follows GLM-5.3 not being a parameter-count jump over GLM-5.2 (Claim 5) — Tang has an incentive to reframe the scaling conversation away from a dimension where his model didn't move. That said, the underlying point (a single scalar undersells a model's shape) is not new to careful practitioners and is consistent with `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 8's Jamin Ball critique that raw parameter comparisons ignore token efficiency and serving footprint — a different lab commentator arriving at "parameter count alone is misleading" from the deployment-cost angle rather than the capability angle.

### Claim 2: AINews argues Chinchilla-style scaling laws no longer hold in an "Inference Inflection" world, where tokens-per-parameter ratios vary widely (200-900) by task, per Roberts et al.
- **Evidence**: AINews's own editorial framing, citing a named external source ("Roberts et al") for the task-dependent range.
- **Confidence**: anecdotal (an aggregator's own claim, backed by a citation this Miner did not independently retrieve or verify — "Roberts et al" is named but not linked or further identified in the accessible text)
- **Quote**: "We have covered Chinchilla (and post-Chinchilla) scaling laws in past LS years, but, so we will skip the history lesson, but it is good to level-set on why Chinchilla's assumptions were wrong in the Inference Inflection world (no fixed number, between 200-900 toks/param, citing Roberts et al on task dependence)."
- **Our assessment**: This is AINews's own editorial claim, not Tang's — it's presented as scene-setting context for why Tang's argument matters, not as something Tang himself said. The "200-900 toks/param" range is a specific, checkable number, but without a link or full citation for "Roberts et al" this should be treated as a claim to verify before citing in the guide, not as settled.

### Claim 3: AINews frames the training implication as "memorization prefers more parameters; reasoning prefers more post-training data and effective depth"
- **Evidence**: AINews's own summary sentence, presented as the takeaway from Tang's argument, immediately preceding the GLM-5.3 RL-environment description.
- **Confidence**: emerging (a clean, quotable heuristic, but AINews's paraphrase of Tang's position rather than Tang's own words)
- **Quote**: "In short: Memorization prefers more parameters. Reasoning prefers more post-training data and effective depth."
- **Our assessment**: This is a useful, citable heuristic for model-selection discussions (a memorization-heavy task like broad factual QA may still favor a larger base model; a reasoning-heavy agentic task may benefit more from a smaller model with better post-training), but it is AINews's compressed framing of Tang's argument, not a measured result with a benchmark attached. Treat as a hypothesis worth testing against task-specific benchmarks, not a settled rule.

### Claim 4: GLM-5.3's capability gains came solely from RL training on long-horizon environments simulating multi-day, real-world engineering/research work with access to compute clusters, documentation, and codebases
- **Evidence**: Quoted description (via AINews) of the RL environment design, including a concrete example task (an ML-infrastructure optimization task requiring bottleneck diagnosis, implementing optimizations, running experiments, and delivering a measured speedup).
- **Confidence**: emerging (specific, concrete methodology description from the vendor, not independently verified by benchmark reproduction)
- **Quote**: "The environments now cover a much broader range of production workflows, with tasks designed around how engineering and research work is actually carried out in practice. Some represent several days of work for an experienced engineer. In an ML infrastructure task, for example, the model may be given the same working environment as an engineer, with access to compute clusters, storage systems, internal documentation, codebases, and experiment results. It must diagnose bottlenecks across the training stack, implement optimizations, run experiments, and deliver a measurable end-to-end speedup while preserving correctness. Training on environments at this level pushes the model toward taking ownership of substantial work end to end, rather than relying on users to decompose the problem and supervise each step."
- **Our assessment**: This is the most concrete methodological claim in the source: training environments modeling multi-day, end-to-end engineering ownership (not single-turn tasks) as the source of capability gains. It is directly relevant to how practitioners think about what "agentic capability" improvements actually measure — a model trained this way should be expected to handle longer-horizon, less-decomposed tasks better, which is a testable prediction for anyone evaluating GLM-5.3 on real engineering work rather than short benchmarks.

### Claim 5: GLM-5.3 is reportedly based on the same core base model/architecture as GLM-5.2, with its gains coming from about one month of additional RL — corroborated independently in two places in the same article
- **Evidence**: Stated twice in the article: once implicitly in the framing around Tang's own thread, and explicitly later in the "Post-Training, Mid-Training, and RL Systems Work" section, attributed to a separate account (`@kimmonismus`) surfacing "a notable claim from the zAI/GLM founder."
- **Confidence**: emerging (vendor-attributed claim, restated by an independent aggregator subsection within the same digest, but neither instance is an independently reproduced architecture diff)
- **Quote**: "@kimmonismus surfaced a notable claim from the zAI/GLM founder: progress is still scaling, but too much discourse has fixated on parameter count rather than data quality, inference compute, and post-training. The cited example is GLM-5.3, reportedly based on the same core base model/architecture as GLM-5.2, but improved substantially via about one month of extra RL."
- **Our assessment**: This is the single most concrete, checkable claim in the source: no architecture or parameter-count change, ~1 month of extra RL, "substantial" improvement. It directly corroborates `blog-latentspace-glm52-open-frontier-parity.md` Claim 5 (GLM-5.2 at 753B total/~40B active parameters, MIT, 28.5T-token pretraining) as still describing GLM-5.3's base — this is a training-recipe-only revision, not a scale jump, consistent with the 5.1→5.2 pattern that note already documented. Practitioners tracking the GLM series should not expect a new parameter/architecture spec sheet for 5.3; the delta is training data/environment quality only.

### Claim 6: Jie Tang identifies "5 knobs of scaling" beyond parameter count, including MoE sparsity expressed in a new "XA-YB" notation, and argues advanced skills like vulnerability-finding require carrying 20+-step causal chains that don't live in total parameter count past a knowledge threshold
- **Evidence**: AINews's paraphrase of Tang's argument; the "5 knobs" are referenced but not enumerated beyond MoE sparsity in the accessible text.
- **Confidence**: anecdotal (AINews's summary of a claim; the specific 5 knobs are not listed, so the claim cannot be fully checked from this source alone)
- **Quote**: "To put an end to parameter count obsesssion, Prof Jie identifies 5 knobs of scaling, including MoE sparsity with the new XA-YB notation. He notes that advanced skills (e.g., finding software vulnerabilities) are not retrieval/memorization problems. They require carrying long causal chains (20+ inference steps) without losing the thread. This ability does not live in total parameter count once a certain knowledge-holding threshold is reached."
- **Our assessment**: The "20+ inference steps without losing the thread" framing for advanced/reasoning skills is a specific, useful operational definition of "effective depth" (tying back to Claim 3), but this Miner could not locate the full "5 knobs" list or the "XA-YB" notation definition in the accessible article text or the embedded tweet excerpt — this claim is thinner than it first appears and should be flagged for follow-up if a fuller Tang thread or Z.ai technical report becomes available.

### Claim 7: Prof Jie Tang has separately predicted an open-weights "Fable-class" model by end of 2026; AINews's own spot-check finds two 2-3T-parameter open models (Qwen 3.8 Max, Kimi K3) already exist, with Fable itself estimated at 3-7T parameters and only ~2 points ahead on the AA index, with 134 days left in the year
- **Evidence**: AINews's own editorial "spot check" against a Tang prediction referenced from prior coverage, comparing current open-weight parameter scale to their own estimate of Fable's parameter count and an unspecified "AA index" gap.
- **Confidence**: anecdotal (AINews's own real-time estimate/spot-check, not a benchmark run; "3-7T" for Fable and "2 points higher on the AA index" are both stated without methodology in the accessible text)
- **Quote**: "We've covered GLM 5.2 very excitedly before, and Prof Jie Tang's belief that there will be an open weights Fable-class model by end of the year (spot check - with 134 days left, there are now two 2-3T models (Qwen 3.8 Max and Kimi K3) with estimates that Fable is 3-7T, and only 2 points higher on the AA index.)"
- **Our assessment**: This corroborates and extends `blog-latentspace-ainews-qwen38-max-27b-launch.md` (which documents Qwen 3.8 Max at 2.4T total parameters) and the corpus's existing Kimi K3 tracking — both are independently confirmed to be in the 2-3T-parameter range Tang's prediction requires as precedent. The "AA index" gap figure (2 points) is not the same figure as `blog-latentspace-fable-5-mythos-launch.md` Claim 4's ~5-point Intelligence Index gap at Fable 5's June 2026 launch — the gap AINews cites here is narrower and from August 2026, suggesting (if both figures use the same Artificial Analysis Intelligence Index methodology, which this Miner could not confirm from either source) that open models closed roughly 3 points of gap over about two months. This should be treated as a directional signal, not a verified trend line, since neither source specifies whether "AA index" and "Intelligence Index" refer to the identical benchmark version.

### Claim 8: ValsAI ranked GLM-5.3 #2 on Terminal Bench, #3 on Legal Bench, and #6 on Skills Bench among open-weight models
- **Evidence**: AINews's Twitter recap, attributed to named account `@ValsAI`.
- **Confidence**: anecdotal (single third-party benchmark aggregator's ranking, not independently reproduced by this Miner, and the absolute scores are not given — only ordinal rank "among open weights")
- **Quote**: "For open models, @ValsAI also highlighted GLM 5.3 as #2 on Terminal Bench, #3 on Legal Bench, and #6 on Skills Bench among open weights."
- **Our assessment**: This is the only independent (non-Z.ai) benchmark data point for GLM-5.3 in this source. Placing #2-#6 across three different benchmark categories among open-weight models is consistent with Claim 5's framing of GLM-5.3 as a solid, broad-based incremental improvement rather than a category-leading jump — useful as a first external data point for anyone evaluating GLM-5.3 specifically, but thin (no absolute scores, no comparison to GLM-5.2's placement on the same boards).

### Claim 9: A 14-task enterprise benchmark reportedly found TrueForge (an MIT-licensed, self-hostable agent harness) matched Claude Managed Agents running Opus 4.8 while using ~30% fewer tokens, and that routing the same harness to GLM-5.2 cut cost by ~75% while preserving accuracy
- **Evidence**: AINews's Twitter recap, attributed to named accounts `@truefoundry`, `@omarsar0`, and `@kimmonismus` covering TrueForge's launch.
- **Confidence**: anecdotal (vendor-adjacent benchmark, launch-announcement context, not independently reproduced; benchmark task composition not described beyond "14-task enterprise benchmark")
- **Quote**: "The technical claim that resonated: on a 14-task enterprise benchmark, TrueForge matched Claude Managed Agents on Opus 4.8 while using about 30% fewer tokens, and routing to GLM-5.2 cut cost by around 75% while preserving accuracy."
- **Our assessment**: This is a harness-level (not model-level) claim, but it directly corroborates `blog-latentspace-glm52-open-frontier-parity.md` Claim 4's finding that GLM-5.2 occupies a "good enough, much cheaper" tier relative to frontier proprietary models — a second, independent source now reports a ~75% cost cut from routing to GLM-5.2 "while preserving accuracy," on top of the earlier AA-Briefcase per-task cost comparison. Neither source's benchmark has been independently reproduced by this Miner, but two different third parties reporting large GLM-5.2 cost savings without a corresponding accuracy hit is a mild corroboration signal worth flagging together.

### Claim 10: Ornith-1.5 was released in 9B dense, 35B MoE, and 397B MoE variants under MIT with FP8/GGUF/MLX/NVFP4 quantized formats, claiming end-to-end self-improvement (the model proposes tasks, generates scaffolds, and produces RL rollouts to create new training experiences)
- **Evidence**: AINews's Twitter recap, attributed to named account `@ornith_`, with specific reported benchmark scores.
- **Confidence**: anecdotal (vendor's own launch announcement and self-reported benchmark scores, not independently reproduced)
- **Quote**: "@ornith_ released Ornith-1.5 in 9B dense, 35B MoE, and 397B MoE variants under MIT, with quantized formats including FP8, GGUF, MLX, and NVFP4. The headline claim is end-to-end self-improvement: the model proposes tasks, generates scaffolds, and produces RL rollouts to create new training experiences. Reported evals are strong across agentic/coding workloads, including Terminal-Bench 2.1: 86.1, SWE-Bench Verified: 86, DeepSWE: 56, HLE: 44.6, and Tool Decathlon: 71.2."
- **Our assessment**: This directly extends `blog-simonwillison-ornith.md`, which documented Ornith-1.0's self-scaffolding RL training pattern (models generating their own task-specific RL scaffolds). Ornith-1.5 appears to keep the same self-improvement thesis while adding a 397B MoE variant not present in the 1.0 lineup per that note, and MIT-licenses the whole family. This is tangential to this source's GLM/scaling focus but is a relevant, checkable update to an already-tracked model family, so it is preserved here rather than discarded.

## Concrete Artifacts

### Jie Tang's X thread framing (quoted by AINews, embedded tweet preview text)

```
jietang @jietang
Thoughts About Scaling Law

Scaling, but not only of parameters. Every model release now ends with the
same question: how many parameters? It isn't a question that can be answered
on its own. Parameter count is only meaningful alongside three others — how
much data you have,
[tweet preview truncated by embed — full text quoted in article body, see
Claim 1]

5:04 AM · Aug 19, 2026 · 1.02M Views · 170 Replies · 661 Reposts · 4.83K Likes

Source: Latent Space AINews, latent.space/p/ainews-death-of-params-zai-ceo-jie,
Aug 20, 2026
```

### GLM-5.3 RL-environment synthesis pipeline description

```
As agent capability improves, much of the difficulty in scaling post-training
moves from the model to the environment. A useful task environment has to be
executable, verifiable, and close to real professional work — and we need
many of them, not a handful of hand-built ones. To scale this process, we
built pipelines that synthesize environments end to end, and for a subset of
tasks, the RL reward signal as well. Research agents collect task patterns
from real work and turn them into runnable long-horizon environments with
multi-step dependencies and hidden state; a judge agent then attempts each
task to verify that it is actually solvable. Verifiers are synthesized
without access to the reference solution, while solver trajectories are used
to discover and close reward shortcuts. A verifier that passes oracle,
no-op, and unsolved-state checks produces a binary reward reliable enough to
train on directly.

Source: Latent Space AINews, Aug 20, 2026, quoting Z.ai/Jie Tang.
```

### GLM-5.3 open-weight benchmark placement (ValsAI, via AINews)

```
Benchmark          Rank among open weights
------------------------------------------
Terminal Bench      #2
Legal Bench         #3
Skills Bench        #6

Source: Latent Space AINews, Aug 20, 2026, attributed to @ValsAI.
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-glm52-open-frontier-parity.md` Claim 5 (GLM-5.2 at
    753B total/~40B active parameters, MIT license, 28.5T-token pretraining):
    Claim 5 here confirms GLM-5.3 retains the same base
    model/architecture — this is a training-recipe-only revision extending
    the same "no scale jump between point revisions" pattern that note
    already established for 5.1→5.2.
  - `blog-latentspace-glm52-open-frontier-parity.md` Claim 4 (GLM-5.2 as the
    cheapest frontier-tier model on AA-Briefcase at $2.40/task): Claim 9
    here (TrueForge routing to GLM-5.2 cutting cost ~75% "while preserving
    accuracy") is a second, independent source reporting large GLM-5.2 cost
    savings without an accuracy penalty.
  - `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 1 (Qwen 3.8 Max
    at 2.4T parameters) and Claim 8 (Jamin Ball's critique that raw
    parameter comparisons overstate/understate real cost and capability):
    Claim 7 here independently reuses the same Qwen 3.8 Max parameter figure
    as precedent for Tang's "2-3T is now normal for open models" spot-check,
    and Claim 1 here (Tang's "parameter count alone is misleading" argument)
    arrives at a similar conclusion to Ball's critique from a different
    angle (capability framing vs. deployment-cost framing).
  - `blog-simonwillison-ornith.md` (Ornith-1.0's self-scaffolding RL training
    pattern): Claim 10 here documents the 1.5 release of the same model
    family, retaining the self-improvement thesis and adding a 397B MoE
    variant.

- **Contradicts**: None filed. Jie Tang's "parameter count alone is
  misleading" argument (Claim 1) is not in tension with any existing source
  note — it is a different axis of critique (capability framing) than
  Jamin Ball's parameter-count critique in
  `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 8 (deployment/
  serving-cost framing); both converge on "don't compare models by parameter
  count alone" without disagreeing about anything else. This does not meet
  the MINER.md §4a bar for a filed contradiction — no existing note asserts
  that parameter count alone *is* sufficient for capability comparison.

- **Extends**:
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 4 (Fable 5 #1 on
    Artificial Analysis's Intelligence Index at 64.9, ~5 points ahead of
    GPT-5.5, as of its June 2026 launch): Claim 7 here provides a later
    (August 2026), narrower gap figure ("2 points higher on the AA index")
    for open models generally closing on Fable-class models, though this
    Miner could not confirm both figures use the identical benchmark
    version — flagged as a directional extension, not a confirmed trend.
  - `blog-latentspace-ainews-kimi-k3-wiki-memory.md` and the corpus's
    existing Kimi K3 parameter tracking: Claim 7 reuses Kimi K3 as a
    2-3T-class open model alongside Qwen 3.8 Max, giving a second named
    reference point for the "how close are open models to Fable-class
    scale" question this corpus already tracks piecemeal across several
    notes.

- **Novel**:
  - **The RL-environment synthesis pipeline for GLM-5.3** (Claim 4, Concrete
    Artifacts): research agents extracting task patterns from real work,
    judge agents verifying solvability without reference solutions, and
    reward-shortcut discovery via solver trajectories — this specific
    training-environment-generation methodology is not documented elsewhere
    in this corpus for any model.
  - **The "memorization prefers parameters, reasoning prefers post-training
    data and effective depth" heuristic** (Claim 3): a new, quotable framing
    not present elsewhere in the corpus for reasoning about when parameter
    count matters vs. when post-training investment matters more.
  - **"Effective depth" / 20+-step causal chains as an operational
    definition of advanced reasoning skill** (Claim 6): new terminology to
    the corpus.
  - **ValsAI as a named benchmark aggregator for GLM-5.3** (Claim 8): first
    appearance of ValsAI in this corpus.
  - **Ornith-1.5** (Claim 10) and **TrueForge** (Claim 9): neither is
    documented elsewhere in the corpus under these specific version/product
    names.

## Guide Impact

- **Chapter 02 (Model Selection & Procurement)**: Claim 5 (GLM-5.3 is a
  training-recipe-only revision of GLM-5.2's exact base architecture,
  achieved via ~1 month of extra RL) is directly citable evidence that
  point-release version bumps in fast-moving open-weight model families do
  not necessarily mean new parameter counts or hardware requirements —
  practitioners re-evaluating a model family after a version bump should
  check whether the base architecture changed before assuming new deployment
  math is needed. Pair with the existing GLM-5.1→5.2 continuity finding in
  `blog-latentspace-glm52-open-frontier-parity.md`.
- **Chapter 02 or Chapter 04 (evaluation/selection criteria)**: Claim 3's
  "memorization prefers parameters, reasoning prefers post-training data and
  effective depth" heuristic is a citable (if vendor-sourced) rule of thumb
  for framing model-selection discussions around task type rather than
  parameter count alone — recommend adding as an attributed claim (Z.ai's
  own framing, not independently verified) rather than settled guidance.
- **Chapter 03/05 (Training & Scaling approaches)** if the guide covers
  post-training methodology: Claim 4's RL-environment synthesis pipeline
  (research agents → judge agents → reward-shortcut-resistant verifiers) is
  a concrete, novel-to-corpus example of how a frontier lab claims to scale
  RL training environments themselves, which is a different scaling
  bottleneck than the parameter/compute scaling the guide likely already
  discusses. Worth adding as a named example of "environment scaling" as a
  training lever distinct from "parameter scaling" or "compute scaling."

## Extraction Notes

- **Fetch method**: WebFetch's summarizing pass was too thin to support
  verbatim quote extraction (it paraphrased rather than quoted), so the raw
  article HTML was fetched directly via `curl`, tag-stripped, and
  HTML-entity-decoded to plain text. All `Quote` fields in this note were
  copied character-for-character (including em dashes and curly
  quotes/apostrophes) from that parsed text, re-joining text fragments that
  the source's inline-hyperlink markup had split across lines, without
  altering wording, punctuation, or word order.
- **Paywall**: Per the same pattern documented in
  `blog-latentspace-glm52-open-frontier-parity.md`, the "AI Reddit Recap"
  section is paywalled after its first subsection ("1. Qwen/DeepSeek
  Open-Weight Inference Speedups" — "Keep reading with a 7-day free trial").
  That one accessible Reddit subsection (Unsloth's Qwen3.8-27B Dynamic v3
  GGUFs) is about quantization tooling for a different model family and was
  read but not extracted as a claim here — it is tangential to this issue's
  GLM-5.3/scaling-law focus and largely duplicates ground already covered by
  `blog-latentspace-ainews-qwen38-max-27b-launch.md` and
  `blog-simonwillison-qwen38-27b-overthinking.md`.
- **Out-of-scope sections not extracted as claims**: Consistent with the
  Prospector's triage focus (Ch02-05, GLM-5.3/post-training scaling law),
  several "AI Twitter Recap" items were read in full but not extracted as
  standalone claims because they are unrelated to GLM/scaling and each is a
  one-paragraph vendor/tooling mention without benchmark depth tying it to
  this issue's topic: DeepSeek Harness (Cordis plugin architecture),
  Qdrant's filterable HNSW vs. ACORN, Sentence Transformers v6.0 multi-vector
  retrieval, a production-agent-latency instrumentation paper, Agent
  Lightning v1.0 (RL-through-harness), CPT/mid-training knob framing, Linear/
  turbopuffer's vector-infra migration, and the Google/OpenAI/Anthropic
  productization items (Gemini 3.7 Flash, Private Safety Processing, Claude
  Code's Concise output style). A future Miner could mine the harness-focused
  items (DeepSeek Harness, Agent Lightning) separately if RL-through-harness
  tooling becomes a priority topic — they were noted but deliberately left
  unextracted here to keep this note focused on the issue's flagged topic.
- **"5 knobs of scaling" incompletely documented**: As noted in Claim 6, the
  accessible article text references "5 knobs" but only names one (MoE
  sparsity, "XA-YB" notation) without defining that notation or listing the
  other four. This Miner did not find the notation defined elsewhere on the
  page (including the embedded tweet preview, which is truncated by the
  platform's own embed widget). If a fuller version of Tang's thread or a
  Z.ai technical report is filed as a future source, it should explicitly
  cross-reference this note's Claim 6 as the incomplete precedent.
