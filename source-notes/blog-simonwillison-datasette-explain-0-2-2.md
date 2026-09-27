---
source_url: https://simonwillison.net/2026/Sep/20/datasette-explain/
source_type: blog-post
title: "datasette-explain 0.2.2"
author: Simon Willison
date_published: 2026-09-20
date_extracted: 2026-09-27
last_checked: 2026-09-27
status: current
confidence_overall: settled
issue: "#3748"
---

# datasette-explain 0.2.2

> A one-line "beat" release announcement for datasette-explain 0.2.2, a
> Datasette plugin that runs `EXPLAIN QUERY PLAN` against the SQL a user is
> currently typing into the query editor and renders the plan (or an error)
> live, as-you-type. The 0.2.2 release fixes the plan display for read-only
> stored-query pages; the underlying plugin has otherwise seen almost no
> activity since early 2024.

## Source Context

- **Type**: blog-post — a "beat" (Simon Willison's short-form release-
  announcement format at simonwillison.net, consistent with
  `blog-simonwillison-datasette-1-0a38.md` and `blog-simonwillison-datasette-1-0a39.md`).
  The beat itself is two sentences plus a one-bullet changelog excerpt. Per
  MINER.md §1, the linked GitHub release page
  (`github.com/simonw/datasette-explain/releases/tag/0.2.2`) and the plugin's
  README (`raw.githubusercontent.com/simonw/datasette-explain/main/README.md`)
  were fetched for additional detail. The GitHub *release page itself* is a
  JavaScript-rendered React app whose static HTML carries no readable release
  body (only Open Graph meta tags); the release body text was instead
  retrieved via the public GitHub REST API
  (`api.github.com/repos/simonw/datasette-explain/releases`), which returns
  the exact same Markdown Willison writes for each tagged release. All six
  releases in the project's history (0.1a0 through 0.2.2) were pulled this
  way to establish the version-history claims below.
- **Author credibility**: Simon Willison is the creator of Datasette and the
  sole author of datasette-explain (first commit and all releases attributed
  to him in the GitHub release history). This is first-party release
  documentation and a first-party README for a tool he wrote and maintains.
  No vendor affiliation; no external corroboration needed for "what the tool
  does" claims since the README and release notes are the tool's own
  specification.
- **Scope**: Covers the plugin's stated purpose and mechanism (README), the
  full public release history (six tagged releases, 2023-02 through
  2026-09), and the specific 0.2.2 changelog entry and its stated motivation.
  Does NOT cover: the plugin's install/adoption numbers, any AI-agent use of
  the tool (this is a human-facing query-editor aid, not an agent tool —
  distinct from `datasette-agent` plugins covered elsewhere in the corpus),
  performance of the `EXPLAIN QUERY PLAN` polling mechanism, or any
  discussion of *why* the plugin went quiet between February 2024 and
  September 2026.

## Extracted Claims

### Claim 1: datasette-explain 0.2.2 fixes explain-plan display specifically on read-only stored-query pages
- **Evidence**: Verbatim, single-bullet changelog identical across the blog
  post and the GitHub release body (confirmed via GitHub REST API).
- **Confidence**: settled (first-party changelog, directly verifiable)
- **Quote**: "Explain plans now work on read-only stored-query pages."
  *(Source: simonwillison.net/2026/Sep/20/datasette-explain/, and identically
  in the GitHub release body for tag `0.2.2`)*
- **Our assessment**: This is the entire substantive content of the 0.2.2
  release: a display-scope fix for one specific page type (Datasette's
  read-only view of a saved/"stored" query) where the plugin previously did
  not render explain output. No other behavior changed in this release.

### Claim 2: The 0.2.2 fix was discovered through the author's own dogfooding — upgrading his personal Datasette instance surfaced the bug
- **Evidence**: Direct first-party statement of motivation in the blog post.
- **Confidence**: settled (first-party statement)
- **Quote**: "I upgraded datasette.simonwillison.net to Datasette 1.0a40, which inspired me to ship a new version of this explain plugin."
  *(Source: simonwillison.net/2026/Sep/20/datasette-explain/)*
- **Our assessment**: The trigger is routine self-hosted-instance maintenance
  (upgrading the Datasette core version), not an external bug report or a
  planned feature push. This is a small, concrete instance of "upgrade your
  own dependency, notice what breaks, fix it" as a maintenance pattern —
  consistent with Willison's general practice of running his own tools in
  production (`datasette.simonwillison.net`) as the first test environment
  for plugin compatibility, also visible in the 1.0a38/1.0a39 security-release
  notes' Datasette Cloud references.

### Claim 3: The plugin's core mechanism is client-side JavaScript that continuously re-runs `EXPLAIN QUERY PLAN` against the SQL currently in the query editor, updating the page live as the user types
- **Evidence**: First-party README description of the plugin's usage.
- **Confidence**: settled (first-party README, the plugin's own specification)
- **Quote**: "The plugin adds JavaScript to the query editor page which will constantly update the page with information gained from running EXPLAIN QUERY PLAN queries against the entered SQL."
  *(Source: raw.githubusercontent.com/simonw/datasette-explain/main/README.md)*
- **Our assessment**: This is the plugin's one real mechanism, and it is
  narrowly scoped: it does not execute the user's query, only
  `EXPLAIN QUERY PLAN` against it, so it can give feedback (or surface a
  syntax/binding error) before the user runs anything against real data.
  This is a human-facing editor affordance, not an agent tool or API — no
  tool-call schema, no LLM involvement anywhere in the plugin's own
  description.

### Claim 4: The live feedback surfaces either an error message (for invalid SQL) or the query plan together with the names and columns of every table the query touches
- **Evidence**: First-party README description, corroborated by the
  screenshot alt text on the same README.
- **Confidence**: settled (first-party README)
- **Quote**: "This may result in an error message, or it may show the query plan along with any tables used by the query."
  *(Source: raw.githubusercontent.com/simonw/datasette-explain/main/README.md)*
- **Our assessment**: The screenshot's alt text independently confirms the
  same two-table-plus-plan behavior described in prose: "a SQL query shows
  the explain plan as well as the three tables that were used in the query
  (their names and columns)" — i.e., the plugin's stated behavior and its
  own demo screenshot agree, which is the strongest corroboration available
  for a single-author, single-source tool description.

### Claim 5: The plugin is officially described (in the blog post's own metadata and the GitHub repo's page metadata) as validating queries, not just explaining them, even though the README's usage section only describes explaining
- **Evidence**: Cross-comparison of two first-party descriptions of the same
  tool.
- **Confidence**: settled that both descriptions exist verbatim; anecdotal/
  unresolved as to which is the more accurate characterization of current
  behavior
- **Quote**: "Explain and validate SQL queries as you type them into Datasette" *(blog post `og:description` meta tag and the GitHub repository's page-description meta tag)* vs. "Explain SQL queries executed using Datasette" *(README.md, top-line description)*
- **Our assessment**: This is a minor but real inconsistency in a single-
  author project's own self-description: the short tagline used for search/
  social metadata claims a "validate" capability (implying it flags invalid
  or unsafe SQL, not just displays its plan) that the README's longer usage
  section never actually describes — the README only documents plan display
  and error surfacing, which is a byproduct of running `EXPLAIN QUERY PLAN`
  (invalid SQL naturally errors) rather than a distinct validation feature.
  We read "validate" here as marketing shorthand for "you'll see an error
  before you run it," not evidence of a separate validation ruleset.

### Claim 6: datasette-explain's public release history spans three and a half years (Feb 2023 to Sep 2026) across only six tagged releases, with a gap of roughly two and a half years between 0.2.1 (Feb 2024) and 0.2.2 (Sep 2026)
- **Evidence**: Full release history retrieved via the GitHub REST API
  (`api.github.com/repos/simonw/datasette-explain/releases`), which returns
  exact publish timestamps for every tag.
- **Confidence**: settled (directly verifiable via the public API; timestamps
  are GitHub-recorded, not self-reported)
- **Quote**: (no direct quote; see verbatim release list in Concrete
  Artifacts below)
- **Our assessment**: This is a small, low-maintenance-burden plugin: six
  releases total, most of them one-line bug fixes, with a multi-year
  dormant period before this one-bullet patch. It is a useful data point on
  what "actively maintained" means for a single-author Datasette plugin —
  the plugin was not abandoned (it still received a fix in 2026) but it also
  was not under active development for over two years. Nothing in the
  source explains the gap; we do not speculate about cause.

### Claim 7: The prior release (0.2.1, February 2024) added compatibility testing against both the Datasette 0.64.x stable line and the then-new 1.0 alpha series, and migrated the project's packaging from `setup.py` to `pyproject.toml`
- **Evidence**: Verbatim GitHub release body for tag `0.2.1`.
- **Confidence**: settled (first-party changelog, directly verifiable)
- **Quote**: "Now tested against both Datasette 0.64.x and the Datasette 1.0 alphas" / "Switched from `setup.py` to `pyproject.toml`"
  *(Source: GitHub release body, tag `0.2.1`, api.github.com/repos/simonw/datasette-explain/releases)*
- **Our assessment**: This shows that, at least in this February 2024
  release, the plugin's maintenance work explicitly targeted compatibility
  with both a Datasette stable line (0.64.x) and the 1.0 alpha series. The
  corpus does not establish a standing dual-branch maintenance policy for
  Datasette core; the closest related evidence is
  `blog-simonwillison-datasette-1-0a39.md` Claim 6, which documents a single
  security release where fixes landed on main and a selected subset was
  backported to the 0.65.x stable line so both versions shipped the same
  day. Together the two are consistent with stable and alpha lines
  coexisting in the ecosystem. This source shows one plugin release testing
  against both lines, and the other shows one core release shipping to both.
  Neither shows how often that happens.

### Claim 8: A live, publicly-viewable demo of the plugin exists on the author's own hosted Datasette instance, running against his own blog's database
- **Evidence**: README demo link with a pre-filled example query (a join
  across `blog_blogmark`, `blog_blogmark_tags`, and `blog_tag` tables).
- **Confidence**: settled (the link and query are given verbatim in the
  README; not independently re-verified that the live instance currently
  renders the described output)
- **Quote**: "You can see this plugin in action on [datasette.simonwillison.net]" (link text and target URL, README.md, Demo section)
- **Our assessment**: The demo is dogfooding on Willison's own long-running
  public Datasette deployment (the same instance referenced in Claim 2's
  1.0a40 upgrade), rather than a synthetic example — consistent with his
  general pattern of using his own blog's database as the running example
  for Datasette plugin demos across the corpus (e.g., the SQL query used in
  `blog-simonwillison-sqlite-column-provenance.md`'s research also targets
  his own blog schema).

## Concrete Artifacts

### Full blog post text (verbatim, from simonwillison.net/2026/Sep/20/datasette-explain/)

```
Release: datasette-explain 0.2.2 — Explain and validate SQL queries as you
type them into Datasette

  - Explain plans now work on read-only stored-query pages.

I upgraded datasette.simonwillison.net to Datasette 1.0a40, which inspired
me to ship a new version of this explain plugin.

Posted 20th September 2026 at 12:22 am
Tags: sqlite (487), datasette (1,547)
```
*Source: simonwillison.net/2026/Sep/20/datasette-explain/, fetched
2026-09-27 via direct HTML retrieval.*

### README usage description (verbatim, raw.githubusercontent.com/simonw/datasette-explain/main/README.md)

```
# datasette-explain

Explain SQL queries executed using Datasette

## Usage

The plugin adds JavaScript to the query editor page which will constantly
update the page with information gained from running EXPLAIN QUERY PLAN
queries against the entered SQL.

This may result in an error message, or it may show the query plan along
with any tables used by the query.
```
*Source: raw.githubusercontent.com/simonw/datasette-explain/main/README.md,
fetched 2026-09-27.*

### Full public release history (verbatim release bodies, via GitHub REST API `api.github.com/repos/simonw/datasette-explain/releases`)

```
0.2.2  — published 2026-09-20T00:22:04Z
  - Explain plans now work on read-only stored-query pages.

0.2.1  — published 2024-02-28T16:55:58Z
  - Now tested against both Datasette 0.64.x and the Datasette 1.0 alphas
  - README includes a screenshot and a link to a demo
  - Switched from setup.py to pyproject.toml

0.2    — published 2024-02-28T16:35:44Z
  - Fixed a bug where `explain` queries showed an error because you can't
    explain an explain. (#5)

0.1a2  — published 2023-04-24T03:57:18Z
  - Fix for "You did not supply a value for binding parameter" error. (#4)

0.1a1  — published 2023-04-04T19:10:06Z
  - `:param` parameters in SQL queries are now supported. (#3)

0.1a0  — published 2023-02-09T02:06:24Z
  - Initial alpha release. (#1)
```
*Source: api.github.com/repos/simonw/datasette-explain/releases, fetched
2026-09-27. Release bodies are reproduced verbatim except for the removal of
Markdown link syntax around issue numbers and the demo link, which are noted
here as plain text.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-1-0a39.md` Claim 6 (fixes for one
    security release were developed on main, and then a selected subset was
    backported to the 0.65.x stable line so both versions could ship the
    same day): weak corroboration only. That claim documents one
    release's backport decision, not a standing policy. This source's
    Claim 7 is a similarly one-off data point one layer down: a single
    plugin release (0.2.1) that was tested against both a stable line
    (0.64.x) and the 1.0 alphas.
  - `blog-simonwillison-sqlite-column-provenance.md` (introspecting SQL
    structure — source columns, in that case — without necessarily executing
    the query against real data): both sources document Willison building or
    documenting small tools that extract structural information from SQL
    (query plan here; column provenance there) as a pre-execution or
    parallel-to-execution aid, rather than relying solely on running the
    query and inspecting its output.

- **Contradicts**: None filed. Claim 5 notes an internal inconsistency
  between this single source's own tagline ("validate") and its own README
  body ("explain" only) — this is the source disagreeing with itself in the
  sense described by MINER.md §4a, but it is a minor marketing-copy
  imprecision about a niche single-author tool's feature set, not a claim
  that would lead to different guide advice either way. Per MINER.md §4a
  ("one side is so weakly supported it doesn't rise to a real claim"), no
  contradiction issue was filed.

- **Extends**:
  - `blog-simonwillison-lobsters-sqlite-migration.md` Claims 6–7. Claim 6
    there documents a production incident: the first Lobsters SQLite
    deploy was reverted after read-only traffic spiked every CPU to 100%.
    The cause, found later, was "SQLite doing full table scans on the
    largest tables in the database for 2 of queries". Claim 7 records the
    engineer's wish to "Fail if you encounter any full table scans" in a
    test. A commenter answers that SQLite bytecode-instruction counts can
    serve as a proxy for query-plan shape. That note and this source
    tackle the same problem: catching a bad SQLite query plan (such as a
    full table scan) before it reaches production. They take different
    approaches:
    - **datasette-explain (this source)** is human-facing and live. It
      shows the `EXPLAIN QUERY PLAN` output while a person is writing the
      query in an editor. Catching a problem depends on someone reading
      the plan and noticing the scan.
    - **Lobsters Claim 7** is an automated CI check. A test fails based
      on plan-shape evidence, with no human reading the plan. The same
      note's Claim 7 assessment adds a caveat: the check is only reliable
      against sufficiently large test tables.

    The live-display approach would not have prevented the Lobsters
    incident unless someone had explicitly inspected those specific
    queries. That limitation is why the automated approach matters more
    for regression-proofing. It is also why this source doesn't change
    the Guide Impact verdict below.

- **Novel**: First corpus documentation of datasette-explain and of a
  "constantly re-run EXPLAIN QUERY PLAN as the user types" interaction
  pattern for a SQL editor. This is a narrow, human-facing (not agent-facing)
  tool, so its novelty to the corpus does not translate into novelty for
  AI-native engineering practice — see Guide Impact.

## Guide Impact

- **No chapter change recommended.** This source documents a small,
  single-author Datasette plugin that gives a *human* editing SQL by hand
  live feedback from `EXPLAIN QUERY PLAN`. It contains no AI-agent
  involvement, no LLM-assisted workflow, and no metric, incident, or
  practice that generalizes to AI-native engineering — all three Prospector
  triage comments on the source issue independently reached the same "low
  novelty / minimal-to-no chapter relevance" conclusion, and deep reading
  (README, full release history, GitHub API data) did not surface anything
  beyond what the triage comments anticipated. The closest analogy — giving
  a user pre-execution feedback on SQL correctness before it runs — is a
  generic "fast feedback loop" idea already covered in the corpus by
  agent-facing tools (e.g., the permission/approval-dialog pattern in
  `blog-simonwillison-datasette-agent-write-sql.md`), which are a better fit
  for Ch02/Ch03 citations than this human-only editor aid.

## Extraction Notes

- **The entry-point beat is thin by design** (Willison's short-form release
  format), consistent with the "novelty: low" assessment three separate
  Prospector triage comments converged on for this issue. Per MINER.md §1,
  the linked GitHub release page and the plugin's README were both read to
  extend the note beyond the two-sentence beat.
- **The GitHub release page's static HTML carries no readable release body**
  — it is a client-rendered React application; only Open Graph/Twitter meta
  tags are present in the raw HTML (confirmed by direct `curl` retrieval and
  grep across the full page source). The full six-release history used in
  Claims 6–7 and the Concrete Artifacts section was instead retrieved via
  the public, unauthenticated GitHub REST API
  (`api.github.com/repos/simonw/datasette-explain/releases`), which returns
  the release Markdown bodies as JSON — the same text as the rendered page,
  just accessible without JavaScript execution.
- **No contradiction issue filed.** See Cross-References → Contradicts.
- **Confidence rationale**: `confidence_overall` is `settled` because every
  claim in this note is a directly verifiable first-party statement (blog
  post text, README text, or GitHub API release data) about a tool whose
  entire specification is these same first-party sources — there is no
  higher-level, contested, or unverified thesis in this source the way there
  is in, e.g., `blog-simonwillison-datasette-1-0a39.md`'s audit-methodology
  claims. The *guide relevance* of these settled facts is separately judged
  to be minimal (see Guide Impact), which is a novelty judgment, not a
  confidence judgment.
- **Existing-notes search**: Searched `source-notes/` for prior
  datasette-explain coverage (none found) and for adjacent SQL-introspection
  and query-plan concepts (`blog-simonwillison-sqlite-column-provenance.md`,
  `blog-simonwillison-datasette-agent-write-sql.md`, and
  `blog-simonwillison-lobsters-sqlite-migration.md`, all reviewed in full
  for the Cross-References above).
