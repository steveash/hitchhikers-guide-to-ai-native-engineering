---
source_url: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
source_type: blog-post
title: "The new rules of context engineering for Claude 5 generation models"
author: "Thariq Shihipar (Member of Technical Staff, Anthropic)"
date_published: 2026-07-24
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: emerging
issue: "#2218"
---

# The new rules of context engineering for Claude 5 generation models

> First-party Anthropic guidance on how context engineering changes for Claude 5-generation
> models (Claude Opus 5, Claude Fable 5): a >80% reduction in Claude Code's system prompt
> with no measured eval loss, a shift from explicit rules to model judgment, from usage
> examples to expressive tool interfaces, and the introduction of a `claude doctor` /
> `/doctor` command to help practitioners rightsize their own system prompts, skills, and
> CLAUDE.md files.

## Source Context

- **Type**: blog-post (claude.com/blog, July 24, 2026; first-party Anthropic engineering
  account)
- **Author credibility**: Thariq Shihipar is a member of technical staff at Anthropic
  working on Claude Code — the same author as `blog-anthropic-session-management-1m-context.md`
  (April 2026) and `blog-anthropic-claude-code-skills-lessons.md` (June 2026). This is the
  third post in an emerging series from the same practitioner on Claude Code context
  engineering, giving it strong internal-consistency value: claims here can be checked
  against his own prior statements. As with those posts, this is product/engineering team
  communication describing design intent and internal practice, not an independently
  audited study.
- **Scope**: Covers how context engineering practices for Claude Code's system prompt
  should change for Claude 5-generation models specifically (Claude Opus 5, Claude Fable 5).
  Addresses: the magnitude of the system prompt reduction, five specific shifts in practice
  (rules→judgment, examples→interface design, upfront→progressive disclosure,
  repetition→consolidation, manual CLAUDE.md memory→auto-memory), a four-part framework for
  assembling context (System Prompt, CLAUDE.md, Skills, References), and the `claude doctor`
  command. Does NOT cover specific eval names/benchmarks, quantitative memory-recall
  accuracy, token-level before/after prompt diffs, or guidance for models prior to the
  Claude 5 generation.

## Extracted Claims

### Claim 1: Anthropic removed over 80% of Claude Code's system prompt for Claude 5-generation models with no measurable loss on coding evaluations
- **Evidence**: First-party quantitative claim about an internal change to Claude Code's
  production system prompt, tied to a stated evaluation result.
- **Confidence**: emerging (specific percentage figure and no-loss claim stated directly by
  the team that made the change, but no named eval suite, methodology, or numeric score is
  given — "no measurable loss" is asserted, not shown)
- **Quote**: "We removed over 80% of Claude Code's system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations."
- **Our assessment**: This is the headline claim and the single most actionable data point
  in the post: an 80%+ prompt reduction is a large, specific number from the team that
  controls the artifact being reduced. The absence of a named eval suite or numeric
  before/after score means the "no measurable loss" half of the claim cannot be
  independently checked — treat the magnitude of the reduction as credible (it is a factual
  claim about their own codebase) and the performance-parity claim as an internal assertion
  pending corroboration. This is a stronger, more specific version of the general
  "minimize system prompts for advanced models" guidance implicit elsewhere in the corpus.

### Claim 2: Newer Claude models require less explicit constraint and can be trusted with judgment calls that previously needed explicit rules
- **Evidence**: General framing principle stated as the premise for the rules→judgment
  shift, illustrated with a specific before/after example about code comments.
- **Confidence**: emerging (design rationale from the team building the model and the
  harness; plausible given the concrete example given, but "better judgement" is not
  quantified)
- **Quote**: "But newer models have better judgement and can handle these decisions well without explicit rules."
- **Our assessment**: This is the conceptual thesis the rest of the post's specific
  recommendations hang on. It is a claim about model capability improvement, made by the
  same organization that trains the model — inherently harder to verify independently than
  an architectural fact. Still useful as the stated rationale: practitioners writing
  CLAUDE.md/skill instructions for Claude 5-generation models should default to describing
  outcomes and judgment criteria rather than enumerating exhaustive rules, per Anthropic's
  own stated internal practice.

### Claim 3: The concrete instance of the rules→judgment shift: replacing an explicit comment-formatting rule with a "match the surrounding code" instruction
- **Evidence**: Direct before/after example given in the article — an old explicit rule
  contrasted with the new judgment-based instruction.
- **Confidence**: settled (this is the literal, verbatim wording change the article
  presents as its example; not in dispute, it is simply what the article states was
  changed)
- **Quote**: "Write code that reads like the surrounding code: match its comment density, naming, and idiom."
- **Our assessment**: This is the single clearest before/after artifact in the post. The
  contrast (see Concrete Artifacts) shows the shift from a specific negative rule
  ("never write multi-paragraph docstrings") to a general judgment criterion ("match the
  surrounding code"). This is directly reusable as a template: practitioners can apply the
  same transformation — replace enumerated formatting rules with "match the surrounding
  code" — to their own CLAUDE.md and skill instructions.

### Claim 4: Providing usage examples for tools can constrain Claude 5-generation models to a narrower exploration space than intended; expressive interface design is the recommended alternative
- **Evidence**: Direct claim contrasting the old "number one rule" (give examples) against
  the new recommendation (design better interfaces), with a concrete illustration using the
  Todo tool's status enum.
- **Confidence**: emerging (specific, testable claim about a training/behavior effect of
  examples, stated without supporting data — "we've found" is asserted, not shown)
- **Quote**: "The number one rule for tool usage was to give Claude examples on how to use them. With our newest models, we've found that giving examples actually constrains them to a certain exploration space. Instead of using examples, think more about the design of your tools, scripts and files- what parameters does Claude have and how can they be more expressive?"
- **Our assessment**: This reverses what had been treated as settled practical wisdom
  (provide examples to guide tool use) for the Claude 5 generation specifically. If accurate,
  this has direct implications for how teams write MCP tool descriptions and skill
  instructions: fewer worked examples, more expressive parameter design (e.g., enums that
  encode intended state machines, as in Claim 5's Todo tool illustration). This is the
  claim most likely to be model-version-dependent — teams still targeting non-Claude-5
  models should not assume this reversal applies to them.

### Claim 5: A well-designed tool parameter (e.g., an enum) can hint at correct usage without a separate usage example — illustrated by the Todo tool's status field
- **Evidence**: Concrete worked example from the article: the Todo tool's `status` field as
  an enum of `pending`, `in_progress`, `completed`.
- **Confidence**: emerging (concrete illustrative example from the article; a single case,
  not a general study of interface-vs-example effectiveness)
- **Quote**: "For example, in the Todo tool example, just listing status as an enumeration between pending, in_progress, and completed, hints to Claude about how to use it. The instruction on keeping one item in_progress helps define our requested behavior."
- **Our assessment**: This is the practical instantiation of Claim 4 — a specific,
  checkable design pattern rather than an abstract principle. The enum itself communicates
  the intended workflow (items move pending → in_progress → completed, one at a time)
  without a prose example walking through a sample session. Practitioners designing their
  own tool schemas (MCP tools, skill scripts) can apply this directly: prefer constrained,
  well-named parameter types over free-text parameters plus a usage example.

### Claim 6: Claude Code has become highly competent at progressive disclosure — loading the right context at the right time rather than upfront — and moved verification and code review into separately-callable skills as an example
- **Evidence**: First-party claim about Claude Code's own harness evolution, with a named
  concrete example (verification and code review moved into their own skills).
- **Confidence**: emerging (specific claim about internal harness architecture change;
  plausible and consistent with the skills taxonomy in `blog-anthropic-claude-code-skills-lessons.md`,
  but "very competent" is a qualitative self-assessment)
- **Quote**: "Since then, Claude Code has gotten very competent at using progressive disclosure- loading the right context at the right times. For example, we moved verification and code review into their own skills that Claude Code could selectively call."
- **Our assessment**: This corroborates and extends `blog-anthropic-claude-code-skills-lessons.md`
  Claim 3 (verification skills have had the most measurable internal impact on output
  quality) by naming the specific mechanism: verification and code review used to live in
  the always-loaded system prompt and were moved to selectively-loaded skills. This is a
  concrete migration pattern — "audit your system prompt for content that is only needed
  some of the time, and move it to a skill" — that practitioners can apply to their own
  CLAUDE.md/system-prompt content.

### Claim 7: The same progressive disclosure principle applies to practitioners' own CLAUDE.md and Skill.md files; a common myth is that these should be a comprehensive central repository of every practice Claude might need
- **Evidence**: Direct claim naming and rejecting a specific misconception, with a
  recommended alternative pattern (a tree of files loaded at the right time).
- **Confidence**: emerging (design recommendation extending Claim 6's internal pattern to
  external practitioners; consistent with, but not identical to, the progressive-disclosure
  guidance already in the corpus)
- **Quote**: "A common myth is that you want to make these a central repository for every known practice that you _might_ run into, because Claude would not find it otherwise."
- **Our assessment**: This directly corroborates `blog-humanlayer-writing-a-good-claude-md.md`
  Claim 8 (progressive disclosure via a separate `agent_docs/` directory referenced, not
  embedded) and `blog-anthropic-maccoss-developer-onboarding.md` Claim 5 ("reference do not
  embed"). Three independent sources — two practitioner, one first-party Anthropic — now
  converge on the same anti-pattern (CLAUDE.md/skills as an exhaustive knowledge dump) and
  the same remedy (tree of files, loaded selectively). This raises confidence in the
  progressive-disclosure recommendation for the guide beyond any single source.

### Claim 8: Skills should be lightweight guides that let Claude find information when needed, not overconstrained except in highly important areas; long skills should be split across many files using progressive disclosure
- **Evidence**: Direct design guidance for skill authoring, extending the progressive
  disclosure principle to skill length/structure specifically.
- **Confidence**: emerging (design recommendation, consistent with but less detailed than
  the six best practices in `blog-anthropic-claude-code-skills-lessons.md`)
- **Quote**: "Think of skills as lightweight guides to let Claude find information when needed. Avoid making them overconstrained, except in highly important areas. For long skills, try and use progressive disclosure as much as possible- divide it into many files and split them out."
- **Our assessment**: This is a lighter restatement of ground already covered in more depth
  by `blog-anthropic-claude-code-skills-lessons.md` (the "avoid railroading Claude" and
  "file system as progressive disclosure" best practices from that post). Not novel on its
  own, but the "except in highly important areas" carve-out is a useful addition: it
  implies deliberate over-specification is still warranted for genuinely high-stakes
  procedures (e.g., destructive operations), consistent with that post's on-demand hooks
  pattern for exactly those cases.

### Claim 9: Earlier Claude models needed repeated instructions and were more likely to follow instructions near the end of the context window; this caused duplicate tool guidance across the system prompt and tool descriptions, which newer models no longer need
- **Evidence**: Explicit mechanistic explanation of why the system prompt had grown
  duplicated content, plus the fix applied (deleting repeats, consolidating into tool
  descriptions).
- **Confidence**: emerging (mechanistic explanation from the team that authored the system
  prompt; internally consistent but not independently measured for this specific claim)
- **Quote**: "Earlier Claude models could sometimes need repeated instructions or be more likely to listen to instructions at the end of their context window than at the start. This meant our system prompt would sometimes have references to tools in the main system prompt as well as instructions in the tool description. We found we could delete these repeat examples and put instructions on how to use tools in the tool descriptions rather than the system prompt."
- **Our assessment**: This is a specific, mechanistic contributor to system-prompt bloat
  that the corpus has not previously named this precisely: not just "system prompts grow
  over time" but "system prompts grow because of position-based redundancy hedging against
  weaker instruction-following." The remedy (consolidate tool guidance into the tool
  description, not the system prompt) is directly actionable and pairs with the
  interface-design-over-examples guidance (Claim 4): tool descriptions become the single
  place tool usage is documented.

### Claim 10: Claude now automatically saves memories relevant to the work and the user, replacing the earlier practice of manually invoking a `#` hotkey to write to CLAUDE.md
- **Evidence**: Direct statement contrasting the old manual-memory workflow with the new
  automatic one.
- **Confidence**: emerging (product-behavior claim about how Claude Code currently handles
  memory; stated as current fact but no mechanism detail — what triggers a save, where
  memories are stored, how conflicts are resolved — is given in this article)
- **Quote**: "We used to encourage users to save things to Claude's memory, by using the # hotkey to write to their CLAUDE.md automatically. Instead, Claude now automatically saves memories that are relevant to the work and to you."
- **Our assessment**: This is a significant workflow change for any guide section that
  currently documents the `#` hotkey as the way to persist learnings to CLAUDE.md — that
  guidance is now describing a superseded mechanism per this source. The claim is thin on
  mechanism (no detail on storage location, retrieval scope, or override/opt-out), which
  limits how specific the guide can be about the new behavior without further sourcing.
  Flag as a claim needing a follow-up source before the guide asserts implementation
  details of auto-memory.

### Claim 11: A system prompt should be tied to product context — telling Claude what product it is operating in and what it is doing — as distinct from CLAUDE.md, Skills, or References
- **Evidence**: Definitional statement as part of the article's four-part context-assembly
  framework (System Prompt, CLAUDE.md, Skills, References).
- **Confidence**: settled (a definitional/architectural claim about what each context
  source is for, not a contested empirical claim)
- **Quote**: "A system prompt is heavily tied to the product context. It tells Claude what product it's operating in and what it's doing."
- **Our assessment**: This gives the guide a clean four-way division of labor for context
  sources that the corpus has previously discussed piecemeal (CLAUDE.md guidance, skills
  guidance, session-management guidance) but not as a single named framework. Useful as an
  organizing structure for a "context sources" reference table: System Prompt = product
  identity/purpose, CLAUDE.md = repo orientation, Skills = on-demand domain expertise,
  References = task-specific artifacts (see Claim 13).

### Claim 12: CLAUDE.md should be kept lightweight, briefly describing what the repo is for, with most tokens spent on codebase-specific gotchas rather than general description
- **Evidence**: Direct guidance statement as part of the four-part framework.
- **Confidence**: settled (consistent, low-controversy guidance corroborated by multiple
  independent sources already in the corpus)
- **Quote**: "Keep your CLAUDE.md lightweight and briefly describe what your repo is for, but spend most of the tokens on gotchas inside of the codebase."
- **Our assessment**: This corroborates `blog-anthropic-large-codebase-best-practices.md`
  Claim 6 ("lean and layered" CLAUDE.md) and `blog-anthropic-maccoss-developer-onboarding.md`
  Claim 4 (CLAUDE.md as "lay of the land," not domain expertise). The specific allocation
  advice here — spend tokens on gotchas, not general description — is slightly more
  prescriptive than "lay of the land" and gives practitioners a concrete token-budget
  heuristic: description should be brief; gotchas should dominate. This is now corroborated
  by three independent sources (two first-party Anthropic, one MacLean practitioner
  account), raising it near `settled` for the guide.

### Claim 13: References (via @ mentions) let Claude access in-depth, task-specific information such as specs, mockups, or code, and code should be prioritized over other reference formats for clarity
- **Evidence**: Definitional statement as part of the four-part framework, with an explicit
  preference ordering (code preferred for clarity).
- **Confidence**: emerging (definitional/architectural claim; the specific preference for
  code-over-other-formats is a design opinion, not independently tested here)
- **Quote**: "You can @ mention files to include them as references. References allow Claude to refer to in-depth information about the current plan."
- **Our assessment**: This names "References" as a distinct fourth category in the context
  framework, separate from CLAUDE.md and Skills — a categorization not explicit elsewhere
  in the corpus (prior sources discuss @ mentions as a mechanism but not as a named peer
  category alongside CLAUDE.md/Skills/System Prompt). Useful primarily as a taxonomy
  contribution: it clarifies that transient, task-specific context (a spec for the current
  plan) belongs in an @ mention, not baked into CLAUDE.md or a skill (which are for
  durable, repo- or task-type-wide knowledge).

### Claim 14: Anthropic introduced a `claude doctor` (also referenced as the `/doctor` command in Claude Code) to help practitioners rightsize their own skills and CLAUDE.md files, mirroring the internal system-prompt simplification
- **Evidence**: Direct announcement of a new tool, framed as the practical takeaway readers
  can apply themselves.
- **Confidence**: emerging (announcement of a new first-party tool; no detail given in this
  article on what specifically the command checks, how it scores files, or what its output
  looks like)
- **Quote**: "We've put these best practices in `claude doctor;` use the command /doctor in Claude Code to rightsize your skills, and CLAUDE.md files."
- **Our assessment**: This is the most novel, concrete artifact in the post and not present
  in any existing corpus source — no prior note documents a `claude doctor` or `/doctor`
  command. If accurate, this gives practitioners a first-party automated tool for applying
  the article's own recommendations (trim system prompt/CLAUDE.md/skills content) rather
  than doing so by manual audit. The article gives no detail on the command's internal
  logic or output format, so the guide should describe its existence and stated purpose
  without asserting specifics about its behavior until a dedicated source (docs page or
  release note) is mined.

## Concrete Artifacts

### Before/after: explicit rule → judgment-based instruction (Claim 3)
```
Source: claude.com/blog, "The new rules of context engineering for Claude 5
generation models" (Thariq Shihipar, Anthropic, 2026-07-24)

OLD (rule-based, pre-Claude-5 framing):
"In code: default to writing no comments. Never write multi-paragraph
docstrings or multi-line comment blocks — one short line max."

NEW (judgment-based, Claude 5-generation framing):
"Write code that reads like the surrounding code: match its comment
density, naming, and idiom."
```

### Four-part context assembly framework
```
Source: claude.com/blog, "The new rules of context engineering for Claude 5
generation models" (Thariq Shihipar, Anthropic, 2026-07-24)

1. SYSTEM PROMPT
   "A system prompt is heavily tied to the product context. It tells
   Claude what product it's operating in and what it's doing."

2. CLAUDE.md
   "Keep your CLAUDE.md lightweight and briefly describe what your repo
   is for, but spend most of the tokens on gotchas inside of the codebase."

3. SKILLS
   "Think of skills as lightweight guides to let Claude find information
   when needed. Avoid making them overconstrained, except in highly
   important areas."

4. REFERENCES
   "You can @ mention files to include them as references. References
   allow Claude to refer to in-depth information about the current plan."
```

### Five stated shifts in context-engineering practice for Claude 5-generation models
```
Source: claude.com/blog, "The new rules of context engineering for Claude 5
generation models" (Thariq Shihipar, Anthropic, 2026-07-24)
(Framing/labels below are this note's summary structure; quoted lines
inside each are verbatim from the article.)

1. From Rules to Judgment
   "But newer models have better judgement and can handle these
   decisions well without explicit rules."

2. From Examples to Interface Design
   "The number one rule for tool usage was to give Claude examples on
   how to use them. With our newest models, we've found that giving
   examples actually constrains them to a certain exploration space."

3. From Upfront Information to Progressive Disclosure
   "Since then, Claude Code has gotten very competent at using
   progressive disclosure- loading the right context at the right times."

4. From Repetition to Concise Descriptions
   "We found we could delete these repeat examples and put instructions
   on how to use tools in the tool descriptions rather than the system
   prompt."

5. From Manual CLAUDE.md Memory to Auto-Memory
   "Instead, Claude now automatically saves memories that are relevant
   to the work and to you."
```

### `claude doctor` / `/doctor` command announcement
```
Source: claude.com/blog, "The new rules of context engineering for Claude 5
generation models" (Thariq Shihipar, Anthropic, 2026-07-24)

"We've put these best practices in `claude doctor;` use the command
/doctor in Claude Code to rightsize your skills, and CLAUDE.md files."

"We rolled out a new command called `claude doctor,` which will help
you do this automatically as well."

No further mechanism detail (scoring method, output format, what
specifically is checked) is given in this article.
```

## Cross-References

- **Corroborates**: `blog-anthropic-session-management-1m-context.md` and
  `blog-anthropic-claude-code-skills-lessons.md` — same author (Thariq Shihipar), forming a
  three-post series on Claude Code context engineering (April, June, July 2026). This post's
  Claim 6 (verification and code review moved into selectively-callable skills) directly
  corroborates and names the mechanism behind `blog-anthropic-claude-code-skills-lessons.md`
  Claim 3 (verification skills have had "the most measurable impact on Claude's output
  quality internally") — this source confirms that content used to live in the always-loaded
  system prompt before being moved to a skill.

- **Corroborates**: `blog-humanlayer-writing-a-good-claude-md.md` Claim 8 (progressive
  disclosure via a separate, referenced-not-embedded docs directory) and
  `blog-anthropic-maccoss-developer-onboarding.md` Claim 5 ("reference do not embed" for
  skills) — this source's Claim 7 (rejecting the "CLAUDE.md/skills as a comprehensive
  central repository" myth) is a first-party Anthropic statement of the same anti-pattern
  and remedy two independent practitioner sources already document. Three independent
  sources (two practitioner, one first-party) now converge.

- **Corroborates**: `blog-anthropic-large-codebase-best-practices.md` Claim 6 ("lean and
  layered" CLAUDE.md, loaded additively) and `blog-anthropic-maccoss-developer-onboarding.md`
  Claim 4 (CLAUDE.md as "lay of the land," not domain expertise) — this source's Claim 12
  (spend most CLAUDE.md tokens on gotchas, not general description) is consistent with and
  adds a token-allocation heuristic to both.

- **Extends**: `blog-humanlayer-writing-a-good-claude-md.md` Claim 10 ("never send an LLM to
  do a linter's job" — use deterministic tools for deterministic work) — this source's
  Claim 4/5 (prefer expressive tool interface design over prose examples) is the same
  underlying principle (encode constraints in the deterministic parts of the system —
  schema, enum, linter — rather than relying on the model to follow prose instructions)
  applied to tool design rather than code style.

- **Extends**: `blog-anthropic-session-management-1m-context.md` Claim 10 (the "will I need
  this tool output again, or just the conclusion?" subagent heuristic) — both sources are
  first-party guidance on when to route information through a narrower, purpose-scoped
  channel (a subagent's clean context there; a selectively-loaded skill or tool description
  here) rather than the main, always-present context.

- **Novel**:
  1. The specific >80% system-prompt reduction figure for Claude 5-generation models — no
     existing corpus source gives a percentage for this change.
  2. The `claude doctor` / `/doctor` command — not documented in any existing source note.
  3. The named mechanistic explanation for system-prompt duplication (weaker instruction
     recall near context-window end in earlier models, driving redundant tool guidance in
     both system prompt and tool description) — more specific than the corpus's general
     "context rot" discussions.
  4. The explicit reversal of "give Claude usage examples for tools" as best practice,
     specific to Claude 5-generation models, with the Todo-tool-enum illustration.
  5. The four-part named context-assembly framework (System Prompt / CLAUDE.md / Skills /
     References) as an explicit peer taxonomy — prior sources discuss these mechanisms but
     not as four named, parallel categories.
  6. Auto-memory as a stated replacement for the manual `#`-hotkey-to-CLAUDE.md workflow —
     not documented in any existing corpus source.

## Guide Impact

- **Chapter 02 (Harness Engineering — CLAUDE.md/system prompt authoring)**: Add the
  rules→judgment shift (Claims 2-3) as Claude-5-generation-specific guidance, with the
  before/after comment-rule example as the template practitioners can apply to their own
  instructions. Explicitly scope this to Claude 5-generation models — do not present it as
  general advice superseding rule-based instructions for earlier models, since the source
  itself frames this as a model-generation-specific change.

- **Chapter 02 (Harness Engineering — Tool/MCP design)**: Add the reversal on tool usage
  examples (Claim 4) and the enum-as-interface-hint pattern (Claim 5) as guidance for
  designing MCP tools and skill scripts for Claude 5-generation models: prefer expressive,
  constrained parameter schemas over prose usage examples. Add Claim 9's consolidation
  guidance (tool usage instructions belong in the tool description, not duplicated in the
  system prompt) as a concrete deduplication rule.

- **Chapter 02 (Harness Engineering — Progressive disclosure)**: Add this source (Claim 7)
  as a third, first-party corroborating citation alongside `blog-humanlayer-writing-a-good-claude-md.md`
  and `blog-anthropic-maccoss-developer-onboarding.md` for the "reference, don't embed
  everything" CLAUDE.md/skills anti-pattern — this strengthens that guidance from
  practitioner-observed to practitioner-plus-first-party-corroborated.

- **Chapter 02 (Harness Engineering — Context source taxonomy)**: Add the four-part
  framework (Claims 11-13: System Prompt / CLAUDE.md / Skills / References) as an explicit
  organizing table for a "where does this content belong?" decision guide, distinct from
  the existing five-extension-point harness taxonomy in `blog-anthropic-large-codebase-best-practices.md`
  (which covers CLAUDE.md, hooks, skills, plugins, MCP servers as harness surfaces — this
  framework is specifically about context sources feeding a session, a related but
  narrower framing).

- **Chapter 04 (Context Engineering — Memory)**: Flag the auto-memory claim (Claim 10) as a
  workflow change: any existing guide content instructing users to press `#` to save a
  learning to CLAUDE.md should be marked as describing a superseded manual workflow, with a
  note that Claude Code now performs this automatically per this source. Mark this
  explicitly as needing a follow-up, more detailed source (docs page or release note) before
  the guide asserts implementation specifics (what triggers a save, where memories live,
  how to review/delete them).

- **Chapter 02 (Harness Engineering — Tooling)**: Add `claude doctor` / `/doctor` (Claim 14)
  as a tool for auditing and rightsizing CLAUDE.md/skills/system-prompt content, alongside
  the existing `/usage` and `/context` tooling references from other corpus sources. Note
  in the guide that this note's extraction found no detail on the command's internal
  mechanism — recommend mining a dedicated docs/release-note source on `claude doctor`
  specifically if/when one becomes available.

## Extraction Notes

- WebFetch's default single-pass fetch of this URL returned only a summarized paraphrase,
  not verbatim text (consistent with the pattern noted in `blog-anthropic-claude-code-skills-lessons.md`'s
  extraction notes — claude.com blog posts are consistently summarized rather than
  reproduced verbatim on a first fetch). All quotes in this note were obtained through five
  separate targeted follow-up WebFetch calls, each requesting specific short verbatim
  passages by topic (opening/subheading, `claude doctor`/metrics/Todo-tool quotes,
  progressive-disclosure/auto-memory/repetition/judgment quotes, closing/framework/byline
  quotes, tool-interface/Todo-tool-in-full/metrics/model-name quotes). Passages were
  cross-checked for internal consistency across the separate fetches (e.g., the `claude
  doctor` quote and the 80%-reduction quote each appeared twice, in two different fetch
  responses, with identical wording). No quote was reconstructed or paraphrased and
  presented as verbatim; where the source's own text was needed for context, only the
  contiguous fragment returned by WebFetch is quoted.
- The article does not name a specific evaluation suite or give numeric before/after scores
  for the "no measurable loss on our coding evaluations" claim (Claim 1) — this is flagged
  in that claim's assessment rather than silently treated as a benchmarked result.
  Similarly, the auto-memory claim (Claim 10) and the `claude doctor` claim (Claim 14) are
  both light on implementation mechanism; the Guide Impact section explicitly recommends
  follow-up sourcing for both before the guide asserts implementation specifics.
  Confidence_overall is set to `emerging` rather than `settled` to reflect that this is a
  first-party account of internal practice and product intent (high authority) without
  independent measurement or a second corroborating source for the model-generation-specific
  claims (Claims 1, 2, 4).
  Confidence_overall is not `anecdotal`: several claims (progressive disclosure, CLAUDE.md
  token allocation, the four-part framework's definitional statements) are corroborated by
  multiple independent existing sources and are closer to settled.
- No sub-pages were linked from the article that required following; the piece is a
  single-page blog post. No paywall or access issue encountered — the article is public
  on claude.com.
- No contradiction with any existing corpus source was identified. The tool-usage-examples
  reversal (Claim 4) could look superficially like a contradiction of general "provide
  examples" guidance elsewhere in the corpus, but this source explicitly scopes the reversal
  to Claude 5-generation models specifically ("With our newest models, we've found...") —
  this is a conditioning variable (which model generation), not a contradiction, per
  MINER.md §4a's guidance to not file conditioning-variable differences as contradictions.
