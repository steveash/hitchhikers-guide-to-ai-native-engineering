---
source_url: https://github.github.com/gh-aw/blog/2026-11-15-ecosystem-spotlight/
source_type: blog-post
title: "Ecosystem Spotlight: githubnext/evergreen (GitHub Agentic Workflows)"
author: Copilot (GitHub Agentic Workflows blog byline)
date_published: 2026-11-15
date_extracted: 2026-11-16
last_checked: 2026-11-16
status: current
confidence_overall: anecdotal
issue: "#4755"
---

# Ecosystem Spotlight: githubnext/evergreen

> A gh-aw blog spotlight on an agentic workflow that repairs opted-in PRs without merge or default-branch write power, notable for a SHA-pinned deterministic preflight gate, a lease label with non-cancelling concurrency, post-write reload-and-verify rules, a PATH git wrapper that blocks merge/rebase, and per-PR quota with named stop states.

## Source Context

- **Type**: blog-post (filed as "documentation"; dated Ecosystem Spotlight bylined "Copilot", from the `github-agentic-workflows` trusted feed)
- **Author credibility**: GitHub-run gh-aw blog summarizing a `githubnext` project. It describes design and file names (`workflows/evergreen.md`, `safe-output-policy.md`, `quota-policy.md`, `INSTALL.md`). No metrics, incidents, or measured outcomes. The post itself says the project is early-stage.
- **Scope**: Overview, five design points, a four-step flow, install notes and adoption caveats. I read only this post; the linked repo and its policy files were not read, so file-level claims are secondhand. Patterns are design intent, not validated outcomes.

## Extracted Claims

### Claim 1: The trigger is a 15-minute schedule plus `workflow_dispatch`, deliberately not `pull_request`, to avoid confused-deputy guards
- **Evidence**: The post cites a comment at the top of `workflows/evergreen.md`. Teams needing immediacy are told to use a separate deterministic controller that never checks out or runs PR code.
- **Confidence**: anecdotal
- **Quote**: "generated pre-activation runs can trip confused-deputy guards for bot-authored or indirect PR events."
- **Our assessment**: A real operational constraint worth recording, and the trade is latency (up to 15 min) for fewer guard trips. The post does not say which guards or show an incident.

### Claim 2: A deterministic preflight job gates the agent on PR open state, opt-in label, lease label and the selected head SHA
- **Evidence**: Design description; no config shown.
- **Confidence**: anecdotal
- **Quote**: "A deterministic gate runs before any agent."
- **Our assessment**: Gating in plain workflow logic before any model runs puts the admission decision outside the model's reach. Compare the activation gate note, which gates on budget rather than PR state.

### Claim 3: A pre-agent step re-fetches `refs/pull/<n>/head` and aborts on SHA mismatch, so a stale checkout fails closed
- **Evidence**: Design description. It closes the time-of-check/time-of-use gap between selecting a PR and running on it.
- **Confidence**: anecdotal
- **Quote**: "A stale checkout fails closed."
- **Our assessment**: Strong, cheap, generalizable (pin the SHA you selected, verify it at checkout). Not shown in code here.

### Claim 4: A lease label prevents two runs on one PR; dispatch is refused if the lease can't be added; a separate cleanup job removes it; `cancel-in-progress: false` queues rather than cancels
- **Evidence**: Design description naming the `evergreen_active` label.
- **Confidence**: anecdotal
- **Quote**: "Runs are queued with cancel-in-progress: false, so a second run waits rather than cancelling the first."
- **Our assessment**: Novel to our corpus: a visible, label-based mutual-exclusion lease on top of concurrency groups. Note the choice of non-cancelling here versus cancel-older in review-council: writers shouldn't be killed mid-write, read-only reviewers can be. The post does not say how stale leases are handled after a crashed cleanup job.

### Claim 5: Write rules are operating rules: reload GitHub state after every safe output and report "blocked" if the change isn't visible
- **Evidence**: Attributed to `safe-output-policy.md`; it also forbids direct merges, base-branch writes and base-merging/rebasing branch updates.
- **Confidence**: anecdotal
- **Quote**: "requires the agent to reload GitHub state after every safe output and to report the operation as blocked if the expected change is not visible."
- **Our assessment**: Verify-after-write guards against silently dropped safe outputs. It is a prompt-level rule, so only as reliable as agent compliance; contrast with Claim 6.

### Claim 6: A git wrapper on the agent's PATH exits 64 for `merge` and `rebase`, enforcing the no-merge rule in the workflow rather than only in policy text
- **Evidence**: Design description.
- **Confidence**: anecdotal
- **Quote**: "a git wrapper placed on the agent’s path exits with status 64 for merge and rebase."
- **Our assessment**: Useful pairing of prompt rule plus mechanical block. A PATH wrapper is bypassable (e.g. absolute path to the real binary), so it is defense in depth, not a boundary; the post makes no stronger claim.

### Claim 7: Quota is counted per PR across runs, with explicit exhaustion behavior and five named stop states
- **Evidence**: Attributed to `quota-policy.md`. Only two of the five states are named (`awaiting-controller-recheck`, `quota-exhausted`).
- **Confidence**: anecdotal
- **Quote**: "Every run ends in one of five named stop states, such as awaiting-controller-recheck or quota-exhausted."
- **Our assessment**: Enumerated terminal states make agent runs auditable and easy to alert on. The quota size and the other three states are not given.

### Claim 8: Fail-closed install default: `REQUIRED_CHECKS_JSON` ships as `'[]'` and installers must replace it
- **Evidence**: Cited from a comment in the workflow; the post's adoption checklist repeats that the empty list means the agent can't clear anything until gates are named.
- **Confidence**: anecdotal
- **Quote**: "The workflow ships REQUIRED_CHECKS_JSON as '[]'"
- **Our assessment**: A good install-time pattern: an unconfigured template does nothing rather than something permissive.

### Claim 9: The agent is limited to safe outputs and runs diagnose-before-repair with runtime-installed, SHA-pinned skills
- **Evidence**: How-it-works steps: comments, labels, PR-branch pushes limited to PRs with the `evergreen` label, and at most one review; skills "pinned to a commit SHA and installed at runtime".
- **Confidence**: anecdotal
- **Quote**: "Both skills are pinned to a commit SHA and installed at runtime, so the prompt does not carry their full text."
- **Our assessment**: Keeps the prompt small and supply-chain pinned. Pinning guards against tampering but not against a bad pinned version.

### Claim 10: The post is candid about the control-plane's own risk and maturity
- **Evidence**: Adoption checklist: preflight holds write permissions; fork PRs need trusted approval; project is early-stage.
- **Confidence**: anecdotal
- **Quote**: "The preflight job has contents, issues and pull-requests: write permissions, so review its gate logic whenever you change it."
- **Our assessment**: Worth noting: the deterministic gate is itself the privileged component, so the safety shifts to reviewing gate code. Treat Evergreen as a reference design, not an endorsed tool.

## Concrete Artifacts

```
Source: gh-aw blog, 2026-11-15 (secondhand description of githubnext/evergreen)
Control flow:
  cron (15 min) / workflow_dispatch
   -> preflight job: PR open? `evergreen` label? `evergreen_active` lease? head SHA == selected?
   -> add lease label (refuse to dispatch if it fails)
   -> agent job: fetch refs/pull/<n>/head, abort if SHA differs; checkout verified head
   -> evergreen-diagnose, then evergreen-repair if needed
   -> safe outputs: comments, labels, PR-branch pushes (evergreen-labelled PRs only), <=1 review
   -> reload state to verify each write; cleanup job removes lease
Stop states (two of five named): awaiting-controller-recheck, quota-exhausted
Guards: git wrapper exit 64 on merge/rebase; concurrency cancel-in-progress: false;
        REQUIRED_CHECKS_JSON='[]' placeholder
```

## Cross-References

- **Corroborates**: `blog-ghaw-ecosystem-spotlight-svennijhuis-agentic-workflows.md` Claim 1 (runner-enforced limits rather than prompt text) and Claim 6 (fail-closed shared fragments); `blog-ghaw-ecosystem-spotlight-review-council.md` Claim 4 (a PR cannot influence its own review criteria; here, a stale/changed head fails the gate).
- **Contradicts**: None. `blog-ghaw-ecosystem-spotlight-review-council.md` Claim 5 has newer pushes cancel older reviews, while Evergreen uses `cancel-in-progress: false`; this differs by context (read-only reviewer vs writing repairer), so no contradiction issue filed.
- **Extends**: `blog-ghaw-activation-gate-admission.md` Claim 1 (a pre-agent decision point; here a PR-state/SHA gate rather than a budget gate); `docs-ghaw-labelops.md` Claim 3 (persistent label as state marker; the lease label is such a marker); `docs-ghaw-concurrency-reference.md` Claim 2 (per-trigger cancel vs non-cancel groups).
- **Novel**: Lease label with refuse-on-failure dispatch and separate cleanup job; SHA re-fetch fail-closed check; reload-and-verify after safe outputs; PATH git wrapper exit 64; per-PR persistent quota with named stop states; schedule trigger chosen to avoid confused-deputy guards.

## Guide Impact

- **Chapter 02**: Add a "write-safety control plane" example: preflight gate, lease, non-cancelling queue, named stop states, citing this note as a single early-stage reference design.
- **Chapter 03**: Add reload-and-verify-after-write as a verification step for agent side effects (Claim 5), noting it is prompt-level.
- **Chapter 06**: Add the PATH-wrapper no-merge guard (as defense in depth) and the schedule-over-`pull_request` rationale for confused-deputy guards.

## Extraction Notes

- Fetched raw HTML via curl and read the full article body; no sub-pages followed (the repo files are linked only by name).
- Quotes are verbatim from the post text (the Claim 6 quote uses the post's typographic apostrophe).
- Prospector asked not to present star count as adoption evidence; it is mentioned only as the post's own caveat.
