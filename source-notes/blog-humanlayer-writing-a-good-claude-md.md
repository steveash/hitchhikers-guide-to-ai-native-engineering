---
source_url: https://www.humanlayer.dev/blog/writing-a-good-claude-md
source_type: blog-post
title: "Writing a good CLAUDE.md"
author: "Kyle (HumanLayer, @0xblacklight)"
date_published: 2025-11-25
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1825"
---

# Writing a good CLAUDE.md

> HumanLayer's practitioner framework for CLAUDE.md content: a WHAT/WHY/HOW
> structure for what to include, an instruction-budget rationale (backed by an
> external arXiv citation) for why less is more, and a progressive-disclosure
> pattern (a separate `agent_docs/` directory referenced, not embedded) for
> keeping the file itself lean while still surfacing deep project knowledge.

## Source Context

- **Type**: blog-post (humanlayer.dev/blog, November 25 2025; practitioner
  synthesis from an agentic-coding-tools company)
- **Author credibility**: Kyle, writing for HumanLayer (@0xblacklight), a
  company building agentic coding / human-in-the-loop tooling. This is the
  earliest of what is now three related HumanLayer posts already in or
  entering the corpus (`blog-humanlayer-skill-issue-harness-engineering.md`,
  published 2026-03-12, and `blog-humanlayer-long-context-isnt-the-answer.md`,
  published ~11 days after that) — all first-party practitioner accounts
  grounded in HumanLayer's own production CLAUDE.md (stated at "less than
  sixty lines," a figure repeated verbatim in the later `skill-issue` post).
  The 150-200 instruction-following claim is backed by a linked external arXiv
  paper (arxiv.org/pdf/2507.11538) rather than asserted from anecdote alone —
  the same paper is independently cited and more deeply extracted in
  `blog-humanlayer-long-context-isnt-the-answer.md` Claim 6.
- **Scope**: Covers what to put in a CLAUDE.md (WHAT/WHY/HOW), why Claude
  Code's harness can cause CLAUDE.md content to be deprioritized, an
  instruction-count budget argument for keeping the file short, a progressive-
  disclosure pattern for offloading detail to a separate docs directory, an
  argument against using the LLM as a linter, and an argument against
  auto-generating CLAUDE.md via `/init` or similar tools. Does NOT cover: MCP
  servers, skills, sub-agents, hooks, or back-pressure as harness surfaces
  (those are covered in the companion `skill-issue-harness-engineering` post,
  which explicitly recommends configuring CLAUDE.md/AGENTS.md first, before
  those other surfaces) — nor does it define the "instruction budget" concept
  by that name (that term and its full treatment appear only in the third,
  later companion post).

## Extracted Claims

### Claim 1: Coding agents are stateless between sessions, so CLAUDE.md is the default mechanism for reintroducing codebase knowledge every session
- **Evidence**: Framing statement opening the post, presented as the
  foundational principle the rest of the post's recommendations follow from.
- **Confidence**: settled (this is a widely corroborated architectural fact
  about how Claude Code injects CLAUDE.md into context, not a contested claim)
- **Quote**: "Coding agents know absolutely nothing about your codebase at the
  beginning of each session. The agent must be told anything that's important
  to know about your codebase each time you start a session. `CLAUDE.md` is
  the preferred way of doing this."
- **Our assessment**: This is the same statelessness principle already
  well-established in the corpus (e.g., MacLean's "Claude can't learn without
  you recording 'context'" in `blog-anthropic-maccoss-developer-onboarding.md`
  Claim 3). It is not novel on its own, but it is the load-bearing premise for
  every other recommendation in this post — the instruction-budget argument,
  the progressive-disclosure pattern, and the WHAT/WHY/HOW framework all follow
  from "this file is read fresh every time, so its contents must earn their
  place."

### Claim 2: CLAUDE.md should be structured around three questions — WHAT (tech stack, project structure, codebase map), WHY (purpose and functional roles), and HOW (tooling, testing, verification)
- **Evidence**: Explicit three-part framework presented as the post's central
  organizing recommendation for CLAUDE.md content, with a specific note that
  the codebase map is "especially critical for monorepos."
- **Confidence**: emerging (a clear, actionable content framework, but a
  single practitioner's structuring choice rather than a tested taxonomy)
- **Quote**: "Tell Claude about the tech, your stack, the project structure.
  Give Claude a map of the codebase."
- **Our assessment**: This is a more explicit, named framework than the
  corpus's existing CLAUDE.md guidance. MacLean's post
  (`blog-anthropic-maccoss-developer-onboarding.md` Claim 4) describes
  CLAUDE.md as the "lay of the land" but does not break that orientation into
  named sub-categories. WHAT/WHY/HOW gives practitioners a concrete checklist
  ("did I cover all three?") rather than a single evocative metaphor. The two
  framings are complementary, not competing: "lay of the land" is the *scope*
  discipline (don't put domain expertise here), WHAT/WHY/HOW is the *content*
  checklist for what belongs within that scope.

### Claim 3: Claude Code's harness wraps injected CLAUDE.md content with a disclaimer telling the model the context "may or may not be relevant," giving it license to deprioritize CLAUDE.md instructions
- **Evidence**: Direct quote of the harness's system-reminder wrapper text,
  presented as the mechanism explaining why Claude sometimes ignores CLAUDE.md
  rules.
- **Confidence**: settled (the exact wrapper text is independently confirmed
  in `failure-claudemd-ignored-compaction.md`, which documents the same
  mechanism via GitHub issue reporters and notes it is "visible in our own
  system prompt")
- **Quote**: "You should not respond to this context unless it is highly
  relevant to your task."
- **Our assessment**: This is a direct corroboration — the same harness
  mechanism, the same verbatim wrapper text — as the root-cause finding in
  `failure-claudemd-ignored-compaction.md` (its Lesson 1: "CLAUDE.md rules are
  advisory, not mandatory — by design"). This post frames the wrapper's intent
  charitably (Anthropic added it so non-universal "hotfixes" appended to
  CLAUDE.md don't degrade performance on unrelated tasks) rather than purely
  as a bug, which adds useful nuance: the mechanism is a deliberate design
  tradeoff, and the corpus's actionable takeaway (keep CLAUDE.md universally
  applicable) is the correct response to it rather than a workaround for a
  defect.

### Claim 4: Frontier "thinking" LLMs can follow roughly 150-200 instructions with reasonable consistency, per a cited arXiv study
- **Evidence**: Numeric claim attributed to a linked external research paper
  (arxiv.org/pdf/2507.11538), used to argue Claude Code's own system prompt
  already consumes a meaningful share of that budget (~50 instructions per
  this post) before CLAUDE.md content is even added.
- **Confidence**: emerging (the paper is the same one more deeply extracted in
  `blog-humanlayer-long-context-isnt-the-answer.md` Claim 6, where it is
  treated as `emerging` confidence — this post's citation is secondhand
  relative to that deeper extraction, so we inherit that confidence level
  rather than treating the number as settled)
- **Quote**: "Frontier thinking LLMs can follow ~ 150-200 instructions with
  reasonable consistency."
- **Our assessment**: This is the earliest of the three HumanLayer posts to
  cite this paper, predating the "instruction budget" name coined in the later
  companion post by roughly four months. It shows the underlying research
  finding was already informing HumanLayer's CLAUDE.md guidance before it was
  formalized into the named "instruction budget" concept — useful for dating
  the idea's development in the corpus, and it independently corroborates that
  the 150-200 figure and the ~50-instruction system-prompt baseline are
  consistent across both posts by the same author.

### Claim 5: Smaller models degrade exponentially in instruction-following as instruction count increases, while larger frontier thinking models degrade only linearly
- **Evidence**: Direct claim about the shape of the degradation curve,
  distinguishing model size classes, attributed to the same cited research.
- **Confidence**: emerging (specific curve-shape claim from a secondhand
  citation; not independently re-verified against the source paper by this
  extraction)
- **Quote**: "Smaller models tend to exhibit an expotential decay in
  instruction-following performance as the number of instructions increase,
  whereas larger frontier thinking models exhibit a linear decay." [sic —
  "expotential" is the source's own spelling]
- **Our assessment**: This is a genuinely new data point for the corpus — no
  other source note we cross-checked distinguishes *how* instruction-following
  degrades by model tier (exponential vs. linear), only that it degrades. This
  has a practical implication the corpus doesn't currently capture: teams
  using smaller/cheaper models for agentic coding tasks should apply a
  stricter CLAUDE.md instruction budget than teams using frontier models,
  since the same instruction count costs them disproportionately more
  compliance.

### Claim 6: An LLM performs better when its context window holds focused, relevant content — so CLAUDE.md content must be universally applicable across sessions, not task-specific
- **Evidence**: General principle stated directly, with the concrete
  counter-example of including database-schema guidance that is irrelevant
  when working on an unrelated feature.
- **Confidence**: emerging (consistent with, and likely drawing on, the same
  context-rot research family cited in the companion `skill-issue` post's
  Claim 13, but stated here as a general principle rather than tied to a
  specific citation)
- **Quote**: "An LLM will perform better on a task when its context window is
  full of focused, relevant context."
- **Our assessment**: This is the practical filter the post uses to derive its
  "universally applicable only" rule for CLAUDE.md — content should not
  describe things relevant to only some tasks (e.g., database schema details
  when the agent isn't touching the database). It's a specific, applicable
  test practitioners can run against a candidate CLAUDE.md line: "does this
  apply to every session, or only some?" If only some, it belongs in a
  progressive-disclosure doc (Claim 8), not in CLAUDE.md directly.

### Claim 7: CLAUDE.md should stay under roughly 300 lines, and HumanLayer's own root CLAUDE.md is under sixty lines
- **Evidence**: Stated numeric guideline plus a first-party concrete example
  from the author's own project.
- **Confidence**: anecdotal (single team's numbers, not a study-derived
  threshold)
- **Quote**: "At HumanLayer, our root `CLAUDE.md` file is _less than sixty
  lines_."
- **Our assessment**: The "under sixty lines" figure is not new to the corpus
  — it is repeated verbatim in the later `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 3, which cites the same fact about the same file. What's new here is
  the additional, softer upper bound of "under 300 lines" as a general
  guideline distinct from HumanLayer's own tighter internal practice — the
  post treats 300 lines as a rough ceiling and sixty lines as evidence that
  going well under that ceiling is achievable in practice, not just a
  theoretical target.

### Claim 8: Progressive Disclosure — keep CLAUDE.md itself lean and route to a separate, self-descriptive documentation directory instead of embedding all detail inline
- **Evidence**: Concrete directory-structure example (`agent_docs/` containing
  files like `building_the_project.md`, `running_tests.md`,
  `code_conventions.md`) with the recommendation that CLAUDE.md contain only a
  brief pointer list, and Claude either self-selects which docs to read or
  requests approval before reading them.
- **Confidence**: emerging (concrete, actionable pattern; single practitioner
  source, but structurally consistent with the "reference do not embed"
  skills principle documented independently in
  `blog-anthropic-maccoss-developer-onboarding.md` Claim 5)
- **Quote**: "Tell it _how to find_ important information so that it can find
  and use it, but only when it needs to."
- **Our assessment**: This is the practical resolution to the tension between
  Claim 6 (keep CLAUDE.md universally applicable) and the reality that
  projects have plenty of legitimately useful but non-universal knowledge
  (database schema, service communication patterns). Rather than omitting that
  knowledge or bloating CLAUDE.md with it, this pattern moves it into files
  loaded on demand — directly parallel to MacLean's "reference do not embed"
  skills principle, but applied one layer earlier (plain docs directory,
  before skills enter the picture at all). Teams without a skills system yet
  can adopt this pattern with nothing more than a docs folder and a pointer
  list.

### Claim 9: Documentation in the progressive-disclosure directory should prefer `file:line` references over embedded code snippets, since snippets go stale
- **Evidence**: Explicit best-practice statement warning that embedded code
  examples in agent-facing docs will drift out of sync with the actual
  codebase.
- **Confidence**: emerging (sound engineering principle, single-source
  articulation; not independently corroborated elsewhere in the corpus)
- **Quote**: "Prefer pointers to copies. Don't include code snippets in these
  files if possible - they will become out-of-date quickly. Instead, include
  `file:line` references to point Claude to the authoritative context."
- **Our assessment**: This is a novel, concrete rule not present elsewhere in
  the corpus's CLAUDE.md/docs guidance. It's the direct analogue of "don't
  duplicate documentation content in skills" (Claim 5 of the MacCoss note)
  applied to code examples specifically: a `file:line` pointer stays correct
  as the code evolves, while a pasted snippet silently rots. This is a small,
  mechanically checkable rule practitioners can apply immediately to any
  agent-facing documentation, not just CLAUDE.md itself.

### Claim 10: LLMs should not be used as linters — style and formatting enforcement should be handled by deterministic tools, not the model
- **Evidence**: Explicit warning that LLMs are comparatively expensive and
  slow versus dedicated linters/formatters, plus the observation that
  including style guidelines in context bloats the window and degrades
  instruction-following, with the recommendation to instead use actual
  linting tools and (optionally) a Claude Code Stop hook that runs formatters
  and surfaces errors back to Claude.
- **Confidence**: settled (the cost/speed comparison between an LLM call and a
  deterministic linter run is not seriously contestable; the context-bloat
  mechanism is consistent with Claim 6 and the broader corpus's "deterministic
  tools for deterministic work" tenet)
- **Quote**: "Never send an LLM to do a linter's job. LLMs are comparably
  expensive and incredibly slow."
- **Our assessment**: This is a clean, quotable articulation of a principle
  the corpus already holds implicitly (e.g., the enforcement-hierarchy ranking
  in `failure-claudemd-ignored-compaction.md`'s Guide Impact section, which
  ranks settings.json/hooks above CLAUDE.md prose for reliability) but had not
  stated specifically about code style/linting. It gives a concrete
  implementation path — Stop hooks running real formatters — that slots
  directly into the corpus's existing hooks guidance.

### Claim 11: Avoid `/init` or other auto-generation tools for CLAUDE.md; because it is one of the harness's highest-leverage points, it should be manually crafted line by line
- **Evidence**: Explicit recommendation against auto-generation, reasoned from
  CLAUDE.md's position at the start of every agent workflow — an error there
  propagates through research, planning, and implementation phases downstream.
- **Confidence**: anecdotal (a single practitioner's stated preference and
  rationale; no comparative test of auto-generated vs. hand-written CLAUDE.md
  quality is presented in this post specifically)
- **Quote**: "CLAUDE.md is one of the highest leverage points of the harness."
- **Our assessment**: This is directionally consistent with, and adds a
  mechanistic rationale to, the empirically-measured finding already in the
  corpus: `paper-gloaguen-agentsmd-effectiveness.md` found LLM-generated
  AGENTS.md files actively hurt performance while costing 20%+ more compute,
  versus a ~4% improvement for human-written files (also cited secondhand in
  the companion `skill-issue-harness-engineering.md` Claim 9). This post
  predates that framing and doesn't cite a study for this specific claim, but
  the "errors propagate downstream through every phase" rationale is a useful
  mechanistic explanation for *why* the measured gap between generated and
  hand-written files might exist, which the paper's own note does not offer.

## Concrete Artifacts

### Progressive Disclosure directory structure
```
Source: https://www.humanlayer.dev/blog/writing-a-good-claude-md

agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- service_architecture.md
  |- database_schema.md
  |- service_communication_patterns.md

CLAUDE.md contains a brief list pointing to these files; Claude either
self-selects which to read for a given task, or requests approval before
reading them.
```

### Statelessness framing (opening principle)
```
Source: https://www.humanlayer.dev/blog/writing-a-good-claude-md

"Coding agents know absolutely nothing about your codebase at the beginning
of each session. The agent must be told anything that's important to know
about your codebase each time you start a session. CLAUDE.md is the
preferred way of doing this."
```

### Instruction-count guidance
```
Source: https://www.humanlayer.dev/blog/writing-a-good-claude-md

- Frontier thinking LLMs: ~150-200 instructions followed with reasonable
  consistency (cited: arxiv.org/pdf/2507.11538)
- Claude Code's own system prompt: ~50 instructions before CLAUDE.md is
  even added
- Smaller models: exponential decay in instruction-following as count rises
- Larger frontier thinking models: linear decay in instruction-following
  as count rises
- Recommended CLAUDE.md ceiling: under ~300 lines
- HumanLayer's own root CLAUDE.md: less than 60 lines
```

## Cross-References

- **Corroborates**: `failure-claudemd-ignored-compaction.md` — Claim 3 of
  this note independently confirms the exact verbatim harness wrapper text
  ("you should not respond to this context unless it is highly relevant to
  your task") that failure-report's Lesson 1 identifies as the root cause of
  CLAUDE.md instructions being treated as advisory rather than mandatory. Two
  independent sources now quote the identical wrapper string.
- **Corroborates**: `blog-anthropic-maccoss-developer-onboarding.md` — Claim 1
  (statelessness) corroborates that note's Claim 3 ("Claude can't learn
  without you recording 'context'"); Claim 8 here (progressive disclosure via
  a docs directory) is structurally the same "reference do not embed"
  principle as that note's Claim 5, applied one layer before skills enter the
  picture.
- **Corroborates**: `blog-humanlayer-skill-issue-harness-engineering.md` — the
  "under sixty lines" HumanLayer CLAUDE.md figure (Claim 7 here) is the exact
  same fact restated verbatim in that note's Claim 3, confirming the same
  team's practice was stable across the roughly four months between the two
  posts (Nov 2025 → Mar 2026). Both posts also independently recommend
  CLAUDE.md as the first/primary harness surface to configure.
- **Extends**: `blog-humanlayer-long-context-isnt-the-answer.md` — this post
  cites the same underlying arXiv paper (arxiv.org/pdf/2507.11538) as that
  note's Claim 6, roughly four months before the "instruction budget" concept
  was named and developed in depth in that later post. This note shows the
  same author's CLAUDE.md-specific guidance (150-200 instruction ceiling,
  ~50-instruction system-prompt baseline) predates and directly feeds into the
  later, more general "instruction budget" framing — useful for tracing how
  the concept evolved from a CLAUDE.md-specific rule of thumb into a named,
  general harness-engineering principle.
- **Extends**: `paper-gloaguen-agentsmd-effectiveness.md` — Claim 11 here
  (avoid auto-generating CLAUDE.md; hand-craft it because it's the highest-
  leverage point) offers a mechanistic rationale ("errors propagate through
  every downstream phase") for that paper's empirically measured finding that
  LLM-generated AGENTS.md files hurt performance while costing more compute
  than human-written ones.
- **Novel**: (1) The explicit WHAT/WHY/HOW content framework as a named,
  three-part checklist for CLAUDE.md authors — more structured than the
  corpus's existing "lay of the land" metaphor. (2) The exponential-vs-linear
  instruction-decay distinction by model size class — no other corpus source
  distinguishes *how* degradation differs across model tiers, only that it
  occurs. (3) The `file:line`-over-code-snippets rule for progressive-
  disclosure documentation, to prevent embedded examples from going stale.
  (4) "Never send an LLM to do a linter's job" as a specific, quotable framing
  of the deterministic-tools-for-deterministic-work principle applied to code
  style enforcement.

## Guide Impact

- **Chapter 02 (Harness Engineering) — CLAUDE.md content structure**: Add the
  WHAT/WHY/HOW framework (Claim 2) as a concrete authoring checklist,
  presented alongside (not replacing) the existing "lay of the land" scope
  discipline from `blog-anthropic-maccoss-developer-onboarding.md` — the two
  are complementary: scope discipline says what NOT to include, WHAT/WHY/HOW
  says how to organize what remains.
- **Chapter 02 (Harness Engineering) — instruction budget**: Add the model-size
  degradation distinction (Claim 5: exponential decay for smaller models,
  linear for frontier models) as a refinement to whatever "instruction budget"
  guidance the guide adopts from the companion `long-context-isnt-the-answer`
  note — teams on smaller/cheaper models need a stricter CLAUDE.md line
  budget than teams on frontier models.
- **Chapter 02 (Harness Engineering) — progressive disclosure**: Add the
  `agent_docs/` directory pattern (Claim 8) and the `file:line`-over-snippets
  rule (Claim 9) as a concrete, low-effort pattern teams can adopt even before
  building a full skills system.
- **Chapter 02 (Harness Engineering) — Claude as linter**: Add "never send an
  LLM to do a linter's job" (Claim 10) as an explicit anti-pattern, with the
  Stop-hook-runs-formatters pattern as the recommended alternative — this
  slots directly next to existing hooks guidance.
- **Chapter 02 (Harness Engineering) — auto-generation warning**: Add a
  caution against `/init`-style auto-generated CLAUDE.md (Claim 11), citing
  both this post's "highest leverage point" rationale and the measured cost
  from `paper-gloaguen-agentsmd-effectiveness.md`.

## Extraction Notes

- Fetched via WebFetch (URL content converted to markdown and processed by a
  fetch-time model, which by default resists returning full verbatim text due
  to copyright caution — the first fetch attempt returned only a refusal and
  offer of a summary). All quotes in this note were obtained through multiple
  targeted follow-up fetches, each requesting specific short verbatim
  fragments (under ~25 words) for a named topic, cross-checked across fetches
  for internal consistency rather than relying on a single full-page
  summarization pass. No quote was reconstructed or paraphrased and presented
  as verbatim.
- The post links to an external arXiv paper (arxiv.org/pdf/2507.11538) for the
  150-200 instruction figure and the exponential/linear decay claim. This
  extraction did not independently re-fetch and verify the arXiv paper itself
  — the same paper is more deeply extracted and verified in
  `blog-humanlayer-long-context-isnt-the-answer.md` Claim 6, and confidence
  levels here are set consistent with that note's treatment (`emerging`, not
  `settled`) since we are relying on the secondhand citation in both posts.
- No contradiction with any existing corpus source was found. This post's
  recommendations (universally-applicable-only content, progressive
  disclosure, avoid LLM-as-linter, avoid auto-generation, keep it short) are
  consistent with and extend the existing CLAUDE.md guidance in
  `blog-anthropic-maccoss-developer-onboarding.md` and
  `failure-claudemd-ignored-compaction.md` rather than conflicting with it.
- The post's "In Conclusion" section (six numbered takeaways) restates Claims
  1-2, 6-11 in summary form and was not separately extracted as its own claim,
  since it introduces no content beyond what those claims already cover.
- `confidence_overall` is set to `emerging`: the core statelessness and
  harness-framing claims (Claims 1, 3) are settled architectural facts
  independently corroborated elsewhere in the corpus, but the instruction-
  count specifics (Claims 4-5) rest on a secondhand citation not independently
  re-verified here, and several of the most actionable recommendations
  (Claims 7, 8, 9, 11) are single-practitioner patterns without independent
  corroboration beyond this author's own later post.
