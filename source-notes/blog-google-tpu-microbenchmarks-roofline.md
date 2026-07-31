---
source_url: https://developers.googleblog.com/how-to-use-google-microbenchmarks-for-evaluating-tpu-performance/
source_type: blog-post
title: "How to use Google microbenchmarks for evaluating TPU performance"
author: "Junjie Qian, Chi Shuen Lee, Yu-Hsuan (Amy) Lin, Haixiong (Sean) Wang (Google)"
date_published: 2026-07-30
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: emerging
issue: "#2359"
---

# How to use Google microbenchmarks for evaluating TPU performance

> A short, first-party Google Developers Blog how-to introducing an
> open-source TPU microbenchmark suite (Network, Compute, HBM, Host
> Transfer, Ragged-Paged Attention) and the Roofline model it feeds, plus a
> one-paragraph case study claiming a 21.2% training-step-time reduction on
> a 110B MoE workload — a low-level ML-serving/training performance
> methodology report with no direct connection to this guide's actual scope
> (AI-assisted software engineering practice, not ML systems/kernel
> engineering).

## Source Context

- **Type**: blog-post (Google Developers Blog, tagged AI / Cloud /
  Tutorials / How-To Guides / Learn / Explore; published July 30, 2026).
  Discovered via the trusted `google-developers` RSS feed. This is a short
  post (~1,000 words of body text) — thinner than the corpus's other three
  Google/TPU source notes, which are dense engineering-report-length pieces.
- **Author credibility**: Four named Google authors (Junjie Qian, Chi Shuen
  Lee, Yu-Hsuan (Amy) Lin, Haixiong (Sean) Wang), consistent with this
  corpus's other first-party Google technical posts that name individual
  contributors rather than only "Google for Developers" (compare
  `blog-google-ray-tpu-serve-data-train.md`, two named authors). No named
  Acknowledgements section of the scale seen in
  `blog-google-qwen35-ironwood-moe-optimization.md` (35+ contributors) —
  this reads as an introductory/explainer post rather than a
  postmortem-style engineering deep-dive.
- **Scope**: Covers the five benchmark categories in Google's open-source
  `accelerator-microbenchmarks` suite (Network, Compute, HBM, Host
  Transfer, Ragged-Paged Attention/RPAv3), the suite's GitHub directory
  structure (`src/`, `configs/`), a sample `kubectl` invocation, the
  Roofline model's three-way bottleneck categorization (compute-bound,
  memory-bound, network-bound), one hardware-architecture insight (TPU7x's
  256x256 systolic array and `head_dim` alignment), three named software
  optimization levers (kernel selection, sharding/mesh tuning,
  rematerialization), a "predictive optimization" pitch, and a one-paragraph
  case study on a 110B MoE training workload. Does **not** cover: the
  benchmark suite's actual measured numbers for any specific TPU generation
  (no GB/s, TFLOPS, or latency figures are given for the benchmarks
  themselves — only for the case study), a step-by-step tuning walkthrough,
  cost/pricing, comparison against non-TPU hardware, or any claim about
  AI-assisted software engineering workflows.

## Extracted Claims

### Claim 1: The microbenchmark suite standardizes performance evaluation across five core areas — Network, Compute, HBM, Host Transfer, and Ragged-Paged Attention (RPAv3) — each with named test primitives and metrics
- **Evidence**: Direct enumeration in the "Key categories and metrics"
  section, with named collective operations, named metrics, and units for
  each category.
- **Confidence**: settled (a factual description of the open-source
  benchmark suite's structure, independently checkable against the linked
  GitHub repository)
- **Quote**: "Network: Characterizes interconnect performance for collective communication operations essential for scaling models across multiple chips through inter-chip interconnect (ICI). Key tests include all-gather, all-reduce, reduce-scatter, and all-to-all. Metrics include throughput (GB/s), and latency (seconds)."
- **Our assessment**: This is a useful taxonomy for anyone evaluating
  accelerator performance in general, independent of TPU specifics: split
  the measurement surface into network/compute/memory-bandwidth/host-I-O/
  attention-primitive categories rather than a single aggregate benchmark
  number. The categories map cleanly onto the Roofline model's inputs
  (Claim 4), which is the post's actual organizing thesis.

### Claim 2: The microbenchmark suite is open-source, structured into a `src/` directory (benchmark implementations) and a `configs/` directory (tuning parameters — buffer sizes, iteration counts, supported dtypes) with runnable YAML-based tests invoked via `kubectl`
- **Evidence**: Direct description of the GitHub repository structure, paired
  with a verbatim shell code example.
- **Confidence**: settled (a specific, independently checkable claim about a
  public GitHub repository's directory layout and invocation method)
- **Quote**: "src/: Contains the fundamental implementations and source code for the microbenchmarks configs/: Manages the tuning parameters for each test, such as data buffer sizes, number of iterations, and supported data types (e.g., bf16, fp8, fp32)"
- **Our assessment**: Concrete and checkable — the repo
  (`AI-Hypercomputer/accelerator-microbenchmarks` on GitHub, linked twice in
  the post, once at a `tpu7x-auto/Ironwood` branch) is a real artifact a
  reader could clone and run today, not just a described methodology. The
  `kubectl apply -f Ironwood/guides/collectives/tpu7x-2x2x1-ici-all-gather-microbenchmark.yaml`
  invocation (Concrete Artifacts) confirms the suite runs as Kubernetes
  jobs, not a standalone CLI.

### Claim 3: Microbenchmarks establish a "Speed-of-Light" (SOL) baseline — the theoretical hardware limit — which converts performance optimization from trial-and-error into an empirical engineering discipline
- **Evidence**: Direct framing statement in the "Performance tuning impact"
  section.
- **Confidence**: emerging (a methodological claim about SOL-baselining as
  a practice; the value of the practice is asserted rather than measured
  against a trial-and-error baseline in this post, though the case study in
  Claim 8 does apply the SOL framing to a specific workload)
- **Quote**: "Microbenchmarks take performance optimization from a trial-and-error process into an empirical engineering discipline. By establishing a "Speed-of-Light" (SOL) baseline (the theoretical limit of the hardware modules), they provide a clear target for training and inference efficiency."
- **Our assessment**: The general pattern — measure the theoretical ceiling
  first, then express observed performance as a percentage of that ceiling
  — is the same "roofline-percentage" framing already documented in
  `blog-google-qwen35-ironwood-moe-optimization.md` Claim 8 (82.4%/79.6% of
  a discounted roofline limit), just named differently ("SOL" here vs.
  "discounted roofline limit" there). See Cross-References.

### Claim 4: The Roofline model categorizes a workload's bottleneck into exactly three types — compute-bound, memory-bound, or network-bound — each pointing to a distinct, non-overlapping remediation strategy
- **Evidence**: Direct three-way enumeration in "The Roofline model: A
  diagnostic North Star" section, each with its own remediation
  implication.
- **Confidence**: settled (a standard, well-established performance-analysis
  framework — the Roofline model predates this post — described accurately
  and specifically for the TPU/ICI/DCN context)
- **Quote**: "Compute-bound: The model is hitting the MXU plateau. Tuning memory access will yield no benefit; optimizations must focus on kernel efficiency or reducing FLOPs. Memory-bound: The model is limited by the sloped "eaves" of the roofline. Performance can be improved by optimizing data locality (VMEM) or reducing HBM traffic. Network-bound: Stalls in ICI or DCN prevent the chips from reaching their compute potential. This identifies the need for better sharding strategies or communication-overlap techniques."
- **Our assessment**: The value here is the explicit statement that
  "tuning memory access will yield no benefit" once compute-bound — a
  falsifiable, actionable claim that tells a practitioner which class of
  optimization to *not* waste time on, rather than a generic "profile your
  workload" suggestion. This is a genuinely transferable diagnostic
  heuristic independent of TPU specifics.

### Claim 5: On Ironwood (TPU7x), the MXU's 256x256 systolic array imposes a physical constraint on operand shapes such that models using a `head_dim` of 128 (common in older Llama variants) achieve less optimal MXU utilization, which is driving researchers to co-design frontier models with dimensions aligned to 256-byte boundaries
- **Evidence**: Direct hardware-architecture claim in "Hardware-aware model
  architecture" section, naming a specific dimension value (128) and a
  specific model family (Llama) as the negative example.
- **Confidence**: emerging (a specific, named hardware/model-shape
  interaction claim — plausible and consistent with known systolic-array
  tiling behavior — but no benchmark numbers, MFU percentages, or specific
  Llama-variant measurements are given to quantify "less optimal," and the
  claim that this is "driving" model co-design is a forward-looking/causal
  assertion about the field, not a demonstrated instance)
- **Quote**: "For example, on the Ironwood (TPU7x) architecture, the 256x256 systolic array imposes a physical constraint on operand shapes. Benchmarking confirms that models using a head_dim of 128 (common in older Llama variants) achieve less optimal MXU utilization. This insight drives researchers to co-design frontier models with dimensions aligned to 256-byte boundaries to maximize hardware efficiency."
- **Our assessment**: This is the post's most specific, quotable technical
  detail — a concrete "gotcha" (head_dim=128 is suboptimal on this specific
  MXU shape) rather than generic advice. It complements
  `blog-google-qwen35-ironwood-moe-optimization.md` Claim 7 (KV-cache block
  size of 16 causing VPU indexing stalls on TPU, fixed by coarsening to 256)
  as a second, independent instance of the same underlying pattern: TPU
  hardware has specific power-of-256-adjacent alignment preferences that
  differ from GPU/CPU intuition, and smaller/legacy dimension choices can
  silently cost utilization. No quantified utilization delta is given here,
  unlike the Qwen note's precise 428µs→283µs figure, so this claim is
  weaker evidence on its own.

### Claim 6: Once a bottleneck is diagnosed, microbenchmarks point to one of three named software levers — kernel selection (JAX vs. Pallas vs. Tokamax Splash Attention), sharding/mesh topology tuning (e.g., comparing 2x2x2 vs. 4x2x1 for FSDP), or rematerialization (trading compute cycles for memory pressure to avoid HBM overflow)
- **Evidence**: Direct three-item enumeration in "Software levers and
  optimization strategies" section.
- **Confidence**: emerging (named, specific levers with named comparison
  points, but no before/after numbers are given for any of the three — the
  post asserts that microbenchmarks "provide the ground truth" for kernel
  selection without showing an example result)
- **Quote**: "Kernel selection: You can compare standard JAX operations against specialized Pallas kernels or Tokamax Splash Attention. Microbenchmarks provide the ground truth for which implementation minimizes the backward pass overhead. Sharding and mesh tuning: By measuring collective performance across different topologies (e.g., 2x2x2 vs 4x2x1), you can optimize Fully Sharded Data Parallel (FSDP) parameters to ensure that communication time is fully hidden behind computing, i.e., tasks complete fast enough so that the TPU does not need to stop and wait for a response. Rematerialization: Microbenchmarks help calculate the exact trade-off between compute cycles and memory pressure, guiding decisions on when to store calculated data in memory vs. “rematerialize” (recalculate) it, to avoid HBM overflows."
- **Our assessment**: The specific pairing of "compute-bound → don't touch
  memory access" (Claim 4) with "network-bound → tune topology/overlap
  communication with compute" gives a practitioner a decision tree, not
  just a list of levers. The rematerialization framing (a compute-vs-memory
  trade-off calculated *from* benchmark data, not guessed) is a specific,
  checkable engineering practice, though it is asserted rather than
  demonstrated with a worked example in this post.

### Claim 7: Microbenchmark data enables predictive modeling — building analytical models that forecast training throughput, TTFT, Time-Per-Output-Token (TPOT), and MFU for large-scale deployments, without needing to run expensive tests on full TPU slices
- **Evidence**: Direct claim in the "Predictive optimization" section.
- **Confidence**: anecdotal (an asserted capability with no worked example,
  no accuracy figures for the predictive models, and no description of the
  modeling methodology itself — the entire section is two sentences)
- **Quote**: "Finally, microbenchmark data allows for predictive modeling of large-scale deployments. Instead of running expensive tests on full TPU slices, you can use results to build analytical models that accurately predict training-throughput, TTFT, Time-Per-Output-Token (TPOT), and MFU before they scale up."
- **Our assessment**: This is the thinnest claim in the post — a genuinely
  useful idea (small-scale microbenchmarks as inputs to a cost model for
  full-slice-scale predictions, avoiding expensive full-scale dry runs) but
  stated as a two-sentence assertion with zero supporting detail on how the
  analytical model is built or how accurate its predictions have proven.
  Flagged as anecdotal rather than emerging because there is no example
  instance in this post at all, unlike Claims 3-6 which at least name a
  mechanism.

### Claim 8: In a case study, a 110B-parameter Mixture-of-Experts training workload on a 4x4x4 TPU7x configuration showed forward-pass/dense-core operations compute-bound at 1.85 PFLOPS, while MoE routing and attention primitives were memory-bound at only 30-60% of SOL due to HBM saturation during expert dispatch
- **Evidence**: Direct case-study measurement in "Case study: Ironwood
  (TPU 7x) performance analysis" section, naming the model size, hardware
  topology, and a specific compute figure plus a percentage range for the
  memory-bound component.
- **Confidence**: anecdotal (a single, self-reported case study with no
  independent reproduction; the workload is described only as "a 110B
  Mixture-of-Experts (MoE) training workload," not a named, publicly
  identifiable model, unlike `blog-google-qwen35-ironwood-moe-optimization.md`'s
  named Qwen 3.5-397B case study)
- **Quote**: "In one example, we analyzed the performance tuning of a 110B Mixture-of-Experts (MoE) training workload deployed on a 4x4x4 TPU 7x configuration, leveraging microbenchmarks to establish hardware baselines and drive optimization for complex, sparse workloads. Here is what we found: Roofline analysis: Diagnostic profiling of the training workload revealed a clear division in performance bottlenecks. The forward-pass and dense-core operations were primarily compute-bound, reaching 1.85 PFLOPS. Conversely, the routing and attention primitives in the MoE architecture remained memory-bound, operating at 30–60% of the SOL due to HBM saturation, where sparse activation patterns become heavily IO-bound during expert dispatch, sending incoming requests to sub-networks."
- **Our assessment**: This is a real-world instance of the Claim 4 Roofline
  categorization applied to a mixed workload where *different parts of the
  same model* land in different bottleneck categories (dense layers
  compute-bound, MoE routing/attention memory-bound) — a more nuanced
  picture than treating a whole model as uniformly compute- or
  memory-bound. The 30-60% SOL range for the memory-bound component is a
  wide band, suggesting either high variance across MoE layers/experts or
  imprecise reporting; no per-layer breakdown is given.

### Claim 9: Microbenchmark-guided interventions — SparseCore collective offloading (addressing communication stalls found via ICI benchmarks) and adoption of Tokamax Splash Attention (addressing HBM-bound attention primitives) — reduced the case-study workload's training step time by 21.2%
- **Evidence**: Direct before/after outcome statement immediately following
  Claim 8's diagnostic breakdown, naming the two specific interventions and
  linking each to the specific benchmark category that identified it.
- **Confidence**: anecdotal (a single self-reported percentage improvement
  for an unnamed, non-independently-verifiable workload; no baseline step
  time or absolute step-time figures are given, only the relative 21.2%
  delta)
- **Quote**: "Correlation with microbenchmarks: Microbenchmark results directly guided interventions that reduced the training step time by 21.2%. ICI collective benchmarks identified communication stalls resolved by SparseCore collective offloading, while HBM bandwidth tests identified memory-bound Attention primitives, prompting the adoption of Tokamax Splash Attention."
- **Our assessment**: This is the post's clearest end-to-end example of the
  full workflow it's arguing for: benchmark → diagnose bottleneck category
  → apply the category-specific lever → measure improvement. It is
  consistent with `blog-google-qwen35-ironwood-moe-optimization.md`'s
  Claim 5 (that team replaced tensor parallelism with a hybrid 8-way
  Attention Batch Sharding / DP=8 plus 8-way Expert Parallelism / EP=8
  scheme for MoE feed-forward layers) and with that note's general finding
  that MoE serving/training on TPU is bottlenecked by routing/collective
  overhead rather than raw compute: both sources reach for a
  collective-communication remedy, though by different means (sharding
  redesign there, SparseCore offloading here) — see Cross-References. The
  "fourth-generation SparseCores"/irregular-memory-access framing below
  comes from the externally linked Ironwood training-guide page, not from
  that note. Followed the
  post's own linked resource (`cloud.google.com/blog/products/compute/
  training-large-models-on-ironwood-tpus`, one of the "learn more" links)
  for the underlying mechanism: it describes SparseCore collective
  offloading as using "specific XLA flags" to offload All-Gather and
  Reduce-Scatter operations to Ironwood's fourth-generation SparseCores so
  TensorCores stay dedicated to primary computation while communication
  runs in parallel — a more mechanistic explanation than this post itself
  gives, though that detail comes from the linked page, not from the
  mined article's own text.

## Concrete Artifacts

### Sample microbenchmark invocation (verbatim from the post)

```shell
# Run a compute microbenchmark with a sample configuration

kubectl apply -f Ironwood/guides/collectives/tpu7x-2x2x1-ici-all-gather-microbenchmark.yaml
```

Source: developers.googleblog.com/how-to-use-google-microbenchmarks-for-evaluating-tpu-performance/,
code block following the "Microbenchmark suite" section.

### Benchmark suite repository structure (verbatim from the post)

```
"src/: Contains the fundamental implementations and source code for the
microbenchmarks
configs/: Manages the tuning parameters for each test, such as data
buffer sizes, number of iterations, and supported data types (e.g., bf16,
fp8, fp32)"
```

Source: developers.googleblog.com/how-to-use-google-microbenchmarks-for-evaluating-tpu-performance/,
"Microbenchmark suite" section. Linked repository:
`github.com/AI-Hypercomputer/accelerator-microbenchmarks` (main branch and
a `tpu7x-auto/Ironwood` branch are both linked from different points in
the post).

### "Learn more" resource list (verbatim from the post)

```
"Ironwood: The first Google TPU for the age of inference
Optimizing frontier model training on TPU v7x (Ironwood)
AI accelerator performance and benchmarking
A developer’s guide to training with Ironwood TPUs"
```

Source: developers.googleblog.com/how-to-use-google-microbenchmarks-for-evaluating-tpu-performance/,
closing "To learn more, check out the following resources" list. None of
these four linked pages were fetched independently in this extraction
except the fourth (`cloud.google.com/blog/products/compute/training-large-models-on-ironwood-tpus`,
also linked inline as the "SparseCore collective offloading" citation for
Claim 9) — see Extraction Notes.

## Cross-References

- **Corroborates**: `blog-google-qwen35-ironwood-moe-optimization.md`
  Claim 8 (measured throughput reported as a percentage of a first-party
  roofline ceiling — this post's "SOL baseline" framing in Claim 3 and the
  30-60%-of-SOL figure in Claim 8 is the same methodology under a
  different name) and that note's Claim 5/general finding that MoE serving
  on Ironwood requires specific handling of routing/collective overhead
  (this post's Claim 9 names SparseCore collective offloading as the fix
  for ICI-bound MoE communication stalls, consistent with that note's
  DP+EP sharding redesign motivated by the same class of MoE-specific
  bottleneck). Also corroborates that note's Claim 7 (KV-cache block-size
  tuning: 16→256 fixes VPU indexing stalls) with an independent second
  instance of the same "TPU hardware rewards larger, 256-aligned
  dimensions over smaller legacy ones" pattern, this time for attention
  `head_dim` (Claim 5) rather than KV-cache page size.
- **Contradicts**: None identified. No existing source note takes a
  position on the Roofline model, TPU microbenchmarking methodology, or
  head_dim/systolic-array alignment that this post's claims oppose.
- **Extends**: This is the corpus's fifth Google/TPU source note (after
  `blog-google-tunix-gemma-reasoning-hackathon.md`,
  `blog-google-tunix-agentic-rl-throughput.md`,
  `blog-google-qwen35-ironwood-moe-optimization.md`, and
  `blog-google-ray-tpu-serve-data-train.md`). It extends
  `blog-google-qwen35-ironwood-moe-optimization.md` specifically by giving
  the general-purpose diagnostic *methodology* (the open-source
  microbenchmark suite plus the Roofline model) that a reader would use to
  arrive at the kind of case-specific findings that note documents (that
  note's Qwen case study measures throughput against a self-derived
  roofline but does not name or link the underlying benchmark tooling used
  to establish it; this post supplies that missing piece — the actual
  open-source suite and its five benchmark categories).
- **Novel**: This is the corpus's first source documenting: (1) the
  open-source `accelerator-microbenchmarks` GitHub suite and its five
  benchmark categories (Network, Compute, HBM, Host Transfer,
  Ragged-Paged Attention/RPAv3) by name; (2) the "Speed-of-Light" (SOL)
  baseline terminology; (3) the explicit three-way Roofline
  bottleneck-to-remediation mapping (compute-bound → kernel/FLOPs,
  memory-bound → VMEM/HBM traffic, network-bound → sharding/overlap); (4)
  the specific head_dim=128-vs-256-systolic-array MXU utilization claim;
  (5) the "predictive optimization" pitch (using small-scale
  microbenchmarks to forecast full-slice-scale throughput/TTFT/TPOT/MFU
  without running full-scale tests).

## Guide Impact

Following the same assessment reached independently by all four prior
Google/TPU source notes in this corpus
(`blog-google-tunix-gemma-reasoning-hackathon.md`,
`blog-google-tunix-agentic-rl-throughput.md`,
`blog-google-qwen35-ironwood-moe-optimization.md`,
`blog-google-ray-tpu-serve-data-train.md`): this article is ML
training/serving performance-measurement methodology — how to benchmark
and diagnose bottlenecks in TPU hardware — not guidance about how a
practitioner builds, configures, or operates an AI coding agent/harness.
The guide's actual chapters (confirmed by reading `guide/*.md` headers
directly: 00-principles, 01-daily-workflows, 02-harness-engineering,
03-verification, 04-context-engineering, 05-team-adoption,
06-security-threat-model) address working *with* deployed AI coding
agents in a software-engineering context — none covers accelerator
benchmarking, ML training infrastructure performance tuning, or hardware
roofline analysis.

- **No direct chapter impact recommended.** None of Claims 1-9 describes
  a harness-configuration practice, a verification technique for
  AI-generated code, a context-management pattern, a team-adoption
  process, or a security consideration for coding-agent usage. The
  Prospector's two triage comments proposed Ch02 (harness engineering /
  infrastructure fundamentals) and Ch04 (context engineering / scaling
  patterns) relevance, but on reading the full article its subject is
  entirely accelerator-hardware performance measurement for training and
  serving generic ML workloads — a different audience (ML systems/infra
  engineers tuning TPU deployments) and a different layer of the stack
  (the compute substrate an AI product runs on, not the harness a
  developer uses to write code with AI assistance) — the same
  discrepancy already flagged in each of the four prior TPU notes' Guide
  Impact sections for their own respective triage comments.
- **Weak, indirect analogy only, flagged rather than forced**: Claim 4's
  Roofline model — categorize a bottleneck first, then apply only the
  remediation that matches that category, rather than guessing — is
  structurally the same discipline this guide's Ch03 (Verification)
  content advocates for diagnosing AI-generated code failures
  (root-cause before patching), but the specific technical content (MXU
  plateaus, ICI/DCN network stalls, VMEM locality) has no transferable
  detail for a coding-harness context. If the guide ever adds content on
  the economics/performance characteristics of self-hosting or
  fine-tuning models for agentic-coding workloads, this post (together
  with the four other TPU notes) would be background reading for that
  new scope, not a citation for any existing section.

## Extraction Notes

- **Verified the source is real and live before extraction.** Fetched the
  raw article HTML directly via `curl` (HTTP 200, ~46KB response) and
  confirmed the JSON-LD `Article` schema block's headline, author list
  (Junjie Qian, Chi Shuen Lee, Yu-Hsuan (Amy) Lin, Haixiong (Sean) Wang),
  and July 30, 2026 `datePublished` are internally consistent with the
  page's visible title and byline before extracting any quotes. Located
  the article body inside `inner-block-content rich-content` /
  `inner-block-content code-block` divs (this page is much shorter than
  the corpus's other Google Developers Blog posts — the body text totals
  roughly 1,000 words across the entire post) and stripped markup with a
  Python script to obtain full, character-for-character article text
  before extracting quotes. All `Quote` fields above were verified as
  literal substrings of that stripped text.
- **Followed one of the four "learn more" links.** Fetched
  `cloud.google.com/blog/products/compute/training-large-models-on-ironwood-tpus`
  (linked twice from the mined post — once inline as the citation for
  "SparseCore collective offloading" in the case study, once again in the
  closing resource list) because it directly substantiates the mechanism
  behind Claim 9's named intervention. That page's own SparseCore
  description is quoted, clearly attributed as coming from the linked
  page rather than the mined post, only inside Claim 9's "Our assessment"
  — it is not presented as a `Quote` field of this note, since this
  note's source is the microbenchmark post, not the linked Ironwood
  training guide. The other three "learn more" links (a `blog.google`
  Ironwood-launch announcement, a `discuss.google.dev` forum thread, and a
  `docs.cloud.google.com` benchmarking-concepts doc) were not fetched —
  they are general background/launch material the post itself does not
  depend on for any of the claims extracted here.
- **This is a thin source relative to this corpus's other TPU posts.**
  The post itself is roughly a fifth the length of
  `blog-google-qwen35-ironwood-moe-optimization.md` and contains no
  benchmark-suite measurement numbers of its own (GB/s, TFLOPS, or latency
  figures for the five categories) — only the one-paragraph case study
  supplies any numeric result. Nine claims were extracted, at the low end
  of MINER.md's 5-15 target range; a tenth or eleventh claim was not
  manufactured from padding, since the post's remaining content (the
  conclusion paragraph and resource list) restates points already covered
  in Claims 1-9 rather than introducing new substantive material.
- **Existing overlap checked before writing.** Searched all
  `source-notes/*.md` for "roofline", "MFU", "systolic", "rematerializ",
  "Ironwood", "MXU", "Speed-of-Light", and "microbenchmark" before
  drafting. Found the same three prior Google/TPU notes referenced
  throughout (Qwen/Ironwood, Ray-on-TPU, and by extension the two Tunix
  notes checked via the "Ironwood"/TPU family search) and one unrelated
  false-positive match (`blog-cursor-agent-autonomy-auto-review.md` uses
  "rematerializing" in an eval-relabeling sense, unrelated to TPU memory
  management) — confirmed net-new coverage of the microbenchmark suite,
  SOL/Roofline terminology, and the head_dim/systolic-array claim,
  addressed in Cross-References.
- **Confidence rationale**: Set to `emerging` overall. The benchmark-suite
  structure and Roofline three-way categorization (Claims 1, 2, 4) are
  concrete, independently checkable facts (rated `settled` individually).
  The SOL-baselining framing (Claim 3) and the head_dim/systolic-array
  and software-lever claims (Claims 5, 6) are named, specific mechanism
  claims not independently benchmarked in this extraction (rated
  `emerging` individually). The predictive-optimization pitch (Claim 7)
  and both case-study figures (Claims 8, 9) are self-reported,
  unquantified-baseline, single-instance vendor claims for an unnamed
  workload (rated `anecdotal`/`anecdotal` individually) — weaker evidence
  than the Qwen note's named-model case study. The overall `emerging`
  rating reflects that mix: the methodology/taxonomy claims are solid,
  the specific numeric outcomes are vendor-reported and unverified.
- **Off-topic relative to this guide's scope, flagged explicitly rather
  than force-fit.** Per MINER.md's instruction to be specific about guide
  impact rather than vaguely gesture at relevance, this note states
  plainly in Guide Impact that the source has no direct chapter mapping,
  consistent with all four prior Google/TPU notes' independent conclusions
  reaching the same result.
