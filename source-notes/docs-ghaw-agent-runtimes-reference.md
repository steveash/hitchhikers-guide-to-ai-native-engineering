---
source_url: https://github.github.com/gh-aw/reference/agent-runtimes
source_type: docs
title: "Agent Runtime Selection"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-09
last_checked: 2026-08-09
status: current
confidence_overall: settled
issue: "#2592"
---

# Agent Runtime Selection

> The authoritative reference for choosing among gh-aw's four agent isolation
> options — Docker (default), gVisor, Docker sbx (KVM microVM), and ARC
> Docker-in-Docker — with per-runtime runner requirements, tradeoffs,
> mutual-exclusion rules, and troubleshooting guidance.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/agent-runtimes`
  page — in the "Reference" section alongside `reference/sandbox`,
  `reference/network`, `reference/self-hosted-runners`. The page's own
  breadcrumb nav shows it nested under "Sandbox (Agent Runtimes)".)
- **Author credibility**: First-party from GitHub Next / Microsoft Research,
  the team behind `gh aw` and its documentation site. Configuration field
  names, generated setup-step behavior, and mutual-exclusion rules are
  authoritative platform specifications, not third-party observation.
- **Scope**: How to select and configure `sandbox.agent.runtime` (Docker,
  gVisor, Docker sbx) and `runner.topology: arc-dind`; per-runtime runner
  prerequisites, tradeoffs, and troubleshooting; the distinction between
  `sandbox.agent.runtime`, `runner.topology`, `sandbox.agent.runtime-install`,
  and `tools.github.bounded-queries.runtime`. Does NOT cover: the AWF
  filesystem/environment-variable sandbox model in depth (see
  `docs-ghaw-sandbox-reference.md`), network egress/domain allowlisting (see
  `docs-ghaw-guides-network-configuration.md`), or the full self-hosted-runner
  provisioning reference (linked but not itself mined in this note).

## Extracted Claims

### Claim 1: `sandbox.agent.runtime`, `runner.topology`, `sandbox.agent.runtime-install`, and `tools.github.bounded-queries.runtime` are four distinct, easily-confused frontmatter fields that control different layers of agent execution

- **Evidence**: A field-purpose-values table lists all four fields side by
  side, plus a fifth unrelated field `runtimes` (language toolchain
  installation). The page opens by stating ARC DinD "is a runner topology
  that changes how the standard Docker environment is reached; it is not
  another value of `sandbox.agent.runtime`."
- **Confidence**: settled (first-party reference; the field table is a
  platform specification)
- **Quote**: "Agentic workflows use AWF (Agent Workflow Firewall) to run the agent in an isolated environment. The environment can use the runner’s standard Docker runtime, gVisor, or Docker sbx. ARC DinD is a runner topology that changes how the standard Docker environment is reached; it is not another value of `sandbox.agent.runtime`."
- **Our assessment**: This distinction resolves a real confusion risk:
  `sandbox.agent.runtime` selects the isolation *backend* (what wraps the
  agent process), while `runner.topology` selects the Docker daemon
  *reachability model* (local socket vs. DinD sidecar). Conflating them is
  exactly the mistake the page repeatedly warns against (see Claims 5, 7, 8).
  `docs-ghaw-sandbox-reference.md` (extracted 2026-05-12) predates this
  runtime-selector field entirely and only documents `sandbox.agent: awf` or
  `false`; `blog-ghaw-weekly-2026-07-13.md` Claims 1 and 6 first reported
  gVisor and docker-sbx as new PR-level changelog items without the field
  taxonomy. This page is the first source to lay out all four fields in one
  authoritative table.

### Claim 2: The page recommends a strict priority order for runtime selection: ARC DinD if the runner is a Kubernetes DinD pod, else Docker sbx if KVM is available, else gVisor if isolation is warranted, else default to Docker

- **Evidence**: A four-step "Apply this selection order" list, followed by an
  explicit default-to-Docker instruction when requirements are unclear.
- **Confidence**: settled (first-party prescriptive guidance, stated as an
  ordered procedure)
- **Quote**: "1. Use **ARC DinD** when the runner is an ARC pod or another Kubernetes runner whose Docker daemon is a DinD sidecar. Do not combine it with gVisor or Docker sbx. 2. Otherwise, use **Docker sbx** when the user requires a hardware-virtualized boundary and the runner exposes working KVM. 3. Otherwise, use **gVisor** when untrusted agent code warrants a smaller host-kernel attack surface and the workload is compatible with `runsc`. 4. Use the default **Docker** runtime when compatibility, startup time, or runner portability is more important than an additional kernel or VM boundary."
- **Our assessment**: This is a genuine decision framework, not just an
  enumeration — `blog-ghaw-weekly-2026-07-13.md` Claim 6's assessment
  explicitly flagged that "no cost or latency comparison across the three
  tiers is documented yet in the corpus." This page still gives no
  quantitative cost/latency numbers, but it does supply the qualitative
  decision procedure that weekly note was missing: topology constraint first
  (ARC DinD is infrastructure-driven, not a choice), then strongest available
  isolation (Docker sbx), then a lighter kernel-isolation tier (gVisor),
  defaulting to Docker. The explicit "prefer Docker...do not select a
  stronger runtime until the runner prerequisites are known to be available"
  guidance is risk-averse: it discourages speculative hardening.

### Claim 3: Docker sbx cannot be combined with `runner.topology: arc-dind` because ARC DinD does not expose nested KVM and the sbx daemon must run on the runner host, not inside the DinD sidecar

- **Evidence**: A standalone caution statement in the Docker sbx section.
- **Confidence**: settled (first-party documentation of a hard incompatibility)
- **Quote**: "Docker sbx cannot be combined with `runner.topology: arc-dind`. ARC DinD normally does not expose nested KVM, and the sbx daemon must run on the runner host rather than inside the DinD sidecar."
- **Our assessment**: This is a concrete, checkable incompatibility rule a
  harness engineer needs before provisioning infrastructure — choosing ARC
  DinD for Kubernetes-fleet reasons silently forecloses the strongest
  isolation tier (Docker sbx). Combined with Claim 4 (gVisor also
  incompatible with ARC DinD), the page establishes that ARC DinD workflows
  are locked to standard Docker isolation; there is no path to stronger
  per-agent isolation on that topology.

### Claim 4: gVisor cannot be combined with `runner.topology: arc-dind` because the generated installer must register `runsc` with the same Docker daemon that starts the agent and restart that daemon via systemd, which an ARC runner cannot do against its DinD sidecar

- **Evidence**: Standalone caution statement in the gVisor section,
  consistent with the generated-setup-step list (Claim 6) that requires
  `sudo systemctl restart docker`.
- **Confidence**: settled (first-party documentation of a hard incompatibility)
- **Quote**: "gVisor cannot be combined with `runner.topology: arc-dind`. The generated installer must register `runsc` with the same Docker daemon that starts the agent and restart that daemon through systemd. An ARC runner cannot perform those operations against its DinD sidecar."
- **Our assessment**: The stated reason is mechanistic, not policy — the
  gVisor installer's `systemctl restart docker` step has no meaning against a
  DinD sidecar it doesn't control. This corroborates Claim 3's pattern: both
  non-default runtimes require host-level control the ARC DinD topology
  structurally withholds from the runner container.

### Claim 5: Compilation-generated gVisor installation requires host-level `sudo`, but `sandbox.agent.sudo: true` is a different field that is not required and, if set, is rejected in strict mode

- **Evidence**: A "Caution" callout distinguishing runner-provisioning sudo
  from the agent-security-mode sudo field.
- **Confidence**: settled (first-party documentation explicitly warning
  against a specific misconfiguration)
- **Quote**: "Host-level `sudo` is required by the generated gVisor installation step, but `sandbox.agent.sudo: true` is not required. Leave that field omitted or false to retain AWF’s default network-isolation mode. Setting it to true changes the agent security mode and is rejected in strict mode."
- **Our assessment**: This is a specific, named foot-gun: the field names are
  similar enough (`sudo` at the runner-provisioning level vs.
  `sandbox.agent.sudo` at the agent-security level) that a practitioner
  debugging a gVisor `sudo` failure could reasonably reach for
  `sandbox.agent.sudo: true` and instead trigger a strict-mode rejection.
  This directly parallels the page's closing troubleshooting principle
  (Claim 14) — don't reach for `sandbox.agent.sudo` to patch a missing host
  capability.

### Claim 6: The generated gVisor setup step follows a fixed six-step sequence — architecture detection, pinned-binary download with SHA-512 verification, sudo install, `runsc install` + `systemctl restart docker`, and a smoke test

- **Evidence**: A numbered six-item list describing exactly what the
  generated CI step does.
- **Confidence**: settled (first-party documentation of the generated
  installer's exact behavior)
- **Quote**: (no single contiguous prose sentence; see the six-step
  procedure in Concrete Artifacts, copied verbatim from the source's ordered
  list)
- **Our assessment**: Documenting the generated step's exact behavior lets a
  harness engineer reason about failure points precisely instead of treating
  the installer as a black box — e.g., a download failure implicates step 2
  (network access to `storage.googleapis.com/gvisor`), while an "unknown
  runtime name" error implicates step 5 (`runsc install` / daemon restart),
  matching the troubleshooting table (Claim 9) one-to-one.

### Claim 7: `runtime-install: false` lets a pre-provisioned runner skip the generated installer for gVisor or Docker sbx, but Docker sbx still requires `DOCKER_USERNAME`/`DOCKER_PAT` secrets even with installation disabled, because credentials are refreshed immediately before every agent run

- **Evidence**: Separate statements for each runtime. For gVisor:
  "`runtime-install: false`... skips the generated download, checksum,
  installation, Docker registration, restart, and smoke-test step. The
  runner no longer needs workflow-time `sudo`, systemd, or access to the
  gVisor download host, but `docker info` must already list `runsc`." For
  Docker sbx: "`DOCKER_PAT` is required for Docker sbx, including when
  `runtime-install: false`, because the compiled workflow refreshes sbx
  credentials immediately before agent execution."
- **Confidence**: settled (first-party documentation of the flag's exact
  scope per runtime)
- **Quote**: "`DOCKER_PAT` is required for Docker sbx, including when `runtime-install: false`, because the compiled workflow refreshes sbx credentials immediately before agent execution."
- **Our assessment**: The asymmetry is the interesting part: for gVisor,
  `runtime-install: false` removes *all* workflow-time requirements tied to
  installation (sudo, systemd, network access to the download host); for
  Docker sbx, it removes the installation checks but the credential-refresh
  step survives independently, so `DOCKER_USERNAME`/`DOCKER_PAT` remain a
  hard requirement regardless of the flag. A practitioner who sets
  `runtime-install: false` on Docker sbx expecting to shed the Docker Hub
  secret requirement will be wrong. This connects to
  `blog-ghaw-weekly-2026-07-13.md` Claim 7, which documented a related
  credential-lifecycle bug (Docker Hub OAuth token expiry between daemon
  setup and agent run, fixed in PR #45146 by running `sbx login` immediately
  before agent execution) — this page's "refreshes sbx credentials
  immediately before agent execution" statement is the current, post-fix
  behavior that PR produced.

### Claim 8: ARC DinD forbids setting any `sandbox.agent.runtime` value — there is no explicit `docker` runtime value, and the field must be omitted entirely for this topology

- **Evidence**: Direct instruction in the ARC DinD section, following the
  workflow YAML example that omits `sandbox:` entirely and sets only
  `runner: topology: arc-dind`.
- **Confidence**: settled (first-party documentation of required frontmatter
  shape)
- **Quote**: "Do not set `runtime: docker`, `runtime: gvisor`, or `runtime: docker-sbx` in this configuration. There is no explicit `docker` value for `sandbox.agent.runtime`."
- **Our assessment**: This closes a plausible authoring mistake — a
  practitioner might reasonably try to write `runtime: docker` explicitly to
  "confirm" the default under ARC DinD, but the field has no such value; the
  correct configuration is to omit `sandbox.agent.runtime` and set only
  `runner.topology: arc-dind`. This is consistent with Claims 3 and 4
  (ARC DinD is exclusive with the two non-default runtimes) — together, ARC
  DinD's only valid runtime posture is "no `sandbox.agent.runtime` set at
  all."

### Claim 9: ARC DinD requires an unprivileged runner container with a separately privileged DinD sidecar, a shared `/home/runner/_work` volume, `DOCKER_HOST` pointed at the sidecar's TCP endpoint, and forbids `sudo`/`apt install` anywhere in workflow steps

- **Evidence**: A seven-item runner-requirements list for the ARC/Kubernetes
  pod.
- **Confidence**: settled (first-party documentation of runner prerequisites)
- **Quote**: "An unprivileged runner container; only the DinD sidecar needs `privileged: true`."
- **Our assessment**: The "unprivileged runner, privileged sidecar only"
  design is the security rationale for choosing ARC DinD at all — it lets an
  organization run agentic workflows on Kubernetes without granting the
  runner container itself elevated privilege, at the cost of routing all
  Docker operations through a separate privileged sidecar (named explicitly
  as "a significant infrastructure trust boundary" in Claim 12). The
  no-`sudo`/no-`apt install` rule in workflow steps is a compile-time
  validation constraint, not just a recommendation (see Claim 13).

### Claim 10: Docker sbx omits TTY mode because sbx TTY execution can prematurely terminate long-running agent sessions — a concrete, named microVM behavioral difference from standard Docker

- **Evidence**: Stated as an example within the Docker sbx tradeoffs
  paragraph, immediately after listing path/networking/CLI-installation
  differences.
- **Confidence**: settled (first-party documentation naming a specific
  platform workaround)
- **Quote**: "For example, gh-aw omits TTY mode for Docker sbx because sbx TTY execution can terminate long-running sessions prematurely."
- **Our assessment**: This is a narrow but concrete artifact: it is evidence
  that the strongest-isolation runtime (Docker sbx) has behavioral quirks
  beyond raw overhead — a naive assumption that "Docker sbx behaves like
  Docker but slower" would miss this TTY-mode omission entirely. It also
  implies gh-aw's compiler makes runtime-specific code-generation decisions
  (omitting TTY flags) rather than treating all runtimes as interchangeable
  behind one execution path.

### Claim 11: Docker sbx secrets are unavailable on workflows triggered from untrusted forks, making Docker sbx unsuitable for fork-triggered runs unless the trigger and credential model are changed

- **Evidence**: Stated in the Docker sbx troubleshooting section under the
  `DOCKER_PAT`/`DOCKER_USERNAME`-empty failure mode.
- **Confidence**: settled (first-party documentation; consistent with
  standard GitHub Actions fork-secret behavior)
- **Quote**: "Secrets are not passed to workflows triggered from untrusted forks, so Docker sbx is unsuitable for such runs unless the trigger and credential model are changed safely."
- **Our assessment**: This connects a general GitHub Actions security
  property (forked-PR workflows don't receive repository secrets) to a
  specific runtime-selection consequence: any agentic workflow that needs to
  run against untrusted-fork PRs (e.g., an automated PR reviewer) cannot use
  Docker sbx as configured by default. For such workflows, the choice
  narrows to Docker, gVisor, or a `pull_request_target`-style trusted trigger
  with its own separate security tradeoffs (not covered on this page).

### Claim 12: ARC DinD's tradeoff is explicitly framed as infrastructure necessity, not an isolation upgrade — "Choose ARC DinD because the runner platform requires it, not as an isolation upgrade over Docker"

- **Evidence**: Closing sentence of the ARC DinD tradeoffs subsection,
  following a description of the privileged sidecar as a trust boundary and
  the added filesystem/caching complexity.
- **Confidence**: settled (first-party prescriptive framing)
- **Quote**: "Choose ARC DinD because the runner platform requires it, not as an isolation upgrade over Docker."
- **Our assessment**: This is a corrective against a plausible
  misunderstanding — since ARC DinD sits in the same "four runtime options"
  frame as gVisor and Docker sbx, a reader could assume it forms a security
  gradient alongside them. The page explicitly denies this: ARC DinD's agent
  isolation is identical to standard Docker (Claim 8 — no runtime value is
  even set); its only benefit is Kubernetes-fleet compatibility, at the cost
  of a privileged sidecar trust boundary and filesystem-splitting complexity
  (Claim 9). For a harness engineer, this reframes the earlier four-way
  comparison table: it is really "three isolation tiers (Docker / gVisor /
  Docker sbx) × two topologies (local daemon / ARC DinD sidecar)," with ARC
  DinD compatible only with the Docker tier.

### Claim 13: gVisor and Docker sbx workloads can fail for reasons unrelated to configuration — unsupported syscalls, devices, eBPF behavior, or `/proc`/`/sys` semantics — and the page recommends reproducing failures directly against the runtime backend before investigating AWF

- **Evidence**: gVisor tradeoffs: "Some low-level workloads can fail because
  they depend on an unsupported syscall, privileged operation, device,
  kernel module, eBPF behavior, unusual `/proc` or `/sys` semantics, or exact
  host-kernel behavior." Troubleshooting: "**Tests fail only under gVisor:**
  Treat this as a compatibility issue if the failure involves syscalls,
  devices, namespaces, tracing, eBPF, or kernel-specific filesystem behavior.
  Reproduce with `docker run --runtime=runsc ...` and compare it with the
  same image under standard Docker."
- **Confidence**: settled (first-party documentation naming specific failure
  categories and a specific reproduction command)
- **Quote**: "Some low-level workloads can fail because they depend on an unsupported syscall, privileged operation, device, kernel module, eBPF behavior, unusual `/proc` or `/sys` semantics, or exact host-kernel behavior. Prefer Docker for kernel-sensitive build and test workloads unless the stronger boundary is required."
- **Our assessment**: This is a practical debugging heuristic worth
  preserving as-is: reproduce the failure with `docker run --runtime=runsc
  ...` directly, bypassing AWF and the agent entirely, before assuming the
  agentic-workflow layer is at fault. It also gives harness engineers a
  concrete pre-adoption check — a build or test suite with heavy eBPF,
  device, or `/proc` dependencies is a signal to default to Docker rather
  than gVisor, independent of the security-vs-compatibility framing in
  Claim 2.

### Claim 14: The page's closing troubleshooting principle instructs engineers not to compensate for a missing host capability with extra agent mounts, manual AWF arguments, or `sandbox.agent.sudo` — the fix is the runner prerequisite or a different runtime, not a workaround

- **Evidence**: Final sentence of the "Debug in dependency order" section,
  following a six-step ordered debugging procedure (verify runner OS/arch →
  verify Docker → verify specialized backend → confirm frontmatter/compile →
  inspect lock file → inspect AWF logs).
- **Confidence**: settled (first-party prescriptive guidance stated as an
  explicit principle)
- **Quote**: "Do not compensate for a missing host capability with extra agent mounts, manual AWF arguments, or `sandbox.agent.sudo`. Fix the runner prerequisite or select a compatible runtime."
- **Our assessment**: This is the page's central operational philosophy,
  restated from Claim 5's specific `sandbox.agent.sudo` warning to a general
  rule: security-relevant configuration fields (mounts, AWF arguments, sudo)
  should never be used as a substitute for correct runner provisioning. This
  is a harness-engineering discipline worth generalizing beyond gh-aw — the
  pattern "if a specialized isolation backend is failing, don't loosen the
  isolation to make the symptom go away" applies to any agent sandboxing
  system, not just AWF specifically.

## Concrete Artifacts

### Field Purpose Table (verbatim from source)

```
| Field                                  | Purpose                                                          | Values covered here                          |
|-----------------------------------------|-------------------------------------------------------------------|-----------------------------------------------|
| sandbox.agent.runtime                   | Selects the isolation backend for the main agent                 | gvisor, docker-sbx, or omitted for Docker     |
| sandbox.agent.runtime-install           | Controls whether gh-aw installs and prepares gVisor or Docker sbx | true by default; false for a pre-provisioned runner |
| runner.topology                         | Describes how the runner reaches Docker                          | arc-dind, or omitted for a local Docker daemon |
| tools.github.bounded-queries.runtime    | Selects the backend for bounded-query scripts only                | docker, gvisor, sbx                           |
| runtimes                                | Installs language toolchains such as Node.js, Python, and Go      | Unrelated to agent isolation                  |
```

*Source: `https://github.github.com/gh-aw/reference/agent-runtimes` — "Runtime and topology fields" section*

### Choose-a-Runtime Comparison Table (verbatim from source)

```
| Choice     | Isolation boundary                                          | Runner requirements                                                        | Main tradeoff                                                                    |
|------------|--------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Docker     | Linux namespaces, cgroups, and the host kernel                | Linux and a usable Docker daemon                                             | Fastest and most compatible, but the agent shares the host kernel                 |
| gVisor     | A runsc user-space kernel between the agent and host kernel    | Local Docker daemon, sudo, systemd, and access to gVisor downloads           | Stronger kernel isolation with syscall compatibility and performance overhead      |
| Docker sbx | A KVM-backed microVM for the agent                             | KVM, nested virtualization, sudo, apt, Docker Hub credentials, and local Docker | Strongest boundary here, but has the most setup cost and platform constraints    |
| ARC DinD   | Standard Docker agent container in a DinD sidecar               | ARC or equivalent Kubernetes runner with a privileged DinD sidecar and shared work volume | Supports Kubernetes runner fleets, but adds split-filesystem and daemon-connectivity complexity |
```

*Source: `https://github.github.com/gh-aw/reference/agent-runtimes` — "Choose a runtime" section*

### Generated gVisor Setup Step (verbatim ordered list)

```
1. Detects x86_64 or aarch64 with `uname -m`.
2. Downloads pinned `runsc` and `containerd-shim-runsc-v1` binaries and their
   SHA-512 files from `storage.googleapis.com/gvisor`.
3. Verifies both checksums.
4. Uses `sudo` to install the binaries under `/usr/local/bin`.
5. Runs `sudo runsc install` and `sudo systemctl restart docker`.
6. Verifies the runtime with `docker run --rm --runtime=runsc hello-world`.
```

*Source: `https://github.github.com/gh-aw/reference/agent-runtimes` — "gVisor runner requirements" section*

### Frontmatter Examples per Runtime (verbatim from source)

```yaml
# Docker (default) — sandbox block may be omitted entirely
---
on: issues
sandbox:
  agent:
    id: awf
---
Investigate this issue.
```

```yaml
# gVisor
---
on: issues
sandbox:
  agent:
    id: awf
    runtime: gvisor
---
Investigate this issue.
```

```yaml
# gVisor with runtime-install disabled (pre-provisioned runner)
---
sandbox:
  agent:
    id: awf
    runtime: gvisor
    runtime-install: false
---
```

```yaml
# Docker sbx
---
on: issues
sandbox:
  agent:
    id: awf
    runtime: docker-sbx
    sudo: true
---
Investigate this issue.
```

```yaml
# ARC DinD — sandbox.agent.runtime omitted entirely
---
on: issues
runs-on: arc-runner-set
runner:
  topology: arc-dind
---
Investigate this issue.
```

```yaml
# Bounded-query runtime (separate from sandbox.agent.runtime)
---
tools:
  github:
    bounded-queries:
      runtime: gvisor # docker, gvisor, or sbx
---
```

*Source: `https://github.github.com/gh-aw/reference/agent-runtimes` — Docker, gVisor, Docker sbx, ARC DinD, and Bounded-query runtime-names sections*

### Debug-in-Dependency-Order Procedure (verbatim ordered list)

```
1. Verify the runner operating system, architecture, disk, memory, and
   required privilege.
2. Verify Docker independently with `docker version`, `docker info`,
   `docker compose version`, and `docker run --rm hello-world`.
3. Verify the specialized backend independently: `docker run
   --runtime=runsc ...` for gVisor, `sbx create` and `sbx exec` for Docker
   sbx, or Docker API access through `DOCKER_HOST` for ARC DinD.
4. Confirm the frontmatter uses the correct field and value, then run
   `gh aw compile`.
5. Inspect the generated lock file for the expected setup and pre-flight
   steps.
6. Inspect AWF logs. Conventional runners use
   `/tmp/gh-aw/sandbox/firewall/logs/`; ARC DinD uses
   `$RUNNER_TEMP/gh-aw/sandbox/firewall/logs/`.
```

*Source: `https://github.github.com/gh-aw/reference/agent-runtimes` — "Debug in dependency order" section*

### Docker Hub Secrets Required for Docker sbx (verbatim table)

```
| Secret          | Purpose                                                        |
|------------------|-----------------------------------------------------------------|
| DOCKER_USERNAME  | Docker Hub account used by both the Docker and sbx CLIs         |
| DOCKER_PAT       | Docker Hub personal access token used to pull the sandbox template |
```

*Source: `https://github.github.com/gh-aw/reference/agent-runtimes` — "Docker sbx" section*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-07-13.md` Claim 1 (gVisor runtime, PR #44796,
    `sandbox.agent.runtime: gvisor`) and Claim 6 (docker-sbx runtime, PR
    #45006, `sandbox.agent.runtime: docker-sbx`): this reference page
    confirms both runtime names, the field path, and the "stronger isolation
    for untrusted input" framing that weekly note extracted from the
    changelog. This page is the durable reference; that note is the
    changelog announcement.
  - `blog-ghaw-weekly-2026-07-13.md` Claim 7 (Docker Hub OAuth token expiry
    fix, PR #45146, fresh `sbx login` immediately before agent execution):
    Claim 7 of this note ("the compiled workflow refreshes sbx credentials
    immediately before agent execution") describes the current, resulting
    behavior of that fix as now-documented, stable platform behavior.
  - `docs-ghaw-sandbox-reference.md` Claim 2 (AWF is the default coding
    agent sandbox providing network egress control): this page's Docker
    section statement "AWF still provides network isolation and proxy
    enforcement; 'Docker' does not mean that the agent runs without a
    sandbox" confirms that even the default runtime keeps the AWF network
    layer from that note active — runtime selection and AWF's network/
    filesystem sandbox (Claims 2 and 4 of `docs-ghaw-sandbox-reference.md`)
    are orthogonal, composable layers, not alternatives.

- **Contradicts**: None identified. This page's qualitative isolation
  ranking (Docker weakest/fastest → gVisor moderate → Docker sbx
  strongest/slowest) does not conflict with any existing note. It also does
  not resolve the quantitative cost/latency gap that
  `blog-ghaw-weekly-2026-07-13.md` Claim 6's assessment flagged as
  unverified — no benchmark numbers appear on this page either, so that gap
  remains open. No contradiction issue filed.

- **Extends**:
  - `docs-ghaw-sandbox-reference.md`: that note's `sandbox.agent` field
    documentation (Claim 1: defaults to `sandbox.agent: awf` when omitted;
    Claim 3: `sandbox.agent: false` disables only the agent firewall), both
    extracted 2026-05-12, covers only the `awf`/`false` values — it predates
    the `runtime` sub-field entirely. This note supplies the full
    `sandbox.agent.runtime` taxonomy (`gvisor`/`docker-sbx`/omitted) plus the
    sibling `runtime-install` and `runner.topology` fields that reference did
    not and could not cover at its extraction date.
  - `blog-ghaw-weekly-2026-07-13.md` Claims 1 and 6: those changelog-level
    claims announced gVisor and docker-sbx as new options with brief
    "What's New" descriptions and flagged the missing cost/latency
    comparison and missing "internal implementation" detail as explicit
    scope gaps. This note fills the implementation gap substantially: full
    runner requirement lists, the generated gVisor installer's exact
    six-step sequence, Docker sbx's credential-refresh mechanism, and the
    ARC DinD mutual-exclusion rules for both. The cost/latency comparison
    gap remains unfilled by any source in the corpus.
  - `docs-ghaw-guides-network-configuration.md`: that guide documents
    `network.allowed` domain allowlisting; this page's shared-requirements
    section adds the runtime-specific outbound-access prerequisites
    (`storage.googleapis.com/gvisor` for gVisor; `get.docker.com` and Docker
    Hub for Docker sbx) that a harness engineer must add to an allowlist
    before those runtimes will provision successfully — a concrete
    consequence not covered in that guide.

- **Novel** (nothing in the corpus previously covered these):
  - **The full four-runtime field taxonomy** (Claim 1) — the distinction
    between `sandbox.agent.runtime`, `runner.topology`,
    `sandbox.agent.runtime-install`, and `tools.github.bounded-queries.runtime`
    as four separate, commonly-confused fields.
  - **ARC (Actions Runner Controller) Docker-in-Docker as a runtime topology**
    (Claims 8, 9, 12) — no existing source note in the corpus mentions ARC
    DinD, `runner.topology`, or Kubernetes runner fleets for gh-aw agents at
    all. This is entirely new corpus content, including the explicit framing
    that ARC DinD is infrastructure necessity rather than an isolation
    upgrade (Claim 12).
  - **Runtime mutual-exclusion rules** (Claims 3, 4, 8) — gVisor × ARC DinD
    and Docker sbx × ARC DinD incompatibilities, and the "no explicit
    `docker` value" rule for ARC DinD, are new constraints not present
    anywhere else in the corpus.
  - **The `sandbox.agent.sudo` vs. host-level `sudo` foot-gun** (Claim 5) and
    the general "don't compensate with mounts/arguments/sudo" troubleshooting
    principle (Claim 14) — a specific, named misconfiguration risk and a
    generalizable harness-debugging discipline, both new to the corpus.
  - **Docker sbx TTY-mode omission** (Claim 10) and **fork-secret
    incompatibility** (Claim 11) — concrete, narrow platform behaviors not
    documented elsewhere.
  - **The ordered "debug in dependency order" procedure and generated
    gVisor installer's exact six-step sequence** (Claims 6, 13, 14) — first
    corpus source with this level of operational/debugging specificity for
    runtime provisioning failures.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "choosing an agent runtime"
  subsection using the four-way comparison table and the priority-ordered
  selection procedure (Claim 2) as the primary decision framework — this is
  more actionable than the prior corpus state, where
  `blog-ghaw-weekly-2026-07-13.md` only announced runtime names without
  guidance on when to pick each. Explicitly flag that no source yet supplies
  quantitative cost/latency numbers across the three isolation tiers,
  consistent with the existing gap noted in that weekly-update source note.
  Also add the `sandbox.agent.sudo` vs. host-`sudo` foot-gun (Claim 5) and
  the general debugging principle "fix the runner prerequisite or select a
  compatible runtime, don't patch around a missing capability" (Claim 14) as
  named harness-debugging guidance applicable beyond gh-aw specifically.

- **Chapter 03 (Safety and Verification)**: Extend the AWF security-model
  material (currently sourced from `docs-ghaw-how-they-work.md` Claim 3's
  five-layer pipeline and `docs-ghaw-sandbox-reference.md`'s filesystem-tier
  model) with the fact that "runtime isolation" is not a single mechanism —
  it is a selectable tier (Docker namespaces/cgroups → gVisor user-space
  kernel → Docker sbx hardware-virtualized microVM), each with a distinct
  security boundary and distinct compatibility cost. Add the explicit
  correction that ARC DinD is a topology choice, not a security upgrade
  (Claim 12) — teams evaluating ARC DinD for Kubernetes-fleet reasons should
  not assume they are also gaining isolation strength.

- **Chapter 02 or 05 (operational readiness)**: Add the Docker sbx
  fork-secret incompatibility (Claim 11) to any guidance about running
  agentic workflows against pull requests from forks — a team that adopts
  Docker sbx for its strongest-isolation properties and then tries to point
  it at a PR-review workflow triggered from forks will find secrets absent
  and the runtime non-functional as configured.

## Extraction Notes

1. **Verbatim text sourced from raw HTML, not the WebFetch AI-summarization
   tool.** An initial WebFetch pass returned plausible-looking but
   unverifiable prose (it renders through a summarizing model). To satisfy
   the verbatim-quote requirement, the page was re-fetched directly via
   `curl` (following the `github.com` → `github.github.com` redirect) and
   converted to text with `html2text`, then every `Quote` field above was
   copied character-for-character from that raw conversion, not from the
   WebFetch summary. Line numbers in the raw conversion were cross-checked
   against the rendered page structure (nav breadcrumbs, "On this page"
   table of contents) to confirm section boundaries.

2. **No linked sub-pages were followed as separate deep-reads.** The page
   links to `/gh-aw/reference/sandbox/`, `/gh-aw/reference/self-hosted-runners/`,
   and `/gh-aw/guides/arc-dind-copilot-agent/`. The first is already mined
   (`docs-ghaw-sandbox-reference.md`); the latter two were not fetched
   separately for this note — the agent-runtimes page's own troubleshooting
   and requirements sections were judged sufficiently self-contained for
   this note's scope, and the linked guide is ARC-specific rollout detail
   beyond the runtime-selection scope the Prospector's triage question asked
   about. A future source-submission for `guides/arc-dind-copilot-agent`
   would be a reasonable follow-up if ARC DinD rollout mechanics become
   relevant to the guide.

3. **No publication date on the page.** Astro/Starlight reference pages in
   this corpus consistently omit a visible publication date; `date_published`
   is left null, consistent with `docs-ghaw-sandbox-reference.md` and
   `docs-ghaw-how-they-work.md`.

4. **Confidence rated `settled` throughout**, higher than the `emerging`
   rating used for `docs-ghaw-how-they-work.md` and
   `docs-ghaw-sandbox-reference.md` (both rated `emerging` due to some
   experimental-feature content or single-page rendering uncertainty). This
   page contains no features marked experimental or beta, and its content
   (mutual-exclusion rules, generated setup steps, troubleshooting tables) is
   precise, mechanistic platform specification rather than architectural
   framing — the kind of content least likely to be materially wrong.

5. **No contradictions filed.** Reviewed `docs-ghaw-sandbox-reference.md`,
   `docs-ghaw-how-they-work.md`, `docs-ghaw-guides-network-configuration.md`,
   and all `blog-ghaw-weekly-*.md` notes that mention gVisor, docker-sbx, or
   ARC DinD. No claim in this source materially opposes an existing note at
   the MINER.md §4a filing threshold — this page consistently extends or
   corroborates prior corpus content rather than conflicting with it.
