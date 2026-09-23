---
source_url: https://simonwillison.net/2026/Sep/16/datasette-2/
source_type: blog-post
title: "datasette 0.65.5"
author: Simon Willison (vulnerability reported by dpfkdlemtp)
date_published: 2026-09-16
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: settled
issue: "#3624"
---

# datasette 0.65.5

> A two-sentence release "beat" pointing to GHSA-h547-rmjf-5m2m, a full
> security advisory disclosing that Datasette's `escape_sqlite()` identifier
> quoting used an anchored regex (`re.match()` against a `$`-terminated
> pattern) that Python allows to match immediately before a single trailing
> line feed — so a table name ending in `\n` was emitted unquoted, SQLite
> silently treated the LF as whitespace, and an actor authorized for the
> newline-suffixed name could read (and, on the 1.0 alpha line, rename) a
> permission-denied table of the same base name. The bug was found and
> reported five days after Datasette's own "first ever" multi-model coding
> agent security audit (documented in `blog-simonwillison-datasette-1-0a39.md`)
> shipped fixes for a related but distinct class of permission-check gaps.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release
  announcement format at simonwillison.net, 16th September 2026, tagged
  `security` and `datasette`). The beat itself is one sentence and links
  directly to a GitHub Security Advisory (GHSA-h547-rmjf-5m2m) that contains
  the full technical disclosure. Per MINER.md §1, the advisory page (a very
  long, formally structured vulnerability report, ~3,000 words) and the
  companion release beat for Datasette 1.0a40
  (simonwillison.net/2026/Sep/16/datasette/, which ships "the same security
  fix as 0.65.5") were also fetched, along with the 0.65.5 changelog entry
  (docs.datasette.io/en/stable/changelog.html#v0-65-5). All four pages were
  retrieved via direct HTML fetch and stripped of markup with a script; every
  quote below was checked against that stripped text. No separate
  datasette.io blog post exists for this release (unlike the 1.0a39/0.65.4
  releases) — the project's blog's most recent entry as of this extraction is
  still the 11th September post covered in `blog-simonwillison-datasette-1-0a39.md`.
- **Author credibility**: The beat and changelog are first-party, from
  Datasette creator Simon Willison. The advisory's technical content
  (root-cause analysis, exploit reproduction, CVSS scoring, patch) is
  authored by the external reporter `dpfkdlemtp` but published on
  `simonw/datasette`'s own GitHub Security Advisories page and credited by
  the maintainer as the source of the fix — i.e., a third-party report that
  the first-party maintainer confirmed, patched, and released against. The
  advisory itself is unusually rigorous: it includes exact commit hashes
  tested, a 639-case deterministic property-testing harness with a fixed
  seed, full pytest-suite pass counts on patched targets, SHA-256-hashed
  artifact manifests for an independent reproduction rerun, and an explicit
  "duplicate search" methodology (a hashed, timestamped GitHub API sweep) to
  rule out a pre-existing public report of the same root cause.
- **Scope**: Covers one vulnerability (GHSA-h547-rmjf-5m2m) in
  `datasette.utils.escape_sqlite()`, affecting Datasette <=0.65.4 and
  1.0a0–1.0a39, patched in 0.65.5 and 1.0a40. Does NOT cover: a CVE
  identifier (none was assigned — "No known CVE"), any other vulnerability
  in the same releases, or whether any real-world Datasette deployment was
  actually exploited. The advisory explicitly states it is not claiming
  exhaustive coverage of every `escape_sqlite()` call site (81 counted, not
  proven exhaustive) or of every other anchored-regex validator in the
  codebase (five related-but-unexploited validators are named but not fixed
  in this release).

## Extracted Claims

### Claim 1: A trailing newline in a requested table name could bypass Datasette's table-level permission checks and expose private rows, because `escape_sqlite()`'s "is this identifier safe to leave unquoted" regex used `.match()` against a `$`-anchored pattern, and Python's `$` matches immediately before one trailing line feed
- **Evidence**: First-party changelog entry plus the advisory's own root-cause section, which quotes the vulnerable code directly.
- **Confidence**: settled (maintainer-confirmed, patched, with the exact vulnerable and fixed code shown)
- **Quote**: "Fixed a security issue where a trailing newline in a requested table name could bypass table permissions and expose private rows."
  *(Source: docs.datasette.io/en/stable/changelog.html#v0-65-5)*
- **Our assessment**: This is a textbook instance of a permission-check being architecturally sound (a `view-table` check does run) while the *identifier resolution* underneath it silently maps two different authorized-resource strings (`"secret"` and `"secret\n"`) onto the same underlying SQLite object. The bug is not in the permission logic itself — it's in a shared low-level string-escaping utility that every table-permission check implicitly trusts to preserve identifier distinctness. This directly extends the pattern documented in `blog-simonwillison-datasette-1-0a39.md` Claim 7 (permission checks failing on secondary/derived code paths, e.g. case-insensitive names, FTS indexes) to a new sub-case: the *identifier normalization itself*, not just which endpoints re-check permissions.

### Claim 2: The root cause is specifically `_boring_keyword_re.match(s)` where `_boring_keyword_re = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")`, and Python's `.match()` with a `$` anchor accepts a string ending in exactly one trailing LF; `.fullmatch()` on the same pattern correctly rejects it
- **Evidence**: Verbatim code and interactive-shell-style demonstration in the advisory's "Root cause" section.
- **Confidence**: settled (verifiable against Python's own documented `re` semantics — `$` matches at the end of the string or just before a trailing newline)
- **Quote**: "Python's dollar anchor accepts a position immediately before exactly one final LF: `bool(_boring_keyword_re.match("secret\n"))  # True` `bool(_boring_keyword_re.fullmatch("secret\n"))  # False` `repr(escape_sqlite("secret\n"))  # 'secret\n' (unquoted)`"
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, "Root cause" section)*
- **Our assessment**: This is a specific, reusable, language-level gotcha for any Python codebase using `$`-anchored regexes to validate "is this string exactly this shape" for security-relevant decisions (here, "is this identifier safe to interpolate unquoted"): `$` is not equivalent to end-of-string in Python's `re` module the way a naive reader might assume — `\Z` or `.fullmatch()` is required for that. This is worth surfacing to the guide as a concrete named footgun, not just "validate your inputs."

### Claim 3: Because SQLite (not Datasette) is the layer that consumes the trailing LF as whitespace, the reporter argues this bug should not be classified as SQL injection (CWE-89) — the SQL grammar itself is unchanged, only an identifier-to-object mapping is confused
- **Evidence**: The advisory's own dedicated "This is not SQL injection" subsection, with a 639-case regression harness cited as supporting evidence that no other whitespace/control character passes the same faulty check.
- **Confidence**: settled (first-party technical argument from the report's author, who also authored the classification)
- **Quote**: "The regular-expression behavior admits only one final LF and nothing after it. SQLite consumes that LF as whitespace; it does not close a quote or introduce a token, expression, clause, or second statement. The SQL grammar is unchanged. [...] This should not be classified as SQL injection."
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, "This is not SQL injection" section)*
- **Our assessment**: This is a useful taxonomic distinction for practitioners triaging similar bugs: not every "an attacker-controlled string reaches raw SQL and produces unintended results" bug is SQL injection in the classic sense. Here the attacker cannot alter SQL structure at all — they can only cause an *authorization* check to be performed against a different string than the one the *execution* engine ultimately resolves. The advisory assigns CWE-625 (Permissive Regular Expression) as root cause, CWE-706 (Use of Incorrectly-Resolved Name or Reference) for the cross-layer mismatch, and CWE-863 (Incorrect Authorization) for the consequence — three distinct CWEs for one bug, none of them CWE-89. This is directly relevant to `blog-simonwillison-datasette-1-0a38.md` Claim 1, which *did* document a genuine SQL-injection-based permission bypass (GHSA-w3hf-fcg5-p4cc) in the same function family — the two bugs share a symptom (unauthorized table read) and a root component (`escape_sqlite`-adjacent identifier handling) but have different mechanisms, and this advisory explicitly distinguishes itself from that prior one (see Claim 8 below).

### Claim 4: The exploit path requires only an authenticated actor who is explicitly denied access to a plain table name but explicitly allowed access to that same name with a trailing newline appended, requested via Datasette's existing tilde-percent-encoding for the newline character
- **Evidence**: The advisory's "Preconditions" and "Read reproduction" sections, with an exact reproduced HTTP request/response trace.
- **Confidence**: settled (reproduced and traced by the reporter, with request/response codes shown)
- **Quote**: "GET /data/secret.json                  -> 403" / "GET /data/secret~0A.json?_shape=array  -> 200, PRIVATE marker present" / "DECOY marker absent"
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, "Read reproduction" section)*
- **Our assessment**: No SQL injection payload, no authentication bypass, and no unusual privilege is required — only a standard, documented Datasette URL-encoding mechanism (`~0A` for a newline in a path segment) applied to a table name the actor is legitimately authorized to see under its literal (newline-suffixed) name. The advisory reports this exact read-bypass reproduced across "table HTML, JSON array and object shapes, CSV, a row route, filtering, the table fragment, autocomplete, content negotiation, and 1.0 OPTIONS" — i.e., the bypass was not confined to one endpoint but present everywhere `escape_sqlite()`'s output reached a query.

### Claim 5: On the Datasette 1.0 alpha line only, an actor with `create-table`, `view-table`, and `alter-table` database-level grants (but explicitly denied on the specific protected table) could use this same identifier confusion to create the newline-suffixed sibling table via the built-in structured-write API, then use the alter/rename endpoint to rename the protected table entirely — a persistent schema modification, not just an unauthorized read
- **Evidence**: The advisory's "Deterministic 1.0 write/rename reproduction" section, with a full sequential HTTP request trace and before/after "ground truth" table-to-content mapping.
- **Confidence**: settled (reproduced on 1.0a38, 1.0a39, and a main snapshot, with an independently hash-verified rerun on a separate clean checkout)
- **Quote**: "GET  /data/secret.json                           -> 403" / "POST /data/-/create           table=\"secret\\n\"  -> 201" / "POST /data/secret~0A/-/insert decoy row          -> 201" / "GET  /data/secret~0A.json?_shape=array           -> 200, PRIVATE_WRITE_TARGET_4f91" / "POST /data/secret~0A/-/alter  rename to moved_private      -> 200" / "GET  /data/moved_private.json?_shape=array       -> 200, PRIVATE_WRITE_TARGET_4f91"
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, "Deterministic 1.0 write/rename reproduction" section)*
- **Our assessment**: This is the most severe consequence in the advisory: on the 1.0 alpha line (which has the newer structured create/alter write API that 0.65.x lacks), the bug escalates from a confidentiality-only read bypass to an availability/integrity issue — an attacker can make a protected resource disappear from its expected name and reappear under an attacker-chosen name, while the actual row contents remain intact. The reporter is careful to scope this precisely: "I did not execute [further writes to the renamed table] and treat that statement only as an inference" — the advisory does not overclaim beyond what was actually demonstrated. This is a good example of a security report distinguishing "demonstrated" from "plausible but untested" impact, worth citing as a disclosure-writing pattern in its own right.

### Claim 6: GitHub's own published severity score for the advisory (7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) is a single blended score, while the reporter recommended two separate, lower, version-scoped scores (6.7 for the 1.0 alpha write/rename chain, 5.3 for the 0.65.x stable read-only case) because the two release lines have materially different preconditions and impact
- **Evidence**: Direct comparison between the advisory's published "Severity" section (GitHub's own score) and the reporter's own "Severity" section with reasoned, version-scoped alternative scores.
- **Confidence**: settled (both scores are directly readable on the same advisory page; the discrepancy is a fact of the page, not an inference)
- **Quote**: "The impact and preconditions differ by release line, so I recommend version-scoped scoring." / Published score: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N" / "7.5" / "High"
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, reporter's "Severity" subsection and the advisory's top-level "Severity" panel)*
- **Our assessment**: This is a small but instructive gap between a reporter's nuanced, precondition-aware severity analysis (which explicitly separates confidentiality-only impact on the stable line from confidentiality+integrity impact on the alpha line, and argues against several alternative scorings with specific reasoning — e.g. rejecting `A:H` because "the rows survive, the rename is reversible, and the rest of Datasette remains available") and the single number that ends up as the advisory's headline severity. Teams consuming GHSA/CVSS scores as a triage signal should be aware the published top-line score can be a simplification that discards a more careful, version-scoped analysis available lower on the same page — read past the badge.

### Claim 7: The reporter explicitly identifies five other regex validators in the Datasette codebase with the same `.match()`-against-`$`-anchored-pattern shape, but did not demonstrate an exploitable impact for any of them, and recommends a broader hardening sweep as optional rather than required
- **Evidence**: The advisory's "Related validators, not separately exploited" section, naming each validator and its assessed risk.
- **Confidence**: settled as a code-inventory claim (these five call sites are named and their pattern is verifiable); the "no independent exploit" assessment is the reporter's own judgment, not independently re-verified by us
- **Quote**: "I recommend a repository-wide hardening audit that replaces anchored `.match()` validation with `.fullmatch()` or strict `\A...\Z` expressions where a final LF is outside the contract. That is broader than the one-line fix required for this demonstrated vulnerability."
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, "Related validators, not separately exploited" section)*
- **Our assessment**: This is a disciplined disclosure practice worth naming explicitly: the reporter separates the *minimal causal fix* (one line, `.match()` to `.fullmatch()` in `escape_sqlite()` only) from *defense-in-depth hardening* (sweeping every similarly-shaped regex in the codebase), and does not inflate the advisory's claimed severity by bundling unproven risks from the other five validators into the same report. This is a good template for how a vulnerability report should scope "demonstrated" fixes separately from "here are other places with the same code smell."

### Claim 8: This vulnerability is a distinct root cause from a prior, related Datasette SQL-injection disclosure (GHSA-w3hf-fcg5-p4cc, fixed in 0.65.3/1.0a38) that involved `]` breaking square-bracket identifier quoting, and this report reproduces successfully on top of that earlier fix
- **Evidence**: The advisory's own "Duplicate distinction" section, explicitly comparing the two reports' root causes and confirming the new bug is present on releases that already contain the prior fix.
- **Confidence**: settled (first-party technical comparison, cross-checked by us against `blog-simonwillison-datasette-1-0a38.md`, which documents GHSA-w3hf-fcg5-p4cc's parent SQL-injection disclosure)
- **Quote**: "This report is distinct: it reproduces on 0.65.3 and 1.0a38—the releases containing that advisory's fix—and on later refs; its root is Python `$`/`.match()` final-LF behavior; SQLite receives only an identifier followed by whitespace, so SQL grammar is unchanged; its consequence is authorization-to-object-name confusion, including a 1.0 structured-write rename path."
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, "Duplicate distinction" section)*
- **Our assessment**: This is now the *third* documented identifier-escaping/permission-bypass bug in Datasette's `escape_sqlite`-adjacent code within about six weeks of corpus-covered releases (the August `]`-quoting SQL injection in `blog-simonwillison-datasette-1-0a38.md`; the September 10–11 case-insensitivity, FTS, and schema-column-name fixes in `blog-simonwillison-datasette-1-0a39.md`; and this September 16 trailing-newline bug). Read together, the three notes show that "identifier handling in a permission-gated SQL tool" is a recurring, not one-off, vulnerability class for this project — each fix closed one specific shape of the problem without the earlier fixes' review catching the next shape.

### Claim 9: This bug survived Datasette's own "first ever" multi-model coding-agent security audit — which ran in rounds specifically to find "similar issues" to what had already been found and produced the 1.0a39/0.65.4 releases on September 10–11 — and was instead found and disclosed by an external reporter five days later, on September 16
- **Evidence**: Cross-referenced dates and claims between this advisory and `blog-simonwillison-datasette-1-0a39.md`: that note's Claim 3 states the September 10–11 release was "the first time we've run a thorough coding agent security audit," and its Claim 4 states the audit deliberately ran "several rounds... looking for similar issues to those that were already found." The advisory here (Sept 16) states the bug reproduces on 1.0a39 itself — the *output* of that audit — meaning the audit's own release still contained this bug.
- **Confidence**: settled on the dates and version-affected range (both are first-party, independently verifiable facts: 1.0a39 shipped Sept 10, per `blog-simonwillison-datasette-1-0a39.md` frontmatter's cited changelog; the GHSA-h547-rmjf-5m2m advisory's own "Confirmed affected revisions" table lists 1.0a39 as vulnerable with the exact commit hash tested); interpretive claim (why the audit missed it) is our own assessment, not stated by either source
- **Quote**: "Affected versions: <= 0.65.4, >= 1.0a0, <= 1.0a39" / "Patched versions: 0.65.5, 1.0a40"
  *(Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, advisory header)*
- **Our assessment**: This is the single most important claim in this note for the guide. The September 10–11 audit's changelog (per `blog-simonwillison-datasette-1-0a39.md` Claim 8) included "Fixed SQL identifier escaping for column names from untrusted database schemas" — i.e., the audit *did* work on identifier-escaping correctness, and even touched `escape_sqlite`-adjacent code paths — but it fixed callers that passed untrusted *column names* into escaping, not a latent flaw in the shared escaping *function itself* that every caller (column names, table names, view names) implicitly relies on. A systematic, multi-model, "look for similar issues" audit still had this class-level blind spot: it can miss a bug in a shared, load-bearing utility function if the audit's search pattern is organized around "which callers pass untrusted data" rather than "which shared validation primitives have off-by-one-character anchoring bugs." For teams running AI-assisted security audits: auditing *call sites* of a trusted utility is not equivalent to auditing the utility's own correctness, and a five-day gap between "we ran an extensive audit" and "an external reporter found a new bug in the exact code the audit had just touched" is a concrete, dated illustration of that gap — not a criticism of the audit's value, but a bound on what "we ran a security audit" should be taken to guarantee.

## Concrete Artifacts

### Release beat (verbatim, from simonwillison.net/2026/Sep/16/datasette-2/)

```
Release: datasette 0.65.5
16th September 2026

Security fix for an issue where a trailing newline in a requested table
name could bypass table permissions and expose private rows, reported by
dpfkdlemtp in GHSA-h547-rmjf-5m2m.

Posted 16th September 2026 at 11:51 pm
Tags: security, datasette
```
*Source: simonwillison.net/2026/Sep/16/datasette-2/, fetched 2026-09-23 via direct HTML retrieval.*

### Companion 1.0a40 release beat (verbatim, from simonwillison.net/2026/Sep/16/datasette/)

```
Release: datasette 1.0a40
16th September 2026

Same security fix as 0.65.5, plus some neat new features and bug fixes:

Plugins can now launch and manage background tasks using the new
datasette.add_background_task() method. Thanks, Alex Garcia.

I've migrated Datasette to httpx2 for features like the internal
datasette.client.get() method.

A whole lot of bug fixes, many of them stemming from a recent effort to
triage issues for a 1.0 stable release.

Posted 16th September 2026 at 11:51 pm
```
*Source: simonwillison.net/2026/Sep/16/datasette/, fetched 2026-09-23.*

### 0.65.5 changelog entry (verbatim, docs.datasette.io/en/stable/changelog.html#v0-65-5)

```
0.65.5 (2026-09-16)

Fixed a security issue where a trailing newline in a requested table name
could bypass table permissions and expose private rows. Thanks for the
report, dpfkdlemtp. GHSA-h547-rmjf-5m2m
```
*Source: docs.datasette.io/en/stable/changelog.html, fetched 2026-09-23.*

### Vulnerable and fixed code (verbatim, from the advisory's "Root cause" and "Causal fix" sections)

```
# Vulnerable:
_boring_keyword_re = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")

def escape_sqlite(s):
    if _boring_keyword_re.match(s) and (s.lower() not in reserved_words):
        return s
    return '"{}"'.format(s.replace('"', '""'))

# Fix (one line):
-   if _boring_keyword_re.match(s) and (s.lower() not in reserved_words):
+   if _boring_keyword_re.fullmatch(s) and (s.lower() not in reserved_words):
```
*Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, fetched 2026-09-23 via direct HTML retrieval.*

### Advisory metadata (verbatim fields, GHSA-h547-rmjf-5m2m)

```
Title: Table permission bypass using trailing newlines in table names
Severity: High (7.5) — CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
CVE ID: No known CVE
Weakness: CWE-625 (Permissive Regular Expression)
Package: pip / datasette
Affected versions: <= 0.65.4, >= 1.0a0, <= 1.0a39
Patched versions: 0.65.5, 1.0a40
Reporter (credited): dpfkdlemtp
Published by: simonw, Sep 17, 2026
```
*Source: github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m, fetched 2026-09-23.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-1-0a39.md` Claim 7 (permission checks
    failing on secondary/derived code paths — case-insensitive names, FTS
    indexes, `?_through=` filters, row primary-key resolution — rather than
    the primary check being absent): this advisory is another concrete
    instance of the same failure shape, this time at the identifier-escaping
    layer rather than at an endpoint-permission layer. Both notes converge on
    the same guide-level lesson: a permission model is only as strong as
    every code path (including shared utility functions) that resolves the
    protected resource's identity.
  - `blog-simonwillison-datasette-1-0a38.md` Claim 2 (a permission check
    existing and being actively enforced while an underlying enforcement
    path still has an escape hatch): this advisory is a second, mechanically
    distinct example of exactly that pattern in the same project, six weeks
    later.

- **Contradicts**: None filed. There is a notable tension worth flagging
  rather than a contradiction: `blog-simonwillison-datasette-1-0a39.md`
  Claim 13 states the maintainers "plan to continue auditing Datasette with
  these tools to help us stay ahead of further vulnerabilities," and this
  advisory shows a new vulnerability class surfacing five days after that
  audit's release, found externally rather than by the audit itself. This
  does not contradict any claim about what the audit *found* or *fixed* —
  it is a data point about the audit's *coverage boundary*, which the 1.0a39
  note's own Extraction Notes already flagged as unverified ("no independent
  verification of audit coverage... no comparison to a non-AI-assisted audit
  baseline"). Per MINER.md §4a, an audit's stated scope not extending to a
  bug class the audit didn't target is a conditioning-variable gap, not two
  sources disagreeing about what happened or what practitioners should do.

- **Extends**:
  - `blog-simonwillison-datasette-1-0a39.md` Claims 3, 4, and 8 (the audit's
    "first ever" status, its "search for similar issues in rounds"
    methodology, and its column-name-escaping fixes): Claim 9 of this note
    directly extends those by showing a concrete boundary of that
    methodology — the audit fixed escaping for untrusted callers of
    `escape_sqlite()` but did not catch a defect in the shared function
    itself, five days before an external reporter did.
  - `blog-simonwillison-datasette-1-0a38.md` Claim 1 (the prior SQL-injection
    permission bypass via `]`-breaking identifier quoting): Claim 8 of this
    note extends that with the reporter's own explicit technical comparison,
    establishing these are two distinct root causes in related code, not a
    regression of the same bug.

- **Novel**:
  - **First corpus documentation of a third-party, externally reported
    vulnerability disclosure with a full CVSS/CWE-level technical writeup**,
    as distinct from the maintainer's own first-party release-note framing
    that `blog-simonwillison-datasette-1-0a38.md` and
    `blog-simonwillison-datasette-1-0a39.md` were built from. This source
    lets us see the *reporter's* reasoning (severity scoring debate,
    duplicate-search methodology, explicit "demonstrated vs. inferred"
    impact boundaries) rather than only the maintainer's summary of it.
  - **First corpus example of a documented gap between an AI-assisted
    security audit's stated methodology and its actual coverage**, dated and
    quantified (a five-day gap, with the exact affected-version range
    including the audit's own just-shipped release).
  - **First corpus instance of the "this is not SQL injection, here is why"
    taxonomic argument** — a reusable distinction for practitioners
    classifying similar identifier-confusion bugs.

## Guide Impact

- **Chapter 05 (Data access & isolation) / Chapter 06 (Production safety &
  security)**: Cite Claims 1–5 as a concrete, dated case study of an
  input-normalization edge case (trailing whitespace/newline in an
  identifier) defeating a permission model that assumed exact string
  matching between the authorization check and the execution layer.
  Recommend: any permission system that authorizes access by resource *name*
  must ensure the exact same normalization/escaping is applied consistently
  between the authorization check and the query-execution layer — and that
  the two layers cannot be tricked into resolving the "same" name
  differently (here, one leading whitespace/newline byte was enough).
- **Chapter 03 (Verification)**: Cite Claim 9 as a specific, load-bearing
  caveat to pair with `blog-simonwillison-datasette-1-0a39.md`'s Chapter 03
  recommendation (multi-model audit + two-human review as a verification
  pattern): that pattern is valuable but not a coverage guarantee — this
  advisory shows a bug surviving exactly that process, in the exact release
  the process produced, found five days later by an unrelated external
  report. The guide should frame "we ran an AI-assisted security audit" as
  raising the floor, not proving the ceiling.
- **Chapter 04 (Common Pitfalls)**: Cite Claim 2 as a specific, named Python
  footgun (`$`-anchored regex `.match()` vs. `.fullmatch()`/`\A...\Z`) worth
  calling out anywhere the guide discusses input-validation code review,
  independent of the AI/agent framing — this is a general secure-coding
  pitfall that happens to have been surfaced via a vulnerability report
  whose methodology resembles the AI-assisted reporting pattern discussed
  in the Extraction Notes below.

## Extraction Notes

- **The entry-point beat is extremely thin (one sentence) but links directly
  to a very deep, formally structured GitHub Security Advisory** — the
  opposite information shape from `blog-simonwillison-datasette-1-0a39.md`
  (a two-sentence beat linking to a ~350-word maintainer blog post) and
  closer in spirit to `blog-simonwillison-datasette-1-0a38.md` (thin beat,
  but there the linked content was also thin). Here the linked advisory is
  the single richest technical artifact encountered across the four
  Datasette security-related notes in this corpus to date, per MINER.md §1's
  instruction to follow substantive linked pages.
- **The Prospector's three triage comments on this issue disagree
  substantially** about source type (`failure-report` in one comment,
  `blog-post`/"release announcement" in the other two) and about relevant
  chapters. Both `triaged:text` and `triaged:failure` labels were applied to
  the issue. Per the task instructions these comments were treated as
  advisory, not authoritative; this note follows the precedent set in
  `blog-simonwillison-datasette-1-0a38.md` and `-1-0a39.md` (which used
  `source_type: blog-post` for maintainer security-release disclosures) for
  consistency, while incorporating the failure-report-style analytical
  structure (root cause, exploit reproduction, fix, "our take" on audit
  coverage) into the claims themselves, since the underlying content is
  genuinely a vulnerability/failure disclosure regardless of which template
  field is used.
- **The advisory's technical depth (deterministic property-testing harness,
  hash-verified independent rerun, explicit CVSS self-scoring debate,
  timestamped duplicate-search sweep) is itself notable as a report style.**
  This level of formal rigor in a third-party vulnerability report —
  including phrases carefully bounding claims ("I did not execute them and
  treat that statement only as an inference", "A private, embargoed,
  deleted, or unindexed report cannot be excluded through public search")
  — reads as consistent with the "AI-assisted vulnerability report" pattern
  `blog-simonwillison-datasette-1-0a39.md` Claim 2 already documents for a
  different reporter (Sevban Dönmez) on the same project five weeks earlier.
  Neither this advisory nor Willison's beat states that `dpfkdlemtp`'s report
  was AI-assisted; this is our own pattern-matching observation on writing
  style and methodology, not a sourced claim, and is flagged here only as a
  hypothesis for future corpus cross-referencing, not asserted as fact in
  any claim above.
- **No CVE identifier exists for this vulnerability** ("No known CVE" is
  stated directly on the advisory page) — tracking should use the GHSA
  identifier (GHSA-h547-rmjf-5m2m) rather than expecting a CVE to appear
  later, since the advisory gives no indication one is pending.
- **No contradiction issue filed.** See Cross-References → Contradicts above
  for the reasoning: the gap between the audit's stated goal and this bug's
  survival is a coverage-boundary observation, not two sources making
  opposing claims about the same fact.
- **Cross-references verified**: `blog-simonwillison-datasette-1-0a39.md`
  Claims 3, 4, 7, 8, and 13, and `blog-simonwillison-datasette-1-0a38.md`
  Claims 1 and 2, were each confirmed by re-reading the cited note in full
  and matching claim numbers to their `### Claim N:` headings in document
  order before citing them here. The 1.0a39 changelog's "Fixed SQL identifier
  escaping for column names from untrusted database schemas" bullet (cited
  in Claim 9's assessment) was re-confirmed against that note's own
  Concrete Artifacts section rather than re-fetched from docs.datasette.io,
  since that note already verified it via direct HTML retrieval.
- **Confidence rationale**: `confidence_overall` is set to `settled`. Every
  extracted claim traces to either (a) a first-party changelog/beat
  statement from the maintainer, or (b) the published, maintainer-credited
  security advisory containing exact code diffs, reproduced HTTP traces, and
  test-suite results that are independently checkable claims about what the
  vulnerable and patched code do. The one clearly `anecdotal`-grade
  component (Claim 9's "why did the audit miss this" interpretation, and the
  Extraction Notes' AI-assisted-reporting-style hypothesis) is explicitly
  marked as our own assessment rather than blended into the overall rating.
