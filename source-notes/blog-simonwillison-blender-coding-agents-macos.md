---
source_url: https://simonwillison.net/2026/Sep/5/blender-coding-agents-macos/
source_type: blog-post
title: "Using Blender with coding agents on macOS"
author: Simon Willison
date_published: 2026-09-05
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: anecdotal
issue: "#3319"
---

# Using Blender with coding agents on macOS

> Simon Willison's TIL walkthrough of driving the desktop Blender application
> from ChatGPT Codex (GPT-6 Astra) on macOS: three successive natural-language
> prompts iteratively build and re-render a "pelican riding a bicycle" scene
> via Blender's Python API, Codex recovers from a sandboxed-launch crash by
> retrying with expanded execution permission, and Codex's built-in
> "skill-creator" skill is used to auto-author and install a reusable local
> `blender-local` SKILL.md from what it learned during the session — which
> Willison confirms he has since reused for further Blender work. Total
> project cost: covered by an existing Codex subscription, estimated by the
> local cost-tracking tool AgentsView at $4.24 at API prices for `gpt-6-astra`.

## Source Context

- **Type**: blog-post / TIL (Willison publishes TILs at
  `til.simonwillison.net` and cross-posts a shorter version to his main
  weblog at `simonwillison.net`; the issue's source URL is the weblog
  cross-post, which is substantially shorter than the canonical TIL page at
  `til.simonwillison.net/llms/blender-coding-agents-macos`). Per MINER.md
  §1, this note follows the canonical TIL page directly, since it contains
  material — the more explicit invocation command, the per-turn timing data,
  the "Creating a skill" section, and links to the generated `SKILL.md` and
  Codex transcript — that the shorter weblog cross-post omits entirely. Both
  pages were fetched and cross-checked; the two texts do not conflict, the
  TIL page is simply longer.
- **Author credibility**: Simon Willison is a `trusted-feed` source already
  extensively used in this corpus (creator of Django, Datasette,
  `sqlite-utils`, the `llm` CLI, and originator of the recurring "pelican
  riding a bicycle" benchmark prompt examined in
  `blog-simonwillison-pelicanmaxxing.md` and
  `blog-simonwillison-astra-pelican-comparison-grid.md`). This post is a
  first-person hands-on practitioner account — Willison ran the sessions
  himself, on his own Mac, and links the full project repo and an exported
  Codex transcript as primary evidence, which is stronger sourcing than a
  purely descriptive blog post.
- **Scope**: Covers a single practitioner's single project (three
  Blender-rendering turns plus one skill-authoring turn) using ChatGPT
  Codex with GPT-6 Astra (Medium reasoning) on macOS. Does not cover:
  reliability across repeated runs, other operating systems, other coding
  agents (Claude Code, Cursor, etc.) driving Blender, quantitative
  render-quality scoring, or any systematic evaluation — this is a single
  anecdotal TIL, not a benchmark.

## Extracted Claims

### Claim 1: Willison asserts that current frontier models have become "really good" at operating Blender, able to both produce editable `.blend` files and render images or image-sequence movies via Blender's Python API
- **Evidence**: Author's direct first-person assessment, stated as the opening claim of the post, followed by a working demonstrated example.
- **Confidence**: anecdotal (single practitioner's qualitative assessment, no comparison across models or repeated trials)
- **Quote**: "Modern frontier models have got really good at using Blender."
- **Our assessment**: A general capability claim from a credible, experienced practitioner, but backed by exactly one demonstrated project in this post (GPT-6 Astra only). The claim that models can render "even movies (by rendering a sequence of images and combining them with ffmpeg)" is stated but not demonstrated in this particular post — no video output appears in the linked repo's `outputs/` directory, only `.blend` files and PNG stills.

### Claim 2: Setting up a coding agent to drive Blender on macOS requires only installing the standard Blender desktop application and issuing a single natural-language prompt referencing its install path
- **Evidence**: Direct step-by-step setup instructions with a literal example prompt that Willison confirms worked.
- **Confidence**: anecdotal
- **Quote**: "Setting this up, at least on macOS, is really easy. Install the Blender desktop app from blender.org and then tell the coding agent: Use the already install /Applications/Blender to render a scene of a pelican riding a bicycle"
- **Our assessment**: Notably low-friction: no MCP server, no custom tool definition, no plugin — the agent discovers and drives a full third-party GUI creative application purely by being told its install path and invoked through its command-line/Python interface. This is a concrete example of "agent uses an arbitrary local application via its native CLI/scripting interface" rather than a purpose-built integration.

### Claim 3: A more explicit invocation command that names Blender's actual background-rendering flags saves the model time it would otherwise spend discovering how to invoke Blender itself
- **Evidence**: Author's stated optimization, given as an alternative to the plain-English setup prompt in Claim 2.
- **Confidence**: anecdotal
- **Quote**: "You can also be a bit more explicit, to save the model some time figuring out how to use it: Use Blender like this: /Applications/Blender.app/Contents/MacOS/Blender --background --python scene.py"
- **Our assessment**: A small but generalizable pattern for tool-invocation prompting: giving the exact CLI invocation up front avoids spending agent turns on trial-and-error discovery of a tool's interface, trading a small amount of prompt specificity for reduced latency/cost on the first turn.

### Claim 4: Three successive short natural-language follow-up prompts, each requesting general creative improvement rather than specific edits, produced a visibly more elaborate and polished 3D scene at each step
- **Evidence**: The prompts and resulting file names are given in sequence in the TIL post's "A pelican riding a bicycle with GPT-6 Astra" section, and separately preserved (not overwritten) as three distinct `.blend`/script pairs in the linked GitHub repo.
- **Confidence**: anecdotal
- **Quote**: "OK add a background and a lot of flair" / "OK make it a whole lot better"
- **Our assessment**: The prompts are strikingly non-specific ("a lot of flair," "a whole lot better") yet the agent produced concrete, described improvements each round (see Concrete Artifacts) — evidence that the model is filling in creative/technical specifics itself rather than requiring the user to specify exact changes. This mirrors iterative-refinement patterns seen elsewhere in the corpus for code and image generation, applied here to a 3D scene-graph domain.

### Claim 5: Each of the three Blender-rendering turns took multiple minutes of wall-clock time, with later (more complex) turns taking longer
- **Evidence**: Explicit elapsed-time labels given after each prompt in the TIL post's session walkthrough: 2m39s, 3m51s, 5m59s for the three successive turns.
- **Confidence**: anecdotal (single session, single project, no repeated-trial variance data)
- **Quote**: "2m39s later:" / "3m51s later:" / "5m59s later:"
- **Our assessment**: Useful as a concrete order-of-magnitude data point: agentic Blender workflows here run in single-digit minutes per turn, not seconds, and cost scales with scene complexity (the final, most elaborate turn took over twice as long as the first). Relevant for setting expectations about latency when an agent is driving a real rendering pipeline rather than just generating text or code.

### Claim 6: Codex's first attempt to launch Blender inside a sandboxed execution environment crashed (exit code 139) before the script ran; retrying with expanded, unsandboxed execution permission succeeded
- **Evidence**: Documented in the "Execution and diagnosis" section of the `SKILL.md` file Codex authored during the session (linked from the TIL post as `outputs/blender-local/SKILL.md` in the project repo), and independently visible in the exported Codex transcript ("Blender crashed at startup in the restricted environment. I'm retrying with the access Blender needs to render.").
- **Confidence**: anecdotal (single observed occurrence)
- **Quote**: "The first sandboxed launch in this project exited with code 139 before running the script and wrote `blender.crash.txt` in the system temporary directory. A retry through the approved unsandboxed execution mechanism succeeded."
- **Our assessment**: A concrete, specific failure mode for agents driving full desktop GUI applications from within a sandbox: a heavyweight native application (Blender) may simply fail to start under sandbox restrictions that are fine for typical CLI tools, requiring an explicit unsandboxed retry. The generated skill explicitly cautions against over-generalizing from this single crash ("Treat this as an observed environment issue, not proof that every crash needs escalation"), which is a notably calibrated, non-alarmist note for a self-authored artifact.

### Claim 7: After completing the rendering task, Codex used its own built-in "skill-creator" skill, unprompted in structure (only prompted in intent), to author and install a new local skill summarizing what it had learned about using this Blender installation
- **Evidence**: Described directly in the TIL post's "Creating a skill" section and confirmed in the Codex transcript, which shows Codex reading `~/.codex/skills/.system/skill-creator/SKILL.md`, writing `outputs/blender-local/SKILL.md` (58 lines), validating it with a `quick_validate.py` script, and copying it into `~/.codex/skills/blender-local`.
- **Confidence**: anecdotal
- **Quote**: "Codex makes it pretty easy to create skills (using its built-in skill creating skill), so I finished up by prompting: Create a quick skill that describes how to use the currently installed /Application/Blender based on what you learned"
- **Our assessment**: This is the most novel-to-corpus claim in the post: a coding agent's tool-use session ending in the agent packaging its own accumulated procedural + failure-mode knowledge into an installed, reusable skill file, using a meta-skill provided by the harness itself (Codex's `skill-creator`), rather than a human manually writing the skill afterward. This is a live, concrete instance of the reactive "Gotchas section" pattern described first-party by Anthropic's Claude Code team in `blog-anthropic-claude-code-skills-lessons.md` (Claim 6) — except here the skill is self-authored by the agent from its own session experience rather than accumulated by a human maintainer over many uses.

### Claim 8: The self-authored skill records specific, non-obvious visual-QA lessons about 3D rendering correctness that a saved render alone does not guarantee — including that a "successfully saved render is not visual QA"
- **Evidence**: Direct text from the "Modeling and visual lessons" section of the generated `SKILL.md`.
- **Confidence**: anecdotal
- **Quote**: "Inspect the rendered image after meaningful changes. Check the silhouette, grip and pedal contacts, floating parts, frame cropping, shadows, and whether background details are actually visible. A successfully saved render is not visual QA."
- **Our assessment**: A specific, well-formed verification principle that generalizes beyond Blender: a process completing without error (the render saves) is not evidence that the output is correct (the scene composition may still be broken — e.g., the skill separately notes that a retained studio floor plane silently occluded a new beach/ocean addition, "coincident surfaces produced black bands"). This is the same "process success ≠ output correctness" principle the corpus documents elsewhere for code (tests passing ≠ code correct) applied here to generative 3D content — a genuinely new domain instance of a recurring corpus theme, not a new principle.

### Claim 9: Willison confirms the self-authored `blender-local` skill was subsequently reused, unmodified in origin, for further Blender work after this initial session
- **Evidence**: Author's direct statement following the skill installation.
- **Confidence**: anecdotal (single follow-on use case cited, not a sustained-use track record)
- **Quote**: "It produced and installed this Markdown skill, which I have since used for further Blender experiments with prompts like this: Use your Blender Local skill to build this scene (attached image)"
- **Our assessment**: This is the load-bearing evidence that the self-authored skill was not a one-off artifact abandoned after creation — it persisted in `~/.codex/skills/` and was actively invoked by name in later, separate sessions. That said, "further Blender experiments" is vague (no count, no time span, no evidence the skill was ever *updated* after its initial authoring) — treat as confirmation the pattern works at all, not evidence of long-term skill maintenance.

### Claim 10: The full multi-turn Blender project was covered by Willison's existing Codex subscription, but the local cost-tracking tool AgentsView estimated it would have cost $4.24 at API list prices for `gpt-6-astra`
- **Evidence**: Author's direct cost statement, sourced from a named third-party local analytics tool (AgentsView, an open-source local session-cost tracker for coding agents by developer "kenn-io", confirmed via its GitHub repo description: "Browse, search, and track costs across all your AI coding agents. One binary, no accounts, everything local.").
- **Confidence**: anecdotal (single project, single cost estimate, tool-reported rather than independently verified against OpenAI's billing)
- **Quote**: "This was covered by my existing Codex subscription, but according to AgentsView it would have cost $4.24 at API prices for gpt-6-astra."
- **Our assessment**: Consistent with `gpt-6-astra`'s API pricing of $10/million input tokens and $50/million output tokens established in `blog-simonwillison-gpt6-astra-launch.md` (Claim 3) — a multi-turn, multi-minute agentic session producing several hundred lines of generated Python plus multiple renders plausibly lands in low-single-dollar API cost at that pricing. This is also the first appearance of the AgentsView tool in this corpus (see Cross-References → Novel).

## Concrete Artifacts

Three-turn session sequence, from the TIL post's "A pelican riding a bicycle with GPT-6 Astra" section (model: GPT-6 Astra, Medium reasoning, ChatGPT macOS app, Codex mode):

```
Turn 1 prompt: "Use the already install /Applications/Blender to render a
                scene of a pelican riding a bicycle"
  -> 2m39s later: pelican-bicycle.blend, pelican_scene.py

Turn 2 prompt: "OK add a background and a lot of flair"
  -> 3m51s later: pelican-bicycle-festival.blend, pelican_flair.py

Turn 3 prompt: "OK make it a whole lot better"
  -> 5m59s later: pelican-coastal-parade.blend, pelican_final.py

Turn 4 prompt: "Create a quick skill that describes how to use the
                currently installed /Application/Blender based on what
                you learned"
  -> installed outputs/blender-local/SKILL.md to ~/.codex/skills/blender-local
```
(Source: `til.simonwillison.net/llms/blender-coding-agents-macos`, cross-checked
against the exported Codex transcript at
`github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/codex-transcript.md`.)

Rendered image alt text (from the weblog cross-post's embedded image, describing the
final `pelican-coastal-parade` render):

```
"A 3D illustration of a white pelican cycling along a seaside boardwalk at
sunset. It wears a cream boater hat and a coral scarf, with wings on the
handlebars and long orange legs reaching the pedals of a turquoise bicycle.
A wicker front basket holds pink and white flowers, and three balloons float
behind. Pastel bunting stretches overhead between palm trees. Striped beach
huts stand beside a teal sea with a small sailboat, beneath a large
peach-colored sun. The scene has a softly lit, toy-like style."
```

Excerpts from the agent-authored `outputs/blender-local/SKILL.md` (58 lines
total; fetched from
`github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/outputs/blender-local/SKILL.md`),
representative sections only:

```
---
name: blender-local
description: Build, edit, and render 3D scenes with the locally installed
Blender on this Mac. Use when the user requests Blender work or an editable
Blender scene.
---

## Working workflow
Write scene-building scripts in the task's `work/` directory. Execute `bpy`
scripts with Blender's bundled Python, not an ordinary Python interpreter:

    /Applications/Blender.app/Contents/MacOS/Blender --background --python work/scene.py

## Execution and diagnosis
- The first sandboxed launch in this project exited with code 139 before
  running the script and wrote `blender.crash.txt` in the system temporary
  directory. A retry through the approved unsandboxed execution mechanism
  succeeded. Treat this as an observed environment issue, not proof that
  every crash needs escalation.
- Background rendering can produce little output for tens of seconds. If
  execution returns a session ID, poll that session until completion instead
  of launching duplicate renders.

## Modeling and visual lessons
- Inspect the rendered image after meaningful changes. Check the silhouette,
  grip and pedal contacts, floating parts, frame cropping, shadows, and
  whether background details are actually visible. A successfully saved
  render is not visual QA.
- Avoid overlapping coplanar surfaces. The retained studio floor hid the new
  beach and ocean; coincident surfaces produced black bands.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt6-astra-launch.md` (Claim 3) — this post's $4.24
    total-cost figure for `gpt-6-astra` is directionally consistent with
    that note's confirmed $10/million input, $50/million output API pricing
    for the same model.
  - `blog-anthropic-claude-code-skills-lessons.md` (Claim 6) — Anthropic's
    first-party claim that "the highest-signal content in any skill is the
    Gotchas section...built up from common failure points" is independently
    corroborated here by a different vendor's agent (OpenAI Codex): the
    self-authored `SKILL.md`'s "Execution and diagnosis" section is exactly
    a Gotchas section, populated from the one crash actually observed in
    this session, not written speculatively in advance.

- **Contradicts**: None found.

- **Extends**:
  - `blog-anthropic-claude-code-skills-lessons.md` (Claim 4, Claim 6) — that
    note documents skills as a human-designed extension point ("a common
    misconception we hear about skills is that they are 'just markdown
    files'"), with Gotchas sections built up by human maintainers over
    repeated internal use. This post extends the pattern one step further:
    the skill is authored *by the agent itself*, in a single session,
    immediately after encountering the one failure it documents — compressing
    the human-maintainer accumulation loop into a single agent-driven turn.
  - `blog-simonwillison-astra-pelican-comparison-grid.md` and
    `blog-simonwillison-pelicanmaxxing.md` — both use Willison's recurring
    "pelican riding a bicycle" prompt as an informal cross-model test
    subject; this post extends that running motif from 2D SVG generation
    into a new modality (3D scene construction and rendering via a real
    third-party desktop application's Python API), and is explicitly linked
    from the TIL/blog post's own "Recent articles" list alongside the
    Sep 4, 2026 Astra pelican comparison-grid post.

- **Novel**:
  - First corpus source describing a coding agent driving a full third-party
    desktop GUI/creative application (Blender) via its native Python API/CLI,
    including recovery from a sandbox-launch crash specific to that
    application.
  - First corpus source documenting an agent's built-in meta-skill
    ("skill-creator") being used to have the agent author and install its
    *own* new skill from a single session's experience, with confirmed
    reuse in a later, separate session.
  - First corpus appearance of the AgentsView local cost-tracking tool
    (`github.com/kenn-io/agentsview`).
  - Concrete per-turn wall-clock timing data (2m39s / 3m51s / 5m59s) for an
    agentic 3D-rendering workflow — no prior corpus source has timing data
    for this kind of task.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The self-authored-skill pattern
  (Claim 7, Claim 9) is a concrete, small-scale illustration to pair with
  `blog-anthropic-claude-code-skills-lessons.md`'s human-maintained Gotchas
  section guidance — recommend adding a short example showing that the same
  "write the Gotchas section from observed failures" principle can be
  triggered by prompting the agent to self-author a skill immediately after
  a session with a real failure/recovery in it, rather than only relying on
  a human to write it retrospectively. Flag clearly as a single anecdote
  (one crash, one skill, one confirmed reuse), not a validated workflow.
- **Chapter 04 (Context Engineering)**: Claim 3 (giving the agent the exact
  CLI invocation up front to avoid discovery overhead) is a small, reusable
  context-engineering tactic for tool-invocation prompts generally, not
  specific to Blender — worth a one-line mention alongside existing guidance
  on reducing agent exploration turns for known tool interfaces.
- **Chapter 03 (Verification)**: Claim 8's "a successfully saved render is
  not visual QA" is a domain-specific instance of the "process success is
  not output correctness" principle already established in the corpus for
  code/tests — cite as a generative-3D-content example if the chapter wants
  a non-code illustration of the same idea.

## Extraction Notes

- Followed the canonical TIL page
  (`til.simonwillison.net/llms/blender-coding-agents-macos`), the linked
  GitHub project repo (`github.com/simonw/gpt-6-astra-blender-pelican-bicycle`),
  its `codex-transcript.md`, and its `outputs/blender-local/SKILL.md`, in
  addition to the shorter weblog cross-post at the issue's source URL — four
  substantive linked pages followed, within MINER.md §1's "up to 5" guidance.
  Did not fetch the individual `.blend` binary files or the three per-turn
  Python scripts (`pelican_scene.py`, `pelican_flair.py`, `pelican_final.py`)
  in full; the transcript and `SKILL.md` were sufficient to document the
  claims above without needing the raw scene-construction code.
- WebFetch's AI-summarized read of the main weblog post declined to
  reproduce article prose verbatim (citing copyright), consistent with the
  same behavior noted in `blog-simonwillison-astra-pelican-comparison-grid.md`'s
  Extraction Notes. Worked around it the same way: fetched the raw HTML of
  both the weblog post and the TIL mirror directly and parsed the text by
  hand for verbatim quotes, rather than relying on WebFetch's summarized
  output.
- The source issue's three separate Prospector triage comments disagree
  with each other on novelty ("high" / "low" / "high") and relevant chapter
  (Ch04 / Ch05, under differing descriptions of what those chapters cover);
  none of the chapter numbers cited in those comments match this repo's
  actual chapter set (`00-principles` through `06-security-threat-model`).
  This note's Guide Impact section maps to the guide's actual current
  chapters instead of the triage comments' chapter references.
