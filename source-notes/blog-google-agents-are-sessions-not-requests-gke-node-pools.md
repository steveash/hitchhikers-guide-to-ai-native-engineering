---
source_url: https://developers.googleblog.com/agents-are-sessions-not-requests-size-gke-node-pools-for-ai-agent-sessions/
source_type: blog-post
title: "Agents are sessions, not requests: size GKE node pools for AI agent sessions"
author: Drake Williams (Senior Product Manager, Google Cloud) and Ivan Nardini (AI Developer Relations)
date_published: 2026-11-16
date_extracted: 2026-11-17
last_checked: 2026-11-17
status: current
confidence_overall: emerging
issue: "#4776"
---

# Agents are sessions, not requests: size GKE node pools for AI agent sessions

> A vendor-authored, explicitly *modeled* cost argument that long-lived agent sessions should be sized by the sessions currently holding a worker (not sessions open), by suspending idle sandboxes to object storage via Agent Substrate / AX, with a stated break-even near 4.5 prompts/hour.

## Source Context

- **Type**: blog-post (Google Developers Blog, product/how-to article promoting Agent Substrate 1.0 GA on GKE and the pre-stable AX project)
- **Author credibility**: A Google Cloud Senior PM and an AI Developer Relations engineer — first-party for the product, but with a commercial interest. All cost figures come from "our cost model" (Google Cloud list prices, us-central1), not from measured production fleets. The authors themselves flag the prompt rate as "the input we are least sure of."
- **Scope**: Idle-time economics of one-Pod-per-session vs. scale-to-zero vs. suspend-to-object-storage; warm-pool sizing; operational traps (no auto-suspend, 503s); gateway credential injection. Does NOT cover agent quality, measured latency of suspend/restore, or CPU-overcommit pricing for Agent Substrate (explicitly unpriced).

## Extracted Claims

### Claim 1: Agent sessions are long-lived and idle most of the time, so they need a different runtime model than web requests
- **Evidence**: Citation of a study of GitHub Copilot agent traces (Banruo Liu et al.); average turn of 396.3 s of agent work; authors' assumption of 2 prompts/hour over 8 hours.
- **Confidence**: emerging
- **Quote**: "In a study of GitHub Copilot agent traces, Banruo Liu and colleagues found that in a typical session with several prompts, the agent waits for the user about 80% of the time."
- **Our assessment**: Plausible and intuitive; the 80% comes from a third-party trace study (not independently checked here), while the 22%/78% day split is the authors' own assumption ("2 prompts an hour over an 8 hour workday, which is our assumption").

### Claim 2: One Pod per session wastes spend on waiting; scale-to-zero loses process memory
- **Evidence**: Cost-model example: 1 vCPU / 1 GiB Pods, 3 per c3-standard-4 node after GKE reservations, so 100 agents need 34 nodes, ~USD 1,288/month.
- **Confidence**: emerging
- **Quote**: "The node is free, and files on a persistent volume survive, but the process and its memory do not, so the next prompt starts a new agent process."
- **Our assessment**: The trade-off framing (state retained vs. compute freed) is useful and generalizes beyond GKE. Dollar figures are modeled.

### Claim 3: Parking = suspend the sandbox (not the session) to object storage and restore on any warm worker
- **Evidence**: Agent Substrate `SuspendActor`; actor/worker/warm-pool architecture; AX `ax suspend` keeps `/workspace` via volume snapshot, but processes restart fresh.
- **Confidence**: emerging
- **Quote**: "SuspendActor snapshots an idle actor to object storage and frees its worker, and the next request restores the actor on any warm worker."
- **Our assessment**: A clean session/compute split. Note the AX caveat: "the files come back on resume and the agent's processes start fresh" — so AX today is closer to scale-to-zero-with-files than to full memory-preserving parking; the Agent Substrate path is the one described as snapshotting the actor. Not verified by practitioners.

### Claim 4: Parking saves ~40% of the node bill at 2 prompts/hour for 100 coding agents (modeled)
- **Evidence**: Cost model with 2-minute idle timeout → each session holds a worker 29% of open time; pool sized to p99 concurrent-active plus 15% headroom → 15 nodes; plus one always-on control-plane node (Agent Substrate + PostgreSQL) and a scale-to-zero-after-hours job.
- **Confidence**: anecdotal (single vendor model, unvalidated)
- **Quote**: "Parking saves 40% of the node bill."
- **Our assessment**: Treat as an illustrative output of a parameterized model, not a benchmark. Useful mainly for its parameters (idle timeout, p99 sizing, headroom).

### Claim 5: Savings collapse as prompt rate rises; break-even is ~4.5 prompts/hour
- **Evidence**: At 4 prompts/hour agent works 44% of the hour, pool grows to 27 nodes, saving 4%.
- **Confidence**: anecdotal
- **Quote**: "Around 4.5 prompts an hour, one Pod per session becomes the cheaper option, so measure your prompt rate first."
- **Our assessment**: The qualitative point (parking pays when agents wait most) is robust; the 4.5 threshold is specific to the model's assumptions. Interactive coding sessions with fast agent loops may sit above it.

### Claim 6: Parking is not automatic — the harness must call suspend; full pools yield HTTP 503 after 5 s
- **Evidence**: Cites Agent Substrate issue #424 and docs.
- **Confidence**: settled (stated product behavior)
- **Quote**: "Agent Substrate does not suspend an idle actor by itself (#424), so your agent harness, or the service in front of it, calls the suspend API after an idle timeout."
- **Our assessment**: The key operational trap for harness designers: idle-timeout policy is a harness responsibility. Companion quote: "When idle actors hold every worker, a request for another actor waits up to 5 seconds by default, then fails with HTTP 503".

### Claim 7: Size the pool for busiest hour, not average; small rate changes matter a lot
- **Evidence**: Pool full about once in 3,500 turns at 2 prompts/hour; at 2.5 prompts/hour the same 15 nodes are full for 3% of turns.
- **Confidence**: emerging
- **Quote**: "In an hour at 2.5 prompts instead of 2, the same 15 nodes are full for 3% of turns, so size the pool for your busiest hour."
- **Our assessment**: Good capacity-planning heuristic; the sharp sensitivity is a risk for team rollouts with bursty usage (e.g., post-standup).

### Claim 8: Autoscaling follows worker Pods, so idle pools must be scaled down by schedule or they cost ~2× the Pod-per-session bill
- **Evidence**: GKE install guide autoscaling behavior; 730-hour month.
- **Confidence**: emerging
- **Quote**: "a pool that runs all 730 hours of the month costs about twice the one Pod per session bill."
- **Our assessment**: Shows the 40% saving depends on an after-hours scale-to-zero job — an easily missed dependency.

### Claim 9: Fixed control-plane cost means parking only pays above a fleet size (~37 coding sessions)
- **Evidence**: Control plane costs the same for 10 or 1,000 sessions; ~13 sessions for an assumed chat assistant working ~1 min/hour.
- **Confidence**: anecdotal
- **Quote**: "parking pays from about 37 coding sessions, or 13 for an assumed chat assistant that works about a minute an hour."
- **Our assessment**: Relevant to team-size decisions: small teams should not adopt this infrastructure for cost reasons.

### Claim 10: CPU overcommit with Pod requests < limits can beat parking, but trades off noisy-neighbor slowdowns
- **Evidence**: 0.25 vCPU request / 1 vCPU limit packs 12 per node → 9 nodes for 100 agents. Overcommit via Agent Substrate worker-pool capacity is not priced.
- **Confidence**: emerging
- **Quote**: "Overcommit has the same cost on both sides: agents share CPU and slow down when their neighbors are busy, during builds and tests."
- **Our assessment**: The honest caveat undercuts the headline saving: the 40% is vs. fully-guaranteed-CPU Pods. Compare at equal CPU guarantee.

### Claim 11: Gateways inject credentials by actor identity so the agent never holds keys
- **Evidence**: Architectural description only; no config shown.
- **Confidence**: emerging
- **Quote**: "Gateways control the actor's inbound and outbound traffic and add credentials on the way out, based on the actor's identity, so the agent never holds the keys."
- **Our assessment**: Standard credential-proxy pattern; supports security guidance. AX gateways/budgets/policies are only on the roadmap, not shipped.

## Concrete Artifacts

Cost-model parameters as stated by the authors (modeled, not measured):

```
Fleet: 100 coding agents; 2 prompts/hour; 8-hour workday; GCP list prices, us-central1
Pod-per-session: 1 vCPU / 1 GiB; c3-standard-4 fits 3 Pods -> 34 nodes, ~USD 1,288/month
Parked: 2-minute idle timeout -> worker held 29% of open time
        pool = p99 concurrent holders + 15% headroom -> 15 nodes
        + 1 always-on node (control plane + PostgreSQL) + after-hours scale-to-zero job
        -> ~40% saving; pool full ~1 in 3,500 turns
4 prompts/hour: 27 nodes, ~4% saving; break-even ~4.5 prompts/hour
Overcommit comparison: 0.25 vCPU request / 1 vCPU limit -> 12 per node -> 9 nodes (not priced for Agent Substrate)
```
(Source: article body, "What parking saves on GKE" and "When one Pod per session costs less".)

## Cross-References

- **Corroborates**: None directly on economics. Loosely consistent with `docs-ghaw-agent-runtimes-reference.md` and `blog-cognition-what-we-learned-building-cloud-agents.md` in treating the agent sandbox as a distinct runtime concern (those notes do not quantify idle cost).
- **Contradicts**: None found; no contradiction issue filed.
- **Extends**: `blog-google-mcp-stateless-scaling.md` (Google's stateless-MCP scaling argument — here the contrast is that agent sessions are inherently stateful, so state must be parked rather than eliminated); `blog-vercel-cursor-cloud-agents-vercel-sandbox.md` and `blog-vercel-sandbox-managed-images.md` (sandbox runtimes, without idle-parking economics); `blog-anthropic-claude-code-self-hosted-environments.md` (self-hosted sessions, no cost model); `docs-ghaw-enclaves.md` (isolation/credential-handling angle).
- **Novel**: Idle-time cost model for agent sessions; session-vs-sandbox split with suspend-to-object-storage; break-even prompt-rate and fleet-size thresholds; Agent Substrate / AX; the "harness must call suspend; pool-full → 503" operational trap.

## Guide Impact

- **Chapter 02**: Add a short subsection on runtime lifecycle for long-lived agent sessions: idle timeout and explicit suspend/resume are harness responsibilities (Claim 6), and session state vs. sandbox compute should be treated separately (Claim 3). Label as vendor-described.
- **Chapter 05**: When discussing shared-cluster hosting for teams, cite the modeled break-even (~4.5 prompts/hour, ≥~37 sessions) as a vendor-modeled heuristic and recommend measuring prompt rate from gateway logs first (Claims 4, 5, 9); note the overcommit caveat (Claim 10).
- **Chapter 06**: Cite gateway-side credential injection by actor identity as a pattern for keeping keys out of agent sandboxes (Claim 11).

## Extraction Notes

- Full article read via raw HTML text extraction (all five figures are images; their captions were read, chart data was not). No paywall.
- All quotes were copied from the extracted article text. Linked docs (Agent Substrate docs, issue #424, AX repo, Liu et al. study) were not followed, so the 80% wait figure and the #424 status are not independently verified.
- All cost numbers are the vendor's model outputs; the authors acknowledge the prompt rate is their least certain input.
