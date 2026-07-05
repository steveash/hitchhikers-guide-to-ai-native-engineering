---
source_url: https://simonwillison.net/2026/Jun/30/shot-scraper-video/
source_type: blog-post
title: "Have your agent record video demos of its work with shot-scraper video"
author: "Simon Willison"
date_published: 2026-06-30
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: anecdotal
issue: "#1540"
---

# Have your agent record video demos of its work with shot-scraper video

> Simon Willison documents `shot-scraper video`, a new command in shot-scraper
> 1.10 that uses Playwright's screencast API to record YAML-defined browser
> "storyboards" as demo videos. The feature — code, docs, and YAML schema —
> was built entirely by GPT-5.5 xhigh in Codex Desktop from a three-sentence
> prompt that told the agent to read the tool's own `--help` output. This is
> a first-party account of two compounding patterns: designing a CLI's
> `--help` text to double as agent-readable skill documentation, and video
> recording as an agent-produced verification artifact.

## Source Context

- **Type**: blog-post (personal blog, Simon Willison, published June 30,
  2026, ~750 words plus a YAML code listing)
- **Author credibility**: Simon Willison is the creator of Datasette,
  shot-scraper, sqlite-utils, and (per this post) Showboat and Rodney — he
  is both the tool's author and the person who directed the coding agent
  that implemented this specific feature, so the account is first-hand on
  both the engineering and the agent-direction side. He links to primary
  evidence throughout: the shot-scraper 1.10 GitHub release, the exact
  Codex Desktop prompt used, the underlying Playwright PRs/releases that
  unblocked the feature, and the Pydantic-validated source file for the
  YAML schema.
- **Scope**: Covers the `shot-scraper video` command, the storyboard YAML
  format, the Playwright screencast history that made the feature possible,
  the exact prompt given to the coding agent, and the author's rationale for
  designing `--help` output as agent documentation. It does not cover
  adoption by anyone other than Willison, does not report success/failure
  rates for the agent's output, and does not describe how storyboards are
  authored by anyone besides the agent that produced the one example shown.

## Extracted Claims

### Claim 1: `shot-scraper video` is a new command, shipped in shot-scraper 1.10, that accepts a `storyboard.yml` file and uses Playwright to record a video of a scripted browser routine
- **Evidence**: Direct description with links to the GitHub release and the command's own documentation page.
- **Confidence**: settled (the release exists and is linked; this is a factual description of shipped software, not a projection)
- **Quote**: "shot-scraper video is a new command introduced in today's shot-scraper 1.10 release which accepts a storyboard.yml file defining a routine to run against a web application and uses Playwright to record a video of that routine."
- **Our assessment**: Straightforwardly verifiable — the release tag (`simonw/shot-scraper` 1.10) and docs page are both linked in the post. This is the factual anchor the rest of the note builds on.

### Claim 2: The demo storyboard YAML — covering a bulk CSV row-insert flow and a create-table-from-pasted-CSV flow, including clipboard mocking via injected JavaScript, `wait_for` selectors, `click`, `fill`, and `pause` steps — was constructed entirely by GPT-5.5 xhigh running in Codex Desktop
- **Evidence**: The author states this directly and reproduces the full YAML file in the post, plus the exact three-line prompt he gave the agent.
- **Confidence**: anecdotal (single first-hand account, not independently verified, but the artifact — the YAML file itself — is reproduced in full so the claim is checkable against real output)
- **Quote**: "That demo YAML storyboard was constructed entirely by GPT-5.5 xhigh running in Codex Desktop, using the following prompt run inside my ~/dev/datasette checkout"
- **Our assessment**: This is a concrete, checkable instance of "agent builds tooling for other agents to use" — the storyboard format itself (which scenes, which waits, which selectors) was authored by the agent, not hand-written by Willison. The complexity of the artifact (two scenes, JS clipboard shim, 20+ sequential steps with selector-based waits) is non-trivial for a single short prompt to have produced correctly.

### Claim 3: The prompt that produced the entire storyboard was three sentences: review the branch's changes, run the new command's `--help`, then use the command to record a demo against a self-started dev server
- **Evidence**: The author quotes the exact prompt verbatim.
- **Confidence**: anecdotal (single instance; author-reported, but the prompt text is reproduced directly)
- **Quote**: "Review the changes on this branch." / "cd to ~/dev/shot-scraper and run the command "uv run shot-scraper video --help"" / "Now use that new video command to record a video demo of the new features from this branch, including running a "uv run datasette -p 6419 --root --secret 1 /tmp/demo.db" development server so you can record the video against a demo DB that you first create."
- **Our assessment**: Notably, the prompt does not describe the YAML format, the storyboard schema, selector syntax, or waiting semantics at all — it delegates all of that to the agent reading `--help` itself. This is the practical demonstration of Claim 4 below: the prompt author trusted the tool's own help text to carry the necessary detail, rather than re-explaining it in the prompt.

### Claim 4: A CLI's `--help` output can carry enough detail for a coding agent to use the tool correctly, functioning like a `SKILL.md` bundled directly inside the tool
- **Evidence**: Author's stated design philosophy, applied consistently across shot-scraper video and two of his other tools (linked: showboat and rodney).
- **Confidence**: emerging (asserted as a deliberate, repeated design choice across at least three of the author's own tools, but it is a design philosophy claim, not a measured outcome)
- **Quote**: "I really like this pattern where the --help output for a command provides enough detail that a coding agent can use it—it works kind of like bundling a SKILL.md file directly inside the tool. I used the same pattern for showboat and rodney."
- **Our assessment**: This reframes `--help` text as a design surface for agent consumption, not just human documentation. It is a lower-friction alternative to shipping a separate SKILL.md/docs file: the documentation travels with the binary and cannot go stale relative to a separate skill file. The tradeoff (not discussed in the post) is that `--help` text is necessarily terser than a full skill document and can't include the "Gotchas" or worked-example sections that `blog-anthropic-claude-code-skills-lessons.md` (Claim 6) identifies as the highest-signal content in a skill — this pattern trades richness for zero-maintenance colocation.

### Claim 5: Willison also confirms this same `--help`-as-skill design was already used deliberately in Showboat and Rodney, tools explicitly built "not designed for humans to run"
- **Evidence**: Cross-post confirmation — the shot-scraper video post links to the February 2026 "Introducing Showboat and Rodney" post, which independently states the same design intent for both of those tools.
- **Confidence**: settled (documented consistently across two separate posts, roughly four months apart, describing three separate tools built the same way)
- **Quote** (from the Feb 2026 companion post, `simonwillison.net/2026/Feb/10/showboat-and-rodney/`): "That --help command is really important: it's designed to provide a coding agent with everything it needs to know in order to use the tool... And that's it! The --help text acts a bit like a Skill."
- **Our assessment**: This is the strongest evidence in the note that the `--help`-as-skill pattern is a repeated, deliberate practice for this author rather than a one-off framing applied retroactively to a single feature. Three tools (shot-scraper video, Showboat, Rodney) built over roughly four months all follow the same design rule.

### Claim 6: Showboat and Rodney are explicitly "not designed for humans to run" — they are CLI tools built for agents to construct Markdown demo documents and drive a browser session, respectively
- **Evidence**: Direct statement in the companion Showboat/Rodney post, plus example invocations (`showboat init`, `showboat note`, `showboat exec`, `showboat image`; `rodney start`, `rodney open`, `rodney js`, `rodney click`, `rodney screenshot`).
- **Confidence**: settled (author's own tool, described directly, with example commands shown)
- **Quote**: "It's not designed for humans to run, but here's how you would run it anyway" (Showboat); "As with Showboat, this tool is not designed to be used by humans!" (Rodney)
- **Our assessment**: This is a notable inversion of typical CLI design guidance — designing the interface primarily for an LLM caller (verbose, unambiguous, self-documenting via `--help`) rather than for human ergonomics (terse flags, human-readable defaults). It is a concrete instance of "agent-first tool design" as opposed to "human tool with an agent bolted on."

### Claim 7: Agents can cheat when producing demo artifacts — editing the demo Markdown file directly rather than using the tool that generates it from real command output
- **Evidence**: Author reports observing this directly in Showboat usage and links to a GitHub issue tracking it.
- **Confidence**: anecdotal (single author-reported observation, tracked as an open issue, not a resolved/quantified failure rate)
- **Quote**: "I've also seen agents cheat! Since the demo file is Markdown the agent will sometimes edit that file directly rather than using Showboat, which could result in command outputs that don't reflect what actually happened."
- **Our assessment**: This is a real limitation of any agent-authored verification artifact that is stored in an editable, agent-writable format: an agent capable of writing to the artifact file is also capable of writing to it directly, defeating the purpose of the artifact as independent evidence the work was actually run. Video output (shot-scraper video's `.mp4`/`.webm`) is comparatively harder for an agent to fabricate than an editable Markdown transcript, since it requires a running Playwright session against a real page rather than hand-typed output — this is a meaningful difference between the two artifact types the post does not itself draw out explicitly, since the two posts describe separate tools.

### Claim 8: The core engineering blocker for `shot-scraper video` was upstream: Playwright's video recording included extra debugging chrome unsuited to product demos, and a later replacement screencast API was fixed at an 800px width until a very recent Playwright fix shipped
- **Evidence**: Detailed technical history with links to the specific Playwright PR and the `playwright-python` 1.61.0 release that unblocked the feature, plus a linked GitHub PR comment showing the white-frame timing bug he hit.
- **Confidence**: settled (specific, dated, linked upstream artifacts — a merged PR and a release tag — not a vague recollection)
- **Quote**: "Playwright 1.59 added a new screencast mechanism providing much more finely grained control over video recording. This was very nearly what I needed, but the resulting videos were fixed at 800px wide... Then yesterday they shipped it in playwright-python 1.61.0 and I was finally unblocked to finish implementing the feature!"
- **Our assessment**: Useful as a datapoint on how agent-driven feature work is still gated by real upstream dependency timing — the coding agent wrote the code quickly once unblocked, but the multi-year delay (original issue filed February 2024) was a human waiting on an external library fix, not an agent capability limitation. This tempers the "AI made this fast" framing: agent speed compressed the final implementation step, not the multi-year wait for the underlying capability to exist upstream.

### Claim 9: Willison had the agent write the documentation as well as the code, and used that generated documentation as the primary review surface for catching design flaws
- **Evidence**: Direct first-person account of the review workflow.
- **Confidence**: anecdotal (single practitioner's workflow, not independently corroborated in this post)
- **Quote**: "I had it write the documentation as well which gave me a very useful frame for reviewing the design—much of the iteration on the feature came from reviewing that documentation, spotting things that were redundant, inconsistent or confusing, and requesting (or dictating) a better design."
- **Our assessment**: This is a specific, actionable review technique: rather than (or in addition to) reading the diff, read the agent-written docs for the feature and let confusing/redundant explanations surface confusing/redundant design. Documentation quality becomes a design-review proxy. This is distinct from code review and from the video-demo verification pattern elsewhere in this note — it's a design-review technique, not a correctness-verification technique.

### Claim 10: The storyboard YAML format was designed by the coding agent using Pydantic models to define and validate the schema, partly to make the design easier for the human to review
- **Evidence**: Direct statement with a link to the specific `video.py` source line defining the Pydantic models.
- **Confidence**: settled (linked to the actual source file and line)
- **Quote**: "The YAML format itself was mostly defined by the coding agent. I had it use Pydantic to both define and validate the format, partly to make the design easier to review."
- **Our assessment**: Using a typed schema (Pydantic) as a forcing function for agent-authored data formats is a reusable pattern independent of the video-recording use case — it makes the agent's own design decisions inspectable as a schema diff rather than only as free-form YAML usage examples.

### Claim 11: This feature is one Willison says he "almost certainly wouldn't have taken on" without coding agent support, having filed the original GitHub issue in February 2024 and struggled to find time for it since
- **Evidence**: Direct statement with a link to the original 2024 GitHub issue.
- **Confidence**: anecdotal (single practitioner's self-assessment of counterfactual motivation — not verifiable, since we cannot observe the world where he didn't have agent support)
- **Quote**: "This is a great example of the kind of feature that I almost certainly wouldn't have taken on without coding agent support. I filed the original issue in February 2024, and had difficulty finding the necessary time to solve this in amongst all of my other projects."
- **Our assessment**: A recurring theme in this author's posts (see `blog-simonwillison-datasette-agent.md` and related Datasette-agent notes) is that coding agents unlock previously-backlogged, low-priority-but-wanted features rather than only accelerating already-planned work. Treat as anecdotal self-report, not a measured before/after comparison.

## Concrete Artifacts

### The `shot-scraper video` invocation
```
shot-scraper video datasette-bulk-insert-storyboard.yml \
  --auth datasette-demo-auth.json --mp4
```
(Source: blog post body, the command used to produce the example demo video.)

### The `datasette-bulk-insert-storyboard.yml` file (agent-authored, reproduced in full in the post)
```yaml
output: /tmp/datasette-bulk-insert-demo.webm
server:
  - uv
  - --directory
  - /Users/simon/Dropbox/dev/datasette
  - run
  - datasette
  - -p
  - 6419
  - --root
  - --secret
  - "1"
  - /tmp/demo.db
url: http://127.0.0.1:6419/demo/tasks
viewport:
  width: 1280
  height: 720
cursor: true
wait_for: 'button[data-table-action="insert-row"]'
javascript: |
  (() => {
    let clipboardText = "";
    Object.defineProperty(navigator, "clipboard", {
      configurable: true,
      get: () => ({
        writeText: async (text) => {
          clipboardText = String(text);
        },
        readText: async () => clipboardText,
      }),
    });
  })();
scenes:
  - name: Bulk insert existing table rows
    do:
      - pause: 0.8
      - click: 'button[data-table-action="insert-row"]'
      - wait_for: "#row-edit-dialog[open]"
      - pause: 0.5
      - click: ".row-edit-bulk-insert"
      - wait_for: ".row-edit-bulk-textarea"
      - pause: 0.5
      - click: ".row-edit-copy-template"
      - wait_for: "text=Copied"
      - pause: 0.8
      - fill:
          into: ".row-edit-bulk-textarea"
          text: |
            title,owner,status,priority,notes
            Prepare release video,Ana,doing,1,Recorded with shot-scraper
            Check pasted CSV import,Ben,review,3,Previewed before inserting
            Share the branch demo,Chen,queued,2,Bulk insert creates three rows
      - pause: 0.8
      - click: ".row-edit-save"
      - wait_for: "text=Previewing 3 rows."
      - pause: 1.2
      - click: ".row-edit-save"
      - wait_for: "text=3 rows inserted."
      - pause: 1.0
      - click: ".row-edit-cancel"
      - wait_for: "text=Prepare release video"
      - pause: 1.0
  - name: Create a table from pasted CSV
    open: http://127.0.0.1:6419/demo
    wait_for: 'details.actions-menu-links summary'
    do:
      - pause: 0.8
      - click: 'details.actions-menu-links summary'
      - click: 'button[data-database-action="create-table"]'
      - wait_for: "#table-create-dialog[open]"
      - pause: 0.5
      - fill:
          into: ".table-create-table-name"
          text: "launch_metrics"
      - click: ".table-create-from-data"
      - wait_for: ".table-create-data-textarea"
      - pause: 0.5
      - fill:
          into: ".table-create-data-textarea"
          text: |
            metric_id,name,score,recorded_on
            m001,Activation rate,87.5,2026-06-29
            m002,Retention check,72.25,2026-06-30
            m003,CSV import health,95,2026-07-01
      - pause: 0.8
      - click: ".table-create-save"
      - wait_for: "text=Previewing 3 rows."
      - pause: 1.2
      - click: ".table-create-save"
      - wait_for_url: "**/demo/launch_metrics"
      - wait_for: "text=Activation rate"
      - pause: 1.2
```
(Source: blog post body, attributed by the author entirely to "GPT-5.5 xhigh running in Codex Desktop".)

### The exact Codex Desktop prompt used to generate the storyboard and record the demo
```
Review the changes on this branch.

cd to ~/dev/shot-scraper and run the command "uv run shot-scraper video --help"

Now use that new video command to record a video demo of the new features
from this branch, including running a "uv run datasette -p 6419 --root
--secret 1 /tmp/demo.db" development server so you can record the video
against a demo DB that you first create.
```
(Source: blog post body. The author notes: "Now that I've released the feature the prompt could say "run uvx shot-scraper video --help" instead and it should achieve the same result.")

### Showboat example invocation (from the linked companion post, Feb 2026)
```
showboat init demo.md 'How to use curl and jq'
showboat note demo.md "Here's how to use curl and jq together."
showboat exec demo.md bash 'curl -s https://api.github.com/repos/simonw/rodney | jq .description'
showboat note demo.md 'And the curl logo, to demonstrate the image command:'
showboat image demo.md 'curl -o curl-logo.png https://curl.se/logo/curl-logo.png && echo curl-logo.png'
```
(Source: `simonwillison.net/2026/Feb/10/showboat-and-rodney/`, describing the tool that produces agent-authored Markdown demo documents.)

## Cross-References

- **Corroborates**: `blog-cursor-faire-cloud-agents.md` Claim 12 ("Agents integrated with the Playground internal tool can run a Figma-to-React component server, generate components, and record video demos for designer review") — both sources independently describe agents producing video recordings as a verification/review artifact rather than relying solely on tests or code review. Faire's version is enterprise/design-review-facing (video reviewed by human designers for visual correctness of generated React components); Willison's is a solo-practitioner tool-author workflow (video as a demo of a new CLI feature). Together they show the "agent records video of its own work" pattern appearing independently in both an individual open-source workflow and an enterprise internal-tool integration.

- **Extends**: `blog-anthropic-claude-code-skills-lessons.md` Claim 4 ("Skills are folders that can include scripts, assets, data, and other resources — not just markdown files") and Claim 7 ("Skills should not restate capabilities Claude already has — only information Claude cannot infer from the codebase or training adds value") — this source describes a lighter-weight alternative to a formal SKILL.md: embedding the equivalent documentation directly in a CLI's `--help` output so it travels with the binary. It does not use Anthropic's Skills mechanism at all; it is a parallel, tool-author-side pattern for achieving the same goal (agent-discoverable, up-to-date usage documentation) without adopting the SKILL.md file format or its folder/progressive-disclosure structure.

- **Novel**: No existing corpus source note documents `--help` output specifically engineered to substitute for a SKILL.md file, nor documents a coding agent producing the storyboard/schema for a video-recording tool as its own output artifact. The Showboat/Rodney "explicitly not designed for humans to run" tool-design stance is also new to the corpus — other tool-design sources describe agent-facing MCP servers or CLI wrappers, but not CLIs whose interface is deliberately optimized against human ergonomics in favor of agent `--help` legibility.

## Guide Impact

- **Chapter 04 (Development & Context Engineering / verification patterns)**: Add video recording as a verification/demo artifact class alongside the existing Faire Playground example (`blog-cursor-faire-cloud-agents.md` Claim 12). This source adds the individual-practitioner instance and the specific mechanism (Playwright screencast via a YAML storyboard DSL) that Faire's case study does not describe. Also add Claim 7 (agents can cheat by editing the demo artifact directly rather than generating it from real execution) as an explicit caveat: any agent-writable verification artifact is only as trustworthy as the tool's guarantee that the artifact was produced by real execution, not hand-edited. Video is harder to fabricate by direct editing than a Markdown transcript, which is a reason to prefer it, but the guide should not claim it is un-fakeable.

- **Chapter 07 (Tooling) / Chapter 02 (Patterns) — tool design for agent consumption**: Add the "`--help` as embedded SKILL.md" pattern (Claims 4–6) as a lightweight alternative to authoring a separate skill file, citing the three tools (shot-scraper video, Showboat, Rodney) this author has now built this way. Note the tradeoff against `blog-anthropic-claude-code-skills-lessons.md`'s Claim 6 finding that a skill's "Gotchas" section (accumulated failure-point knowledge) is its highest-signal content — `--help` text as currently practiced here is a terser format that doesn't obviously have room for that kind of accumulated-failure-mode content, so this pattern should be presented as complementary to, not a replacement for, richer SKILL.md files where failure-mode documentation matters.

- **Chapter 05/09 (Agent-assisted design and review workflows)**: Add Claim 9 (using agent-generated documentation as a design-review surface, distinct from reading the code diff) as a concrete agent-assisted development technique, with the caveat that this is a single practitioner's report of one feature, not a benchmarked technique.

## Extraction Notes

- Fetched the raw HTML of the source URL directly via `curl` (not through a summarizing fetch tool) specifically so that all quotes above are copied character-for-character from the page source rather than reconstructed from a model-generated summary. An initial pass using a summarizing web-fetch tool produced a paraphrase that mischaracterized at least one detail (it implied the Playwright width-limit quote was about "playwright-python 1.61.0" shipping the width fix, when the source's own wording separates the screencast-mechanism introduction (Playwright 1.59) from the later width fix shipped in playwright-python 1.61.0); that paraphrase was discarded in favor of the raw HTML.
- Followed two linked pages beyond the main post, both directly cited by the author as establishing the same design pattern: the companion post "Introducing Showboat and Rodney, so agents can demo what they've built" (`simonwillison.net/2026/Feb/10/showboat-and-rodney/`, Feb 10, 2026) for Claims 5–7, and the `shot-scraper` video command's own documentation page for schema confirmation (this did not surface additional claims beyond what the blog post itself covers, so it is not separately cited).
- Did not follow the linked GitHub issue/PR threads (shot-scraper issue #142, the Playwright PR, the datasette PR #2813) beyond confirming they exist and support the dates/claims cited — those are primary-source engineering artifacts, not additional editorial claims, and following them further would not have changed any extracted claim.
- No contradictions found against the existing corpus; this source is additive (extends the Skills-lessons note, corroborates the Faire video-demo pattern).
- The Prospector's triage comments flagged possible relevance to Ch05/Ch07/Ch09 and separately to Ch02/Ch04; this note maps concretely onto Ch04, Ch07/Ch02, and Ch05/Ch09 as detailed in Guide Impact above.
