---
source_url: https://claude.com/resources/articles/self-hosted-claude-managed-agents
source_type: blog-post
title: "Operate Claude Managed Agents inside your security perimeter"
author: Anthropic (product announcement)
date_published: 2026-11-12
date_extracted: 2026-11-14
last_checked: 2026-11-14
status: current
confidence_overall: anecdotal
issue: "#4720"
---

# Operate Claude Managed Agents inside your security perimeter

> November 12, 2026 Anthropic announcement (private beta) that the entire Managed Agents service (harness, sandboxes, credentials, session history) can run in the customer's own cloud or on-premise, restated around four security principles; all claims are vendor-stated with no metrics or customer evidence.

## Source Context

- **Type**: blog-post (first-party Anthropic product announcement, claude.com resources, "Product updates", 5 min read)
- **Author credibility**: Anthropic is authoritative on what the product does and how it is scoped. The post is product description only: no metrics, no customer quotes, no practitioner validation. Treat everything as vendor claims about a private-beta product.
- **Scope**: Covers (1) the move from self-hosted sandboxes to a fully self-hosted control plane, (2) what the customer operates, (3) model-request routing and ZDR, (4) four security principles. Does NOT cover: architecture details, setup steps (deferred to docs), pricing, limitations, security failure modes, or how a customer enforces each principle (e.g. firewall rule examples). Docs link not followed (article only references it).

## Extracted Claims

### Claim 1: Self-hosted Managed Agents moves the whole service into the customer's environment, not just the sandbox
- **Evidence**: First-party product description; private beta. No deployment data.
- **Confidence**: emerging (explicit product statement, unvalidated in practice)
- **Quote**: "every part of the service runs in your own cloud or on-premise, including the harness, sandboxes, credentials, and session history."
- **Our assessment**: This is the new step beyond the May 2026 self-hosted sandboxes (orchestration stayed with Anthropic there; see blog-anthropic-claude-managed-agents-selfhosted.md Claim 1). The harness loop itself now runs inside the perimeter. Taken at face value; we have no way to verify what residual Anthropic-side dependencies exist beyond model calls.

### Claim 2: The customer operates three components: the Managed Agents server, its database, and the workers that run shell/file tools
- **Evidence**: Stated operational boundary; no sizing or ops guidance given.
- **Confidence**: emerging
- **Quote**: "You operate the Managed Agents server, its database, and the workers where agents run their shell and file tools."
- **Our assessment**: Useful for the "who owns what" question in team adoption: self-hosting converts a managed service into a platform you run (server + DB + worker fleet), with the associated patching, backup, and availability burden. The post is silent on that cost beyond the one sentence "Until now, that meant building the platform themselves."

### Claim 3: Self-hosting is motivated by agents becoming more capable, running unattended, and needing access to internal systems
- **Evidence**: Assertion/motivation; example tasks listed but no evidence of adoption.
- **Confidence**: anecdotal
- **Quote**: "They run unattended on your code and need access to your internal systems."
- **Our assessment**: The framing (unattended + internal access ⇒ want whole service inside perimeter) is a reasonable threat-model argument, consistent with the guide's least-agency theme, but is positioned as marketing rationale, not evidence.

### Claim 4: Model requests can be routed to Anthropic directly, a cloud provider (Bedrock, Google's Agent Platform, Microsoft Foundry), or the customer's own gateway
- **Evidence**: Product capability statement.
- **Confidence**: emerging
- **Quote**: "Model requests go where you choose, whether that's Anthropic directly, your cloud provider (Amazon Bedrock, Google's Agent Platform, or Microsoft Foundry), or your own gateway."
- **Our assessment**: Notable contrast with Claude Code self-hosted environments, where inference could not be routed via Bedrock/Foundry/gateway (blog-anthropic-claude-code-self-hosted-environments.md Claim 7). Different products, so this is a conditioning difference, not a contradiction, but practitioners should not assume parity between the two self-hosting offerings.

### Claim 5: Session history lives in the customer's database, and ZDR applies to requests sent to Claude as for any Messages API call
- **Evidence**: Stated policy; no further detail on what is and is not covered.
- **Confidence**: emerging
- **Quote**: "Session history is stored in your own database. If your organization has zero data retention (ZDR) in place with Anthropic, it applies to the requests sent to Claude in the same way as any other Messages API call."
- **Our assessment**: The ZDR statement is scoped narrowly to model requests; session history is the customer's own responsibility. This differs from the Claude Code self-hosted environments note, where ZDR orgs were excluded because Anthropic stored transcripts (Claim 7 there; Claim 6 there on the residency split). If accurate, full self-hosting is the route to combining ZDR with durable session records. Needs doc confirmation.

### Claim 6: Principle 1, the brain (harness) and hands (sandbox) are split by design
- **Evidence**: Architectural assertion; consistent with Anthropic's earlier engineering writing.
- **Confidence**: emerging
- **Quote**: "The agent's code runs in the sandbox, while the agent loop, session history, and vault secrets stay outside it."
- **Our assessment**: Gives a concrete security consequence (secrets and loop outside the code-executing boundary) plus resilience consequences ("sandboxes start only when a tool needs them", session history as an event log outside the sandbox). The split is the structural basis for the other three principles.

### Claim 7: Principle 2, credentials stay out of the sandbox via a proxy outside it; self-hosters can use their own secrets manager
- **Evidence**: Design statement; wording is hedged ("designed to", "supported API calls").
- **Confidence**: emerging
- **Quote**: "For MCP tools and supported API calls, a proxy outside the sandbox adds the credential to the request."
- **Our assessment**: Matches the injection-at-boundary pattern (Vercel in blog-anthropic-claude-managed-agents-selfhosted.md Claim 8). The hedge matters: coverage is "MCP tools and supported API calls", so credentials used by other means (e.g. arbitrary CLI tools) may not be covered. Customer-supplied secrets manager shifts correctness onto the customer.

### Claim 8: Principle 3, each environment can be limited to an allowlist of hosts; when self-hosting the sandbox, the same limits are set in the customer's own firewall
- **Evidence**: Capability statement plus one illustrative example (build-fixing agent: git host + package registry).
- **Confidence**: emerging
- **Quote**: "You can limit each environment to a list of allowed hosts, and requests to any other host are blocked."
- **Our assessment**: Default-deny egress per environment is the right pattern. Key point for the guide: in self-hosted mode enforcement is explicitly the customer's firewall ("you set the same limits in your own firewall"), so the guarantee is only as strong as your own network config.

### Claim 9: Principle 4, every session leaves a full record (tool calls and results) exportable over OpenTelemetry
- **Evidence**: Capability statement.
- **Confidence**: emerging
- **Quote**: "The record exports over OpenTelemetry, so you can send it to the monitoring tools you already use and review agent activity alongside the rest of your systems."
- **Our assessment**: Corroborates the OTel export in blog-anthropic-agent-observability-claude-platform.md (Claims 1-2). Does not say whether the record includes full prompt content or metadata-only (that note's Claim 5 says content defaults to metadata only), nor retention behaviour in self-hosted mode.

### Claim 10: The four principles apply identically whether Anthropic hosts everything, the customer hosts only the sandbox, or the customer hosts the whole service
- **Evidence**: Assertion only.
- **Confidence**: anecdotal
- **Quote**: "These principles apply whether Anthropic hosts everything, you host just the sandbox, or you host the whole service."
- **Our assessment**: Framing is architecture-first security ("agent security starts with architecture"). Plausible for design intent, but the post itself concedes enforcement moves to the customer (firewall, secrets manager), so equivalence of guarantees is not demonstrated.

## Concrete Artifacts

```
Four principles as headed in the source (Anthropic, 2026-11-12):
1. The brain and the hands are split
2. Credentials stay out of the sandbox
3. Network access can be limited
4. Every session leaves a full record

Operational boundary (customer-operated): Managed Agents server + its database + workers (shell/file tools)
Model routing options: Anthropic direct | Amazon Bedrock | Google's Agent Platform | Microsoft Foundry | own gateway
Access: private beta, via Anthropic account team
```

## Cross-References

- **Corroborates**: blog-anthropic-claude-managed-agents-selfhosted.md Claim 8 (credentials injected at the network boundary, never in the sandbox) and Claim 2 (sensitive data stays within perimeter); blog-anthropic-agent-observability-claude-platform.md Claims 1-2 (OpenTelemetry export of agent turns and tool calls).
- **Contradicts**: None filed. The ZDR/routing differences versus blog-anthropic-claude-code-self-hosted-environments.md (Claim 7) are product-conditioned (Claude Code self-hosted environments vs Managed Agents self-hosting), not a contradiction.
- **Extends**: blog-anthropic-claude-managed-agents-selfhosted.md Claim 1 (orchestration used to stay on Anthropic; now the harness and session store are customer-run); blog-anthropic-claude-managed-agents.md Claim 7 (governance layer, scoped permissions, tracing); blog-anthropic-zero-trust-ai-agents.md Claim 19 (isolation as primary boundary, network as backstop; here per-environment host allowlists).
- **Novel**: Full control-plane self-hosting; explicit statement that ZDR applies to model requests while session history is customer-stored; Bedrock/Google/Foundry/gateway routing for Managed Agents.

## Guide Impact

- **Chapter 06 (security threat model)**, section "The Sandbox Is the Control — Even When Someone Else Runs It": add this as the next point on the hosting spectrum (hosted → self-hosted sandbox → fully self-hosted), noting the four principles, and that in self-hosted mode egress allowlisting and secrets management become customer-enforced. Attribute as vendor-stated, private beta.
- **Chapter 02 (harness engineering)**: the brain/hands split and proxy-based credential injection can be cited as an architectural pattern for harness design (low priority; no evidence beyond assertion).
- **Chapter 05 (team adoption)**: note that full self-hosting makes the team the operator of a server, DB, and worker fleet; weigh against the hosted option.

## Extraction Notes

- Read the full article text (short, ~5 min). No customer quotes, metrics, or code. The linked docs page was not followed. Prospector comments said the fourth principle was unverified; it is verified here (session record via OpenTelemetry).
- Claims are marked emerging/anecdotal because they are unvalidated vendor claims about a private beta.
