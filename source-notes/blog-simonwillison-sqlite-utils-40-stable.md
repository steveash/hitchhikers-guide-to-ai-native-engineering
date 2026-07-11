---
source_url: https://simonwillison.net/2026/Jul/7/sqlite-utils-4/
source_type: blog-post
title: "sqlite-utils 4.0, now with database schema migrations"
author: Simon Willison
date_published: 2026-07-07
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1748"
---

# sqlite-utils 4.0, now with database schema migrations

> Simon Willison ships sqlite-utils 4.0 (the first major version bump since
> 3.0 in 2020), documents its migrations/nested-transaction/compound-FK
> feature set, has GPT-5.5 and Fable 5 independently review the full diff
> before tagging — GPT-5.5 finds only documentation nits while Fable 5 finds
> a set of release blockers plus further verified bugs (4 blockers and 6
> non-blockers per Fable's own "10 verified bugs" report; the post's summary
> sentence phrases the count differently — the two primary sources are
> reconciled in Claim 10) — and has the upgrade guide and release notes fully
> authored by three different models.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, published 2026-07-07 at
  7:32pm; auto-discovered via trusted feed `simon-willison`. The canonical
  article URL is `simonwillison.net/2026/Jul/7/sqlite-utils-4/`; the
  `#atom-everything`-suffixed URL in the issue body resolves to a short
  "beat" pointer post that links to this article — consistent with the
  pattern already noted in `blog-simonwillison-sqlite-utils-40rc1.md`'s
  Extraction Notes. This note cites the canonical article URL.)
- **Author credibility**: Simon Willison is the creator and maintainer of
  sqlite-utils, Datasette, and the `llm` Python CLI. This is first-party
  release engineering documentation — he is both the practitioner and the
  project owner making the ship/no-ship call, with 124 releases of this
  specific project behind him. The post explicitly names Claude Fable 5,
  Claude Opus 4.8, and GPT-5.5 individually and evaluates each on its own
  merits, including reproducing GPT-5.5's underwhelming review in full.
- **Scope**: Covers the stable 4.0 release: the migrations system's design
  and prior art (Django, `sqlite-migrate`), `db.atomic()` nested
  transactions, compound foreign keys, the full list of breaking changes,
  AI-authored documentation, and a head-to-head "final review before
  shipping" comparison between GPT-5.5 and Fable 5 on the same task. Does
  NOT cover: the rc1→rc2 `delete_where()` data-loss bug and AgentsView cost
  breakdown (see `blog-simonwillison-sqlite-utils-40rc2.md` for that), or
  performance benchmarks.

## Extracted Claims

### Claim 1: sqlite-utils 4.0 is the project's 124th release and its first major (breaking) version bump since 3.0 in November 2020, introducing three major features — database migrations, nested transactions via `db.atomic()`, and compound foreign keys
- **Evidence**: Author's direct statement, opening the post.
- **Confidence**: settled (first-party; a verifiable release/version claim)
- **Quote**: "This morning I released sqlite-utils 4.0, the 124th release of that project and the first major version bump since 3.0 in November 2020."
- **Our assessment**: Establishes the release's weight — this is a rare major-version event for a foundational, widely-depended-upon library (the persistence layer for `llm` and part of the Datasette ecosystem), not a routine point release. That context matters for interpreting how seriously Willison treated the pre-release review described in Claims 8–11: a breaking-change release that "promises no backwards-incompatible fixes for a very long time" (Claim 9's prompt) justifies unusually thorough AI-assisted auditing.

### Claim 2: The migrations system was promoted from a three-year-old separate package (`sqlite-migrate`) into sqlite-utils core, deliberately omitting reverse/rollback migrations because rollback is rarely used in practice
- **Evidence**: Author's direct statement of design provenance and philosophy; corroborated by `blog-simonwillison-sqlite-utils-40rc1.md` Claim 2 (same design decision, described at the rc1 stage).
- **Confidence**: settled (first-party design decision, stated as deliberate, and already validated via `sqlite-migrate`'s multi-year production use before promotion)
- **Quote**: "The design of sqlite-utils migrations is three years old now—I had originally released it as a separate package called sqlite-migrate, which never quite graduated beyond a beta release."
- **Quote (rollback rationale)**: "I decided to skip rollback, since in my experience it's a feature that is rarely used. With a SQLite project, an easy way to achieve rollback is to create a copy of your database file before you apply the migrations!"
- **Our assessment**: This is not new claim content relative to the rc1 note (which already documents the forward-only design decision), but it adds the provenance detail that the design sat in a separate, lower-stakes package for three years and was battle-tested there before being promoted to the widely-depended-upon core library — a specific, verifiable maturation path rather than a fresh design shipped straight into a major version.

### Claim 3: Willison frames Django's Migrations (built by Andrew Godwin, based on Godwin's earlier `South` project) as his favorite implementation of the schema-migration pattern, tracing his own involvement in the design space back to a competing 2008 DjangoCon proposal called `dmigrations`
- **Evidence**: Author's direct historical account, with named people, named prior art, and a specific dated event (the first DjangoCon).
- **Confidence**: anecdotal (a personal historical account; not evaluable as a factual claim about migration system quality, but the historical details — DjangoCon's first year being 2008, Godwin's authorship of Django Migrations via South — are independently verifiable public facts)
- **Quote**: "My favorite implementation of this pattern remains Django's Migrations, developed by Andrew Godwin based on his earlier project South. Fun fact: Andrew, Russ Keith-Magee, and I presented our competing approaches to schema migrations for Django on the Schema Evolution panel at the very first DjangoCon back in 2008! My attempt was called dmigrations, developed with a team at Global Radio in London."
- **Our assessment**: This is scope/positioning context rather than an AI-native engineering claim on its own — it explains that sqlite-utils' migrations design is explicitly *not* attempting to be Django's ORM-driven, auto-generating, rollback-capable system, but a deliberately simpler one for a library that "encourages programmatic table creation rather than a model definition ORM." Relevant mainly as design-philosophy context for Claim 2's forward-only decision.

### Claim 4: Compound foreign key support was added to 4.0 because a coding agent, asked to review all open issues and PRs for anything that should ship as a breaking change now rather than later, correctly identified compound foreign keys as exactly that kind of feature
- **Evidence**: Author's direct account of the origin of a specific shipped feature, attributing the feature's *inclusion* in this release (not merely its implementation) to an agent's issue-triage judgment.
- **Confidence**: emerging (a single, specific, first-party account of an agent's scoping recommendation being accepted and shipped; not independently replicated)
- **Quote**: "This came about when I asked a coding agent to review all open issues and PRs for things that should be included in a 4.0 release since they would represent breaking changes if I added them later, and it correctly identified that compound foreign keys were exactly that kind of feature."
- **Our assessment**: This is a distinct pattern from AI-assisted *implementation* or *review* — here an agent performed release-scoping triage across an issue/PR backlog and made a judgment call about breaking-change timing that Willison accepted. It's a narrow but concrete example of delegating a planning/prioritization task (not just a coding task) to an agent, and the recommendation held up: the feature shipped and, per Claim 5, its API design was independently praised.

### Claim 5: Claude Fable 5 helped design the compound foreign key *creation* API (as opposed to just the breaking-change introspection method Willison wrote himself), producing an API design Willison judged consistent with the rest of the library
- **Evidence**: Author's direct account distinguishing what he wrote himself (the introspection breaking change) from what he delegated to Fable 5 (the "more fiddly" creation API).
- **Confidence**: anecdotal (single practitioner's subjective judgment of API design quality, though the case is specific: one method he wrote vs. one he delegated, within the same release)
- **Quote**: "I started with a breaking change to the table.foreign_keys introspection method, and then decided to see if Claude Fable 5 could handle the more fiddly job of integrating compound foreign key creation into the library. The API design it helped create felt exactly right to me—consistent with how the rest of the library worked already."
- **Our assessment**: A concrete, scoped example of "use the agent for the harder API-design sub-problem, keep the simpler one yourself" — the opposite of assuming agents are only useful for boilerplate. Consistency with existing library conventions (rather than a locally-clever but inconsistent design) is the specific quality Willison credits, which is a harder bar for API design than "does it work."

### Claim 6: The upgrade guide and release notes for sqlite-utils 4.0 were entirely written by three different models — Claude Fable 5, Claude Opus 4.8, and GPT-5.5 — and Willison states he has reviewed them closely and confirms they are accurate and comprehensive
- **Evidence**: Author's direct statement of authorship and his own verification step.
- **Confidence**: settled (first-party, shipped, released documentation — the upgrade guide and release notes are live at `sqlite-utils.datasette.io`)
- **Quote**: "The upgrade guide was entirely written by Claude Fable 5, Claude Opus 4.8 and GPT-5.5. The same is true of the release notes."
- **Quote (rationale)**: "This is the kind of documentation I've slowly become comfortable outsourcing to the robots. It doesn't need to convince people of anything, or express any opinions—its job is to be as accurate and detailed as possible. I've reviewed the release notes closely and can confirm they are accurate and comprehensive."
- **Our assessment**: This generalizes and extends the existing corpus finding (`blog-simonwillison-sqlite-utils-40rc2.md` Claim 12) that Willison considers release notes "boring, predictable and accurate" writing safe to delegate — here the delegation is explicit multi-model (three separate vendors' models jointly producing one document set) and extends beyond the changelog to the full upgrade guide. The stated boundary condition — safe because the writing "doesn't need to convince people of anything, or express any opinions" — is the generalizable rule, not "AI can write good docs" as an unqualified claim.

### Claim 7: Willison attributes overcoming a year of inertia on shipping the stable 4.0 release specifically to AI assistance, primarily from Fable 5 with lesser contributions from Opus 4.8 and GPT-5.5
- **Evidence**: Author's direct causal attribution, contrasted with his own account of having released the first 4.0 alpha over a year earlier and "dragging my heels" since.
- **Confidence**: anecdotal (single practitioner's self-reported motivational account; not independently verifiable, but specific and dated — first alpha "over a year ago" against this July 2026 stable release)
- **Quote**: "Assistance from Claude Fable 5 (and to a lesser extent Opus 4.8 and GPT-5.5) gave me just the boost I needed to overcome inertia and make the most of the time I could afford to spend on this library."
- **Our assessment**: A distinct value proposition from "AI makes you faster at a task" — this is "AI assistance made a long-delayed task feel tractable enough to actually start/finish," a psychological/motivational effect on a maintainer's willingness to take on accumulated technical debt, not a raw throughput claim. Harder to generalize from a single anecdote, but notable as a claim not covered by the corpus's existing productivity-metric-style Fable claims.

### Claim 8: Willison characterizes Fable 5 as having "really good taste" in API design and being "relentlessly proactive" when given an open-ended goal, explicitly citing his own earlier post on that behavior
- **Evidence**: Author's direct characterization, with an inline link to his own prior post (`blog-simonwillison-fable-relentlessly-proactive.md` in this corpus) as the basis for the "relentlessly proactive" framing.
- **Confidence**: anecdotal (subjective practitioner characterization, though explicitly tied back to a previously-documented, more detailed episode)
- **Quote**: "Fable has really good taste in API design, and is relentlessly proactive if you give it a more open goal."
- **Our assessment**: This is a direct self-citation linking this release's compound-FK API design experience (Claim 5) to Willison's earlier, more granular account of "relentlessly proactive" behavior (a 17-step autonomous CSS debugging session, per `blog-simonwillison-fable-relentlessly-proactive.md` Claim 1). It shows the "relentlessly proactive" framing has become a standing descriptor Willison reaches for repeatedly across different projects/sessions, not a one-off phrase — see Cross-References.

### Claim 9: Willison's most successful prompt for pre-release review was a two-part instruction: review the diff against the last stable tag as a shipping-readiness audit, then separately have the model write and save (but not commit) scratch scripts exercising every new v4 feature against the changelog and upgrade guide
- **Evidence**: Author reproduces the exact prompt text used, calling it his "most successful prompt," and states he ran the identical prompt against two different models for a head-to-head comparison (Claim 10).
- **Confidence**: emerging (a specific, reusable prompt structure, directly followed by comparative before/after results in Claims 10–11)
- **Quote**: "review the changes on main since the last tagged 3.x release - I am about to ship them as sqlite-utils 4.0, a stable version that promises no backwards-incompatible fixes for a very long time. review the changelog and upgrade guide, and write yourself scratch scripts to try out all of the new features in v4 - save those scripts but don't commit them"
- **Our assessment**: This is a specific, reusable release-audit prompt pattern with two components worth separating: (1) framing the task as "review the diff since the last stable tag, you are about to ship this as a version with a long-term compatibility promise" — which anchors the model on shipping-consequence stakes rather than a generic "review this code" ask; (2) explicitly instructing the model to write scratch verification scripts against its own claims in the docs (not just read the docs), which is what produced the concrete, reproducible bug list in Claim 11. This extends `blog-simonwillison-sqlite-utils-40rc2.md` Claim 7's cross-model review pattern with a specific, quotable prompt template rather than a paraphrased description of "review changes since the last RC."

### Claim 10: Run head-to-head on the identical prompt, GPT-5.5 (Codex Desktop, "xhigh" reasoning) wrote 5 Python scripts and found nothing substantive — only documentation/versioning nits — while Fable 5 (Claude Code) wrote 12 scripts and found a substantive defect list, 4 of them release blockers (the non-blocker count is reported inconsistently between the post's summary and Fable's own report — see Our assessment)
- **Evidence**: Author's direct comparative account, with both models' full reports linked and (for Fable) reproduced via a combined repro script whose output is quoted in full in the post.
- **Confidence**: emerging (a real, verifiable, single head-to-head comparison — both underlying reports are public and were independently fetched and cross-checked for this note — but it is one comparison on one task, not a controlled study)
- **Quote**: "GPT-5.5 wrote 5 Python scripts and didn't turn up anything particularly interesting—its final report is here. Fable 5 wrote 12 scripts, identified 4 release blockers and 10 additional issues in its report, and built a neat combined repro script, which, when run, output the following:"
- **Our assessment**: This is a striking asymmetry from a single practitioner's identical-prompt, identical-task comparison, and it is checkable: GPT-5.5's actual findings (per the linked GitHub comment, fetched directly for this note) were four minor documentation/versioning gaps — a stale version string, an un-updated changelog section, two documentation omissions — none of which were correctness bugs in the shipped code. Fable 5's report, by contrast, enumerated specific, reproducible defects with file/line references and a working repro script (Concrete Artifacts). This is a data point for "cross-model review value is not symmetric — one model can dramatically outperform another on the identical prompt, on the identical task, in the identical session cadence," which nuances (without contradicting) `blog-simonwillison-sqlite-utils-40rc2.md` Claim 9's "habitually having Anthropic's best model review OpenAI's work and vice versa... often enough to be valuable" — here, one direction (Fable reviewing) was far more valuable than the other (GPT-5.5 reviewing) on this specific task.
- **Note on the issue count — two conflicting primary sources**: The blog post's summary sentence (the Quote above) states Fable "identified 4 release blockers **and 10 additional issues**," which read additively is 14 issues. Fable 5's own report, quoted in Claim 11, instead says "**10 verified bugs, four of which** I'd treat as release blockers" — inclusive counting, 10 total (4 blockers + 6 non-blockers). The combined repro script reproduced in full under Concrete Artifacts enumerates exactly **10 numbered bugs**, which matches Fable's own inclusive "10 verified bugs" figure, not Willison's additive "4 + 10." This note treats **10 total / 4 blockers / 6 non-blockers** as the load-bearing count because it is corroborated by two independent primary sources (Fable's own report language and the 10-item repro script) against the post's single looser summary sentence — but the discrepancy is real, and is surfaced here rather than silently resolved. A future cross-referencing note that needs a total should cite Fable's "10 verified bugs" report figure, not the post's "10 additional issues" phrasing.

### Claim 11: Fable 5's review found two silent-data-loss bugs in the new transaction model, a data-corrupting column-order bug in compound foreign keys, and a data-corrupting default in CSV insert — all four rated release blockers for a version "promising long-term stability"
- **Evidence**: Fable 5's own written report (fetched directly from the linked GitHub issue comment, `simonw/sqlite-utils#769`, for this note), including its methodology (three parallel review agents over an ~8,600-insertion diff, each high-severity finding independently re-verified by Fable itself) and file/line-referenced descriptions of each blocker.
- **Confidence**: emerging (a specific, independently-fetched, verifiable primary-source report; the bugs were confirmed real by the maintainer and fixed pre-release — see Claim 12 — but this remains a single review episode)
- **Quote**: "The documented features all work as advertised — every claim in the changelog and upgrade guide that I tested held up, and the full test suite passes (1253 passed, 16 skipped). But the review found 10 verified bugs, four of which I'd treat as release blockers for a version promising long-term stability: two silent-data-loss bugs in the new transaction model, a data-corrupting column-order bug in the new compound foreign key support, and a data-corrupting default in CSV insert." (Simon Willison, quoting Fable 5's report, `github.com/simonw/sqlite-utils/issues/769#issuecomment-4900034150`)
- **Our assessment**: The methodology detail — three parallel review agents by *category* (transaction model; foreign keys/case-insensitivity; migrations/CLI) followed by Fable independently re-verifying every high-severity finding itself before reporting — is a specific, reusable review-fan-out pattern distinct from a single linear read-through. It also demonstrates a self-skepticism step (re-verify your own subagents' findings before reporting them as confirmed) that guards against subagent false positives, which is a different mechanism than `blog-simonwillison-sqlite-utils-40rc2.md` Claim 8's cross-*model* verification (paste findings into a fresh session of a different model) — this is intra-model, pre-report verification by the orchestrating agent itself.

### Claim 12: All 10 of Fable 5's reported bugs were accepted as genuine and fixed pre-release across a single 16-commit pull request (756 additions, 52 deletions, 20 files changed)
- **Evidence**: Author's direct statement plus a linked PR; PR metadata independently confirmed via the GitHub API for this note (`simonw/sqlite-utils#779`, title "Fixes for final review in issue #769").
- **Confidence**: settled (a concrete, closed, verifiable PR — not a self-reported estimate)
- **Quote**: "I found myself agreeing with almost all of them. Here's the PR with 16 commits where we worked through them in turn."
- **Our assessment**: "Almost all" (not literally "all 10") is the author's own hedge — worth preserving rather than rounding up to "100% acceptance." The PR scope (16 commits, 20 files, +756/-52) shows that acting on an AI-generated pre-release bug report was, again as in the rc1→rc2 audit (`blog-simonwillison-sqlite-utils-40rc2.md` Claim 2, "37 prompts, 34 commits... over 30 separate files"), a substantial, multi-commit engineering effort rather than a handful of one-line patches — a second data point calibrating what "AI does a pre-release audit, then the fixes get made" actually costs in follow-through work across this project's two most recent release cycles.

### Claim 13: Willison's overall verdict is unequivocal — sqlite-utils 4.0 is a significantly higher-quality release than it would have been without frontier-model assistance
- **Evidence**: Author's closing statement, made after the full account of both the documentation-authorship and bug-finding assistance described above.
- **Confidence**: anecdotal (a single practitioner's subjective, summary self-assessment; not independently measurable, but made by the person with the most complete first-hand knowledge of what the release would have looked like without that assistance — himself)
- **Quote**: "There's no doubt in my mind that sqlite-utils 4.0 is a significantly higher-quality release than if I had built it without the assistance of the latest frontier models."
- **Our assessment**: As a closing claim it is the least specific/falsifiable item in the note (it's a counterfactual about a release that didn't happen), but it is grounded by everything preceding it in the same post: a specific accepted feature-scoping recommendation (Claim 4), a specific praised API design (Claim 5), specific authored documentation Willison verified himself (Claim 6), and a specific, fetched, four-blocker bug report with a working repro script and a 16-commit fix PR (Claims 10–12). The verdict is a summary of concrete, individually-checkable evidence rather than a standalone vibes claim.

## Concrete Artifacts

### Migration system — Python API (from the post)

```python
from sqlite_utils import Migrations

migrations = Migrations("creatures")

@migrations()
def create_table(db):
    db["creatures"].create(
        {"id": int, "name": str, "species": str},
        pk="id",
    )

@migrations()
def add_weight(db):
    db["creatures"].add_column("weight", float)

@migrations()
def change_column_types(db):
    db["creatures"].transform(types={"species": int, "weight": str})
```

*Source: Simon Willison, simonwillison.net/2026/Jul/7/sqlite-utils-4/*
*CLI usage: `uvx sqlite-utils migrate data.db migrations.py`, then
`uvx sqlite-utils migrate data.db migrations.py --list` to show applied vs.
pending migrations.*

### `db.atomic()` nested transaction example (from the post)

```python
with db.atomic():
    db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")
    db.table("dogs").insert({"id": 2, "name": "Pancakes"})
```

*Source: Simon Willison, simonwillison.net/2026/Jul/7/sqlite-utils-4/*
*Willison: "SQLite supports Savepoints, and as a result db.atomic() can be
nested to carry out transactions inside of transactions."*

### Fable 5's combined repro script output (verbatim from the post)

```
=== 1. Failed db.execute() write leaves an implicit transaction open ===
  in_transaction after failed write: True
  BUG: table 'other' silently lost when connection closed

=== 2. Leading ';' bypasses the query() first-token scanner ===
  BUG: raised OperationalError: no such savepoint: sqlite_utils_query
  BUG: row persisted despite rollback (count=1)

=== 3. Rejected write PRAGMA via query() still takes effect ===
  BUG: user_version=5 after 'rejected' statement (docs say no effect)

=== 4. Implicit compound FK resolves pk columns in table order, not PK order ===
  BUG: other_columns reported as ('b', 'a'), should be ('a', 'b')
  BUG: transform of valid data raised IntegrityError: FOREIGN KEY constraint failed

=== 5. ForeignKey (now a dataclass) is no longer hashable ===
  BUG: cannot use 'sqlite_utils.db.ForeignKey' as a set element (unhashable type: 'ForeignKey')

=== 6. Mixed ForeignKey objects and tuples in foreign_keys= rejected ===
  BUG: foreign_keys= should be a list of tuples

=== 7. insert --csv into an EXISTING table transforms its column types ===
  BUG: existing zip '01234' is now 1234 (column type: int)

=== 8. insert(pk=, alter=True) regression: InvalidColumns before alter runs ===
  BUG: InvalidColumns: Invalid primary key column ['id'] for table t with columns ['a']

=== 9. migrate --stop-before an already-applied migration applies everything ===
  BUG: m2 was applied despite --stop-before m1 (m1 already applied)

=== 10. ensure_autocommit_on() silently commits an open transaction ===
  BUG: row survived rollback (count=1) - transaction was committed
```

*Source: Simon Willison, simonwillison.net/2026/Jul/7/sqlite-utils-4/,
reproducing Fable 5's `12_bug_repros.py` output (also independently fetched
from `gist.githubusercontent.com/simonw/95800bf584f8e437f1cf0d48d9ef81e6` for
this note, which confirms identical content).*

### GPT-5.5's full findings (fetched directly from the linked GitHub comment, not quoted in the blog post itself)

```
Not much interesting from GPT-5.5:

- pyproject.toml is still version = "4.0rc3", and uv run sqlite-utils
  --version reports 4.0rc3. If you ship current main as-is, you won't
  publish a stable 4.0.
- docs/changelog.rst still has the current post-rc3 notes under
  "Unreleased", with the next section as 4.0rc3. Before tagging, move
  those bullets into a "4.0 (2026-07-06/07)" section and update the anchor.
- docs/upgrading.rst doesn't mention the JSON Unicode output change /
  --ascii escape hatch, even though docs/changelog.rst does. That's a
  byte-for-byte CLI behavior change, so I'd add it to the command-line
  upgrade notes.
- docs/upgrading.rst says raw db.execute() writes now commit
  automatically, but the INSERT ... RETURNING carve-out is only
  documented in docs/python-api.rst. I reproduced that
  db.execute("insert ... returning ...") stays in a transaction until
  explicit commit(), so the upgrade guide should include that caveat.
- The post-rc3 --no-headers for --fmt/--table change from d516e58
  appears in CLI docs/tests, but not in the current changelog's
  post-rc3 bullets.

Verification passed: `uv run pytest` had `1253 passed, 16 skipped`;
Sphinx `-W` passed; and the scratch v4 smoke suite passed.
```

*Source: GPT-5.5 via Codex Desktop (xhigh reasoning), as quoted by Simon
Willison, `github.com/simonw/sqlite-utils/issues/769#issuecomment-4899982463`
(markdown link syntax stripped for readability; wording otherwise verbatim).
This full report is linked but not reproduced in the blog post itself —
fetched directly from GitHub for this note to allow a fair comparison
against Fable 5's report below.*

### sqlite-utils 4.0's other notable breaking changes (from the post)

```
- Upserts now use SQLite's INSERT ... ON CONFLICT ... DO UPDATE SET syntax,
  detect existing table primary keys automatically and reject records that
  are missing required primary key values. (#652)
- db.query() now executes immediately and rejects statements that do not
  return rows; use db.execute() for writes and DDL. ("Probably the most
  disruptive breaking change" per Willison.)
- CSV and TSV imports now detect column types by default, while inserts
  into existing tables preserve those tables' column types. (#679)
- table.extract() and extracts= no longer create lookup table records for
  all-null values. (#186 — "the oldest issue addressed by this release...
  opened (by me) in October 2020.")
```

*Source: Simon Willison, simonwillison.net/2026/Jul/7/sqlite-utils-4/,
paraphrasing the release notes with his own inline annotations.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-sqlite-utils-40rc1.md` Claim 2 ("The migrations
    system intentionally omits reverse migrations—mistakes must be fixed
    by deploying fresh forward migrations"): this source (Claim 2) restates
    the identical design decision at the stable-release stage, adding the
    provenance detail that the design shipped in the separate `sqlite-migrate`
    package for three years before being promoted to core.
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 9 ("Willison states he
    has moved from skepticism to habitual practice on cross-vendor model
    review"): this source is a third documented instance (after the CSRF
    review and the rc2 audit) of Willison running a cross-vendor comparative
    review — here explicitly head-to-head on the identical prompt (Claim 9),
    rather than sequential (one model reviewing after another already fixed
    things, as in rc2).
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 12 (AI-authored release
    notes: "these are better than I would have created myself... because
    they need to be boring, predictable and accurate"): this source's Claim 6
    extends the identical rationale from the changelog to the full upgrade
    guide, and to three-model joint authorship rather than one.
  - `blog-simonwillison-fable-relentlessly-proactive.md` Claim 1 (Fable 5's
    17-step autonomous debugging session, framed under the same
    "relentlessly proactive" description): this source's Claim 8 is
    Willison explicitly reapplying that same descriptor, with an inline
    self-citation, to a different project and task (compound FK API design)
    five weeks later — evidence the framing has become a standing
    characterization for this practitioner rather than a one-off reaction.

- **Contradicts**: None filed. See "nuance, not contradiction" note below
  under Extends — Claim 10's finding that Fable 5 dramatically outperformed
  GPT-5.5 on this identical-prompt review does not contradict
  `blog-simonwillison-sqlite-utils-40rc2.md` Claim 7 (GPT-5.5 catching two
  P1 bugs Fable's own review-and-fix pass missed, one release earlier): the
  two episodes have different task structures (parallel independent review
  here vs. sequential re-review-after-fixes there) and are each a single
  data point, not conflicting general claims about either model's fixed
  capability. Per MINER.md §4a, this is a conditioning-variable difference
  (task structure/ordering), not a contradiction — both are captured here
  as complementary evidence under Claim 10's "Our assessment" rather than
  filed as a contradiction issue.

- **Extends**:
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 7 (GPT-5.5 cross-model
    review finding real bugs Fable's own review-and-fix pass missed): this
    source's Claims 9–11 extend that pattern with a specific, quotable,
    reusable prompt template (Claim 9) and a documented case where the
    asymmetry ran the *other* direction — Fable 5 dramatically
    outperforming GPT-5.5 on an identical head-to-head prompt (Claim 10).
    Together the two notes show cross-model review value is real but not
    symmetric or guaranteed in either direction.
  - `blog-simonwillison-sqlite-utils-40rc1.md` (the entire note, covering
    4.0rc1's feature announcement): this source is the stable-release
    capstone, documenting the same three headline features (migrations,
    `db.atomic()`, compound foreign keys) as shipped, plus the two
    additional pre-release audit rounds (rc2's `delete_where()` fix, this
    post's Fable-vs-GPT-5.5 final review) that hardened them between rc1
    and stable.
  - `blog-simonwillison-fable-judgement.md` (the corpus's coverage of
    Willison's stated subagent-delegation policy): this source's
    methodology detail in Claim 11 (three parallel review subagents by
    category, then self-re-verification of each high-severity finding by
    the orchestrating agent before reporting) is a specific instance of
    fan-out-then-verify subagent structure that could be cross-checked
    against that note's delegation-policy claims in a future synthesis pass.

- **Novel**:
  - **First in-corpus documented case of an identical review prompt run
    head-to-head against two vendors' frontier models on the same
    real-world task, with both full reports independently fetched and
    compared** (Claim 10, Concrete Artifacts): prior corpus entries document
    sequential cross-model review (model A implements/reviews, model B
    reviews after); this is simultaneous, identical-prompt, comparable
    output.
  - **First in-corpus example of an agent's issue/PR-backlog triage
    judgment (not code implementation or review) being credited with
    shaping release scope** (Claim 4): the agent recommended *including* a
    feature in the current release rather than deferring it, based on
    breaking-change timing reasoning — a planning-layer contribution
    distinct from writing or reviewing code.
  - **First in-corpus documented three-model joint authorship of a single
    piece of technical documentation** (Claim 6): Claude Fable 5, Claude
    Opus 4.8, and GPT-5.5 jointly wrote one upgrade guide and one set of
    release notes, reviewed by the human author as a single artifact rather
    than per-model sections.

## Guide Impact

- **Chapter 02 (Harness Engineering) / release-audit workflows**: Add
  Claim 9's exact two-part prompt template ("review the diff since the
  last stable tag, framed against shipping stakes" + "write and save
  scratch scripts exercising every new feature against the docs, don't
  commit them") as a concrete, reusable pre-release review prompt,
  alongside the existing rc2-sourced pattern. This is more specific and
  quotable than the rc2 note's paraphrased "review changes since the last
  RC" prompt.

- **Chapter 01 (Daily Workflows) — "Cross-model audit for shortcut
  detection"**: Add Claim 10 as a caution alongside the existing
  cross-model-review guidance: running the identical review prompt against
  two vendors' models does not guarantee comparable value from each
  direction — here Fable 5 found 4 release blockers and 6 further issues
  where GPT-5.5 found only documentation nits, on the same task. Recommend
  against treating "get a second model's review" as interchangeable across
  vendors/models without expecting variance in outcome quality.

- **Chapter 03 (Patterns & Practices) — subagent review fan-out**: Add
  Claim 11's methodology (three parallel review subagents split by
  functional area, then the orchestrating agent independently re-verifying
  every high-severity finding before including it in the final report) as
  a concrete fan-out-then-self-verify pattern for AI-assisted code review,
  distinct from and complementary to the cross-*model* verification pattern
  already documented via `blog-simonwillison-sqlite-utils-40rc2.md` Claim 8.

- **Chapter 04 (Model Judgement / Capability Arcs)**: If the guide
  documents AI-authored technical writing as a delegation category, cite
  Claim 6's specific boundary condition — Willison's stated rule is that
  this kind of writing is safe to delegate because "it doesn't need to
  convince people of anything, or express any opinions," not because AI
  writing is broadly trustworthy for documentation. The three-model joint
  authorship (Fable 5 + Opus 4.8 + GPT-5.5) is a novel data point for
  multi-model collaborative documentation generation, reviewed once by the
  human as a finished artifact.

## Extraction Notes

- **Canonical URL resolution**: The issue's source URL
  (`simonwillison.net/2026/Jul/7/sqlite-utils/#atom-everything`) is a short
  "beat" pointer post (body: "See sqlite-utils 4.0, now with database
  schema migrations for details.") that links to the actual article at
  `simonwillison.net/2026/Jul/7/sqlite-utils-4/`. I fetched both pages
  directly via `curl` (not WebFetch, per the verbatim-quote requirement)
  and confirmed the pointer post contains no independent content beyond the
  link. This note's `source_url` is the canonical article.
- **Sub-pages followed**: Per MINER.md §1, I followed the two GitHub issue
  comments containing GPT-5.5's and Fable 5's full pre-release review
  reports (`github.com/simonw/sqlite-utils/issues/769`, comments
  `4899982463` and `4900034150`), fetched directly via the GitHub API
  (`gh api repos/simonw/sqlite-utils/issues/769/comments`) to get verbatim
  text rather than relying on the blog post's paraphrase/excerpt. I also
  fetched PR `simonw/sqlite-utils#779` metadata via the GitHub API to
  confirm the "16 commits" claim (Claim 12) and get exact diff stats. I did
  not follow the two Gist links (`823fdecc...` for GPT-5.5's scripts,
  `95800bf5...` for Fable 5's scripts) beyond the already-quoted repro
  script output, or the `sqlite-utils.datasette.io` changelog/upgrade-guide
  pages themselves, as the blog post's own reproduced content and the two
  fetched GitHub comments already cover the load-bearing claims.
- **Verbatim quotes**: All blog-post quotes in this note were extracted from
  raw HTML fetched via `curl` (not WebFetch's summarizing pass) and checked
  character-for-character against the source HTML, including exact
  apostrophe/em-dash characters. The GPT-5.5 and Fable 5 report quotes were
  extracted from the raw GitHub API JSON response for the two comments (not
  the blog post's excerpts), which is a stricter verbatim source than the
  post itself since Willison's post only paraphrases/summarizes GPT-5.5's
  report rather than reproducing it — this note reproduces GPT-5.5's report
  in full in Concrete Artifacts precisely because the blog post doesn't,
  which is necessary to support Claim 10's comparison.
- **Cross-reference verification** (per MINER.md §4b): all claim citations
  above were checked against the actual numbered `### Claim:` headings in
  the cited notes before writing:
  - `blog-simonwillison-sqlite-utils-40rc1.md` Claim 2 verified at lines
    63–75 of that note (heading "Claim 2: The migrations system
    intentionally omits reverse migrations...").
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 7 verified at lines
    134–153 of that note (heading "Claim 7: A second, independent model
    (GPT-5.5 via Codex Desktop, 'xhigh' reasoning effort) reviewing the
    same changes after Fable's pass found two additional P1 transaction
    bugs...").
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 8 verified at lines
    155–167 of that note (heading "Claim 8: Willison confirms a second
    model's findings by pasting them into a fresh session of the first
    model...").
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 9 verified at lines
    169–184 of that note (heading "Claim 9: Willison states he has moved
    from skepticism to habitual practice on cross-vendor model review...").
  - `blog-simonwillison-sqlite-utils-40rc2.md` Claim 12 verified at lines
    218–233 of that note (heading "Claim 12: Fable wrote the changelog
    incrementally into an 'Unreleased' section...").
  - `blog-simonwillison-fable-relentlessly-proactive.md` Claim 1 verified
    at lines 44–61 of that note (heading "Claim 1: Fable, given only a
    screenshot and a one-line prompt about a CSS scrollbar bug, autonomously
    executed 17 investigative steps...").
- **No contradictions filed**: The one candidate tension (Claim 10 vs.
  `...40rc2.md` Claim 7 on relative GPT-5.5/Fable review performance) was
  assessed per MINER.md §4a as a conditioning-variable difference (task
  structure), not a genuine contradiction, and is documented under
  Cross-References → Contradicts and Claim 10's "Our assessment" rather
  than filed as a separate issue.
