---
source_url: https://www.thoughtworks.com/insights/blog/data-engineering/enabling-evolutionary-database-branching-with-lakebase-part-2
source_type: blog-post
title: "Enabling Evolutionary Database Development: Database Branching with Lakebase (Part Two)"
author: Pramod Sadalage and Kevin Hartman (Thoughtworks)
date_published: 2026-06-12
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1611"
---

# Enabling Evolutionary Database Development: Database Branching with Lakebase (Part Two)

> Thoughtworks revisits Martin Fowler's 2003 "Evolutionary Database Design" seven
> practices twenty years later, arguing that Databricks Lakebase's copy-on-write
> Postgres branching (O(1), ~1-second, zero-copy-at-creation branches of
> production-scale databases) removes the cost/time constraint that made
> per-developer database instances and per-PR CI isolation aspirational, and
> documents a concrete GitHub Actions-based CI workflow (branch-per-PR, schema
> diff posted on the PR, branch teardown on merge) plus four newly-viable
> practices (destructive testing as default, A/B schema prototyping, catalog-wide
> governance inheritance, and agent-as-branch-practitioner).

## Source Context

- **Type**: blog-post (Part 2 of a 3-part series; cross-posted to
  databricks.com per the source's closing note: "A version of this blog post
  was published on databricks.com"). Auto-discovered via the trusted
  `thoughtworks` RSS feed.
- **Author credibility**: Pramod Sadalage is a Thoughtworks veteran and
  co-author (with Scott Ambler) of the 2006 book *Refactoring Databases*,
  the practitioner catalog this series explicitly builds on
  (databaserefactoring.com). Kevin Hartman is credited alongside him. This
  is first-party continuity from the original practice-catalog author,
  writing about a specific vendor product (Databricks Lakebase); the piece
  is promotional in the sense that it centers one vendor's proprietary
  branching feature, but the practices described are methodology-level
  (applicable to any copy-on-write branchable database), not API-tutorial
  level.
- **Scope**: Covers the 2003 Evolutionary Database Design seven practices,
  which of the seven were previously aspirational and why, what Lakebase's
  copy-on-write branching architecture changes technically, a worked
  GitHub Actions CI workflow (per-PR branch creation, schema-diff-on-PR,
  branch cleanup on merge), and a practice-by-practice "new playbook" (9 of
  11 numbered practices get full treatment in this part; practices #10
  governance-inheritance and #11 agent-as-practitioner are named but
  explicitly deferred to Part 3, "we'll discuss this in more detail in part
  three"). Does NOT cover: Part 3's team-scale governance/DBA-policy
  content, the Lakebase SCM Extension for VS Code/Cursor (mentioned only as
  a pointer to a separate "Companion" piece), or any agent-specific
  workflow details beyond naming practice #11.

## Extracted Claims

### Claim 1: Lakebase's copy-on-write branching is a metadata-only operation — a branch shares all pages with its parent until it writes, so branch creation is O(1) regardless of the parent database's size

- **Evidence**: Architectural description of the mechanism (shared storage
  layer, divergence marker, page-level copy-on-write), stated as the causal
  explanation for why per-developer/per-PR database instances became cheap.
- **Confidence**: emerging (vendor-described architecture in a partner blog
  post; no independent benchmark or third-party verification in this
  source)
- **Quote**: "Branching is a metadata operation, no data copy required, completing in roughly one second regardless of parent size."
- **Our assessment**: This is the load-bearing technical claim the rest of
  the article's methodology argument depends on. It's architecturally
  plausible (consistent with copy-on-write / Neon-style storage-compute
  separation described in `blog-latentspace-databricks-agent-clouds.md`
  Claim 5, which independently describes Lakebase's storage layer as reused
  Neon architecture) but this specific source gives no benchmark numbers,
  only the qualitative "roughly one second" figure repeated later for a
  "1TB database in the same one second as a 1MB database" (Practice #4
  mechanics section). Treat the timing claim as vendor-stated, not
  independently measured.

### Claim 2: The removed constraint specifically unblocks Practice #4 ("everybody gets their own database instance") from the original 2003 essay, which the authors say had stayed aspirational for 20+ years due to licensing, infrastructure, and DBA provisioning cost

- **Evidence**: Direct statement contrasting the 2003 practice list against a
  stated 2026 "Limitations in their application" section that names the
  specific blocker for each of five practices.
- **Confidence**: settled (as a historical/methodological claim about *why*
  a well-known named practice failed to spread — this tracks with widely
  reported industry experience of shared dev/test database contention, not
  a novel or contestable technical claim)
- **Quote**: "Licensing costs, infrastructure costs, DBA time. Aspirational on most teams. Most teams fell back to shared development databases and accepted the contention."
- **Our assessment**: Credible as a description of pre-branching industry
  norms. The "now solved" half of the claim (Claim 1) is vendor-specific;
  the "here's what was broken and why" half is a reasonable, unremarkable
  description of a well-known pain point independent of any vendor.

### Claim 3: The authors add a new authorship rule to the "all database changes are migrations" practice: migrations must be idempotent, because the same migration script now runs against many independently-created branches over its lifetime rather than once against a single shared database

- **Evidence**: Stated as the specific delta between the 2003 practice and
  its 2026 re-cast form; justified by the new operational fact that
  branch-per-PR means the same migration executes repeatedly against fresh
  branch instances.
- **Confidence**: emerging (a specific, falsifiable prescriptive claim about
  migration authorship, presented as a natural consequence of the new
  workflow rather than backed by an incident or measurement)
- **Quote**: "The same migration runs against many branches over the life of a transition, so it has to behave the same way every time. A migration that fails on re-apply is a bug."
- **Our assessment**: This is a genuinely new prescriptive detail not
  present in the original 2003/2006 practice catalog as described in this
  piece — idempotency wasn't a first-class authorship requirement when
  migrations ran once against a single shared target. It's a plausible and
  specific consequence of branch-per-PR CI (Claim 5), and the article backs
  it operationally with an "expand first, contract later" mechanic
  (splitting add-column and drop-column across separate migrations) as the
  concrete technique for achieving it.

### Claim 4: The CI schema-diff-on-PR mechanism is what converts DBA review from synchronous, gating collaboration to asynchronous, ordinary code review

- **Evidence**: Causal claim tying a specific CI artifact (a `pg_dump
  --schema-only` diff between the CI branch and its parent, posted as a PR
  comment via `gh pr comment`) directly to a role/process change (DBA
  review timing and cadence).
- **Confidence**: emerging (a plausible causal story, but this source is the
  vendor/methodology description of the mechanism, not an account of a team
  that adopted it and observed the review-cadence change)
- **Quote**: "With the schema diff posted on every PR, the DBA reviews async, like any other code reviewer."
- **Our assessment**: The causal link (artifact availability → review-mode
  change) is stated as inevitable but is really a claim about how a
  specific team's DBA changed behavior once given the artifact; the source
  gives no evidence that DBA review actually moved off the calendar in
  practice, only that the mechanism now makes it possible. Worth treating
  as a design intent/argument rather than an observed outcome.

### Claim 5: Destructive testing (deliberately corrupting data, killing a migration mid-run, simulating failover during backup-restore) becomes routine practice rather than a quarterly exercise once branch reset costs approach zero

- **Evidence**: Named as Practice #8, new for 2026, with four example
  destructive test scenarios and a worked illustration via the Jen
  narrative example (see Concrete Artifacts).
- **Confidence**: emerging (logically follows from Claim 1's cost
  architecture, but is a prescriptive practice recommendation, not an
  observed adoption result)
- **Quote**: "When reset costs nothing, teams stop treating the test database as a precious resource. Tests can be aggressive. Cleanup can be skipped, because the next branch starts fresh."
- **Our assessment**: This is one of the more transferable claims in the
  piece — the underlying mechanism (near-zero-cost disposable database
  branches lowering the bar for destructive testing) doesn't depend on
  Lakebase specifically; it applies to any copy-on-write branchable
  database. The specific example scenarios (kill a migration mid-`UPDATE`,
  simulate failover during restore, measure DR runbook time-to-recover) are
  concrete and reusable as a checklist independent of vendor.

### Claim 6: A/B schema-design prototyping at the database level — building two competing schema designs on parallel branches, measuring against production-shaped data, and discarding the loser — is presented as newly viable and is illustrated with a concrete before/after example

- **Evidence**: Named as Practice #9, new for 2026; illustrated with the Jen
  narrative choosing between "three new columns on the existing inventory
  table" vs. "a separate inventory_attributes lookup table," measuring
  common-read-path query performance on each branch, and rejecting the
  lookup-table design because it required a join on the hot read path.
- **Confidence**: anecdotal (the specific "Jen" scenario is a narrative
  illustration constructed for the article, not a reported real-world case
  study — the piece never claims Jen is a real practitioner or team)
- **Quote**: "The lookup-table version performed worse on the common read path because every inventory display required a join. She shipped the columns version, threw away the lookup-table branch and left a note in the PR description."
- **Our assessment**: Useful as a worked pattern (parallel-branch A/B plus a
  documented rejection rationale in the PR description) but the evidence
  tier is weak — "Jen" is an illustrative narrative device inherited from
  Fowler's original 2003 essay, not a cited case study with a named
  company or measured outcome. The pattern itself (build both, measure,
  document why the loser lost) is sound engineering practice independent
  of whether this specific instance is real.

### Claim 7: The CI workflow enforces branch-per-PR and branch teardown as pipeline properties, not developer discipline, via two GitHub Actions templates — `pr.yml` (creates a `ci-pr-<N>` branch on `pull_request: [opened, synchronize]`) and `merge.yml` (deletes the CI branch and the linked feature branch on merge)

- **Evidence**: Two YAML code excerpts in the "How the workflow runs in CI"
  section, plus links to full example workflows in a public GitHub repo
  (`databricks-solutions/lakebase-app-dev-kit`).
- **Confidence**: settled (this is a description of a concrete, linked,
  publicly inspectable artifact — the workflow templates exist in a real
  repository — rather than a general prescriptive claim)
- **Quote**: "Together, these workflows enforce every PR gets its own database and branches are ephemeral as properties of the pipeline, not developer disciplines."
- **Our assessment**: This is the most concretely verifiable claim in the
  piece since it points to an actual public repository
  (`github.com/databricks-solutions/lakebase-app-dev-kit`) containing the
  named workflow files rather than only describing the pattern in prose.
  We did not independently fetch and read the linked `pr.yml`/`merge.yml`
  files in the GitHub repo beyond the excerpts quoted in this blog post —
  see Extraction Notes.

### Claim 8: Lakebase branches integrate with Databricks' Unity Catalog so that governance policy is "designed once, inherited by all the branches" — but this article explicitly defers the mechanism and detail to Part 3

- **Evidence**: Named as Practice #10 with one sentence of description and
  an explicit forward-reference.
- **Confidence**: anecdotal (asserted, not explained or demonstrated in this
  part of the series)
- **Quote**: "With the integrated Unity Catalog, governance is designed once, inherited by all the branches. Policies follow each branch automatically. (We'll discuss this in more detail in part three.)"
- **Our assessment**: Flagged as a gap, not a strong claim — this source
  explicitly withholds the substantive mechanism ("in more detail in part
  three"), so there is nothing here for the guide to cite as evidence about
  *how* governance inheritance actually works. If Part 3 becomes available
  as a source, that would be the piece to mine for the real claim.

### Claim 9: "Agent-as-practitioner with the same branching capability" is named as a new practice (#11) — agents get their own branches, not production access — but again with the substantive detail deferred to Part 3

- **Evidence**: One-sentence practice statement plus explicit
  forward-reference, mirroring the treatment of Practice #10.
- **Confidence**: anecdotal (asserted, not explained in this part)
- **Quote**: "Agents get branches, not production. (We'll also discuss this in more detail in part three.)"
- **Our assessment**: This is the single most guide-relevant sentence in the
  piece for Ch04/Ch02 (agents-and-data-access), and it is also the
  thinnest — one clause, no mechanism, no example of an agent actually
  using a branch. The article's own closing section confirms this
  explicitly: "In part three we'll look at ... the agents creating
  branches alongside Jen. Practices #10 and #11 get their full treatment
  there." Do not cite this source as evidence for *how* agents use
  database branches — only that the practice is named and reserved for
  Part 3.

## Concrete Artifacts

Per-PR branch creation trigger, from the "Per-PR branch creation" section
(full file linked as `templates/project/common/.github/workflows/pr.yml`
in `databricks-solutions/lakebase-app-dev-kit`):

```yaml
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  build-and-test:
    steps:
      - name: Create CI database branch (Lakebase)
        run: |
          PR="${{ github.event.pull_request.number }}"
          ./scripts/ci/resolve-lakebase-branch.sh \
            --lakebase-name "ci-pr-${PR}" \
            --create-from "${{ github.event.pull_request.base.ref }}" \
            --recreate-on-source-mismatch \
            --ensure-endpoint \
            --github-env
```

Branch cleanup on merge, from the "Branch cleanup on merge" section (full
file linked as
`templates/project/common/.github/workflows/merge.yml`):

```yaml
on:
  pull_request:
    types: [closed]
jobs:
  cleanup-lakebase-branches:
    if: github.event_name == 'pull_request' && github.event.pull_request.merged == true
    steps:
      - name: Delete CI and feature DB branches (Lakebase)
        run: |
          PR_NUM="${{ github.event.pull_request.number }}"
          FEATURE_BRANCH="$(bash scripts/sanitize-branch-name.sh \
            "${{ github.event.pull_request.head.ref }}")"
          ./scripts/delete-lakebase-branches.sh \
            "ci-pr-${PR_NUM}" "$FEATURE_BRANCH"
```

The article also links a third, unquoted workflow for periodic cleanup of
orphaned branches (`cleanup-orphans.yml`) and notes teams may want a
"weekly cleanup script that removes orphaned and unused branches" as
branch count grows.

Eleven-practice list (source: "Emerging practices for 2026" section,
paraphrased/enumerated by us from the article's own numbered list — not a
direct quote of the full list, since the article presents it as prose
bullets rather than a single quotable block):

1. DBAs collaborate closely with developers (re-cast: async PR review)
2. All database artifacts are version controlled with application code (+ schema diff, migration test results)
3. All database changes are migrations (+ idempotency authorship rule)
4. Everybody gets their own database instance (now operational per-developer/PR/experiment)
5. Developers continuously integrate database changes (operational at PR granularity)
6. All database changes are database refactorings (branches as rehearsal space)
7. Developers can update their databases on demand ("on demand" = one second)
8. Destructive testing as a default option (new)
9. A/B variant prototyping at the database level (new)
10. Governance designed once via Unity Catalog, inherited by all branches (new; detail deferred to Part 3)
11. Agent-as-practitioner with the same branching capability (new; detail deferred to Part 3)

## Cross-References

- **Corroborates**: `blog-latentspace-databricks-agent-clouds.md` Claim 5
  ("Omnigent's cloud sandbox architecture was built quickly by reusing
  Databricks' Lakebase/Neon storage-compute-separation architecture...")
  and Claim 3 ("...keeping the operational reliability layer (e.g.,
  Lakebase's uptime guarantees) proprietary"). That note describes Lakebase
  only as infrastructure reused for a different product (Omnigent sandboxes)
  and as a proprietary reliability layer; it does not describe branching as
  a feature at all. This note is the first in the corpus to document
  Lakebase's copy-on-write branching mechanism and the workflow built on
  top of it.
- **Contradicts**: None identified. No existing source note makes a
  competing claim about database branching cost, CI-per-PR database
  isolation, or migration idempotency that this source disagrees with.
- **Extends**: `blog-latentspace-databricks-agent-clouds.md` Claim 5's brief
  mention of Lakebase's storage-compute-separation architecture, by
  documenting the specific developer-facing capability (branching) that
  architecture enables, and the CI/CD mechanics built around it.
- **Novel**: The full "evolutionary database design practices, twenty years
  later" framing; the specific CI workflow pattern (branch-per-PR, schema
  diff posted as PR comment, teardown-on-merge); the idempotent-migration
  authorship rule tied explicitly to branch-per-PR re-execution; destructive
  testing and A/B schema prototyping as named practices enabled by
  near-zero branch cost. `blog-simonwillison-browser-compat-db.md`, flagged
  by the Prospector as a possible overlap for "database versioning/branching
  patterns," is not actually about database branching — it covers SQLite
  file hosting via a git orphan branch, which only overlaps at the surface
  level of the word "branch." No claim-level overlap found; not cited above
  as corroborating or extending.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: If Ch02 has (or plans) a section on
  CI/CD pipeline design for data-layer changes, this source provides a
  concrete, linked, publicly-inspectable workflow pattern (Claim 7:
  branch-per-PR creation + schema-diff-as-PR-comment + teardown-on-merge)
  that could be cited as a specific implementation example — with the
  caveat that it's vendor-specific (Databricks Lakebase) and the guide
  should frame it as "one instance of a generalizable pattern" (ephemeral,
  disposable database branches gating CI) rather than a Lakebase
  endorsement.
- **Chapter 04 (Context Engineering)**: The article's most guide-relevant
  claim for agents-and-data (Claim 9: "agents get branches, not
  production") is explicitly a placeholder — the source defers all
  mechanism detail to Part 3. Do not cite this source alone as evidence for
  *how* agents should be given database access; flag Part 3 as a
  follow-up source to mine once published (not yet in the corpus per this
  note's search of `source-notes/`).
- No chapter should cite the ~1-second/O(1) branch-creation performance
  claim (Claim 1) as independently verified — it is vendor-stated with no
  benchmark data in this source.

## Extraction Notes

- Fetched the full article text via the source URL and read it in its
  entirety, including all eleven practice sections, the CI workflow
  section, and the closing "What Jen's New Playbook Shows" summary. Did
  not fetch Part 1 (`thoughtworks.com/insights/blog/data-engineering/enabling-evolutionary-database-branching-with-lakebase`,
  linked in the article) or Part 3 (not yet published — the article
  repeatedly forward-references it as future content) — Part 1 is a
  reasonable follow-up source for the Prospector to queue separately if not
  already discovered, since the Prospector's triage comment confirms it
  had not yet been triaged as of this issue.
- Did not independently fetch the linked GitHub repository
  (`databricks-solutions/lakebase-app-dev-kit`) to verify the full
  `pr.yml`/`merge.yml`/`cleanup-orphans.yml` files beyond the excerpts
  quoted in the blog post itself; the Concrete Artifacts section above
  reproduces only what the article itself quotes.
- Also fetched and read `martinfowler.com/articles/evodb.html` context
  only insofar as this article summarizes it (did not independently fetch
  Fowler's original 2003 essay); all quotes in this note are from the
  Thoughtworks article, not from Fowler's original.
- No paywall or access issue; the article was fully readable.
