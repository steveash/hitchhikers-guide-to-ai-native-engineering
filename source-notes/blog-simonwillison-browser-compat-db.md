---
source_url: https://simonwillison.net/2026/Jun/24/browser-compat-db/
source_type: blog-post
title: "simonw/browser-compat-db"
author: Simon Willison
date_published: 2026-06-24
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: anecdotal
issue: "#1391"
---

# simonw/browser-compat-db

> Simon Willison converts Mozilla's `mdn/browser-compat-data` into a normalized,
> idempotent SQLite database — using Claude Code (Opus 4.8) to write the Python
> importer and a separate model, Codex Desktop (GPT-5.5), to write the GitHub
> Actions publishing workflow — and hosts the resulting ~66MB database on a
> force-pushed GitHub "orphan" branch specifically to get free, open-CORS,
> CDN-backed hosting that GitHub Releases doesn't provide. The project is
> explicitly framed as inspired by Mozilla's own MDN MCP server, whose launch
> post supplies a concrete, quoted example of an AI coding agent fabricating
> browser-support facts from stale training data — and of an MCP tool call
> fixing both the accuracy and the latency of that lookup.

## Source Context

- **Type**: blog-post (Simon Willison's link-blog, ~140 words of original
  commentary across four short paragraphs, published 2026-06-24; auto-discovered
  via trusted feed `simon-willison`). The post is a "link post" that points at a
  GitHub repository (`simonw/browser-compat-db`) as its real substance. Per
  MINER.md §1, this note follows the linked repository (README, `build_db.py`,
  the GitHub Actions workflow YAML, `notes.md`) and the linked Mozilla blog post
  that the project says it was inspired by
  (`developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/`) as substantive
  linked pages.
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  `sqlite-utils`, and the `llm` CLI, and a designated `trusted-feed` source in
  this repo. This is a first-person account of his own hobby project with a
  publicly verifiable GitHub repository, commit history, and a working demo
  (Datasette Lite pointed at the hosted database). No vendor affiliation to
  either Anthropic or OpenAI is disclosed or implied — he uses tools from both
  in the same project.
- **Scope**: Covers (1) using Claude Code for web (Opus 4.8) to generate a
  Python/Pydantic/sqlite-utils importer script that normalizes MDN's
  browser-compat-data JSON into a relational SQLite schema; (2) using a second,
  different tool — Codex Desktop (GPT-5.5) — to write the GitHub Actions
  workflow that builds and publishes that database; (3) the GitHub "orphan
  branch + force-push" technique for hosting a large binary artifact with open
  CORS headers via the GitHub CDN, as an alternative to GitHub Releases; (4) the
  Mozilla MDN MCP server that inspired the project, including Mozilla's own
  before/after accuracy and latency comparison of Claude Code with and without
  that MCP server. Does NOT cover: the internals of the MDN MCP server's
  implementation, Datasette Lite's architecture, or any cost/pricing discussion
  of the models used.

## Extracted Claims

### Claim 1: Willison used Claude Code for web (Opus 4.8) to generate the entire Python importer that transforms MDN's nested browser-compat-data JSON into a normalized SQLite database

- **Evidence**: Direct statement in the post, naming the specific tool and model.
  The linked script (`build_db.py`, 300+ lines) is public and was independently
  read for this note: it defines Pydantic models for schema validation, a
  recursive tree-walker (`CompatParser._walk`) that discovers arbitrarily nested
  `__compat` nodes, and idempotent upsert/prune logic (`sync_table`) built on
  `sqlite-utils`.
- **Confidence**: anecdotal (single practitioner, one project; but the generated
  artifact is public and independently inspectable, unlike most "AI wrote this"
  claims in the corpus)
- **Quote**: "This new GitHub repo includes a Claude Code for web (Opus 4.8) generated script for doing that using sqlite-utils."
- **Our assessment**: Unlike many AI-generated-code claims in this corpus, the
  artifact here is fully public and was read directly for this extraction
  (see Concrete Artifacts). It is not a toy script: it handles three distinct
  support-value shapes in the upstream data (a literal `"mirror"` string, a
  single support-statement object, or an array mixing strings and objects — see
  Claim 7), validates every record through Pydantic before writing it, and
  implements sync-with-deletion semantics rather than a naive drop-and-rebuild.
  This is a concrete, verifiable data point for "Claude Code can write a
  production-quality ETL script from a single generation," which is a stronger
  claim than most vibe-coding anecdotes in the corpus because the artifact's
  correctness is independently checkable against the upstream JSON schema.

### Claim 2: Willison used a second, different AI tool — Codex Desktop (GPT-5.5) — specifically to write the GitHub Actions workflow, splitting the project across two vendors by task type rather than by implement/review role

- **Evidence**: Direct statement naming the specific tool and model, immediately
  following the Claude Code attribution for the Python script. The linked
  workflow YAML (`.github/workflows/build-db.yml`) was independently read: it
  installs `uv`, clones the upstream data repo with `git clone --depth 1`,
  runs the importer, then publishes the output by creating a fresh orphan
  branch in a temp directory and force-pushing it.
- **Confidence**: anecdotal (single practitioner, one project)
- **Quote**: "I wanted the resulting ~66MB SQLite database to be available via the GitHub CDN with open CORS headers. GitHub releases don't have those, but any file stored in a regular GitHub repository does - so I had Codex Desktop (GPT-5.5) build a GitHub Actions workflow that builds the database and then force-pushes it to a db \"orphan\" branch."
- **Our assessment**: This is a different multi-model pattern than the one
  documented in `blog-simonwillison-csrf-multimodel-review.md` Claims 1–2, where
  Willison used Claude Code to implement and GPT-5.4 to cross-review the *same*
  change. Here there is no review relationship between the two models at all —
  Claude Code and Codex Desktop each own a disjoint deliverable (data-transform
  logic vs. CI/CD YAML) with no stated overlap or cross-check. This is
  task-type routing, not a generator/verifier pair, and it is a distinct pattern
  worth keeping separate from the cross-review pattern in the guide: it argues
  for picking whichever tool/model a practitioner has handy or trusts for a
  given *kind* of artifact (data pipeline code vs. YAML/infra glue), not for
  running two models over the same output.

### Claim 3: A force-pushed GitHub "orphan" branch is used specifically to obtain open-CORS, CDN-backed hosting for a large binary artifact, which GitHub Releases does not provide

- **Evidence**: Direct statement of the motivating constraint (open CORS headers
  needed; Releases don't have them; regular repository files do) followed by the
  chosen mechanism (orphan branch, force-pushed). The workflow YAML, read
  directly, confirms the mechanism: it creates a fresh git repo in a temp
  directory (`git checkout --orphan db`), commits only the built database file,
  and force-pushes that single commit to the `db` branch on every run
  (`git push --force origin db`), which keeps the branch's history — and
  therefore the repository's stored size — from growing on each rebuild.
- **Confidence**: anecdotal (Willison's specific technique is one practitioner's
  choice; the underlying platform fact — that GitHub serves raw repository blobs
  with open CORS headers but Release assets do not — is a verifiable, stated
  constraint driving the design, not a general claim being advanced as best
  practice)
- **Quote**: "GitHub releases don't have those, but any file stored in a regular GitHub repository does - so I had Codex Desktop (GPT-5.5) build a GitHub Actions workflow that builds the database and then force-pushes it to a db \"orphan\" branch."
- **Our assessment**: This is a genuinely novel deployment pattern for this
  corpus: hosting a periodically-rebuilt binary data artifact for free, with
  browser-side CORS access, using only GitHub as infrastructure — no S3 bucket,
  no CDN service, no Releases API. The `--orphan` branch plus `--force` push is
  the detail that makes it sustainable: because the branch's history is
  discarded and replaced on every build rather than accumulating a new 66MB
  commit each time, the repository doesn't grow unboundedly across rebuilds.
  This is a specific, transferable technique for any AI-native workflow that
  needs to publish a machine-generated data artifact (embeddings, indexes,
  scraped datasets, eval results) for other agents or browser-side tools to
  fetch without a hosting bill.

### Claim 4: The hosted database is directly explorable in-browser via Datasette Lite because it is served with open CORS headers, requiring no server component

- **Evidence**: Direct statement with a working, linked demo URL
  (`lite.datasette.io/?url=https://github.com/simonw/browser-compat-db/blob/db/browser-compat.db#/browser-compat/releases_tree`).
- **Confidence**: anecdotal (single practitioner's demonstrated setup, but the
  demo link is independently checkable)
- **Quote**: "You can download the resulting database from here, and since it's hosted with open CORS headers you can also explore it with Datasette Lite."
- **Our assessment**: This closes the loop on Claim 3 — the CORS requirement
  wasn't incidental, it was specifically so that a purely client-side tool
  (Datasette Lite runs SQLite via WASM in the browser) could fetch and query the
  database with no backend at all. Combined with `blog-simonwillison-sqlite-utils-40rc1.md`
  Claim 11's "capability evolution arc" (read-only data publishing →
  agent-readable SQL → agent-writable SQL → user app-hosting), this project sits
  at the "agent-readable SQL" rung: a bulk dataset published once, then queried
  ad hoc by humans or agents via SQL, as a complement to the MDN MCP server's
  live, per-query lookups (see Claim 10).

### Claim 5: The importer is idempotent — re-running it against a refreshed checkout of the upstream data repository syncs additions, edits, and deletions in place on the same database file

- **Evidence**: Stated directly in the repository README (a linked, substantive
  page followed per MINER.md §1) and confirmed by reading `build_db.py`'s
  `sync_table` function, which calls `table.upsert_all(..., alter=True)` and
  then computes and deletes the set of primary keys present in the table but
  absent from the newly parsed records.
- **Confidence**: settled (the mechanism was independently verified by reading
  the actual code, not just asserted by the source)
- **Quote**: "The importer is idempotent. Pull the latest `main` in the data repo and run it again against the same database file: features, releases and browsers that were added, changed or removed upstream are all synced in place."
- **Our assessment**: This is a specific, checkable correctness property of the
  AI-generated script, not just a functionality claim — the README additionally
  states this was verified by "importing an old commit, then a newer `main`, on
  the same database file (feature/release counts went up, `support_flags` went
  down as expected, and features removed upstream disappeared)"
  (source: repository `notes.md`). For a script substantially generated by
  Claude Code, having an explicit sync-then-verify test of the delete path
  clears a meaningfully higher bar than most single-shot AI-generated ETL
  scripts in this corpus, and it is the property that makes the GitHub
  Actions rebuild-on-every-push workflow (Claim 2) safe to run unattended.

### Claim 6: Every parsed record is validated through Pydantic models before it reaches the database, so an upstream change to MDN's JSON schema surfaces as a loud validation error rather than silently corrupting the import

- **Evidence**: Stated directly in the README and confirmed in `build_db.py`,
  where both `parse_browsers` and `CompatParser._add_feature` wrap
  `Model.model_validate(raw)` in a `try/except ValidationError` that raises
  `SystemExit` with the offending file path and validation error attached.
- **Confidence**: settled (verified directly in code, not just asserted)
- **Quote**: "[`build_db.py`](build_db.py) loads a checkout of the MDN browser-compat-data repository into a normalized SQLite database. Every record is validated through [Pydantic models](models.py) first, so if MDN changes the shape of the data the import fails loudly."
- **Our assessment**: This is a specific, load-bearing design decision that
  distinguishes robust AI-generated data-pipeline code from brittle
  AI-generated data-pipeline code: rather than trusting the shape of
  externally-controlled upstream JSON, every record round-trips through an
  explicit schema before being written. For AI-native engineering guidance:
  when an AI agent is asked to build an importer over a data source it does not
  control, requiring (or prompting for) fail-loud schema validation at the
  parse boundary is the difference between "silently ships bad data" and
  "breaks the build the moment the upstream shape changes" — the latter is
  strictly preferable for unattended, scheduled pipelines like the one in
  Claim 2's GitHub Actions workflow.

### Claim 7: The importer correctly normalizes three structurally different shapes that the same "browser support" field can take in the upstream JSON — a literal `"mirror"` string, a single support-statement object, or an array mixing strings and objects — into one flat, typed `support` table

- **Evidence**: Documented in the repository's `notes.md` working notes and
  independently confirmed by reading the `_add_support` method in
  `build_db.py`, which branches on `statement == "mirror"` vs. a
  `SimpleSupportStatement` instance vs. iterating a list of either.
- **Confidence**: settled (verified directly in both the documentation and the
  code)
- **Quote**: "A browser's support value is one of three shapes: 1. The literal string `"mirror"` — "mirror whatever the upstream browser does" (e.g. `chrome_android` mirroring `chrome`). Resolving this fully requires the upstream build logic; we store it faithfully as `is_mirror = 1` rather than resolving it. 2. A single **simple support statement** object. 3. An **array** mixing strings and objects (multiple support ranges / history)."
- **Our assessment**: This is a concrete illustration of AI-generated code
  correctly handling a real-world "stringly-typed union" data-modeling problem
  — a field that is sometimes a bare string, sometimes an object, sometimes a
  heterogeneous array — without requiring the practitioner to spell out the
  full type union up front. `notes.md` also records that this shape survey was
  itself a deliberate, documented investigation step ("Working notes captured
  while building the importer"), suggesting the schema-discovery process, not
  just the final code, was part of what Claude Code produced or that Willison
  captured alongside it.

### Claim 8: Mozilla's own before/after testing found that Claude Code without the MDN MCP server got browser-support facts right in only 1 of 4 tested cases, in one instance fabricating specific incorrect browser version numbers

- **Evidence**: Direct, first-party comparison from the Mozilla blog post that
  this project cites as its inspiration (`developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/`,
  published 2026-06-15, authored by "The MDN Team"). Mozilla tested Claude Code
  Opus 4.7 with and without the MDN MCP on four specific, recently-shipped
  Firefox 151 features (the `light-dark()` CSS function, the `:buffering` CSS
  pseudo-class, the `shadowrootslotassignment` `<template>` attribute, and the
  Web Serial API), asking usage and browser-support questions for each.
- **Confidence**: emerging (first-party but small-sample: four features, one
  model, one vendor's own MCP server being evaluated by that same vendor —
  directionally credible but not independently replicated)
- **Quote**: "Claude Code without the MCP got the browser support right only in one case: for the `:buffering` pseudo-class."
- **Quote (fabrication example)**: "Claude Code without the MCP insisted that the declarative shadowrootslotassignment attribute is supported in Chrome 120 and Safari 18.3, possibly conflating it with the Element.attachShadow()'s slotAssignment option. But in fact, Firefox 151 is the first browser to ship support for this attribute."
- **Our assessment**: The `shadowrootslotassignment` example is a concrete,
  named instance of confident, specific-sounding fabrication (exact browser
  version numbers, for browsers that don't actually support the feature) driven
  by training-data staleness rather than a vague "I'm not sure" hedge — exactly
  the failure mode that makes ungrounded LLM answers about fast-moving
  platform facts dangerous to trust at face value. This is a stronger, more
  concrete example than a generic "training cutoff" warning because it names
  the specific wrong browsers and versions the model asserted.

### Claim 9: Mozilla found that MCP-grounded responses were roughly twice as fast as ungrounded responses, because without the MCP the agent had to fetch and parse multiple full HTML pages to find the same information — and even then got it wrong

- **Evidence**: Direct statement from the same Mozilla blog post, describing the
  mechanism (HTML fetch-and-parse loop) behind the latency difference, not just
  the latency number itself.
- **Confidence**: emerging (first-party, small-sample, single vendor evaluating
  its own tool — but the stated mechanism, that raw web-fetch-and-parse is
  slower than a purpose-built tool call, is independently plausible)
- **Quote**: "we noticed that in our tests, responses which used the MDN MCP were roughly twice as fast. Without the MCP, Claude Code had to fetch and parse quite a few HTML pages to find current information, which took some time, but even then didn't provide accurate results."
- **Our assessment**: This is a two-for-one result worth separating from Claim 8:
  it is not just that grounding via MCP improved accuracy at a latency cost (the
  usual trade-off framing), but that the *ungrounded* path was simultaneously
  slower and less accurate, because it substituted a general-purpose web-fetch
  loop for a purpose-built, structured tool call. For practitioners deciding
  whether an MCP integration is worth building versus letting the agent fall
  back to ad hoc web fetching: this is evidence that a well-scoped MCP tool can
  dominate on both axes at once rather than trading one for the other.

### Claim 10: The MDN MCP server is deployed as a public, remote, HTTP-transport MCP endpoint, and is explicitly compatible with editors (VS Code, Zed, Cursor), agent CLIs (Claude Code, Codex CLI, Antigravity CLI), and chat apps (Claude Desktop)

- **Evidence**: Direct installation instructions and a named client-compatibility
  list from the Mozilla blog post.
- **Confidence**: settled (first-party, directly verifiable technical fact —
  install command and named client list)
- **Quote**: "The MDN MCP server works with any MCP-compatible client, including: Editors: VS Code, Zed, and Cursor. Agent CLIs: Claude Code, Codex CLI, and Antigravity CLI (previously Gemini CLI). Chat apps: Claude Desktop."
- **Our assessment**: This corroborates `blog-anthropic-mcp-production-agents.md`
  Claim 5 ("Build remote servers so agents can use your system wherever they
  run") with a real-world instance from outside Anthropic: Mozilla, a major
  documentation provider, chose a remote HTTP MCP server
  (`https://mcp.mdn.mozilla.net/`, added via `claude mcp add --transport http`)
  over a local stdio server, specifically so the same server could serve any
  MCP-compatible client rather than requiring a per-tool integration. This is
  independent confirmation, from a production deployment by a different
  organization, that the "remote over local stdio" guidance in the Anthropic
  post is being followed in practice by third parties building MCP servers
  for a broad client audience.

### Claim 11: Willison frames the SQLite-export project as directly inspired by Mozilla's MDN MCP server launch, producing a bulk/offline data-access pattern for the same underlying dataset that the MCP serves as live, per-query lookups

- **Evidence**: The opening sentence of the post explicitly names the MDN MCP
  service as the inspiration and links both the announcement and its source
  code before describing the SQLite conversion.
- **Confidence**: anecdotal (stated motivation from one practitioner)
- **Quote**: "Inspired by Mozilla's new MDN MCP service - source code here - I decided to try converting their comprehensive mdn/browser-compat-data repository full of browser compatibility data into a SQLite database."
- **Our assessment**: The MCP server and the SQLite export are not competing
  solutions to the same problem — they are complementary access patterns for
  the same source dataset. The MCP server is optimized for single, live,
  per-question lookups embedded in an agent's reasoning loop (as in Claim 8's
  "does browser X support feature Y" queries). The SQLite database is optimized
  for bulk, ad hoc, or aggregate queries that would be prohibitively slow or
  expensive as a sequence of individual tool calls — e.g., "which CSS features
  are unsupported in the most browsers" or "list every experimental API feature
  added in the last year," which are single SQL queries against the exported
  database but would require many round-trip MCP calls (or none at all, if the
  MCP doesn't expose a bulk/aggregate query tool) otherwise. The guide should
  treat "does this dataset need an MCP server, a bulk export, or both" as a
  genuine design decision rather than assuming MCP subsumes bulk access.

## Concrete Artifacts

### GitHub Actions workflow: build + publish to an orphan branch (verbatim, from `.github/workflows/build-db.yml`)

```yaml
# Source: github.com/simonw/browser-compat-db/blob/main/.github/workflows/build-db.yml
# Attributed by the blog post to Codex Desktop (GPT-5.5)

      - name: Clone browser-compat-data
        run: |
          rm -rf /tmp/browser-compat-data
          git clone --depth 1 https://github.com/mdn/browser-compat-data.git /tmp/browser-compat-data

      - name: Build database
        run: |
          rm -f browser-compat.db
          uv run build_db.py /tmp/browser-compat-data --db browser-compat.db

      - name: Publish database branch
        run: |
          publish_dir="$(mktemp -d)"
          cp browser-compat.db "$publish_dir/browser-compat.db"

          git -C "$publish_dir" init
          git -C "$publish_dir" checkout --orphan db
          git -C "$publish_dir" config user.name "github-actions[bot]"
          git -C "$publish_dir" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git -C "$publish_dir" add browser-compat.db
          git -C "$publish_dir" commit -m "Build browser-compat.db"
          git -C "$publish_dir" remote add origin "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
          git -C "$publish_dir" push --force origin db
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Idempotent sync-with-deletion logic (verbatim, from `build_db.py`)

```python
# Source: github.com/simonw/browser-compat-db/blob/main/build_db.py
# Attributed by the blog post to Claude Code for web (Opus 4.8)

def sync_table(
    db: sqlite_utils.Database,
    name: str,
    records: List[dict],
    pk,
    foreign_keys=None,
) -> None:
    """Upsert all records, then delete rows whose PK is no longer present.

    This keeps the table in sync with the source on every run, handling
    additions, updates and deletions without recreating the database.
    """
    table = db[name]
    if not records:
        if table.exists():
            table.delete_where()
        return

    table.upsert_all(records, pk=pk, foreign_keys=foreign_keys or [], alter=True)

    pk_cols = [pk] if isinstance(pk, str) else list(pk)
    current_keys = {
        tuple(r[c] for c in pk_cols) for r in records
    }
    existing = list(
        table.rows_where(select=", ".join(f'"{c}"' for c in pk_cols))
    )
    to_delete = [
        tuple(row[c] for c in pk_cols)
        for row in existing
        if tuple(row[c] for c in pk_cols) not in current_keys
    ]
    if to_delete:
        where = " AND ".join(f'"{c}" = ?' for c in pk_cols)
        with db.conn:
            for key in to_delete:
                db.conn.execute(
                    f'DELETE FROM "{name}" WHERE {where}', key
                )
```

### Resulting dataset scale (from the repository README, generated by `cog`)

```
Table              Rows
browsers             17
browser_releases  1,599
features         19,834
feature_tags     16,210
feature_spec_urls 17,321
support         260,715
support_flags       885
metadata               4

Source: github.com/simonw/browser-compat-db (README.md, "Tables and row counts")
Database size: ~66MB
browser-compat-data version imported: 8.0.4
```

### Mozilla's MCP-vs-no-MCP failure example (verbatim, from developer.mozilla.org)

```
Question tested: "How to use the shadowrootslotassignment attribute on
<template> and which browsers support it?"

Without MDN MCP (Claude Code Opus 4.7):
  "Claude Code without the MCP insisted that the declarative
  shadowrootslotassignment attribute is supported in Chrome 120 and
  Safari 18.3, possibly conflating it with the Element.attachShadow()'s
  slotAssignment option."

Actual: Firefox 151 is the first browser to ship support for this
attribute.

Without MDN MCP, on the Web Serial API question, Claude Code additionally
stated Firefox support was:
  Not implemented (and not on the roadmap — see Mozilla's standards
  position: "harmful")
  — also incorrect; Firefox 151 shipped Web Serial API support in May 2026.

Source: developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/
("What difference does the MCP make?" section)
```

### MDN MCP installation (verbatim, from developer.mozilla.org)

```bash
# Source: developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/
claude mcp add --transport http mdn https://mcp.mdn.mozilla.net/
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 5 ("Build remote servers so
    agents can use your system wherever they run"): the MDN MCP server is a
    named, third-party (non-Anthropic) production instance of exactly this
    architecture choice — a public remote HTTP MCP endpoint rather than a local
    stdio server — deployed by Mozilla specifically to support a broad,
    named list of heterogeneous clients (see Claim 10).
  - `blog-simonwillison-sqlite-utils-40rc1.md` overall: this project is a
    concrete, independently-read practitioner use of `sqlite-utils` (via
    `upsert_all`, `delete_where`, and index/vacuum calls in `build_db.py`) for
    exactly the kind of AI-native data pipeline that note's Guide Impact
    section recommends `sqlite-utils` for. This source does not use the v4
    migrations system from that note, but does use the same underlying
    `Database`/table API.

- **Contradicts**: None identified. No existing corpus note makes claims about
  GitHub artifact hosting, MCP-vs-training-data accuracy, or multi-model task
  division that this source conflicts with. No contradiction issue required.

- **Extends**:
  - `blog-simonwillison-csrf-multimodel-review.md` Claims 1–2 (Claude Code
    implements, GPT-5.4 cross-reviews the same production security change):
    this source documents a structurally different multi-model pattern —
    task-type routing with no review relationship between the two models
    (Claim 2 of this note) — broadening the corpus's multi-model taxonomy
    beyond the generator/verifier pairing that Claim 2 of the CSRF note
    established as the only documented instance.
  - `blog-simonwillison-liteparse-browser.md` Claim 13 (GitHub Pages + Vite +
    GitHub Actions, fully delegated to a separate Claude Code session) and
    `blog-simonwillison-moebius-browser.md` Claim 11 (Claude Code autonomously
    publishing large model weights to Hugging Face): both document delegating
    an entire deployment/publishing pipeline to an AI coding tool. This source
    extends the pattern with a specific, novel hosting trick within that
    delegated pipeline — the orphan-branch-plus-force-push technique for
    getting free, CORS-enabled, unbounded-size-safe hosting of a periodically
    rebuilt binary artifact directly from GitHub, without an external storage
    service (Claim 3).
  - `blog-simonwillison-sqlite-utils-40rc1.md` Claim 11's "capability evolution
    arc" for Datasette (read-only publishing → agent-readable SQL →
    agent-writable SQL → app-hosting): this source is a concrete instance
    sitting at the "agent-readable SQL" rung, complementary to (not competing
    with) the MDN MCP server's live per-query access (Claim 11 of this note).

- **Novel**:
  - **Orphan-branch-plus-force-push as free CORS-enabled binary hosting**: no
    existing corpus source documents using a force-pushed GitHub orphan branch
    as a hosting mechanism for a periodically rebuilt data artifact, or names
    the specific constraint (Releases lack open CORS headers; regular repo
    files have them) that motivates it.
  - **Task-type multi-model routing with no review relationship**: no existing
    corpus source documents splitting a single project across two different
    AI coding tools by disjoint task type (data-pipeline code vs. CI/CD YAML)
    with neither tool reviewing the other's output — distinct from every
    other multi-model pattern in the corpus, which pairs models in
    generator/verifier or planner/implementer roles.
  - **Concrete, named example of MCP grounding fixing simultaneous accuracy and
    latency failures**: no existing corpus source documents a first-party,
    before/after comparison naming the specific fabricated facts (wrong browser
    names and version numbers) that an ungrounded coding agent produced on a
    fast-moving technical domain, paired with a stated latency mechanism
    (HTML fetch-and-parse fallback) for why the ungrounded path was also slower.
  - **MCP server and bulk data export as complementary, not competing, agent
    data-access patterns for the same dataset**: no existing corpus source
    frames this design choice explicitly (Claim 11).

## Guide Impact

- **Chapter 02 (Harness Engineering — Deployment/hosting patterns)**: Add the
  orphan-branch-plus-force-push technique (Claim 3, Concrete Artifacts →
  GitHub Actions workflow) as a named option for hosting periodically-rebuilt,
  machine-generated binary artifacts (datasets, indexes, eval snapshots) that
  need public, CORS-enabled, CDN-backed access without provisioning external
  storage. Note the specific reason GitHub Releases doesn't work for this use
  case (no open CORS headers) so practitioners understand when to reach for
  this pattern versus Releases versus external object storage.

- **Chapter 02 (Harness Engineering — Multi-model workflows)**: Add task-type
  model routing (Claim 2) as a third multi-model pattern alongside the
  generator/verifier pairing already documented via
  `blog-simonwillison-csrf-multimodel-review.md`. Recommend the guide
  explicitly distinguish "two models split disjoint tasks with no
  cross-checking" from "two models work the same task in generator/reviewer
  roles" — they carry different reliability guarantees and the guide currently
  only documents the latter.

- **Chapter 04 (Context Engineering — Grounding vs. training-data staleness)**:
  Add Mozilla's MDN MCP before/after comparison (Claims 8–9) as a concrete,
  quotable example of the "stale training data" failure mode for fast-moving
  technical domains (browser/platform compatibility), including the specific
  fabricated-fact example (`shadowrootslotassignment` falsely attributed to
  Chrome 120/Safari 18.3). Pair with Claim 9's finding that the MCP-grounded
  path was also faster, to argue against treating grounding as a pure
  accuracy/latency trade-off.

- **Chapter 04 (Context Engineering — Bulk vs. live data access for agents)**:
  Add Claim 11's framing — MCP servers for live per-query lookups, bulk
  exports (e.g., SQLite/Datasette) for aggregate or ad hoc queries over the
  same dataset — as a design consideration when deciding whether a data source
  needs an MCP server, a bulk export, or both.

## Extraction Notes

- **Primary source is a short link post; the substance is in linked pages**:
  The blog post itself is four short paragraphs. Per MINER.md §1, this note
  follows the linked GitHub repository (README, `build_db.py`, the GitHub
  Actions workflow YAML, `notes.md`) and the linked Mozilla MDN MCP
  announcement post, all fetched and read directly (not summarized by an
  intermediary tool) via `curl`, except where noted below.
- **Verbatim text obtained directly, not via AI summarization, for the primary
  sources**: The blog post HTML, the GitHub repository files (README,
  `build_db.py`, workflow YAML, `notes.md`), and the MDN MCP blog post HTML
  were all fetched directly (via `curl`) and parsed for exact text, rather than
  relying on an AI-summarization fetch tool for quote extraction. This avoids
  the paraphrase risk that comes with LLM-mediated content extraction; all
  quotes in this note were copied character-for-character from the fetched raw
  text. Note that the model tested in the MDN MCP comparison (Claims 8–9) is
  "Claude Code Opus 4.7", per the MDN blog post's own text — a different model
  from the "Claude Code for web (Opus 4.8)" that Willison used for the SQLite
  importer (Claim 1); the two posts are by different authors on different dates
  and there is no inconsistency to reconcile, just two separate tools used in
  two separate projects.
- **Commit history reviewed**: The repository's commit log (7 commits, all by
  Simon Willison, 2026-06-24) was reviewed via the GitHub API to confirm no
  human commits materially altered the AI-generated script or workflow after
  the initial generation; commit messages ("Add normalized SQLite importer...",
  "GitHub Actions to build database", "Better README...") are consistent with
  the sequence described in the blog post.
- **No contradictions filed**: No existing corpus source makes claims that
  conflict with this source's content (see Cross-References → Contradicts).
- **Cross-references verified**: All claim numbers cited from other source
  notes were verified by reading the respective notes and counting `### Claim`
  headings in document order before citing (per MINER.md §4b):
  `blog-anthropic-mcp-production-agents.md` Claim 5 confirmed as the 5th
  `### Claim:` heading; `blog-simonwillison-csrf-multimodel-review.md` Claims
  1–2 confirmed as the 1st and 2nd headings; `blog-simonwillison-liteparse-browser.md`
  Claim 13 confirmed as the 13th heading; `blog-simonwillison-moebius-browser.md`
  Claim 11 confirmed as the 11th heading; `blog-simonwillison-sqlite-utils-40rc1.md`
  Claim 11 confirmed as the 11th heading.
- **Confidence set to anecdotal overall**: The core project claims (Claims
  1–7, 11) are a single practitioner's account of one hobby project, though
  several (Claims 5–7) were independently verified against the actual code
  rather than taken on the author's word alone. The Mozilla MCP comparison
  (Claims 8–10) is first-party vendor testing on a four-feature sample —
  directionally useful but not independently replicated, hence rated
  `emerging` rather than `settled` at the individual-claim level. The overall
  note confidence is set to the more conservative `anecdotal` to reflect that
  the majority of claims rest on a single source's single project and a
  single vendor's small-sample internal test.
