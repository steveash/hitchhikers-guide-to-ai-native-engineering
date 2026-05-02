---
source_url: https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/
source_type: blog-post
title: "Extract PDF text in your browser with LiteParse for the web"
author: Simon Willison
date_published: 2026-04-23
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: anecdotal
issue: "#474"
---

# Extract PDF text in your browser with LiteParse for the web

> A documented 59-minute Claude Code session that browser-ported LlamaIndex's
> LiteParse PDF tool from Node.js to client-side TypeScript, demonstrating:
> (a) spatial text parsing + Visual Citations as browser-native RAG preprocessing
> patterns for Ch04; and (b) a concrete harness workflow — mobile exploration →
> notes.md → plan.md → Playwright TDD → small commits → parallel sessions →
> queue-based prompting → cross-model audit — for Ch02.

## Source Context

- **Type**: blog-post (Willison practitioner experience report; ~1,200 words;
  links to a public GitHub repo, live demo, shared Claude Code transcript, and
  a detailed plan.md. The plan.md was read separately for this extraction.)
- **Author credibility**: Simon Willison is the creator of Django, creator of
  the `llm` CLI, and one of the most widely-cited independent commentators on
  LLM tooling. He is a designated `trusted-feed` source in this repo. This post
  documents work he did himself — a first-person observation report with publicly
  verifiable artifacts (live app at `simonw.github.io/liteparse/`, public GitHub
  repo, shared Claude transcript). No affiliation with Anthropic or LlamaIndex.
- **Scope**: Covers one build session — porting LlamaIndex's LiteParse PDF parser
  from Node.js to a browser-native TypeScript web app, deployed to GitHub Pages.
  The post is notable for documenting *both* the technical result (browser PDF
  pipeline) *and* the full harness workflow used to produce it. Does NOT cover:
  enterprise harness patterns, multi-session long-running workflows, team patterns,
  or performance benchmarks. The vibe coding framing (Willison reviewed zero lines
  of generated code) is explicitly discussed and risk-justified by the author.
  The plan.md (89 lines, 12 test cases, full architecture) was read as a
  supplementary artifact.

## Extracted Claims

### Claim 1: Browser-native PDF processing (PDF.js + Tesseract.js) enables fully client-side document-to-text pipelines with no server round-trips

- **Evidence**: The resulting app processes PDFs entirely in-browser using PDF.js
  for page rendering and Tesseract.js for OCR, with no data sent to any server.
  Willison verified via the browser network panel: "no private data is transferred
  anywhere." The app is publicly live at `simonw.github.io/liteparse/`.
- **Confidence**: settled (publicly verifiable live demo; the two libraries used
  are established browser-compatible tools)
- **Quote**: "All of the processing happens entirely in my browser—I checked the
  network panel and no private data is transferred anywhere."
  — Simon Willison, simonwillison.net/2026/Apr/23/liteparse-for-the-web/
- **Our assessment**: This is the first in-corpus documentation of a fully
  browser-native PDF-to-text pipeline as a RAG preprocessing pattern. The
  architectural implication is significant: for privacy-sensitive document
  workflows (legal, healthcare, personal finance), browser-side extraction
  eliminates the server-side data handling requirement entirely. The same two
  libraries (PDF.js, Tesseract.js) are available in React, Vue, and vanilla JS
  environments without bundler complications, making this a portable pattern.
  The tradeoff is bundle size and first-load latency (Tesseract WASM is large);
  the plan.md explicitly notes the CDN default for Tesseract traineddata and
  the lazy-load mitigation.

### Claim 2: LiteParse's "spatial text parsing" uses classical heuristics — not LLMs — to detect multi-column PDF layouts and extract reading-order text

- **Evidence**: Willison quotes LlamaIndex's documentation: LiteParse uses
  "good old-fashioned PDF parsing, falling back to Tesseract OCR (or other
  pluggable OCR engines) for PDFs that contain images." The spatial text parsing
  detects "the infuriating vagaries of PDF layouts" through "clever heuristics
  to detect things like multi-column layouts." The JSON output includes text
  dimensions, positioning, and font detection metadata.
- **Confidence**: emerging (LlamaIndex's own documentation; no independent
  benchmark of quality vs. LLM-based extraction in this post)
- **Quote**: "LiteParse uses 'good old-fashioned PDF parsing, falling back to
  Tesseract OCR... for PDFs that contain images'" — LlamaIndex docs, quoted
  by Willison
- **Our assessment**: Classical heuristic parsing is cheaper and faster than
  LLM-based document understanding for structured PDFs. The tradeoff: heuristics
  handle standard multi-column layouts well but break on non-standard layouts
  (tables without borders, overlapping text blocks). For RAG pipelines where
  documents are known-format (financial reports, academic papers, government
  docs), classical spatial parsing is the right first choice — LLM-based
  fallback is warranted only for non-standard documents. The JSON output with
  positioning metadata also enables the Visual Citations pattern (Claim 3) as a
  first-class capability, which LLM-based extraction does not naturally produce.

### Claim 3: Visual Citations with Bounding Boxes — serving highlighted page image crops alongside extracted text — increases RAG answer credibility

- **Evidence**: LiteParse supports a "Visual Citations with Bounding Boxes"
  pattern (referenced in the LlamaIndex docs linked from the post). The JSON
  output from spatial parsing includes bounding box coordinates for extracted
  text, enabling downstream code to crop and highlight the specific source region
  of a PDF answer. The browser version generates optional page screenshots to
  support this pattern.
- **Confidence**: emerging (the pattern is documented in LlamaIndex's own
  tooling; no controlled user study of credibility is cited in this post)
- **Quote**: (pattern name from LlamaIndex documentation; Willison implements
  the screenshot generation component)
- **Our assessment**: The bounding-box citation pattern is a practitioner
  answer to the "where did this answer come from?" question in RAG Q&A. By
  returning a highlighted image crop of the source PDF region alongside the
  extracted text, the system lets users verify answers without leaving the app.
  This is corroborated by the `blog-simonwillison-muse-spark.md` note on
  `container.visual_grounding`'s three-mode output (bbox/point/count) — the
  commercial AI vendors independently arrived at structured localization output
  as a first-class capability. No existing guide chapter currently addresses
  visual grounding as a citation technique for document RAG; this would be a
  new addition to Ch04.

### Claim 4: Mobile → Desktop pipeline: starting exploration on phone with Claude chat for feasibility, switching to Claude Code on laptop for implementation

- **Evidence**: Willison explicitly documents the two-phase inception: he
  uploaded a PDF and ran `"Clone https://github.com/run-llama/liteparse and try
  it against this file"` on his iPhone using regular Claude chat, then asked
  `"Does this library run in a browser? Could it?"`. Only after getting a
  positive feasibility answer did he switch to his laptop and start Claude Code.
- **Confidence**: anecdotal (one practitioner's described approach; no
  controlled comparison with going directly to laptop)
- **Quote**: "I started on my iPhone, using regular Claude chat... I then
  switched to my laptop and Claude Code to actually build it."
  — paraphrase from post structure; Willison explicitly describes the two-phase
  flow
- **Our assessment**: This is a concrete two-phase inception pattern for
  avoiding sunk costs on infeasible ideas before committing to implementation.
  The mobile-first exploration uses the lower-friction Claude chat interface for
  a quick "is this possible?" check, reserving the Claude Code harness for
  implementation. The pattern is particularly useful when the feasibility
  question involves an unfamiliar library — the phone session produces a quick
  technical read before any environment setup or forking work. This is the first
  in-corpus documentation of this specific two-phase mobile → desktop workflow.

### Claim 5: Notes.md → Plan.md context injection: pasting prior research into notes.md, asking Claude Code to read it and write plan.md before touching any code

- **Evidence**: Willison explicitly documents the handoff: he pasted the output
  of the Claude mobile chat into `notes.md`, then opened Claude Code and
  prompted: `"Get this working as a web app... Read notes.md for initial
  research on this problem, then write out plan.md with your detailed
  implementation plan"`. The resulting plan.md (89 lines, full architecture,
  12 Playwright test cases) is publicly available and was read for this
  extraction.
- **Confidence**: anecdotal (one practitioner's approach, but the prompt is
  verbatim and the artifacts are verifiable)
- **Quote**: "Read notes.md for initial research on this problem, then write
  out plan.md with your detailed implementation plan"
  — Simon Willison, simonwillison.net/2026/Apr/23/liteparse-for-the-web/
- **Our assessment**: This is the first in-corpus documentation of this
  specific two-file context injection pattern with named files. The pattern
  externalizes prior research into Claude Code's working memory via a named
  artifact (notes.md) rather than a long system prompt or inline context dump.
  Having Claude Code *write* plan.md (rather than receive it as input) surfaces
  the agent's interpretation of the prior research — if the plan misunderstands
  the notes, the human can correct it before any code is written. The plan.md
  artifact is then persistent context for the rest of the session. This is
  distinct from CLAUDE.md as a persistent rule file — plan.md is a per-session
  task artifact, not a cross-session configuration file.

### Claim 6: Plan iteration before "build it": reviewing and correcting the plan's scope is a mandatory step before executing

- **Evidence**: After Claude Code wrote plan.md, Willison reviewed it and found
  that screenshot generation had been deferred. He prompted: `"Update the plan
  to say we WILL do the canvas-encode swap so the screenshots thing works"`. He
  then deemed the plan "strong enough to implement" before running `"build it."`.
- **Confidence**: anecdotal (one practitioner's described approach)
- **Quote**: "Update the plan to say we WILL do the canvas-encode swap so the
  screenshots thing works" — Simon Willison, verbatim prompt, same post
- **Our assessment**: The plan iteration step is what prevents the agent from
  making scope decisions the human wouldn't endorse. In this case, Willison
  explicitly corrected the agent's instinct to defer a feature to "v2," asserting
  that screenshots were in scope for v1. The plan-then-approve-then-build loop
  is a first-class workflow step, not an optional extra. Without the scope
  correction, the agent would have shipped a v1 without screenshots — a choice
  Willison explicitly did not want. This corroborates Claim 10 in
  `blog-addyosmani-code-agent-orchestra.md` (specification imperative: vague
  thinking multiplies errors) and makes it concrete: the plan review is *where*
  vagueness is corrected, before it propagates into implementation.

### Claim 7: Red/green TDD with Playwright is a repeatable prompt habit for establishing correctness harnesses around Claude Code output

- **Evidence**: Willison's prompt: `"When you implement this use playwright and
  red/green TDD, plan that too"`. The resulting plan.md documents 12 specific
  test cases with explicit TDD discipline: "one failing test at a time, watch
  it fail with expected error before implementing, minimum code to pass green,
  refactor only on green, commit per test, no code without failing test." The
  tests covered mobile viewport, cross-browser compatibility, OCR behavior,
  clipboard, error handling, and responsive layout.
- **Confidence**: anecdotal (one practitioner's consistent practice — but
  Willison applies this across multiple documented projects, so it's a
  repeatable habit, not a one-off)
- **Quote**: "When you implement this use playwright and red/green TDD, plan
  that too" — Simon Willison, verbatim prompt, same post
- **Our assessment**: Asking Claude Code to include TDD in the plan (not as a
  separate instruction but as part of the planning step) is the operationally
  important detail — the test structure becomes part of the agent's
  implementation contract, not a post-hoc check. The 12-test plan in plan.md
  is directly derivable from this single prompt addition. Willison notes he
  applied this habit across multiple projects ("I've written more about this
  pattern in my agentic engineering guides"), making it a recommended repeatable
  habit rather than project-specific configuration.

### Claim 8: "Small commits along the way" is a repeatable prompt addition that improves reviewability and may help agent focus

- **Evidence**: Willison adds `"small commits along the way"` to his standard
  prompt set. His stated reasons: creates "code that's easier to understand or
  review later on," and potentially helps the agent focus by "encouraging it to
  plan what it's working on and tackle one problem at a time."
- **Confidence**: anecdotal (one practitioner's consistent practice across
  multiple documented projects — CSRF note, this post)
- **Quote**: "small commits along the way" — Simon Willison, verbatim prompt,
  same post
- **Our assessment**: The dual rationale (reviewer benefit + potential agent
  benefit) is worth noting. The reviewer benefit is well-established engineering
  practice (small atomic commits are easier to understand). The agent-focus
  hypothesis is Willison's own speculation and should not be stated as settled.
  This pattern is corroborated by `blog-simonwillison-csrf-multimodel-review.md`
  Claim 1, where 10-commit structure was used for a security-sensitive migration
  — the same habit applied in a higher-stakes context.

### Claim 9: Parallel Claude Code sessions against the same repository serve independent tasks without conflict

- **Evidence**: While the main Claude Code session was building the app, Willison
  launched a separate Claude Code instance on the same directory to ask
  operational questions (how to run the dev server). A third session was later
  started specifically for GitHub Actions CI/CD configuration. The sessions ran
  independently and produced non-conflicting output.
- **Confidence**: anecdotal (one practitioner, one project — but the post
  explicitly describes this as a deliberate practice)
- **Quote**: (paraphrase) While one session built the main app, Willison
  started a separate session for GitHub Actions setup — a fresh instance
  that could focus on one concern without inheriting the build session's context
- **Our assessment**: The key condition enabling parallel sessions is task
  independence — the CI/CD setup task had no dependency on the in-progress
  build session. The pattern is analogous to git worktrees for parallelism
  (Claim 11 in `blog-addyosmani-code-agent-orchestra.md`) but at the session
  level rather than the file system level. The three sessions (exploration,
  main build, CI/CD) naturally decomposed by concern: one per bounded task.

### Claim 10: Queue-based prompting lets practitioners add prompts while Claude Code is mid-task; the queue is recoverable from `~/.claude/projects/`

- **Evidence**: Willison describes queuing additional prompts while Claude Code
  was working ("caught up on Duolingo"). He notes these queued prompts do not
  appear in exported transcripts but can be extracted via:
  `rg queue-operation --no-filename | grep enqueue | jq -r '.content'`
  run against the relevant directory in `~/.claude/projects/`.
- **Confidence**: settled (the command is specific and verifiable; the queue
  mechanism is a documented Claude Code feature)
- **Quote**: `rg queue-operation --no-filename | grep enqueue | jq -r '.content'`
  — Simon Willison, verbatim recovery command, same post
- **Our assessment**: The queue recovery command is a concrete, practical
  technique for reconstructing what prompts drove a session — useful for audit,
  for session replay, and for writing accurate post-hoc documentation. The fact
  that queued prompts are *not* in exported transcripts is a gap in the standard
  session export tooling; this recovery command fills it. This is the first
  in-corpus documentation of this command.

### Claim 11: Cross-model audit for shortcuts detection: asking a second model to describe the implementation independently verifies that the first model didn't fake features

- **Evidence**: Willison prompted GPT-5.5 (via OpenAI preview access): `"Describe
  the difference between how the node.js CLI tool runs and how the web/ version
  runs"`. GPT-5.5's accurate description gave him "confidence that Claude hadn't
  taken any project-threatening shortcuts."
- **Confidence**: anecdotal (one practitioner, one session — but the technique
  is intentional and the audit prompt is verbatim)
- **Quote**: "Describe the difference between how the node.js CLI tool runs and
  how the web/ version runs" — Simon Willison, verbatim GPT-5.5 prompt, same post
- **Our assessment**: This is a semantic audit, not a code review. Rather than
  reading the code, Willison asked a second model to explain what the code does —
  a technique that catches the class of shortcuts where the agent produces
  plausible-looking code that doesn't actually implement the requested feature.
  A model that faked the browser port would be unable to accurately describe the
  architectural difference between Node.js and browser execution. This extends
  `blog-simonwillison-csrf-multimodel-review.md` Claim 2 (cross-model code review
  for security changes) with a different audit framing: implementation description
  rather than code review. The two techniques cover different failure modes:
  code review catches code-level bugs; implementation description catches
  architectural shortcuts.

### Claim 12: Blast-radius-justified vibe coding: choosing static hosting + local processing makes zero-code-review delegation acceptable for certain app types

- **Evidence**: Willison explicitly defends coding with zero code review
  ("I have not looked at a _single line_ of the HTML and TypeScript written
  for this project") on risk grounds: the app runs locally (no server-side
  execution), processes data entirely in the browser (no data exfiltration
  surface), and is deployed to static hosting (no backend attack surface). He
  distinguishes this from "irresponsible" vibe coding by pointing to the
  architectural choices that constrain the blast radius.
- **Confidence**: anecdotal (one practitioner's framing — but the reasoning
  is explicit and logically coherent; Willison has written independently about
  vibe coding at simonwillison.net/2025/Mar/19/vibe-coding/)
- **Quote**: "I have not looked at a _single line_ of the HTML and TypeScript
  written for this project." — Simon Willison, same post
- **Our assessment**: This is the first in-corpus treatment of vibe coding as
  a risk-management decision rather than a careless one. The framework implied:
  (1) choose a static hosting target; (2) do all processing locally; (3) verify
  no data egress via network panel; (4) then code review avoidance is acceptable.
  The guide should not prescribe vibe coding, but should document this framework
  for practitioners who want to know *when* it's acceptable. The contrast with
  `blog-simonwillison-csrf-multimodel-review.md` (close human guidance, 10
  commits, cross-model review for security-critical changes) shows Willison
  applying risk-calibrated review intensity — not a uniform "always review" or
  "never review" rule.

### Claim 13: GitHub Pages + Vite is a zero-cost, zero-risk deployment target worth delegating entirely to Claude Code

- **Evidence**: Willison's GitHub Actions setup prompt produced a complete
  CI/CD workflow (deploy on push, run tests, GitHub Pages deploy of built Vite
  app) in a fresh Claude Code session. He values GitHub Pages for projects
  because it enables "zero-cost deployment with whatever build step is
  necessary" and works even for private repositories with secret URLs.
- **Confidence**: anecdotal (one practitioner's preference, but with strong
  practical backing — GitHub Pages and Vite are both stable, widely-used tools)
- **Quote**: "Look at the web/ folder - set up GitHub actions for this repo
  such that any push runs the tests, and if the tests pass it then does a
  GitHub Pages deploy of the built vite app..."
  — Simon Willison, verbatim CI/CD prompt, same post
- **Our assessment**: The delegation pattern (fresh Claude Code session for
  CI/CD setup, with a complete task description) is the transferable piece.
  The specific technologies (GitHub Pages, Vite) are a current practitioner
  recommendation, not the abstract principle. The pattern is: for infrastructure
  setup that is bounded and independent from the main build, a fresh session
  with a complete task description produces a working result without needing
  context from the main session.

### Claim 14: A full browser PDF parsing app was built in 59 minutes of Claude Code work with minimal human interruption

- **Evidence**: Willison reports the core "build it" phase took 59 minutes in
  Claude Code. During this time, he "caught up on Duolingo" while queuing
  follow-up prompts. The output was a cross-browser, mobile-responsive,
  Playwright-tested TypeScript web app, deployed to GitHub Pages.
- **Confidence**: anecdotal (single session, self-reported time; the output
  is publicly verifiable but the clock time is not independently measurable)
- **Quote**: "The whole 'build it' step took 59 minutes in Claude Code."
  — Simon Willison, same post
- **Our assessment**: 59 minutes for a full browser app (file input, OCR
  toggle, screenshot generation, dual text+JSON output, clipboard, mobile
  responsive, cross-browser tested) is a concrete data point for setting
  expectations about autonomous session scope. This is larger in scope than
  the `blog-simonwillison-servo-crate-exploration.md` servo-shot tool but
  comparable in autonomy level. Three in-corpus examples (servo, Codex plugin,
  liteparse) from the same practitioner converge on single-session delivery of
  non-trivial outputs — enough to state this as a pattern for the guide, not
  just an anecdote.

## Concrete Artifacts

### The complete harness workflow (verbatim prompts in sequence)

```
Phase 0 — Mobile feasibility exploration (iPhone, Claude chat):
  "Clone https://github.com/run-llama/liteparse and try it against this file"
  "Does this library run in a browser? Could it?"

Phase 1 — Context injection (laptop, Claude Code):
  "Get this working as a web app. index.html, when loaded, should render an
   app that lets users open a PDF in their browser and select OCR or non-OCR
   mode... Read notes.md for initial research on this problem, then write out
   plan.md with your detailed implementation plan"

Phase 2 — Plan refinement:
  "Update the plan to say we WILL do the canvas-encode swap so the screenshots
   thing works"
  [other scope corrections]
  "strong enough to implement"

Phase 3 — Execution:
  "When you implement this use playwright and red/green TDD, plan that too"
  "let's use PDF.js's own renderer"
  "small commits along the way"
  "build it."

Phase 4 — Queue-based follow-up (while session runs):
  "The final UI should include both the text and the pretty-printed JSON
   output... both with copy-to-clipboard buttons"
  "Run OCR should be unchecked by default"
  "When 'Copy' is clicked the text should change to 'Copied!' for 1.5s"
  [safari compatibility fix prompts]
  [layout refinement prompts via screenshot]

Phase 5 — CI/CD (fresh Claude Code session):
  "Look at the web/ folder - set up GitHub actions for this repo such that
   any push runs the tests, and if the tests pass it then does a GitHub Pages
   deploy of the built vite app such that the web/index.html page is the
   index.html page for the thing that is deployed and it works on GitHub Pages"

Phase 6 — Cross-model audit (GPT-5.5 via OpenAI preview):
  "Describe the difference between how the node.js CLI tool runs and how the
   web/ version runs"
```

*Source: Simon Willison, simonwillison.net/2026/Apr/23/liteparse-for-the-web/*

### Queue recovery command for Claude Code sessions

```bash
# Run inside ~/.claude/projects/<your-project-dir>/
rg queue-operation --no-filename | grep enqueue | jq -r '.content'
```

*Recovers queued prompts that do not appear in standard exported transcripts.*
*Source: Willison, same post. First in-corpus documentation of this command.*

### plan.md architecture summary (generated by Claude Code from notes.md)

```
Architecture:
  web/index.html            — UI shell
  web/main.ts               — UI wiring
  web/liteparse-browser.ts  — browser-safe parser entry
  web/pdfjs-renderer.ts     — PDF.js-based renderer (replaces PDFium)

Key technical decisions:
  1. Replace PDFium + Sharp with PDF.js canvas rendering
  2. Node module shimming via Vite aliases (fs, path, os → empty stubs)
  3. OCR via Tesseract.js Web Workers + WASM (CDN default for traineddata)
  4. OffscreenCanvas.convertToBlob() for PNG encoding (same Uint8Array shape)
  5. PDF-only input with magic number check (%PDF-)

TDD: 12 Playwright test cases, one failing test at a time, commit per test

Risks mitigated:
  - CORS on file:// (require vite dev or static server)
  - Bundle size (lazy-load Tesseract)
  - Top-level await + worker interplay (smoke test)

Total estimated build time: 3.5–4 days
Actual build time: 59 minutes (autonomous Claude Code session)
```

*Source: github.com/simonw/liteparse/blob/web/plan.md — generated by Claude Code
from notes.md as the first step of the session.*

### Cross-model audit technique

```
Second-model audit prompt template (semantic, not code-review):
  "Describe the difference between how [the original version] runs and how
   [the new version] runs."

Purpose: Detect architectural shortcuts — faked features, unimplemented browser
         ports, incorrect behavioral claims — that code review might miss.

Used here: GPT-5.5 describing the difference between the Node.js CLI and the
           browser web/ version, to verify the browser port was real.

Contrast with blog-simonwillison-csrf-multimodel-review.md:
  - That note: GPT-5.4 reviews production security code (code-level review)
  - This note: GPT-5.5 describes the architecture (semantic/behavioral audit)
  Two complementary verification patterns from the same practitioner.
```

*Source: Willison, same post.*

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-csrf-multimodel-review.md** (Claims 1, 2): Both notes
    document Willison using small commits + a second model as an independent
    auditor. The CSRF note applies these patterns to security-critical work under
    close human guidance; the liteparse note applies them to low-blast-radius
    vibe coding with zero code review. Together they show these as consistent
    Willison practices *calibrated* to risk context — not uniform rules.
  - **blog-simonwillison-servo-crate-exploration.md** and
    **blog-simonwillison-gpt55-codex-plugin.md** (single-session delivery pattern):
    Three in-corpus examples from the same practitioner — servo (library
    bootstrapping), Codex plugin (OAuth reverse-engineering), and liteparse
    (browser port + full UI). All three deliver publicly verifiable artifacts in
    a single Claude Code session. Three examples from the same author establish
    this as a repeatable workflow pattern, not an anecdote.
  - **blog-addyosmani-code-agent-orchestra.md** (Claim 10 — specification
    imperative): Osmani says "vague thinking multiplies errors across agent
    fleets." The plan.md iteration step (Claim 6 here) is the concrete mechanism
    by which Willison prevents vague thinking from reaching code: the plan review
    is where scope ambiguity is corrected before it propagates.
  - **blog-addyosmani-code-agent-orchestra.md** (Claim 7 — LLM-generated AGENTS.md
    harmful): Willison's plan.md pattern is an instance of human-guided planning
    artifacts rather than auto-generated context files. The plan is generated by
    Claude Code but reviewed and corrected by the human — consistent with the
    distinction between "developer-written, surgically-focused" context files
    (good) and auto-generated bloat (bad).

- **Contradicts**: None. The CSRF note's "closely guided 10 commits" and this
  note's "59-minute autonomous build" are not contradictory — they reflect
  different risk contexts, and Willison explicitly conditions both on blast
  radius.

- **Extends**:
  - **blog-simonwillison-servo-crate-exploration.md** and
    **blog-simonwillison-gpt55-codex-plugin.md**: Both document "give Claude
    Code a repo and a goal" but do not document the Notes.md → Plan.md multi-step
    harness structure. This post adds the full workflow scaffolding that the other
    two posts elide.
  - **blog-simonwillison-csrf-multimodel-review.md**: The multi-model audit
    pattern there (implementation by Claude Code, GPT-5.4 code review) is
    extended here with a different audit technique: asking the second model to
    *describe* the implementation rather than *review* the code. Two complementary
    audit strategies from the same practitioner.
  - **blog-simonwillison-muse-spark.md** (Claim 6 — visual_grounding as a tool
    primitive): The muse-spark note documents `container.visual_grounding` returning
    structured bounding boxes in meta.ai's commercial harness. The Visual Citations
    with Bounding Boxes pattern here is the same concept applied to PDF document
    processing: bounding box coordinates from spatial text parsing enable
    cropped image citations in RAG Q&A. Two independent paths to the same
    architectural pattern.

- **Novel**:
  - **Notes.md → Plan.md context injection as a named, explicit harness step**:
    No existing note documents this two-file handoff pattern with named files as
    an explicit, repeatable workflow. The specific convention (notes.md for prior
    research, plan.md for the session task artifact) is new to the corpus.
  - **Browser-native PDF-to-text pipeline (PDF.js + Tesseract.js)**:
    No existing note covers browser-native document-to-text extraction as a
    pattern for client-side RAG preprocessing. This is the first in-corpus
    source on this architecture.
  - **Blast-radius-justified vibe coding as an architectural decision criterion**:
    No existing note frames the choice of static hosting + local processing as
    a *risk management strategy* that unlocks more aggressive AI delegation. This
    is a new pattern: using architecture to reduce blast radius in order to
    increase delegation latitude.
  - **Queue recovery command (`rg queue-operation | grep enqueue | jq`)**:
    The specific command for extracting queued prompts from `~/.claude/projects/`
    is not documented anywhere else in the corpus. Concrete, verifiable,
    immediately usable.
  - **Semantic cross-model audit (describe the implementation)**:
    The specific audit technique — asking the second model to describe the
    architecture to detect shortcuts — is not documented elsewhere. The CSRF
    note covers code-level cross-model review; this is the behavioral/semantic
    variant.
  - **Mobile → Desktop two-phase inception pipeline**:
    No other source documents the specific pattern of using mobile Claude chat
    for feasibility and switching to Claude Code for implementation. New to corpus.

## Guide Impact

- **Chapter 04 (Context Engineering — Document Preprocessing)**:
  Currently the chapter does not address browser-native document pipelines.
  Recommend adding: "For privacy-sensitive document workflows, PDF.js +
  Tesseract.js enables fully client-side PDF-to-text extraction with no server
  round-trips. LiteParse's spatial text parsing (classical heuristics for
  multi-column layout detection) is a faster, cheaper alternative to LLM-based
  extraction for known-format PDFs. The Visual Citations pattern — returning
  bounding-box coordinates alongside extracted text — lets downstream UI serve
  highlighted page crops as answer citations." Cite this source at `[emerging]`,
  corroborated by muse-spark's `visual_grounding` tool primitive.

- **Chapter 02 (Harness Engineering — Session Structure)**:
  Recommend adding the Notes.md → Plan.md workflow as an explicit named pattern
  for session context injection: "Before writing any code, paste prior research
  into `notes.md`, then ask Claude Code to read it and write `plan.md`. Review
  and correct the plan — especially scope inclusions/exclusions — before running
  `build it`." Three in-corpus examples (servo, gpt55-codex-plugin, liteparse)
  now support the "give Claude Code a goal" pattern; liteparse is the first to
  document the full harness scaffolding (notes → plan → build).

- **Chapter 02 (Harness Engineering — Prompt Habits)**:
  The "small commits" and Playwright TDD prompts are repeatably documented across
  multiple Willison posts. Recommend elevating them from "tips" to named prompt
  habits: "`small commits along the way`" and `"use playwright and red/green TDD,
  plan that too"`. Both are single-sentence prompt additions with disproportionate
  downstream benefits (reviewability, correctness harness). The queue recovery
  command belongs in a "session audit" section of Ch02.

- **Chapter 01 (Daily Workflows — Inception Patterns)**:
  Recommend adding the mobile → desktop two-phase inception pattern. Also
  recommend adding queue-based prompting (Claim 10) as a documented async
  working style — Claude Code sessions do not require constant human supervision;
  practitioners can queue follow-up prompts and do other work.

- **Chapter 03 (Safety and Verification — Risk-Calibrated Delegation)**:
  Recommend adding a framework for blast-radius-justified delegation latitude:
  "When your app is statically hosted, processes data entirely locally, and
  transfers no user data externally (verify via network panel), code-review
  avoidance is more acceptable than in server-executed, data-handling code." Cite
  this source alongside `blog-simonwillison-csrf-multimodel-review.md` to show the
  contrast: close review for security changes, delegated review for static apps.

## Extraction Notes

- **plan.md read in full**: The plan.md linked from the post
  (`github.com/simonw/liteparse/blob/web/plan.md`) was fetched and read
  completely. It is 89 lines covering architecture, technical decisions, 12
  Playwright test cases, phase structure, risks/mitigations, and time estimates.
  It is a primary artifact — not supplementary — and was used to extract Claims
  5, 6, 7, and the plan.md Concrete Artifact.
- **Shared Claude transcript not read**: The shared Claude conversation
  (`claude.ai/share/44a5ed86-...`) requires authentication and was not accessible
  via WebFetch. The post's own narration provided sufficient prompt coverage.
- **Agentic engineering patterns guide**: Willison's guide at
  `simonwillison.net/guides/agentic-engineering-patterns/` was fetched.
  It corroborates the TDD and small-commits patterns but does not add new claims
  beyond what's in this post; its content is captured through this post's
  references.
- **Fragment URL**: The issue body includes `#atom-everything` (Atom feed
  anchor). `source_url` uses the canonical page URL without the fragment.
- **Three Prospector triage comments**: Three separate triage runs were filed.
  The extraction integrates all three: Ch04 (document processing), Ch02 (harness
  workflow patterns), and the full multi-chapter impact. No conflicts between
  the three triages; they are complementary in scope.
- **Novelty assessment**: The Prospector assessed novelty as "high" (first
  triage) and "medium" (third triage). The workflow patterns (Ch02) are high
  novelty; the document processing patterns (Ch04) are medium novelty (PDF
  ingestion is a known problem). Both assessments are captured accurately in the
  individual claim confidence ratings.
