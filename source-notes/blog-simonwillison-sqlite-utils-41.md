---
source_url: https://simonwillison.net/2026/Jul/11/sqlite-utils/
source_type: blog-post
title: "sqlite-utils 4.1: STRICT table transforms, --code rows, and Codex-driven backlog triage"
author: Simon Willison
date_published: 2026-07-11
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: emerging
issue: "#1875"
---

# sqlite-utils 4.1: STRICT table transforms, --code rows, and Codex-driven backlog triage

> Simon Willison ships sqlite-utils 4.1, a dot-release four days after 4.0
> stable, with six minor features — two of them ("easiest ones" backlog
> triage) suggested by Codex, and the STRICT-table transform feature
> implemented same-day by GPT-5.6 Sol in response to a Hacker News post, then
> manually probed with a single targeted `uv run python -c` prompt that
> surfaced two real bugs, both fixed via an explicit red/green TDD cycle.

## Source Context

- **Type**: blog-post (Simon Willison's weblog "beat" release-announcement
  format — a GitHub release tag embedded with inline commentary — published
  2026-07-11; auto-discovered via trusted feed `simon-willison`. Unlike the
  4.0 stable post, this URL is the canonical article itself, not a short
  pointer to a separate page — the full commentary is embedded directly in
  the `beat-note blogmark-body` block at this URL.)
- **Author credibility**: Simon Willison is the creator and maintainer of
  sqlite-utils (this is release #125+ of the project, per the prior
  124th-release note in `blog-simonwillison-sqlite-utils-40-stable.md`), and
  the same first-party practitioner voice as the three existing sqlite-utils
  notes in this corpus. No vendor affiliation with OpenAI or Anthropic — he
  names and uses both a Claude-family and a GPT-family model in this single
  post.
- **Scope**: Covers six minor features shipped in the 4.1 dot-release
  (`--code` row generation, `--type` column overrides, `drop-index`, stdin
  SQL queries, upsert primary-key inference, STRICT-mode transform toggle),
  their individual provenance (issue number, HN discussion, or Codex
  backlog-triage suggestion), and one detailed AI-testing anecdote (STRICT
  mode implementation, manual bug-hunting prompt, two bugs found and fixed).
  Does NOT cover: the 4.0 stable release itself (see
  `blog-simonwillison-sqlite-utils-40-stable.md`), any cost/pricing data for
  this release cycle (unlike `blog-simonwillison-sqlite-utils-40rc2.md`,
  this post includes no AgentsView cost breakdown), or the `--code`/`--type`
  features' own implementation process (the post only documents the STRICT
  feature's implementation and testing in detail).

## Extracted Claims

### Claim 1: sqlite-utils 4.1 is the first dot-release after 4.0 stable, shipped four days later, bundling six minor features rather than a single headline feature
- **Evidence**: Author's direct opening statement; release cadence
  independently verifiable against `blog-simonwillison-sqlite-utils-40-stable.md`
  (4.0 stable published 2026-07-07; this post published 2026-07-11).
- **Confidence**: settled (first-party, dated, verifiable release cadence)
- **Quote**: "The first dot-release since 4.0 a few days ago, introducing a number of minor new features."
- **Our assessment**: Establishes this as routine maintenance-cadence work
  rather than a major feature push — useful context for interpreting the
  scale of the AI-assisted testing episode in Claims 7–10: even a small,
  four-day-turnaround dot-release included a manual AI-driven bug hunt that
  found two real defects, not just a rubber-stamped feature merge.

### Claim 2: The `--code` option for `insert`/`upsert` generalizes an existing "pass a Python code block as a CLI argument" pattern (already used by `sqlite-utils convert`) into full row-generation via a `rows()` function
- **Evidence**: Author's direct feature description plus a working example
  contrasting the existing `convert` pattern with the new `insert --code`
  usage.
- **Confidence**: settled (shipped, linked to issue #684)
- **Quote**: "sqlite-utils insert and sqlite-utils upsert now accept a --code option for providing a block of Python code (or a path to a .py file) that defines a rows() function or rows iterable of rows to insert, as an alternative to importing from a file. (#684)"
- **Quote (design rationale, verbatim including the source's own wording)**: "Allowing blocks of code to generate new rows directly was on obvious extension of that pattern:"
- **Our assessment**: Not an AI-development-process claim on its own, but a
  concrete example of API surface growing by generalizing an existing
  convention (inline Python in a CLI flag) rather than inventing a new one —
  relevant if the guide documents CLI design patterns for tools meant to be
  driven by agents composing shell commands.

### Claim 3: The new `--type column-name type` override for `insert`/`upsert` addresses a long-standing feature request (issue #131) for preserving leading zeros in CSV/TSV columns such as ZIP codes, and Willison describes the fix as turning out to be simple
- **Evidence**: Author's direct feature description and follow-up remark.
- **Confidence**: settled (shipped, linked to issue #131)
- **Quote**: "sqlite-utils insert and sqlite-utils upsert now accept --type column-name type to override the type automatically chosen when the table is created. This is useful for CSV or TSV columns such as ZIP codes that look like integers but should be stored as TEXT to preserve leading zeros. (#131)"
- **Quote (follow-up)**: "A long-standing feature request which turned out to be a simple implementation."
- **Our assessment**: This directly resolves the specific data-loss risk
  flagged as a hypothetical in this corpus's own earlier assessment of
  sqlite-utils' CSV/TSV auto-type-detection (see Cross-References →
  Extends) — the exact "ZIP codes... ID with leading zeros" scenario now has
  an explicit, documented escape hatch rather than requiring users to
  pre-declare schema or post-process the column.

### Claim 4: Two further small features — dropping an index by name and reading SQL queries from stdin — shipped as independent, separately-numbered issue resolutions in the same release
- **Evidence**: Author's direct feature descriptions, each linked to its own
  issue number.
- **Confidence**: settled (shipped, linked to issues #626 and #765)
- **Quote**: "New table.drop_index(name) method and sqlite-utils drop-index command for dropping an index by name. Both accept ignore=True/--ignore to ignore a missing index. (#626)"
- **Quote (stdin queries)**: "sqlite-utils query can now read the SQL query from standard input by passing - in place of the query, for example echo \"select * from dogs\" | sqlite-utils query dogs.db -. (#765)"
- **Our assessment**: Routine CLI ergonomics work; included for completeness
  of the release's feature inventory but not itself an AI-process claim.

### Claim 5: Willison had Codex review the full open issue/PR backlog and highlight the easiest items to implement, which directly produced the upsert primary-key-inference feature shipped in this release
- **Evidence**: Author's direct statement of the triage prompt's outcome,
  immediately followed by the resulting feature and a second remark crediting
  the same source.
- **Confidence**: emerging (single, specific, first-party account of an
  agent's backlog-triage recommendation being accepted and shipped; extends
  a similar but distinct pattern already in the corpus — see
  Cross-References)
- **Quote**: "Two more small features. I had Codex review all open issues and highlight the easiest ones!"
- **Quote (feature)**: "sqlite-utils upsert can now infer the primary key of an existing table, so --pk can be omitted when upserting into a table that already has a primary key."
- **Quote (attribution)**: "Another Codex suggestion, an obvious missing CLI feature from a Python library improvement that shipped in the 4.0 release."
- **Our assessment**: This is a second, distinct instance of agent-driven
  backlog triage shaping release scope (see Cross-References → Extends), but
  a different triage criterion than the 4.0 stable release's instance: there
  the agent was asked to find breaking-change-timing candidates for a major
  version; here it was asked to find low-effort, easy-win items for a minor
  dot-release. Together the two episodes show this practitioner uses agent
  backlog triage repeatedly, with the triage question itself tailored to the
  release type (major vs. dot-release).

### Claim 6: The STRICT-mode transform toggle was directly inspired by a same-day Hacker News-trending blog post (Evan Hahn's "Prefer STRICT tables in SQLite"), which identified that SQLite's `ALTER TABLE` cannot convert an existing table to strict mode — a gap Willison recognized sqlite-utils' existing `transform` (copy-and-rebuild) mechanism could fill
- **Evidence**: Author's direct account naming the external source and
  quoting Evan Hahn's specific technical observation, followed by his own
  causal reasoning for why `transform` was the right existing mechanism to
  extend.
- **Confidence**: settled (dated, externally linked, independently
  verifiable trigger — the HN thread, Evan Hahn's post, and the shipped
  issue #787 all exist and are linked from the post)
- **Quote**: "These two were inspired by Prefer STRICT tables in SQLite by Evan Hahn, which did the rounds on Hacker News today. Evan pointed out that:"
- **Quote (Evan Hahn, as quoted in the post)**: "Unfortunately, I don't think there's a way to ALTER a table to make it strict. I think you have to copy the data out of the non-strict table into the strict one."
- **Quote (Willison's synthesis)**: "That's exactly what the sqlite-utils transform mechanism does, so I extended it to add the ability to switch tables from strict to non-strict and vice-versa."
- **Our assessment**: This is a same-day external-trigger-to-shipped-feature
  cycle — a third-party blog post trending on Hacker News, read, mapped onto
  an existing internal mechanism, and implemented and released the same day.
  Distinct from both of this release's other feature sources (issue-tracker
  requests in Claims 2–4, agent backlog triage in Claim 5): here the
  practitioner's own domain knowledge ("I already have a mechanism for
  this") was the key ingredient, with the external post supplying the
  motivating problem statement and market signal (HN traction) rather than
  the solution.

### Claim 7: Willison names the exact model and tool combination used to implement the STRICT-mode feature as "GPT-5.6 Sol xhigh Codex," and links its full session transcript — the corpus's first documented real coding-task usage of GPT-5.6 Sol, as opposed to vendor benchmark or pricing coverage
- **Evidence**: Author's direct statement plus a linked, publicly fetchable
  GitHub Gist transcript (`gist.github.com/simonw/ab8256b81646ad967a601975e206de64`,
  fetched directly for this note) recording the full multi-turn session,
  including the exact prompts used and the model's file-by-file
  implementation work.
- **Confidence**: emerging (a single, specific, first-party account, but
  independently verified via the fetched transcript rather than taken on
  faith)
- **Quote**: "Here's the GPT-5.6 Sol xhigh Codex transcript I used to implement those new strict table features. One of the most useful prompts I ran was this one:"
- **Our assessment**: This is a concrete follow-up data point to Willison's
  own earlier, more general early-access impression of GPT-5.6 Sol (see
  Cross-References — "definitely very competent... hasn't struck me as
  better than Fable") — here the model is put through an actual, complete,
  shipped feature-implementation task rather than informal comparison, with
  a fetchable transcript rather than a summary judgment. "xhigh" reasoning
  effort matches the terminology used for GPT-5.5 via Codex Desktop in
  `blog-simonwillison-sqlite-utils-40-stable.md` Claim 10, suggesting
  Willison applies a consistent reasoning-effort-tier vocabulary across
  successive OpenAI model generations.

### Claim 8: Willison's single most useful prompt for this release was a narrow, targeted instruction to manually exercise one specific new option via `uv run python -c`, explicitly framed as testing outside of the automated tests the model had already written for that feature
- **Evidence**: Author's direct statement identifying this as his most
  useful prompt, reproduced verbatim, immediately followed by his own
  generalization of why it worked and what it found.
- **Confidence**: emerging (a specific, reusable, single-feature-scoped
  testing prompt, with a concrete before/after result — two bugs found,
  detailed in Claim 9)
- **Quote**: "use uv run python -c and manually exercise the new .transform(strict=) option, see if you can find any edge-cases or bugs"
- **Quote (Willison's generalization)**: "Effectively telling the model to manually test its work, outside of the automated tests it had already written. This turned up two minor issues that we then fixed."
- **Our assessment**: This narrows and specializes the two-part release-audit
  prompt already documented in this corpus (see Cross-References → Extends)
  from "write and save scratch scripts exercising every new feature in the
  whole release, as a separate pre-release audit pass" to "immediately after
  implementing one specific option, manually poke at just that option with
  ad hoc one-liner Python, before moving on." The two patterns operate at
  different scopes (whole-release audit vs. single-feature spot-check) and
  different timing (pre-release gate vs. inline during implementation) —
  useful as a lighter-weight, more frequently-applicable variant of the
  same underlying idea (have the model verify its own work manually, not
  just via the tests it wrote).

### Claim 9: The manual `python -c` probing found two concrete, distinct bugs in the new STRICT transform option — a silent no-op on unsupported SQLite versions (instead of an error) and a stale cached `strict` default on the `Table` object after a successful transform — alongside a documented list of edge cases that were checked and found *not* to be bugs
- **Evidence**: GPT-5.6 Sol's full bug report, posted as a PR comment on
  `simonw/sqlite-utils#788` and fetched directly via the GitHub API for this
  note (not reproduced in the blog post itself, which only says "turned up
  two minor issues").
- **Confidence**: settled (a concrete, independently fetched, verifiable
  primary-source report; both bugs were subsequently fixed with regression
  tests in the same PR — see Claim 10 and Concrete Artifacts)
- **Quote**: "Manual probing found two bugs directly relevant to the new option. 1. Explicit strict=True silently fails on unsupported SQLite ... create_table_sql() only appends STRICT when db.supports_strict is true (db.py). An explicit conversion should probably raise an informative error instead of succeeding as a no-op. 2. The Table object retains stale strict defaults ... The schema becomes non-strict, but t._defaults[\"strict\"] remains True. Dropping and recreating through the same object unexpectedly creates another strict table."
- **Our assessment**: Notable beyond just "found two bugs": the same report
  also explicitly lists roughly seven further edge cases it deliberately
  probed and confirmed were *not* broken (SQLite `ANY`-column introspection,
  incompatible column defaults, trigger-dropping during transform, `keep_table`
  retention, behavior inside an existing `db.atomic()` block, repeated
  strict/non-strict transitions) — see Concrete Artifacts. A manual
  exploratory testing pass that documents both what it broke *and* what it
  checked and found fine is a more complete audit trail than a bug list
  alone, and gives the maintainer confidence about the boundaries of what
  was actually tested rather than an unstated scope.

### Claim 10: Both bugs found by manual probing were fixed using an explicit red/green TDD cycle — a failing regression test reproducing the exact reported bug was written and confirmed to fail before the fix was implemented and the test (plus the broader transform suite) confirmed to pass
- **Evidence**: The Codex session transcript (fetched via the GitHub Gist
  API), which reports each fix using an explicit "TDD results: Red: ...
  Green: ..." structure for both the unsupported-SQLite-version bug and
  (per the same transcript, immediately prior) the stale-defaults bug.
- **Confidence**: emerging (single transcript's self-reported methodology,
  but explicit, structured, and independently readable in the raw
  transcript rather than inferred)
- **Quote**: "TDD results: - Red: both methods silently produced non-strict transformations. - Green: both unsupported-version tests passed. - Transform-related suite: 119 passed. - Generated-doc checks passed. - Sphinx build passed."
- **Our assessment**: This is a specific, reusable bug-fix methodology
  distinct from a direct patch: confirm the reported defect reproduces as a
  failing test first, then fix, then confirm both the targeted test and the
  full surrounding test suite are green. It closes the loop opened by
  Claim 8's manual-probing prompt — the manual, non-automated-test
  exploration that *found* the bugs fed back into new *automated* regression
  tests that lock in the fix, rather than the fix being verified only by
  re-running the same manual probe.

## Concrete Artifacts

### `--code` row-generation — CLI usage (from the post)

```
sqlite-utils convert content.db articles headline '
def convert(value):
    return value.upper()'

sqlite-utils insert data.db creatures --code '
def rows():
    yield {"id": 1, "name": "Cleo"}
    yield {"id": 2, "name": "Suna"}
' --pk id
```

*Source: Simon Willison, simonwillison.net/2026/Jul/11/sqlite-utils/*

### GPT-5.6 Sol's full STRICT-mode bug report (verbatim, from PR comment `simonw/sqlite-utils#788#issuecomment-4948473657`, fetched via GitHub API — not reproduced in the blog post itself)

```
> use `uv run python -c` and manually exercise the new `.transform(strict=`) option, see if you can find any edge-cases or bugs

GPT-5.6 Sol then found some edge-cases:

> Manual probing found two bugs directly relevant to the new option.
>
> 1. Explicit `strict=True` silently fails on unsupported SQLite
>
> Simulating an older SQLite version produced:
>
> t.transform(strict=True)
> t.strict  # False
>
> `create_table_sql()` only appends `STRICT` when `db.supports_strict` is
> true (db.py:1554). An explicit conversion should probably raise an
> informative error instead of succeeding as a no-op.
>
> 2. The `Table` object retains stale strict defaults
>
> After:
>
> t = db.table("items", strict=True)
> t.create({"id": int})
> t.transform(strict=False)
>
> The schema becomes non-strict, but `t._defaults["strict"]` remains `True`.
> Dropping and recreating through the same object unexpectedly creates
> another strict table. The reverse happens when converting from non-strict
> to strict.
>
> The default should be updated after a successful transformation,
> including storing `False`. It should remain unchanged if the
> transformation rolls back.
>
> Other notable edge cases:
>
> - SQLite `ANY` columns are introspected as `float`, so transforming a
>   native strict table containing `ANY` can fail or change it to `REAL`.
>   This is an existing transform/introspection limitation, but applies to
>   `strict=None` and `strict=True`.
> - An incompatible declared default does not prevent conversion. An empty
>   `INTEGER DEFAULT 'not-an-integer'` table becomes strict successfully,
>   but later inserting the default raises `IntegrityError`. This is SQLite
>   behavior.
> - Triggers are dropped during transformation. This is existing documented
>   behavior, not introduced by this change.
> - Losslessly convertible values work: `"123"` and `"123.0"` become
>   integer `123`.
> - Fractional numbers, incompatible text, and BLOBs correctly fail and
>   roll back.
> - Indexes and foreign keys were preserved.
> - Failed conversion inside an existing `db.atomic()` transaction rolled
>   back only the transform; the outer transaction remained usable.
> - `keep_table` correctly retained the original non-strict table alongside
>   the new strict table.
> - Repeated `None → True → None → False → None` transitions behaved
>   correctly.
>
> No files were changed during this diagnostic pass.
```

*Source: GPT-5.6 Sol (via Codex, xhigh reasoning), posted by Simon Willison
as a PR comment, `github.com/simonw/sqlite-utils/pull/788#issuecomment-4948473657`,
fetched via `api.github.com/repos/simonw/sqlite-utils/pulls/788` for this
note. Code fragments de-indented from the original markdown blockquote for
readability; wording otherwise verbatim.*

### Red/green TDD fix report for the unsupported-SQLite-version bug (verbatim, from the fetched Codex transcript)

```
Implemented the unsupported-SQLite guard.

`transform(strict=True)` and `transform_sql(strict=True)` now raise:

TransformError("SQLite does not support STRICT tables")

when `db.supports_strict` is false. The shared guard is in db.py:2634.

TDD results:

- Red: both methods silently produced non-strict transformations.
- Green: both unsupported-version tests passed.
- Transform-related suite: 119 passed.
- Generated-doc checks passed.
- Sphinx build passed.
```

*Source: GPT-5.6 Sol session transcript, `gist.github.com/simonw/ab8256b81646ad967a601975e206de64`
(raw file `codex.md`), fetched via `gist.githubusercontent.com` for this
note.*

### Willison's own follow-up directive after receiving the bug report (verbatim, from PR `simonw/sqlite-utils#788` comments)

```
I'm going to raise errors if you attempt to convert to STRICT with a SQLite
version that fails the `db.supports_strict` test.
```

*Source: Simon Willison, `github.com/simonw/sqlite-utils/pull/788#issuecomment-4948479356`,
fetched via GitHub API for this note.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt56-sol-launch.md` Claim 1 ("OpenAI previewed a
    three-tier GPT-5.6 series — Sol (flagship), Terra (balanced/everyday),
    and Luna (fast/affordable)"): confirms the identity and tier of the
    model named in this post ("GPT-5.6 Sol"), corroborating that Willison is
    using the flagship tier for this coding task, not a lower-cost tier.
  - `blog-simonwillison-sqlite-utils-40-stable.md` Claim 4 (agent backlog
    triage recommended shipping compound foreign keys as a breaking change
    in the 4.0 release): this source's Claim 5 is a second, distinct
    instance of the same practitioner using agent backlog triage to shape
    release scope, four days later, for a different release type — see
    Extends below for how the triage criterion itself differs.

- **Contradicts**: None identified. No existing corpus note makes a claim
  this source conflicts with. No contradiction issue required per MINER.md
  §4a.

- **Extends**:
  - `blog-simonwillison-sqlite-utils-40rc1.md` Claim 7 (CSV/TSV type
    detection risks silently mis-typing columns like ZIP codes, losing
    leading zeros — flagged in that note's "Our assessment" as "a data loss
    risk for AI pipelines where falsy values are meaningful"): this source's
    Claim 3 documents the shipped fix — an explicit `--type column-name type`
    override — that directly closes the exact ZIP-code scenario that note's
    assessment raised as an open risk.
  - `blog-simonwillison-sqlite-utils-40-stable.md` Claim 4 (agent-driven
    backlog triage for breaking-change timing) and Claim 9 (the two-part
    "review the diff since the last stable tag + write and save scratch
    scripts exercising every new v4 feature" pre-release audit prompt):
    this source's Claim 5 extends the backlog-triage pattern with a second,
    differently-scoped instance (routine "easiest wins" triage for a
    dot-release, vs. breaking-change-timing triage for a major version).
    This source's Claim 8 extends the scratch-script audit prompt with a
    narrower, single-feature, inline variant (one `python -c` one-liner
    against one just-implemented option, not a saved multi-script
    whole-release audit pass) — see that Claim's "Our assessment" for the
    scope/timing distinction.
  - `blog-simonwillison-gpt56-ga-launch.md` Claim 7 (Willison's early-access
    verdict: GPT-5.6 Sol is "definitely very competent" but "hasn't struck
    me as better than Fable at the kind of complex coding tasks" he uses
    day to day): this source's Claim 7 is a concrete, dated (2026-07-11, two
    days after the 2026-07-09 GA note) follow-up data point — an actual
    shipped feature GPT-5.6 Sol implemented end-to-end, with a fetchable
    transcript, rather than an informal comparative impression. It doesn't
    resolve the earlier claim's Fable-vs-Sol comparison (no side-by-side is
    run here), but it does substantiate that the "definitely very
    competent" verdict extends to real, non-trivial, shipped library work.

- **Novel**:
  - **First in-corpus real coding-task usage of GPT-5.6 Sol**, as opposed to
    vendor benchmark/pricing coverage (`blog-simonwillison-gpt56-sol-launch.md`,
    `blog-simonwillison-gpt56-ga-launch.md`) or informal comparative
    impressions (`blog-simonwillison-gpt56-ga-launch.md` Claim 7) — this is
    a complete, shipped, transcript-verified feature implementation.
  - **First in-corpus documented case of an external, non-AI source (a
    third-party blog post trending on Hacker News) directly triggering a
    same-day feature implementation cycle** (Claim 6): distinct from
    issue-tracker-sourced features (Claims 2–4) and agent-suggested features
    (Claim 5) — here the practitioner's own recognition of an existing
    internal mechanism as the solution was the key step, not an agent's
    suggestion or a queued issue.
  - **First in-corpus example of a coding agent explicitly self-reporting a
    red/green TDD cycle as its bug-fix methodology** (Claim 10): distinct
    from the fan-out-then-self-verify review methodology in
    `blog-simonwillison-sqlite-utils-40-stable.md` Claim 11 (parallel review
    subagents, then self-re-verification before reporting) — this is a
    single-agent, single-session, explicit test-first fix workflow applied
    immediately after a bug is found, not a separate review pass.
  - **First in-corpus example of a bug-hunting report that documents a
    "checked and confirmed fine" list alongside its bug list** (Claim 9,
    Concrete Artifacts): most AI-review reports in this corpus (e.g. Fable's
    10-bug report in `blog-simonwillison-sqlite-utils-40-stable.md` Claim 11)
    report only what was found broken; this report also explicitly lists
    seven specific behaviors it verified were correct, giving the maintainer
    visibility into the actual scope of what was tested.

## Guide Impact

- **Chapter 03 (Patterns & Practices) — single-feature manual spot-check
  prompt**: Add Claim 8's exact prompt ("use `uv run python -c` and manually
  exercise the new [feature], see if you can find any edge-cases or bugs")
  as a lightweight, inline variant of the whole-release scratch-script audit
  already documented from `blog-simonwillison-sqlite-utils-40-stable.md`
  Claim 9. Recommend it as a fast, low-ceremony check to run immediately
  after implementing a single new option or feature, distinct from (and not
  a substitute for) a full pre-release audit — cite Claim 9's concrete
  before/after result (two real bugs found from one targeted prompt).

- **Chapter 03 (Patterns & Practices) — bug-fix verification methodology**:
  Add Claim 10's explicit red/green TDD reporting pattern (write a failing
  regression test that reproduces the exact reported bug, confirm it fails,
  implement the fix, confirm the specific test and the broader suite pass)
  as a concrete methodology for turning a manually-found bug into a durable
  regression test, distinct from a one-line patch with no new coverage.

- **Chapter 02 (Harness Engineering) — release-scope backlog triage**: Add
  Claim 5 as a second data point alongside
  `blog-simonwillison-sqlite-utils-40-stable.md` Claim 4 for using an agent
  to triage an open issue/PR backlog for release-planning purposes — note
  that the triage *question* should be tailored to the release type
  ("what's a breaking change we should ship now" for majors vs. "what are
  the easiest wins" for dot-releases), not a single fixed prompt reused
  regardless of release type.

- **Chapter 04 (Model Judgement / Capability Arcs)**: If the guide tracks
  GPT-5.6 Sol as a distinct capability data point, cite Claim 7 as the
  corpus's first real (non-benchmark) coding-task usage, and pair it with
  `blog-simonwillison-gpt56-ga-launch.md` Claim 7's earlier informal verdict
  — together they show a practitioner's day-to-day usage moving from
  "tried it informally, seemed competent" to "used it to implement and ship
  a real feature" within two days of GA.

## Extraction Notes

- **Canonical URL**: Unlike `blog-simonwillison-sqlite-utils-40-stable.md`
  (where the issue's URL was a short pointer post linking to a separate
  canonical article), this issue's URL
  (`simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything`) resolves
  directly to the full article — the entire commentary is embedded in the
  page's `entry entryPage` / `beat-note blogmark-body` block at this URL.
  Confirmed via direct `curl` fetch (not WebFetch, per the verbatim-quote
  requirement in MINER.md §2a — WebFetch's summarizing pass returned only a
  paraphrase on first request, consistent with the same limitation noted in
  prior Willison source notes in this corpus).
- **Sub-pages followed** (per MINER.md §1): fetched the linked GitHub Gist
  transcript (`gist.github.com/simonw/ab8256b81646ad967a601975e206de64`,
  843KB raw markdown, via the GitHub Gist API) in full, and the linked pull
  request `simonw/sqlite-utils#788` and its comments (via the GitHub API) to
  get GPT-5.6 Sol's full bug report and Willison's follow-up directive
  verbatim, since the blog post itself only summarizes ("turned up two minor
  issues that we then fixed") rather than reproducing them. Did not follow
  the individual linked GitHub issues (#684, #131, #626, #765, #787) or
  Evan Hahn's full external blog post, since the post's own blockquotes
  already reproduce the load-bearing text for each (issue descriptions
  verbatim from the changelog; Evan Hahn's quote reproduced in full by
  Willison). Did not follow the linked commit
  (`github.com/SAY-5/sqlite-utils/commit/d2ac3765...`) for the `--type`
  feature, as the post's own description of that feature was sufficient for
  Claim 3.
- **Transcript scope**: The fetched Gist transcript spans multiple sessions
  across this and a prior task (it opens with an unrelated "Explain
  create-table strict" exchange), consistent with Willison reusing a single
  long-running Codex conversation across several related prompts over time.
  This note extracts only the portions relevant to the STRICT-transform
  feature's implementation, the manual-testing prompt, the resulting bug
  report, and the TDD fix cycle — the transcript's earlier exploratory
  content (explaining existing behavior, unrelated file reads) was read but
  not separately extracted as it does not contain claims distinct from what
  the post itself summarizes.
- **Cross-reference verification** (per MINER.md §4b): all claim citations
  above were checked against the actual numbered `### Claim:` headings in
  the cited notes before writing:
  - `blog-simonwillison-gpt56-sol-launch.md` Claim 1 verified at lines 43–57
    of that note (heading "Claim 1: OpenAI previewed a three-tier GPT-5.6
    series — Sol (flagship), Terra (balanced/everyday), and Luna
    (fast/affordable)").
  - `blog-simonwillison-sqlite-utils-40-stable.md` Claim 4 verified at lines
    72–76 of that note (heading "Claim 4: Compound foreign key support was
    added to 4.0 because a coding agent, asked to review all open issues and
    PRs for anything that should ship as a breaking change now rather than
    later, correctly identified compound foreign keys as exactly that kind
    of feature").
  - `blog-simonwillison-sqlite-utils-40-stable.md` Claim 9 verified at lines
    103–107 of that note (heading "Claim 9: Willison's most successful
    prompt for pre-release review was a two-part instruction...").
  - `blog-simonwillison-sqlite-utils-40-stable.md` Claim 11 verified at
    lines 116–120 of that note (heading "Claim 11: Fable 5's review found
    two silent-data-loss bugs in the new transaction model...").
  - `blog-simonwillison-sqlite-utils-40rc1.md` Claim 7 verified at lines
    126–138 of that note (heading "Claim 7: Type detection is now on by
    default for CSV/TSV imports in v4...", with the ZIP-codes/leading-zeros
    risk stated in that claim's "Our assessment").
  - `blog-simonwillison-gpt56-ga-launch.md` Claim 7 verified at lines
    164–180 of that note (heading "Claim 7: Willison's own early-access
    testing found GPT-5.6 Sol \"definitely very competent\" but not better
    than Claude Fable 5 on the complex coding tasks he uses day to day").
- **No contradictions filed**: No existing corpus source makes a claim in
  conflict with this source's content. No contradiction issue required per
  MINER.md §4a.
