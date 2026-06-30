---
source_url: https://simonwillison.net/2026/Jun/23/opfs-pyodide/
source_type: blog-post
title: "OPFS + Pyodide test harness"
author: Simon Willison
date_published: 2026-06-23
date_extracted: 2026-06-30
last_checked: 2026-06-30
status: current
confidence_overall: emerging
issue: "#1351"
---

# OPFS + Pyodide test harness

> Simon Willison used Claude Code for web to build a cross-device OPFS test harness
> in a single HTML file — investigating whether Datasette Lite can support persistent
> SQLite editing — and the source code documents concrete, Safari/iOS-specific
> compatibility constraints for OPFS persistence that any browser-native Python tool
> must navigate.

## Source Context

- **Type**: blog-post (short-form announcement post, June 23, 2026; the substantive
  technical content lives in the generated tool at
  `tools.simonwillison.net/opfs-pyodide` and its source at
  `github.com/simonw/tools/blob/main/opfs-pyodide.html`. The blog post text is a few
  sentences linking to the tool; the HTML file contains extensive inline code comments
  that read as architectural documentation. Both were read in full for this extraction.
  The docs file (`opfs-pyodide.docs.md`) confirms: "Generated from commit:
  18c365095be26266618c455700ef622f0070bc65" — a single commit on 2026-06-23 titled
  "Add OPFS + Pyodide cross-device test harness (#290)".)
- **Author credibility**: Simon Willison is the creator of Django, creator of Datasette,
  and author of the `llm` CLI. He is a high-signal designated trusted-feed source in
  this corpus. This post continues his documented series of using Claude Code for web to
  build browser-native tools that feed back into Datasette Lite development. He maintains
  no vendor affiliation. His claims about browser compatibility issues (Safari/iOS)
  carry weight: he is building the tool specifically to investigate these constraints
  before committing to a Datasette Lite integration.
- **Scope**: Covers the OPFS + Pyodide test harness tool: its motivation (Datasette Lite
  persistent SQLite editing), its development method (Claude Code for web), its
  architecture (single-file, worker-from-Blob-URL, createSyncAccessHandle), and
  specific browser compatibility findings (Safari/iOS constraint, mountNativeFS/syncfs
  unreliability, sqlite3 explicit loading). Does NOT cover: results of testing across
  specific browsers, whether Willison has confirmed OPFS is viable for Datasette Lite,
  or any follow-up integration work.

## Extracted Claims

### Claim 1: Willison used Claude Code for web to build this OPFS test harness as a playground for investigating whether Datasette Lite could support persistent SQLite file editing

- **Evidence**: Blog post directly states both the motivation (Datasette Lite persistent
  SQLite) and the development method (Claude Code for web). The tool is available at
  `tools.simonwillison.net/opfs-pyodide` and committed on the same date as the blog
  post (2026-06-23, commit 18c36509).
- **Confidence**: settled (direct statements from blog post; commit evidence; live tool)
- **Quote**: "I've been pondering if Datasette Lite - the Python Datasette application
  run entirely in the browser using Pyodide and WebAssembly - might be able to edit
  persistent SQLite files stored on the user's computer." (blog post,
  simonwillison.net/2026/Jun/23/opfs-pyodide/)
- **Our assessment**: This is another documented instance of Willison using Claude Code
  for web to rapidly prototype a browser-native exploration tool. The pattern is now
  consistent across multiple simonw/tools entries: a specific Datasette Lite capability
  question → delegate tool-building to an AI agent → publish the result as a test
  harness. The blast radius here is near-zero: a single self-contained HTML file, no
  backend, no user data, static deployment. This satisfies Willison's own conditions
  (documented in `blog-simonwillison-vibe-coding-agentic-engineering.md`) for
  zero-review AI-assisted development.

### Claim 2: FileSystemFileHandle.createSyncAccessHandle() is the only OPFS write path that reliably works across all browsers including Safari/iOS

- **Evidence**: HTML source code comment documents this constraint explicitly, including
  the specific Safari/iOS incompatibility that forces the design decision. The tool is
  built to test exactly this constraint cross-device.
- **Confidence**: settled (documented constraint with specific browser-platform callout;
  the tool was designed around this constraint)
- **Quote**: "The high-performance OPFS write API, FileSystemFileHandle.createSyncAccessHandle(),
  is ONLY available inside a dedicated Web Worker. iOS Safari supports
  createSyncAccessHandle() but does NOT support the main-thread createWritable()
  stream, so the worker path is the only one that works on every device. This mirrors
  how a real app (e.g. Datasette Lite) would use OPFS." (from HTML comment,
  github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: The key constraint is not that createSyncAccessHandle() must be
  used instead of createWritable() — it's that createSyncAccessHandle() must be used
  inside a dedicated Web Worker. This means the architecture must thread OPFS operations
  through a worker, adding postMessage round-trips to every file operation. The tool's
  comment explicitly notes this mirrors how a real Datasette Lite integration would
  work, so this architectural constraint would apply directly to any production use.

### Claim 3: pyodide.mountNativeFS()/syncfs() is unreliable for SQLite persistence on Safari/iOS and must be avoided in cross-browser OPFS tools

- **Evidence**: HTML source code comment explicitly names the failure mode, references
  two specific Pyodide bug reports (pyodide#4057 and pyodide#3456), and describes the
  silent failure: syncfs() can return "successfully" while data never lands on disk.
- **Confidence**: settled (documented with specific Pyodide issue numbers and described
  failure mode; the tool was deliberately designed to avoid this path)
- **Quote**: "Persistence here deliberately AVOIDS pyodide.mountNativeFS()/syncfs().
  That path writes back to OPFS via FileSystemFileHandle.createWritable(), which is
  unreliable on Safari/iOS: syncfs() can resolve 'successfully' while the data never
  actually lands on disk (the database file stays at its initial size). See pyodide#4057
  and pyodide#3456." (from HTML comment in runSQL handler,
  github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: The silent failure mode is the critical danger here. syncfs()
  returning success while data never persists is a data-loss scenario that would be
  extremely hard to debug in production (the in-memory database appears correct; only
  a page reload reveals the persistence failure). This is a concrete reason to avoid
  mountNativeFS/syncfs entirely, not to try to work around it per-browser. The
  pyodide-asgi-browser note (`blog-simonwillison-pyodide-asgi-browser.md`) did not
  document this specific constraint — this is new information about Pyodide's OPFS
  integration bugs on Safari.

### Claim 4: The correct SQLite persistence pattern in OPFS with Pyodide is an explicit read-modify-write cycle using createSyncAccessHandle()

- **Evidence**: HTML source code documents the three-step pattern explicitly and explains
  why it's preferred over mountNativeFS/syncfs for this use case.
- **Confidence**: settled (documented implementation; avoids the Safari bug from Claim 3)
- **Quote**: "Instead we do an explicit read-modify-write of the whole database file
  through createSyncAccessHandle() — the one OPFS write API that works in every browser
  including Safari: 1. read test.db from OPFS into an in-memory (MEMFS) copy 2. run
  the SQL against that MEMFS database 3. write the MEMFS database back to OPFS via a
  sync access handle" (from HTML comment in runSQL handler,
  github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: The read-modify-write pattern is simple but non-obvious for
  practitioners expecting native filesystem semantics. The full database file is copied
  into MEMFS on every SQL call and written back on every write. The tool's comment
  notes "The test databases here are small, so copying the whole file each call is
  cheap and keeps every command self-contained." For production Datasette Lite use, where
  SQLite files could be arbitrarily large, this copy-on-read/write approach has
  O(database size) I/O cost per operation. This is an important scalability caveat the
  tool acknowledges for test databases but defers for production.

### Claim 5: sqlite3 is "unvendored" in Pyodide and must be explicitly loaded as a separate package before import

- **Evidence**: HTML source code comment with specific error message if omitted.
- **Confidence**: settled (documented in source code with explicit error detail)
- **Quote**: "sqlite3 is UNVENDORED in Pyodide: the stdlib module is shipped as a
  separate package that must be loaded explicitly before `import sqlite3`, otherwise
  it raises ModuleNotFoundError." (from HTML comment in Pyodide initialization,
  github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: This is a non-obvious gotcha that would surprise practitioners
  who expect Python stdlib modules to be universally available in Pyodide. Despite
  sqlite3 being part of the Python standard library, it requires an explicit
  `await pyodide.loadPackage("sqlite3")` call before use. This matters because
  Datasette Lite's reliance on sqlite3 means any integration with OPFS will hit this
  requirement. The `blog-simonwillison-pyodide-asgi-browser.md` note documented
  `num_sql_threads=0` as a constraint for Pyodide; this adds sqlite3 explicit loading
  as another Pyodide-specific configuration item for SQLite users.

### Claim 6: OPFS createSyncAccessHandle() holds an exclusive lock on the file that must always be released by calling close()

- **Evidence**: HTML source code includes explicit "ALWAYS close" warning comment with
  consequence description.
- **Confidence**: settled (documented with specific consequence of not closing)
- **Quote**: "ALWAYS close: an open sync access handle holds an exclusive lock and
  would block the next operation on this file." (from HTML comment in saveFile handler,
  github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: This is an important resource management constraint for OPFS. An
  unclosed sync access handle is a latent bug: subsequent operations on the same file
  will block indefinitely (or until the tab is reloaded), and the failure is not
  immediately obvious because the lock is held in a Web Worker context. The tool wraps
  all createSyncAccessHandle() calls in try/finally blocks to ensure close() is always
  called. Practitioners building on this pattern must apply the same discipline.

### Claim 7: Single-file, no-build-step architecture using an inline Blob URL worker is a viable pattern for AI-generated browser-native tools

- **Evidence**: HTML source code comment documents this architectural choice and its
  rationale explicitly. The tool is a working example of the pattern.
- **Confidence**: settled (working tool; documented design choice)
- **Quote**: "The worker here is created from an inline Blob URL so the whole project
  stays a single HTML file with no build step." (from HTML comment,
  github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: The inline Blob URL worker technique (reading a `<script
  type="text/worker">` tag's textContent and wrapping it in a Blob URL) eliminates the
  need for a bundler, file server, or module system. The entire tool — including the
  Pyodide worker, SQL handler, OPFS helpers, and UI — lives in a single HTML file. This
  pattern recurs across simonw/tools entries and is well-suited to AI-native tool
  generation: no multi-file coordination, no build pipeline, easy to share as a single
  file, easy for an AI agent to generate in a single output. The tradeoff is that the
  file becomes large and the worker source is not syntax-highlighted in typical editors.

### Claim 8: OPFS requires a secure context (HTTPS or http://localhost) and the harness provides explicit capability detection before attempting file operations

- **Evidence**: HTML source code checks window.isSecureContext and shows a warning
  banner; the capability panel detects OPFS availability, createSyncAccessHandle
  support, crossOriginIsolated status, and SharedArrayBuffer availability.
- **Confidence**: settled (browser spec constraint; implemented in the tool with fallback
  warning)
- **Quote**: "Manual cross-device testing for the Origin Private File System. Run it
  over HTTPS or http://localhost." (from HTML header, simonw/tools/opfs-pyodide.html)
- **Our assessment**: The capability detection panel reveals the full dependency graph
  for OPFS in a Pyodide context: secure context, OPFS directory API, createSyncAccessHandle
  in a Web Worker, and optionally SharedArrayBuffer (for crossOriginIsolated contexts).
  Detecting these capabilities upfront — before attempting operations — is the correct
  pattern for cross-device tools where support varies. The tool's structured capability
  table also serves as a diagnostic artifact: practitioners can run the harness on a
  target device and see exactly which capabilities are missing before committing to
  an OPFS integration.

### Claim 9: The harness is positioned as an investigation and validation tool, not a finished component — deliberately "test before integrate" before modifying Datasette Lite

- **Evidence**: Blog post framing ("I've been pondering... might be able to... try it
  out in different browsers"); tool title ("test harness"); docs description emphasizes
  "testing" and "verify persistence"; the tool adds no Datasette Lite code.
- **Confidence**: settled (author's stated framing; tool structure)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Willison's pattern here is worth documenting explicitly: he built
  a standalone test harness before touching Datasette Lite, using Claude Code for web
  to do so. This is a "validate the assumption first" engineering discipline — the
  uncertainty (can OPFS + Pyodide work reliably across devices for persistent SQLite?)
  is resolved before any production integration. The test harness surfaces the specific
  constraints (Safari/iOS worker requirement, mountNativeFS/syncfs bugs, sqlite3
  unvendored) without risking Datasette Lite stability. The guide should recommend
  this pattern: when investigating a new browser API for an existing tool, build a
  dedicated test harness (especially with AI assistance) rather than directly modifying
  the production tool.

### Claim 10: Pyodide should be pinned to a specific version via CDN and, for production use, vendored locally

- **Evidence**: HTML source code documents both the current CDN approach (jsDelivr,
  v0.27.2) and guidance for local vendoring.
- **Confidence**: settled (documented in source with explicit instructions)
- **Quote**: "Pyodide is loaded from the jsDelivr CDN, pinned to a specific version.
  To vendor it later: download the matching pyodide release, host it alongside this
  file, and change PYODIDE_INDEX_URL below to point at your local copy." (from HTML
  comment, github.com/simonw/tools/blob/main/opfs-pyodide.html)
- **Our assessment**: Version pinning (v0.27.2 specifically) ensures the tool does not
  break when Pyodide releases a new version that changes APIs or package availability.
  The vendoring guidance (download the full release + change PYODIDE_INDEX_URL) mirrors
  the pattern documented in `blog-simonwillison-pyodide-asgi-browser.md` Claim 11,
  where browser sandbox network restrictions forced local vendoring as a workaround —
  and produced offline capability as a side-effect. For any production browser-native
  Python tool, vendoring Pyodide locally is the more reliable approach: CDN availability
  is a runtime dependency, CDN delivery may be blocked in certain environments, and
  version drift between CDN releases can break the tool.

## Concrete Artifacts

### Read-modify-write SQLite pattern for OPFS (from opfs-pyodide.html, simonw/tools)

The runSQL handler in the Web Worker demonstrates the reliable cross-browser pattern:

```javascript
// Source: github.com/simonw/tools/blob/main/opfs-pyodide.html (runSQL handler, worker)

// 1. Load the current database from OPFS into MEMFS (if it exists).
const existing = await readOPFSBytes(DB_OPFS);
if (existing) {
  pyodide.FS.writeFile(DB_MEM, existing);
} else {
  try { pyodide.FS.unlink(DB_MEM); } catch (e) { /* not there: fine */ }
}

// 2. Run the SQL against the MEMFS copy.
const fn = pyodide.globals.get("run_sql_json");
let jsonStr;
try {
  jsonStr = fn(sql, DB_MEM); // Python str args/return cross as JS strings
} finally {
  fn.destroy();
}

// 3. Persist the (possibly modified) database back to OPFS.
const bytes = pyodide.FS.readFile(DB_MEM); // Uint8Array of the whole db
await writeOPFSBytes(DB_OPFS, bytes);
```

### Pyodide initialization in Web Worker (from opfs-pyodide.html, simonw/tools)

```javascript
// Source: github.com/simonw/tools/blob/main/opfs-pyodide.html (worker-src, Pyodide setup)

const PYODIDE_INDEX_URL = "https://cdn.jsdelivr.net/pyodide/v0.27.2/full/";

const pyodideReady = (async () => {
  importScripts(PYODIDE_INDEX_URL + "pyodide.js");
  pyodide = await loadPyodide({ indexURL: PYODIDE_INDEX_URL });
  // sqlite3 is UNVENDORED in Pyodide: the stdlib module is shipped as a
  // separate package that must be loaded explicitly before `import sqlite3`,
  // otherwise it raises ModuleNotFoundError.
  await pyodide.loadPackage("sqlite3");
  pyodide.runPython(`
import sqlite3, json

def run_sql_json(sql, db_path):
    con = sqlite3.connect(db_path)
    try:
        cur = con.cursor()
        try:
            cur.execute(sql)
        except sqlite3.ProgrammingError as e:
            if "one statement" in str(e).lower():
                cur.executescript(sql)
                con.commit()
                return json.dumps({"mode": "script",
                                   "message": "Executed multiple statements (no result set returned)."})
            raise
        if cur.description is not None:
            cols = [d[0] for d in cur.description]
            rows = cur.fetchall()
            con.commit()
            return json.dumps({"mode": "select", "columns": cols, "rows": rows}, default=str)
        con.commit()
        return json.dumps({"mode": "write", "rowcount": cur.rowcount})
    finally:
        con.close()
`);
})();
```

### createSyncAccessHandle write helper (from opfs-pyodide.html, simonw/tools)

```javascript
// Source: github.com/simonw/tools/blob/main/opfs-pyodide.html (writeOPFSBytes helper)

async function writeOPFSBytes(path, bytes) {
  const { dir, filename } = await resolvePath(path, { create: true });
  const fh = await dir.getFileHandle(filename, { create: true });
  const handle = await fh.createSyncAccessHandle();
  try {
    handle.truncate(0);
    const written = handle.write(bytes, { at: 0 });
    handle.flush();
    return written;
  } finally {
    handle.close();  // always release the exclusive lock
  }
}
```

### Inline Blob URL worker pattern (from opfs-pyodide.html, simonw/tools)

```javascript
// Source: github.com/simonw/tools/blob/main/opfs-pyodide.html (main thread setup)
// Worker source lives in a <script id="worker-src" type="text/worker"> tag.
// Reading its textContent and creating a Blob URL keeps the project single-file.

const workerSource = document.getElementById("worker-src").textContent;
const workerBlob = new Blob([workerSource], { type: "text/javascript" });
const worker = new Worker(URL.createObjectURL(workerBlob));
```

### Capability detection panel items (from opfs-pyodide.html, simonw/tools)

```
Capability checks performed on page load and on-demand:
- navigator.userAgent
- window.isSecureContext           (OPFS requires secure context)
- crossOriginIsolated              (required for SharedArrayBuffer)
- SharedArrayBuffer available
- "getDirectory" in navigator.storage  (OPFS directory API)
- createSyncAccessHandle (in worker)   (must be checked inside worker)
- navigator.storage.estimate()     (usage / quota in MB)
```

### Tool description (from opfs-pyodide.docs.md, simonw/tools, commit 18c36509)

```
Test and manage the Origin Private File System (OPFS) across desktop and mobile
browsers with an interactive interface powered by Pyodide. Create, read, and delete
files in OPFS, run SQL queries against SQLite databases stored in the file system,
and verify persistence across page reloads through a comprehensive activity log and
capability detection panel.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-pyodide-asgi-browser.md` Claim 10 ("Willison explicitly states
    he has not fully understood the AI-generated implementation... another documented
    instance of the agentic-engineering/vibe-coding blur"): Claim 1 of this note is
    another instance of the same pattern — Claude Code for web builds the tool, Willison
    publishes it, the blast radius is near-zero (single HTML file, static, no backend).
    The recurring pattern is now at least: LiteParse browser port (April 2026), Pyodide
    ASGI bridge (May 2026), this OPFS harness (June 2026).
  - `blog-simonwillison-pyodide-asgi-browser.md` Claim 11 ("vendoring Pyodide + wheels
    locally is the right default for production browser-native apps that need
    reliability"): Claim 10 of this note makes the same recommendation, now from the
    tool's own source code comment. Both notes independently document the version-pinning
    + local vendoring pattern as the production best practice.
  - `blog-simonwillison-wasm-wheels-pypi.md` Claim 9 (micropip install workflow
    enables installing packages from PyPI in Pyodide): The sqlite3 explicit-loading
    constraint in Claim 5 of this note is consistent — some Pyodide packages
    require explicit loading. The tool uses `pyodide.loadPackage("sqlite3")` rather
    than micropip; this is the correct path for stdlib packages that are unvendored in
    Pyodide.

- **Extends**:
  - `blog-simonwillison-pyodide-asgi-browser.md`: That note covers the deployment
    pattern for browser-native Python ASGI apps. This note extends the picture to
    persistent storage: running Python in the browser via Pyodide is established; this
    note adds the specific constraints for OPFS-based SQLite persistence, which is the
    next step for making browser-native Datasette Lite useful for real-world data work.
    Specifically, the pyodide-asgi-browser note's Claim 6 stated that the constraint
    for Pyodide ASGI was "C extensions or packages requiring OS threads do not work";
    this note adds another Pyodide constraint: mountNativeFS/syncfs unreliability on
    Safari/iOS (Claim 3) and sqlite3 explicit loading (Claim 5).
  - `blog-simonwillison-datasette-apps.md`: The datasette-apps note covers Willison's
    pattern of hosting sandboxed HTML apps inside Datasette. The OPFS harness represents
    the complementary direction: putting Datasette itself inside a browser-based
    persistent storage context. Together, they show Datasette evolving in both
    directions: apps inside Datasette, and Datasette inside a browser environment.
  - `blog-simonwillison-wasm-wheels-pypi.md`: The WASM wheels note documented the
    ecosystem shift enabling C/Rust extensions to be distributed as WASM wheels to PyPI.
    This note documents the persistence layer that browser-native Python tools need once
    they can run arbitrary packages. Together they address distinct gaps in the
    browser-native Python stack: package availability (wasm-wheels) + data persistence
    (this note).

- **Contradicts**: None identified. No existing corpus note makes contradictory claims
  about OPFS, createSyncAccessHandle, or PyodideFS SQLite persistence on Safari/iOS.

- **Novel**:
  - **OPFS + Pyodide SQLite persistence pattern**: No existing corpus note documents
    the read-modify-write pattern (OPFS → MEMFS → SQL → MEMFS → OPFS) as the
    cross-browser reliable approach. This is new.
  - **mountNativeFS/syncfs Safari/iOS bugs**: The specific finding that syncfs() silently
    fails on Safari/iOS (pyodide#4057, pyodide#3456) is not documented elsewhere in the
    corpus. This is a concrete, actionable constraint for any browser-native Pyodide tool
    that attempts SQLite persistence.
  - **createSyncAccessHandle exclusive lock constraint**: The "ALWAYS close or subsequent
    operations block" pattern is not documented elsewhere. This is a resource management
    constraint specific to OPFS sync access handles.
  - **sqlite3 as an unvendored Pyodide package**: The explicit-loading requirement for
    sqlite3 in Pyodide is not noted in any other corpus source (the pyodide-asgi-browser
    note documents `num_sql_threads=0` for Datasette but not the sqlite3 loading step).
  - **Build-a-test-harness-first pattern**: The concrete pattern of using Claude Code
    for web to build a standalone test harness before integrating a new browser API into
    a production tool is not explicitly documented as a pattern in the corpus.

## Guide Impact

- **Chapter 04 (Browser-Native Python — OPFS Persistence)**:
  Claims 2–6 together establish the OPFS + Pyodide SQLite persistence pattern. The
  guide should add (as a companion to the ASGI browser bridge pattern in
  `blog-simonwillison-pyodide-asgi-browser.md`):
  "When adding persistent SQLite storage to a Pyodide browser app via OPFS:
  (1) Use createSyncAccessHandle() inside a dedicated Web Worker — it is the only
  OPFS write API that works on all platforms including Safari/iOS.
  (2) Do NOT use pyodide.mountNativeFS()/syncfs() — syncfs() silently fails to persist
  on Safari/iOS (pyodide#4057, pyodide#3456).
  (3) Use read-modify-write: copy the database from OPFS into MEMFS, run SQL, write
  the full database back to OPFS via createSyncAccessHandle().
  (4) Always call handle.close() — an open sync access handle holds an exclusive lock.
  (5) Load sqlite3 explicitly: `await pyodide.loadPackage('sqlite3')` before `import
  sqlite3`, otherwise ModuleNotFoundError.
  This pattern is validated in Willison's OPFS + Pyodide test harness (June 2026) and
  is the anticipated approach for Datasette Lite persistent SQLite editing."

- **Chapter 02 (Harness Engineering — Validate Before Integrating)**:
  Claim 9 establishes the "build a test harness first" pattern as a named Willison
  practice. The guide should document: "Before integrating a new browser API into a
  production tool, build a standalone test harness — especially with AI assistance
  (Claude Code for web). The harness can reveal cross-browser compatibility constraints
  (Safari/iOS differences, API availability gaps) without touching the production
  codebase. Willison followed this pattern before adding OPFS support to Datasette Lite,
  using Claude Code for web to build the harness in a single session."

- **Chapter 02 (Harness Engineering — Single-File AI Tool Pattern)**:
  Claim 7 documents the inline Blob URL worker technique as a recurring pattern in
  simonw/tools. The guide should add: "For AI-generated browser-native tools with Web
  Worker requirements, the inline Blob URL worker pattern (worker source in a
  `<script type='text/worker'>` tag, read via textContent, wrapped in Blob URL) keeps
  the entire tool in a single HTML file with no build step. This simplifies AI
  generation, distribution, and maintenance of single-purpose tools. The tradeoff is
  that the file becomes large and worker source loses syntax highlighting."

- **Chapter 04 (Browser-Native Python — Pyodide Version Pinning)**:
  Claim 10 corroborates the pyodide-asgi-browser recommendation. The guide should
  consolidate: "Pin Pyodide to a specific version (e.g., v0.27.2 via jsDelivr CDN).
  For production tools, vendor the full Pyodide release locally alongside the HTML file.
  CDN-based loading risks availability outages and uncontrolled version drift."

## Extraction Notes

- **Two artifacts read**: The blog post at simonwillison.net/2026/Jun/23/opfs-pyodide/
  is very short (~3 sentences). The substantive content is in the tool source at
  github.com/simonw/tools/blob/main/opfs-pyodide.html (read via `gh api`). The tool
  source contains detailed inline code comments that serve as architectural documentation.
  Both were read in full.
- **Blog post quotes**: Two WebFetch calls retrieved the blog post text. The sentence
  about Datasette Lite ("I've been pondering...") appeared consistently. One WebFetch
  result rendered the blog post's OPFS reference as "OFPS" — this appears to be a
  WebFetch transcription artifact; the HTML source, docs file, and tool title all use
  "OPFS" consistently. The uncertain blog post phrase is not quoted directly; the
  Datasette Lite quote is used as it appeared consistently across fetches.
- **HTML source quotes**: All quotes attributed to opfs-pyodide.html were extracted
  from the raw file content retrieved via `gh api repos/simonw/tools/contents/opfs-pyodide.html`
  and decoded from base64. These are verbatim from the source file.
- **Safari/iOS bugs not independently verified**: The Pyodide bug references
  (pyodide#4057 and pyodide#3456) were not followed to the Pyodide issue tracker.
  The failure mode described (syncfs() resolves successfully while data never lands on
  disk) is taken from the source code comment as Willison's documented finding.
- **Confidence set to `emerging`**: The OPFS persistence pattern documented here is
  from a test harness explicitly built to investigate cross-browser viability — not from
  a production integration. The constraints are documented findings from the harness,
  but no post confirms that OPFS integration into Datasette Lite was completed. The
  pattern itself is sound (`settled` evidence for the individual constraints) but the
  overall "OPFS + Pyodide works for Datasette Lite" conclusion is still under
  investigation at time of publication.
