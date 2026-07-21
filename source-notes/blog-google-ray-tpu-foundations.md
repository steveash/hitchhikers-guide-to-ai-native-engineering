---
source_url: https://developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/
source_type: blog-post
title: "Run Ray on TPU, Part 1: The foundations"
author: "Ivan Nardini, AI Developer Relations (Google Developers Blog)"
date_published: 2026-07-20
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2096"
---

# Run Ray on TPU, Part 1: The foundations

> Google Developers Blog announcement that as of Ray 2.55, Google Cloud TPUs
> are a first-class, officially supported accelerator in Ray, and a technical
> walkthrough of the two-layer mechanism (GKE Ray Operator + Ray Core's
> `slice_placement_group()`) that guarantees a multi-host Ray workload lands
> atomically on one intact TPU "slice" — a distributed-systems orchestration
> report with only a thin, indirect connection to this guide's actual scope
> (AI-assisted software engineering practice, not ML infrastructure/cluster
> scheduling).

## Source Context

- **Type**: blog-post (official Google Developers Blog, developers.googleblog.com,
  published July 20, 2026; tagged AI / How-To Guides / Announcements).
  Auto-discovered via the trusted `google-developers` feed. This is Part 1 of
  a two-part series; Part 2 (covering Ray AI libraries — Train, Serve, Data —
  on TPU) was not yet published at extraction time and was not fetched.
- **Author credibility**: Ivan Nardini, AI Developer Relations at Google,
  writing on Google's own developer blog about a Google Cloud product
  capability (TPU support landing officially in the open-source Ray project).
  First-party vendor/DevRel content describing a real, versioned software
  release (Ray 2.55) rather than a speculative roadmap — the claims are
  architectural and mechanism-level (how slice placement works) rather than
  performance-benchmark claims, so there is less of the "self-reported
  multiplier" credibility problem seen in other first-party Google posts in
  this corpus (compare `blog-google-qwen35-ironwood-moe-optimization.md`).
- **Scope**: Covers why TPU support needs anything special (the TPU "slice"
  hardware model and the ICI interconnect), how GKE's Ray Operator add-on
  provisions and labels TPU slices for Ray (KubeRay + a TPU-specific webhook),
  the RayCluster manifest fields used to request a slice, and the Ray Core
  `ray.util.tpu.slice_placement_group()` primitive that atomically reserves a
  whole slice. Does NOT cover: the Ray AI libraries (Train/Serve/Data) that
  consume this primitive in practice (deferred to Part 2, not yet published),
  any performance numbers or benchmarks, pricing, or a comparison against
  running Ray on GPUs beyond the NVLink analogy used to explain the concept.

## Extracted Claims

### Claim 1: As of Ray 2.55, Google Cloud TPUs became a first-class, officially supported accelerator in Ray — shipping in Ray's release pipeline with pre-built images and support across core libraries — replacing an earlier "experimental" path that required hand-built containers and community support
- **Evidence**: Direct statement of the release/support-status change, with a
  specific Ray version number cited.
- **Confidence**: settled (a specific, versioned, checkable claim about an
  open-source project's release status, not a performance or marketing claim)
- **Quote**: "As of Ray 2.55, Google Cloud TPUs are a first-class accelerator in Ray. This means that TPUs are now in Ray's release pipelines with official pre-built images and support across the core libraries, instead of the old "experimental" path where you built your own containers and leaned on community help."
- **Our assessment**: This is the article's news hook — TPU support moving from community-maintained/experimental to officially shipped. It's independently checkable against Ray's own release notes for 2.55, so we treat it as a settled factual claim about release status rather than a persuasive claim about quality or performance.

### Claim 2: TPU chips are wired into a fixed hardware group called a "slice" — several host VMs whose chips share a dedicated high-speed interconnect (ICI) — and a multi-host model must land entirely on one intact slice, or the workers can't reach each other and the job hangs
- **Evidence**: Direct explanation of the core hardware constraint that
  motivates the rest of the post.
- **Confidence**: settled (a factual hardware/networking description)
- **Quote**: "TPU chips are wired together into a fixed group called a slice: several host machines (VMs) whose chips share a dedicated high-speed link called the ICI (Inter-Chip Interconnect). A multi-host model has to land on one whole slice, or its workers can't reach each other and the job just hangs."
- **Our assessment**: This is the load-bearing constraint the entire post exists to solve: ICI connectivity is scoped to a single slice, so any placement that splits a multi-host job across two slices is not a performance problem but a correctness/hang problem. This framing sets up why "something has to guarantee all your workers land on one intact slice" (see Claim 7).

### Claim 3: The post analogizes a TPU slice to a single multi-GPU box where the fast interconnect (NVLink) exists only inside the box — splitting workers across two such boxes with no connecting cable causes collective operations (the all-reduce steps that synchronize gradients) to hang, and the TPU's ICI plays the same role as that missing cable
- **Evidence**: Explanatory analogy offered to readers already familiar with
  GPU-based distributed training.
- **Confidence**: settled (an internally consistent teaching analogy, not an
  empirical claim requiring independent verification)
- **Quote**: "If you think in GPUs, picture a slice as a single multi-GPU box where the fast interconnect (NVLink) only exists inside the box. Split your workers across two boxes with no cable between them and the collective operations, the all-reduce steps that synchronize gradients, never finish. Training just hangs. A TPU slice behaves the same way: the ICI is that cable, and it only reaches the chips of one slice."
- **Our assessment**: A clean, transferable mental model for anyone coming from GPU-based multi-node training: "slice" maps directly onto "single NVLink domain," and the failure mode (hung collectives, not slow ones) is the same in both hardware families. Useful shorthand independent of Ray specifically.

### Claim 4: "Topology" denotes the shape of a TPU slice, expressed as dimensions like 4x4 for a 16-chip slice, and users request a topology rather than a raw chip count
- **Evidence**: Direct terminology definition.
- **Confidence**: settled
- **Quote**: "One more word you'll see everywhere is topology: it's the shape of a slice, written like 4x4 for a 16-chip slice. You ask for a topology, not a chip count."
- **Our assessment**: A small but important vocabulary point for reading the rest of the post's code and YAML: `topology="4x4"` is a shape specifier, not merely a resource-count request, because the physical wiring geometry of the slice matters for which collective algorithms are efficient.

### Claim 5: The GKE Ray Operator add-on (enabled via `--enable-ray-operator` on Autopilot clusters or `--addons=RayOperator` on Standard clusters) installs two components: KubeRay — the generic Kubernetes operator that turns RayCluster/RayService/RayJob YAML into running Ray clusters, identical to GPU usage — and a TPU-specific Ray TPU webhook that stamps every TPU host with labels like `ray.io/tpu-slice-name` so Ray can tell which machines share a slice's wiring
- **Evidence**: Direct description of what the add-on flag installs, naming
  both components and their distinct roles.
- **Confidence**: settled (a specific, named architectural description of a
  shipping GKE feature)
- **Quote**: "That single flag installs two things that matter for TPU. The first, KubeRay, is the Kubernetes operator that turns RayCluster, RayService, and RayJob YAML into running Ray clusters; it's the same KubeRay you'd use with GPUs. The second is the TPU-specific part: the Ray TPU webhook, which stamps every TPU host with labels like ray.io/tpu-slice-name so Ray can tell which machines are wired into the same slice."
- **Our assessment**: This separates "generic Ray-on-Kubernetes plumbing" (KubeRay, shared with GPU deployments) from "TPU-slice-awareness" (the webhook), which clarifies that adopting TPU support does not require learning a new orchestration layer — only a new labeling mechanism layered on top of the existing KubeRay path.

### Claim 6: A RayCluster worker-group manifest requests a TPU slice the same way it requests any node — via a `nodeSelector` specifying TPU generation/accelerator type and topology, plus a `numOfHosts` field for multi-host slices — and applying it brings up a head pod plus one worker pod per host in the slice
- **Evidence**: Direct YAML snippet and description of the resulting pod
  topology after applying the manifest.
- **Confidence**: settled (a concrete, reproducible configuration description)
- **Quote**: "From there, you ask for TPUs in a manifest the same way you'd ask for any node, with a nodeSelector for the generation and topology and the chip count as a resource. A multi-host slice adds one field, numOfHosts." / "applying that manifest brings up a head pod plus one worker pod per host in the slice."
- **Our assessment**: `numOfHosts` is the one addition beyond a standard single-node nodeSelector request, and it is what tells KubeRay to provision a genuinely multi-host slice rather than a single-host TPU node — a small but easy-to-miss detail for anyone porting a GPU RayCluster manifest to TPU.

### Claim 7: Ray Core's public `ray.util.tpu.slice_placement_group()` function is the mechanism that guarantees worker cohesion on TPU — it reserves a whole slice atomically (all hosts or none) by matching the webhook-applied labels
- **Evidence**: Direct description of the function's purpose and mechanism,
  paired with a runnable code example.
- **Confidence**: settled (a specific, named public API with a clearly stated
  atomicity guarantee)
- **Quote**: "Its TPU support lives in the public ray.util.tpu API, and there's really one function to know: slice_placement_group(). It takes that "keep my workers on one intact slice" guarantee from earlier and turns it into a single call, reserving a whole slice atomically (all hosts or none) by matching on the webhook labels."
- **Our assessment**: This is the single Ray Core primitive that closes the loop opened in Claim 2 — it is the concrete answer to "something has to guarantee all your workers land on one intact slice." Everything upstream (GKE provisioning, webhook labeling) exists to feed this one atomic reservation call.

### Claim 8: In practice, developers rarely call `slice_placement_group()` directly — Ray's AI libraries (Data, Train, Serve) invoke it internally, so users just declare a topology and the libraries handle slice reservation; direct calls are reserved for custom distributed workloads outside those three libraries
- **Evidence**: Direct statement about typical usage patterns, contrasting
  the low-level API with the higher-level libraries that wrap it.
- **Confidence**: emerging (plausible and consistent with the function being
  described as a foundational primitive, but this post does not itself show
  Train/Serve/Data calling the function internally — that detail is deferred
  to the not-yet-published Part 2, so it cannot be independently checked from
  this source alone)
- **Quote**: "It is important to highlight that you rarely call slice_placement_group yourself. The Ray AI libraries (Data, Train, Serve) call it for you, so in practice you declare a topology and they handle the slice. You'd only reach for slice_placement_group() directly when you're writing a custom distributed workload that isn't Train, Serve, or Data."
- **Our assessment**: This is a "trust the abstraction" claim rather than a demonstrated one within this specific post — reasonable given the described architecture, but readers writing custom distributed TPU workloads outside Train/Serve/Data are the actual audience for the code sample in Claim 7, and should not assume the libraries' internal call patterns without checking Part 2 or the library source directly.

### Claim 9: The `ray.util.tpu` API, including `slice_placement_group()`, is public but marked alpha-stability (`@PublicAPI(stability="alpha")`), meaning the surface can still change between Ray releases
- **Evidence**: Direct stability-marker disclosure.
- **Confidence**: settled (a specific, checkable API stability annotation)
- **Quote**: "One caveat worth knowing: the API is public but marked alpha (@PublicAPI(stability="alpha")), so it's usable today but the surface can still shift between releases."
- **Our assessment**: A useful caveat for anyone building production tooling directly against `ray.util.tpu` today: it is usable now, but not yet a stability-guaranteed interface. Teams should expect potential breaking changes and pin Ray versions accordingly if depending on this API directly rather than through Train/Serve/Data.

### Claim 10: This post is Part 1 of a two-part series establishing the GKE + Ray Core foundation for TPU support; Part 2 will cover the Ray AI libraries on TPU — serving LLMs with vLLM, feeding slices with Ray Data, and training with JaxTrainer
- **Evidence**: Direct statement of the series structure and Part 2's planned
  scope.
- **Confidence**: settled (a direct statement of publication plan, though
  Part 2's actual content cannot be verified until it is published)
- **Quote**: "In Part 2, we will explore how you can use Ray AI libraries on TPU for serving LLMs with vLLM, feeding slices with Ray Data and training with JaxTrainer."
- **Our assessment**: This post is explicitly scoped as foundational/mechanism-level; the higher-level, more directly usable library APIs (which most practitioners would actually call) are deferred to Part 2. A future source-mining pass should check for Part 2's publication and extract it separately once available.

## Concrete Artifacts

### GKE cluster creation commands enabling the Ray Operator add-on (verbatim from the post)

```bash
# Autopilot (fully managed nodes)
gcloud container clusters create-auto CLUSTER \
--enable-ray-operator --location=LOCATION

# or Standard (you manage node pools)
gcloud container clusters create CLUSTER \
--addons=RayOperator --location=LOCATION
```

Source: developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/,
"How GKE orchestrates Ray on TPU" section

### RayCluster worker-group manifest snippet requesting a TPU slice (verbatim from the post)

```yaml
# inside a RayCluster workerGroupSpec
nodeSelector:
  cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice   # the TPU generation
  cloud.google.com/gke-tpu-topology: "4x4"              # the slice shape
# ... and request chips via the google.com/tpu resource limit
numOfHosts: 4   # multi-host: how many host VMs make up this slice
```

Source: developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/,
"How GKE orchestrates Ray on TPU" section

### Ray Core `slice_placement_group()` usage example (verbatim from the post)

```python
from ray.util.tpu import slice_placement_group
from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy

# Reserve one whole v6e 4x4 slice (16 chips across 4 hosts), atomically
spg = slice_placement_group(topology="4x4", accelerator_version="v6e")
ray.get(spg.placement_group.ready(), timeout=600)

@ray.remote(resources={"TPU": 4})
def worker(rank, world): ...

tasks = [
    worker.options(
        scheduling_strategy=PlacementGroupSchedulingStrategy(
            placement_group=spg.placement_group)
    ).remote(rank=i, world=spg.num_hosts)
    for i in range(spg.num_hosts)
]
```

Source: developers.googleblog.com/run-ray-on-tpu-part-1-the-foundations/,
"Ray Core on TPU" section

## Cross-References

- **Corroborates**: No existing corpus note documents Ray's orchestration
  layer specifically, so there is nothing to directly corroborate this post's
  Ray-specific claims. More generally, this post follows the same first-party
  Google DevRel pattern already seen in `blog-google-qwen35-ironwood-moe-optimization.md`
  and `blog-google-tunix-gemma-reasoning-hackathon.md`: a named individual or
  team writing on the official Google Developers Blog about TPU-based ML
  infrastructure, with architectural/mechanism claims that are concrete and
  checkable even where headline framing ("first-class," "fully supported")
  is vendor-optimistic.
- **Contradicts**: No material contradictions identified with existing corpus
  source notes.
- **Extends**: `blog-google-tunix-gemma-reasoning-hackathon.md` (TPU v5e used
  for single-pod RL post-training via the JAX-based Tunix library) and
  `blog-google-qwen35-ironwood-moe-optimization.md` (TPU v7/Ironwood used for
  single-host custom-kernel inference serving) both document optimization
  work *within* a single TPU host or pod. This post covers the orchestration
  layer *above* that: how a workload gets placed onto a correct multi-host
  slice in the first place, before any training loop or serving kernel runs.
  Read together, the three notes span TPU-based ML work from cluster-level
  slice placement (this post) down to single-host kernel/training-loop
  optimization (the other two) — none of the three overlap in claims, but
  they describe adjacent layers of the same TPU-based ML infrastructure
  stack.
- **Novel**: This is the corpus's first source documenting: (1) Ray's
  official (Ray 2.55) TPU support and its move out of an experimental,
  community-supported status; (2) the TPU "slice" and "topology" hardware
  model and the ICI interconnect constraint; (3) the GKE Ray Operator add-on
  and its two constituent components (KubeRay, Ray TPU webhook); (4) the
  `ray.util.tpu.slice_placement_group()` atomic-slice-reservation API and its
  alpha stability status. No prior corpus note discusses Ray, KubeRay, or
  Kubernetes-based TPU slice scheduling in any form.

## Guide Impact

- **No direct chapter impact identified.** This guide (per `guide/*.md`
  chapter headers: 00-principles, 01-daily-workflows, 02-harness-engineering,
  03-verification, 04-context-engineering, 05-team-adoption,
  06-security-threat-model) is about the practice of AI-assisted software
  engineering — CLAUDE.md/harness design, multi-agent coding workflows,
  verification of AI-generated code, context management for coding agents,
  team adoption, and security threat modeling for agentic tools. This source
  is a distributed-systems/ML-infrastructure orchestration report about
  scheduling Ray workloads onto TPU hardware slices via Kubernetes. It
  contains no claims about coding agents, AI-assisted development workflows,
  or engineering practices for building *with* AI models — only
  infrastructure plumbing for running large-scale ML training/serving
  workloads. The Prospector's two triage comments proposed chapter mappings
  ("Ch05 Agent Infrastructure & Scale," "Ch04 Integrations & Context Windows,"
  "Ch04 Orchestration patterns," "Ch03 Distributed compute") that do not
  correspond to this guide's actual chapter structure or titles (confirmed by
  reading `guide/*.md` headers directly) — the same discrepancy already
  flagged in `blog-google-qwen35-ironwood-moe-optimization.md`'s Extraction
  Notes for a different issue's triage comments.
- **Weakest possible connection, flagged rather than forced**: If the guide
  ever adds content on infrastructure considerations for teams running large
  agentic-coding-adjacent ML workloads (e.g., self-hosted model fine-tuning
  or evaluation pipelines at scale), the slice/topology hardware model and
  the "atomic reservation of a hardware group" pattern (Claim 7) could be
  cited as a general distributed-scheduling concept — but this guide does not
  currently have such a section, and this single source does not justify
  adding one.

## Extraction Notes

- **WebFetch returned a paraphrased/summarized version on the first pass**,
  consistent with this corpus's prior experience that developers.googleblog.com
  is rendered through an AI-summarization layer in this environment (see
  Extraction Notes in `blog-google-agentic-resource-discovery.md` and
  `blog-google-qwen35-ironwood-moe-optimization.md`). To guarantee quote
  fidelity, the raw page HTML was fetched directly via `curl`, stripped of
  markup with a Python script, and all quotes above were taken from that
  raw, character-for-character text — not from the WebFetch summarizer's
  paraphrase.
- **No sub-pages followed.** The post links to three external resources (a
  "Ray on TPU get-started" runnable sample in the `kubernetes-engine-samples`
  GitHub repository, the "Ray Operator add-on on GKE" documentation, and the
  "Use TPUs with KubeRay" documentation) that were not fetched — the post
  itself states its claims (the slice/topology model, the manifest fields,
  the `slice_placement_group()` API and code sample) in sufficient, checkable
  detail without needing the linked pages, and per MINER.md's "up to 5 linked
  pages" guidance, these were judged as supporting reference material rather
  than substantive additional content the post's own claims depend on.
- **Existing overlap checked before writing.** Searched all `source-notes/*.md`
  for "Ray", "TPU", "KubeRay", and "GKE" before drafting. Found two
  topically-adjacent Google/TPU notes (`blog-google-qwen35-ironwood-moe-optimization.md`,
  TPU v7/Ironwood inference serving; `blog-google-tunix-gemma-reasoning-hackathon.md`,
  TPU v5e training) but no note covering Ray, KubeRay, or Kubernetes-based TPU
  slice orchestration — confirmed net-new coverage, addressed in
  Cross-References.
- **Part 2 not yet published.** This series' second installment (Ray AI
  libraries — Train, Serve, Data — on TPU) was referenced by this post but
  not available at extraction time (2026-07-21). A future mining pass should
  check whether Part 2 has been published and, if so, file it as a separate
  source for extraction — it should not be treated as already covered by
  this note.
- **Confidence rationale**: Set to `emerging` overall. The hardware/mechanism
  claims (slice/ICI model, GKE Operator components, manifest fields,
  `slice_placement_group()` API and its alpha-stability marker) are
  individually rated `settled` — they are concrete, specific, and
  independently checkable against Ray's and GKE's own documentation. The
  overall rating is `emerging` rather than `settled` because: (1) this is a
  first-party vendor announcement of a feature that only just reached
  official support status (Ray 2.55), with no independent adopter reports or
  production case studies cited; (2) Claim 8 (library-internal usage
  patterns) could not be verified from this post alone; (3) the series is
  incomplete (Part 2 not yet published), so the practical, most-commonly-used
  surface (the AI libraries) is not yet documented in the corpus.
