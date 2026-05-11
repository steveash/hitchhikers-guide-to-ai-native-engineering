---
source_url: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-quality-hygiene/
source_type: blog-post
title: "Meet the Workflows: Fault Investigation"
author: Don Syme, Peli de Halleux, Mara Kiefer (GitHub Agentic Workflows team)
date_published: 2026-01-13
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#147"
---

# Meet the Workflows: Fault Investigation

> Part 8 of GitHub's 19-part "Peli's Agent Factory" series — provides first-party
> production evidence for three specialized fault-investigation workflows (CI Doctor,
> Schema Consistency Checker, Breaking Change Checker) that collectively form a
> proactive "hygiene cluster," with the CI Doctor achieving a 69% merge rate (9/13 PRs)
> for autonomous CI failure investigation and the Schema Consistency Checker generating
> 55 analysis discussions from cross-concern drift detection.

## Source Context

- **Type**: blog-post (GitHub Agentic Workflows team; gh-aw blog, published 2026-01-13;
  page URL slug is "quality-hygiene" though the series entry is titled "Fault
  Investigation Workflows" in the series index)
- **Author credibility**: Don Syme (F# creator, GitHub), Peli de Halleux (Principal
  Researcher, GitHub Next), and Mara Kiefer — the same core team across all "Meet the
  Workflows" posts. First-party reports from the factory operators on workflows they
  built and run. Production metrics (69% merge rate, 55 discussions) are self-reported
  from the live `github/gh-aw` repository. High credibility for claims about their own
  system; claims may not generalize to other codebases or CI environments.
- **Scope**: Three workflows — CI Doctor (CI failure investigation), Schema Consistency
  Checker (cross-concern drift detection), Breaking Change Checker (backward-compatibility
  monitoring). Covers production metrics and concrete fix examples for each. Does NOT
  cover: engine assignments per workflow (those come from `docs-ghaw-agent-factory-status.md`
  Claim 2, which places Schema Consistency Checker under claude), cost or latency of runs,
  how the workflows handle false positives, or the implementation internals of the
  diagnostic algorithms.

## Extracted Claims

### Claim 1: CI Doctor achieves a 69% merge rate (9/13 PRs) for autonomous CI failure investigation — the first production benchmark for agentic CI repair in this corpus

- **Evidence**: Production data from GitHub's own `gh-aw` repository. The post reports
  "9 merged PRs out of 13 proposed (69% merge rate)" for the CI Doctor workflow. Specific
  fix examples include: adding Go module download pre-flight checks, and adding retry logic
  to prevent proxy 403 failures. Both are concrete CI infrastructure fixes, not trivial
  comment changes.
- **Confidence**: anecdotal (self-reported by workflow authors; no time window disclosed,
  no rejection reasons given for the 4 non-merged PRs, no control group)
- **Quote**: "9 merged PRs out of 13 proposed (69% merge rate)"
- **Our assessment**: The 69% merge rate for CI failure investigation is the first
  production benchmark for agentic CI repair in the corpus. It is comparable to but
  slightly below the Changeset Generator's 78% merge rate (from
  `blog-gh-aw-operations-release-workflows.md` Claim 1). The difference may reflect
  task complexity: CI failure investigation requires diagnosing root causes across
  diverse failure types, whereas release versioning follows Conventional Commits rules
  with a small decision space. The 31% rejection rate is unexplained — it may reflect
  incorrect root-cause attribution, insufficient log context, or CI flakiness that
  resists deterministic fixes. For Ch03 (Safety and Verification): even a well-performing
  CI repair agent needs human-in-the-loop review; the 69% rate validates the automation,
  and the 31% gap validates keeping humans in the approval loop. For Ch04 (Multi-Agent
  Orchestration): the CI Doctor is an example of a reactive investigation agent —
  triggered by failures, producing targeted fix proposals, requiring human merge approval.

### Claim 2: CI Doctor performs deep investigation — analyzing logs, identifying patterns, searching for similar past issues, and suggesting fixes — rather than simply reporting that something broke

- **Evidence**: The post describes the CI Doctor's investigation process in terms of
  four distinct analytical steps: log analysis, pattern identification, historical issue
  search, and fix suggestion. The concrete fix examples (Go module download pre-flight
  checks; proxy 403 retry logic) demonstrate that the suggested fixes are real
  infrastructure changes, not boilerplate.
- **Confidence**: emerging (described by the workflow authors; the 69% merge rate
  corroborates that the suggestions are substantive enough for humans to accept)
- **Quote**: "doesn't just tell us something broke - it analyzes logs, identifies
  patterns, searches for similar past issues, and even suggests fixes"
- **Our assessment**: The four-step process (analyze logs → identify patterns → search
  history → suggest fix) is a concrete investigative pipeline for CI repair agents. The
  historical search step is particularly notable: by comparing current failures to past
  issues, the agent can recognize recurring flakiness patterns rather than treating every
  failure as novel. For Ch04 (Multi-Agent Orchestration): this is a production example
  of a multi-step agentic workflow where each step provides context to the next —
  log analysis informs pattern matching, which informs historical search, which informs
  fix suggestion. The pipeline nature means the agent's output quality depends on each
  upstream step succeeding.

### Claim 3: CI Doctor excels at the tedious investigation work that humans find draining — the value comes from consistent attention, not superhuman capability

- **Evidence**: The post frames CI Doctor's primary advantage as willingness to perform
  tedious tasks consistently — log analysis and historical issue search are tasks humans
  perform poorly due to fatigue and attention cost. The two concrete examples (proxy 403
  retry logic, Go module pre-flight check) are both infrastructure fixes that required
  reading CI logs and recognizing patterns, not deep architectural reasoning.
- **Confidence**: anecdotal (framing by the workflow authors; not measured against human
  investigator performance)
- **Quote**: "excels at the tedious investigation work that humans find draining"
- **Our assessment**: This is the most practically actionable framing in the post. The
  claim positions CI repair agents not as superior reasoners but as tireless pattern
  matchers. Humans find CI log analysis draining precisely because it requires sustained
  attention on low-signal, high-volume output; agents have no attention cost. This is
  consistent with `blog-ghaw-pelis-agent-factory-intro.md` Claim 7's observation that
  "specialization reveals possibilities" — the CI Doctor's value is clearest when a
  team's CI fails frequently enough that manual investigation creates a sustained burden.
  For Ch01 (Daily Workflows): frame CI investigation as a canonical "tedious but
  important" task category that agents handle well, alongside documentation maintenance
  and dependency updates.

### Claim 4: Schema Consistency Checker detects cross-concern drift between JSON schemas, Go structs, and documentation — generating 55 analysis discussions from live production runs

- **Evidence**: Production data: 55 analysis discussions created by the Schema Consistency
  Checker. Example: Discussion #7020 examining conditional logic consistency across the
  codebase. The workflow monitors three specific artifact types (JSON schemas, Go structs,
  documentation) for semantic alignment — detecting when one layer is updated without
  corresponding updates to the others.
- **Confidence**: anecdotal (self-reported production data; 55 discussions is an output
  count, not a count of bugs caught or prevented)
- **Quote**: "created 55 analysis discussions"
- **Our assessment**: The 55-discussion output volume is comparable to the Issue Arborist's
  77 discussion reports (from `blog-ghaw-issue-pr-mgmt.md` Claim 1), suggesting a similar
  cadence of output-per-run. The cross-concern drift pattern — JSON schemas, Go structs,
  and documentation drifting independently — is a real and common problem in typed language
  codebases that update frequently. The workflow's value depends on the codebase having
  enough inter-component consistency requirements that drift actually occurs. For a small
  codebase with few schemas, 55 discussions may represent a lot of false positives; for a
  large typed codebase, it may represent caught drift. The discussion count alone cannot
  distinguish signal from noise. For Ch04: Schema Consistency Checker is an example of a
  "catch-before-humans" audit agent — the analysis runs before any engineer has manually
  compared schemas, Go structs, and docs. If it runs frequently enough, humans never need
  to perform the comparison manually.

### Claim 5: Breaking Change Checker provides proactive backward-compatibility monitoring by creating alert issues before incompatible changes reach production

- **Evidence**: The Breaking Change Checker creates alert issues when backward-incompatible
  changes are detected. Example: Issue #14113 flagging CLI version updates before they
  could cause downstream breakage. The workflow is explicitly positioned as a pre-production
  gate — catching changes before they become incidents.
- **Confidence**: anecdotal (workflow described by its authors; no merge rate or false
  positive rate given)
- **Quote**: (no direct quote capturing the full mechanism; see paraphrase in Our assessment)
- **Our assessment**: The Breaking Change Checker addresses a different failure mode than
  CI Doctor: not "something already broke" but "something is about to break for users who
  depend on the current behavior." This is a proactive guardrail rather than a reactive
  investigator. The CLI version example (Issue #14113) suggests the workflow monitors
  changelogs or commit diffs for incompatible version bumps, though the specific detection
  mechanism is not described. For Ch03 (Safety and Verification): Breaking Change Checker
  is an example of safety-as-automation — moving backward-compatibility review from an ad
  hoc human responsibility to a systematic automated check. The value scales with how
  many downstream consumers depend on the interface being checked.

### Claim 6: The three fault-investigation workflows constitute a complementary cluster — first line of defense before users detect problems

- **Evidence**: The post presents all three workflows under the framing of "vigilant
  caretakers" that catch problems proactively. The three workflows cover distinct failure
  modes: (1) active CI failures (CI Doctor), (2) accumulated drift between layers (Schema
  Consistency Checker), and (3) breaking changes in flight (Breaking Change Checker).
  Together they form a pre-incident monitoring cluster.
- **Confidence**: anecdotal (framing by the workflow authors; the "first line of defense"
  positioning is editorial, not measured)
- **Quote**: "vigilant caretakers"
- **Our assessment**: The cluster framing is the most important architectural contribution
  of the post. Individual fault-detection agents each have a narrow scope; deploying three
  with complementary scopes creates defense-in-depth for different failure categories.
  CI Doctor covers active failures (something already broke). Schema Consistency Checker
  covers accumulated drift (something is slowly becoming inconsistent). Breaking Change
  Checker covers breaking changes in flight (something is about to break). A team deploying
  only one would miss the other two failure modes. For Ch04 (Multi-Agent Orchestration):
  this is a production example of agent specialization by failure-mode domain — not one
  "quality agent" but three distinct fault-detection specialists. The "vigilant caretakers"
  framing positions these as always-on background monitors, not reactive tools invoked by
  humans.

### Claim 7: The fault-investigation workflows are installable via `gh aw add-wizard` with version-pinned URLs — making the cluster immediately adoptable

- **Evidence**: Each of the three workflows can be added using `gh aw add-wizard` with
  a specific GitHub URL pointing to a versioned workflow specification file. The
  version-pinning (v0.45.5 per the operations/release post's pattern) ensures
  reproducibility at installation time.
- **Confidence**: settled (installation mechanism is consistent with all other posts in
  the "Meet the Workflows" series)
- **Quote**: (no workflow-specific URL quoted; see Concrete Artifacts for the pattern)
- **Our assessment**: The add-wizard installation model makes these three workflows
  immediately adoptable without rebuilding from scratch. The version pin ensures that
  a team installing the workflow gets the same specification the gh-aw team tested. For
  Ch05 (Team Adoption): the fault-investigation cluster is a ready-made first deployment
  for teams that already have frequent CI failures or schema drift — two problems that are
  universal enough that most teams can benefit immediately from at least CI Doctor.

## Concrete Artifacts

### Production Metrics (from the post)

```
Peli's Agent Factory — Fault Investigation Workflow Output (as of Jan 13, 2026):

CI Doctor:
  Output: 9 merged PRs out of 13 proposed (69% merge rate)
  Example fixes:
    - Adding Go module download pre-flight checks
    - Adding retry logic to prevent proxy 403 failures
  Purpose: Autonomous CI failure investigation (log analysis, pattern search,
           historical issue search, fix suggestion)

Schema Consistency Checker:
  Output: 55 analysis discussions created
  Example: Discussion #7020 — conditional logic consistency across the codebase
  Purpose: Cross-concern drift detection (JSON schemas ↔ Go structs ↔ documentation)

Breaking Change Checker:
  Output: Alert issues filed before production deployment
  Example: Issue #14113 — flagging CLI version updates
  Purpose: Proactive backward-compatibility monitoring
```

### Comparative Merge-Rate Benchmarks (from corpus)

```
Agentic workflow merge rates in Peli's Agent Factory:

Workflow                  | Task type          | Merge rate | PRs
--------------------------+--------------------+------------+-------
Changeset Generator       | Release versioning | 78% (22/28)| gh-aw
CI Doctor                 | CI repair          | 69% (9/13) | gh-aw

Interpretive note:
  Changeset Generator follows Conventional Commits rules (small decision space).
  CI Doctor investigates diverse failure types (larger decision space).
  Lower CI Doctor merge rate may reflect diagnosis uncertainty, not quality deficit.
```

### Installation Pattern (from series)

```bash
# Add fault-investigation workflows to your repository:
gh aw add-wizard https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/ci-doctor.md
gh aw add-wizard https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/schema-consistency-checker.md
gh aw add-wizard https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/breaking-change-checker.md

# After adding/editing workflow specifications:
gh aw compile
git push
```

Note: Exact URLs follow the series convention; the specific file paths above are
inferred from the workflow naming convention used across the series (e.g., changeset.md,
audit-workflows.md). The Assayer should verify exact URLs from the source page.

### Fault-Investigation Cluster Scope Map

```
Failure mode          | Workflow               | Trigger       | Output type
----------------------+------------------------+---------------+--------------
Active CI failure     | CI Doctor              | Event (CI fail)| Fix PR
Accumulated drift     | Schema Consistency     | Scheduled     | Analysis discussion
                      |   Checker              |               |
Breaking change       | Breaking Change        | Event (commit/ | Alert issue
  in flight           |   Checker              |   PR)         |

Together: covers pre-incident (drift, breaking changes) AND post-incident (CI failure).
"First line of defense before users detect problems."
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agent-factory-status.md` Claim 2 (engine assignment gradient — Claude for
    investigation/analysis): The Schema Consistency Checker is listed in the agent factory
    status catalog as a Claude workflow. CI Doctor is also described there as using Claude
    (see "CI Failure Doctor" in the catalog, which the status note lists under the claude
    engine). The investigation-intensive nature of fault detection aligns with the pattern
    that Claude handles tasks requiring multi-step reasoning over complex states.
  - `blog-ghaw-agent-observability.md` Claim 5 (autonomous remediation loop — observe →
    diagnose → flag → fix): CI Doctor extends the observability-to-remediation pipeline
    from the observability note into a fully automatic fix-proposal workflow. Audit
    Workflows raises issues (4/9 convert to downstream PRs); CI Doctor goes further by
    *directly opening fix PRs* (9/13 merged). Both patterns close the loop between
    detection and remediation; CI Doctor is more direct.
  - `blog-ghaw-pelis-agent-factory-intro.md` Claim 3 (production task taxonomy includes
    "Diagnosing CI failures"): CI Doctor is the concrete production implementation of the
    "Diagnosing CI failures" task category named in the intro. Claim 7 ("Specialization
    reveals possibilities") is also validated: three distinct fault-investigation workflows
    serve three distinct failure-mode domains that a single "quality agent" would bundle.
  - `blog-ghaw-issue-pr-mgmt.md` Claim 1 (Issue Arborist — 77 discussion reports): The
    Schema Consistency Checker's 55 analysis discussions follow the same output pattern
    as Issue Arborist's 77 discussion reports. Both workflows produce analysis discussions
    rather than direct PRs, showing that "read-only analyst" workflows generating
    structured discussion threads are a consistent output format in the factory.

- **Extends**:
  - `blog-ghaw-agent-observability.md` (three-tier observability: performance, cost,
    meta-audit): The observability layer described in that note monitors agent performance
    and cost. The fault-investigation cluster described here monitors codebase health —
    CI, schema drift, breaking changes. Together they form two distinct monitoring planes:
    an *agent observatory* (monitoring the factory itself) and a *codebase observatory*
    (monitoring the artifact being produced). This two-observatory architecture is not
    named in either post alone; it emerges from combining the two.
  - `docs-ghaw-agent-factory-status.md` Claim 5 (factory self-monitoring layer): That
    note identifies Schema Consistency Checker as part of the platform self-monitoring
    cluster. This note provides the first production metrics and concrete examples for
    that workflow (55 discussions, Discussion #7020), upgrading the factory status
    catalog's thin reference.
  - `blog-gh-aw-operations-release-workflows.md` Claim 1 (Changeset Generator 78% merge
    rate as first production benchmark): CI Doctor's 69% merge rate is now the second
    production merge-rate benchmark in the corpus, enabling a comparison between
    release-versioning tasks (78%) and CI-repair tasks (69%).

- **Contradicts**: None found. No existing note makes claims about CI repair merge rates
  or fault-investigation patterns that conflict with this source. The difference between
  CI Doctor's 69% and Changeset Generator's 78% is not a contradiction — they are
  different task types with different decision spaces.

- **Novel**:
  - **First production benchmark for agentic CI failure repair** (Claim 1): The 69%
    merge rate (9/13 PRs) for CI Doctor is the first corpus entry for autonomous CI
    investigation merge-rate performance. Prior notes document CI failure as a task
    category (factory intro, factory status) without production metrics.
  - **Fault-investigation cluster pattern** (Claim 6): The three-workflow cluster covering
    complementary failure modes (active CI failures, schema drift, breaking changes) is a
    novel architectural pattern not described in any existing source note. Previous notes
    document individual workflows; this post frames three specialized workflows as a
    deliberately complementary cluster.
  - **Schema drift as a detectable multi-layer inconsistency pattern** (Claim 4):
    No existing note describes detecting drift specifically between JSON schemas, Go
    structs, and documentation as a distinct failure mode. The Schema Consistency Checker
    is the first production implementation of multi-layer consistency monitoring in the
    corpus.
  - **Breaking Change Checker as proactive backward-compatibility gate** (Claim 5): The
    pattern of a dedicated agent monitoring for backward-incompatible changes before they
    reach production is not described in any existing source note.
  - **CI investigation as "tedious but valuable" framing** (Claim 3): The explicit framing
    that CI investigation is work "humans find draining" positions this class of agent by
    its ergonomic fit rather than by capability — a framing not previously captured in the
    corpus.

## Guide Impact

- **Chapter 01: Daily Workflows** — Add CI investigation to the canonical "tedious but
  important" task category that agents handle well (Claim 3). Frame alongside documentation
  maintenance and dependency updates: these are tasks agents can do consistently at no
  attention cost, whereas humans skip them when under deadline pressure. The 69% merge rate
  is the evidence that CI investigation is viable as an always-on workflow, not just a
  one-off experiment. Reference CI Doctor as the production implementation.

- **Chapter 03: Safety and Verification** — The fault-investigation cluster (Claim 6)
  is a production reference for defense-in-depth monitoring: three agents covering three
  failure-mode categories. For Ch03's treatment of safety as a practice, the cluster
  demonstrates that "monitoring for failures" can be systematized as a dedicated workflow
  layer, not just a human oncall responsibility. The Breaking Change Checker (Claim 5) is
  specifically relevant as a pre-production backward-compatibility gate. The 69% merge
  rate (Claim 1) is evidence for why humans must remain in the approval loop even for
  well-performing repair agents.

- **Chapter 04: Multi-Agent Orchestration** — The cluster framing (Claim 6) updates the
  multi-agent architecture picture: a mature factory deploys multiple specialized
  fault-detection agents covering complementary failure modes, not one generic monitor.
  The CI Doctor pipeline (Claim 2 — analyze logs → identify patterns → search history →
  suggest fix) is a concrete multi-step investigation workflow to reference when
  discussing single-agent pipelines. Cross-reference with `blog-ghaw-agent-observability.md`
  Claim 5 for the broader context: CI Doctor's fix-PR approach extends the autonomous
  remediation loop beyond meta-agents to specialized repair agents.

- **Chapter 05: Team Adoption** — The fault-investigation cluster (three workflows, two
  of which have production metrics) is a ready-made starting point for teams whose primary
  pain point is CI flakiness or schema drift. The `gh aw add-wizard` installation model
  (Claim 7) means adoption is a matter of running three commands, not building from
  scratch. For teams asking "where do we start?", CI Doctor is a compelling first
  deployment: CI failures are universal, the task is well-defined (repair this broken
  run), and the 69% merge rate demonstrates production viability.

## Extraction Notes

1. **Page URL vs. series title mismatch**: The page URL slug is "quality-hygiene" but
   the series index (from `blog-ghaw-pelis-agent-factory-intro.md`) lists the
   corresponding entry as "Fault Investigation Workflows." The note uses the series
   title. Both refer to the same blog post.

2. **WebFetch model processing**: This post was fetched via WebFetch, which processes
   the page through a model before returning content. Verbatim accuracy cannot be
   guaranteed for descriptive passages. The metric-specific quotes ("9 merged PRs out
   of 13 proposed (69% merge rate)" and "55 analysis discussions") are highly specific
   numeric statements consistent with the format used for similar metrics in companion
   posts (e.g., "22 merged PRs out of 28 proposed" in the operations/release note),
   and are considered high-confidence. Descriptive quotes (CI Doctor capabilities, "vigilant
   caretakers", "excels at the tedious investigation work that humans find draining")
   appeared consistently across multiple fetch passes and are treated as likely verbatim,
   but the Assayer should spot-check against the source URL.

3. **Exact `gh aw add-wizard` URLs not confirmed**: The installation URLs in the Concrete
   Artifacts section follow the pattern from the operations/release note (v0.45.5 pin,
   GitHub blob path). The specific file paths (ci-doctor.md, schema-consistency-checker.md,
   breaking-change-checker.md) are inferred from workflow naming conventions and should be
   verified against the source page. The installation *mechanism* is confirmed; the exact
   URLs are approximations.

4. **Series position**: Based on the series index from `blog-ghaw-pelis-agent-factory-intro.md`,
   Fault Investigation is the 8th of the 19-part series (6 core articles + 2nd specialized
   category). The adjacent posts are Issue & PR Management (part 7, issue #146) and Metrics
   & Analytics (part 9, issue #165).

5. **Engine assignments not in this post**: The blog post does not specify which AI engines
   run CI Doctor, Schema Consistency Checker, or Breaking Change Checker. Engine assignments
   come from `docs-ghaw-agent-factory-status.md` (the live factory catalog), which lists
   Schema Consistency Checker and CI Failure Doctor under Claude. This note does not assert
   engine assignments that were not stated in the source.

6. **No contradictions found**: Reviewed all existing source notes. The CI Doctor's 69%
   merge rate is lower than the Changeset Generator's 78% (different task types — not a
   contradiction). Schema Consistency Checker is mentioned briefly in the factory status
   catalog; this note provides its first production metrics. No existing note claims
   conflict with the patterns described here.
