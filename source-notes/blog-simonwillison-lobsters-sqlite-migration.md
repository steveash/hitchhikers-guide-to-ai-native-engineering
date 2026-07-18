---
source_url: https://simonwillison.net/2026/Jul/14/lobsters-sqlite/
source_type: blog-post
title: "lobste.rs is now running on SQLite"
author: Simon Willison
date_published: 2026-07-14
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: anecdotal
issue: "#1987"
---

# lobste.rs is now running on SQLite

> Simon Willison links to Lobsters' completed MariaDB→SQLite migration as "a really
> useful case study" of single-server SQLite in production. The linked announcement
> thread (which this note also mines, per MINER.md §1's "follow substantive linked
> pages") tells a fuller and more complicated story than the blog post's snapshot:
> a genuinely successful, well-tested, multi-year-planned migration that, four days
> after the celebratory announcement, was followed by a Rails-bug-triggered deletion
> of 3.2 million database rows and a severe, still-unresolved performance regression
> — see the filed contradiction, issue #2005.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a `trusted-feed` source; a short
  "link post" / "blogmark" format — three short paragraphs plus a blockquote, dated
  14 July 2026, 7:44pm). The blog post itself links to two substantive primary
  sources that this note also mines directly, per MINER.md §1: the lobste.rs
  announcement thread (`lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite`,
  111 comments) and the GitHub migration PR (`github.com/lobsters/lobsters/pull/1927`).
  Both were fetched directly (via `curl`, not WebFetch's summarizing pass) to get
  verbatim text for quotes, per MINER.md §2a.
- **Author credibility**: Simon Willison is a high-signal, frequently-cited commentator
  on SQLite and LLM tooling (maintainer of Datasette, `sqlite-utils`, and the `llm`
  CLI — see the corpus's existing `blog-simonwillison-sqlite-*.md` notes). For this
  post he is a curator/pointer, not the primary source — the substantive claims in
  this note are attributed to Thomas Dziedzic (`thomas0`, the engineer who did the
  migration) and `pushcx` (Lobsters' site admin/"Sysop"), both posting directly on
  the lobste.rs thread under their own names/handles.
- **Scope**: Covers a single production database migration (Lobsters, a Rails-based
  link-aggregator community site) from MariaDB to SQLite on a single VPS: the
  timeline, the two deployment attempts (one failed, one succeeded), the resulting
  architecture and database sizes, community discussion of SQLite production
  configuration, and — critically, since the announcement thread is a live comment
  section that continued to accumulate replies after Willison's post was
  published — a post-migration data-loss incident and unresolved performance
  regression that emerged four days after the initial success announcement. Does
  NOT cover: AI/agentic tooling (no coding agent involvement is mentioned anywhere
  in the migration); it is included in this AI-native-engineering corpus primarily
  for its verification/testing and production-risk lessons, which the Guide Impact
  section addresses explicitly.

## Extracted Claims

### Claim 1: The initial announcement characterized the migration as an unqualified operational success — CPU and memory usage down, the site "snappier," and VPS cost cut in half
- **Evidence**: thomas0 and pushcx, posting on the lobste.rs announcement thread the Monday after the weekend deployment (thread post timestamp 2026-07-13 15:03:24 UTC), reproduced verbatim by Willison's blog post.
- **Confidence**: anecdotal (single-team, self-reported, no controlled comparison) — **and see the "Our assessment" note below: this claim was posted before the incident in Claims 8–9 occurred; contradiction issue #2005 tracks the two conflicting snapshots from the same source.**
- **Quote**: "SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down"
- **Our assessment**: This is the claim the Willison blog post surfaces and that a reader who only sees the blog post (not the full thread) would take away. It is genuine and specific (named metrics, named cost driver: decommissioning the old MariaDB VPS). But it is a snapshot taken ~2-4 days post-deploy, before the incident documented in Claims 8-9 (posted to the *same thread* roughly four days later) revealed a serious data-loss bug and an unresolved performance regression. **Contradiction filed as issue #2005** — do not cite this claim as the guide's settled characterization of the migration's outcome without also citing Claims 8-9.

### Claim 2: The resulting architecture runs on a single VPS with a ~3.8GB primary content database, plus separate 1.1GB cache, 218MB queue, and 555MB (still-growing) rate-limiting databases
- **Evidence**: Willison's blog post prose, corroborated independently by pushcx's reply in the thread with the same figures.
- **Confidence**: settled (specific, named figures, stated twice independently by the admin with direct access to the servers)
- **Quote**: "The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB. There's also a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack_attack database used by the Rack::Attack middleware for blocking and throttling abusive requests."
- **Our assessment**: The "still growing" qualifier on rack_attack is important context Willison's summary preserves — pushcx later clarifies in the thread that this database "hasn't yet been running 8 days to hit its full retention period, and it swings significantly when multiple scrapers with hundreds of thousands of IPs hit the site," so 555MB is not yet a steady-state figure. The use of separate SQLite database files per concern (content, cache, background jobs, rate-limiting) — rather than one monolithic file — is itself a concrete architectural pattern: splitting write-heavy, ephemeral, or high-churn data (cache, queue, rate-limiting) from the durable content database.

### Claim 3: The migration PR added 735 lines and removed 593 across 30 commits and 188 files, and was the third of three PR attempts spanning roughly a year, following a multi-year (2018–2026) planning history
- **Evidence**: Willison's blog post states the diff statistics; thomas0's own "Background Story" comment on the thread gives the multi-year timeline and explains why there were three PR attempts (the first two were closed/abandoned, not merged).
- **Confidence**: settled (specific, verifiable numeric claims about a public, still-accessible PR; the timeline is a first-party account from the engineer who did the work)
- **Quote (diff stats)**: "There are plenty more details in both the linked thread and this SQLite migration PR by Thomas Dziedzic, which added 735 lines and removed 593 lines across 30 commits and 188 files. That PR built on top of previous PRs #1705, #1871, and #1924."
- **Quote (timeline)**: "I got involved with this migration because back in 2019 I stumbled upon #539 and because I had lots of experience working with, managing and migrating largish databases, I left a comment suggesting MySQL as an alternative... Fast forward to 2025, Rahul left a comment mentioning K1's acquisition of MariaDB... In August 2025 I opened my first pull request attempt when I got busy and couldn't attend to the PR. Github closed it as stale and I couldn't reopen it so I opened another PR."
- **Our assessment**: The "three attempts over roughly a year, two of them abandoned/reverted" trajectory is a useful corrective to any reading of this as a quick or low-effort migration. The planning horizon traces back to 2018 (per Willison's framing, corroborated by thomas0's own account referencing a 2019 GitHub issue comment), meaning the total elapsed time from "first considered" to "shipped" was roughly 6-8 years for a site of Lobsters' modest scale (a single community news aggregator). This tempers any "just migrate to SQLite, it's easy" reading — the actual attempt that shipped was preceded by two failed/abandoned attempts and built on institutional risk-tolerance developed over years of discussion.

### Claim 4: The choice of SQLite over PostgreSQL was an explicitly pragmatic decision — driven by who volunteered to do the work and a preference to avoid unnecessary operational complexity — not a claim that SQLite is technically superior to PostgreSQL for this workload
- **Evidence**: pushcx (site admin), directly addressing "why not PostgreSQL?" questions in the thread, since PostgreSQL had been the original plan per issue #539.
- **Confidence**: settled (a direct, first-party statement of decision rationale by the person who made the call)
- **Quote**: "I've heard \"why not PostgreSQL?\" a few times this week. It was even our original plan in #539! Well, it was a pragmatic choice in two different ways: [1] The person who volunteered to do the work used SQLite. [2] I don't want to use solutions that are bigger and more complex than our likely needs. Postgresql is my default for projects, but it does have the added complexity of being a separate service to run, tune, and maintain."
- **Quote (surprise)**: "As a pleasant surprise both our CPU and RAM usage dropped (I expected an increase and steady, respectively)."
- **Our assessment**: This is a meaningful qualifier the blog post's brief framing omits: the admin explicitly frames the choice as contingent on volunteer availability and a general anti-complexity bias, not as a conclusion that SQLite beats PostgreSQL on the merits for a community site's workload. He also states he *expected* CPU usage to increase and RAM usage to stay flat — the drop in both was a surprise to him, not a predicted outcome. Guide advice drawn from this source should avoid overgeneralizing "SQLite wins" and instead present the actual decision structure: contributor availability + operational-simplicity preference, with the performance outcome as an unexpected bonus rather than the reason for the choice.

### Claim 5: The engineer credits the existing Lobsters test suite as essential to migrating the underlying database without extensive manual testing
- **Evidence**: thomas0's own retrospective "lessons learned" list on the thread, under "Lobsters codebase lessons."
- **Confidence**: settled (first-party statement from the person who did the migration)
- **Quote**: "The lobsters testsuite was essential in making sure I could migrate to SQLite without a ton of manual testing."
- **Our assessment**: This is a direct, generalizable claim about test-suite value for a specific high-risk category of change (swapping the underlying data-storage engine, not just refactoring application code) — a category where behavioral drift is easy to introduce silently (see Claim 12 on collation/search-ranking differences) and expensive to detect manually. It corroborates the broader "comprehensive test suite as prerequisite for confident large-scale change" pattern, though notably no AI/agentic tooling is credited anywhere in this account — the test suite substituted for AI-assisted verification, not the other way around.

### Claim 6: The first production deployment attempt failed — read-only traffic alone spiked all CPUs to 100%, root cause was undiagnosed in the moment, and the team reverted; the actual cause (SQLite full table scans on two queries, an N+1 issue on a third) was found afterward and fixed before a second, successful attempt
- **Evidence**: thomas0's first-party account of the Feb 21st deployment and the subsequent root-causing before the July 11th second attempt.
- **Confidence**: settled (specific, first-party, dated account with linked commit references for each of the three fixes)
- **Quote**: "Then came the first deploy on Feb 21st. @pushcx and I got on a call, came up with a checklist for the deployment. Everything went right up until the deployment of the PR. Once deployed the site was in readonly mode, but just the readonly traffic was spiking all the cpus to 100%. We couldn't figure out what the problem was so we decided to revert."
- **Quote (root cause)**: "The performance issues boiled down to SQLite doing full table scans on the largest tables in the database for 2 of queries and the 3rd one solved an n+1 issue."
- **Our assessment**: This complicates the "clean success" framing further upstream of the Claim 1/Claims 8-9 contradiction: the *first* production attempt at this migration also failed, for a different reason (undiagnosed performance collapse under real read traffic, not reproducible from local testing against a partial dataset). The team's response — revert immediately rather than debug live, then root-cause offline with production-scale synthetic data before re-attempting — is a concrete incident-response pattern: prioritize restoring service, then invest in reproduction before the next attempt. Notably, this first failure was caused by exactly the two-query-pattern the team's own database migration script and prior mariadb-based test data could not surface locally, because thomas0 lacked production database access (see Claim 5 in the thread's "Overall lessons," not separately extracted here as it repeats this point).

### Claim 7: The engineer wished for a test assertion that fails on any full-table-scan, and a commenter confirmed this is achievable in SQLite today via bytecode instruction counting, citing a real ORM (Axiom) that implements exactly this
- **Evidence**: thomas0's stated "wish" in his retrospective, and a direct, technically substantive reply from commenter `itamarst` describing a concrete implementation approach with a named prior-art project.
- **Confidence**: emerging (a documented technique with a real reference implementation cited, though not something thomas0 or pushcx confirmed they've since adopted for Lobsters)
- **Quote (the wish)**: "I wish we could say in a test, \"Fail if you encounter any full table scans\". Which would have caught the perf issues we experienced during the first deploy."
- **Quote (the answer)**: "This is possible with sqlite! You can see this e.g. in the testing approach in the Axiom object database/ORM, which is built on top of SQLite. When you run a SQLite query, you can measure how many SQLite bytecode instructions were run, which is far more consistent than measuring run time. This is exposed to Python, at least. Axiom uses this functionality to test that queries' performance is behaving as expected. For example, you can write a test that checks if the query is efficient or not, by running the same query on multiple table sizes. If the query is inefficient and results in a linear scan, the number of bytecodes executed will grow linearly with the size of the table."
- **Our assessment**: This is a concrete, actionable verification pattern distinct from timing-based performance tests: asserting on SQLite VM bytecode-instruction counts (not wall-clock time) as a proxy for query plan shape (scan vs. index seek), which is deterministic and hardware-independent in a way timing assertions are not. A follow-up commenter (`ankhers`) adds an important caveat: this only works reliably against sufficiently large and sufficiently varied test tables, since small tables legitimately favor full scans over index lookups — a test written against typical small unit-test fixtures would give a false sense of safety. This caveat is as load-bearing as the technique itself for anyone adopting it.

### Claim 8: Four days after the success announcement, a routine cleanup migration triggered a Rails bug that silently deleted 3.2 million comment-vote rows, undetected for hours because the affected scores were memoized
- **Evidence**: pushcx's first-party incident account, posted directly to the same announcement thread (comment timestamp 2026-07-17 23:13:20 UTC, i.e. roughly four days after the original post and shortly before this note's extraction).
- **Confidence**: anecdotal (single-team, self-reported, but specific, dated, and posted by the admin actively remediating it in real time — not a secondhand report)
- **Quote**: "We've been working though some cleanups and minor bugs. One task was to replace a MariaDB-specific performance kludge for sorting trees of comments (SQL and trees having infamous friction). The first step was to make the key column on the comments table nullable. Then the plan would be to remove the code that used and filled it, then to drop it entirely. This initial migration unexpectedly deleted every vote on a comment, 3.2 million rows in the database."
- **Quote (why undetected)**: "We didn't know it because comment scores are memoized. So a comment with 30 points looked fine sitting at the top of its thread until someone upvoted it again, and then its score started over at 1. Overnight this happened enough to become apparent."
- **Our assessment**: The root cause is attributed to an upstream Rails bug (`add_foreign_key` on a `change_column_null`-style migration, linked by pushcx to a specific Rails PR and a related lobste.rs story about the same class of bug), not a defect in the SQLite migration work itself — this is a genuine nuance: the bug is in Rails' migration DSL, and would presumably have been latent regardless of which database engine backed the app, though it surfaced during a post-migration cleanup pass specifically prompted by the SQLite migration (removing a MariaDB-specific performance workaround that was no longer needed). The detection mechanism failing silently because of memoized/cached derived state (comment score) is a specific, generalizable failure mode: a data-loss bug can hide behind a cache or memoization layer that doesn't get invalidated by the buggy write path, and only surfaces when something else (a fresh upvote) forces recomputation.

### Claim 9: After restoring the deleted votes, the site entered a severe, unresolved performance regression — CPU usage roughly tripled (25% baseline to 85%) and even single-row indexed-primary-key lookups stalled for seconds — which the admins could not root-cause and left unresolved overnight
- **Evidence**: pushcx's same incident comment, continuing the account after describing the vote-recovery process (3 hours restoring from backups plus reconstructing recent votes from HTTP server logs).
- **Confidence**: anecdotal (self-reported, in-progress incident account; explicitly described by the author as unresolved at time of writing, so this is a snapshot, not a postmortem with a confirmed root cause)
- **Quote**: "I went to run an errand and start mentally drafting a postmortem. When I returned, the site was noticeably sluggish, as it still is now. Pages are often taking seconds to load, sometimes over 10, and browsing the site is unpleasant. @355E3B, @thomas0, and I have been debugging this slowdown for hours without discovering a clear cause. The CPU is pinned, disk is nearly idle, flamegraphs show time burned in SQLite3::Statement#step but even trivial queries (select * from users where id = 123 looking up a single row by indexed primary key) can stall for seconds. The activity charts make it unmistakeable that this didn't start until after I reloaded the votes and exited read-only mode; before CPU was typically 25% and after it's typically 85%."
- **Quote (giving up for the night)**: "We're all tired and we're going to call it a night rather than make sleepy mistakes on prod. I'm sorry we're not back to that lovely speedup we enjoyed for 6 days, but hopefully we'll get there soon."
- **Our assessment**: This is the strongest evidence for the contradiction filed as issue #2005: the same admin who reported CPU usage *down* and the site *snappier* four days earlier is now reporting CPU usage roughly 3.4x higher than pre-incident baseline (25%→85%) and multi-second stalls on trivial indexed primary-key lookups, with no identified cause after "hours" of debugging by three people. That even an indexed single-row lookup by primary key can stall for seconds is notable because it rules out the most common SQLite production footgun (unindexed scans, per Claim 6) as the explanation — something else (write contention, WAL checkpoint behavior, a lock-related regression introduced during the emergency data restore, or something specific to the bulk vote-reload operation) is implicated instead, per the flamegraph detail (`SQLite3::Statement#step`). At time of extraction this remains an open incident with no confirmed resolution.

### Claim 10: The nightly backup strategy accepts up to roughly a day of potential data loss in a worst-case host failure, which the engineer explicitly states is no worse than the risk profile under the prior MariaDB setup
- **Evidence**: thomas0, answering a direct question from commenter `xavdid` about worst-case backup exposure.
- **Confidence**: settled (direct first-party statement about a specific, named operational risk, with an explicit before/after comparison)
- **Quote (the question)**: "So in worst case scenario where the host exploded in the 23rd hour, would all the comments/posts from the day be lost?"
- **Quote (the answer)**: "Yes that's what I believe would happen. This was true with the MariaDB setup as well."
- **Quote (the mechanism)**: "There's a nightly job which calls restic."
- **Our assessment**: This is a candid, specific acknowledgment of accepted operational risk rather than a claim that SQLite introduced a new risk — the team is explicit that the backup cadence (and therefore worst-case data-loss window) is unchanged from the prior database engine. Community replies (not from the Lobsters team) suggested alternatives — `litestream` for continuous replication, `sqlite3_rsync` for incremental backups — but a separate commenter (`kevincox`) reported reproducible corruption with `sqlite3_rsync` in his own testing ("I wouldn't trust it in prod (or at all really)"), and pushcx's only commitment was to "file a feature request" for more frequent backups as follow-up work, not to implement it immediately. The gap between "acknowledged risk" and "risk actually closed" is worth preserving as-is.

### Claim 11: SQLite's out-of-the-box defaults required deliberate production hardening via explicit PRAGMA configuration, and a community-shared "make SQLite sane" config was offered as a reference
- **Evidence**: Discussion thread responding to a reader question about SQLite's write-concurrency model; commenter `zie` shared a specific PRAGMA configuration block described as "current."
- **Confidence**: emerging (a community-contributed configuration, not confirmed as what Lobsters itself actually runs in production — thomas0 and pushcx did not confirm or deny using this exact config)
- **Quote**: "Yes-ish. It does have one, but the default situation is pretty terrible, but you can make it sane. Here is my current make SQLite sane config along with sources for more info."
- **Our assessment**: See Concrete Artifacts for the full PRAGMA block. The framing — SQLite's defaults are "pretty terrible" for concurrent server workloads and require explicit opt-in hardening (WAL mode, busy timeout, synchronous level, mmap size) — is corroborated independently by thomas0's own unprompted complaint in Claim 12 ("I'm constantly surprised by the default choices of SQLite"). This is a recurring, specific theme across multiple independent commenters in the same thread, not a single person's opinion.

### Claim 12: The migration surfaced concrete SQLite-vs-MariaDB behavioral gaps that required application-level workarounds: no unsigned bigint type, weaker (ASCII-only) case-insensitive collation, and non-default full-text-search table configuration
- **Evidence**: thomas0's "SQLite lessons" retrospective list, itemizing three specific technical gaps encountered during the migration.
- **Confidence**: settled (first-party, specific, technically falsifiable claims about SQLite's type system and collation behavior)
- **Quote (unsigned bigints)**: "SQLite doesn't support unsigned bigints. Previously, the mariadb was using unsigned bigints for certain ids, so we had to switch those to bigints for the migration."
- **Quote (collation)**: "Collation in SQLite is rather weak compared to MariaDB. Lobste.rs used utf8mb4_general_ci in MariaDB, but used NOCASE in SQLite. The downside of NOCASE is that it only supports ASCII characters, not the full UTF case folding."
- **Quote (FTS default)**: "Use the preferred Contentless-Delete Tables in SQLite for your full text search tables. These are not the default. I'm constantly surprised by the default choices of SQLite."
- **Our assessment**: The collation gap is the most consequential of the three for a UGC site: `NOCASE`'s ASCII-only case folding means that non-ASCII usernames, tags, or search terms that differed only by case under MariaDB's `utf8mb4_general_ci` could now be treated as distinct under SQLite — a silent behavioral change with no test failure to catch it unless someone specifically tests non-ASCII case-folding. Combined with Claim 5's point that search *ranking* also changed as a side effect of the migration (mentioned by thomas0 elsewhere in the thread, not separately quoted here), this establishes that "migrate the schema and pass the test suite" does not guarantee behavioral equivalence for text/search semantics — those need dedicated verification beyond a general-purpose test suite.

## Concrete Artifacts

### Migration PR statistics (from Willison's blog post, corroborated by thomas0's account)

```
PR #1927 "Migrate to SQLite" (Thomas Dziedzic / thomas0) — the 3rd and final attempt
  +735 / -593 lines, 30 commits, 188 files changed
  Built on prior PRs: #1705 (1st attempt, closed stale), #1871 (2nd attempt),
  #1924 (revert of the failed Feb 21st deploy)

Timeline:
  2018 (Aug)  — issue #539 "Migrate to SQLite" opened; PostgreSQL originally planned
  2019        — thomas0 first comments on #539, suggests MySQL as MariaDB-compatible alt
  2025 (~)    — K1's acquisition of MariaDB reopens the migration discussion
  2025 (Feb)  — Rahul asks "Can lobsters run on sqlite?" with a detailed proposal
  2025 (Jun)  — thomas0 officially takes on the project
  2025 (Aug)  — 1st PR attempt opened, later closed stale by GitHub's bot
  2026 (date unstated) — 2nd PR attempt (#1871), includes perf testing + custom
                migration script since no existing MariaDB/MySQL→SQLite tool sufficed
  2026-02-21  — 1st production deploy attempt: read-only traffic spikes all CPUs to
                100%; team reverts (PR #1924)
  2026 (~Feb 23) — 3rd PR attempt (#1927) opened, with 3 targeted perf fixes for the
                full-table-scan and N+1 issues found during the failed deploy
  2026-07-11  — 2nd (successful) production deploy
  2026-07-13/14 — Success announced on lobste.rs and picked up by Willison's blog
  2026-07-17  — Post-migration cleanup migration deletes 3.2M vote rows (Rails bug);
                site enters unresolved severe performance regression after recovery
```
*Source: Simon Willison's blog post + thomas0's/pushcx's comments on the lobste.rs
announcement thread (`lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite`),
fetched 2026-07-18. Some dates (2nd PR attempt date, exact 3rd-attempt open date)
are approximate/unstated in the source and are marked as such above.*

### Database file sizes (from the thread, pushcx)

```
primary content db:  ~3.8 GB
cache db:              1.1 GB
queue db:              218 MB
rack_attack db:        555 MB  (still growing — <8 days into its retention window
                                 at time of comment; swings with scraper traffic)
```
*Source: pushcx, lobste.rs thread comment, confirming figures Willison's post
also states for the primary db.*

### Community-shared "make SQLite sane" production PRAGMA config (comment by `zie`)

```
PRAGMA foreign_keys=ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA busy_timeout = 5000;
PRAGMA temp_store = MEMORY;
PRAGMA mmap_size = 134217728;
PRAGMA journal_size_limit = 67108864;
PRAGMA cache_size = 2000;
```
*Source: commenter `zie`, lobste.rs thread, offered as "my current make SQLite
sane config" in response to a reader's concurrency-model question. Also noted:
"also turn on immediate mode so the busy_timeout works." This is a community
suggestion, not confirmed as Lobsters' actual production configuration.*

### Incident timeline (from pushcx's comment, posted 2026-07-17 23:13 UTC)

```
[overnight, ~2026-07-16/17] Cleanup migration (nullable key column, prep to drop
    a MariaDB-specific comment-sorting kludge) silently deletes 3.2M comment-vote
    rows via a Rails migration bug.
[overnight]  Bug goes undetected — comment scores are memoized, so scores only
    reset to 1 when a comment is next upvoted, not immediately.
[~morning]   pushcx notices score anomalies, puts site in read-only mode to
    investigate. ~90 minutes to identify cause (a Rails bug, cross-linked to a
    specific Rails PR).
[~+3 hours]  Votes restored: bulk restore from nightly backups, plus manual
    reconstruction of the most recent votes from HTTP server access logs.
[later that day] Site exits read-only mode. Becomes "noticeably sluggish" —
    pages "often taking seconds to load, sometimes over 10."
[+hours]     pushcx, @355E3B, and thomas0 debug the slowdown without finding a
    root cause: CPU pinned (~85% vs. a ~25% pre-incident baseline), disk nearly
    idle, flamegraph time concentrated in SQLite3::Statement#step, even a
    single-row indexed primary-key SELECT can stall for seconds.
[end of day]  Team stops debugging for the night; incident left unresolved.
```
*Source: pushcx, lobste.rs thread, comment timestamp 2026-07-17 23:13:20 UTC.
Reconstructed as a timeline from the prose account; all facts are directly
stated in the source, ordering follows the source's own narrative order.*

## Cross-References

- **Corroborates**: This source has minimal direct topical overlap with the
  existing corpus — it is a non-agentic, human-executed infrastructure/database
  migration, whereas the corpus's other `blog-simonwillison-sqlite-*.md` notes
  (`blog-simonwillison-sqlite-agents-md.md`, `blog-simonwillison-sqlite-utils-40rc1.md`,
  `blog-simonwillison-sqlite-utils-40rc2.md`, `blog-simonwillison-sqlite-utils-40-stable.md`,
  `blog-simonwillison-sqlite-column-provenance.md`) all concern SQLite *tooling*
  built by Willison himself, AI-assisted development of that tooling, or SQLite
  governance policy toward AI agents. The only genuine thematic corroboration is
  weak and general: these notes collectively establish that SQLite received
  sustained, serious engineering investment across 2026 (a new major sqlite-utils
  release, active governance-policy development, and now a large-scale production
  migration), consistent with this source's framing of SQLite as viable production
  infrastructure "in 2026" (per the blog post's closing line, quoted under Guide
  Impact). No specific numbered claim from those notes overlaps with this one
  closely enough to cite by claim number.
- **Contradicts**: This source contradicts itself. **Filed as issue #2005**
  ("Lobsters SQLite migration: unqualified success vs. data-loss incident +
  unresolved perf regression"): Claim 1 (posted ~2026-07-13, "passed with flying
  colors") vs. Claims 8-9 (posted ~2026-07-17, silent 3.2M-row data loss plus a
  severe, unresolved CPU/latency regression), both from the identical primary
  source (the same lobste.rs thread, the same two named authors) describing the
  same migration four days apart. Recommended verdict left as `unresolved` in the
  filed issue pending a resolution update from the source thread — see that
  issue's "Additional context" for a note to re-check the thread before assigning
  any other verdict.
- **Extends**: No existing corpus source covers production database-engine
  migrations, SQLite production PRAGMA tuning, or SQLite-vs-MariaDB behavioral
  gaps (collation, unsigned integer types, FTS table configuration) — this note
  does not build on prior corpus coverage in this area; it opens it.
- **Novel**: Everything in this note is novel to the corpus: (1) a concrete,
  large-scale (community site, 3.8GB+ of data) production database-engine
  migration case study with real before/after operational metrics; (2) a
  documented two-attempt deployment failure/recovery pattern (Claim 6); (3) a
  SQLite-specific verification technique — bytecode-instruction-count assertions
  against query plans — not previously documented in the corpus (Claim 7); (4) a
  live, in-progress production incident (data loss + unresolved perf regression)
  documented from the admin's own real-time account (Claims 8-9); (5) a
  community-contributed SQLite production hardening PRAGMA reference (Concrete
  Artifacts); (6) SQLite-vs-MariaDB behavioral-parity gaps encountered during a
  real migration (Claim 12). Notably, no AI/agentic tooling is mentioned anywhere
  in the source as having been used for the migration itself — this is a
  traditional, human-executed engineering effort, which is itself a data point
  about the corpus's scope (see Guide Impact and Extraction Notes).

## Guide Impact

- **This source's direct fit with the guide's stated scope (harness engineering,
  daily agentic workflows, verification, context engineering, team adoption,
  security) is limited** — no coding agent or AI tool is credited anywhere in the
  source as having been used for the migration, the incident response, or the
  fixes. The guide should not cite this source as an "AI-native engineering"
  case study; it is a traditional infrastructure/database migration story that
  happens to be well-documented and instructive on adjacent themes. The two
  genuine points of overlap with the guide's actual chapters are below.
- **Chapter 03 (Verification)**: Claim 7 (the bytecode-instruction-count technique
  for asserting "no full table scans" in a test, with the Axiom ORM as prior art,
  plus `ankhers`' caveat that it only works against sufficiently large/varied test
  tables) is a concrete, previously-undocumented verification pattern applicable
  to any SQLite-backed test suite — agentic or not. Claim 5 (the existing test
  suite as the stated enabler of a risky migration without "a ton of manual
  testing") and Claim 12 (search-ranking and collation behavior silently changed
  despite the test suite passing) together make a specific, two-sided point worth
  adding: a general-purpose test suite is necessary but not sufficient for
  verifying behavioral equivalence across a data-layer migration — text/collation/
  ranking semantics need dedicated tests that a typical CRUD test suite won't
  exercise.
- **Chapter 02 (Harness Engineering) — incident response / rollback discipline**:
  Claim 6 (first deploy attempt: revert immediately under live production
  degradation rather than debug in place, then root-cause offline before
  re-attempting) is a generalizable incident-response pattern independent of
  whether the deploying agent is human or AI-assisted: prioritize restoring
  service over diagnosing live, and don't re-attempt until the specific failure
  mode is reproduced and fixed. If the guide ever covers agent-driven deployment
  or migration workflows, this is a citable human-precedent pattern for what
  "safe revert-first" discipline looks like in practice.
- **No chapter currently covers infrastructure/deployment architecture decisions
  (e.g. "when to choose SQLite vs. Postgres") or production-incident postmortems
  as a topic in their own right** — the Prospector's triage comments on issue
  #1987 proposed several chapter mappings (referencing "Ch05 Deployment &
  Infrastructure," "Ch03 Scaling") that do not correspond to any file under
  `guide/` (the actual chapters are 00-principles, 01-daily-workflows,
  02-harness-engineering, 03-verification, 04-context-engineering,
  05-team-adoption, 06-security-threat-model). This note maps the source's real,
  usable content to the two chapters above rather than to the triage comments'
  proposed (non-existent) chapter names.

## Extraction Notes

- **Fetching method**: The blog post itself was first fetched via WebFetch, which
  returned an AI-summarized (not verbatim) version — per MINER.md §2a this is
  insufficient for quote extraction, so the blog post and the linked lobste.rs
  thread were both re-fetched via direct `curl` requests to get raw HTML, from
  which all quotes in this note were extracted and checked character-for-character
  against the source HTML (including exact wording, punctuation, and the specific
  numeric figures). The GitHub PR page (`github.com/lobsters/lobsters/pull/1927`)
  was also fetched via `curl`, but returned a client-rendered GitHub app shell
  with no server-rendered PR description text extractable from raw HTML within a
  reasonable time budget; no quotes in this note are drawn from that fetch — the
  PR's diff statistics are instead sourced from Willison's blog post text and
  cross-corroborated by thomas0's own narrative account in the thread.
- **Sub-pages followed** (per MINER.md §1, "follow up to 5 linked pages that seem
  substantive"): the lobste.rs announcement thread (fetched in full, ~197KB HTML,
  111 comments — read through the first ~30 comments in detail, which contained
  all claims extracted here; the remainder of the thread continues into more
  granular technical tangents — PRAGMA semantics, strict-mode table debates — not
  extracted as separate claims since they did not add claims beyond Claim 11's
  PRAGMA artifact). The GitHub PR page was attempted but not usable (see above).
  The two GitHub issue-comment permalinks cited inline by thomas0 (from 2018 and
  2025, documenting the multi-year planning history) were not independently
  fetched; the timeline in Claim 3/Concrete Artifacts relies on thomas0's own
  narrative summary of those comments, not on independently re-verified issue
  text — flagged here in case a future note wants to verify those primary GitHub
  issue comments directly.
- **The thread is a live comment section that changed after Willison's blog post
  was published.** Willison's post (2026-07-14) captures only the initial success
  announcement (Claim 1). The incident described in Claims 8-9 was posted to the
  same thread on 2026-07-17, three days after Willison's post and roughly the same
  day as this note's extraction (2026-07-18) — this note captures a more complete
  picture than the blog post alone by reading the live thread rather than stopping
  at the blog post's own text, per MINER.md §1's instruction to read deeply and
  follow substantive linked pages rather than summarizing the first few paragraphs.
  Given the incident was actively unresolved at extraction time, `last_checked`
  and `date_extracted` are both set to 2026-07-18; this note should be re-checked
  if the guide ever cites Claims 8-9, since the incident's resolution/root cause
  was not yet known.
- **Contradiction filed**: Issue #2005, per MINER.md §4a — see Cross-References →
  Contradicts above. Checked existing `contradiction`-labeled issues and
  CONTRADICTIONS.md entries C-001 through C-008 before filing; none cover SQLite,
  Lobsters, or database migrations.
- **No cross-reference claim-number citations were made** to other source notes
  (see Cross-References → Corroborates) because, per MINER.md §4b, none of the
  existing SQLite-tagged notes contain a claim specific enough to cite by number
  without overstating the overlap — the existing notes are about a different
  author-maintained tool (sqlite-utils) and a different topic (AI-agent
  governance), not production database migrations. This is a deliberate choice
  to avoid a superficial cross-reference per MINER.md's Quality Bar.
