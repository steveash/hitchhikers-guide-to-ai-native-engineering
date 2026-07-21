---
source_url: https://simonwillison.net/2026/Jul/16/mermaid-ascii/
source_type: blog-post
title: "Mermaid to ASCII art (mermaid-ascii)"
author: Simon Willison
date_published: 2026-07-16
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: anecdotal
issue: "#2087"
---

# Mermaid to ASCII art (mermaid-ascii)

> The same day he shipped a Rust-based Mermaid-to-Unicode renderer ported from xAI's
> Grok Build, Simon Willison learned of an older, more feature-complete Go library
> (AlexanderGrooff/mermaid-ascii) that does the same job, and had Claude Fable 5 compile
> it — unmodified — to WebAssembly in a second single-prompt session so he could compare
> the two side by side. The resulting PR shows the agent stripping a CLI/web-server
> dependency graph, writing a `syscall/js` shim, and adding an XSS-hardened rendering path
> and its own Playwright test suite, all without those details being specified in the prompt.

## Source Context

- **Type**: blog-post (Simon Willison "Tool" post — his short-form category for shipped
  utilities. Extremely short: four sentences of body text plus a screenshot and posting
  metadata. As with the companion post about the same day's other Mermaid tool (see
  `blog-simonwillison-grok-mermaid.md`), the substantive technical content lives in the
  linked GitHub pull request that shipped the tool, not the blog post itself.)
- **Author credibility**: Simon Willison is the creator of Django and Datasette, author of
  the `llm` CLI, and a designated `trusted-feed` source in this corpus with dozens of prior
  notes documenting his own Claude Code / Claude Code for web sessions (see
  `blog-simonwillison-grok-mermaid.md`, `blog-simonwillison-liteparse-browser.md`,
  `blog-simonwillison-opfs-pyodide.md`, `blog-simonwillison-servo-crate-exploration.md`).
  He publishes the underlying artifacts (PR, live tool, exact prompt) for every session he
  reports on, making his claims independently verifiable rather than self-reported. No
  vendor affiliation with Anthropic or with AlexanderGrooff (the third-party library author).
- **Scope**: Covers one concrete build: compiling the unmodified upstream
  `AlexanderGrooff/mermaid-ascii` Go library (a terminal Mermaid renderer, MIT-licensed,
  1,481 GitHub stars as of this extraction) to WebAssembly and wrapping it in a browser
  playground, via a single Claude Code for web (Fable 5) session. Does NOT cover: a session
  transcript, duration, or token cost (the PR links a Claude.ai session URL that requires
  authentication and was not fetched); a rendering-fidelity comparison between this tool's
  output and the upstream CLI's terminal output; or any assessment of why the agent chose
  the specific dependency-stripping approach it used (the PR states what was done, not the
  agent's reasoning process).

## Extracted Claims

### Claim 1: The shipped tool converts Mermaid syntax into ASCII/Unicode box-drawing art entirely client-side via WebAssembly, and — unlike the companion Rust-based tool shipped the same day — supports color definitions
- **Evidence**: Willison's own tool description in the post body, contrasted explicitly
  with his prior Rust-based tool (`blog-simonwillison-grok-mermaid.md`).
- **Confidence**: settled (author's direct description of a live, publicly runnable tool)
- **Quote**: "Convert Mermaid diagram syntax into ASCII and Unicode box-drawing art rendered entirely in your browser using a Go library compiled to WebAssembly. The tool supports flowcharts with labeled edges, subgraphs, and color definitions, as well as sequence diagrams with notes and control flow fragments, while offering customizable padding and output options."
- **Our assessment**: This is a working utility with configurable output (padding, ASCII-only
  toggle), not a proof-of-concept — consistent with the pattern already documented across
  Willison's other browser-WASM tools in this corpus. The color-definition support is the
  single capability Willison calls out as differentiating this Go-based port from the
  Rust-based one he'd shipped hours earlier, which is the entire stated motivation for
  building a second tool that does the same underlying job (see Claim 2).

### Claim 2: Willison built this second Mermaid-to-ASCII tool specifically to compare it against the Rust-based one he had just shipped, after learning the Go library was "older" and "more fully-featured"
- **Evidence**: Willison's own narrative connecting the two tools, published in the same
  post.
- **Confidence**: settled (first-person account, both artifacts independently verifiable)
- **Quote**: "After building the Mermaid to ASCII tool based on Grok Build's Rust code I learned that there's an older, more fully-featured Go library called AlexanderGrooff/mermaid-ascii that implements a similar pattern, so I had Claude Fable 5 compile that one to WebAssembly as well so I could compare the two."
- **Our assessment**: This is a distinct workflow shape from the discovery-then-port pattern
  in the companion note (finding code while reading an unrelated codebase): here Willison
  deliberately went looking for a second, independent implementation of the same capability
  specifically to benchmark it against the one he'd just built, using the same
  agent-compiles-to-WASM technique on a different source language (Go vs. Rust) and a
  different upstream project entirely. The "compile it to WASM to compare" motive is new to
  this corpus — prior WASM-porting notes document a single library each, not two competing
  implementations ported for side-by-side evaluation.

### Claim 3: The exact prompt instructed the agent to clone the target repo, figure out if it could be made to work in WebAssembly "like the most recently added project in this repo," and build an HTML playground with examples reusing samples from the prior Rust tool where they fit
- **Evidence**: The prompt is quoted verbatim (as a Markdown blockquote) at the top of the
  GitHub pull request Willison's tooling links as the source of the build.
- **Confidence**: settled (verbatim artifact reproduced in a merged, public pull request)
- **Quote**: "Clone https://github.com/AlexanderGrooff/mermaid-ascii to /tmp\n\nFigure out if you can get it working in WebAssembly, like the most recently added project in this repo - then build a similar HTML playground called mermaid-ascii.html but with a ser if examples that fits this Go library (reusing existing samples from the Rust one if they work)" (github.com/simonw/tools/pull/295, PR body, blockquoted prompt)
- **Our assessment**: The prompt explicitly points at prior work in the same repository
  ("like the most recently added project in this repo") rather than re-explaining the WASM
  build approach from scratch — a compact way of saying "follow the pattern you already
  established" without spelling out any of the steps (build-tag stubbing, FFI surface,
  playground layout) that pattern actually involves. It also asks the agent to reuse
  existing examples "if they work," delegating the compatibility judgment about which Rust
  demo diagrams also exercise this Go library's supported feature set to the agent. Note the
  prompt contains a verbatim typo ("a ser if examples" — apparently "a set of examples"); it
  is reproduced here exactly as written, not corrected.

### Claim 4: To make the CLI-and-web-server-oriented Go library WASM-compatible, the agent's build script pins a specific upstream commit, strips the Cobra CLI and Gin web-server entry points (identified as unused by anything else in the codebase), and adds a hand-written `syscall/js` shim exporting a single `renderMermaidAscii()` function
- **Evidence**: Stated directly in the PR's bullet list describing `build_wasm.sh`.
- **Confidence**: settled (verifiable in the merged PR description and the 64-line
  `build_wasm.sh` file it added)
- **Quote**: "mermaid-ascii/build_wasm.sh clones upstream at a pinned commit, strips the cobra CLI and gin web-server entry points (nothing else imports them), adds a syscall/js shim exporting renderMermaidAscii(), and builds a 3.7 MB module (wasm-opt -Oz; ~1.1 MB gzipped)." (github.com/simonw/tools/pull/295, PR body)
- **Our assessment**: This mirrors the dependency-isolation judgment call already documented
  in the companion Rust port (`blog-simonwillison-grok-mermaid.md` Claim 4, stripping
  `ratatui` via a shim) but applied to a different problem: instead of reimplementing a
  narrow slice of a UI library's types, here the agent identifies and deletes two entire
  *entry-point* dependencies (a CLI framework and a web server framework) that the
  compilation target (a library function call, not a running program) doesn't need at all —
  then verifies via import analysis that nothing else in the codebase depends on them
  ("nothing else imports them"). Pinning the upstream commit in the build script is also a
  reproducibility practice not explicitly requested in the prompt.

### Claim 5: The web page renders using the library's own "html" output style (so `classDef color:#hex` styling works) but sanitizes that output through a strict tokenizer plus `textContent`, rather than passing the library's raw HTML string to `innerHTML`
- **Evidence**: Stated directly in the PR's implementation bullet list.
- **Confidence**: settled (verifiable in the merged PR description)
- **Quote**: "The page renders with the library's \"html\" style so classDef color:#hex classes work, sanitizing the unescaped span output via a strict tokenizer + textContent instead of innerHTML." (github.com/simonw/tools/pull/295, PR body)
- **Our assessment**: This is a security-relevant design decision the prompt did not ask
  for: the upstream Go library emits raw, apparently-unescaped HTML `<span>` tags to support
  colored output, which is untrusted-input territory once user-supplied Mermaid `classDef`
  text can influence that output. The agent recognized that naively assigning the library's
  HTML string to `.innerHTML` would be an XSS vector and built a parser that only trusts a
  constrained token grammar, writing displayed text via `textContent` rather than raw HTML
  injection. Claim 7 (a dedicated XSS probe in the test suite) shows this wasn't just a
  passing design note but something the agent also wrote a regression test for.

### Claim 6: The prompt's requested example set was scoped to the features this specific Go library actually supports (labeled edges, fan-out, subgraphs, multi-line labels via `<br>`, `classDef` colors, and sequence diagrams with alt/loop/par fragments and notes), reusing two examples from the earlier Rust-based tool where compatible
- **Evidence**: Listed explicitly in the PR's bullet describing the examples added.
- **Confidence**: settled (verifiable in the merged PR description and the 338-line
  `mermaid-ascii.html` file)
- **Quote**: "Examples cover the features this library actually supports: labeled edges, A --> B & C fan-out, subgraphs, <br> multi-line labels, classDef colors, and sequence diagrams with alt/loop/par fragments and notes (two examples reused from grok-mermaid where compatible)." (github.com/simonw/tools/pull/295, PR body)
- **Our assessment**: "The features this library actually supports" implies the agent had to
  determine that feature set empirically or by reading the source, rather than assuming
  parity with the Rust tool it was explicitly told to reuse examples from — an example that
  only the Rust renderer supports would presumably be dropped rather than included and
  silently fail. This is the same kind of scoped, verified example curation seen in the
  companion note's tool (`blog-simonwillison-grok-mermaid.md`), applied here across two
  independently-sourced libraries with partially overlapping feature sets.

### Claim 7: The PR includes 8 Playwright tests for the tool, one of which is explicitly described as an XSS probe
- **Evidence**: Stated directly in the PR's bullet list, and reflected in the added
  89-line `tests/test_mermaid_ascii.py` file.
- **Confidence**: settled (verifiable in the merged PR's file list and description)
- **Quote**: "tests/test_mermaid_ascii.py: 8 Playwright tests incl. an XSS probe." (github.com/simonw/tools/pull/295, PR body)
- **Our assessment**: Combined with Claim 5, this shows the agent didn't just implement an
  output-sanitization mitigation but also wrote an automated test specifically targeting
  that risk, rather than leaving the security property unverified. This matches the
  "Playwright TDD" habit already documented in this corpus (`blog-simonwillison-grok-mermaid.md`
  Claim 7, `blog-simonwillison-liteparse-browser.md` Claim 7) as a recurring pattern in
  Willison's AI-ported browser tools — here extended to include a security-focused test
  case, not just functional-rendering coverage.

### Claim 8: The entire change — 9 new files, 1,258 added lines, zero deletions — was produced as a single commit and merged within roughly 13 minutes of that commit being authored
- **Evidence**: GitHub PR/commit metadata for `simonw/tools#295`: one commit authored at
  2026-07-16T14:44:00Z ("mermaid-ascii: Mermaid to ASCII art playground via Go WASM"), PR
  opened 2026-07-16T14:56:40Z, merged 2026-07-16T14:57:40Z. Files added: `mermaid-ascii.html`
  (338 lines), `mermaid-ascii.wasm` (compiled binary), `mermaid-ascii/LICENSE` (21 lines),
  `mermaid-ascii/README.md` (73 lines), `mermaid-ascii/build_wasm.sh` (64 lines),
  `mermaid-ascii/main.go` (85 lines), `mermaid-ascii/wasm_exec.js` (575 lines, Go's runtime
  shim), `mermaid-ascii/wasm_globals.go` (13 lines), `tests/test_mermaid_ascii.py` (89 lines).
- **Confidence**: settled (directly queried GitHub API metadata for the merged PR, its
  single commit, and its file list)
- **Quote**: (no direct quote; see paraphrase above — quantities are from GitHub API JSON
  fields, not prose)
- **Our assessment**: The commit-to-merge gap (~13 minutes) is short enough to suggest the
  entire task — cloning the upstream repo, building the WASM stripping/shim logic, writing
  the HTML playground, writing 8 Playwright tests, and authoring the license/README — was
  completed within a single agent session before that session's output was committed and
  merged as-is, with no separate human review-and-revise cycle visible in the PR's commit
  history (one commit total). This is consistent with, but not proof of, a "one-shot"
  session; as in the companion note, no session transcript or duration was independently
  fetched, since the linked Claude.ai session URL requires authentication.

### Claim 9: The PR was merged by a GitHub App-driven Claude Code integration, evidenced by an automated "I'll analyze this and get back to you" comment and a separate "Claude encountered an error" comment linking to a GitHub Actions run
- **Evidence**: The two comments on `simonw/tools#295`, and the PR's
  `performed_via_github_app` metadata identifying the `claude` GitHub App (description:
  "Run Claude Code from your GitHub Pull Requests and Issues to respond to reviewer
  feedback, fix CI errors, or modify code").
- **Confidence**: emerging (the comments and app metadata are directly observable, but their
  precise cause — e.g., what triggered the error, what "analyze" refers to — is not
  documented anywhere in the PR itself)
- **Quote**: "I'll analyze this and get back to you." (simonw/tools#295, issue comment)
- **Quote (error)**: "Claude encountered an error" (simonw/tools#295, issue comment, linking to a GitHub Actions run)
- **Our assessment**: This indicates Willison's `simonw/tools` repo has the Claude GitHub
  App installed and wired into CI/PR automation beyond just the ad hoc "Claude Code for web"
  session that authored the commit — i.e., there's a second, repo-level automation layer
  that reacts to the PR (and apparently hit an error doing so). The PR merged successfully
  regardless, so whatever this automation was attempting was not blocking. This is a minor,
  incidental data point about Willison's repo tooling rather than part of the mermaid-ascii
  build narrative itself; it is not independently confirmed what the automation was for.

## Concrete Artifacts

### The exact prompt (verbatim, from github.com/simonw/tools/pull/295)

```
Clone https://github.com/AlexanderGrooff/mermaid-ascii to /tmp

Figure out if you can get it working in WebAssembly, like the most recently
added project in this repo - then build a similar HTML playground called
mermaid-ascii.html but with a ser if examples that fits this Go library
(reusing existing samples from the Rust one if they work)
```

### PR description (verbatim, from github.com/simonw/tools/pull/295)

```
In-browser playground (mermaid-ascii.html) that renders Mermaid flowchart
and sequence diagram source as ASCII / Unicode box-drawing art, using
https://github.com/AlexanderGrooff/mermaid-ascii (MIT) compiled unmodified
to WebAssembly with the standard Go toolchain (GOOS=js GOARCH=wasm).

Follows the pattern of grok-mermaid.html but for the Go library:

- mermaid-ascii/build_wasm.sh clones upstream at a pinned commit, strips
  the cobra CLI and gin web-server entry points (nothing else imports
  them), adds a syscall/js shim exporting renderMermaidAscii(), and
  builds a 3.7 MB module (wasm-opt -Oz; ~1.1 MB gzipped).
- The page renders with the library's "html" style so classDef
  color:#hex classes work, sanitizing the unescaped span output via a
  strict tokenizer + textContent instead of innerHTML.
- Examples cover the features this library actually supports: labeled
  edges, A --> B & C fan-out, subgraphs, <br> multi-line labels,
  classDef colors, and sequence diagrams with alt/loop/par fragments
  and notes (two examples reused from grok-mermaid where compatible).
- Controls: ASCII-only toggle, node padding X/Y, box padding, copy as
  text, permalink via URL fragment.
- tests/test_mermaid_ascii.py: 8 Playwright tests incl. an XSS probe.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01UPeaso82zQbKb67TTSVQ2e
```

### `mermaid-ascii/main.go` — the `syscall/js` shim (verbatim excerpts, from github.com/simonw/tools/pull/295)

The agent-written WASM entry point exposes exactly one function to JavaScript.
Its package doc comment explicitly flags the unescaped-HTML hazard behind
Claim 5 (the reason the page must sanitize rather than use `innerHTML`):

```go
// It exposes a single function to JavaScript:
//
//	renderMermaidAscii(source, {ascii, styleType, direction,
//	                            paddingX, paddingY, borderPadding})
//	  -> {output: string} | {error: string}
//
// With styleType "html", colored text (mermaid classDef ... color:#hex)
// is wrapped in <span style='color: ...'> tags. The values inside those
// tags are NOT escaped by the library, so the page must sanitize the
// output rather than assigning it to innerHTML directly.
```

The exported `render` function wraps the library call in a panic-recovery
`defer` so a Go-side panic degrades to a normal error result instead of
killing the runtime, and `main()` registers the export and blocks forever to
keep it callable:

```go
func render(this js.Value, args []js.Value) (result any) {
	// A panic would otherwise kill the Go runtime and leave the page with a
	// dead render function; recover turns it into a normal error result.
	defer func() {
		if r := recover(); r != nil {
			result = map[string]any{"error": fmt.Sprintf("renderer panic: %v", r)}
		}
	}()
```

```go
func main() {
	logrus.SetLevel(logrus.ErrorLevel)
	js.Global().Set("renderMermaidAscii", js.FuncOf(render))
	// Keep the Go runtime alive so the exported function stays callable.
	select {}
}
```

### `mermaid-ascii/build_wasm.sh` — pinned clone + dependency stripping (verbatim excerpts, from github.com/simonw/tools/pull/295)

The build script clones upstream at a pinned commit (the reproducibility
practice noted in Claim 4):

```bash
UPSTREAM=https://github.com/AlexanderGrooff/mermaid-ascii
# Pinned upstream commit this build is known to work against.
PIN=a4f23212201cbd62b5a8707b7502b281bb18543f
```

...then removes the Cobra CLI and Gin web-server entry points after
identifying (via a code comment asserting import analysis) that only
`cmd/root.go` and `cmd/web.go` import them — the concrete mechanism behind
Claim 4's "nothing else imports them":

```bash
# Strip the CLI (cobra) and web server (gin) so neither ends up in the
# module, along with tests and their fixtures. Only cmd/root.go and
# cmd/web.go import those dependencies; the layout/drawing code in cmd/
# and pkg/ is untouched.
rm main.go cmd/root.go cmd/web.go
rm -rf cmd/*_test.go cmd/testdata pkg/*/*_test.go pkg/diagram/testutil
```

### PR file/change summary (from GitHub API, `simonw/tools#295`)

```
mermaid-ascii.html               added   338 lines
mermaid-ascii.wasm                compiled binary (not text-diffable)
mermaid-ascii/LICENSE            added    21 lines
mermaid-ascii/README.md          added    73 lines
mermaid-ascii/build_wasm.sh      added    64 lines
mermaid-ascii/main.go            added    85 lines
mermaid-ascii/wasm_exec.js       added   575 lines (Go's Wasm runtime shim)
mermaid-ascii/wasm_globals.go    added    13 lines
tests/test_mermaid_ascii.py      added    89 lines

Totals: 9 files changed, 1258 additions, 0 deletions, 1 commit
Commit authored:  2026-07-16T14:44:00Z
PR opened:        2026-07-16T14:56:40Z
PR merged:        2026-07-16T14:57:40Z
```

### Upstream library facts (from GitHub API, `AlexanderGrooff/mermaid-ascii`)

```
Description: "Render Mermaid graphs inside your terminal"
Language:    Go
License:     MIT
Stars:       1,481 (at time of extraction)
Created:     2023-02-24
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-grok-mermaid.md` (entire note): both notes document the same
    author using Claude Code for web (Fable 5) to compile an existing, unmodified
    third-party library into a browser-based WASM playground in a single prompt, on the
    same day, in the same target repo (`simonw/tools`). This note is the direct sequel: it
    reuses the "follow the pattern of [prior project]" prompting shorthand (Claim 3) instead
    of re-specifying the WASM build approach, and Claim 7 (Playwright + XSS test) matches
    the "Playwright TDD" habit documented across that note and
    `blog-simonwillison-liteparse-browser.md`.
  - `blog-simonwillison-opfs-pyodide.md` and `blog-simonwillison-pyodide-asgi-browser.md`:
    both document standalone, no-backend browser tools compiled from another language
    runtime. This note adds a second Go-toolchain WASM instance (`GOOS=js GOARCH=wasm`),
    reinforcing the pattern across a third source-language ecosystem in this corpus (Python,
    Rust, and now Go).

- **Contradicts**: None identified. No existing corpus note makes claims about Go-to-WASM
  compilation, Cobra/Gin dependency stripping, or the AlexanderGrooff/mermaid-ascii library
  that conflict with this source.

- **Extends**:
  - `blog-simonwillison-grok-mermaid.md` Claim 4 (the `ratatui`-shim dependency-isolation
    decision in the Rust port): this note's Claim 4 documents the same underlying skill
    (identify and remove the minimum blocking dependency surface for a WASM target) applied
    to a different problem shape — instead of reimplementing a narrow slice of a UI
    library's *types*, the agent here deletes two entire unused *entry-point* frameworks
    (Cobra CLI, Gin web server) after confirming via import analysis that nothing else
    depends on them. Together the two notes show the same dependency-isolation judgment
    call recurring across two different source languages and two different classes of
    blocking dependency (a UI-styling crate vs. CLI/server frameworks).
  - `blog-simonwillison-grok-mermaid.md` Claim 3 (the original WASM-porting prompt template):
    this note's Claim 3 shows the same practitioner reusing that established pattern via a
    much shorter prompt that points back at "the most recently added project in this repo"
    rather than re-specifying build-target, deliverable-format, and license-handling
    instructions from scratch — evidence that once a WASM-porting workflow has been
    demonstrated once in a repo, a much lower-effort prompt suffices to repeat it for a new
    source library.

- **Novel**:
  - **Building a second AI-compiled port of the same capability specifically to benchmark
    it against a first** (Claim 2): no existing corpus source documents deliberately
    building two independent library ports (different upstream projects, different source
    languages) to compare them side by side. Prior WASM-porting notes in this corpus each
    document a single library.
  - **Agent-driven removal of unused CLI/web-server entry-point frameworks (not just
    type-level shimming) to satisfy a WASM build target** (Claim 4): distinct from the
    `ratatui` type-shimming approach in the companion note; this is whole-dependency-tree
    deletion verified by import analysis, a different resolution strategy for the same class
    of "native library isn't WASM-portable as-is" problem.
  - **Unprompted XSS mitigation (tokenizer + `textContent`) plus a dedicated XSS regression
    test, for HTML output from a third-party library the agent didn't otherwise modify**
    (Claims 5, 7): no other AI-tool-porting note in this corpus documents an agent
    identifying and closing an injection vector introduced by wiring an unmodified
    third-party library's output into a web page.
  - **A GitHub App-level Claude Code automation layer with an observed failure ("Claude
    encountered an error") on a PR that still merged successfully** (Claim 9): first corpus
    documentation of this specific repo-level automation artifact, distinct from the
    "Claude Code for web" session-based workflow that authored the actual commit.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add Claim 2 as a distinct instance of an AI-native
  workflow habit not yet in the corpus: when comparing implementation options (here, two
  competing open-source libraries solving the same problem), a low-cost way to evaluate
  them is to have an agent independently compile each to the same target (WASM) and try
  them side by side, rather than reading source code or documentation comparisons. Also
  cite Claim 3 alongside `blog-simonwillison-grok-mermaid.md` Claim 3: once a practitioner
  has demonstrated a WASM-porting workflow once in a repo, later repeats of that workflow
  can be prompted with a much shorter "do it like the last one" instruction instead of
  re-specifying the full build-target/deliverable/license instructions.
- **Chapter 02 (Harness Engineering / practitioner patterns)**: Cite Claim 4 as a second,
  differently-shaped example (alongside the `ratatui` shim in the companion note) of an
  agent resolving a WASM-compatibility blocker by identifying and removing the *minimum*
  dependency surface actually blocking the build — here, entire unused CLI/web-server
  entry-point packages, verified via import analysis before deletion — rather than
  attempting a full recompile of the blocking dependency. Cite Claims 5 and 7 as a concrete
  example worth adding to any guide section on agent-driven security hygiene: when an agent
  is asked to wire a third-party library's raw HTML output into a browser page, it can
  proactively add output sanitization and a regression test for it, without being asked to.
- **Chapter 04 (Practitioner Patterns) / Chapter 09 (Observability)**: If either chapter
  discusses repo-level Claude Code GitHub App automation (as opposed to interactive Claude
  Code for web sessions), Claim 9 is a small but concrete data point that such automation
  can fail silently on a PR ("Claude encountered an error") without blocking the PR's merge
  — worth flagging if the guide makes any claim that GitHub App-driven Claude Code
  automation reliably succeeds or blocks merges on failure.

## Extraction Notes

- The blog post itself is four sentences (~60 words) plus a screenshot; the substantive
  technical content lives entirely in the linked GitHub PR (`simonw/tools#295`), which was
  read in full via `gh api` (PR body, commit list, file list, and issue comments) rather
  than relying on WebFetch's summarizer, so every quote above could be checked
  character-for-character against source text. The upstream library repo
  (`AlexanderGrooff/mermaid-ascii`) was also queried via `gh api` for basic facts (stars,
  license, language, creation date) used in Source Context and Concrete Artifacts.
- The companion blog post from the same day (`blog-simonwillison-grok-mermaid.md`'s
  source, `simonwillison.net/2026/Jul/16/grok-mermaid/`) and its PR (`simonw/tools#293`)
  were re-read to verify the cross-references above are accurate rather than assumed from
  memory of the existing source note.
- The live tool (`tools.simonwillison.net/mermaid-ascii`) was checked via WebFetch and
  confirmed to describe the same build (WASM module size, `syscall/js` shim, MIT
  attribution to AlexanderGrooff) but is a WASM application shell with no additional
  extractable prose beyond what the PR body already covers in more detail.
- The PR body's linked Claude.ai session (`https://claude.ai/code/session_01UPeaso82zQbKb67TTSVQ2e`)
  was not followed: it requires Claude.ai authentication and is outside what an
  unauthenticated fetch can retrieve. This means no session transcript, duration, or
  step-by-step reasoning is available for this extraction — Claim 8's "~13 minutes"
  figure is a commit-to-merge timestamp gap, not a session-duration measurement, and is
  described as such rather than conflated with actual working time.
- Two issue comments on the PR were queried via `gh api` (Claim 9): one is a boilerplate
  "I'll analyze this and get back to you" acknowledgment, the other links a GitHub Actions
  run with the message "Claude encountered an error." Neither the triggering event nor the
  resolution is documented in the PR itself; this is reported as an observed, unexplained
  artifact rather than interpreted further.
- No contradictions with existing corpus notes were identified; no contradiction issue was
  filed per MINER.md §4a.
