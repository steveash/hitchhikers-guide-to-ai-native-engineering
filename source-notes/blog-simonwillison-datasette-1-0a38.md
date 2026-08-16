---
source_url: https://simonwillison.net/2026/Aug/6/datasette/
source_type: blog-post
title: "datasette 1.0a38"
author: Simon Willison
date_published: 2026-08-06
date_extracted: 2026-08-16
last_checked: 2026-08-16
status: current
confidence_overall: settled
issue: "#2732"
---

# datasette 1.0a38

> A short security-release "beat" in which Willison discloses and fixes a SQL
> injection vulnerability that let users with access to a public table bypass
> Datasette's `execute-sql` permission check and read private tables sharing
> the same database — the first corpus documentation of a permission-check
> bypass in a tool the corpus had previously cited as a model for
> permission-gated agent tooling.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release
  announcement format at simonwillison.net, August 6, 2026. The post is three
  short paragraphs with no code samples, screenshots, or demo, tagged
  `security`, `sql-injection`, `datasette`. It links to Datasette's
  authentication/permissions documentation and to a companion release beat for
  Datasette 0.65.3, both of which were also read for this note.)
- **Author credibility**: Simon Willison is the creator of Datasette and the
  primary developer of the Datasette Agent ecosystem documented elsewhere in
  this corpus. This is first-party disclosure of a vulnerability in his own
  tool, with a stated fix and a stated mitigation. No vendor affiliation.
- **Scope**: Covers a single security fix in Datasette 1.0a38 (and its
  backport to 0.65.3): a SQL injection bug that bypassed the `execute-sql`
  permission check for databases mixing public and private tables. Does NOT
  cover: the technical mechanism of the injection itself (no proof-of-concept,
  payload, or affected code path is shown), a CVE identifier, whether any
  instances were exploited in the wild, or how the fix was implemented.

## Extracted Claims

### Claim 1: Datasette 1.0a38 fixes a SQL injection vulnerability specific to instances that serve a mixture of public and private tables in the same database, with access controlled via Datasette's permissions system

- **Evidence**: First-party security release announcement from the tool's
  creator, published as a dedicated "beat" tagged `security` and
  `sql-injection`.
- **Confidence**: settled (first-party vulnerability disclosure with a stated
  fix, from the tool's author)
- **Quote**: "This release fixes a SQL injection security issue that affects
  Datasette instances that serve a mixture of public and private tables in the
  same database, with access configured using the Datasette permissions
  system."
  *(Source: simonwillison.net/2026/Aug/6/datasette/)*
- **Our assessment**: The vulnerability is scoped narrowly to a specific
  deployment topology — public and private tables coexisting in one database,
  with visibility enforced through Datasette's permissions system rather than
  through separate databases or instances. This scoping matters for
  practitioners: the bug is not "Datasette has a general SQL injection
  problem," it is "mixed-visibility tables within a single database are a
  distinct attack surface."

### Claim 2: The bug allowed a user with legitimate access to any public table to run SQL injection attacks that granted read-only access to private tables in the same database, circumventing the permission restriction that was supposed to block that access

- **Evidence**: First-party description of the vulnerability's impact and
  attack precondition (public-table access as the entry point) in the release
  post.
- **Confidence**: settled (first-party disclosure of the vulnerability's
  effect, stated directly by the tool's author)
- **Quote**: "The bug that has been fixed would have allowed users with access
  to any public table to execute SQL injection attacks despite that
  restriction, giving them read-only access to data in private tables in the
  same database."
  *(Source: simonwillison.net/2026/Aug/6/datasette/)*
- **Our assessment**: This is the concrete failure mode: a permission
  restriction existed (the private table was supposed to be off-limits) and
  was bypassed via SQL injection reachable through a table the attacker was
  legitimately allowed to query. The privilege gained was read-only, which
  bounds the impact relative to a write-capable bypass, but any unauthorized
  cross-tenant read of private data is a serious breach in a multi-tenant or
  access-controlled deployment. This is a textbook example of a permission
  *check* existing while the underlying enforcement path (raw SQL execution)
  still had an escape hatch.

### Claim 3: As a workaround, site administrators serving private tables in this mixed configuration are advised to disable the `execute-sql` permission on the affected database to prevent access to private tables via raw SQL queries

- **Evidence**: Direct mitigation guidance from the tool's creator in the
  release post, naming the specific permission to disable.
- **Confidence**: settled (first-party mitigation guidance from the author)
- **Quote**: "Site administrators who serve private tables in this way are
  advised to disable the execute-sql permission"
  *(Source: simonwillison.net/2026/Aug/6/datasette/; quote truncated at a
  rendering artifact in the source page — see Extraction Notes)*
- **Our assessment**: The recommended mitigation is coarse: disable raw SQL
  execution entirely for the affected database rather than a more surgical
  fix (e.g., scoping SQL execution to only public tables). This tracks with
  `blog-simonwillison-datasette-agent-charts.md` Claim 3, which documents
  `execute-sql` as the permission Datasette's own agent tooling checks before
  running any SQL — the two sources together establish `execute-sql` as the
  single load-bearing gate for raw-SQL access in Datasette, and this source
  shows that gate can itself be circumvented by injection rather than only by
  a missing permission check.

### Claim 4: The SQL injection fix is also available in Datasette 0.65.3, a back-port to the pre-1.0 stable release line

- **Evidence**: A direct statement in the 1.0a38 post plus a separate,
  independently-published companion release beat for 0.65.3.
- **Confidence**: settled (first-party release notes for both the 1.0a38 and
  0.65.3 releases, cross-confirming the same fix)
- **Quote**: "This fix is also available in Datasette 0.65.3."
  *(Source: simonwillison.net/2026/Aug/6/datasette/)*

  Companion post: "Back-ported the SQL Injection security fix from 1.0a38."
  *(Source: simonwillison.net/2026/Aug/6/datasette-2/, posted 6th August 2026
  at 6:22pm, two minutes before the 1.0a38 post)*
- **Our assessment**: Datasette maintains two active release lines
  concurrently — the 1.0 alpha series (where new features land, per
  `blog-simonwillison-datasette-1-0a33.md` and `blog-simonwillison-datasette-1-0a34.md`)
  and a 0.65.x line for users not yet on the 1.0 alphas. A security fix landing
  in both, on the same day, indicates the maintainer treats security patches
  as required for both lines regardless of alpha/stable status — unlike
  features, which only ship to 1.0a. Practitioners running Datasette in
  production on 0.65.x (rather than tracking the 1.0 alphas) still needed to
  upgrade to receive this fix; watching only the 1.0a changelog would have
  missed it.

### Claim 5: Willison assesses the vulnerable configuration — private and public tables exposed from the same database within the same instance — as likely rare, and states he has not personally encountered an instance configured that way

- **Evidence**: The author's own qualitative assessment of the deployment
  pattern's prevalence, offered without supporting data (e.g., a scan of
  known Datasette deployments).
- **Confidence**: anecdotal (single practitioner's impression, not measured)
- **Quote**: "Thankfully this particular configuration - private tables and
  public tables exposed for the same database within the same instance - is
  likely to be rare. I've not encountered an instance like that myself."
  *(Source: simonwillison.net/2026/Aug/6/datasette/)*
- **Our assessment**: This caveat is doing real work: it is the author telling
  readers not to panic, based on his own experience rather than measurement.
  For a guide audience, the caveat is worth relaying but not worth trusting
  as a ceiling on real-world exposure — "I haven't seen it" is weak evidence
  for a hosted, self-serve tool where the maintainer cannot see most
  deployments. The mixed-table topology is also exactly the kind of
  configuration an agent-facing deployment might create incidentally (e.g., a
  team database with some tables meant for public dashboards and others
  meant for internal-only agent queries), so "rare today" does not mean "rare
  as agentic use of Datasette grows."

### Claim 6: Per Datasette's authentication documentation (linked from the release post), the `execute-sql` permission controls whether an actor can run arbitrary read-only SQL queries against a database, and Datasette defaults to allowing any site visitor to run such queries unless this is explicitly restricted

- **Evidence**: Datasette's own permissions documentation, linked directly
  from the 1.0a38 post as the definition of the permission administrators are
  told to disable.
- **Confidence**: settled (first-party documentation of the permission's
  default behavior and scope)
- **Quote**: (no direct quote from the linked docs page reproduced verbatim
  here; see Extraction Notes — this claim is a paraphrase of the docs page's
  description of `execute-sql`, not a quote from the simonwillison.net post
  itself)
- **Our assessment**: This background is necessary to understand why the
  vulnerability was possible at all: `execute-sql` is not a narrow,
  off-by-default permission — Datasette's default posture is to *allow* any
  visitor to run custom SQL unless an administrator opts out (`allow_sql:
  false` or scoping it to specific users). A deployment that wants some
  tables private therefore depends on either disabling `execute-sql` entirely
  or on table-level permission checks holding up against arbitrary SQL —
  and this release shows the latter path had a gap. For practitioners: any
  tool that exposes a "run SQL against this data" capability to an agent or
  end user, with some data meant to stay private, needs to treat raw-SQL
  access as a permission boundary in its own right, not assume table-level
  ACLs compose safely with free-form SQL.

## Concrete Artifacts

### Release Post Text (verbatim, from simonwillison.net/2026/Aug/6/datasette/)

```
Release: datasette 1.0a38
6th August 2026

This release fixes a SQL injection security issue that affects Datasette
instances that serve a mixture of public and private tables in the same
database, with access configured using the Datasette permissions system.

Site administrators who serve private tables in this way are advised to
disable the execute-sql permission on that database to prevent users from
accessing private tables using raw SQL queries. The bug that has been fixed
would have allowed users with access to any public table to execute SQL
injection attacks despite that restriction, giving them read-only access to
data in private tables in the same database.

This fix is also available in Datasette 0.65.3.

Thankfully this particular configuration - private tables and public tables
exposed for the same database within the same instance - is likely to be
rare. I've not encountered an instance like that myself.

Posted 6th August 2026 at 6:24 pm
Tags: security, sql-injection, datasette
```

*Source: simonwillison.net/2026/Aug/6/datasette/, fetched 2026-08-16 via
direct HTML retrieval (not WebFetch summarization).*

### Companion Release Beat (verbatim, from simonwillison.net/2026/Aug/6/datasette-2/)

```
Release: datasette 0.65.3
6th August 2026

Back-ported the SQL Injection security fix from 1.0a38.

Posted 6th August 2026 at 6:22 pm
Tags: datasette
```

*Source: simonwillison.net/2026/Aug/6/datasette-2/, fetched 2026-08-16.*

## Cross-References

- **Corroborates**: None identified — no existing corpus note documents a
  Datasette or Datasette Agent security vulnerability, so there is no prior
  claim for this source to directly corroborate.

- **Contradicts**: None. `blog-simonwillison-datasette-agent-charts.md`
  Claim 3 recommends checking the `execute-sql` permission as "a concrete
  example of the 'check permissions before any query, including discovery
  queries' principle" — this source does not dispute that recommendation
  (the permission check is still the correct control, and disabling
  `execute-sql` is still the stated mitigation). Instead it shows the
  underlying enforcement of that same permission had a bypassable gap in one
  specific topology. This is a qualification of the earlier claim's
  reliability, not an opposing claim about what practitioners should do, so
  no contradiction issue was filed per MINER.md §4a ("claims differ only in
  context" / conditioning variable, not a material disagreement about guide
  advice).

- **Extends**:
  - `blog-simonwillison-datasette-agent-charts.md` Claim 3: That claim
    establishes `execute-sql` as the permission Datasette's own agent
    tooling checks before running preparatory SQL queries, framed as a
    positive example of permission-aware plugin design. This source extends
    that claim with a security caveat: the `execute-sql` gate itself could be
    bypassed via SQL injection in databases mixing public and private
    tables. Together the two notes show both the design intent (check
    `execute-sql` before any SQL) and a concrete case where the mechanism
    enforcing that check had a bug.
  - `blog-simonwillison-datasette-agent-write-sql.md` Claims 1–2: That note
    documents `execute_write_sql`'s approval dialog, which displays required
    Datasette permissions (`insert-row`, `update-row`, `delete-row`) alongside
    proposed SQL so a human can authorize writes. This source is the
    read-side counterpart risk: even without any write capability, raw
    read-only SQL execution against a permission-restricted database can leak
    private data if the permission boundary has a bypass. The two notes
    together suggest that both the write-approval UI and the read-permission
    check are guarding the same underlying capability — arbitrary SQL
    execution — and both depend on that capability being correctly bounded.
  - `blog-simonwillison-datasette-1-0a33.md` and
    `blog-simonwillison-datasette-1-0a34.md` overall: Those notes document the
    two most recent prior 1.0-alpha releases in this corpus (June 11 and June
    16, 2026 respectively), both purely feature-driven (composable JSON API
    extras, CRUD UI). This source, roughly seven weeks later, is the first
    corpus-documented release in the 1.0 alpha series that is a security fix
    rather than a feature addition — extending the corpus's picture of the
    1.0 alpha cadence from "adding capability" to "hardening existing
    capability."

- **Novel**:
  - **First corpus documentation of a security vulnerability in Datasette or
    the Datasette Agent ecosystem.** Every other Datasette-related note in
    this corpus (agent platform launch, charts plugin, write-SQL approval
    flow, JSON API extras, CRUD UI) documents a feature or capability. This
    is the first to document a bug with security impact — specifically a
    permission-check bypass reachable through SQL injection.
  - **First corpus example of a permission check being reachable-but-bypassed
    via injection, as distinct from a missing permission check.** The prior
    corpus pattern (`blog-simonwillison-datasette-agent-charts.md` Claim 3)
    documents *adding* a permission check that was previously absent. This
    source documents a case where the check existed and was still
    circumventable — a materially different and arguably more instructive
    failure mode for practitioners relying on permission checks as their
    security boundary.

## Guide Impact

- **Chapter 06 (Security and Threat Model — "Bounding Your Own Agents: Least
  Agency and the Toolchain Attack Surface")**: Add this source as a concrete,
  dated example of a permission check that existed but was bypassable — not
  a missing-permission-check failure, but an injection-based circumvention of
  a present one. The specific lesson for practitioners granting an agent (or
  end user) a "run SQL against this database" capability: if the database
  contains any private tables, do not treat a permission-system check on that
  capability as a sufficient boundary by itself; either isolate private data
  into a separate database/instance, or disable raw SQL execution
  (`execute-sql`/`allow_sql: false`) for any database with mixed visibility.
  Cite Claims 1–3 for the vulnerability and mitigation, and Claim 6 for why
  Datasette's default posture (SQL execution allowed by default) makes this a
  real-world risk rather than a hypothetical misconfiguration.

- **Chapter 06 (Security and Threat Model — "The Sandbox Is the Control —
  Even When Someone Else Runs It")**: Use this source as a specific
  illustration of the chapter's broader "verify the control, don't just trust
  that it exists" theme, applied to permission systems rather than sandboxes:
  a permission check being present and even actively enforced in normal
  usage does not guarantee it holds up against adversarial input (SQL
  injection) on the same code path. Cite Claim 2.

- **Chapter 02 (Harness Engineering) — data-tool/agent permission design**:
  When citing `blog-simonwillison-datasette-agent-charts.md` Claim 3 as a
  positive example of permission-aware plugin design (per that note's own
  Guide Impact section), pair it with this source's Claim 3 caveat: checking
  a permission before running SQL is necessary but the corpus now has a
  documented case where it was not sufficient. Recommend the guide note both
  sources together wherever it cites Datasette Agent's `execute-sql` check as
  a security pattern to emulate.

## Extraction Notes

- **Fetched via direct HTML retrieval, not WebFetch summarization.** An
  initial WebFetch pass returned a fluent but paraphrased summary (e.g.
  rendering the mitigation as "disable the execute-sql permission... as
  workaround" rather than the source's exact sentence). To satisfy MINER.md
  §2a's verbatim-quote requirement, the post and its companion 0.65.3 beat
  were re-fetched with `curl` and the raw HTML was stripped and compared
  character-for-character against every quote in this note.
- **Rendering artifact in the source page, affecting Claim 3's quote.** The
  live HTML for the mitigation sentence contains a literal, unexplained
  fragment — `<actions_execute_sql>` followed by a backtick — inserted
  between the `execute-sql permission` link and the words "on that database."
  This reads as an unrendered template artifact on Simon Willison's own site,
  not an OCR or WebFetch error (confirmed by inspecting the raw HTML
  directly). Per MINER.md §2a.3, the Claim 3 quote was truncated at the
  contiguous fragment before the artifact rather than spliced across it; the
  remainder of the sentence ("on that database to prevent users from
  accessing private tables using raw SQL queries") is accurately paraphrased
  in Claim 3's "Our assessment" text rather than re-quoted. The Assayer
  should independently verify this artifact is present in the live page
  rather than an extraction error on our part.
- **Claim 6 is sourced from a linked docs page, not the beat itself.** Per
  MINER.md §1 ("follow up to 5 linked pages that seem substantive"), the
  `execute-sql` permission documentation
  (docs.datasette.io/en/latest/authentication.html#execute-sql) linked from
  the post was read to establish what the permission actually governs and
  its default state. That page was fetched via WebFetch (summarized, not
  verbatim), so no direct quote from it is presented as a source quote —
  Claim 6 is explicitly flagged as a paraphrase per MINER.md §2a.5.
  Practitioners or the Assayer wanting the exact docs wording should consult
  that URL directly.
- **No CVE identifier, PoC, or affected-version-range detail in the source.**
  The post does not name a CVE, does not show the injection payload or
  vulnerable code path, and does not state which prior 1.0-alpha versions
  (back to when) were affected — only that the fix is in 1.0a38 and
  backported to 0.65.3. This note does not speculate beyond what the post
  states.
- **Thin source, consistent with prior "beat" format notes in this corpus.**
  At three short paragraphs (~120 words), this is comparable in length to
  `blog-simonwillison-datasette-1-0a34.md` (also assessed as "thin" with four
  claims). Six claims were extracted here, one more than that note, because
  this post additionally required a linked-docs claim (Claim 6) to make the
  vulnerability's mechanism intelligible, and the security framing supported
  separating the vulnerability description (Claim 1), its impact (Claim 2),
  and its mitigation (Claim 3) into distinct claims rather than merging them.
- **Cross-references verified**: `blog-simonwillison-datasette-agent-charts.md`
  Claim 3 confirmed at lines 75–91 of that note ("The plugin gates
  visualization on the `execute-sql` Datasette permission before running
  column-discovery queries" / quote: "Now checks `execute-sql` permission
  before running the query to find the column names."). `blog-simonwillison-datasette-agent-write-sql.md`
  Claims 1–2 confirmed at lines 42–77 of that note (`execute_write_sql`
  approval dialog and its permissions table). `blog-simonwillison-datasette-1-0a33.md`
  and `blog-simonwillison-datasette-1-0a34.md` confirmed as overall-note
  citations (release dates June 11 and June 16, 2026 respectively, per their
  own frontmatter `date_published` fields), not tied to specific claim
  numbers.
- **No contradiction issue filed.** See Cross-References → Contradicts above
  for the reasoning: this source qualifies rather than opposes the existing
  `execute-sql` permission-check recommendation.
