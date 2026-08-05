---
source_url: https://simonwillison.net/2026/Jul/31/datasette-agent/
source_type: blog-post
title: "datasette-agent 0.4a0"
author: Simon Willison
date_published: 2026-07-31
date_extracted: 2026-08-05
last_checked: 2026-08-05
status: current
confidence_overall: emerging
issue: "#2495"
---

# datasette-agent 0.4a0

> Simon Willison's release of `await context.browser_task()` — a new Datasette
> Agent ToolContext method letting agent tools run agent-provided JavaScript
> directly in the user's browser rather than only server-side — which he
> immediately dogfooded in datasette-apps 0.2a0 to build `app_debug()`, a tool
> that opens an app invisibly in a hidden iframe and runs JavaScript against it
> to smoke-test the app the agent just generated.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release
  announcement format at simonwillison.net, posted 31st July 2026, tagged
  "datasette", "llm-tool-use", "datasette-agent"). The post itself is three
  sentences long. It links forward to a same-author companion release,
  datasette-apps 0.2a0 (simonwillison.net/2026/Aug/1/datasette-apps/, posted
  1st August 2026), which documents the first concrete use of the API
  announced in this post. Both pages were read for this extraction, per
  MINER.md §1's instruction to follow substantive linked pages.
- **Author credibility**: Simon Willison is the creator of Datasette and the
  primary developer of Datasette Agent and the datasette-apps plugin. This is
  first-party release documentation — authoritative for the API's existence,
  purpose, and (via the linked companion post) its first real usage. No vendor
  affiliation.
- **Scope**: Covers the introduction of `context.browser_task()` in
  datasette-agent 0.4a0, and its first application — the `app_debug()` and
  `app_list()` tools in datasette-apps 0.2a0. Does NOT cover: the
  `browser_task()` function signature, its parameters, how results are
  returned to the calling tool, error handling, timeout behavior, or any
  security review of running agent-provided JavaScript in the user's browser
  session (unlike the datasette-apps sandbox architecture note, this release
  post includes no explicit security discussion of the new capability).

## Extracted Claims

### Claim 1: datasette-agent 0.4a0 adds `await context.browser_task()`, a new ToolContext method that lets agent tools run code directly in the user's browser instead of only server-side
- **Evidence**: First-party release announcement from the tool's creator,
  describing the new method by name and its effect.
- **Confidence**: emerging (first-party alpha release; the mechanism is
  named and described in one sentence with no further technical detail —
  parameters, return values, and error semantics are not documented in this
  post)
- **Quote**: "New `await context.browser_task()` mechanism allowing agent tools to run code directly in the user's browser."
  *(Source: simonwillison.net/2026/Jul/31/datasette-agent/)*
- **Our assessment**: This is a genuine architectural shift, not an
  incremental feature. Every prior Datasette Agent tool capability in the
  corpus — `ask_user()`, `save_query`, `execute_write_sql`, the MicroPython
  WASM sandbox, the Fly Sprites remote sandbox — executes on the server. This
  is the first ToolContext method that moves execution to the client. It
  reframes what an "agent tool" can be: not just a function that computes a
  result and returns it, but a function that can reach into the user's live
  browser session and act on the rendered page.

### Claim 2: Willison frames `browser_task()` as specifically enabling plugins to provide tools that execute custom JavaScript in the user's browser
- **Evidence**: Author's own characterization of the capability's purpose,
  in the same release post.
- **Confidence**: emerging (first-party statement of design intent; no
  worked example of a plugin using it appears in this post itself)
- **Quote**: "This is an exciting new capability: it makes it easy for Datasette Agent plugins to provide tools that execute custom JavaScript _in the user's browser_."
  *(Source: simonwillison.net/2026/Jul/31/datasette-agent/)*
- **Our assessment**: The framing is plugin-first: this is presented as
  infrastructure for third-party tool authors, not a one-off feature for a
  single use case. Combined with the plugin extensibility pattern already
  documented in the corpus (`blog-simonwillison-datasette-agent.md` Claim 5),
  this extends the surface area plugin authors can build against from
  "server-side Python with mediated host functions" to "server-side Python
  plus arbitrary client-side JavaScript in the user's live session."

### Claim 3: Willison used `browser_task()` himself to add a debug loop to Datasette Apps, released the next day as datasette-apps 0.2a0
- **Evidence**: Author's direct statement in the release post, pointing to
  a same-author follow-up release as the first real usage of the API.
- **Confidence**: emerging (first-party statement; the referenced usage was
  independently verified by reading the linked datasette-apps 0.2a0 post,
  see Claims 4–6)
- **Quote**: "I used this to add a debug loop to Datasette Apps in datasette-apps 0.2a0."
  *(Source: simonwillison.net/2026/Jul/31/datasette-agent/)*
- **Our assessment**: A same-day-adjacent dogfood release (0.4a0 on July 31,
  the consuming release on August 1) is a stronger signal than an announced
  capability with no consumer — it shows the API was validated against a
  real use case before or immediately after publication, not left as a
  speculative primitive.

### Claim 4: datasette-apps 0.2a0 adds `app_debug()`, a tool that lets the agent open an app invisibly and test it using JavaScript, built directly on `browser_task()`
- **Evidence**: First-party release announcement for datasette-apps 0.2a0,
  explicitly naming `context.browser_task()` from datasette-agent 0.4a0 as
  the mechanism `app_debug()` is built on.
- **Confidence**: settled (first-party; the dependency on `browser_task()`
  is stated explicitly, not inferred)
- **Quote**: "New `app_debug()` tool allowing agent to open an app (invisibly) and test it using JavaScript."
  *(Source: simonwillison.net/2026/Aug/1/datasette-apps/)*
- **Our assessment**: This is the first concrete worked example of
  `browser_task()` in the corpus. It closes a loop that was previously
  one-directional: `blog-simonwillison-datasette-apps.md` documented
  Datasette Apps as a system for *hosting* LLM-generated HTML/JS
  applications; `app_debug()` is the agent *verifying its own generated
  app* by driving it in the browser after creating it. This is a
  self-check capability specific to UI code, which is otherwise hard to
  verify deterministically (unlike a lint pass or a unit test on typical
  backend code).

### Claim 5: `app_debug()` displays the app in a hidden, non-interactive iframe (`opacity: 0`, `pointer-events: none`) and runs agent-provided JavaScript inside that sandboxed iframe
- **Evidence**: First-party release documentation, giving the exact CSS
  properties used to hide the iframe and confirming it is the same
  sandboxed iframe used to host apps normally.
- **Confidence**: settled (first-party; specific, verifiable CSS values
  given, not a general description)
- **Quote**: "displaying the app in a `opacity: 0` iframe with `pointer-events: none` (so it can't be seen or interacted with)" and "agent-provided JavaScript inside that sandboxed iframe"
  *(Source: simonwillison.net/2026/Aug/1/datasette-apps/)*
- **Our assessment**: The debug iframe reuses the same sandboxed hosting
  architecture (iframe `sandbox` attribute + injected CSP) that
  `blog-simonwillison-datasette-apps.md` Claim 1 documents for normal app
  hosting — it is not a separate, less-restricted execution path built for
  testing convenience. Hiding it via `opacity: 0` / `pointer-events: none`
  rather than by not rendering it at all means the app still runs through
  its normal layout and rendering pipeline (so dimension measurements are
  real), while being invisible and non-interactive to the human user
  watching the page.

### Claim 6: `app_debug()` lets the agent smoke-test that the app is working and measure the dimensions of different elements
- **Evidence**: First-party release documentation describing the intended
  use cases for the tool.
- **Confidence**: emerging (first-party statement of capability; no
  worked example of the JavaScript the agent writes for this is given)
- **Quote**: "smoke test that the app is working and even do things like measure the dimensions of different elements"
  *(Source: simonwillison.net/2026/Aug/1/datasette-apps/)*
- **Our assessment**: "Smoke test that the app is working" and "measure
  dimensions of different elements" are two distinct verification classes:
  the first is functional (does it run without erroring, does it produce
  expected DOM state), the second is layout/visual (is an element rendered
  at a sane size). Both are checks a human reviewer would otherwise have to
  perform manually by opening the app and looking at it — `app_debug()`
  lets the agent close part of that verification loop itself before
  handing the app back to the user.

### Claim 7: datasette-apps 0.2a0 also adds `app_list()`, a tool for listing the apps the user has permission to edit, so the agent can edit them
- **Evidence**: First-party release documentation, describing the tool
  alongside `app_debug()` in the same release.
- **Confidence**: settled (first-party; stated plainly with no ambiguity)
- **Quote**: "New `app_list()` tool for listing apps the user has permission to edit, so the agent can edit them."
  *(Source: simonwillison.net/2026/Aug/1/datasette-apps/)*
- **Our assessment**: Unlike `app_debug()`, this tool is unrelated to
  `browser_task()` — it is a permission-scoped discovery tool (the agent
  needs to know what apps exist and what it's allowed to touch before it
  can edit one). Included here for completeness since it shipped in the
  same release read for Claims 4–6, but it does not extend the
  client-side-execution capability that is this source's main subject.

## Concrete Artifacts

### browser_task() capability summary (from simonwillison.net/2026/Jul/31/datasette-agent/)

```
New ToolContext method: await context.browser_task()
Effect: runs agent tool code in the user's browser (client-side),
        not server-side.
Stated purpose: makes it easy for Datasette Agent plugins to provide
        tools that execute custom JavaScript in the user's browser.
```

*Source: simonwillison.net/2026/Jul/31/datasette-agent/, 2026-07-31. No
function signature, parameters, or return-value description appear in the
post.*

### app_debug() mechanism (from simonwillison.net/2026/Aug/1/datasette-apps/)

```
Tool: app_debug() (datasette-apps 0.2a0)
Built on: context.browser_task() (datasette-agent 0.4a0)

Mechanism:
  1. App is rendered in the same sandboxed iframe used for normal hosting
  2. Iframe is styled: opacity: 0; pointer-events: none;
     -> invisible and non-interactive to the human user
  3. Agent-provided JavaScript executes inside that sandboxed iframe
  4. Agent can smoke-test app behavior and measure element dimensions

Companion tool in the same release:
  app_list() - lists apps the user has permission to edit
```

*Source: simonwillison.net/2026/Aug/1/datasette-apps/, 2026-08-01.*

## Cross-References

- **Extends**:
  - `blog-simonwillison-datasette-agent-askuser.md` Claim 1: "The `ask_user()`
    API enables agent tools to ask yes/no, multiple-choice, or free-text
    questions mid-execution via a `ToolContext` object declared as a
    `context` parameter." `browser_task()` is a new method on that same
    `ToolContext` object. The `context` parameter dependency-injection
    convention established for `ask_user()` in 0.2a0 is confirmed still
    live and being extended with new capabilities two releases later.
  - `blog-simonwillison-datasette-apps.md` Claim 1: "Datasette Apps run in
    `<iframe sandbox=\"allow-scripts allow-forms\">` combined with an
    injected Content Security Policy meta tag, creating defense-in-depth
    isolation." `app_debug()` (Claim 5 of this note) reuses that exact
    sandboxed iframe for a new purpose — automated, invisible testing
    rather than normal user-facing hosting. The security boundary
    documented in that note is the boundary `app_debug()`'s
    agent-provided JavaScript runs inside; this note adds no new
    isolation mechanism, it repurposes the existing one.
  - `blog-simonwillison-datasette-agent.md` Claim 6: "Three plugins shipped
    at launch — ... and datasette-agent-sprites (Fly Sprites code
    execution)." Together with `blog-simonwillison-datasette-agent-micropython.md`
    Claim 1 (local WASM Python sandbox), Datasette Agent's code-execution
    surface now spans three distinct contexts: a remote persistent cloud
    sandbox (Fly Sprites), a local embedded WASM sandbox (MicroPython),
    and — new in this source — the user's own live browser session
    (`browser_task()`). This is the first of the three that executes in a
    context the agent does not fully control end-to-end (the user's
    browser, with the user potentially still interacting with the page,
    versus a sandbox spun up solely for the agent).

- **Contradicts**: None identified. No existing corpus note makes claims
  about client-side/browser-side agent tool execution that would conflict
  with this source. No contradiction issue required.

- **Novel**:
  - **First corpus documentation of an agent tool capability that executes
    in the user's browser rather than server-side**: every prior
    code-execution or tool-execution pattern in the corpus (Fly Sprites,
    MicroPython WASM, `save_query`, `execute_write_sql`) runs on the
    server. `browser_task()` is architecturally distinct — it grants agent
    tools a foothold in the client, not just the server.
  - **First corpus documentation of an agent using a hidden iframe as an
    automated self-verification harness for its own generated UI code**:
    `app_debug()`'s opacity-0/pointer-events-none iframe technique is a
    specific, reusable pattern for letting an agent test rendered output
    it cannot otherwise verify deterministically (visual layout, DOM
    behavior) without a human opening the page.

## Guide Impact

- **Chapter 03 (Verification — Layer 1: Deterministic Tools)**: Add
  `app_debug()` as a concrete example of a deterministic, zero-human-attention
  verification tool for a class of output (LLM-generated browser UI code)
  that is otherwise hard to check automatically. The guide's existing Layer
  1 examples are backend-oriented (linters, pre-commit checks); this source
  provides a worked pattern for the visual/UI case: render invisibly, run
  agent-provided JS against the live DOM, check for errors and measure
  layout. Cite Claim 4 for the capability and Claim 5 for the specific
  hide-but-still-render technique (`opacity: 0; pointer-events: none;`
  inside the existing sandboxed iframe, rather than a separate headless
  renderer).

- **Chapter 06 (Security and Threat Model — tool boundary expansion)**: Add
  `browser_task()` as an example of a tool capability that expands the
  agent's boundary into a new execution context (the user's browser
  session) with no explicit security discussion in the source itself —
  worth flagging as a gap. Note that the one concrete use case documented
  (`app_debug()`) mitigates this by running inside the pre-existing
  sandboxed iframe from `blog-simonwillison-datasette-apps.md` rather than
  granting the agent a new, less-restricted execution surface. The guide
  should note this as the safer pattern: when adding client-side agent
  tool execution, route it through an existing security boundary rather
  than inventing a new one per tool.

## Extraction Notes

- **Primary source is extremely thin**: the datasette-agent 0.4a0 post is a
  three-sentence "beat." Full verbatim reproduction was declined by WebFetch
  on copyright grounds; five targeted extraction prompts were used instead,
  and cross-checked against each other for consistency (the same three
  substantive sentences were returned across all passes: the
  `browser_task()` mechanism sentence, the "exciting new capability"
  sentence, and the "I used this to add a debug loop" sentence). No code
  examples, function signature, or security discussion appear in this post.
- **Followed the linked datasette-apps 0.2a0 post per MINER.md §1**: the
  0.4a0 post explicitly points to this as the first real usage of
  `browser_task()`, and the Prospector's triage comment flagged it as a
  directly relevant downstream use case. It was read in full via targeted
  WebFetch passes; all Claim 4–7 quotes were obtained from
  simonwillison.net/2026/Aug/1/datasette-apps/ and are cited with that URL,
  distinct from the frontmatter `source_url` (the 0.4a0 post named in the
  issue). This mirrors the two-URL citation pattern used in
  `blog-simonwillison-datasette-agent-micropython.md` (release post +
  companion technical article).
  - The Aug 1 post has no separate GitHub issue in this repo's tracker as
    of extraction time; if the Prospector later files it as its own source,
    the two notes should cross-reference each other.
- **Cross-references verified**:
  - `blog-simonwillison-datasette-agent-askuser.md` Claim 1 confirmed at
    lines 42–57 of that note (document-order first `### Claim` heading):
    the `ToolContext` / `context` parameter dependency-injection pattern.
  - `blog-simonwillison-datasette-apps.md` Claim 1 confirmed at lines
    50–72 of that note (document-order first `### Claim` heading): the
    `<iframe sandbox="allow-scripts allow-forms">` + CSP defense-in-depth
    architecture.
  - `blog-simonwillison-datasette-agent.md` Claim 6 confirmed at lines
    131–149 of that note (document-order sixth `### Claim` heading):
    the three launch plugins including `datasette-agent-sprites` (Fly
    Sprites code execution).
  - `blog-simonwillison-datasette-agent-micropython.md` Claim 1 confirmed
    at lines 47–61 of that note (document-order first `### Claim`
    heading): the local WASM Python sandbox.
- **No contradictions filed**: no existing corpus note makes claims about
  client-side agent tool execution or browser-based agent self-verification
  that conflict with this source. No contradiction issue required.
- **Note on pre-screen history**: this issue's automated pre-screen
  rejected the source as a bare version announcement with no extractable
  claims. The human owner overrode that rejection with a `triaged:text`
  label and a Triage Assessment citing high novelty for the
  `context.browser_task()` API and its downstream use in datasette-apps
  0.2a0. This note bears that out: the primary post is indeed minimal, but
  the linked downstream release (Claims 4–7) supplies the substantive,
  concrete material the pre-screen missed by evaluating the 0.4a0 post in
  isolation.
