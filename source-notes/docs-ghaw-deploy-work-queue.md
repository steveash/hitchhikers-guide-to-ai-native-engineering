---
source_url: https://github.github.com/gh-aw/guides/deploy-work-queue
source_type: docs
title: "GitHub Agentic Workflows: How to deploy a work queue (native Git-backed tools.work-queue)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-10-09
last_checked: 2026-10-09
status: current
confidence_overall: emerging
issue: "#4018"
---

# GitHub Agentic Workflows: How to deploy a work queue

> First-party operator guide for the native version-3 `tools.work-queue`: a producer/dispatcher/worker split where scheduling and authorization live in an administrator-installed Policy and a protected Git branch, not in workflow frontmatter or the prompt — and where branch-protection verification is explicitly still deferred.

## Source Context

- **Type**: docs (operator guide; no publication date on the page)
- **Author credibility**: The gh-aw maintainers' own documentation. Authoritative on what the feature does; it is not a measured evaluation, so no performance or scheduling-quality claims are supported.
- **Scope**: Deployment steps: publish worker and dispatcher, define QueuePolicy JSON, protect the queue branch and install Policy, enable backing-Issue projection, submit/inspect work. Does not cover the Work Queue Specification, the backing Issue reference, or the queue reference (linked, not followed).

## Extracted Claims

### Claim 1: Native `tools.work-queue` is always Git-backed and provides things the issue-backed patterns do not
- **Evidence**: Stated in the page's introduction, contrasting with lightweight issue-backed patterns. No benchmark.
- **Confidence**: emerging (first-party statement, unmeasured)
- **Quote**: "Those patterns use GitHub read tools and safe outputs, but do not provide native fair scheduling, Claim authority, or verified dependency graphs."
- **Our assessment**: This answers the gap left by `docs-ghaw-workqueue-ops.md`, which describes only the prompt-level strategies. The page also says "Native version-3 `tools.work-queue` always uses Git; no storage selector is available." — which conflicts with the weekly post's "selectable issue-backed queue storage" wording for the native feature (see Cross-References).

### Claim 2: Four roles are separated — producer submits, dispatcher requests assignments, worker processes — plus an administrator who installs Policy
- **Evidence**: Prerequisites paragraph and the Submit section (`work_queue_submit`, `work_queue_dispatch_next`).
- **Confidence**: emerging
- **Quote**: "The producer submits tasks; the dispatcher requests assignments; the worker processes them."
- **Our assessment**: A clean privilege-separation model. Notably the scheduler, not the agent, picks work: "The scheduler—not the agent—selects eligible Work (immutable tasks) and an approved worker profile."

### Claim 3: Workflow frontmatter cannot install Policy or restrict who writes to the queue branch
- **Evidence**: Stated twice (intro and Policy-install section).
- **Confidence**: emerging
- **Quote**: "Workflow frontmatter does not install Policy or configure restrictions on who can write to that branch."
- **Our assessment**: Central finding for the guide: the enforcement boundary is deliberately outside the agent-authored/PR-reviewable workflow file. Also: "Frontmatter never installs or updates Policy."

### Claim 4: The `safe-outputs.dispatch-workflow` allowlist is a compile-time approval list, not dispatch authorization
- **Evidence**: Dispatcher frontmatter (`workflows: [eslint-refiner]`, `max: 3`) and the explanatory paragraph.
- **Confidence**: emerging
- **Quote**: "The allowlist tells the compiler which workers are approved. It does not authorize a dispatch."
- **Our assessment**: Authority comes from the installed worker profile: "Queue dispatch uses the fixed commit SHA and authenticated principal (the GitHub identity) in the installed worker profile, not the dispatcher's moving target-ref." Pinning to an immutable SHA avoids a moving-branch worker swap. Compare `docs-ghaw-dispatch-ops.md`, which covers plain dispatch.

### Claim 5: Workers are made unrunnable without Claims via `require-assignment: true`, and a Claim authorizes exactly one attempt
- **Evidence**: Worker frontmatter snippet; Submit section on Claims and `max_claims: 1` in the profile.
- **Confidence**: emerging
- **Quote**: "Require an assignment for the worker so it cannot run without the Claims that authorize its work:"
- **Our assessment**: A harness-enforced precondition rather than a prompt instruction. Further: "A Claim authorizes one attempt at a task. Associate every effect (such as creating an issue) with its original Claim handle."

### Claim 6: Producer and worker identities must be numeric authenticated principal IDs; display names and `github.actor` are not proof
- **Evidence**: Define-the-Policy instructions.
- **Confidence**: emerging
- **Quote**: "A display name or github.actor is not proof of that identity."
- **Our assessment**: Takes the page's requirement as written: "Verify that each actor ID is a positive decimal GitHub principal ID. Set the revision to the actual 40- or 64-character commit SHA containing the worker workflow." Also "Administrator status alone does not grant these producer entitlements" — admin and producer rights are separate.

### Claim 7: Branch protection must be configured separately before installing Policy, and its automated verification is still deferred
- **Evidence**: "Protect the queue branch and install Policy" section with a Caution block.
- **Confidence**: emerging (self-declared gap)
- **Quote**: "Automated verification and provisioning of writer restrictions are still deferred. Installing Policy does not configure or verify these protections."
- **Our assessment**: Honest and important gap: the security of the queue rests on a manual operator step. Required protections as written: "Allow only the trusted operator or runtime host to write to the queue branch. Prevent force updates and branch deletion, and ensure that workflow-agent credentials cannot bypass these rules." Also: "Do not give the agent credentials that can write to the queue branch."

### Claim 8: Policy changes require a quiescent queue; cancellation does not stop a worker
- **Evidence**: Operational note after the install command.
- **Confidence**: emerging
- **Quote**: "Cancellation alone does not stop a worker or release its reservation; reconcile exact termination or nonlaunch evidence separately."
- **Our assessment**: Warns against assuming cancel == stopped. Quiescent means settling "all nonterminal (unfinished) Work, outstanding reservations, and unresolved delivery of completed Work."

### Claim 9: Worker "finish" is intent, not proof; Result requires independently verified delivery
- **Evidence**: Submit-and-inspect section; also "Native runs and failed/skipped jobs never substitute for Result."
- **Confidence**: emerging
- **Quote**: "Worker finish is an intent, not proof of delivery: Completion records task completion, and Result requires independently verified delivery."
- **Our assessment**: Strong instance of "don't trust the agent's self-report"; closure of backing Issues is governed by trusted policy: "This trusted policy, not agent payload, controls closure after verified non-PR delivery."

### Claim 10: Backing-Issue projection requires a mixed-reader-safe rollout and separately protected coordination refs
- **Evidence**: "Enable backing Issue projection" section.
- **Confidence**: emerging
- **Quote**: "Older version-3 closed-schema readers cannot read the new projector rules, Issue links, or comment handles; do not enable them during a mixed-reader rollout."
- **Our assessment**: Operational versioning hazard. Also protect `gh-aw-issue-projection/*` refs; a pre-existing Issue needs its full identity in `backing_issues` — "A repository allowlist alone does not authorize a pre-existing Issue."

### Claim 11: Resource limits are hard-capped; the ordinary ledger and recovery reserve are separate budgets
- **Evidence**: Template limits and explanatory paragraph.
- **Confidence**: emerging
- **Quote**: "Its 64 MiB ordinary budget and 16 MiB recovery reserve are separate: you cannot set the ordinary ledger limit to 80 MiB."
- **Our assessment**: Bounded-by-construction design (pool `logical_limit`/`native_limit` 16, `payload_bytes` 16384, etc.). Limits "Lower the limits if needed, but do not exceed the values in the template."

## Concrete Artifacts

Source: page "Publish the worker and dispatcher".

```yaml
# Worker frontmatter
tools:
  work-queue:
    require-assignment: true
    worker: true
```

```yaml
# Dispatcher frontmatter
tools:
  work-queue: true
safe-outputs:
  dispatch-workflow:
    workflows: [eslint-refiner]
    target-ref: ${{ github.event.repository.default_branch }}
    max: 3
  noop:
```

Source: "Define the Policy" (queue-policy.json, verbatim).

```json
{
  "mode": "weighted-priority",
  "class_weights": [8, 4, 2, 1, 1],
  "accounting_weights": { "": 1 },
  "producers": {
    "REPLACE_WITH_PRODUCER_ACTOR_ID": {
      "pools": ["default"],
      "priorities": [1, 2, 3, 4, 5],
      "fairness_keys": [""]
    }
  },
  "pools": {
    "default": {
      "default_profile": "eslint-refiner",
      "profiles": {
        "eslint-refiner": {
          "workflow": ".github/workflows/eslint-refiner.lock.yml",
          "ref": "REPLACE_WITH_40_OR_64_HEX_COMMIT_SHA",
          "principal": "REPLACE_WITH_WORKER_CREDENTIAL_ACTOR_ID",
          "trust_domain": "eslint-refiner",
          "credential_scope": "repository",
          "effect_scope": "github/gh-aw",
          "max_claims": 1,
          "share_keys": false
        }
      },
      "logical_limit": 16,
      "native_limit": 16,
      "allowed_repositories": ["github/gh-aw"],
      "max_observation_age_ms": 60000,
      "retry": { "max_attempts": 3, "backoff_ms": 1000 },
      "reconciliation": { "max_attempts": 5, "deadline_ms": 300000 }
    }
  },
  "limits": {
    "ledger_bytes": 67108864,
    "recovery_bytes": 16777216,
    "payload_bytes": 16384,
    "graph_nodes": 4096,
    "predecessors": 64,
    "pending_nodes": 4096,
    "operations": 256,
    "assignment_bytes": 49152,
    "result_bytes": 4096,
    "evidence_bytes": 1024,
    "observation_writes": 4096
  }
}
```

Source: "Protect the queue branch and install Policy".

```bash
gh aw work-queue --repo github/gh-aw policy \
  --file queue-policy.json --epoch eslint-queue-v1
# default queue branch: work-queue; use --branch QUEUE_BRANCH before `policy` for another
# inspect: gh aw work-queue --repo github/gh-aw state | tui | replay --json
```

Source: "Enable backing Issue projection" — the `projectors` array (principal, workflow, ref, pools, repositories, `completion_policy: "keep-open"`, `backing_issues[]` with repository_id/resource_id/number) is merged into the full Policy; frontmatter option `issues: true` or `issues: {label: cookie, status-field: WorkStatus}`.

## Cross-References

- **Corroborates**: `docs-ghaw-repo-memory-ledger-specification.md` Claim 3 (duties split across jobs with different privileges) and Claim 4 (restored branch content treated as untrusted) — same least-privilege, untrusted-branch posture; the queue is "the queue's transaction log" ("The ledger is the queue's transaction log"), plausibly sharing mechanics, though this page does not say so.
- **Contradicts**: None filed. Mild tension to note, not a clear contradiction: `blog-ghaw-weekly-2026-10-05.md` Claim 2 says work-queue storage became "selectable (issue-backed)", whereas this page says native version-3 `tools.work-queue` has "no storage selector"; issue-backed is described as a separate lighter pattern. Likely terminology/timeline difference; the weekly note's claim should be read accordingly.
- **Extends**: `docs-ghaw-workqueue-ops.md` (prompt-level strategies, Claims 3–6, concurrency Claim 9) — adds the enforced native alternative; `docs-ghaw-dispatch-ops.md` (dispatcher-to-worker handoff); `blog-ghaw-weekly-2026-10-05.md` Claims 1–2, whose Ch02 recommendation was "unverified pending docs" — this page is the first-party doc that verifies the existence of Git-backed operator commands (`gh aw work-queue ... policy/state/tui/replay`) and trusted-worker dispatch.
- **Novel**: QueuePolicy (weighted-priority scheduling, per-producer entitlements, pinned worker SHA + principal), Claim-based single-attempt authority, Completion-vs-Result distinction, and the explicitly deferred branch-protection verification.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Where WorkQueueOps is described at prompt level (citing `docs-ghaw-workqueue-ops.md`), add the native `tools.work-queue` as the harness-enforced variant: scheduler picks work, worker cannot run without a Claim (`require-assignment: true`), dispatch uses a pinned SHA/principal. Replace the "unverified pending docs" flag from the weekly note with a citation to this page (Claims 1, 4, 5).
- **Chapter 03 (Safety/governance)**: Add the trust-boundary lessons: allowlist ≠ authorization (Claim 4), numeric principal IDs not `github.actor` (Claim 6), agent credentials must not write the queue branch, and "finish is intent, not proof" (Claim 9). Flag Claim 7 as a known gap: Policy install does not verify branch protection.
- **Chapter 05 (Team Adoption)**: Note the role split — who may be producer, who administers Policy ("Administrator status alone does not grant these producer entitlements"), and the quiescence requirement for Policy changes (Claim 8).

## Extraction Notes

- Fetched raw HTML via curl and read the rendered text in full, including the Caution block that the triage truncated; quotes copied from that text. Page has no date, so `date_published: null`.
- Linked pages (Work Queue Specification, backing Issue reference, queue reference, implementation coverage table, daily report portfolio) were not followed; claims about them are not made.
- Performance/scheduling-quality properties (fair scheduling) are the docs' assertions only and unverified.
- Cross-referenced claim numbers were checked against the cited notes' `### Claim` headings.
