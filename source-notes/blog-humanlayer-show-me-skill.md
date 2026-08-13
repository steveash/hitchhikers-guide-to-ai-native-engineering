---
source_url: https://www.humanlayer.dev/blog/show-me-skill
source_type: blog-post
title: "show-me: a coding agent skill for compact visual representations"
author: "Dex Horthy (HumanLayer)"
date_published: 2026-08-12
date_extracted: 2026-08-13
last_checked: 2026-08-13
status: current
confidence_overall: emerging
issue: "#2676"
---

# show-me: a coding agent skill for compact visual representations

> HumanLayer's Dex Horthy introduces "show-me," an installable Claude Code
> skill that prompts coding agents to communicate with compact visual
> representations — component trees, call stacks, Mermaid diagrams, file
> layouts, pseudocode, type signatures, diff syntax, and HTML mockups — instead
> of verbose prose, arguing that visual processing is cognitively cheaper than
> reading dense text and that agent output has grown more jargon-laden and less
> readable even as models have gotten more capable.

## Source Context

- **Type**: blog-post (practitioner tool announcement, first-party, < 7 min
  read, from an agentic coding-tools company)
- **Author credibility**: Dex Horthy, writing for HumanLayer. Per the corpus's
  existing profile of Horthy in `blog-pragmaticengineer-orosz-horthy-context-engineering.md`,
  he is CEO/cofounder of HumanLayer, the coiner of the term "context
  engineering," and author of "12-Factor Agents" — an established,
  independently-recognized voice in this specific subfield (agent context and
  harness design), not an anonymous blog byline. The skill itself is described
  as already deployed ("It's live in humanlayer today"), giving this a
  first-party production-use basis rather than a purely speculative proposal.
  The post also credits an inspiration source (Coda Hale's conference talk on
  "intuition vs. attention in infrastructure systems") and several named
  practitioners (Dillon Mulroy, tanish, Matt Pocock) who built on or reacted to
  the skill, which is evidence of external uptake beyond HumanLayer's own use,
  though that uptake is self-reported by the author rather than independently
  verified.
- **Scope**: Covers the motivating problem (verbose, jargon-heavy agent
  output), a cognitive-science-flavored justification for visual over textual
  communication, a catalogue of eight visual representation formats mapped to
  problem shapes, installation/invocation instructions, and a short roundup of
  community reactions and derivative skills. Does NOT cover: any quantitative
  measurement of comprehension time, token cost, or accuracy improvement from
  using visual vs. prose output (no benchmark or user study is presented — the
  case is made by analogy and worked examples, not data); a technical
  specification of the skill's prompt/implementation; or guidance on how this
  interacts with existing harness configuration surfaces (CLAUDE.md, other
  skills) beyond installation.

## Extracted Claims

### Claim 1: The core recommendation is to make coding agents communicate visually rather than in dense prose

- **Evidence**: Framing statement given as the article's tl;dr.
- **Confidence**: emerging
- **Quote**: "tl;dr make your agent converse visually instead of in walls of prose."
- **Our assessment**: This is the article's organizing thesis and the
  Prospector's flagged chapter anchor. It's a prescriptive design
  recommendation for agent *output*, not agent *input/context* — most of the
  corpus's context-engineering material (including the companion HumanLayer
  posts) addresses what goes into the context window; this addresses what
  comes out of it toward the human. That's a genuinely different axis of
  harness design: communication ergonomics rather than instruction adherence
  or token budget.

### Claim 2: Agent output has become more jargon-filled and less readable even as underlying model capability has increased, and something of Claude's earlier "voice" or "personality" has been lost in the process

- **Evidence**: Author's own observed trend, offered as the motivating problem
  for the whole post.
- **Confidence**: anecdotal
- **Quote**: "agents got more intelligent on paper, but the experience of using
  them got noticeably worse along this dimension. the thing people used to
  love about claude - its voice, it's personality, its "soul" has been flushed
  out in the RL dungeon"
- **Our assessment**: This is a striking, quotable claim but it's a personal
  impression with no supporting metric (no before/after transcript comparison,
  no user survey) — "RL dungeon" is a colorful causal attribution (implying
  RLHF/post-training is responsible for the perceived personality loss) that
  the article does not substantiate mechanistically. Treat the *symptom*
  (output feels more jargon-heavy/less readable) as the useful, checkable part
  of this claim, and the *causal attribution* (RL post-training specifically)
  as an unverified aside. The author gestures at corroborating opinion from
  named third parties (a former Reddit CEO, another practitioner) but those
  are embedded tweet screenshots in the source page, not extractable text — we
  could not independently verify their content, so they are not quoted here.

### Claim 3: Visual processing is cognitively cheaper for humans than reading prose because it leverages evolved visual-processing capacity, and software/tools should be shaped to fit human cognition rather than the reverse

- **Evidence**: Author's stated justification, citing a conference talk by
  Coda Hale as partial inspiration and using a tool-design analogy.
- **Confidence**: anecdotal
- **Quote**: "your visual cortex was trained over millions of years to process
  rich visual information effortlessly" / "Just as an axe must fit the human
  hand to be useful, software must fit the human mind to be useful"
- **Our assessment**: This is an appeal to evolutionary intuition, not a cited
  study — no cognitive-science research is referenced for the specific claim
  that structured visual formats reduce comprehension load for *code-shaped*
  information (as opposed to, say, photographs or natural scenes, which is
  what most visual-cognition research actually studies). The tool-design
  analogy ("axe must fit the human hand") is a reusable framing for why
  agent-output ergonomics matters as a harness-engineering concern in its own
  right, independent of whether the specific evolutionary claim holds up.

### Claim 4: The skill supports eight distinct visual representation formats, each mapped to a specific problem shape

- **Evidence**: Enumerated catalogue with a one-line rationale per format.
- **Confidence**: anecdotal
- **Quote**: "Same idea on the frontend, with the state hooks and module
  boundaries that matter kept in and everything else left out." (component
  trees) / "A shallow file tree, one line of responsibility per entry." (file
  layouts) / "The shape of the code before any of it exists—the stuff that's
  too internal for an architecture doc" (types and signatures)
- **Our assessment**: This is the most concrete, directly reusable artifact in
  the post — a checklist practitioners can map onto their own problem type
  (see Concrete Artifacts below for the full catalogue). No format is claimed
  to be universally best; each is scoped to a stated use case (frontend state,
  backend control flow, algorithms, pre-implementation design, incremental
  diffs, interactive prototypes), which is a more calibrated claim than "always
  show a diagram."

### Claim 5: Program design — discussing the shape of code (types, signatures, call stacks) before an agent writes it — is a phase many practitioners skip, and visual representations make that phase practical again

- **Evidence**: Author's stated opinion connecting the visual-formats
  catalogue back to a broader software-process argument.
- **Confidence**: anecdotal
- **Quote**: "This is really good for program design - the phase many folks
  skip these days, but that I think is essential. You should be discussing the
  shape of the code (the types, the signatures, the call stacks) before agents
  get to work on writing it."
- **Our assessment**: This reframes visual output as a design-review tool, not
  just a post-hoc explanation aid — the implied workflow is: agent proposes a
  visual sketch of types/call stacks → human reviews/approves → agent
  implements. That is a concrete, adoptable verification-gate pattern
  (design-before-code) distinct from the formatting claim itself, and it
  connects this post to the corpus's broader "review before you let the agent
  proceed" theme (see Cross-References).

### Claim 6: The same visual techniques can be used after the fact to navigate large diffs during code review, not only before writing code

- **Evidence**: Author's stated secondary use case, plus an explicit "diff
  syntax" format in the catalogue.
- **Confidence**: anecdotal
- **Quote**: "The same techniques can also be used to explore large diffs
  post-hoc to understand what to dig into during review." / "You can also use
  diff syntax for this, if most of the content is unchanged"
- **Our assessment**: This extends the tool's use case from "explain a plan
  before implementation" to "triage a large diff during review," making it
  relevant to both Chapter 02 (harness/output design) and any guide material
  on human review of agent-generated diffs. No data is given on how much
  faster or more accurate review becomes with this technique — it is offered
  as a workflow suggestion, not a measured result.

### Claim 7: HumanLayer already treats HTML as a first-class agent output format, not just Markdown, and the show-me skill's HTML mockup/diagram formats build on that existing capability

- **Evidence**: First-party statement about HumanLayer's own product
  behavior.
- **Confidence**: settled (as a factual description of HumanLayer's own
  product; not a general claim about other harnesses)
- **Quote**: "In [humanlayer](https://humanlayer.com) we let the agent include
  HTML directly in assistant responses." / "HTML has replaced figma for a lot
  of our prototyping work."
- **Our assessment**: This corroborates the corpus's existing
  `blog-simonwillison-html-effectiveness.md` note (Thariq Shihipar/Anthropic's
  argument that requesting HTML rather than Markdown unlocks SVG diagrams,
  interactive widgets, and richer presentation) with an independent,
  second-vendor data point: two different agentic-tooling teams have
  converged on "let the agent emit HTML for output" as a harness-level
  decision, not a one-off prompt trick.

### Claim 8: The skill is distributed and installed through the same third-party skill-registry mechanism ("npx skills add ...") already flagged elsewhere in the corpus as a supply-chain risk

- **Evidence**: Concrete installation instructions given in the article.
- **Confidence**: settled (as a factual description of the distribution
  mechanism; the security implication is our assessment, not the article's)
- **Quote**: "`npx skills add humanlayer/skills --skill show-me`" / "It's live
  in humanlayer today, and if you want it in any other coding agent - you can
  get it here"
- **Our assessment**: The article does not itself discuss security, but this
  is directly relevant to `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 12, which — from the *same author/company* — warns that skills carry a
  supply-chain risk comparable to `npm install random-package` and that skill
  registries have distributed malicious skills. show-me is a concrete,
  named example of exactly the installation pattern that warning describes
  (`npx skills add <namespace>/<repo> --skill <name>`), from a source the
  guide would otherwise cite approvingly. This is not a contradiction (both
  claims are from HumanLayer and are mutually consistent — "here's a useful
  skill; also, read what you install before installing it") but the guide
  should pair any recommendation of show-me (or skills generally) with that
  existing supply-chain caution rather than presenting skill installation as
  risk-free.

### Claim 9: The skill has been publicly customized/extended by independent practitioners, evidenced by named derivative work

- **Evidence**: Author-reported examples of third-party adoption and
  variation.
- **Confidence**: anecdotal
- **Quote**: "Dillon Mulroy even made a skill, `/bro`" / "tanish even wrote a
  tool to compute them straight from the AST" / "Restate your last message.
  Stop using jargon and speak coherently. State it more simply and concisely,
  like one human talking to another." (the `/bro` skill's instruction text,
  as quoted by the author)
- **Our assessment**: This is self-reported evidence of uptake (the author
  chose which examples to highlight), not independently verified adoption
  data, but the specificity — a named person, a named derivative skill, a
  quoted instruction string — is more concrete than a vague "people liked it"
  claim. The `/bro` skill in particular is a distinct pattern worth noting on
  its own: it targets the *same* verbosity/jargon problem (Claim 2) but via a
  text-simplification instruction rather than a visual-format substitution,
  suggesting the underlying "agent output is too dense" problem has more than
  one harness-level fix.

## Concrete Artifacts

### Visual format catalogue (verbatim descriptions, article's "What's inside" section)

```
Source: https://www.humanlayer.dev/blog/show-me-skill

1. component trees  — "Same idea on the frontend, with the state hooks and
   module boundaries that matter kept in and everything else left out."
   (frontend program design)
2. call stacks       — "For orchestration or control-flow work, or just any
   backend-shaped problem" (backend orchestration / control flow)
3. diagrams          — "A classic. If your chat interface supports inline
   mermaid, these can help a lot." (state/sequence diagrams)
4. file layouts      — "A shallow file tree, one line of responsibility per
   entry." (scoping refactors, locating code)
5. pseudocode        — "Especially for algorithmic stuff, pseudocode can be
   more concise." (algorithm walkthroughs)
6. types and signatures — "The shape of the code before any of it exists—the
   stuff that's too internal for an architecture doc" (pre-implementation
   design)
7. diff syntax       — "You can also use diff syntax for this, if most of the
   content is unchanged" (incremental changes, post-hoc diff review)
8. html mockups / html diagrams — "HTML has replaced figma for a lot of our
   prototyping work." / "Sometimes a diagram or explainer is what you need."
   (prototyping, interactive explainers)
```

### Installation and invocation (verbatim)

```
Source: https://www.humanlayer.dev/blog/show-me-skill

Install: "npx skills add humanlayer/skills --skill show-me"

Invoke: "After installing the skill, invoke `/show-me` or ask the agent to
use the `show-me` skill."

Example prompts:
"this is too much content. show me."
"/show-me as an html explainer"
```

### Article section structure (for navigation / re-reading)

```
Source: https://www.humanlayer.dev/blog/show-me-skill

1. show-me: a coding agent skill for compact visual representations (title)
2. Coding agents are pretty much unreadable
3. i am so sick of this
4. my proposal: show me
5. What's inside
   - component trees / call stacks / diagrams / file layouts / pseudocode /
     types and signatures / diff syntax / html mockups / html diagrams
6. other inspiration
7. go try it
```

## Cross-References

- **Corroborates**: `blog-simonwillison-html-effectiveness.md` (Thariq
  Shihipar/Anthropic's argument that requesting HTML output over Markdown
  unlocks richer presentation) — see Claim 7 above. Two independent
  agentic-tooling sources now converge on "let agents emit HTML, not just
  Markdown" as a deliberate output-format decision.
- **Corroborates**: `blog-humanlayer-skill-issue-harness-engineering.md`
  (same author/company) — that note's Claim 3 ("HumanLayer's CLAUDE.md is
  under 60 lines") and general "lean, high-leverage configuration" thesis are
  consistent with this post's implicit argument that agent *output* should
  also be kept lean (visual, compact) rather than verbose — extending the
  "minimize what gets pushed at the human/context" principle from inputs to
  outputs.
- **Extends**: `blog-humanlayer-skill-issue-harness-engineering.md` Claim 12
  (skills-as-supply-chain-risk, `npm install random-package` analogy) — see
  Claim 8 above. This post is a concrete worked example of the exact
  installation mechanism that warning targets, from the same company; the
  guide should present them together rather than recommending show-me without
  the caution.
- **Extends**: `blog-cognition-codemaps.md` — that note documents Windsurf
  Codemaps, a product feature generating AI-annotated navigable visual maps of
  a codebase specifically to deepen developer understanding before "vibe
  coding." Both sources argue that visual/structural representations of code
  should precede or accompany agent action, but come from different angles:
  Codemaps is a vendor-built, always-on product feature for codebase
  comprehension, while show-me is a lightweight, prompt-driven skill for
  agent *output* on demand. Together they suggest "visual representation of
  code structure as a pre-implementation checkpoint" is emerging as a
  pattern across multiple independent teams, not a one-off idea.
- **Extends**: `blog-simonwillison-mermaid-ascii-go.md` and
  `blog-simonwillison-grok-mermaid.md` — those notes document Mermaid-to-text
  rendering tooling for terminal/non-graphical contexts. This post's
  "diagrams" format explicitly names Mermaid as the preferred diagram syntax
  when the chat interface supports inline rendering; the Willison notes are
  relevant for the case where it doesn't (rendering Mermaid to ASCII/Unicode
  for terminal display).
- **Novel**: (1) A named, installable skill (not just a prompting tip) that
  operationalizes "communicate visually, not verbosely" as a reusable harness
  component — no prior corpus source packages agent-output formatting as an
  installable skill. (2) The explicit catalogue of eight visual formats mapped
  to problem shapes (frontend/backend/algorithmic/pre-implementation/diff/
  prototype) — more granular than any prior corpus guidance on agent
  communication style. (3) The "personality/soul flushed out" framing of
  degraded agent communication as a *separate* failure mode from the corpus's
  existing instruction-adherence and context-degradation themes (see
  `blog-humanlayer-long-context-isnt-the-answer.md`) — this is about output
  *readability*, not output *correctness* or instruction-following.

## Guide Impact

- **Chapter 02 (Harness Engineering — Skills)**: Add show-me as a concrete,
  named worked example of a Skill (extending the existing skills coverage in
  `blog-humanlayer-skill-issue-harness-engineering.md`), paired explicitly
  with that same note's Claim 12 supply-chain warning — the guide should not
  recommend installing third-party skills like this one without also stating
  the "read it like an npm package" caution.
- **Chapter 02 or Chapter 04 (Agent Output / Communication Design)**: Add
  "agent output ergonomics" as a distinct harness-design concern from context
  input management — the guide currently has strong coverage of what goes
  into a context window (instruction budget, CLAUDE.md leanness, MCP tool
  descriptions) but no coverage of how agents should format what comes back
  out to a human reviewer. Cite the eight-format catalogue (Claim 4 /
  Concrete Artifacts) as a starting checklist: component trees, call stacks,
  Mermaid diagrams, file layouts, pseudocode, type signatures, diff syntax,
  HTML mockups/diagrams.
- **Chapter 03 (Safety and Verification)**: Add the "discuss the shape of the
  code before agents write it" design-review pattern (Claim 5) as a concrete
  verification-gate technique — a visual sketch of types/signatures/call
  stacks as a cheap, human-reviewable checkpoint before implementation
  begins, distinct from post-hoc diff review (Claim 6, which is the same
  toolset applied after the fact).
- **Chapter 04 (Context Engineering)**: Note the HTML-as-output-format
  convergence (Claim 7) alongside the existing `blog-simonwillison-html-effectiveness.md`
  note as two independent teams' evidence that Markdown is not the only or
  best default output format for agent communication.

## Extraction Notes

- Fetched via WebFetch (URL content converted to markdown and processed by a
  fetch-time model). The first fetch returned a paraphrased summary rather
  than verbatim text; all quotes in this note were obtained through multiple
  follow-up targeted fetches, each requesting a specific short passage,
  cross-checked across fetches for consistency, per the same process used in
  the existing `blog-humanlayer-skill-issue-harness-engineering.md` and
  `blog-humanlayer-long-context-isnt-the-answer.md` notes. No quote was
  reconstructed, tightened, or paraphrased and presented as verbatim.
- The article references reactions from "the former CEO of reddit" (implied
  to be Yishan Wong), Mario Zechner, and Connor from Replicas, presented on
  the page as embedded tweet screenshot images rather than extractable text.
  We could not obtain their exact wording through WebFetch and have not
  quoted them; Claim 2's assessment flags this explicitly rather than
  fabricating a quote or paraphrasing an unreadable image as if it were text.
  Per MINER.md §2a, only the `/bro` skill's instruction text (quoted directly
  by the author as plain text, not an image) was quotable and is used in
  Claim 9.
- No contradiction with any existing source note was found. This post's core
  claim (visual output reduces cognitive load and should be preferred to
  verbose prose) does not conflict with any prior corpus claim; the
  supply-chain-risk connection to `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 12 (see Cross-References) is a pairing/caution relationship, not a
  disagreement, so no contradiction issue was filed per MINER.md §4a.
- Confidence set to `emerging`: the underlying communication-ergonomics
  problem (verbose, jargon-heavy agent output) and the practical fix (an
  installed, usable skill with a concrete format catalogue) are credible and
  first-party production-grounded, but the specific cognitive-science
  justification (visual cortex evolution) is an appeal to intuition rather
  than a cited study, and no comprehension/efficiency metric is reported for
  the technique itself.
