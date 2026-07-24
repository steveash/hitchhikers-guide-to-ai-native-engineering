---
source_url: https://simonwillison.net/2026/Jul/18/sqlite-query-explainer/
source_type: blog-post
title: "SQLite Query Explainer"
author: Simon Willison
date_published: 2026-07-18
date_extracted: 2026-07-24
last_checked: 2026-07-24
status: current
confidence_overall: settled
issue: "#2189"
---

# SQLite Query Explainer

> Simon Willison shipped a browser-only SQLite query-plan explainer, built end-to-end
> by Claude Fable 5 from a single natural-language prompt, that translates `EXPLAIN
> QUERY PLAN` and raw `EXPLAIN` bytecode into plain English via a large hand-authored
> lookup table rather than a live LLM call — while candidly admitting he cannot verify
> the explanations himself. A follow-up automated "docs generation" commit on the same
> repo silently overwrote the tool's correct listing description with an unrelated one,
> undetected in the post itself, giving the source a second, self-supplied case study in
> unverified AI output.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a `trusted-feed` source; short-form
  announcement post, July 18, 2026, auto-discovered from the trusted feed). The blog
  post itself is brief (~150 words); nearly all technical substance lives in the linked
  tool (`tools.simonwillison.net/sqlite-query-explainer`) and its source in
  `github.com/simonw/tools`, merged via pull request #299. This note draws on the blog
  post, PR #299's description (the literal build prompt), the tool's HTML/Python source
  (`sqlite-query-explainer.html`, 1613 lines, fetched via `gh api
  repos/simonw/tools/contents/...`), its Playwright test file
  (`tests/test_sqlite_query_explainer.py`), and its `.docs.md` file plus that file's
  commit history.
- **Author credibility**: Simon Willison is the creator of Django, creator of Datasette,
  and author of the `llm` CLI — a high-signal, designated trusted-feed source in this
  corpus. He builds and publishes working tools with public source, not just commentary.
  He maintains no vendor affiliation, though the tool here was built with an Anthropic
  model (Claude Fable 5) and he discloses that plainly (`Co-Authored-By: Claude Fable 5`
  in the merge commit).
- **Scope**: Covers one tool: a client-side (Pyodide/WASM) SQLite query-plan and
  bytecode explainer. Does NOT cover: how well the explanations hold up against expert
  SQLite review (Willison explicitly says he can't judge this), performance of the tool
  at scale, or any backend/server-side query-explanation approach. This note also covers
  a discrepancy in the tool's own repository (docs.md drift) that Willison's post does
  not mention or address — this is our own finding from reading the linked repository,
  not a claim made in the source text.

## Extracted Claims

### Claim 1: The tool runs a user's SQL against a SQLite database entirely in the browser and annotates both `EXPLAIN QUERY PLAN` and raw `EXPLAIN` bytecode output with plain-English descriptions, using Python's `sqlite3` inside Pyodide (no backend)

- **Evidence**: Blog post opening paragraph; corroborated by the tool source, which
  loads Pyodide via ESM import from jsDelivr and calls
  `pyodide.loadPackage("sqlite3")` before running any query (verified in
  `sqlite-query-explainer.html` lines 1179–1181).
- **Confidence**: settled
- **Quote**: "Run SQL queries against a SQLite database in your browser and see exactly
  how SQLite executes them: the tool runs your query, then annotates every line of both
  `EXPLAIN QUERY PLAN` and the low-level `EXPLAIN` bytecode output with plain-English
  descriptions of what the query planner and virtual machine are doing." (blog post,
  simonwillison.net/2026/Jul/18/sqlite-query-explainer/)
- **Our assessment**: This is a clean, self-contained instance of Willison's recurring
  "browser-native Python developer tool via Pyodide" pattern (see Cross-References).
  Running entirely client-side means no user SQL or data ever leaves the browser — a
  meaningful trust property for a tool designed to be pasted with real (possibly
  sensitive) database files.

### Claim 2: The entire tool was built from a single natural-language prompt given to Claude Fable 5 via Claude Code for web, merged as one pull request with no visible follow-up iteration in the repo

- **Evidence**: PR #299 ("Add SQLite Query Explainer tool") on `simonw/tools`, merged
  2026-07-18T17:19:10Z. The PR body is the literal prompt, blockquoted, followed by a
  human-readable feature summary and a `Co-Authored-By: Claude Fable 5` trailer with a
  `Claude-Session` link. The tool's commit history shows one commit for the tool itself
  (`b82441e6`) and a separate, automated docs-generation commit 50 seconds later (see
  Claim 9) — no manual fix-up commits.
- **Confidence**: settled (verified directly against the GitHub PR via `gh api
  repos/simonw/tools/pulls/299`)
- **Quote**: "Build a tool that uses Pyodide to run sql queries against a SQLite
  database and also runs explain (and explain query plan) against them and annotates
  the explain output with really clear explanations of what everything means" (PR #299
  description, github.com/simonw/tools/pull/299)
- **Our assessment**: This is a strong, verifiable single-prompt-to-shipped-tool example
  — the prompt is fully preserved in the PR description, and the resulting tool (1613
  lines of HTML/CSS/JS/Python, ~90 hand-styled opcode explanations, a 170k-row synthetic
  database generator, an interactive bytecode cross-reference UI) is substantially more
  complex than the prompt's length would suggest. Corroborates the "terse prompt,
  disproportionately complete output" pattern documented elsewhere in the corpus (see
  Cross-References, `blog-simonwillison-doomql.md` Claim 3).

### Claim 3: The build prompt explicitly directed a two-phase development method — prototype the explanation logic in Python first, then build the interactive tool around it — rather than asking for the finished UI directly

- **Evidence**: Second paragraph of the PR #299 prompt, distinct from the feature
  requirements that follow it.
- **Confidence**: settled (verbatim from PR body)
- **Quote**: "Start by prototyping with Python to figure out the best ways to explain
  the different things that can happen in an explain" (PR #299 description,
  github.com/simonw/tools/pull/299)
- **Our assessment**: This is a concrete, actionable prompting pattern for
  explanation-heavy tools: separate "get the domain logic/content right" (prototype in
  a scriptable language, iterate on the explanations themselves) from "build the
  delivery mechanism" (wire the validated logic into an interactive UI). The shipped
  code reflects this split structurally — `explain_opcode()` and
  `annotate_eqp_detail()` are pure Python functions operating on parsed SQLite output,
  entirely separable from the JavaScript/DOM code that calls them (see Concrete
  Artifacts). A team asking an agent to build an explanation tool for a dense technical
  format could reuse this exact two-phase instruction.

### Claim 4: Willison explicitly states he lacks the SQLite expertise to verify the correctness of the AI-generated query-plan explanations himself, and ships the tool anyway on the basis that the output "seems cromulent"

- **Evidence**: Direct first-person statement in the blog post, immediately following
  the feature description — his only explicit caveat in the entire post.
- **Confidence**: settled (verbatim quote from the primary source)
- **Quote**: "Approach with caution, since I don't know enough about SQLite query plans
  to verify the results myself, but it seems cromulent enough to me." (blog post,
  simonwillison.net/2026/Jul/18/sqlite-query-explainer/)
- **Our assessment**: This is a direct, named instance of publishing an AI-assisted
  explanatory tool without independent expert verification of its core claims — precisely
  the trust/verification tension the Prospector flagged. Note the asymmetry: Willison
  *can* verify that the tool runs correctly (it executes real SQLite and displays real
  `EXPLAIN` output — that part is not AI-generated, see Claim 6), but he cannot verify
  that the *prose explaining* that output is accurate, because that requires SQLite
  internals expertise he doesn't have. "Seems cromulent" is an aesthetic/plausibility
  judgment, not a correctness check — a distinction worth naming explicitly for any
  guide advice about publishing AI-authored explanations of technical output the
  publisher can't independently verify.

### Claim 5: The project was directly inspired by a specific line in a Julia Evans blog post about SQLite, in which Evans expressed uncertainty about reading query plans

- **Evidence**: Blog post tags Julia Evans by name and links her post; the motivating
  line is quoted directly.
- **Confidence**: settled (verbatim quotes from the primary source)
- **Quote**: "Julia Evan's, in Learning a few things about running SQLite" ... "Maybe one
  day I'll learn to read a query plan." (blog post,
  simonwillison.net/2026/Jul/18/sqlite-query-explainer/; the post links Evans' piece at
  jvns.ca/blog/2026/07/17/learning-about-running-sqlite/)
- **Our assessment**: The tool's origin is a one-day turnaround from "an expert
  practitioner (Evans) publicly admits she can't read a query plan" to "a working,
  AI-built explainer for exactly that gap" (Evans' post is dated 2026-07-17; the tool
  shipped 2026-07-18). This is a fast, low-friction path from an observed pain point in
  someone else's writing to a shipped tool, made viable by the low cost of a single
  AI-delegated build session.

### Claim 6: The plain-English opcode explanations are not produced by a live LLM call in the browser — they are a static Python dictionary of roughly 90 hand-authored explanation strings, one per SQLite VDBE opcode, baked into the tool's shipped source and looked up by opcode name at runtime

- **Evidence**: Direct inspection of `sqlite-query-explainer.html` lines 793–960: the
  `explain_opcode(op, p1, p2, p3, p4, p5)` function builds a dict literal `E` mapping
  ~90 opcode names (`Init`, `OpenRead`, `SeekGE`, `Column`, `ResultRow`, `AggStep`,
  etc.) to f-string-templated English sentences referencing the specific register/cursor
  operands of the instruction being explained, then returns `E.get(op, "")`.
- **Confidence**: settled (verified directly against the shipped source code)
- **Quote**: (no direct quote from Willison's blog post; the tool's own source is the
  evidence — see Concrete Artifacts for a verbatim excerpt of the opcode dictionary)
- **Our assessment**: This materially changes what "AI-generated explanation" means for
  this tool, and it is a distinction the blog post never draws. The explanations are
  not runtime LLM inference over arbitrary bytecode (which would be unauditable and
  could hallucinate per-query) — they are a fixed, inspectable, testable lookup table
  that Claude Fable 5 *authored once* during the build session, covering SQLite's known,
  finite VDBE opcode set. This is a stronger trust posture than it first appears: a
  reader (or future maintainer) can read all ~90 explanations directly, diff them
  against SQLite's own opcode documentation, and file a correction — none of which is
  possible for a live per-query LLM narration. It also means Willison's "I can't verify
  this" caveat (Claim 4) applies to a closed, reviewable artifact, not an open-ended
  generative process — a materially easier verification problem than the caveat's
  phrasing suggests, though still an unaddressed one at time of publication.

### Claim 7: The `EXPLAIN QUERY PLAN` annotations use the same static-lookup approach: a Python function pattern-matches SQLite's known planner detail-string vocabulary (e.g. "MULTI-INDEX OR", "USE TEMP B-TREE FOR ORDER BY", "MATERIALIZE ...") against regexes and returns a matching hand-written explanation, rather than interpreting arbitrary plan text generatively

- **Evidence**: `annotate_eqp_detail(detail, derived_names)` in
  `sqlite-query-explainer.html` lines 454–589 handles roughly 20 distinct SQLite
  query-planner phrase patterns (compound queries, CTE materialization vs. co-routine,
  subquery types, Bloom filters, temp b-trees) via literal string matches and `re.match`
  calls, falling through to `annotate_scan_search()` for SCAN/SEARCH lines.
- **Confidence**: settled (verified directly against the shipped source code)
- **Quote**: (no direct quote; see Concrete Artifacts for a verbatim excerpt of
  `annotate_eqp_detail`)
- **Our assessment**: Same structural pattern as Claim 6, applied to the query-plan
  side rather than the bytecode side. Both annotation surfaces of this tool are
  template/lookup engines over SQLite's own finite, documented vocabulary (opcode names;
  `EXPLAIN QUERY PLAN` detail-string grammar), not free-form generation. This is the
  load-bearing design decision that makes "plain-English explanations of dense technical
  output" tractable to build and (in principle, though not yet done here) verify: the
  input space SQLite can produce is finite and the mapping was authored, not inferred
  per-request.

### Claim 8: The tool ships a deterministic 170,000+ row synthetic example database (fixed random seed) covering five related tables — including a `WITHOUT ROWID` table and a view — paired with 22 curated example queries selected specifically to exercise distinct query-plan patterns

- **Evidence**: `load_example_database()` in `sqlite-query-explainer.html` (lines
  383–420) seeds Python's `random` with `random.seed(42)` before generating 2,000
  customers, 200 products, 20,000 orders, up to 60,000 order_items, and 50,000 events;
  the `EXAMPLE_SCHEMA` (lines 339–380) defines the `order_items` table as `WITHOUT
  ROWID` and an `order_totals` view. The `EXAMPLES` array (lines 1041–1153) lists 22
  named queries, each with a one-sentence `desc` explaining what plan feature it
  demonstrates.
- **Confidence**: settled (verified directly against the shipped source code)
- **Quote**: "\"Load example database\" builds 170k+ rows across five tables (with
  indexes, a WITHOUT ROWID table and a view) using loops with a fixed random seed, plus
  22 example queries chosen to illustrate as many query plan patterns as possible: full
  scans, rowid lookups, covering indexes, nested-loop joins, temp b-tree sorts,
  MULTI-INDEX OR, automatic indexes, materialized vs co-routine CTEs, recursive CTEs,
  window functions and more" (PR #299 description, github.com/simonw/tools/pull/299)
- **Our assessment**: The fixed seed (`random.seed(42)`) makes the example database
  fully reproducible across sessions and machines — the same "random" data every time
  a user clicks "Load example database." This is a deliberate determinism choice for a
  teaching tool: the 22 example queries' descriptions (e.g. "no index on
  `customers.name`, so SQLite must ... sort") are only guaranteed accurate if the
  underlying data is the same every run. This is a reusable pattern for AI-built (or
  any) demo/teaching tools that pair canned example queries with generated data: seed
  the generator, don't leave it to chance.

### Claim 9: The bytecode view is interactive, not just annotated text — jump-target addresses render as clickable links, target rows show which instructions jump to them, and hovering a register or cursor highlights every other row that references it

- **Evidence**: PR #299 description explicitly enumerates this as a feature; the test
  file exercises it directly (`test_full_flow_with_example_database` clicks an
  `a.addr-link`, reads its `data-addr` attribute, and asserts the corresponding
  `#op-{addr}` row gains a `flash` class).
- **Confidence**: settled (verified against both the PR description and the Playwright
  test in `tests/test_sqlite_query_explainer.py`)
- **Quote**: "EXPLAIN bytecode instructions cross-reference each other: jump\ntargets
  are clickable links, jump-target rows show which\ninstructions jump to them, loop
  bodies get depth bars, and hovering\na register or cursor highlights everywhere else
  it is used" (PR #299 description, github.com/simonw/tools/pull/299)
- **Our assessment**: This is a UX design choice worth naming separately from the
  explanation content itself: VDBE bytecode is a flat list of numbered instructions
  with implicit control-flow (jump targets by address) and implicit data-flow
  (registers/cursors referenced across many rows). Rendering it with explicit
  cross-links converts a list a reader would otherwise have to trace by eye into a
  navigable graph. This is a generalizable technique for explaining any bytecode-like
  or instruction-trace format (VM bytecode, assembly, compiled query plans) via a
  browser tool: pair prose annotation with structural highlighting of the underlying
  jump/reference graph.

### Claim 10: The tool's Playwright test suite is split into an offline structural test and a single full-flow test gated on network access (for the ~15 MB Pyodide download) with an extended 240-second timeout for the example-database build

- **Evidence**: `tests/test_sqlite_query_explainer.py` (74 lines): `test_initial_state`
  runs against a local file server with no network dependency; `
  test_full_flow_with_example_database` is explicitly commented `"""Loads Pyodide from
  the CDN - needs network access."""` and calls `page.wait_for_selector("#output:not([hidden])",
  timeout=240_000)`.
- **Confidence**: settled (verified directly against the shipped test file)
- **Quote**: "Loads Pyodide from the CDN - needs network access." ... "# Pyodide (~15 MB)
  plus building 170k rows can take a while on CI" (tests/test_sqlite_query_explainer.py,
  github.com/simonw/tools)
- **Our assessment**: Splitting tests into a network-independent structural tier and a
  network-dependent (and much slower) full-flow tier is a sound CI design for any
  Pyodide-based browser tool: the offline tier can run on every commit cheaply, while
  the slow, flaky-network-prone tier can be run less frequently or tolerated as slower.
  The 240-second timeout is itself a data point on Pyodide cold-start + 170k-row
  synthetic data generation cost in a CI environment — useful context for anyone
  budgeting CI time for a similar tool.

### Claim 11: A separate, automated "docs generation" commit landed 50 seconds after the tool's merge and silently overwrote its correct, tool-specific description with an unrelated description about "Mozilla Bugzilla bug reports" — a mismatch still live in the repository at time of extraction, and never mentioned by Willison

- **Evidence**: `gh api "repos/simonw/tools/commits?path=sqlite-query-explainer.docs.md"`
  shows two commits: the merge of PR #299 at `2026-07-18T17:19:10Z` (which added a
  correct, tool-specific `.docs.md`), followed by a commit titled "Generated docs:
  sqlite-query-explainer" at `2026-07-18T17:20:00Z` (sha `4a4ff8eb`) whose diff (fetched
  via `gh api repos/simonw/tools/commits/4a4ff8eb...`) replaces the entire file content.
  The replacement text is currently live at both
  `github.com/simonw/tools/blob/main/sqlite-query-explainer.docs.md` and
  `raw.githubusercontent.com/simonw/tools/main/sqlite-query-explainer.docs.md`
  (independently verified via `curl`).
- **Confidence**: settled (directly observed via GitHub commit API and raw file fetch;
  not mentioned in the blog post or PR — this is our own finding, not the source's claim)
- **Quote**: Original (PR #299, correct): "Run SQL queries against a SQLite database in
  your browser and see exactly how SQLite executes them: the tool runs your query, then
  annotates every line of both `EXPLAIN QUERY PLAN` and the low-level `EXPLAIN` bytecode
  output with plain-English descriptions of what the query planner and virtual machine
  are doing." Replacement (commit `4a4ff8eb`, currently live): "View Mozilla Bugzilla
  bug reports and run SQL queries against a SQLite database to see exactly how SQLite
  executes them. The tool annotates every line of `EXPLAIN QUERY PLAN` and low-level
  `EXPLAIN` bytecode output with plain-English descriptions of what the query planner
  and virtual machine are doing." (both from
  github.com/simonw/tools/commits/sqlite-query-explainer.docs.md, fetched via `gh api`)
- **Our assessment**: This is a self-supplied, verifiable case study in exactly the
  failure mode the guide should warn about: a secondary, automated AI-assisted pipeline
  (evidently a per-tool description generator that runs across the `simonw/tools` repo,
  given the "Generated docs" commit message and the `<!-- Generated from commit: ... -->`
  trailer it stamps into every `.docs.md`) partially corrupted a correct artifact
  one minute after it was created, and the corruption was never caught or corrected —
  it is still live as of this extraction. The replacement text is not nonsensical
  (it's fluent, plausible-sounding prose that even preserves most of the correct
  content), which is precisely why a "does this read sensibly?" check would not catch
  it — only cross-referencing against the tool's actual purpose reveals the
  "Mozilla Bugzilla bug reports" clause as wrong. This directly parallels Claim 4's
  trust caveat but at one remove: Willison flagged that he can't verify the *content*
  of the AI-authored explanations; here, a *different* AI-assisted step (docs
  generation) produced a verifiably wrong artifact that nobody — including Willison —
  appears to have checked, because it's metadata (a catalog description) rather than
  the user-facing product itself.

## Concrete Artifacts

### The build prompt, verbatim (PR #299 description, github.com/simonw/tools/pull/299)

```
Build a tool that uses Pyodide to run sql queries against a SQLite database and also runs explain (and explain query plan) against them and annotates the explain output with really clear explanations of what everything means

Start by prototyping with Python to figure out the best ways to explain the different things that can happen in an explain

The page should come with a default database which is loaded if the user clicks "Load example database" - that one can have some large tables in since it can run loops to populate them. It should include several example queries for the user to pick which illustrate as many explain patterns as possible

OR the user can open their own SQLite database and run their own queries - if they open their own SQLite database it starts by showing them the schema of it using a query against sqlite_master

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Vx3Jgd4JPLFsKLwT8BemnL
```

### VDBE opcode explanation dictionary, excerpt (sqlite-query-explainer.html, `explain_opcode()`, lines 793–830, 958–960)

```python
# Source: github.com/simonw/tools/blob/main/sqlite-query-explainer.html
def explain_opcode(op, p1, p2, p3, p4, p5):
    """Return a human explanation for one VDBE instruction.

    Jump-target addresses are wrapped in [[a:N]] markers so the UI can turn
    them into links to the referenced instruction.
    """
    p4 = p4 or ""

    def r(n):
        return f"r[{n}]"

    def c(n):
        return f"cursor {n}"

    def a(n):
        return f"[[a:{n}]]"

    E = {
        "Init": f"Start of the program: jump to instruction {a(p2)} (the one-time setup code placed at the end), which will jump back to the top. Every compiled statement begins with Init.",
        "Transaction": f"Begin a {'write' if p2 else 'read'} transaction on database {p1}. Every statement that touches the database needs this.",
        "SeekRowid": f"Jump {c(p1)} straight to the row whose rowid equals {r(p3)} — an O(log n) primary-key lookup, the fastest way to find a row. If that row doesn't exist, jump to {a(p2)}.",
        "Column": f"Read column {p2} of the row {c(p1)} is on, into {r(p3)}." + (f" ({p4})" if p4 else ""),
        "ResultRow": f"Emit one result row to the caller, made of registers {r(p1)}..r[{p1 + p2 - 1}]. Execution pauses here until the caller asks for the next row.",
        # ... ~85 more entries covering the full VDBE opcode set ...
    }
    return E.get(op, "")
```

### `EXPLAIN QUERY PLAN` detail-string annotator, excerpt (sqlite-query-explainer.html, `annotate_eqp_detail()`, lines 454–478, 536–553)

```python
# Source: github.com/simonw/tools/blob/main/sqlite-query-explainer.html
def annotate_eqp_detail(detail, derived_names):
    d = detail

    if d == "COMPOUND QUERY":
        return ("compound", "This query combines multiple SELECTs with a compound "
                "operator (UNION, UNION ALL, INTERSECT or EXCEPT). Each arm runs as "
                "its own sub-plan below.")
    ...
    if d == "MULTI-INDEX OR":
        return ("search", "The WHERE clause has OR terms that can each use a different "
                "index. SQLite evaluates each OR branch separately with its own index "
                "(the INDEX 1, INDEX 2… branches below) and combines the matching "
                "rowids, skipping duplicates. Usually much faster than a full scan.")
    ...
    m = re.match(r"^BLOOM FILTER ON (\S+)", d)
    if m:
        return ("bloom", f"SQLite builds a Bloom filter on “{m.group(1)}” — a compact "
                "in-memory bitmap that can instantly answer “definitely not present” "
                "for a join key. Before doing the more expensive index/table lookup for "
                "each row, SQLite consults the filter and skips rows that cannot "
                "possibly match. A cheap trick that speeds up large joins.")
```

### Example query catalog, excerpt (sqlite-query-explainer.html, `EXAMPLES` array, lines 1041–1057)

```javascript
// Source: github.com/simonw/tools/blob/main/sqlite-query-explainer.html
const EXAMPLES = [
    {
        title: "Full table scan",
        desc: "The events table has no index on event_type, so SQLite has to visit all 50,000 rows and test each one.",
        sql: "SELECT * FROM events WHERE event_type = 'purchase' LIMIT 10"
    },
    {
        title: "Rowid primary key lookup",
        desc: "Looking a row up by its INTEGER PRIMARY KEY is the fastest operation in SQLite — a single descent of the table's b-tree.",
        sql: "SELECT * FROM customers WHERE id = 42"
    },
    // ... 20 more entries, including MULTI-INDEX OR, recursive CTEs,
    //     MATERIALIZED vs co-routine CTEs, and window functions ...
];
```

### Example database generator, deterministic seed (sqlite-query-explainer.html, `load_example_database()`, lines 383–388)

```python
# Source: github.com/simonw/tools/blob/main/sqlite-query-explainer.html
def load_example_database():
    global conn
    import random
    random.seed(42)
    conn = sqlite3.connect(":memory:")
    conn.executescript(EXAMPLE_SCHEMA)
```

### Docs.md drift — before (correct, from PR #299) vs. after (wrong, live at extraction time)

```
# Before — commit b82441e6 (merge of PR #299, 2026-07-18T17:19:10Z)
Run SQL queries against a SQLite database in your browser and see exactly how SQLite
executes them: the tool runs your query, then annotates every line of both `EXPLAIN
QUERY PLAN` and the low-level `EXPLAIN` bytecode output with plain-English descriptions
of what the query planner and virtual machine are doing. Load the built-in example
database — 170,000+ rows with indexes, a view and 22 example queries illustrating
patterns like covering indexes, nested-loop joins, temp b-tree sorts, automatic indexes
and recursive CTEs — or open your own SQLite file, which is inspected via
`sqlite_master` to show its schema first. Bytecode instructions are cross-linked, so
jump targets are clickable and hovering a register or cursor highlights everywhere
else it is used. Powered by Python's `sqlite3` module running in Pyodide, so no data
leaves your machine.

# After — commit 4a4ff8eb ("Generated docs: sqlite-query-explainer", 2026-07-18T17:20:00Z)
# Still live at github.com/simonw/tools/blob/main/sqlite-query-explainer.docs.md at
# time of extraction (2026-07-24).
View Mozilla Bugzilla bug reports and run SQL queries against a SQLite database to see
exactly how SQLite executes them. The tool annotates every line of `EXPLAIN QUERY PLAN`
and low-level `EXPLAIN` bytecode output with plain-English descriptions of what the
query planner and virtual machine are doing. Load the built-in example database with
170,000+ rows across multiple tables with indexes and a view, or open your own SQLite
file, then write queries with clickable bytecode instruction links and hoverable
register highlighting. Powered by Python's `sqlite3` module running in Pyodide, so all
data stays in your browser.

<!-- Generated from commit: b82441e63ff0b1fc8a1942aaf5ba3dda6d6ebcdd -->
```

### Playwright test split (tests/test_sqlite_query_explainer.py, github.com/simonw/tools)

```python
"""
Playwright tests for sqlite-query-explainer.html

The initial-state tests run offline. The full flow (loading Pyodide from the
CDN, building the example database, running annotated queries) is covered by
a single test marked as needing network access.
"""

def test_full_flow_with_example_database(page: Page, unused_port_server):
    """Loads Pyodide from the CDN - needs network access."""
    unused_port_server.start(root)
    page.goto(f"http://localhost:{unused_port_server.port}/sqlite-query-explainer.html")

    page.click("#load-example")
    # Pyodide (~15 MB) plus building 170k rows can take a while on CI
    page.wait_for_selector("#output:not([hidden])", timeout=240_000)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-doomql.md` Claim 3 ("A single terse, technically-scoped
    natural-language prompt pasted into Claude chat (Fable 5) produced a working
    HTML+JavaScript Datasette App"): this source is a second, independently verified
    instance of a single prompt (here, four short paragraphs in a PR description)
    producing a substantially more complex working artifact — corroborating that this
    is a repeatable pattern with Claude Fable 5 specifically, not a one-off.
  - `blog-simonwillison-opfs-pyodide.md` Claim 5 (sqlite3 is "unvendored" in Pyodide and
    must be explicitly loaded via `pyodide.loadPackage("sqlite3")` before `import
    sqlite3`): this tool's source independently reproduces the identical call
    (`await pyodide.loadPackage("sqlite3")`, `sqlite-query-explainer.html` line 1181),
    confirming the constraint still held as of Pyodide v0.27.5 (this tool) vs. v0.27.2
    (the opfs-pyodide note, six weeks earlier) — the constraint is stable across at
    least two Pyodide point releases.
  - `blog-simonwillison-claude-fable-5.md` Claim 9 ("Claude Fable 5 produced API
    design, tests, code, and documentation for LLM 0.32a3 at a quality level Willison
    characterizes as impressive"): this source's shipped tool (1613 lines, working
    tests, an internally consistent ~90-entry opcode dictionary) is consistent with that
    characterization for a from-scratch build, not just an extension of existing code.

- **Contradicts**: None identified. No existing corpus note makes claims about
  browser-native SQLite query-plan explanation, VDBE bytecode annotation, or the
  `simonw/tools` docs-generation pipeline specifically.

- **Extends**:
  - `blog-simonwillison-opfs-pyodide.md`: that note documents Pyodide + OPFS for
    persistent SQLite storage in the browser, using a dedicated Web Worker for OPFS
    writes. This tool is a Pyodide + SQLite browser app with no persistence requirement
    (databases are ephemeral/in-memory or a copied-in user file) and, correspondingly,
    runs Pyodide on the main thread with no Worker at all (verified: no `new Worker(`
    call anywhere in `sqlite-query-explainer.html`). Together the two notes show the
    Worker-vs-main-thread choice tracks directly with whether the tool needs
    `createSyncAccessHandle()` (OPFS write path, Worker-only) — a concrete decision
    rule for future Pyodide browser tools.
  - `blog-simonwillison-sqlite-column-provenance.md`: that note documents mapping
    SQLite result columns back to source tables via a ctypes bridge or APSW, for
    programmatic (non-visual) use. This source is a complementary, human-facing
    counterpart: instead of resolving column provenance for a downstream program, it
    resolves *execution-plan* semantics for a human reader, using SQLite's own
    `EXPLAIN`/`EXPLAIN QUERY PLAN` output as the substrate in both cases. Neither note's
    underlying technique depends on the other, but both mine dense SQLite introspection
    output for machine- or human-readable structure.
  - `blog-simonwillison-doomql.md` Claim 6 ("DOOMQL's underlying game engine was built
    by a third party ... not Claude — Claude's only role in this post is generating a
    read-only viewer layered on top of an already-complete system"): that note
    documents a case where the AI-built layer is thin (a viewer) atop non-AI-built
    substance. This source is the inverse: the AI-built layer (Claude Fable 5's
    explanation dictionary and EQP annotator) *is* the substance — SQLite itself
    supplies only the raw `EXPLAIN`/`EXPLAIN QUERY PLAN` text; every word of the
    plain-English explanation layered on top was authored by the agent. This is a
    useful contrast for characterizing how much interpretive weight an "AI layer" is
    actually carrying in different projects.

- **Novel**:
  - **Static, hand-authored opcode/plan-vocabulary lookup tables as an alternative to
    live LLM narration** (Claims 6, 7): no existing corpus source documents this design
    choice — using an AI agent to *author once* a finite, reviewable mapping from a
    closed vocabulary (SQLite's ~130 VDBE opcodes, ~20 `EXPLAIN QUERY PLAN` phrase
    patterns) to explanatory prose, then shipping that mapping as static code rather
    than calling an LLM per query. This is a distinct, more auditable pattern than
    "the AI explains this user's specific output live," relevant to any tool explaining
    a technical format with a closed, enumerable vocabulary (bytecode, protocol
    messages, error codes, opcodes).
  - **Verified docs-generation drift in a live, shipped AI-native tool repository**
    (Claim 11): no existing corpus source documents a concrete, dated, diffable instance
    of an automated documentation/metadata generation step silently corrupting a
    correct artifact, uncaught by the human publisher, and still live weeks later. This
    is a first-hand, independently reproducible (via `gh api` / `curl`) case study for
    the corpus's coverage of unverified AI output — previously covered mostly through
    authors' self-reported caveats (e.g. Claim 4 here, or Willison's "I don't know
    enough to verify" pattern in `blog-simonwillison-sqlite-agents-md.md`), this is a
    case the *source author himself did not catch or mention*.
  - **Fixed-seed synthetic data generation paired with curated example queries** (Claim
    8) as a reproducibility pattern for AI-built teaching/demo tools: not documented
    elsewhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the two-phase prompting instruction from
  Claim 3 ("prototype the explanation/domain logic in a scriptable language first,
  then build the delivery UI around it") as a concrete pattern for prompting an agent
  to build explanation-heavy or content-heavy tools, distinct from prompting for the
  finished UI directly. Cite the PR #299 prompt (Concrete Artifacts) as a worked
  example: four short paragraphs, no code, produced a 1613-line working tool.

- **Chapter 03 (Verification)**: Add Claims 4, 6, 7, and 11 together as a worked case
  study in layered, uneven AI-output verification within a single project. Distinguish
  three tiers actually present in this one tool: (1) SQLite's own `EXPLAIN` output —
  ground truth, not AI-generated, fully trustworthy; (2) the static opcode/plan
  explanation dictionary — AI-authored once, closed vocabulary, in principle fully
  reviewable/diffable against SQLite's documentation, but *not actually reviewed* by
  Willison, who states this directly; (3) the tool's own catalog description
  (`.docs.md`) — regenerated by a separate automated pipeline, silently wrong, and
  never checked by anyone. The guide should note that "AI-generated" is not one risk
  tier: a static, closed-vocabulary lookup table is a categorically easier
  verification problem than live per-input generation, but easier-to-verify is not the
  same as verified — this tool ships with neither the explanations nor the
  auto-generated docs actually checked against ground truth by a domain expert.

- **Chapter 04 (Context Engineering)**: Add the finite-vocabulary lookup-table pattern
  (Claims 6, 7) as a concrete alternative to runtime LLM calls for explaining structured,
  closed-vocabulary technical output (bytecode, opcodes, status/error codes, protocol
  frames). When the space of possible inputs is enumerable, an agent can author a
  complete static mapping once instead of generating an explanation per instance —
  trading a one-time authoring cost for zero runtime inference cost, full
  offline/client-side operation, and a reviewable artifact.

## Extraction Notes

- **Sources read in full**: the blog post (via WebFetch, multiple targeted passes since
  the tool's default summarization otherwise elided verbatim quotes); PR #299 and its
  full description (via `gh api repos/simonw/tools/pulls/299`); the complete tool source
  `sqlite-query-explainer.html` (1613 lines, fetched via `gh api
  repos/simonw/tools/contents/sqlite-query-explainer.html` and base64-decoded); the full
  Playwright test file (74 lines); the `.docs.md` file and its two-commit history
  (`gh api "repos/simonw/tools/commits?path=..."` and the diff of each commit).
- **Julia Evans' post was not separately mined**: her post
  (jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) is referenced only as
  motivation (Claim 5); no existing corpus source note covers it, and it was out of
  scope for this extraction (the triaged source is Willison's post, not Evans').
  Flagging it as a candidate for separate submission if Julia Evans' broader SQLite
  post has independent guide-relevant content.
- **No contradiction issue filed**: nothing in this source materially opposes an
  existing source-note claim (see Cross-References → Contradicts).
- **Docs.md drift (Claim 11) is our own finding, not Willison's**: this was surfaced by
  following the repository's commit history per MINER.md §1 ("follow up to 5 linked
  pages that seem substantive"), not by anything stated in the blog post. It is
  presented as directly verified (commit diffs, live file content) rather than as
  Willison's claim, and is explicitly labeled as such throughout.
- **Cross-reference verification** (per MINER.md §4b): `blog-simonwillison-doomql.md`
  Claim 3 and Claim 6 verified against that note's numbered claims directly (both exist
  as stated, content matches citation). `blog-simonwillison-opfs-pyodide.md` Claim 5
  verified at that note's Claim 5 (sqlite3 unvendored / explicit `loadPackage` call);
  content matches citation. `blog-simonwillison-claude-fable-5.md` Claim 9 verified;
  content matches citation.
