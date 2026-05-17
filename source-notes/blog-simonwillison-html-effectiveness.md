---
source_url: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/
source_type: blog-post
title: "Using Claude Code: The Unreasonable Effectiveness of HTML"
author: Simon Willison (linking Thariq Shihipar / Claude Code team at Anthropic)
date_published: 2026-05-08
date_extracted: 2026-05-17
last_checked: 2026-05-17
status: current
confidence_overall: emerging
issue: "#784"
---

# Using Claude Code: The Unreasonable Effectiveness of HTML

> Simon Willison amplifies Thariq Shihipar's (Claude Code team, Anthropic) argument that
> requesting HTML output from Claude — rather than defaulting to Markdown — unlocks SVG
> diagrams, interactive widgets, in-page navigation, and other rich presentation capabilities;
> substantiated with a PR-review prompt template and a live copy.fail exploit-explanation
> demo, plus a 20-example companion catalogue.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, May 8, 2026; a short framing post that
  introduces and endorses Thariq Shihipar's companion page at
  https://thariqs.github.io/html-effectiveness/ and adds Willison's own live demonstration
  using his `llm` CLI. Both pages were fetched and read for this extraction.)
- **Author credibility**: Simon Willison is the creator of Django, one of the highest-signal
  independent LLM-tooling commentators, and the author of the `llm` CLI. He has no Anthropic
  affiliation. His endorsement of Shihipar's argument is practitioner validation, not vendor
  advocacy. Thariq Shihipar is named as being "on the Claude Code team at Anthropic" —
  giving the underlying pattern first-party authority about what Claude itself is capable of
  producing. The combination of an Anthropic team member's claimed best practice and an
  independent practitioner's corroborating live demonstration raises the signal quality above
  typical blog advocacy.
- **Scope**: Covers the specific prompting technique of requesting HTML (rather than
  Markdown) from Claude for explanation and analysis tasks; the historical Markdown
  efficiency argument and why it now applies less; two concrete prompt examples (PR review
  and code explanation); and a 20-example catalogue of HTML use cases across 9 categories.
  Does NOT cover: quantified comparisons of HTML vs. Markdown output quality, token cost
  analysis of HTML vs. Markdown prompting, model-specific behaviour differences, or failure
  modes where HTML output degrades.

## Extracted Claims

### Claim 1: Requesting HTML output from Claude enables richer presentation than Markdown — specifically SVG diagrams, interactive widgets, and in-page navigation

- **Evidence**: Willison's own assertion in the framing post, stated as the consequence of
  adopting Shihipar's technique. Not measured — presented as an inherent capability.
- **Confidence**: emerging (practitioner claim from a high-credibility source; independently
  corroborated by the 20-example companion catalogue; mechanism is transparent and verifiable)
- **Quote**: "Asking Claude for an explanation in HTML means it can drop in SVG diagrams,
  interactive widgets, in-page navigation and all sorts of other neat ways of making the
  information more pleasant to navigate."
- **Our assessment**: The claim is structurally sound — HTML/CSS/JS does enable these
  capabilities where Markdown cannot. The implicit mechanism is that by specifying HTML
  as the output format and naming specific capabilities (SVG, interactivity, navigation)
  in the prompt, practitioners unlock Claude's ability to use those capabilities, rather
  than constraining it to flat text. The catalogue at thariqs.github.io/html-effectiveness/
  provides 20 independent examples that instantiate the claim across diverse use cases.
  The guide should present this not as "HTML is better than Markdown" (absolute) but as
  "HTML unlocks capabilities Markdown cannot express" (contextual).

### Claim 2: The historical token-efficiency argument for Markdown no longer applies at today's context window sizes

- **Evidence**: Willison's direct contextual argument. He names the GPT-4 era (8,192 token
  limit) as the origin of the Markdown-first convention and implies that modern context
  windows have made the efficiency gap irrelevant.
- **Confidence**: anecdotal (one practitioner's reasoning; the historical claim about GPT-4
  is accurate, but the implication that token efficiency is now irrelevant is not quantified)
- **Quote**: "when the 8,192 token limit meant that Markdown's token-efficiency over HTML
  was extremely worthwhile."
- **Our assessment**: The underlying historical fact is correct: Markdown emerged partly
  as a token-efficient alternative to HTML during the era of tight context windows. At
  current context window sizes (100k+ tokens), the marginal token cost of HTML tags is
  unlikely to be the binding constraint for most tasks. However, the claim is made without
  measurement — Willison does not quantify the current HTML vs. Markdown token delta or
  argue it is below any specific threshold. The guide should present this as a directional
  argument for revisiting the Markdown default, not as a proven efficiency claim.

### Claim 3: Thariq Shihipar's HTML-first advocacy represents an internal Claude Code team position, not just individual preference

- **Evidence**: Willison's direct identification of Shihipar as "on the Claude Code team
  at Anthropic." The companion page (thariqs.github.io/html-effectiveness/) was authored
  by Shihipar and presents 20 curated examples.
- **Confidence**: emerging (one named team member; Willison vouches for the affiliation
  but the position is not a formal Anthropic engineering blog post)
- **Quote**: "Thought-provoking piece by Thariq Shihipar (on the Claude Code team at
  Anthropic) advocating for HTML over Markdown as an output format to request from Claude."
- **Our assessment**: The affiliation matters because it gives the pattern a degree of
  first-party credibility — the argument comes from someone who works on the tool and
  presumably knows what Claude can produce. However, this is still one team member's
  advocacy, not an official Anthropic recommendation. Willison's own adoption ("has caused
  me to reconsider that, especially for output") is the practitioner corroboration that
  lifts the signal quality.

### Claim 4: Willison has reconsidered his default of using Markdown for output after reading Shihipar's piece

- **Evidence**: First-person self-report from Willison in the post.
- **Confidence**: anecdotal (single practitioner decision; but from a high-credibility
  commentator who writes explicitly about his own practice)
- **Quote**: "Thariq's piece here has caused me to reconsider that, especially for output."
- **Our assessment**: The significance here is not that Willison changed his mind — it is
  that the Markdown-first convention he held was habitual rather than the result of
  deliberate evaluation. The convention formed in the GPT-4 era and persisted through
  inertia. This is a pattern the guide should name: many prompting conventions from earlier
  AI tool generations persist not because they are optimal but because they formed early and
  were not revisited.

### Claim 5: The PR-review HTML prompt — requesting inline margin annotations, severity color-coding, and diff rendering — is a concrete, reusable template from the Claude Code team

- **Evidence**: The prompt is attributed to Thariq Shihipar's companion page; Willison
  reproduces it as an example of effective HTML prompting.
- **Confidence**: emerging (single example; sourced from a Claude Code team member)
- **Quote**: "Help me review this PR by creating an HTML artifact that describes it. I'm
  not very familiar with the streaming/backpressure logic so focus on that. Render the
  actual diff with inline margin annotations, color-code findings by severity and whatever
  else might be needed to convey the concept well."
- **Our assessment**: This prompt has three extractable structural elements: (1) it names
  the output format explicitly ("HTML artifact"), (2) it scopes the focus to a specific
  technical concern ("streaming/backpressure logic"), and (3) it specifies the visual
  treatment ("inline margin annotations, color-code findings by severity") rather than
  leaving it to Claude's default. The result is a richer diff representation than GitHub's
  flat hunk display. The structural pattern — name the format, scope the focus, specify
  visual treatment — is generalizable beyond PR review.

### Claim 6: HTML output enables spatial and interactive representations of inherently spatial information (diffs, call-graphs, timelines) that Markdown cannot capture

- **Evidence**: Multiple assertions from the companion page (thariqs.github.io/html-effectiveness/),
  presented as the organizing rationale for the 20-example catalogue.
- **Confidence**: emerging (analytical claim from the companion page; mechanism is
  transparent but not quantified)
- **Quote**: "Diffs and call-graphs are spatial information; markdown flattens them."
- **Our assessment**: This is the strongest conceptual argument in the companion page —
  not that HTML looks better, but that some information structures are inherently spatial
  and Markdown's linear rendering discards that structure. A diff with inline margin notes
  (Claim 5's PR review prompt) is a spatial document; a Markdown table of file changes is
  a flattened version. The claim generalizes to any information that has spatial structure:
  call-graphs, dependency trees, timelines, flowcharts. The guide should use this as the
  principled basis for recommending HTML: use HTML when the information has spatial or
  interactive structure; Markdown when it does not.

### Claim 7: Motion and interactivity cannot be described in text — only experienced through the artifact itself

- **Evidence**: Assertion from the companion page, used to motivate the prototyping and
  animation categories in the catalogue.
- **Confidence**: anecdotal (a conceptual claim; the argument is directionally correct
  but presented without evidence)
- **Quote**: "Motion and interaction can't be described, only felt. A throwaway page with
  the real easing curve or the real click-through tells you in five seconds what a paragraph
  of prose never could."
- **Our assessment**: The five-seconds claim is illustrative rather than measured, but the
  underlying argument is sound: text descriptions of UI transitions, animation easing, and
  interaction flows are lossy representations of what can instead be demonstrated live.
  The "throwaway page" framing is important — the cost of producing an interactive HTML
  prototype is low enough for Claude to generate one disposably, where producing the same
  artifact manually would require substantial design effort. This reframes HTML output not
  as a formatting improvement but as a prototyping acceleration tool.

### Claim 8: The collapsible/navigable structure of an HTML explainer produces a qualitatively different reading experience from the same content dumped linearly

- **Evidence**: Assertion from the companion page, used to motivate the Research & Learning
  and Reports categories.
- **Confidence**: anecdotal (qualitative claim; mechanism is transparent)
- **Quote**: "An explainer with collapsible sections, tabbed code samples and a glossary in
  the margin reads very differently from the same words dumped linearly."
- **Our assessment**: The claim is about *document architecture*, not just styling. Collapsible
  sections, tabs, and margin glossaries are navigation affordances that allow readers to
  jump to what they need rather than scanning linearly. For the typical use case of "explain
  this codebase feature to me," the linear Markdown version requires the reader to hold the
  entire explanation in working memory; the navigable HTML version externalizes structure
  into the document itself. This maps directly to the information-bandwidth framing in
  `blog-cursor-canvas.md` Claim 8 ("We want to remove friction in human-agent collaboration
  and make it easier to express your intent beyond plain text").

### Claim 9: Recurring report formats (status updates, post-mortems) benefit most from HTML structure and color

- **Evidence**: Assertion from the companion page, motivating the Reports category.
- **Confidence**: anecdotal (design opinion; directionally consistent with general technical
  communication practice)
- **Quote**: "Recurring documents — status updates, post-mortems — benefit most from a bit
  of structure and color. A small chart and a colored timeline turn something people skim
  into something they actually read."
- **Our assessment**: The "people actually read" outcome is the guide-relevant claim. If
  status updates and post-mortems are structurally important communication artifacts but
  consistently skimmed in Markdown form, HTML formatting that increases reading rate has
  a measurable team-communication benefit. The "recurring documents" qualifier is important:
  documents generated repeatedly with a predictable structure are the best candidates for
  HTML formatting because the structure template can be reused. This suggests a specific
  prompting pattern: for recurring reports, maintain an HTML template prompt alongside the
  content prompt.

### Claim 10: Willison used a real Linux exploit (copy.fail) as a demonstration case, and the resulting HTML explanation was "pretty good"

- **Evidence**: First-person live demonstration by Willison in the framing post. The
  copy.fail exploit is described as "a recently discovered Linux security exploit, including
  a proof of concept distributed as obfuscated Python." The resulting HTML output is linked
  at https://gisthost.github.io/?ae53e3461ffdbfd0826156aacf025c7e.
- **Confidence**: anecdotal (one practitioner test; "pretty good" is not a quality benchmark)
- **Quote**: (no single direct quote that captures both the test and the "pretty good" result
  together; see Our assessment)
- **Our assessment**: The demo structure is extractable as a prompting pattern: pipe code
  directly to an LLM with an HTML output system prompt, and receive a self-contained
  interactive explanation. The result Willison describes is "dark-themed technical
  documentation" — an HTML document with formatting, sections, and safety notes. "Pretty
  good" is a deliberately modest assessment; the implicit point is that the HTML format
  enabled a richer explanation than a plain-text response would have. The guide should
  present the demo as a pattern, not a quality claim.

### Claim 11: Exploration tasks — "fan out across several directions and lay them next to each other" — are a primary use case where HTML outperforms sequential Markdown walls of text

- **Evidence**: Opening framing statement from the companion page's introduction.
- **Confidence**: emerging (analytical claim; the mechanism — side-by-side comparison
  is easier to evaluate than sequential reading — is well-supported in cognition research
  but not cited here)
- **Quote**: "When you're not sure what you want yet. Ask the agent to fan out across
  several directions and lay them next to each other so you can point at one — instead
  of reading three sequential walls of text and trying to hold them all in your head."
- **Our assessment**: This is the strongest practical argument for HTML in the exploration
  and planning phase of development. Comparing three architecture approaches side by side
  in a single HTML document (with a shared layout, consistent headings, aligned trade-off
  tables) is cognitively easier than reading three sequential Markdown responses and
  maintaining a mental comparison table. The "point at one" framing captures the output:
  the HTML comparison produces a decision input, not just information. This use case is
  directly actionable: practitioners choosing between architectural options or implementation
  approaches should request HTML comparison documents rather than sequential evaluations.

### Claim 12: Willison plans to "start experimenting more with rich HTML explanations in response to ad-hoc prompts"

- **Evidence**: Willison's closing statement in the framing post.
- **Confidence**: anecdotal (forward-looking self-report)
- **Quote**: "I'm excited to start experimenting more with rich HTML explanations in
  response to ad-hoc prompts."
- **Our assessment**: The significance is not the plan itself but the signal it represents:
  a practitioner who defaulted to Markdown for all output is shifting his default. "Ad-hoc
  prompts" is the key scope — this is not about generating final deliverables in HTML, but
  about using HTML for day-to-day analysis and explanation tasks. The guide should present
  this as the adoption pattern: start using HTML for ad-hoc explanations and analysis,
  not as a wholesale replacement of Markdown for documentation.

## Concrete Artifacts

### The PR-Review HTML Prompt (from Thariq Shihipar, Claude Code team)

```
Source: Thariq Shihipar / thariqs.github.io/html-effectiveness/
Via: Simon Willison, simonwillison.net, May 8, 2026

"Help me review this PR by creating an HTML artifact that describes it. I'm not very
familiar with the streaming/backpressure logic so focus on that. Render the actual diff
with inline margin annotations, color-code findings by severity and whatever else might
be needed to convey the concept well."

Structural elements:
  - Names output format explicitly: "HTML artifact"
  - Scopes technical focus: "streaming/backpressure logic"
  - Specifies visual treatment: "inline margin annotations, color-code findings by severity"
```

### The copy.fail Code Explanation LLM Command (Willison's live demo)

```
Source: Simon Willison, simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/

curl https://copy.fail/exp | llm -m gpt-5.5 -s 'Explain this code in detail. Reformat it,
expand out any confusing bits and go deep into what it does and how it works. Output HTML,
neatly styled and using capabilities of HTML and CSS and JavaScript to make the explanation
rich and interactive and as clear as possible'

Context: copy.fail is a Linux security exploit (privilege-escalation PoC, obfuscated Python).
The resulting HTML page is at: https://gisthost.github.io/?ae53e3461ffdbfd0826156aacf025c7e

System prompt pattern elements:
  - Explanation task: "Explain this code in detail. Reformat it, expand out any confusing bits"
  - Depth instruction: "go deep into what it does and how it works"
  - Output format: "Output HTML, neatly styled"
  - Capability descriptors: "using capabilities of HTML and CSS and JavaScript"
  - Quality targets: "make the explanation rich and interactive and as clear as possible"
```

### Nine-Category HTML Use Case Catalogue (Thariq Shihipar, thariqs.github.io/html-effectiveness/)

```
Source: Thariq Shihipar, thariqs.github.io/html-effectiveness/ (companion page)
Via: Simon Willison, May 8, 2026

20 examples across 9 categories:

1. Exploration & Planning (3 examples)
   - Three code approaches: side-by-side comparison with inline trade-offs
   - Visual design directions: layout and palette options rendered live
   - Implementation plan: milestones, data-flow diagram, inline mockups, risk table

2. Code Review & Understanding (3 examples)
   - Annotated pull request: diff with margin notes, severity tags, jump links
   - PR writeup for reviewers: motivation, before/after, file-by-file tour with the why
   - Module map: package as boxes and arrows, hot path highlighted, entry points listed

3. Design (2 examples)
   - Living design system: colors, type scale, spacing tokens as swatches
   - Component variants: every size/state/intent on one sheet

4. Prototyping (2 examples)
   - Animation sandbox: transition in isolation with duration/easing sliders
   - Clickable flow: four screens linked together for interaction review

5. Illustrations & Diagrams (2 examples)
   - SVG figure sheet: blog-post diagrams inline for tweaking and copy-out
   - Annotated flowchart: deploy pipeline as real flowchart — click step to see timings,
     failure paths

6. Decks (1 example)
   - Arrow-key slide deck: presentation as one HTML file, no build step

7. Research & Learning (2 examples)
   - How a feature works: prompt "Explain rate limiting in this repo" → TL;DR box,
     collapsible request-path steps, FAQ
   - Concept explainer: consistent hashing with live ring, comparison table,
     hover-linked glossary

8. Reports (2 examples)
   - Weekly status: what shipped, what slipped, small chart
   - Incident timeline: post-mortem with minute-by-minute timeline, log excerpts,
     follow-up checklist

9. Custom Editing Interfaces (3 examples)
   - Ticket triage board: drag across Now/Next/Later/Cut, copy result as markdown
   - Feature flag editor: toggles grouped by area, dependency warnings
   - Prompt tuner: editable template with variable slots; three sample inputs
     re-render live
```

### Key Framing Statements from the Companion Page (verbatim)

```
Source: Thariq Shihipar, thariqs.github.io/html-effectiveness/

Opening:
"Twenty self-contained `.html` files an agent produced instead of a wall of markdown.
Each one trades a document you'd skim for one you'd actually read."

On spatial information:
"Diffs and call-graphs are spatial information; markdown flattens them."

On motion and interaction:
"Motion and interaction can't be described, only felt. A throwaway page with the real
easing curve or the real click-through tells you in five seconds what a paragraph of
prose never could."

On document architecture:
"An explainer with collapsible sections, tabbed code samples and a glossary in the
margin reads very differently from the same words dumped linearly."

On recurring documents:
"Recurring documents — status updates, post-mortems — benefit most from a bit of
structure and color. A small chart and a colored timeline turn something people skim
into something they actually read."

On exploration:
"When you're not sure what you want yet. Ask the agent to fan out across several
directions and lay them next to each other so you can point at one — instead of reading
three sequential walls of text and trying to hold them all in your head."
```

## Cross-References

- **Corroborates**: `blog-cursor-canvas.md` Claim 4 ("Before canvases, the agent would
  represent time-series data in a markdown table, which was hard to interpret and required
  additional steps to visualize") — Both this source and the Canvas note diagnose the same
  root problem: Markdown is an insufficient output medium for spatial, temporal, or
  interactive information. Cursor's solution is a React-based component library (canvases);
  this source's solution is open HTML/CSS/JS output. The two approaches solve the same
  "information bandwidth" problem via different mechanisms. The guide should present both
  as implementations of the same underlying principle: structured rich output reduces
  cognitive load vs. flat Markdown.

- **Corroborates**: `blog-cursor-canvas.md` Claim 5 ("Traditional tools present all changes
  equally, requiring us to figure out what parts of the diff are most important. With canvases,
  Cursor can logically group changes together, prioritize what's most important for you to
  review") — This source's PR-review HTML prompt (Claim 5 and the Concrete Artifacts section)
  is the Claude Code equivalent of Cursor's canvas-based PR review. Both patterns use rich
  output to solve the same diff-prioritization problem: rather than presenting all changes
  equally, the agent produces a structured review artifact (HTML with severity color-coding
  vs. React canvas with logical grouping). Convergent independent implementations of the
  same pattern.

- **Corroborates**: `blog-cursor-canvas.md` Claim 8 ("We want to remove friction in human-agent
  collaboration and make it easier to express your intent beyond plain text") — Cursor frames
  the canvas feature as part of an "information bandwidth" initiative. This source names the
  same need from the user side: Markdown is a low-bandwidth agent output channel; HTML enables
  higher-bandwidth presentation. Both sources agree on the diagnosis (Markdown insufficient)
  and the direction (richer structured output); they differ on the mechanism (vendor component
  library vs. open HTML authoring by the model).

- **Extends**: `blog-cursor-canvas.md` — The Canvas note documents Cursor's first-party
  implementation of rich agent output, constrained to pre-built React components. This source
  documents the open-ended version: instructing Claude to produce arbitrary HTML/CSS/JS within
  any context, without requiring a Cursor-specific environment. Together they frame a spectrum:
  from opinionated first-party canvases (predictable, safe, limited) to open HTML output
  (flexible, powerful, less constrained). The guide should describe both ends of this spectrum.

- **Contradicts**: None identified. No existing corpus source argues that Markdown is the
  correct default for Claude output in all cases, or that HTML output is inferior. The
  Markdown-default convention exists by inertia (Claim 2 and 4 above) rather than by explicit
  argument in any corpus source.

- **Novel**:
  - **HTML-as-output as a named prompting strategy with explicit capability descriptors**:
    No prior corpus source names requesting HTML output — with specific descriptors like "SVG
    diagrams, interactive widgets, in-page navigation" — as a deliberate prompting technique.
    The technique is distinct from "use a rich output format"; it is a specific pattern of
    naming HTML capabilities in the prompt to unlock them.
  - **The "spatial information" argument for HTML over Markdown**: The claim that diffs,
    call-graphs, and timelines are inherently spatial and Markdown flattens them is a
    principled design argument not found in any other corpus source.
  - **The "fan out for comparison" HTML pattern**: Using HTML to present side-by-side option
    comparisons rather than sequential text responses is a specific exploration technique not
    documented elsewhere in the corpus.
  - **LLM CLI pipe pattern for code explanation**: `curl <code-url> | llm -s '<HTML-output-
    system-prompt>'` as a code explanation workflow is a concrete, reusable pattern not
    documented in any prior corpus source.
  - **Nine-category HTML use case taxonomy**: The companion page's 20-example, 9-category
    catalogue is the most comprehensive published typology of HTML output use cases for
    Claude. No prior corpus source organizes HTML use cases at this level of specificity.

## Guide Impact

- **Chapter 03 (Prompting Patterns) — HTML Output as a Named Technique**: Add "Request
  HTML output with capability descriptors" as a named prompting pattern. Structure: (1) name
  the output format explicitly in the prompt, (2) list specific HTML capabilities to activate
  (SVG diagrams, interactive widgets, collapsible sections, etc.), (3) state the quality goal
  (rich, interactive, as clear as possible). The PR-review prompt (Concrete Artifacts) is the
  canonical example. The guide should also note when NOT to use HTML: simple Q&A, short
  code snippets, or any context where the output will be consumed programmatically rather
  than read by a human.

- **Chapter 04 (Tool Use & Output Optimization) — HTML vs. Markdown Decision Framework**:
  Add a decision rubric based on information type: use HTML when the content has spatial
  structure (diffs, call-graphs, timelines), interactive requirements (prototypes, animation
  review), recurring format (status reports, post-mortems), or comparative structure (option
  evaluation, A/B design review). Use Markdown when the content is linear prose, short
  explanations, or will be processed programmatically. The "diffs and call-graphs are spatial
  information; markdown flattens them" framing (Claim 6) is the anchor quote for this section.

- **Chapter 03 (Prompting Patterns) — Exploration Pattern**: Add the "fan-out for comparison"
  HTML pattern explicitly (Claim 11). When evaluating architectural options or implementation
  approaches, instruct Claude to produce a single HTML document with side-by-side comparisons
  rather than sequential responses. This is a concrete workflow change: instead of asking
  "What are three ways to approach X?" (three sequential Markdown blocks), ask "Create an
  HTML comparison of three approaches to X, with trade-offs called out inline."

- **Chapter 01 (Daily Workflows) — Historical Markdown Default**: Acknowledge that the
  Markdown-first convention for Claude prompting formed in the GPT-4 era when token efficiency
  mattered more. At current context window sizes, practitioners should actively evaluate
  whether HTML output better serves the task. The guide should frame this as "revisit your
  defaults," not "always use HTML."

## Extraction Notes

- Simon Willison's post is short (a few paragraphs of framing + two examples). The
  substantive content comes from the companion page at thariqs.github.io/html-effectiveness/,
  which was fetched and read separately. Both pages were read for this extraction.
- The copy.fail result page at https://gisthost.github.io/?ae53e3461ffdbfd0826156aacf025c7e
  was fetched but returned an empty preview frame (the file hosting service requires
  a specific file path query parameter that was not resolvable via WebFetch). The description
  of the result as "dark-themed technical documentation" is drawn from Willison's description
  in the post, not direct inspection of the HTML file.
- The verbatim quotes in this note were verified against the source via multiple targeted
  WebFetch requests against simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/.
  The companion page quotes were similarly verified against thariqs.github.io/html-effectiveness/.
- The PR-review prompt (Concrete Artifacts) was confirmed verbatim across two separate fetch
  requests. The copy.fail LLM command was confirmed verbatim in a separate fetch.
- Cross-reference claim numbers for `blog-cursor-canvas.md` were verified by reading that
  note in document order: Claim 4 (line 51 in that note — "Before canvases, the agent would
  represent time-series data in a markdown table..."), Claim 5 (line 54 — "Traditional tools
  present all changes equally..."), Claim 8 (line 76 — "We want to remove friction in
  human-agent collaboration..."). All three verified.
- Confidence is set to `emerging` rather than `settled` because: the technique is advocated
  by a Claude Code team member and corroborated by a high-credibility independent practitioner,
  but there is no controlled comparison of HTML vs. Markdown output quality, no user study,
  and no quantified evidence that HTML prompting produces better outcomes. The evidence is
  practitioner advocacy + live demonstration + a catalogue of examples.
