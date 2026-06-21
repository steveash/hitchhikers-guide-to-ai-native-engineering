---
source_url: https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/
source_type: blog-post
title: "Mapping SQLite result columns back to their source `table.column`"
author: Simon Willison
date_published: 2026-06-13
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: settled
issue: "#1247"
---

# Mapping SQLite result columns back to their source `table.column`

> Simon Willison documents five concrete approaches for mapping SQLite query
> result columns back to their source `table.column` pairs from Python, using
> AI-assisted research. The winning technique — a pure-stdlib ctypes bridge to
> libsqlite3's column-metadata C API — requires no external dependencies,
> handles joins/CTEs/subqueries/aliases correctly, and resolves column sources
> at prepare time without executing the query.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a `trusted-feed` source; 2026-06-13).
  The blog post is a short research announcement linking to a GitHub research folder at
  https://github.com/simonw/research/tree/main/sqlite-column-provenance. The detailed
  findings live in the GitHub repo (README.md, notes.md, column_provenance.py). The README
  and `_summary.md` in the GitHub repo carry an explicit "AI-GENERATED-NOTE" marker — the
  text and code were produced by an LLM. The notes.md is the human-authored research log.
  This source note draws claims from both the blog post and the research repo.
- **Author credibility**: Simon Willison is the creator of Datasette, the `llm` Python CLI,
  and a high-signal commentator on SQLite and LLM tooling. The research was conducted for
  a real, planned feature in Datasette (richer query result display). Working, tested code
  in the research repo (test_provenance.py, compare_all.py) provides empirical backing.
  No vendor affiliation.
- **Scope**: Covers the full problem of mapping SQL result columns to source table.column
  pairs from Python+SQLite, with five enumerated approaches compared side-by-side across
  a 10-query test battery. The research is self-contained — motivated by Datasette but
  not specific to it. Does NOT cover: performance benchmarks, integration into Datasette
  proper, non-Python clients, or SQLite versions other than 3.45.1.

## Extracted Claims

### Claim 1: SQLite already computes result-column-to-source-table.column mappings internally and exposes them via a C API when compiled with `SQLITE_ENABLE_COLUMN_METADATA`

- **Evidence**: Working code in column_provenance.py (MIT-licensed, in research repo)
  uses three C functions (`sqlite3_column_origin_name`, `sqlite3_column_table_name`,
  `sqlite3_column_database_name`) and passes a 10-query verification battery. This is
  corroborated by the SQLite C API documentation at https://sqlite.org/c3ref/column_database_name.html.
- **Confidence**: settled
- **Quote**: "SQLite already computes exactly this. Compiled with `SQLITE_ENABLE_COLUMN_METADATA`
  (the default on virtually every Linux distro and in `apsw`), it exposes three C functions —
  `sqlite3_column_origin_name`, `sqlite3_column_table_name`,
  `sqlite3_column_database_name` — that report, per result column, the **real base
  table and column** the value came from, or `NULL` if the column is a computed
  expression. You don't even have to run the query; *preparing* it is enough."
  *(Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance)*
- **Our assessment**: The insight that preparation (not execution) is sufficient
  makes this technique safe for untrusted queries — a critical property for any
  harness that inspects user-supplied SQL before execution. The `SQLITE_ENABLE_COLUMN_METADATA`
  compilation flag is present in the system libsqlite3 on virtually all Linux distributions
  and in the apsw package, making this approach broadly deployable without recompilation.

### Claim 2: Python's standard-library `sqlite3` module does NOT expose the column-metadata API — its `cursor.description` is name-only

- **Evidence**: Direct statement in article and README, corroborated by the necessity
  of the ctypes workaround (if stdlib exposed it, ctypes wouldn't be needed). The research
  notes confirm "stdlib sqlite3 cannot do this directly" with explanation.
- **Confidence**: settled
- **Quote**: "The catch: Python's standard-library `sqlite3` module does **not** surface these
  (its `cursor.description` is name-only). This report shows four ways to get at the
  answer anyway, three of which need nothing but the standard library."
  *(Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance)*
- **Our assessment**: This is the core gap the research addresses. The stdlib's
  `cursor.description` returns 7-field tuples where only the first field (name) is
  populated — the remaining six are always `None`. This is a known limitation: Python
  intentionally kept the DB-API interface database-agnostic, losing SQLite-specific
  metadata. Any Python code that needs column provenance must use apsw or a ctypes bridge.

### Claim 3: The APSW library's `cursor.description_full` is the best execution-based approach (rated 5/5) — each entry is a 5-tuple with database, table, and origin column

- **Evidence**: Verified against all 10 queries in the test battery. The notes.md
  labels it "WINNER for execution-based." The apsw library is the reference
  implementation against which all other approaches are verified.
- **Confidence**: settled
- **Quote**: "`cursor.description_full` returns 5-tuples:
  (output_name, declared_type, database, table, origin_column)
  When a column is a clean reference, table+origin are populated. When it's an
  expression (||, function, literal, arithmetic) both are None."
  *(Source: notes.md, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/notes.md)*
- **Our assessment**: APSW's design choice to expose `description_full` alongside
  the standard `description` is the cleanest integration path. The 5-tuple format
  maps cleanly to downstream use: output_name drives display, table+origin drive
  provenance annotation, and `None` for both signals "expression, not a raw column."
  The apsw package is well-maintained and available on PyPI, so adding it as a dependency
  is the recommended path for projects that can accept third-party packages.

### Claim 4: A pure-stdlib ctypes bridge to libsqlite3 (`column_provenance.py`) matches APSW 10/10 on a verification battery, including in-memory databases

- **Evidence**: test_provenance.py exercises the ctypes bridge against the apsw
  oracle across file-backed and in-memory connections, 10/10 verified per notes.md.
  The code is in the research repo and is directly runnable.
- **Confidence**: settled
- **Quote**: "Verified: matches apsw description_full 10/10 on the battery, in-memory + file."
  *(Source: notes.md, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/notes.md)*
- **Our assessment**: The ctypes bridge is the recommended path for stdlib-only
  environments. Its approach — `ctypes`-loading the system libsqlite3 and calling
  `sqlite3_prepare_v2` + metadata functions directly — exploits the fact that the
  system library has the metadata API even when Python's bundled module doesn't expose
  it. The 10/10 verification match against apsw gives high confidence in correctness.
  This is the clearest example in the corpus of "use ctypes to bridge a gap between
  Python's stdlib and an underlying C library's unexposed API."

### Claim 5: Both the ctypes bridge and EXPLAIN approaches work at query-prepare time — no rows are read and the technique is safe for side-effect-free inspection

- **Evidence**: README.md key findings section; corroborated by column_provenance.py
  module docstring (uses `sqlite3_prepare_v2`, not `sqlite3_step`).
- **Confidence**: settled
- **Quote**: "You don't need to execute the query. Both the metadata and EXPLAIN
  approaches only *prepare* it, so no user rows are read and side-effect-free."
  *(Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance)*
- **Our assessment**: Prepare-only execution is load-bearing for safe tooling. A
  harness that resolves column provenance before executing a query can annotate
  results before they're returned, or refuse to execute if the provenance reveals
  access to restricted columns (cf. the authorizer approach, Claim 8). For AI agents
  that generate and then execute SQL, knowing that prepare-only is sufficient means
  the inspection step has zero data-access cost or risk.

### Claim 6: Computed expressions (functions, string concatenation, arithmetic, aggregates) correctly report NULL/no-source — the API distinguishes "clean column reference" from "derived value"

- **Evidence**: Verified in the 10-query battery: `name || '-suffix'` returns
  `(t1.id, EXPR)`, `count(*)` and `max(age)` return `(EXPR, EXPR)`. This is the
  intended behavior per the SQLite C API documentation.
- **Confidence**: settled
- **Quote**: "Expressions correctly resolve to 'no source.' `name || '-suffix'`,
  `upper(x)`, arithmetic, literals, and aggregates all report `NULL`
  table/column — exactly the desired 'this is no longer a clean match' signal."
  *(Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance)*
- **Our assessment**: The NULL-for-expression semantics is the most important correctness
  property of the metadata API. A system that falsely attributed expression outputs to
  a source column would give misleading provenance. The explicit NULL signal allows
  downstream systems to distinguish "this column is a direct copy of `t1.name`" from
  "this column is derived from `t1.name` via transformation." That distinction matters
  for data lineage, access control, and UI display.

### Claim 7: The EXPLAIN bytecode parsing approach agrees with the metadata oracle on 9/10 queries, failing only on UNION (compound selects route through ephemeral cursors)

- **Evidence**: compare_all.py output shows 9/10 agreement. The failure case is
  documented: "only UNION misses (compound co-routine -> ephemeral cursor)" per notes.md.
  `PRAGMA automatic_index=OFF` is required to prevent the optimizer from routing joined
  columns through ephemeral indexes.
- **Confidence**: settled
- **Quote**: "Result: agrees with metadata 9/10 (even subquery + CTE, which get flattened);
  only UNION misses (compound co-routine -> ephemeral cursor). Good enough for
  'simple queries', which was the brief."
  *(Source: notes.md, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/notes.md)*
- **Our assessment**: The EXPLAIN approach is pure-stdlib with no native calls, making
  it the most portable option. The 9/10 accuracy is good for simple queries but the
  UNION failure is a known, irreducible limitation of the approach — UNION results are
  routed through ephemeral cursors that have no base-table rootpage. Teams that cannot
  use ctypes (e.g., locked-down environments, WebAssembly) can use the EXPLAIN approach
  with the explicit caveat that UNION queries return "no source" rather than the correct
  attribution. Using `PRAGMA automatic_index=OFF` before running EXPLAIN is a required
  setup step, not optional.

### Claim 8: The authorizer hook approach yields a dependency set (columns read), not a per-output mapping — it over-reports for output attribution but is ideal for access control

- **Evidence**: notes.md documents the semantics clearly: authorizer fires on all
  column reads including WHERE/JOIN/ORDER/GROUP columns, not just output columns.
  The authorizer can be used to deny a column (return `SQLITE_DENY`), which is a
  different use case than mapping.
- **Confidence**: settled
- **Quote**: "NOT a per-output mapping: reads != outputs once there's WHERE/JOIN/ORDER,
  and an expression like name||'-suffix' just shows a read of t1.name with no transform
  signal (naive_output_mapping gives a FALSE POSITIVE there). naive mapping only
  trusted when #reads == #outputs (single table, no filter, no expr)."
  *(Source: notes.md, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/notes.md)*
- **Our assessment**: The authorizer approach solves a different problem than the
  metadata API. For column-level access control (can this query access `users.salary`?),
  the authorizer is the right tool — return `SQLITE_DENY` and the query fails with an
  authorization error. For output annotation (which output column came from which table?),
  the authorizer over-reports because it includes filter columns that don't appear in the
  result set. Teams should choose based on their use case: access control → authorizer;
  output attribution → ctypes/apsw.

### Claim 9: sqlglot's `qualify()` uniquely traces expression output columns back to their input columns — a capability the C metadata API cannot provide

- **Evidence**: notes.md explicitly contrasts: "Unique strength: attributes EXPRESSION
  columns to their INPUT columns (name||'-suffix' -> 'uses t1.name'), which the C API
  cannot." The C API returns NULL for expressions; sqlglot's static analysis resolves
  which source columns feed into the expression.
- **Confidence**: settled
- **Quote**: "Unique strength: attributes EXPRESSION columns to their INPUT columns
  (name||'-suffix' -> 'uses t1.name'), which the C API cannot. Downsides: extra
  dependency, its own SQL parser/dialect quirks, must supply schema, no data-level
  truth."
  *(Source: notes.md, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/notes.md)*
- **Our assessment**: sqlglot's `qualify()` is complementary to, not a replacement for,
  the metadata API. The two approaches give different information: metadata API gives
  output-column → source-column (clean references only); sqlglot gives output-column →
  input-columns (including expressions). A complete lineage system would use both:
  the metadata API for cheap, accurate clean-reference attribution, and sqlglot for
  expression lineage where the C API returns NULL. The downside — must supply the
  schema as a dict, extra dependency, dialect handling — limits it to controlled
  environments where the schema is known ahead of time.

### Claim 10: Ambiguous bare column names are a hard error at prepare time — the metadata approach forces disambiguation before execution

- **Evidence**: Battery query `select id, ... from t1 join t2` where both tables have
  `id` → SQLite raises "ambiguous column name: id" at prepare time. Verified and noted
  explicitly in README.md and notes.md.
- **Confidence**: settled
- **Quote**: "Ambiguous bare columns are a hard error. `select id, ... from t1 join t2`
  when both tables have `id` raises `ambiguous column name: id` at prepare time
  (the user's 'harder still' example only resolves when the bare column lives in
  exactly one joined table; qualify it as `t1.id` and it's fine)."
  *(Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance)*
- **Our assessment**: This is the one case where the metadata API provides no help —
  the error surfaces at prepare time, before metadata can be read. For AI-generated
  SQL, this means any agent that generates queries with bare column names across joins
  will hit this error at prepare time. The fix is SQL-generation discipline: always
  qualify column references in joins. This is actionable as an agent instruction or
  a post-generation validation step.

### Claim 11: For in-memory `sqlite3.Connection` objects, the ctypes bridge uses `Connection.serialize()` to snapshot the schema and `sqlite3_deserialize` to load it into a private ctypes handle — requiring Python 3.11+

- **Evidence**: resolve_columns_for_connection() implementation in column_provenance.py,
  lines spanning the `serialize()` branch. The in-memory path is explicitly tested
  in test_provenance.py and confirmed in notes.md ("Verified: matches apsw description_full
  10/10 on the battery, in-memory + file").
- **Confidence**: settled
- **Quote**: "We never need to *run* the query: preparing the statement is enough for SQLite
  to resolve every output column — including ``*`` expansion, joins, aliases, and
  even subqueries / CTEs / unions — down to the underlying base-table column."
  *(Source: column_provenance.py module docstring, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/column_provenance.py)*
- **Our assessment**: The in-memory bridge is an elegant workaround: stdlib sqlite3
  can't give its connection handle to ctypes, so instead it serializes the entire
  database to bytes and hands those bytes to the ctypes connection. This technique
  generalizes: any case where two Python layers need to share an in-memory SQLite
  database (e.g., a test harness and a ctypes-based inspector) can use
  `serialize()`/`sqlite3_deserialize`. The Python 3.11+ requirement for
  `Connection.serialize()` is the one real constraint; file-backed connections work
  on any Python version that has ctypes.

### Claim 12: The GitHub research README and `_summary.md` are explicitly labeled as AI-generated — the research files were produced by an LLM, with notes.md as the human-authored log

- **Evidence**: README.md carries `<!-- AI-GENERATED-NOTE --> > [!NOTE] > This is an
  AI-generated research report. All text and code in this report was created by an LLM
  (Large Language Model).`
- **Confidence**: settled (explicit first-person label in the repo)
- **Quote**: "This is an AI-generated research report. All text and code in this report was
  created by an LLM (Large Language Model)."
  *(Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance)*
- **Our assessment**: The AI-generated label is a transparency marker, not a quality
  disclaimer. The code in the repo is tested and passes a 10/10 verification battery.
  The research is credible because it is empirically verified (working code, test suite,
  side-by-side comparison) rather than relying on LLM authority. This is the model for
  responsible AI-assisted research publication: LLM-generated content that is explicitly
  labeled as such AND empirically verified, so readers can assess the basis for claims
  independently. The blog post (simonwillison.net) is human-authored; the research artifacts
  are AI-generated but verified.

## Concrete Artifacts

### TL;DR Recommendation Table

Source: README.md, https://github.com/simonw/research/tree/main/sqlite-column-provenance (AI-generated, verified)

```
| If you can…                        | Use                                              | Robustness |
|------------------------------------|--------------------------------------------------|------------|
| add a dependency                   | apsw → cursor.description_full                   | ★★★★★ best, one line |
| use only the stdlib                | column_provenance.py (ctypes → libsqlite3)       | ★★★★★ matches apsw 10/10 |
| use only the stdlib, no native API | explain_provenance.py (EXPLAIN bytecode)         | ★★★☆☆ simple queries |
| just need the dependency set       | authorizer_lineage.py (authorizer hook)          | ★★★☆☆ set, not mapping |
| no execution, expression lineage   | sqlglot qualify()                                | ★★★★☆ needs schema dict |
```

### APSW Usage (one-liner entry point)

Source: README.md (AI-generated, verified)

```python
import apsw
db = apsw.Connection("my.db")
for name, decltype, dbname, table, origin in db.execute(sql).description_full:
    print(name, "<-", f"{table}.{origin}" if table else "(expression)")
```

### ctypes Bridge Entry Points

Source: README.md (AI-generated, verified)

```python
from column_provenance import resolve_columns, resolve_columns_for_connection

# (a) against a database file (opened read-only, query only prepared, never run):
for c in resolve_columns("my.db", "select id, name from t1"):
    print(c)                       # id <- t1.id

# (b) against a live stdlib sqlite3.Connection — including :memory: databases:
import sqlite3
conn = sqlite3.connect(":memory:"); conn.executescript(schema)
for c in resolve_columns_for_connection(conn, sql):
    print(c.output_name, c.table, c.origin_column, c.source)
```

### EXPLAIN Bytecode Parser Key Logic

Source: README.md (AI-generated, verified)

```
Parse VDBE program from EXPLAIN <sql>:
- OpenRead p1=cursor p2=rootpage  -> map cursor -> table via sqlite_master.rootpage
- Column   p1=cursor p2=colidx p3=reg -> register reg holds table.colidx
- Rowid    p1=cursor p2=reg       -> register holds INTEGER PRIMARY KEY alias
- ResultRow p1=start p2=count     -> output = registers start..start+count-1

Set PRAGMA automatic_index=OFF so joined columns stay on their base cursors.
Agrees with metadata oracle 9/10; only UNION fails (ephemeral co-routine cursor).
```

### Side-by-Side Results Table (from compare_all.py)

Source: README.md (AI-generated, empirically verified by running compare_all.py)

```
Query                                              | metadata/apsw             | EXPLAIN  | authorizer (dependency set)
select id, name from t1                           | t1.id, t1.name            | ✅ same  | {t1.id, t1.name}
select * from t1                                  | t1.id, t1.name, t1.extra  | ✅ same  | {t1.id, t1.name, t1.extra}
select t1.id, t1.name, age from t1 join t2        | t1.id, t1.name, t2.age   | ✅ same  | {t1.id, t1.name, t2.age, t2.name}
select id, name || '-suffix' from t1              | t1.id, EXPR               | ✅ same  | {t1.id, t1.name}
select id as the_id, name as nm from t1           | t1.id, t1.name (aliased)  | ✅ same  | {t1.id, t1.name}
select count(*), max(age) from t2                 | EXPR, EXPR                | ✅ same  | {t2.age}
select age from (select * from t2) sub            | t2.age                    | ✅ same  | {t2.id, t2.name, t2.age}
with c as (select id,name from t1) select * from c | t1.id, t1.name          | ✅ same  | {t1.id, t1.name}
select name from t1 union select name from t2     | t1.name                   | ❌ EXPR  | {t1.name, t2.name}
```

### Bottom Line (from notes.md, human-authored research log)

Source: notes.md, https://raw.githubusercontent.com/simonw/research/main/sqlite-column-provenance/notes.md

```
## Bottom line / recommendation
- Best correctness with least code: APSW description_full (if you can add the dep).
- Best for stdlib-only: column_provenance.py (ctypes bridge) — robust, matches APSW.
- All-stdlib, no native calls: explain_provenance.py (simple queries) +
  authorizer_lineage.py (dependency set). 
- Want expression-input lineage or no execution at all: sqlglot.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-agent.md` Claim 1: Datasette Agent provides
    "an extensible AI assistant for interacting with your SQLite databases." The
    column-provenance research is Willison's investigation into the technical
    mechanism needed to annotate Datasette Agent's SQL results with source-column
    information — this source provides the implementation foundation for that
    capability. Both sources concern Datasette's SQL querying layer.
  - `blog-simonwillison-sqlite-agents-md.md` Claim 6: SQLite's AGENTS.md "serves
    a dual purpose — governance of what agents may contribute, and technical context
    for how agents should operate in the codebase." This source shows a third pattern:
    SQLite as a subject for AI-assisted research (column provenance resolved by an LLM,
    verified with working code). The two sources together establish that the SQLite
    ecosystem is a recurring site for AI-native tooling development.

- **Contradicts**: None identified. No existing corpus source claims column provenance
  is infeasible or that Python's stdlib provides it natively.

- **Extends**:
  - `blog-simonwillison-datasette-agent.md` overall: That note covers Datasette Agent
    as an SQL conversational agent. This source provides the specific underlying mechanism
    that would let Datasette Agent annotate query result columns with their source tables —
    a concrete capability extension not described in the earlier note.
  - `blog-simonwillison-sqlite-agents-md.md` Claim 7: "Explicitly stating what the
    project does NOT use ('not Git', 'not GNU Autoconf') to counteract default agent
    assumptions is a concrete context-engineering pattern." This source demonstrates a
    parallel pattern in the other direction: using ctypes to access a C API that Python
    does NOT expose — working around a stdlib gap without replacing the stdlib. Both
    sources illustrate workarounds for things Python/SQLite don't expose by default.

- **Novel**:
  - **Ctypes-as-stdlib-bridge for SQLite metadata**: No existing corpus source documents
    the pattern of `ctypes`-loading a system C library to access APIs that Python's
    wrapper module intentionally omits. This is generalizable beyond SQLite.
  - **Prepare-only inspection for safe SQL analysis**: The finding that `sqlite3_prepare_v2`
    alone (without `sqlite3_step`) is sufficient to resolve full column provenance — including
    `*` expansion, CTEs, subqueries, and aliases — is novel in the corpus. This technique
    enables side-effect-free SQL inspection before execution.
  - **Five-approach taxonomy with quantified accuracy**: The side-by-side comparison
    (10-query battery, explicit star ratings, failure-case documentation) is more systematic
    than any prior corpus source on SQLite tooling. The taxonomy (apsw / ctypes / EXPLAIN /
    authorizer / sqlglot) with explicit decision criteria (dependency allowed? native calls
    allowed? expression lineage needed?) provides a reusable decision framework.
  - **AI-generated + empirically verified research artifacts**: The explicit
    `AI-GENERATED-NOTE` label in the README combined with a passing test suite is the
    corpus's clearest example of responsible AI-assisted research publication. The label
    distinguishes "LLM-assisted" from "unverified" — the two are decoupled by the test battery.
  - **Authorizer-hook semantics clarified**: The corpus has not previously documented
    the distinction between SQLite's authorizer hook (dependency set, fires on all reads
    including WHERE/JOIN/GROUP) and the metadata API (per-output mapping). The notes.md
    warning about "naive_output_mapping gives a FALSE POSITIVE" for expressions is a
    non-obvious gotcha for teams reaching for the authorizer approach.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add the prepare-only column-provenance technique
  (Claims 1, 5) as a concrete example of augmenting query results with source-column
  context. AI agents that generate and execute SQL can annotate results with table.column
  provenance before presenting them to users, enriching the context window with
  attribution information. The technique is side-effect-free (prepare-only) and
  handles `*`, joins, CTEs, and subqueries correctly. Recommend ctypes bridge
  (`column_provenance.py`) for stdlib-only environments; apsw for environments
  that can accept a dependency.

- **Chapter 02 (Harness Engineering)**: Add the ctypes-as-bridge pattern (Claim 4)
  as a technique for accessing C library APIs that Python's stdlib intentionally omits.
  The column_provenance.py implementation demonstrates: (1) locating libsqlite3 via
  `ctypes.util.find_library` with fallback paths; (2) declaring minimal C function
  signatures; (3) handling both file-backed and in-memory connections. This pattern
  is directly applicable to any harness that needs to access unexposed system library
  capabilities from a stdlib-constrained environment.

- **Chapter 03 (Safety and Verification)**: Add the authorizer-hook pattern (Claim 8)
  as a column-level access control mechanism. Returning `SQLITE_DENY` from the authorizer
  blocks a query at prepare time if it accesses a restricted column — a hard gate, not
  a soft warning. Contrast with the column-metadata approach (attribution after the fact)
  vs. the authorizer (prevention before execution). The notes.md warning about authorizer
  over-reporting for output mapping (vs. access control) is a key distinction for
  teams implementing query safety gates.

- **Chapter 05 (Team Adoption)**: Add the five-approach decision table (Concrete
  Artifacts → TL;DR Recommendation Table) as a reference for teams choosing a SQL
  column-provenance approach under different constraints. The explicit criteria
  (can add dependency? native calls allowed? expression lineage needed?) make this
  a direct decision tool rather than a general recommendation.

## Extraction Notes

- **Primary source**: The blog post at simonwillison.net/2026/Jun/13/sqlite-column-provenance/
  is the indexed source URL. It is short (~3 paragraphs) and links to the research
  GitHub repo for all technical detail. This note draws primarily from the GitHub repo
  (README.md, notes.md, column_provenance.py module docstring), all fetched verbatim
  via `curl` from raw.githubusercontent.com.
- **AI-generation disclosure**: The GitHub research repo's README.md and `_summary.md`
  carry an explicit AI-GENERATED-NOTE marker. All code, text, and comparison tables
  in those files were LLM-produced. Claims drawn from these files are rated accordingly,
  but the empirical verification (test_provenance.py passing, compare_all.py output)
  provides independent ground truth.
- **Quote sourcing**: Quotes from the blog post proper are from WebFetch extraction
  (marked with source URL). Quotes from README.md and notes.md are from `curl`-fetched
  raw content (verbatim), marked with their raw GitHub URLs.
- **Cross-reference verification** (per MINER.md §4b):
  - `blog-simonwillison-datasette-agent.md` Claim 1 verified at lines 44–59 of that
    note: "Datasette Agent is an open source plugin for Datasette providing an extensible
    AI assistant for conversational querying of SQLite databases." Content matches citation.
  - `blog-simonwillison-sqlite-agents-md.md` Claim 6 verified at lines 113–128 of that
    note: "SQLite's AGENTS.md serves a dual purpose — governance of what agents may
    contribute, and technical context for how agents should operate in the codebase."
    Content matches citation.
  - `blog-simonwillison-sqlite-agents-md.md` Claim 7 verified at lines 129–143 of that
    note: re "not Git", "not GNU Autoconf" framing. Content matches citation.
- **No contradictions identified**: No existing source note makes claims about SQLite
  column provenance from Python, so no contradiction issues need to be filed.
- **Triage chapter mapping**: The Prospector triage listed Ch04, Ch05, and Ch07. The
  current guide has chapters 00–05. Ch07 does not yet exist; the Ch05 in the triage
  appears to reference a planned "Debugging & Repair" chapter that maps to current Ch03
  (Safety and Verification) and Ch05 (Team Adoption). Guide Impact above maps to the
  actual existing chapters.
