---
source_url: https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/
source_type: blog-post
title: "sqlite-utils 4.0rc1 adds migrations and nested transactions"
author: Simon Willison
date_published: 2026-06-21
date_extracted: 2026-06-28
last_checked: 2026-06-28
status: current
confidence_overall: emerging
issue: "#1338"
---

# sqlite-utils 4.0rc1 adds migrations and nested transactions

> Simon Willison announces sqlite-utils 4.0rc1, adding a migration system
> ported from his battle-tested `sqlite-migrate` package (already running in
> the `llm` CLI for several years) and a `db.atomic()` context manager over
> SQLite savepoints for reliable nested transactions — along with a set of
> backwards-incompatible changes documenting the library's maturation toward a v4
> stable release.

## Source Context

- **Type**: blog-post (release announcement and feature walkthrough; Simon
  Willison's weblog, published 2026-06-21; auto-discovered via trusted feed
  `simon-willison`. The post covers the two major new features — migrations and
  `db.atomic()` — with working code examples, installation instructions, and a
  summary of backwards-incompatible changes from prior alphas 4.0a0 and 4.0a1.)
- **Author credibility**: Simon Willison is the creator of sqlite-utils, Datasette,
  and the `llm` Python CLI. sqlite-utils is foundational to the Datasette
  ecosystem and serves as the persistence layer for the `llm` CLI. This is
  first-party release documentation from the library's maintainer. No vendor
  affiliation.
- **Scope**: Covers sqlite-utils 4.0rc1's two major new features (migrations and
  `db.atomic()`), backwards-incompatible changes from 4.0a0 and 4.0a1, and
  additional incremental improvements. Does NOT cover: the full sqlite-utils API
  surface, performance benchmarks, Datasette integration details, or the internal
  implementation of the migration system's schema tracking.

## Extracted Claims

### Claim 1: sqlite-utils 4.0rc1 adds a database migrations system ported from the `sqlite-migrate` package, which has been used by the `llm` CLI and other projects for several years

- **Evidence**: Author's direct statement with named provenance (`sqlite-migrate`
  package, verifiable on GitHub) and a named production user (`llm`). The `llm`
  CLI's use of sqlite-utils for persistence is independently corroborated by
  `blog-simonwillison-llm032a0.md` Claim 5.
- **Confidence**: settled (first-party; the migration system's origin and track
  record are stated explicitly by the maintainer)
- **Quote**: "The first is support for **database migrations**. This isn't a completely new implementation—it's a slightly modified port of the [sqlite-migrate](https://github.com/simonw/sqlite-migrate) package I released a few years ago."
- **Quote (track record)**: "Its predecessor has been used by [LLM](https://llm.datasette.io/) and various other projects for several years, so I'm confident that the design is stable and works well."
- **Our assessment**: The migration system's provenance is significant: this is not
  new code introduced speculatively, but a design already exercised in production
  in the `llm` CLI (which stores conversation history, log data, and plugin
  configuration in SQLite). For AI-native applications that use SQLite as their
  data layer — increasingly common given SQLite's zero-infrastructure footprint —
  having a migration system in the primary Python library closes a gap that
  previously required adding an external package. The `sqlite-migrate` battle test
  in a production tool is a stronger provenance signal than a freshly written
  migration system would be.

### Claim 2: The migrations system intentionally omits reverse migrations — mistakes must be fixed by deploying fresh forward migrations

- **Evidence**: Author's direct statement of design philosophy.
- **Confidence**: settled (first-party design decision, stated as deliberate)
- **Quote**: "The system is deliberately small: it doesn't provide reverse migrations, so any mistakes you make should be fixed by deploying a fresh migration to undo them."
- **Our assessment**: This is a deliberate trade-off for simplicity. Reverse
  migrations (down migrations) add significant complexity — they require maintaining
  bidirectional schema transforms, handling data migrations in both directions, and
  are often skipped in practice because production databases rarely roll back at
  the schema level. For AI-native applications where schema iteration speed matters
  more than rollback fidelity, a forward-only migration system is appropriate.
  Practitioners should plan "undo" as another forward migration, not a one-click
  rollback.

### Claim 3: `db.atomic()` provides a context manager abstraction over SQLite savepoints for nested transactions, borrowing terminology from Django and Peewee

- **Evidence**: Author's direct statement with working code example and explicit
  acknowledgment of the borrowed terminology from Django and Peewee.
- **Confidence**: settled (first-party; the SQLite savepoint mechanism is
  well-documented; the API design is stated explicitly)
- **Quote**: "SQLite supports nested transactions in the form of savepoints, so I wanted an abstraction that could make those as easy to use as possible."
- **Our assessment**: SQLite savepoints have always existed but are underused
  because they require raw SQL (`SAVEPOINT name`, `RELEASE name`,
  `ROLLBACK TO name`). The `db.atomic()` context manager makes nested savepoints
  as natural as Django's `with transaction.atomic()`. For AI pipelines executing
  sequential write operations where partial failure should roll back a subset
  without rolling back everything, this is the missing primitive. A multi-step
  LLM output processing pipeline can use nested `db.atomic()` blocks to checkpoint
  intermediate results with fine-grained rollback.

### Claim 4: Version 4 requires SQLite 3.23.1 or newer for upsert operations, which now use `INSERT ... ON CONFLICT SET` syntax; `use_old_upsert=True` is available for legacy behavior

- **Evidence**: Stated as a backwards-incompatible change from the 4.0a0 alpha.
- **Confidence**: settled (first-party; stated directly; SQLite 3.23.1 was released
  August 2018 — requirement is reasonable for most production environments)
- **Quote**: (no direct quote; described as backwards-incompatible change from 4.0a0)
- **Our assessment**: SQLite 3.23.1 is old enough that most production systems
  should have it, but practitioners on embedded systems, older Linux distributions,
  or specific Python environments should verify before upgrading. The
  `use_old_upsert=True` parameter provides a migration path for code that cannot
  immediately adopt the new syntax.

### Claim 5: Python 3.8 support is dropped and Python 3.13 is added in sqlite-utils v4; `sqlite-utils tui` is split into a separate `sqlite-utils-tui` plugin

- **Evidence**: Stated as backwards-incompatible changes from the 4.0a0 alpha.
- **Confidence**: settled (first-party; stated directly)
- **Quote**: (no direct quote; described as backwards-incompatible changes from 4.0a0)
- **Our assessment**: Python 3.8 reached end-of-life in October 2024; dropping it
  in 2026 is expected. Splitting the TUI into a plugin follows the Datasette
  ecosystem pattern of keeping the core package minimal. Practitioners who use the
  TUI interface will need a separate `pip install sqlite-utils-tui`.

### Claim 6: `db.table()` in v4 now only accesses database tables; SQL views require `db.view()`; floating-point columns default to `REAL` instead of `FLOAT`; identifiers use double-quotes instead of square brackets

- **Evidence**: Stated as backwards-incompatible changes from the 4.0a1 alpha.
- **Confidence**: settled (first-party; stated directly)
- **Quote**: (no direct quote; described as backwards-incompatible changes from 4.0a1)
- **Our assessment**: The `db.table()` / `db.view()` split clarifies the API at
  the call site but breaks any code that accessed views via `db.table()`. The
  `REAL` vs `FLOAT` change normalizes to SQLite's native type affinity string.
  The double-quotes change brings sqlite-utils into alignment with ISO SQL
  standards — but breaks any code that parses the generated SQL strings.

### Claim 7: Type detection is now on by default for CSV/TSV imports in v4; `table.convert()` no longer skips False-evaluating values; `insert_all()` and `upsert_all()` now accept iterators of lists or tuples

- **Evidence**: Stated as backwards-incompatible changes from the 4.0a1 alpha.
- **Confidence**: settled (first-party; stated directly)
- **Quote**: (no direct quote; described as backwards-incompatible changes from 4.0a1)
- **Our assessment**: Auto-detecting types from CSV data is convenient but can
  misdetect columns that should remain as strings (ZIP codes, phone numbers, IDs
  with leading zeros). The `convert()` fix is a correctness change — previously,
  rows with `None`, `0`, `""`, or `False` values were silently skipped during
  conversion, which was a data loss risk for AI pipelines where falsy values are
  meaningful (e.g., a zero score is not "no score"). Accepting lists/tuples in
  `insert_all()` / `upsert_all()` removes a conversion step for pipelines that
  receive array-structured data from APIs.

## Concrete Artifacts

### Migrations System — Python API (from the post)

```python
from sqlite_utils import Database, Migrations

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
```

*Source: Simon Willison, simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/*
*Usage: `db = Database("creatures.db"); migrations.apply(db)` in Python, or
`sqlite-utils migrate creatures.db migrations.py` from the CLI.*

### db.atomic() Nested Transactions — Code Example (from the post)

```python
with db.atomic():
    db.table("dogs").insert({"id": 1, "name": "Cleo"}, pk="id")
    try:
        with db.atomic():
            db.table("dogs").insert({"id": 2, "name": "Pancakes"})
            raise ValueError("skip this one")
    except ValueError:
        pass
    db.table("dogs").insert({"id": 3, "name": "Marnie"})
```

*Source: Simon Willison, simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/*
*Result: rows 1 (Cleo) and 3 (Marnie) are inserted; row 2 (Pancakes) is rolled
back via savepoint. The outer transaction commits successfully. Terminology
borrowed from Django and Peewee.*

### Installation (from the post)

```bash
pip install sqlite-utils==4.0rc1

# or via uvx:
uvx --with sqlite-utils==4.0rc1 sqlite-utils --help
```

*Source: Simon Willison, simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/*

### Backwards-Incompatible Changes Summary

```
From 4.0a0:
  - Upsert syntax: now uses INSERT ... ON CONFLICT SET (requires SQLite 3.23.1+)
    Legacy behavior available via: use_old_upsert=True parameter
  - Python support: 3.8 dropped; 3.13 added
  - sqlite-utils tui: moved to separate sqlite-utils-tui plugin

From 4.0a1:
  - db.table(): now tables only; use db.view() for SQL views
  - Float columns: default type is now REAL (was FLOAT)
  - table.convert(): no longer skips False-evaluating values (None, 0, '', False)
    --skip-false CLI flag removed
  - Identifier quoting: double-quotes instead of square brackets (ISO SQL standard)
  - CSV/TSV type detection: now on by default; use --no-detect-types to disable
  - insert_all() / upsert_all(): now accept iterator of lists or tuples
```

*Source: Simon Willison, simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/*
*(post summarizes alpha release notes for 4.0a0 and 4.0a1)*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm032a0.md` Claim 5: "The llm CLI tool worked around this
    through a custom mechanism for persisting and inflating conversations using SQLite,
    but that never became a stable part of the LLM API." This source confirms that
    sqlite-utils is the foundational library behind the `llm` CLI's SQLite storage.
    The migration system in sqlite-utils 4.0rc1 was derived from `sqlite-migrate`,
    which was first developed for exactly this use case. The two notes together show
    sqlite-utils and the `llm` CLI as tightly coupled tools in the AI-native data
    ecosystem, with the library's migration system directly benefiting the tool.

- **Extends**:
  - `blog-simonwillison-sqlite-column-provenance.md` overall: That note documents
    advanced SQLite column provenance techniques for Python data tools. This source
    adds the practitioner library (sqlite-utils) responsible for schema management
    and data insertion in those same AI-native data applications. The two notes
    describe complementary concerns: this note covers schema lifecycle (create,
    evolve via migrations, insert with nested-transaction safety), that note covers
    query result analysis (which output column came from which table).
  - `blog-simonwillison-sqlite-agents-md.md` overall: That note covers SQLite's
    AGENTS.md governance for the C codebase of the database engine itself. This
    source covers the Python practitioner library for *working with* SQLite databases.
    Together they establish the SQLite ecosystem as a recurring site for AI-native
    tooling: the database engine has explicit AI contribution governance; the Python
    library now has production schema migration and reliable nested transaction support
    for AI applications.
  - `blog-simonwillison-datasette-apps.md` Claim 11: "Datasette Apps represent a
    capability evolution arc: Datasette went from read-only data publishing →
    agent-readable SQL → agent-writable SQL → user app-hosting, with each step
    driven by AI capability expansion." sqlite-utils v4's migration system and nested
    transactions directly underpin this evolution — schema management for iterating
    AI-driven applications and reliable write atomicity for agent-writable operations
    (datasette-agent 0.3a0's write SQL capability runs on the same sqlite-utils
    layer). The library is the data foundation beneath all of Datasette's
    capabilities.

- **Contradicts**: None identified. No existing corpus note makes claims about
  SQLite migration systems, nested transaction APIs for Python, or sqlite-utils
  that conflict with this source's claims. No contradiction issue required.

- **Novel**:
  - **First in-corpus documentation of a SQLite migration system designed for
    AI-native Python applications**: The migrations system ported from `sqlite-migrate`
    and tested in `llm` and other projects is not documented in any prior source note.
    For practitioners building AI applications on SQLite, this is the first
    corpus-documented migration approach for that environment.
  - **First in-corpus documentation of `db.atomic()` as a nested transaction primitive
    for LLM pipelines**: The context manager wrapping SQLite savepoints for reliable
    partial rollback is not documented elsewhere in the corpus. This pattern enables
    multi-step agentic write pipelines with checkpointed failure handling.
  - **sqlite-utils v4 backwards-incompatible changes as a library maturation signal**:
    The collection of breaking changes (upsert syntax, Python versions, identifier
    quoting, type defaults) documents a library moving from pragmatic-first to
    standards-aligned. This maturation has direct upgrade-planning implications for
    any AI-native project that depends on sqlite-utils.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add sqlite-utils migrations as the recommended
  schema management approach for AI harnesses that use SQLite as their data layer.
  The forward-only migration philosophy (no reverse migrations, fix by deploying a
  new forward migration) matches AI application iteration cadence. The
  `sqlite-migrate`-derived system's track record in the `llm` CLI is the strongest
  available credibility signal. Cite Claims 1–2 and the migrations code example.

- **Chapter 02 (Harness Engineering)**: Add `db.atomic()` as the primitive for
  checkpointed writes in multi-step agentic data pipelines. An agent that writes N
  rows in sequence, where some subset may fail, can use nested `db.atomic()` blocks
  to roll back failed subsets without aborting the outer transaction. This is the
  correct pattern for AI data pipelines processing batches where partial failure
  should not undo prior successful steps. Cite Claim 3 and the `db.atomic()` code
  example. Note the v4 upgrade requirements alongside any recommendation to adopt
  sqlite-utils (Concrete Artifacts → backwards-incompatible changes summary).

- **Chapter 01 (Daily Workflows)**: If the guide covers the `llm` CLI toolchain,
  add a note that sqlite-utils is the underlying data layer for `llm`'s SQLite
  persistence, and that the v4 migration system was derived from `sqlite-migrate`
  which was first developed for `llm`. The two tools are tightly coupled: any
  team using `llm` in their AI-native workflow will eventually follow sqlite-utils v4.
  Pair with `blog-simonwillison-llm032a0.md` Claim 5 for the storage architecture
  context.

## Extraction Notes

- **Source URL**: The issue URL (`simonwillison.net/2026/Jun/21/sqlite-utils/
  #atom-everything`) resolves to a beat/index entry on the blog that links to
  the actual article at `simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/`. This
  note uses the canonical article URL. The `#atom-everything` fragment is an Atom
  feed anchor, consistent with prior Willison source notes in this corpus.
- **Verbatim quotes**: The WebFetch tool returns AI-processed content. Quotes in
  this note were extracted across three independent fetches and returned consistent
  text; they are believed to be verbatim but cannot be confirmed character-for-character
  given the tool's processing behavior. Claims without confirmed verbatim quotes use
  "(no direct quote; see paraphrase in Our assessment)" per MINER.md §2a.
- **Code examples**: The migrations Python API and `db.atomic()` code blocks were
  consistently returned across multiple fetches and are believed to be verbatim.
- **Backwards-incompatible changes**: The post references the alpha release notes
  for 4.0a0 and 4.0a1 rather than reproducing them in full. Changes summarized in
  this note are from the fetched content; specific alpha release note URLs were not
  followed.
- **Cross-reference verification** (per MINER.md §4b):
  - `blog-simonwillison-llm032a0.md` Claim 5 verified at lines 56–59 of that note:
    "The llm CLI tool worked around this through a custom mechanism for persisting
    and inflating conversations using SQLite, but that never became a stable part of
    the LLM API." Content matches citation. Verified as the 5th `### Claim:` heading
    in document order.
  - `blog-simonwillison-datasette-apps.md` Claim 11 verified at lines 262–281 of
    that note: "Datasette Apps represent a capability evolution arc: Datasette went
    from read-only data publishing → agent-readable SQL → agent-writable SQL → user
    app-hosting, with each step driven by AI capability expansion." Verified as the
    11th `### Claim:` heading in document order.
  - `blog-simonwillison-sqlite-column-provenance.md` overall: confirmed as covering
    column provenance techniques for Python+SQLite via reading that full note (lines
    1–474).
  - `blog-simonwillison-sqlite-agents-md.md` overall: confirmed as covering SQLite
    AGENTS.md governance via reading that full note (lines 1–474).
- **No contradictions filed**: No existing corpus source makes claims that conflict
  with this source's content. No contradiction issue required.
