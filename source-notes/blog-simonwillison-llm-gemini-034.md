---
source_url: https://simonwillison.net/2026/Sep/2/llm-gemini/
source_type: blog-post
title: "llm-gemini 0.34"
author: Simon Willison
date_published: 2026-09-02
date_extracted: 2026-09-07
last_checked: 2026-09-07
status: current
confidence_overall: settled
issue: "#3287"
---

# llm-gemini 0.34

> A short Willison "beat" release-note post announcing llm-gemini 0.34 (`gemini-3.8-flash` support, an async-response bug fix), but the real substance is downstream: the linked transcript shows Willison using his own `llm-coding-agent` plugin — itself built by Claude ("Fable 5") via a two-prompt spec-then-TDD workflow — to drive Gemini 3.8 Flash through a ~99-tool-call session that adds sandboxed HTML-iframe rendering to his `markdown-svg-renderer` tool, surfacing concrete evidence of explore-before-edit agent discipline, per-call human approval/decline, prompt-cache growth to ~98% of input tokens, and a real CSP/iframe sandboxing pattern for untrusted content.

## Source Context

- **Type**: blog-post (Willison "beat" format — a short link-blog release note, ~90 words, with two release bullets and three outbound links: the GitHub release page, Google's model announcement, and a gist transcript). The blog post itself is thin (same minimal format as `blog-simonwillison-llm-gemini-032.md`), but per MINER.md §1 this note follows all three substantive linked pages: the GitHub release (confirms the blog post verbatim), Google's official Gemini 3.8 Flash / 3.8 Flash Cyber announcement (blog.google), and — the richest source — the 9,161-line gist transcript of an actual `llm-coding-agent` session using Gemini 3.8 Flash, plus the `llm-coding-agent` plugin's own README for its approval-flow documentation.
- **Author credibility**: Simon Willison is the creator of the `llm` CLI and the `llm-gemini` plugin; this is first-party release documentation. He is also the author of the linked `llm-coding-agent` plugin and the person operating it in the transcript — so the transcript is a first-party, unedited record of his own tool-building session (a gist, not a curated case study).
- **Scope**: Covers the llm-gemini 0.34 release (new model, one bug fix), Google's official framing of Gemini 3.8 Flash / 3.8 Flash Cyber (pricing, capability claims, the Cyber variant's restricted access), and a full agentic coding session transcript demonstrating `llm-coding-agent`'s tool-approval mechanics, an untrusted-HTML sandboxing pattern, and a debugged HTML-escaping bug. Does NOT cover: independent benchmarking of Gemini 3.8 Flash (Willison's own "pelican" test grid for 3.8 Flash is linked but is a separate post, not fetched here since it was already flagged by the Prospector as being covered by a sibling issue on the Astra pelican comparison); Gemini 3.8 Flash Cyber's technical internals beyond what Google's announcement states.

## Extracted Claims

### Claim 1: llm-gemini 0.34 adds a `gemini-3.8-flash` model slug with low, medium, and high thinking levels
- **Evidence**: Verbatim release-note bullet, identical in the blog post and the GitHub release page (github.com/simonw/llm-gemini/releases/tag/0.34, credited to issue #146).
- **Confidence**: settled (first-party release documentation, corroborated by two independently fetched pages with identical text)
- **Quote**: "New model gemini-3.8-flash for Gemini 3.8 Flash, with low, medium and high thinking levels."
- **Our assessment**: This is the fourth Gemini Flash generation to reach the `llm` CLI in this corpus's version history (3.5 → 3.6/3.7 → 3.8), each retaining a tiered thinking-effort control. Compared to `blog-simonwillison-llm-gemini-033.md` Claim 8 — which noted Gemini 3.7 Flash *removed* the "minimal" tier present in 3.6 Flash, leaving only high/medium/low — 0.34's three-tier scheme (low/medium/high) is consistent with that narrowed 3.7 baseline rather than a reversal.

### Claim 2: The release also fixes async responses failing to record the resolved model version, credited to external contributor Charlie Tonneslan
- **Evidence**: Verbatim release-note bullet with a linked PR (github.com/simonw/llm-gemini/pull/137).
- **Confidence**: settled (first-party changelog with named contributor and PR reference)
- **Quote**: "Fixed async responses failing to record the resolved model version. Thanks, Charlie Tonneslan."
- **Our assessment**: A narrow correctness fix rather than a feature — before this fix, code using the plugin's async response path could not reliably determine which underlying Gemini model actually served a given request (relevant for the plugin's own "resolved model" logging, later visible in the transcript's own metadata line `Model: gemini/gemini-3.8-flash (resolved: gemini-3.8-flash)`). Minor but a real operational hazard for anyone building usage/cost dashboards keyed on resolved model IDs.

### Claim 3: Willison demonstrates Gemini 3.8 Flash generating a complete interactive HTML/JS artifact from a single vague prompt in 13 seconds for 1.8 cents
- **Evidence**: First-party demonstration in the blog post body, described as an unprompted experiment ("I was messing around with it").
- **Confidence**: anecdotal (single, informal demonstration; no benchmark methodology)
- **Quote**: "Something I appreciate about Gemini Flash is that it's fast, cheap, and competent at things like HTML and JavaScript. I was messing around with it and prompted \"make me a cool thing in html\" and it built this, which is certainly a cool thing in HTML! Took 13 seconds, cost 1.8 cents."
- **Our assessment**: A single anecdotal data point, but the cost/latency figures are concrete and match the pattern established across this corpus's other Gemini Flash coverage — Flash-tier models optimized for fast, cheap, front-end-code generation. Useful as a citable order-of-magnitude figure for "cost of a small HTML/JS generation task on a current Flash-tier model" rather than as a rigorous benchmark.

### Claim 4: Google frames Gemini 3.8 Flash as its best reasoning-and-coding model to date, priced and speed-matched to its predecessor, with gains driven by the model "working harder" (more reasoning steps and tool calls) rather than a larger model
- **Evidence**: Google's official announcement (blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/), fetched directly and cross-checked against the raw page text.
- **Confidence**: settled (first-party vendor announcement; capability framing, not independently verified benchmark)
- **Quote**: "today we’re introducing Gemini 3.8, our best reasoning and coding model yet, at the same speed and low cost of 3.7... delivering significant improvements from 3.7 Flash across software engineering, agentic tasks, and critical, multi-step reasoning in specialized domains." And separately: "3.8 Flash works harder. On complex tasks, it exhibits greater diligence — executing extra reasoning steps, and calling tools iteratively."
- **Our assessment**: This is standard vendor-benchmark framing and should be weighted as such (settled that Google *claims* this, not settled that it is independently verified). The "works harder, not bigger" framing is a genuinely distinct engineering claim from typical "next model is bigger and better" narratives — it implies token-cost variance rather than latency variance is the main deployment risk, consistent with Willison's own observation that effort levels are user-selectable (Claim 1).

### Claim 5: Gemini 3.8 Flash launched at an introductory price of $0.75/million input tokens and $3.75/million output tokens through December 31, 2026, after which pricing rises to $1.50/million input and $7.50/million output tokens
- **Evidence**: Google's official announcement, pricing section.
- **Confidence**: settled (first-party published pricing, time-boxed)
- **Quote**: "It is available at the same introductory price as 3.7 Flash at $0.75 per million input tokens and $3.75 per million output tokens." And: "Introductory price expires on December 31, 2026. Starting January 1, 2027, $1.50/1M input tokens and $7.50/1M output tokens will apply."
- **Our assessment**: Unlike the 3–6x pricing jump documented for Gemini 3.5 Flash in `blog-simonwillison-gemini35-flash-pricing.md` Claim 2, 3.8 Flash launches at price parity with its immediate predecessor (3.7 Flash) — the cost story here is a scheduled 2x price increase four months after launch, not an immediate jump. Practitioners building on this pricing should plan for the January 1, 2027 doubling rather than assume it's a permanent baseline.

### Claim 6: Gemini 3.8 Flash Cyber, a separate cybersecurity-specialized variant, is restricted to "trusted defenders" through a new "Fairwind Program," and Google reports it produced 2.6x more correct vulnerability patches than larger commercial models when tested internally by Chrome Security
- **Evidence**: Google's official announcement, Cyber-variant section.
- **Confidence**: settled (first-party vendor claim, citing an internal team's result — not independently reproduced)
- **Quote**: "our most capable cybersecurity model with frontier-level performance in vulnerability detection and automated patching, available to trusted defenders through our new Fairwind Program." And: "The Chrome Security team found that 3.8 Flash Cyber produced 2.6 times more correct patches to vulnerabilities in Chrome than the best commercial models that are much larger."
- **Our assessment**: The access restriction (government/critical-infrastructure "trusted defenders" only, via application) means this variant is not a practitioner-accessible tool for the guide's general audience — worth noting as context for why the `llm-gemini` plugin release covers only the general-availability `gemini-3.8-flash` slug and not a Cyber variant. The 2.6x figure is a single internal customer's result, not an independent benchmark.

### Claim 7: Willison used Gemini 3.8 Flash, driven through his own `llm-coding-agent` plugin, to add sandboxed-iframe HTML rendering to his `markdown-svg-renderer` tool, and published the full session transcript
- **Evidence**: Direct statement in the blog post, with a linked gist transcript (gist.github.com/simonw/3e36b98292dfdc1b3baff158faa743f7) that this note fetched and read in full (9,161 lines, 99 distinct tool calls across a ~13-minute session from 16:56:45 to 17:09:46 UTC on 2026-09-02).
- **Confidence**: settled (first-party demonstration with a complete, unedited raw transcript as evidence)
- **Quote**: "I used Gemini 3.8 Flash (with my very basic llm-coding-agent coding agent plugin) to add support for HTML as well, so now any HTML blocks in the Markdown are rendered using a sandboxed iframe. Here's the transcript."
- **Our assessment**: Willison explicitly calls the plugin "very basic," yet the transcript shows a full explore→implement→test→debug loop with dozens of tool calls, self-correction, and a real bug fix — evidence that a minimal from-scratch agent harness (not a heavyweight commercial product) is sufficient to complete a real multi-file feature addition when paired with a competent tool-calling model. This is a useful counterpoint to guide chapters that assume agent harness sophistication is the primary lever on task success.

### Claim 8: `llm-coding-agent` gates every `execute_command` call behind per-call human approval — including read-only shell commands — and the linked transcript shows the decline path exercised four times in a single session, with the model adapting rather than retrying each time
- **Evidence**: Combination of the plugin's own README (github.com/simonw/llm-coding-agent, fetched directly) describing the approval mechanism, and a grep of the full raw transcript for `Cancelled: User declined this tool call` / `Error: CancelToolCall: User declined this tool call`, which returns four distinct declines out of the 11 `execute_command` calls issued in the session (the other 7 — `pytest`, `python3 -m pytest`, `git status` ×2, `echo $PATH`, `node -e '...'`, `python3 -m py_compile ...` — were approved and ran). The four declined commands, in transcript order:

  | # | Declined command | Transcript line | Model's very next action |
  |---|---|---|---|
  | 1 | `which python python3; find / -name pytest 2>/dev/null` | ~4048 | `execute_command: python3 -m pytest` (corrected approach; succeeded) |
  | 2 | `type pytest` | ~7547 | `execute_command: git diff` (different command, not a retry) |
  | 3 | `git diff` | ~7588 | `read_file markdown-svg-renderer.html` (offset 330, limit 70) — switched from the gated shell tool to the un-gated read tool |
  | 4 | `rm I` (deleting a stray empty file) | ~9121 | No further tool calls; delivered its final prose answer (the `</script>` root-cause explanation) instead of retrying |

- **Confidence**: settled (README documentation, and the decline count is a full grep of the transcript, not a sample) / anecdotal (four declines in one session is not a measured rate)
- **Quote**: "Read-only tools run freely; file writes, edits and shell commands show you what the model wants to do and ask for approval - `y` approves once, `a` approves similar actions for the rest of the session, anything else declines (the model is told, and can try another approach)." And, from the README's Python-API section, the classification that makes the gate's boundary explicit: "The `approve=` parameter controls what happens when the model wants to run a mutating tool (`write_file`, `edit_file`, `execute_command` - read-only tools never ask):"
- **Our assessment**: Two things stand out, and the second qualifies the plugin's own framing.

  First, the "correct rather than repeat" instruction in the agent's system prompt (Claim 9) held after all four declines, not just one: the model never re-issued a declined command. After decline #1 it immediately switched to `python3 -m pytest` on the very next tool call; after #2 and #3 it tried a different inspection route each time; after #4 it abandoned the cleanup entirely and moved to its final answer. That is observed evidence — across every instance available, not a cherry-picked one — that the decline signal is genuinely acted on rather than looped against. It complements the large-scale "93% approval rate → approval fatigue" finding in `blog-anthropic-how-contain-claude.md` Claim 6: this single-session anecdote shows the decline path being exercised and respected, not sitting unused.

  Second, and worth flagging for anyone porting this design: **the gate is on the tool, not on the effect.** The README's "read-only tools run freely" means the `read_file`/`list_files`/`search_files` tools; `execute_command` is classified as a *mutating* tool categorically, so read-only shell commands are gated identically to destructive ones. Declines #2 (`type pytest`) and #3 (`git diff`) are pure inspection commands that could not change anything, and they hit the same prompt as `rm I`. Willison's approvals in this session were human judgment, not a policy the harness enforces — `git status` was approved twice in the same session while `git diff` was declined. This is precisely the shape of interaction that generates approval fatigue, and the plugin ships a mitigation for it in its own CLI (`--allow "pytest*" --allow "git diff*"` pre-approves command patterns; `a` approves similar actions for the rest of the session). A harness that wants meaningful approvals has to solve command-level classification, which tool-level gating alone does not give you.

### Claim 9: The coding agent's system prompt explicitly instructs it to explore before changing code, prefer minimal matching-style edits, verify its own work by running tests, correct rather than repeat failed tool calls, and value honesty over the appearance of success
- **Evidence**: The system prompt is embedded verbatim at the start of the transcript.
- **Confidence**: settled (verbatim system prompt text, directly observed)
- **Quote**: "Explore before you change anything: use list_files and search_files to find the relevant code, and always read_file a file before editing it. Prefer edit_file (exact string replacement) over write_file for existing files, and keep edits minimal - match the style, naming and conventions of the surrounding code. Verify your work: after making changes, run the project's tests or another relevant command with execute_command and check the result. If a tool returns an error, read the message and correct your approach rather than repeating the same call. Honesty matters more than appearing successful. If tests fail, report the failure and include the relevant output. If you cannot complete something, say so plainly. If the task is ambiguous, stop and ask rather than guessing."
- **Our assessment**: This is a compact, explicit statement of an "explore-first, minimal-diff, verify, don't-bluff" harness discipline pattern that recurs across this corpus under different names; having it as verbatim system-prompt text (rather than inferred from behavior) makes it a directly citable artifact for any chapter documenting how to instruct a coding agent's tool-use discipline.

### Claim 10: The transcript documents a real debugging cycle: the agent introduced a syntax error by embedding a literal, unescaped `</script>` tag inside a JavaScript template literal, correctly diagnosed the HTML-tokenizer root cause, and fixed it by escaping the closing tag
- **Evidence**: The transcript's final response, after a `python3 -m py_compile` check and a `git status` review, explaining the bug it had introduced and fixed within the same session.
- **Confidence**: settled (directly observed in the transcript, root cause explained by the model itself and consistent with standard HTML-parsing behavior)
- **Quote**: "Under HTML parsing rules, the browser's HTML tokenizer detects </script> anywhere inside a <script> tag (even within JavaScript string literals or template literals) and immediately closes the enclosing script block. This caused the main <script type=\"module\"> to truncate prematurely, resulting in an unclosed template literal and the Uncaught SyntaxError: Unexpected end of input error."
- **Our assessment**: A genuinely useful, narrow gotcha for anyone generating HTML documents that embed sample/demo `<script>` content inside JS template literals (exactly the kind of untrusted-HTML-in-Markdown scenario this session was building support for) — and notable that the same repo already had the fix pattern (`<\/script>` escaping) established elsewhere in its own codebase (`csp-allow.html`), which the model found and reused rather than inventing a new fix.

### Claim 11: The repo already implements a documented CSP-meta-tag-plus-iframe-sandbox pattern for rendering untrusted SVG/HTML, modeled on "the datasette-apps sandbox," and the agent researched and summarized this pattern before implementing the new HTML-block feature
- **Evidence**: The transcript's response to Willison's first prompt ("research the patterns used in this repo for displaying untrusted HTML content in an iframe...") synthesizes a multi-file survey of `markdown-svg-renderer.html`, `cors-chat.html`, and `csp-allow.html`, quoting an in-repo code comment.
- **Confidence**: settled (directly observed; the agent quotes an existing code comment as its source)
- **Quote**: "Match the datasette-apps sandbox: put a restrictive CSP before any user-controlled markup in srcdoc, and repeat it on the iframe as defense in depth."
- **Our assessment**: This corroborates `blog-simonwillison-datasette-apps.md`'s coverage of the same sandboxing philosophy (CSP-plus-`sandbox=""`-plus-`referrerpolicy=no-referrer` layering) as a portable pattern Willison has now reused across at least two separate tools (Datasette Apps and this markdown/SVG/HTML renderer) — evidence it functions as a personal defense-in-depth template rather than a one-off implementation. The concrete mechanics as summarized in the transcript: a `<meta http-equiv="Content-Security-Policy">` tag placed at the very start of the `srcdoc` HTML (before any untrusted content), `sandbox=""` or `sandbox="allow-scripts"` on the `<iframe>` (never combined with `allow-same-origin`, to force an opaque null origin), `referrerpolicy="no-referrer"`, and — for the script-allowed variant — a monkey-patched `window.fetch` and `securitypolicyviolation` listener that reports blocked network requests back to the parent via `postMessage`.

### Claim 12: Over the course of the session, the model's input-token cache hit rate climbed to roughly 98% of a ~128,000-token context (125,906 of 127,966 tokens cached in the final recorded turn)
- **Evidence**: Per-turn `Token usage` metadata blocks embedded throughout the transcript, e.g. the final `py_compile` check turn: `127,966 input, 396 output ... "cachedContentTokenCount": 125906`.
- **Confidence**: settled (directly observed numeric metadata, provider-reported)
- **Quote**: (no direct quote; figures read directly from the transcript's structured `Token usage` JSON blocks, e.g. `{"candidatesTokenCount": 273, "cachedContentTokenCount": 125906, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 127966}], "cacheTokensDetails": [{"modality": "TEXT", "tokenCount": 125906}]...}`)
- **Our assessment**: A concrete, provider-agnostic corroboration of `blog-anthropic-prompt-caching-everything.md` Claim 1's claim that prompt caching is what makes long-running agentic sessions economically feasible — this transcript is Gemini API usage (not Claude), so it's independent evidence the same caching dynamic applies across at least two major providers' agentic tool-use APIs. It also empirically demonstrates the "static content first, dynamic content last" structuring implied by `blog-anthropic-prompt-caching-everything.md` Claim 3: the growing tool-call history stays almost entirely cached turn over turn, with only the newest exchange paid at full input-token rate.

### Claim 13: `llm-coding-agent` — the plugin used to run this whole session — was itself built by Claude ("Fable 5") from just two prompts: one to write a spec, one to implement it via red/green TDD
- **Evidence**: The plugin's own README, "Built by Fable 5" section, linking to a Claude Code session transcript.
- **Confidence**: settled (first-party README attribution with a linked session URL)
- **Quote**: "Write a spec.md for this project - it will depend on the latest \"llm\" alpha from PyPI and implement a Claude code style coding agent complete with tools for reading and editing files and executing commands" ... "Commit the spec, then build it using red/green TDD in a series of sensible commits (each with passing tests and updated docs) - occasionally manually test it using the OpenAI API key in your environment"
- **Our assessment**: A meta-level detail worth flagging: the tool Willison used to drive Gemini 3.8 Flash through this session was itself built by a different vendor's model (Claude/Fable 5, per `blog-simonwillison-claude-fable-5.md`) from a two-prompt spec-then-TDD instruction, explicitly modeled on "a Claude code style coding agent." This is a small but concrete example of cross-vendor tool-building — an agent harness built by one model family, then used to operate a different model family — and a real-world instance of the "spec first, then red/green TDD, commit per passing test" workflow pattern this corpus has documented elsewhere as a prompting strategy, here shown actually producing a working, published plugin.

## Concrete Artifacts

### GitHub release notes (verbatim, github.com/simonw/llm-gemini, tag 0.34, released 2026-09-02 16:39 UTC)
```
- New model `gemini-3.8-flash` for Gemini 3.8 Flash, with low, medium and
  high thinking levels. #146
- Fixed async responses failing to record the resolved model version.
  Thanks, Charlie Tonneslan. #137
```
*Source: github.com/simonw/llm-gemini/releases/tag/0.34*

### `llm-coding-agent` CLI usage (verbatim, README.md)
```bash
llm code                                   # interactive session, default model
llm code "add type hints to utils.py"      # start with an initial task
llm code -m gpt-4.1 -d ~/dev/myproject     # pick a model and directory
llm code --yolo                            # auto-approve every tool call
llm code --allow "pytest*" --allow "git diff*"   # pre-approve some commands
```
*Source: github.com/simonw/llm-coding-agent/blob/main/README.md*

### `llm-coding-agent` Python API — explicit approval modes (verbatim, README.md)
```python
agent = CodingAgent(
    model="gpt-4.1-mini",        # any llm model ID, or a model instance
    root="/path/to/project",
    approve=True,                # approve every tool call
)
```
- `approve=True` approves everything
- `approve=callable` — a `(tool, tool_call) -> bool` function; returning `False` cancels that call and the model is told it was declined
- `approve=None` (the default) pauses the run: `result.paused` is true, `result.pending_tool_calls` lists what the model wants to do, and calling `agent.resume()` approves those calls and continues the loop

*Source: github.com/simonw/llm-coding-agent/blob/main/README.md*

### CSP directives for the strict, zero-script SVG/HTML isolation pattern (verbatim, markdown-svg-renderer.html, as read and quoted by the agent in the transcript)
```js
const svgPreviewCsp = [
  "default-src 'none'",
  "script-src 'none'",
  "style-src 'unsafe-inline'",
  "img-src data: blob:",
  "form-action 'none'",
  "base-uri 'none'"
].join("; ") + ";";
```
*Source: gist.github.com/simonw/3e36b98292dfdc1b3baff158faa743f7 (coding-agent-3.8-flash.md transcript, agent's research turn)*

### Session token-usage growth (from the transcript's per-turn metadata)
```
Early turn:  961 input tokens,  87 output  (no cache yet)
Mid turn:    74,141 input, 1,897 output, cachedContentTokenCount: 69,175
Final turn:  127,966 input,   396 output, cachedContentTokenCount: 125,906
```
*Source: gist.github.com/simonw/3e36b98292dfdc1b3baff158faa743f7, Gemini API `usageMetadata` blocks embedded per tool-call turn*

### Root-cause explanation for the introduced `</script>` bug (verbatim, transcript's final response)
```
The syntax error occurred because the sample markdown string inside
markdown-svg-renderer.html contained an unescaped literal </script> tag...
Under HTML parsing rules, the browser's HTML tokenizer detects </script>
anywhere inside a <script> tag (even within JavaScript string literals or
template literals) and immediately closes the enclosing script block...
Fix: Escaped the closing tag as <\/script> (the same pattern used in
csp-allow.html).
```
*Source: gist.github.com/simonw/3e36b98292dfdc1b3baff158faa743f7, final turn*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-gemini-032.md` Claim 2: 0.34 restores the same-day plugin-release-matching-GA-launch pattern first documented there (llm-gemini 0.32 shipped the same day as Gemini 3.5 Flash's Google I/O GA launch; this release shipped the same day as Gemini 3.8 Flash's GA announcement, per the GitHub release timestamp 16:39 UTC and Willison's "today" framing). Notably, `blog-simonwillison-llm-gemini-033.md` Claim 1 documented a break from this pattern (a ~3-month gap for 0.33) — 0.34 shows the same-day cadence is not permanently lost, just intermittent.
  - `blog-anthropic-prompt-caching-everything.md` Claim 1: The transcript's growing `cachedContentTokenCount` (Claim 12 above) is independent, cross-provider (Gemini, not Claude) evidence that prompt caching is what keeps a long tool-use session's cost from scaling linearly with total context — corroborating the claim's core mechanism outside the Anthropic ecosystem it was originally documented in.
  - `blog-anthropic-how-contain-claude.md` Claim 6: That note's "93% of permission prompts approved → approval fatigue" finding is corroborated at small scale by this transcript's four declines (Claim 8) — evidence that when a human *does* decline, the decline is respected and the agent adapts, i.e. the review mechanism functions correctly when actually used, even if aggregate approval rates elsewhere in the corpus run high. The transcript also independently illustrates the *cause* that note identifies: because `llm-coding-agent` gates every shell command regardless of effect, two of the four approval prompts here were for pure-inspection commands (`type pytest`, `git diff`), i.e. exactly the low-stakes prompt volume that drives approval rates toward reflexive assent.
  - `blog-simonwillison-datasette-apps.md`: The CSP-meta-tag-plus-iframe-sandbox pattern (Claim 11) is an explicit, named reuse of "the datasette-apps sandbox" — direct textual corroboration that this is a portable pattern Willison applies across multiple of his own tools, not a one-off.

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-llm-gemini-033.md` and `blog-simonwillison-llm-gemini-032.md`: Direct continuation of the llm-gemini plugin's version history (0.32 → 0.33 → 0.34), adding `gemini-3.8-flash` to the model-slug inventory documented in both predecessor notes.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 2: Extends the corpus's Gemini Flash pricing history — 3.5 Flash launched at a 3–6x premium over its predecessor tier, whereas 3.8 Flash (Claim 5 above) launches at price parity with 3.7 Flash, with a scheduled 2x increase four months out. The two notes together show Gemini Flash-tier pricing behaving inconsistently release-to-release rather than following a single trend.
  - `blog-simonwillison-claude-fable-5.md`: Extends this corpus's coverage of "Fable 5" (Claude) by documenting a concrete artifact it built — the `llm-coding-agent` plugin (Claim 13) — via a two-prompt spec-then-TDD workflow, outside of Anthropic's own marketing material.

- **Novel**:
  - First in-corpus documentation of the `llm-coding-agent` plugin itself: its `llm code` CLI, its `approve=` parameter's three modes (`True`/callable/`None`-with-`resume()`), and its `CodingTools` toolbox (read/write/edit/search/execute, confined to a root directory).
  - First in-corpus full-transcript-level view of an agentic coding session's tool-approval decline path actually being exercised (Claim 8) rather than just described in the abstract.
  - First in-corpus concrete numeric demonstration of prompt-cache growth over a single agentic session on Google's Gemini API specifically (prior caching coverage in this corpus, e.g. `blog-anthropic-prompt-caching-everything.md`, is Anthropic-specific).
  - First in-corpus detailed documentation of the CSP-meta-tag-plus-sandboxed-iframe pattern for safely rendering untrusted HTML/SVG content generated by (or embedded from) an LLM, including the specific directive set and the "never combine `sandbox=\"allow-scripts\"` with `allow-same-origin`" rule.
  - First in-corpus record of Gemini 3.8 Flash and Gemini 3.8 Flash Cyber, including the Cyber variant's restricted "Fairwind Program" access model — a gated-access pattern for a specialized model variant not previously documented in this corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows — model access)**: Add `gemini-3.8-flash` to the `llm`/`llm-gemini` model-slug inventory (`llm install -U llm-gemini && llm -m gemini-3.8-flash`), noting it retains the low/medium/high thinking-level scheme introduced with Gemini 3.7 Flash rather than the wider 4-tier scheme Gemini 3.6 Flash had. Cite Claim 1.
- **Chapter 02 (Harness Engineering — tool-approval and agent discipline)**: This is the strongest candidate for new material. Add `llm-coding-agent`'s three-mode `approve=` design (`True` / callable / `None`+`resume()`) as a minimal, citable reference implementation of human-in-the-loop tool approval for a from-scratch agent harness — worth contrasting with heavier commercial harnesses already documented elsewhere in the guide. Pair with the transcript-observed system prompt (Claim 9, quoted verbatim above) as a compact template for "explore first, minimal diff, verify, don't bluff" instructions, and with Claim 8's concrete evidence that all four declined tool calls in the session were respected — the agent adapted on the very next turn each time rather than retrying. Carry Claim 8's caveat across too: this design gates on the *tool* (`execute_command` is categorically "mutating"), not on the command's actual effect, so read-only shell commands like `git diff` prompt exactly as `rm` does. If the guide recommends this pattern, it should recommend it alongside command-pattern pre-approval (`--allow`), or it is recommending approval fatigue. Cite Claims 7, 8, 9.
- **Chapter 02 or 06 (Harness Engineering / Security — sandboxing untrusted content)**: Add the CSP-meta-tag-plus-iframe-sandbox pattern (Claim 11, with the full directive set and code in Concrete Artifacts) as a concrete recipe for any tool that must render LLM-generated or user-supplied HTML/SVG safely — this is more specific and code-level than the general sandboxing discussion in `blog-simonwillison-datasette-apps.md` already cited in the guide. Cite Claim 11.
- **Chapter 03 or 05 (Tooling / Orchestration — prompt caching economics)**: If the guide's prompt-caching coverage is currently Anthropic-specific (via `blog-anthropic-prompt-caching-everything.md`), add this transcript's ~98%-cached final-turn figure as cross-provider evidence the same caching economics apply to Gemini's agentic tool-use API. Cite Claim 12.
- **Chapter 04 (Deployment — model pricing/availability tracking)**: Update pricing tables with Gemini 3.8 Flash's time-boxed introductory rate ($0.75/$3.75 per million tokens through Dec 31, 2026, then $1.50/$7.50) and flag the scheduled increase date as an operational planning item, distinct from the immediate multi-x price jump the guide may already note for Gemini 3.5 Flash. Cite Claim 5.

## Extraction Notes

- **Five sources fetched and read in full**: the blog post (via `curl` + HTML-stripping, quotes verified character-for-character against raw HTML), the GitHub release page (confirms blog post text verbatim), Google's official Gemini 3.8 Flash/Cyber announcement (blog.google, fetched via `curl` and cross-checked against the raw stripped text — not relied upon via an intermediary summarizer), the `llm-coding-agent` GitHub repo page and its raw `README.md` (fetched separately to get exact code-block formatting), and the full 9,161-line gist transcript (fetched via `curl`, read start-to-finish plus targeted greps for `playwright`/`pytest`/tool-call counts to confirm session scope: ~99 tool calls, 2026-09-02T16:56:45 to 17:09:46 UTC).
- **Not fetched**: Willison's separate "pelican riding a bicycle" benchmark grid for Gemini 3.8 Flash — the blog post links to it via the rendered SVG demo tool, but it is a distinct artifact from a sibling in-feed post (`2026/Sep/4/astra-pelicans/`) rather than part of this release note; left for that post's own mining pass if triaged separately.
- **No contradictions found requiring MINER.md §4a filing**: the pricing-trend difference noted under Claim 5's "Our assessment" (3.8 Flash launching at price parity vs. 3.5 Flash's 3–6x jump) is a release-to-release variation in the same vendor's pricing behavior, not two sources disagreeing about the same fact — not a contradiction under MINER.md's guidance.
- **Cross-reference verification performed**: `blog-simonwillison-llm-gemini-032.md` Claim 2 confirmed at lines 33-38 (same-day GA-to-plugin pattern). `blog-simonwillison-llm-gemini-033.md` Claim 1 confirmed at lines 26-30 (the ~3-month gap that broke the same-day cadence) and Claim 8 confirmed at lines 68-72 (3.7 Flash's high/medium/low tiers, dropping "minimal"). `blog-simonwillison-gemini35-flash-pricing.md` Claim 2 confirmed at lines 33-38 (3.5 Flash's 3-6x pricing jump). `blog-anthropic-prompt-caching-everything.md` Claim 1 confirmed at line 39 heading text and Claim 3 confirmed at line 65 heading text. `blog-anthropic-how-contain-claude.md` Claim 6 confirmed at lines 137-152 (93% approval rate, approval fatigue). `blog-simonwillison-datasette-apps.md` confirmed to exist and cover CSP/sandbox content via grep match (not re-read in full for this note; cited only for the corroboration that the pattern name "datasette-apps sandbox" traces to that tool, which the transcript itself states directly). `blog-simonwillison-claude-fable-5.md` confirmed to exist as the corpus's coverage of "Fable 5"/Claude naming, cited only for that identification, not for specific numbered claims. All numbered claim citations verified by document-order count in the cited notes before writing this note's cross-references.
