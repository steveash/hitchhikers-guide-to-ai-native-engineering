---
source_url: https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/
source_type: blog-post
title: "Cloudflare Python Workers are now generally available"
author: Simon Willison
date_published: 2026-09-21
date_extracted: 2026-09-28
last_checked: 2026-09-28
status: current
confidence_overall: settled
issue: "#3764"
---

# Cloudflare Python Workers are now generally available

> Simon Willison's linkblog commentary on Cloudflare's GA announcement for Python
> Workers, which documents a production-grade server-side deployment target for
> Pyodide-compiled Python: full framework support (FastAPI/Django/Flask), database
> access via Hyperdrive, AI/ML library support (openai, langchain, mcp), and a
> documented `multiprocessing`/`threading` limitation inherited from the WebAssembly VM.

## Source Context

- **Type**: blog-post — Simon Willison's linkblog entry, September 21, 2026. This is a
  short commentary post (a handful of sentences) that links to Cloudflare's own GA
  announcement at `blog.cloudflare.com/python-workers-ga/` (authored by Dominik Picheta)
  as the primary technical source. Willison adds his own framing (why the implementation
  is "neat") and one detail not emphasized in Cloudflare's post: the local development
  tooling. Both the linkblog entry and the linked Cloudflare announcement were read for
  this extraction, plus Cloudflare's `developers.cloudflare.com/workers/languages/python/`
  overview page and its `.../python/stdlib/` sub-page for the standard-library exclusion
  list Willison references as "documented here."
- **Author credibility**: Simon Willison is the creator of Django and Datasette, author
  of the `llm` CLI, and a designated `trusted-feed` source in this repo. He has an
  established practitioner history with Pyodide/WebAssembly Python (see
  `blog-simonwillison-pyodide-asgi-browser.md`, `blog-simonwillison-wasm-wheels-pypi.md`)
  — this is a domain he has hands-on familiarity with, not a topic he is encountering
  cold. He has no Cloudflare affiliation. The underlying technical claims about GA scope,
  code examples, and limitations originate from Cloudflare's own engineering blog post
  (vendor-authored, not independently verified by Willison) and Cloudflare's own docs
  site, which is consistent with how Willison's linkblog format generally works: his own
  commentary is anecdotal/interpretive, the linked vendor content is the primary source.
- **Scope**: Covers the Python Workers GA milestone, its Pyodide/WebAssembly/workerd
  implementation, the `multiprocessing`/`threading` limitation, local dev tooling
  (pywrangler/workers-py), the GA release's simplified type-conversion for Cloudflare
  service bindings, new database driver support via Hyperdrive, AI/ML library support,
  and Cloudflare's role in PEP 783. Does NOT cover: pricing, request-per-second or
  cold-start performance benchmarks, bundle-size limits, or a comparison against other
  serverless Python platforms (AWS Lambda, Vercel Functions, etc.) — none of these are
  addressed in either Willison's post or Cloudflare's announcement.

## Extracted Claims

### Claim 1: Python Workers has reached general availability after a two-year preview, and Cloudflare now treats Python as "a first-class, fully supported language on the Cloudflare Developer Platform"

- **Evidence**: Cloudflare's own GA announcement blog post states this as the headline
  claim. Willison's post references the "two years ago" preview launch as context.
- **Confidence**: settled (vendor GA announcement; the preview-to-GA transition is a
  concrete, checkable product-status claim)
- **Quote**: "a first-class, fully supported language on the Cloudflare Developer
  Platform"
- **Our assessment**: GA status matters for guide purposes because it changes the risk
  calculus for recommending this platform: a preview feature is not something to build
  production agent infrastructure on, while a GA feature vendor-committed to support is.
  This is the key fact that elevates Cloudflare Python Workers from "interesting
  experiment" to "viable edge-deployment target worth evaluating."

### Claim 2: Python Workers execute Python compiled to WebAssembly via Pyodide, running inside Cloudflare's V8-based `workerd` runtime

- **Evidence**: Willison states this directly as his own technical summary of how the
  platform works, and it is consistent with Cloudflare's own architecture documentation.
- **Confidence**: settled (stated directly by both the vendor and an independent
  practitioner with Pyodide expertise)
- **Quote**: "Cloudflare are running Python compiled to WebAssembly via Pyodide in their
  V8-based workerd runtime."
- **Our assessment**: This confirms Cloudflare did not build a bespoke Python-to-WASM
  toolchain — they adopted Pyodide, the same CPython-in-WebAssembly distribution
  Willison has documented extensively in browser contexts (`blog-simonwillison-pyodide-asgi-browser.md`,
  `blog-simonwillison-wasm-wheels-pypi.md`, `blog-simonwillison-opfs-pyodide.md`). This
  means constraints and ecosystem developments documented for browser-side Pyodide
  (e.g., the PEP 783 WASM-wheel distribution mechanism) apply directly to Cloudflare's
  server-side Python Workers as well — they share the same underlying runtime.

### Claim 3: `multiprocessing` and `threading` are non-functional in Python Workers because of WebAssembly VM limitations, though the modules can still be imported

- **Evidence**: Willison quotes Cloudflare's documented limitations directly. Cloudflare's
  own `developers.cloudflare.com/workers/languages/python/stdlib/` page independently
  corroborates this, stating the same two modules by name as non-functional (alongside a
  separate list of stdlib modules excluded entirely: curses, dbm, fcntl, tkinter, venv,
  winreg, and others).
- **Confidence**: settled (stated in both the vendor announcement and the vendor's own
  reference documentation, using nearly identical language)
- **Quote**: "This comes with some limitations, documented here - most notably both
  `multiprocessing` and `threading` are non-functional in the WebAssembly VM."
- **Our assessment**: This is the load-bearing constraint for guide purposes. Any Python
  agent code, tool, or backend service that relies on thread-based concurrency (thread
  pools, `concurrent.futures.ThreadPoolExecutor`, background threads) or process-based
  parallelism cannot be deployed to Python Workers without rewriting to async/single-
  threaded patterns. This directly corroborates and generalizes
  `blog-simonwillison-pyodide-asgi-browser.md` Claim 6, which found the same threading
  constraint in browser-side Pyodide (Datasette required `num_sql_threads=0` to run
  there) — confirming the constraint is a property of Pyodide/WebAssembly itself, not
  specific to the browser deployment context.

### Claim 4: The local development tool `pywrangler` (distributed on PyPI as `workers-py`) runs a full local simulation of the Cloudflare stack, executing Python code via Pyodide in WebAssembly in V8, using a 123MB `workerd` binary

- **Evidence**: Willison describes this from direct first-person use, including the exact
  local file path where the binary landed on his machine.
- **Confidence**: settled (first-person practitioner account, specific enough — exact
  binary size and file path — to indicate direct verification rather than paraphrase of
  marketing copy)
- **Quote**: "One particularly interesting detail of this is the local development
  environment story - their pywrangler development tool (confusingly packaged as
  workers-py on PyPI) runs a full local simulation of their stack, including executing
  code with Pyodide in WebAssembly in V8 in a 123MB `workerd` binary, which for me ended
  up in `node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd`."
- **Our assessment**: The naming mismatch (`pywrangler` the tool vs. `workers-py` the
  PyPI package) is a real practitioner friction point worth flagging in the guide as a
  "gotcha" for anyone setting this up. More substantively, the fact that local dev runs
  the *same* WebAssembly execution path as production (Pyodide-in-WASM-in-V8, not a
  native-Python shim) means local testing should reliably surface the `multiprocessing`/
  `threading` limitation (Claim 3) and other WASM-specific behavior before deployment,
  rather than only failing in production. Cloudflare's own docs page separately confirms
  the toolchain: `uv run pywrangler dev` for local dev and `uv run pywrangler deploy` for
  deployment, with `uv` and Node.js as prerequisites.

### Claim 5: The GA release eliminated manual type-conversion glue code between Python values and Cloudflare service bindings (e.g., Queues) — a Python dict can now be sent directly, whereas previously it required explicit `pyodide.ffi.to_js()` conversion

- **Evidence**: Cloudflare's GA announcement shows the before/after code directly: the
  old pattern imported `to_js` from `pyodide.ffi` and `js`, then called
  `to_js({"key": "value"}, dict_converter=js.Object.fromEntries)`; the new pattern is
  `self.env.QUEUE.send({"key": "value"})`.
- **Confidence**: settled (direct before/after code comparison from the vendor's own
  announcement post)
- **Quote**: "sending a Python dictionary into a Cloudflare Queue required the following
  glue code to work" [followed by the `to_js`/`dict_converter` example, contrasted with
  the simplified GA-era call]
- **Our assessment**: This is a meaningful ergonomics improvement specific to Cloudflare's
  Python-JS FFI bridge (a bridge Cloudflare built on top of Pyodide's own FFI layer,
  `pyodide.ffi`), not a general Pyodide change. It matters for guide purposes as evidence
  that Cloudflare is investing in reducing Python-Workers-specific friction beyond simply
  running Pyodide unmodified — this is Cloudflare-specific integration work layered on
  top of the shared Pyodide runtime described in Claim 2.

### Claim 6: Python Workers now support PostgreSQL and MySQL via Hyperdrive, implemented by adding socket system-call support through the Workers connect API, which enables standard async database drivers (`aiomysql`, `asyncpg`) to function inside the WebAssembly sandbox

- **Evidence**: Cloudflare's GA announcement states this as a new GA-era capability,
  naming the specific drivers and the underlying mechanism (socket syscalls via the
  Workers connect API).
- **Confidence**: settled (stated directly in the vendor GA announcement, with named
  drivers as concrete evidence rather than a vague capability claim)
- **Quote**: (no direct quote captured verbatim for this claim's mechanism description;
  see paraphrase above — WebFetch summarized this section as: "The team implemented
  socket system calls using the Workers connect API, enabling standard database drivers
  like `aiomysql` and `asyncpg` to function properly within the WebAssembly sandbox.")
- **Our assessment**: Database connectivity is a binding constraint for most real backend
  services. Before this, a Pyodide/WASM sandbox with no socket support could not speak
  the wire protocols of PostgreSQL or MySQL, which would rule out most stateful Python
  backends. Adding socket syscalls via a Workers-specific `connect` API — rather than
  requiring an HTTP-based database proxy — means existing async database drivers work
  largely unmodified. This is a significant expansion of what "a real backend service"
  can mean on this platform, moving it from "stateless request handlers only" toward
  "general-purpose async Python backend."

### Claim 7: The same socket-support work that enabled database drivers also unblocked AI/ML ecosystem libraries including `openai`, `langchain`, and `mcp`, which were previously hindered by missing socket operations

- **Evidence**: Cloudflare's GA announcement names these three libraries specifically as
  now-supported, attributing their prior breakage to the same missing-socket-operations
  gap addressed in Claim 6.
- **Confidence**: settled (named specific packages in the vendor announcement, consistent
  with the socket-support mechanism described in Claim 6)
- **Quote**: (no direct quote captured verbatim; see paraphrase — WebFetch summarized:
  "The announcement highlights support for libraries including `openai`, `langchain`,
  and `mcp`. These were previously hindered by missing socket operations, which have now
  been addressed.")
- **Our assessment**: This is the claim most directly relevant to this guide's subject
  matter: Cloudflare Workers is now a viable deployment target specifically for the
  Python AI/agent tooling stack (OpenAI client library, LangChain, MCP), not just for
  generic Python web services. Combined with Claim 6 (database access) and framework
  support (Claim 9), this positions Python Workers as a candidate edge-deployment
  platform for a Python-based agent backend — one that needs an LLM API client, possibly
  MCP tool-server capability, and database access. The `threading`/`multiprocessing`
  limitation (Claim 3) remains the key constraint to design around for any such
  deployment.

### Claim 8: Cloudflare proposed PEP 783, which standardizes a platform for running Python in browser/WASM runtimes (the "PyEmscripten" platform), and it has been accepted

- **Evidence**: Cloudflare's GA announcement states Cloudflare's authorship role in PEP
  783 directly, per the WebFetch summary of that section of the post.
- **Confidence**: settled for PEP 783's existence and acceptance (independently
  corroborated by `blog-simonwillison-wasm-wheels-pypi.md`, which documents the PyPI
  warehouse implementation of PEP 783's `pyemscripten` platform tags); emerging for the
  specific claim that Cloudflare (rather than the Pyodide team generally) was the
  proposing party, since that attribution comes from Cloudflare's own self-authored
  announcement and was not cross-checked against the PEP's own authorship record.
- **Quote**: (no direct quote captured verbatim; see paraphrase — WebFetch summarized:
  Cloudflare "proposed and had accepted PEP 783, which 'standardizes a platform for
  running Python in the browser runtimes called PyEmscripten.'" The quoted fragment
  inside the summary — "standardizes a platform for running Python in the browser
  runtimes called PyEmscripten" — was reported as a direct quote by WebFetch but was
  not independently re-verified word-for-word against the source page in a second pass;
  treat with the same caution as other WebFetch-summarized quotes noted in Extraction
  Notes.)
- **Our assessment**: This connects directly to `blog-simonwillison-wasm-wheels-pypi.md`,
  which documents the *result* of PEP 783 (PyPI's `pyemscripten_*_wasm32` wheel tags,
  28 early-adopting packages as of June 2026) without attributing its origin to any
  specific party. This source adds the missing attribution: Cloudflare positions itself
  as a proposer of PEP 783, which — if accurate — means Cloudflare has a direct
  commercial interest in growing the WASM-wheel ecosystem, since every package that
  publishes a `pyemscripten` wheel becomes usable inside Python Workers as well as
  browser Pyodide.

### Claim 9: Python Workers support popular Python web frameworks (FastAPI, Django, Flask) via `workers.asgi` for async frameworks and `workers.wsgi` for synchronous ones, without requiring a separate web server process

- **Evidence**: Cloudflare's GA announcement and the `developers.cloudflare.com/workers/languages/python/`
  overview page both describe framework support; the overview page shows a minimal
  four-line Worker using `WorkerEntrypoint` and `Response` as the baseline pattern
  beneath the framework adapters.
- **Confidence**: settled (documented in both the GA announcement and Cloudflare's
  reference docs, with a concrete minimal code example)
- **Quote**: "Cloudflare Workers provides a first-class Python experience" (from the
  `developers.cloudflare.com/workers/languages/python/` overview page)
- **Our assessment**: This directly parallels the ASGI-bridge pattern Willison built
  himself for browser Pyodide (`blog-simonwillison-pyodide-asgi-browser.md`), except
  Cloudflare's version is a vendor-supported, GA, server-side equivalent: `workers.asgi`
  plays the role Willison's custom service-worker bridge played for FastAPI/Datasette in
  the browser. For teams already running ASGI Python services, this lowers the porting
  cost to Python Workers to "point the existing app at `workers.asgi`" rather than a
  rewrite — assuming the app doesn't hit the threading/multiprocessing wall (Claim 3).

### Claim 10: The Python Workers GA release team credited by name includes Gyeongjae Choi, Dominik Picheta, and Hood Chatham, with Picheta and Chatham identified as Pyodide core maintainers

- **Evidence**: Willison names these three people in his commentary as the release team,
  and characterizes Picheta and Chatham's role as Pyodide core maintainers.
- **Confidence**: anecdotal (single-source attribution from Willison's commentary; not
  independently cross-checked against a Cloudflare team page or the Pyodide project's own
  maintainer list)
- **Quote**: (no direct quote captured verbatim for this specific attribution sentence;
  WebFetch reported it as: "The release team includes Gyeongjae Choi, Dominik Picheta,
  and Hood Chatham—the latter two being Pyodide core maintainers, underscoring the
  collaboration with the Python community." Note: Cloudflare's GA blog post itself is
  attributed to "Dominik Picheta" as author per a separate WebFetch pass, which is at
  least partially consistent with this claim.)
- **Our assessment**: If accurate, Pyodide core maintainers working directly at
  Cloudflare (or in close collaboration with Cloudflare on this feature) explains why
  Python Workers tracks Pyodide's own release cadence and ecosystem developments (PEP
  783, WASM wheels) so closely rather than lagging behind as a downstream consumer. This
  is a credibility signal for treating Cloudflare's Pyodide integration as well-informed
  rather than a superficial wrapper, but the claim itself is thin (a name-drop in a short
  linkblog post) and should not be treated as more than anecdotal without further
  corroboration.

### Claim 11: Python Workers integrate with Cloudflare's platform services: D1, R2, Workers AI, Hyperdrive, Durable Objects, Queues, and Workflows

- **Evidence**: Cloudflare's GA announcement lists these integrations directly, and the
  `developers.cloudflare.com/workers/languages/python/` overview page independently
  confirms bindings to "KV, D1, Durable Objects, R2, Workers AI, and Vectorize."
- **Confidence**: settled (stated in both the GA announcement and the reference docs
  overview page, with substantial overlap between the two lists)
- **Quote**: (no direct quote captured verbatim; see paraphrase — WebFetch summarized:
  "Python Workers integrate with Cloudflare services including D1, R2, Workers AI,
  Hyperdrive, Durable Objects, Queues, and Workflows.")
- **Our assessment**: This is the platform-breadth claim: a Python Worker is not limited
  to stateless request/response handling — it can use Cloudflare's own object storage
  (R2), SQL database (D1), key-value store (KV, per the overview page), vector database
  (Vectorize), durable stateful actors (Durable Objects), async job orchestration
  (Workflows), and Cloudflare's own inference platform (Workers AI). Combined with
  Claims 6, 7, and 9, this is a reasonably complete platform for building a Python-based
  agent backend end-to-end on Cloudflare's infrastructure, provided the workload avoids
  threading/multiprocessing.

## Concrete Artifacts

### Old vs. new type-conversion code for Cloudflare service bindings (from Cloudflare's GA announcement, blog.cloudflare.com/python-workers-ga/)

```python
# OLD (pre-GA): manual conversion required to send a Python dict into a Cloudflare Queue
from pyodide.ffi import to_js
import js

self.env.QUEUE.send(to_js({"key": "value"}, dict_converter=js.Object.fromEntries))

# NEW (GA): direct dict passing, conversion handled internally by the runtime
self.env.QUEUE.send({"key": "value"})
```

### Minimal Python Worker (from developers.cloudflare.com/workers/languages/python/)

```python
from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response("Hello World!")
```

### Local dev / deploy commands (from developers.cloudflare.com/workers/languages/python/)

```bash
# Prerequisites: uv and Node.js installed
uv run pywrangler dev      # local development (full Pyodide/WASM/V8 simulation)
uv run pywrangler deploy   # deployment
```

### Python standard library exclusions and limitations (from developers.cloudflare.com/workers/languages/python/stdlib/)

```
Non-functional (importable but do not work — WebAssembly VM limitation):
  multiprocessing, threading

Completely unavailable:
  curses, dbm, ensurepip, fcntl, grp, idlelib, lib2to3, msvcrt, pwd,
  resource, syslog, termios, tkinter, turtle.py, turtledemo, venv,
  winreg, winsound

Unavailable due to a removed dependency:
  pty, tty  (both depend on termios, which is removed)

Limited functionality:
  decimal   — only the C implementation is available (compiled to WebAssembly)
  pydoc     — help messages for Python builtins are not available
  webbrowser — the original webbrowser module is not available
```

### Local dev tooling detail (from Willison's post, quoting his own first-person setup)

```
Tool name:        pywrangler
PyPI package name: workers-py   (name mismatch — tool name != package name)
Local binary:     workerd, ~123MB
Willison's local path (macOS/arm64):
  node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-pyodide-asgi-browser.md` Claim 6 ("pure-Python wheels and
    Pyodide-compatible packages work; C extensions or packages requiring OS threads do
    not"): This note's Claim 3 independently confirms the threading limitation from
    Cloudflare's own server-side Pyodide deployment, generalizing the constraint beyond
    the browser-specific context that note documented (Datasette's
    `num_sql_threads=0` workaround).
  - `blog-simonwillison-wasm-wheels-pypi.md` Claim 1 (PyPI's native WASM wheel support
    via PEP 783's `pyemscripten` platform tags): This note's Claim 8 references the same
    PEP 783 mechanism from the Cloudflare side, adding the (lightly-sourced) claim that
    Cloudflare itself proposed the PEP.

- **Extends**:
  - `blog-simonwillison-pyodide-asgi-browser.md`: That note documents a Willison-built,
    experimental, browser-only ASGI-over-Pyodide bridge with real limitations (no cookie
    auth, iframe hosting required, offline vendoring needed due to sandbox network
    restrictions). This note documents a vendor-supported, GA, server-side equivalent
    (`workers.asgi`/`workers.wsgi`) running on production infrastructure with database
    access, platform service bindings, and no browser-specific constraints (no iframe,
    no forbidden-header issues, no client-side vendoring requirement) — a materially
    more production-ready deployment path for the same underlying Pyodide runtime.
  - `blog-simonwillison-wasm-wheels-pypi.md`: That note covers the *distribution*
    mechanism (PyPI WASM wheels) that makes compiled Python dependencies available to
    any Pyodide-based runtime. This note shows a concrete, GA, production *consumer* of
    that mechanism (Cloudflare Python Workers), beyond the browser context that note
    focused on.
  - `blog-simonwillison-temporary-cloudflare-accounts.md`: That note documents a
    separate Cloudflare Workers feature (ephemeral deployment via `--temporary`) aimed
    at frictionless agent-driven deployment. Combined with this note, Cloudflare Workers
    now offers both zero-friction JS/general deployment (temporary accounts) and a
    GA Python-specific runtime with AI/ML library and database support — two
    complementary pieces of Cloudflare's pitch to AI-agent-driven development workflows.

- **Contradicts**: None identified. No existing corpus source makes claims about
  Cloudflare Python Workers' GA status, database support, or threading limitations that
  would conflict with the findings here.

- **Novel**:
  - **Server-side, GA, vendor-supported Pyodide deployment target**: No existing corpus
    source documents a production-grade, non-browser deployment path for Pyodide-compiled
    Python. All prior Pyodide coverage in the corpus (`pyodide-asgi-browser`,
    `wasm-wheels-pypi`, `opfs-pyodide`) is browser-context or distribution-mechanism
    focused.
  - **Database connectivity from a WASM Python sandbox via socket syscalls**: The
    Workers-connect-API-based socket support enabling `asyncpg`/`aiomysql` is new to the
    corpus — no prior source documents how (or whether) a WASM-sandboxed Python runtime
    can speak raw database wire protocols.
  - **AI/ML library support gated on socket operations**: The specific claim that
    `openai`, `langchain`, and `mcp` were blocked by missing socket support (not by
    Pyodide/WASM limitations generally) is a new, specific technical detail not
    documented elsewhere in the corpus.
  - **`multiprocessing`/`threading` non-functional in a *server-side* Pyodide runtime**:
    prior corpus coverage of this limitation (`pyodide-asgi-browser.md`) was in a browser
    context where the constraint might plausibly have been attributed to browser
    sandboxing specifically. This note shows the same limitation applies server-side,
    confirming it is intrinsic to Pyodide/WebAssembly rather than an artifact of the
    browser environment.
  - **`pywrangler`/`workers-py` naming mismatch and local-dev-mirrors-production
    architecture**: Not documented elsewhere in the corpus.

## Guide Impact

- **Chapter 04 (Context Engineering — Browser-Native / Edge-Native Python Deployment)**:
  The guide's coverage of Pyodide-based Python deployment (informed by
  `blog-simonwillison-pyodide-asgi-browser.md`) should distinguish two tiers: (1) the
  experimental, self-built, browser-only ASGI bridge pattern (static hosting, no
  backend, significant DIY constraints) and (2) Cloudflare Python Workers — a GA,
  vendor-supported, server-side deployment target with database access (Claim 6),
  platform service bindings (Claim 11), and native framework support (Claim 9). For teams
  evaluating whether to build the DIY browser pattern versus use a managed platform, this
  source is direct evidence that a managed option now exists and has reached GA. The
  shared constraint across both — `threading`/`multiprocessing` unavailable (Claim 3) —
  should be stated as a property of the underlying Pyodide/WASM runtime, not of either
  specific deployment context.

- **Chapter 02 (Harness Engineering — Edge Deployment Options for Python Agent
  Backends)**: Claims 6, 7, 9, and 11 together establish Cloudflare Python Workers as a
  candidate deployment target specifically for Python-based agent backends: it supports
  the `openai`/`langchain`/`mcp` stack, PostgreSQL/MySQL via async drivers, FastAPI/
  Django/Flask via ASGI/WSGI adapters, and Cloudflare's own platform primitives (D1, R2,
  KV, Durable Objects, Workflows, Workers AI). The guide should add this as an option
  alongside existing serverless/edge deployment coverage, with the explicit caveat that
  any thread-pool-based or multiprocessing-based concurrency pattern must be redesigned
  as async/single-threaded before it can run there.

- **Chapter 04 (Context Engineering — WASM Wheel Ecosystem)**: This source adds
  attribution context to `blog-simonwillison-wasm-wheels-pypi.md`'s coverage of PEP 783:
  Cloudflare claims a proposing role (Claim 8), which — combined with Cloudflare's own
  commercial interest in the WASM-wheel ecosystem's growth — is worth noting as context
  for why the ecosystem might continue to receive vendor investment beyond the Pyodide
  team's own efforts.

## Extraction Notes

- **Willison's post is very short** (five sentences of original commentary); the
  substantive technical content lives in the linked Cloudflare GA announcement
  (`blog.cloudflare.com/python-workers-ga/`, authored by Dominik Picheta) and
  Cloudflare's own reference documentation (`developers.cloudflare.com/workers/languages/python/`
  and its `stdlib/` sub-page). All three pages were fetched and read for this extraction,
  consistent with MINER.md's instruction to follow substantive linked pages (up to 5).
  The Hacker News discussion thread and the `github.com/cloudflare/workerd` and
  `pypi.org/project/workers-py/` links were also identified but not deeply followed —
  the PyPI page failed to load during a WebFetch attempt (returned a client-side loading
  error, not a paywall or 404), and the GitHub repo and HN thread were judged
  lower-priority than the two Cloudflare-owned pages that directly supported the claims
  above.
- **Quote verification caveat**: Quotes were extracted via multiple targeted WebFetch
  calls explicitly requesting verbatim text. WebFetch processes fetched content through
  a smaller model before returning it, which means quotes are best-effort rather than
  guaranteed character-for-character, especially for the Cloudflare blog post (where
  several claims — Claims 6, 7, 8, 11 — could not be pinned to a single verbatim sentence
  despite multiple targeted fetch attempts, and are marked accordingly with "(no direct
  quote captured verbatim)"). The Willison-authored quotes (Claims 1–4) came back
  consistently identical across separate fetch passes with different prompts, which
  increases confidence they are accurate; the Cloudflare-post quotes were less
  consistently reproducible verbatim and are treated with more caution, per Claim 8's
  explicit flag.
- **stdlib exclusion list cross-checked**: The `multiprocessing`/`threading` limitation
  (Claim 3) was independently confirmed on Cloudflare's separate `stdlib/` reference
  page using near-identical wording to Willison's quote of the GA announcement, which
  increases confidence in this specific claim beyond a single-source citation.
- **No contradictions found requiring a filed issue**: This source does not conflict
  with any existing source note; it extends and corroborates existing Pyodide-related
  notes rather than disputing them.
