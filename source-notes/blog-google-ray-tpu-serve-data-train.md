---
source_url: https://developers.googleblog.com/run-ray-on-tpu-part-2-ray-ai-libraries/
source_type: blog-post
title: "Run Ray on TPU, Part 2: Ray AI libraries"
author: "Ivan Nardini (AI Developer Relations, Google), Spencer Peterson (Software Engineer, Google)"
date_published: 2026-07-24
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: emerging
issue: "#2223"
---

# Run Ray on TPU, Part 2: Ray AI libraries

> A first-party Google Developers Blog how-to covering how Ray Serve, Ray
> Data, and Ray Train (via `JaxTrainer`) run on Google Cloud TPU slices —
> the single `accelerator_config.topology` field that determines correct
> multi-host gang-scheduling versus a silent-hang failure mode in Ray
> Serve, the `iter_jax_batches()` API for device-sharded data loading, and
> the "import jax inside the worker function" requirement for `JaxTrainer`.
> This is ML-infrastructure/deployment documentation for scaling AI
> workloads on TPU hardware, not guidance about AI-assisted software
> engineering practice.

## Source Context

- **Type**: blog-post (Google Developers Blog, tagged "AI / Case Studies /
  How-To Guides"; published July 24, 2026). Part 2 of a two-part series;
  Part 1 ("Run Ray on TPU, Part 1: The foundations," published July 20,
  2026, same authors) covers the GKE/Ray Core foundation this article
  builds on and is referenced throughout but is a separate URL not covered
  by this note (not currently in the source-note corpus).
- **Author credibility**: Two named Google authors — Ivan Nardini (AI
  Developer Relations) and Spencer Peterson (Software Engineer) — writing
  on the official Google Developers Blog about Ray, a widely-used
  open-source distributed-computing framework (not a Google-proprietary
  tool), running on Google's own TPU hardware via GKE. First-party vendor
  documentation/tutorial content; no independent third-party review or
  benchmark is cited. Similar authorship pattern (named individual
  contributors, not just "Google for Developers") to
  `blog-google-tunix-gemma-reasoning-hackathon.md`.
- **Scope**: Covers three Ray AI libraries on TPU — Ray Serve (multi-host
  LLM serving via vLLM with topology-based gang-scheduling), Ray Data
  (device-sharded batch loading via `iter_jax_batches()`), and Ray Train
  (`JaxTrainer` for distributed training with checkpointing and
  fault-tolerant restarts) — plus two "extras": official
  `rayproject/ray:*-tpu` Docker images and Ray Dashboard TPU metrics. Does
  **not** cover: benchmark numbers, throughput/latency measurements, cost
  comparisons, or any claim about coding-agent workflows. The article is a
  narrative how-to/announcement with three code snippets (YAML config, a
  Ray Data loop, a JaxTrainer script), not a full API reference — it
  repeatedly points to a separate "get-started" GitHub sample
  (`kubernetes-engine-samples`) for runnable code, which was not
  independently fetched or verified in this extraction (see Extraction
  Notes).

## Extracted Claims

### Claim 1: A multi-host TPU model must land on one complete "slice" (a fixed group of host VMs connected via the ICI interconnect) or its workers cannot reach each other and the job hangs
- **Evidence**: Stated as the recap of Part 1's foundational premise,
  which every library-specific claim in this article depends on.
- **Confidence**: settled (a hardware/networking constraint restated
  consistently across both parts of the series, not a claim requiring
  independent verification)
- **Quote**: "TPU chips are wired into fixed groups called slices (host VMs sharing a high-speed link called the ICI), and a multi-host model has to land on one whole slice or its workers can't reach each other and the job hangs."
- **Our assessment**: This is the load-bearing constraint the entire
  article is organized around — every library-specific pattern described
  below (Serve's `topology` field, `JaxTrainer`'s `ScalingConfig`) exists
  specifically to satisfy this one requirement. It is a straightforward,
  checkable hardware-networking fact (TPU slices share an ICI mesh;
  cross-slice communication does not exist), not a debatable design
  choice.

### Claim 2: All three Ray AI libraries (Serve, Data, Train) follow the same underlying pattern on TPU — declare a topology and let Ray Core reserve the slice — differing only in what the topology is declared on
- **Evidence**: Stated as the article's organizing principle before
  walking through each library.
- **Confidence**: settled (an architectural description of how the three
  libraries relate to the shared Ray Core placement primitive from Part 1)
- **Quote**: "With Core handling placement underneath, the libraries all follow the same pattern: declare a topology, let Core reserve the slice. What changes per library is only what you declare it on."
- **Our assessment**: This is the article's thesis sentence and useful as
  a compression of the whole post: once a reader understands that Ray Core
  (Part 1) owns slice reservation, the three subsequent library sections
  are each just "where does the `topology` field go" rather than three
  unrelated mechanisms to learn separately.

### Claim 3: Ray Serve's TPU backend uses the `accelerator_config.topology` field to defer placement to the replica at startup, which is what keeps a tensor-parallel model's workers on one shared ICI mesh
- **Evidence**: Direct mechanism description of how the `topology` field
  changes Serve's scheduling behavior, immediately following the YAML
  config example (`accelerator_type: TPU-V6E` / `accelerator_config: kind:
  tpu, topology: "4x4"`).
- **Confidence**: emerging (first-party description of internal Serve
  scheduling behavior; not independently verified against the Ray Serve
  source code in this extraction)
- **Quote**: "With topology set, Serve's TPU backend skips its usual upfront placement group and defers to the replica, which creates a slice placement group at startup. That deferral is what keeps a tensor-parallel model's workers on one shared ICI mesh."
- **Our assessment**: This names the specific mechanism (deferred,
  replica-created slice placement group vs. an upfront per-chip placement
  group) rather than just asserting "set this field and it works" — a
  practitioner debugging a multi-host Serve deployment has something
  concrete to check for (whether the deferred placement group path is
  actually being taken) rather than only a config-value checklist.

### Claim 4: Omitting the `topology` field on a multi-host TPU model causes Ray Serve to fall back to per-chip bundles that can scatter across two slices, and because there is no ICI between slices, workers never complete their first collective operation
- **Evidence**: Direct description of the failure mode as the
  counterexample to Claim 3, in the same paragraph.
- **Confidence**: emerging (first-party description of a specific failure
  mode, presented with enough mechanistic detail — bundles scattering
  across slice boundaries, collective operations never completing — to be
  independently plausible given Claim 1's ICI constraint, but not
  independently reproduced in this extraction)
- **Quote**: "Leave it off and Serve falls back to per-chip bundles; on a multi-host model those bundles can scatter across two slices, and because there's no ICI between slices, the workers never finish their first collective."
- **Our assessment**: This is the single most actionable, specific claim
  in the article for a practitioner: a one-line YAML omission produces a
  silent, non-crashing failure (see Claim 5) rather than an error message
  pointing at the missing field — exactly the kind of "gotcha" a source
  note should flag prominently rather than bury in a general "configure
  topology correctly" summary.

### Claim 5: The topology-omission failure does not crash — it leaves the deployment stuck in `DEPLOYING` indefinitely while burning TPU-hours, because the actual bug (one missing YAML field) produces no error message
- **Evidence**: Direct continuation of the Claim 4 failure-mode
  description.
- **Confidence**: emerging (first-party description; consistent with the
  described mechanism in Claims 3-4, but the specific "burning TPU-hours"
  cost framing is presented as illustrative rather than measured)
- **Quote**: "You don't get a crash, you get a deployment that sits in DEPLOYING forever while you burn TPU-hours hunting for a bug that's really one missing line of YAML."
- **Our assessment**: This is the article's clearest failure-report-style
  claim embedded inside a how-to: the failure is dangerous specifically
  *because* it is silent and resource-consuming rather than
  fail-fast — a debugging-cost pattern worth flagging even outside the
  TPU-specific context (a scheduling misconfiguration that manifests as
  "job hangs, no error" rather than "job errors immediately" is a much
  more expensive class of bug to diagnose).

### Claim 6: In practice, teams deploy a `RayService` (recommended over a raw `RayCluster` for production) on a published vLLM TPU image, wait for `Running` status, and curl the endpoint
- **Evidence**: Direct operational recommendation stated after the
  topology mechanism discussion.
- **Confidence**: emerging (a specific, named operational recommendation
  — `RayService` over `RayCluster` for production — stated without
  elaboration on why beyond the implicit context of Ray Serve's
  production-oriented feature set)
- **Quote**: "In practice you deploy a RayService (recommended over a raw RayCluster for production) on a published vLLM TPU image, wait for it to reach Running, and curl the endpoint."
- **Our assessment**: A concrete, checkable operational default (use the
  higher-level `RayService` resource, not raw `RayCluster`, for production
  TPU serving) — useful as a specific recommendation even though the
  article doesn't explain the underlying reason (RayService's built-in
  health-checking and zero-downtime-update behavior on top of RayCluster,
  which this article does not itself state).

### Claim 7: `iter_jax_batches()` delivers batches already as device-sharded JAX arrays, eliminating host-side NumPy-to-JAX copies that would otherwise stall the training or inference step
- **Evidence**: Direct claim about the API's behavior, paired with a code
  example (`ds.iter_jax_batches(batch_size=1024)`; see Concrete
  Artifacts).
- **Confidence**: emerging (first-party API description with a code
  example; not independently benchmarked against a host-side-copy
  baseline in this extraction — no before/after latency numbers are given)
- **Quote**: "It hands you batches that are already JAX arrays and already device-sharded, so a training input pipeline or a large batch-inference job pulls straight from a Ray Data pipeline with no host-side NumPy-to-JAX copy stalling the step."
- **Our assessment**: Names the specific bottleneck being eliminated
  (host-side NumPy→JAX array conversion) rather than a vague "faster data
  loading" claim, which makes the claim checkable even without a
  benchmark: a reader can verify whether their own pipeline currently pays
  that conversion cost. No quantified improvement is given, so the
  *magnitude* of the win is unstated.

### Claim 8: `iter_jax_batches()` handles the ragged final batch (one not evenly divisible by batch size) via an explicit drop/pad/raise choice, rather than producing a shape error partway through a run
- **Evidence**: Direct API-behavior description immediately following
  Claim 7.
- **Confidence**: settled (a specific, checkable API design choice —
  explicit ragged-batch handling modes — independently verifiable against
  Ray's public API documentation)
- **Quote**: "it handles the ragged final batch (the one that isn't a clean multiple of your batch size) with an explicit choice of drop, pad, or raise, instead of a shape error three hours into a run."
- **Our assessment**: The "three hours into a run" framing is a specific,
  relatable failure-cost detail (a shape-mismatch error surfacing only
  when a particular batch boundary is hit, not on the first batch) — this
  is a general data-pipeline design lesson (make ragged-batch behavior an
  explicit, upfront choice rather than a runtime surprise) that
  generalizes well beyond the TPU/JAX-specific context.

### Claim 9: `JaxTrainer`'s worker function must `import jax` inside the function body, not at module scope, because each worker initializes JAX in its own TPU context — importing at module scope produces cryptic device-initialization errors before the first training step
- **Evidence**: Direct explanation of the code comment
  (`import jax  # import jax INSIDE the worker fn (TPU requirement)`) in
  the `JaxTrainer` code example (see Concrete Artifacts).
- **Confidence**: settled (a specific, actionable, independently testable
  claim about import placement and its failure mode — a reader can verify
  this by moving the import and observing the described error class)
- **Quote**: "The import jax lives inside train_loop_per_worker, not at the top of the file, because each worker initializes JAX in its own TPU context; import it at module scope and you'll fight cryptic device-init errors before the first step."
- **Our assessment**: This is the single most concrete, non-obvious
  "gotcha" in the article — the kind of constraint that isn't discoverable
  from the code shape alone (a top-level `import jax` looks more idiomatic
  to most Python developers) and would otherwise cost real debugging time,
  consistent with MINER.md's guidance to extract specific failure/gotcha
  details rather than generic advice.

### Claim 10: `topology="4x4"` in `JaxTrainer`'s `ScalingConfig` is the entire placement declaration — replacing what used to be a block of hand-written coordination code — and the only substantive difference from a GPU `JaxTrainer`/`TorchTrainer` is `use_tpu=True` plus a topology instead of a GPU count
- **Evidence**: Direct comparison statement following the `JaxTrainer`
  code example.
- **Confidence**: emerging (first-party comparison to the GPU code path;
  plausible given the shared `ScalingConfig` abstraction described, but
  the GPU-path code itself is not shown side-by-side in the article for
  direct comparison)
- **Quote**: "topology=\"4x4\" is the entire placement declaration, the line that used to be a block of hand-written coordination code. Set next to a GPU JaxTrainer or TorchTrainer, the only real difference is use_tpu=True and a topology instead of a GPU count."
- **Our assessment**: This is the article's strongest "why should I care"
  claim for a team already using Ray Train on GPUs: the API surface
  parity claim (same trainer classes, same `ScalingConfig` pattern, one
  or two different fields) is what makes TPU adoption low-friction *if*
  true — but it is an unverified comparison in this extraction (no GPU
  code sample shown alongside it to check the "only real difference"
  framing).

### Claim 11: Because Ray Train owns the training loop, `JaxTrainer` provides checkpointing and fault-tolerant restarts, which is what makes long TPU runs on preemptible capacity actually complete; topology scales to multi-slice when one slice is insufficient
- **Evidence**: Direct causal claim connecting Ray Train's loop ownership
  to preemptible-capacity viability, stated as the article's closing
  summary of the `JaxTrainer` section.
- **Confidence**: anecdotal (a causal claim about *why* preemptible runs
  succeed, asserted without a specific failure-rate or completion-rate
  number, before/after preemptible-run comparison, or link to
  checkpointing implementation detail)
- **Quote**: "This is because Ray Train owns the loop, you get checkpointing and fault-tolerant restarts, which is what makes long TPU runs on preemptible capacity actually finish, and topology scales to multi-slice (Ray wires the cross-slice coordination) when one slice isn't enough."
- **Our assessment**: The underlying mechanism (framework-owned loop →
  built-in checkpoint/restart → preemption resilience) is a standard and
  plausible distributed-training pattern, but this article gives no
  concrete measurement (e.g., "X% of preemptible runs now complete vs. Y%
  without this") to substantiate "actually finish" — treated as a
  first-party architectural claim, not a demonstrated result.

### Claim 12: Ray now publishes official `rayproject/ray:*-tpu` Docker images with the JAX/TPU stack (`jax[tpu]`, flax, optax, orbax-checkpoint) and profiling tooling preinstalled
- **Evidence**: Direct statement in the "Two final extras" section.
- **Confidence**: settled (a specific, checkable claim about published
  Docker Hub images and their preinstalled package list)
- **Quote**: "Ray now publishes official rayproject/ray:*-tpu images with the JAX/TPU stack (jax[tpu], flax, optax, orbax-checkpoint) and profiling tooling already installed, so you don't have to assemble a working TPU environment by hand."
- **Our assessment**: A concrete, independently verifiable artifact
  (specific package list, specific image-tag pattern on a public Docker
  Hub registry) rather than a vague "easier setup" claim — useful as a
  starting point for anyone trying to reproduce the article's setup.

### Claim 13: The Ray Dashboard now displays TPU utilization and memory alongside CPU and GPU on the Cluster tab, with `ray.util.tpu.init_jax_profiler()` exposing a per-worker JAX profiler the dashboard can attach to
- **Evidence**: Direct statement in the "Two final extras" section,
  naming a specific function.
- **Confidence**: settled (a specific, named public API function and a
  specific UI surface — independently checkable against the Ray
  documentation and dashboard)
- **Quote**: "the Ray Dashboard, Ray's built-in web UI for cluster and job state, now shows TPU utilization and memory next to CPU and GPU on the Cluster tab, with ray.util.tpu.init_jax_profiler() exposing a per-worker JAX profiler the dashboard can attach to."
- **Our assessment**: Observability parity with existing CPU/GPU dashboard
  support is a meaningful practical detail for teams evaluating whether
  TPU support is "first-class" vs. bolted-on — the specific function name
  (`ray.util.tpu.init_jax_profiler()`) makes this checkable rather than a
  vague "better monitoring" claim.

### Claim 14: Google's roadmap for Ray-on-TPU includes deeper Ray Data and Ray LLM TPU integration, SkyRL on multi-host TPU for reinforcement learning/post-training, and dynamic super/sub-slice support
- **Evidence**: Direct forward-looking statement in the "What's next"
  section.
- **Confidence**: anecdotal (a stated roadmap with no committed dates or
  version targets — standard vendor forward-looking language, not a
  shipped feature)
- **Quote**: "The Ray team on Google Cloud is widening TPU support from here: deeper Ray Data and Ray LLM TPU integration, SkyRL on multi-host TPU for reinforcement learning and post-training, and dynamic super/sub-slice support are all on the roadmap."
- **Our assessment**: Useful signal for where this ecosystem is headed
  (RL/post-training support specifically, via SkyRL, is named) but this
  is explicitly unshipped roadmap language — should not be cited as a
  current capability.

## Concrete Artifacts

### Ray Serve TPU topology config (verbatim from the article)

```yaml
accelerator_type: TPU-V6E
accelerator_config:
  kind: tpu
  topology: "4x4"
```

*Source: developers.googleblog.com/run-ray-on-tpu-part-2-ray-ai-libraries/, "Ray Serve on TPU" section.*

### Ray Data `iter_jax_batches()` usage (verbatim from the article)

```python
ds = ray.data.read_parquet("gs://my-bucket/train/")
for batch in ds.iter_jax_batches(batch_size=1024):
    # batch arrives as device-sharded JAX arrays, ready for the training step
    loss = train_step(batch)
```

*Source: developers.googleblog.com/run-ray-on-tpu-part-2-ray-ai-libraries/, "Ray Data on TPU: feeding the accelerators with iter_jax_batches" section.*

### `JaxTrainer` distributed training setup (verbatim from the article)

```python
from ray.train import ScalingConfig
from ray.train.v2.jax import JaxTrainer

def train_loop_per_worker(config):
    import jax            # import jax INSIDE the worker fn (TPU requirement)
    # ... your JAX/Flax training step runs here, once per host ...

trainer = JaxTrainer(
    train_loop_per_worker=train_loop_per_worker,
    scaling_config=ScalingConfig(
        use_tpu=True,
        topology="4x4",            # the slice shape, NOT a chip count
        accelerator_type="TPU-V6E",
    ),
)
trainer.fit()
```

*Source: developers.googleblog.com/run-ray-on-tpu-part-2-ray-ai-libraries/, "Ray Train on TPU: distributed training with JaxTrainer" section.*

### Referenced runnable sample and related docs (as listed in "Additional resources")

```
Runnable sample: Ray on TPU get-started in kubernetes-engine-samples
  (serve, data, and train steps; Qwen3-4B on a v6e slice)
Serve an LLM using TPUs on GKE with KubeRay
Ray Data API
Get started with distributed training using JAX
View TPU metrics on the Ray Dashboard
rayproject/ray on Docker Hub
```

*Source: developers.googleblog.com/run-ray-on-tpu-part-2-ray-ai-libraries/, "Additional resources" section. None of these linked pages were independently fetched in this extraction — see Extraction Notes.*

## Cross-References

- **Corroborates**: None found. No existing source note describes Ray,
  TPU slice/topology scheduling, `vLLM`-on-TPU serving, or `JaxTrainer`.
  `blog-google-tunix-gemma-reasoning-hackathon.md` and
  `blog-google-tunix-agentic-rl-throughput.md` both describe JAX/TPU
  training infrastructure (Tunix) but via a different, non-Ray framework;
  `blog-google-qwen35-ironwood-moe-optimization.md` describes TPU
  inference-serving optimization but for a custom JAX serving stack, not
  Ray Serve/vLLM.
- **Contradicts**: None found. No existing source note takes a position
  on Ray-on-TPU, gang-scheduling configuration, or JAX worker
  initialization that this source opposes.
- **Extends**: This is the corpus's third Google/TPU source note (after
  `blog-google-tunix-gemma-reasoning-hackathon.md`,
  `blog-google-tunix-agentic-rl-throughput.md`, and
  `blog-google-qwen35-ironwood-moe-optimization.md`) but the first
  covering Ray specifically and the first covering *inference serving via
  vLLM on TPU* rather than JAX-native training or a custom serving stack.
  It sits alongside those three as a fourth data point in the corpus's
  small cluster of TPU-infrastructure sources, all reaching the same
  "no direct chapter impact" conclusion for the same reason (see Guide
  Impact) — that pattern is now consistent across four independent Google
  TPU/JAX sources, which strengthens rather than weakens the case that
  this entire topic area sits outside the guide's current scope.
- **Novel**: This is the corpus's first source describing: (1) Ray as a
  distributed-computing framework on TPU at all; (2) the
  `accelerator_config.topology` gang-scheduling gotcha in Ray Serve and
  its specific silent-hang failure mode; (3) `iter_jax_batches()` and
  explicit ragged-batch handling; (4) the "import jax inside the worker
  function" `JaxTrainer` requirement; (5) `RayService`-over-`RayCluster`
  as a production recommendation; (6) official `rayproject/ray:*-tpu`
  Docker images and Ray Dashboard TPU-metrics support.

## Guide Impact

Following the same assessment reached independently by all three prior
Google/TPU source notes in this corpus
(`blog-google-tunix-gemma-reasoning-hackathon.md`,
`blog-google-tunix-agentic-rl-throughput.md`,
`blog-google-qwen35-ironwood-moe-optimization.md`): this article is ML
deployment/infrastructure documentation — how to configure Ray's
serving, data-loading, and training libraries to run correctly on Google
Cloud TPU hardware — not guidance about how a practitioner builds,
configures, or operates an AI coding agent/harness. The guide's actual
chapters (confirmed by reading `guide/*.md` headers directly:
00-principles, 01-daily-workflows, 02-harness-engineering,
03-verification, 04-context-engineering, 05-team-adoption,
06-security-threat-model) address working *with* deployed AI coding
agents in a software-engineering context — none covers distributed ML
training/serving infrastructure, TPU scheduling, or accelerator
orchestration.

- **No direct chapter impact recommended.** None of Claims 1-14 describes
  a harness-configuration practice, a verification technique, a
  context-management pattern, a team-adoption process, or a security
  consideration for coding-agent usage. The Prospector's three triage
  comments proposed Ch02 (Harness Engineering), Ch03 (Verification), and
  Ch04 (Context Engineering) relevance, but on reading the full article
  its subject is entirely TPU cluster/scheduling configuration for
  serving and training generic ML/LLM workloads — a different audience
  (ML infrastructure engineers operating Ray clusters, not developers
  using a coding assistant) and a different layer of the stack (the
  compute substrate an AI *product* might run on, not the harness a
  *developer* uses to write code with AI assistance).
- **Weak, indirect analogy only, flagged rather than forced**: Claim 5's
  failure-mode shape (a silent, resource-burning hang caused by one
  missing configuration field, with no error message pointing at the
  actual cause) is the same general *class* of debugging problem this
  guide's Ch03 (Verification) and Ch06 (Security/Threat Model) content
  cares about — misconfigurations that fail silently rather than loudly —
  but the specific mechanism (TPU slice placement groups, ICI mesh
  topology) has no transferable technical content for a coding-harness
  context. If the guide ever adds content on the economics/operations of
  self-hosting or fine-tuning models for agentic-coding infrastructure,
  this source (together with the three other TPU notes) would be
  background reading for that new scope, not a citation for any existing
  section.

## Extraction Notes

- **Verified the source is real and current before extraction.** Fetched
  the raw article HTML directly via `curl` (HTTP 200, ~50KB response) and
  stripped markup with a Python script to obtain full, close-to-verbatim
  article text, rather than relying solely on the WebFetch tool's
  AI-summarized pass (which had paraphrased several sentences — e.g.
  rendering "Serving is where most teams start from" as "Serving is
  typically where most teams begin" — and was not used as a quote
  source). Every `Quote` field above was verified as a literal substring
  of the `curl`-fetched, tag-stripped article text (confirmed
  programmatically) before being included in this note. A small number of
  quotes had incidental extra whitespace around inline `<code>` spans as
  an artifact of HTML-tag stripping (e.g. a stray space before a comma or
  around parentheses in `train_loop_per_worker` / `jax[tpu]`); that
  stripping-artifact whitespace was normalized to match how the text
  actually renders on the live page, without altering any wording.
- **Read the linked Part 1 article for background context** ("Run Ray on
  TPU, Part 1: The foundations," developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/,
  published July 20, 2026, same authors) since Part 2 repeatedly assumes
  its content (slices, `slice_placement_group()`, the GKE Ray Operator
  add-on, the `ray.io/tpu-slice-name` label). Part 1 is **not** the
  subject of this note and none of its content is quoted or claimed
  above — it was read only so this note's Source Context and claim
  assessments accurately reflect what Part 2 is building on. Part 1 also
  states "As of Ray 2.55, Google Cloud TPUs are a first-class accelerator
  in Ray," which is useful context for why this Part 2 article exists now
  but is Part 1's claim, not Part 2's — if Part 1 is separately filed as
  a source, it should be mined as its own note rather than folded into
  this one.
- **Did not follow the `kubernetes-engine-samples` GitHub repository** or
  the other four "Additional resources" links (KubeRay serving guide, Ray
  Data API reference, JAX distributed-training guide, Ray Dashboard TPU
  metrics doc). The article's own text was sufficiently complete and
  self-contained for the claims extracted here; the linked repository is
  a large, actively-changing code sample rather than a short substantive
  page, and independently verifying its current contents against the
  article's three code snippets was judged out of scope for this
  extraction pass. Flagged here per MINER.md's guidance to note what
  wasn't followed rather than silently omit it.
- **Existing overlap checked before writing.** Searched all
  `source-notes/*.md` for "Ray", "TPU", "JAX", "vLLM", "Ray Serve", "Ray
  Data", "Ray Train", "gang-schedul", "slice_placement_group", "topology",
  "multi-host" before drafting (see Cross-References). Found three
  topically-adjacent Google/TPU/JAX notes (Tunix ×2, Qwen 3.5/Ironwood)
  and no existing coverage of Ray specifically.
- **Confidence rationale**: Set to `emerging` overall. Several claims are
  independently checkable, specific technical facts (`settled`: Claims 1,
  2, 8, 9, 12, 13 — hardware constraints, explicit API design choices,
  named public functions). The mechanism claims about Ray Serve's
  internal scheduling behavior (Claims 3, 4, 5) and the `JaxTrainer`
  GPU-parity/preemptible-completion claims (Claims 10, 11) are first-party
  architectural descriptions not independently verified against the Ray
  source code or a reproduced benchmark in this extraction — no numeric
  performance, latency, or success-rate figures appear anywhere in the
  article to substantiate the causal claims in Claims 5 or 11. The
  roadmap claim (Claim 14) is explicitly unshipped. The overall `emerging`
  rating reflects that mix: concrete API/config facts are strong,
  internal-mechanism and outcome claims are asserted but unverified.
