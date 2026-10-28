---
source_url: https://github.github.com/gh-aw/blog/2026-10-27-activation-gate/
source_type: blog-post
title: "Before the Agent Starts: The Activation Gate (GitHub Agentic Workflows)"
author: Copilot (GitHub Agentic Workflows blog byline)
date_published: 2026-10-27
date_extracted: 2026-10-28
last_checked: 2026-10-28
status: current
confidence_overall: anecdotal
issue: "#4381"
---

# Before the Agent Starts: The Activation Gate (GitHub Agentic Workflows)

> gh-aw adds an opt-in "admission" step (`on.admission: true`) in which a compiler-generated job authenticates by OIDC to an external authority that approves or denies the run and returns explicit AI Credit allowances, with the post candidly stating that this is a cooperative gate and not a hard spending cap.

## Source Context

- **Type**: blog-post (official gh-aw blog, bylined "Copilot", 2026-10-27; arrived via the `github-agentic-workflows` trusted feed)
- **Author credibility**: First-party vendor description of its own feature. No measurements or deployments are reported; the post describes a protocol and its stated limits.
- **Scope**: Covers the admission flow, approval payload semantics, opt-in and variable configuration, OIDC auth, the CAO integration boundary, the `conclusion_admission` callback, and outage/limit caveats. Does NOT cover the admission service specification itself, example authority implementations, or any outcomes. It links to "centralized cost controls" docs for rollout details; that page was not followed.

## Extracted Claims

### Claim 1: Admission adds a central start-time decision point before the agent session starts
- **Evidence**: Feature description; no metrics.
- **Confidence**: anecdotal
- **Quote**: "The activation gate adds a place to make that decision before the agent starts."
- **Our assessment**: Real design point: the budget/priority decision is moved out of the workflow repo into a separate authority. Mechanism is concrete, but unvalidated in practice.

### Claim 2: The protocol is a compiler-owned job that gets an OIDC token and posts workflow identity plus compiled hash to `/api/admission`
- **Evidence**: Protocol description.
- **Confidence**: anecdotal
- **Quote**: "It requests a GitHub Actions OIDC identity token for the authority’s audience, then posts the invocation identity and compiled workflow hash to /api/admission."
- **Our assessment**: Binding the request to the compiled workflow hash lets the authority reason about exactly which compiled workflow is asking; OIDC avoids distributing PATs or provider credentials.

### Claim 3: Approvals carry independent per-component AI Credit allowances that replace, not cap, local limits
- **Evidence**: Example JSON payload and semantics statement.
- **Confidence**: anecdotal
- **Quote**: "Each supplied allowance replaces that component’s runtime limit, even if it is higher than the workflow’s configured limit."
- **Our assessment**: Important and slightly surprising: the authority can raise limits above what the workflow author configured, so trust in the authority is total for supplied components. Omitted allowances leave existing limits (post: "the three values are not a shared pool").

### Claim 4: A valid approval supersedes the local daily-credit check; explicit denial stops activation
- **Evidence**: Stated behavior.
- **Confidence**: anecdotal
- **Quote**: "A valid approval supersedes the local daily-credit check for that activation."
- **Our assessment**: Consequence: once admission is on, shared-budget enforcement lives only in the authority; local checks are bypassed on approval.

### Claim 5: Opt-in is per-workflow or repo-wide, and a workflow cannot opt out of a repo-wide opt-in; compile is required
- **Evidence**: Configuration examples.
- **Confidence**: anecdotal
- **Quote**: "A workflow-level false cannot override that repository opt-in."
- **Our assessment**: Gives repo admins a way to mandate participation, though the post's own caveat (Claim 8) says editors with write access can still remove it.

### Claim 6: Endpoint, audience and outage policy are Actions variables changeable without recompilation
- **Evidence**: Variable table (`GH_AW_DEFAULT_ADMISSION_URL`, `_AUDIENCE`, `_ON_OUTAGE`).
- **Confidence**: anecdotal
- **Quote**: "Once the jobs are compiled in, changing these variables does not require recompilation."
- **Our assessment**: Good separation of compile-time wiring from runtime policy endpoints; repo variables take precedence over org variables, which is also the override path the post flags as a weakness.

### Claim 7: Outage policy is an explicit availability-vs-control choice; denials fail closed regardless
- **Evidence**: Stated behavior.
- **Confidence**: anecdotal
- **Quote**: "Explicit denials and invalid approvals block under either policy."
- **Our assessment**: Default `ignore` favors availability (falls back to local controls); `block` favors control. Sensible, standard fail-open/fail-closed tradeoff made explicit.

### Claim 8: Admission is cooperative, not a hard cap
- **Evidence**: Authors' own stated limitations.
- **Confidence**: anecdotal
- **Quote**: "Admission remains cooperative."
- **Our assessment**: Strongest takeaway. The post lists the gaps: "Workflow editors can remove participation, repository-variable administrators can override organization defaults, and concurrent runs can overshoot a shared budget. Hard quotas, reservations, and mid-run cancellation require independently enforced backend controls." (Same passage; summarized here, not a single quote.) Teams should not treat it as a guarantee.

### Claim 9: Least-privilege OIDC scoping: `id-token: write` goes only to isolated admission and callback jobs, not the agent
- **Evidence**: Stated design.
- **Confidence**: anecdotal
- **Quote**: "The feature grants id-token: write to its isolated admission and completion-callback jobs, not to the agent merely because admission is enabled."
- **Our assessment**: Consistent with keeping credentials away from the agent job; note hand-authored reusable-workflow callers must also grant that scope.

### Claim 10: A best-effort `conclusion_admission` callback delivers end-of-session metadata to the authority
- **Evidence**: Stated behavior.
- **Confidence**: anecdotal
- **Quote**: "It is end-of-session delivery, not live streaming or billing settlement."
- **Our assessment**: The authority gets usage metadata after the fact (and artifact IDs for full session retrieval), but failure only warns, so authority-side accounting can have gaps.

### Claim 11: The gate is an integration contract, not a hosted service
- **Evidence**: CAO section.
- **Confidence**: anecdotal
- **Quote**: "That is an integration contract, not a claim that installing gh-aw deploys CAO or a hosted admission server."
- **Our assessment**: Adopters must build or provision the authority; the practical cost of adoption is higher than the config snippet suggests.

## Concrete Artifacts

```json
// Illustrative approval payload (source: "illustrative allowances, not built-in tiers")
{
  "max_ai_credits": 1000,
  "max_ai_credits_threat_detection": 100,
  "max_ai_credits_evals": 50
}
```

```yaml
# Workflow opt-in (source)
on:
  workflow_dispatch:
  admission: true
```

```
Repo-wide opt-in: "admission": true in .github/workflows/aw.json
Variables: GH_AW_DEFAULT_ADMISSION_URL (HTTPS, ends /api/admission)
           GH_AW_DEFAULT_ADMISSION_AUDIENCE (default: endpoint URL)
           GH_AW_DEFAULT_ADMISSION_ON_OUTAGE (ignore | block; default ignore)
Endpoints: POST /api/admission (pre-run), /api/conclusion (post-run callback)
Note: setting an endpoint alone does not generate admission jobs; recompile with `gh aw compile`.
```

## Cross-References

- **Corroborates**: `blog-ghaw-weekly-2026-09-21.md` Claim 10 — also a fail-closed guardrail stance for ambiguous cost evidence (different layer: post-run AIC accounting vs. pre-run admission).
- **Contradicts**: None found.
- **Extends**: `blog-ghaw-ai-credits-migration.md` Claim 1 (AIC as the primary spend metric) — this post uses AIC as the unit the authority allocates; `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` pre-agent cancellation as the highest-leverage saving) — admission adds a centralized budget decision at the same pre-agent point, versus a local trigger-condition filter.
- **Novel**: Centralized OIDC-authenticated admission authority, replace-not-cap allowance semantics, the `conclusion_admission` callback, and an explicit vendor statement that such gates are cooperative and need backend enforcement for hard quotas.

## Guide Impact

- **Chapter 05**: When discussing org-wide agent cost governance, add admission as a pattern for central budgets and contrast it with per-workflow limits; include the caveat that it is advisory and concurrent runs can overshoot.
- **Chapter 06**: Cite the OIDC-scoped, isolated-job design (`id-token: write` only on admission/callback jobs) as an example of keeping identity credentials away from the agent.
- **Chapter 02**: Mention start-time admission as a harness-level gate in front of the agent runtime; note the fail-open default (`ignore`) as a design choice to make deliberately.

## Extraction Notes

Read the full post via raw HTML fetch; quotes copied from the rendered text. Single vendor post, no outcome data, hence `anecdotal`. Linked "centralized cost controls" docs and the admission service specification were not followed. Triage-listed notes `blog-ghaw-weekly-2026-03-30.md` and `docs-ghaw-triggers-reference.md` were not cited because I did not verify specific claim numbers.
