---
source_url: https://simonwillison.net/2026/May/30/pyodide-asgi-browser/
source_type: blog-post
title: "Running Python ASGI apps in the browser via Pyodide + a service worker"
author: Simon Willison
date_published: 2026-05-30
date_extracted: 2026-06-08
last_checked: 2026-06-08
status: current
confidence_overall: emerging
issue: "#1107"
---

# Running Python ASGI apps in the browser via Pyodide + a service worker

> Simon Willison documents a working AI-generated proof-of-concept (Claude Opus 4.8 via
> Claude Code for web) that runs complete Python ASGI apps entirely in the browser using
> Pyodide + a service worker — demonstrating that AI agents can solve non-trivial
> cross-layer infrastructure architecture problems, and providing a concrete novel deployment
> pattern that eliminates backend servers for compatible Python web apps.

## Source Context

- **Type**: blog-post (Simon Willison's short-form announcement post, May 30, 2026; the
  post links to a GitHub repository at `github.com/simonw/research/tree/main/pyodide-asgi-browser`
  containing the AI-generated code, working notes, README, and tests. Both the blog post and
  the GitHub repository were read in full for this extraction. The repository's README carries
  an explicit note: "This is an AI-generated research report. All text and code in this report
  was created by an LLM." The working notes (`notes.md`) provide detailed step-by-step
  reasoning from the Claude Opus 4.8 session.)
- **Author credibility**: Simon Willison is the creator of Django, creator of Datasette,
  author of the `llm` CLI, and one of the highest-signal independent LLM-tooling commentators.
  He publishes working demos with public GitHub repositories and live deployments. He maintains
  no vendor affiliation. He has a documented pattern of being candid about both capabilities
  and limitations of AI-assisted development. This post continues his practitioner series on
  using AI agents to build real infrastructure.
- **Scope**: Covers a specific research project: a proof-of-concept system for running Python
  ASGI web applications in the browser via Pyodide + service workers. Includes: architecture
  design decisions, key implementation constraints (SW statelessness, iframe requirement,
  forbidden headers), two working demos (FastAPI, Datasette 1.0a31), 27 passing tests, and
  Willison's stated plan to upgrade Datasette Lite. Does NOT cover: performance benchmarks,
  production deployment suitability, comparison to other browser-native Python approaches
  (e.g., Pyscript, Jupyter in the browser), or general Pyodide usage patterns.

## Extracted Claims

### Claim 1: Claude Opus 4.8, via Claude Code for web, designed and fully implemented a working service worker + Pyodide + ASGI bridge architecture in a single delegated session

- **Evidence**: Blog post directly states the delegation. The GitHub repository's README
  carries an explicit LLM-generated notice. The working notes (`notes.md`) read as a
  step-by-step AI reasoning log: environment probes, architecture decisions, debug traces,
  and test results — all consistent with a single AI agent session. The result includes 27
  passing unit and browser tests, two live demos, and a complete offline vendoring solution.
- **Confidence**: settled (blog post + GitHub repo README explicitly confirm AI authorship;
  live demos and test results confirm the implementation works)
- **Quote**: "This morning I set Claude Opus 4.8 the task (in Claude Code for web) of
  figuring out how to run Python ASGI apps in Pyodide using Service Workers instead"
- **Our assessment**: This is one of the strongest in-corpus examples of an AI agent solving
  a multi-layer infrastructure architecture problem without practitioner code authorship. The
  task was not "write this function" but "figure out an architecture for running Python ASGI
  in the browser using service workers." The agent chose the architecture (SW + iframe +
  MessageChannel bridge), discovered a browser sandbox networking constraint, vendored
  dependencies locally to solve it, implemented a TDD test suite, and produced working demos.
  The practitioner's role was task direction and demo validation, not code authorship.

### Claim 2: Running Python ASGI apps entirely in the browser via a service worker eliminates the need for a backend HTTP server for all dynamic content

- **Evidence**: The GitHub README and project summary both state this as the core result.
  The working demos (FastAPI and Datasette) serve links, form submissions, JSON APIs, and
  SQL queries entirely in-browser with no backend.
- **Confidence**: settled (working live demos; the GitHub `_summary.md` states "removing
  the need for a backend server except for static files")
- **Quote**: "run Python ASGI apps entirely in the browser using Pyodide and a dedicated
  service worker"
- **Our assessment**: The architectural significance is non-trivial: this pattern converts
  any compliant ASGI app into a static site that can be deployed on GitHub Pages (or any
  CDN) without server infrastructure. The tradeoffs (no persistent state, Pyodide startup
  latency, no multi-user, large bundle size with vendored wheels) are real, but the use
  case — interactive data tools, documentation, demos, single-user local apps — is a natural
  fit for AI-native tooling where tools.simonwillison.net-style single-purpose Python apps
  are the norm.

### Claim 3: The service worker approach solves a critical limitation of the Web Worker approach used in the original Datasette Lite: JavaScript in `<script>` tags was not executed

- **Evidence**: Willison explicitly identifies this as the motivation for the new approach.
  The original Datasette Lite (built four years earlier) used Web Workers, but that approach
  broke Datasette functionality because `<script>` tags in returned HTML would not execute.
  Service workers intercept at the fetch level rather than the navigation level, so the
  browser renders responses normally including executing inline JavaScript.
- **Confidence**: settled (author of both implementations; the constraint is a documented
  Web Worker limitation)
- **Quote**: "had the disadvantage that any JavaScript in `<script>` tags would not be
  executed - breaking some Datasette functionality"
- **Our assessment**: This is the key architectural reason service workers are necessary
  rather than Web Workers for this pattern. Web Workers intercept at the response-HTML level
  before browser rendering; service workers intercept at the fetch/response level and return
  a real `Response` object that the browser renders normally. Any ASGI app that returns HTML
  with `<script>` tags (virtually all Datasette-style apps) requires the service worker
  approach. The LiteParse browser port (`blog-simonwillison-liteparse-browser.md`) avoided
  this constraint because it was a pure single-page app with no server-rendered HTML.

### Claim 4: The architecture requires an iframe to host the Python app, to prevent page navigation from destroying the long-lived Pyodide Web Worker

- **Evidence**: The `notes.md` working notes document this as the core chicken-and-egg
  problem discovered during design. The shell page owns the long-lived Pyodide worker;
  if the user navigates within the app, the shell page itself would be replaced, killing
  the Python runtime. The iframe keeps Pyodide alive across in-app navigations.
- **Confidence**: settled (documented design decision in working notes; architecture
  is consistent with browser iframe isolation semantics)
- **Quote**: "Chicken-and-egg problem: the top page hosts the long-lived Pyodide worker,
  but if a navigation replaced that page we'd lose Pyodide. Solution: **iframe**."
  (from `notes.md`, Simon Willison / Claude Opus 4.8 working notes, github.com/simonw/research)
- **Our assessment**: The iframe requirement is an architectural constraint that cascades
  into several downstream issues: anti-clickjacking headers must be stripped (Claim 8),
  URL routing must bridge the iframe boundary, and the app must be designed for the
  `/app/` prefix. Any team implementing this pattern must account for the iframe as a
  first-class constraint, not a detail. The AI agent discovered this constraint independently
  and designed around it without practitioner direction.

### Claim 5: Service workers must not cache long-lived MessageChannel ports because they are terminated when idle; the bridge must use fresh `clients.matchAll()` lookups on every request

- **Evidence**: Documented in both `sw.js` (source code comment) and `notes.md` ("Bridge
  robustness: service worker restarts" section). The first implementation cached the port
  and failed; the fix was to redesign so the SW holds no long-lived state.
- **Confidence**: settled (browser spec constraint; documented with concrete failure mode
  and fix in working notes)
- **Quote**: "Service workers are terminated when idle, so we must NOT cache a long-lived
  MessageChannel port in worker memory — it would be lost on restart and later requests
  would hang."
  (from `sw.js`, github.com/simonw/research/blob/main/pyodide-asgi-browser/sw.js)
- **Our assessment**: This is a non-obvious browser behavior that the AI agent discovered
  through implementation and corrected. The failure mode is subtle: SW termination is not
  deterministic (the browser kills idle SWs at its discretion), so the bug would appear
  intermittently — specifically after periods of inactivity. The fix (stateless SW with
  per-request shell lookup) is a general pattern for any service-worker-brokered
  communication that must survive SW restarts.

### Claim 6: The ASGI protocol provides a framework-agnostic seam that allows any compliant Python ASGI app to be hosted in the browser bridge without framework-specific code changes

- **Evidence**: The bridge was tested with both FastAPI (a popular microframework) and
  Datasette (a complex, plugin-based ASGI app with SQL queries, static assets, full HTML
  rendering, and authentication). The notes.md states "Datasette is itself an ASGI app,
  so it drops into the same bridge."
- **Confidence**: settled (two distinct ASGI apps running on the same bridge code; 27 tests
  passing; live demos operational)
- **Quote**: "Datasette is itself an ASGI app, so it drops into the same bridge."
  (from `notes.md`, Simon Willison / Claude Opus 4.8 working notes, github.com/simonw/research)
- **Our assessment**: The ASGI protocol's clean scope/receive/send abstraction is what makes
  this generality possible. Any ASGI-compliant app — FastAPI, Starlette, Django ASGI,
  Datasette, Litestar — could be hosted in the browser with the same bridge code. The
  constraint is not the framework but the Python dependencies: pure-Python wheels and
  Pyodide-compatible packages work; C extensions or packages requiring OS threads do not
  (Datasette required `num_sql_threads=0`).

### Claim 7: Cookie-based authentication cannot round-trip through a service worker bridge because the `Cookie` header is a forbidden header; authentication must be implemented via a plugin or request-level hook

- **Evidence**: Documented in `notes.md` under "Log in as root (equiv. of `datasette --root`)".
  The forbidden-header restriction is a browser security specification. The workaround used
  was a Datasette plugin implementing `actor_from_request` to return root actor for every
  request.
- **Confidence**: settled (browser spec constraint; documented with implementation workaround)
- **Quote**: "a service worker cannot read the `Cookie` request header (forbidden header),
  so cookie-based sessions can't round-trip through this bridge."
  (from `notes.md`, Simon Willison / Claude Opus 4.8 working notes, github.com/simonw/research)
- **Our assessment**: This is a significant architectural limitation for apps that rely on
  session cookies for authentication (most web apps). The workaround — bypassing session
  management entirely with a direct actor hook — is acceptable for single-user local-tools
  use cases but not for multi-user or security-sensitive contexts. Teams building on this
  pattern should design authentication at the plugin/middleware level from the start, not
  assume cookie sessions will work.

### Claim 8: Anti-clickjacking response headers (`X-Frame-Options`, `CSP frame-ancestors`) must be stripped by the service worker for all responses, because the iframe requirement is an architectural constraint of the bridge, not a per-app concern

- **Evidence**: Documented in `notes.md`. Datasette's write pages set both
  `X-Frame-Options: DENY` and `Content-Security-Policy: frame-ancestors 'none'` which
  the browser enforced even for SW-synthesized responses. The fix (SW strips these headers
  from every app response) was chosen over per-app patches because the iframe is imposed
  by the bridge architecture, not by the app.
- **Confidence**: settled (implemented fix; principled rationale documented in working notes)
- **Quote**: "the iframe requirement is imposed by *our* architecture, so neutralising
  frame-busting belongs at the bridge for any hosted app, not per-app."
  (from `notes.md`, Simon Willison / Claude Opus 4.8 working notes, github.com/simonw/research)
- **Our assessment**: This is a general design principle for the ASGI browser bridge pattern:
  any concern imposed by the bridge architecture (iframe hosting, prefix routing, stateless
  SW) should be handled at the bridge layer, not patched app-by-app. This makes the bridge
  reusable across ASGI apps. The same principle would apply to other headers that conflict
  with the iframe constraint (e.g., Strict-Transport-Security in certain configurations).

### Claim 9: Running ASGI apps under a custom `root_path` prefix in the browser bridge exposes URL-handling bugs in apps that assume certain path patterns, turning the browser bridge into a correctness test for app URL generation

- **Evidence**: Two Datasette bugs were discovered by running it through the browser bridge:
  (1) `/-/jump` navigation endpoint was not prefixed with `base_url` (hardcoded in template),
  causing SW passthrough; (2) export links had `base_url` applied twice (once in `request.path`,
  once by `urls.path()`), producing `/app/app/demo/items.json` → 404. Both are genuine
  Datasette bugs that would not appear in normal deployment.
- **Confidence**: settled (two specific bugs documented with root causes and fixes in working notes)
- **Quote**: "Genuine a Datasette base_url bug; fix upstream."
  (from `notes.md`, Simon Willison / Claude Opus 4.8 working notes, github.com/simonw/research)
- **Our assessment**: This is a practically useful side-effect of the browser bridge pattern:
  the `root_path`/`base_url` constraint is a stricter-than-usual test for URL generation
  correctness. Apps that pass the browser bridge's URL tests likely have correct URL
  generation for reverse-proxy / sub-path deployment scenarios as well. For teams working
  on ASGI apps: running in the browser bridge may surface base_url handling bugs that would
  otherwise only appear in staging or production sub-path deployments.

### Claim 10: Willison explicitly states he has not fully understood the AI-generated implementation and plans to study it before integrating it into Datasette Lite — another documented instance of the agentic-engineering/vibe-coding blur

- **Evidence**: Direct quote from the blog post. Willison is the person who delegated the
  task and validated the working demos, but by his own admission has not yet grasped how
  the implementation works. This mirrors the vibe-coding convergence he documented in
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1.
- **Confidence**: settled (direct quote from the practitioner)
- **Quote**: "I'm still getting my head around exactly how it works, but once I've done
  that I plan to upgrade Datasette Lite itself."
- **Our assessment**: This is the third in-corpus Willison example of shipping working
  infrastructure without having reviewed the underlying code (after LiteParse's browser
  port and the vibe-coding post itself). For the guide: this pattern — task direction +
  demo validation without code review — is now a stable Willison workflow for browser-native
  static apps with near-zero blast radius. The common thread is the static deployment
  condition: GitHub Pages, no backend, no user data. The forthcoming Datasette Lite
  integration will be the test: Datasette Lite is a production-facing tool, which may
  require the deeper code understanding Willison says he's deferring.

### Claim 11: The vendoring constraint (Pyodide + Python wheels must be served locally) can be forced by browser sandbox network restrictions, making offline-capable deployment a byproduct of the development environment limitation

- **Evidence**: The `notes.md` documents the development environment had no outbound
  network from the browser sandbox (while the host did), forcing local vendoring.
  The `vendor.py` script downloads the full Pyodide runtime + dependency closure for
  local serving. The result is an offline-capable deployment.
- **Confidence**: settled (documented in working notes with specific failure symptom
  and fix)
- **Quote**: "Outbound network OK to `cdn.jsdelivr.net` (Pyodide) and `pypi.org` (micropip).
  [...] the browser sandbox has no outbound network even though the host did"
  (from `notes.md`, Simon Willison / Claude Opus 4.8 working notes, github.com/simonw/research)
- **Our assessment**: The development-environment constraint (browser can't reach CDN)
  forced a solution (local vendoring) that turns out to be a deployment advantage (fully
  offline-capable app). This is a recurring pattern in constrained-environment AI development:
  the AI agent adapted to the constraint rather than failing. For practitioners: vendoring
  Pyodide and wheels locally is also the right default for production browser-native apps
  that need reliability (CDN availability, package version stability).

## Concrete Artifacts

### Architecture diagram — request flow (from GitHub README, github.com/simonw/research)

```
Browser tab
┌──────────────────────────────────────────────────────────────────────--──┐
│  Shell page  (index.html + bootstrap.js)                                 │
│    • registers the service worker                                        │
│    • starts the long-lived Pyodide Web Worker                            │
│    • brokers each captured request from the SW to the worker             │
│    • shows the app in an <iframe src="/app/">                            │
│                                                                          │
│   ┌─────────────────┐   postMessage + reply port   ┌──────────────────┐  │
│   │  Service worker │  ───────────────────────────>│  Shell (window)  │  │
│   │  (sw.js)        │   (SW finds the shell via    │   ──┐            │  │
│   │  intercepts     │    clients.matchAll each     │     │ MessageChan│  │
│   │  fetch() for    │<──────────────────────────── │   <─┘ to worker  │  │
│   │  /app/*         │       request response       └────────┬─────────┘  │
│   └─────────────────┘                                       v            │
│            ▲  intercepts navigations / forms / ┌──────────────────────┐  │
│            │  fetch from the iframe            │  Web Worker          │  │
│   ┌────────┴───────────────────────────────┐   │  Pyodide + FastAPI   │  │
│   │  <iframe src="/app/">  the FastAPI app │   │  + ASGIBridge        │  │
│   └────────────────────────────────────────┘   └──────────────────────┘  │
└───────────────────────────────────────────────────────────────────────--─┘
```

*Source: github.com/simonw/research/blob/main/pyodide-asgi-browser/README.md*

### Request flow (4 steps, from README)

```
1. User clicks link / submits form / JS calls fetch() inside the /app/ iframe.
2. Service worker (sw.js) intercepts the fetch event. Serializes
   {method, url, headers, body}, locates shell window via clients.matchAll(),
   posts it with one-shot reply port; other requests fall through to network.
3. Shell relays to Pyodide Web Worker (worker.js): builds ASGI http scope,
   drives the app via ASGIBridge, collects http.response.start /
   http.response.body messages.
4. Response {status, headers, body} flows back through shell to SW → real
   Response; browser renders including 303 redirects and inline <script>.
```

*Source: github.com/simonw/research/blob/main/pyodide-asgi-browser/README.md*

### Key design decisions (from README)

```
- Service worker + Pyodide in a dedicated Web Worker, with shell page brokering.
  SW holds NO long-lived state; on every request it finds shell fresh via
  clients.matchAll() and hands it a one-shot reply port. Survives SW restarts.

- <iframe> hosts the app. Shell owns the long-lived Pyodide worker; iframe keeps
  Pyodide alive across in-app navigations (otherwise navigation kills the worker).

- App served under /app/ prefix using ASGI root_path mechanism. SW intercepts
  /app/*; everything else passes through. With scope["root_path"] = "/app",
  Starlette routes on un-prefixed path AND generated links include /app.

- FastAPI installed at runtime via micropip; Python source embedded inline
  in worker.js.
```

*Source: github.com/simonw/research/blob/main/pyodide-asgi-browser/README.md*

### Datasette-specific architecture notes (from notes.md)

```
Datasette is itself an ASGI app, so it drops into the same bridge.

- base_url="/app/" makes every generated link/static asset/API URL
  root-relative under /app/ — no extra root_path needed.
- num_sql_threads=0 required: Pyodide has no threads; run SQLite inline.
- Cookie header is forbidden for service workers → can't use Datasette's
  token-based auth; workaround: actor_from_request plugin returning root.
- CrossOriginProtectionMiddleware (1.0a CSRF) allows same-origin unsafe
  methods — both real browser same-origin fetch and header-less Python
  tests are accepted.
- Anti-clickjacking: SW strips X-Frame-Options + frame-ancestors CSP from
  every response. Rationale: iframe is bridge architecture, not app concern.
- hash-routing: bootstrap.js mirrors iframe path to parent #fragment;
  hashchange drives iframe from parent URL. Bookmarkable + back-button works.
```

*Source: notes.md, github.com/simonw/research/blob/main/pyodide-asgi-browser/notes.md*

### TDD approach (from notes.md)

```
TDD plan:
1. Pure-Python unit tests of the ASGI bridge harness (scope building,
   receive/send, header/body round-trip) — fast, no browser. RED then GREEN.
2. Playwright tests driving real Chromium: SW serves navigation HTML, form
   POST redirect, JSON fetch, and a page whose own inline JS does an
   intercepted fetch. RED then GREEN.

Total: 27 unit and browser tests, all passing.
```

*Source: notes.md, github.com/simonw/research/blob/main/pyodide-asgi-browser/notes.md*

### Two live demos (as of 2026-05-30)

```
FastAPI demo:   https://simonw.github.io/research/pyodide-asgi-browser/
                Links, form POST→303 redirect, JSON API, inline JS fetch()
                all served by Python ASGI in-browser.

Datasette demo: https://simonw.github.io/research/pyodide-asgi-browser/datasette.html
                Full Datasette 1.0a31 — database/table navigation, SQL,
                .json API, shareable URLs via hash routing.
```

*Source: blog post + GitHub README, github.com/simonw/research*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1 ("the boundary between
    vibe coding and responsible agentic engineering has begun to blur"): Claim 10 of this
    note is a concrete additional instance of that blur. Willison delegated the task, validated
    the demos, and explicitly states he hasn't understood the implementation yet. This is
    the third documented Willison example of shipping working browser-native infrastructure
    without reviewing the AI-generated code — the same pattern he names as troubling in
    the vibe-coding post.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 2 ("normalization of
    deviance: each successful unreviewed AI output increases false confidence"): The pattern
    here continues. Willison's LiteParse port (April 2026), the Datasette blog session (May
    2026), and now this Pyodide ASGI bridge (May 2026) are three successful unreviewed
    browser-native AI implementations in close succession. Each success makes the next
    unreviewed delegation more natural.
  - `blog-simonwillison-liteparse-browser.md` Claim 12 ("browser-native static apps with
    no server and no data transfer have 'almost non-existent' blast radius that makes vibe
    coding justifiable"): This post is another instance satisfying Willison's three
    conditions. The Pyodide ASGI browser pattern is a static GitHub Pages deployment with
    no backend and all processing in-browser — exactly the conditions under which Willison
    frames zero-review vibe coding as acceptable.

- **Extends**:
  - `blog-simonwillison-vibe-coding-agentic-engineering.md`: That post frames the vibe
    coding / agentic engineering blur theoretically. This post is a concrete case of the
    infrastructure-level delegation case that post anticipates — a complete, novel,
    non-trivial architecture designed and implemented by Claude Opus 4.8 with Willison
    directing and validating, not reviewing. The "still getting my head around how it works"
    admission is the practitioner-level confirmation of the blur Willison described in May.
  - `blog-simonwillison-liteparse-browser.md`: The LiteParse port showed AI-assisted
    porting of a Node.js library to a browser static app. This post extends that pattern to
    full Python ASGI web applications — a substantially more complex case (multi-component
    architecture, framework-agnostic bridge, service worker lifecycle management, TDD harness).
  - `blog-simonwillison-datasette-agent.md`: Datasette continues to evolve as a testbed
    for AI-assisted development patterns. The browser bridge adds a new deployment mode
    (fully in-browser, no server) that complements the AI agent mode (datasette-agent for
    LLM-driven SQL exploration). Both are Willison-directed, AI-built Datasette extensions.

- **Contradicts**: None identified. No existing corpus note makes claims about browser-based
  Python ASGI execution or the Pyodide + service worker pattern that would conflict with
  the findings here.

- **Novel**:
  - **First in-corpus documentation of a complete Python ASGI browser bridge pattern**:
    No existing source note documents the Pyodide + service worker architecture for running
    full ASGI apps in the browser. The LiteParse note covers browser-native JavaScript apps
    with Python preprocessing; this covers full Python ASGI apps serving all dynamic content.
  - **Iframe-as-ASGI-host design constraint**: The specific design insight (shell page owns
    Pyodide worker → app must be in iframe to survive navigation) is a non-obvious constraint
    with cascading architectural implications (forbidden headers, hash routing, prefix routing).
    No other corpus note documents this.
  - **Service worker statelessness as a reliability design principle**: The constraint that SW
    must not hold long-lived ports, with `clients.matchAll()` as the per-request lookup
    pattern, is a specific, transferable lesson for any service-worker-brokered communication
    architecture. No other corpus note documents this.
  - **Cookie-header forbidden in service workers**: The forbidden-header constraint on the
    `Cookie` header for service workers — and the authentication plugin workaround — is a
    concrete, surprising constraint not documented elsewhere in the corpus.
  - **ASGI bridge as a URL-correctness test**: The observation that running ASGI apps through
    a `root_path`-prefixed bridge surfaces URL-handling bugs (Claim 9) is a novel diagnostic
    use of the pattern not documented elsewhere.
  - **AI-generated research report format**: The GitHub repository's explicit "all text and
    code created by an LLM" README pattern is a novel in-corpus example of how AI-generated
    research can be packaged, attributed, and published as a public reference artifact.

## Guide Impact

- **Chapter 02 (Harness Engineering — Agentic Delegation for Infrastructure)**:
  Claim 1 is the strongest guide-facing finding: Claude Opus 4.8 designed and implemented
  a complete multi-component infrastructure architecture (SW + iframe + MessageChannel bridge
  + ASGI bridge + TDD harness + offline vendoring) from a single high-level task description.
  The guide should add this as a worked example of infrastructure-level task delegation:
  "AI agents can solve cross-layer architectural problems when given a specific goal,
  relevant constraints (use service workers), and a validation mechanism (working demo +
  tests). The practitioner's role is task direction and demo validation, not code authorship."
  The explicit "all code created by an LLM" attribution model is worth documenting as a
  citation practice for AI-generated components.

- **Chapter 00 (Principles — Blast-Radius-Conditioned Review)**:
  Claim 10 (Willison's "still getting my head around how it works") is the third in-corpus
  instance of the pattern documented in `blog-simonwillison-vibe-coding-agentic-engineering.md`
  Claim 2 (normalization of deviance). The guide's principles section should note: "The
  vibe coding / agentic blur is not theoretical — experienced practitioners are documenting
  it repeatedly in browser-native, static-hosting contexts. The pattern appears stable under
  the blast-radius conditions Willison identifies: static deployment, no backend, in-browser
  processing only. Outside those conditions, the guide should name the normalization-of-deviance
  risk explicitly."

- **Chapter 04 (Context Engineering — Browser-Native Python Deployment)**:
  Claims 2–9 together establish a new deployment pattern worth documenting in the guide:
  "Pyodide + service worker enables full Python ASGI apps as static browser deployments.
  Key constraints: iframe hosting, SW statelessness (no cached ports), cookie-header
  forbidden (no session auth), anti-clickjacking headers must be stripped at SW layer,
  `root_path` prefix required (surfaces URL-handling bugs in apps not designed for it).
  Use cases: single-user local tools, interactive demos, offline-capable data exploration
  tools. Not suitable for: multi-user apps, apps requiring persistent state, security-sensitive
  contexts."

- **Chapter 03 (Safety and Verification — AI-Generated Infrastructure Attribution)**:
  The GitHub repository's README attribution model ("all text and code created by an LLM")
  is worth recommending as a practice for AI-generated components in production or
  reference artifacts. The guide should address: when AI generates infrastructure code that
  will be published or reused, explicit LLM authorship attribution in the README helps
  future readers understand review expectations, contribution patterns, and maintenance
  responsibilities.

## Extraction Notes

- **Two source artifacts read**: The blog post (`simonwillison.net/2026/May/30/pyodide-asgi-browser/`)
  is a short announcement; the substantive content is in the GitHub repository
  (`github.com/simonw/research/tree/main/pyodide-asgi-browser`). Both were read. The GitHub
  repository was accessed via `gh api` (raw file contents via base64-decoded API response).
- **Quotes from the blog post**: All blog-post quotes were extracted via multiple targeted
  WebFetch requests. The WebFetch tool returns summaries by default; targeted prompts for
  specific sentences were used to recover verbatim text. All blog-post quotes are as reported
  by WebFetch in response to verbatim-quote requests.
- **Quotes from the GitHub repo**: Quotes from `notes.md`, `README.md`, and `sw.js` are
  verbatim from the raw file content retrieved via `gh api`. These are attributed in the
  source note with their GitHub file paths.
- **AI-generated notes.md**: The `notes.md` file in the repository was written by Claude
  Opus 4.8 during the session. It serves as a structured working-notes log: problem framing,
  design decisions, debugging traces, and implementation notes. It is a primary-source record
  of the AI agent's reasoning, not Willison's retrospective account.
- **Confidence set to `emerging`**: Two working demos and 27 tests provide good evidence
  that the implementation works. But the approach is genuinely novel (no prior production
  deployments documented), and Willison himself has not reviewed the implementation code.
  `emerging` better reflects the current state than `settled` (which would require broader
  validation) or `anecdotal` (which understates the working evidence).
- **No sub-pages beyond the 5 GitHub files read**: Read `README.md`, `notes.md`, `sw.js`,
  `_summary.md`, and the directory listing. Did not follow individual test files, `vendor.py`,
  or the worker JS files — the working notes and README captured the architectural substance.
- **Three Prospector triage comments**: Three separate triage assessments were filed (all
  by the repo owner). All three focused on the agentic engineering pattern and the browser
  ASGI pattern; all were synthesized into this note. The second and third comments
  corroborated the first and added detail on the Claude Opus 4.8 involvement and the
  relationship to existing Willison source notes.
