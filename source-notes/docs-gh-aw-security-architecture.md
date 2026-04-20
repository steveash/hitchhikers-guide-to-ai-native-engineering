---
source_url: https://github.github.com/gh-aw/introduction/architecture
source_type: docs
title: "GitHub Agentic Workflows: Security Architecture"
author: GitHub Agentic Workflows team (Peli de Halleux, Don Syme, Mara Kiefer)
date_published: 2026-01-01
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#253"
---

# GitHub Agentic Workflows: Security Architecture

> The official gh-aw security architecture reference: a 3-layer defense-in-depth
> model (Substrate / Configuration / Plan) with concrete components — MCP Gateway
> sandboxing, SafeOutputs write buffering, Agent Workflow Firewall, content
> sanitization, integrity filtering, and secret redaction — that together prevent a
> fully compromised agent from modifying repository state or exfiltrating data.

## Source Context

- **Type**: docs (official security architecture reference page from the GitHub
  Agentic Workflows documentation site, `github.github.com/gh-aw/introduction/architecture`;
  first-party GitHub engineering documentation, not a blog post or changelog)
- **Author credibility**: The gh-aw team (Peli de Halleux — Principal Researcher,
  GitHub Copilot; Don Syme — Distinguished Engineer, creator of F#; Mara Kiefer)
  builds and operates the production gh-aw platform running on `github.com` itself.
  This is a formal architecture document describing production infrastructure, not a
  concept paper. The threat model scoping statements ("explicitly out of scope:
  hardware side-channels and covert channels") indicate rigorous engineering intent.
  Claims here carry high author credibility for the system described; generalizability
  to other platforms requires adaptation.
- **Scope**: Covers the complete security model of the gh-aw runtime: threat model,
  three trust layers, each of the five main security subsystems (MCP Gateway, AWF,
  SafeOutputs, compilation pipeline, content sanitization/integrity/redaction), the
  6-stage job execution flow, and observability artifacts. Does NOT cover: internal
  implementation details of individual scanners (actionlint/zizmor/poutine), how
  the threat detection AI agent is prompted, cost or latency of the security pipeline,
  or the history of how this architecture evolved (see weekly update notes for that).

## Extracted Claims

### Claim 1: A formal 3-layer trust model (Substrate / Configuration / Plan) enforces distinct security properties under different adversary assumptions

- **Evidence**: Architecture reference specifies three layers with named mechanisms
  and explicit failure assumptions for each. Layer 1 (Substrate): GitHub Actions VM
  + kernel + container runtime; kernel-enforced memory isolation, CPU isolation,
  privileged operation mediation. Layer 2 (Configuration): declarative specs bound
  component connectivity and token distribution; failures are misconfigurations or
  overly permissive specs. Layer 3 (Plan): trusted compiler + SafeOutputs; failures
  are workflow-level policy violations.
- **Confidence**: emerging (first-party architecture document; production system,
  but independent security evaluation not available)
- **Quote**: The source describes the layers as providing "memory isolation between
  components, CPU and resource isolation, mediation of privileged operations" at
  Layer 1; treating authentication tokens as "imported capabilities that bound
  components' external effects" at Layer 2; and decomposing workflows into stages
  with bounded permissions at Layer 3.
- **Our assessment**: This is the most architecturally significant claim in the source.
  The three-layer framing is a practitioner-grade defense-in-depth model, not marketing
  copy. The explicit failure-mode specification per layer is what makes it useful:
  Layer 1 fails only if the kernel/hypervisor/hardware is compromised; Layer 2 fails
  if specifications are overly permissive; Layer 3 fails if the compilation or output
  pipeline is bypassed. For Ch02 (Harness Engineering): this three-layer mental model
  is a template for any agent harness design — not just gh-aw. Teams designing
  harnesses should ask "what layer enforces this property?" rather than treating
  security as a single monolithic concern.

### Claim 2: Three privileged containers (network firewall, API proxy, MCP Gateway) constitute the entire Substrate layer — all other containers are untrusted

- **Evidence**: Architecture reference names exactly three privileged containers in
  the substrate layer. All other components — the agent container, MCP server
  containers — run unprivileged under these three mediating containers.
- **Confidence**: emerging (architecture reference is production documentation; the
  privilege topology is explicitly described)
- **Quote**: "Three privileged containers enforce isolation: Network firewall —
  configures connectivity via iptables, launches agent container; API proxy — routes
  model traffic, manages engine-specific credentials; MCP Gateway — configures and
  spawns isolated MCP-server containers."
- **Our assessment**: The three-container privilege topology is a concrete design
  decision: the agent itself is unprivileged. All network traffic, model API calls,
  and MCP tool invocations flow through one of the three privileged containers, each
  of which can enforce policy. For Ch02 (Harness Engineering): this is the production
  answer to "how do you trust your harness but not your agent?" — the harness runs
  privileged; the agent runs sandboxed. Teams building harnesses should position
  all policy enforcement in harness-controlled components, not in agent instructions.

### Claim 3: The MCP Gateway API key mounted into the agent container is explicitly not a strong security boundary against a compromised agent

- **Evidence**: Architecture reference contains an explicit warning: "The MCP gateway
  API key mounted into the agent container is not a strong security boundary against
  a compromised or malicious agent. Keys should be treated as inherently leaked; rely
  on substrate isolation and permission separation instead."
- **Confidence**: settled (explicit architectural disclaimer from the system's own
  documentation)
- **Quote**: "The MCP gateway API key mounted into the agent container is not a strong
  security boundary against a compromised or malicious agent."
- **Our assessment**: This is the most important caveat in the entire document. The
  MCP Gateway provides isolation for MCP *servers*, but the key the agent uses to
  reach the gateway is visible inside the agent container. A compromised agent can
  use that key to reach the MCP Gateway — which is why the gateway's security relies
  on substrate-level container isolation and permission separation, not key secrecy.
  For Ch03 (Safety and Verification): any harness that treats an in-container secret
  as a security boundary against the agent is relying on a false assumption. The
  correct model is "assume the agent can read any secret mounted into its container;
  enforce limits at the substrate and permission layer." This is a direct, citable
  refutation of "just use a different API key to limit the agent's access."

### Claim 4: SafeOutputs buffers all external writes as artifacts before executing them, such that a fully compromised agent cannot directly modify repository state

- **Evidence**: Architecture reference describes the SafeOutputs subsystem: the agent
  job executes with "minimal read-only permissions" and produces `agent_output.json`
  as an artifact. A separate threat detection job analyzes the artifact. Only after
  detection passes do safe output jobs execute with scoped write permissions (`issues:
  write`, `contents: write`). The source states: "even a fully compromised agent
  cannot directly modify repository state."
- **Confidence**: emerging (first-party description of a production mechanism; the
  "fully compromised agent" guarantee requires the substrate layer to be intact)
- **Quote**: "even a fully compromised agent cannot directly modify repository state"
- **Our assessment**: SafeOutputs is the most portable pattern in this document.
  The core insight is decoupling: the agent *describes* its intended writes in a
  structured artifact; a separate, deterministic pipeline *applies* those writes
  after vetting. This means the agent's execution environment never has write
  permissions. For Ch03 (Safety and Verification): this is a production implementation
  of the "verify before commit" principle. The pattern generalizes beyond gh-aw —
  any agent harness can implement a SafeOutputs equivalent by requiring agents to
  emit structured output artifacts and delegating actual execution to a separate
  privileged component. The caveat: "fully compromised" still assumes the substrate
  is intact; a kernel exploit breaks this guarantee.

### Claim 5: The Agent Workflow Firewall (AWF) uses iptables + Squid proxy to enforce domain allowlisting for outbound network traffic from agent containers

- **Evidence**: Architecture reference describes AWF as "containerizing the agent
  within a Docker network and using iptables to redirect HTTP/HTTPS traffic through
  a Squid proxy. The proxy enforces domain allowlisting to prevent data exfiltration.
  AWF drops iptables capabilities before launching the agent."
- **Confidence**: emerging (described in production architecture documentation; specific
  technical mechanisms — iptables + Squid — are concrete implementation details)
- **Quote**: "AWF drops iptables capabilities before launching the agent" (after
  establishing the network policy, so the agent cannot modify its own firewall rules).
- **Our assessment**: Two design details matter here: (1) Squid-based allowlisting
  means the firewall is application-layer (domain names), not just IP-layer — the
  agent cannot exfiltrate data to an IP address by bypassing DNS. (2) Dropping
  iptables capabilities after setup means the agent cannot modify its own network
  policy. For Ch02 (Harness Engineering): this is the production answer to the
  question "how do you prevent an agent from exfiltrating data to an attacker-
  controlled endpoint?" — network-layer isolation with domain allowlisting, applied
  before the agent runs, with the policy capability revoked during agent execution.
  The AWF configuration example (`network.allowed: [defaults, python, node,
  "api.example.com"]`) shows the operator controls the allowlist, not the agent.

### Claim 6: Compilation-time security (actionlint + zizmor + poutine + SHA-pinning) is a security gate, not just a reproducibility mechanism — it runs before any agent step executes

- **Evidence**: Architecture reference describes four compilation-time security checks:
  actionlint (workflow linting + shellcheck + pyflakes), zizmor (security vulnerabilities,
  privilege escalation), poutine (supply chain risks, third-party actions), and SHA
  pinning of all Actions. Output is a validated `.lock.yml`. The command `gh aw compile
  --actionlint --zizmor --poutine` runs all scanners before any workflow execution.
- **Confidence**: settled (these are the published CLI flags and scanner names; the
  compilation step is documented across multiple gh-aw sources)
- **Quote**: "Schema validation, expression allowlisting, and action SHA pinning
  constrain what components load and how they connect" at compile time.
- **Our assessment**: This extends what `blog-gh-aw-operations-release-workflows.md`
  documents about `gh aw compile` as a reproducibility mechanism. Compilation is also
  a security gate: supply chain attacks (poutine), privilege escalation (zizmor), and
  insecure shell expressions (actionlint/shellcheck) are all caught at compile time
  before any agent executes. For Ch02 (Harness Engineering): the compile-then-stage
  model separates the security review phase from the execution phase — a practitioner
  can review the `.lock.yml` and know exactly what Actions, expressions, and
  permissions the workflow will use before running it. The supply chain coverage is
  particularly notable given the Trivy compromise documented in
  `blog-ghaw-weekly-2026-03-23.md` Claim 2.

### Claim 7: Content sanitization neutralizes @mentions, bot triggers, XML/HTML tags, and filters URIs before the agent processes user-generated content

- **Evidence**: Architecture reference enumerates specific sanitization transforms:
  `@user` → `` `@user` `` (mention neutralization); `fixes #123` → `` `fixes #123` ``
  (bot trigger protection); `<script>` → `(script)` (XML/HTML tag conversion);
  HTTPS-only URI filtering from trusted domains, non-compliant → `(redacted)`.
  Plus: content limit (0.5MB, 65k lines), control character removal (ANSI escapes),
  special character normalization.
- **Confidence**: emerging (specific transforms documented in production architecture
  reference)
- **Quote**: Transforms listed with exact before/after examples: "@mention
  neutralization: `@user` → `` `@user` ``"; "bot trigger protection: `fixes #123`
  → `` `fixes #123` ``"; "URI filtering: HTTPS-only from trusted domains;
  non-compliant URLs → `(redacted)`."
- **Our assessment**: This is the prompt-injection defense layer. The @mention
  neutralization is specific to GitHub's agentic surface: an attacker who controls
  an issue comment could write `@copilot do X` to trigger agent behaviors — wrapping
  mentions in code blocks defuses this. The bot trigger protection (`fixes #123`
  becoming inert) prevents an attacker from crafting issue text that would cause the
  agent to close issues or reference commits. The URI filtering prevents exfiltration
  attempts via URLs embedded in user content. For Ch03 (Safety and Verification):
  this is the most concrete, enumerable prompt-injection defense catalog in our
  corpus — each transform addresses a specific attack vector, not a general "sanitize
  inputs" guidance.

### Claim 8: Integrity filtering controls which user content the agent can access based on author trust level (4 levels) and merge status, independently of push access

- **Evidence**: Architecture reference describes four integrity levels: `merged`,
  `approved`, `unapproved`, `none`. The MCP gateway intercepts tool calls and filters
  content below the configured `min-integrity` threshold. Public repositories
  automatically enforce `min-integrity: approved`. Individual users can be blocked;
  trusted reviewers can promote items via approval labels.
- **Confidence**: settled (this is the production configuration API; the four levels
  and public-repo default are documented behavior)
- **Quote**: "Controls agent access based on author trust and merge status rather
  than push access. MCP gateway intercepts tool calls and filters content below
  `min-integrity` threshold."
- **Our assessment**: The independence from push access is the key design insight.
  An org collaborator with push access can still submit a malicious issue comment;
  integrity filtering evaluates the *content's* provenance (was this from a merged
  PR? An approved reviewer?), not just the actor's repo permissions. For Ch03:
  this is a concrete example of content-level trust that is orthogonal to
  permission-level trust — a practitioner principle with wider applicability than
  gh-aw. The corroboration with `blog-ghaw-weekly-mar2026.md` Claim 1 (public repo
  auto-enforcement) and `blog-ghaw-weekly-2026-03-23.md` Claim 3 (migration from
  `lockdown: true` to `min-integrity`) is strong — the weekly updates document
  the evolution of this system from a binary control to a graduated API.

### Claim 9: Secret redaction runs unconditionally (if: always()) after the agent step and before artifact upload, scanning /tmp/gh-aw for any secret values referenced in workflow YAML

- **Evidence**: Architecture reference describes the redaction process: "(1) Scan
  workflow YAML for `secrets.*` patterns; (2) extract secret names; (3) find
  matching files (.txt, .json, .log, .md, .yml) in /tmp/gh-aw; (4) replace exact
  secret values with masked format (first 3 characters + asterisks). Executes
  unconditionally with `if: always()` to protect secrets even if workflow fails
  earlier."
- **Confidence**: emerging (specific mechanism documented; the exact masking format
  and file types covered are concrete implementation details)
- **Quote**: "Replace exact secret values with masked format: first 3 characters +
  asterisks. Executes unconditionally with `if: always()` to protect secrets even
  if workflow fails earlier."
- **Our assessment**: The `if: always()` is critical: a workflow that fails mid-run
  still runs secret redaction before uploading artifacts. This means agent errors,
  panics, or deliberate early exits cannot be used to bypass the redaction gate.
  The first-3-characters + asterisks masking format preserves enough context for
  debugging (which secret is this?) without exposing the full value. For Ch02
  (Harness Engineering): any harness that uploads agent artifacts should apply
  unconditional post-run redaction — not "redact if the run succeeds" but "redact
  always, because failures can leak too." The custom `secret-masking:` configuration
  option means teams can add domain-specific redaction beyond the YAML-declared
  secrets.

### Claim 10: The threat detection job uses a security-focused AI agent to analyze buffered artifacts (agent_output.json, aw.patch, prompt.txt) and can block all safe output execution on failure

- **Evidence**: Architecture reference describes a dedicated "threat detection job"
  that downloads buffered artifacts and invokes a security-focused AI agent. Detection
  checks include secret leakage, malicious code patterns, and policy violations. If
  detection fails, all safe output jobs are prevented from executing. The job runs
  with no write permissions. Custom detection steps are supported, including TruffleHog
  integration.
- **Confidence**: emerging (described in production documentation; the specific AI
  agent prompt for threat detection is not disclosed)
- **Quote**: "Separate detection job downloads buffered artifacts and invokes a
  security-focused AI agent. Detection checks include secret leakage, malicious code
  patterns, and policy violations. Job runs isolated with no write permissions;
  failure prevents all safe output execution."
- **Our assessment**: Threat detection-as-a-separate-job is architecturally important:
  the detection agent has no write permissions and cannot be used to apply the changes
  it is analyzing. The TruffleHog example shows that detection can be augmented with
  specialized tools beyond the base AI scan. For Ch03 (Safety and Verification): the
  pattern here is "use AI to check AI's work, but in a lower-trust context." The
  detection agent's job is adversarial review of the main agent's output — a
  formalization of the "verifier agent" pattern. The caveat: the effectiveness of
  the AI-based threat detection depends on the quality of its prompting and the
  attack surface it covers; the architecture reference does not disclose the detection
  agent's system prompt.

### Claim 11: The formal threat model explicitly excludes hardware side-channel attacks and covert channels — the security model assumes kernel and hypervisor integrity

- **Evidence**: Architecture reference scopes the threat model explicitly: "The system
  assumes an adversary capable of compromising user-level components and executing
  arbitrary code within granted privileges. Hardware compromise and side-channel attacks
  are explicitly out of scope."
- **Confidence**: settled (explicit scope statement in the architecture document)
- **Quote**: "Hardware compromise and side-channel attacks are explicitly out of scope."
- **Our assessment**: This scoping statement is load-bearing for the security
  guarantees. All three layers ultimately depend on the GitHub Actions runner
  infrastructure — if the hypervisor is compromised, none of the container-level
  isolation holds. The Meltdown/Spectre class of attacks could, in theory, bypass
  the memory isolation guarantees of Layer 1. For Ch03: when citing gh-aw's security
  architecture as a model, practitioners must understand that the guarantees are
  conditional on the underlying cloud infrastructure's integrity. This is an honest
  and important limitation statement. It also implies teams running agent workloads
  on shared infrastructure cannot eliminate hardware-level attack surfaces through
  software-only harness design.

### Claim 12: The 6-stage job execution flow (Pre-Activation → Activation → Agent → Detection → Safe Outputs → Conclusion) enforces security at stage boundaries through strict dependency ordering

- **Evidence**: Architecture reference documents the complete job ordering with explicit
  dependency relationships. Pre-Activation: role permission check, deadline validation,
  skip-if-match. Activation: context preparation, event text sanitization, lock file
  validation. Agent: checkout, MCP startup, prompt generation, engine execution, secret
  redaction, artifact upload. Detection: artifact download, AI + custom analysis,
  security verdict. Safe Outputs: issue/comment/PR creation (only if detection passes).
  Conclusion: result aggregation and summary.
- **Confidence**: settled (this is the production execution pipeline; the stage
  dependency structure is documented architecture)
- **Quote**: "Strict dependency order enforces security at stage boundaries."
- **Our assessment**: The stage ordering makes the security model auditable: each
  stage's inputs, outputs, and permission scope are deterministic. The most
  important dependency is Detection → Safe Outputs: safe output jobs cannot start
  until the detection job completes with a passing verdict. For Ch02 (Harness
  Engineering): the staged pipeline model — with explicit permission scopes per stage
  and strict inter-stage dependencies — is the production template for "how do you
  build a harness that maintains security invariants even when the agent is
  compromised?" The pre-activation checks (role permission, skip-if-match) also
  show that authorization happens before any agent code runs, not inside the agent.

## Concrete Artifacts

### 3-Layer Trust Model Summary

```
GitHub Agentic Workflows — Security Architecture
Source: github.github.com/gh-aw/introduction/architecture

LAYER 1 — SUBSTRATE-LEVEL TRUST
  Enforced by: GitHub Actions runner (CPU, MMU, kernel, container runtime)
  Privileged containers (only 3):
    1. Network firewall — iptables policy + Squid proxy; launches agent container
    2. API proxy — routes model traffic, manages engine credentials
    3. MCP Gateway — spawns isolated MCP-server containers
  Guarantees: memory isolation, CPU isolation, privileged operation mediation
  Failure mode: requires kernel/hypervisor/hardware vulnerability
  Explicitly out of scope: hardware side-channels, covert channels

LAYER 2 — CONFIGURATION-LEVEL TRUST
  Enforced by: declarative specs (workflow YAML, firewall policies, MCP configs)
  Auth tokens = "imported capabilities" that bound external effects
  Failure mode: misconfigurations or overly permissive specifications

LAYER 3 — PLAN-LEVEL TRUST
  Enforced by: trusted compiler (gh aw compile) + SafeOutputs subsystem
  Compiler decomposes workflows into stages with per-stage permission scopes
  SafeOutputs buffers all external writes as artifacts before execution
  Failure mode: policy violations in compilation or output pipeline
```

### AWF Configuration Example

```yaml
# Agent Workflow Firewall — network allowlist configuration
engine: copilot
network:
  firewall: true
  allowed:
    - defaults       # GitHub domains + common CI tooling
    - python         # Python package registries
    - node           # npm registry
    - "api.example.com"  # Custom domain allowlist entry
```

### SafeOutputs Permission Separation Flow

```
Agent Job (read-only permissions)
  → Executes agent
  → Produces: agent_output.json artifact
  → Runs secret redaction (if: always())
  → Uploads artifacts

Threat Detection Job (no write permissions)
  → Downloads: agent_output.json, aw.patch, prompt.txt
  → Runs AI security analysis + custom steps (e.g., TruffleHog)
  → Emits: security verdict
  ↓ (only if verdict = pass)

Safe Output Jobs (scoped write permissions)
  Issues workflow:    issues: write
  PR workflow:        contents: write, pull-requests: write
  Comment workflow:   issues: write / pull-requests: write
  → Creates GitHub artifact (issue, PR, comment)

Result: "even a fully compromised agent cannot directly modify
repository state"
```

### Compilation-Time Security Commands

```bash
# Compile workflow spec to validated lock file
gh aw compile

# Compile with all security scanners enabled
gh aw compile --actionlint --zizmor --poutine

# Scanners:
#   actionlint — workflow syntax, shellcheck for run: steps, pyflakes for Python
#   zizmor     — security vulnerabilities, privilege escalation patterns
#   poutine    — supply chain risks, third-party action vetting
# Output: .lock.yml (validated, SHA-pinned executable workflow)
```

### Content Sanitization Transforms (user-generated content)

```
INPUT                     → OUTPUT (agent sees)
───────────────────────────────────────────────────────────
@username                 → `@username`          (mention neutralization)
fixes #123                → `fixes #123`          (bot trigger protection)
<script>alert()</script>  → (script)alert()(script)  (HTML/XML tag conversion)
http://attacker.com/x     → (redacted)            (non-HTTPS URI)
https://evil.io/payload   → (redacted)            (non-allowlisted domain)
[long content]            → truncated at 0.5MB / 65k lines
[ANSI escape sequences]   → stripped

GitHub domains + network.allowed domains pass URI filtering unchanged.
```

### Secret Redaction Process

```
Post-agent, pre-upload (runs with if: always()):

Step 1: Scan workflow YAML for secrets.* references → extract secret names
Step 2: Find files in /tmp/gh-aw matching: *.txt, *.json, *.log, *.md, *.yml
Step 3: Replace each secret value with: first_3_chars + "***..."
         e.g., "ghp_abc123xyz" → "ghp_***"
Step 4: Upload redacted artifacts

Custom masking: secret-masking: configuration block for domain-specific patterns
```

### Integrity Filtering Levels

```
Level       Who qualifies                         Public repo default
───────────────────────────────────────────────────────────────────────
merged      Content from merged commits/PRs       ✓ (included)
approved    Approved PRs, trusted reviewers        ✓ min-integrity default
unapproved  Open PRs, unreviewed contributions    ✗ filtered out
none        No filtering (all content allowed)    ✗ not applied to public repos

Operator controls: blocked-users (always excluded), approval-labels (promote items)
MCP Gateway intercepts tool calls and filters content below configured threshold
```

### 6-Stage Job Execution Flow

```
1. PRE-ACTIVATION
   — Role permission check
   — Deadline validation (has this trigger expired?)
   — Skip-if-match (idempotency gate)
   — Command position check

2. ACTIVATION
   — Context preparation
   — Event text sanitization (content sanitization transforms applied here)
   — Lock file validation

3. AGENT
   — Repository checkout
   — Runtime setup
   — MCP container startup (via MCP Gateway)
   — Prompt generation
   — Engine execution (LLM call)
   — Secret redaction (if: always())
   — Artifact upload (agent_output.json, aw.patch, prompt.txt)

4. DETECTION (no write permissions)
   — Artifact download
   — AI threat analysis + custom steps
   — Security verdict: pass / fail

5. SAFE OUTPUTS (only if detection passes)
   — Create GitHub PR / issue / comment with scoped permissions

6. CONCLUSION
   — Result aggregation
   — Summary generation
```

## Cross-References

- **Corroborates** `blog-gh-aw-operations-release-workflows.md` Claim 4: the
  `gh aw compile` step gains a new dimension from this source. That note documents
  compilation as a reproducibility mechanism (spec → lock file). This source reveals
  it is also a security gate: actionlint, zizmor, and poutine scanners run at compile
  time, and SHA pinning of Actions prevents silent supply chain changes. The compile
  step should be understood as both mechanisms simultaneously: reproducibility **and**
  security vetting.

- **Extends** `blog-ghaw-weekly-2026-03-23.md`: The `min-integrity` breaking change
  (Claim 3 there) and the MCP Gateway `trustedBots` support (v0.62.3) now have formal
  architectural context from this source. The weekly update documented what changed;
  this source documents why the integrity filtering model exists and how the MCP
  Gateway fits into the three-layer trust model. Together they give both the
  architectural rationale and the changelog evolution.

- **Extends** `blog-ghaw-weekly-mar2026.md` (March 18 weekly): Claims 1–2 there
  (visibility-tiered guard policies, write-sink guard for non-GitHub MCP servers)
  are instances of the Configuration-Level Trust layer described here. The formal
  architecture provides the governing principle; the weekly changelog shows how
  specific configuration defaults evolved under that principle.

- **Corroborates** `blog-cursor-security-agents.md` on tiered trust — both
  Cursor's time-based rollout (shadow → inform → gate) and gh-aw's depth-based
  layers converge on the same principle: trust should be proportional to verified
  confidence. However, SafeOutputs (Claim 4 here) is architecturally different from
  Cursor's approach. Cursor uses gradual trust expansion over time; gh-aw uses
  structural permission separation at runtime — the agent never holds write
  permissions regardless of trust level. These are complementary designs, not
  alternatives: time-based trust calibration for rollout; permission separation for
  ongoing runtime safety.

- **Extends** `blog-ghaw-agent-observability.md`: The observability artifacts
  documented there (agent_output.json, aw.patch, prompt.txt, engine logs, firewall
  logs) are produced at Stage 3 of the 6-stage execution flow described here.
  The architecture provides the provenance for what the observability layer consumes:
  artifacts generated during agent execution, before the SafeOutputs stage writes
  anything externally. The observability layer is reading the same artifacts that
  the threat detection job analyzes — same data pipeline, different consumers.

- **Novel**:
  - **The explicit MCP Gateway key caveat** (Claim 3): No other corpus source
    states directly that agent-side API keys are not a strong security boundary.
    This is the first citable, first-party admission that key-based access control
    for MCPs inside agent containers is a false sense of security. The correct model —
    rely on substrate isolation, not key secrecy — is not documented elsewhere.
  - **The SafeOutputs permission separation pattern** (Claim 4): The weekly notes
    reference SafeOutputs as a feature; this is the first source to describe its
    internal mechanics — agent runs read-only, artifact produced, detection runs
    no-write, safe output job runs with scoped permissions. The "fully compromised
    agent cannot modify repository state" guarantee is new to the corpus.
  - **Content sanitization catalog** (Claim 7): The specific enumeration of
    sanitization transforms (mention neutralization, bot trigger protection,
    XML/HTML tag conversion, URI filtering, content limits, ANSI stripping) is the
    most concrete prompt-injection defense inventory in the corpus. No other source
    provides this level of specificity.
  - **Formal threat model with explicit out-of-scope declarations** (Claim 11):
    No other corpus source provides a formal threat model with explicit scoping of
    what is NOT covered. This is the first source to establish that the security
    guarantees are conditional on kernel/hypervisor integrity.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the three-layer trust model (Substrate / Configuration / Plan) as the
    canonical framework for reasoning about harness security. Teams designing
    harnesses should map every security property to a layer: what enforces memory
    isolation (substrate)? What constrains which tools can load (configuration)?
    What prevents irreversible actions (plan/SafeOutputs)?
  - Add SafeOutputs as a named harness pattern: agents emit structured output
    artifacts; a separate privileged component applies external writes after vetting.
    This pattern is portable to any harness, not just gh-aw. The agent should never
    hold write permissions to external systems; the harness should.
  - Add compilation-as-security-gate: the `gh aw compile --actionlint --zizmor
    --poutine` sequence is a concrete template for pre-execution security review.
    Any harness with a "compile" or "build" step should use that step to run security
    scanners, not just resolve dependencies.
  - Add "assume agent-visible secrets are leaked" as a design principle: in-container
    secrets (API keys, tokens) should be treated as known to the agent. Enforce limits
    at the substrate and permission layer, not through key secrecy.

- **Chapter 03 (Safety and Verification)**:
  - Add content sanitization as a first-class prompt-injection defense layer. The
    gh-aw catalog (mention neutralization, bot trigger protection, URI filtering,
    content limits) is the production reference for what "input sanitization for
    agents" looks like in practice.
  - Add integrity filtering (trust by author provenance and merge status, not push
    access) as a concrete trust model for agent-readable content. The four-level
    API (merged / approved / unapproved / none) gives practitioners a vocabulary for
    expressing content trust policies.
  - Add the threat detection job pattern: AI-checks-AI in a lower-trust, no-write
    context. Cite the TruffleHog integration as evidence that specialized tools can
    augment AI-based threat detection.
  - Cite Claim 11 explicitly: all software-only security models are conditional on
    kernel/hypervisor/hardware integrity. Do not overclaim the guarantees of
    container-based agent isolation in the guide.

## Extraction Notes

1. **Source is an architecture reference page**, not a blog post or changelog. It is
   intentionally comprehensive rather than narrative — the extraction covers the full
   page. All major components (AWF, MCP Gateway, SafeOutputs, compilation, content
   sanitization, integrity filtering, secret redaction, threat detection, job flow)
   are documented.
2. **No related sub-pages were followed**: The architecture page is self-contained.
   The gh-aw site has other introduction pages (overview, quickstart) but the
   Prospector specifically identified this architecture page as the source.
3. **Threat detection agent prompt is not disclosed**: The architecture documents
   that a security-focused AI agent analyzes artifacts, but does not disclose its
   system prompt. Confidence for Claim 10 is kept at emerging for this reason.
4. **No contradictions to file**: Reviewed all existing source notes. The formal
   architecture described here is consistent with the feature-level descriptions in
   the weekly update notes. The MCP Gateway key caveat (Claim 3) does not contradict
   any existing note — no corpus source claims agent-side API keys are strong security
   boundaries. The SafeOutputs pattern extends rather than contradicts existing notes.
5. **Cross-reference to weekly notes**: The weekly update notes (`blog-ghaw-weekly-*`)
   document the evolution of specific features (min-integrity API, trustedBots, Trivy
   removal) that appear in this architecture page. This architecture page is the
   formal specification; the weekly notes are the changelog. Both are needed for full
   picture.
