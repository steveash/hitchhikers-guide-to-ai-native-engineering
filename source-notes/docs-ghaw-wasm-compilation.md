---
source_url: https://github.github.com/gh-aw/reference/wasm-compilation
source_type: docs
title: "GitHub Agentic Workflows: WebAssembly Compilation Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#455"
---

# GitHub Agentic Workflows: WebAssembly Compilation Reference

> Defines how the gh-aw compiler can be packaged as a browser-runnable
> WebAssembly module — covering build prerequisites, the Go build-tag
> stubbing architecture, the `compileWorkflow(markdown)` JS API, compression
> targets, and the specific capabilities unavailable in the Wasm build
> (remote imports, external tool validation, terminal UI, filesystem writes).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/wasm-compilation`
  page — the "Reference" section, parallel to `reference/compilation-process`
  which covers the server-side native compiler. This page is the authoritative
  reference for the Wasm compilation target specifically.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory and all gh-aw documentation.
  Build commands, API signatures, stub file names, and limitation statements are
  authoritative for the `gh aw` platform's Wasm target. Claims about browser
  compatibility and compression ratios are stated as documentation facts, not
  practitioner observations.
- **Scope**: The WebAssembly build target of the gh-aw compiler — prerequisites,
  build artifacts, JavaScript integration API, Go build-tag stubbing architecture,
  and limitations. Does NOT cover: the server-side compilation pipeline (see
  `docs-ghaw-compilation-process.md`), the conceptual compilation model (see
  `docs-ghaw-how-they-work.md` Claim 7), Safe Outputs (see
  `docs-ghaw-how-they-work.md` Claim 5), or runtime workflow execution. This
  page is about distributing the compiler itself to browsers, not about running
  compiled workflows.

## Extracted Claims

### Claim 1: The gh-aw compiler can be packaged as a WebAssembly module, enabling browser-based workflow compilation without a server-side Go installation

- **Evidence**: The page describes the Wasm module as enabling "browser-based
  compilation of agentic workflows without requiring a server-side Go installation,"
  supporting "interactive development environments and offline tooling scenarios."
- **Confidence**: emerging (first-party documentation; the Wasm build is a
  supported target but the page does not cite production deployments using it)
- **Quote**: (no direct quote for the overall capability claim; see paraphrase in
  Our assessment)
- **Our assessment**: This extends the gh-aw toolchain from a CLI-only tool to
  one that can be embedded in browser-based IDEs, documentation sites, or offline
  tools — practitioners could build interactive workflow editors that run
  compilation client-side. The key architectural value: no server required,
  compilation happens in the browser. For Ch02 (Harness Engineering): worth
  noting as a deployment pattern for teams building tooling around gh-aw — if
  you want to offer workflow authoring in a web UI without backend infrastructure,
  the Wasm build provides that capability.

### Claim 2: The Wasm build includes the core compilation engine — markdown parsing, frontmatter extraction, import resolution (local only), and YAML generation — in a single distributable module

- **Evidence**: The page describes the Wasm build as encompassing "markdown
  parsing, frontmatter extraction, import resolution, and YAML generation" in a
  single module. The "local only" qualifier for import resolution is established
  by Claim 8 (remote imports produce an error).
- **Confidence**: settled (first-party; the capabilities are explicitly listed)
- **Quote**: "markdown parsing, frontmatter extraction, import resolution, and
  YAML generation"
- **Our assessment**: The Wasm build runs a meaningful subset of the full
  five-phase compilation pipeline documented in `docs-ghaw-compilation-process.md`
  Claim 1. Specifically: Phase 1 (parsing/validation — but with import resolution
  restricted to local files), Phase 2 (job construction), Phase 3 (dependency
  resolution), and Phase 5 (YAML generation). Phase 4 (action pinning via GitHub
  API) is effectively unavailable (no HTTP calls). For Ch02: the Wasm build is
  sufficient for structural validation and local workflow development but cannot
  produce fully pinned lock files.

### Claim 3: Building requires Go 1.25+ and GNU Make; `make build-wasm` produces two artifacts: `gh-aw.wasm` and Go's runtime shim `wasm_exec.js`

- **Evidence**: The page lists prerequisites as "Go 1.25 or later" and
  "make (GNU Make)." The build command `make build-wasm` is documented as
  producing `gh-aw.wasm` and `wasm_exec.js` (from `$(go env GOROOT)/misc/wasm/`).
  Both files must be copied to the project directory.
- **Confidence**: settled (first-party; CLI command and artifacts are named)
- **Quote**: "Go 1.25 or later"
- **Our assessment**: The two-artifact model is important for deployment: `gh-aw.wasm`
  is the compiled compiler; `wasm_exec.js` is Go's standard runtime bridge that
  must accompany any Go-compiled Wasm binary. Both must be served from the same
  origin or accessible via `fetch()`. The Go version requirement (1.25+) aligns
  with recent Go Wasm improvements and must be kept in sync with the project's Go
  toolchain version.

### Claim 4: Brotli compression reduces the Wasm binary from ~17 MB to ~5 MB (70% reduction); gzip fallback produces ~6 MB

- **Evidence**: The page documents the raw binary size as approximately 17 MB and
  states that brotli compression reduces it to roughly 5 MB. A gzip fallback
  yields approximately 6 MB. The page implies automatic browser delivery based on
  detected compression support.
- **Confidence**: settled (first-party; specific byte sizes are documented)
- **Quote**: (no direct quote; sizes confirmed across both WebFetch passes)
- **Our assessment**: The 70% compression ratio makes the Wasm build viable for
  web delivery — 5 MB on first load with brotli is acceptable for developer
  tooling (comparable to large web framework bundles). The gzip fallback (~6 MB)
  covers browsers without brotli support. The brotli command is `brotli -k -q 11
  gh-aw.wasm` (maximum compression, keeps original file). For Ch02: teams deploying
  a Wasm-based workflow editor should serve brotli-compressed artifacts with
  Content-Encoding negotiation; don't serve the 17 MB uncompressed binary.

### Claim 5: The JavaScript API exposes `compileWorkflow(markdown)` which accepts workflow markdown and returns a Promise resolving to `{ yaml, warnings, error }`

- **Evidence**: The page documents the API signature as:
  ```
  compileWorkflow(markdown: string): Promise<{ yaml: string, warnings: string[], error: null }>
  ```
  The function "accepts workflow content and returns compiled YAML with any
  warnings."
- **Confidence**: settled (first-party; the API signature is explicitly documented)
- **Quote**: (no direct quote for the description; the API signature is verbatim
  from the page's JavaScript API section)
- **Our assessment**: The API design is intentionally minimal — a single function
  accepting a string and returning structured output. The `warnings` array is
  significant: it surfaces compilation warnings (not just errors) that a UI could
  display to the workflow author in real time. The `error: null` in the success
  type suggests the error field is present but null on success, providing a
  discriminated union in the returned object. For Ch02: when building a Wasm-based
  workflow editor, display `warnings` alongside the compiled YAML — they may
  indicate deprecated patterns or non-fatal issues that would not prevent
  compilation but should be addressed.

### Claim 6: Go build tags conditionally compile platform-specific code — `//go:build js || wasm` for browser stubs, `//go:build !js && !wasm` for native implementations — with shared core logic across both targets

- **Evidence**: The page documents the build tag convention: "Files use
  `//go:build js || wasm` for stubs and `//go:build !js && !wasm` for native
  implementations." The page states "Each stubbed file uses a pair of build
  constraints" maintaining separate implementations while sharing core compiler logic.
- **Confidence**: settled (first-party; the build tag syntax is directly stated)
- **Quote**: "Each stubbed file uses a pair of build constraints"
- **Our assessment**: The build tag architecture is the mechanism that makes the
  Wasm compilation feature maintainable — the core compilation logic (Phases 2–5
  from `docs-ghaw-compilation-process.md` Claim 1) is shared between native and
  Wasm builds; only platform-specific components (terminal UI, network calls,
  filesystem) are swapped out via paired constraint files. This is a well-understood
  Go pattern for cross-platform builds. Teams maintaining their own Go-based tools
  that target both CLI and browser can adopt this pattern.

### Claim 7: Terminal UI components — Lip Gloss, Bubble Tea, and Huh — are replaced with plain-text equivalents in the Wasm build; ten specific UI files are stubbed out

- **Evidence**: The page names the terminal UI libraries replaced: "Lip Gloss,
  Bubble Tea, and Huh." The stubbed files listed include: banner, confirm, console,
  form, input, layout, list, progress, select, spinner — ten components in total.
- **Confidence**: settled (first-party; library names and file list are explicitly
  enumerated)
- **Quote**: "Lip Gloss, Bubble Tea, and Huh"
- **Our assessment**: These are all Go terminal rendering libraries used in the
  native CLI for interactive prompts, colored output, and progress indicators.
  In the Wasm target they are replaced with no-op or plain-text implementations
  since browsers have no terminal. This means the Wasm build produces no styled
  output — output suitable for programmatic consumption by a JS caller, not for
  display in a terminal. For Ch02: the Wasm build is not a terminal emulator;
  any UI for displaying compiler output must be built in the host JavaScript
  application.

### Claim 8: Remote imports and HTTP calls are entirely unavailable in the Wasm build — workflows using `imports:` produce a compilation error, and the `importResolver` callback is not currently supported

- **Evidence**: The first WebFetch confirms: "Workflows that use `imports:` will
  produce an error." The second WebFetch adds: "Import resolution (importResolver
  callback) is not currently supported." Remote import stubs "Return error; HTTP
  calls unavailable."
- **Confidence**: settled (first-party; the limitation is explicitly stated and
  the error behavior is documented)
- **Quote**: "Workflows that use `imports:` will produce an error."
- **Our assessment**: This is the most significant practical limitation for
  practitioners. The full server-side compilation pipeline supports BFS import
  resolution (`docs-ghaw-compilation-process.md` Claim 2), which enables shared
  workflow libraries. In the Wasm build, that entire capability is absent — any
  workflow that uses `imports:` fails to compile. The `importResolver` callback
  note suggests this may be a future extension point (a callback that could
  provide import content without HTTP), but it is not yet implemented. For Ch02:
  the Wasm build is appropriate for single-file workflows; teams with multi-file
  workflows using shared imports cannot use the Wasm compiler for those workflows
  today.

### Claim 9: External tool validators (npm, pip, docker, git, gh CLI) return nil in the Wasm build, bypassing tool availability checks; filesystem writes are also disabled

- **Evidence**: The page states external validation stubs return `nil` — npm, pip,
  docker, git, and gh validators are all listed. Filesystem writes are in "no-emit
  mode" (the compiler validates but does not write output files).
- **Confidence**: settled (first-party; the stubbed validator list is explicitly
  enumerated)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `nil` return for validators means the Wasm compiler
  does not check whether required tools are installed — it cannot execute
  subprocesses in a browser environment. This is a silent capability difference
  from the native compiler: a workflow that requires `npm` will compile successfully
  in Wasm but may fail at runtime on a native runner that lacks npm. For Ch02:
  practitioners using the Wasm build for pre-flight validation should be aware
  that tool availability errors will not surface at compile time in the browser —
  only at runtime on the actual GitHub Actions runner.

## Concrete Artifacts

### Build Prerequisites and Commands

```bash
# Prerequisites:
#   Go 1.25 or later
#   make (GNU Make)

# Build the Wasm module
make build-wasm

# Artifacts produced:
#   gh-aw.wasm          (~17 MB uncompressed)
#   wasm_exec.js        (Go's Wasm runtime shim — from Go installation)

# Copy to your project:
cp gh-aw.wasm your-project/
cp "$(go env GOROOT)/misc/wasm/wasm_exec.js" your-project/

# Optional: brotli compression (70% size reduction, 17 MB → 5 MB)
brotli -k -q 11 gh-aw.wasm
# Produces: gh-aw.wasm.br (~5 MB)
# Gzip fallback: ~6 MB
```

*Source: `reference/wasm-compilation` — "Prerequisites" and "Building" sections*

### JavaScript Module Loading

```html
<script src="wasm_exec.js"></script>
<script>
const go = new Go();
WebAssembly.instantiateStreaming(
  fetch("gh-aw.wasm"),
  go.importObject
).then((result) => {
  go.run(result.instance);
});
</script>
```

*Source: `reference/wasm-compilation` — "JavaScript API > Loading the module" section*

### JavaScript API Signature

```javascript
// Exposed after module initialization:
compileWorkflow(markdown: string): Promise<{
  yaml: string,
  warnings: string[],
  error: null
}>

// Basic usage:
const result = await compileWorkflow(markdownSource);
if (result.error) {
  console.error(result.error);
} else {
  console.log(result.yaml);       // compiled lock YAML
  console.log(result.warnings);   // non-fatal warnings
}
```

*Source: `reference/wasm-compilation` — "JavaScript API > compileWorkflow(markdown)" section*

### Go Build Tag Convention

```go
// File: banner_js.go  (Wasm stub — no-op plain-text implementation)
//go:build js || wasm

// File: banner.go     (Native implementation — full terminal UI)
//go:build !js && !wasm
```

*Source: `reference/wasm-compilation` — "How it works > Build tag convention" section*

### Wasm Capability Comparison

```
Capability                   | Native CLI  | Wasm Build
-----------------------------|-------------|------------------
Markdown parsing             | Yes         | Yes
Frontmatter extraction       | Yes         | Yes
YAML generation              | Yes         | Yes
Local workflow compilation   | Yes         | Yes
Remote imports (imports:)    | Yes         | No — produces error
HTTP / gh CLI calls          | Yes         | No — unavailable
External tool validation     | Yes         | No — returns nil
Action SHA pinning (Phase 4) | Yes         | No — no HTTP
Filesystem writes            | Yes         | No — no-emit mode
Terminal UI (TUI)            | Yes         | No — plain-text only
Interactive prompts          | Yes         | No — stubbed
importResolver callback      | Yes         | Not yet supported
```

*Source: `reference/wasm-compilation` — "Limitations" section*

### Stubbed UI Components (10 files)

```
Terminal UI libraries replaced: Lip Gloss, Bubble Tea, Huh
Stubbed files: banner, confirm, console, form, input, layout,
               list, progress, select, spinner
```

*Source: `reference/wasm-compilation` — "How it works > What gets stubbed" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation model):
    the Wasm build provides a browser-side execution path for the same `.md` →
    compiled YAML transformation. Both establish that compilation is a discrete step
    that can be run independently of workflow execution; this source adds that the
    step can also run client-side in a browser.
  - `docs-ghaw-compilation-process.md` Claim 7 (only frontmatter changes require
    recompilation; markdown body loaded at runtime): the Wasm build's `compileWorkflow`
    function embodies the same boundary — it compiles the frontmatter-defined
    structure and validates the workflow spec. The markdown instruction body is still
    runtime-loaded; the Wasm compiler handles the structural compilation step.

- **Extends**:
  - `docs-ghaw-compilation-process.md` Claim 1 (five-phase pipeline): the Wasm
    build runs a subset of the pipeline. Phases 1 (partial — local imports only),
    2, 3, and 5 are available; Phase 4 (action SHA pinning via GitHub API) is
    unavailable due to the HTTP restriction. The Wasm build is best understood
    as a Phase 1–3 + 5 compiler that cannot perform Phase 4 pinning.
  - `docs-ghaw-compilation-process.md` Claim 2 (BFS import resolution): this source
    adds the browser-target constraint — BFS import resolution works in the native
    compiler but is entirely absent in the Wasm build. Any workflow using `imports:`
    fails to compile in the browser. This is a significant scope limitation that
    practitioners must understand when choosing between the CLI and a browser-based
    Wasm tool.
  - `docs-ghaw-agentic-authoring.md` Claim 4 (GitHub Web Interface for non-interactive
    workflow creation): the Wasm build enables a third path for browser-based
    workflow tooling — in addition to GitHub's Copilot web UI, teams can build
    custom browser editors using the Wasm compiler. Both are browser-based; the
    difference is that the Copilot web UI is hosted by GitHub while the Wasm build
    can be embedded in any web application.

- **Contradicts**: None identified. The Wasm compilation capability is additive
  to the existing compilation model documented in `docs-ghaw-how-they-work.md`
  and `docs-ghaw-compilation-process.md`. The limitations in the Wasm build (no
  remote imports, no action pinning) are environment constraints, not contradictions
  of the server-side compiler's claims. No contradiction issue required.

- **Novel**:
  - **Browser-side compilation path** (Claim 1): No other source in the corpus
    documents a browser-runnable version of the gh-aw compiler. All prior
    compilation notes (`docs-ghaw-how-they-work.md`, `docs-ghaw-compilation-process.md`)
    describe the native CLI. This is the first documented path for embedding
    gh-aw compilation in a browser-based tool.
  - **`compileWorkflow(markdown)` JS API** (Claim 5): The specific API surface
    exposed by the Wasm build — a single async function with a structured return
    type — is new to the corpus.
  - **Go build-tag stubbing architecture** (Claim 6): The paired `//go:build js
    || wasm` / `//go:build !js && !wasm` constraint pattern for sharing core logic
    across targets is documented here for the first time in the corpus.
  - **Wasm-specific limitation set** (Claims 8, 9): The specific set of disabled
    capabilities in the browser target (no `imports:`, no tool validators, no
    action pinning, no TUI) creates a distinct capability profile not described
    in any other source note.
  - **Compression targets** (Claim 4): Brotli/gzip compression ratios and the
    17 MB → 5 MB / 6 MB figures are deployment-relevant data new to the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add Wasm compilation as a deployment pattern for browser-based tooling**
  (Claim 1): Teams building workflow editors, documentation playgrounds, or
  interactive tutorials can embed the gh-aw compiler in a web page via the Wasm
  build. Document this as a "browser tooling" pattern distinct from the CLI-based
  compile → watch → run loop. Key trade-off: browser compilation works for
  single-file workflows but cannot handle workflows with `imports:`.

- **Document the `imports:` limitation for Wasm targets** (Claim 8): If Ch02
  recommends `imports:` for shared workflow libraries (per `docs-ghaw-compilation-process.md`
  Claim 2 on BFS import resolution), it should note that any tool built on the
  Wasm compiler cannot validate multi-file workflows. Teams choosing between
  building a CLI-integrated tool vs. a browser tool for workflow validation need
  to know this limitation upfront.

- **Add `compileWorkflow(markdown)` API to reference material** (Claim 5): For
  practitioners building custom tooling, document the JS API signature and the
  `warnings` array as a real-time feedback mechanism for workflow authors.

- **Serve Wasm with brotli compression** (Claim 4): If the guide covers Wasm
  deployment, recommend brotli-compressed delivery (`Content-Encoding: br`) with
  gzip fallback. The 17 MB uncompressed binary is not suitable for casual web
  delivery; the 5 MB brotli-compressed version is.

### Chapter 01: Daily Workflows

- **Mention browser-based compilation as a low-friction preview path** (Claim 1):
  For teams that want to explore gh-aw workflow syntax without CLI setup, a
  browser-based tool built on the Wasm compiler is a possible entry point. This
  complements the GitHub Web Interface path documented in
  `docs-ghaw-agentic-authoring.md` Claim 4 — both are browser-based; the Wasm
  path is for teams building their own tooling.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The gh-aw documentation is an
   Astro/Starlight SPA. Two separate WebFetch passes were used — a general
   content extraction and a focused verbatim extraction — to maximize fidelity.
   Claims with direct quotes have been verified across both passes. Claims marked
   "(no direct quote; see paraphrase in Our assessment)" reflect cases where the
   WebFetch returned paraphrased summaries without clear verbatim markers.

2. **API signature confirmed across both passes**: The `compileWorkflow` function
   signature was returned identically in both WebFetch passes and is treated as
   verbatim.

3. **Build tag syntax confirmed verbatim**: The `//go:build js || wasm` and
   `//go:build !js && !wasm` conventions appeared as code in the second WebFetch
   pass and are treated as verbatim.

4. **Phase 4 (action pinning) inference**: The page does not explicitly state
   that action pinning is unavailable in the Wasm build. However, pinning requires
   GitHub API HTTP calls, which the page states are unavailable. The Phase 4
   inference in Claim 2 and the capability comparison table is therefore an
   assessment, not a direct citation.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-11.

6. **No contradictions to file**: Reviewed all existing source notes. The Wasm
   limitations (no remote imports, no action pinning) are environment constraints
   on a new deployment target, not claims that oppose the server-side compiler's
   capabilities documented in prior notes.
