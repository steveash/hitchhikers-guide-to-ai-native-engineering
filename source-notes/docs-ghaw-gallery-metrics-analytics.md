---
source_url: https://github.github.com/gh-aw/gallery/metrics-analytics
source_type: docs
title: "GitHub Agentic Workflows Gallery: Automated Workflow Metrics and Analytics"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: settled
issue: "#3061"
---

# GitHub Agentic Workflows Gallery: Automated Workflow Metrics and Analytics

> A short, self-contained gallery page presenting a portable "Metrics
> Collector" workflow — a daily-scheduled, read-only, repo-memory-backed
> agent that snapshots GitHub Actions run health into dated JSON files —
> as the platform's worked example of automated workflow metrics
> collection. Fetching the exact pinned production workflow this example
> is modeled on surfaces a real discrepancy with the corpus's existing
> narrative-level account of the same-named agent (see Cross-References →
> Contradicts).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Gallery" section — the
  same worked-example tier as `docs-ghaw-gallery-code-improvement.md` and
  `docs-ghaw-gallery-triage-from-side-repo.md`. One YAML frontmatter block,
  one short prompt body, three short paragraphs of prose, and a three-link
  "Learn More" section. No metrics, no production numbers, no author byline
  beyond the team.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team and doc set behind every other `docs-ghaw-*` note in this
  corpus, and the same team that writes the "Meet the Workflows" blog series
  (`blog-ghaw-agent-observability.md`, `blog-ghaw-pelis-agent-factory-intro.md`).
  The reproduced YAML and prompt text are authoritative as a shipped,
  installable example. Fetched via raw markdown source
  (`raw.githubusercontent.com/github/gh-aw/main/docs/src/content/docs/gallery/metrics-analytics.md`),
  not through the rendered SPA, so quotes are exact rather than
  AI-summarized.
- **Scope**: Covers exactly one worked example — a daily-scheduled,
  repository-portable agent that records the last 24 hours of GitHub
  Actions activity as a compact JSON snapshot in repo memory. Does NOT
  cover: the Repo Memory parameter surface in depth (see
  `docs-ghaw-repo-memory-reference.md`), the `gh aw audit`/`gh aw logs`
  command schemas (see `docs-ghaw-audit-reference.md`), cost-monitoring
  mechanics (see `docs-ghaw-cost-management.md`), or GitHub's own
  production "Peli's Agent Factory" observability numbers (see
  `blog-ghaw-agent-observability.md`) — this page is a teaching example,
  not a production case study, despite sharing a name with a workflow
  described in that case study.

## Extracted Claims

### Claim 1: The gallery defines "metrics and analytics" as collecting recent GitHub Actions activity on a schedule and storing a compact snapshot for later trend analysis, explicitly portable to any repository using GitHub Actions
- **Evidence**: Opening paragraph of the page, present before the workflow YAML.
- **Confidence**: settled (first-party framing statement, verbatim from raw source)
- **Quote**: "Metrics and analytics with GitHub Agentic Workflows means collecting recent GitHub Actions activity on a schedule and storing a compact snapshot for later trend analysis. This example works with any repository that uses GitHub Actions."
- **Our assessment**: The "works with any repository" framing is the key differentiator from `blog-ghaw-agent-observability.md`'s treatment of the same concept: that source documents a specific, GitHub-internal production deployment inside `github/gh-aw` monitoring 100+ other workflows; this page presents a generic, repo-agnostic starter template with no assumption of a large agent fleet to monitor. A single-repository team adopting this pattern gets a much smaller, simpler use case (monitor this repo's own CI health) than the fleet-monitoring scenario the blog post describes.

### Claim 2: The published workflow scopes itself to exactly four read-only GitHub permissions (`actions`, `contents`, `issues`, `pull-requests`), a dedicated repo-memory branch/file-glob pair, and a `noop`-only safe-output — a three-part minimal-privilege configuration
- **Evidence**: The full YAML frontmatter block reproduced on the page (see Concrete Artifacts).
- **Confidence**: settled (verbatim YAML from raw source)
- **Quote**: (no prose quote; see YAML frontmatter in Concrete Artifacts)
- **Our assessment**: The three restrictions compound rather than duplicate each other: read-only permissions prevent the agent from writing anything via the GitHub API regardless of what it decides to do; `noop` as the sole safe output means even if the agent tried to request a write-capable safe output (create-issue, create-discussion, add-comment), none is configured for it to call; and the `file-glob: "metrics/**"` constrains what repo-memory itself will accept, scoping the one write path (memory) to a single subdirectory. This is a stronger safety posture than the `noop: report-as-issue: false` config pattern in `docs-ghaw-monitoring-patterns.md` Claim 6 (which merely suppresses one specific issue-creation path for otherwise-writable workflows) — here there is no write-capable safe output configured at all, so the restriction isn't conditional or a fallback, it's structural. For Ch02 (Harness Engineering): document this three-layer minimal-privilege pattern (read-only permissions + noop-only safe-outputs + scoped file-glob) as the reference configuration for any purely observational, data-collection-only agent.

### Claim 3: The collection instructions specify five run-outcome categories per workflow — total, successful, failed, cancelled, and skipped runs — plus execution duration and queue time, scoped to a rolling 24-hour window
- **Evidence**: The workflow's own prompt body, reproduced verbatim on the page.
- **Confidence**: settled (verbatim prompt text from raw source)
- **Quote**: "Collect GitHub Actions activity from the last 24 hours. For each workflow, record total, successful, failed, cancelled, and skipped runs, plus execution duration and queue time when available."
- **Our assessment**: This metric set maps cleanly onto the "operational metrics" layer defined in `docs-ghaw-measuring-impact.md` Claim 6 ("tell you whether the workflow runs reliably") and is a subset of that source's six-metric starter dashboard (Claim 3: run volume, execution success, Actions minutes, inference cost, useful output rate, and acceptance over time) — this gallery example implements only the run-volume and execution-success portions (total/successful/failed/cancelled/skipped, duration, queue time) and captures none of the cost-efficiency (Actions minutes, inference cost), outcome (useful output rate, acceptance), or long-term-impact layers from that four-layer taxonomy. For Ch05 (Team Adoption): cite this gallery example as a "minimum viable operational-layer collector" and explicitly note it is not a complete measurement solution against the four-layer framework — teams adopting it as their only metrics workflow will have zero cost or outcome visibility.

### Claim 4: Snapshots are stored as one dated JSON file per collection window (`metrics/YYYY-MM-DD.json`) that must record the collection window itself, the repository and workflow names, and any missing or incomplete data
- **Evidence**: Second sentence of the workflow's prompt body.
- **Confidence**: settled (verbatim prompt text from raw source)
- **Quote**: "Write a compact JSON snapshot to `metrics/YYYY-MM-DD.json` in repo memory. Include the collection window, repository and workflow names, and any missing or incomplete data. Do not create issues, comments, or pull requests."
- **Our assessment**: Requiring the agent to record "missing or incomplete data" inside the snapshot itself (rather than silently omitting gaps) is a small but important self-reporting discipline — a downstream consumer reading `metrics/2026-08-30.json` six months later can distinguish "this workflow had zero runs that day" from "the collector couldn't reach this workflow's data." The explicit "Do not create issues, comments, or pull requests" restates the safe-output restriction from Claim 2 directly in the agent's own instructions, giving the constraint two independent enforcement layers: the platform-level `safe-outputs: noop:` configuration and the prompt-level instruction. For Ch02: recommend restating structural safety constraints (what the agent cannot do) in the prompt body even when they are already enforced by frontmatter configuration — belt-and-suspenders instruction reduces the chance an agent attempts an action it will only discover is blocked after the fact.

### Claim 5: The page's stated rationale for repo memory over default-branch reporting is that it lets later workflows compare snapshots without adding reports to the default branch
- **Evidence**: Prose sentence immediately following the workflow YAML block.
- **Confidence**: settled (verbatim prose from raw source)
- **Quote**: "Repository memory lets later workflows compare snapshots without adding reports to the default branch."
- **Our assessment**: This is a specific, narrow justification distinct from the fuller Repo Memory vs. Cache Memory tradeoff documented in `docs-ghaw-repo-memory-reference.md` Claim 10 (retention, storage backend, performance) — this page cites only the "don't clutter the default branch" benefit, which is really a proxy for "the memory branch is orphaned and isolated from the code history" (per `docs-ghaw-repo-memory-reference.md` Claim 8, `create-orphan: true` default). For a metrics-collection use case specifically, keeping hundreds of daily JSON snapshots off the default branch avoids polluting `git log`/`git blame` history for the actual codebase with unrelated data files — a concrete, relatable justification for a pattern that could otherwise sound abstract.

### Claim 6: The page frames the combination of read-only GitHub permissions and a `noop`-only safe output as jointly guaranteeing that collection "cannot directly mutate issues or pull requests"
- **Evidence**: Closing prose sentence of the page's main body, before "Learn More."
- **Confidence**: settled (verbatim prose from raw source)
- **Quote**: "The agent receives read-only GitHub permissions and has only the `noop` safe output, so collection cannot directly mutate issues or pull requests."
- **Our assessment**: The word "directly" is doing real work here — it is a precise, hedged safety claim, not an absolute one. The agent still has write access to repo-memory (a git branch), and if that data is later consumed by a different, less-constrained workflow (e.g., a Portfolio Analyst reading the snapshot and acting on it), an *indirect* mutation path exists through the data pipeline even though the collector itself cannot mutate anything. This connects directly to the `noop` safe-output tool documented in `docs-ghaw-audit-with-agents.md` Claim 6 — that note frames `noop` as a completion-signal for *conditional*, otherwise-writable audit-consumer workflows ("if no critical findings, call `noop`"); this gallery example is the stronger case where `noop` is the *only* safe output ever available, not a conditional fallback among several. For Ch03 (Safety and Verification): distinguish "cannot mutate directly" (this pattern) from "cannot mutate at all" (which would require no other agent to ever consume the collected data) when documenting the safety guarantees of read-only collector agents.

### Claim 7: The gallery's teaching example diverges substantially from GitHub's own production Metrics Collector workflow — the exact pinned file the companion "Meet the Workflows" blog post recommends installing — in branch naming, engine, tool access, imports, timeout, and JSON schema richness
- **Evidence**: Direct comparison between this page's reproduced YAML/prompt and `raw.githubusercontent.com/github/gh-aw/v0.45.5/.github/workflows/metrics-collector.md`, fetched independently. The production file was not linked from this gallery page; it was located via the companion blog post `blog-ghaw-agent-observability.md`'s `gh aw add-wizard` installation command for the "Metrics Collector" (same workflow name, same core purpose), which names the identical pinned tag and path.
- **Confidence**: settled (verbatim comparison of two first-party files, both fetched directly)
- **Quote**: (no single quote captures a comparison; see both YAML blocks side by side in Concrete Artifacts)
- **Our assessment**: The production file uses a different repo-memory branch (`memory/meta-orchestrators` vs. this page's `memory/workflow-metrics`), an additional `discussions: read` permission, `engine: copilot` (unspecified on the gallery page), an `agentic-workflows` MCP tool plus the `github` toolset (the gallery page configures only `repo-memory`), a `shared/mood.md` import, a 15-minute timeout, and a JSON schema with per-workflow `safe_outputs`/`engagement`/`quality_indicators` sub-objects plus ecosystem-wide aggregates (`total_workflows`, `active_workflows`, `overall_success_rate`) — none of which appear in the gallery's minimal five-field-plus-duration schema. It also specifies an explicit 30-day retention/cleanup policy (`find ... -mtime +30 -delete`) that the gallery page does not mention at all. This mirrors the same "teaching example is a simplified subset of the real thing" gap already documented for the Code Simplifier gallery page (`docs-ghaw-gallery-code-improvement.md` Claim 6) — a second, independent instance of GitHub Next's gallery pages presenting a deliberately reduced-scope version of a workflow that in production carries substantially more configuration. This is a design choice (accessible teaching example vs. full production complexity), not an error, but readers copying the gallery snippet verbatim get a narrower agent than the one the "Meet the Workflows" post describes.

### Claim 8: The production Metrics Collector's own prose names its repo-memory mount path using the slash-separated form `/tmp/gh-aw/repo-memory/default/metrics/`, matching the patterns/guides documentation rather than the hyphen-separated form shown on the Repo Memory reference page
- **Evidence**: Production `metrics-collector.md` "Current Context" section: "**Storage Path**: `/tmp/gh-aw/repo-memory/default/metrics/`".
- **Confidence**: settled (verbatim text from the production workflow file), though its bearing on the open reference-page discrepancy is circumstantial rather than dispositive
- **Quote**: "Storage Path: `/tmp/gh-aw/repo-memory/default/metrics/`"
- **Our assessment**: `docs-ghaw-repo-memory-reference.md` Claim 1 and its Extraction Notes flag an unresolved discrepancy: the Repo Memory *reference* page (fetched via WebFetch, AI-summarized) reports the default mount path as `/tmp/gh-aw/repo-memory-default/` (hyphen-separated), while the MemoryOps *patterns* and *guides* pages report `/tmp/gh-aw/repo-memory/default/` (slash-separated), and that note recommends the Assayer verify against a live source. This production workflow's own prose — written by the same team, describing its own runtime environment, not fetched via any AI-summarizing tool — uses the slash-separated form. It is one data point, not the reference page itself, so it does not resolve the discrepancy outright, but it is evidence favoring the slash-separated form as the one actually used in shipped GitHub Next workflows. No new contradiction issue filed for this; it corroborates the side already flagged as more likely correct in the existing note.

### Claim 9: The gallery page's "Learn More" section points readers to three separate reference pages — Repository memory, Audit commands, and Cost management — positioning this teaching example as requiring those three references to operate and monitor in practice, rather than being self-contained
- **Evidence**: The page's closing "Learn More" list.
- **Confidence**: settled (verbatim link labels from raw source)
- **Quote**: (list; see Concrete Artifacts) — link labels are "Repository memory", "Audit commands", and "Cost management"
- **Our assessment**: The three linked topics map directly onto pre-existing corpus notes: `docs-ghaw-repo-memory-reference.md` (storage mechanism used by this example), `docs-ghaw-audit-reference.md` (Claim 6: `gh aw logs` for cross-run aggregate reports — the natural tool for reading back what this collector wrote), and `docs-ghaw-cost-management.md` (Claim 4: `gh aw logs` as the primary cost-monitoring command, `gh aw audit <run-id>` for per-run cost breakdown — relevant since this collector workflow itself incurs Actions-minute and inference cost that a team would want to track). None of the three linked pages were re-fetched for this note since all three already have dedicated, deep source notes in the corpus; this claim documents only the page's own framing of what a practitioner needs to read next, not new content from those pages.

## Concrete Artifacts

### Full workflow YAML and prompt (verbatim, from raw markdown source)

```aw wrap title=".github/workflows/metrics-collector.md"
---
on:
  schedule: daily

permissions:
  actions: read
  contents: read
  issues: read
  pull-requests: read

tools:
  repo-memory:
    branch-name: memory/workflow-metrics
    file-glob: "metrics/**"

safe-outputs:
  noop:
---

# Metrics Collector

Collect GitHub Actions activity from the last 24 hours. For each workflow, record total, successful, failed, cancelled, and skipped runs, plus execution duration and queue time when available.

Write a compact JSON snapshot to `metrics/YYYY-MM-DD.json` in repo memory. Include the collection window, repository and workflow names, and any missing or incomplete data. Do not create issues, comments, or pull requests.
```

*Source: `github.github.com/gh-aw/gallery/metrics-analytics`, fetched via `raw.githubusercontent.com/github/gh-aw/main/docs/src/content/docs/gallery/metrics-analytics.md`.*

### "Learn More" links (verbatim from raw source)

```markdown
## Learn More

- [Repository memory](/gh-aw/reference/repo-memory/)
- [Audit commands](/gh-aw/reference/audit/)
- [Cost management](/gh-aw/reference/cost-management/)
```

### Production Metrics Collector frontmatter (for comparison — NOT this gallery page's content)

Fetched directly from `raw.githubusercontent.com/github/gh-aw/v0.45.5/.github/workflows/metrics-collector.md`, the file that `blog-ghaw-agent-observability.md`'s companion blog post links via `gh aw add-wizard`. Reproduced here strictly as comparative evidence for Claims 7–8, not as content of the gallery page itself.

```yaml
---
description: Collects daily performance metrics for the agent ecosystem and stores them in repo-memory
on: daily
permissions:
  contents: read
  issues: read
  pull-requests: read
  discussions: read
  actions: read
engine: copilot
tools:
  agentic-workflows:
  github:
    toolsets: [default]
  repo-memory:
    branch-name: memory/meta-orchestrators
    file-glob: "metrics/**"
timeout-minutes: 15
imports:
  - shared/mood.md
---
```

Selected body text (Current Context and Important Notes sections):

```
- **Storage Path**: `/tmp/gh-aw/repo-memory/default/metrics/`
...
- **DO NOT** create issues, PRs, or comments - this is a data collection agent only
- **DO NOT** analyze or interpret the metrics - that's the job of meta-orchestrators
...
**Retention Policy**:
- Keep last 30 days of daily metrics
- Delete daily files older than 30 days from the metrics directory
```

*Source: `raw.githubusercontent.com/github/gh-aw/v0.45.5/.github/workflows/metrics-collector.md`.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-audit-with-agents.md` Claim 6 (`noop` safe output as an explicit completion signal, preventing silent-success ambiguity): this gallery example is a stronger, unconditional instance of the same mechanism — `noop` is the *only* configured safe output, not a conditional fallback among several write-capable options.
  - `docs-ghaw-repo-memory-reference.md` Claim 8 (`create-orphan: true` default decouples memory branch history from code history): Claim 5 above's stated rationale ("without adding reports to the default branch") is the practitioner-facing benefit of exactly this orphan-branch default.
  - `docs-ghaw-repo-memory-reference.md` Claim 1 / Extraction Notes (open path-format discrepancy between reference page and patterns/guides pages): Claim 8 above adds a third, independently-sourced data point (the production workflow's own prose) favoring the slash-separated `/tmp/gh-aw/repo-memory/default/` form.
  - `docs-ghaw-measuring-impact.md` Claim 6 (operational metrics answer "does the workflow run reliably?"): Claim 3 above shows this gallery example implements exactly and only the operational layer of that four-layer taxonomy.

- **Contradicts**:
  - **Filed as new issue #3094**: `blog-ghaw-agent-observability.md` Claim 3 and its Concrete Artifacts state that GitHub's production "Metrics Collector" agent created 41 daily Discussion posts (e.g., Discussion #6986) as its own output. The actual production `metrics-collector.md` workflow file at the exact pinned version (`v0.45.5`) that same blog post links readers to install has no `safe-outputs:` configuration at all, only read-only permissions, and its own prompt text states "DO NOT create issues, PRs, or comments - this is a data collection agent only" — it writes exclusively to repo-memory. Both sources are first-party GitHub Next material describing the same named, pinned workflow, and they give incompatible answers to a checkable factual question (does this agent post human-visible Discussions, or is it a silent repo-memory-only collector?). This gallery page's own teaching example (`safe-outputs: noop:` only, explicit "Do not create issues, comments, or pull requests" in its prompt) is a second, independently-authored GitHub Next source consistent with the "silent collector" reading — corroborating but not dispositive, since the gallery example is explicitly a simplified/portable variant rather than the exact production file. No verdict is picked in this note; see issue #3094 for the full Side A/Side B writeup and resolution status.

- **Extends**:
  - `docs-ghaw-gallery-code-improvement.md` Claim 6 (gallery page's reproduced YAML omits safety/scoping fields present in the "real" linked source workflow): Claim 7 above is a second, independent instance of the same gap pattern — a GitHub Next gallery page presenting a reduced-configuration teaching version of a workflow that carries materially more configuration (and, in this case, a different repo-memory branch name and JSON schema) in its actual production form.
  - `docs-ghaw-monitoring-patterns.md` Claim 6 (`noop: report-as-issue: false` as a conditional no-op-suppression config for otherwise-writable workflows): Claim 2 above documents the structurally stronger case of a workflow with no write-capable safe output configured at all, rather than one write path being conditionally suppressed.
  - `docs-ghaw-cost-management.md` and `docs-ghaw-audit-reference.md`: Claim 9 above shows this gallery page explicitly directing practitioners to those two references (plus Repo Memory) as the necessary follow-up reading to operate this pattern in production — no new content extracted from those pages here, since both already have dedicated corpus notes.

- **Novel**:
  - **The specific five-category run-outcome metric set (total/successful/failed/cancelled/skipped + duration + queue time) as a minimal operational-layer starter** (Claim 3): not documented in this exact form in `docs-ghaw-measuring-impact.md`, which describes the operational layer abstractly without this concrete field list.
  - **The three-layer minimal-privilege pattern for pure-collector agents** (Claim 2: read-only permissions + noop-only safe-outputs + scoped file-glob, with no conditional write path at all): new to the corpus as a named, complete pattern; prior notes document each layer independently but not this specific combination as a reference configuration for observation-only agents.
  - **The Metrics Collector Discussions-vs-repo-memory-only discrepancy** (Claim 7's underlying comparison, filed as contradiction issue #3094): entirely new to the corpus, surfaced only by fetching the exact pinned production file rather than relying on the narrative account in the existing blog post note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the three-layer minimal-privilege collector pattern (Claim 2) as the reference configuration for any workflow whose sole job is data collection with zero intended side effects: read-only GitHub permissions, a `noop`-only (not merely conditional) safe-output set, and a `file-glob`-scoped repo-memory write path. Distinguish this from the conditional `noop: report-as-issue: false` pattern in `docs-ghaw-monitoring-patterns.md`, which suppresses one write path on an otherwise-writable workflow rather than configuring no write path at all.
  - Add the "restate structural constraints in the prompt body even when already enforced by frontmatter" discipline (Claim 4) as a defense-in-depth habit for safety-relevant agent instructions.

- **Chapter 05 (Team Adoption — measurement and rollout)**:
  - Cite this gallery example as a "minimum viable operational-layer collector" against the four-layer measurement taxonomy in `docs-ghaw-measuring-impact.md` (Claim 3, Claims 5–9): it implements only run-volume and execution-success metrics, with zero cost-efficiency, outcome, or long-term-impact instrumentation. Teams adopting only this pattern should understand it answers "is CI running reliably?" and nothing about cost, acceptance, or system-level impact.
  - Do not cite `blog-ghaw-agent-observability.md`'s "Metrics Collector created 41 discussions" claim without also surfacing the filed contradiction (issue #3094) — the Smith should treat the Metrics Collector's actual output mechanism (Discussions vs. silent repo-memory) as unresolved pending that issue.

- **Chapter 03 (Safety and Verification)**:
  - Add the "cannot mutate *directly*" hedge (Claim 6) as a precise-language example: a read-only, noop-only agent still has a write path (repo-memory) that downstream, less-constrained agents could act on indirectly. Safety claims about collector agents should specify whether "cannot mutate" means "this agent has no write path" or "this agent's data has no consumers with write paths," which are different guarantees.

## Extraction Notes

1. **Fetched raw markdown, not the rendered SPA**: An initial `WebFetch` pass on the gallery page's rendered URL returned a plausible-looking but AI-paraphrased summary (invented section headings like "## Key Features" and "## Workflow Functionality" that do not appear in the actual source markdown, and a paraphrased rather than verbatim rendering of the prompt text) — the same WebFetch-summarization failure mode already documented in several existing `docs-ghaw-*` notes for this Astro/Starlight-rendered documentation site. I located and fetched the underlying raw markdown source directly (`raw.githubusercontent.com/github/gh-aw/main/docs/src/content/docs/gallery/metrics-analytics.md`) via the `github/gh-aw` repository's git tree, and all quotes in this note are copied verbatim from that raw file, not from the discarded WebFetch summary.

2. **Followed a related page reached via cross-reference rather than a direct link**: MINER.md §1 directs following up to 5 linked pages that seem substantive. This gallery page's own links (Repository memory, Audit commands, Cost management) all already have dedicated, deep corpus notes and were not re-fetched. However, in the course of researching this page I identified — via the companion "Meet the Workflows: Metrics & Analytics" blog post already in the corpus (`blog-ghaw-agent-observability.md`) — that the same-named, same-purpose production workflow file is publicly available at a pinned tag (`v0.45.5`) in `github/gh-aw`. I fetched that file directly (not a link on the gallery page itself) because it is the real-world counterpart to this teaching example and because comparing them surfaced both a legitimate "teaching vs. production" gap (Claim 7) and a factual contradiction with the existing blog-post note (Claim 7/Contradicts, issue #3094). This is disclosed here so the Assayer can evaluate whether that comparison was in scope; I judge it was, since MINER.md's "read deeply" and "cross-reference against existing notes" instructions both point toward exactly this kind of verification.

3. **Companion blog post's other two workflows (Portfolio Analyst, Audit Workflows) out of scope**: The "Meet the Workflows: Metrics & Analytics" blog post covers three workflows; this gallery page covers only the Metrics Collector. I fetched the production `portfolio-analyst.md` and `audit-workflows.md` files as well while investigating, but did not extract claims from them here since they are not the subject of issue #3061's source URL and are already narratively covered (at the production-metrics level) by the existing `blog-ghaw-agent-observability.md` note. If a future source issue targets a gallery page or documentation specific to either of those two workflows, that richer configuration data would be a natural extraction target at that time.

4. **No publication date**: The gallery page carries no visible publication or last-updated date; `date_published` is left null, consistent with other `docs-ghaw-*` notes in this corpus.

5. **One contradiction filed**: Reviewed `blog-ghaw-agent-observability.md`, `blog-ghaw-pelis-agent-factory-intro.md`, `docs-ghaw-measuring-impact.md`, `docs-ghaw-monitoring-patterns.md`, `docs-ghaw-repo-memory-reference.md`, `docs-ghaw-audit-reference.md`, `docs-ghaw-audit-with-agents.md`, `docs-ghaw-cost-management.md`, and `docs-ghaw-gallery-code-improvement.md`. One claim (Claim 7's underlying comparison) materially opposes `blog-ghaw-agent-observability.md` Claim 3 at the MINER.md §4a threshold — filed as contradiction issue #3094, verdict left to human/Smith resolution. No other claims in this source oppose existing source notes; the repo-memory rationale, safe-output pattern, and reference-page pointers are all consistent with (and corroborate) the existing corpus.
