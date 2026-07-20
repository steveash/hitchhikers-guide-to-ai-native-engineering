---
source_url: https://simonwillison.net/2026/Jul/16/grok-mermaid/
source_type: blog-post
title: "Mermaid to Unicode box art (grok-mermaid)"
author: Simon Willison
date_published: 2026-07-16
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: anecdotal
issue: "#2057"
---

# Mermaid to Unicode box art (grok-mermaid)

> Simon Willison found a self-contained Mermaid-to-Unicode-box-art Rust renderer while
> reading through xAI's newly open-sourced Grok Build agent codebase, then used a single
> prompt in Claude Code for web (Fable 5) to extract that renderer from its parent
> codebase, strip its dependency on the `ratatui` TUI crate via a hand-written shim, and
> compile it to a standalone WebAssembly module with a browser playground — a concrete,
> verifiable instance of "discover reusable code inside another AI-native agent's
> open-sourced repo, then repurpose it via an agent in a different runtime."

## Source Context

- **Type**: blog-post (Simon Willison "Tool" post — his short-form category for shipped
  utilities, as opposed to "blogmark" links or long-form essays. Very short: roughly 90
  words of body text plus a screenshot and posting metadata. The substantive technical
  content lives in two linked artifacts that were read in full for this extraction: the
  GitHub pull request that shipped the tool (`simonw/tools#293`, containing the exact
  prompt used and an implementation write-up) and Willison's companion post from the day
  before (`simonwillison.net/2026/Jul/15/grok-build/`) describing the xAI Grok Build
  open-sourcing that made the source code available to find in the first place.)
- **Author credibility**: Simon Willison is the creator of Django and Datasette, author of
  the `llm` CLI, and a designated `trusted-feed` source in this corpus with dozens of
  prior notes documenting his own Claude Code / Claude Code for web sessions (see
  `blog-simonwillison-liteparse-browser.md`, `blog-simonwillison-opfs-pyodide.md`,
  `blog-simonwillison-pyodide-asgi-browser.md`, `blog-simonwillison-servo-crate-exploration.md`).
  He publishes the underlying artifacts (PRs, live tools, prompts) for every session he
  reports on, making his claims independently verifiable rather than self-reported. No
  vendor affiliation with Anthropic or xAI.
- **Scope**: Covers one concrete build: porting `xai-grok-markdown/src/mermaid.rs` (a
  terminal Mermaid renderer from xAI's Grok Build agent) into a browser-based WebAssembly
  tool, using a single Claude Code for web (Fable 5) session. Does NOT cover: a session
  transcript or timing/cost data for the mermaid port itself (unlike some of Willison's
  more detailed workflow posts, no duration or token cost is given for this session); a
  deep technical review of the Mermaid rendering algorithm; or any assessment of whether
  the ported tool's output is faithful to the original TUI renderer beyond the screenshot
  shown.

## Extracted Claims

### Claim 1: The shipped tool converts Mermaid diagram syntax into terminal-style Unicode box-drawing art rendered entirely client-side in the browser via WebAssembly, supporting five diagram types with a defined fallback for the rest

- **Evidence**: Willison's own tool description in the post body, describing the live tool
  at `tools.simonwillison.net/grok-mermaid`.
- **Confidence**: settled (author's direct description of a live, publicly runnable tool)
- **Quote**: "Convert Mermaid diagram syntax into terminal-style Unicode box-drawing art rendered entirely in your browser using WebAssembly. The tool supports flowcharts, sequence, state, class, and ER diagrams, with other diagram types falling back to a framed source listing. You can adjust the output width, copy the rendered diagram as text, or generate a shareable link to your diagram."
- **Our assessment**: This is a complete, working utility (adjustable width, copy-as-text,
  shareable links) rather than a proof-of-concept demo, and it runs with no backend —
  consistent with the pattern already documented across Willison's other browser-WASM
  tools in this corpus (`blog-simonwillison-opfs-pyodide.md`,
  `blog-simonwillison-pyodide-asgi-browser.md`). The stated diagram-type support (graph/flowchart,
  sequence, state, class, ER) is broader than the module's own Rust doc comment claims
  (see Extraction Notes) — the ported code evidently exercises class- and ER-diagram code
  paths that exist in the source but aren't mentioned in its top-of-file summary.

### Claim 2: Willison discovered the Mermaid renderer by reading through the newly open-sourced Grok Build codebase, not by searching for a Mermaid-rendering library specifically

- **Evidence**: Willison's own narrative of how he found the code, with a direct link to
  the specific file and commit.
- **Confidence**: settled (first-person account, verifiable via the linked commit)
- **Quote**: "While exploring the codebase for the newly open-sourced Grok CLI coding agent I came across xai-grok-markdown/src/mermaid.rs, a \"self-contained terminal renderer for Mermaid diagrams\" written in Rust."
- **Our assessment**: This is the core novel pattern the Prospector flagged: the code
  wasn't sought out — it was found incidentally while exploring a competitor AI lab's
  open-sourced agent internals for an unrelated reason (Willison's companion post,
  Claim 6 below, shows the codebase exploration was originally about auditing xAI's data
  practices, not about finding a Mermaid renderer). "Read a competitor's open-sourced
  agent code for other reasons, notice a reusable component, port it" is a more
  serendipitous discovery path than the deliberate "give the agent a crate name" pattern
  in `blog-simonwillison-servo-crate-exploration.md`.

### Claim 3: The exact prompt Willison used in Claude Code for web (Fable 5) instructed the agent to clone the Grok Build repo, isolate the Rust renderer from its parent codebase, compile it to WebAssembly, and build a browser playground with example diagrams, license attribution, and build scripts, all in one delegation

- **Evidence**: The prompt is quoted verbatim (as a Markdown blockquote) at the top of the
  GitHub pull request Willison linked from the blog post as "the prompt."
- **Confidence**: settled (verbatim artifact reproduced in a merged, public pull request)
- **Quote**: "Clone https://github.com/xai-org/grok-build to /tmp\n\nLook at the code in crates/codegen/xai-grok-markdown/src/mermaid.rs which renders some chart types as \"Unicode box-drawing art\"\n\nFigure out how to run that Rust code independent of the Rust of that codebase. Then figure out how to compile it to WebAssembly and build grok-mermaid.html as a browser-based playground for trying out the code, with several example mermaid charts you can try out.\n\nPut your Rust code in a subfolder - with an appropriate license note, and the build scripts for turning that into the WASM blob" (github.com/simonw/tools/pull/293, PR body, blockquoted prompt)
- **Our assessment**: This single prompt bundles four distinct sub-tasks that would
  traditionally be separate engineering steps: (1) source extraction/isolation from a
  much larger foreign codebase, (2) cross-compilation target change (native Rust →
  wasm32), (3) building an interactive web UI around the compiled artifact, and (4)
  license compliance (explicit instruction to add "an appropriate license note"). The
  prompt does not specify *how* to decouple the code from its dependencies — that
  decision (the `shim.rs` approach in Claim 4) was left entirely to the agent. This is a
  concrete, reproducible example of "loose goal + concrete deliverable" prompting for a
  cross-language, cross-runtime porting task, distinct from the crate-exploration pattern
  in `blog-simonwillison-servo-crate-exploration.md` (Claim 5) because here the target
  code already existed and worked — the task was extraction and re-targeting, not
  API discovery from scratch.

### Claim 4: To port the renderer without pulling in the full `ratatui` TUI dependency, Claude Code for web wrote a minimal shim module providing stand-in versions of only the four `ratatui` types the renderer actually used

- **Evidence**: Listed explicitly in the PR's "Key Changes" section as a distinct new
  file, with its purpose stated.
- **Confidence**: settled (verifiable in the merged PR's file list and description)
- **Quote**: "src/shim.rs: Minimal stand-ins for ratatui types (Style, Modifier, Span, Line) to avoid pulling in the full ratatui dependency" (github.com/simonw/tools/pull/293, PR body, "Key Changes" section)
- **Our assessment**: This is the most technically interesting decision in the port, and
  it wasn't specified in the prompt — the agent identified that `ratatui` (a terminal-UI
  crate with a large dependency graph, much of it irrelevant or incompatible with
  wasm32) was the actual blocker to a small WASM build, and resolved it by reimplementing
  just the narrow surface the renderer touches rather than attempting to compile the full
  `ratatui` crate to WASM or forking it. This is a dependency-isolation strategy a
  practitioner would recognize as good judgment for a cross-target port: identify the
  minimum interface actually consumed, and stub only that.

### Claim 5: The WASM build exposes a hand-written, minimal FFI surface (`wasm_alloc`, `wasm_render_html`, `wasm_result_ptr`) instead of using `wasm-bindgen`, specifically to avoid its overhead

- **Evidence**: Stated directly in the PR's "Implementation Details" section.
- **Confidence**: settled (verifiable in the merged PR description and source)
- **Quote**: "The WebAssembly module uses a simple FFI surface (wasm_alloc, wasm_render_html, wasm_result_ptr) for browser integration, avoiding wasm-bindgen overhead" (github.com/simonw/tools/pull/293, PR body, "Implementation Details" section)
- **Our assessment**: `wasm-bindgen` is the conventional, higher-level tool for Rust↔JS
  interop and most Rust-to-WASM tutorials default to it. Choosing a hand-rolled
  alloc/pointer-passing FFI instead is a lower-level, more manual approach that trades
  ergonomics for a smaller/simpler build — a reasonable choice for a single-function
  renderer (source text in, styled HTML out) where `wasm-bindgen`'s richer type-marshalling
  isn't needed. Notable as a second instance (after the `shim.rs` decision) of the agent
  making an unprompted architecture simplification rather than reaching for the
  heavier standard tool.

### Claim 6: The PR explicitly separates the vendored Rust source (kept in its own subfolder with its own LICENSE file matching the original Apache-2.0 license) from the new WASM/web-integration code, following the prompt's instruction for "an appropriate license note"

- **Evidence**: Listed in the PR's "New Rust library" and "Build artifacts" bullets.
- **Confidence**: settled (verifiable in the merged PR file list)
- **Quote**: "src/mermaid.rs: Core renderer (copied from xai-org/grok-build under Apache-2.0)" and "LICENSE: Apache-2.0 license (matching source)" and "README.md: Documentation on the origin and rebuild process" (github.com/simonw/tools/pull/293, PR body, "Key Changes" and "Build artifacts" bullets)
- **Our assessment**: This is a concrete example of an agent following an
  under-specified compliance instruction ("with an appropriate license note") correctly:
  it identified the source license (Apache-2.0, from the Grok Build repo), replicated it
  alongside the copied code, and added a README explaining provenance and how to rebuild
  — the standard practice for vendoring third-party code, done without the prompt
  spelling out any of those specific steps. This is a positive data point for "AI agents
  copying code from other repos will handle basic license attribution if told to add
  license notes," though it is a single instance and the correctness of the attribution
  was not independently audited by Willison in the post.

### Claim 7: The PR includes Playwright browser tests that validate the WebAssembly module's rendering behavior, covering initial render, example-loading, and error handling

- **Evidence**: Listed in the PR's "Testing" section as a distinct deliverable.
- **Confidence**: settled (verifiable in the merged PR file list)
- **Quote**: "tests/test_grok_mermaid.py: Playwright tests validating rendering via the WebAssembly module" and "Tests for initial render, example loading, and error handling" (github.com/simonw/tools/pull/293, PR body, "Testing" section)
- **Our assessment**: The agent produced browser-level (not just Rust unit-level) tests
  for the ported tool, which is the appropriate test layer for a WASM-in-browser artifact
  — a Rust `cargo test` alone wouldn't catch WASM loading, JS↔WASM marshalling, or DOM
  rendering failures. This mirrors the "Playwright TDD" pattern already documented in
  `blog-simonwillison-liteparse-browser.md` Claim 7 ("Use playwright and red/green TDD,
  plan that too" as a repeatable prompt habit), reinforcing that browser-based Playwright
  testing is a repeat pattern across several of Willison's AI-ported browser tools, not a
  one-off for this project.

### Claim 8: xAI's Grok CLI ("Grok Build") faced a community backlash after it was found to upload entire directories — including SSH keys and password manager databases — to xAI's Google Cloud buckets when run, and xAI responded by disabling the behavior and open-sourcing the full agent codebase under Apache 2.0

- **Evidence**: From Willison's companion post the day before, describing the incident
  that led to the open-sourcing, including a direct user report and an Elon Musk quote
  about data deletion.
- **Confidence**: emerging (Willison is relaying a community-reported incident and a
  public statement from Musk; he states he has "not seen an official explanation for why
  it was doing this" — the mechanism/intent behind the upload behavior itself is not
  independently confirmed, only the reported symptom and xAI's public response)
- **Quote**: "xAI's grok CLI tool faced severe community backlash yesterday when it became apparent that running the command in a directory could upload that entire directory to xAI's Google Cloud buckets." (simonwillison.net/2026/Jul/15/grok-build/)
- **Quote (user report)**: "my SSH keys, my password manager database, my documents, photos, videos, everything" (relayed by Willison, simonwillison.net/2026/Jul/15/grok-build/, attributed to a user report)
- **Quote (Musk)**: "As a precautionary measure, all user data that was uploaded to SpaceXAI before now will be completely and utterly deleted." (relayed by Willison, simonwillison.net/2026/Jul/15/grok-build/)
- **Our assessment**: This is important context for why the source code was available to
  find at all: the open-sourcing wasn't a routine developer-relations move, it was a
  trust-recovery response to a serious agentic-tool privacy incident (an agent silently
  exfiltrating an entire home directory, including credentials, to the vendor's cloud
  storage). For a guide covering agent security/trust boundaries, this is a concrete,
  named incident of exactly the "agent has broad filesystem access and an undisclosed
  network egress path" failure mode — distinct from the mermaid-porting story itself, but
  the reason that story was possible.

### Claim 9: Willison measured the Grok Build codebase at 844,530 lines of Rust (excluding whitespace and comments, ~3% vendored) using his own SLOCCount tool, compared to 950,933 lines of Rust for `openai/codex`, and concluded that terminal coding agents are more complex than he had realized

- **Evidence**: Willison's own measurement, using a tool he built himself, stated as a
  direct comparison with a named competitor codebase.
- **Confidence**: settled (first-party measurement using the author's own public tool,
  applied to a public, open-sourced repository)
- **Quote**: "It's quite a surprising codebase! Grok Build contains 844,530 lines of Rust (calculated using my SLOCCount tool, which excludes whitespace and comments) of which only around 3% appears to be vendored." (simonwillison.net/2026/Jul/15/grok-build/)
- **Quote (comparison)**: "For comparison, openai/codex is 950,933 lines of Rust. Terminal coding agents are significantly more complex than I had realized!" (simonwillison.net/2026/Jul/15/grok-build/)
- **Our assessment**: This is a useful, verifiable scale data point for anyone estimating
  the engineering investment behind frontier terminal coding agents — both Grok Build and
  Codex CLI sit under a million lines of largely non-vendored Rust, which is a
  substantial from-scratch systems-engineering effort, not a thin wrapper around an API.
  It's tangential to the mermaid-porting story itself but corroborates that the codebase
  Willison was browsing (and found the renderer in) is large and substantive, not a toy
  reference implementation.

## Concrete Artifacts

### The exact prompt (verbatim, from github.com/simonw/tools/pull/293)

```
Clone https://github.com/xai-org/grok-build to /tmp

Look at the code in crates/codegen/xai-grok-markdown/src/mermaid.rs which renders
some chart types as "Unicode box-drawing art"

Figure out how to run that Rust code independent of the Rust of that codebase.
Then figure out how to compile it to WebAssembly and build grok-mermaid.html as a
browser-based playground for trying out the code, with several example mermaid
charts you can try out.

Put your Rust code in a subfolder - with an appropriate license note, and the
build scripts for turning that into the WASM blob
```

### PR file/change summary (from github.com/simonw/tools/pull/293, "Key Changes" section)

```
New Rust library (grok-mermaid/):
  - src/mermaid.rs: Core renderer (copied from xai-org/grok-build under Apache-2.0)
  - src/lib.rs: Safe Rust entry points (render_plain, render_html) and
    WebAssembly FFI surface
  - src/shim.rs: Minimal stand-ins for ratatui types (Style, Modifier, Span, Line)
    to avoid pulling in the full ratatui dependency
  - Cargo.toml: Package configuration for wasm32 target
  - build_wasm.sh: Build script to compile to WebAssembly

Web UI (grok-mermaid.html):
  - Interactive playground with live rendering
  - Example buttons for quick testing
  - Syntax highlighting and error display
  - Styled output with CSS classes mirroring the original TUI theme (b for
    border, n for node text, e for edge, el for edge label, t for title, i
    for italic)
  - Copy-to-clipboard functionality

Testing (tests/test_grok_mermaid.py):
  - Playwright tests validating rendering via the WebAssembly module
  - Tests for initial render, example loading, and error handling

Build artifacts:
  - grok-mermaid.wasm: Compiled WebAssembly module
  - LICENSE: Apache-2.0 license (matching source)
  - README.md: Documentation on the origin and rebuild process
```

Demo link included in the PR: `https://claude-mermaid-unicode-wasm.tools-b1q.pages.dev/grok-mermaid`.
The PR body also links a Claude.ai session at `https://claude.ai/code/session_01NHbXcjun9Rg1yn55N4P497`
(not independently fetched for this extraction — requires Claude.ai authentication).

### Original Rust module doc comment (verbatim, from xai-org/grok-build, mermaid.rs, commit `b189869b7755d2b482969acf6c92da3ecfeffd36`)

```rust
//! Self-contained terminal renderer for Mermaid diagrams.
//!
//! Renders `graph`/`flowchart`, `sequenceDiagram`, and `stateDiagram` blocks
//! as Unicode box-drawing art; unsupported diagram types fall back to the raw
//! source in a framed box.
```

### Screenshot description (alt text, verbatim, from simonwillison.net/2026/Jul/16/grok-mermaid/)

```
Screenshot of a Mermaid diagram editor showing source code and rendered flowchart.
The code reads: graph TD Start[Request received] --> Auth{Authenticated?}
Auth -->|yes| Rate{Rate limit OK?} Auth -->|no| R401[401 Unauthorized]
Rate -->|yes| H(Handle request) Rate -->|no| R429[429 Too Many Requests]
H -.-> Log[Audit log] H ==> Resp[200 OK]. Below the code are controls labeled
Max width: Fit output panel, Copy as text, and Copy link to this diagram. The
rendered flowchart on a dark background flows top-down: Request received leads
to Authenticated?, which branches yes to Rate limit OK? and no to 401
Unauthorized. Rate limit OK? branches yes to Handle request and no to 429 Too
Many Requests. Handle request connects with a dotted arrow to Audit log and a
thick arrow to 200 OK.
```

### Grok Build codebase scale comparison (from simonwillison.net/2026/Jul/15/grok-build/)

```
Grok Build (xai-org/grok-build):    844,530 lines of Rust (~3% vendored)
openai/codex:                       950,933 lines of Rust
(measured with Willison's SLOCCount tool, excluding whitespace and comments)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-servo-crate-exploration.md` Claim 1 and Claim 5: both notes
    document Claude Code (CLI in that case, "for web" here) taking a loose, one-sentence
    goal against an unfamiliar Rust codebase and returning a working artifact in one
    session without a detailed spec. This note adds a distinct sub-pattern: the source
    material here is working, already-functional code being *extracted and re-targeted*
    (native TUI → WASM), not a fresh crate being explored for capabilities from scratch.
  - `blog-simonwillison-opfs-pyodide.md` Claim 7 (single-file/self-contained
    architecture pattern for AI-generated browser-native tools) and
    `blog-simonwillison-pyodide-asgi-browser.md`: both document Willison using Claude
    Code for web to produce standalone, no-backend browser tools compiled from another
    language runtime (Python via Pyodide there, Rust via wasm32 here). This note adds a
    third instance of "AI agent + Claude Code for web → single-session browser/WASM
    port," now applied to Rust rather than Python, reinforcing this as a repeated
    Willison workflow across multiple language ecosystems.
  - `blog-simonwillison-liteparse-browser.md`: shares the general "port an existing
    open-source tool into a self-contained browser app via a single Claude Code session"
    shape, and Claim 7 here (Playwright tests for the WASM build) matches the
    "Playwright TDD" workflow habit already documented across that note as a Willison
    practice for browser-native tools.

- **Contradicts**: None identified. No existing corpus note makes claims about Rust→WASM
  porting, `ratatui` dependency stripping, or xAI's Grok Build codebase that conflict
  with this source.

- **Extends**:
  - `blog-simonwillison-servo-crate-exploration.md`: that note's Claim 2 documents Claude
    Code correctly recognizing that Servo itself was infeasible to compile to WASM (due
    to threads and SpiderMonkey) and pivoting to a WASM-compatible sub-crate instead. This
    note documents the same underlying skill in the opposite direction: rather than
    recognizing infeasibility and picking an already-portable alternative, the agent here
    made an *originally TUI-only* module WASM-portable by actively stripping its
    problematic dependency (`ratatui`) via a hand-written shim (Claim 4) — a more
    invasive, proactive resolution of a WASM-compatibility blocker than the
    pivot-to-something-else approach in the Servo case.
  - `blog-simonwillison-xai-anthropic-datacenter.md`: that note covers xAI's compute/
    datacenter arrangements; this note's Claim 8 adds a distinct, contemporaneous xAI
    data-handling incident (the Grok CLI directory-upload backlash) not covered there —
    together they broaden the corpus's xAI-specific coverage from infrastructure deals to
    a concrete agent-security failure and its remediation (open-sourcing under Apache 2.0).

- **Novel**:
  - **"Discover reusable code while reading a competitor AI lab's open-sourced agent
    internals for an unrelated reason, then port it via a different agent"** (Claims 2,
    3): no existing corpus source documents this specific discovery-then-port pathway.
    Prior porting examples in the corpus (LiteParse, OPFS/Pyodide harness) start from
    Willison deliberately seeking out a specific library to port; here the source material
    was found incidentally during unrelated codebase exploration.
  - **Minimal hand-written FFI as a deliberate alternative to `wasm-bindgen`** (Claim 5):
    not documented elsewhere in the corpus, which otherwise has no examples of Rust→WASM
    FFI design choices.
  - **Agent-authored dependency-stripping shim to satisfy a build-target constraint**
    (Claim 4): distinct from the "recognize infeasibility and pivot" pattern in the Servo
    note; this is "recognize infeasibility and resolve it by reimplementing the narrow
    dependency surface," a more proactive failure-resolution mode not seen before in this
    corpus.
  - **Concrete xAI Grok CLI directory-exfiltration incident and its Apache-2.0
    open-sourcing remediation** (Claim 8): first corpus documentation of this specific
    incident.
  - **Grok Build vs. codex Rust line-count comparison** (Claim 9): first corpus data
    point comparing the raw codebase scale of two competing terminal coding agents.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add this as a second, distinct instance (alongside
  `blog-simonwillison-servo-crate-exploration.md`) of the "give the agent a rough goal
  against unfamiliar code, not a detailed spec" pattern — but note the important
  variant here: the practitioner did not go looking for a library to port; the porting
  candidate was noticed incidentally while reading another AI-native project's source for
  an unrelated purpose (auditing data-handling behavior). Recommend the guide explicitly
  name "read other AI-native agents' open-sourced internals; when you spot a reusable,
  self-contained component, a single prompt can often extract and re-target it" as a
  distinct daily-workflow habit, separate from "deliberately explore a new library."
- **Chapter 02 (Harness Engineering)**: Claim 3's prompt is a compact, reusable template
  for cross-runtime porting tasks: name the source location, name the target constraint
  (independent of its parent codebase; compiled to a specific new target), name the
  deliverable format (a single HTML playground with examples), and explicitly require
  license handling when copying code from another project. Claims 4 and 5 (the `ratatui`
  shim and the hand-rolled WASM FFI) are worth citing as evidence that, left
  unconstrained on *how* to solve a dependency/target-compatibility problem, Claude Code
  for web chose a proportionate, minimal-surface solution over either a heavier
  standard tool (`wasm-bindgen`) or a wholesale dependency compile — reinforcing existing
  guide advice (if any) that agents given latitude on implementation approach for a
  narrowly-scoped extraction task tend toward minimal, targeted solutions rather than
  maximal ones.
- **Chapter 06 (Security & Threat Model)**: Claim 8 (the Grok CLI directory-upload
  incident) is a concrete, named, dated example of an agent tool with broad filesystem
  access exfiltrating data via an undisclosed cloud-upload path, and of the remediation
  (disable the feature, delete retained data, open-source the code for trust recovery).
  Worth adding as a citable incident if the chapter discusses agent filesystem-access
  scope or telemetry/data-retention transparency, independent of this note's main
  mermaid-porting subject.

## Extraction Notes

- The blog post itself is very short (~90 words); the two linked pages that carry the
  substantive content — the GitHub PR (`simonw/tools#293`) and the prior-day companion
  post (`simonwillison.net/2026/Jul/15/grok-build/`) — were both read in full via raw
  HTML/`gh api` rather than relying on WebFetch's summarizer, so that every quote above
  could be checked character-for-character against source text. A third linked page (the
  raw `mermaid.rs` source file at the pinned commit) was also fetched in full to verify
  the module doc comment quoted in Concrete Artifacts and to check the diagram-type
  discrepancy noted in Claim 1. A fourth link — the live tool itself
  (`tools.simonwillison.net/grok-mermaid`) — was fetched but is a WASM application shell
  with no extractable prose content beyond what the screenshot alt text already captures.
  The fifth link (the Claude.ai session transcript linked from the PR body) was not
  followed: it requires Claude.ai authentication and is outside what an unauthenticated
  fetch can retrieve; this is noted in Concrete Artifacts rather than silently omitted.
- **Diagram-type discrepancy between the module's doc comment and its actual behavior**:
  the Rust module's own top-of-file doc comment (quoted in Concrete Artifacts) states it
  renders "graph/flowchart, sequenceDiagram, and stateDiagram" blocks, but the blog post's
  tool description (Claim 1) states the shipped tool also supports class and ER diagrams,
  and reading the full `mermaid.rs` source confirms `parse_class` and `parse_er` functions
  exist and are wired into the render dispatch. This is a minor inconsistency in xAI's
  original source documentation (undercounting its own module's capability), not a
  contradiction between sources worth filing under MINER.md §4a — it doesn't affect any
  existing guide claim, and both "sides" originate from the same underlying code rather
  than being competing claims about AI-native engineering practice.
- The Prospector filed two triage comments on this issue with overlapping but not
  identical framing (first: "medium" novelty, chapters Ch01/Ch02; second: "high" novelty,
  same chapters). This note follows the more detailed second assessment's chapter
  targeting; both agree on Ch01/Ch02 relevance.
- No contradictions with existing corpus notes were identified; no contradiction issue
  was filed per MINER.md §4a.
