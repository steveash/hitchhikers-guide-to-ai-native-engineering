---
source_url: https://www.latent.space/p/modal2026
source_type: blog-post
title: "Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO"
author: Akshat Bubna (Modal), interviewed by swyx and Vibhu (Latent Space)
date_published: 2026-07-08
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: emerging
issue: "#2224"
---

# Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO

> A long-form Latent Space podcast interview with Modal's CTO, recorded just after
> Modal's $355M Series C, covering the shift from "developer experience" to "agent
> experience" as a design principle, and the concrete infrastructure Modal has built
> for agent-shaped workloads: elastic inference with GPU snapshotting, open-sourced
> block-based speculative decoding (DeFlash), a 17-cloud-provider "supercloud" with
> its own reliability layer, private IPv6/RDMA networking for serverless multi-node
> training, and a hard-guardrails stance on sandbox-level agent permissions.

## Source Context

- **Type**: blog-post (podcast transcript, Latent Space / swyx and Vibhu). Long-form
  recorded interview (~58 minutes per the episode's own timestamps), transcribed in
  full with timestamps and speaker attribution.
- **Author credibility**: Akshat Bubna is Modal's CTO, speaking days after Modal's
  disclosed $355M Series C. This is first-party, high-authority testimony about
  production infrastructure he personally directs — but it is also promotional
  (a launch-adjacent interview timed to the funding announcement), self-reported (all
  technical figures — 17 cloud providers, ~3 terabit/second internal networking,
  100,000 sandboxes for RL rollouts, "up to 30%"-style efficiency claims are absent
  here but similar unaudited figures appear — are Modal's own numbers, no third-party
  audit), and conversational (many claims are stated informally mid-interview, without
  the rigor of a written spec or blog post).
- **Scope**: Covers Modal's origin story (serverless-runtime-first, GPUs added before
  ChatGPT), the shift from developer experience (DX) to "agent experience" (AX),
  elastic inference for custom (non-LLM-API) models, GPU snapshotting, LLM inference
  work (DeFlash speculative decoding, Auto Endpoints), the 17-cloud-provider capacity
  pool and reliability layer, sandboxes (sidecars, private IPv6 overlay, RDMA
  multi-node training), compute strategy/capacity planning, batch tiers, an internal
  agentic auto-tuning system ("auto inference"), "Modal Bench," managed-agent
  partnerships (Anthropic and unnamed others) versus Modal's own specialized-sandbox
  positioning, and closing takes on competitors (Gitpod/Ona, Astral) and SDK language
  strategy. Does **not** cover: pricing, churn/retention data, independently verified
  benchmarks for any of the performance claims (GPU snapshotting speedup, DeFlash
  speedup vs. proprietary providers, "3 terabit per second" figure), or technical
  detail on how the contextual/stateful side of "hard guardrails" is actually
  implemented (the interview states the *position*, not the mechanism).

## Extracted Claims

### Claim 1: Modal added GPU support a year before ChatGPT launched, originally targeting classical (non-LLM) inference workloads, because Kubernetes was seen as unsuited to bursty, resource-heavy, and highly specialized (varying accelerators/images) compute
- **Evidence**: First-party origin-story account from the CTO, describing the initial product thesis (serverless runtime as a base primitive) and the specific technical gap in Kubernetes that motivated it.
- **Confidence**: emerging (specific, falsifiable company-history claim from a company officer; internally consistent; not independently dated/verified)
- **Quote**: "initially what we were thinking about was if we build a better runtime, it's a very useful primitive in itself. It's There's a lot of things that, get solved by serverless functions, like you can do, ETL stuff, you can do job queues, you can do all this, like, bursty processing, which it turns out every company had needs for. but then we also were thinking about this as like, this is a primitive that we can build a whole collection of products on, which are very verticalized. So perhaps data engineering would've been the first one, but we were thinking about inference. Back then it was more classical inference, like computer vision stuff and running XGBoosts and whatnot. But we added GPUs to the product a year before ChatGPT came out."
- **Our assessment**: A concrete, checkable historical claim (GPU support predating ChatGPT by roughly a year) that frames Modal's later AI-cloud pivot as opportunistic rather than founding-thesis — the founding bet was on serverless runtime primitives generally, not GPUs or LLMs specifically. Useful context for reading the rest of the interview's infrastructure claims as evolved, not originally designed, for agent workloads.

### Claim 2: The Kubernetes gap Modal targeted was specifically burstiness and environment specialization — Kubernetes was designed for slow-scaling web-server workloads, not compute-heavy workloads that need to burst up and down and run varying accelerators/images
- **Evidence**: First-party technical rationale for the original product decision, in response to a direct question about the founding problem.
- **Confidence**: emerging (specific technical characterization of a well-known system's design fit; internally coherent; not benchmarked against Kubernetes directly in this source)
- **Quote**: "Primarily it's just, none of the tooling that was out there was built for, one, a really great developer experience, and also there's a general trend of, a lot of the workloads that we were seeing were very. I wish there was a better word for it, but compute-heavy. Like, they need, one, like, need a lot more resources, so you need to burst up and down a lot, versus like Kubernetes designed for, like, slow scaling and, more for, like, web server use cases. And also there's just a lot more specialization in, like, what kinds of environments these workloads run in. Like, we had sometimes they need accelerators, sometimes they need different kinds of images, and this is just like a consistent thing that we saw across a lot of companies."
- **Our assessment**: Provides the specific technical vocabulary ("burst up and down," "specialization... in what kinds of environments") for a claim that appears throughout the rest of the interview in different forms (elastic inference, 100,000-sandbox RL rollouts, batch jobs) — Modal's positioning is consistently "workloads shaped differently from steady-state web servers," not merely "AI workloads."

### Claim 3: Modal reoriented its SDK team from optimizing for developer experience (DX) to optimizing for "agent experience" (AX), on the premise that the same self-provisioning, code-colocated infrastructure that benefits human developers benefits agents even more — an agent should not have to read hundreds of untyped Kubernetes YAML files to make an infrastructure change
- **Evidence**: First-party design-team-reorientation statement, with a specific comparison (decorator-based self-provisioning vs. reading/writing Kubernetes YAML) and a stated customer signal.
- **Confidence**: emerging (concrete organizational and design claim from the CTO; the "customers we talk to" comparison is asserted, not sourced to named customers or a benchmark)
- **Quote**: "We've changed our SDK team to think about agent experience instead of, developer experience and we think that the same benefits that apply for DX also apply for AX, which is why would you have an agent read through hundreds of Kubernetes files and like write YAML that's not even typed when it can make a couple of changes in a decorator and it gets this self-provisioning runtime of, being able to see its changes live in action? yeah, it just seems from the customers we talk to, they find Modal is much faster for agents to use versus operating on a different substrate."
- **Our assessment**: This is the interview's central framing claim and the one the Prospector's triage flagged as a "meta-pattern." It is a specific, actionable design principle — decorator-based, typed, code-colocated infrastructure configuration is asserted to be faster for agents to operate than untyped YAML at a different layer than the code — rather than a vague "agents need good tools" statement. No comparative data is given for "much faster," so treat the magnitude as vendor-asserted, but the underlying mechanism (agents manipulating typed code vs. untyped config in a separate file/format) is a concrete, testable design choice.

### Claim 4: Even as fewer humans read agent-generated code, observability (dashboards, CLI-accessible investigation tools) becomes more important than code-reading, because humans still need to interpret system behavior and make judgment calls
- **Evidence**: First-party operational observation, given as a direct answer to whether DX-era priorities still apply when agents write the code.
- **Confidence**: emerging (first-party practitioner claim; plausible mechanism given the premise that code review time drops when agents write code, but no usage/adoption data on how much CLI-based investigation actually happens)
- **Quote**: "Like how good is your dashboard? And of course, like we have, we push a lot of it to the CLI so the agents can do their own investigation, but you still need humans to go interpret what's going on and, make judgment calls and whatnot. and that's I feel like, Maybe more important now than looking at the code itself."
- **Our assessment**: This is the specific claim the Prospector's third triage comment highlighted as "guide contradiction potential" against "traditional DevOps assumed-competencies." It is not actually a contradiction of any existing corpus source (no note argues code-reading remains primary), but it is a distinct, quotable articulation of a priority shift: investment in dashboards/CLI-exposed observability over investment in code readability, once agents (not humans) are the primary code writers and readers.

### Claim 5: Modal's largest use case today is elastic inference for custom (non-LLM) models — it deliberately stayed out of the general LLM-API market and instead serves companies like Suno (audio) and Runway (video) plus robotics and computational-biology companies, whose combined multi-model, multi-region deployments compound the autoscaling problem beyond a single model's traffic pattern
- **Evidence**: First-party product-usage breakdown, naming specific customers and describing the specific autoscaling complexity (offset diurnal cycles across regions and across multiple deployed models per customer).
- **Confidence**: emerging (specific customer names and stated mechanism; usage-share claim ("biggest use case") is asserted without a percentage or revenue breakdown)
- **Quote**: "our biggest use case is, elastic inference. And the thing we first found product market fit, with was inference for custom models. So we stayed away from the LLM space, and we were serving companies like Suno for audio, Runway for video, robotics, comp bio companies that train their own model elsewhere. But Modal is the best black box that for deployment, scaling to however many GPUs you need as your traffic pattern changes. And we saw all of them like have a very unpredict- predict- predictable, traffic pattern. it's like diurnal. It's Some days, like the company will do a launch and, they'll need like, way more. And it's not just one model that they deploy. They-- all these companies deploy, lots of different models in different regions, and so the autoscaling problem becomes even harder because then you have to scale within a certain region, and those cycles are offset."
- **Our assessment**: This distinguishes Modal from LLM-token-serving inference providers (Fireworks, Together, Base10 — named later in the same turn) — its stated differentiator is autoscaling across many deployed custom models per customer, not per-token pricing on shared foundation models. Directly relevant to any guide discussion of "which inference infra to use for what" — Modal's own positioning is explicitly non-LLM-API-first.

### Claim 6: Modal built GPU snapshotting into its product — capturing GPU/model state (e.g., a compiled `torch.compile` model) so that a subsequent cold start restores from the snapshot and is substantially faster than a cold boot
- **Evidence**: First-party technical description of a specific, named product capability, given as the concrete answer to "why does inference need so much burstiness."
- **Confidence**: emerging (specific, named technical mechanism; no cold-start latency numbers given to quantify "way faster")
- **Quote**: "Because we found that it's not universally true that everyone else can autoscale, and we've gone deeper into it on the tech side by, we've incorporated GPU snapshotting into the product so we can take the GPU state, like your torch.compile model, snapshot it, and the next cold start is way faster."
- **Our assessment**: A concrete engineering answer to a burstiness problem, but "way faster" is unquantified — cite as a named capability, not a benchmarked result. This is the same "environment reconstruction speed" problem documented for CPU/code environments in `blog-cursor-cloud-agent-lessons.md` (Claim 1), applied here at the GPU/model-state layer instead of the filesystem/dependency layer.

### Claim 7: RL rollout workloads can require up to 100,000 sandboxes at once, making them "insanely bursty" compared to typical agent sandbox usage
- **Evidence**: First-party anecdotal figure, given in direct response to a question about whether agent sandbox usage is bursty like inference or batch jobs.
- **Confidence**: anecdotal (single round figure, no distribution, duration, or frequency data — how often a customer hits 100,000, for how long, or how many customers do this at all is not stated)
- **Quote**: "Yeah. Like when you're doing, rollouts, you sometimes need a hundred thousand sandboxes in your sandboxes."
- **Our assessment**: The episode description and this quote both use the "100,000 sandboxes" figure as the headline scale claim for RL/agentic training workloads — it is a real, specific number, but it is presented as an occasional peak ("sometimes"), not a sustained or typical load. The trailing "in your sandboxes" is preserved as it appears in the transcript (a transcription artifact, not corrected here per the no-paraphrase rule).

### Claim 8: Speculative decoding's speedup comes overwhelmingly from increasing "accept length" (how many draft-model-predicted tokens the larger model accepts per verification pass), not from kernel optimization — kernel work yields only a few percentage points, while accept-length gains are described as multiplicative
- **Evidence**: First-party technical explanation of speculative decoding mechanics, given as the stated thesis of Modal's own published work on the topic.
- **Confidence**: emerging (specific, technically detailed mechanism claim from a team that has published open-source work on this exact topic; no benchmark numbers given in this source to quantify "few percentage points" vs. "multiplicative")
- **Quote**: "Speculative decoding is you have a smaller model, called a draft model, predict tokens ahead of the bigger model, and then you have the bigger model, verify all of this, all the tokens are predicted. And the reason it's faster is if you're predicting, one token at once, you're bound by memory bandwidth. But if you can batch the verification of, the draft model, then you're much more efficient using compute, and it's faster, and as long as your draft model is producing a lot of tokens that can get accepted, which is called the accept length, you can get a speed up that's, multiple times of, the original model speed. and well, that's what we highlight here. It's Like people talk a lot about we made these kernels faster and whatnot, but improving kernel will only give you like few percentage points of improvement, and, increasing accept length, literally is a multiplicative decrease"
- **Our assessment**: This is a specific engineering-priorities claim: for teams working on inference speed, Modal's stated position is that draft-model quality/accept-length is a higher-leverage investment than kernel micro-optimization. It's asserted, not benchmarked in this source, but it is a checkable claim against Modal's own published DeFlash work (referenced but not itself fetched for this note).

### Claim 9: Modal open-sourced DeFlash, a block-based speculative decoder (predicting a block of tokens at once rather than one token at a time), explicitly to let anyone match the inference performance of proprietary providers without lock-in
- **Evidence**: First-party product/open-source-strategy description.
- **Confidence**: emerging (specific named artifact and stated open-source rationale; no independent confirmation that open-source DeFlash actually matches proprietary-provider performance)
- **Quote**: "we've been working a bunch on DeFlash, which is a block-based speculator. so it's instead of predicting, one token at a time, it's predicting a block. And we've been open sourcing our work with it. The next thing for us here is for helping people train speculators and custom models. it's it's something that traditionally is very forward-deployed engineering driven, support deployed, engineer driven, like you work with customers and help them do that. And our vision for. This is why we launched Auto Endpoints, is we want to make frontier-level performance available to everyone."
- **Our assessment**: Frames DeFlash and Auto Endpoints (Claim 10) as parts of a single strategy: open-source the inference-speed research, then productize access to it (Auto Endpoints) so customers don't need dedicated forward-deployed engineers to get the benefit. This is a specific build-vs-buy argument for inference optimization work.

### Claim 10: Auto Endpoints lets a customer get a fully-optimized (DeFlash-included) inference endpoint from the UI/CLI without touching model code, with full transparency (the generated code is visible and can be "ejected" into the full Modal code-based workflow once the customer wants to customize)
- **Evidence**: First-party product description of a specific, named feature and its transparency/escape-hatch design.
- **Confidence**: emerging (specific, named shipped feature with a described mechanism; not independently verified)
- **Quote**: "sometimes people don't wanna touch the code, and they wanna get started with an endpoint that works and has all the great performance and, scalability that Modal has. So we've made that easier with, a way to create an endpoint from our UI, from the CLI, that has all of our optimizations that we talked about, like the DeFlash stuff already baked in, and there's full transparency. So we give you the code, you can go run it yourself, and if you want, you can eject out into the full Modal experience, which we see as people get sophisticated, they do wanna tweak the models, they wanna, fine-tune stuff."
- **Our assessment**: The "eject" framing is notable — Modal is explicitly designing a low-code entry point that degrades gracefully into its full code-first product rather than being a walled-off, separate no-code tier. This is a specific product-design pattern (transparent generated code + explicit escape hatch) worth citing wherever the guide discusses no-code/low-code AI infra tooling.

### Claim 11: Running production-grade inference is a hard problem independent of autoscaling — Modal's stated differentiator beyond raw GPU rental or open-source inference engines (vLLM, SGLang) is controlling tail latency and ensuring every request is delivered at least once
- **Evidence**: First-party answer to a direct comparative question ("what's the delta between using Modal and running vLLM/SGLang yourself on rented GPUs").
- **Confidence**: emerging (specific claim about what production inference requires beyond an inference engine; no latency/reliability numbers given to substantiate the comparison)
- **Quote**: "it's it's not just that. I think it's it's that running production-grade inference is a hard infer problem."
- **Our assessment**: The transcript's immediately following turn (a separate speaker turn, not spliced into this quote) adds that this specifically means tail-latency control and at-least-once delivery guarantees — the point being that "delta vs. self-hosting an open-source engine" is not primarily about the model-serving code itself, but about the surrounding reliability engineering. Modal also states in the same exchange that it works closely with and upstreams contributions to the SGLang team, rather than treating open-source engines as a competitor to route around.

### Claim 12: Modal operates as a "supercloud" spanning 17 cloud providers with no owned data centers, betting that staying capital-light and focusing on a software reliability layer is a better strategy than building physical infrastructure — and built its own reliability layer specifically because "neo cloud" capacity varies widely in reliability
- **Evidence**: First-party infrastructure-strategy description with a stated mechanism for how reliability is achieved despite variable underlying capacity quality.
- **Confidence**: emerging (specific, named strategic and technical claim from the CTO; the count "17" and the reliability-layer mechanism are asserted, not independently audited)
- **Quote**: "we've built this capacity pool that spans, 17 cloud providers, so we're, we're very good at Running on various kinds of cloud capacity across the world" ... "There are a lot more neo clouds than you expect, and they all have various degrees of, various levels of reliability. And, that's why it's something we've invested a lot of time in, is building our own reliability layer on top. so if the GPU falls off the bus or something happens, we user workloads are not affected"
- **Our assessment**: This is a two-part claim worth keeping together: (1) breadth (17 providers, no owned data centers, capital-light-by-design) and (2) the reason breadth is viable (a reliability layer that absorbs individual neo-cloud failures so user workloads don't see them). The second half is the more operationally interesting claim for infra decisions — it implies Modal customers get provider-outage resilience "for free" as part of using Modal's abstraction, without needing their own multi-cloud failover logic.

### Claim 13: Modal built a private IPv6 overlay network (I6PN) so containers within the same customer workspace can address each other privately, originally as a primitive needed for its serverless multi-node GPU training product (which adds RDMA networking via a decorator), and separately observed customers using the overlay network for undocumented purposes Modal did not anticipate
- **Evidence**: First-party technical description of a named networking primitive, its original motivating use case, and an anecdote about unplanned customer usage.
- **Confidence**: emerging (specific named technical mechanism and stated design history; the "found it, it's not even in our docs" anecdote is a single, undated, unquantified observation)
- **Quote**: "we have this thing called I6PN, which we haven't talked about, which is this, like, overlay network using IPv6 addresses. so if Modal containers, within the same workspace, when this is enabled, can address each other using this private IPv6 address, and no one else can." ... "We built it because we needed it as a primitive for our distributed training product. so we have this other feature, which is you can add a decorator to a function, and you get a cluster of GPUs. and they have RDMA networking. so you can run a distributed training job, that's truly serverless."
- **Our assessment**: A specific instance of infrastructure built for one purpose (RDMA key exchange for distributed training) being discovered and repurposed by customers for another (general private container networking) — Modal frames this positively ("build primitives and let people figure it out") rather than as scope creep to police. Relevant as a data point for the "build narrow, well-defined primitives" school of infra design referenced elsewhere in the corpus.

### Claim 14: Modal's internal multi-node training networking runs at roughly 3 terabit/second, using RDMA to bypass the standard TCP networking stack for GPU-to-GPU memory transfer during distributed training
- **Evidence**: First-party technical figure given in direct response to a networking-architecture question.
- **Confidence**: anecdotal (single approximate figure — "I think like 3 terabit per second" — explicitly hedged by the speaker, no methodology or measurement conditions given)
- **Quote**: "When you run multi-node training on Modal, RDMA, I think Mellanox, is, or InfiniBand is like a, is all seen as RDMA. but it's a way to bypass the TCP networking stack and, transfer, stuff much faster, between one node, to the other. And we have I think like 3 terabit per second, internal networking"
- **Our assessment**: The speaker's own hedging ("I think like") marks this as an approximate, not a precisely measured or independently verified figure — cite it as an order-of-magnitude claim about Modal's internal training network bandwidth, not a benchmarked spec.

### Claim 15: Modal is skeptical of LLM-mediated permission systems at the sandbox level and argues production agent systems need hard, non-negotiable boundaries (which can be paired with softer, model-mediated guardrails on top) rather than trusting a model's in-context judgment for sandbox-level access control
- **Evidence**: First-party security-design position, stated directly in response to a question contrasting Modal's stance with Claude Code-style adaptive/model-mediated permission modes.
- **Confidence**: emerging (a stated design principle from the CTO of an infrastructure provider whose product is the sandbox layer this principle would be enforced in; not a technical implementation detail, no description of how the hard/soft pairing is actually built)
- **Quote**: "Yeah, I'm, I'm skeptical of LLM media permission for stuff that is at the sandbox level because you do want hard boundaries." ... "Yeah. I think you always need hard guardrails when you want, And you can pair those with softer guardrails, right? And that's gonna be a lot of mediated."
- **Our assessment**: "LLM media permission" is preserved verbatim as it appears in the transcript (evidently a transcription artifact for "LLM-mediated permission"). This directly extends the guide's existing "least agency" security material (see Cross-References) with a named infrastructure vendor's position: sandbox/execution-boundary enforcement should not be delegated to the model's own judgment, even as softer, model-negotiated layers exist above that hard boundary.

### Claim 16: Modal explicitly positions itself as a "specialized sandbox provider" for production-grade agents that outgrow foundation-lab managed-agent offerings, citing a named customer (Ramp, which runs its external-facing accounting agent on Modal) needing fine-grained control over file persistence/snapshotting, networking, and GPU access — while partnering with Anthropic and unnamed other foundation labs on the managed-agent side rather than competing with them directly
- **Evidence**: First-party market-positioning statement naming both a partner (Anthropic) and a customer (Ramp) with a specific use case.
- **Confidence**: emerging (specific partnership and named-customer claim; Ramp's use case is described by Modal, not independently corroborated by Ramp in this source)
- **Quote**: "we're, very excited to partner with Anthropic and some of the other foundation labs, will not name who we're also working with. the way we see it is the manage agent thing is a great place to start if you're starting out building an agent and, But then when you get to, building something more production grade, like you're a company that's like Ramp that's building their own, Ramp also runs their accounting agent on us, so their external-facing agent. You need a lot more control over, your compute primitive on things like, what sort - how do you persist different files that the agent has access to, and how do you snapshot and restore? How do you control the networking? maybe you want GPUs. When you get to that point, you kinda want, a specialized sandbox provider, that gives you those things, and that's the role that we are trying to play."
- **Our assessment**: This is the interview's clearest articulation of Modal's build-vs-buy positioning in the managed-agent market: managed agents (Claude Managed Agents and unnamed competitors) are framed as a good starting point, with Modal as the "graduate to production" layer beneath them, not a competitor to them. Notably, Modal does not take a position on where the agent harness itself runs (Claim 17) — its stated scope is the compute/persistence/networking primitives underneath, regardless of which harness or managed-agent product sits on top.

### Claim 17: Modal takes no position on whether the agent harness runs as a cloud-managed agent hooked up to a Modal sandbox, or runs inside the Modal sandbox itself, treating this as an open architectural question the market has not yet converged on
- **Evidence**: First-party statement of explicit architectural neutrality, immediately following Claim 16.
- **Confidence**: emerging (a stated non-position from a company officer; genuinely falsifiable if Modal later ships a harness-specific product)
- **Quote**: "We don't really have an opinion on the harness, whether it runs - it's a cloud-managed agent, and you hook it up to Model Sandbox, or you run the harness in Model Sandbox. We'll see where people converge with that."
- **Our assessment**: "Model Sandbox" (capitalized, singular) is preserved verbatim as a transcription artifact for "Modal Sandbox." This is a useful data point for the guide's treatment of the infra-vs-harness layering debate: Modal explicitly declines to bundle a harness opinion with its sandbox product, distinguishing it from vendors (Cognition/Devin, LangChain/Deep Agents Deploy) that ship an opinionated harness alongside their infrastructure.

### Claim 18: Modal has automated its own forward-deployed-engineering inference-tuning work with an internal agentic system ("auto inference") that runs configuration sweeps, profiles GPU workloads, and can even change the target GPU type (e.g., from H200 to B200) to find the best-performing configuration
- **Evidence**: First-party description of an internal tool, given as a concrete example of "auto research"/agent-run infrastructure experimentation.
- **Confidence**: anecdotal (single internal-tool description, no success rate, time-savings figure, or comparison to human-led tuning given)
- **Quote**: "our internal both training and inference teams use this the general shape of this quite a bit. like we have this one internal repo called auto inference, which essentially we've automated our own forward-deployed engineering efforts using, this harness, which is, the agent will just spin up a sweep of different things. It'll even run like, NVIDIA inside profiler and it'll like tweak configs and it'll arrive the right thing. it'll change your GPUs both from H200 to B200, and works really well."
- **Our assessment**: "NVIDIA inside profiler" is preserved verbatim (likely a transcription artifact for "NVIDIA Nsight profiler"). This is a concrete example of an infrastructure vendor using its own agent-native primitives (sandboxes, elastic GPU access) to automate a task that previously required a human forward-deployed engineer (inference configuration tuning across GPU types) — a specific, named instance of "agents operating the infrastructure" rather than merely "agents running inside the infrastructure."

## Concrete Artifacts

### Episode framing: "We discuss" bullet list (verbatim)
```
Source: latent.space/p/modal2026, episode description

- Why Kubernetes wasn't built for bursty AI workloads
- How Modal started as a better runtime before becoming an AI cloud
- Why Modal added GPUs before ChatGPT
- The shift from developer experience to agent experience
- Why observability matters when agents are writing the code
- Elastic inference for custom models across audio, video, robotics, and comp bio
- GPU snapshotting, cold starts, and why inference workloads are so bursty
- Why RL rollouts can require 100,000 sandboxes
- DeFlash, speculative decoding, and frontier-level inference performance
- Auto Endpoints and making optimized inference easier to deploy
- What Modal adds beyond vLLM, SGLang, and raw GPU rental
- Modal's 17-cloud capacity pool and supercloud strategy
- Networked sandboxes, sidecars, private IPv6, and RDMA
- Serverless multi-node training for post-training and research workloads
- Auto-research, model-guided sweeps, and agents launching GPU experiments
- Compute strategy, capacity planning, and batch tiers
- Why production agents need specialized sandboxes and hard guardrails
- Modal's take on managed agents, CI, Gitpod/Ona, Python, TypeScript, and Modal Bench
```

### Sandbox networking feature: sidecars (Docker Compose-style multi-container sandboxes)
```
Source: latent.space/p/modal2026, Akshat Bubna [00:27:04]

"So if you want Docker Compose, our sandboxes now support, this thing called
sidecars. So you can. A sandbox is a pod of containers, and you can run multiple
containers in, a sandbox. also useful because, going back to networking, people
want a lot of control over, outbound networking from a sandbox. Like, they might
wanna run a middle proxy for, like, maybe logging stuff for RL or, controlling
how egress can happen to a domain, injecting credentials."
```

### Batch tier: latency-insensitive pricing lever
```
Source: latent.space/p/modal2026, Akshat Bubna [00:39:16]

"one of the things we're building now is like a way for customers to get, If
they don't care about latency, like get much cheaper pricing and they'll get
results back in like next 24 hours or something, like a batch tier essentially."
```
Stated demand source (Akshat Bubna [00:40:11]): "it's from a lot of LLM companies,
like people who are doing computational bio, like they have to run really big
batch jobs and they don't care about when they get it back." Akshat states LLM
eval and synthetic-data-prep workloads are the exception where batch tiers are
requested for LLM use cases specifically.

### Modal Bench: internal benchmark for agent-tool gaps
```
Source: latent.space/p/modal2026, Akshat Bubna [00:37:26]

"we have a Modal skill now. ... Which is why we built this Modal Bench. It's to
find things like that, so we can address them in our tool."
```
Named gap this benchmark targets (Akshat Bubna [00:37:01]): agents "struggle with,
without right guidance and a skill" at using Modal's observability — specifically,
diagnosing a failure by reading logs and determining the correct fix.

## Cross-References

- **Corroborates**: `blog-cognition-devin-desktop.md` Claim 13 (Modal named as a
  design partner on Devin Desktop's multi-agent support, quoting Rahul Chalamala,
  Modal MTS: "Our engineers run multiple agents every day and Devin Desktop is the
  first tool that lets them manage all of them together, with shared context, from
  one place") — that note documents Modal as a *customer* of an agent-management
  IDE; this note documents Modal's own infrastructure-provider stance that agent
  workflows require purpose-built primitives (sandboxes, elastic inference,
  observability pushed to the CLI). The two sources are independent (one is Modal
  using another vendor's product, the other is Modal describing its own product)
  but both show Modal treating "manage/operate multiple agents" as a first-class
  design problem.
- **Corroborates**: `blog-langchain-deep-agents-deploy.md` Claim 9 (Modal listed by
  LangChain as one of four out-of-the-box sandbox integrations — Daytona, Runloop,
  Modal, LangSmith Sandboxes) — independent, third-party confirmation from a
  different vendor's own product announcement that Modal is used as a named
  sandbox backend in the broader agent-infra ecosystem, consistent with this
  source's Claim 16 framing of Modal as a "specialized sandbox provider."
- **Extends**: `blog-anthropic-zero-trust-ai-agents.md` Claim 5 ("least agency" —
  OWASP-coined extension of least privilege that constrains what an agent tool can
  do, how often, and where) — this source's Claim 15 (skepticism of LLM-mediated
  permission at the sandbox level; hard boundaries paired with softer guardrails)
  is an infrastructure vendor's concrete design stance for enforcing exactly that
  kind of boundary at the execution layer, independent of and consistent with the
  security-focused framing in that note.
- **Extends**: `blog-cursor-cloud-agent-lessons.md` Claim 1 (environment quality —
  not crashes — is the primary determinant of cloud agent output quality) — this
  source's Claim 6 (GPU snapshotting to speed up cold starts by restoring prior
  GPU/model state) is the same "reconstruct the environment fast and completely"
  principle applied at the GPU/model-state layer rather than the filesystem/
  dependency layer Cursor's note describes.
- **Novel**: The DX→AX (developer experience → agent experience) framing as an
  explicit, named SDK-team reorientation (Claim 3) is a new articulation in this
  corpus of "agents need different infrastructure primitives than humans" — prior
  corpus sources on harness design (e.g. `blog-latentspace-databricks-agent-clouds.md`)
  discuss agent-specific security/policy layers but not a company reorganizing its
  developer-facing SDK team around an "agent experience" mandate specifically. Also
  novel: the DeFlash accept-length-over-kernel-optimization argument (Claim 8), the
  17-cloud "supercloud" strategy with its own cross-provider reliability layer
  (Claim 12), the I6PN private-IPv6-overlay-repurposed-by-customers anecdote
  (Claim 13), and the internal "auto inference" agentic GPU-tuning system (Claim 18)
  — none of these appear in any existing corpus source.
- **Contradicts**: None identified. No existing source note stakes out a position
  that conflicts with the specific claims extracted here. No contradiction issue
  filed.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 3 (Modal's SDK team reorientation
  from DX to "agent experience," with the specific decorator-vs-untyped-YAML
  comparison) as a named example of a vendor explicitly redesigning developer-facing
  tooling around agent operators rather than human operators. Pair with Claim 4
  (observability over code-readability as agents write more code) as the
  operational consequence of that shift.
- **Chapter 06 (Security & Threat Model)**: Add Claim 15 (hard guardrails at the
  sandbox level, explicit skepticism of LLM-mediated permission for execution
  boundaries) as a named infrastructure vendor's position, directly alongside the
  existing "least agency" material from `blog-anthropic-zero-trust-ai-agents.md`
  Claim 5 — this gives the guide a second, independent voice (infra provider, not
  just a security-framework source) making the same "hard boundary, not model
  judgment" argument for the execution layer specifically.
- **Chapter 06 (Infrastructure & Cost) / Chapter 02**: Add Claim 16–17 (Modal's
  "specialized sandbox provider beneath managed agents" positioning, and its
  explicit non-opinion on where the harness runs) as a concrete data point in any
  discussion of managed-agent vs. self-hosted-harness tradeoffs, alongside the
  existing `blog-anthropic-claude-managed-agents.md` /
  `blog-langchain-deep-agents-deploy.md` material — this source adds the
  infrastructure-layer perspective (what a sandbox/compute vendor thinks
  production-grade agents need beyond a managed-agent starting point) that neither
  of those two notes currently covers.
- **Chapter 06 (Infrastructure & Cost)**: Add Claims 5–7, 9–14 (elastic inference
  for custom models, GPU snapshotting, 100,000-sandbox RL bursts, DeFlash/accept-
  length, Auto Endpoints, the 17-cloud reliability layer, I6PN/RDMA networking) as
  concrete, named examples of infrastructure specifically shaped by agent/AI
  workload burstiness and scale, distinct from traditional web-server capacity
  planning — useful supporting detail wherever the guide discusses GPU cost/scaling
  decisions for teams running their own model inference or RL training.

## Extraction Notes

- WebFetch's summarizing pass returned only a ~250-word abstract of this ~58-minute,
  ~1,440-line transcript even when explicitly prompted for full verbatim text — this
  would not have supported verbatim quoting per the extraction rubric. The full
  transcript was recovered by fetching the raw page HTML directly (`curl` with a
  browser user-agent) and converting the `available-content` article body to text
  locally; all quotes above were copied character-for-character from that recovered
  transcript, following the same recovery approach documented in
  `blog-latentspace-databricks-agent-clouds.md`'s Extraction Notes.
- This is a natural-speech interview transcript (filler words, interjections,
  cross-talk, incomplete sentences) rather than edited prose. Quotes were selected
  from Akshat Bubna's continuous single-turn statements and bounded at turn
  boundaries to avoid splicing non-adjacent material spoken across separate turns,
  per the no-splice rule. Transcription artifacts present in the source itself
  (e.g., "LLM media permission" for what is evidently "LLM-mediated permission,"
  "Model Sandbox" for "Modal Sandbox," "NVIDIA inside profiler" for what is evidently
  "NVIDIA Nsight profiler," the doubled "sandboxes in your sandboxes") are preserved
  verbatim in quotes rather than silently corrected, consistent with the precedent
  set in `blog-latentspace-databricks-agent-clouds.md`.
- Checked all four overlapping notes named across the issue's three Prospector
  triage comments (`blog-cognition-devin-desktop.md`,
  `blog-anthropic-code-w-claude-london-2026.md`,
  `blog-langchain-deep-agents-deploy.md`, `blog-latentspace-databricks-agent-clouds.md`)
  plus `blog-anthropic-zero-trust-ai-agents.md` and `blog-cursor-cloud-agent-lessons.md`
  for security/environment-quality overlap. `blog-anthropic-code-w-claude-london-2026.md`
  was read but contained no Modal-specific or directly overlapping claim worth
  cross-referencing beyond general "managed agents" context already covered via
  the other three notes. All cited claim numbers were re-read and confirmed against
  the current text of the cited notes before writing this note's Cross-References
  section; none were guessed or approximated.
- The issue's three Prospector triage comments cover the same source with
  overlapping but not identical chapter/novelty assessments (apparently repeated
  triage passes); all three were read and reconciled into the single extraction
  above rather than treated as three separate findings.
- Not extracted in depth (present in the transcript but too thin, off-topic for
  guide chapters, or purely personal/conversational to extract as standalone
  claims): the closing discussion of Python/TypeScript/Rust SDK language strategy,
  the compute-strategy/capacity-planning team discussion (interesting but no
  concrete mechanism beyond "reservation blends" and "supply chain bets" were
  given), the Gitpod/Ona and Astral competitor commentary, and the video-generation-
  agent tangent near the end of the interview.
