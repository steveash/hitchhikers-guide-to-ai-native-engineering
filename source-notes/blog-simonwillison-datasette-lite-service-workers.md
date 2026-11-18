---
source_url: https://simonwillison.net/2026/Nov/17/datasette-lite/
source_type: blog-post
title: "Running the full server-side Datasette Python app in the browser with service workers and Pyodide"
author: Simon Willison
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: emerging
issue: "#4787"
---

# Running the full server-side Datasette Python app in the browser with service workers and Pyodide

> Production follow-up to the May 2026 AI-generated spike: a service-worker + per-tab-session + Pyodide web worker architecture ships Datasette Lite as URL-addressable, zero-server preview and bug-repro environments, with a six-month agent-assisted spike-to-ship timeline.

## Source Context

- **Type**: blog-post
- **Author credibility**: Simon Willison, creator of Datasette and Datasette Lite (first launched 2022); long-running first-party practitioner of LLM-assisted development. Claims here are about his own shipped project.
- **Scope**: Covers the Datasette Lite rewrite architecture, URL parameters, the `?sqlite=` version picker with 163 WASM-built pysqlite3 wheels, and a short generalization to other Python apps. Weak AI-engineering angle: Claude models appear as build tools. Does not cover verification of the AI-generated code, tests, or how the rewrite was prompted.

## Extracted Claims

### Claim 1: The rewrite replaces the 2022 innerHTML hack with service-worker request interception, making JavaScript/CSS-dependent features work
- **Evidence**: Author's description of the old design (Pyodide web worker, simulated requests, HTML injected via innerHTML) and why it failed; the new version serves `/app/<session>/...` HTML, JS and CSS through the service worker. Demonstrated with the datasette-maplibre plugin demo URL.
- **Confidence**: emerging
- **Quote**: "any feature that used JavaScript failed to work, because script tags in innerHTML don’t execute, and the web worker tricks it used failed to load additional JavaScript or CSS files."
- **Our assessment**: Credible and specific; consistent with the May prototype note. Author-reported, no independent test.

### Claim 2: A random per-tab session ID prefix is needed so a shared service worker does not collapse all tabs onto one Datasette instance
- **Evidence**: Architecture explanation; example URLs with `/app/aa94e6851595/` prefix.
- **Confidence**: emerging
- **Quote**: "If it routed to a single instance of Datasette then every tab would share that underlying instance, no matter what plugins or other settings their URL attempted to configure."
- **Our assessment**: A clean, reusable design constraint for any "one SW per origin, many configured instances" browser app. New relative to the May note.

### Claim 3: Pyodide still needs a dedicated web worker because a service worker cannot hold state beyond about 30 seconds
- **Evidence**: Parenthetical architectural explanation; requests are relayed service worker → parent page → web worker.
- **Confidence**: emerging
- **Quote**: "We still need a web worker because Pyodide in a service worker would not be able to maintain state beyond around 30 seconds, depending on the browser."
- **Our assessment**: Plausible given service-worker lifecycle rules; stated without measurements ("depending on the browser"). Matches the May note's finding that service workers are terminated when idle (Claim 5 there).

### Claim 4: The result is claimed to be "almost indistinguishable" from the real server-side app and supports pinned refs, plugins, and data via URL
- **Evidence**: List of capabilities (any PyPI release, any GitHub commit/tag/branch, plugins from PyPI or wheel URLs, SQLite/JSON/CSV/SQL script loading); a worked URL decomposed parameter by parameter.
- **Confidence**: emerging
- **Quote**: "I’ve released a complete rewrite of Datasette Lite using service workers, and it’s now almost indistinguishable from the real server-side application."
- **Our assessment**: Qualitative self-assessment; no compatibility matrix. Cookie/auth limits noted in the May note presumably still apply but this post does not discuss them.

### Claim 5: URL-addressable environments are practical for linking to demos of work-in-progress features and bug reproductions without spinning up a server
- **Evidence**: A real Datasette issue on a pagination bug where the author compared the broken (`ref=1.0a42`) and fixed (`ref=1.0a43`) behavior via two Lite links.
- **Confidence**: anecdotal
- **Quote**: "makes this a fantastic tool for linking to demos of work-in-progress features or bug reproductions, without needing to spin up a full web server to serve that demo."
- **Our assessment**: A concrete, low-cost verification/communication pattern relevant to agent-produced PRs (reviewer clicks a link instead of checking out a branch). One real example, single author.

### Claim 6: The system went from AI research spike (May, Claude Opus 4.8) to production (November, Claude Fable 5.2) only once the author understood it well enough to ship confidently
- **Evidence**: Author's own timeline statement; also used Fable 5.2 to generate SVG explanatory diagrams embedded in the README.
- **Confidence**: anecdotal
- **Quote**: "It wasn’t until November (and Claude Fable 5.2) that I felt familiar enough with how it all works to confidently ship it to production!"
- **Our assessment**: Follows up Claim 10 of the May note (author had not yet understood the AI-generated implementation). Here the resolution: comprehension gating, over ~6 months, was the release criterion. Useful evidence for "understand before shipping" as an agentic-engineering norm, though it is one anecdote.

### Claim 7: Compiling an arbitrary Python version of SQLite as WASM wheels (163 versions) was done with agent help and enables version-pinned debugging in the browser
- **Evidence**: New repo `datasette/pysqlite3-wasm-wheels`; example wheel filename; `?sqlite=` parameter resolves, fetches and installs the wheel. A bonus comparison tool was also built with Fable 5.2.
- **Confidence**: emerging
- **Quote**: "datasette/pysqlite3-wasm-wheels is my new repository which contains WebAssembly compiled Python wheels for pysqlite3 for 163 different SQLite versions."
- **Our assessment**: Verifiable artifact (public repo). The post does not say how much of the wheel build was agent-done versus scripted; only the comparison tool is explicitly attributed to Fable 5.2. Note the post also says "87 further releases" since 3.25 and the issue's "over 100 versions" list item, so counts differ by context (163 wheels vs. Datasette-supported releases).

### Claim 8: Coding agents make compiling C/Rust extensions to Pyodide WASM routine, and PEP 783 makes publishing them possible
- **Evidence**: Assertion only, no transcript; links to the author's June WASM-wheels post by implication (PEP 783 date given as April 2026).
- **Confidence**: anecdotal
- **Quote**: "C and Rust extensions used to be a blocker for this kind of thing, but any good coding agent can compile those to Pyodide-compatible WebAssembly now."
- **Our assessment**: Broad generalization ("any good coding agent") backed only by the author's own experience with the SQLite wheels. Treat as a hypothesis worth testing.

### Claim 9: The pattern generalizes to almost any Python app as cheap preview environments, with databases beyond SQLite as the stated limit
- **Evidence**: Author's reasoning; no second app demonstrated.
- **Confidence**: anecdotal
- **Quote**: "One catch is databases. SQLite is no problem at all, but running PostgreSQL or MySQL in WebAssembly, while possible, is still a path less trodden."
- **Our assessment**: Honest limitation statement. Generalization to other apps is untested here, though the May note (Claim 6) argues ASGI is a framework-agnostic seam.

## Concrete Artifacts

URL scheme for session-routed requests (from the post, "How this works, using service workers"):

```
/app/aa94e6851595/ # the homepage (HTML)
/app/aa94e6851595/data/places # a table page (HTML)
/app/aa94e6851595/-/static/navigation-search.js # (JavaScript)
/app/aa94e6851595/-/static/app.css # (CSS)
```

Decomposed Datasette Lite URL (from the post):

```
https://lite.datasette.io/
  ?install=datasette-maplibre
  &url=https://.../demo.db
  &metadata=https://.../metadata.yml
  #/demo/capitals_and_countries%23map=0/4.2/180&color=continent
```

Bug-repro pair used in a Datasette issue (from the post):

```
https://lite.datasette.io/?ref=1.0a42&sql=https://gist.github.com/simonw/75ececf61d50e6e8d50f0c150150ee81#/data/scores?_size=2&_sort=score
https://lite.datasette.io/?ref=1.0a43&sql=https://gist.github.com/simonw/75ececf61d50e6e8d50f0c150150ee81#/data/scores?_size=2&_sort=score
```

Wheel naming (from the post):

```
pysqlite3-0.6.2-3.54.1-cp314-cp314-pyemscripten_2026_0_wasm32.whl
```

Request path: browser tab → iframe → service worker (one per origin) → parent page relay (keyed by session ID) → dedicated Pyodide web worker per tab.

## Cross-References

- **Corroborates**: `blog-simonwillison-pyodide-asgi-browser.md` Claim 3 (service worker fixes the script-tag limitation of the Web Worker approach), Claim 4 (iframe plus long-lived Pyodide web worker), and Claim 5 (service workers are terminated when idle, so state must live elsewhere).
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-pyodide-asgi-browser.md` Claim 1 and Claim 10 (spike generated by Opus 4.8; author had not yet understood it) by recording the November production rewrite and the understanding-before-shipping outcome. `blog-simonwillison-wasm-wheels-pypi.md` Claim 1 and Claim 4 (PyPI WASM wheels via PEP 783 / pyemscripten tags) with a concrete 163-wheel use. `blog-simonwillison-opfs-pyodide.md` Claim 9 (investigate in a test harness before integrating into Datasette Lite) by showing the eventual integration.
- **Novel**: Per-tab random session prefix to multiplex a shared service worker; `?sqlite=` runtime SQLite version selection; URL-addressable pinned environments as bug-repro/PR-demo links; the claim that agents routinely compile C/Rust to Pyodide WASM. Related background only: `blog-simonwillison-datasette-agent-micropython.md` (WASM sandboxing for agents; different runtime, no direct claim overlap).

## Guide Impact

- **Ch03 (verification)**: Optional short example: for agent-built changes to Python web apps, a URL-addressable in-browser build (pinned ref plus data) lets reviewers see a before/after repro without a server (Claim 5). Single-author anecdote; label as emerging.
- **Ch01 (daily workflows)**: Possible one-line mention of linking to live demos from issues/PRs. Weak fit.
- **Agentic-engineering/comprehension sections**: Cite Claim 6 alongside the May note's Claim 10 as a spike-then-understand-then-ship timeline.
- No chapter currently covers browser-side Python runtimes; no structural change recommended.

## Extraction Notes

- Read the full post (fetched raw HTML and stripped tags); quotes copied verbatim from the extracted text. Did not follow the linked README/repos, since the post is self-contained and the triage asked for a narrow extraction.
- Triage comments differ on chapter placement (Ch01/Ch03 vs Ch02); placement above is a suggestion for the Smith.
- The post's AI-engineering content is thin, so confidence stays "emerging".
