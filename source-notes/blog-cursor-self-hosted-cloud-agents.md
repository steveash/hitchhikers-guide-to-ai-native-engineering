---
source_url: https://cursor.com/blog/self-hosted-cloud-agents
source_type: blog-post
title: "Run cloud agents in your own infrastructure"
author: Katia Bazzi (Cursor)
date_published: 2026-03-25
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#180"
---

# Run cloud agents in your own infrastructure

> Cursor's product announcement for self-hosted cloud agents documents a concrete split-brain architecture (cloud inference + on-prem execution via outbound-only HTTPS workers) and three named enterprise customers (Brex, Money Forward, Notion) whose adoption stories reveal that the real blockers to deploying background coding agents at enterprise scale are data security and infrastructure access — not model quality.

## Source Context

- **Type**: blog-post (Cursor product blog, product GA announcement, ~1,000 words, published March 25, 2026)
- **Author credibility**: Katia Bazzi, writing on the official Cursor blog. This is vendor marketing for a product launch — the claims serve a commercial purpose. However, the architecture details (specific Kubernetes CRD name, fleet management API, outbound-HTTPS-only worker pattern) and the three named enterprise customers with attributed quotes are concrete enough to treat as genuine practitioner evidence. The Brex (financial services), Money Forward (regulated fintech), and Notion quotes are attributed to named engineers at named companies — these are not anonymous endorsements.
- **Scope**: Covers the self-hosted worker architecture, deployment options (single command, Kubernetes operator, fleet management API), and enterprise customer stories. Does NOT cover: pricing, performance benchmarks vs. cloud-hosted, failure modes, latency characteristics of the split inference/execution model, how the worker handles intermittent connectivity, or what happens to an in-progress agent session if the worker process dies.

## Extracted Claims

### Claim 1: The primary blockers to enterprise coding agent adoption are data security and infrastructure access — not model quality

- **Evidence**: All three enterprise customer quotes (Brex, Money Forward, Notion) center on the same two concerns: (1) code, credentials, and build artifacts leaving the corporate network, and (2) agents needing access to internal caches, dependencies, and network resources. None of the customers mention model quality as a blocker. The product announcement frames the self-hosted product as specifically addressing these two concerns.
- **Confidence**: emerging (three named enterprise customers is a small sample, but the pattern is consistent and independently corroborated by Shopify's stated blockers in `blog-bvp-shopify-ai-playbook.md`)
- **Quote**: "Your codebase, tool execution, and build artifacts never leave your environment" — Cursor product framing for self-hosted agents.
- **Our assessment**: This is the most strategically important claim in the source. If the bottleneck to enterprise coding agent deployment is trust/control rather than quality, then the path to enterprise adoption is infrastructure architecture (where to run the execution), not model improvement. This reframes the enterprise adoption problem for the guide.

### Claim 2: An outbound-only HTTPS worker pattern eliminates inbound network exposure while preserving full on-prem execution

- **Evidence**: Architecture description: "A worker process establishes outbound HTTPS connectivity to Cursor's infrastructure without necessitating inbound port exposure, firewall modifications, or VPN configuration." The worker runs inside the customer's network and connects out to Cursor's cloud; no traffic flows inward.
- **Confidence**: emerging (vendor-described architecture; the mechanism is technically coherent and is how many enterprise SaaS integrations work in other domains — e.g., CI runners, agent-based monitoring)
- **Quote**: "without necessitating inbound port exposure, firewall modifications, or VPN configuration"
- **Our assessment**: The outbound-only pattern is a well-established enterprise deployment primitive used by CI systems (GitHub Actions self-hosted runners, GitLab runners) and monitoring agents. Applying it to AI coding agents is a direct adoption of that prior art. The architectural implication: enterprises that cannot open inbound ports for security or compliance reasons can still run agent workloads, because the agent reaches out rather than being reached in. This is a concrete design pattern with a name practitioners can use in discussions with security teams.

### Claim 3: The execution model splits inference (cloud-side) from tool execution (on-prem)

- **Evidence**: Explicit description of the operation flow: "Users initiate agent sessions; Cursor's inference engine handles reasoning and generates tool instructions sent to workers for local execution. Results return for subsequent inference iterations."
- **Confidence**: emerging (vendor-described; the split is architecturally clear)
- **Quote**: "Cursor's inference engine handles reasoning and generates tool instructions sent to workers for local execution."
- **Our assessment**: This is the key architectural novelty of the self-hosted pattern. Inference (which model to use, what to reason about) stays in Cursor's cloud. Tool execution (running bash commands, reading files, running tests, accessing internal dependencies) happens on the customer's machine. The customer's code never leaves their environment; the AI's "thinking" still happens externally. This is not full on-premises AI — it is a deliberate split where the data-sensitive part (code execution) stays local while the compute-intensive part (model inference) stays cloud-side. Security teams need to understand this distinction: data sovereignty is achieved at the execution layer, not the model layer.

### Claim 4: Per-session VM isolation — one dedicated VM per agent session with terminal, browser, and desktop environment — enables safe parallelization

- **Evidence**: Product description: "Dedicated machines per agent without resource sharing for improved concurrent execution." Each agent gets its own isolated environment.
- **Confidence**: emerging (vendor-described capability; consistent with how isolation is achieved in other agent systems)
- **Quote**: "Dedicated machines per agent without resource sharing for improved concurrent execution"
- **Our assessment**: Per-session VM isolation solves two problems: (1) safety — an agent session that goes wrong cannot affect other sessions or the host environment; (2) parallelization — multiple agents can run simultaneously without contending for shared resources. The isolation boundary is the VM, not just the process. This is a stronger isolation guarantee than running multiple Claude Code instances in separate tmux sessions (which share the host OS).

### Claim 5: Kubernetes deployment uses a `WorkerDeployment` CRD managed via Helm charts and operators — targeting organizations scaling to thousands of workers

- **Evidence**: Product description: "Kubernetes support through Helm charts and operators with `WorkerDeployment` resource management." The framing targets organizations needing to scale to many concurrent workers.
- **Confidence**: emerging (vendor-described; the Kubernetes CRD name is specific enough to be verifiable)
- **Quote**: "WorkerDeployment resource management"
- **Our assessment**: The existence of a custom Kubernetes operator and CRD (`WorkerDeployment`) signals that Cursor expects enterprise deployments to be managed as infrastructure-as-code alongside other Kubernetes workloads — not as ad-hoc processes. This is a maturity indicator: organizations that deploy via Kubernetes already have GitOps, RBAC, and resource quota tooling that can govern agent worker fleets just like any other service. The Helm chart as entry point lowers the barrier for orgs already running Kubernetes.

### Claim 6: A fleet management API provides non-Kubernetes autoscaling and monitoring for organizations without Kubernetes infrastructure

- **Evidence**: Product description: "Fleet management API for non-Kubernetes environments supporting monitoring and custom autoscaling."
- **Confidence**: anecdotal (single product claim; no specifics on the API surface or autoscaling triggers)
- **Quote**: "Fleet management API for non-Kubernetes environments supporting monitoring and custom autoscaling"
- **Our assessment**: The fleet management API is the escape hatch for organizations that cannot or will not run Kubernetes. It allows programmatic control of worker pools without the Kubernetes operator. The "custom autoscaling" description implies the API exposes enough state (active sessions, worker capacity) to drive scaling decisions from external orchestration. This is architecturally sound but underdeveloped in the source — no specifics on the API protocol, authentication, or what metrics are exposed.

### Claim 7: Single-command deployment (`agent worker start`) lowers the adoption barrier for individual or small-team self-hosting

- **Evidence**: Product description of deployment options, with `agent worker start` listed as the entry point for single instances.
- **Confidence**: anecdotal (vendor claim; not independently verified)
- **Quote**: "Single command activation: `agent worker start`"
- **Our assessment**: The single-command path is the developer-experience entry point. It allows a team to try self-hosting without Kubernetes infrastructure overhead. The progressive deployment model (single command → Kubernetes operator) follows the same "start simple, scale to infrastructure" pattern as other enterprise tools. The practical question — what does the worker process need to run? (Docker? specific OS? outbound internet?) — is not answered in the source.

### Claim 8: Brex (financial services) uses self-hosted agents to access internal tool validation infrastructure for complete software build delegation

- **Evidence**: Named customer quote from Graham Fuller, Senior Software Engineer at Brex: "Cursor cloud agents excel at code development using our codebase context. Self-hosted capability grants infrastructure access for test execution and internal tool validation, enabling complete software build delegation."
- **Confidence**: anecdotal (single practitioner quote from a named engineer at a named company; represents Brex's experience, not a controlled study)
- **Quote**: "Self-hosted capability grants infrastructure access for test execution and internal tool validation, enabling complete software build delegation."
- **Our assessment**: The Brex quote is specifically about what self-hosting enables that cloud-hosting cannot: access to internal test execution infrastructure and validation tooling. "Complete software build delegation" — delegating an entire build to an agent — is a significant capability claim. The key enabling factor is the agent's ability to run tests against internal dependencies that Cursor's cloud would not have access to. This is the clearest practitioner statement in the source that the execution layer (access to internal infra) is the real unlock, not the model.

### Claim 9: Money Forward (~1,000 engineers, regulated fintech) is enabling a PR-from-Slack workflow for its entire engineering org via self-hosted agents

- **Evidence**: Named customer quote from Yokoyama Tatsuo, Deputy Manager SRE & MEPAR at Money Forward: "As a financial services organization with stringent security protocols, self-hosted support addresses critical needs. We're establishing workflows enabling approximately 1,000 engineers to generate pull requests via Slack integration."
- **Confidence**: anecdotal (named practitioner; the workflow is described as in-progress, not complete — "we're establishing")
- **Quote**: "We're establishing workflows enabling approximately 1,000 engineers to generate pull requests via Slack integration."
- **Our assessment**: The PR-from-Slack workflow at ~1,000 engineer scale is the most specific enterprise deployment pattern in the source. The workflow: engineer sends a request via Slack → agent picks it up, runs in the self-hosted worker, creates a PR. This is a concrete enterprise-scale background agent pattern that bypasses the requirement for engineers to run agents interactively. The "we're establishing" language indicates this is not fully deployed at the time of writing — it is an in-progress rollout. The financial services context (Money Forward) is significant: the self-hosted architecture is specifically what enables a regulated fintech to participate at all.

### Claim 10: Notion's framing of self-hosted agents as "enterprise readiness advancement" centers on safer tool access and eliminating multiple technology stacks

- **Evidence**: Named customer quote from Ben Kraft, Software Engineer at Notion: "Self-hosted cloud agents represent meaningful enterprise readiness advancement. Operating agent workloads within our cloud infrastructure enables safer tool access and eliminates maintaining multiple technology stacks."
- **Confidence**: anecdotal (single practitioner quote)
- **Quote**: "Operating agent workloads within our cloud infrastructure enables safer tool access and eliminates maintaining multiple technology stacks."
- **Our assessment**: Notion's framing introduces a second operational benefit beyond security: operational simplicity. Running agent workloads within their own cloud infrastructure means they use their existing logging, monitoring, access controls, and deployment tooling — not Cursor-specific management interfaces. The "multiple technology stacks" pain is real for teams that currently run agents with different toolchains in different environments. The enterprise readiness framing (from a software engineer, not a CTO) suggests this is a ground-level practitioner concern, not just an executive talking point.

### Claim 11: Self-hosted agents have feature parity with cloud-hosted agents, including multi-model support, MCPs, subagents, rules, and hooks

- **Evidence**: Product description: "identical functionality to cloud-hosted variants," with explicit enumeration of Composer 2 support, MCPs, subagents, rules, and hooks.
- **Confidence**: anecdotal (vendor claim at GA; feature parity at launch does not guarantee future parity as products evolve)
- **Quote**: "Self-hosted cloud agents provide identical functionality to cloud-hosted variants"
- **Our assessment**: Feature parity is the expected baseline for a GA product, but worth noting as it was not guaranteed at early availability. The explicit enumeration of MCPs, subagents, rules, and hooks confirms that the full agent toolchain is available in the self-hosted deployment — enterprises are not trading capability for security.

## Concrete Artifacts

### Self-Hosted Worker Architecture

```
Cursor Self-Hosted Cloud Agent Architecture (March 2026)

Customer's network:
  ┌─────────────────────────────────────────────────┐
  │  Worker process                                  │
  │  ├── Terminal environment                        │
  │  ├── Browser environment                         │
  │  ├── Desktop environment                         │
  │  ├── Access to internal caches/dependencies      │
  │  └── Outbound HTTPS to Cursor cloud only         │
  └─────────────────────────────────────────────────┘
                      │ outbound HTTPS
                      ▼
Cursor cloud:
  ┌─────────────────────────────────────────────────┐
  │  Inference engine (reasoning + tool instructions)│
  │  ├── Composer 2 or other frontier models         │
  │  └── Routes tool instructions → worker           │
  └─────────────────────────────────────────────────┘

Security properties:
  - No inbound ports opened on customer network
  - No firewall modifications required
  - No VPN configuration required
  - Code, credentials, build artifacts never leave customer environment
  - Inference (model weights, reasoning) stays cloud-side
```

### Deployment Options

```bash
# Single instance (entry-level)
agent worker start

# Kubernetes (fleet-scale via Helm chart + operator)
# WorkerDeployment CRD manages worker pool lifecycle
helm install cursor-worker cursor/agent-worker

# Non-Kubernetes (fleet management API)
# Exposes monitoring and custom autoscaling hooks
```

### Enterprise Customer Deployment Patterns

```
Brex (financial services):
  Use case: internal tool validation, test execution
  Capability unlocked: complete software build delegation
  Key requirement: access to internal build infrastructure

Money Forward (regulated fintech):
  Scale: ~1,000 engineers
  Workflow: PR-from-Slack (engineer requests via Slack → agent creates PR)
  Key requirement: financial services compliance (code cannot leave network)
  Status: in-progress rollout at time of writing (March 2026)

Notion:
  Use case: agent workloads within own cloud infrastructure
  Benefits: safer tool access, eliminated multiple tech stacks
  Key requirement: use existing logging/monitoring/access controls
```

### Security/Compliance Split

```
What stays in customer's environment:
  ✓ Code files and repositories
  ✓ Build artifacts
  ✓ Credentials and secrets
  ✓ Test execution and results
  ✓ Internal dependency access

What stays in Cursor's cloud:
  ✓ Model inference (reasoning)
  ✓ Tool instruction generation
  ✓ Session orchestration

What this means for compliance:
  → Data sovereignty achieved at execution layer, not model layer
  → Regulated industries can satisfy requirements without on-prem AI
  → Audit trail for code changes remains within customer's systems
```

## Cross-References

- **Corroborates**: `blog-cursor-security-agents.md` — Cursor's internal security agent fleet (Agentic Security Review, Vuln Hunter, Anybump, Invariant Sentinel) demonstrates that Cursor's own engineering team runs agent workloads at production scale. This self-hosted product gives enterprise customers the same underlying infrastructure capability Cursor uses internally. The shared MCP coordination substrate pattern in the security agents note (MCP as Lambda providing persistence and deduplication) is architecturally complementary to the self-hosted worker pattern — both are about giving agents stable execution environments with controlled external state.

- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` — Shopify's LLM proxy as "meta-harness" addresses the same enterprise concern from the other direction: Shopify built their own layer of control and routing above client tools; Cursor's self-hosted workers give enterprises execution-layer control below the model. Both converge on the same insight: enterprise AI adoption blockers are trust and control architecture, not model quality. Shopify's "not yet at the place where we allow AI to check in code automatically" and Cursor's PR-from-Slack workflow are different maturity points on the same spectrum — Shopify retains human merge approval; Money Forward's workflow creates PRs for human review, not autonomous merges.

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` (Claim 4, Agent Teams + tmux isolation) — Osmani's per-session isolation principle (separate context per agent, no shared state) is implemented at the infrastructure level here: each self-hosted worker gets a dedicated VM. The isolation primitive scales from tmux sessions (local, lightweight) to VMs (cloud, heavier) as deployment scope grows. Both reach the same design conclusion from different starting points.

- **Extends**: `discussion-hn-ttal-multiagent-factory.md` — TTal's two-plane architecture (persistent Manager + ephemeral Worker plane) describes the same logical separation at the tooling layer that Cursor implements at the product layer: a cloud-side coordination/inference plane and a local execution plane. TTal's Workers get isolated git worktrees; Cursor's workers get isolated VMs. The structural pattern is the same; the infrastructure layer is different. Cursor's product is the enterprise-grade, vendor-managed instantiation of the pattern TTal builds by hand.

- **Extends**: `blog-anthropic-harness-long-running.md` — The Anthropic harness post documents a split execution model for a different reason: generator vs. evaluator roles. The Cursor self-hosted architecture adds a second axis of splitting: inference location vs. execution location. Both sources demonstrate that distributing agent workloads across multiple computational contexts is an emergent architectural pattern, not a corner case.

- **Novel**: The following are not documented in any other source note:
  - **Outbound-only HTTPS worker as a named enterprise deployment primitive**: No other source describes this specific pattern for AI coding agents. It is common in CI (GitHub Actions self-hosted runners) but novel in the agent context.
  - **Data sovereignty through execution-layer splitting**: The specific design choice to keep inference cloud-side and execution on-prem — rather than full on-prem AI — is not documented elsewhere in the corpus. It resolves the tension between enterprise compliance requirements and the cost of running frontier models on-prem.
  - **WorkerDeployment Kubernetes CRD for agent fleet management**: No other source documents a vendor-defined Kubernetes custom resource for agent infrastructure.
  - **PR-from-Slack at ~1,000 engineer scale**: The Money Forward workflow (engineer requests via Slack → agent creates PR) at this scale is the largest-scale background agent deployment pattern in our corpus.
  - **Feature parity argument as enterprise readiness signal**: The explicit claim that self-hosted agents have feature parity with cloud-hosted (MCPs, subagents, hooks, multi-model) is a new dimension of "enterprise readiness" — enterprises are not trading capability for security.

## Guide Impact

- **Chapter 04 (Agent Infrastructure / Deployment)**: This source should anchor any section on enterprise agent deployment with the self-hosted worker architecture. Extract the outbound-only HTTPS pattern as a named design primitive — "enterprise coding agents follow the CI runner pattern: workers connect out, not in." The WorkerDeployment CRD and fleet management API show the two scaling paths (Kubernetes-native vs. API-driven). The three deployment tiers (single command → Kubernetes → fleet API) map the full adoption spectrum from individual to org-scale. The PR-from-Slack workflow (Money Forward) is the canonical enterprise-scale background agent pattern for this chapter.

- **Chapter 06 (Enterprise AI Adoption)**: Lead the adoption blockers section with the finding from this source: the three named enterprises all cite security (data leaving the network) and infrastructure access (internal caches/dependencies) as their blockers — not model quality. This fundamentally reframes the "how do we get enterprises to adopt coding agents?" question: the work is infrastructure architecture, not model improvement. Use the Brex/Money Forward/Notion testimonials as the practitioner validation. Pair with `blog-bvp-shopify-ai-playbook.md`'s LLM proxy pattern for a complete picture of enterprise control architectures.

- **Chapter 07 (Security and Compliance for AI Agents)**: The inference/execution split is the canonical answer to "how can we use AI coding agents without our code leaving the building?" The security chapter should describe this pattern with the Cursor architecture as the primary example: inference cloud-side (model weights, reasoning, tool instructions), execution on-prem (bash, file access, tests, internal dependencies). This is not full on-prem AI — it is selective data sovereignty at the execution layer. Add the compliance framing: regulated industries (financial services: Brex, Money Forward) can satisfy requirements through execution-layer controls without waiting for on-prem model inference.

## Extraction Notes

- Source is a product launch blog post — inherently marketing, but with three named enterprise customers and specific architectural descriptions that provide genuine evidence. Treat customer quotes as practitioner evidence at anecdotal confidence; treat architectural claims as emerging confidence given their technical specificity.
- The blog post is short (~1,000 words). The architectural description is high-level. Key gaps not answered by the source: latency of the inference/execution round-trip, behavior when the worker loses connectivity mid-session, worker resource requirements, and whether the fleet management API is REST/gRPC/WebSocket.
- Money Forward's workflow is described as in-progress at writing time ("we're establishing") — the quote documents intent and early deployment, not a completed rollout. Treat as an in-progress enterprise deployment, not a validated at-scale pattern.
- The source does not describe failure modes or limitations of the self-hosted architecture. The Prospector's triage note explicitly identifies this as high-novelty content; the extraction reflects that assessment.
- Related blog posts linked from the source (computer-use agents, build-agents-automatically, Bugbot Autofix) were not fetched for this extraction — they address different product features and would be separate source submissions if they contain novel claims.
