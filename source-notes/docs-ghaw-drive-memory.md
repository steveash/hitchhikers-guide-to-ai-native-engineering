---
source_url: https://github.github.com/gh-aw/experimental/drive-memory
source_type: docs
title: "GitHub Agentic Workflows: Drive Memory (Experimental)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: emerging
issue: "#3105"
---

# GitHub Agentic Workflows: Drive Memory (Experimental)

> Reference documentation for `drive-memory`, an experimental, feature-gated gh-aw
> integration that mounts a GitHub Drives preview volume into the agent — a third
> memory storage backend alongside Cache Memory and Repo Memory, with its own
> mount-path convention, permission grant, threat-detection-gated publish job,
> single-active-writer concurrency model, and size-provisioning syntax.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `experimental/` section —
  the same tier as `experimental/correction-ops` (previous page) and
  `experimental/enclaves` (next page). Experimental pages document preview
  features gated behind explicit GitHub enrollment, distinct from the
  `reference/` section's generally-available tools like `cache-memory` and
  `repo-memory`.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind the `gh aw` CLI and its `reference/`, `patterns/`, and
  `guides/` documentation used throughout this corpus. The page is explicit
  that it "records behavior for enrolled preview repositories" rather than
  offering general guidance, so claims here describe preview-service behavior
  that may change before general availability.
- **Scope**: The entire page is short — one intro paragraph, a danger callout,
  and two sections ("Preview behavior", "Drive size") plus a "Limitations"
  list. It covers: the mount path convention, the permission grant, the
  checkout/commit lifecycle, threat-detection integration for publishing,
  writer-lease contention, the `disk-size` configuration parameter, and five
  operational limitations. Does NOT cover: how to request preview enrollment,
  the GitHub Drives service itself (linked externally to
  `https://github.com/actions/gh-drives-preview`, not followed — see
  Extraction Notes), pricing/quota beyond `disk-size`, or a worked end-to-end
  workflow example (the page has no YAML example beyond the `disk-size`
  snippet).

## Extracted Claims

### Claim 1: Drive memory is an experimental, feature-gated integration that must not be configured unless GitHub has explicitly enrolled the repository in the private preview

- **Evidence**: Opening sentence of the page, reinforced by a "Danger" callout
  immediately below it.
- **Confidence**: settled (first-party documentation; the enrollment
  requirement is stated as a directive, not a suggestion)
- **Quote**: "Drive memory is an experimental, feature-gated integration
  backed by the GitHub Drives preview. Do not configure it unless GitHub has
  explicitly enrolled the repository in the private preview."
- **Our assessment**: This is a stronger gating statement than typical
  "experimental, subject to change" disclaimers elsewhere in gh-aw docs — the
  page tells readers not to configure the feature at all without explicit
  enrollment, implying the compiler or runtime may behave unpredictably (or
  simply fail) for non-enrolled repositories. The companion Danger callout —
  "This reference records behavior for enrolled preview repositories and is
  not a recommendation for general use" — confirms the page is a behavioral
  record, not a how-to guide. For the guide: any mention of Drive Memory
  should carry an explicit "private preview, do not use without enrollment"
  caveat, distinct from the more permissive framing used for GA tools like
  `cache-memory` and `repo-memory`.

### Claim 2: For enrolled repositories, the compiler mounts configured drives into the agent at `/tmp/gh-aw/drive-memory/`, or `/tmp/gh-aw/drive-memory-{id}/` for named entries

- **Evidence**: First sentence of the "Preview behavior" section.
- **Confidence**: settled (first-party documentation; explicit path syntax)
- **Quote**: "For enrolled preview repositories, the compiler mounts
  configured drives into the agent at `/tmp/gh-aw/drive-memory/` (or
  `/tmp/gh-aw/drive-memory-{id}/` for named entries)."
- **Our assessment**: The path convention mirrors the `{tool}-{id}/` pattern
  already established for `cache-memory` (`/tmp/gh-aw/cache-memory-{id}/`, per
  `docs-ghaw-cache-memory-reference.md` Claim 3) and `repo-memory`
  (`/tmp/gh-aw/repo-memory-{id}/`, per `docs-ghaw-repo-memory-reference.md`
  Claim 7). This consistency means an agent harness that already knows the
  `/tmp/gh-aw/{tool}[-{id}]/` mount convention needs no new mental model to
  read/write drive-memory content — only a new tool name.

### Claim 3: The compiler grants the generated job `contents: read`, `id-token: write`, and the required `drives` permission

- **Evidence**: Second sentence of the "Preview behavior" section, listing the
  three permission scopes verbatim.
- **Confidence**: settled (first-party documentation; explicit permission
  list)
- **Quote**: "It grants the generated job `contents: read`, `id-token:
  write`, and the required `drives` permission."
- **Our assessment**: The `drives` permission scope does not appear in
  `docs-ghaw-permissions-reference.md`'s ten standard read scopes or its
  GitHub App-Only taxonomy — it is new to the corpus, consistent with this
  being a preview-only capability layered on top of the standard permission
  model. The `id-token: write` grant is notable because
  `docs-ghaw-permissions-reference.md` Claims 7–8 document that permission as
  an anomaly whose only prior documented use case in the corpus was OIDC
  authentication to cloud providers (AWS/GCP/Azure) and that it "does not
  require safe-outputs" because it grants no repository-modification ability.
  Drive Memory's use of `id-token: write` to authenticate to the GitHub
  Drives preview service is architecturally the same pattern (external
  service auth, no repo-content modification) applied to a second external
  service. For Ch02/Ch03: document `drives` as a new permission scope
  specific to the preview, and note this as a second confirmed use case for
  `id-token: write` beyond cloud-provider OIDC.

### Claim 4: The compiler checks out each drive before the agent runs and commits validated changes afterward

- **Evidence**: First sentence of the paragraph following the permission
  grant, in "Preview behavior".
- **Confidence**: settled (first-party documentation)
- **Quote**: "The compiler checks out each drive before the agent and commits
  validated changes afterward."
- **Our assessment**: This checkout-before/commit-after lifecycle is
  structurally similar to Repo Memory's model (branch checked out, changes
  auto-committed after validation — `docs-ghaw-repo-memory-reference.md`
  Claim 2), but Drive Memory's backing store is the GitHub Drives preview
  service rather than a Git branch, so "commits" here likely refers to
  persisting changes back to the drive rather than a Git commit object. The
  page does not clarify whether "validated" refers to the same
  file-glob/max-file-size-style validation gates documented for repo-memory,
  or to something specific to the Drives service. This is a gap the Assayer
  or a future extraction pass should flag if a more detailed Drives reference
  page becomes available.

### Claim 5: With threat detection enabled, drive contents are staged as an artifact and published by a separate `update_drive_memory` job only after detection succeeds and the drive is confirmed unchanged since checkout

- **Evidence**: Second sentence of the same paragraph in "Preview behavior".
- **Confidence**: settled (first-party documentation; the job name and the
  two publish conditions are stated explicitly)
- **Quote**: "With threat detection enabled, it stages drive contents as an
  artifact; a separate `update_drive_memory` job publishes it only after
  detection succeeds and verifies the drive has not changed since checkout."
- **Our assessment**: This is a concrete, named implementation of the
  threat-detection-gated persistence pattern that `docs-ghaw-threat-detection.md`
  Claim 1 describes architecturally (threat detection as a separate job
  between the agentic job and safe-output/persistence jobs) and Claim 12
  documents as fail-secure (detection failures block persistence rather than
  degrading to allow it). The `update_drive_memory` job adds a second gate
  beyond "detection succeeded": it also re-verifies the drive has not
  changed since checkout, which guards against the same class of
  time-of-check/time-of-use race that a naive artifact-then-publish design
  would be vulnerable to if another run wrote the drive in between. This is
  the most concrete corroboration in the corpus of the threat-detection gate
  being applied specifically to a memory-persistence write path (Repo
  Memory's reference page documents an auto-commit/push gate tied to threat
  detection in general terms — `docs-ghaw-repo-memory-reference.md` Claim
  2 — but does not name a dedicated publish job the way this page does for
  drives).

### Claim 6: Drive names are repository-wide and branch-aware, and GitHub Drives allows only one active writer per drive, so overlapping runs writing the same drive can contend for the writer lease

- **Evidence**: Third paragraph of "Preview behavior".
- **Confidence**: settled for the stated behavior (first-party documentation);
  emerging for its operational implications, since the page does not describe
  what happens to a run that loses the writer-lease race (retry? fail? block?)
- **Quote**: "Drive names are repository-wide and branch-aware according to
  the preview service. GitHub Drives allows one active writer for a drive, so
  overlapping runs that write the same drive can contend for the writer
  lease."
- **Our assessment**: This is a materially different concurrency model from
  Repo Memory's "your changes win" replay-based conflict resolution
  (`docs-ghaw-repo-memory-reference.md` Claim 3), where the GraphQL
  `createCommitOnBranch` mutation merges concurrent writers by replaying the
  diff on the latest remote state — no writer is blocked, both writes
  eventually land. Drive Memory instead has a single-active-writer lease:
  overlapping runs contend for exclusive write access rather than having
  their changes merged. This is not a contradiction between the two source
  notes (they document different storage backends with different concurrency
  primitives by design — a GitHub Drives volume is not a Git branch), but it
  is an important distinction for harness engineers choosing between the two:
  teams that need multiple concurrent writers merged automatically should
  prefer Repo Memory; teams using Drive Memory need to design for lease
  contention (e.g., serializing writers via workflow concurrency groups,
  documented separately in `docs-ghaw-concurrency-reference.md`) rather than
  relying on automatic merge.

### Claim 7: `disk-size` sets the size used only when creating a new drive (ignored for an existing drive), must be a number with an optional K/M/G/T suffix, rejects compound suffixes like `1GB` at compile time, and normalizes lowercase suffixes to uppercase

- **Evidence**: "Drive size" section, followed by a YAML configuration
  example showing `disk-size: 100M`.
- **Confidence**: settled (first-party documentation; the format rules are
  stated as explicit compile-time behavior)
- **Quote**: "`disk-size` sets the size used when creating a new drive; it is
  ignored for an existing drive. The value must be a number with an optional
  `K`, `M`, `G`, or `T` suffix (for example `100M`). Suffixes such as `1GB`
  are rejected at compile time. Leading/trailing whitespace is trimmed and
  lowercase suffixes (for example `100m`) are normalized to upper case
  automatically."
- **Our assessment**: The "ignored for an existing drive" behavior is a
  practical footgun: a team that changes `disk-size` in workflow frontmatter
  expecting to resize an already-provisioned drive will see no effect,
  because the parameter only applies at creation time. This differs from
  Cache Memory's `retention-days` (which does affect existing caches going
  forward, per `docs-ghaw-cache-memory-reference.md` Claim 2) and from Repo
  Memory's `max-file-size`/`max-patch-size` (enforced on every write, per
  `docs-ghaw-repo-memory-reference.md` Claim 6) — Drive Memory's `disk-size`
  is create-time-only. For Ch02: document this as a configuration gotcha —
  resizing an existing drive is not achieved by editing `disk-size` in the
  workflow.

### Claim 8: Drive mounts are supported only on the GitHub-hosted `ubuntu-latest` preview runner, require preview enrollment, and are not supported inside job containers

- **Evidence**: First three bullets of the "Limitations" section.
- **Confidence**: settled (first-party documentation; stated as a bulleted
  limitations list)
- **Quote**: "GitHub-hosted `ubuntu-latest` is the supported preview runner."
  / "Repositories must be enrolled in the GitHub Drives preview." / "Drive
  mounts are not supported inside job containers."
- **Our assessment**: These three constraints rule out common gh-aw
  deployment variants for Drive Memory specifically: self-hosted runners
  (`docs-ghaw-agent-runtimes-reference.md` territory) and containerized jobs
  are both unsupported, leaving only GitHub-hosted `ubuntu-latest` as a
  viable target during the preview period. Teams already running gh-aw on
  ARC/self-hosted runners or in containers (per
  `docs-ghaw-arc-dind-copilot-agent.md`) cannot adopt Drive Memory without
  changing runner configuration, even once enrolled. For Ch02: flag Drive
  Memory as incompatible with containerized or self-hosted gh-aw deployments
  during the preview.

### Claim 9: The upstream Drive-mounting actions have no versioned release, so gh-aw pins the preview `main` commit, and secrets must never be stored in drive memory

- **Evidence**: Fourth and fifth bullets of the "Limitations" section.
- **Confidence**: settled for the stated facts (first-party documentation);
  emerging for the supply-chain risk implication, which is our assessment
  rather than a claim the page itself makes
- **Quote**: "The upstream actions currently have no versioned release, so
  gh-aw pins the preview `main` commit." / "Do not store secrets in drive
  memory."
- **Our assessment**: Pinning to an upstream `main` commit (rather than a
  tagged release or commit SHA with a changelog) is a materially different
  supply-chain posture than gh-aw's typical guidance elsewhere in the corpus,
  which favors pinned, versioned dependencies. The page doesn't say whether
  "pins the preview `main` commit" means a fixed SHA snapshot (safer) or a
  floating `main` reference (unpinned in practice, higher risk) — this
  ambiguity should be verified against the live source or the linked
  `gh-drives-preview` repository before the guide makes a strong claim either
  way. The "no secrets" rule matches the same prohibition documented for
  Cache Memory and Repo Memory (`docs-ghaw-memory-ops.md` Claim 11,
  `docs-ghaw-repo-memory-reference.md` Claim 11), but unlike those two pages,
  this page does not explain Drive Memory's access-control boundary (it
  doesn't state whether drive contents are "visible to anyone with repository
  access" the way cache-memory and repo-memory explicitly are). That gap is
  worth flagging for the Smith rather than assuming parity — see Extraction
  Notes.

## Concrete Artifacts

### Minimal `disk-size` Configuration (from `experimental/drive-memory` — "Drive size" section)

```yaml
tools:
  drive-memory:
    drive-name: my-drive
    disk-size: 100M
```

### Permission Grant (from `experimental/drive-memory` — "Preview behavior" section)

```
contents: read
id-token: write
drives: <required, exact scope value not further specified on this page>
```

### Threat-Detection-Gated Publish Flow (from `experimental/drive-memory` — "Preview behavior" section)

```
1. Compiler checks out drive before agent runs
2. Agent modifies drive contents
3. Compiler stages drive contents as an artifact (only when threat detection is enabled)
4. update_drive_memory job runs threat detection
5. On success AND drive-unchanged-since-checkout verification: publish
6. On failure of either check: publish is blocked
```

### Limitations (from `experimental/drive-memory` — "Limitations" section, verbatim list)

```
- GitHub-hosted ubuntu-latest is the supported preview runner.
- Repositories must be enrolled in the GitHub Drives preview.
- Drive mounts are not supported inside job containers.
- The upstream actions currently have no versioned release, so gh-aw pins
  the preview main commit.
- Do not store secrets in drive memory.
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-threat-detection.md` Claim 1 (threat detection runs as a
    dedicated job between the agentic job and downstream jobs) and Claim 12
    (fail-secure: detection failures stop the pipeline rather than degrading
    to allow it): the `update_drive_memory` job (Claim 5 here) is a concrete,
    named instance of exactly this pattern applied to a memory-persistence
    write path, with an additional drive-unchanged verification layered on
    top.
  - `docs-ghaw-permissions-reference.md` Claims 7–8 (`id-token: write` grants
    no repository-modification ability and does not require safe-outputs
    routing, documented use case: OIDC to cloud providers): Claim 3 here
    provides a second documented use case for `id-token: write` — GitHub
    Drives preview authentication — consistent with the "external service
    auth, no repo write" characterization in that note.
  - `docs-ghaw-cache-memory-reference.md` Claim 3 and
    `docs-ghaw-repo-memory-reference.md` Claim 7 (`/tmp/gh-aw/{tool}-{id}/`
    mount path convention for named multi-instance configurations): Claim 2
    here shows Drive Memory follows the identical `{tool}[-{id}]/` mount
    convention.

- **Contradicts**: None identified. The single-active-writer lease model
  (Claim 6) differs from Repo Memory's replay-based "your changes win" merge
  semantics (`docs-ghaw-repo-memory-reference.md` Claim 3), but this is a
  difference in concurrency primitives between two distinct storage backends
  (a GitHub Drives volume vs. a Git branch), not two sources disagreeing
  about the same mechanism — no contradiction issue filed per the MINER.md
  §4a "conditioning variable, not a contradiction" guidance. Similarly, this
  page's silence on Drive Memory's access-control/visibility boundary is a
  documentation gap relative to Cache Memory and Repo Memory (both of which
  explicitly state memory is "visible to anyone with repository access"), not
  a conflicting claim — see Extraction Notes.

- **Extends**:
  - `docs-ghaw-memory-ops.md` (Cache Memory / Repo Memory two-type
    architecture) and `docs-ghaw-repo-memory-reference.md` Concrete Artifacts
    → "Repo Memory vs. Cache Memory Comparison" table: Drive Memory is a
    third storage backend not covered by either existing comparison. Unlike
    Cache Memory (GitHub Actions cache, ephemeral, fast) or Repo Memory (Git
    branch, unlimited retention, GraphQL-mediated merge), Drive Memory is
    backed by an external preview service (GitHub Drives) with
    size-provisioned storage (`disk-size`) and single-writer-lease
    concurrency — none of which fits the existing two-column comparison
    model. A future Smith pass should consider whether a three-way
    comparison table (Cache Memory / Repo Memory / Drive Memory) belongs in
    the guide, with Drive Memory clearly marked preview-only.
  - `docs-ghaw-repo-memory-reference.md` Claim 2 (auto-commit/push gated on
    threat detection passing): Claim 5 here extends that general gating
    behavior with a named, more detailed implementation (`update_drive_memory`
    job, artifact staging, unchanged-since-checkout verification) for a
    different storage backend.

- **Novel**:
  - **GitHub Drives as a third gh-aw memory backend** (Claims 1–2, 4): No
    existing corpus source documents any memory storage type beyond Cache
    Memory and Repo Memory. This is the first.
  - **The `drives` permission scope** (Claim 3): Does not appear among the
    ten standard read scopes or the GitHub App-Only taxonomy in
    `docs-ghaw-permissions-reference.md`. New to the corpus.
  - **`update_drive_memory` as a named threat-detection-gated publish job**
    (Claim 5): No prior source names a dedicated job for threat-detection-gated
    memory publishing, or documents a drive-unchanged-since-checkout
    verification step.
  - **Single-active-writer lease concurrency model** (Claim 6): No prior
    memory-related source documents a lease-based (contend-and-block) write
    model, as opposed to Repo Memory's merge-based model.
  - **`disk-size` create-time-only provisioning with format validation**
    (Claim 7): New parameter, new configuration gotcha (ignored on existing
    drives) not seen in Cache Memory or Repo Memory's parameter surfaces.
  - **Preview-specific limitations** (Claims 8–9): The `ubuntu-latest`-only
    runner constraint, container-mount unsupported status, and unversioned
    upstream-`main`-commit pinning are all new operational constraints not
    documented for any other gh-aw memory tool.

## Guide Impact

- **Chapter 03 (Long-Running Sessions & State)**:
  - Add Drive Memory as a third, explicitly preview-gated storage option
    alongside Cache Memory and Repo Memory (Claims 1–2), with a hard caveat
    that it requires GitHub's explicit private-preview enrollment and "is not
    a recommendation for general use" (Claim 1's Danger-callout quote).
  - Document the single-active-writer lease model (Claim 6) as the key
    architectural difference from Repo Memory's merge-based concurrency —
    teams needing automatic multi-writer merge should use Repo Memory, not
    Drive Memory, during the preview.
  - Flag the `disk-size` create-time-only behavior (Claim 7) as a
    configuration gotcha worth calling out if the guide ever includes a
    Drive Memory configuration walkthrough.

- **Chapter 02 (Harness Engineering)**:
  - Add the `/tmp/gh-aw/drive-memory[-{id}]/` mount convention (Claim 2) to
    any existing summary of gh-aw's `/tmp/gh-aw/{tool}/` path conventions, so
    it's consistent with the Cache Memory and Repo Memory path documentation
    already covered.
  - Note the `drives` permission scope and second `id-token: write` use case
    (Claim 3) if the guide maintains a permissions-scope reference table
    sourced from `docs-ghaw-permissions-reference.md`.
  - List the preview-only runner/container limitations (Claim 8) alongside
    other gh-aw feature-compatibility caveats for self-hosted/ARC/containerized
    deployments.

- **Chapter 03 (Safety and Verification)**:
  - Add the `update_drive_memory` threat-detection-gated publish job (Claim 5)
    as a concrete example when documenting how threat detection integrates
    with memory-persistence write paths, alongside Repo Memory's more general
    threat-detection gate (`docs-ghaw-repo-memory-reference.md` Claim 2).
  - Flag the unresolved question of Drive Memory's access-control boundary
    (Claim 9's assessment) — do not assume parity with Cache/Repo Memory's
    "visible to anyone with repository access" model without verification
    against the live source or GitHub Drives preview documentation.

## Extraction Notes

1. **Fetched via raw HTML, not `WebFetch`'s AI-summarization pass**: This
   page is a small, server-rendered Astro/Starlight page (the full article
   content is present in the initial HTML response, not injected by
   client-side JS). All quotes in this note were extracted by fetching the
   raw HTML directly (`curl`) and locating the exact text inside the
   `sl-markdown-content` container, then verified a second time against the
   raw HTML for each quoted passage individually — not processed through an
   intermediate AI summarization step. This differs from the extraction
   method noted in several other `docs-ghaw-*` notes in this corpus (which
   flag `WebFetch`'s AI-summarization as a source of quote uncertainty); this
   note's quotes should carry higher confidence for verbatim accuracy.

2. **Whole page read; no sub-pages followed**: The page is short (one intro
   paragraph, one danger callout, two H2 sections, one limitations list) and
   is entirely self-contained. Its only content-relevant outbound link is to
   `https://github.com/actions/gh-drives-preview` (the underlying GitHub
   Drives preview service repository, external to the gh-aw docs site) — not
   followed, since it is a separate product's repository rather than a gh-aw
   documentation sub-page, and following it would exceed the scope of this
   docs-site source note. The prev/next navigation links
   (`experimental/correction-ops`, `experimental/enclaves`) are unrelated
   experimental features, not sub-pages of this topic.

3. **No publication date**: Like other gh-aw documentation pages in this
   corpus, this page carries no explicit publication date. `date_published`
   is left null. Content reflects gh-aw platform state as of the extraction
   date (2026-08-30).

4. **`confidence_overall` set to `emerging`, not `settled`**: While the
   individual factual claims (mount path, permission grant, `disk-size`
   format rules, limitations list) are extracted verbatim and graded
   `settled`, the overall grade is `emerging` because: (a) this is explicitly
   a private-preview feature the source itself says is "not a recommendation
   for general use"; (b) several operational implications are our inference
   rather than stated fact (writer-lease-loss behavior, whether "pins the
   preview main commit" means a fixed SHA or a floating reference, and
   whether Drive Memory's access-control boundary matches Cache/Repo Memory);
   (c) the feature could change materially or be withdrawn before GA, as is
   typical for private previews.

5. **No contradictions filed**: Reviewed `docs-ghaw-memory-ops.md`,
   `docs-ghaw-cache-memory-reference.md`, `docs-ghaw-repo-memory-reference.md`,
   `docs-ghaw-threat-detection.md`, and `docs-ghaw-permissions-reference.md`.
   No claim in this source materially opposes a claim in those notes at the
   MINER.md §4a filing threshold — the concurrency-model difference from Repo
   Memory (Claim 6) is a difference between two distinct storage backends
   with different underlying primitives, not a factual disagreement about the
   same mechanism. No contradiction issue required.
