---
source_url: https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them
source_type: blog-post
title: "How the product designer who built Claude Design uses it to explore ideas before building them"
author: Nate Parrott (Anthropic, product designer)
date_published: 2026-07-24
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: anecdotal
issue: "#2217"
---

# How the product designer who built Claude Design uses it to explore ideas before building them

> First-person account from the Anthropic product designer who built Claude Design (in beta), describing how prompting Claude to generate HTML — rather than a dedicated image model — turned into a general-purpose visual ideation medium for prototypes, decks, animations, and design-system generation, with nine concrete best practices for prompting it.

## Source Context

- **Type**: blog-post (official Anthropic claude.com blog, "Enterprise AI" / "Product" category, published July 24, 2026, ~5 min read)
- **Author credibility**: Nate Parrott, the product designer at Anthropic who built Claude Design and was, per the post, "the only product designer on Claude Code for VS Code" during its fall 2025 beta. First-person account of his own tool's origin and his own daily practice with it — maximal insider authority on intent and design rationale, but zero independent verification and an obvious incentive to present the tool favorably. The post explicitly frames itself as "his opinions, usage patterns, and advice."
- **Scope**: Covers the origin story of Claude Design (HTML as the underlying medium), what it is and isn't for (vs. Claude Code, vs. image-generation/logo tools), the round-trip relationship with Claude Code, four examples from the author's own work, and nine numbered best practices for prompting it. Does NOT cover: pricing, team-wide adoption data or usage metrics, engineer (non-designer) usage patterns, technical implementation of the design-system generation feature, or any critique/failure mode beyond the explicit "not for logo design" caveat.

## Extracted Claims

### Claim 1: Claude is unusually capable at generating HTML, and HTML itself is a general-purpose visual medium, not just a website format

- **Evidence**: Origin-story claim explaining why Claude Design is HTML-based rather than built on an image-generation model.
- **Confidence**: anecdotal (single practitioner's design rationale for his own product)
- **Quote**: "Eventually I stumbled onto the answer: Claude is really good with HTML. We think of HTML as the format for websites, but it's also a rich, interactive visual medium: anything you can make in a slide deck, a video file, or a PDF, you can make in a web page."
- **Our assessment**: This is the load-bearing design decision behind the whole tool. Treating HTML as a general visual substrate (not "the thing websites are made of") is what lets one prompting surface produce prototypes, slide decks, PDFs-via-print, emails, and animations. It reframes "Claude is good at code" as "Claude is good at a code format that happens to render as arbitrary visuals" — a reusable insight for any team deciding whether to reach for an image model or a code-generation model for visual output.

### Claim 2: Feeding brand guidelines (fonts, colors, assets, principles) into the prompt layer made output compliant with brand without per-designer manual enforcement

- **Evidence**: Author describes distilling Anthropic's brand guide into prompts as the step that made the internal prototype useful to other product designers.
- **Confidence**: anecdotal
- **Quote**: "product design is driven by applying knowledge of the product and brand you work on, so as a next step I spent a while distilling the essence of Anthropic's brand (the fonts, colors, assets, and principles our products use) into prompts. This way, when I type my prompt into the tool, the output is compliant with the Anthropic brand guide."
- **Our assessment**: This is a concrete instance of the general "encode standing constraints in the prompt/context layer rather than relying on the model's defaults" pattern that recurs across the corpus for code style and architecture. Here it's applied to visual brand identity instead of code conventions — the same context-engineering principle, different artifact type.

### Claim 3: Every Claude Design artifact produces a shareable link, eliminating the traditional cost of building click-through prototypes by hand

- **Evidence**: Direct comparison to traditional design-tool prototyping workflow.
- **Confidence**: anecdotal
- **Quote**: "Making a click-through prototype in traditional design tools means mocking up every state of every screen and wiring them together by hand. Here, you hand Claude your assets and say: make it work. Every artifact it delivers has a link you can share the way you'd share a doc."
- **Our assessment**: The comparison is specific and plausible (manual state-wiring is a well-known pain point in tools like Figma), and the "share like a doc" framing lowers the distribution cost of a prototype to the same as sharing a text document. No metrics are given on time saved, so this remains a qualitative, unverified comparison.

### Claim 4: An internal team offsite pitch session, where attendees built slides in Claude Design mid-meeting, was the inflection point that got the tool formally staffed

- **Evidence**: Specific anecdote about organizational adoption dynamics.
- **Confidence**: anecdotal
- **Quote**: "I first realized how compelling Claude Design was at an idea pitch session during an Anthropic Labs team offsite: every person there threw together slides using it, often in the middle of the meeting before their turn to present. That session convinced the Labs team to staff it, and Claude Design went from a side project to a real project."
- **Our assessment**: This is an internal-adoption story, not a usage-pattern claim, but it's evidence of a low-friction threshold effect: when a tool is fast enough that people reach for it live, in a meeting, under time pressure, that's a strong bottom-up adoption signal distinct from top-down mandated rollout. Worth noting as a pattern for how AI-native tools spread inside organizations.

### Claim 5: Claude Design is explicitly scoped to ideation, communication, and pre-commitment exploration — not production software, and not image/logo generation

- **Evidence**: Explicit scope statement contrasting Claude Design with Claude Code and with image-generation tools.
- **Confidence**: settled (first-party, explicit product positioning statement from the tool's own designer)
- **Quote**: "Claude Code is for coding; Claude Design is for the other parts of the design work: early ideation, collaboration, or getting buy-in on a direction before anyone commits to building it."
- **Our assessment**: This is a hard scope boundary from the person who built the tool, so we treat it as settled/authoritative for what the tool is designed to do (as opposed to anecdotal for how well it works). It matters for the guide because it draws an explicit line: Claude Design for pre-commitment visual exploration, Claude Code for anything that ships. The post separately states the tool "doesn't have an image model and isn't built for image generation, so it's a poor fit for logo design" — a second, adjacent scope exclusion (not included verbatim above since it is a non-adjacent sentence in the source) that reinforces the same point: Claude Design fills a specific ideation niche, not general-purpose image generation or production coding.

### Claim 6: Claude Design and Claude Code round-trip — a prototype can move from one to the other in either direction

- **Evidence**: Direct statement of the interop mechanism.
- **Confidence**: settled (first-party product capability statement)
- **Quote**: "The two work together round-trip, so you can sync a prototype you started in Claude Code to Claude Design for iteration and editing on the canvas, or hand off a prototype you're ready to build from Claude Design to Claude Code."
- **Our assessment**: This is the concrete mechanism that operationalizes the ideation/production split in Claim 5 — without round-tripping, the "explore in Design, build in Code" workflow would require manual re-implementation at the handoff point. The claim is a capability statement (round-trip sync exists) rather than a usage report of how well it works in practice; the post gives no example of actually exercising this handoff.

### Claim 7: The Claude Design intro animation was made by first having Claude build a bespoke video editor, then using that editor to make the animation

- **Evidence**: Concrete first-person example from the author's own work.
- **Confidence**: anecdotal
- **Quote**: "The animation that plays when you sign up for Claude Design was made in the tool itself, but not directly: I'm not an animator, so I first had Claude Design build me a bespoke video editor, then used that editor to make the animation."
- **Our assessment**: This is a distinctive two-hop workflow pattern: instead of prompting Claude directly for a finished artifact it may be weak at (animation, as a non-animator's task), the author had it build a purpose-specific tool first, then used that tool. This "build the instrument, then play it" pattern is a reusable meta-strategy that goes beyond simple one-shot prompting and is worth extracting as a named technique.

### Claim 8: The recommended workflow is "ask for ten options, then remix" — most generated options are discarded and the value comes from combining fragments of the survivors

- **Evidence**: One of nine explicit best-practice recommendations, given as a numbered practice with a sample follow-up prompt.
- **Confidence**: anecdotal (practitioner's own workflow advice)
- **Quote**: "Ask for ten options, then remix. Most of them won't be good, and that's fine; one or two will be. Then say, \"I like option B and a little of option D. Give me five riffs that smoosh those together.\""
- **Our assessment**: This generate-wide-then-recombine pattern mirrors best-of-N / divergent-then-convergent sampling strategies seen elsewhere in the corpus for code generation, applied here to visual design options. The explicit acceptance that "most of them won't be good" is a useful expectation-setting note: the value of the practice is in the breadth of the option set, not in each individual generation being high quality.

### Claim 9: Direct manual editing (not re-prompting) is recommended for final-touch adjustments because it costs no tokens and is more precisely controllable by eye

- **Evidence**: Explicit best-practice recommendation contrasting prompted edits with direct manipulation tools.
- **Confidence**: anecdotal
- **Quote**: "Make the last mile manual. Use the direct editing tools (rearrange, delete, edit text, resize, change colors) for final touches instead of prompting for them. Direct edits use no tokens, and small calls like sizing and alignment are better eyeballed anyway."
- **Our assessment**: This is a token-economy and precision argument for a hybrid prompt+direct-manipulation interface, not a "prompt for everything" philosophy. It's a concrete, actionable rule of thumb: use natural language for structural/conceptual changes and direct manipulation for fine positioning — directly analogous to the "know when to hand-edit vs. re-prompt" guidance that recurs in the corpus for code, here applied to visual layout.

### Claim 10: Connecting GitHub lets Claude Design fetch a team's real components and existing screens, reproducing existing designs with "pretty high fidelity" as a starting point

- **Evidence**: Best-practice recommendation describing a specific data-connection capability.
- **Confidence**: anecdotal (practitioner claim, no fidelity metric given beyond "pretty high")
- **Quote**: "Give Claude your real context. If you're designing a feature for an existing app or website, connect GitHub: Claude will fetch your components and existing screens and use them as a starting point, and with a few tries it can recreate your existing designs with pretty high fidelity."
- **Our assessment**: This grounds Claude Design output in a team's actual component library rather than Claude's generic aesthetic defaults (which Claim 11 explicitly warns against). "With a few tries" is an important qualifier — the claim is not first-shot fidelity, it's fidelity reached through iteration. No quantification of "pretty high" is offered.

### Claim 11: Left unguided, Claude defaults to a small set of recognizable "favorite aesthetics," so specifying fonts/colors/moodboards is necessary to avoid generic output

- **Evidence**: Explicit best-practice warning about unguided model output.
- **Confidence**: anecdotal
- **Quote**: "Tell Claude what it should look like. Left undirected, Claude picks one of its favorite aesthetics. You'd probably recognize them. Head that off by specifying fonts and colors, or providing a moodboard of images for inspiration, or asking Claude to brainstorm font-and-color pairings and going back and forth until a pairing feels right."
- **Our assessment**: This is a specific, named failure mode ("favorite aesthetics" that are recognizable across generations) rather than a vague "quality varies" caveat. It's consistent with a broader, model-agnostic pattern where generative visual/text output regresses to a small number of stylistic defaults absent explicit steering — useful as a concrete example when the guide discusses the need for explicit style/constraint context even in creative, non-code generation tasks.

### Claim 12: Uploading brand assets (logos, slide decks, screenshots, typography specs) lets Claude analyze them and generate a reusable design system that seeds subsequent artifacts

- **Evidence**: Explicit best-practice recommendation describing the design-system generation feature.
- **Confidence**: anecdotal
- **Quote**: "Turn recurring work into a design system. Upload your brand files and assets such as logos, slide decks, screenshots, typography specs, and anything else you reuse, and Claude will analyze them and generate a design system. This way, each artifact you make afterward starts from your choices, rather than a blank slate."
- **Our assessment**: This generalizes Claim 2 (the author manually distilling Anthropic's brand into prompts) into a first-class product feature: instead of a human distilling brand guidelines into prompt text once, Claude itself performs that distillation from raw source assets. This is a "bootstrap a persistent context artifact from raw materials, then reuse it" pattern — structurally similar to CLAUDE.md-style persistent context in coding agents, applied to visual brand identity.

## Concrete Artifacts

### Nine Best Practices for Prompting Claude Design

```
Best practices for using Claude Design
(Nate Parrott, Anthropic blog, July 24, 2026)
Source: https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them

1. Do the thinking before you prompt.
   Write/dictate the prompt before sitting down to design — via voice
   button, phone Notes app, or a walking voice memo transcribed later.

2. Tell Claude what it should look like.
   Specify fonts/colors or a moodboard, or have Claude brainstorm
   font-and-color pairings iteratively — otherwise it defaults to
   its own recognizable "favorite aesthetics."

3. Turn recurring work into a design system.
   Upload brand files (logos, decks, screenshots, typography specs);
   Claude analyzes them and generates a design system that seeds
   future artifacts instead of starting from a blank slate.

4. Ask for ten options, then remix.
   Most won't be good; combine fragments of the ones that are
   ("I like option B and a little of option D. Give me five riffs
   that smoosh those together.")

5. Sketch what you can't describe.
   Draw a layout on paper and upload a photo if you lack the words
   for it.

6. Point and talk.
   Enable device dictation, select "comment," click an element, and
   speak — words appear in the comment box as if typed.

7. Wireframe first when fidelity doesn't matter.
   Faster, and keeps Claude focused on structure over visuals for
   rapid idea iteration.

8. Make the last mile manual.
   Use direct editing tools (rearrange, delete, edit text, resize,
   change colors) for final touches — no tokens used, and small
   sizing/alignment calls are better eyeballed than prompted.

9. Give Claude your real context.
   Connect GitHub so Claude fetches real components/screens as a
   starting point (recreates existing designs with "pretty high
   fidelity" after a few tries); web search and MCP connections also
   work in Claude Design.

Bonus (process note, not numbered in source):
   Keep working alongside Claude — queue multiple messages, or keep
   talking while a prior turn is still running.
```

### Four First-Person Usage Examples

```
Nate Parrott's own Claude Design use cases
Source: https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them

1. Intro animation: had Claude Design build a bespoke video editor
   first, then used that editor to make the sign-up animation
   (author is "not an animator").

2. Subway-times app with adjustable animation controls for dialing
   in motion physics.

3. Instagram-style color controls: asked Claude to expose an app's
   color scheme as sliders and presets rather than describing colors
   in words.

4. Redesign of Claude Design itself, done inside the tool with two
   teammates (Helen and Andrew) as an ongoing exploration, not a
   committed ship plan.
```

## Cross-References

- **Corroborates** `blog-cursor-design-mode.md` (Claim 1, Claim 9): Cursor's Design Mode post argues text chat is a "category mismatch" for spatial UI work and frames the design goal as flow-state preservation across abstraction levels. This source makes a parallel but distinct argument at the medium level rather than the interaction-modality level: HTML-as-a-general-visual-medium (Claim 1 here) is what makes a single prompt-driven surface span prototypes, decks, and animations, whereas Cursor's post is about *how you point at* a running UI to edit it. Both sources independently converge on the idea that AI-native visual/design tools need something richer than plain text chat — Cursor solves it with spatial pointing input, Claude Design solves it (per this source) by using a maximally expressive rendering substrate (HTML) as both the medium and the editable artifact.
- **Extends** `blog-anthropic-claude-code-artifacts.md` (Claim 9, "DESIGNERS & FRONTEND" prompt pattern): The Claude Code artifacts note documents a designer-facing artifact prompt ("Give me an artifact with 5 UX variations of this signup form, built from our component library") as one of nine role-based Claude Code artifact patterns, grounded in a codebase's component library via Claude Code session context. This source describes the inverse-but-complementary tool: Claude Design is a dedicated, iteration-first surface for that same "many visual options, grounded in real components" workflow (Claim 10, Claim 8 here), with round-trip handoff back to Claude Code (Claim 6) once a direction is chosen. Read together, they suggest an emerging two-tool split: Claude Code artifacts for grounded-but-secondary visual output from an engineering session, Claude Design for primary, iteration-heavy visual ideation that later hands off into Claude Code.
- **Contradicts**: None found. No existing source note makes a claim about Claude Design or a comparable Anthropic-native visual design tool that this source disagrees with.
- **Novel**:
  - **HTML as a deliberately chosen general-purpose visual medium** (Claim 1) — no prior corpus source frames HTML generation this way (as a substitute for slide decks, PDFs, and video, not just web pages).
  - **Brand-guideline-to-prompt distillation as a design-context-engineering pattern** (Claim 2, Claim 12) — the corpus has "context engineering" claims for code (CLAUDE.md, skills) but this is the first source applying the same "persist standing constraints outside the model's defaults" pattern to visual brand identity.
  - **"Build the instrument, then play it" two-hop workflow** (Claim 7) — a non-animator having Claude build a custom video editor first, then using that editor, is a distinct meta-pattern not previously documented in the corpus: delegate tool-building as a first step when the end task is outside the practitioner's own skill.
  - **Claude Design/Claude Code round-trip as a named product capability** (Claim 6) — first corpus source describing bidirectional sync between a visual ideation tool and a coding agent as a first-class supported workflow.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: The chapter currently has no coverage of visual/design ideation workflows (confirmed by search — no matches for "design," "prototype," "visual," or "artifact" as workflow topics). Add a short subsection on AI-native visual ideation for teams that do product/UI work, anchored on Claim 5's explicit scope split (Claude Design for pre-commitment ideation, Claude Code for production) and the round-trip mechanism (Claim 6). Cite the nine best practices (Concrete Artifacts) as a starting checklist, especially "ask for ten options, then remix" (Claim 8) and "make the last mile manual" (Claim 9), since both generalize beyond this specific tool to any generate-then-refine visual workflow.
- **Chapter 04 (Context Engineering)**: Add Claim 2 / Claim 12 (brand-guideline distillation, design-system generation from uploaded assets) as a visual-domain instance of the guide's existing context-engineering principle: persist standing constraints (brand, style, components) outside the prompt so every subsequent generation inherits them, rather than re-specifying constraints per request. This is the same principle the guide likely already states for code style/CLAUDE.md, now with a second concrete domain example.
- **Chapter 02 (Harness Engineering)**: Note Claim 7 ("build the instrument, then play it") as a reusable meta-pattern worth naming explicitly: when a practitioner lacks the skill for a task (here, animation), one option is to have the agent build a purpose-built tool for that task first, then use the tool, rather than prompting for the end artifact directly in one shot.

## Extraction Notes

- Full article text was retrieved by fetching the raw page HTML directly (`curl` + tag-stripping), not via a summarizing tool, so all quotes above were copied verbatim from the extracted plain-text article body rather than paraphrased or reconstructed. The Assayer can verify by fetching the live URL and searching for each quoted string directly.
- The article is short (~5 min read, per its own byline) and consists of an origin narrative, a "what it's not for" section, four personal examples, and nine explicit numbered best practices. All nine best practices and all four examples were extracted; nothing substantive was left out.
- Three separate Prospector triage comments are attached to the issue and disagree with each other on relevant chapters (one says only Ch01; another says Ch02/Ch04/Ch06; a third says Ch01 "marginally" and questions scope fit). This note independently checked the actual guide chapter files rather than deferring to any one triage comment: the current guide has chapters 00 (principles), 01 (daily workflows), 02 (harness engineering), 03 (verification), 04 (context engineering), 05 (team adoption), 06 (security/threat model) — there is no dedicated "design system" chapter as one triage comment assumed. Guide Impact above is scoped to the chapters that actually exist and where this source's claims concretely apply (01, 04, 02), not to the union of all three triage comments' guesses.
- No contradiction with any existing source note was identified during cross-referencing; none filed.
- Confidence set to `anecdotal` overall: this is a single first-person practitioner account (the tool's own creator) describing his own workflow and product, with no independent corroboration, no usage metrics, and an inherent incentive to present the tool favorably. Two individual claims (Claim 5, scope positioning; Claim 6, round-trip capability) are marked `settled` within their own entries because they are explicit, unambiguous first-party product-capability/positioning statements rather than subjective workflow assessments — but the note's overall confidence reflects the anecdotal nature of the bulk of the content (personal workflow tips, examples, and internal anecdotes).
