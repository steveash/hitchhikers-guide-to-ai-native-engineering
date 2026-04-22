---
source_url: https://github.github.com/gh-aw/guides/self-hosted-runners
source_type: docs
title: "GitHub Agentic Workflows: Self-Hosted Runners"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#299"
---

# GitHub Agentic Workflows: Self-Hosted Runners

> Concrete infrastructure constraints and security architecture for deploying
> gh-aw on self-hosted runners — fills in the runner-level implementation of
> Layers 2 (runtime isolation) and 4 (network controls) from the five-layer
> security model in `docs-ghaw-how-they-work.md`, and introduces AWF (Agentic
> Workflow Firewall) as the named outer security boundary for all agent containers.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Guides /
  Self-Hosted Runners" page; not a blog post or practitioner account)
- **Author credibility**: First-party documentation from the GitHub Agentic
  Workflows team. Same team behind the Peli de Halleux / Don Syme agent factory
  series. Claims about runner requirements, AWF mechanics, and runner
  configuration semantics are settled for this platform; they do not
  automatically generalize to other agentic systems or CI/CD platforms.
- **Scope**: Runner infrastructure for gh-aw — hardware/OS requirements, the AWF
  security model, the four-tier runner field architecture, import merge semantics
  for `runs-on`, and runner configuration for framework/maintenance/detection
  jobs. Does NOT cover: the full Safe Outputs permission model (see
  `docs-ghaw-how-they-work.md`), workflow frontmatter syntax beyond runner fields,
  the ephemeral lifecycle model (see `docs-ghaw-ephemerals.md`), or cost benchmarks.

## Extracted Claims

### Claim 1: AWF (Agentic Workflow Firewall) applies host-level iptables rules on the Linux kernel DOCKER-USER chain to enforce network egress for all agent containers

- **Evidence**: The page states directly: "AWF applies host-level `iptables`
  rules to the Linux kernel `DOCKER-USER` chain to enforce network egress
  filtering for all agent containers." This is the concrete implementation of
  what `docs-ghaw-how-they-work.md` Claim 3 names abstractly as Layer 4
  (Network Controls) in the five-layer security pipeline.
- **Confidence**: settled (first-party documentation; specific kernel chain name
  and mechanism are documented)
- **Quote**: "AWF applies host-level `iptables` rules to the Linux kernel
  `DOCKER-USER` chain to enforce network egress filtering for all agent containers."
- **Our assessment**: The DOCKER-USER chain is the correct hook for host-level
  Docker egress control — rules inserted there apply to all traffic leaving any
  container on the host before the container's own iptables rules run. This is a
  meaningful architectural detail: it means AWF enforces egress at the host
  kernel level, not just inside the container namespace. A container running as
  root could potentially modify its own container-level iptables, but cannot
  remove the host-level DOCKER-USER rules without host root access. For Ch03
  (Safety): this is the concrete mechanism behind Layer 4 of the five-layer
  model — the network control is at the host, not the container, which is the
  correct placement for a tamper-resistant outer boundary.

### Claim 2: AWF requires runner root/sudo access; non-sudo mode is not supported, and ARC configurations with `allowPrivilegeEscalation: false` are explicitly unsupported

- **Evidence**: "Runners must allow `sudo` for agentic workflows." And explicitly:
  "Non-sudo mode is not supported, including ARC configurations with
  `allowPrivilegeEscalation: false`." This eliminates a common Kubernetes runner
  hardening option and constrains which self-hosted runner deployments are compatible.
- **Confidence**: settled (first-party documentation; explicit statement of what
  is NOT supported)
- **Quote**: "Non-sudo mode is not supported, including ARC configurations with
  `allowPrivilegeEscalation: false`."
- **Our assessment**: The ARC (Actions Runner Controller) + `allowPrivilegeEscalation:
  false` combination is the standard Kubernetes-based runner hardening pattern.
  Its explicit exclusion means teams running gh-aw on Kubernetes cannot use the
  typical pod security standard that restricts privilege escalation. This is a
  hard infrastructure constraint that eliminates otherwise common runner setups.
  For Ch02 (Harness Engineering): flag this explicitly when discussing self-hosted
  runner options — teams evaluating gh-aw on Kubernetes-based ARC runners will hit
  this incompatibility. The correct deployment path is a dedicated Linux VM with
  Docker and sudo, not a locked-down pod.

### Claim 3: AWF implements a nested defense-in-depth isolation stack: host-level iptables (outer boundary) → container-level iptables → Squid proxy ACLs → capability drops

- **Evidence**: The page describes the security layers in order: "AWF applies
  host-level `iptables` rules to the Linux kernel `DOCKER-USER` chain to enforce
  network egress filtering for all agent containers. This outer security boundary
  requires root UID. Container-level `iptables`, Squid proxy ACLs, and capability
  drops provide additional defense."
- **Confidence**: emerging (first-party documentation; the specific Squid version,
  proxy ACL syntax, and capability drop list are not detailed on this page)
- **Quote**: "Container-level `iptables`, Squid proxy ACLs, and capability drops
  provide additional defense."
- **Our assessment**: This four-layer nested stack maps concretely onto the
  five-layer security model in `docs-ghaw-how-they-work.md`. Host-level iptables
  is the outer enforcement of Layer 4 (Network Controls); container-level iptables
  and Squid proxy ACLs add depth within Layer 4; capability drops implement
  Layer 2 (Runtime Isolation). The page notes that the host-level layer is "the
  outer security boundary" — the rest add defense-in-depth but do not replace
  it. For Ch03: this is the most concrete description of how gh-aw implements
  its security model at the infrastructure level. The two-tier network control
  (host + container iptables + proxy) is worth calling out: disabling the proxy
  in the container does not escape AWF's outer boundary.

### Claim 4: Self-hosted runners must be Linux with Docker support; macOS and Windows are not supported

- **Evidence**: "Runners must be Linux with Docker support. macOS and Windows are
  not supported." No exceptions or workarounds are documented.
- **Confidence**: settled (first-party documentation; explicit OS restrictions)
- **Quote**: "macOS and Windows are not supported"
- **Our assessment**: This is a straightforward platform constraint with practical
  implications for teams in Windows-primary shops or those using macOS-based
  GitHub-hosted runners (e.g., GitHub's `macos-latest`). The Docker requirement
  means the runner must support Docker-in-Docker or a standard Docker daemon, which
  also excludes some minimal container environments. For Ch02: document this
  constraint alongside the ARC incompatibility (Claim 2) as the two constraints
  that most commonly surprise teams evaluating self-hosted runner deployment.

### Claim 5: gh-aw uses a four-tier runner field architecture — `runs-on` (agent job), `runs-on-slim` (framework jobs), `safe-outputs.threat-detection.runs-on` (detection job), and `maintenance.runs_on` in `aw.json` (maintenance jobs)

- **Evidence**: The page documents four distinct runner configuration fields
  controlling four different job classes:
  1. `runs-on:` — the main agent job
  2. `runs-on-slim:` — all framework/generated jobs (activation, pre-activation,
     safe-outputs, unlock, APM, update_cache_memory, push_repo_memory); default: `ubuntu-slim`
  3. `safe-outputs.threat-detection.runs-on:` — the threat detection job
  4. `runs_on` in `.github/workflows/aw.json` under `maintenance:` — all jobs in
     `agentics-maintenance.yml` (close-expired-entities, cleanup-cache-memory,
     run_operation, apply_safe_outputs, create_labels, validate_workflows,
     activity_report)
- **Confidence**: settled (first-party documentation; four fields are named and
  scoped precisely)
- **Quote**: "The `runs-on` field controls only the main agent job. The
  `runs-on-slim` field controls all framework and generated jobs."
- **Our assessment**: The four-tier architecture is a non-obvious harness design
  pattern. A practitioner who sets only `runs-on` will find that framework
  jobs, the detection job, and maintenance jobs still run on their defaults
  (ubuntu-slim / whatever the detection job inherits / ubuntu-slim). This matters
  for teams with network-restricted self-hosted runners — if those runners can't
  reach the internet, the AI-powered threat detection will silently fail unless
  `safe-outputs.threat-detection.runs-on` is overridden to a cloud runner. For
  Ch02: include this four-tier diagram explicitly in any section on self-hosted
  runner configuration for gh-aw. It is not discoverable from `runs-on` alone.

### Claim 6: `runs-on` is NOT merged from imports; `network` and `tools` settings CAN be shared via imports

- **Evidence**: "The `runs-on` field must be set in each workflow individually
  and is not merged from imports. Other settings like `network` and `tools` can
  be shared through imports."
- **Confidence**: settled (first-party documentation; the exception is stated
  explicitly)
- **Quote**: "The `runs-on` field must be set in each workflow individually and
  is not merged from imports."
- **Our assessment**: This is a footgun for teams trying to standardize runner
  configuration across many workflows via a shared import file. A team that
  puts `runs-on: [self-hosted, linux, x64]` in a shared config file and imports
  it will find that each workflow still runs on the default runner. The contrast
  with `network` and `tools` (which DO merge from imports) makes this asymmetry
  easy to miss. For Ch02: flag this explicitly alongside import patterns. The
  practical implication: shared imports are the right mechanism for standardizing
  tool allowlists and network permissions, but runner selection must be duplicated
  in each workflow file.

### Claim 7: `runs-on` supports three format variants — string (single label), array (logical AND), and object (named group with optional label filtering)

- **Evidence**: Three YAML examples are documented:
  1. String: `runs-on: self-hosted`
  2. Array: `runs-on: [self-hosted, linux, x64]` (runner must match all labels)
  3. Object: `runs-on: { group: my-runner-group, labels: [linux, x64] }` (named
     runner group with optional label filter)
- **Confidence**: settled (first-party documentation; concrete YAML examples provided)
- **Quote**: (examples are in YAML, no prose quote)
- **Our assessment**: The array format is the most useful for mixed runner pools —
  `[self-hosted, linux, x64]` targets only runners with all three labels,
  preventing an agent job from landing on a runner that lacks the required Docker
  environment. The object format with `group:` is the enterprise pattern for
  managed runner fleets. For Ch02: these are the three standard GitHub Actions
  `runs-on` formats; no gh-aw-specific complexity here, but worth including in
  the self-hosted runner configuration reference.

### Claim 8: The threat detection job runner can be overridden independently from the agent job runner, enabling cost optimization and airgap scenarios

- **Evidence**: "When threat detection is enabled, the detection job runs on the
  agent job's runner by default. Override this using `safe-outputs.threat-detection.
  runs-on`. This is useful when self-hosted runners lack outbound internet access
  for AI detection or when you want to run detection on a cheaper runner."
  The documented pattern: agent job on `[self-hosted, linux, x64]`, detection job
  on `ubuntu-latest`.
- **Confidence**: settled (first-party documentation; YAML example provided)
- **Quote**: "useful when self-hosted runners lack outbound internet access for
  AI detection or when you want to run detection on a cheaper runner"
- **Our assessment**: This is an important operational detail: if your self-hosted
  runner is on a network with restricted outbound access (common in enterprise
  environments), the AI-powered threat detection will fail silently unless the
  detection job is routed to a cloud runner with internet access. Teams that
  deploy airgapped self-hosted runners and don't configure this override will
  lose threat detection silently. For Ch03 (Safety): flag this as a required
  configuration check when deploying gh-aw in network-restricted environments.

### Claim 9: `safe-outputs.runs-on` takes precedence over `runs-on-slim` for safe-output jobs specifically

- **Evidence**: "The `safe-outputs.runs-on` setting still takes precedence over
  `runs-on-slim` for safe-output jobs specifically." This implies a runner
  configuration precedence order: per-job override (`safe-outputs.runs-on`) >
  framework-wide override (`runs-on-slim`) > default (`ubuntu-slim`).
- **Confidence**: settled (first-party documentation; explicit precedence statement)
- **Quote**: "The `safe-outputs.runs-on` setting still takes precedence over
  `runs-on-slim` for safe-output jobs specifically."
- **Our assessment**: Precedence rules across four runner fields add complexity
  to debugging unexpected runner selection. The hierarchy is:
  specific-job override > `runs-on-slim` > platform default. For Ch02: include
  this precedence rule alongside the four-tier architecture diagram so practitioners
  can reason about which field "wins" for each job class.

### Claim 10: Maintenance workflow runner is configured via `runs_on` in `.github/workflows/aw.json`; must re-run `gh aw compile` after any `aw.json` change

- **Evidence**: Two `aw.json` formats are documented — string and array for
  multi-label runner targeting. The note: "Re-run `gh aw compile` after changing
  `aw.json` to regenerate the workflow." The field applies to every job in
  `agentics-maintenance.yml`: close-expired-entities, cleanup-cache-memory,
  run_operation, apply_safe_outputs, create_labels, validate_workflows, and
  activity_report.
- **Confidence**: settled (first-party documentation; explicit compile requirement
  stated)
- **Quote**: "Re-run `gh aw compile` after changing `aw.json` to regenerate the
  workflow."
- **Our assessment**: `aw.json` changes are a common footgun — practitioners
  who update runner configuration in `aw.json` but forget to recompile will
  find the maintenance workflow still using the old runner. This is consistent
  with the broader gh-aw pattern where `aw.json` changes require a compile
  step to take effect (also noted in `docs-ghaw-ephemerals.md` for the
  `action_failure_issue_expires` field). For Ch02: document the `aw.json`
  → compile dependency explicitly, alongside the other cases where forgetting
  to recompile silently applies old configuration.

## Concrete Artifacts

### Runner Configuration: Three `runs-on` Format Variants

```yaml
# String format (single runner label)
---
on: issues
runs-on: self-hosted
---

# Array format (runner must have ALL listed labels)
---
on: issues
runs-on: [self-hosted, linux, x64]
---

# Object format (named runner group with optional label filtering)
---
on: issues
runs-on:
  group: my-runner-group
  labels: [linux, x64]
---
```
*Source: gh-aw Self-Hosted Runners documentation, "runs-on Formats" section*

### Four-Tier Runner Field Architecture

```
Job class                       Config field                              Default
---------                       ------------                              -------
Main agent job                  runs-on: (workflow frontmatter)           ubuntu-latest
Framework/generated jobs        runs-on-slim: (workflow frontmatter)      ubuntu-slim
  (activation, pre-activation,
   safe-outputs, unlock, APM,
   update_cache_memory,
   push_repo_memory)
Threat detection job            safe-outputs.threat-detection.runs-on:    inherits runs-on
Maintenance workflow jobs       maintenance.runs_on in aw.json            ubuntu-slim
  (close-expired-entities,
   cleanup-cache-memory,
   run_operation, apply_safe_outputs,
   create_labels, validate_workflows,
   activity_report)

Precedence for safe-output jobs:
  safe-outputs.runs-on > runs-on-slim > ubuntu-slim (default)
```
*Source: gh-aw Self-Hosted Runners documentation*

### Detection Job Override (Airgap / Cost Optimization Pattern)

```yaml
# Agent job on self-hosted; detection job on cloud runner
---
on: issues
runs-on: [self-hosted, linux, x64]
safe-outputs:
  create-issue: {}
  threat-detection:
    runs-on: ubuntu-latest   # override: cloud runner for AI detection
---
```
*Source: gh-aw Self-Hosted Runners documentation, "Configuring the Detection Job
Runner" section*

### Framework Job Override Pattern

```yaml
# Agent job on self-hosted; all framework jobs also on self-hosted
---
on: issues
runs-on: [self-hosted, linux, x64]
runs-on-slim: self-hosted   # overrides ubuntu-slim for framework jobs
safe-outputs:
  create-issue: {}
---
```
*Source: gh-aw Self-Hosted Runners documentation, "Configuring the Framework Job
Runner" section*

### Shared Import Pattern (runner NOT shared, but network and tools are)

```yaml
# .github/workflows/shared/runner-config.md
---
network:
  allowed:
    - defaults
    - private-registry.example.com
tools:
  bash: {}
---

# Workflow using the shared config:
---
on: issues
imports:
  - shared/runner-config.md
runs-on: [self-hosted, linux, x64]   # must be set here; NOT inherited from import
---
```
*Source: gh-aw Self-Hosted Runners documentation, "Sharing Configuration via
Imports" section*

### Maintenance Workflow Runner Configuration (aw.json)

```json
// Single label:
{
  "maintenance": {
    "runs_on": "self-hosted"
  }
}

// Multiple labels (runner must match all):
{
  "maintenance": {
    "runs_on": ["self-hosted", "linux", "x64"]
  }
}
```

After changing `aw.json`, run `gh aw compile` to regenerate `agentics-maintenance.yml`.

*Source: gh-aw Self-Hosted Runners documentation, "Configuring the Maintenance
Workflow Runner" section*

### AWF Security Stack (as documented)

```
Network egress isolation stack for gh-aw self-hosted runners:

Layer (outermost → innermost):
1. Host-level iptables on Linux kernel DOCKER-USER chain (AWF)
   → Enforces network egress filtering for ALL agent containers on the host
   → Requires root UID (sudo)
   → This is the outer security boundary

2. Container-level iptables
   → Additional network filtering within the container namespace
   → Provides depth behind Layer 1

3. Squid proxy ACLs
   → Application-layer proxy filtering
   → Outbound network permissions configured via allowlist

4. Capability drops
   → Linux capabilities removed from agent container
   → Implements Layer 2 (Runtime Isolation) of the five-layer model

Incompatible configurations:
  - macOS runners (no Docker support matching AWF requirements)
  - Windows runners
  - ARC (Actions Runner Controller) with allowPrivilegeEscalation: false
    → AWF cannot write DOCKER-USER chain rules without host root

Compatible: Linux VM with Docker daemon and sudo access
```
*Source: gh-aw Self-Hosted Runners documentation*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security model): this page
    fills in the concrete runner-level implementation of Layer 2 (Runtime
    Isolation, via capability drops) and Layer 4 (Network Controls, via AWF
    host-level iptables). The conceptual model names the layers; this page
    explains the specific kernel mechanisms that implement them.
  - `docs-ghaw-how-they-work.md` Claim 4 (zero capability by default; tool
    allowlists): the AWF allowlist-controlled egress model is the network
    dimension of the same "zero capability by default, explicit permit" design
    principle. This page gives the infrastructure grounding for that principle.
  - `docs-ghaw-ephemerals.md` Claim 7 (maintenance workflow runner via `aw.json`):
    both pages document the `maintenance.runs_on` field in `aw.json` and the
    requirement to recompile after changing it. This page adds more detail on
    the field format (string vs. array) and the jobs it covers.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claims 3 and 4 (security architecture): the
    abstract five-layer model in that note is given its runner-infrastructure
    implementation here. Together the two notes provide the full picture: the
    design principle (that note) and the deployment reality (this note).
  - `docs-ghaw-ephemerals.md`: the Ephemerals note documents `agentics-maintenance.yml`
    jobs and their configuration in `aw.json`; this note adds the runner selection
    dimension for those same jobs.
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw compile` /
    lock file separation): the compile-required-after-aw.json-change constraint
    in Claim 10 is another instance of the same compilation dependency that note
    first documented. Runner configuration is part of what gets baked into the
    compiled lock file.

- **Contradicts**: None. No existing source note makes claims about AWF,
  self-hosted runner requirements, or the four-tier runner field architecture
  for gh-aw. No contradictions identified.

- **Novel**:
  - **AWF as a named security component with concrete iptables implementation**
    (Claims 1, 3): The Agentic Workflow Firewall name and its DOCKER-USER chain
    mechanism are not documented in any existing source note. `docs-ghaw-how-they-work.md`
    names Layer 4 (Network Controls) abstractly; this is the first note to give
    it a named component and a specific kernel-level implementation.
  - **ARC/Kubernetes incompatibility (`allowPrivilegeEscalation: false` unsupported)**
    (Claim 2): This hard constraint — eliminating the most common Kubernetes runner
    hardening option — is completely new to the corpus. Practitioners evaluating
    gh-aw on Kubernetes ARC runners will hit this and find no documentation of it
    in any prior note.
  - **Four-tier runner field architecture** (Claim 5): The complete mapping of
    four runner fields to four job classes — and the precedence rules — is new
    to the corpus. `runs-on` is mentioned in other notes; `runs-on-slim`, the
    detection job override, and `aw.json` `maintenance.runs_on` are not.
  - **`runs-on` NOT merged from imports** (Claim 6): This specific asymmetry
    in import merge behavior (runner config not inherited; network/tools are)
    is undocumented in any prior note.
  - **Detection job runner override pattern for airgapped runners** (Claim 8):
    The specific failure mode (airgapped self-hosted runner silently disabling
    AI threat detection) and its override pattern are new.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add four-tier runner field diagram** (Claim 5): Any guide section on gh-aw
  self-hosted runner configuration must show all four runner fields and their
  job scope. Setting only `runs-on` is the common error; framework, detection,
  and maintenance jobs each have their own default and their own override.

- **Document `runs-on` import asymmetry as a gotcha** (Claim 6): Add to any
  import patterns section: `network` and `tools` share via imports; `runs-on`
  does not. This is non-obvious and frequently misunderstood by teams trying
  to centralize runner configuration.

- **Platform constraints for self-hosted deployment** (Claims 2, 4): When
  recommending self-hosted runners for gh-aw, document the two hard constraints
  upfront: Linux + Docker only, and no ARC with `allowPrivilegeEscalation: false`.
  Teams running on Kubernetes-based ARC must choose between gh-aw self-hosted
  runner support and Kubernetes pod security hardening.

- **`aw.json` → compile dependency** (Claim 10): Add to the "common compile
  footguns" list: changing `aw.json` (runner config, failure issue expiration)
  requires `gh aw compile` to take effect, just like frontmatter changes.

### Chapter 03: Safety and Verification

- **AWF as the concrete Layer 4 mechanism** (Claims 1, 3): In the five-layer
  security model section, replace the abstract "Network Controls" description
  with the concrete AWF mechanism: host-level iptables on the DOCKER-USER chain,
  layered with container-level iptables and Squid proxy ACLs. Name AWF as the
  outer boundary; explain why it requires sudo.

- **Detection job runner as a safety-critical configuration** (Claim 8):
  Add a safety callout: if deploying gh-aw on airgapped self-hosted runners,
  explicitly configure `safe-outputs.threat-detection.runs-on` to a cloud
  runner with internet access; otherwise, AI threat detection is silently
  disabled. This is the most likely-to-be-missed safety configuration item
  for network-restricted deployments.

- **ARC incompatibility and the Kubernetes tension** (Claim 2): Add a
  discussion of the tradeoff: `allowPrivilegeEscalation: false` is a well-
  motivated Kubernetes hardening option, but it is incompatible with AWF's
  requirement for host-level iptables access. Teams cannot have both AWF
  egress filtering and the standard Kubernetes pod security standard for the
  same runner. Document this as a known architectural tension, not a user error.

## Extraction Notes

1. **Source fills in a significant gap in the security model**: `docs-ghaw-how-they-work.md`
   named Layers 2 and 4 of the five-layer model without explaining the runner-level
   implementation. This page is the implementation complement. The two notes
   should be cited together in any Ch03 discussion of gh-aw security architecture.

2. **Page does not detail Squid proxy ACL configuration or capability drop list**:
   The nested isolation stack is named (iptables + Squid + capability drops) but
   the specific Squid ACL syntax, proxy configuration, and list of dropped
   capabilities are not on this page. A deeper runner-sandbox page or the
   "Sandbox" documentation linked at the bottom of the page would be the next
   place to look for those details.

3. **No publication date**: Documentation page carries no explicit date. Content
   is consistent with gh-aw v0.45+ based on the `runs-on-slim` field being
   documented (introduced alongside the framework job separation in early 2026).

4. **No contradictions filed**: Reviewed all existing source notes. AWF,
   self-hosted runner OS constraints, ARC incompatibility, the four-tier runner
   architecture, and the import non-merge behavior for `runs-on` are all new to
   the corpus. No prior claims to contradict.

5. **Linked documentation not followed**: The page references "Frontmatter",
   "Imports", "Threat Detection", "Network Access", "Sandbox", and "Ephemerals"
   as related documentation pages. "Ephemerals" is already mined as
   `docs-ghaw-ephemerals.md`. "Sandbox" and "Network Access" are not yet in the
   corpus and would be the highest-value next pages to mine for the security
   architecture coverage (they would likely fill in the Squid ACL config and
   the full capability drop list).
