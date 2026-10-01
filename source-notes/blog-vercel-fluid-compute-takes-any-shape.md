---
source_url: https://vercel.com/blog/fluid-compute-takes-any-shape
source_type: blog-post
title: "Compute that takes any shape"
author: Luke Phillips-Sheard (Engineering Manager, Infrastructure, Vercel)
date_published: 2026-09-01
date_extracted: 2026-10-01
last_checked: 2026-10-01
status: current
confidence_overall: anecdotal
issue: "#3839"
---

# Compute that takes any shape

> Vercel's infrastructure team reframes "Fluid" as a single compute layer (Hive VMs + Fluid images + Vercel Drives) under builds, sandboxes, and functions, and argues agent workloads need machines assembled instantly with state decoupled from compute.

## Source Context

- **Type**: blog-post (first-party vendor engineering/positioning post, ~4 min read)
- **Author credibility**: Engineering manager for Vercel Infrastructure; first-party knowledge of the system, but vendor-authored and promotional.
- **Scope**: Architecture overview of Fluid (Hive, Fluid images, Drives) and why agents need it. No code, benchmarks, pricing tables, or limits. Millisecond/scale figures are asserted without methodology.

## Extracted Claims

### Claim 1: Vercel runs builds, sandboxes and functions on one shared compute system, with stated production scale
- **Evidence**: Vendor-reported usage figures; no methodology.
- **Confidence**: anecdotal
- **Quote**: "Fluid compute now runs over 15 million builds a day, 25 million sandboxes a week, and a trillion requests a month."
- **Our assessment**: Plausible scale claim from first party; useful as a "production-proven" signal but unverifiable. Note the term "Fluid compute" is now used both for the execution model and for the whole substrate.

### Claim 2: Iteration velocity is gated by how fast the machine an app or agent needs can be provisioned
- **Evidence**: Assertion/framing.
- **Confidence**: anecdotal
- **Quote**: "Iteration velocity is now set by how quickly you can provision the computer your app or agent needs."
- **Our assessment**: A thesis, not a measured result. Reasonable for agent loops where each task needs a fresh environment.

### Claim 3: Standard cloud VMs are too slow to provision for agent workloads
- **Evidence**: Assertion; no numbers for the VM baseline.
- **Confidence**: anecdotal
- **Quote**: "For agents, even the cloud is too slow. A standard VM can't provision fast enough to keep up with how they work, but this is where Fluid excels."
- **Our assessment**: Directionally consistent with the broad move to snapshot/microVM sandboxes, but the comparison is unquantified and self-serving.

### Claim 4: Different workloads have different bottlenecks (build = compute-bound, function = IO-bound, sandbox = flexibility-bound), so the platform assembles a differently-shaped machine for each
- **Evidence**: Conceptual taxonomy.
- **Confidence**: anecdotal
- **Quote**: "A build is compute-bound, so it wants a beefy machine, heavy on CPU and memory. A function is IO-bound, loading specific code to run the instant a request lands, usually on a small VM. A sandbox is flexibility-bound, taking whatever configuration the work calls for with a Drive attached for user data."
- **Our assessment**: Useful vocabulary for choosing compute for agent components (orchestrator vs. code-execution vs. build).

### Claim 5: Hive is an internal control plane that provisions isolated VMs (usually pre-warmed) with one API for all products
- **Evidence**: Architecture description; no benchmarks beyond "milliseconds".
- **Confidence**: anecdotal
- **Quote**: "If an agent needs to run code, Hive provides an isolated VM, usually one already warm, so it's ready instantly."
- **Our assessment**: Warm pools are the standard way to hide VM boot cost. Detail on pool sizing/cost is absent.

### Claim 6: Isolation stronger than an isolate or container is available without a startup-time penalty
- **Evidence**: Vendor assertion.
- **Confidence**: anecdotal
- **Quote**: "Hive provisions a full VM in milliseconds and brings your filesystem state along with it, so you get isolation stronger than an isolate or a container, without paying for it in startup time."
- **Our assessment**: Important if true for running untrusted agent code; needs independent benchmarking ("milliseconds" is unspecified).

### Claim 7: Customers can bring their own OS image, converted to a resumable snapshot format (VHS) rather than booted
- **Evidence**: Product description; links to Dockerfile deploys, sandbox custom images, Sandbox Snapshots; v0 cited as internal user.
- **Confidence**: emerging
- **Quote**: "In the background, Vercel converts images into a Fluid image in a format we call VHS (Vercel Hive Snapshot), the optimized boot format behind Dockerfile deploys and sandbox custom images, so it can resume rather than boot and a custom machine is ready in milliseconds."
- **Our assessment**: Resume-from-snapshot instead of cold boot is the key mechanism. Extends the sandbox managed-images note.

### Claim 8: Storage should outlive compute — Drives let agent state persist across swapped machines and sessions (sandbox private beta only)
- **Evidence**: Product description; availability caveat stated.
- **Confidence**: emerging
- **Quote**: "Drives aren't bound to a single machine, you can swap the compute underneath it and pick up exactly where you left off in the next session. Drives attach to sandboxes today, in private beta, and extend to the rest of Fluid from there."
- **Our assessment**: Matches the agent-state-outside-the-harness principle. Functions/builds support is roadmap, not shipped.

### Claim 9: A unified substrate means improvements propagate to all products and new compute shapes can be added without rebuilding
- **Evidence**: Design argument.
- **Confidence**: anecdotal
- **Quote**: "a gain in boot time, isolation, scheduling, or caching lands across functions, sandboxes, and builds at once, instead of being rebuilt three times."
- **Our assessment**: Sound platform-engineering reasoning; the benefit accrues to the vendor and indirectly to users.

### Claim 10: Agents have three infrastructure requirements: secure boundary, own environment, state that outlives compute
- **Evidence**: Argument from agent behavior.
- **Confidence**: emerging
- **Quote**: "An agent runs untrusted code, so the machine needs a secure boundary. It brings its own tools, so the machine needs its own environment. And because an agent spins up and tears down constantly, its state has to outlive the compute."
- **Our assessment**: A clean three-point checklist for evaluating agent execution platforms.

### Claim 11: Fluid compute (execution model) multiplexes requests on one instance and bills Active CPU only
- **Evidence**: Restatement of previously documented behavior.
- **Confidence**: settled
- **Quote**: "Many requests run on one instance, instead of each spinning up its own."
- **Our assessment**: Not new; corroborates earlier notes.

## Concrete Artifacts

```
Source: Vercel blog, "Compute that takes any shape" (2026-09-01)
Stack: Hive (isolated VMs / "hardware") + Fluid images (VHS snapshot format, pushed to Vercel Container Registry) + Vercel Drives (portable durable storage)
Scale: 15M builds/day, 25M sandboxes/week, 1 trillion requests/month
Shapes: build = compute-bound; function = IO-bound; sandbox = flexibility-bound
Availability: Drives = private beta, sandboxes only
```

## Cross-References

- **Corroborates**: `blog-vercel-zero-config-node-servers.md` Claim 8 (many concurrent invocations on one warm instance) and Claim 5 (Active CPU billing); `blog-vercel-websocket-support-public-beta.md` Claim 2 (one instance multiplexes many connections).
- **Contradicts**: None found.
- **Extends**: `blog-vercel-sandbox-managed-images.md` (Claim 10 custom images pushed to VCR) — this post names the underlying VHS snapshot format and Hive control plane; `blog-vercel-herdr-agent-sandboxes.md` (persistent sandboxes) — Drives is the storage layer generalizing that persistence.
- **Novel**: The Hive / Fluid images / Drives decomposition, the "workload shape" taxonomy, and the claim that all Vercel compute products share one substrate. Earlier Vercel notes cover pricing and limits, not this architecture.

## Guide Impact

- **Chapter 05 (agent infrastructure)**: Could add the three-requirement checklist (Claim 10) and the "state outlives compute" principle (Claim 8) as criteria for choosing an agent execution environment, citing this note as a vendor-reported, unbenchmarked example.
- **Chapter 02**: Optional supporting reference for separating agent state from the machine; low priority given the evidence level.
- No existing guide recommendation is contradicted.

## Extraction Notes

- Fetched the full page and read it in full; it is short (~4 min) and marketing-leaning. Linked pages (docs for Drives, Fluid images) were not followed.
- Triage comments disagreed on novelty (low to high). Assessment: architecturally new relative to the corpus, but low in evidence depth (no code, benchmarks, or limits), hence `anecdotal`.
