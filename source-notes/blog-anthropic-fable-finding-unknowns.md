---
source_url: https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
source_type: blog-post
title: "A field guide to Claude Fable 5: Finding your unknowns"
author: Thariq Shihipar (Anthropic, Claude Code team)
date_published: 2026-07-06
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: anecdotal
issue: "#1618"
---

# A field guide to Claude Fable 5: Finding your unknowns

> First-party Anthropic post framing "reducing and planning for your unknowns"
> as the core skill of agentic coding, and giving a named, ordered set of
> techniques — blind spot pass, brainstorms/prototypes, interviews, references,
> implementation plans, implementation notes, pitches/explainers, quizzes — for
> surfacing the gap between what you tell Claude (the map) and what the
> codebase actually requires (the territory), before/during/after implementation.

## Source Context

- **Type**: blog-post (official claude.com blog, published 2026-07-06)
- **Author credibility**: Thariq Shihipar, member of technical staff at
  Anthropic on the Claude Code team. This is the same author as
  `blog-anthropic-seeing-like-an-agent.md` (the AskUserQuestion / TodoWrite→Task
  / RAG→Grep tool-design retrospective), giving direct continuity: that post
  covers why Claude Code's elicitation tools were built the way they were,
  this post covers how a practitioner (the author himself) uses those and
  other techniques day-to-day when working with Claude Fable. First-party
  and written from the inside, not an external practitioner write-up.
- **Scope**: Covers a practitioner workflow for identifying "unknowns" before,
  during, and after implementation when working with Claude Fable 5 (the
  fast/cheap model tier), organized as a four-part unknowns taxonomy (known
  knowns, known unknowns, unknown knowns, unknown unknowns) plus eight named
  techniques mapped to project phase. Illustrated with a worked example (video
  editing for the Fable launch video, using Remotion/Whisper/ffmpeg). Does NOT
  cover multi-agent coordination, cost/pricing, model benchmarks, or specific
  CLAUDE.md/settings authoring — it is a single-practitioner, single-session
  workflow post, not an architecture or infra post.

## Extracted Claims

### Claim 1: Unknowns break into four categories — known knowns, known unknowns, unknown knowns, and unknown unknowns — and this taxonomy is the organizing frame for the whole post
- **Evidence**: Author-stated framework, presented as a working mental model
  rather than a benchmarked result.
- **Confidence**: anecdotal (single practitioner's framing, not measured, though
  the underlying "map vs. territory" metaphor is a well-known epistemics idea
  the author is applying to agentic coding specifically)
- **Quote**: "Known Knowns: This is essentially what is in my prompt." / "Known
  Unknowns: What haven't I figured out yet, but I'm aware that I haven't?" /
  "Unknown Knowns: What's so obvious I'd never write it down, but would
  recognize it if I saw it?" / "Unknown Unknowns: What haven't I considered at
  all?"
- **Our assessment**: This is a useful vocabulary more than a novel technique —
  the value is in giving each of the four quadrants a named, repeatable
  countermeasure (see Claims 2-8), rather than the taxonomy itself. Worth
  citing as the frame that ties the individual techniques together, since the
  guide currently lacks a shared vocabulary for "why do I need to
  brainstorm/interview/reference at all."

### Claim 2: The "map" is what you give Claude (prompts, skills, context); the "territory" is where the work actually has to happen (the codebase, the real world, its constraints) — and the entire practice described is about closing the gap between them
- **Evidence**: Opening framing of the post, restated at the close.
- **Confidence**: anecdotal (author's framing)
- **Quote**: "The map, a representation of the work to be done, is my prompts
  and skills and context, it's what I give Claude. The territory is where the
  work needs to happen, the codebase, the real world, its actual constraints."
- **Our assessment**: This is a useful one-line explanation for *why*
  context-engineering failures happen even with a "good" prompt: the prompt is
  never the territory, only a map of it, and the techniques in this post are
  presented as ways to check the map against the territory before, during, and
  after acting on it.

### Claim 3: To surface unknown unknowns, explicitly ask Claude to do a "blind spot pass" using those literal words, before starting unfamiliar work
- **Evidence**: Named technique with a concrete example prompt for an
  unfamiliar-codebase scenario (adding an auth provider).
- **Confidence**: anecdotal (practitioner technique, no measurement of hit rate)
- **Quote**: "In these situations, you can ask Claude to help you find your
  unknown unknowns and explain them to you. I like to use the literal words
  'blind spot pass' and 'unknown unknowns.'"
- **Our assessment**: The specificity here — using the literal phrase rather
  than a vague "anything I should know?" — is the actionable part. This maps
  cleanly onto Ch04 (context-engineering)'s territory: it's a technique for
  discovering missing context *before* burning a turn on a wrong-context
  implementation, which is cheaper than discovering the gap mid-implementation.

### Claim 4: Verbalizing unknown knowns is best done early, during brainstorming/prototyping, because discovering them during implementation is comparatively expensive
- **Evidence**: Author's cost framing, illustrated with a design-exploration
  example prompt (asking for 4 wildly different HTML design directions to
  react to, when the author has "no visual taste").
- **Confidence**: anecdotal
- **Quote**: "It's extremely valuable to identify and verbalize unknown knowns
  early during prototyping, because finding them out during implementation can
  be (relatively) expensive."
- **Our assessment**: This is the same "cost curve" logic that underlies test-
  driven development and spec review generally — catch the gap when it's a
  sketch, not when it's wired into a codebase. Novel here is applying it
  explicitly to *unknown knowns* (things the requester would recognize but
  never thought to state), not just to unknown unknowns.

### Claim 5: After brainstorming, ask Claude to interview you one question at a time, prioritized by which answers would most change the implementation
- **Evidence**: Named technique ("Interviews") with example prompt.
- **Confidence**: anecdotal
- **Quote**: "Interview me one question at a time about anything ambiguous,
  prioritize questions where my answer would change the architecture."
- **Our assessment**: The "one question at a time, prioritized by architectural
  impact" instruction is the specific, transferable part — a generic "ask me
  clarifying questions" prompt tends to produce a flat list of equally-weighted
  questions; this prompt asks the model to rank by consequence, which is a
  cheap addition worth putting directly into a reusable prompt/skill.

### Claim 6: The single best reference for clarifying an unknown is source code itself — pointing Claude at an existing implementation to reimplement its semantics elsewhere
- **Evidence**: Named technique ("References") with example prompt pointing at
  a vendored Rust crate to reimplement backoff semantics in TypeScript.
- **Confidence**: anecdotal
- **Quote**: "In this case, the best approach is a reference... the absolute
  best reference is *source code*."
- **Our assessment**: Consistent with the general "show, don't just tell"
  principle already in this corpus (e.g. giving Claude concrete examples over
  abstract prose descriptions), but sharpened to a specific claim: prefer
  reference *code* over reference *prose* when the ambiguity is about exact
  behavior/semantics rather than intent.

### Claim 7: Before implementing, ask Claude to produce an implementation plan for review, ordered to foreground the decisions the requester is most likely to want to change (data model, new type interfaces, user-facing surface)
- **Evidence**: Named technique ("Implementation Plans") with example prompt.
- **Confidence**: anecdotal
- **Quote**: "When I think I'm ready to implement, I tend to ask Claude to put
  together an implementation plan for me to review."
- **Our assessment**: The ordering instruction — lead with the parts most
  likely to be tweaked — is the transferable detail; a plan that buries the
  contestable decisions under boilerplate defeats the point of review.

### Claim 8: During implementation, have Claude maintain a running "implementation-notes.md" file logging deviations and decisions made when it hits edge cases, defaulting to the conservative option and continuing rather than stopping
- **Evidence**: Named technique ("Implementation notes") with example prompt
  and file-naming convention.
- **Confidence**: anecdotal, but directly actionable and specific (file name,
  default-to-conservative rule, explicit "Deviations" log heading)
- **Quote**: "I ask Claude Code to keep a temporary 'implementation-notes.md'
  (or .html) file where it keeps track of decisions it makes so we can learn
  for our next attempt." / "If you hit an edge case that forces you to deviate
  from the plan, pick the conservative option, log it under 'Deviations,' and
  keep going."
- **Our assessment**: This is the most concretely reusable artifact in the
  post — a specific file convention plus a specific decision policy
  (conservative-default-and-continue rather than stop-and-ask) for autonomous
  or semi-autonomous implementation runs. Directly citable for Ch02
  (harness-engineering): it's a lightweight audit trail that doesn't require
  interrupting the agent loop.

### Claim 9: After implementation, package the prototype, spec, and implementation notes into a single review artifact to accelerate reviewer buy-in, because reviewers start with the same unknowns the author started with
- **Evidence**: Named technique ("Pitches and explainers") with example prompt
  requesting a Slack-shareable doc leading with a demo GIF.
- **Confidence**: anecdotal
- **Quote**: "Building pitch and explainer artifacts in the final document
  helps: Accelerate understanding when reviewers start with the same unknowns
  you did"
- **Our assessment**: Reframes documentation-for-review as closing the
  reviewer's *own* unknowns gap, not just as a courtesy — the same map/territory
  frame applied to the reviewer's mental model rather than the implementer's.

### Claim 10: Post-implementation, ask Claude to quiz you on the change after providing full context, and only merge after passing the quiz perfectly
- **Evidence**: Named technique ("Quizzes") with example prompt and an explicit
  personal merge gate.
- **Confidence**: anecdotal (self-imposed practitioner rule, not a team policy
  or measured outcome)
- **Quote**: "Asking Claude to quiz me about the change after giving me a bunch
  of context helps me understand what happens. I only merge after I pass the
  quiz perfectly."
- **Our assessment**: This is a comprehension-verification gate distinct from
  code review or test suites — it verifies the *human's* understanding of a
  change the AI wrote, which is a different failure mode than "does the code
  work" (covered by Ch03/verification's existing test-based content). Worth
  flagging as a complementary practice: tests verify the code is correct;
  the quiz verifies the human reviewer actually understands what shipped.

### Claim 11: Claude Fable 5 is characterized as the first model where the author's own work quality is bottlenecked by his ability to clarify its unknowns, rather than by the model's raw capability
- **Evidence**: Author's direct first-person claim about working with Fable
  specifically, not stated as a benchmarked comparison to other model tiers.
- **Confidence**: anecdotal (single author's subjective assessment, no
  benchmark or comparative data given)
- **Quote**: "Claude Fable is the first model where I find the quality of the
  work is bottlenecked by my ability to clarify its unknowns."
- **Our assessment**: This is the article's stated reason for tying the
  "unknowns" practice specifically to Fable 5, but the post does not actually
  argue Fable is uniquely suited to this workflow for cost/speed/iteration
  reasons — the Prospector's triage comments speculated about a Fable-specific
  cost/speed rationale, but no such claim exists in the source. The techniques
  described are general agentic-coding practices; the Fable framing is really
  "here's what surfaces once the model stops being the bottleneck," not a
  claim that Fable requires or specially rewards this workflow. Guide citations
  should attribute these techniques to Claude Code practice generally, not to
  Fable's model characteristics specifically.

### Claim 12: The unifying thesis is that reducing and planning for unknowns is itself a learnable, improvable skill of agentic coding, not an inherent trait some coders have and others don't
- **Evidence**: Direct authorial claim bridging the whole post; reinforced by
  a closing call to action.
- **Confidence**: anecdotal
- **Quote**: "In many ways, reducing and planning for your unknowns is the
  **skill** of agentic coding." / "Every explainer, brainstorm, interview,
  prototype, and reference is a cheap way to find out what you didn't know
  before it gets expensive to fix. So start your next project by asking Claude
  to help you find your unknowns."
- **Our assessment**: This is the framing claim that would anchor a guide
  section, if one is added: it argues the eight techniques above are drills for
  a single underlying skill, rather than a checklist to apply mechanically.
  Consistent with this corpus's general stance that agentic-coding proficiency
  is trainable practitioner skill, not just tool configuration.

## Concrete Artifacts

Example prompts, quoted verbatim from the post, one per named technique:

```
Blind spot pass (unfamiliar codebase, pre-implementation):
"I'm working on adding a new auth provider but I know nothing about the auth
modules in this codebase. Can you do a blind spot pass to help me figure out
my relevant unknown unknowns and help me prompt you better."

Brainstorms and prototypes (surfacing unknown knowns, pre-implementation):
"I want a dashboard for this data but I have no visual taste and don't know
what's possible. Make me an HTML page with 4 wildly different design
directions so I can react to them."

Interviews (pre-implementation):
"Interview me one question at a time about anything ambiguous, prioritize
questions where my answer would change the architecture."

References (pre-implementation, pointing at source code):
"This Rust crate in vendor/rate-limiter implements the exact backoff behavior
I want. Read it and reimplement the same semantics in our TypeScript API
client."

Implementation plans (pre-implementation, review gate):
"Write an implementation plan in HTML, but lead with the decisions I'm most
likely to tweak with: data model changes, new type interfaces, and anything
user-facing."

Implementation notes (during implementation, running decision log):
"Keep an implementation-notes.md file. If you hit an edge case that forces
you to deviate from the plan, pick the conservative option, log it under
'Deviations', and keep going."

Pitches and explainers (post-implementation, reviewer buy-in):
"Package the prototype, the spec, and the implementation notes into a single
doc I can drop in Slack to get buy-in. Lead with the demo GIF."

Quizzes (post-implementation, comprehension gate before merge):
"I want to make sure I understand everything that's happened in this change.
Give me a HTML report on the changes for me to read and understand with
context, intuition, what was done, etc. and a quiz at the bottom on the
changes that I must pass."
```

Section structure of the post, in order (for anyone following up to
re-extract or verify quotes against source): Knowing your unknowns → Help
Claude help you → Pre-implementation (Blind Spot Pass, Brainstorms and
prototypes, Interviews, References, Implementation Plans) → During
implementation (Implementation notes) → Post implementation (Pitches and
explainers, Quizzes) → How this comes together: launching Fable → Matching
the Map and Territory.

## Cross-References

- **Corroborates**: `blog-anthropic-seeing-like-an-agent.md` — same author
  (Thariq Shihipar); that post's "see like an agent" principle (match tool
  granularity to model ability) and this post's "unknowns" framework are
  complementary halves of the same worldview: design tools around how the
  model actually perceives the task (that post), then use techniques to close
  the gap between what you told the model and what the task actually needs
  (this post).
- **Corroborates**: `blog-kentbeck-jessicakerr-learning-system.md` (Claim 11) —
  independent convergence on a comprehension-gated merge. That note's Claim 11
  reports Kent Beck proposing "a PR-merge learning gate — a multiple-choice
  quiz on what the developer should have learned from the change, which blocks
  merge if the developer fails it," with Jessica Kerr naming a real existing
  analogue (a Claude plugin by Dr. Nicole Forsgren). This is substantively the
  same pattern as this note's Claim 10 (ask Claude to quiz you on the change
  and only merge after passing the quiz). Two independent practitioner sources
  landing on the same quiz-before-merge comprehension gate strengthens the case
  for citing it as an emerging pattern — though both notes independently grade
  the pattern `anecdotal`, so the convergence itself is the signal, not any
  measured validation.
- **Contradicts**: None identified. No existing source note makes a
  conflicting claim about pre/during/post-implementation unknown-surfacing
  practices.
- **Extends**: `blog-simonwillison-datasette-agent-askuser.md` — that note
  covers the `ask_user()` API mechanism (a tool-level primitive for an agent
  to pause and ask the human a question mid-execution). This post covers the
  human-initiated inverse: prompts the *human* sends to Claude to surface the
  human's own unknowns before/during/after implementation. Different
  direction of the same "surface unknowns via structured question-asking"
  idea — one is agent-asks-human, the other is human-asks-agent-to-interview-
  human.
- **Novel**: The four-part unknowns taxonomy (known knowns/known unknowns/
  unknown knowns/unknown unknowns) applied specifically to agentic coding is
  new to this corpus, as is the concrete "implementation-notes.md" convention
  with a conservative-default-and-log deviation policy, and the "quiz before
  merge" comprehension gate. No existing source note names these specific
  artifacts or policies.

## Guide Impact

- **Chapter 04 (context-engineering)**: Add the map/territory framing (Claim 2)
  and the "blind spot pass" technique (Claim 3) as a named pre-implementation
  practice for surfacing missing context before prompting for an implementation
  — currently the chapter lacks a concrete phrase/ritual for this; "blind spot
  pass" is specific enough to recommend verbatim.
- **Chapter 01 (daily-workflows)**: Add the brainstorm/interview/reference
  sequence (Claims 4-6) as an ordered pre-implementation workflow, with the
  example prompts in Concrete Artifacts above as copy-pasteable starting
  points, and the "quiz before merge" gate (Claim 10) as a post-implementation
  comprehension check distinct from code review.
- **Chapter 02 (harness-engineering)**: Add the `implementation-notes.md`
  convention (Claim 8) as a lightweight, non-interrupting audit-trail pattern
  for semi-autonomous implementation runs — conservative-default-and-log
  rather than stop-and-ask keeps the agent loop moving while preserving a
  decision record.
- **Chapter 03 (verification)**: Add the "quiz" post-implementation gate
  (Claim 10) as a human-comprehension verification step, distinct from and
  complementary to the test-based verification already covered — note this
  verifies reviewer understanding, not code correctness.

## Extraction Notes

Read the full post via WebFetch in three passes: a full-content pass, a
targeted quote-extraction pass per named technique, and a follow-up pass to
verify the opening/closing paragraphs, section-heading order, the Fable-
specific claim, and the Remotion/Whisper/ffmpeg worked example context. All
quotes above were checked against these passes rather than reconstructed from
summary. The post's own launch-video worked example (Remotion/Whisper/ffmpeg)
is mentioned in Source Context/Claim 11 discussion but not extracted as a
separate numbered claim, since it is illustrative of the techniques already
captured in Claims 3-10 rather than a distinct claim. No sub-pages were
linked from the post that warranted following. The Prospector's triage
comments (see issue #1618) speculated Fable was chosen for cost/speed/
iteration reasons specific to a fast model — I did not find that claim in the
source itself (see Claim 11's assessment) and did not fabricate one to match
the triage framing.
