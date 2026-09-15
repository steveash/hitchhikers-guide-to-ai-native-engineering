---
source_url: https://simonwillison.net/2026/Sep/11/datasette-2/
source_type: blog-post
title: "datasette 1.0a39"
author: Simon Willison (with Alex Garcia)
date_published: 2026-09-11
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: emerging
issue: "#3445"
---

# datasette 1.0a39

> A one-line "beat" pointing to the substantive Datasette blog security-release
> announcement: Datasette 1.0a39 and 0.65.4 fix a large batch of
> permission-check and injection-adjacent vulnerabilities found via the
> project's first full "coding agent security audit" — a multi-round sweep
> using Claude Fable 5.1, GPT-5.6 Sol, and GPT-6 Astra, triggered by an
> external contributor's AI-assisted vulnerability reports, with every issue
> reviewed by two humans (one writing a reproducing test, the other
> implementing the fix) in addition to the models.

## Source Context

- **Type**: blog-post. The entry point is a two-sentence "beat" at
  simonwillison.net (Willison's short-form release-announcement format,
  consistent with `blog-simonwillison-datasette-1-0a38.md` and
  `blog-simonwillison-datasette-1-0a34.md`) that itself contains no security
  detail — it links straight to the actual announcement. Per MINER.md §1, the
  linked page (datasette.io/blog/2026/september-security-releases/, ~350
  words) and both linked changelogs (docs.datasette.io `/en/latest/` and
  `/en/stable/` changelog anchors for `v1-0-a39` and `v0-65-4`) were fetched
  and are the basis for nearly all extraction in this note. All four pages
  were retrieved via direct HTML fetch (not WebFetch summarization) and quotes
  were matched character-for-character against the stripped HTML.
- **Author credibility**: Simon Willison is the creator of Datasette and
  co-author (with Alex Garcia, a named collaborator with his own site,
  alexgarcia.xyz) of this release's fixes. This is first-party vulnerability
  disclosure and release documentation from the people who wrote the fixes,
  in a shared private repository, with concrete changelog entries as
  supporting evidence. No vendor affiliation to the three LLM providers named.
- **Scope**: Covers two simultaneous releases (1.0a39 for the 1.0 alpha
  series, 0.65.4 for the 0.65.x stable line), the audit methodology and
  human-AI division of labor that produced them, and the two releases'
  changelogs. Does NOT cover: CVE identifiers, proof-of-concept exploits for
  any individual bug, the count of issues found ("a significant number" is
  never quantified), the specific prompts or harness used to run the three
  LLMs, or any measurement of the audit's false-negative rate or cost. The
  post explicitly withholds the automated tests that would reveal
  vulnerability mechanics, so several fixes are documented here only at the
  level of "what changed," not "how it was exploitable."

## Extracted Claims

### Claim 1: The two releases bundle fixes from two distinct sources — external researcher reports and the maintainers' own internal security audit
- **Evidence**: Direct framing statement in the Datasette blog release post, first-party.
- **Confidence**: settled (first-party release announcement)
- **Quote**: "These releases bundle a number of different fixes, some reported by external researchers and others found by our own extensive security audit."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This framing matters for scoping the rest of the note: not every fix in 1.0a39/0.65.4 came from the LLM-assisted audit described in Claims 2–5 below. The post never separates which specific changelog bullets came from which source, so the technical claims below (Claims 7–10) should be read as "fixes shipped in this release," not "fixes the LLM audit specifically found."

### Claim 2: The internal audit was directly triggered by an external contributor's AI-assisted vulnerability reports
- **Evidence**: Direct first-party attribution naming the external reporter (Sevban Dönmez, linked to a GitHub profile in the post) as the proximate cause of the audit.
- **Confidence**: settled (first-party, named attribution)
- **Quote**: "Sevban Dönmez submitted several AI-assisted vulnerability reports to the project, which inspired us to run a full audit using a combination of Claude Fable 5.1, GPT-5.6 Sol, and GPT-6 Astra."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This is a concrete instance of a two-stage pattern: an outside contributor's own AI-assisted security research (not otherwise detailed in this source — no link to Dönmez's actual reports) prompts the maintainers to run a broader, project-initiated audit using their own choice of three named frontier models. The causal chain (external AI-assisted find → internal AI-assisted sweep) is asserted but not independently verified here; we only have the maintainers' own account of the trigger.

### Claim 3: This was the first time Datasette's maintainers ran a full, dedicated "coding agent security audit" of the codebase
- **Evidence**: Direct first-party statement distinguishing this audit from prior security work (including the 1.0a38 SQL injection fix documented in `blog-simonwillison-datasette-1-0a38.md`, which was not described as agent-audit-driven).
- **Confidence**: settled (first-party statement of a milestone)
- **Quote**: "This is the first time we've run a thorough coding agent security audit."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This corroborates `blog-simonwillison-datasette-1-0a38.md`'s Extraction Notes finding — that the August 2026 SQL injection fix was reported/fixed without any stated LLM-assisted audit process. Read together, the two notes show Datasette's security process moving from ad hoc, individually-reported-and-fixed bugs (1.0a38) to a systematic, multi-model audit sweep (1.0a39) within about five weeks — a documented before/after in the same project's own security practice.

### Claim 4: The audit ran multiple rounds specifically to search for variants of already-found issues, and this systematic sweep surfaced many more problems than the initial trigger
- **Evidence**: Direct first-party description of the audit's iterative methodology.
- **Confidence**: settled (first-party process description), though the outcome ("a significant number of problems") is anecdotal — never quantified
- **Quote**: "Several rounds of auditing (looking for similar issues to those that were already found) revealed a significant number of problems."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: The stated methodology is pattern-generalization, not just fixing the specific bugs Dönmez reported — each confirmed finding became a seed for a further round of "find similar issues" auditing. This is a specific, repeatable technique (treat each confirmed vulnerability class as a query for more instances of the same class) rather than a generic "we used AI to scan the code" claim. The lack of a concrete count ("a significant number") limits how much weight this claim can bear as evidence of audit thoroughness — it is a qualitative, self-reported outcome.

### Claim 5: The two maintainers split audit-response labor by role — one writes a reproducing test, the other implements the fix — specifically to guarantee two independent human reviewers per issue, on top of the coding agents
- **Evidence**: Direct first-party description of the review workflow, naming both participants (Willison and Garcia) and the specific division of labor.
- **Confidence**: settled (first-party workflow description)
- **Quote**: "Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us would create the automated tests highlighting the issue, then the other would implement the fix. This ensured that two separate humans had eyes on each of the issues, in addition to our coding agents running different models."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This is the most reusable process pattern in the source: the test-writer and the fix-writer are deliberately different people, so no single person's blind spot (human or model-induced) reaches production unreviewed by a second person. The explicit phrase "in addition to our coding agents running different models" frames the multi-model audit (Claude Fable 5.1, GPT-5.6 Sol, GPT-6 Astra) as a third layer of independent scrutiny stacked on top of, not a replacement for, two-human review — a specific human-AI collaboration shape for security-critical work, directly answering the triage comment's "how do teams coordinate human and AI effort" question.

### Claim 6: Fixes were developed on the main branch first, then a selected subset was backported to the 0.65.x stable line, so both releases could ship the same day
- **Evidence**: Direct first-party statement, independently corroborated by diffing the two changelogs: the 1.0a39 changelog lists 18 distinct security-fix bullets; the 0.65.4 changelog lists 6 bullets, of which 5 have counterparts in the 1.0a39 list (case-insensitive permission names, `?_through=` permission, SQL identifier escaping for untrusted schema column names — worded more narrowly in 0.65.4 as "primary-key column names... including row lookups and pagination" — `Cache-Control` tightening, and extension-loading lockdown). The sixth 0.65.4 bullet ("Full-text search index detection now uses parameterized SQL and treats wildcard characters in table names literally") has *no* counterpart bullet in the 1.0a39 list; the nearest 1.0a39 FTS bullet is about permission-checking, not SQL parameterization. So the backport is a selected, largely-overlapping subset rather than a strict subset of the 1.0a39 list.
- **Confidence**: settled (first-party statement plus independently verifiable changelog comparison)
- **Quote**: "We fixed these on main, and then backported selected fixes to the 0.65.x branch so we could release both versions on the same day."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This extends `blog-simonwillison-datasette-1-0a38.md` Claim 4, which documented a security fix landing in both the 1.0a and 0.65.x lines on the same day but did not describe *how* the maintainers decided what to backport. This source makes the selection process explicit: backporting is deliberate and partial, not automatic or complete — for example, the 1.0a39-only fixes (foreign-key permission checks, primary-key-resolution-order changes, JSON write-API permission improvements, write-SQL `CREATE VIEW` permission checks, HTML escaping for untrusted schema names, URL-scheme validation, cookie `expire_after` enforcement, restricting API-token creation for restricted actors, and clickjacking protection) did not ship to 0.65.x in this release. Practitioners pinned to 0.65.x should not assume "a security release shipped" means "every fix in the alpha line's release also reached me."

### Claim 7: Most of the security fixes target permission-check gaps reachable through case-normalization, discovery/schema endpoints, and query parameters — not the core query-execution path itself
- **Evidence**: Verbatim changelog bullets from the 1.0a39 changelog (`docs.datasette.io/en/latest/changelog.html#v1-0-a39`).
- **Confidence**: settled (first-party changelog, directly verifiable against the linked docs)
- **Quote**: "Table and view permission checks now take SQLite's case-insensitive names into account." / "Viewing a full-text search index table now checks you have permission to view the table from which it draws its content." / "Table filters using `?_through=` require permission to view the intermediate table." / "Row endpoints check permissions before resolving primary keys, to avoid revealing the existence of an otherwise invisible primary key."
  *(Source: docs.datasette.io/en/latest/changelog.html#v1-0-a39)*
- **Our assessment**: The common shape across these bullets is that a primary permission check existed (e.g., "you need `view-table` to see a table") but a secondary code path — a case-variant table name, a derived FTS index, a `?_through=` join target, an intermediate lookup needed only to resolve a row — did not re-check that same permission before touching the same data. This is the same failure category `blog-simonwillison-datasette-1-0a38.md` documented for `execute-sql` (a permission check existing but not covering every path to the protected data), now shown to recur across at least six different discovery/rendering endpoints rather than being a one-off SQL-injection bug. For the guide: this is evidence that "add a permission check" is not a one-time fix per capability — it requires auditing every code path that can reach the same underlying data, including secondary/derived views of it.

### Claim 8: The release also fixes injection-and-rendering-adjacent bugs distinct from the permission-check category — SQL/HTML identifier escaping for untrusted schema names, and URL-scheme validation before rendering links
- **Evidence**: Verbatim changelog bullets.
- **Confidence**: settled (first-party changelog)
- **Quote**: "Fixed SQL identifier escaping for column names from untrusted database schemas." / "Fixed HTML escaping for column names from untrusted database schemas." / "URL columns now render links only for validated HTTP or HTTPS URLs."
  *(Source: docs.datasette.io/en/latest/changelog.html#v1-0-a39)*
- **Our assessment**: These three bullets share a root cause distinct from Claim 7's permission gaps: Datasette treats *column names themselves* (not just row data) as untrusted input when the database schema itself is attacker-influenced — a schema-as-attack-surface class of bug. The URL-rendering fix ("validated HTTP or HTTPS URLs" only) implies the prior behavior could render arbitrary URL schemes (e.g., `javascript:`) as clickable links from untrusted column data, a classic stored-XSS-adjacent pattern. Neither of these is about the LLM-audit's headline permission-check theme, which is a useful caveat against assuming the whole release is one bug class.

### Claim 9: Several fixes harden session and authorization behavior unrelated to SQL or permission checks — response caching, cookie expiry, and API token issuance for restricted actors
- **Evidence**: Verbatim changelog bullets.
- **Confidence**: settled (first-party changelog)
- **Quote**: "Private and personalized dynamic responses now use `Cache-Control: private, no-store`. Anonymous dynamic responses vary by `Cookie` and `Authorization`." / "Actor cookies now respect `expire_after`." / "Restricted actors can no longer create API tokens."
  *(Source: docs.datasette.io/en/latest/changelog.html#v1-0-a39)*
- **Our assessment**: The `Cache-Control` fix addresses a distinct risk class from the rest of the release: a shared or intermediate cache (browser, CDN, proxy) could previously have stored and replayed a private, personalized response to a different user — a caching-layer data leak, not a Datasette-internal permission bug. This is worth flagging separately because it is the kind of vulnerability that a permission-focused code audit (human or LLM) can miss if it only reasons about application-level access checks and not about HTTP caching semantics.

### Claim 10: The release adds defense-in-depth hardening not tied to a specific reported vulnerability — clickjacking protection, case-insensitive secret redaction, and locking SQLite extension loading after startup
- **Evidence**: Verbatim changelog bullets.
- **Confidence**: settled (first-party changelog)
- **Quote**: "Stored-query create, edit and delete forms now block framing to prevent clickjacking." / "Configuration secret redaction now matches key names case-insensitively." / "SQLite extension loading is disabled after extensions supplied using `--load-extension` have been loaded."
  *(Source: docs.datasette.io/en/latest/changelog.html#v1-0-a39)*
- **Our assessment**: The extension-loading lockdown is notable as a capability-reduction fix in the classic "principle of least privilege" mold — once startup-time extensions are loaded, the ability to load further extensions is revoked, closing a window where a compromised request-handling path could otherwise load an arbitrary native SQLite extension. This reads as exactly the kind of secondary-hardening fix a broad "look for similar issues" audit round (Claim 4) would surface even without an external report naming it.

### Claim 11: The maintainers deliberately withheld some automated tests that would reveal vulnerability details, to give users time to upgrade before exploit mechanics become public
- **Evidence**: Direct first-party statement of a coordinated-disclosure practice.
- **Confidence**: settled (first-party statement of policy)
- **Quote**: "We are holding back some of the automated tests from the public repo to give people more time to upgrade before we spell out the details of the vulnerabilities described by those tests."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This is a specific operational consequence of running an LLM-assisted audit that produces working exploit-demonstrating tests as a byproduct: those tests are themselves disclosure material and have to be handled with the same care as a manually-written PoC. Teams adopting a similar coding-agent audit workflow should expect the audit's own artifacts (reproducing tests) to need a separate, delayed-disclosure release process, not just the code fix itself.

### Claim 12: The maintainers had already deployed these fixes to their own hosted product, Datasette Cloud, ahead of or alongside the public release
- **Evidence**: Direct first-party statement.
- **Confidence**: settled (first-party statement, though not independently verifiable — no timestamp given for when the Datasette Cloud rollout occurred relative to the public release)
- **Quote**: "We have already rolled these fixes out to Datasette Cloud."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This is a reasonable operational sequencing (patch your own hosted instances before publishing details that could be used against instances that haven't upgraded yet), consistent with Claim 11's delayed-disclosure practice for the automated tests. No detail is given on how much lead time Datasette Cloud had, so this should not be read as evidence of a specific responsible-disclosure window.

### Claim 13: The maintainers frame this audit as the start of an ongoing practice, motivated by a broader belief that frontier LLMs and coding agents have transformed the security ecosystem this year
- **Evidence**: Direct first-party editorial statement of intent and belief.
- **Confidence**: anecdotal (a stated intention and a broad industry characterization, neither backed by data in this source)
- **Quote**: "The software security ecosystem has been transformed this year by frontier LLMs and coding agents. We plan to continue auditing Datasette with these tools to help us stay ahead of further vulnerabilities."
  *(Source: datasette.io/blog/2026/september-security-releases/)*
- **Our assessment**: This corroborates the general "AI is changing the economics of security work" thesis in `blog-simonwillison-cybersecurity-proof-of-work.md` (see Cross-References), but from the practitioner-adoption side rather than the benchmark/economic-analysis side: a real, small, open-source-maintainer team (two people) is committing to recurring LLM-assisted audits as ongoing practice, not a one-off stunt. It is still a single project's stated intention as of this post — there is no evidence yet (in this source) of a second audit cycle actually happening.

## Concrete Artifacts

### Security release announcement (verbatim, from datasette.io/blog/2026/september-security-releases/)

```
Datasette 1.0a39 and 0.65.4 security releases
11th September 2026 at 00:04 UTC by Simon Willison

We have two big security updates for Datasette today - one for the 1.0
alpha series and another for the 0.65.x stable release:

- 1.0a39 changelog
- 0.65.4 changelog

If you are running Datasette instances on the public internet you should
upgrade now, in particular if you are using a Datasette authentication
plugin to protect private data.

These releases bundle a number of different fixes, some reported by
external researchers and others found by our own extensive security
audit. The software security ecosystem has been transformed this year by
frontier LLMs and coding agents. We plan to continue auditing Datasette
with these tools to help us stay ahead of further vulnerabilities.

Most of the issues we are fixing today affect Datasette instances that
are hosted on the public internet while providing authenticated users
with access to private data. We have already rolled these fixes out to
Datasette Cloud.

How we identified and fixed these issues

Sevban Dönmez submitted several AI-assisted vulnerability reports to the
project, which inspired us to run a full audit using a combination of
Claude Fable 5.1, GPT-5.6 Sol, and GPT-6 Astra. This is the first time
we've run a thorough coding agent security audit. Several rounds of
auditing (looking for similar issues to those that were already found)
revealed a significant number of problems. We fixed these on main, and
then backported selected fixes to the 0.65.x branch so we could release
both versions on the same day.

Alex Garcia and I worked together running and then responding to the
audit, working in a shared private repository. For most of the issues we
split the work: one of us would create the automated tests highlighting
the issue, then the other would implement the fix. This ensured that two
separate humans had eyes on each of the issues, in addition to our coding
agents running different models.

We are holding back some of the automated tests from the public repo to
give people more time to upgrade before we spell out the details of the
vulnerabilities described by those tests.
```
*Source: datasette.io/blog/2026/september-security-releases/, fetched 2026-09-15 via direct HTML retrieval.*

### 1.0a39 changelog security-fix list (verbatim bullets, docs.datasette.io/en/latest/changelog.html#v1-0-a39)

```
1.0a39 (2026-09-10)

This alpha release includes security fixes for permissions, SQL
construction, HTML rendering, authentication and caching, plus
improvements to application startup and write execution.

Some of the security fixes include:

- Table and view permission checks now take SQLite's case-insensitive
  names into account.
- Viewing a full-text search index table now checks you have permission
  to view the table from which it draws its content.
- Viewing SQLite statistics tables (sqlite_stat1 through sqlite_stat4)
  is now denied by a default.
- Table schema display now obeys the view-table permission.
- Table filters using ?_through= require permission to view the
  intermediate table.
- Foreign-key target and suggestion APIs, incoming foreign-key
  relationships and their row counts now respect view-table permission.
- Row endpoints check permissions before resolving primary keys, to
  avoid revealing the existence of an otherwise invisible primary key.
- Improved permission checks for the create-table API.
- The write SQL interface now checks view-table permission for tables
  referenced by CREATE VIEW statements.
- Fixed SQL identifier escaping for column names from untrusted
  database schemas.
- Fixed HTML escaping for column names from untrusted database schemas.
- URL columns now render links only for validated HTTP or HTTPS URLs.
- Private and personalized dynamic responses now use Cache-Control:
  private, no-store. Anonymous dynamic responses vary by Cookie and
  Authorization.
- Actor cookies now respect expire_after.
- Restricted actors can no longer create API tokens.
- Stored-query create, edit and delete forms now block framing to
  prevent clickjacking.
- Configuration secret redaction now matches key names
  case-insensitively.
- SQLite extension loading is disabled after extensions supplied using
  --load-extension have been loaded.

Other improvements and fixes:
- db.execute_write() now has a default execution time limit of
  2,000ms. Plugins can override this using time_limit_ms= or disable it
  using time_limit_ms=None. This limit is independent of the
  sql_time_limit_ms setting for read queries.
```
*Source: docs.datasette.io/en/latest/changelog.html#v1-0-a39, fetched 2026-09-15 via direct HTML retrieval.*

### 0.65.4 changelog security-fix list (verbatim bullets, docs.datasette.io/en/stable/changelog.html#v0-65-4)

```
0.65.4 (2026-09-10)

This release includes security fixes for permissions, SQL construction
and caching, backported to the stable 0.65.x branch.

Some of the security fixes include:

- Table and view permission checks now take SQLite's case-insensitive
  names into account.
- Table filters using ?_through= require permission to view the
  intermediate table.
- Fixed SQL identifier escaping for primary-key column names from
  untrusted database schemas, including row lookups and pagination.
- Full-text search index detection now uses parameterized SQL and
  treats wildcard characters in table names literally.
- Private and personalized dynamic responses now use Cache-Control:
  private, no-store. Anonymous dynamic responses vary by Cookie and
  Authorization.
- SQLite extension loading is disabled after extensions supplied using
  --load-extension have been loaded.
```
*Source: docs.datasette.io/en/stable/changelog.html#v0-65-4, fetched 2026-09-15 via direct HTML retrieval. Note the 0.65.4 wording for the third bullet ("primary-key column names... including row lookups and pagination") is more specific than the 1.0a39 phrasing of the same underlying fix ("column names"), and 0.65.4 adds a "full-text search index detection... parameterized SQL" bullet that has no exact-wording counterpart in the 1.0a39 list — the two changelogs describe overlapping but not identically-worded fixes for what appears to be the same underlying issue class.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 6 (open-source
    libraries become more valuable under a token-economy security model
    because hardening costs amortize across all users): this source is a
    concrete, real-world instance of that argument being enacted — Datasette
    is exactly the kind of widely-used open-source library Claim 6 describes,
    and its maintainers ran a security-hardening audit whose benefit accrues
    to every Datasette deployment, not just theirs. Claim 6 was framed there
    as an "anecdotal... logical argument... no empirical data on actual shared
    security spending" — this source is a specific data point (not a
    statistical one) toward that argument, though it does not resolve the
    "unmaintained libraries do not benefit" caveat also noted there.
  - `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 1 (AI-assisted
    vulnerability discovery has become a token-spend problem for defenders):
    this source corroborates the general shift toward AI-driven security
    auditing as practitioner reality, though at a much smaller and less
    quantified scale than the $12,500–$125,000-per-run AISI/Mythos figures in
    that note's Claims 2 and 5 — this is two humans and three named models
    doing an ad hoc, non-benchmarked audit, not a metered autonomous
    red-team campaign. The two sources describe the same broad trend at very
    different scales of rigor and cost-accounting.

- **Contradicts**: None filed. There is a scope difference worth flagging
  rather than a contradiction: `blog-simonwillison-cybersecurity-proof-of-work.md`
  frames AI security work as autonomous, metered, token-budgeted agent runs
  (Claim 1, Claim 5), while this source describes a workflow where two humans
  are permanently in the loop on every issue (Claim 5) and the models are
  described as audit assistants, not autonomous operators. These are
  different conditioning variables (a controlled capability evaluation vs. a
  real maintainer team's actual process) rather than opposing claims about
  what practitioners should do, so per MINER.md §4a this does not rise to a
  contradiction issue.

- **Extends**:
  - `blog-simonwillison-datasette-1-0a38.md` Claims 1–4 (the prior,
    non-audit-driven SQL injection fix and its same-day backport to 0.65.x):
    this source's Claim 3 explicitly marks the current release as the
    project's *first* dedicated coding-agent audit, implying 1.0a38's fix
    predates this practice. Claim 6 here also makes explicit *how* the
    same-day dual-branch release pattern documented in 1.0a38 Claim 4 is
    produced (fix on main, then a deliberately selected subset backported) —
    a mechanism 1.0a38 did not describe.
  - `blog-simonwillison-datasette-1-0a38.md` Claim 6 (Datasette's default
    posture allows arbitrary SQL execution unless an admin opts out, making
    permission-check gaps on secondary code paths a real risk): this source's
    Claim 7 shows that risk materializing repeatedly across different
    discovery/rendering endpoints (FTS tables, `?_through=` filters,
    foreign-key APIs, row primary-key resolution) rather than only in the
    single `execute-sql` bypass 1.0a38 documented.

- **Novel**:
  - **First corpus documentation of a named, multi-model coding-agent
    security audit workflow with an explicit two-human-review structure.**
    No other Datasette-related note, and no note found via keyword search
    across the corpus for "security audit" and related terms, documents a
    real team's process for coordinating human reviewers against multiple
    named frontier LLMs (Claude Fable 5.1, GPT-5.6 Sol, GPT-6 Astra) run in
    parallel on the same codebase for security auditing.
  - **First corpus example of a project explicitly withholding audit-derived
    automated tests as a disclosure-control measure** (Claim 11) — a
    process detail specific to the fact that an LLM-assisted audit produces
    working, reproducing tests as a direct byproduct of finding each bug.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 5's two-human-plus-multi-model
  review structure as a concrete, named pattern for verification on
  security-critical changes: assign the reproducing-test author and the
  fix author to different humans, and run multiple independently-configured
  coding agents (different model families) as an additional, non-replacing
  layer rather than trusting any single model's audit pass. This is a more
  specific recommendation than "have a human review AI output" — it
  specifies *which* two roles should be split between people, and that
  models should be used in parallel with each other, not just with a human.
- **Chapter 02 (Harness Engineering)**: Cite Claim 4's "audit in rounds,
  each round searching for variants of previously-confirmed issues" as a
  concrete technique for structuring an AI-assisted audit task, distinct
  from a single one-shot "scan this codebase for vulnerabilities" prompt.
  Recommend framing each confirmed finding as a seed for a follow-up
  audit pass targeting the same vulnerability class elsewhere in the
  codebase.
- **Chapter 05 (Team Adoption) / incident-response guidance**: Cite Claim 11
  (withholding audit-derived tests) and Claim 12 (patch owned infrastructure
  before public disclosure) as two concrete operational practices teams
  should adopt if they run a similar LLM-assisted security audit: the
  audit's own reproducing tests need the same disclosure handling as a
  manually-found exploit, and any self-hosted instances of the affected
  software should be patched before, or at minimum simultaneously with,
  public disclosure of the fix.

## Extraction Notes

- **The entry-point beat is content-free; nearly all extraction is from the
  linked Datasette blog post and its two linked changelogs**, followed per
  MINER.md §1. This mirrors `blog-simonwillison-datasette-mcp-02.md`'s
  finding that a thin simonwillison.net "beat" can link to a substantially
  richer page that is where the real corpus value lives.
- **All four pages (beat, security-release post, both changelogs) were
  fetched via direct HTML retrieval (`curl`) and stripped of markup with a
  script, then every quote was checked against the raw HTML source (not the
  stripped text) to rule out tag-stripping artifacts** — e.g., the stripped
  text initially rendered "upgrade now ," with a spurious space before the
  comma because of an inline `<strong>` tag; the raw HTML confirmed the
  correct wording has no such space, which is what is quoted in this note.
  This follows the precedent set in `blog-simonwillison-datasette-1-0a38.md`'s
  Extraction Notes for handling similar rendering/markup artifacts.
- **No CVE identifiers, PoC payloads, or issue counts are given anywhere in
  either source page.** "A significant number of problems" (Claim 4) is the
  only quantification offered, and it is not a number. This note does not
  speculate about scale beyond counting changelog bullets directly (18 for
  1.0a39, 6 for 0.65.4, per Claim 6's assessment).
- **Three Prospector triage comments on this issue disagree substantially**
  about this source's novelty (high / medium / low-to-medium) and even about
  basic facts — one comment's "Existing notes that overlap" cites
  `blog-simonwillison-datasette-mcp-02.md` (a different Datasette topic, MCP
  row formatting, with no security content) as overlapping, which does not
  hold up on inspection; another cites `blog-thebatch-gpt55-hallucination-kimi-k26.md`
  as overlapping "LLM security capabilities," which is a model-benchmark
  source unrelated to Datasette or to an audit workflow. Per the task
  instructions, all three comments were treated as untrusted advisory input
  rather than authoritative fact, and this note's Cross-References section
  was built from independently reading the actual overlapping notes
  (`blog-simonwillison-datasette-1-0a38.md`,
  `blog-simonwillison-cybersecurity-proof-of-work.md`) rather than from any
  single triage comment's claim.
- **No contradiction issue filed.** See Cross-References → Contradicts above
  for the reasoning: the difference in AI-security-work framing between this
  source and `blog-simonwillison-cybersecurity-proof-of-work.md` is a scope/
  context difference (real small-team maintainer workflow vs. a controlled,
  metered capability evaluation), not a disagreement about what practitioners
  should do.
- **Cross-references verified**: `blog-simonwillison-datasette-1-0a38.md`
  Claims 1, 4, and 6, and its Extraction Notes, were confirmed by re-reading
  that note in full and matching claim numbers to its `### Claim N:` headings
  in document order. `blog-simonwillison-cybersecurity-proof-of-work.md`
  Claims 1, 2, 5, and 6 were confirmed the same way, including re-reading
  Claim 6's full quoted text before citing it here.
- **Confidence rationale**: `confidence_overall` is set to `emerging` rather
  than `settled`. The individual factual claims about what shipped and what
  the post says are `settled` (first-party, verifiable against the linked
  changelogs). But the higher-level claim this source is most valuable for —
  that a named multi-model coding-agent security audit process, with
  two-human review, is an effective and repeatable practice — rests on a
  single, self-reported instance with no independent verification of audit
  coverage, no comparison to a non-AI-assisted audit baseline, and an
  explicitly stated intention (Claim 13) to repeat the practice that has not
  yet been observed happening a second time in this corpus.
