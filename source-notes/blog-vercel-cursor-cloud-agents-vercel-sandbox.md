---
source_url: https://vercel.com/changelog/run-cursor-cloud-agents-vercel-sandbox
source_type: blog-post
title: "Cursor Cloud Agents can now run in Vercel Sandbox"
author: Allen Zhou (Vercel)
date_published: 2026-09-03
date_extracted: 2026-10-03
last_checked: 2026-10-03
status: current
confidence_overall: emerging
issue: "#3880"
---

# Cursor Cloud Agents can now run in Vercel Sandbox

> A Vercel changelog entry (plus its linked 12-minute Knowledge Base walkthrough, published 2026-09-02) documents a reference architecture for running Cursor's self-hosted cloud agent workers as scale-to-zero, one-microVM-per-request Vercel Sandboxes, with a durable-workflow control plane whose retry safety rests on atomic claims, deterministic IDs, and leases.

## Source Context

- **Type**: blog-post (Vercel changelog, ~200 words) and its linked step-by-step Knowledge Base guide (https://vercel.com/kb/guide/cursor-vercel-sandbox, ~12 min read, followed per MINER.md §1). Most concrete evidence comes from the guide.
- **Author credibility**: Allen Zhou, Member of Technical Staff at Vercel, writing on Vercel's own changelog and KB. It is first-party vendor material promoting Vercel Sandbox/Workflows, but the guide ships working code and names specific API endpoints, so its claims are checkable. Cursor's side of the integration (Self-Hosted Machines) is described only as Vercel understands it.
- **Scope**: Covers the control-plane/compute-plane split, claim/lease/idempotency design, credential handling, and production caveats. Does NOT cover: measured cold-start or pickup latency, cost figures, failure data from real use, Cursor-side limits on the pool API, or any comparison with other sandbox providers.

## Extracted Claims

### Claim 1: Cursor keeps the harness and inference loop; the customer supplies only the execution environment, which Vercel Sandbox provides
- **Evidence**: Product description in the changelog; the KB guide repeats the split and builds the integration on Cursor's Self-Hosted Machines APIs. Requires a Cursor Enterprise plan.
- **Confidence**: emerging
- **Quote**: "Cursor manages the agent harness and inference loop."
- **Our assessment**: Same inference/execution split Cursor described in its own self-hosted announcement (`blog-cursor-self-hosted-cloud-agents.md` Claim 3). New here is a third-party platform acting as the execution half, showing the split is a real integration seam, not only an on-prem story. Plan gating (Enterprise) is a practical constraint.

### Claim 2: Each agent request gets its own isolated Firecracker microVM, with a Functions + Workflows control plane that claims, provisions, monitors, and cleans up
- **Evidence**: Architecture description in the changelog; the guide shows the code (a discovery workflow plus one child workflow per claimed request).
- **Confidence**: emerging
- **Quote**: "Vercel Sandbox provides that execution environment as an isolated Firecracker microVM for each agent request."
- **Our assessment**: Per-request microVM isolation matches the per-session VM model in `blog-cursor-self-hosted-cloud-agents.md` Claim 4 and Herdr's sandbox-per-agent in `blog-vercel-herdr-agent-sandboxes.md` Claim 1. Here the sandbox is also ephemeral (`persistent: false`), unlike Herdr's persistent sandboxes.

### Claim 3: A registered pool with zero workers enables scale-to-zero; capacity is created only when a request arrives
- **Evidence**: Guide registers the pool with `"workerReadyTimeoutSeconds": 0` so a follow-up on an offline worker is immediately re-acquirable from the pool and gets a fresh Sandbox.
- **Confidence**: emerging
- **Quote**: "Cursor's team pool remains registered when it has zero workers."
- **Our assessment**: A clean pattern: the queue lives in the vendor's control plane, compute lives nowhere until needed. Cost: pickup latency is bounded by controller polling (see Claim 6); the guide gives no measured numbers.

### Claim 4: Retry safety comes from layering several idempotency mechanisms, and the guide is explicit that the atomic claim covers request assignment only
- **Evidence**: Guide lists: Cursor's atomic claim; deterministic worker ID (`pw_<normalized id>`); deterministic Sandbox name with `Sandbox.getOrCreate()`; Workflow hook leases (`createHook` + `getConflict`) for controller and child; and `flock -n` so a retried start cannot launch a second worker process in the same Sandbox.
- **Confidence**: emerging
- **Quote**: "That guarantee covers request assignment only."
- **Our assessment**: The most reusable lesson for agent infrastructure: each layer closes a specific duplicate-execution hole at a different level (request, workflow, VM, process). Worth a checklist in the infrastructure chapter. It is a design the vendor asserts is safe; no failure-injection results are shown.

### Claim 5: The long-lived service key never enters the microVM; only a one-hour, user-scoped worker token does
- **Evidence**: Guide mints the token via `POST /v1/sub-tokens` with `forUserId`, writes it to a `0o600` file, and passes `--auth-token-file` so it never appears in process arguments.
- **Confidence**: emerging
- **Quote**: "Only the one-hour token for the requesting Cursor user enters the microVM."
- **Our assessment**: A concrete least-privilege pattern (credential stays in control plane; agent gets short-lived, per-user identity). Parallels Herdr's no-credential-copy rule (`blog-vercel-herdr-agent-sandboxes.md` Claim 4). The guide admits the limit: tokens cannot refresh themselves, so sessions over an hour need a separate scheme.

### Claim 6: Adaptive durable polling avoids always-on compute, with a concurrency cap as the spike control
- **Evidence**: Controller code sleeps 5s while draining, 1m when recently idle, 5m after five consecutive empty checks; `MAX_WORKERS_PER_TICK = 5`. Guide states durable sleeps do not consume compute and are not bound by Function duration, so it works on Hobby. SSE list-then-watch is offered for lower latency.
- **Confidence**: emerging
- **Quote**: "It prevents one queue spike from creating unbounded compute and gives you a simple concurrency control to tune for your team."
- **Our assessment**: Note the cap limits claims per tick, not total concurrent sandboxes, so it is a rate limit more than a true concurrency ceiling. The guide implies it is a simple control; teams needing hard ceilings should rely on pool quotas as well.

### Claim 7: Cleanup is layered, with three independent termination paths
- **Evidence**: Worker exits after `CURSOR_WORKER_IDLE_RELEASE_TIMEOUT` (600s); child workflow polls agent status every 30s (up to 90 checks) and stops the Sandbox and releases the claim when `IDLE`/`ARCHIVED`; Sandbox has a 45-minute hard timeout. Release treats 404 as already released.
- **Confidence**: emerging
- **Quote**: "with the 45-minute Sandbox timeout as a final safety net"
- **Our assessment**: Good defense in depth against runaway cost. Because the 45-minute timeout is also the Hobby maximum, long agent runs on that tier are cut off; Pro/Enterprise support longer.

### Claim 8: Boot time is cut by building a snapshot once with the Cursor Agent CLI preinstalled
- **Evidence**: `scripts/build-snapshot.ts` starts from `vercel/sandbox/universal:latest`, installs the CLI, and snapshots with `expiration: 0`; the guide says to rebuild periodically to update the CLI and packages.
- **Confidence**: emerging
- **Quote**: "Installing the Cursor Agent CLI for every request would add setup time before an agent can begin."
- **Our assessment**: Standard "bake the toolchain" approach; consistent with the managed-image story in `blog-vercel-sandbox-managed-images.md` Claim 1. Snapshots that are never refreshed become a stale-dependency risk; the guide notes this.

### Claim 9: Credentials and network egress are the remaining production gaps the implementer must close
- **Evidence**: "Production considerations" section: configure Git integration or short-lived Git credentials, do not bake credentials into snapshots, restrict egress, log request/worker/Sandbox IDs but never worker tokens.
- **Confidence**: emerging
- **Quote**: "Do not bake credentials into a snapshot."
- **Our assessment**: Candid that the reference is "intentionally small". Egress allowlists and credential brokering are asserted as Sandbox capabilities but not demonstrated. Compare Cursor's own egress restrictions in `blog-cursor-cloud-agent-environment-operations.md` Claim 3.

### Claim 10: The design needs no inbound port, load balancer, or publicly reachable worker
- **Evidence**: Guide statement after the API example; the workers dial out to Cursor and the controller polls Cursor's API.
- **Confidence**: emerging
- **Quote**: "No inbound port, load balancer, or publicly reachable worker service is required."
- **Our assessment**: Corroborates the outbound-only worker pattern (`blog-cursor-self-hosted-cloud-agents.md` Claim 2) in a cloud-hosted rather than on-prem setting.

## Concrete Artifacts

Pool registration (KB guide, "Register a scale-to-zero team pool"):

```
curl --request POST \
  --url https://api.cursor.com/v0/private-workers/pools \
  --header "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "scope": "team",
    "poolName": "vercel-sandbox",
    "workerReadyTimeoutSeconds": 0
  }'
```

Worker start with single-process lock (KB guide, `lib/cursor-workers.ts`):

```
"exec flock -n /tmp/cursor-worker.lock agent worker " +
  "--auth-token-file $CURSOR_AUTH_TOKEN_FILE --pool $CURSOR_POOL " +
  "--worker-dir /vercel/sandbox/workspace start",
```

Adaptive polling (KB guide, `workflows/cursor-pool-controller.ts`):

```
const interval = jobs.length ? "5s" : emptyChecks >= 5 ? "5m" : "1m";
await sleep(interval);
```

Targeting the pool via API (KB guide):

```
"env": { "type": "pool", "name": "vercel-sandbox" },
```

Cursor endpoints used: `GET /v0/private-workers/pending-requests?pool=`, `POST /v0/private-workers/claim`, `POST /v1/sub-tokens`, `GET /v1/agents/{id}` (status `ACTIVE|IDLE|ARCHIVED`), `POST /v0/private-workers/claims/{id}/release`.

Key parameters: 45-minute Sandbox timeout, 10-minute idle release, 30s status checks (max 90), `MAX_WORKERS_PER_TICK = 5`, one-hour worker token.

## Cross-References

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` Claims 2, 3, 4 (outbound-only workers, inference/execution split, per-session VM isolation); `blog-vercel-herdr-agent-sandboxes.md` Claims 1 and 4 (sandbox per agent; credentials not copied into the sandbox).
- **Contradicts**: None found. Herdr uses persistent sandboxes while this uses ephemeral ones; that is a context difference (interactive vs. queued), not a contradiction.
- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` (adds a concrete third-party implementation of the worker pool, which that note says lacks specifics such as what a worker needs); `blog-vercel-sandbox-managed-images.md` Claim 1 (snapshot built from the `universal:latest` image); `blog-cursor-cloud-agent-environment-operations.md` Claim 3 (egress/secret hygiene, here left to the implementer).
- **Novel**: The layered idempotency design for durable agent-worker orchestration; scale-to-zero via a zero-worker registered pool; the explicit token-expiry limit on sessions over one hour; and the Enterprise-plan requirement for Self-Hosted Machines.

## Guide Impact

- **Chapter 03 / Chapter 05 (infrastructure and sandboxes)**: Add this as a worked example of "harness vendor-hosted, execution customer-supplied". Suggest a short checklist of duplicate-execution defenses (atomic claim, deterministic IDs, leases, process lock) citing this note's Claim 4.
- **Chapter 05**: Add the layered-termination pattern (idle release, status-poll cleanup, hard timeout) from Claim 7 and the credential-scoping rule from Claim 5, with the one-hour token caveat.
- **Cost/limits discussion**: Note that the reference has no published latency or cost data; do not state scale-to-zero pickup latency as a benefit without a source.

## Extraction Notes

- Read the changelog in full and followed its main link (the KB guide, read in full). Did not follow the Cursor Self-Hosted docs or Vercel Sandbox docs pages.
- The changelog is thin on its own; most claims come from the guide, which is dated one day earlier (2026-09-02).
- Triage comments listed several overlapping notes; only those with verified claim numbers are cited above.
