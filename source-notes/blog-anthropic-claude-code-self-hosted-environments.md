---
source_url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
source_type: blog-post
title: "Run Claude Code sessions on your own compute"
author: Anthropic (product announcement)
date_published: 2026-08-06
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: settled
issue: "#2545"
---

# Run Claude Code sessions on your own compute

> August 6, 2026 Anthropic product announcement for self-hosted environments
> for Claude Code (public beta, Team/Enterprise plans): a runner-based
> architecture where customer-operated "runner" processes claim queued cloud
> sessions, clone the repository, and spawn a full Claude Code process on the
> customer's own host, while session orchestration, queueing, and model
> inference stay Anthropic-hosted. The linked documentation (self-hosted
> environments overview, deploy-to-production, and customize-sessions pages)
> supplies the operational detail the blog post omits: a security hardening
> checklist, a full network-egress table, Kubernetes/Compose deployment
> recipes, shutdown/drain timing, and known limitations.

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com
  blog, published August 6, 2026) plus three linked first-party documentation
  pages fetched for depth: the self-hosted environments overview
  (`code.claude.com/docs/en/self-hosted-environments`), the deploy-to-production
  guide (`.../self-hosted-environments-deploy`), and the customize-sessions
  guide (`.../self-hosted-environments-configuration`). All four pages are
  first-party Anthropic sources; the docs pages are technical reference
  material, not marketing, and contain CLI flags, environment variables,
  a Dockerfile, a Kubernetes Deployment manifest, and a full Stop-hook shell
  script.
- **Author credibility**: First-party Anthropic product and documentation
  team. Maximum authority for what the feature is and how it's configured.
  One named customer quote (George Jacob, Senior Engineering Manager,
  company unnamed) — anecdotal weight, single source, company not identified
  in the visible text.
- **Scope**: Covers the self-hosted environments architecture (environment /
  runner / session model), the two runner modes (fixed vs. on-demand),
  data-residency boundaries, network topology, availability/plan
  restrictions, the security hardening checklist for production deployments,
  the full outbound network-requirements table, deployment recipes
  (Dockerfile, Kubernetes, Docker Compose), shutdown/drain semantics, known
  limitations, and the customization surface (wrapper scripts, lifecycle
  hooks, on-demand orchestrator, MCP server config, permission/auto-mode
  behavior for headless sessions). Does NOT cover: pricing details beyond
  "consumes usage the same way," a published pre-built runner image (there
  is none — customers build their own), or benchmarked performance/latency
  numbers for the runner-claim-to-session-start path.

## Extracted Claims

### Claim 1: Self-hosted environments run cloud sessions from any Claude Code surface (web, mobile, desktop, terminal `--cloud`, scheduled routines) on customer-controlled infrastructure instead of Anthropic-hosted infrastructure

- **Evidence**: First-party architectural description naming all supported
  dispatch surfaces.
- **Confidence**: settled (explicit product description)
- **Quote**: "Now in public beta, self-hosted environments let you run Claude Code sessions on your own infrastructure. Start a session from the web, mobile, desktop, or a routine, and it runs inside your network, next to your internal services, toolchains, and security controls, rather than on Anthropic-hosted infrastructure."
- **Our assessment**: This is a distinct product surface from Managed Agents'
  self-hosted sandboxes (`blog-anthropic-claude-managed-agents-selfhosted.md`).
  That announcement covers Anthropic's autonomous/headless agent platform;
  this one covers Claude Code, the interactive coding CLI/product, extended
  to run its cloud-session mode (web, mobile, desktop, routines) on
  customer infrastructure. Both products now offer a "your infrastructure,
  Anthropic's control plane" deployment option, but they are separate
  features shipped four months apart (Managed Agents: 2026-05-19; Claude
  Code: 2026-08-06) with materially different execution splits — see Claim
  3 and Cross-References below.

### Claim 2: Self-hosting has three architectural parts — Environment (named routing destination), Runner (long-lived customer-hosted process), and Session (one Claude Code task) — modeled explicitly on self-hosted CI runners

- **Evidence**: First-party architecture description from the docs overview
  page, with an explicit CI-runner analogy.
- **Confidence**: settled (explicit product architecture documentation)
- **Quote**: "Runner: a program running on hosts inside your network. Runners execute the sessions; the idea is the same as a self-hosted CI runner."
- **Our assessment**: The CI-runner framing is the clearest mental model in
  the source: an Environment is analogous to a GitHub Actions runner group,
  a Runner is analogous to a self-hosted Actions runner process, and a
  Session is one job dispatched to it. This corroborates the general
  industry pattern of "outbound-only worker polls for work" documented for
  a different vendor in `blog-cursor-self-hosted-cloud-agents.md` (Claim 2).

### Claim 3: The full Claude Code process — not just tool/sandbox execution — runs on the customer's runner; only session orchestration, queueing, the claude.ai interface, and model inference stay Anthropic-hosted

- **Evidence**: First-party architecture description, stated twice (overview
  page and "What stays on your infrastructure" section) with consistent
  wording.
- **Confidence**: settled (explicit, repeated architectural claim)
- **Quote**: "the runner claims it, clones the repository the developer chose, and starts a Claude Code process on your host to run it" ... "Session orchestration, queueing, and the claude.ai interface remain Anthropic-hosted: a self-hosted environment moves session execution into your network, not the control plane."
- **Our assessment**: This is a materially different split from Managed
  Agents' self-hosted sandboxes, where "the agent loop that handles
  orchestration, context management, and error recovery stays on
  Anthropic's infrastructure, while tool execution moves to your own
  configured environment" (`blog-anthropic-claude-managed-agents-selfhosted.md`,
  Claim 1). There, only the sandbox (tool execution) is customer-hosted;
  the harness/agent loop stays with Anthropic. Here, the entire Claude Code
  process — which is itself the harness/agent loop for that session — runs
  on the customer's runner; Anthropic's side is reduced to session
  routing/queueing plus the inference API calls the process makes. This is
  architecturally closer to the Cursor self-hosted worker model
  (`blog-cursor-self-hosted-cloud-agents.md`, Claim 3: "Cursor's inference
  engine handles reasoning and generates tool instructions sent to workers
  for local execution") than to Anthropic's own Managed Agents split. This
  is a genuine architectural distinction between two Anthropic products
  covering the same "self-host agent execution" problem differently, not a
  contradiction requiring a filed issue (different products, different
  designs — see MINER.md §4a "when not to file": this is a conditioning
  variable, not a disagreement about the same claim).

### Claim 4: Runners are locked to a single user account for the lifetime of their active sessions, so checked-out code never mixes between developers or accounts

- **Evidence**: First-party lifecycle description, stated in both the
  overview and the hardening checklist.
- **Confidence**: settled (explicit architectural invariant)
- **Quote**: "A runner serves one user at a time. The first session a runner picks up locks the runner to that user, and the runner then runs sessions only for that user, up to a configured capacity. The minimum fleet size is therefore the number of users you expect to be active at once."
- **Our assessment**: This has a direct capacity-planning implication the
  source states explicitly: fleet size must be provisioned per concurrent
  *user*, not per concurrent *session* — a team of 50 engineers with bursty
  usage needs a fleet sized for peak concurrent users, not peak concurrent
  sessions, since one user's multiple sessions share a runner up to
  `--capacity` but a second user's session cannot land on an
  already-locked runner. This is a concrete, non-obvious operational
  planning number worth surfacing in a deployment-sizing guide.

### Claim 5: Two runner scaling modes are supported — fixed fleet (static replica count) and on-demand (a separately-run orchestrator that spawns a runner per queued session via a `spawn-runner` hook and tears it down when work finishes)

- **Evidence**: First-party description of both modes, plus a detailed
  operational contract for the on-demand orchestrator in the
  customize-sessions doc (idempotency on `CLAUDE_RUNNER_ORDER_ID`, exit-code
  contract, `--expected-spawn-seconds` lease).
- **Confidence**: settled (explicit product architecture with CLI-level
  detail)
- **Quote**: "Fixed: you keep a set number running and sessions are distributed across them." / "On-demand: an orchestrator watches for queued sessions, starts a runner as sessions arrive, and stops them when work finishes so capacity tracks demand."
- **Our assessment**: On-demand mode is also the security-preferred mode per
  Claim 7 (credential hygiene), not just a cost-optimization option — the
  source frames it as the production-hardening default, not merely an
  autoscaling convenience. The orchestrator's hook contract (idempotent on
  order ID, must not retry the workload itself, four-tier exit-code
  semantics: 0=submitted, 1=retryable, 2+=non-retryable requiring manual
  admin retry) is detailed enough to be implemented directly from the docs
  without additional vendor support — a maturity signal consistent with a
  public-beta feature aimed at platform engineering teams rather than
  individual developers.

### Claim 6: Data residency is split at the model-inference boundary — repository checkouts, build artifacts, secrets, and session-created files stay on customer infrastructure, but conversation content (prompts, responses, tool results, including code Claude reads) is sent to Anthropic for inference and the transcript is stored by Anthropic

- **Evidence**: First-party data-flow description, stated identically in the
  blog post and the docs overview page.
- **Confidence**: settled (explicit, repeated data-flow claim)
- **Quote**: "Repository checkouts, build artifacts, secrets, and any files a session creates or modifies stay on the machines you provision. The conversation itself, including prompts, responses, and tool results, goes to api.anthropic.com for model inference, and the session transcript is stored by Anthropic so a session can be picked up from any surface."
- **Our assessment**: This is the load-bearing compliance caveat for the
  entire feature: self-hosting does not achieve full data sovereignty.
  Code that Claude *reads* as part of a tool result is explicitly called
  out as leaving the network ("which can include code that Claude reads" —
  blog post framing). Teams evaluating this for regulatory reasons need to
  understand that only checkout/artifact/secret storage is kept local; the
  conversational content of every session — which can include arbitrary
  file contents — still transits to Anthropic. This directly parallels the
  Cursor architecture (`blog-cursor-self-hosted-cloud-agents.md`, Claim 3),
  which draws the same line: execution/data local, inference/reasoning
  cloud-side. Neither vendor offers a self-hosted-inference option for
  their coding-agent product.

### Claim 7: Self-hosted environments are unavailable to organizations with Zero Data Retention (ZDR) enabled, and model inference cannot be routed through Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or an LLM gateway

- **Evidence**: First-party availability/limitations list from the docs
  overview page.
- **Confidence**: settled (explicit product limitation)
- **Quote**: "Zero Data Retention: unavailable for organizations with Zero Data Retention enabled." / "Model inference: sessions use the Anthropic API, and inference can't be routed through Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or an LLM gateway."
- **Our assessment**: This is a hard, non-obvious eligibility gate that
  contradicts an intuitive assumption a compliance-driven team might make:
  "self-hosted" sounds like it should be the *more* restrictive/private
  option, so it might seem compatible with or even a substitute for ZDR.
  The opposite is true — ZDR and self-hosted environments are mutually
  exclusive, because self-hosting still requires Anthropic to process and
  (per Claim 6) store session transcripts for cross-surface resume. Teams
  that need both full data sovereignty *and* zero retention cannot get
  both from this product today. The cloud-routing restriction (no Bedrock/
  Vertex/Foundry/gateway) is also a real constraint for enterprises that
  standardized their model access on one of those channels for billing or
  governance reasons — self-hosted Claude Code sessions must call
  `api.anthropic.com` directly regardless.

### Claim 8: The runner-side security hardening checklist for production deployment covers seven areas: ephemeral per-session containers, no broad credentials baked into the image, keeping the environment secret off session-running hosts, default-deny network egress, least-privilege host IAM, blocking the cloud metadata endpoint, and per-runner filesystem isolation — plus two structural warnings (dispatch is organization-wide; a repo-settings confine guard is needed)

- **Evidence**: First-party, itemized hardening checklist in the
  deploy-to-production doc, framed as mandatory ("work through each item
  before you connect an environment to production systems").
- **Confidence**: settled (explicit operator guidance with concrete
  mechanisms named per item)
- **Quote**: "A self-hosted runner executes arbitrary, model-directed code on your infrastructure on behalf of any member of your Anthropic organization. Work through each item before you connect an environment to production systems:"
- **Our assessment**: This checklist is the single most operationally dense
  artifact in the source and reframes what "self-hosted" means from a
  security posture: the runner host is *not* a trusted boundary by
  default. The two structural warnings are the sharpest findings: (1)
  "Dispatch is organization-wide: any member of your Anthropic organization
  can dispatch a session to any of its environments, and there's no
  per-environment access control on dispatch" — meaning every runner host
  must be treated as reachable by every org member's code, not just the
  team that provisioned it; and (2) the environment secret (the single
  shared credential that registers new runners) lives on every host in a
  fixed fleet, readable by any session's code, unless the team adopts
  on-demand mode specifically to keep it off session-running hosts (see
  Claim 5 and Claim 9). Full text is preserved verbatim in Concrete
  Artifacts below.

### Claim 9: On-demand runners are framed as a credential-hygiene improvement, not just an autoscaling convenience — the environment secret stays only on the orchestrator host, which never runs user code, while each spawned runner receives a single-use work order

- **Evidence**: First-party architectural rationale in the customize-sessions
  doc, directly connected to the hardening checklist's "keep the
  environment secret off session-running hosts" item.
- **Confidence**: settled (explicit security rationale for a specific
  deployment mode)
- **Quote**: "On-demand runners improve credential hygiene. On a fixed fleet, the environment secret lives on every runner host, which is the same host that runs user sessions. With the orchestrator, the environment secret stays only on the orchestrator host, which never runs user code; each spawned runner receives a single-use work order that registers exactly one runner and then expires."
- **Our assessment**: This makes on-demand mode the recommended production
  default rather than a scaling nice-to-have — a fixed fleet is explicitly
  described elsewhere as needing the operator to "treat the
  environment-secret file as readable by every session and rotate the
  secret after any suspected session compromise" (deploy doc, hardening
  checklist), which is a materially worse security posture than the
  single-use work-order model. Teams choosing fixed-fleet for operational
  simplicity should understand they're trading away this specific
  protection, not just accepting a less-elastic scaling model.

### Claim 10: The runner and its sessions make outbound-only connections; Anthropic never connects into the customer's network, and the full egress allowlist is a short, enumerated set of hosts dominated by `api.anthropic.com`

- **Evidence**: First-party network architecture description plus a
  complete network-requirements table (required hosts: `api.anthropic.com`
  and the customer's git host; conditional hosts: `downloads.claude.ai`,
  `storage.googleapis.com`, `code.claude.com`/`claude.com`,
  `*.frame.claudeusercontent.com`, `raw.githubusercontent.com`,
  `registry.npmjs.org`, two Datadog telemetry hosts — each gated by a named
  feature flag or env var that disables it).
- **Confidence**: settled (explicit, itemized network reference table)
- **Quote**: "the traffic to Anthropic, queue polling, the session's event stream, and model inference, is outbound HTTPS to api.anthropic.com, with the short list of further hosts sessions can reach in Network requirements. Anthropic never connects into your network."
- **Our assessment**: This is the same "outbound-only worker" pattern
  documented for Cursor (`blog-cursor-self-hosted-cloud-agents.md`, Claim
  2: "without necessitating inbound port exposure, firewall modifications,
  or VPN configuration") — now confirmed as an Anthropic Claude Code
  pattern too, with a materially more detailed reference table than the
  Cursor source provides (Cursor's post gives no enumerated host list; this
  source gives all required and conditional hosts with the exact env vars
  that suppress each optional one, e.g. `CLAUDE_CODE_BYOC_ENABLE_DATADOG=1`
  gates Datadog telemetry, off by default). The doc also explicitly
  debunks stale guidance: "The runner doesn't reach statsig.anthropic.com,
  *.sentry.io, claude.ai, or platform.claude.com... These hosts appear in
  some older enterprise network checklists, but you don't need to
  allowlist them for runner or session traffic" — useful for any team
  that copies an old Anthropic network-allowlist template.

### Claim 11: Shutdown/drain timing is a fully specified, addable budget — the drain path needs up to `--session-stop-grace-sec` + `--drain-wait-sec` + `--post-session-hook-timeout-sec`, plus 15 seconds fixed overhead, plus 30 more seconds if `--push-outcome-on-release` is set, totaling 80 seconds at defaults — and Kubernetes' default 30-second termination grace period is shorter than this, causing pods to be killed mid-cleanup

- **Evidence**: First-party operational specification with an explicit
  numeric example and an explicit warning about a common misconfiguration.
- **Confidence**: settled (precise, numbered operational specification)
- **Quote**: "The full drain path needs up to --session-stop-grace-sec + --drain-wait-sec + --post-session-hook-timeout-sec, plus 15 seconds of fixed overhead for process cleanup, plus 30 more seconds when --push-outcome-on-release is set. That is 80 seconds at defaults, and the runner logs the total at startup... The Kubernetes default of 30 seconds is shorter than the runner's drain path and will kill the pod mid-cleanup."
- **Our assessment**: This is a specific, verifiable footgun: a team that
  deploys the documented Kubernetes recipe without reading this section and
  overriding `terminationGracePeriodSeconds` will silently lose
  in-progress session cleanup (uncommitted work, post-session hooks) on
  every rolling restart. Notably, the source's own Kubernetes Deployment
  recipe (Concrete Artifacts below) does set `terminationGracePeriodSeconds: 90`
  — the doc practices what it preaches, but only in the copy-pasteable
  YAML, not as a loud top-of-page warning, so a team that hand-rolls their
  own manifest from the prose description alone could easily miss it.

### Claim 12: Two known limitations reduce self-hosted parity with Anthropic-hosted sessions: connector traffic (GitHub, Slack, Linear, etc.) always routes through Anthropic's infrastructure even in a self-hosted environment, and a session that's idle-released or resumed after a runner restart loses any unpushed work by default

- **Evidence**: First-party "Known issues and limitations" section, two
  itemized findings with named workarounds.
- **Confidence**: settled (explicit, first-party limitation disclosure with
  workarounds)
- **Quote**: "Connector tools, such as GitHub, Slack, Linear, and the other claude.ai connectors, are called from Anthropic's side rather than from your runner, so when a self-hosted session uses a connector, that traffic routes through api.anthropic.com, not from inside your network boundary." / "Resumed sessions lose unpushed work: when a session is released, on idle timeout or on a runner restart, and the user sends another message, the session resumes on a fresh runner that clones the repository again from its starting branch, so work the session hadn't pushed is gone."
- **Our assessment**: Both limitations puncture the "everything stays
  inside your network" framing from the marketing blog post. Connector
  traffic is a genuine compliance gap for a team that adopted self-hosting
  specifically to keep *all* tool traffic internal — the workaround (block
  connectors via `allowedMcpServers`/`deniedMcpServers` and run equivalent
  tools as local MCP servers instead) requires the operator to know this
  limitation exists and act on it proactively; it isn't enforced by
  default. The unpushed-work limitation has a real workaround
  (`--push-outcome-on-release`) but that workaround introduces its own
  documented risk: "on resume, the runner fetches the previously pushed
  branch without verifying who pushed it, so anyone with push access to
  those refs can place content into the resumed workspace" — meaning the
  fix for one failure mode (data loss) opens a second one (unauthenticated
  branch injection) unless the operator also restricts push access to
  `claude/*` refs.

### Claim 13: A self-hosted session has no attached terminal, so any tool call that isn't pre-approved stalls the turn until a human responds in the session UI; the default configuration already pre-approves routine calls including Bash, and auto mode should only be enabled on environments that also have default-deny network egress and the rest of the hardening checklist in place

- **Evidence**: First-party operational description directly connecting the
  permission model to the network hardening posture.
- **Confidence**: settled (explicit first-party operational guidance with an
  explicit security precondition)
- **Quote**: "A self-hosted session has no terminal attached, so an unanswered permission prompt stalls the turn until the user responds in the UI... Only enable auto mode on an environment whose session containers run with default-deny network egress and the rest of the hardening section in place. Routine tool calls, including Bash network requests, run without a human in the loop on both the default pre-approved tool set and in auto mode, so the network boundary is what limits where those calls can reach."
- **Our assessment**: This is a precise statement of where the real safety
  boundary sits for headless/self-hosted agent execution: not the
  permission-prompt layer (which is already bypassed for "routine" calls
  including Bash by default), but the network egress layer. This
  corroborates and sharpens the guide's existing framing in
  `guide/06-security-threat-model.md` (Bounding Your Own Agents / Least
  Agency section) — the source makes explicit that for unattended
  execution, network-layer controls are not optional hardening but the
  primary control once Bash is pre-approved, which it is by default even
  outside auto mode.

## Concrete Artifacts

### Security Hardening Checklist (deploy-to-production doc, verbatim)

```
"A self-hosted runner executes arbitrary, model-directed code on your
infrastructure on behalf of any member of your Anthropic organization.
Work through each item before you connect an environment to production
systems:"

- Ephemeral, per-session containers: run each runner process in a fresh
  container or VM that's destroyed when the process exits, with
  --capacity 1 and the default --drain-grace-sec 0 so each container
  serves exactly one session.
- No broad credentials in the image: don't include long-lived SSH keys,
  cloud-provider credentials, or personal access tokens that grant more
  than a session needs. Mint credentials per session from a wrapper
  script instead.
- Keep the environment secret off session-running hosts: prefer
  on-demand runners, where the secret stays on the orchestrator host,
  which never runs user code.
- Default-deny network egress: restrict runner and session container
  outbound traffic at your own network boundary on every environment.
- Least-privilege host IAM: the compute identity attached to the runner
  host should grant only what the runner itself needs.
- Block the cloud metadata endpoint from sessions: IMDSv2 with a hop
  limit of one; GKE Workload Identity with metadata concealment; an
  explicit deny for 169.254.169.254 in the session container's network
  namespace.
- Per-runner filesystem isolation: each runner process gets its own
  working directory that no other process on the host can read or write.
- Dispatch is organization-wide: any member of your Anthropic
  organization can dispatch a session to any of its environments, and
  there's no per-environment access control on dispatch.
- Enforce the repo-settings guard: --confine-repo-settings (warn /
  enforce / off) scans committed repo settings for grants that resolve
  outside the session's workspace, non-empty env blocks, and
  operator-posture overrides like sandbox.enabled: false.

Source: code.claude.com/docs/en/self-hosted-environments-deploy
(section "Harden your deployment")
```

### Network Requirements Table (deploy-to-production doc)

```
Always required:
  api.anthropic.com (443 HTTPS, WSS for SCM connector) — control plane,
    session streaming, model inference, feature flags, JWKS, commit
    signing, git proxy, SCM connector tunnel
  Your git host (443 or 22) — clone/push; not needed if using
    --use-anthropic-git-proxy

Conditionally required:
  downloads.claude.ai (443) — install-time binary fetch; runtime plugin
    installs from official marketplace
  storage.googleapis.com (443) — marketplace plugin catalog fetches,
    Artifact publishing (falls back to api.anthropic.com if blocked)
  code.claude.com / claude.com (443) — claude-code-guide agent doc
    lookups, pre-approved WebFetch
  *.frame.claudeusercontent.com (443) — Artifact tool; disable with
    CLAUDE_CODE_DISABLE_ARTIFACT=1
  raw.githubusercontent.com (443) — changelog/release-notes fetch;
    suppressed by CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
  registry.npmjs.org (443) — plugin/npx MCP server Node deps
  http-intake.logs.us5.datadoghq.com (443) — operational metrics, only
    when CLAUDE_CODE_BYOC_ENABLE_DATADOG=1 (off by default)
  browser-intake-us5-datadoghq.com (443) — error-report uploads;
    suppressed by DISABLE_ERROR_REPORTING=1 or DISABLE_TELEMETRY=1

Explicitly NOT required (despite appearing in some older enterprise
network checklists): statsig.anthropic.com, *.sentry.io, claude.ai,
platform.claude.com, mcp-proxy.anthropic.com

Source: code.claude.com/docs/en/self-hosted-environments-deploy
(section "Network requirements")
```

### Minimal Runner Dockerfile (deploy-to-production doc, verbatim)

```dockerfile
FROM debian:bookworm-slim
ARG CLAUDE_CODE_VERSION
RUN apt-get update && apt-get install -y --no-install-recommends git curl ca-certificates openssh-client \
    && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL "https://downloads.claude.ai/claude-code-releases/${CLAUDE_CODE_VERSION:?set with --build-arg CLAUDE_CODE_VERSION}/linux-x64/claude" \
    -o /usr/local/bin/claude && chmod +x /usr/local/bin/claude
RUN git config --system user.name "Claude" \
    && git config --system user.email "noreply@anthropic.com" \
    && git config --system --add safe.directory '*'
ENTRYPOINT ["claude"]
```

```
docker build --build-arg CLAUDE_CODE_VERSION=2.1.224 -t <your-registry>/claude-runner:latest .
```

Source: code.claude.com/docs/en/self-hosted-environments-deploy
(section "Build the runner image"). Requires Claude Code 2.1.224+.

### Kubernetes Deployment Recipe (deploy-to-production doc, verbatim)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: claude-runner
  namespace: claude-runners
spec:
  replicas: 3
  selector:
    matchLabels:
      app: claude-runner
  template:
    metadata:
      labels:
        app: claude-runner
        app.kubernetes.io/part-of: claude-code-self-hosted-runner
    spec:
      terminationGracePeriodSeconds: 90
      containers:
        - name: runner
          image: <your-registry>/claude-runner:latest
          args:
            - self-hosted-runner
            - --environment-secret-file
            - /etc/claude/environment-secret
            - --capacity
            - "4"
          volumeMounts:
            - name: environment-secret
              mountPath: /etc/claude
              readOnly: true
          ports:
            - name: health
              containerPort: 8080
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 30
      volumes:
        - name: environment-secret
          secret:
            secretName: claude-runner-environment-secret
```

Source: code.claude.com/docs/en/self-hosted-environments-deploy
(section "Kubernetes"). Note the 90-second `terminationGracePeriodSeconds`
— the doc explains elsewhere this must cover the full drain-path budget
(Claim 11); Kubernetes' own default of 30 seconds is too short.

### Stop-hook reference implementation (customize-sessions doc)

```
Purpose: Anthropic-hosted sessions run a built-in Stop hook that nudges
Claude to commit and push uncommitted work before ending a turn. Runners
don't install one by default, so self-hosted sessions can silently leave
uncommitted/unpushed work on the runner's disk (which then either gets
wiped at --capacity 1 reset or deleted with the worktree at higher
capacity). The docs page provides a full POSIX-shell reference
implementation (~70 lines) that:
  - Detects a stop_hook_active re-entry guard to nudge only once per turn
  - Checks `git status --porcelain` (excluding .claude/) for uncommitted
    changes and blocks the stop with a message asking Claude to commit
    and push
  - Checks unpushed commits via `git rev-list HEAD --not <base>
    --remotes=origin --count`, handling both init+fetch (FETCH_HEAD) and
    full-clone (origin/*) checkout styles
  - JSON-escapes the branch name before interpolating it into the
    hand-built hook-output JSON, with an explicit code comment
    identifying the branch name as attacker-influenced input
    ("$branch is attacker-influenced — git-check-ref-format(1) allows
    `"` in ref names... Escape JSON metacharacters before interpolating
    into the hand-built payload so a branch like
    x","continue":false can't inject keys into the hook-output JSON")

Source: code.claude.com/docs/en/self-hosted-environments-configuration
(section "Prompt sessions to push their work")
```

### On-demand orchestrator hook contract (customize-sessions doc)

```
The spawn-runner hook must:
  - Submit work asynchronously and return within --hook-timeout
    (default 60s); must not wait for the runner to boot
  - Be idempotent on CLAUDE_RUNNER_ORDER_ID (redelivery of the same
    request must spawn at most one runner)
  - Not retry the workload itself — Anthropic re-requests with a fresh
    order ID after --expected-spawn-seconds if the runner never
    registers
  - Use a four-tier exit code contract:
      0 = submitted
      1 = retryable failure (session backs off, is re-offered)
      2+ = non-retryable (session blocked until an Owner/admin manually
           selects Retry in the environment's Activity tab)

Source: code.claude.com/docs/en/self-hosted-environments-configuration
(section "The spawn-runner hook")
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-self-hosted-cloud-agents.md` (Claim 2: outbound-only HTTPS
    worker pattern; Claim 3: inference cloud-side / execution local split).
    This source confirms the same two design patterns independently for
    Claude Code: "Anthropic never connects into your network" (Claim 10
    here) matches Cursor's "without necessitating inbound port exposure,
    firewall modifications, or VPN configuration," and the data-residency
    split in Claim 6 here matches Cursor's Claim 3 almost exactly (checkout/
    execution local, conversation/inference cloud-side).
  - `blog-cursor-self-hosted-cloud-agents.md` (Claim 1: enterprise adoption
    blockers are data security and infrastructure access, not model
    quality). This source's "Why self-host" section (Network access,
    Customizability, Compliance) names the same three motivations Cursor's
    named customers gave, from the vendor side rather than the customer
    side.

- **Extends**:
  - `blog-anthropic-claude-managed-agents-selfhosted.md` — both describe an
    Anthropic product now offering customer-controlled execution
    infrastructure with Anthropic-hosted orchestration, but with a
    materially different split (see Claim 3): Managed Agents keeps the
    agent loop/harness on Anthropic's side and moves only the sandbox;
    Claude Code self-hosted environments move the entire Claude Code
    process (harness included) to the runner and keep only
    routing/queueing/inference on Anthropic's side. A reader of this guide
    comparing the two products needs to know these are not the same
    architecture despite similar marketing language ("your infrastructure,
    our control plane").
  - `blog-anthropic-claude-code-routines.md` — routines are named explicitly
    as one of the cloud-session surfaces that can be routed to a
    self-hosted environment ("Start a session from the web, mobile,
    desktop, or a routine"). This source adds the self-hosted execution
    option as a deployment variant for the scheduling layer that note
    documents; a routine's execution location (Anthropic-hosted vs.
    self-hosted environment) is now an independent choice from the
    scheduling model itself.

- **Contradicts**: None filed. Claim 3 documents an architectural
  difference between two Anthropic products (Claude Code vs. Managed
  Agents self-hosting), not a disagreement about the same claim — per
  MINER.md §4a this is a conditioning variable (different product), not a
  contradiction requiring an issue.

- **Novel**:
  - **The environment/runner/session terminology and the explicit
    self-hosted-CI-runner analogy** (Claim 2) — no prior corpus source
    uses this specific vocabulary for Claude Code deployment.
  - **The full production-hardening checklist with named mechanisms**
    (Claim 8) — no prior corpus source (including the Managed Agents and
    Cursor self-hosted notes) provides this level of itemized security
    guidance for an agent-execution host: metadata-endpoint blocking,
    repo-settings confine guard, organization-wide dispatch warning.
  - **The complete outbound network-requirements table with per-host env
    var suppression flags** (Claim 10) — neither the Managed Agents nor
    the Cursor self-hosted notes provide an enumerated host allowlist at
    this granularity.
  - **The fully-specified shutdown/drain timing budget and the explicit
    Kubernetes-default-grace-period warning** (Claim 11) — new to the
    corpus; a concrete, numbered operational gotcha.
  - **The auto-mode / network-boundary-as-real-safety-boundary framing for
    headless sessions** (Claim 13) — sharpens rather than duplicates the
    guide's existing Least Agency framing by naming Bash as pre-approved
    by default even outside auto mode.
  - **The runner-account-lock capacity-planning rule** (Claim 4) — the
    "minimum fleet size is therefore the number of users you expect to be
    active at once" statement is a specific, actionable sizing formula not
    present in either comparison source.

## Guide Impact

- **Chapter 02 (Harness Engineering)** — Permissions/settings.json and
  auto-mode sections: add Claim 13's finding that self-hosted/headless
  Claude Code sessions pre-approve Bash and file edits by default
  regardless of permission mode, and that the real safety boundary for
  unattended execution is network egress control, not the permission
  layer. This is a sharper, more citable version of the existing "Bounding
  Your Own Agents" framing in Chapter 06 and could be cross-linked from
  Chapter 02's `.claude/settings.json` section when discussing
  auto-mode-style unattended configurations.

- **Chapter 06 (Security and Threat Model)** — Bounding Your Own Agents /
  Least Agency section: cite the full hardening checklist (Claim 8) as a
  concrete example of what "least agency" enforcement looks like at the
  infrastructure layer for a real production agent-execution product —
  ephemeral per-session containers, credential minting per session rather
  than baked into images, default-deny egress, metadata-endpoint blocking.
  Also add the "dispatch is organization-wide" finding as a specific
  worked example of the guide's threat-modeling framing: a runner host is
  not scoped to the team that provisioned it, but to the entire Anthropic
  organization, unless the operator explicitly hides Anthropic-hosted
  environments and uses `--lock-to-account`.

- **Chapter 05 (Team Adoption)**: add the capacity-planning rule from
  Claim 4 (fleet size = concurrent *users*, not concurrent sessions) and
  the on-demand-vs-fixed-fleet tradeoff from Claims 5 and 9 (fixed fleet is
  operationally simpler but weakens credential hygiene; on-demand requires
  running a second orchestrator process but keeps the environment secret
  off any host that runs user code) as concrete inputs for a team deciding
  whether and how to adopt self-hosted execution.

- **New chapter opportunity (Deployment/Infrastructure, not yet written)**:
  the Prospector's triage comments repeatedly flagged this source for
  "Ch08/Ch09 Deployment & Infrastructure" — those chapters don't exist yet
  in `guide/` (current chapters are 00–06). If a deployment/infrastructure
  chapter is added, this source note plus
  `blog-anthropic-claude-managed-agents-selfhosted.md` and
  `blog-cursor-self-hosted-cloud-agents.md` together form a strong
  three-vendor/two-product comparison base: self-hosted execution
  architecture, network topology, credential handling, and the
  data-residency boundary each draws between "stays local" and "goes to
  the vendor for inference."

## Extraction Notes

- The blog post itself is short (~400 words of body text) and largely
  marketing framing. The three linked documentation pages
  (`self-hosted-environments`, `self-hosted-environments-deploy`,
  `self-hosted-environments-configuration`) supplied the large majority of
  extractable, citable technical detail and were the primary sources for
  most claims above. Four further linked docs pages exist
  (`self-hosted-environments-quickstart`, `self-hosted-environments-testing`,
  `self-hosted-environments-reference`, `self-hosted-environments-identity`)
  and were not fetched — the reference and identity pages in particular
  likely contain the full CLI flag/env var table and JWT claim reference,
  which would be useful for a follow-up extraction focused specifically on
  implementation detail rather than architecture and security posture.
- All quoted passages were extracted from `html2text`-rendered clean prose
  (converted from the raw fetched HTML) rather than from a summarizing
  WebFetch pass, specifically to guarantee verbatim accuracy per MINER.md
  §2a — an initial WebFetch pass on the blog post returned a paraphrased
  summary that was discarded and not used for any quote in this note.
- The named customer quote (George Jacob, Senior Engineering Manager) does
  not include a company name in the visible page text; the quote is
  attached to a company logo image (Faire) elsewhere in the page markup,
  but since the company name does not appear as text associated with the
  quote, it is treated here as attributed to the individual only, with
  "company unnamed" noted rather than inferring the company from the logo
  asset filename.
- No contradiction issue was filed. The one candidate (Claim 3, the
  architectural split difference from Managed Agents self-hosting) was
  assessed against MINER.md §4a's filing criteria and judged to be a
  conditioning variable (different Anthropic product) rather than a
  same-claim disagreement — see the Cross-References "Contradicts" entry
  for the reasoning.
