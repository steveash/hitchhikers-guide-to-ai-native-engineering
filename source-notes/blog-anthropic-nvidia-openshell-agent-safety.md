---
source_url: https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
source_type: blog-post
title: "Giving companies more control over their AI agents, with NVIDIA"
author: Anthropic (no individual byline)
date_published: 2026-09-28
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: emerging
issue: "#3782"
---

# Giving companies more control over their AI agents, with NVIDIA

> Anthropic describes a layered, independently enforced agent-control stack: Managed Agents (credential vault, separate agent loop and sandbox, audit trails) plus NVIDIA's open-source OpenShell runtime (default-deny policy enforced outside the agent, decision logs, a policy prover), announced alongside NVIDIA's Open Agent Safety Platform.

## Source Context

- **Type**: blog-post (product/partnership announcement, ~5 min read, category Agents / Claude Platform)
- **Author credibility**: First-party Anthropic vendor post. Authoritative on Managed Agents architecture; the OpenShell claims are Anthropic's summary of NVIDIA's product, and the post contains no benchmarks or independent verification.
- **Scope**: Covers the layering model, Managed Agents' credential and sandbox separation, OpenShell's policy model, a feature list, three customer one-liners (Notion, Rakuten, Asana) and availability. It does not describe policy syntax, the prover's guarantees or limits, performance overhead, or the internals of the "Open Agent Safety Platform" (NVIDIA's announcement, not linked in detail).

## Extracted Claims

### Claim 1: Agent controls should be layered, with each layer enforcing its limits independently
- **Evidence**: Architectural statement; no incident data or testing.
- **Confidence**: emerging
- **Quote**: "Each layer is designed to enforce its limits independently, so protection doesn't depend on any single layer."
- **Our assessment**: Defense-in-depth framing. Model-internal safeguards are layer one; external limits on what the agent does are layers two and three. The useful point is that external layers must not rely on the model behaving. "Designed to" is a design intent, not a demonstrated property. Also says layers are modular ("companies can adopt the ones that fit their setup").

### Claim 2: The more access an agent has, the more control and checking the company needs
- **Evidence**: Motivating assertion.
- **Confidence**: settled (widely shared premise)
- **Quote**: "The more access an agent has, the more its company needs to control and check what it does."
- **Our assessment**: Sets the frame: as models improve, agents receive more access, so control must scale with capability. Consistent with the identity note's argument that per-user ACLs break down as autonomy grows.

### Claim 3: Managed Agents keeps credentials in a vault so the agent never sees them
- **Evidence**: Architecture description, stated in the intro and again in the Managed Agents section.
- **Confidence**: emerging
- **Quote**: "Credentials, meaning passwords and access keys, are held in a separate vault, so the agent never sees them."
- **Our assessment**: Restates the credential-isolation property already documented in earlier Managed Agents notes; here it is packaged as one layer of a larger stack. Not independently verifiable from outside.

### Claim 4: The agent loop runs on a separate server from the sandbox
- **Evidence**: Architecture description.
- **Confidence**: emerging
- **Quote**: "With Managed Agents, the agent loop runs on a separate server from the sandbox, the isolated environment where the work happens."
- **Our assessment**: Matches the brain/hands decoupling in the engineering post; here it is framed as a security boundary rather than a latency/reliability win.

### Claim 5: Managed Agents provides audit trails and integrates with existing access controls; sandbox is bring-your-own
- **Evidence**: Feature statement only.
- **Confidence**: emerging
- **Quote**: "Managed Agents also provides audit trails, which record what each agent did, and integration with a company's existing access controls."
- **Our assessment**: Audit trail plus enterprise IAM integration is the baseline governance ask. The post gives no detail on log format, retention or export. Adjacent claim in the post: "Companies can bring their own sandbox setup and choose where and how it runs."

### Claim 6: OpenShell is default-deny and enforces policy outside the agent
- **Evidence**: Product description of NVIDIA open-source software (Apache 2.0).
- **Confidence**: emerging
- **Quote**: "OpenShell blocks everything unless a rule allows it."
- **Our assessment**: The key harness design principle: allowlist, not denylist. Related quote: "The rules are enforced outside the agent, and OpenShell logs every decision it allows or blocks." Logging allowed and blocked decisions matters because the blocked-log is the input to the tightening workflow in Claim 7. Rules cover "files, network connections and data the agent accesses".

### Claim 7: Recommended workflow: start narrow, review the log, use Claude to tighten toward least privilege
- **Evidence**: Recommended practice; no case study or metrics.
- **Confidence**: anecdotal
- **Quote**: "Teams can start with narrow permissions, review the log, and use Claude to tighten the rules toward the least access a task needs."
- **Our assessment**: A concrete iterative loop for permission policy authoring, using the model itself as a policy-refinement assistant. Note the tension: the model helps write the rules constraining it, mitigated by the human review step and Claim 8's prover. Worth adding as a named pattern; needs practitioner evidence.

### Claim 8: A policy prover uses mathematical proof to confirm what an agent can reach under the written rules
- **Evidence**: Vendor feature claim; no detail on scope.
- **Confidence**: anecdotal
- **Quote**: "OpenShell's policy prover then uses mathematical proof to confirm what the agent can reach under the rules the team wrote."
- **Our assessment**: Novel to our corpus and potentially significant (verifying reachability rather than testing), but it proves properties of the rules, not agent behavior, and the post does not say what threat model, abstractions or limits apply. Treat as unverified until NVIDIA docs are mined.

### Claim 9: Customers can limit, review, and confirm limits are in place
- **Evidence**: Summary of the combined offering.
- **Confidence**: emerging
- **Quote**: "Customers who are using Managed Agents with OpenShell can limit what an agent can do, review what the agent did and confirm that the limits are in place."
- **Our assessment**: A tidy three-verb governance model: limit (policy), review (audit/logs), confirm (prover). Useful as a checklist for agent-governance sections.

### Claim 10: Managed Agents bundles orchestration, long-running sessions and governance
- **Evidence**: Feature list.
- **Confidence**: emerging
- **Quote**: "Long-running sessions that operate autonomously for hours, with progress and outputs that persist even through disconnections."
- **Our assessment**: Feature list also includes multi-agent orchestration ("agents can spin up and direct other agents to parallelize complex work") and "Trusted governance ... scoped permissions, identity management, and execution tracing built in." Marketing-level; corroborated in more depth by earlier Managed Agents notes.

### Claim 11: Customer usage examples (Notion, Rakuten, Asana)
- **Evidence**: Brief vendor-reported anecdotes, no metrics.
- **Confidence**: anecdotal
- **Quote**: "Rakuten runs specialist agents across engineering, product, sales, marketing, and finance, each deployed within a week."
- **Our assessment**: "Each deployed within a week" is the only quantitative claim and is unsourced. Notion: "Dozens of tasks can run in parallel while the team works on the results together."

## Concrete Artifacts

No code or config is given. The layered stack described (attribution: Anthropic post, restructured by us):

```
Layer 1  Model-internal safeguards
Layer 2  Claude Managed Agents: agent loop on separate server from sandbox;
         credentials in separate vault; audit trails; existing access-control integration
Layer 3  NVIDIA OpenShell (Apache 2.0): default-deny; checks each tool use;
         rules on files / network / data; enforced outside agent;
         logs every allow/block; policy prover
Workflow: narrow permissions -> review log -> Claude tightens rules -> prover confirms reach
```

Availability quote: "It can operate in a sandbox you control either running on your own infrastructure, or with a managed provider."

## Cross-References

- **Corroborates**: blog-anthropic-scaling-managed-agents.md Claim 7 (credentials never accessible from the sandbox) and Claim 2 (session/harness/sandbox split); blog-anthropic-agent-identity-access-model.md Claim 8 (credentials stored independently, injected at the network boundary) and Claim 10 (dual audit trail); blog-anthropic-agent-identity-access-model.md Claim 11 (minimal-footprint start, refined via audit review) parallels Claim 7 here.
- **Contradicts**: None found.
- **Extends**: blog-anthropic-claude-managed-agents-selfhosted.md Claim 1 and Claim 2 (bring-your-own sandbox) by adding a policy-enforcement runtime (OpenShell) inside the customer sandbox; blog-anthropic-managed-agents-scheduled-vaults.md Claim 4 (vault-injected credentials).
- **Novel**: Default-deny external policy runtime (OpenShell) paired with Managed Agents; the "policy prover" (formal reachability confirmation); the NVIDIA Open Agent Safety Platform reference design; the framing of independent, modular, layered enforcement; Claude-assisted least-privilege tightening from logs.

## Guide Impact

- **Chapter 06 (Security & Threat Model)**: Add the layered-control model (model safeguards / credential vault + loop-sandbox separation / external default-deny runtime) as a named architecture, citing this note with the scaling-managed-agents note. Add "allowlist by default, enforced outside the agent, log both allows and blocks."
- **Chapter 02 (Harness Engineering)**: Add the iterative permission-tightening loop (Claim 7) as a harness-configuration practice; flag as vendor-recommended and unvalidated.
- **Chapter 05 (Team Adoption)**: The limit/review/confirm framing (Claim 9) can seed an enterprise governance checklist. Mark policy-prover claims as unverified pending NVIDIA documentation.

## Extraction Notes

- Read the full page (fetched via curl and stripped of HTML; the post is short, ~5 min). All quotes were copied from that text. No sub-pages followed: links to OpenShell on GitHub and NVIDIA's developer page were not fetched, so OpenShell details are second-hand via Anthropic.
- Source is thin on specifics (no metrics, no policy examples); confidence kept at `emerging`.
- Triage comments listed an "Open Agent Safety Platform" from Anthropic; the post attributes that platform to NVIDIA, with Anthropic as collaborator.
