---
source_url: https://github.github.com/gh-aw/blog/2026-09-28-weekly-update/
source_type: blog-post
title: "Weekly Update – September 28, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-09-28
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: emerging
issue: "#3783"
---

# Weekly Update – September 28, 2026 (GitHub Agentic Workflows)

> gh-aw v0.89.22 executes the previously announced removal of the `docker-sbx` and `gvisor` sandbox runtimes (Cloud Hypervisor only), adds a `network.hosted-web` domain policy for provider-hosted web tools, tightens firewall checks for web tools, and expands `gh aw audit` (grouping, MCP payload size, friction cost, skill usage).

## Source Context

- **Type**: blog-post (weekly release-notes digest, byline "Copilot")
- **Author credibility**: First-party gh-aw project blog (GitHub Next / Microsoft Research). Authoritative for what shipped, but a short changelog-style digest: one-line summaries per PR, no design rationale or measurements beyond the Agent-of-the-Week anecdote.
- **Scope**: Release v0.89.22 (Sept 27; builds on v0.89.21 and v0.89.20): one breaking change, six "What's New" items, four "Notable Fixes", three "Notable Pull Requests", and an Agent of the Week (`ci-coach`). Does NOT cover: the PR bodies (not fetched), migration mechanics beyond a one-line frontmatter change, the semantics/schema of `network.hosted-web`, or a removal of the `docker` default runtime.

## Extracted Claims

### Claim 1: The `docker-sbx` and `gvisor` sandbox runtimes were removed in v0.89.22 (breaking change); isolated agent execution now runs only on Cloud Hypervisor
- **Evidence**: Release notes "! Breaking Change" section, PR #63034. First-party statement; no PR body fetched.
- **Confidence**: settled (first-party statement of a shipped change)
- **Quote**: "Docker sbx and gVisor sandbox runtimes removed (#63034) — isolated agent execution now runs exclusively on Cloud Hypervisor."
- **Our assessment**: This is the removal step of the deprecation announced in `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 1 ("deprecated and will be removed in a future release"), executed roughly three weeks later. The Prospector triage framed this as contradicting `blog-ghaw-weekly-2026-07-13.md` (which introduced the two runtimes as new options); that is a lifecycle change over time, and the underlying source disagreement is already tracked in contradiction issue #3285 (Aug docs recommending `docker-sbx`/`gvisor` vs. Sept deprecation). This post strengthens the Side-B position: removal is now shipped, not just planned. "Exclusively" refers to *isolated* execution; the default Docker/AWF runtime is not stated to be removed (see `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 3), so we read it as "the microVM tier is Cloud Hypervisor only."

### Claim 2: Workflows still setting `sandbox.agent.runtime: docker-sbx` or `gvisor` must be switched to `cloud-hypervisor` before the next recompile
- **Evidence**: Same breaking-change bullet; closing "Try It Out" section repeats the warning.
- **Confidence**: settled
- **Quote**: "If your workflow frontmatter still sets sandbox.agent.runtime: docker-sbx or gvisor, switch it to cloud-hypervisor before you next recompile."
- **Our assessment**: This drops the "otherwise fall back to default Docker" branch from `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 6; the post only names `cloud-hypervisor` as the target, which is not viable for workflows off eligible GitHub-hosted runners (`blog-ghaw-cloud-hypervisor-consolidation.md` Claim 5; `blog-ghaw-weekly-2026-09-07.md` Claim 9 records the incompatibilities the platform hit when migrating its own fleet). Whether an ineligible workflow should delete the `runtime:` line is not addressed here. Failure mode on recompile with a removed value is not described.

### Claim 3: A new `network.hosted-web` frontmatter key lets authors allow or block domains reached by provider-hosted Claude and Codex web tools, which operate outside AWF's network boundary
- **Evidence**: "What's New" bullet, PR #63212. No schema, example, or default given.
- **Confidence**: emerging
- **Quote**: "the new network.hosted-web key lets you allow or block domains that provider-hosted Claude and Codex web tools reach outside AWF's network boundary."
- **Our assessment**: Novel and security-relevant: it concedes that provider-side web tools (executed on the vendor's infrastructure) escape the AWF egress firewall that `docs-ghaw-sandbox-reference.md` Claim 2 describes as the isolation implementation for all engines, and adds a separate policy channel for them. The enforcement point is presumably the provider or compiler, not AWF; the post does not say. Compare `docs-ghaw-web-search.md` Claim 5, which covers egress for MCP-based search (Tavily) via `network.allowed`; `hosted-web` is the analogous control for *built-in* provider tools.

### Claim 4: Firewall compatibility checks are now enforced for Copilot and web tools, scoped to the web tools a workflow actually enables, and false blocked-domain warnings for successful requests were fixed
- **Evidence**: "What's New" bullet, PRs #63474, #63632, #63246.
- **Confidence**: emerging
- **Quote**: "Copilot and web tools now get enforced firewall compatibility checks (#63474), scoped precisely to the web tools a workflow actually enables (#63632), while false blocked-domain warnings for otherwise-successful requests were squashed (#63246)."
- **Our assessment**: Shows a shift from advisory to enforced checks (a workflow whose enabled web tools cannot be firewalled is presumably rejected/flagged at compile time; the post does not say which). The scoping fix (#63632) suggests the initial enforcement over-applied. The false-warning fix is a reminder that blocked-domain telemetry can be noisy; treat it cautiously when tuning allowlists.

### Claim 5: `gh aw audit --group` aggregates findings by run and code with occurrence counts, in pretty, markdown, or JSON output
- **Evidence**: "What's New" bullet, PR #63032.
- **Confidence**: settled (shipped feature; description only)
- **Quote**: "gh aw audit --group now aggregates findings by run and code with occurrence counts, in pretty, markdown, or JSON output."
- **Our assessment**: Extends the audit surface in `docs-ghaw-audit-reference.md` (Claims 2, 5, 9: multi-run diff, report sections, `--format`), which predates grouping. Useful for fleet-level triage where one finding code repeats across many runs.

### Claim 6: Audit gained an opt-out for automatic baseline downloads and reports MCP payload size
- **Evidence**: "More audit visibility" bullet, PRs #63012 and #63687.
- **Confidence**: emerging
- **Quote**: "an opt-out for automatic audit baseline downloads (#63012) and MCP payload size reporting in audit (#63687) give workflow authors finer control over what audit runs measure and fetch."
- **Our assessment**: Implies audit fetches a baseline by default (network/artifact cost), consistent with the artifact-caching concerns in `blog-ghaw-weekly-2026-09-21.md` Claims 2 and 4. MCP payload size is a context-cost signal relevant to tool-output bloat.

### Claim 7: Copilot prompts over 100 KiB are now delivered via stdin instead of being truncated
- **Evidence**: "What's New" bullet, PR #62766 (community contribution, credited to @davidslater).
- **Confidence**: emerging
- **Quote**: "prompts over 100 KiB are now delivered via stdin instead of being truncated, preserving full context for big agentic workflows."
- **Our assessment**: Documents a concrete failure mode of CLI-argument prompt passing: silent truncation (presumably an OS/argv size limit; the post does not state the cause). General lesson for harnesses: pass large prompts by stdin/file, not argv, and never truncate silently.

### Claim 8: The daily AIC (cost-accounting) guardrail can now persist its memory in a repository-backed repo-memory backend
- **Evidence**: "What's New" bullet, PR #62958.
- **Confidence**: anecdotal (one line; no detail)
- **Quote**: "memory persistence now supports repository-backed storage for cost accounting."
- **Our assessment**: Continues the AIC guardrail thread in `blog-ghaw-weekly-2026-09-21.md` Claim 10 (fail-closed accounting). Pairs with the staleness risk in `blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 5: repo-backed memory persists across runs but does not guarantee currency.

### Claim 9: Several security/reliability fixes shipped, including pinning `pull_request` activation checkout to the base SHA for supply-chain safety
- **Evidence**: "Notable Fixes" bullets: #63490 (dangling `safe-outputs-app-token` references when staged), #63497 (repo memory retry auth), #63498 (cache-memory validation marker EACCES), #63499, #63678.
- **Confidence**: emerging
- **Quote**: "Pinned pull_request activation checkout to the base SHA for improved supply-chain safety (#63499)."
- **Our assessment**: Checking out the base SHA (not the PR head) during activation prevents PR-controlled code from influencing the activation job that gates agent execution; this is a standard pull_request_target-style hardening. The post gives no threat narrative. The staged-mode token fix (#63490) relates to `docs-ghaw-staged-mode-reference.md`.

### Claim 10: New audit artifacts attribute friction cost, track skill usage, and surface AWF steering counters
- **Evidence**: "Notable Pull Requests" bullets (no PR numbers given in the post).
- **Confidence**: anecdotal
- **Quote**: "audit output now attributes friction costs directly, making it easier to spot where workflows are burning extra cycles."
- **Our assessment**: Points toward audit as an observability layer for agent inefficiency (friction cost), tool/skill invocation visibility, and firewall steering activity. No definition of "friction cost" is given; do not cite as a metric definition.

### Claim 11: The `ci-coach` scheduled agent found and fixed an imbalanced CI test shard across two consecutive days, with projected shard time cut from ~93s to ~29s
- **Evidence**: Agent of the Week narrative: A-C shard ~106s vs 40-48s for the other four; ~20% of the gap from one test with `time.Sleep` cooldowns; PR #63187 removed the 500ms sleep loop via a mocked rate limit; a next-day PR proposed a "Linters" shard. Projection, not a measured outcome.
- **Confidence**: anecdotal
- **Quote**: "Run this class of workflow on a schedule against your CI config files — it's great at spotting shard imbalances and dead-weight sleeps that are easy to miss by eye but add up fast across hundreds of runs."
- **Our assessment**: A plausible, small, verifiable example of a scheduled "coach" agent proposing PRs (human review retained). Numbers are self-reported by the post and the second PR's gain is projected only. Note the iterative behavior: the agent revisits the same target the next day, which is useful but also a possible churn risk.

## Concrete Artifacts

```yaml
# Source: gh-aw weekly update 2026-09-28, Breaking Change section
# Before (no longer valid as of v0.89.22):
sandbox:
  agent:
    runtime: docker-sbx   # or: gvisor
# After:
sandbox:
  agent:
    runtime: cloud-hypervisor
```
(Reconstruction of the frontmatter path named in the post's text, "sandbox.agent.runtime"; the post itself shows no code block.)

```
# Source: same post, "What's New" / "Try It Out"
frontmatter key:  network.hosted-web        (#63212)
CLI:              gh aw audit --group       (#63032)  output: pretty | markdown | JSON
Prompt transport: Copilot prompts > 100 KiB via stdin (#62766)
Release:          v0.89.22 (Sept 27, 2026), after v0.89.21, v0.89.20
```

## Cross-References

- **Corroborates**: `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 1 (deprecation plan) and Claim 4 (`cloud-hypervisor` as the supported direction) — this post confirms the removal shipped. `blog-ghaw-weekly-2026-09-07.md` Claim 9 (fleet migration to Cloud Hypervisor).
- **Contradicts:** Existing contradiction issue #3285 (`docker-sbx`/`gvisor` recommended in `docs-ghaw-agent-runtimes-reference.md` vs. deprecated). This post adds evidence for the "deprecated/removed" side; no new contradiction filed. It also supersedes `blog-ghaw-weekly-2026-07-13.md` Claims 1 and 6 (introduced `gvisor`/`docker-sbx`) and `docs-ghaw-agent-runtimes-reference.md`, which recommends `docker-sbx` as the strongest tier. This is temporal supersession, and no verdict is asserted here.
- **Extends**: `docs-ghaw-sandbox-reference.md` Claim 2 (AWF as default egress control) with `network.hosted-web` for tools outside AWF's boundary; `docs-ghaw-audit-reference.md` with `--group`; `blog-ghaw-weekly-2026-09-21.md` Claim 10 (AIC guardrail).
- **Novel**: Removal (not just deprecation) of two runtimes; `network.hosted-web` for provider-hosted web tools; stdin delivery for >100 KiB Copilot prompts; base-SHA pinning for `pull_request` activation checkout; `ci-coach` agent.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Where the guide describes gh-aw sandbox runtimes, remove `gvisor` and `docker-sbx` as selectable options (Claims 1-2) and state that the microVM tier is Cloud Hypervisor only, with the eligibility limits from `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 5. Add the large-prompt lesson (Claim 7): deliver big prompts via stdin, avoid silent truncation.
- **Chapter 04 (Safety and Constraints)**: Add that provider-hosted web tools run outside the AWF firewall and need a separate domain policy (`network.hosted-web`, Claim 3), and that firewall compatibility checks for web tools are now enforced (Claim 4). Mention base-SHA checkout pinning as a supply-chain control (Claim 9).
- **Chapter 03 (Agent Orchestration)**: Optional: `gh aw audit --group` and friction/skill/steering audit data (Claims 5, 6, 10) as fleet-level observability; `ci-coach` (Claim 11) as a scheduled-agent example with an anecdotal-grade caveat.
- **Contradictions**: When #3285 is resolved, this post should be cited as evidence that removal has shipped.

## Extraction Notes

- Fetched the raw HTML of the post with curl and read the full article text; the WebFetch summarizer was not relied on for quotes. Quotes were copied from the rendered text with typographic apostrophes normalized to ASCII.
- No sub-pages followed: the post links only to PR numbers and the gh-aw repo; PR bodies were not fetched, so claims are limited to the post's one-line descriptions.
- Cross-references were verified against the cited note claim numbers (`blog-ghaw-cloud-hypervisor-consolidation.md` Claims 1, 3-6; `blog-ghaw-weekly-2026-09-07.md` Claim 9; `blog-ghaw-weekly-2026-09-21.md` Claims 2, 4, 10; `docs-ghaw-sandbox-reference.md` Claim 2; `docs-ghaw-audit-reference.md` Claims 2, 5, 9; `docs-ghaw-web-search.md` Claim 5; `blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 5). `blog-ghaw-weekly-2026-07-13.md` Claims 1 and 6 are cited from its claim headings.
- The Prospector's suggestion of a "critical contradiction" with the July 13 note was treated as supersession over time; the standing contradiction issue #3285 already covers the topic, so a duplicate was not filed.
