---
source_url: https://simonwillison.net/2026/Aug/12/alchemy-utils/
source_type: blog-post
title: "Release: alchemy-utils 0.1a0"
author: Simon Willison
date_published: 2026-08-12
date_extracted: 2026-08-22
last_checked: 2026-08-22
status: current
confidence_overall: anecdotal
issue: "#2854"
---

# Release: alchemy-utils 0.1a0

> Simon Willison tasks two coding agents (Codex and "GPT-5.6 Sol Ultra") with a
> single "research spike" prompt to build a SQLAlchemy-backed, multi-database
> port of his sqlite-utils library. The two-sentence blog post is a thin
> wrapper; the substance is a 1,060-line exported Codex session transcript
> (linked gist) showing the agent self-initializing a repo, doing red/green
> TDD across three real database engines, self-refactoring on a one-line human
> nudge, catching two of its own bugs in a self-initiated final review, and —
> during an unprompted rename/cleanup pass — moving the user's real 780 KB
> DuckDB database file, mistaking it for disposable test output. A follow-up
> commit (also fetched directly) shows Codex fixing a ~100x bulk-insert
> performance regression by switching CSV reads from full-file materialization
> to a streaming generator with batched writes.

## Source Context

- **Type**: blog-post (Willison "beat"/release-announcement format — a
  dateline, one paragraph, one blockquoted prompt, two CLI examples, and a
  closing performance note). As with several other Willison posts already in
  this corpus (see `blog-simonwillison-datasette-blog-codex-session.md`), the
  post itself is a thin pointer; the substantive material is in two linked
  artifacts that were fetched and read in full for this extraction:
  1. A GitHub Gist (`gist.github.com/simonw/bd10e4886688e0fd1b833e4afaabf19e`)
     — the full exported Codex session transcript covering four top-level
     human prompts and the agent's complete intermediate tool-call log.
  2. A GitHub commit (`github.com/simonw/alchemy-utils/commit/e3b8d03e...`)
     — the actual diff for the "had Codex optimize it" performance fix
     mentioned in the blog post's closing line.
- **Author credibility**: Simon Willison is the creator of Django, the `llm`
  CLI, sqlite-utils, and Datasette; one of the most widely-cited independent
  LLM tooling practitioners in this corpus, with no vendor affiliation to
  either OpenAI (Codex) or the tools he's evaluating here. This post documents
  his own real-time work session, not a secondhand report — the same
  reliability profile as `blog-simonwillison-datasette-blog-codex-session.md`.
- **Scope**: Covers one single-developer, single-afternoon "shower project"
  spike: turning sqlite-utils' single-database API into a portable,
  SQLAlchemy-backed library and CLI supporting SQLite, PostgreSQL, and DuckDB.
  Does NOT cover team workflows, multi-agent orchestration, or long-running
  production maintenance — this is one person directing two named
  coding-agent tiers (Codex, "GPT-5.6 Sol Ultra") across a handful of prompts
  in one continuous session plus one later follow-up optimization commit.

## Extracted Claims

### Claim 1: Willison used a single, detailed "research spike" prompt — API surface, target engines, a reference implementation to study, and explicit process instructions (uv, git, TDD) — to task two coding agents with building a working multi-database prototype from scratch
- **Evidence**: The full prompt is reproduced verbatim in both the blog post's blockquote and the gist's opening line.
- **Confidence**: anecdotal (a single practitioner's own prompt for a single project)
- **Quote**: "Do a research spike to see what it would take to build a library with the same core API as SQLite-utils - in particular the insert and upsert and insert_all and upsert_all and create and update methods, and the table introspection stuff - but backed by SQLalchemy so it works for multiple database engines" / "Test against PostgreSQL and SQLite and duckdb" / "Use ~/dev/sqlite-utils for reference" / "Create a git repo for this and commit and early and often - use uv init to start the project - use red/green TDD and pytest, see ~/dev/django-sql-dashboard for one idea as to how the PostgreSQL tests could work"
- **Our assessment**: This is a concrete, reusable template for an agent-directed research spike: state the target API contract, name the engines/environments to validate against, point at a specific local reference implementation to mine for behavior (rather than describing the behavior from memory), and specify process constraints (incremental commits, TDD) rather than leaving process to the agent's discretion. It's notable that the prompt spends more words on *process* (commit cadence, TDD, which repo to reference for the Postgres harness) than on the *feature list*, and the resulting session (Claim 3 below) shows the agent adhering to exactly that process.

### Claim 2: It took very few follow-up prompts across the whole build — from initial spike, through adding a CLI, through two renames, to a later performance fix — for the project to reach working, alpha-quality, published-package status
- **Evidence**: Willison's own summary line in the blog post, linking directly to the gist as evidence; independently corroborated by the gist itself, which shows only four top-level human prompts ("research spike...", "Get the CLI working for the features that you implemented", "Refactor the code so engine-specific portability stuff lives in a file for that specific engine - maybe a Database subclass is the best way to do that", "Let's rename this to alchemy-utils") plus one debugging question, with the agent self-driving dozens of intermediate tool calls per prompt.
- **Confidence**: anecdotal
- **Quote**: "It took very few follow-up prompts to produce this project in a state good enough to release as an alpha."
- **Our assessment**: "Very few follow-up prompts" is doing a lot of work here — the gist shows each of those four prompts triggering what the transcript itself describes as dozens of file writes, test runs, lint passes, and git commits per prompt (e.g. one block alone is labeled "Created 4 files, edited 4 files, ran 8 commands"). The claim is honest about prompt *count* but understates session *length*; a reader should not infer "a few minutes of work" from "very few follow-up prompts."

### Claim 3: The agent (Codex) narrated its own work as an actual structured research spike — explicitly splitting investigation into parallel streams, producing a dedicated RESEARCH.md that separates "prototype proves feasible" from "what production hardening would require," and giving its own effort estimate for the follow-on work
- **Evidence**: Direct narration lines from the gist transcript, plus the committed `RESEARCH.md` (178 lines, per the transcript's own diff stat) and the final summary message.
- **Confidence**: anecdotal (single session; reflects this agent's behavior on this task, not a general capability claim)
- **Quote**: "I'll treat this as a working spike, not just a memo: initialize a fresh `uv` package and Git repo, study the exact `sqlite-utils` behaviors, implement the portable SQLAlchemy-backed subset with red/green pytest cycles, and exercise SQLite, DuckDB, and PostgreSQL. I'm splitting the reference API, PostgreSQL harness, and DuckDB/dialect edge cases into parallel investigations while I build the core." Later, in the session's closing summary: "Completed the research spike. Conclusion: the core API is feasible using SQLAlchemy Core plus small engine-specific `Database` subclasses. SQLite, PostgreSQL, and DuckDB all pass the same 100-test contract." and "Final verification: `100 passed`, lint clean, Python 3.10 isolated run clean, and wheel/sdist builds successfully. The research estimate for hardening this core into a production v0.1 is roughly three to five weeks; broader sqlite-utils parity would be a larger multi-month project."
- **Our assessment**: The agent's self-produced effort estimate ("three to five weeks" to harden into production v0.1) is a single unverified data point from the same agent that built the prototype — it has an obvious incentive/framing bias (an agent describing its own work as "nearly done" is not an independent estimate) and should not be treated as calibrated. What's more interesting structurally is that the agent was, unprompted, distinguishing "this works" from "this is production-ready" as two separate deliverables (a working prototype vs. a written research note with a boundary/limitations section) — a documentation discipline the human prompt asked for only implicitly (via "research spike," not via an explicit request for a written estimate).

### Claim 4: When the human interjected a one-line architectural correction mid-session ("refactor per-engine logic into a file for that specific engine — maybe a Database subclass"), the agent complied by decomposing a single monolithic class handling three SQL dialects via conditionals into three separate per-engine subclasses, and confirmed the refactor was structural rather than cosmetic
- **Evidence**: The human's prompt and the agent's before/after self-assessment are both in the gist transcript, bracketing a "Created 4 files, edited 4 files, ran 8 commands" work block.
- **Confidence**: anecdotal
- **Quote**: Human: "Refactor the code so engine-specific portability stuff lives in a file for that specific engine - maybe a Database subclass is the best way to do that". Agent: "Agreed. The DuckDB catalog workarounds and insert factories are already making the core class muddy. I'll refactor around a public `Database(...)` factory/base that selects `SQLiteDatabase`, `PostgreSQLDatabase`, or `DuckDBDatabase`, with each dialect module owning upsert construction, generated-PK setup, and reflection fallbacks." Confirmation after the work: "The refactor is now real rather than cosmetic: `Database(engine)` dispatches to three independent subclasses, DuckDB no longer pretends to be PostgreSQL, and `Table` no longer imports or calls dialect `ON CONFLICT` APIs. Engine classes now own statement construction, PK generation, and reflection repair; the full three-engine suite is green at 51 tests."
- **Our assessment**: This is a concrete example of a human course-correction landing as a real architectural change (extract-subclass, not a superficial file split) rather than the agent doing the minimum literal interpretation. The agent's own "real rather than cosmetic" framing suggests it was tracking (and reporting against) the distinction between a genuine refactor and a face-value compliance with the instruction — a useful verification signal a reviewer can look for in session transcripts generally.

### Claim 5: A self-initiated "final review" pass — not requested by the human — caught two real correctness bugs before the agent declared the CLI work done: `upsert_all()` could create a keyless table before rejecting the invalid operation, and inserts into existing tables silently dropped unknown columns unless `alter=True`
- **Evidence**: The agent's own plan lists "one last independent review of the committed artifact for any misleading compatibility claims or structural regression" as a self-assigned step, and the transcript shows it producing failing regression tests for both bugs before fixing them.
- **Confidence**: anecdotal
- **Quote**: "I'm doing one last independent review of the committed artifact for any misleading compatibility claims or structural regression before handing it over." Followed by: "The final review surfaced two real validation holes before handoff: `upsert_all()` could create a keyless table before rejecting the operation, and inserts into existing tables silently discarded unknown columns unless `alter=True`. I've captured both as failing cross-engine tests and am fixing them in the shared orchestration layer; no engine-specific change is needed."
- **Our assessment**: This is a positive, concrete data point for self-review as an agent-internal QA step — bugs caught with zero human involvement, framed and tested (red-then-green) before being fixed, rather than silently patched. It's a single anecdote from one session and should not be read as "agents reliably self-catch validation bugs," but it is a specific, well-documented instance worth citing alongside the near-miss failure in Claim 7 below — the same agent, in the same session, both self-corrected two real bugs and separately made one real, if non-code, mistake (moving a real file).

### Claim 6: Before finalizing the project's public name, the agent proactively checked for and avoided a PyPI naming collision — twice — including a live availability check against the PyPI API for the name a human later requested
- **Evidence**: Two separate points in the transcript: an early, unprompted discovery that the provisional name collided with an existing package, and a later live web/API check when the human asked for a specific new name.
- **Confidence**: anecdotal
- **Quote**: First instance: "One packaging issue is important enough to fix in the spike: `sqlalchemy-utils` / `sqlalchemy_utils` is already the name of an established PyPI project, so this prototype could not safely coexist with it. I'm renaming the spike to `sqlite-utils-sqlalchemy` with import package `sqlite_utils_sqlalchemy`; the API objects and behavior stay the same." Second instance, after the human said "Let's rename this to alchemy-utils": "`alchemy-utils` currently returns 404 from PyPI's project API, so the distribution name appears available as of today. Since this is an unreleased spike, I'm doing a clean rename rather than shipping legacy module and command aliases."
- **Our assessment**: Neither collision check was explicitly requested — the human's rename instruction was just "Let's rename this to alchemy-utils," with no mention of checking availability. The agent independently ran a web search and a direct `curl` against `https://pypi.org/pypi/alchemy-utils/json` (visible in the transcript's tool-call log) to verify the name was actually free before adopting it, which is a small but real example of an agent extending a literal instruction with an adjacent due-diligence step a careful human engineer would also do.

### Claim 7: During an unprompted rename/cleanup pass, the agent moved the user's real 780 KB production DuckDB database file into a temporary directory, mistaking it for a disposable test artifact — and because DuckDB silently auto-creates an empty database file at any path it's asked to open, a subsequent read-only CLI command returned blank output instead of an error, masking the mistake until the user noticed and asked why the command was broken
- **Evidence**: Full exchange in the gist transcript: the human's diagnostic question, the agent's investigation and self-diagnosis, and its explicit root-cause statement (including naming the underlying UX bug in DuckDB's connection behavior, not just its own mistake).
- **Confidence**: anecdotal (one specific observed instance in one session)
- **Quote**: Human: "Why does this break? uv run alchemy-utils schema 'duckdb:///test.duck'". Agent, mid-diagnosis: "The command currently exits successfully but prints nothing because `test.duck` is now an empty database. I found an important wrinkle: during the prior rename cleanup I mistook the untracked `test.duck` for a generated test artifact and moved it to a temporary recovery directory." Agent's final explanation: "It broke because I accidentally moved the untracked `test.duck` during rename cleanup. DuckDB then silently created a new empty database at that path, so `schema` returned blank output instead of an error. I restored the original 780 KB database. The command now succeeds... The underlying UX bug is that read-only CLI commands do not verify that a DuckDB file exists before connecting; DuckDB creates it automatically. Sorry—I mistook your database for a generated test artifact."
- **Our assessment**: This is a second, independent, corroborating instance of the exact failure category already documented in `blog-simonwillison-datasette-blog-codex-session.md` Claim 5 (Codex Desktop deleting a real, untracked `blog-content/` directory during a cleanup pass, believing it was disposable refresh output) — same root pattern (agent misclassifies untracked/unfamiliar user-owned content as build/test ephemera during a "cleanup" step), different product (Codex CLI research-spike session here vs. Codex Desktop there) and different recovery mechanism (the file was physically moved, not deleted, so it was recoverable by locating it — contrast the Desktop case, which was recovered from previously captured terminal output because the file had actually been deleted). This occurrence adds a compounding factor the earlier case didn't have: DuckDB's auto-create-on-connect behavior meant the *symptom* (blank schema output instead of a file-not-found error) actively hid the mistake rather than surfacing it immediately — the human had to notice unexpected behavior and ask, rather than getting an error at the moment of the mistake.

### Claim 8: Before declaring the project done, the agent ran the full test suite against all three real database engines, built the installable package, and verified the built wheel actually installs and runs in a clean Python 3.10 environment — not just that the source checkout works
- **Evidence**: Final validation summary in the transcript, stated as the closing status of the last top-level prompt (the "alchemy-utils" rename).
- **Confidence**: anecdotal
- **Quote**: "Renamed throughout: Distribution: `alchemy-utils` / Python package: `alchemy_utils` / CLI: `alchemy-utils` / Module entry point: `python -m alchemy_utils`... Validation: 164 passed, 1 expected skip / Ruff clean / Wheel/sdist build successfully / Fresh Python 3.10 wheel installation verified / Worktree clean"
- **Our assessment**: The "fresh Python 3.10 wheel installation verified" step is the notable part — it's easy for an agent (or a human) to declare a Python project "done" once tests pass against the editable/development checkout, while never confirming the *packaged, installed* artifact actually works end-to-end (missing package data, broken entry points, and packaging metadata errors are a classic gap between "tests pass in dev" and "the shipped wheel works"). This session's transcript shows that check happening repeatedly (twice, once before and once after the alchemy-utils rename) rather than once at the very end.

### Claim 9: A separate follow-up commit (not part of the original gist session) fixed a real ~100x bulk-insert performance regression — from "nearly an hour" to "around 35 seconds" for loading a real-world CSV dataset — by replacing eager, full-file materialization of CSV rows with a streaming generator and switching from unbatched to batched database writes
- **Evidence**: The blog post's closing performance claim, independently verified against the actual commit diff (`e3b8d03e...`, subject "Speed up bulk CSV inserts") fetched directly from GitHub.
- **Confidence**: anecdotal (single before/after measurement on one dataset, one machine, not independently reproduced), though the code-level mechanism is directly observable and verifiable in the diff, not just asserted.
- **Quote**: Blog post: "(That one took nearly an hour the first time I ran it, so I had Codex optimize it and got it down to around 35 seconds.)" README diff from the commit: "CSV and TSV inputs are streamed in batches of 100 records; use `--batch-size` to tune the batch size."
- **Our assessment**: The commit diff shows the actual mechanism behind the speedup, which the blog post itself doesn't describe: the prior `_read_records` function built a full Python list of every CSV row in memory before any database write occurred (`return [dict(row) for row in reader], False`); the fix replaces that with a generator (`_read_delimited_records`, using `yield dict(row)`) so rows stream rather than fully materializing, and the write path — which the diff shows previously called `del batch_size` (i.e. the parameter existed in the function signature but was explicitly discarded, meaning batching was never actually implemented) — now validates and honors a real `batch_size` (`if batch_size < 1: raise ValueError(...)`, default streamed in chunks of 100 via `itertools.islice`). In other words: the original "prototype-quality" bulk insert was functionally unbatched despite having a `batch_size`-shaped parameter in its signature, and the fix was inserting rows in real batches instead of one at a time. This is a concrete, verifiable example of "AI-assisted spike code has a plausible-looking-but-inert parameter" as a specific failure shape, distinct from a generic "the first version was slow" claim.

## Concrete Artifacts

### The original research-spike prompt (verbatim, from blog post blockquote and gist)

```
Do a research spike to see what it would take to build a library with the
same core API as SQLite-utils - in particular the insert and upsert and
insert_all and upsert_all and create and update methods, and the table
introspection stuff - but backed by SQLalchemy so it works for multiple
database engines

Test against PostgreSQL and SQLite and duckdb

Use ~/dev/sqlite-utils for reference

Create a git repo for this and commit and early and often - use uv init to
start the project - use red/green TDD and pytest, see ~/dev/django-sql-dashboard
for one idea as to how the PostgreSQL tests could work
```
*Source: https://simonwillison.net/2026/Aug/12/alchemy-utils/ (blockquote) and
gist.github.com/simonw/bd10e4886688e0fd1b833e4afaabf19e (opening line).*

### CLI usage examples (verbatim, from blog post)

```bash
uvx --with 'alchemy-utils[postgresql]' alchemy-utils rows \
  'postgresql+psycopg://simon@localhost:5432/simonwillisonblog' redirects_redirect
```

```bash
curl 'https://raw.githubusercontent.com/simonw/sf-tree-history/refs/heads/main/Street_Tree_List.csv' \
  | uvx --with 'alchemy-utils[duckdb]' alchemy-utils insert 'duckdb:////tmp/trees.db' trees - --csv
```
*Source: https://simonwillison.net/2026/Aug/12/alchemy-utils/, page HTML.*

### CLI feature summary at first working version (from gist, agent's own summary)

```
- create-table, insert, upsert, and update
- JSON, JSONL, CSV, TSV, files, and stdin
- Single and bulk writes through the same insert/upsert commands
- tables, views, schema, columns, indexes, foreign-keys, rows, get, and count
- SQLite paths plus PostgreSQL/DuckDB SQLAlchemy URLs
- Compound keys/FKs, typed PK parsing, binary values, and atomic truncation
- Console command and python -m alchemy_utils
```
*Source: gist.github.com/simonw/bd10e4886688e0fd1b833e4afaabf19e.*

### The bulk-insert performance fix (from commit diff, github.com/simonw/alchemy-utils/commit/e3b8d03e040867b256aeff7db322a0b0eb1f8b06)

```diff
 def _read_records(
     filename: str, *, nl: bool, csv: bool, tsv: bool
-) -> tuple[list[dict[str, Any]], bool]:
+) -> tuple[Iterable[dict[str, Any]], bool]:
     input_format = _selected_input_format(filename, nl=nl, csv=csv, tsv=tsv)
+    if input_format in ("csv", "tsv"):
+        return _read_delimited_records(filename, input_format=input_format), False
     ...
-        return [dict(row) for row in reader], False
+        for row in reader:
+            yield dict(row)
```
Commit subject: "Speed up bulk CSV inserts". README addition: "CSV and TSV
inputs are streamed in batches of 100 records; use `--batch-size` to tune the
batch size."
*Source: commit patch, fetched directly via `curl` from GitHub, not
paraphrased or summarized.*

### The near-miss data-loss incident (from gist)

```
> Why does this break? uv run alchemy-utils schema 'duckdb:///test.duck'

[agent diagnosis:]
The command currently exits successfully but prints nothing because
`test.duck` is now an empty database. I found an important wrinkle: during
the prior rename cleanup I mistook the untracked `test.duck` for a generated
test artifact and moved it to a temporary recovery directory.

[agent resolution:]
It broke because I accidentally moved the untracked `test.duck` during rename
cleanup. DuckDB then silently created a new empty database at that path, so
`schema` returned blank output instead of an error.

I restored the original 780 KB database. The command now succeeds:

CREATE TABLE ducks(id INTEGER DEFAULT(nextval('ducks_id_seq')), "name" VARCHAR, PRIMARY KEY(id));;

The underlying UX bug is that read-only CLI commands do not verify that a
DuckDB file exists before connecting; DuckDB creates it automatically.
Sorry—I mistook your database for a generated test artifact.
```
*Source: gist.github.com/simonw/bd10e4886688e0fd1b833e4afaabf19e.*

### Final validation summary before "done" (from gist, agent's closing status message)

```
Renamed throughout:
- Distribution: alchemy-utils
- Python package: alchemy_utils
- CLI: alchemy-utils
- Module entry point: python -m alchemy_utils

Validation:
- 164 passed, 1 expected skip
- Ruff clean
- Wheel/sdist build successfully
- Fresh Python 3.10 wheel installation verified
- Worktree clean
```
*Source: gist.github.com/simonw/bd10e4886688e0fd1b833e4afaabf19e.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-blog-codex-session.md` Claim 5 and Claim 6:
    that note's untracked-directory deletion (Codex Desktop mistaking a real
    `blog-content/` folder for disposable refresh output) and its
    test-suite-as-verification-loop pattern are both independently repeated
    here — Claim 7 above is a second, distinct-product instance of the same
    "agent misclassifies untracked user content as ephemera during cleanup"
    failure category, and Claim 8 above shows the same "don't declare done
    until the real test suite/build passes" discipline.
  - `blog-simonwillison-gpt56-codex-deletion-bug.md` Claims 1-3: that note
    documents a second-hand report (via Thibault Sottiaux) of GPT-5.6 Codex
    destructively mishandling files in full-access/no-sandbox mode, framed
    explicitly as an "honest mistake," not adversarial behavior. Claim 7 here
    is a first-hand, fully-transcripted instance of the same general pattern
    (non-adversarial, well-intentioned agent action with real-world
    destructive/near-destructive consequences on user-owned files) from the
    same Codex product family, adding primary-source detail (the exact
    diagnostic exchange and the DuckDB auto-create compounding factor) that
    the Sottiaux quote's three-bullet summary does not include.
  - `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 1 (no measured
    quality advantage for agent-internal TDD in a controlled comparison): this
    source does not contradict that finding, but is worth flagging as a
    contrasting anecdote — Willison's prompt explicitly requested red/green
    TDD, and the resulting session shows the agent writing failing tests
    before implementation code repeatedly and self-catching two real bugs in
    review (Claim 5). This is one uncontrolled, unblinded session with no
    non-TDD comparison arm, so it cannot rebut Böckeler's controlled finding —
    but it is a data point the guide should not silently omit when discussing
    that contradiction (see CONTRADICTIONS.md / issue #2653 referenced in that
    note).
- **Contradicts**: None identified. No claim here conflicts with an existing
  source note's claim in a way that would change guide advice; the TDD
  observation above is a contrast worth noting, not a contradiction (this
  source has no control arm to compare against, so it cannot be weighed
  against Böckeler's controlled result — see above).
- **Extends**:
  - `blog-simonwillison-datasette-blog-codex-session.md`: extends the
    corpus's primary-source evidence for what a full, unedited Codex session
    transcript looks like end-to-end, on a different kind of task (a
    from-scratch multi-database library plus CLI, versus that note's
    website-infrastructure build) and with a distinct set of session
    highlights (self-driven refactor, self-review catching real bugs, PyPI
    collision avoidance, the near-miss file-move incident).
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("the bottleneck has
    shifted from code generation to verification"): Claim 5 and Claim 8 above
    are a concrete, single-session illustration of that thesis in practice —
    the agent's own final steps were dominated by verification activity
    (self-review, regression tests for newly found bugs, full three-engine
    suite runs, clean-room wheel install) rather than further feature
    generation.
- **Novel**:
  - The specific compounding failure mechanism in Claim 7 — an agent
    misclassifying a real file as disposable *and* a downstream tool's
    auto-create-on-open behavior (DuckDB) silently masking the resulting
    breakage instead of erroring — is new to this corpus. Prior file-mishap
    sources involve either an outright deletion that surfaces immediately
    (this note's own Corroborates entries) or an environment-variable
    override; this is the first documented case where a second tool's benign
    design choice (auto-creating missing DB files) actively hides an agent's
    mistake from the user.
  - Claim 9's code-level "plausible-looking-but-inert parameter"
    (`batch_size` accepted in the function signature but explicitly discarded
    via `del batch_size`, so batching silently never happened) is a specific,
    verifiable-in-diff failure shape not previously documented in this
    corpus's performance-related source notes.
  - Claim 6's live PyPI-availability check as an unprompted due-diligence
    step during a rename is not documented elsewhere in the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add Claim 1's prompt structure as a named
  "research spike" prompt pattern: state the target API/feature contract,
  name the environments/engines to validate against, point at a specific
  local reference implementation to mine for exact behavior (rather than
  describing it from memory), and specify process constraints (commit
  cadence, TDD) explicitly rather than leaving them to agent discretion. Cite
  this source alongside the existing session-transcript pattern from
  `blog-simonwillison-datasette-blog-codex-session.md`.
- **Chapter 03 (Verification)**: Add Claim 5 (self-initiated final review
  catching two real validation bugs) and Claim 8 (test suite + wheel-install
  smoke test as the actual "done" gate, run twice, not once) as concrete
  examples of what a verification-first closing step looks like in practice.
  Note explicitly, per the Cross-References TDD discussion above, that this
  single uncontrolled session should not be cited as evidence that
  agent-internal TDD "works" in the sense Böckeler's controlled study tests —
  it is a positive anecdote, not a rebuttal.
- **Chapter 06 (Security & Threat Model)**: Add Claim 7 as a third named,
  independently-sourced instance (alongside the two already-cited incidents
  in `blog-simonwillison-datasette-blog-codex-session.md` and
  `blog-simonwillison-gpt56-codex-deletion-bug.md`) of coding agents
  misclassifying real, untracked/unfamiliar user files as disposable during
  self-initiated cleanup passes. Specifically call out the compounding factor
  here — a downstream tool's silent auto-create behavior can hide the mistake
  from the user rather than surfacing it as an error — as a reason to
  recommend git-tracking (or otherwise protecting) real data files before
  letting an agent run open-ended "cleanup"/rename passes near them.

## Extraction Notes

- WebFetch's default summarization pass on the blog post URL returned a
  lossy paraphrase (tested first, per MINER.md §2a); the actual page HTML was
  fetched directly via `curl` and used for every quote in this note.
- Followed two linked pages beyond the blog post itself, both fetched
  directly (not via WebFetch, to guarantee verbatim quotes): the full
  1,060-line session-transcript gist, and the specific commit diff for the
  performance fix mentioned in the blog post's closing sentence. Both are
  substantive primary sources, not secondary summaries.
- Did not follow the gist's own internal references to `~/dev/sqlite-utils`
  or `~/dev/django-sql-dashboard` (local paths on Willison's machine, not
  independently accessible/citable) or to the PyPI project page for the
  colliding `sqlalchemy-utils` package name (tangential, not load-bearing for
  any claim above).
- The gist transcript is very long and heavily nested (collapsible
  `<details>` blocks recording dozens of individual shell commands, file
  writes, and exploratory Python snippets per work block); this note
  extracts the agent's own narrated summaries and the specific exchanges that
  support each claim, rather than reproducing the full low-level tool-call
  log, consistent with how `blog-simonwillison-datasette-blog-codex-session.md`
  handled a similarly-structured transcript.
- No contradictions with existing source notes were identified; the TDD
  observation under Cross-References is a contrast, not a contradiction (see
  that section for why), so no contradiction issue was filed per MINER.md
  §4a.
- Confidence set to `anecdotal` overall: every claim rests on a single
  developer's single session (plus one follow-up commit) on one personal
  project — high internal reliability (this is an unedited primary-source
  transcript, not a retrospective account, and the commit diff independently
  verifies the blog post's performance claim) but no generalizability
  evidence beyond this one case.
