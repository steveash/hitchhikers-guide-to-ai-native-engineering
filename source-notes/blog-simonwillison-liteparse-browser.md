---
source_url: https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/
source_type: blog-post
title: "Extract PDF text in your browser with LiteParse for the web"
author: Simon Willison
date_published: 2026-04-23
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: anecdotal
issue: "#474"
---

# Extract PDF text in your browser with LiteParse for the web

> A documented 59-minute Claude Code session (with Opus 4.7) that ships a browser-native PDF extraction app using a notes.md → plan.md context handoff, Playwright TDD, queue-based prompting, parallel sessions, and a GPT-5.5/Codex cross-model audit — providing the most complete in-corpus example of the full AI-native development workflow for a small web project.

## Source Context

- **Type**: blog-post (Simon Willison practitioner experience report; ~1,500 words; includes linked GitHub transcript, deployed app, and GitHub Actions workflow YAML)
- **Author credibility**: Simon Willison is the creator of Django, author of the `llm` CLI, and a designated `trusted-feed` source in this repo. He documents actual experiments he ran with verifiable public artifacts. This post is a first-person workflow report with a live deployed demo (`simonw.github.io/liteparse/`), a public git branch (`web`), and a linked Claude Code transcript. Claims are first-person observation, not vendor marketing, and the outputs are publicly verifiable.
- **Scope**: Covers two things: (1) LiteParse itself — a LlamaIndex open-source PDF text extraction tool using non-AI spatial heuristics and Tesseract OCR; (2) the complete Claude Code workflow Willison used to port it to the browser, including the planning pattern, TDD habit, queue-based prompting, parallel sessions, cross-model audit, and deployment delegation. Does NOT cover: LLM-based PDF extraction techniques, enterprise RAG pipelines, or multi-session workflows across multiple days. The "spatial text parsing" technique and the "Visual Citations with Bounding Boxes" pattern are documented but not deeply analyzed in the source.

## Extracted Claims

### Claim 1: LiteParse uses classical heuristics ("spatial text parsing") rather than AI for PDF text extraction, with Tesseract OCR as a fallback for image-based PDFs

- **Evidence**: Willison explicitly contrasts LiteParse with AI-based extraction: "Refreshingly, LiteParse doesn't use AI models to do what it does." The tool is a LlamaIndex open-source Node.js CLI that handles complex PDF layouts (multi-column, non-linear reading order) via programmatic heuristics, falling back to Tesseract for scanned documents.
- **Confidence**: settled (first-party description by the author of the post who used the tool; the LiteParse GitHub repo is public and verifiable)
- **Quote**: "Refreshingly, LiteParse doesn't use AI models to do what it does: it's good old-fashioned PDF parsing, falling back to Tesseract OCR (or other pluggable OCR engines) for PDFs that contain images of text rather than the text itself."
- **Our assessment**: This is a practitioner-relevant context engineering pattern: use classical, deterministic preprocessing (not an LLM call) to convert PDFs into clean, linearly-ordered text before feeding to an LLM context window. Using AI for extraction adds cost, latency, and nondeterminism to a step that classical algorithms handle reliably for most structured PDFs. Tesseract fallback for scanned documents covers the remaining case. This is the right architecture for a RAG preprocessing pipeline.

### Claim 2: LiteParse is explicitly designed to be called by AI agents as a CLI tool

- **Evidence**: Willison states this directly. The design choice (pure CLI, no API, designed for agent consumption) is relevant to how it integrates into agentic workflows.
- **Confidence**: settled (direct statement from the post; consistent with the tool's CLI interface)
- **Quote**: "LiteParse is provided as a pure CLI tool, designed to be used by agents."
- **Our assessment**: The CLI-as-agent-interface pattern is a recurring design choice across AI-native tooling. A CLI tool that produces clean text output on stdout is trivially callable from any shell-capable agent harness. This is simpler than building an API wrapper and gives the agent direct composability with shell pipelines.

### Claim 3: The "Visual Citations with Bounding Boxes" RAG pattern — accompanying answers with cropped, highlighted PDF page images — increases the credibility of RAG-style Q&A

- **Evidence**: Willison cites this as a LiteParse-documented pattern from LlamaIndex (`developers.llamaindex.ai/liteparse/guides/visual-citations/`). He notes it specifically as a technique worth attention for building more trustworthy RAG pipelines.
- **Confidence**: emerging (practitioner endorsement + LlamaIndex documentation; no controlled study of credibility improvement is cited)
- **Quote**: "The LiteParse documentation describes a pattern for implementing Visual Citations with Bounding Boxes. I really like this idea: being able to answer questions from a PDF and accompany those answers with cropped, highlighted images feels like a great way of increasing the credibility of answers from RAG-style Q&A."
- **Our assessment**: The specific mechanism — showing the user a cropped, highlighted snippet from the source page alongside the answer — is a UI-level trust pattern for RAG systems. It directly addresses the "where did this come from?" question that makes users distrust RAG answers. The implementation overhead is non-trivial (requires bounding box extraction and image cropping), but the trust benefit is plausible and the LlamaIndex docs provide a concrete implementation path. This is a novel pattern for context engineering Ch04 — no existing corpus source documents it.

### Claim 4: A mobile-to-desktop two-phase inception pattern works for small AI-native projects: explore with Claude.ai on mobile, then commit and build with Claude Code on laptop

- **Evidence**: Willison describes starting LiteParse exploration on his iPhone via the Claude app ("I wanted to try out LiteParse myself, so I started by uploading a random PDF I happened to have on my phone"), determining it was worth porting to the browser, then switching to Claude Code on his laptop.
- **Confidence**: anecdotal (single practitioner, one project; no structured comparison to other inception approaches)
- **Quote**: "The process of building this started in the regular Claude app on my iPhone."
- **Our assessment**: The two-phase structure (explore feasibility on mobile chat → commit to implementation on Claude Code) is a natural workflow given Claude.ai's mobile app and Claude Code's desktop CLI positioning. The mobile phase is lightweight: test the library, understand the problem, get initial research. The laptop phase is where the serious harness work happens. This pattern is low-overhead and doesn't require special setup — it's using the tools in the environments where they're most accessible.

### Claim 5: The notes.md → plan.md context handoff — paste prior AI research into notes.md, then ask Claude Code to read it and write plan.md before touching code — externalizes prior context into the agent's working memory

- **Evidence**: Willison describes the exact steps: forking the repo, cloning locally, pasting the iPhone Claude conversation output into `notes.md`, and then giving Claude Code a prompt that explicitly references `notes.md` and requests a `plan.md` before implementation. The linked `notes.md` is at `github.com/simonw/liteparse/blob/web/notes.md`.
- **Confidence**: anecdotal (single practitioner; one project; no comparison to starting Claude Code without the notes.md step — but the intent is explicit and the approach is deliberate)
- **Quote**: "I forked the original repo on GitHub, cloned a local copy, started a new `web` branch and pasted that last reply from Claude into a new file called notes.md. Then I told Claude Code: `Get this working as a web app. index.html, when loaded, should render an app that lets users open a PDF in their browser and select OCR or non-OCR mode and have this run. Read notes.md for initial research on this problem, then write out plan.md with your detailed implementation plan`"
- **Our assessment**: This is one of the cleanest in-corpus examples of the context injection pattern. The notes.md step solves a specific problem: Claude Code on a fresh session has no memory of the prior iPhone exploration. By externalizing that research into a file and telling the agent to read it first, Willison avoids re-explaining the problem and ensures the implementation plan is grounded in the prior research. Writing plan.md before implementation is the plan-then-approve-then-build loop — making the agent's approach explicit and correctable before any code is written. Both steps together are reusable as a workflow primitive.

### Claim 6: Explicitly correcting the plan before issuing "build it" prevents AI from deferring features to a hypothetical v2

- **Evidence**: Willison noticed Claude's plan included deferring the "canvas-encode swap" (image screenshots from PDFs) to v2. He corrected the plan with a targeted prompt before proceeding.
- **Confidence**: anecdotal (single example; no evidence of what would have happened without the correction — but the intent is clear and the pattern is explicit)
- **Quote**: "I noticed that Claude had decided to punt on generating screenshots of images in the PDF, and suggested we defer a 'canvas-encode swap' to v2. I fixed that by prompting: `Update the plan to say we WILL do the canvas-encode swap so the screenshots thing works`"
- **Our assessment**: The plan correction step is a key step in the plan-then-approve-then-build loop. AI planning tends to defer uncertain or complex features to future iterations. If left uncorrected, these deferrals become permanent omissions. Willison's pattern — inspect the plan, find the deferrals, explicitly reverse them before building — is a lightweight quality gate. The correction is a one-sentence prompt that costs almost nothing but anchors the scope before the agent touches code.

### Claim 7: "Use playwright and red/green TDD, plan that too" is a repeatable prompt habit that establishes automated tests as a correctness harness around AI-generated code

- **Evidence**: Willison includes "When you implement this use playwright and red/green TDD, plan that too" as one of his queued follow-up prompts. This was a subsequent prompt added during the build, not part of the initial plan prompt.
- **Confidence**: anecdotal (one practitioner, one project; no evidence of test quality or coverage achieved — but the pattern is intentional and named as a "habit")
- **Quote**: "When you implement this use playwright and red/green TDD, plan that too"
- **Our assessment**: The "plan that too" qualifier is important — it tells Claude Code to add the TDD approach to the plan.md, not just to the implementation. This ensures the testing approach is treated as a first-class step rather than an afterthought. Playwright for web apps is the natural fit (browser automation, cross-browser testing). The red/green discipline (write failing test, implement to pass) gives Claude Code a structural feedback loop rather than open-ended code generation. This is the same TDD pattern seen in `blog-simonwillison-csrf-multimodel-review.md` Claim 1 (close guidance with small commits on sensitive work) but applied to web UI testing.

### Claim 8: "Small commits along the way" as an explicit prompt addition produces a reviewable commit history and may help the agent focus on incremental completion

- **Evidence**: Willison includes "small commits along the way" as one of his queued prompts. He notes this as a deliberate practice. The hypothesis about focus is his own (not measured).
- **Confidence**: anecdotal (practitioner-reported practice; no controlled comparison to single-commit implementations)
- **Quote**: "small commits along the way"
- **Our assessment**: A reviewable commit history is the most concrete benefit: small commits let a human trace what the agent did in what order, and identify the specific commit that introduced a bug. The focus hypothesis (commits as natural completion checkpoints that prevent scope drift) is plausible but unverified. The pattern is already present in the CSRF note (10 commits for a security migration) and this post — two Willison examples using the same small-commits habit in different contexts.

### Claim 9: Queue-based prompting — adding prompts to the Claude Code queue while it is mid-task — enables an asynchronous/autonomous working style

- **Evidence**: Willison explicitly notes adding prompts to the queue while Claude Code was working. He also documents the internal mechanism for extracting those queued prompts from the project folder, which is a non-obvious discovery.
- **Confidence**: anecdotal (direct observation; the queue mechanism is a Claude Code implementation detail that may change)
- **Quote**: "I added a few prompts to the queue as I was working. Those don't yet show up in my exported transcript, but it turns out running `rg queue-operation --no-filename | grep enqueue | jq -r '.content'` in the relevant `~/.claude/projects/` folder extracts them."
- **Our assessment**: Queue-based prompting lets the developer maintain a flow state — submit prompts without waiting for each to complete, continue with other work (Willison mentions "caught up on Duolingo"), then review results when Claude finishes. The transcript observation (queued prompts don't appear in the exported transcript) is a current limitation worth knowing: practitioners relying on transcripts for audit should be aware that queued prompts may be missing. The `rg queue-operation` command is a useful workaround for now, but it is an implementation-level detail that may not survive version updates.

### Claim 10: Parallel Claude Code sessions against the same directory work without conflict for narrow operational questions

- **Evidence**: While the main Claude Code session was building the app, Willison started a separate Claude Code session against the same directory to ask how to run a development server. It told him to use `npx vite`.
- **Confidence**: anecdotal (single parallel use case; no evidence of conflict avoidance mechanisms beyond luck or filesystem isolation)
- **Quote**: "While it was working I decided it would be nice to be able to interact with an in-progress version. I asked a separate Claude Code session against the same directory for tips on how to run it, and it told me to use `npx vite`."
- **Our assessment**: The implicit assumption here is that a read-only operational question session doesn't conflict with an ongoing build session. That held in this case (the question was "how do I run the dev server" — no file writes needed). For two sessions simultaneously writing files, the conflict risk is real. The broader pattern — use a lightweight parallel session for narrow questions without interrupting the main session — is a useful workflow technique for long-running Claude Code tasks.

### Claim 11: Cross-model audit using GPT-5.5/Codex to describe the implementation independently verifies AI didn't fake features, without requiring full code review

- **Evidence**: Willison used OpenAI Codex with GPT-5.5 to ask "Describe the difference between how the node.js CLI tool runs and how the web/ version runs." The description he received was sufficient to confirm no major shortcuts were taken.
- **Confidence**: anecdotal (single audit on one project; no description of what a "shortcut" would have looked like vs. an acceptable response)
- **Quote**: "With this kind of project there's always a major risk that the model might 'cheat'—mark key features as 'TODO' and fake them, or take shortcuts that ignore the initial requirements. The responsible way to prevent this is to review all of the code... but this wasn't intended as that kind of project, so instead I fired up OpenAI Codex with GPT-5.5 (I had preview access) and told it: `Describe the difference between how the node.js CLI tool runs and how the web/ version runs` The answer I got back was enough to give me confidence that Claude hadn't taken any project-threatening shortcuts."
- **Our assessment**: This is the third in-corpus Willison example of cross-model verification (after the CSRF post's Claude Code + GPT-5.4 pattern). Here the verification is lighter-weight: not a formal review but an independent description of the implementation. If GPT-5.5 can accurately describe how the web version differs from the CLI version, that implies the web version actually implements something, not just a stub. The pattern exploits the fact that a second model reading the code is better than no review at all, and is much cheaper than a full human code review. The cross-vendor choice (Claude Code builds; GPT-5.5/Codex audits) provides independence at the model level.

### Claim 12: Browser-native static apps with no server and no data transfer have "almost non-existent" blast radius that makes vibe coding justifiable

- **Evidence**: Willison explains his reasoning for shipping code he hasn't read: static site (no backend), all processing in browser (no data leaves), GitHub Pages hosting (no infrastructure to compromise). He explicitly frames these as conditions under which vibe coding is acceptable.
- **Confidence**: anecdotal (one practitioner's stated reasoning; no empirical comparison of blast radius across deployment types — but the structural argument is sound)
- **Quote**: "As a static in-browser web application hosted on GitHub Pages the blast radius for any bugs is almost non-existent: it either works for your PDF or doesn't. No private data is transferred anywhere—all processing happens in your browser—so a security audit is unnecessary."
- **Our assessment**: This is the most explicit in-corpus articulation of the conditions under which not reviewing AI-generated code is acceptable. The three conditions (static site, in-browser only, no data transfer) are a concrete checklist for practitioners trying to decide when vibe coding is appropriate. The contrast case — production infrastructure, user data, shared systems — is where blast radius demands review. For the guide: vibe coding acceptability should be framed around blast radius and reversibility, not just code quality. Willison's checklist is a practical starting point.

### Claim 13: GitHub Pages + Vite + GitHub Actions is a zero-cost deployment target that can be fully delegated to Claude Code in a separate parallel session

- **Evidence**: Willison started a separate Claude Code instance with the prompt "Look at the web/ folder - set up GitHub actions for this repo." The resulting workflow deploys via Vite and publishes to `simonw.github.io/liteparse/`. The GitHub Actions YAML is publicly viewable at the linked URL.
- **Confidence**: anecdotal (one project; one deployment target — but the pattern is explicitly named and the output is publicly verifiable)
- **Quote**: "I started a fresh Claude Code instance and told it: `Look at the web/ folder - set up GitHub actions for this repo`"
- **Our assessment**: Delegating CI/CD setup entirely to Claude Code (including writing the GitHub Actions YAML, configuring Vite for production build, setting up Pages deployment) is a substantial time save on the boring-but-required infrastructure work. The GitHub Pages + Vite combination is a natural default for JavaScript/TypeScript static apps: free hosting, deploy-on-push, live-reloading during development. For practitioners building browser-native tools: this is a fully-delegatable deployment stack.

## Concrete Artifacts

### Full Claude Code prompt sequence (verbatim, as extracted from project folder)

```
# Source: simonwillison.net/2026/Apr/23/liteparse-for-the-web/
# Extracted from ~/.claude/projects/ via rg queue-operation

# 1. Initial prompt (with notes.md context)
Get this working as a web app. index.html, when loaded, should render an app
that lets users open a PDF in their browser and select OCR or non-OCR mode and
have this run. Read notes.md for initial research on this problem, then write
out plan.md with your detailed implementation plan

# 2. Plan correction (before build)
Update the plan to say we WILL do the canvas-encode swap so the screenshots thing works

# 3. Build trigger
build it.

# 4. TDD instruction (queued)
When you implement this use playwright and red/green TDD, plan that too

# 5. Renderer instruction (queued)
let's use PDF.js's own renderer

# 6. Commit discipline (queued)
small commits along the way

# 7. Attribution instruction
Make sure the index.html page includes a link back to https://github.com/run-llama/liteparse

# Deployment: separate Claude Code session
Look at the web/ folder - set up GitHub actions for this repo
```

### Queue extraction command

```bash
# Extract queued prompts from Claude Code project folder
# Source: simonwillison.net/2026/Apr/23/liteparse-for-the-web/
rg queue-operation --no-filename | grep enqueue | jq -r '.content'
# Run in: ~/.claude/projects/<project-folder>/
```

*Note: Queued prompts do not appear in Claude Code's exported transcript. This command is the workaround to recover them.*

### Notes.md → Plan.md workflow pattern

```
Pattern: Context handoff from prior AI session to Claude Code
Source: simonwillison.net/2026/Apr/23/liteparse-for-the-web/

Step 1: Complete prior AI research (Claude.ai mobile, or any chat session)
Step 2: Paste last Claude reply into notes.md in the project root
Step 3: Initial Claude Code prompt:
  "Read notes.md for initial research on this problem,
   then write out plan.md with your detailed implementation plan"
Step 4: Review plan.md — correct any deferrals before proceeding
Step 5: Prompt: "build it."

Result: Agent grounds its plan in prior research without re-explaining the problem.
        Plan is externalized and correctable before any code is written.
```

### Cross-model audit pattern

```
Pattern: Independent model audit for detecting shortcuts
Source: simonwillison.net/2026/Apr/23/liteparse-for-the-web/

Conditions: Project is too large to review line-by-line; vibe coding context
Tool:       A second model (different vendor from implementer if possible)
Question:   "Describe the difference between [reference implementation] and [AI-built version]"

Example:
  Implementer: Claude Code (Anthropic)
  Auditor:     OpenAI Codex with GPT-5.5
  Question:    "Describe the difference between how the node.js CLI tool runs
                and how the web/ version runs"
  Goal:        Detect TODO stubs, faked features, or scope omissions

Note: This is not a security audit or quality review — it is a shortcuts-detection
      check. An auditor that accurately describes the implementation difference
      implies the implementation exists and is real.
```

### GitHub Actions deployment workflow (delegated to separate Claude Code session)

```yaml
# URL: github.com/simonw/liteparse/blob/web/.github/workflows/deploy-web.yml
# Built by Claude Code from a single prompt:
#   "Look at the web/ folder - set up GitHub actions for this repo"
# Deploys: Vite-built static app to GitHub Pages at simonw.github.io/liteparse/
```

### Safari debugging sequence

```
# Source: simonwillison.net/2026/Apr/23/liteparse-for-the-web/

Error prompt:
  "When I try to parse a PDF in my browser I see 'Parse failed: undefined is
   not a function (near '...value of readableStream...')'"

Status at that point:
  Chrome: works
  Firefox: works
  Safari: broken

Resolution: Claude Code identified the Safari-specific ReadableStream API difference
            and fixed it once explicitly prompted. Final status: "works in safari now"
```

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-csrf-multimodel-review.md** (Claim 1 — small commits pattern; Claim 2 — multi-model cross-review): The CSRF post shows 10 small commits under close guidance + GPT-5.4 review. This post shows the same two patterns (small commits prompt + GPT-5.5/Codex audit) in a different context (autonomous vibe coding rather than closely-guided security work). The two posts together establish these as Willison's consistent workflow habits, not one-off choices. The cross-vendor audit choice also corroborates: both posts use a different vendor's model for the verification role than for the implementation role.
  - **blog-simonwillison-servo-crate-exploration.md** (Claim 5 — task-framing for loose goals): The servo note documents giving Claude Code a crate name and a loose goal ("figure out what it can do"). This post uses the same loose-goal framing ("Get this working as a web app") but adds the notes.md context injection step that the servo experiment lacked. The notes.md pattern is the evolution: same loose goal, but now with prior research made explicit.
  - **blog-simonwillison-gpt55-codex-plugin.md** (Claim 3 — Claude Code for cold-start on unfamiliar code): Published the same day (2026-04-23). That post documents building an `llm` plugin by having Claude Code reverse-engineer the Codex OAuth flow in one session; this post documents building a browser app by having Claude Code port a Node.js library. Both are single-session implementations from loose task descriptions. Together they establish the pattern as repeatable: Willison successfully ships verifiable artifacts from loose Claude Code task descriptions across different domains (plugin building, web app porting).

- **Contradicts**: None identified.

- **Extends**:
  - **blog-simonwillison-csrf-multimodel-review.md** (Claim 3 — manual PR description): The CSRF post introduces Willison's new practice of writing PR descriptions by hand "as an exercise in keeping myself honest." This post is the counterpoint: a project where Willison explicitly did NOT review the code at all ("I have not looked at a single line of the HTML and TypeScript written for this project"). The pairing is instructive — it shows that the same practitioner applies different review levels (close guidance + manual PRs vs. zero code review) based on blast radius, not personal preference. The CSRF post covers security migrations; this post covers zero-blast-radius browser apps.
  - **blog-simonwillison-servo-crate-exploration.md**: Extends the "give Claude Code a loose goal" pattern with the notes.md context handoff, plan.md review step, TDD instruction, and queue-based prompting. The servo experiment was minimal; this post is the full workflow.

- **Novel**:
  - **Notes.md → plan.md context handoff**: No existing corpus source documents the specific pattern of externalizing prior chat session output into a notes file and having Claude Code read it before writing a plan. The context injection principle is known, but this specific two-file handoff (notes.md from prior session → plan.md written by Claude Code) is new to the corpus.
  - **Queue-based prompting with transcript gap**: No existing corpus source documents that Claude Code queued prompts do not appear in the exported transcript, nor the `rg queue-operation` workaround for recovering them. This is an operationally significant limitation for audit/reproducibility.
  - **GPT-5.5/Codex as a shortcuts-detection auditor**: The CSRF post documented a formal code review with GPT-5.4. This post introduces a lighter-weight pattern: ask a second model to describe the implementation and use that description as a shortcuts-detection signal. The distinction matters: this is a confirmation signal ("does the implementation exist and do the right things?"), not a quality review. The two patterns are complementary.
  - **Visual Citations with Bounding Boxes**: No existing corpus source documents this RAG trust pattern — returning cropped, highlighted PDF page images alongside answers as a credibility signal.
  - **Blast-radius-conditioned vibe coding acceptance**: No existing corpus source provides an explicit three-factor checklist for when vibe coding is acceptable. Willison's three conditions (static site, in-browser processing, no data transfer) are a concrete starting point.

## Guide Impact

- **Chapter 02 (Harness Engineering — Context Injection Patterns)**: The notes.md → plan.md handoff is the most concrete in-corpus example of bridging a prior chat session's research into a Claude Code session without re-explaining the problem. Add as a recommended workflow primitive: "When starting a Claude Code session that builds on prior AI research, externalize that research into a `notes.md` file in the project root and include `Read notes.md for initial research on this problem, then write out plan.md` in the opening prompt. This prevents the agent from re-approaching the problem from scratch and grounds its plan in your prior context." Cite this source (April 2026) as a practitioner-confirmed example.

- **Chapter 02 (Harness Engineering — Plan Review as a Build Gate)**: The plan correction before "build it" (correcting the canvas-encode swap deferral) should be extracted as a workflow step: "Before triggering the build, inspect the plan.md for deferred features. AI planning tends to defer uncertain items to a hypothetical v2. Explicitly reverse any deferrals that are in scope before issuing the build command." This pairs with the notes.md pattern as steps 3 and 4 of the same workflow.

- **Chapter 01 (Daily Workflows — Queue-Based Prompting)**: The queue-based prompting pattern (add prompts while Claude Code is mid-task) is documented here with the operationally important caveat that queued prompts don't appear in exported transcripts. The chapter should note: "Claude Code accepts prompts while a task is running. These are processed after the current task completes, enabling async collaboration. Note: queued prompts are not included in exported transcripts — recover them with `rg queue-operation --no-filename | grep enqueue | jq -r '.content'` from the `~/.claude/projects/` folder."

- **Chapter 03 (Safety and Verification — Cross-Model Audit for Shortcuts Detection)**: Add the GPT-5.5/Codex description-based audit as a lightweight verification pattern for vibe-coded projects. "For low-blast-radius projects where full code review is not warranted, ask a second model (ideally cross-vendor from the implementer) to describe the difference between the reference implementation and the AI-built version. An accurate description confirms the implementation is real, not stubbed. This is a shortcuts-detection signal, not a quality review." Cross-reference with the CSRF note's heavier-weight cross-model review pattern as the complement for security-sensitive work.

- **Chapter 03 (Safety and Verification — Blast-Radius-Conditioned Review Levels)**: Willison's three-factor checklist (static site, in-browser processing, no data transfer) should anchor a framework for deciding how much review AI-generated code requires. Add: "Not all AI-generated code requires the same review level. Willison's LiteParse browser port (April 2026) shipped with zero code review, justified by three conditions: static deployment (no backend), all processing in-browser (no data exfiltration surface), no private data handled. Contrast with his CSRF migration (same month, same author) — sensitive changes to production security code that required 10 commits of close guidance and a GPT-5.4 cross-review."

- **Chapter 04 (Context Engineering — Non-AI PDF Preprocessing for RAG)**: The spatial text parsing approach (classical heuristics + Tesseract fallback, not LLM) should be documented as the recommended architecture for PDF-to-context preprocessing pipelines. "Use deterministic preprocessing (spatial heuristic parsers like LiteParse, classical layout analysis) rather than LLM-based extraction for PDF-to-text conversion in RAG pipelines. LLM extraction adds cost and nondeterminism to a step that classical algorithms handle reliably for structured PDFs. Reserve LLM involvement for the retrieval and generation steps, not the preprocessing step."

- **Chapter 04 (Context Engineering — Visual Citations as RAG Trust Pattern)**: Add the Visual Citations with Bounding Boxes pattern as a trust-building technique for RAG Q&A: "Accompany LLM answers from PDF sources with cropped, highlighted images of the source page sections the answer is drawn from. This directly addresses user distrust of RAG answers by showing the source passage, not just citing a page number. LlamaIndex documents this pattern with a concrete implementation guide."

## Extraction Notes

- **Three Prospector triage comments**: Three separate triage assessments were filed (automated pipeline artifact). The first focuses on the harness engineering patterns (notes.md, plan.md, TDD, parallel sessions, GPT-5.5 audit); the second adds the mobile→desktop workflow and identifies all 9 workflow patterns individually; the third focuses on the LiteParse spatial parsing and Visual Citations patterns for Ch04. All three were read and synthesized; claims cover all three assessors' identified extraction targets.
- **Claude Code transcript linked**: The post links to the Claude Code session transcript, providing higher confidence than author-only reports. Verbatim prompts were extracted from the transcript extraction command described in the post.
- **Model used**: Opus 4.7 (per section heading "Building it with Claude Code and Opus 4.7").
- **Session duration**: 59 minutes for the core "build it" step (total including planning and debugging was longer).
- **Fragment URL**: The issue filed the source URL with `#atom-everything` (an Atom feed anchor). `source_url` uses the canonical page URL without the fragment.
- **WebFetch limitations**: Full verbatim post text was not reproduced by WebFetch (returns summaries). Quotes were extracted via targeted re-fetches with specific questions. All quoted passages were verified against the source URL.
- **No sub-pages followed beyond the GitHub Actions YAML**: The post links to the notes.md file, the plan.md file, the deployed app, and the GitHub Actions workflow. The LlamaIndex Visual Citations docs were referenced but not deeply extracted (the LlamaIndex URL in the post is for reference; the pattern description is in the Willison post itself).
