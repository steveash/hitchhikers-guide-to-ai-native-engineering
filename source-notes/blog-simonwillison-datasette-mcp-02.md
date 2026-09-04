---
source_url: https://simonwillison.net/2026/Sep/1/datasette-mcp/
source_type: blog-post
title: "datasette-mcp 0.2"
author: Simon Willison
date_published: 2026-09-01
date_extracted: 2026-09-04
last_checked: 2026-09-04
status: current
confidence_overall: emerging
issue: "#3220"
---

# datasette-mcp 0.2

> A three-sentence release-announcement "beat" for datasette-mcp 0.2 (first
> non-alpha release) that on its own adds little beyond the row-format change
> already summarized by the Prospector — but the linked GitHub issue and
> release contain a concrete artifact the blog post omits: the `mcp>=2.1.1`
> dependency bump also silently changed how the MCP framework surfaces
> exception messages to clients, breaking the plugin's own error-message
> test assertions.

## Source Context

- **Type**: blog-post — a "beat" (Simon Willison's short-form release-note
  format), three sentences of prose with no analysis or usage narrative.
- **Author credibility**: Simon Willison, creator of Datasette and the `llm`
  CLI, and the author/maintainer of the `datasette-mcp` plugin itself. This is
  first-party release documentation from the person who wrote the code and
  filed/closed the linked GitHub issue that motivated it.
- **Scope**: Covers exactly one plugin release (0.2) — a rows-format change
  (array of objects instead of array of arrays), a dependency bump to
  `mcp>=2.1.1`, and a statement that this is the plugin's first non-alpha
  release. Does NOT cover: the plugin's overall design or tool surface
  (covered by `blog-simonwillison-stateless-mcp-tooling.md`), write support,
  or any usage/adoption data beyond the author's own stated confidence. Per
  MINER.md §1, the linked GitHub issue
  (`github.com/datasette/datasette-mcp/issues/1`) and the GitHub release page
  (`github.com/datasette/datasette-mcp/releases/tag/0.2`) were both followed
  as substantive sub-pages, since the blog post's three sentences are a
  compressed summary of a longer, technically richer issue thread.

## Extracted Claims

### Claim 1: `execute_sql`'s `"rows"` field changed from an array of arrays to an array of objects, specifically to help weaker models track which value maps to which column

- **Evidence**: Direct statement in the blog post release notes, corroborated
  verbatim in the GitHub release notes for tag `0.2` and in the linked issue's
  own release-notes draft comment.
- **Confidence**: settled (first-party; the author wrote both the code change
  and the stated rationale, and the same wording appears in three places: the
  blog post, the GitHub release, and the issue comment drafting the release
  notes)
- **Quote**: "This should help weaker models avoid losing track of which
  positional array element maps to which column."
- **Our assessment**: This is the same claim the Prospector's triage comment
  already identified. It is a specific, named mechanism (positional-index
  mapping failure) rather than a generic "better for AI" justification, and
  it is consistent with the capability-tiering argument for MCP tool design
  already in the corpus (see Cross-References → Extends).

### Claim 2: The underlying problem, as filed by the author in GitHub issue #1, is that the array-of-arrays format "relies on the calling model to be strong enough to map those column names to those row values"

- **Evidence**: The GitHub issue body that motivated the 0.2 release, written
  by the plugin author, including a worked before/after example against a
  real query (`select title, slug from blog_entry order by id desc limit 3`)
  run against the author's own deployed Datasette instance.
- **Confidence**: settled (first-party issue filed and closed by the same
  author who shipped the fix, with a concrete before/after code example)
- **Quote**: "This relies on the calling model to be strong enough to map
  those column names to those row values."
- **Our assessment**: This is the fuller statement of Claim 1's rationale,
  and it names the failure mode more precisely: it is not that weaker models
  produce wrong SQL, but that they can misalign already-correct query results
  when reconstructing which column each positional value belongs to. This is
  a narrow, mechanical claim about output-format ergonomics for weaker
  models, not a broader claim about tool-calling reliability.

### Claim 3: datasette-mcp 0.2 now depends on `mcp>=2.1.1`

- **Evidence**: Direct statement in both the blog post and the GitHub release
  notes.
- **Confidence**: settled (a concrete, verifiable dependency-version pin)
- **Quote**: "Now depends on `mcp>=2.1.1`."
- **Our assessment**: On its own this is a routine dependency bump. Its
  significance only becomes clear from the linked issue thread (Claim 5
  below): the same MCP library version change that the release notes present
  as a one-line bump is also the direct cause of a test-breaking change in
  how exceptions are surfaced to clients.

### Claim 4: This is datasette-mcp's first non-alpha release, and the author states confidence in it based on his own usage rather than any external validation

- **Evidence**: Direct closing statement in the blog post.
- **Confidence**: settled (a direct first-party statement of release status)
- **Quote**: "This is the first non-alpha release of the plugin. I'm
  confident it's ready as I've been using it quite a bit myself."
- **Our assessment**: The stated basis for "ready" is explicitly personal,
  single-user dogfooding ("I've been using it quite a bit myself"), not a
  test suite, a security review, or third-party adoption data. This matches
  the `emerging` confidence grade for `blog-simonwillison-stateless-mcp-tooling.md`,
  whose Extraction Notes rated the whole datasette-mcp project "fresh,
  not-yet-battle-tested practitioner adoption evidence." The version bump
  from alpha to non-alpha is a milestone in the same still-young project,
  not evidence of a materially more mature validation process.

### Claim 5: The `mcp>=2.1.1` dependency bump was not merely routine — it changed how the underlying MCP library surfaces exception messages, and this broke the plugin's own CI before the fix (raising exceptions with more specific, custom-defined text) was applied

- **Evidence**: A sequence of comments by the author on GitHub issue #1, made
  the same day as the release: a comment stating "This broke CI," followed by
  a comment attributing the root cause to a Codex-assisted investigation.
- **Confidence**: settled (first-party developer account of a concrete CI
  failure and its diagnosed root cause, in the same issue thread that
  produced the shipped 0.2 release)
- **Quote**: "This broke CI."
- **Quote (root cause)**: "MCP 2.1.1 now hides messages from unexpected
  exceptions. The plugin raises ValueError and PermissionError, so clients
  receive only Error executing tool …, breaking the error-message
  assertions"
- **Our assessment**: This is the most novel and concrete finding in the
  source, and it is absent from the blog post entirely — the three-sentence
  "beat" only says "now depends on mcp>=2.1.1," giving no indication that the
  dependency bump was itself a breaking change requiring a code fix, not just
  a version-floor increase. This is a citable example of a common
  MCP-ecosystem failure mode: an upstream library changing how it surfaces
  exception detail to callers (here, collapsing unexpected exceptions to a
  generic "Error executing tool …" string) silently breaks any downstream
  code or tests that pattern-match on exception message content.

### Claim 6: After the fix, `execute_sql`'s `"rows"` output is a list of JSON objects keyed by column name, in place of parallel `"columns"` and `"rows"`-as-arrays fields

- **Evidence**: A follow-up comment on the same issue showing the actual
  deployed output of the same example query used in Claim 2's "before"
  example, run against the same live server after the 0.2 release was
  deployed.
- **Confidence**: settled (a real command run against the author's own live
  deployment, shown as direct before/after evidence within the same issue
  thread)
- **Quote**: (no direct prose quote; see the before/after JSON in Concrete
  Artifacts)
- **Our assessment**: This is the concrete, verifiable shape of the format
  change described abstractly in Claims 1 and 2 — the `"columns"` array is
  still present, but `"rows"` becomes a list of per-row objects
  (`{"title": ..., "slug": ...}`) rather than parallel positional arrays.
  This is a reusable, citable before/after example of the specific fix, not
  just a description of it.

## Concrete Artifacts

### Before: `execute_sql` output as array-of-arrays (datasette-mcp <0.2)

```json
{
  "database": "simonwillisonblog",
  "columns": [
    "title",
    "slug"
  ],
  "rows": [
    [
      "Understanding ChatGPT Work",
      "understanding-chatgpt-work"
    ],
    [
      "Conceptual integrity and counting lines of code",
      "conceptual-integrity-and-counting-lines-of-code"
    ],
    [
      "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things",
      "qwen-38-27b"
    ]
  ],
  "truncated": false
}
```
*Source: GitHub issue body, github.com/datasette/datasette-mcp/issues/1,
filed by Simon Willison 2026-09-01, reproducing a real query against
`datasette.simonwillison.net`.*

### After: `execute_sql` output as array-of-objects (datasette-mcp 0.2)

```json
{
  "database": "simonwillisonblog",
  "columns": [
    "title",
    "slug"
  ],
  "rows": [
    {
      "title": "Understanding ChatGPT Work",
      "slug": "understanding-chatgpt-work"
    },
    {
      "title": "Conceptual integrity and counting lines of code",
      "slug": "conceptual-integrity-and-counting-lines-of-code"
    },
    {
      "title": "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things",
      "slug": "qwen-38-27b"
    }
  ],
  "truncated": false
}
```
*Source: GitHub issue comment, github.com/datasette/datasette-mcp/issues/1,
Simon Willison, 2026-09-01T15:40:50Z, run against the deployed 0.2 release.*

### Release notes (verbatim, blog post and GitHub release tag `0.2`)

```
- "rows" from execute_sql is now an array of objects. Previously it was
  an array of arrays. This should help weaker models avoid losing track
  of which positional array element maps to which column. #1
- Now depends on mcp>=2.1.1.
```
*Source: simonwillison.net/2026/Sep/1/datasette-mcp/ and
github.com/datasette/datasette-mcp/releases/tag/0.2, commit `55f1ed1`,
published 2026-09-01T15:30:12Z.*

### CI-breakage root cause (verbatim comment, GitHub issue #1)

```
This broke CI.
```
```
Codex investigation identified MCP 2.1.1 as the problem:

> MCP 2.1.1 now hides messages from unexpected exceptions. The plugin
> raises ValueError and PermissionError, so clients receive only Error
> executing tool …, breaking the error-message assertions
```
*Source: GitHub issue comments, github.com/datasette/datasette-mcp/issues/1,
Simon Willison, 2026-09-01T15:21:09Z and 2026-09-01T15:27:52Z.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-stateless-mcp-tooling.md` Claim 8 (datasette-mcp is a
    minimal, three-tool, read-only Datasette plugin, then "the fourth attempt"
    at shipping): this note documents the same plugin's next release,
    confirming it is still under active, single-maintainer iteration one
    month later — consistent with that note's `emerging` confidence grade
    for the whole project rather than evidence of a step-change in maturity.
  - `blog-simonwillison-stateless-mcp-tooling.md` Claim 3 (MCP tools are
    "simple enough that smaller models that run on a laptop can still drive
    them reasonably well" — a capability-tiering argument for MCP over open
    shell access): Claim 1/2 here is a narrower, output-*format*-level
    instance of the same underlying concern — not just that MCP's tool
    surface is simple enough for weaker models, but that the specific JSON
    shape a tool returns can itself be tuned for weaker-model reliability.

- **Contradicts**: None identified. No existing source note makes a claim
  about MCP row-output formatting or about MCP dependency-version exception
  handling that this source opposes.

- **Extends**:
  - `blog-simonwillison-stateless-mcp-tooling.md`: that note documents
    datasette-mcp's initial design and three-tool surface (list_databases,
    get_database_schema, execute_sql); this note documents a concrete,
    shipped refinement to one of those tools' output format, plus a
    previously undocumented operational incident (the `mcp>=2.1.1`
    exception-hiding regression) in the same project.
  - `blog-simonwillison-llm032.md` Claim 5 (the `datasette.simonwillison.net/-/mcp`
    server, reached there via Anthropic's server-side `AnthropicMCP` tool):
    that note and `blog-simonwillison-stateless-mcp-tooling.md` both target
    the identical live deployment this note's before/after examples are
    drawn from — this is the same server's output format changing under
    every client that queries it, client-side (`llm-mcp-client`) or
    provider-side (`AnthropicMCP`) alike.

- **Novel**:
  - **A named, root-caused failure mode where an MCP library dependency bump
    silently changes exception-message surfacing and breaks a server's
    error-message assertions**: no prior corpus source documents an MCP
    library version bump changing how much exception detail reaches the
    client, or a case where that change broke a downstream project's tests.
  - **A concrete before/after JSON example of the array-of-arrays →
    array-of-objects row format change**, useful as a citable illustration
    of the general "shape API output for weaker-model column tracking"
    pattern, distinct from the abstract statement of the pattern already in
    the corpus.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 5 as a concrete example of a
  dependency-update failure mode specific to MCP servers: bumping an MCP
  library version can silently change how much detail is included in
  exception messages surfaced to callers, which can break error-message-based
  test assertions (or any downstream code that pattern-matches on error
  text) without any change to the server's own source. Recommend that teams
  running MCP servers pin and deliberately re-test error-path behavior on
  MCP library upgrades, not just success-path behavior — this is a narrower,
  more mechanical addition than a broad "test your dependencies" statement,
  citing the exact library (`mcp`), version (`2.1.1`), and symptom (generic
  "Error executing tool …" replacing the plugin's own `ValueError`/
  `PermissionError` messages).
- **Chapter 02 (Harness Engineering)**: If the guide cites
  `blog-simonwillison-stateless-mcp-tooling.md` Claim 3's capability-tiering
  argument for MCP tool design (bounded tool surfaces are drivable by weaker
  models), add this note's Claim 1/2 as a concrete, tool-output-level
  refinement of the same principle: return row data as an array of objects
  (keyed by column name) rather than an array of positional values, so a
  weaker model does not have to correlate a separate columns array against
  each row. This is a specific, shippable API-design recommendation, not
  just a restatement of the general principle.

## Extraction Notes

- **WebFetch's AI summarizer declined full verbatim reproduction on first
  request**, consistent with prior notes' experience with this source
  (`blog-simonwillison-stateless-mcp-tooling.md`, `blog-simonwillison-mcp-claude-chatgpt-setup.md`).
  The blog post's raw HTML was instead fetched directly via `curl` and
  stripped of markup; all quotes in this note from the blog post were
  matched character-for-character against that raw text.
- **Followed two linked sub-pages** per MINER.md §1: the GitHub release page
  (`github.com/datasette/datasette-mcp/releases/tag/0.2`) and the linked
  GitHub issue (`github.com/datasette/datasette-mcp/issues/1`), fetched via
  the GitHub REST API (issue body and comments) to get exact, unparaphrased
  text. The issue thread — not the three-sentence blog post — is where the
  most substantive and novel content in this source actually lives (Claims 2,
  5, and 6, and both Concrete Artifacts JSON examples).
- **Two prior Prospector triage comments on this issue disagree** about
  whether this source merits a standalone note: one rates novelty "medium"
  (citing Ch02/Ch03 relevance) and recommends mining; the other rates
  novelty "low" (citing Ch06/Ch07) and concludes "no new architectural
  claims or patterns worth a separate note," suggesting the blog post's
  content alone is a minor refinement of `blog-simonwillison-stateless-mcp-tooling.md`.
  Read in isolation, the blog post supports the "low novelty" reading — it
  is three sentences. However, following the linked GitHub issue (per
  MINER.md §1's instruction to follow substantive linked pages) surfaced the
  CI-breaking `mcp>=2.1.1` exception-handling regression (Claim 5), which is
  not mentioned in the blog post at all and is not covered by any existing
  source note. This note is written on the strength of that issue-thread
  finding, not the blog post's row-format change alone; the Assayer should
  weigh whether a GitHub issue thread linked from a thin blog "beat" counts
  as within-scope for a `blog-post`-typed source, since the novel material
  here is technically drawn from the linked issue rather than the blog post
  itself.
- **No contradictions filed**: reviewed all four overlapping notes named
  across both Prospector triage comments
  (`blog-simonwillison-stateless-mcp-tooling.md`, `blog-simonwillison-llm032.md`,
  `blog-simonwillison-mcp-claude-chatgpt-setup.md`) plus
  `blog-simonwillison-datasette-llm-limits.md` (same author's adjacent
  Datasette/LLM tooling ecosystem) for conflicting claims; none found.
- **Cross-references verified**: `blog-simonwillison-stateless-mcp-tooling.md`
  Claims 3 and 8, and `blog-simonwillison-llm032.md` Claim 5, were confirmed
  by re-reading each note in full and locating the numbered `### Claim N:`
  heading in document order before citing them here.
- **Confidence rationale**: `confidence_overall` is set to `emerging` rather
  than `settled` — the individual factual claims about what changed and why
  are `settled` (first-party, verifiable against GitHub), but the project as
  a whole is one release past alpha, validated only by the author's own
  single-user testing (Claim 4), and the CI-breaking regression (Claim 5)
  demonstrates the project is still finding and fixing basic integration
  issues with its own dependencies in real time.
