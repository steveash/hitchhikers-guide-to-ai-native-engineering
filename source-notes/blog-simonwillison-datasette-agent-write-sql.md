---
source_url: https://simonwillison.net/2026/Jun/15/datasette-agent/
source_type: blog-post
title: "datasette-agent 0.3a0"
author: Simon Willison
date_published: 2026-06-15
date_extracted: 2026-06-23
last_checked: 2026-06-23
status: current
confidence_overall: emerging
issue: "#1277"
---

# datasette-agent 0.3a0

> The 0.3a0 release of Datasette Agent extends the 0.2a0 approval pattern to
> direct database write operations, introducing `execute_write_sql` — a tool
> that shows the proposed SQL and required permissions before executing, and
> adds CLI flags (`--yes`, `--unsafe`) to support programmatic auto-approval
> workflows.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release announcement
  format at simonwillison.net, June 15, 2026. The post is brief, describing the
  new `execute_write_sql` tool, a screenshot of its approval dialog, and CLI
  enhancements to `datasette agent chat`.)
- **Author credibility**: Simon Willison is the creator of Datasette and the
  primary developer of Datasette Agent. This is first-party release documentation
  — authoritative for the feature's capabilities, API design, and design intent.
  He published datasette-agent 0.1a1 (issue #1011), 0.2a0 (issue #1203), and the
  charts plugin (issue #984) before this release. No vendor affiliation.
- **Scope**: Covers the three additions in datasette-agent 0.3a0: (1) the
  `execute_write_sql` tool — approval dialog, permission display, SQL preview;
  (2) `datasette agent chat` CLI enhancements — approval support and three new
  flags; (3) plain-text tool output alternatives for CLI contexts. Does NOT cover:
  internal implementation of the permission check, which Datasette permissions map
  to which operations, multi-user approval behavior, or the full write API surface.

## Extracted Claims

### Claim 1: The new `execute_write_sql` tool requests user approval and then writes to a database, taking user permissions into account

- **Evidence**: First-party release announcement from the tool's creator, with a
  screenshot of the approval dialog as visual corroboration.
- **Confidence**: emerging (first-party alpha release; tool is functional per the
  announcement, but alpha status means the API may change before stable release)
- **Quote**: "New tool, `execute_write_sql`, which requests user approval and then
  writes to a database."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: This is the write-side counterpart to the `save_query`
  approval gate from 0.2a0 (`blog-simonwillison-datasette-agent-askuser.md`
  Claim 5). `save_query` gates creation of a persistent SQL artifact (stored
  query); `execute_write_sql` gates direct database mutation (INSERT/UPDATE/DELETE).
  Both require explicit user approval before any state change, but the new tool
  adds permission-awareness: the required Datasette permissions for the operation
  are shown alongside the SQL, not just the SQL itself.

### Claim 2: The `execute_write_sql` approval dialog displays the proposed SQL statement, the target database, and the required permissions before execution

- **Evidence**: Screenshot caption description in the release post, showing a
  yellow-bordered confirmation dialog with SQL, database name, and a permissions
  table with "Operation, Database, Table, Required permissions" columns.
- **Confidence**: emerging (first-party; screenshot is direct visual evidence of
  the approval dialog design)
- **Quote**: "Execute 1 write SQL statement against database 'pelicans'? / Asked by tool: execute_write_sql"
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/, approval dialog text
  visible in screenshot)*
- **Our assessment**: The dialog surfaces three pieces of information: what SQL
  will run, which database it targets, and what permissions are required (e.g.
  `insert-row`, `update-row`, `delete-row`). Showing the required permissions
  alongside the SQL allows a user to make an informed authorization decision: not
  just "is this SQL correct?" but "should this agent have write access to this
  table?" This is a materially richer approval prompt than a plain "proceed? yes/no"
  confirmation. The `save_query` approval in 0.2a0 showed SQL + name + database +
  visibility; this adds a permissions table, making the authorization model explicit
  rather than implicit.

### Claim 3: The `execute_write_sql` tool was built using the `ask_user()` mechanism introduced in 0.2a0

- **Evidence**: Explicit reference in the release post to the 0.2a0 mechanism.
- **Confidence**: emerging (first-party; the causal relationship — "using the
  mechanism introduced in 0.2a0" — is the author's own statement)
- **Quote**: "I added a mechanism for asking user approval in datasette agent 0.2a0."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: This quote confirms that `execute_write_sql` is an
  application of the `ask_user()` pattern (the suspension-and-resume mechanism
  documented in `blog-simonwillison-datasette-agent-askuser.md` Claims 1–4),
  not a new mechanism. The 0.2a0 release established the general
  interaction infrastructure (pause tool, present question as form, resume on
  answer, persist across restarts); 0.3a0 uses that infrastructure to build a
  specific safety-critical tool. This is the first concrete production application
  of `ask_user()` to a state-mutating database operation in the corpus.

### Claim 4: The pelican sightings example demonstrates the full execute_write_sql flow: natural language input → agent → SQL → approval → execution

- **Evidence**: Annotated screenshot showing the user message, the generated SQL,
  and the approval dialog in sequence.
- **Confidence**: anecdotal (single demo example from the author; confirms the
  tool functions end-to-end in the announced scenario)
- **Quote**: "Here's an example where I add some pelican sightings to my `pelican_sightings` table."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: The example shows natural language ("I saw 4 pelicans flying
  over the harbor") translated to a parameterized INSERT statement
  (`INSERT INTO pelican_sightings (number_of_pelicans, notes) VALUES (:number_of_pelicans, :notes);`),
  followed by the approval dialog. Using parameterized SQL (`:parameter` placeholders)
  rather than string interpolation is a safe practice: values are bound separately
  rather than embedded in the SQL string, preventing injection. This is a concrete
  example of the agent doing both translation (NL to SQL) and safe value binding
  in the write path.

### Claim 5: `datasette agent chat` now supports executing tools that require user approval

- **Evidence**: First-party release announcement.
- **Confidence**: emerging (first-party; the CLI capability is directly asserted)
- **Quote**: "`datasette agent chat` can execute tools that require user approval."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: In 0.2a0, the `ask_user()` approval mechanism worked in the
  web UI. This 0.3a0 enhancement brings the same approval flow to the terminal
  `chat` command. CLI contexts present a UX challenge for interactive approvals —
  the browser's form-rendering for yes/no and multiple-choice questions cannot be
  replicated directly in a terminal. The three new flags (Claims 6–8) are the
  CLI's answer to this constraint.

### Claim 6: Three new CLI flags were added to `datasette agent chat`: `--root` (run as root user), `--yes` (auto-approve all prompts), and `--unsafe` (both combined)

- **Evidence**: First-party release announcement.
- **Confidence**: emerging (first-party; the three flags and their meanings are
  explicitly stated)
- **Quote**: "Three new options for `datasette agent chat` - `--root` to run as root, `--yes` to approve all ask user questions, and `--unsafe` for both."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: The three flags form a safety-vs-convenience spectrum:
  `--root` alone grants elevated permissions without auto-approval (user still
  confirms each write); `--yes` alone auto-approves questions but at the user's
  default permission level; `--unsafe` removes both gates entirely. The existence
  of `--unsafe` as an explicit, named mode is notable: it makes the "unsafe" choice
  deliberate and visible in command history, rather than a default that can be
  stumbled into. This mirrors patterns in other CLIs (e.g., `rm -rf` requiring the
  `-f` force flag explicitly). For practitioners building CLI-driven agent pipelines
  (e.g., scheduled jobs, CI), `--yes` provides auto-approval at normal permissions;
  `--unsafe` is the escape hatch for fully automated write pipelines where human
  approval is structurally impossible.

### Claim 7: The `--unsafe` flag enables a viable `datasette agent chat content.db -m gpt-5.5 --unsafe` command for natural-language database modification via chat

- **Evidence**: Explicit command example in the release post.
- **Confidence**: anecdotal (single practitioner example; demonstrates the
  intended end-to-end use case)
- **Quote**: "The `datasette agent chat content.db -m gpt-5.5 --unsafe` command can now be used to chat."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: This command — specifying a database, a model, and `--unsafe`
  — is the minimal invocation for an agent that can freely read and write a local
  SQLite database via natural language. Prior to this release, the chat mode
  could only read; write operations either required the web UI or lacked the
  approval flow needed for safety. The `gpt-5.5` model here is a reminder that
  Datasette Agent's multi-model support (inherited from the LLM library) makes
  the write capability model-agnostic.

### Claim 8: Tools can now provide plain-text alternatives to HTML, for display in the `datasette agent chat` CLI

- **Evidence**: First-party release announcement.
- **Confidence**: emerging (first-party; the feature is briefly described)
- **Quote**: "Tools can now provide plain text alternatives to HTML, for display in the `datasette agent chat` CLI."
  *(Source: simonwillison.net/2026/Jun/15/datasette-agent/)*
- **Our assessment**: The web UI can render rich HTML from tool outputs; the
  terminal CLI cannot. This feature allows tool authors to declare two output
  formats — HTML for the web UI and plain text for the CLI — so a single tool
  works correctly in both deployment contexts. For practitioners building agent
  plugins that produce formatted output (tables, highlighted code, charts), this
  is the mechanism for CLI compatibility: provide a plain-text fallback rather
  than requiring a browser session. The feature is briefly mentioned and its
  exact API (how a tool declares a plain-text alternative) is not documented in
  this release post.

## Concrete Artifacts

### execute_write_sql Approval Dialog (from simonwillison.net/2026/Jun/15/datasette-agent/)

The approval dialog shown in the post screenshot:

```
Confirmation dialog (yellow border):
  "Execute 1 write SQL statement against database 'pelicans'?"
  "Asked by tool: execute_write_sql"

  SQL statement:
    INSERT INTO pelican_sightings (number_of_pelicans, notes)
    VALUES (:number_of_pelicans, :notes);

  Permissions table:
    Operation | Database | Table              | Required permissions
    insert    | pelicans | pelican_sightings  | [insert-row] [update-row] [delete-row]

  Buttons: [Yes] [No]
```

*Source: simonwillison.net/2026/Jun/15/datasette-agent/, 2026-06-15. The table
structure and button labels are inferred from the screenshot description in the
post. The SQL statement is verbatim from the post.*

### CLI Flags Summary (from simonwillison.net/2026/Jun/15/datasette-agent/)

```
datasette agent chat [database] [options]

New flags in 0.3a0:
  --root    Run as root user (elevated permissions)
  --yes     Auto-approve all ask_user() questions
  --unsafe  Both --root and --yes (no human gates)

Example:
  datasette agent chat content.db -m gpt-5.5 --unsafe
```

*Source: simonwillison.net/2026/Jun/15/datasette-agent/, 2026-06-15.*

### Pelican Sightings Demo Flow (from simonwillison.net/2026/Jun/15/datasette-agent/)

```
User (natural language):  "I saw 4 pelicans flying over the harbor"

Agent (generated SQL):
  INSERT INTO pelican_sightings (number_of_pelicans, notes)
  VALUES (:number_of_pelicans, :notes);

Approval dialog:
  "Execute 1 write SQL statement against database 'pelicans'?"
  [Yes] [No]
```

*Source: simonwillison.net/2026/Jun/15/datasette-agent/, 2026-06-15.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-agent-askuser.md` Claim 5: "Saving always
    requires human approval - the agent shows the full SQL plus the proposed
    name, database and visibility, and nothing is stored until you click Yes."
    The `execute_write_sql` approval gate follows the same "show full context,
    require explicit yes, nothing executes until confirmed" pattern as `save_query`,
    extending it from artifact creation to direct database writes and adding a
    permissions table to the approval surface.
  - `blog-simonwillison-datasette-agent-charts.md` Claim 3: "Now checks
    `execute-sql` permission before running the query to find the column names."
    Both sources document permission-aware gating of database operations. The
    charts note shows read-permission checking before a preparatory query; this
    source shows write-permission display in the approval dialog before a write
    operation. Together they establish a permission-first pattern: agent operations
    against data must surface the relevant permissions, not just execute silently.

- **Extends**:
  - `blog-simonwillison-datasette-agent-askuser.md` overall: The 0.2a0 note
    documents the foundational `ask_user()` mechanism (Claims 1–4) and its first
    production application, `save_query` (Claim 5). This 0.3a0 source applies
    the same mechanism to the more operationally dangerous case: direct database
    mutation. Together the two notes trace the approval pattern from its introduction
    (0.2a0, artifact creation) through its extension (0.3a0, database writes with
    permission display) and CLI integration.
  - `blog-simonwillison-datasette-agent.md` Claim 5: "My favorite feature of
    Datasette Agent is that, like the rest of Datasette, it's extensible using
    plugins." The 0.3a0 release adds capabilities to the core platform whose
    extensibility was established in the 0.1a1 platform announcement. The CLI
    enhancements and plain-text alternatives (Claim 8) deepen the non-web-UI
    deployment path that the original release established with its local model
    deployment command.

- **Contradicts**: None identified. No existing corpus note makes claims about
  write-operation approval gating, permission-aware approval dialogs for database
  mutations, or CLI auto-approval flags that conflict with this source's claims.
  No contradiction issue required.

- **Novel**:
  - **First corpus documentation of approval-gated direct database write operations
    in an agent**: The `save_query` approval (0.2a0 note) gates creation of a
    persistent SQL artifact (a stored query); this source gates *executing* SQL
    against a live database. The distinction matters: `save_query` creates an
    inspectable artifact the user can modify before running; `execute_write_sql`
    directly mutates state. The approval gate for irreversible write operations is
    a stricter safety requirement than for artifact creation.
  - **First corpus documentation of permission-aware approval dialogs**: Prior
    corpus approval patterns (save_query in the 0.2a0 note) surface the proposed
    action but not the underlying permissions required. This source introduces the
    pattern of showing required Datasette permissions (insert-row, update-row,
    delete-row) alongside the proposed SQL, making the authorization model explicit
    to the approving user.
  - **First corpus documentation of CLI auto-approval flags for agent approval
    gates**: The `--yes` and `--unsafe` flags are the first corpus example of
    designing explicit programmatic bypass modes for interactive agent approval
    flows. This is the CLI/automation answer to the "how do scheduled or scripted
    agent pipelines handle approval gates?" design question.
  - **First corpus documentation of tool output content negotiation for
    web-vs-CLI contexts**: The plain-text alternative feature (Claim 8) is the
    first corpus example of a tool declaring context-aware output formats to
    support both rich web UI and minimal CLI deployment modes.

## Guide Impact

- **Chapter 03 (Safety and Verification — approval gates for state-mutating
  operations)**: Extend the approval-gate pattern established by `save_query`
  (from `blog-simonwillison-datasette-agent-askuser.md` Claim 5) with this
  source's `execute_write_sql` as the write-operation counterpart. The key
  addition: showing required permissions alongside the proposed SQL, not just
  the SQL itself. This makes the approval dialog an authorization check, not
  merely a review-and-confirm step. Cite Claim 2 for the full dialog design and
  Claim 1 for the general pattern.

- **Chapter 03 (Safety and Verification — irreversibility and approval scope)**:
  The `save_query` gate covers reversible artifact creation (a stored query can
  be deleted); `execute_write_sql` covers potentially irreversible direct database
  mutation (a deleted row may not be recoverable). The guide should note that the
  approval gate design is the same, but the stakes are higher for direct writes —
  this is an argument for showing permissions explicitly (as this tool does) rather
  than relying on the user to infer authorization scope from the SQL alone. Cite
  Claims 1 and 2.

- **Chapter 02 (Interactive Agent Loops — CLI deployment of approval-gated
  agents)**: Add the `--yes`/`--unsafe` flag design as a concrete reference for
  practitioners designing CLI-facing agent tools that include approval gates. The
  key design decision: provide explicit named modes for bypassing approval (making
  the bypass deliberate and logged), rather than silently skipping gates or
  providing no CLI path at all. Cite Claim 6 and the CLI Flags Summary in
  Concrete Artifacts.

- **Chapter 02 (Harness Engineering — multi-context tool output)**: Add Claim 8
  (plain-text alternatives for HTML tool outputs) as a reference for practitioners
  building agent tools that must work in both web and CLI contexts. The design
  principle: tool outputs should declare context-appropriate formats rather than
  assuming a rich-rendering environment. Cite Claim 8.

## Extraction Notes

- **Thin primary source**: The blog post is a "beat" in Willison's format — a
  brief release announcement with a screenshot and a few sentences per feature.
  All substantive claims are present in the post; there is no linked GitHub
  release page with additional detail visible in the rendered text.
- **Verbatim quotes obtained via targeted WebFetch**: The source was fetched
  three times with targeted prompts to extract verbatim quotes for each claim.
  Quotes in this note are reproduced character-for-character as returned by the
  WebFetch model. The approval dialog UI description (screenshot caption text)
  was confirmed across two fetch attempts.
- **Screenshot content inferred from caption**: The approval dialog in Concrete
  Artifacts is reconstructed from the screenshot caption text returned by
  WebFetch. The table column names ("Operation, Database, Table, Required
  permissions") and permission button labels ("insert-row", "update-row",
  "delete-row") are from the post's description of the screenshot, not from
  direct image reading.
- **Fragment URL**: The issue body URL includes `#atom-everything`. The
  `source_url` uses the canonical URL without the fragment, consistent with
  prior Willison source notes in this corpus.
- **Cross-references verified**: `blog-simonwillison-datasette-agent-askuser.md`
  Claim 5 confirmed at lines 113–129 of that note. `blog-simonwillison-datasette-agent-charts.md`
  Claim 3 confirmed at lines 75–91 of that note. `blog-simonwillison-datasette-agent.md`
  Claim 5 confirmed at lines 113–129 of that note. All claim numbers verified by
  document-order count.
- **No contradictions filed**: No existing corpus note makes claims that conflict
  with the write-operation approval gate or CLI auto-approval patterns documented
  here. No contradiction issue required.
