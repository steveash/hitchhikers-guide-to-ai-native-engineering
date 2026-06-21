# Auto-Gate Rollout — getting the human out of the merge loop

This repo already has the machinery for autonomous quality (the **Assayer**
AI gate, the Smith `/rework` loop, auto-merge on APPROVE). It stalled for
**operational** reasons, not conceptual ones — a 54-PR backlog built up and
fell to a human gate. This PR fixes the operational failures and stages a
trust-building rollout so the human can exit the loop without losing quality.

## What broke (root causes, all fixed in this PR)

| # | Failure | Fix |
|---|---------|-----|
| B | Assayer runs were **CANCELLED** by `concurrency: cancel-in-progress: true` (a PR gets opened → bot dispatch → synchronize in seconds; each new event killed the running review). 53 of 54 backlog PRs had no final verdict. | `cancel-in-progress: false` in `assayer.yml`. Every (PR, push) now gets a verdict. |
| C | Every miner appended to the **one shared `registry/sources.json`**, so all parallel miner PRs conflicted on it and could never be reviewed. | Miners stop touching it (`miner-batch.yml`); it's regenerated from source-note front-matter by `scripts/build_registry.py` via `registry-rebuild.yml`. |
| D | The `smith-last-run` baseline tag was tagged at the Smith's **feature-branch HEAD**, not main, so it drifted and got stuck ~2 months back, making every Smith run a giant, mutually-conflicting guide diff. | Tag now tracks `origin/main` (`smith-on-source-merge.yml`). |
| A/F | Auto-merge existed for source-notes but the gate was **advisory** (no branch protection) and guide PRs always needed a human. | Guide auto-merge added behind a shadow/live variable; branch-protection + double-gate steps documented below. |
| E/G | No at-a-glance view of gate decisions to build trust. | Per-run decision summary in the Actions UI; shadow mode logs "would merge". |

## Tiered autonomy (the target steady state)

- **APPROVE** → auto-merge (source-notes already; guide via `GUIDE_AUTOMERGE`).
- **REQUEST CHANGES** → Smith `/rework` once, then re-gate (already wired).
- **REJECT** (e.g. fabrication) → stays open with the Assayer's evidence; a
  human only sees these. In the 54-PR backlog this was ~4% (2 fabrications).

You watch the **exception queue and the dashboard**, not every PR.

## Rollout steps (do these in order, after merging this PR)

### 1. Cut the registry over to generated (track C) — **needs your nod**
The generator reproduces the registry but also **normalizes** it, a one-time
visible diff you should eyeball first:
- Indexes **all 403** source notes (today only 216 are indexed — the rest
  silently never got an entry).
- Normalizes `author` to drop trailing role parentheticals
  (`"Fiona Fung (Director…)"` → `"Fiona Fung"`), affecting ~122 entries.
- Backfills missing `date_published` and similar (~37 entries).

Preview the diff, then commit the cutover:
```bash
python3 scripts/build_registry.py
git diff -- registry/sources.json   # review the one-time normalization
```
Also fix the **6 notes with unquoted front-matter** (an `author:` value with a
bare colon); the generator currently keeps them via a fallback parser, but they
should be quoted at the source. `python3 scripts/build_registry.py --check` is a
good CI guard / pre-commit check.

### 2. Re-synthesize the guide from the cleared backlog (track D) — **a choice**
43 source notes just merged; the 6 stale Smith PRs were closed to be
regenerated. Pick the baseline for the next Smith run:
- **Comprehensive** (default, current tag ~April): one solo Smith run produces
  one large but conflict-free guide PR covering everything since. Simplest; may
  be a big PR.
- **Incremental**: `git tag -f smith-last-run <pre-backlog-sha> && git push -f`
  so the next run only synthesizes the 43 new notes. Smaller PR, but synthesis
  of notes merged between April and now is deferred to a later audit.

Then trigger it: `gh workflow run smith-on-source-merge.yml`.

### 3. Enforcement (track A) — DECIDED: no hard branch protection

We tried requiring the `assayer` status check via branch protection and backed it
out (2026-06-21). It is **incompatible with the dispatch-based review path**: bots
review by `workflow_dispatch` (because the `pull_request` webhook is ~35% rate-
limited), and dispatch runs do **not** write a check onto the PR head SHA — so a
required `assayer` check leaves every dispatch-reviewed PR permanently unmergeable
(auto-merge stuck queued). It also deadlocked auto-merge (the merge step runs
inside the assayer job, so the required check was still pending when it merged).

**The gate is the workflow's approve-only-merge logic** (assayer.yml only calls
`gh pr merge` after an APPROVE verdict). That runs on every review regardless of
trigger, so the pipeline flows hands-free. Trust comes from shadow mode + the
gardener audit + the decision log, not from a hard merge block.

If you later want hard enforcement anyway, the robust way is a **status bridge**:
have the assayer post an explicit commit-status (e.g. `assayer-verdict`) on the PR
head SHA in *every* run including dispatch, and require *that* context — never the
implicit job check, which is trigger-dependent.

### 4. Turn on guide auto-merge, shadow → live (tracks E/F/G)
The guide is what readers see, so gate it harder than raw notes:
- **Shadow** first — watch the decisions it *would* make:
  `gh variable set GUIDE_AUTOMERGE --body shadow`
  Every APPROVE on a guide PR logs "would auto-merge" (Actions summary + a PR
  comment) without merging. Review a week of these.
- **Add a second, independent fabrication-only review pass** before going live
  (recommended): a duplicate Assayer job prompted *only* to verify that every
  quote appears verbatim in its source and every prescriptive claim is cited.
  Require both passes to APPROVE. Two agreeing verdicts is the backstop that
  makes auto-merging the published guide trustworthy.
- **Live** once the catch-rate holds: `gh variable set GUIDE_AUTOMERGE --body live`

### 5. Monitor the system, not the PRs (track G)
- Extend `scripts/generate_dashboard.py` to surface gate **pass-rate**,
  **fabrication-catch count**, and **exception-queue depth**.
- Let the weekly **gardener** (`scripts/gardener.py`) re-sample merged notes and
  re-verify quotes, filing an issue on any drift — this catches the rare gate
  miss without putting you back in the per-PR path.

## Trust calibration
The 2026-06 backlog clearance is the evidence this works: an Assayer agent-gate
processed all 54 PRs, cleanly separating 50 independently-verifiable PRs from
**2 real fabrications + 1 duplicate + 1 quote-framing fix**. Shadow mode lets
you reproduce that confidence on live traffic before removing yourself entirely.
