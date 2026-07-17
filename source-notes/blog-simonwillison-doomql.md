---
source_url: https://simonwillison.net/2026/Jul/13/doomql/
source_type: blog-post
title: "DOOMQL"
author: Simon Willison
date_published: 2026-07-13
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1952"
---

# DOOMQL

> Simon Willison link-blogs Peter Gostev's DOOMQL (a Doom-like game whose
> engine is entirely SQL, built with GPT-5.6 Sol), then demonstrates a
> two-prompt chat session with Claude (Fable 5) — using the Datasette Apps
> plugin's copy-paste-prompt pattern — that produces a working live SQL
> viewer, then a minimap overlay, from a single terse follow-up prompt.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, a "link blog" entry — short
  commentary wrapped around a link to a third party's open-source project,
  13th July 2026, posted 10:34pm). The primary post itself is brief (roughly
  200 words plus two screenshots and two code blocks); most of the
  extractable substance requires following the linked GitHub repository
  (`petergpt/doomql`), its README, the linked SQL source file, and the
  linked Gist containing the actual Claude-generated app code.
- **Author credibility**: Simon Willison is the creator of Datasette and the
  `llm` Python CLI, and the author of the `datasette-apps` plugin referenced
  in this post (see [[blog-simonwillison-datasette-apps]]). He is reporting
  first-hand on his own use of Claude here — he pasted the prompts and
  captured the screenshots himself — though the underlying DOOMQL project
  was built by a third party (Peter Gostev) using a different model
  (GPT-5.6 Sol), not Claude.
- **Scope**: Covers (a) the DOOMQL project itself — an open-source
  SQL-as-game-engine demo — and (b) Willison's own two-prompt Claude chat
  session that built a companion live-viewer web app on top of DOOMQL's
  SQLite database using the Datasette Apps plugin. Does not cover Claude
  Code, agentic/tool-use workflows, or any multi-turn debugging — the
  Claude portion of this post is a two-message chat exchange with no
  visible back-and-forth correction.

## Extracted Claims

### Claim 1: DOOMQL implements a complete Doom-like game engine entirely in SQL, with the Python host restricted to raw input/output transport and no game logic
- **Evidence**: The project's GitHub README (`petergpt/doomql`) provides an
  explicit two-column table splitting responsibilities between "SQL owns"
  (key bindings, movement/collision, enemy AI, doors/pickups/death/victory,
  raycasting, sprite scaling, weapon/crosshair/HUD, every final RGB value)
  and "Python only transports" (raw terminal key bytes, a monotonic
  timestamp, terminal columns/rows, fixed SQL execution requests, completed
  scanlines to stdout, terminal mode setup). The README states this
  boundary is enforced by the test suite.
- **Confidence**: settled (verifiable directly against the open-source
  repository; the boundary is asserted by the project's own tests, not just
  described in prose)
- **Quote**: "The host deliberately contains no key map, coordinates, game constants, colours, rendering calculations or game-state decisions. Tests enforce this boundary."
  *(Source: README.md, petergpt/doomql, section "What is really implemented in SQL?")*
- **Our assessment**: This is a strong, testable architectural claim (not
  just a marketing description) — the repository's own verification suite
  is used as the enforcement mechanism. Willison does not repeat or verify
  this claim in his post; he takes the project's framing at face value. We
  have not independently run DOOMQL's test suite to confirm the boundary
  holds, so this claim's strength rests entirely on the project's own
  self-report.

### Claim 2: DOOMQL's renderer is a single SQL view built on a recursive CTE that performs full ray tracing (DDA raycasting) in SQLite, producing one output row per screen pixel
- **Evidence**: Willison links directly to the implementation file
  (`sql/003_render.sql`, 525 lines), which we fetched and confirmed opens
  with `CREATE VIEW frame_pixels AS WITH RECURSIVE cfg AS MATERIALIZED (...)`
  computing player angle, field-of-view plane vectors, and projection
  plane entirely in SQL expressions.
- **Confidence**: settled (the linked file is real, open-source, and
  matches the description)
- **Quote**: "Here's the huge SQL query that implements a full ray tracer in SQLite using a recursive CTE."
  *(Source: simonwillison.net/2026/Jul/13/doomql/)*
- **Our assessment**: This is the most technically novel element of the
  underlying project — using a single recursive CTE as a ray-tracing kernel
  is unusual and worth noting as a demonstration of how far SQL can be
  pushed as a computation substrate, independent of the AI-tooling angle
  the guide otherwise focuses on. It is adjacent to, not itself, an
  AI-development-workflow claim.

### Claim 3: A single terse, technically-scoped natural-language prompt pasted into Claude chat (Fable 5) produced a working HTML+JavaScript Datasette App that live-queries a `frame_pixels` SQL view and auto-refreshes
- **Evidence**: Willison quotes the exact prompt he pasted and shows the
  resulting screenshot of a running app. We independently fetched the
  linked Gist (`gist.github.com/simonw/7c78184476fccd4b70b02f7f9048dffa`)
  containing the actual delivered code and confirmed it is a real,
  self-contained HTML file with a `<canvas id="screen">`, a `datasette.query()`
  call issuing a `SELECT y, group_concat(...) FROM frame_pixels GROUP BY y`
  query, and a `setTimeout`-based refresh loop matching the "refresh once a
  second" instruction.
- **Confidence**: settled (both the prompt text and the resulting code
  artifact are independently verifiable — this is not a paraphrase of what
  the app does, it is the literal code)
- **Quote**: "Build an app that displays the current state of the screen using the frame_pixels view with its x, y, r, g, b columns. have it refresh once a second."
  *(Source: simonwillison.net/2026/Jul/13/doomql/, quoted prompt block)*
- **Our assessment**: The prompt names the exact view and column names but
  gives no UI/layout instruction, no framework choice, and no styling
  guidance — Claude filled in canvas-based pixel rendering, a HUD readout,
  and dark-theme CSS unprompted. This is a useful, concrete example of how
  little specification is needed once the *interface contract* (view name,
  columns, refresh cadence) is stated precisely — the ambiguity Claude
  resolved was presentation, not semantics.

### Claim 4: A two-word follow-up prompt ("add a minimap") extended the already-working app with a second live-rendered panel — a top-down tactical map with player heading/FOV cone, enemy and pickup markers, sliding door graphics, and a legend — without further specification
- **Evidence**: We fetched the raw Gist HTML directly and confirmed it
  contains a second `<canvas id="minimap">` element, a `drawMinimap()`
  function computing a player field-of-view triangle from `angle`/`fov`
  values, per-entity-type dot rendering (`pickup`/`enemy`/`boss` colors),
  door-state rendering keyed on an `open_fraction` column, and a static
  `.legend` block with six labeled swatches — none of which were named or
  described in either prompt.
- **Confidence**: settled (the delivered code is real and independently
  inspectable via the linked Gist)
- **Quote**: "add a minimap"
  *(Source: simonwillison.net/2026/Jul/13/doomql/, second quoted prompt block)*
- **Our assessment**: This is the single most extractable data point in the
  post: a four-character instruction produced ~120 lines of new JavaScript
  (a second SQL query against a `doors`/`entities` union view, a coordinate
  transform, and canvas drawing logic for six distinct visual states) that
  correctly infers domain concepts (FOV cone, door "locked" vs "open"
  states, boss vs regular enemy) from schema and prior context rather than
  from explicit instruction. It is a single example, not a controlled
  comparison, and we cannot rule out that the chat session (not visible to
  us — the linked `claude.ai/share/...` transcript is client-rendered and
  did not yield readable content via fetch) included clarifying exchanges
  Willison didn't quote.

### Claim 5: This chat session used the Datasette Apps plugin's "copy-paste prompt" workflow — a schema-aware prompt template generated by the tool itself and pasted directly into an external chat interface
- **Evidence**: Willison's own description of his workflow, and the prior
  Datasette Apps launch post's description of the same feature.
- **Confidence**: settled (first-party account, and the mechanism it refers
  to is independently documented in [[blog-simonwillison-datasette-apps]],
  Claim 4: "Datasette Apps include a 'copyable prompt' in the create-app
  form that contains the schema of selected databases, enabling users to
  paste directly into an LLM to generate app code")
- **Quote**: "I created a new app, pasted the copy-paste prompt into Claude chat (Fable 5) and told it:"
  *(Source: simonwillison.net/2026/Jul/13/doomql/)*
- **Our assessment**: This post is the first concrete, narrated instance in
  our corpus of the copy-paste-prompt mechanism from
  [[blog-simonwillison-datasette-apps]] Claim 4 being used end-to-end by
  its own author, outside a launch-announcement context. It corroborates
  that claim rather than just restating it: the earlier post described the
  *feature*, this post demonstrates the *workflow it enables* on an
  unrelated third-party dataset (a Doom clone's game-state database) that
  Willison did not design.

### Claim 6: DOOMQL's underlying game engine was built by a third party (Peter Gostev) using GPT-5.6 Sol, not Claude — Claude's only role in this post is generating a read-only viewer layered on top of an already-complete system
- **Evidence**: Willison explicitly attributes the base project to a
  different author and a different model before describing his own,
  separate use of Claude.
- **Confidence**: settled (explicit, unambiguous attribution in the source
  text)
- **Quote**: "Peter Gostev built this using GPT-5.6 Sol."
  *(Source: simonwillison.net/2026/Jul/13/doomql/)*
- **Our assessment**: This scope boundary matters for how the guide should
  cite this source. It is not evidence that "Claude built DOOMQL" or that
  Claude can produce a from-scratch game engine in SQL — it is evidence
  about a much narrower and more common task: Claude generating a
  self-contained visualization/dashboard layer against an existing,
  externally-defined schema it did not design. That narrower claim is
  well-supported; the broader one would not be, and this note should not be
  cited for the broader one.

### Claim 7: DOOMQL's test suite includes 36 tests covering gameplay, collision, progression, deterministic replay, frame/RGB correctness, transactional rollback of audit events, and a hardware-dependent renderer-latency gate that is explicitly excluded from CI because shared runner timing is not a meaningful baseline
- **Evidence**: The project README's "Verification" section.
- **Confidence**: settled (first-party project documentation; we did not
  run the suite ourselves)
- **Quote**: "The 36-test suite checks gameplay, collision, progression, deterministic replay, frame dimensions, RGB ranges, ANSI decoding, read-only inspection, transaction rollback, exact runtime-source identity and the absence of game logic from the Python host. It also includes a strict local renderer-latency gate."
  *(Source: README.md, petergpt/doomql, section "Verification")*
- **Quote**: "GitHub Actions runs the hardware-independent checks on macOS and Linux with supported Python versions. The wall-clock latency assertion stays local because shared virtual-runner timing is not a meaningful performance baseline."
  *(Source: README.md, petergpt/doomql, section "Verification")*
- **Our assessment**: Not a Claude-specific claim, but a concrete example of
  a verification pattern the guide already discusses in the abstract
  (excluding non-deterministic/hardware-sensitive performance assertions
  from shared CI while keeping them as a local gate) — worth noting as a
  real-world instance rather than citing for any AI-authorship claim, since
  we cannot confirm from this post alone which model(s) wrote the test
  suite.

## Concrete Artifacts

**Willison's first prompt to Claude chat (Fable 5), verbatim from the post:**
```
Build an app that displays the current state of the screen using the frame_pixels view with its x, y, r, g, b columns. have it refresh once a second.
```

**Willison's follow-up prompt, verbatim from the post:**
```
add a minimap
```

**Shell commands to run DOOMQL and inspect its SQLite database via Datasette (from the post):**
```bash
cd /tmp
git clone https://github.com/petergpt/doomql
cd doomql
uv run host/doomql.py
```
```bash
uvx --prerelease=allow  --with datasette-apps datasette \
  /tmp/doomql/.doomql/doomql.sqlite \
  -p 4444 --root --secret 1 --internal internal.db
```

**SQL queries the Claude-generated app issues against the live database (from the delivered Gist, `gist.github.com/simonw/7c78184476fccd4b70b02f7f9048dffa`), fetched and confirmed real:**
```javascript
// Per-scanline pixel data — kept below row limits by grouping.
const FRAME_SQL = [
  "select y, group_concat(x || ',' || r || ',' || g || ',' || b, ';') as line",
  "from frame_pixels",
  "group by y",
  "order by y"
].join("\n");

// Static level geometry for the minimap base layer.
const MAP_SQL = [
  "select mc.y, group_concat(",
  "  mc.x || ',' || mc.solid || ',' || mc.is_exit || ',' ||",
  "  m.base_r || ',' || m.base_g || ',' || m.base_b, ';') as line",
  "from map_cells as mc",
  "join materials as m on m.id = mc.material_id",
  "group by mc.y",
  "order by mc.y"
].join("\n");

// Dynamic minimap overlay: doors + live entities in one query.
const OVERLAY_SQL = [
  "select 'door' as k, x * 1.0 as x, y * 1.0 as y, open_fraction as a, locked as b",
  "from doors",
  "union all",
  "select case when et.kind = 'pickup' then 'pickup'",
  "            when et.is_boss = 1 then 'boss'",
  "            else 'enemy' end as k,",
  "       e.x, e.y, 0.0 as a, 0 as b",
  "from entities as e",
  "join entity_types as et on et.id = e.type_id",
  "where e.active = 1"
].join("\n");
```
*(Fetched from the raw Gist by the Miner; not reproduced in the blog post
itself, which links to it rather than inlining it.)*

**DOOMQL's SQL/Python responsibility split (from the project README, "What is really implemented in SQL?" table):**
```
| SQL owns                                        | Python only transports          |
|--------------------------------------------------|----------------------------------|
| Key bindings and input interpretation             | Raw terminal key bytes           |
| Player movement and collision                      | A monotonic timestamp            |
| Enemy AI, combat and progression                   | Terminal columns and rows        |
| Doors, pickups, death and victory                  | Fixed SQL execution requests     |
| DDA raycasting and wall projection                 | Completed SQL scanlines to stdout|
| Sprite scaling, depth and occlusion                | Terminal mode setup and restoration |
| Weapon, crosshair, effects and HUD                 | Nothing game-specific            |
| Every final RGB value and ANSI colour code         |                                  |
```

## Cross-References

- **Corroborates**: [[blog-simonwillison-datasette-apps]] Claim 4 ("Datasette
  Apps include a 'copyable prompt' in the create-app form that contains the
  schema of selected databases, enabling users to paste directly into an
  LLM to generate app code") — this post is a first-person, narrated
  instance of exactly that workflow, applied to a database the tool's own
  author did not design, which is stronger evidence than the launch post's
  self-description alone.
- **Extends**: [[blog-simonwillison-datasette-apps]] Claim 6 (Datasette Apps
  were motivated by Claude Artifacts' lack of persistent database access) —
  this post is a concrete example of the "stateful Artifacts" pattern that
  claim describes in the abstract: a self-contained HTML/JS app, generated
  from a terse chat prompt, wired to a live, externally-defined SQLite
  database via a narrow read-only API.
- **Extends**: [[blog-simonwillison-claude-fable-5]] — that note profiles
  Claude Fable 5's capabilities and pricing in general terms (Claim 1) and
  documents Fable 5 performing autonomous coding/implementation work
  (Claims 6-9) via Claude Code; this post is a data point about the same
  model used in a much lighter-weight setting — two-message chat, no tool
  use, no agentic loop — worth distinguishing from that note's
  Claude-Code-driven examples when the guide discusses "how much
  scaffolding does Fable 5 need."
- **Contradicts**: None identified.
- **Novel**: The specific "one terse prompt, then one near-content-free
  follow-up prompt" progression, with the actual before/after code diff
  independently verifiable via the linked Gist, is new to our corpus. Prior
  vibe-coding/HTML-generation notes (e.g.
  [[blog-simonwillison-rss-vibe-coded-apps]],
  [[blog-simonwillison-vibe-coding-agentic-engineering]]) discuss the
  phenomenon and its risks at a portfolio/industry level; this post is a
  single, inspectable before/after code sample rather than a trend
  description.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: If the chapter discusses rapid UI
  prototyping or "chat, not agentic loop" workflows, this source provides a
  concrete, code-verifiable example (Claims 3-4) of a two-message Claude
  chat session — not Claude Code, not a tool-using agent — producing a
  working data-visualization component against a precisely-named but
  otherwise unstyled interface contract (view + column names + refresh
  cadence). Worth citing as a minimal-specification example specifically
  because the delivered code was independently checked, not just described.
- **Chapter 04 (Context Engineering / Inference-Driven Development)**: The
  minimap follow-up (Claim 4) is a citable example of a follow-up prompt
  carrying almost no explicit content ("add a minimap") relying entirely on
  session context (the existing app's schema access, established visual
  style, and domain vocabulary implicit in the database) to produce a
  correctly-scoped result. If the chapter makes claims about how much
  specification a follow-up turn needs once initial context is established,
  this is a single concrete data point (not a controlled study) supporting
  "very little, when the interface contract from turn one is precise."
- **Caution for both chapters**: Do not cite this source for claims about
  Claude building complex systems from scratch — the complex part (the SQL
  game engine itself) was built by a different author using a different
  model (Claim 6). Only the thin visualization layer is attributable to
  Claude.

## Extraction Notes

The primary blog post itself is short — a typical Willison "link blog"
entry, roughly 200 words of original commentary plus two quoted prompts and
two screenshots. Per MINER.md §1, I followed the substantive linked pages
rather than treating the post text alone as the source:
- The GitHub repository README (`petergpt/doomql`) — read in full, used for
  Claims 1 and 7 and the Concrete Artifacts table.
- The linked SQL implementation file (`sql/003_render.sql`, 525 lines) —
  fetched and skimmed to confirm the recursive-CTE raytracer claim (Claim 2)
  is accurate, not just Willison's characterization.
- The linked Gist containing the actual delivered app code
  (`gist.github.com/simonw/7c78184476fccd4b70b02f7f9048dffa`) — fetched in
  full and read; this is the single most valuable follow-linked page, since
  it lets Claims 3 and 4 be verified against the real generated code rather
  than taken on Willison's description alone.
- The linked `claude.ai/share/...` conversation URL, which the post's text
  points to as the actual chat transcript ("pasted the copy-paste prompt
  into Claude chat (Fable 5) **and told it**"), did **not** yield readable
  content — `claude.ai/share/` pages are client-side-rendered and returned
  only an empty app shell to a direct fetch. This means the two prompts
  quoted in the blog post are the only visibility we have into that
  session; we cannot confirm there was no additional back-and-forth beyond
  what Willison chose to quote. Flagged explicitly in Claim 4's assessment.
- Also read [[blog-simonwillison-datasette-apps]] in full (not just
  grepped) to verify the Claim 4/Claim 6 cross-references above resolve to
  real, correctly-numbered claims in that note, per MINER.md §4b.
- Did not fetch `sql/tick.sql` (the other file the README calls out as
  important) — the render/raytracer file was sufficient to verify Claim 2,
  and the game-logic file is not directly relevant to the AI-workflow
  claims this note prioritizes.
