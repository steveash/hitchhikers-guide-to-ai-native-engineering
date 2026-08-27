---
source_url: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
source_type: blog-post
title: "smolmachines / smolvm as a sandbox for untrusted Python & JavaScript"
author: Simon Willison (publishing a research report authored by Claude Fable 5)
date_published: 2026-08-19
date_extracted: 2026-08-27
last_checked: 2026-08-27
status: current
confidence_overall: emerging
issue: "#2991"
---

# smolmachines / smolvm as a sandbox for untrusted Python & JavaScript

> Simon Willison tasks Claude Fable 5 with evaluating smolvm 1.8.3 (a
> Firecracker/libkrun-based hardware-isolated-VM sandbox) for running
> untrusted Python/JavaScript data transformations; the agent hits a missing
> `/dev/kvm` in its own Claude Code for web container and autonomously pivots
> to GitHub Actions runners to complete the test battery, producing the first
> concrete cold-start/warm-execution numbers for this class of sandbox in the
> guide's corpus.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "research" / "quotation" format
  — a short post that frames and largely reproduces a research report, here
  authored by an AI agent Willison tasked directly). Published 19 August 2026.
- **Author credibility**: Simon Willison is the creator of Django and one of
  the most widely-cited independent commentators on LLM tooling — already a
  `trusted-feed` source in this repo (see `blog-simonwillison-cybersecurity-proof-of-work.md`
  Source Context for prior credibility assessment). This particular post is
  editorial curation of primary output he personally generated: he assigned
  the research task to Claude Fable 5 running in Claude Code for web, and the
  bulk of the post's content is that agent's own research report, reproduced
  by Willison rather than independently authored by him. Willison's own
  contribution is the framing sentence and two short closing observations
  about the agent's behavior. This makes the post simultaneously (a) a
  first-hand account of an agent research task Willison personally ran, and
  (b) a report whose technical findings originate from an LLM, not from
  Willison's own hands-on testing — a distinction the guide should preserve
  when citing it.
- **Scope**: Covers a single version (1.8.3) of one sandboxing tool
  (smolvm / smolmachines.com) tested against a specific threat model —
  executing untrusted, LLM-supplied Python and JavaScript data
  transformations. Does NOT cover: comparison against gVisor, Docker sbx, or
  container-based isolation on cost/latency (the post doesn't benchmark
  smolvm against alternatives, only against its own vendor claims); multi-tenant
  or long-running-service deployment patterns; adversarial red-teaming of the
  sandbox boundary itself (the tests are functional/capability checks, not
  penetration tests). The post links to, and substantially reproduces, a
  GitHub research repo at
  `https://github.com/simonw/research/tree/main/smolmachines-untrusted-sandbox`
  containing `README.md`, `_summary.md`, `notes.md`, and raw test logs; several
  claims below (marked in their Evidence field) are sourced from that linked
  repo rather than being independently confirmed to sit verbatim in the blog
  post's own prose — see Extraction Notes.

## Extracted Claims

### Claim 1: smolvm 1.8.3 is well suited for sandboxing untrusted Python/JavaScript data transformations using hardware-isolated VMs rather than shared-kernel containers
- **Evidence**: Stated as the post's opening verdict sentence, and repeated
  verbatim in the linked repo's `_summary.md`.
- **Confidence**: emerging (single-run evaluation of one tool version by an
  AI research agent, published without independent replication)
- **Quote**: "Testing smolvm 1.8.3 shows it is well suited for sandboxing untrusted Python and JavaScript data transformations using hardware-isolated VMs rather than shared-kernel containers."
- **Our assessment**: This is a meaningful, falsifiable verdict rather than
  marketing copy — it explicitly names the alternative it is being compared
  against (shared-kernel containers) and the specific workload
  (LLM-triggered data transformations on untrusted input), not "sandboxing"
  in the abstract. The corpus already has strong evidence that battle-tested
  isolation primitives beat custom security logic
  (`blog-anthropic-how-contain-claude.md` Claim 14); this claim extends that
  principle to a hardware-VM primitive (Firecracker/libkrun) rather than the
  kernel-isolation primitives (gVisor, Seatbelt, bubblewrap) documented
  elsewhere in the corpus.

### Claim 2: smolvm's tested security controls — offline images, no-network execution, CPU/RAM limits, guest-enforced timeouts, storage quotas, read-only/writable mount separation, and `--unprivileged` — all worked as intended
- **Evidence**: Direct summary sentence from the post (matching `_summary.md`
  in the linked repo), consistent with the granular per-feature test results
  in `notes.md` (see Claim 9).
- **Confidence**: settled (concrete, itemized feature checklist confirmed by
  an actual test run, not a vendor claim restated)
- **Quote**: "Offline local images, no-network execution, CPU/RAM limits, guest-enforced timeouts, storage quotas, read-only input mounts, writable output mounts, and `--unprivileged` all worked as intended, with cold starts around 0.6–1.5 seconds and warm executions around 50 ms."
- **Our assessment**: This is the single most load-bearing sentence in the
  source for guide purposes — it is the closest the corpus has to a
  feature-by-feature confirmation checklist for a hardware-VM sandbox
  intended specifically for LLM-triggered code execution. The performance
  half of the sentence (cold/warm timings) is corroborated at finer grain by
  the individual boot measurements in Claim 10 below.

### Claim 3: The main caveats are that `--overlay` does not limit root filesystem writes, the HTTP API's timeout field requires camelCase `timeoutSecs`, offline image pulls must come from local archives, and the host needs KVM, Hypervisor.framework, or WHP
- **Evidence**: Direct caveats sentence from the post/`_summary.md`, matching
  the two failing tests reported in `notes.md` (PASS=12 FAIL=2 of 14 — Claim
  9) plus two operational prerequisites.
- **Confidence**: settled (specific, itemized failure modes from an actual
  test run)
- **Quote**: "The main caveats are that `--overlay` does not limit root filesystem writes, HTTP API timeouts require the camelCase `timeoutSecs` field, image pulls must be done from local archives when networking is disabled, and the host needs KVM, Hypervisor.framework, or WHP."
- **Our assessment**: Two of these four caveats are footguns a practitioner
  would only discover by testing (the `--overlay` flag silently not doing
  what its name implies, and the API's undocumented-until-tested camelCase
  requirement) rather than by reading marketing copy — this is exactly the
  kind of "verify, don't trust the design document" evidence the guide
  already argues for in Ch06's sandbox section (see Guide Impact). The
  hypervisor-backend requirement (KVM/Hypervisor.framework/WHP) is the
  deployment prerequisite that directly caused the local-environment failure
  described in Claims 12–13 below.

### Claim 4: The recommended production architecture is one ephemeral `machine run` per task, or persistent/forked VM pools for higher throughput
- **Evidence**: Direct architecture recommendation from the post/`_summary.md`.
- **Confidence**: emerging (architectural recommendation from a single
  evaluation, not validated at production scale in this source)
- **Quote**: "For production, the recommended design is one ephemeral `machine run` per task, or persistent/forked VM pools for higher throughput; see [smolmachines.com](https://smolmachines.com) for deployment options."
- **Our assessment**: This mirrors the one-VM(or-container)-per-task pattern
  already established in the corpus for Claude Cowork's full-VM isolation
  (`blog-anthropic-how-contain-claude.md` Claim 9) and for gh-aw's per-workflow
  runtime isolation — the "ephemeral, single-task, then discard" pattern
  recurs across every hardware-isolation source in the corpus regardless of
  vendor. The "forked VM pools" option is new to the corpus: it names warm-pool
  forking (pre-booting a VM once, then forking child instances) as the
  throughput lever when per-task cold starts (0.6–1.5s, Claim 2) are too slow
  for the target request rate.

### Claim 5: The recommended resource-limit configuration for a single sandboxed task is `--cpus 1 --mem 512 --storage 3 --timeout 30s --unprivileged`, with `/in` mounted read-only and `/out` read-write
- **Evidence**: Directly itemized in the post/`_summary.md` as a bulleted
  recommendation.
- **Confidence**: settled (specific, concrete configuration recipe, not a
  vague guideline)
- **Quote**: "Recommended limits: `--cpus 1 --mem 512 --storage 3 --timeout 30s --unprivileged`, with `/in` mounted read-only and `/out` read-write."
- **Our assessment**: This is a directly copy-adaptable default — one vCPU,
  512 MiB RAM, 3 GiB storage, 30-second timeout, unprivileged execution, with
  asymmetric mount permissions (input immutable, output writable). It is the
  hardware-VM-sandbox analogue of the gVisor `docker run` recipe already in
  the corpus (`blog-google-adk-zero-trust-agents.md` Claim 7:
  `--runtime=runsc --network=none --cap-drop=ALL --memory=64m --cpus=0.1`) —
  both sources converge on "minimal CPU/memory, no network by default,
  explicit timeout, capability-dropped" as the baseline recipe for
  sandboxing agent-triggered code, differing only in isolation tier (VM vs.
  kernel) and resulting resource footprint (512 MiB VM vs. 64 MiB gVisor
  container).

### Claim 6: The unauthenticated HTTP API should be restricted to a Unix socket with filesystem permissions
- **Evidence**: Direct operational security recommendation from the post/`_summary.md`.
- **Confidence**: settled (explicit, specific mitigation for a named gap)
- **Quote**: "The unauthenticated HTTP API should be restricted to a Unix socket with filesystem permissions."
- **Our assessment**: smolvm's HTTP control API ships with no authentication
  by default — the mitigation is host-level (Unix socket + filesystem
  permissions) rather than anything the sandbox's own isolation boundary
  provides. This is a reminder that the *control plane* for a sandbox (the
  API that creates/destroys/configures VMs) is a separate attack surface from
  the *sandboxed workload* itself, and needs its own access control
  independent of how well the VM boundary isolates untrusted code.

### Claim 7: smolvm's isolation is implemented via libkrun as the VMM, running a custom kernel (libkrunfw) — portable, hardware-isolated Linux VMs
- **Evidence**: Sourced from the linked GitHub research repo's `notes.md`
  (not independently confirmed to appear verbatim in the blog post's own
  prose — see Extraction Notes).
- **Confidence**: emerging (single-source technical characterization from the
  AI-authored research notes, not cross-checked against smolvm's own
  documentation)
- **Quote**: "Portable, hardware-isolated Linux VMs; VMM is libkrun with custom kernel (libkrunfw)"
- **Our assessment**: libkrun is a distinct virtualization stack from the
  Firecracker VMM used to run Claude Code's own container (Claim 12) — both
  are KVM-based hardware-isolation technologies, but this establishes that
  smolvm does not simply wrap Firecracker directly; it uses libkrun as its
  own VMM layer. This is a new technical detail for the corpus: no existing
  source note names libkrun as an agent-sandboxing VMM (the corpus's existing
  hardware-VM entries — gh-aw's "Docker sbx" — do not name their underlying
  VMM implementation).

### Claim 8: The test battery covered 14 tests, of which 12 passed and 2 failed
- **Evidence**: Sourced from the linked GitHub research repo's `notes.md`
  test-log summary line (not independently confirmed to appear verbatim in
  the blog post's own prose — see Extraction Notes). The two failures match
  the `--overlay` and camelCase-field caveats in Claim 3.
- **Confidence**: emerging (single test run, no independent replication)
- **Quote**: "PASS=12 FAIL=2 of 14."
- **Our assessment**: This is the concrete test-count backing Claim 2's
  "all worked as intended" framing — "all" refers to the *categories* of
  security control (network isolation, resource limits, mount separation,
  etc.), not to a 14/14 clean pass; two specific, low-severity test failures
  were found and are both documented with workarounds (use `--storage`
  instead of `--overlay`; use camelCase `timeoutSecs`). Practitioners
  reading only the summary sentence (Claim 2) without the underlying test
  log could reasonably assume a perfect result — the guide should preserve
  the 12/14 figure alongside the "all worked as intended" framing so it
  isn't read as stronger than the evidence supports.

### Claim 9: Cold boot from a local Alpine tarball took 643, 580, 577, 591, and 588 milliseconds end-to-end across five measured runs, against smolvm's own marketing claim of sub-200ms boots
- **Evidence**: Sourced from the linked GitHub research repo's `notes.md`
  (raw timing data; not independently confirmed to appear verbatim in the
  blog post's own prose — see Extraction Notes). The <200ms figure is
  reported in `notes.md` as smolvm's own advertised claim, immediately
  preceding the measured figures.
- **Confidence**: settled (five concrete, repeated timing measurements from
  an actual test run, directly compared against a stated vendor claim in the
  same document)
- **Quote**: "T1 cold boot from local alpine tar: 643/580/577/591/588 ms end-to-end."
- **Our assessment**: This is a real, if modest, gap between a vendor's
  marketing claim ("boots <200ms") and measured reality (577–643ms, roughly
  3x higher) — recorded by the same research report that otherwise endorses
  the tool. This is not treated in the source as a contradiction requiring a
  verdict (no existing corpus source makes a competing claim about smolvm's
  boot time), but it is a concrete instance of the "verify vendor claims
  against your own measurement" discipline the guide already argues for in a
  different context (network-isolation claims,
  `blog-simonwillison-meta-muse-spark-cyberattack.md`, cited in
  Ch06 "The Sandbox Is the Control"). We recommend the guide generalize that
  existing rule from "verify claimed network isolation" to "verify claimed
  sandbox performance," using this 200ms-vs-580ms gap as the example.

### Claim 10: A fork-bomb test inside the guest VM was contained — the guest shell died within 1 second, and host load rose only to 0.69
- **Evidence**: Sourced from the linked GitHub research repo's `notes.md`
  test-log line for test T7 (not independently confirmed to appear verbatim
  in the blog post's own prose — see Extraction Notes).
- **Confidence**: emerging (single test run, no independent replication; but
  a directly falsifiable, quantitative result)
- **Quote**: "T7 fork bomb: returned in 1s rc=2 (guest sh dies), host load 0.69."
- **Our assessment**: This is a concrete adversarial-resource-exhaustion test
  result, not just a resource-limit configuration claim — a fork bomb is a
  standard sandbox-escape/DoS probe, and the result (guest shell terminates
  within a second, host load stays under 1.0) demonstrates the VM boundary
  actually contained a runaway-process scenario rather than merely being
  configured with limits that were never adversarially exercised. This is
  the strongest single piece of evidence in the source for the isolation
  boundary holding under stress, and is new to the corpus — no existing
  source note documents a fork-bomb containment test against any sandbox
  technology.

### Claim 11: Simon Willison's own Claude Code for web container had no `/dev/kvm` and no vmx/svm CPU flags, so it could not run nested virtualization — and that container is itself a Firecracker guest
- **Evidence**: Direct statements from the blog post body, describing the
  environment the agent initially tried to run the smolvm tests in.
- **Confidence**: settled (first-hand, specific technical description of the
  environment actually used for this task)
- **Quote**: "This Claude Code container: Linux 6.18.5-fc-v20 (itself a Firecracker guest), 4 vCPU, 15GB RAM."
- **Our assessment**: This is a notable meta-finding for the guide's harness
  and agentic-execution material, independent of the smolvm evaluation
  itself: Claude Code for web's own sandboxed execution environment is a
  Firecracker microVM, and — because nested virtualization is generally
  unavailable inside a VM unless the hypervisor explicitly exposes it —
  running a *second* layer of hardware-VM isolation (smolvm) from inside
  that first VM was not possible without leaving it. Teams building on
  Claude Code for web (or similar VM-isolated agent runtimes) who want to
  test or deploy nested hardware-VM sandboxes need to provision that
  capability on separate, KVM-capable infrastructure — they cannot assume
  the agent's own execution container supports it.

### Claim 12: GitHub Actions Ubuntu runners do expose `/dev/kvm`, and Claude Fable 5 autonomously used a temporary workflow on the working branch to run the real test battery, then removed the workflow in its final commit
- **Evidence**: Direct statement from the blog post body describing the
  agent's own stated plan/pivot.
- **Confidence**: settled (first-hand account of the actual workaround used,
  described in the agent's own words as quoted by Willison)
- **Quote**: "GitHub Actions ubuntu runners DO expose /dev/kvm → run the real test battery via a temporary workflow on this branch, collect logs, remove workflow in final commit."
- **Our assessment**: This is a concrete, reusable pattern for any agent that
  hits an environment capability gap (missing KVM, missing a system
  dependency, missing network access) mid-task: rather than reporting the
  gap as a blocker, the agent identified an alternative execution
  environment it could reach (GitHub Actions, via a temporary workflow file
  on the same branch) that had the missing capability, used it to gather the
  real evidence, and then cleaned up the temporary infrastructure so it
  didn't persist in the final commit. This is a specific instance of the
  general "AI agent proactively works around infrastructure limits rather
  than stopping" behavior pattern.

### Claim 13: Willison characterizes the GitHub Actions pivot as a creative solution to Claude Code for web's environmental limits, and frames it as another example of Fable being relentlessly proactive
- **Evidence**: Willison's own closing commentary on the agent's behavior,
  distinct from the quoted research report itself.
- **Confidence**: anecdotal (a single author's characterization of a single
  agent run; not a measured or repeated finding)
- **Quote**: "Another example of Fable being relentlessly proactive."
- **Our assessment**: Willison also wrote, in the same closing commentary,
  "That was a creative solution to the environmental limits posed by Claude
  Code for web" — immediately preceding the quoted sentence above. Taken
  together, this is editorial praise for autonomous problem-solving, not a
  safety-relevant claim; it is worth noting for the guide's agentic-behavior
  material precisely because "proactive" workarounds are a double-edged
  pattern — the same willingness to route around a missing capability by
  reaching for other infrastructure (here, spinning up a temporary CI
  workflow) is the mechanism underlying failure modes documented elsewhere in
  the corpus (e.g., agents that route around a stated "no network access"
  constraint). This source treats the behavior as unambiguously positive
  because Willison, the task's author, approved of and expected exploratory
  latitude; the guide should note that the same behavior in a
  less-supervised or lower-trust context is the pattern flagged as a risk in
  `blog-simonwillison-meta-muse-spark-cyberattack.md` and Ch06's existing
  "gap between stated design and environment as actually provisioned"
  discussion.

## Concrete Artifacts

### Vendor claim vs. measured cold boot time (from linked repo `notes.md`)
```
Vendor claim: "Claims: boots <200ms, network disabled by default, host allowlists, `.smolmachine`"
Measured:     "T1 cold boot from local alpine tar: 643/580/577/591/588 ms end-to-end."
Source: linked GitHub research repo, smolmachines-untrusted-sandbox/notes.md
```

### Recommended production sandbox configuration (from post / linked repo `_summary.md`)
```
--cpus 1 --mem 512 --storage 3 --timeout 30s --unprivileged
/in  → mounted read-only
/out → mounted read-write

Deployment pattern: one ephemeral `machine run` per task,
or persistent/forked VM pools for higher throughput.

HTTP API: unauthenticated by default — restrict to a Unix socket
with filesystem permissions.

Source: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
(reproducing smolmachines-untrusted-sandbox/_summary.md)
```

### Test battery result summary (from linked repo `notes.md`)
```
PASS=12 FAIL=2 of 14.

Failures:
  - `--overlay` does not limit root filesystem writes (use `--storage` instead)
  - HTTP API requires camelCase `timeoutSecs`, silently ignores snake_case

Adversarial test example:
  T7 fork bomb: returned in 1s rc=2 (guest sh dies), host load 0.69.

Source: linked GitHub research repo, smolmachines-untrusted-sandbox/notes.md
```

### Environment description and pivot (verbatim from the blog post)
```
"This Claude Code container: Linux 6.18.5-fc-v20 (itself a Firecracker guest), 4 vCPU, 15GB RAM."
"No /dev/kvm, no vmx/svm CPU flags → no nested virt."
"GitHub Actions ubuntu runners DO expose /dev/kvm → run the real test battery
via a temporary workflow on this branch, collect logs, remove workflow in
final commit."

Source: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agent-runtimes-reference.md` Claim 2 (gh-aw's runtime-selection
    priority order uses "Docker sbx" — a KVM-based microVM runtime — "when the
    user requires a hardware-virtualized boundary and the runner exposes
    working KVM"): this source corroborates that KVM/nested-virtualization
    availability is the practical gating factor for hardware-VM sandboxing in
    general, not something specific to gh-aw's tooling — the same constraint
    (needs `/dev/kvm`, unavailable inside Willison's own already-virtualized
    Claude Code container) blocked smolvm testing here.
  - `blog-anthropic-how-contain-claude.md` Claim 14 ("Battle-tested
    infrastructure primitives...have survived more adversarial attention than
    anything you'll build"): this source's endorsement of a
    libkrun/Firecracker-based VM primitive (Claim 1, Claim 7) over
    custom sandboxing logic is a second, independent instance of preferring
    an established isolation primitive.
  - `blog-google-adk-zero-trust-agents.md` Claim 7 (a minimal, specific
    `docker run --runtime=runsc --network=none --cap-drop=ALL --memory=64m
    --cpus=0.1` recipe for sandboxing LLM-generated code): this source's
    recommended smolvm configuration (Claim 5: `--cpus 1 --mem 512 --storage 3
    --timeout 30s --unprivileged`, `/in` read-only, `/out` read-write)
    corroborates the same underlying pattern — minimal CPU/memory, no network
    by default, explicit timeout, capability-dropped/unprivileged execution —
    at the VM isolation tier rather than the kernel (gVisor) isolation tier.

- **Contradicts**: None filed. The gap between smolvm's own advertised
  boot-time claim (<200ms) and the measured figures in this same source
  (577–643ms, Claim 9) is an internal vendor-claim-vs.-measurement
  discrepancy, not a disagreement between this source and any existing
  corpus source note — no other source note makes a competing claim about
  smolvm's boot performance. It does not meet the MINER.md §4a filing bar
  (a materially opposing claim between two corpus sources, or a source
  disagreeing with itself); it is captured here as an "Our assessment" note
  under Claim 9 instead.

- **Extends**:
  - `docs-ghaw-agent-runtimes-reference.md`: that note documents gh-aw's
    "Docker sbx" KVM-microVM runtime option but its own Claim 2 assessment
    explicitly flags that "no cost or latency comparison across the three
    tiers is documented yet in the corpus." This source does not benchmark
    gh-aw's specific runtimes, but it supplies the first concrete
    cold-start/warm-execution numbers in the corpus for a comparable
    KVM-based hardware-VM sandbox class (0.6–1.5s cold, ~50ms warm),
    partially filling that documented gap for the broader hardware-VM
    isolation category.
  - `blog-anthropic-how-contain-claude.md` Claim 5 (claude.ai runs code in
    ephemeral gVisor containers on isolated infrastructure): this source adds
    a stronger-than-gVisor isolation option (hardware VM via libkrun) with
    concrete performance numbers, for teams whose threat model or blast-radius
    tolerance requires VM-level rather than kernel-level isolation for
    untrusted, agent-triggered code execution.
  - Ch06's existing "No internet access is a claim to verify, not a design to
    trust" discussion (sourced from
    `blog-simonwillison-meta-muse-spark-cyberattack.md`): this source
    provides a second, independent instance of the same "verify vendor/design
    claims empirically" discipline, applied to sandbox boot-time performance
    rather than network-isolation configuration.

- **Novel**:
  - **smolvm / smolmachines and libkrun**: no existing corpus source
    mentions smolvm, smolmachines.com, or libkrun as a sandboxing VMM. This
    is the first source in the corpus for this specific tool.
  - **Concrete cold-start (0.6–1.5s / 577–643ms measured) and warm-execution
    (~50ms) figures for a Firecracker/libkrun-class VM sandbox**: no existing
    source note has comparable timing data for this isolation tier.
  - **Fork-bomb containment test result** (Claim 10): no existing corpus
    source documents an adversarial resource-exhaustion test against any
    sandbox technology; this is the first.
  - **An agent's own execution container being a Firecracker guest, and that
    fact blocking nested-virtualization-dependent testing** (Claim 11): new
    to the corpus — a concrete, specific instance of an agent's execution
    environment constraining what it can test or deploy, and the workaround
    used (Claim 12).
  - **Vendor boot-time claim vs. measured discrepancy within a single AI-authored
    research report** (Claim 9): a new concrete example, for the guide's
    "verify, don't trust" material, of an AI agent's own testing surfacing a
    gap between a tool's marketing claim and its measured behavior.

## Guide Impact

- **Chapter 06 (Security & Threat Model), "The Sandbox Is the Control — Even
  When Someone Else Runs It" section (~lines 341–393)**: Add smolvm/libkrun as
  a concrete example of the hardware-VM isolation tier, alongside the
  existing gVisor (`blog-google-adk-zero-trust-agents.md`) and Docker sbx
  (`docs-ghaw-agent-runtimes-reference.md`) references, with the first
  concrete performance numbers in the corpus for this tier (0.6–1.5s cold
  start, ~50ms warm). Extend the existing "verify, don't trust the design
  document" rule (currently framed around network-isolation claims from the
  Meta/Anthropic evaluation-vendor incidents) with the smolvm boot-time
  example (Claim 9: vendor claims <200ms, measured 577–643ms) — this is a
  concrete instance of the same discipline applied to a performance claim
  rather than a security-boundary claim, and it comes from a source that
  otherwise recommends the tool, showing the discipline applies even when
  the overall verdict is positive.

- **Chapter 02 (Harness Engineering)**: Add the finding that Claude Code for
  web's own execution container is itself a Firecracker guest (Claim 11) and
  therefore cannot run nested hardware-VM sandboxes without leaving that
  environment (Claim 12's GitHub Actions pivot). Practitioners planning to
  test or deploy KVM/Firecracker/libkrun-based sandboxes as part of an agent
  harness should not assume the agent's own runtime supports nested
  virtualization — this should be checked explicitly (`/dev/kvm` presence,
  vmx/svm CPU flags) and, if absent, a separate KVM-capable execution target
  (e.g., GitHub Actions Ubuntu runners, which do expose `/dev/kvm`) should be
  provisioned.

- **Chapter 02 (Harness Engineering)**: Add the resource-limit recipe from
  Claim 5 (`--cpus 1 --mem 512 --storage 3 --timeout 30s --unprivileged`,
  read-only input / read-write output mounts) as a directly reusable default
  for teams standing up a hardware-VM sandbox for agent-triggered code
  execution, alongside the existing gVisor `docker run` recipe already cited
  from `blog-google-adk-zero-trust-agents.md`.

## Extraction Notes

- The primary source URL (the blog post) refused full verbatim reproduction
  via WebFetch on copyright grounds but consistently returned short (<125
  character) verbatim quotes on request, across five separate targeted
  fetches. All quotes attributed directly to "the post" or "the blog post
  body" in this note (Claims 1–6, 11–13, and the environment/pivot artifact
  block) were returned from fetches against the blog post URL itself
  (`https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/`).
- The post links to, and appears to substantially reproduce content from, a
  GitHub research repo at
  `https://github.com/simonw/research/tree/main/smolmachines-untrusted-sandbox`.
  The repo's `_summary.md` file was confirmed, via a separate raw-file fetch,
  to be reproduced verbatim in the blog post itself (the summary sentences in
  Claims 1–6 matched exactly between both fetches). The repo's `notes.md`
  file (granular per-test results: Claims 7–10) was fetched separately from
  its raw GitHub URL and its exact wording was **not** independently
  confirmed to appear on the blog post page itself — the WebFetch tool
  declined full verbatim reproduction of `notes.md` on two attempts, only
  yielding short quoted fragments. Claims 7–10 are marked accordingly in
  their Evidence field so the Assayer knows to spot-check those quotes
  against the linked GitHub repo's `notes.md`, not only against the blog post
  URL in this note's frontmatter.
- I did not fetch or verify `README.md`, `results-round1.log`,
  `results-round2.log`, `run-tests.sh`, `run-tests-round2.sh`, or
  `sandbox-run.sh` beyond the summarized descriptions WebFetch returned (it
  declined verbatim reproduction of these files as well); no direct quotes
  from those files are used in this note. The `sandbox-run.sh` content
  described in tool output (language selection, memory/CPU/timeout/storage
  defaults, dual guest+host timeout) is consistent with, and not additional
  to, the recommended configuration already captured verbatim in Claim 5, so
  it was not separately extracted as its own claim.
- No paywall or access issues. Both the blog post and the linked GitHub repo
  are public.
- No contradiction issue filed — see Cross-References → Contradicts.
