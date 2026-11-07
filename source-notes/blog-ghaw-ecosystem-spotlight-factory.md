---
source_url: https://github.github.com/gh-aw/blog/2026-11-06-ecosystem-spotlight/
source_type: blog-post
title: "Ecosystem Spotlight: sabbasi3-factory-lab/factory (GitHub Agentic Workflows)"
author: Copilot (GitHub Agentic Workflows blog byline)
date_published: 2026-11-06
date_extracted: 2026-11-07
last_checked: 2026-11-07
status: current
confidence_overall: anecdotal
issue: "#4571"
---

# Ecosystem Spotlight: sabbasi3-factory-lab/factory

> A short gh-aw blog case study of a third-party "factory" where a no-AI controller governs agents via risk-tiered merge policy, out-of-scope rules/verifier, a hash-chained audit branch and layered budget caps, with self-reported results of 47/47 tasks merged.

## Source Context

- **Type**: blog-post (filed as "documentation", but it is a dated blog post)
- **Author credibility**: Byline "Copilot" on the GitHub Agentic Workflows blog; a GitHub-run showcase of a community project (`sabbasi3-factory-lab/factory`). The post summarizes the project's README rather than independently verifying it.
- **Scope**: Design overview and headline results of one project (porting a Rust date-parsing library, chrono-node-rs). Does not give config contents, failure analysis, or independent measurement. The project is described as "a design to learn from rather than an installable package". I did not fetch the linked repo (DESIGN.md, docs/JOURNAL.md); only the blog post was read.

## Extracted Claims

### Claim 1: Separate roles: deterministic no-AI code governs; the agent only implements; no single AI both writes and approves
- **Evidence**: Description of the project's README: controller is plain code on GitHub Actions; agent implements one task per PR via a gh-aw implement workflow; a different-model-family reviewer checks risky PRs.
- **Confidence**: emerging
- **Quote**: "The controller is deterministic code on GitHub Actions with no AI: it picks tasks, starts agents, watches checks, merges and records everything."
- **Our assessment**: Strong, reusable architectural pattern (orchestration in deterministic code, judgment in agents). Evidence is a single project's design; the benefit is inferred from reported results, not isolated.

### Claim 2: Cross-model-family review of risky PRs removes single-model write+approve
- **Evidence**: Design statement only; no data on catch rate or reviewer disagreement.
- **Confidence**: anecdotal
- **Quote**: "A reviewer from a different model family inspects the risky PRs. No single AI both writes and approves a change."
- **Our assessment**: Plausible diversity-of-failure argument. No evidence the cross-family choice (vs same-family) matters.

### Claim 3: Merge autonomy is scaled by risk tier set in a policy file, not by the agent
- **Evidence**: Three tiers in `policies/tiers.yaml`; 47 tasks split 39 routine / 8 core.
- **Confidence**: emerging
- **Quote**: "Every PR is assigned a tier in policies/tiers.yaml: auto for routine work, auto-strict for shared or core code (requiring reviewer approval, a full regression run and automatic revert if main breaks), and human for the rules and referees themselves, such as golden tests, gates, workflows and the controller."
- **Our assessment**: Notable: the `human` tier covers the rules/gates themselves, so humans approve policy rather than each change. Unclear how tier assignment is computed (path-based?) from the post.

### Claim 4: Policies and verifier live outside the agents' write scope, read at a pinned commit
- **Evidence**: README statement; separate rulebook repository.
- **Confidence**: emerging
- **Quote**: "Agents work in the product repository and cannot edit the policies or the verifier. The controller reads policy at a pinned commit, and the rulebook repo states plainly that agents can’t write to it."
- **Our assessment**: Directly addresses agents weakening their own gates. Enforcement mechanism (permissions, branch protection) is not described.

### Claim 5: Tamper-evident hash-chained audit log, re-verified by an independent verifier lacking the App key
- **Evidence**: Design description; verifier runs on a schedule and appends anchors to its own branch.
- **Confidence**: anecdotal
- **Quote**: "Each controller decision is a hash-chained event on an append-only audit branch that only the controller App can push to."
- **Our assessment**: Interesting security/audit pattern using only Git primitives. No incident evidence that it caught anything.

### Claim 6: Operational safety nets: heartbeat watchdog, kill switch, layered budget caps
- **Evidence**: Listed features, including `policies/budgets.yaml` and `FACTORY_ENABLED`.
- **Confidence**: emerging
- **Quote**: "A FACTORY_ENABLED variable acts as a kill switch, and policies/budgets.yaml caps AI spend per run, per task, per workflow per day and for the whole factory per day."
- **Our assessment**: Four budget levels plus kill switch is a concrete checklist; the post advises setting them "before scaling up".

### Claim 7: CI repair is bounded to two attempts per task, then escalates to a human
- **Evidence**: Workflow description; 45 of 47 PRs needed no repair run.
- **Confidence**: anecdotal
- **Quote**: "If CI fails, the controller starts the gh-aw repair workflow, at most twice per task. A repeated or persistent failure goes to a person."
- **Our assessment**: Simple retry cap pattern; the 2/47 repair rate suggests it was rarely exercised.

### Claim 8: Self-reported results: 47/47 planned tasks merged, zero reverts, median 13 min, $40.12 total (~$0.76/PR)
- **Evidence**: Project's own audit log and dashboard, as of 2026-11-04, over Oct 22 to Nov 3; no independent verification.
- **Confidence**: anecdotal
- **Quote**: "As of 2026-11-04, the README reports 47 of 47 planned tasks merged (39 routine, 8 core) between Oct 22 and Nov 3 with zero reverts."
- **Our assessment**: Treat as self-reported. A porting task with an existing reference implementation and golden tests is likely favorable; "planned tasks" implies the task list was pre-defined. Cost "about $0.76 per accepted PR" covers agent runs only.

### Claim 9: Outcomes tracking via `gh aw logs --outcomes` after every run feeds a public dashboard
- **Evidence**: Workflow step description.
- **Confidence**: anecdotal
- **Quote**: "The outcomes workflow runs gh aw logs --outcomes after every agent run and publishes the results to a branch that feeds a public dashboard."
- **Our assessment**: Real-world use of the outcomes feature documented elsewhere in the corpus.

## Concrete Artifacts

Control loop as described in "How it works" (paraphrased list, not verbatim):

```
1. controller selects next planned task -> dispatches gh-aw implement workflow
2. agent opens one PR for the task
3. CI fails -> controller starts gh-aw repair workflow (max 2 per task); else human
4. by tier: auto-merge | strict gates + independent review | held for owner
5. outcomes workflow: gh aw logs --outcomes -> branch -> public dashboard
```

Named files: `policies/tiers.yaml`, `policies/budgets.yaml`, variable `FACTORY_ENABLED`, `DESIGN.md`, `docs/JOURNAL.md`.

## Cross-References

- **Corroborates**: `blog-ghaw-pelis-agent-factory-intro.md` Claim 6 (guardrails enable rather than constrain) — this is a concrete high-autonomy instance with explicit guardrails.
- **Contradicts**: none found.
- **Extends**: `blog-ghaw-activation-gate-admission.md` Claim 3 (per-component credit allowances) and Claim 8 (cooperative, not hard cap) — here budget caps are controller-side at four levels; `docs-ghaw-outcomes-reference.md` Claim 1 (outcomes measure repository state changes) — applied as a public dashboard. Comparison point: `blog-pragmaticengineer-orosz-openai-software-factory.md` Claim 11 (traditional review makes less sense at agent velocity) — this project instead keeps human approval at the policy level and tiers review by risk.
- **Novel**: Risk-tiered merge with a human-owned tier for rules/gates; policy at a pinned commit outside agent write scope; hash-chained audit branch with key-less independent verifier; two-attempt repair cap.

## Guide Impact

- **Chapter 02**: Add "deterministic controller outside the agent loop, with policy outside agent write scope and a kill switch" as a harness pattern, citing this note (anecdotal; single project).
- **Chapter 03**: Cite the cross-model-family reviewer for risky PRs and the repair cap of two as verification patterns, flagged as unevidenced design choices.
- **Chapter 05**: Risk-tiered merge policy (auto / auto-strict / human) as a team governance model where humans approve rules, not each change.
- **Chapter 06**: Hash-chained audit branch verified without the signing key, and layered budget caps, as threat-model controls.
- **Chapter 01 (Factory Model)**: Use the 47/47 result only with an explicit "self-reported" caveat.

## Extraction Notes

- Source is short; I read the full page via raw HTML. Only the blog post was read; the repo (README, DESIGN.md, JOURNAL.md) was not followed, so mechanism details (tier assignment, enforcement) are unverified.
- Metrics are self-reported by the project and relayed by the blog; the post itself says to treat them so.
