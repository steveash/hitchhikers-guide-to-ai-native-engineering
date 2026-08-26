---
source_url: https://github.github.com/gh-aw/reference/arc-dind-copilot-agent
source_type: docs
title: "How to run GitHub Copilot coding agent on ARC with Docker-in-Docker"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: settled
issue: "#2977"
---

# How to run GitHub Copilot coding agent on ARC with Docker-in-Docker

> The operational deployment guide for running GitHub Copilot coding agent on
> Actions Runner Controller (ARC) with Docker-in-Docker (DinD): Helm install
> steps, required/optional configuration, tool-cache redirection, AWF log
> locations specific to this topology, a migration checklist away from manual
> workarounds, rootless installation for locked-down clusters, known
> limitations, and a symptom-keyed troubleshooting table.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/arc-dind-copilot-agent`
  page — in the "Reference" section, listed in the site nav as "Self-Hosted
  Runners (ARC DinD)" and positioned between "Self-Hosted Runners" and
  "Workflows" via the page's own Previous/Next links). Reference pages on
  this site document platform configuration and procedures authoritatively.
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind the `gh aw` CLI and its documentation site. Helm
  commands, minimum version numbers, generated-behavior descriptions, and
  troubleshooting fixes tied to specific PR/issue numbers are authoritative
  platform specifications, not third-party observation.
- **Scope**: How to stand up an ARC runner scale set in DinD mode and target
  it from a `gh-aw` workflow using `runner.topology: arc-dind`, specifically
  for GitHub Copilot coding agent; what the compiler and AWF do automatically
  at compile time vs. runtime when this topology is detected; network,
  logging, and tool-cache implications of the split runner/daemon filesystem;
  a migration path off manual pre-`arc-dind` workarounds; rootless install for
  clusters that block `sudo`; and a troubleshooting table for known failure
  modes. Does NOT cover: the general self-hosted-runner reference (`runs-on`
  formats, Docker socket overrides for other split-daemon topologies, GHES
  compatibility — explicitly deferred to a separate `reference/self-hosted-runners`
  page, not yet mined in this corpus); the ARC-DinD-vs-gVisor-vs-Docker-sbx
  runtime *selection* decision (covered by `docs-ghaw-agent-runtimes-reference.md`);
  or non-Copilot engines (this page is Copilot-specific, e.g. `install_copilot_cli.sh`,
  `copilot-setup-steps`).

## Extracted Claims

### Claim 1: DinD container mode is a hard requirement for GitHub Copilot coding agent on ARC — Kubernetes mode is explicitly unsupported for this setup

- **Evidence**: A "Caution" callout in the Prerequisites section, stated as
  an unconditional requirement before any setup steps.
- **Confidence**: settled (first-party documentation of a hard platform
  requirement)
- **Quote**: "DinD (`containerMode.type=\"dind\"`) is required for GitHub Copilot coding agent on ARC. Kubernetes mode (`containerMode.type=\"kubernetes\"`) is not supported for this setup."
- **Our assessment**: This forecloses a plausible alternative before a reader
  invests in provisioning — ARC's `containerMode.type="kubernetes"` (running
  each job step as its own pod, without a Docker daemon) is a real ARC
  configuration option in general, but not a valid choice for Copilot coding
  agent specifically. A harness engineer planning ARC infrastructure for
  Copilot workflows must select DinD mode from the start; this is a go/no-go
  gate, not a preference.

### Claim 2: The `runner.topology: arc-dind` designation is not ARC-specific — it applies to any custom Kubernetes operator using a privileged DinD sidecar, a shared work volume, and a `DOCKER_HOST` `tcp://` endpoint

- **Evidence**: A "Note" callout immediately following the guide's opening
  paragraph, addressed directly to readers not using ARC.
- **Confidence**: settled (first-party documentation broadening the scope of
  a named configuration value beyond the product it's usually associated
  with)
- **Quote**: "**Not using ARC?** If you run a custom Kubernetes operator with a DinD sidecar pattern (not ARC), the same principles apply: your pod needs a privileged DinD sidecar, a shared work volume, and `DOCKER_HOST` set to a `tcp://` endpoint. Set `runner.topology: arc-dind` in workflow frontmatter — the topology applies to any DinD sidecar setup, not just ARC specifically."
- **Our assessment**: This is a scope-widening clarification worth
  preserving distinctly from the rest of the guide, which is otherwise
  entirely ARC/Helm-specific. It confirms that `runner.topology: arc-dind`
  names a *filesystem/daemon topology contract* (privileged sidecar + shared
  volume + TCP `DOCKER_HOST`), not literally "must be running Actions Runner
  Controller" — relevant for teams on other Kubernetes CI runner operators
  who might otherwise assume this topology value doesn't apply to them.

### Claim 3: `runner.topology: arc-dind` drives two distinct activation timings — sysroot staging and tool-cache warnings happen at compile time, while network isolation, chroot identity, and `--docker-host` passthrough activate at runtime only when a `tcp://` value is detected in `DOCKER_HOST`

- **Evidence**: A "Tip" callout immediately after the frontmatter example,
  explicitly separating compile-time from runtime behaviors.
- **Confidence**: settled (first-party documentation of the compiler/runtime
  behavioral split)
- **Quote**: "`runner.topology: arc-dind` enables sysroot staging and tool-cache warnings at compile time. Other ARC-specific behaviors (network isolation, chroot identity, `--docker-host` passthrough) are activated at **runtime** when the compiled workflow detects a `tcp://` value in `DOCKER_HOST`. You do not need to configure these separately."
- **Our assessment**: This two-phase design means the frontmatter flag alone
  is necessary but not sufficient for the full ARC DinD behavior set — the
  runtime environment must actually present a `tcp://` `DOCKER_HOST` for
  network isolation and chroot identity patching to engage. A workflow
  compiled with `runner.topology: arc-dind` but accidentally run on a runner
  without a TCP `DOCKER_HOST` (e.g., a misconfigured pod template) would get
  the compile-time sysroot staging but silently miss the runtime network
  isolation — worth flagging as a verification step (confirm `DOCKER_HOST` is
  actually TCP at runtime, not just that the frontmatter field is set).

### Claim 4: At runtime, ARC DinD detection triggers five automatic behaviors: sysroot staging into a Docker named volume, explicit workspace mounting, chroot identity patching, artifact consolidation, and network isolation via an internal `awf-net` Docker network with a dual-homed Squid proxy as the sole egress path

- **Evidence**: A five-item bulleted list under "6. How it works," each item
  naming the mechanism and its rationale.
- **Confidence**: settled (first-party documentation of the exact automated
  behavior)
- **Quote**: "**Network isolation** — AWF enforces egress via Docker network topology: an internal Docker network (`awf-net`) with no internet route and a dual-homed Squid proxy as the sole egress path. The runner container issues Docker API commands to the DinD sidecar daemon; the daemon creates the networks and manages all traffic enforcement. No host `iptables` rules are applied from the runner container."
- **Our assessment**: This is the mechanistic explanation behind Claim 5 (no
  `NET_ADMIn`/`iptables` needed) — network isolation on ARC DinD is achieved
  by Docker network topology (an isolated `awf-net` with a Squid proxy as
  choke point) rather than kernel-level packet filtering. This is a
  meaningfully different enforcement mechanism from what a harness engineer
  might assume "network isolation" means by default (host firewall rules),
  and it explains why the runner container itself needs no elevated network
  capability — the DinD *sidecar* daemon does the enforcement, not the
  runner. Also corroborates `docs-ghaw-troubleshooting-debugging.md` Claim 11
  (squid-format access logs) — the `TCP_TUNNEL`/`DENIED` format that note
  documents is literally produced by this Squid proxy.

### Claim 5: `NET_ADMIN` capability and the `iptables` binary are explicitly not required on ARC DinD runners — enforcement happens via Docker network topology, and any `iptables`-mentioning log lines are a legacy artifact from a different, privileged runtime profile that can be ignored

- **Evidence**: A "What is NOT required" bulleted list plus a corroborating
  "Note" callout addressing a specific log-line false alarm.
- **Confidence**: settled (first-party documentation explicitly ruling out a
  plausible-seeming requirement and pre-empting a specific misread of logs)
- **Quote**: "If you see `iptables`-related output in workflow logs, it does not mean `iptables` is required. In network-isolation mode (the default for `topology: arc-dind`), AWF logs this as informational context but does not execute any `iptables` commands from the runner container."
- **Our assessment**: This is a named, specific false-alarm pattern worth
  preserving verbatim — a practitioner grepping logs for `iptables` during
  troubleshooting could reasonably (but incorrectly) conclude the runner
  needs `NET_ADMIN` or a privileged container to make `iptables` calls work,
  and escalate pod security unnecessarily. The page pre-empts exactly that
  misdiagnosis. Combined with the "Privileged runner container" bullet
  ("only the DinD sidecar needs `privileged: true`. The runner container runs
  unprivileged"), this reinforces `docs-ghaw-agent-runtimes-reference.md`
  Claim 9's "unprivileged runner, privileged sidecar only" security framing.

### Claim 6: The default `RUNNER_TOOL_CACHE` location (`/opt/hostedtoolcache`) is invisible to the DinD daemon because `/opt` is not on a volume shared with it — tools from `setup-*` actions must be redirected to a shared path, and the compiler emits a runtime warning if it isn't

- **Evidence**: A dedicated "Tool cache redirection" section with the
  problem statement, the fix (a `RUNNER_TOOL_CACHE` env var pointed at
  `/tmp/gh-aw/tool-cache`), and a description of the compiled workflow's
  self-check.
- **Confidence**: settled (first-party documentation of a specific
  filesystem-sharing gotcha and its fix)
- **Quote**: "If your runner image uses the default `RUNNER_TOOL_CACHE` location (`/opt/hostedtoolcache`), tools installed by `setup-*` actions (for example `setup-node`, `setup-python`) will be invisible to the DinD daemon because `/opt` is not on a shared volume."
- **Our assessment**: This is a concrete, easy-to-hit failure mode for any
  team migrating an existing GitHub-Actions-based CI setup (which commonly
  relies on `actions/setup-node`, `actions/setup-python`, etc.) onto ARC
  DinD — the tools install successfully in the setup step but the agent
  container, which reaches the filesystem via the DinD daemon rather than
  the runner's own filesystem, can't see them at `/opt`. The compiler's
  proactive runtime warning ("emits a warning at runtime if it detects
  `RUNNER_TOOL_CACHE` under `/opt`") is a genuinely helpful diagnostic
  surfaced automatically rather than left for the practitioner to discover
  via a mysterious "command not found."

### Claim 7: On ARC DinD, AWF sandbox logs are written to `$RUNNER_TEMP/gh-aw/sandbox/firewall/logs/` rather than the `/tmp/gh-aw/` path used elsewhere, because `$RUNNER_TEMP` sits on the shared work volume while `/tmp` may not

- **Evidence**: A dedicated "Finding AWF logs" section explaining the path
  difference and its cause, plus a three-row table of specific log files and
  their contents.
- **Confidence**: settled (first-party documentation of a topology-specific
  path override, with the rationale stated explicitly)
- **Quote**: "On ARC DinD runners, sandbox logs are written to `$RUNNER_TEMP/gh-aw/sandbox/firewall/logs/`, **not** `/tmp/gh-aw/`. This is because `$RUNNER_TEMP` (typically `/home/runner/_work/_temp`) is on the shared work volume, while `/tmp` may not be."
- **Our assessment**: This directly extends, and is conditioned by runner
  topology rather than contradicting, `docs-ghaw-troubleshooting-debugging.md`
  Claim 11 and its artifact table, which documents `/tmp/gh-aw/firewall-logs`
  and `sandbox/firewall/logs/access.log` as the standard-runner locations.
  This page adds the ARC-DinD-specific override: a practitioner following
  that note's log-path guidance verbatim on an ARC DinD runner would look in
  the wrong place. This is a conditioning variable (runner topology), not a
  contradiction — both notes describe the same log file, at different paths,
  for different runner topologies, and this page states the filesystem
  reason for the difference (shared-volume boundary) directly.

### Claim 8: A five-step migration checklist moves a workflow off manual ARC DinD workarounds (custom bootstrap actions, XDG env overrides, manual `DOCKER_HOST`/`MCP_GATEWAY_DOMAIN` settings, `sandbox.agent.mounts` staging) onto `runner.topology: arc-dind`, because the compiler now automates all of them

- **Evidence**: An "Upgrading from manual workarounds" section with an
  explicit warning about workaround/generated-step conflicts, followed by a
  five-item ordered migration list.
- **Confidence**: settled (first-party documentation of a specific migration
  procedure with named frontmatter fields to remove)
- **Quote**: "If you previously used custom bootstrap actions, copilot shims, `/etc` pre-seeding, XDG environment overrides, or manual `DOCKER_HOST` / `MCP_GATEWAY_DOMAIN` settings to run on ARC DinD, remove them when adopting `runner.topology: arc-dind`. The compiler now handles all of these automatically. Leftover workarounds may conflict with the generated workflow steps."
- **Our assessment**: The "may conflict with the generated workflow steps"
  warning is the operationally important part — this isn't just redundant
  cleanup, leftover manual `engine.env` overrides for `XDG_CACHE_HOME`,
  `MCP_GATEWAY_DOMAIN`/`MCP_GATEWAY_PORT`, or `DOCKER_HOST` could actively
  break the now-automated behavior by fighting with what the compiler
  generates. For any team that adopted ARC DinD before this topology field
  existed (implied by the guide's framing), this is a required cleanup step,
  not an optional simplification.

### Claim 9: Clusters enforcing `allowPrivilegeEscalation: false` block the default Copilot CLI installer's `sudo` call — passing `--rootless` to `install_copilot_cli.sh` installs to `~/.local/bin` instead and appends it to `$GITHUB_PATH` automatically

- **Evidence**: A "Pod security and rootless install" section with the
  problem statement, a `copilot-setup-steps` YAML example invoking the
  script with `--rootless`, and a three-item description of rootless-mode
  behavior.
- **Confidence**: settled (first-party documentation of a specific flag and
  its exact effects)
- **Quote**: "Pass `--rootless` to `install_copilot_cli.sh` in your `copilot-setup-steps` to install to `~/.local/bin` without any `sudo` calls. The script adds that directory to `$GITHUB_PATH` so subsequent steps find the binary."
- **Our assessment**: This is the full operational context for a flag that
  `blog-ghaw-weekly-2026-07-20.md` Claim 7 announced only as a changelog
  entry ("Rootless flag for ARC/DinD runners... a welcome fix for teams
  running Copilot on custom runners") without documenting when it's needed
  or its exact filesystem/PATH effects. This page supplies the trigger
  condition (`allowPrivilegeEscalation: false` via PodSecurity Admission or
  OPA policies), the concrete YAML usage, and the mechanism (`~/.local/bin` +
  automatic `$GITHUB_PATH` append) that changelog announcement was missing.

### Claim 10: A known limitation — the MCP gateway can fail to reach the Docker daemon on runners where `DOCKER_HOST` is a TCP endpoint and no Unix socket exists at `/var/run/docker.sock` — is tracked in an open GitHub issue, with a documented workaround of exposing the DinD sidecar's socket via a shared volume or symlink

- **Evidence**: A "Known limitations" section naming the failure mode and
  linking a tracking issue; repeated in the "Troubleshooting" section with
  the exact error string and a second, more specific fix (`GH_AW_DOCKER_SOCK_PATH`
  / `GH_AW_DOCKER_SOCK_GID` environment variables).
- **Confidence**: settled (first-party documentation of a known, currently
  open limitation with a tracked issue number and a stated workaround)
- **Quote**: "**MCP gateway Docker socket access** — on runners where `DOCKER_HOST` is a TCP endpoint and no Unix socket exists at `/var/run/docker.sock`, the MCP gateway may fail to connect to the Docker daemon (`Docker daemon is not accessible`). As a workaround, expose the DinD sidecar's Unix socket on the runner container at `/var/run/docker.sock` via a shared volume or symlink. See [#44251](https://github.com/github/gh-aw/issues/44251) for tracking."
- **Our assessment**: This is a genuine, currently-unresolved platform gap
  (not a fixed-in-version item like the empty-workspace or detection-job
  bugs elsewhere on the page) — worth flagging distinctly in the guide as an
  open caveat rather than a solved problem, since the workaround
  (`GH_AW_DOCKER_SOCK_PATH`/`GH_AW_DOCKER_SOCK_GID`) is a manual
  configuration step a team must apply themselves, not something the
  compiler does automatically the way it does for the sysroot/workspace/
  chroot/network behaviors in Claim 4.

### Claim 11: Minimum required versions are `gh-aw` v0.82.8 (workspace/detection fixes plus the MCP gateway Docker socket access fix) and AWF v0.27.22 (DinD Squid log permission fixes) — teams on `gh-aw` v0.82.5–v0.82.7 must upgrade and recompile before following this guide

- **Evidence**: A "Required versions" table with component, minimum version,
  and a one-line "why," followed by an explicit upgrade instruction for a
  named prior version range.
- **Confidence**: settled (first-party documentation of specific minimum
  version numbers with named fix rationale)
- **Quote**: "If you're on `gh-aw` `v0.82.5`–`v0.82.7`, upgrade and recompile before using this guide:" (followed by `gh aw upgrade` / `gh aw compile`)
- **Our assessment**: The specificity of the version floor (not just "use a
  recent version" but v0.82.8 exactly, with the reason named) is unusually
  precise for a docs page and useful as a concrete checkable gate before
  troubleshooting anything else — a team hitting any of the symptoms in the
  Troubleshooting section (Claims 10, 12) should check their `gh-aw`/AWF
  version against this table before investigating further, since two of the
  three named Troubleshooting fixes (empty workspace, detection job ENOENT)
  are stated as "fixed in gh-aw v0.82.5" and require nothing but upgrading.

### Claim 12: DinD-spawned containers run on Docker's internal network without access to Kubernetes cluster DNS, so a DIFC proxy hostname that is a Kubernetes service name (e.g. `awmg-cli-proxy`) fails to resolve inside the DinD daemon — the fix is IP-based reachability or DNS forwarding from the DinD Docker network to the cluster DNS resolver

- **Evidence**: The `awf-cli-proxy could not connect to the external DIFC proxy`
  troubleshooting entry, specifically the `getaddrinfo EAI_AGAIN <hostname>`
  branch.
- **Confidence**: settled (first-party documentation naming a specific error
  string, its root cause, and two possible fixes)
- **Quote**: "**If the log shows `getaddrinfo EAI_AGAIN <hostname>`:** The proxy hostname is a Kubernetes service name (for example `awmg-cli-proxy`) that DinD-spawned containers cannot resolve. Docker containers created by the DinD daemon run on Docker's internal network, which does not have access to Kubernetes cluster DNS."
- **Our assessment**: This is a specific, non-obvious cross-boundary DNS gap
  — a practitioner configuring an MCP gateway proxy by Kubernetes service
  name (the natural way to reference another in-cluster service) would hit
  this failure precisely because DinD's Docker network is isolated from
  cluster DNS by design (the same isolation that underlies the network
  security model in Claim 4). The stated fixes (IP-based reachability, or
  DNS forwarding into the DinD Docker network) are both infrastructure-level
  changes outside gh-aw's own configuration surface, so this is a real
  operational gotcha for the Kubernetes/network-admin side of an ARC DinD
  rollout, not something fixable purely in workflow frontmatter.

## Concrete Artifacts

### Full Helm/kubectl deployment sequence (verbatim from source, steps 1–5)

```
# 1. Install the ARC controller
helm install arc \
  --namespace "arc-system" --create-namespace \
  oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set-controller

# 2. Create the runner namespace and auth secret
kubectl create ns arc-runners

# Option A: Personal access token
kubectl create secret generic arc-runner-secret \
  --namespace=arc-runners \
  --from-literal=github_token=<YOUR_PAT>

# Option B: GitHub App (recommended for production)
kubectl create secret generic arc-runner-secret \
  --namespace=arc-runners \
  --from-literal=github_app_id=<APP_ID> \
  --from-literal=github_app_installation_id=<INSTALL_ID> \
  --from-literal=github_app_private_key=<PRIVATE_KEY>

# 3. Install a runner scale set in DinD mode
helm install "arc-runner-set" \
  --namespace "arc-runners" --create-namespace \
  --set githubConfigUrl="https://github.com/<OWNER>/<REPO>" \
  --set githubConfigSecret="arc-runner-secret" \
  --set containerMode.type="dind" \
  --set-json 'template.spec.containers=[{
    "name": "runner",
    "image": "ghcr.io/actions/actions-runner:latest",
    "command": ["/home/runner/run.sh"]
  }]' \
  oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set

# 4. Verify the runner is online at
#    https://github.com/<OWNER>/<REPO>/settings/actions/runners

# 5. Target the runner set from a workflow
```
```yaml
---
on: issues
runs-on: arc-runner-set
runner:
  topology: arc-dind
---
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — sections 1–5*

### Network requirements table (verbatim from source)

```
| Destination                                                  | Purpose                                          |
|---------------------------------------------------------------|---------------------------------------------------|
| github.com (or your GHES instance)                            | Git clone, API calls, Actions runtime              |
| api.githubcopilot.com (or your enterprise Copilot endpoint)   | Copilot engine communication                       |
| ghcr.io and pkg-containers.githubusercontent.com               | Pull MCP gateway and AWF container images          |
| Domains in your workflow's network.allowed list                | Agent egress (npm registries, PyPI, etc.)          |
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Network requirements" section*

### Required and optional configuration table (verbatim from source)

```
| Item                                       | Required? | Notes                                                                                                                                                    |
|---------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| DinD container mode                         | Yes       | GitHub Copilot coding agent needs a Docker daemon in the runner pod.                                                                                     |
| NET_ADMIN capability                        | No        | Not required. AWF enforces egress via Docker network topology (network isolation mode), not host iptables. The DinD sidecar daemon manages all network enforcement internally. |
| ghcr.io/actions/actions-runner:latest       | Recommended | Use the official runner image, or a compatible custom image with equivalent runner requirements.                                                       |
| Runner user                                 | Yes       | Non-root runner users are supported. By default, sudo must be available on the runner container for the Copilot CLI install script. If your cluster enforces allowPrivilegeEscalation: false, use the --rootless flag. |
| DinD sidecar privilege                      | Yes       | ARC DinD mode configures a privileged sidecar for Docker daemon operation.                                                                              |
| Shared work volume (/home/runner/_work)     | Yes       | Runner and Docker daemon share this volume in ARC DinD mode, so workspace mounts work without host path translation.                                    |
| Specific Kubernetes distribution            | No        | Any conformant cluster works (for example minikube, EKS, AKS, or GKE).                                                                                  |
| Specific namespace names                    | No        | arc-system and arc-runners are conventions only.                                                                                                        |
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Required and optional configuration" section*

### AWF log file table (verbatim from source)

```
| Log            | Path                                                              | Contains                                          |
|-----------------|--------------------------------------------------------------------|-----------------------------------------------------|
| CLI proxy      | $RUNNER_TEMP/gh-aw/sandbox/firewall/logs/cli-proxy.log              | DIFC proxy connection attempts, DNS resolution errors |
| Squid access   | $RUNNER_TEMP/gh-aw/sandbox/firewall/logs/squid-access.log           | Egress requests (allowed/denied)                    |
| AWF startup    | $RUNNER_TEMP/gh-aw/sandbox/firewall/logs/awf.log                    | Sandbox setup, network isolation, container creation |
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Finding AWF logs" section*

### Rootless Copilot CLI install step (verbatim from source)

```yaml
copilot-setup-steps:
  runs-on: arc-runner-set
  steps:
    - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
      with:
        repository: github/gh-aw
        path: gh-aw
    - name: Install Copilot CLI (rootless)
      run: bash "${GITHUB_WORKSPACE}/gh-aw/actions/setup/sh/install_copilot_cli.sh" --rootless
      env:
        GH_HOST: github.com
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Pod security and rootless install" section*

### Required versions table (verbatim from source)

```
| Component                          | Minimum version | Why                                                            |
|--------------------------------------|-------------------|------------------------------------------------------------------|
| gh-aw                                | v0.82.8           | Includes ARC DinD workspace/detection fixes and the MCP gateway Docker socket access fix. |
| AWF (agentic-workflow-firewall)      | v0.27.22          | Includes DinD squid log permission fixes.                       |
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Required versions" section*

### Five-step manual-workaround migration checklist (verbatim ordered list)

```
1. Remove any pre-agent-steps, resources, or safe-outputs.threat-detection.steps
   blocks that were workarounds for ARC DinD.
2. Remove manual engine.env overrides for XDG_CACHE_HOME, XDG_CONFIG_HOME,
   XDG_STATE_HOME, MCP_GATEWAY_DOMAIN, MCP_GATEWAY_PORT, and DOCKER_HOST.
3. Remove sandbox.agent.mounts entries that staged files for the DinD daemon.
4. Add runner.topology: arc-dind to frontmatter.
5. Run gh aw compile and commit the updated lock file.
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Upgrading from manual workarounds" section*

### Troubleshooting table (symptom → cause/fix, condensed from source's five entries)

```
| Symptom                                                   | Cause / Fix                                                                                                    |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Agent reports empty workspace                                | Fixed in gh-aw v0.82.5 — `gh aw upgrade && gh aw compile`                                                        |
| Detection job fails: `spawn /usr/local/bin/copilot ENOENT`  | Fixed in gh-aw v0.82.5 (PR #44445) — upgrade and recompile                                                       |
| `sudo: The "no new privileges" flag is set`                  | Pod security context has allowPrivilegeEscalation: false — use `--rootless` on the Copilot CLI installer          |
| `awf-cli-proxy could not connect to the external DIFC proxy` | Check cli-proxy.log; `getaddrinfo EAI_AGAIN` = K8s-service-name DNS unresolvable inside DinD network; timeouts = DinD daemon not ready yet (AWF retries 10x/2s) |
| `RUNNER_TOOL_CACHE is under /opt` warning                     | Redirect RUNNER_TOOL_CACHE to a shared path (e.g. /tmp/gh-aw/tool-cache)                                          |
| `Docker daemon is not accessible` in MCP gateway              | Set GH_AW_DOCKER_SOCK_PATH and GH_AW_DOCKER_SOCK_GID to point at the DinD sidecar's socket                        |
| `chmod: Operation not permitted` on log/audit dirs            | Non-root container post-job permission repair fails harmlessly; AWF v0.27.22+ auto-repairs ownership on persistent runners |
```

*Source: `https://github.github.com/gh-aw/reference/arc-dind-copilot-agent` — "Troubleshooting" section*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-07-20.md` Claim 7 (`install_copilot_cli.sh --rootless`
    flag announced for ARC/DinD runners, PR #46047): this page is the durable
    reference for that changelog item. Claim 9 of this note supplies the
    trigger condition (`allowPrivilegeEscalation: false`), the exact usage
    site (`copilot-setup-steps`), and the mechanism (`~/.local/bin` +
    `$GITHUB_PATH`) that the weekly changelog entry announced without detail.
  - `docs-ghaw-agent-runtimes-reference.md` Claim 9 ("unprivileged runner
    container; only the DinD sidecar needs `privileged: true`"): this page's
    "What is NOT required" list (Claim 5) — "Privileged runner container —
    only the DinD sidecar needs `privileged: true`. The runner container runs
    unprivileged" — restates the identical security posture in operational
    deployment terms.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 11 (Squid-format firewall
    access logs, `TCP_TUNNEL`/`DENIED` entries): this page's Claim 4
    ("dual-homed Squid proxy as the sole egress path") names the Squid proxy
    that produces exactly that log format, and Claim 7's Squid-access log
    file (`squid-access.log`) is the ARC-DinD-path equivalent of the artifact
    that note documents at the standard-runner path.

- **Contradicts**: None identified as a genuine contradiction. Claim 7 (AWF
  logs at `$RUNNER_TEMP/gh-aw/sandbox/firewall/logs/` on ARC DinD, not
  `/tmp/gh-aw/`) differs from the path in
  `docs-ghaw-troubleshooting-debugging.md` Claim 11 and its artifact table
  (`/tmp/gh-aw/firewall-logs`), but this is a topology-conditioned path
  difference with an explicit stated cause (shared-volume boundary), not two
  sources disagreeing about the same runner environment — per MINER.md §4a
  this is a conditioning variable, not a contradiction, so no contradiction
  issue was filed.

- **Extends**:
  - `docs-ghaw-agent-runtimes-reference.md`: that note's extraction notes
    explicitly flagged "A future source-submission for
    `guides/arc-dind-copilot-agent` would be a reasonable follow-up if ARC
    DinD rollout mechanics become relevant to the guide" and covers the
    *decision* to select ARC DinD (mutual exclusion with gVisor/Docker sbx,
    runner requirements, the "infrastructure necessity, not isolation
    upgrade" framing). This page is exactly that follow-up: the *operational*
    guide for actually deploying Copilot on ARC DinD — Helm commands,
    version floors, tool-cache and log-path gotchas, a migration checklist,
    and Copilot-specific installer flags that the runtimes-selection
    reference does not cover. (Note: the runtimes-reference note's link text
    said `/gh-aw/guides/arc-dind-copilot-agent/`; this issue's source URL is
    `/gh-aw/reference/arc-dind-copilot-agent/` — the site nav confirms the
    current page lives under "Reference" as "Self-Hosted Runners (ARC DinD)."
    Whether this reflects a `guides/` → `reference/` page relocation between
    extraction dates, or the runtimes-reference note simply mislabeled the
    path, is not resolvable from this page alone; treated as the same
    intended follow-up target either way, since content and scope match.)
  - `docs-ghaw-troubleshooting-debugging.md`: extends that note's general
    artifact/log-path guidance (Claim 11) with the ARC-DinD-specific
    override and its filesystem-sharing rationale (Claim 7).
  - `blog-ghaw-weekly-2026-07-20.md`: extends Claims 6–7 (rootless-runner
    support announcement) with the full operational detail — trigger
    condition, exact flag, and installed-path/PATH mechanism.

- **Novel** (nothing in the corpus previously covered these):
  - **The full ARC DinD Copilot deployment procedure** (Concrete Artifacts:
    Helm/kubectl sequence) — no existing source note documents the ARC
    controller install, runner scale set creation in DinD mode, or the
    frontmatter targeting steps.
  - **The compile-time vs. runtime activation split for `runner.topology: arc-dind`**
    (Claim 3) and the five specific runtime-detected behaviors (Claim 4) —
    sysroot staging, workspace mount, chroot identity, artifact
    consolidation, and the `awf-net`/Squid network-isolation mechanism are
    all new to the corpus.
  - **Tool cache redirection for `/opt`-based `RUNNER_TOOL_CACHE`** (Claim 6)
    — a concrete, previously undocumented DinD filesystem-sharing gotcha.
  - **ARC-DinD-specific AWF log paths** (Claim 7, Concrete Artifacts log
    table) — new to the corpus; extends but does not duplicate the
    standard-runner log paths already documented.
  - **The five-step manual-workaround migration checklist** (Claim 8) — new
    operational guidance for teams that adopted ARC DinD before this
    topology field existed.
  - **Rootless Copilot CLI installation mechanism and trigger condition**
    (Claim 9) — the `allowPrivilegeEscalation: false` trigger and the
    `~/.local/bin`/`$GITHUB_PATH` mechanism are new to the corpus (the prior
    corpus mention was changelog-level only).
  - **The open MCP-gateway-Docker-socket-access limitation with its tracked
    issue and workaround** (Claim 10) — new to the corpus; a currently
    unresolved gap worth flagging distinctly from the fixed-in-version items.
  - **Minimum version floors with named fix rationale** (Claim 11) and **the
    DinD-internal-network DNS-resolution troubleshooting entry** (Claim 12)
    — both new, specific operational details.

## Guide Impact

- **Chapter 04 (Deployment & Orchestration) / Chapter 02 (Harness Engineering)**:
  Add a concrete "deploying Copilot coding agent on ARC DinD" walkthrough
  using the Helm/kubectl sequence and frontmatter example (Concrete
  Artifacts), positioned as the operational counterpart to
  `docs-ghaw-agent-runtimes-reference.md`'s runtime-selection framework —
  that note tells a harness engineer *when* to choose ARC DinD; this note
  tells them *how* to actually stand it up. Include the version floor table
  (Claim 11) as a pre-flight check and the five-step migration checklist
  (Claim 8) for teams with existing manual ARC DinD workarounds.

- **Chapter 02 or 05 (Operational Readiness / troubleshooting reference)**:
  Add the tool-cache redirection gotcha (Claim 6) and the ARC-DinD-specific
  AWF log path override (Claim 7) as named pitfalls distinct from the
  standard-runner guidance already sourced from
  `docs-ghaw-troubleshooting-debugging.md` — explicitly note that log paths
  and tool visibility are conditioned on runner topology, not universal
  constants. Add the open MCP-gateway-Docker-socket limitation (Claim 10) as
  a currently-unresolved caveat for teams planning to use the MCP gateway on
  ARC DinD.

- **Chapter 03 (Safety and Verification)**: Extend the AWF network-isolation
  material with the `awf-net`/Squid-proxy mechanism (Claim 4) as the concrete
  implementation of "network isolation via Docker topology, not host
  `iptables`" (Claim 5) for the ARC DinD case specifically — this is a
  distinct enforcement mechanism from the domain-allowlist model documented
  elsewhere and worth naming explicitly when discussing how AWF's network
  controls vary by runner topology.

## Extraction Notes

1. **Verbatim text sourced from raw HTML, not the WebFetch AI-summarization
   tool.** As with `docs-ghaw-agent-runtimes-reference.md`, an initial
   WebFetch pass returned a plausible-looking but unverifiable prose summary
   (rendered through a summarizing model, with section content compressed
   and reworded). To satisfy the verbatim-quote requirement, the page was
   re-fetched directly via `curl` and converted to text with `html2text`
   (installed for this extraction), then every `Quote` field above and every
   verbatim table/code artifact was copied character-for-character from that
   raw conversion. Section boundaries were cross-checked against the page's
   own "Section titled..." anchors, which `html2text` preserves as plain
   text markers.

2. **No linked sub-pages followed as separate deep-reads.** The page's
   "Related documentation" section links to `reference/self-hosted-runners/`
   (including its `#docker-socket-override-for-split-daemon-topologies`
   anchor), the ARC Helm charts repository, and a GitHub issue tracking
   rootless Copilot CLI install. The self-hosted-runners reference page is
   not yet mined in this corpus and is a reasonable follow-up source-submission
   candidate — it covers `runs-on` formats, Docker socket overrides for
   *other* split-daemon topologies (not just ARC DinD), and GHES
   compatibility, none of which this ARC-DinD-specific page covers in depth.
   The ARC Helm charts repository and the tracking issue are external/
   non-documentation resources not treated as deep-read targets for a docs
   source note.

3. **No publication date on the page.** Consistent with other Astro/Starlight
   reference pages in this corpus (`docs-ghaw-agent-runtimes-reference.md`,
   `docs-ghaw-sandbox-reference.md`), `date_published` is left null.

4. **Confidence rated `settled` throughout.** The page contains no content
   marked experimental or beta; its claims are mechanistic platform
   specification (Helm commands, exact version numbers, exact file paths,
   named PR/issue numbers for specific fixes) rather than architectural
   framing subject to interpretation — the kind of content least likely to
   be materially wrong, consistent with the `settled` rating given to
   `docs-ghaw-agent-runtimes-reference.md`.

5. **No contradictions filed.** Reviewed `docs-ghaw-agent-runtimes-reference.md`,
   `docs-ghaw-sandbox-reference.md`, `docs-ghaw-troubleshooting-debugging.md`,
   `docs-ghaw-network-reference.md`, and `blog-ghaw-weekly-2026-07-20.md`
   (the notes most likely to overlap on ARC DinD, sandboxing, logging, or
   rootless-runner topics). The one apparent discrepancy (AWF log path:
   `$RUNNER_TEMP/gh-aw/sandbox/firewall/logs/` here vs. `/tmp/gh-aw/` in
   `docs-ghaw-troubleshooting-debugging.md`) is explicitly conditioned on
   runner topology with a stated filesystem cause, not a disagreement
   between sources about the same environment — per MINER.md §4a this is a
   conditioning variable, not a contradiction, so no contradiction issue was
   filed. See the note under "Extends" above regarding the
   `guides/arc-dind-copilot-agent` vs. `reference/arc-dind-copilot-agent`
   path discrepancy relative to `docs-ghaw-agent-runtimes-reference.md`'s
   extraction notes — this is a documentation-site path/navigation detail,
   not a factual contradiction about platform behavior, so it likewise did
   not warrant a contradiction issue.
