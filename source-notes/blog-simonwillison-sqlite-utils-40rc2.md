---
source_url: https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/
source_type: blog-post
title: "sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)"
author: Simon Willison
date_published: 2026-07-05
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1683"
---

# sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)

> Simon Willison has Claude Fable perform a pre-release audit of sqlite-utils
> 4.0, which surfaces a release-blocking data-loss bug; ships the fix across
> 37 prompts and 34 commits; has GPT-5.5 independently re-review the result
> and catch two further P1 transaction bugs Fable's own review missed; then
> uses AgentsView, run from inside the same Claude Code session, to price the
> entire release at $149.25 in unsubsidized API cost.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, published 2026-07-05, 1am;
  auto-discovered via trusted feed `simon-willison`. A first-person narrative
  of a real open-source release cycle, combining a bug-discovery anecdote, a
  transaction-model documentation excerpt, a second AI review episode, a cost
  breakdown table, and the full RC2 changelog.)
- **Author credibility**: Simon Willison is the creator and maintainer of
  sqlite-utils, Datasette, and the `llm` Python CLI. This is first-party
  release engineering documentation — he is both the practitioner and the
  project owner making the ship/no-ship call. No vendor affiliation with
  Anthropic or OpenAI; the post explicitly names both Claude Fable and GPT-5.5
  and evaluates them on their own merits (finding bugs in one, praising the
  other).
- **Scope**: Covers one specific release cycle (sqlite-utils 4.0rc1 → 4.0rc2):
  a Fable-driven pre-release audit, the specific data-loss bug it found, the
  transaction-model documentation it wrote, a follow-up GPT-5.5 review that
  found two additional P1 bugs, and an in-session AgentsView cost calculation
  ($149.25 total). Does NOT cover: sqlite-utils' broader feature set (see
  `blog-simonwillison-sqlite-utils-40rc1.md` for that), a controlled
  comparison of Fable vs. GPT-5.5 review quality, or any outcome data beyond
  this single release.

## Extracted Claims

### Claim 1: A Fable-driven "final review before shipping" pass on a stable major-version release found a critical, previously-undiscovered data-loss bug — `delete_where()` never commits and leaves the connection permanently unable to commit
- **Evidence**: Willison's prompt ("Final review before shipping a stable 4.0
  release...") produced a written report identifying 5 "release blockers." The
  worst one is reproduced with exact file/line references (`db.py:2948`
  compared to the correctly-wrapped `db.py:2944`) and an end-to-end repro
  script showing that after `delete_where()`, all subsequent writes —
  including to unrelated tables — are silently rolled back on connection
  close.
- **Confidence**: emerging (single practitioner, single release, but the bug
  is independently reproducible from the exact repro script given, and was
  fixed and shipped)
- **Quote**: "Table.delete_where() (sqlite_utils/db.py:2948) runs its DELETE via a bare self.db.execute() with no atomic() wrapper — compare Table.delete() at db.py:2944, which wraps correctly. The connection is left in_transaction=True, so every subsequent atomic() call takes the savepoint branch (db.py:430-440) and never commits either."
- **Our assessment**: This is a strong, concrete instance of AI-assisted
  review catching a bug that manual testing missed on a project maintained
  by an expert practitioner (Willison, sqlite-utils' own author). The
  specificity of the finding (exact line numbers, a working repro, an
  explanation of *why* it cascades to unrelated tables) is what makes this
  credible rather than a vague "AI found bugs" claim. Willison's own
  reaction — "That's a really bad bug! Very glad I didn't ship that" —
  confirms this would have been a real production data-loss incident in a
  library used as the persistence layer for other tools (e.g. `llm`).

### Claim 2: The fix required substantial follow-through, not a one-line patch — 37 prompts, 34 commits, +1,321/-190 lines across 30 files
- **Evidence**: Willison's direct statement of the scope of work completed
  after the initial review report.
- **Confidence**: emerging (single, verifiable data point — PR #767 is
  linked)
- **Quote**: "Over the course of 37 prompts, 34 commits and +1,321 -190 code changes over 30 separate files, we worked through the entire set of feedback in turn, making several other design improvements along the way."
- **Our assessment**: This scale (30 files, 34 commits) shows that "final
  review before shipping" is not a rubber-stamp activity when taken
  seriously — a single release-blocker finding cascaded into a substantial
  rework of the transaction model. This is a useful calibration point for
  what "AI does a pre-release audit" can actually cost in follow-up work,
  distinct from the dollar cost captured in Claim 8.

### Claim 3: Harder, longer-running agent tasks create idle time the practitioner can use productively, rather than only being a source of friction
- **Evidence**: Willison's own account of stepping away to attend a local
  parade while Fable worked, checking in periodically from his phone.
- **Confidence**: anecdotal (single practitioner's description of one
  session's pacing)
- **Quote**: "A weird thing about coding agents is that harder tasks like this one actually provide more opportunity to do other things at the same time, since the agent sometimes needs 10-15 minutes to churn away on a new task. I went out to enjoy the Half Moon Bay 4th of July parade, occasionally checking in and prompting the next step for Fable from my phone."
- **Our assessment**: This reframes agent latency as a feature rather than a
  cost for asynchronous work styles (Claude Code for web, prompted from a
  phone) — the opposite of the synchronous pair-programming expectation.
  It's a single anecdote, but it's a concrete, reproducible workflow shape
  (mobile-driven, interrupt-tolerant task delegation) rather than a vague
  claim about "productivity."

### Claim 4: sqlite-utils 4.0's transaction model auto-commits every write method by default, requiring no explicit `commit()` call, with two documented exceptions for `db.atomic()` and `db.begin()`
- **Evidence**: Willison quotes the shipped documentation in full, describing
  it as the RC's "signature new feature," and confirms it was the fix target
  for Claim 1's bug.
- **Confidence**: settled (this is shipped, released documentation for a
  library with a real user base — not a preview or draft)
- **Quote**: "Every method in this library that writes to the database—insert(), upsert(), update(), delete(), delete_where(), transform(), create_table(), create_index(), enable_fts() and the rest—runs inside its own transaction and commits it before returning. Your changes are saved to disk as soon as the method call finishes"
- **Our assessment**: This documents the target behavior the bug in Claim 1
  violated — `delete_where()` was the one write method that didn't follow
  this rule. The two escape hatches (`db.atomic()` for grouped
  all-or-nothing writes, `db.begin()` for fully manual transaction control)
  give a complete mental model for anyone building on sqlite-utils as an
  AI-pipeline persistence layer.

### Claim 5: Reviewing an AI agent's documentation edits first, before its code changes, is Willison's stated technique for building an initial understanding of what changed
- **Evidence**: Willison's explicit statement of review method, applied in
  this session and yielding the discovery described in Claim 6.
- **Confidence**: anecdotal (single practitioner's stated review habit)
- **Quote**: "In reviewing Fable's documentation—I find that reviewing the documentation edits first is an excellent way to build an initial understanding of what has changed—I spotted this detail"
- **Our assessment**: This is a transferable review heuristic distinct from
  reading the diff line-by-line or reading the changelog: docs written to
  explain a change to a third party force a different, more legible framing
  than the code itself, and inconsistencies or unstated assumptions surface
  more readily there. It directly produced the finding in Claim 6, so it's
  not merely a preference — it's shown to work in this instance.

### Claim 6: Willison's doc-first review surfaced an edge case even he — the library's own author — had not previously considered: sqlite-utils' new transaction model is incompatible with Python 3.12+'s explicit `autocommit=True`/`autocommit=False` connection modes, which broke nearly the entire test suite
- **Evidence**: Willison's direct account, plus a linked fix commit.
- **Confidence**: emerging (a specific, reproducible compatibility bug,
  fixed and shipped; single project, single maintainer's account)
- **Quote**: "I admit I hadn't thought about how sqlite-utils would react to the more recent autocommit setting, added in Python 3.12. It turns out 'behave differently on those connections' equated to almost the entire test suite failing"
- **Our assessment**: This is a case where the *documentation the AI wrote*
  (not a bug report or a test failure) is what surfaced a design gap in the
  library's own author's mental model. It's a second, independent example
  (alongside Claim 1) of Fable's work surfacing problems Willison had not
  found through his own manual process — but this one was found through
  writing/reviewing docs rather than dedicated bug-hunting.

### Claim 7: A second, independent model (GPT-5.5 via Codex Desktop, "xhigh" reasoning effort) reviewing the same changes after Fable's pass found two additional P1 transaction bugs that Fable's own review and fixes had missed
- **Evidence**: Willison's account of prompting Codex Desktop / GPT-5.5 with
  "Review changes since the last RC. Also confirm that the changelog is
  up-to-date," which surfaced two specific findings with exact file/line
  references, both confirmed reproducible by pasting the findings into a
  fresh Fable session.
- **Confidence**: emerging (concrete, independently reproduced findings —
  Willison had Fable itself confirm them experimentally — but still a
  single release, single pair of models)
- **Quote**: "[P1] sqlite_utils/db.py:663 db.query() now rejects non-row statements only after calling db.execute(), and sqlite_utils/db.py:705 auto-commits those writes first. So db.query(\"update ...\") raises ValueError but the update is already committed. That is a surprising side effect for a method documented as \"can only be used with SQL that returns rows.\""
- **Our assessment**: This is the most significant finding in the post for
  cross-model review methodology: it is not a "second opinion that agrees"
  scenario — GPT-5.5 found *real, distinct* correctness bugs in code that
  Fable had already reviewed, fixed, and presumably considered complete.
  This directly extends the "cross-model audit for shortcut detection"
  pattern already in the guide (`blog-simonwillison-liteparse-browser`,
  cited in `01-daily-workflows.md`) — that pattern is a *lightweight*
  "describe what this does" audit for faked features; this is a *full*
  independent correctness review that catches logic bugs the first
  reviewer-and-fixer missed, a different and heavier failure mode.

### Claim 8: Willison confirms a second model's findings by pasting them into a *fresh* session of the *first* model, rather than trusting the second model's report directly or re-deriving the fix himself
- **Evidence**: Willison's direct account of his verification step after
  receiving GPT-5.5's findings.
- **Confidence**: anecdotal (single instance of this specific verification
  workflow)
- **Quote**: "I pasted that into a fresh Fable session, which ran some experiments to confirm the problem"
- **Our assessment**: This is a specific, reusable verification pattern:
  treat a second model's bug report as a hypothesis, not a verdict, and have
  the *original* implementing model (in a clean context, so it isn't
  anchored on its prior "this is done" state) independently reproduce the
  claimed problem before accepting it. This guards against both false
  positives from the reviewing model and blind trust transfer between two
  different models' outputs.

### Claim 9: Willison states he has moved from skepticism to habitual practice on cross-vendor model review, calling the pattern something that "really does work"
- **Evidence**: Willison's own framing of his change in stance, generalized
  beyond this one release.
- **Confidence**: anecdotal (a practitioner's self-reported change in
  opinion; not a controlled comparison)
- **Quote**: "I used to think that the idea of having one model review the work of another was somewhat absurd—it felt weirdly superstitious. The problem is it really does work—I've started habitually having Anthropic's best model review OpenAI's work and vice versa, because I've had that turn up interesting results often enough to be valuable."
- **Our assessment**: The value here is less the specific claim (which is
  anecdotal and non-quantified — "often enough to be valuable" has no
  denominator) and more that it is stated as a now-*habitual* practice by a
  practitioner who explicitly started from doubt. Combined with
  `blog-simonwillison-csrf-multimodel-review.md` (a separate, earlier
  instance of Claude Code implementing and GPT-5.4 reviewing a production
  security change), this is the second independently-documented instance of
  Willison using cross-vendor review as standard operating procedure, not a
  one-off experiment.

### Claim 10: The full, unsubsidized API cost of this release cycle was calculated *from inside the same Claude Code session* by having the agent run the AgentsView cost-analytics tool against its own transcript, totaling $149.25
- **Evidence**: Willison's account of prompting `Run "uvx agentsview --help" and then use that tool to calculate the cost of this session`, with Claude figuring out the correct `--include-children` invocation itself, and the resulting six-line cost table.
- **Confidence**: settled (a concrete, itemized cost breakdown, though
  representing a single session)
- **Quote**: "Run \"uvx agentsview --help\"​ and then use that tool to calculate the cost of this session"
- **Our assessment**: This is notable methodologically distinct from
  `blog-simonwillison-agentsview-custom-model-price.md`, where Willison ran
  AgentsView himself, externally, against his local transcript store. Here
  the *agent itself* is prompted to install and run the cost-analytics tool
  against its own session and report the total — a self-instrumenting cost
  audit performed inside the same agentic loop that generated the cost. The
  resulting breakdown (main session $141.02, four review subagents totaling
  $7.91, one `claude-opus-4-8` prompt-counting subagent at $0.32) is a
  concrete, itemized real-world cost model for a non-trivial open-source
  release.

### Claim 11: Willison explicitly critiques his own token usage on this release, saying he should have delegated more subagent work to cheaper models — directly citing his own prior advice
- **Evidence**: Willison's direct self-assessment immediately following the
  cost table, with an explicit link to his own earlier post.
- **Confidence**: anecdotal (single practitioner's self-critique of one
  session)
- **Quote**: "I'm very glad I'm on that subscription! I really should have followed my own advice and leaned more heavily into subagents with cheaper models."
- **Our assessment**: The "own advice" link points to
  `blog-simonwillison-fable-judgement.md` (2026-07-03, two days earlier),
  where Willison documented telling Fable to use its own judgement about
  which lower-power model to delegate coding subagents to. This release
  (started before or contemporaneous with adopting that practice) shows only
  one subagent on a cheaper model (`claude-opus-4-8`, for prompt-counting,
  $0.32) out of five total transcripts — the rest ran on `claude-fable-5`
  itself at $141.02 combined. This is a rare instance of a practitioner
  documenting a gap between their own stated policy and their actual
  session behavior, in the same corpus, within days.

### Claim 12: Fable wrote the changelog incrementally into an "Unreleased" section as each change landed, which Willison reviewed as it went, rather than generating it in one pass at the end
- **Evidence**: Willison's direct description of the changelog-writing
  workflow and its side effect.
- **Confidence**: anecdotal (single practitioner's workflow description for
  one release)
- **Quote**: "I had Fable add these to an \"Unreleased\" section of the changelog as each change landed, reviewing them as it went. This has the neat side effect that the commit history of the changelog acts as a concise summary of each of the changes that went into the release."
- **Our assessment**: This is a specific, reusable pattern distinct from
  "have the AI write release notes at the end": writing changelog entries
  per-commit rather than as a single end-of-release summarization pass
  produces a changelog whose git history is itself a navigable, granular
  changelog-of-the-changelog. Willison also restates his general policy
  toward AI-authored release notes: "these are better than I would have
  created myself... Release notes are a great example of writing that I'm
  OK to outsource to agents because they need to be boring, predictable and
  accurate" — a specific, bounded category of writing task he considers
  safe to fully delegate.

## Concrete Artifacts

### The `delete_where()` data-loss bug — repro script (from the post, quoting Fable's review report)

```
db = sqlite_utils.Database("dw.db")
db["t"].insert_all([{"id": i} for i in range(3)], pk="id")
db["t"].delete_where("id = ?", [0])   # conn.in_transaction is now True
db["t"].insert({"id": 50})
db["u"].insert({"a": 1})
db.close()
# Reopen: rows are [0, 1, 2] — the delete, row 50, AND table u are all gone.
```

*Source: Simon Willison, quoting Fable's `fable-review-4.0rc1.md` report,
simonwillison.net/2026/Jul/5/sqlite-utils-fable/*

### AgentsView self-instrumented cost breakdown (from the post)

```
Transcript                              Model             Cost
Main session                            claude-fable-5    $141.02
API-surface sweep agent                 claude-fable-5    $2.40
Transactions/atomic review agent        claude-fable-5    $2.39
Post-rc1 commits review agent           claude-fable-5    $1.72
Migrations review agent                 claude-fable-5    $1.40
Prompt-counting agent                   claude-opus-4-8   $0.32
                                                    Total: $149.25
```

*Source: Simon Willison, simonwillison.net/2026/Jul/5/sqlite-utils-fable/,
generated by prompting Claude Code to run `uvx agentsview` (with
`--include-children`) against its own session transcript.*

### GPT-5.5's two P1 findings (verbatim from the post)

```
[P1] sqlite_utils/db.py:663 db.query() now rejects non-row statements only
after calling db.execute(), and sqlite_utils/db.py:705 auto-commits those
writes first. So db.query("update ...") raises ValueError but the update is
already committed. That is a surprising side effect for a method documented
as "can only be used with SQL that returns rows."

[P1] sqlite_utils/db.py:672 INSERT ... RETURNING through db.query() only
commits after the returned generator is fully exhausted. db.query("insert
... returning ...") without iteration, or common next(db.query(...)) usage,
leaves the transaction open and the write can be rolled back on close. This
contradicts docs/changelog.rst:15 and docs/python-api.rst:232, which say it
takes effect without iteration.
```

*Source: GPT-5.5 (via Codex Desktop, xhigh reasoning), as quoted by Simon
Willison, simonwillison.net/2026/Jul/5/sqlite-utils-fable/*

### sqlite-utils 4.0rc2 breaking changes (verbatim summary from the post's release notes)

```
Breaking changes:
- Write statements executed with db.execute() are now committed
  automatically, unless a transaction is already open in which case they
  join it.
- db.query() now executes its SQL as soon as it is called, rather than
  waiting until the returned generator is first iterated.
- Python API validation errors now raise ValueError instead of
  AssertionError.
- table.upsert() / upsert_all() now raise PrimaryKeyRequired if a record is
  missing a value for any primary key column, or has a value of None for
  one.
- db.enable_wal() / disable_wal() now raise TransactionError if called
  while a transaction is open.
- The View class no longer has an enable_fts() method (raises
  AttributeError).
- The no-op -d/--detect-types flag has been removed.
- Database() now raises TransactionError if passed a connection created
  with Python 3.12+ sqlite3.connect(..., autocommit=True/False).

Everything else (selected):
- Fixed delete_where(), optimize(), and rebuild_fts() to commit their
  changes via db.atomic() (this is Claim 1's fix).
- Migrations now run inside a transaction with the record of being applied;
  failed migrations roll back and stay pending.
- New db.begin(), db.commit(), db.rollback() for manual transaction
  control.
```

*Source: Simon Willison, quoting sqlite-utils changelog,
simonwillison.net/2026/Jul/5/sqlite-utils-fable/ (full changelog at
sqlite-utils.datasette.io/en/latest/changelog.html#rc2-2026-07-04)*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-csrf-multimodel-review.md` Claim 2 ("Multi-model
    cross-review — Claude Code for implementation, a second model for
    review — is a viable workflow for production security changes"): this
    source is a second, independent instance of Willison using a
    cross-vendor model (there GPT-5.4, here GPT-5.5) to review Claude
    Code/Fable's own work, and explicitly generalizes it as now-habitual
    practice (Claim 9). Together they show this is a repeated pattern for
    this practitioner across at least two different projects and models,
    not a one-off.
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 7 (Claude
    Fable 5 priced at $10/M input, $50/M output, 2x Opus 4.7): this source's
    cost breakdown ($149.25, dominated by a $141.02 `claude-fable-5` main
    session) is consistent with and provides a second real-world data point
    for that pricing, applied to a specific, itemizable piece of work
    (a major open-source release) rather than a single day's aggregate
    usage.
  - `blog-simonwillison-fable-judgement.md` Claim 3/4 (Jesse Vincent's tip
    to delegate smaller tasks to cheaper models via Fable's own judgement,
    motivated by conserving tokens before a price increase): this source is
    Willison's own explicit, self-critical acknowledgment (Claim 11) that he
    didn't follow that advice on this release — a direct, dated
    (2026-07-05, two days after the 2026-07-03 judgement post) instance of
    the gap between a stated practice and actual session behavior.

- **Contradicts**: None identified. No existing corpus note makes a claim
  this source conflicts with. No contradiction issue required.

- **Extends**:
  - `blog-simonwillison-sqlite-utils-40rc1.md` (the entire note): that note
    documents 4.0rc1's *new* transaction model (`db.atomic()`, migrations)
    as a feature announcement; this source documents the *hardening* of
    that same transaction model one release later — specifically, a
    critical bug in the write path (`delete_where()`) that the rc1 feature
    announcement did not surface, plus a previously-unconsidered Python
    3.12+ `autocommit` incompatibility. Anyone citing the rc1 note's
    `db.atomic()` code example should be aware this source documents a
    real data-loss bug that existed in the surrounding write-path code at
    that time.
  - `01-daily-workflows.md`'s existing "Cross-model audit for shortcut
    detection" section (sourced from `blog-simonwillison-liteparse-browser`
    Claim 11): that pattern is explicitly a *lightweight* "describe what
    this does" audit aimed at catching faked/stubbed features, not logic
    bugs — "The auditor never approves or rejects code; it describes what
    the code does." This source documents a *heavier* variant: a full
    independent review (not just a description prompt) that found genuine
    P1 correctness bugs the first model's own review-and-fix pass had
    missed (Claim 7), followed by a distinct confirm-via-original-model
    verification step (Claim 8) not present in the lighter pattern.
  - `blog-simonwillison-claude-fable-5.md` (Fable 5's capabilities and
    initial $110.42/day cost data): this source extends that with a second,
    later, task-scoped (rather than daily-aggregate) real-world cost
    figure for a specific, well-defined body of work.

- **Novel**:
  - **First in-corpus example of an agent self-instrumenting its own
    session cost using a third-party cost-analytics tool**: prior AgentsView
    coverage (`blog-simonwillison-agentsview-custom-model-price.md`) has
    Willison running the tool himself, externally, against his local
    transcript store. Here, the cost query is issued *to the agent*, which
    installs and runs the tool against its own session in progress.
  - **First in-corpus example of a "review the AI's docs first" review
    heuristic that itself surfaced a bug** (Claims 5–6): distinct from
    reading the diff or the changelog, and shown to work in this instance.
  - **First in-corpus documented case of a second model's review finding
    real bugs a first model's completed review-and-fix pass missed**, with
    a documented verification step (paste findings into a *fresh* session of
    the *original* model) rather than trusting either model's report
    directly (Claims 7–8).
  - **First in-corpus documented gap between a practitioner's stated
    subagent-delegation policy and their actual session behavior, dated
    within days of each other** (Claim 11, cross-referenced against
    `blog-simonwillison-fable-judgement.md`).

## Guide Impact

- **Chapter 01 (Daily Workflows) — "Cross-model audit for shortcut
  detection"**: This section currently documents only the lightweight
  "describe what this does" audit variant. Add this source as a second,
  heavier cross-model review pattern: a full independent review pass (not
  just a description prompt) by a different vendor's model, which can find
  genuine logic/correctness bugs the first model's own review missed — even
  after that first model already reviewed and "fixed" the code once. Cite
  Claim 7 (GPT-5.5's two P1 findings) and note the follow-up verification
  technique from Claim 8 (paste the second model's findings into a *fresh*
  session of the *first* model to independently confirm before accepting).
  This is a distinct, escalate-if-stakes-warrant variant, not a replacement
  for the lightweight audit.

- **Chapter 01 (Daily Workflows) — "Model mixing across orchestration
  tiers"**: Add Claim 10's cost breakdown and Claim 11's self-critique as a
  concrete, dated illustration that stated delegation policy
  (`blog-simonwillison-fable-judgement.md`) does not automatically translate
  into practice — of five transcripts, only one (a prompt-counting subagent)
  ran on a cheaper model. Useful as a caution alongside any recommendation
  to delegate subagent work to cheaper models: the intent is easy to state
  and easy to not follow through on even by the practitioner who stated it.

- **Chapter 02 (Harness Engineering) — transaction/persistence patterns**:
  If sqlite-utils' `db.atomic()` / auto-commit model is cited (per the rc1
  note's existing Guide Impact recommendation), add a caveat citing Claim 1:
  the write-path auto-commit guarantee had a real data-loss bug
  (`delete_where()` not committing) in the immediately preceding RC, found
  only through a dedicated pre-release AI audit. This tempers "sqlite-utils
  auto-commits your writes" as a safe default with "this guarantee has had
  at least one release-blocking violation in practice, caught by review
  rather than by the test suite."

- **Chapter 04 (Model Judgement / Capability Arcs)**: Claim 9 (Willison's
  stated shift from skepticism to habitual cross-vendor review practice) and
  its corroboration by `blog-simonwillison-csrf-multimodel-review.md` are
  worth citing together as evidence that cross-vendor review is becoming a
  standing practice for at least one prolific practitioner, not a novelty
  demo — useful if the chapter frames model-judgement patterns by maturity/
  adoption stage.

## Extraction Notes

- **WebFetch limitation**: WebFetch's summarizing model returned only a
  paraphrased summary of this post on first request, not verbatim text (the
  same behavior noted in several prior Willison source notes in this
  corpus). I fetched the raw HTML directly via `curl`, isolated the
  `<div class="entry entryPage">` block, and converted it to plain text by
  hand (stripping tags, preserving link targets inline, unescaping HTML
  entities). All quotes in this note are taken from that hand-extracted
  text, not from WebFetch's paraphrase.
- **Full post read**: The entire post was read, including the full
  changelog section reproduced at the end. No sub-pages were followed — the
  post links to the PR (`simonw/sqlite-utils#767` and `#768`), two Claude
  Code session transcripts (`claude.ai/code/session_...`), and the
  Anthropic "Fablepocalypse" pricing announcement
  (`anthropic.com/news/redeploying-fable-5`); these are referenced in the
  post's own text (transcript links, PR links, the pricing-context
  paragraph) and were not separately fetched, since the post's own prose
  already states the load-bearing facts (37 prompts/34 commits/cost table;
  the July 7th end of subsidized Max-plan Fable access). A future source
  note specifically on the Anthropic "Fablepocalypse" pricing change, if
  mined separately, should cross-reference this note's mention of it as
  Willison's stated motivation for running this review before that date.
- **Cross-reference verification** (per MINER.md §4b): all claim citations
  above were checked against the actual numbered `### Claim:` headings in
  the cited notes:
  - `blog-simonwillison-csrf-multimodel-review.md` Claim 2 verified at
    lines 70–80 of that note (heading "Claim 2: Multi-model cross-review —
    Claude Code for implementation, a second model for review — is a viable
    workflow for production security changes").
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 7 verified
    at lines 149–162 of that note (heading "Claim 7: Claude Fable 5 is
    priced at 2x Claude Opus 4.7 for input and output...").
  - `blog-simonwillison-fable-judgement.md` Claims 3 and 4 verified at lines
    89–117 of that note (headings "Claim 3: Jesse Vincent's related tip..."
    and "Claim 4: Willison operationalized the advice with the literal
    prompt...").
  - `blog-simonwillison-liteparse-browser` Claim 11 verified indirectly via
    its direct quotation in `guide/01-daily-workflows.md` lines 424–446
    ("Cross-model audit for shortcut detection" section), which attributes
    the quoted material to that claim.
- **No contradictions filed**: no existing corpus source makes a claim in
  conflict with this source. No contradiction issue required per MINER.md
  §4a.
