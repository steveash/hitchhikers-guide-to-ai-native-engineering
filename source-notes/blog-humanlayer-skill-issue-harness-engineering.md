---
source_url: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
source_type: blog-post
title: "Skill Issue: Harness Engineering for Coding Agents"
author: "Kyle (HumanLayer)"
date_published: 2026-03-12
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1823"
---

# Skill Issue: Harness Engineering for Coding Agents

> HumanLayer's practitioner framework for harness engineering — defining "coding
> agent = AI model(s) + harness," ordering the configuration surfaces by ROI
> (CLAUDE.md/AGENTS.md → MCP servers → skills → sub-agents → hooks →
> back-pressure), and arguing that most agent failures attributed to "the model"
> are actually configuration problems. Introduces the "instruction budget" concept
> later expanded in a companion post (see `blog-humanlayer-long-context-isnt-the-answer.md`).

## Source Context

- **Type**: blog-post (practitioner production experience from an agentic
  coding-tools company)
- **Author credibility**: Kyle, writing for HumanLayer (@0xblacklight on
  Twitter/X), a company building agentic coding / human-in-the-loop tooling.
  This is first-party practitioner synthesis grounded in HumanLayer's own
  production configuration decisions (their Linear CLI wrapper, their CLAUDE.md
  length, their sub-agent experiments), not a controlled study. The post cites
  external research to back specific sub-claims: Chroma's context-rot research,
  the ETH Zurich AGENTS.md study (already in the corpus as
  `paper-gloaguen-agentsmd-effectiveness.md`), Terminal Bench 2.0, and "Viv"
  (Vivek Trivedy of LangChain, whose LangChain post is already in the corpus as
  `blog-langchain-better-harness-evals.md`) — giving the practitioner narrative
  real external grounding rather than pure anecdote.
- **Scope**: Covers the taxonomy of harness configuration surfaces (CLAUDE.md/
  AGENTS.md, MCP servers, skills, sub-agents, hooks, back-pressure), the
  recommended ordering/ROI sequence for configuring them, the "too many tools"
  failure mode, sub-agents as context isolation (not specialization), the
  security risk of installing third-party skills, and the "harness engineering
  as a subset of context engineering" conceptual hierarchy. Does NOT cover:
  the "instruction budget" concept in depth (that is developed further in the
  companion post, `blog-humanlayer-long-context-isnt-the-answer.md`, which this
  article is cited as the origin of), specific benchmark methodology for the
  Terminal Bench 2.0 ranking claim (that is attributed secondhand to "Viv"), or
  a step-by-step implementation guide for any single surface.

## Extracted Claims

### Claim 1: A coding agent is defined as "AI model(s) + harness," and most failures attributed to the model are actually harness/configuration problems

- **Evidence**: Framing claim stated as the article's organizing thesis, backed
  by a first-party list of observed failure modes over a year of production use.
- **Confidence**: emerging
- **Quote**: "coding agent = AI model(s) + harness"
- **Our assessment**: This is the conceptual anchor for the entire post and, per
  the Prospector's triage, the intended anchor for the guide's harness engineering
  framing. It reframes "the agent did something dumb" from a model-capability
  question into a configuration-surface question. The companion recurring-failure
  list ("ignoring instructions, executing dangerous commands un-prompted, and
  going in circles on the simplest of tasks") gives this thesis a concrete
  failure inventory rather than leaving it abstract.

### Claim 2: CLAUDE.md/AGENTS.md should be the first harness configuration surface touched, because it is deterministically injected into the system prompt at no marginal cost

- **Evidence**: Explicit sequencing recommendation with a mechanism-based
  rationale (deterministic injection vs. the conditional/probabilistic activation
  of other surfaces).
- **Confidence**: emerging
- **Quote**: "Before touching any other harness configuration points, it's
  usually worth customizing your CLAUDE.md / AGENTS.md files."
- **Our assessment**: This gives a concrete tactical ordering — not just "CLAUDE.md
  matters" (already well-established in the corpus, e.g.
  `blog-anthropic-founders-playbook.md` Claim 7, `blog-anthropic-large-codebase-best-practices.md`
  Claim 6) but "configure it before anything else, because it's guaranteed to be
  read." This is a genuinely new sequencing argument not present in either of
  those corroborating notes, which describe CLAUDE.md's content and structure but
  not its priority relative to MCP servers, skills, sub-agents, hooks, and
  back-pressure as a set.

### Claim 3: HumanLayer's CLAUDE.md is kept under 60 lines

- **Evidence**: First-party stated fact about their own configuration.
- **Confidence**: anecdotal
- **Quote**: "Our CLAUDE.md is under 60 lines."
- **Our assessment**: A concrete, checkable number that corroborates
  `blog-anthropic-large-codebase-best-practices.md` Claim 6 ("lean and layered"
  CLAUDE.md) and the compaction-drop failure mode documented in
  `failure-claudemd-ignored-compaction.md` — long CLAUDE.md files risk being
  marked "may or may not be relevant" and dropped. HumanLayer's number gives
  practitioners a concrete target rather than the qualitative "lean" guidance
  alone. Note this is a single team's number, not a study-derived threshold — treat
  it as an anecdotal data point, not a rule.

### Claim 4: MCP servers should be used only for capabilities the model has not already learned from CLI tools during training — not as a default integration mechanism

- **Evidence**: Explicit decision rule with a worked example (GitHub, Docker,
  most databases) and a concrete counter-example (their custom Linear CLI
  wrapper replacing the Linear MCP server).
- **Confidence**: emerging
- **Quote**: "For things like GitHub, Docker, or most databases, your coding
  agent can just use the right CLIs and shell commands. The model has seen these
  tools enough during training that it already knows how to use them."
- **Our assessment**: This is a concrete, actionable decision rule ("is this tool
  well-represented in training data? if yes, prefer CLI") that is more specific
  than generic "avoid tool sprawl" advice. It's the practical complement to
  Claim 5 (too many tools is bad): this claim tells you *which* integrations to
  avoid converting to MCP servers in the first place, rather than just warning
  about the aggregate effect. The worked example — replacing the Linear MCP
  server with a small CLI wrapper documented via six examples in CLAUDE.md,
  saving "thousands of tokens from the MCP server's tool definitions" — is a
  reusable pattern, not just a claim.

### Claim 5: Connecting too many MCP tools fills the context window with tool descriptions, degrading agent performance ("the dumb zone"), and every irrelevant tool description costs reasoning tokens even without being used

- **Evidence**: Mechanism claim (context window fills with tool descriptions)
  plus an "instruction budget" citation (linking to an external explainer) plus
  reference to Anthropic's MCP tool-search feature as the vendor-side mitigation.
- **Confidence**: emerging
- **Quote**: "plug too many MCP tools into your agent, and the context window
  fills up with tool descriptions, pushing you into [the dumb zone] much faster"
- **Our assessment**: The mechanism is plausible and consistent with the
  ETH Zurich reasoning-token findings (Claim 9 below): irrelevant instructions
  measurably cost reasoning tokens without a corresponding benefit. The article
  does not define "dumb zone" inline — it links out to a companion video — so
  treat the term as a label for a described phenomenon (context saturation
  degrading performance) rather than a rigorously defined threshold. The
  companion citation, "every irrelevant tool description is an instruction the
  agent has to process without any benefit," extends the instruction-budget
  framing from tool descriptions specifically, which was not the focus of the
  companion long-context post (that post is about instructions generally).

### Claim 6: Sub-agents work as a "context firewall" for isolating discrete tasks in separate context windows, but role-based specialization (frontend/backend/data-analyst sub-agents) does not work

- **Evidence**: First-party negative experiment report ("We tried... It doesn't
  work") contrasted with a positive framing for the isolation use case.
- **Confidence**: anecdotal
- **Quote**: "We tried the 'frontend engineer' sub-agent and 'backend engineer'
  sub-agent and 'data analyst' sub-agent thing. It doesn't work. What does work
  is using sub-agents for context control."
- **Our assessment**: This is a specific, falsifiable negative claim (role-based
  specialization failed for this team) that sits in tension with — but does not
  cleanly contradict — `blog-addyosmani-code-agent-orchestra.md` Claim 4, which
  describes Claude Code's "Agent Teams" experimental feature enabling
  peer-to-peer coordination through role-like teammates (e.g., "backend," based
  on the shared-task-list example). We are not filing this as a formal
  contradiction per MINER.md §4a: Osmani's own note explicitly caveats Claim 4 as
  "a vendor feature description, not a practitioner experience report... we have
  no independent verification of its effectiveness" — it does not rise to a
  competing claim of the same evidentiary weight, so this reads as HumanLayer
  supplying the negative practitioner data point that Osmani's note says is
  missing, not as two sources asserting opposite conclusions with comparable
  confidence. The "context firewall" framing itself — isolation for noise
  containment, not role specialization — is the more load-bearing and reusable
  claim here.

### Claim 7: Hooks are user-defined commands/scripts automatically executed at points in the agent's lifecycle, used for deterministic control flow

- **Evidence**: Definitional statement, presented as the harness surface for
  guaranteed (non-probabilistic) execution.
- **Confidence**: emerging
- **Quote**: "Hooks are user-defined commands or scripts that are automatically
  executed when certain events occur and at various points of the agent's
  lifecycle."
- **Our assessment**: This is a plain definitional claim rather than a novel
  finding, but it matters for the ordering argument (Claim 1/2): hooks are
  positioned as the deterministic-execution complement to the probabilistic
  CLAUDE.md/skills/MCP surfaces — the harness's answer to "how do I guarantee
  this step happens" rather than "how do I make the model more likely to do
  this." This corroborates the general "deterministic tools for deterministic
  work" tenet already present in the corpus (see cross-references in
  `paper-gloaguen-agentsmd-effectiveness.md`'s Guide Impact section).

### Claim 8: Success with a coding agent is strongly correlated with the agent's ability to verify its own work, and context-window flooding from raw verification output (e.g., full test suite runs) itself becomes a failure mode

- **Evidence**: Stated correlation claim plus a first-party concrete failure
  anecdote about running the full test suite after every change.
- **Confidence**: anecdotal
- **Quote**: "The core insight is that your likelihood of successfully solving a
  problem with a coding agent is strongly correlated with the agent's ability to
  verify its own work."
- **Our assessment**: The correlation claim itself is asserted, not measured —
  no effect size or comparison group is given, so treat it as a strong
  practitioner belief rather than a tested finding. The supporting anecdote is
  more concrete and useful: "early on we had our agent run the full test suite
  after every change, and 4,000 lines of passing tests would flood the context
  window. The agent would then lose track of the actual task and start
  hallucinating about test files it had just read." This is a specific, checkable
  failure symptom (context flooding from verification output causing task
  confusion and hallucination) that motivates "back-pressure" as a distinct
  harness surface — verification needs to be summarized/filtered, not dumped
  raw into context. This corroborates the general context-as-budget principle
  already present via `paper-gloaguen-agentsmd-effectiveness.md` (reasoning
  token overhead from irrelevant content) but applies it specifically to
  verification/test output rather than context files.

### Claim 9: LLM-generated AGENTS.md files hurt performance while costing 20%+ more; human-written ones help ~4%; agents spend 14-22% more reasoning tokens processing context-file instructions (secondhand ETH Zurich citation)

- **Evidence**: Secondhand citation of the ETH Zurich study, already in the
  corpus as `paper-gloaguen-agentsmd-effectiveness.md`.
- **Confidence**: emerging
- **Quote**: "human-written ones only helped about 4%." / "Agents spent 14-22%
  more reasoning tokens processing context file instructions" / "LLM-generated
  ones actually _hurt_ performance while costing 20%+ more"
- **Our assessment**: This is a secondhand summary of findings already extracted
  directly from the primary paper in `paper-gloaguen-agentsmd-effectiveness.md`
  (Claims 1, 2, 3, 8). Cross-checking: the primary paper's Claim 2 gives "~4% on
  average" improvement for developer-written files on AGENTbench — matches this
  post's "~4%" figure. The primary paper's Claim 3 gives cost increases of "20%
  increase on average" (SWE-bench Lite) and "23% increase on average"
  (AGENTbench) — roughly matches this post's "20%+." The primary paper's Claim 8
  gives reasoning-token increases of "+22% reasoning tokens on SWE-Bench, +14%
  on AGENTbench" for GPT-5.2 — this post's "14-22%" range matches those two
  endpoints exactly. Per the primary source note's own Guide Impact section,
  these headline numbers should carry `emerging`, not `settled`, confidence
  (arXiv preprint, no reported significance tests on the headline percentages,
  high per-repository variance). This post does not add new data beyond the
  primary paper — it is included here because it demonstrates the claim is now
  independently propagating through the practitioner community as settled
  wisdom, which is itself worth noting, but the guide should cite the primary
  paper note directly rather than this secondhand mention.

### Claim 10: Models can be over-fitted to their post-training harness — Opus 4.6 ranked #33 in Claude Code on Terminal Bench 2.0 but #5 in a different harness not seen during post-training

- **Evidence**: Secondhand citation attributed to "Viv" (Vivek Trivedy of
  LangChain — see `blog-langchain-better-harness-evals.md`), citing Terminal
  Bench 2.0 results.
- **Confidence**: anecdotal
- **Quote**: "Opus 4.6 in Claude Code comes in position #33, but when placed in
  a different harness...it comes in at #5 (+/- about 4 positions in either
  direction)."
- **Our assessment**: This is a striking claim (a 28-position ranking swing for
  the same underlying model, driven purely by harness choice) but it is a
  secondhand attribution with no methodology given in this post — we were not
  able to verify the ranking numbers against `blog-langchain-better-harness-evals.md`
  directly, as that source note's extraction does not include a Terminal Bench
  2.0 ranking claim among its numbered claims (it covers Better-Harness's
  eval-driven optimization methodology, not model leaderboard rankings). This
  may mean "Viv" made this specific ranking observation somewhere not captured
  in that source note's extraction (e.g., a talk, a different post, or social
  media), or it may be a different "Viv." We cannot confirm this citation chain
  independently and flag it here as an unverified secondhand claim rather than
  treating the ranking numbers as corroborated. The underlying mechanism claim
  (post-training can overfit a model to its training-time harness, and a
  differently-configured harness can outperform the "native" one) is directionally
  consistent with the "harness matters more than raw model choice" thesis running
  through this whole post, but the specific #33 → #5 numbers should be treated
  as anecdotal pending independent verification.

### Claim 11: Harness engineering is a subset of context engineering, which is a superset of prompt engineering — skills, MCP servers, sub-agents, hooks, and back-pressure are all tactical solutions within that hierarchy

- **Evidence**: Explicit conceptual-hierarchy statement tying the whole post's
  taxonomy together.
- **Confidence**: emerging
- **Quote**: "Harness engineering then is the subset of context engineering
  which primarily involves leveraging harness configuration points to carefully
  manage the context windows of coding agents."
- **Our assessment**: This is the organizing frame the Prospector flagged as the
  chapter anchor. It explicitly subordinates prompt engineering (least
  important, in this framing) to context engineering (most important), with
  harness engineering as the practical, configurable subset of context
  engineering. This is a cleaner nesting than most of the corpus offers — other
  sources treat "context engineering," "harness engineering," and "prompt
  engineering" as roughly parallel concerns rather than explicitly nested ones.
  Guide chapters organized around "prompting tips" as a primary lever would be
  contradicted by this framing, which treats prompting as the least-leveraged
  layer.

### Claim 12: Skills carry a real security risk comparable to installing an unvetted npm package, because skill registries have distributed malicious skills that can execute arbitrary code

- **Evidence**: Explicit security warning with a direct analogy to dependency
  installation risk.
- **Confidence**: settled (the analogy/mechanism — skills execute code with the
  installing agent's privileges — is a straightforward security fact; the claim
  that malicious skills have already been distributed "in the hundreds" per the
  Prospector's triage framing is not independently verified in what we could
  extract from this article's text)
- **Quote**: "Treat skills like you'd treat `npm install random-package` — read
  what you're installing."
- **Our assessment**: This is a genuinely new, practically important warning for
  the corpus — no other source note we cross-checked frames Skills specifically
  as a supply-chain/dependency-style risk requiring the same scrutiny as
  installing a third-party package. This should be a first-class warning
  wherever the guide recommends adopting Skills as a harness surface, not a
  footnote. It pairs naturally with the corpus's existing emphasis on
  deterministic, auditable tooling (see `paper-gloaguen-agentsmd-effectiveness.md`
  Guide Impact section) — an unaudited skill is the opposite of a deterministic,
  reviewed harness component.

### Claim 13: Chroma's context-rot research provides empirical backing that models perform worse at longer context lengths

- **Evidence**: External citation to Chroma's published context-rot research,
  used to justify the emphasis on context management throughout the post.
- **Confidence**: emerging (external citation, not independently re-verified by
  this extraction — the underlying Chroma research was not separately fetched)
- **Quote**: "Chroma's [context rot research](https://research.trychroma.com/context-rot)
  provides empirical backing to what we've been saying for a long time: models
  perform worse at longer context lengths."
- **Our assessment**: This citation is the connective tissue between this post
  and its companion, `blog-humanlayer-long-context-isnt-the-answer.md`, which
  makes the same "longer context degrades performance, independent of window
  size" argument in much greater depth (with the "instruction budget" concept).
  This post cites Chroma's research as background support for the general
  context-degradation claim; the companion post is where HumanLayer's own
  production evidence for the specific mechanism lives. We have not independently
  fetched the Chroma research itself — if it becomes relevant to cite directly
  (rather than through this or the companion HumanLayer post), it should be
  separately mined.

## Concrete Artifacts

### Recommended harness configuration ordering (article's section sequence, doubling as a de facto priority ordering per Claim 2)

```
Source: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents

1. CLAUDE.md & AGENTS.md   — deterministic, injected into every session, first
2. MCP Servers              — for tools/capabilities not well-represented in training data
3. Skills                   — progressive disclosure of reusable knowledge/tools
4. Sub-Agents                — context control (isolation), not role specialization
5. Hooks                    — deterministic control flow at lifecycle events
6. Back-Pressure             — verification signal, filtered/summarized to avoid context flooding
```

### Linear CLI wrapper (MCP → CLI replacement pattern)

```
Source: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents

HumanLayer replaced the Linear MCP server with a small custom CLI wrapper,
documented via six example usages directly in CLAUDE.md.

"This saved us thousands of tokens from the MCP server's tool definitions
that were ending up in our agent's system prompt."
```

### Verification-flooding failure anecdote

```
Source: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents

"early on we had our agent run the full test suite after every change, and
4,000 lines of passing tests would flood the context window. The agent would
then lose track of the actual task and start hallucinating about test files
it had just read."
```

### Closing thesis (verbatim)

```
Source: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents

"The next time your coding agent isn't performing the way you expect, before
you blame the model, check the harness. Agentfiles, MCP servers, skills,
sub-agents, hooks, and back-pressure — that's where we've found most of the
leverage. The model is probably fine. It's just a skill issue."
```

### Article section structure (for navigation / re-reading)

```
1. Harness Engineering (title/intro)
2. ... as a Subset of Context Engineering
3. Engineering Your Harness
4. CLAUDE.md & AGENTS.md
5. MCP Servers Are for Tools
6. Skills Are for Reusable Knowledge (and Tools)
7. Sub-Agents Are for Context Control
8. Hooks Are for Control Flow
9. Back-Pressure Increases Your Chances of Success
10. Closing Notes
```

## Cross-References

- **Corroborates**: `paper-gloaguen-agentsmd-effectiveness.md` (Claims 1, 2, 3,
  8) — this post's secondhand ETH Zurich figures (~4% help for human-written
  files, 20%+ cost increase, 14-22% reasoning token overhead) match the primary
  paper's numbers closely (see Claim 9 above for the exact reconciliation). The
  guide should cite the primary paper note, not this secondhand mention, per
  that note's own Guide Impact recommendation to prefer primary sources.
- **Corroborates**: `blog-anthropic-large-codebase-best-practices.md` (Claim 6:
  lean/layered CLAUDE.md; Claim 5: the seven-extension-point harness taxonomy) —
  this post's five-plus-one surface list (CLAUDE.md/AGENTS.md, MCP, skills,
  sub-agents, hooks, back-pressure) substantially overlaps with Anthropic's
  first-party seven-point taxonomy (CLAUDE.md, hooks, skills, plugins, MCP
  servers, LSP integrations, subagents). This post adds "back-pressure" as a
  named surface not present in Anthropic's taxonomy, and omits "plugins" and
  "LSP integrations." Both sources independently converge on CLAUDE.md-first
  and lean/layered configuration as the starting point.
- **Corroborates**: `blog-anthropic-founders-playbook.md` (Claim 7: CLAUDE.md as
  first artifact) — both sources agree CLAUDE.md should be established early/
  first, though the playbook frames this as "before any production code," while
  this post frames it as "before touching any other harness configuration
  point" — a slightly different but compatible sequencing claim.
- **Extends**: `blog-humanlayer-long-context-isnt-the-answer.md` — that
  companion post (same author, same site, published ~11 days later) explicitly
  identifies this article as the origin of the "instruction budget" concept
  ("We've written about the concept of the instruction budget before") and
  develops it in much greater depth with a concrete production anecdote (Opus
  4.6 reversion) and a specific 100k-token context-warning threshold. This post
  only gestures at the concept via the "dumb zone" link and the "every
  irrelevant tool description is an instruction the agent has to process
  without any benefit" framing; the companion post is where the concept is
  actually defined and tested.
- **Extends**: `blog-langchain-better-harness-evals.md` — this post cites "Viv"
  (Vivek Trivedy, that note's author) for the Terminal Bench 2.0 ranking claim
  (Claim 10 above), but we could not locate a matching claim about model-ranking
  shifts in that source note's own numbered claims — that note documents
  LangChain's eval-driven harness-optimization methodology (Better-Harness), not
  benchmark leaderboard rankings. Treat the "Viv" attribution as unverified
  against our corpus pending a direct check of the cited talk/post; the two
  sources share only the general "harness configuration matters more than raw
  model capability" thesis, not a specific verified data point.
- **Novel**: (1) The explicit CLAUDE.md-first sequencing rationale (deterministic
  injection vs. probabilistic activation of other surfaces) — no prior corpus
  source frames the *order* in which to configure harness surfaces, only what
  each surface should contain. (2) "Back-pressure" as a named, distinct harness
  surface for filtering/summarizing verification output — no prior corpus source
  names this as a configuration surface on par with CLAUDE.md/MCP/skills/sub-agents/hooks.
  (3) The MCP-vs-CLI decision rule based on training-data representation ("is
  this tool well-represented enough that the model already knows how to drive
  it via CLI?") as an explicit, actionable filter for MCP adoption decisions.
  (4) Skills-as-supply-chain-risk (`npm install random-package` analogy) — no
  other corpus source frames Skill adoption as a dependency-security decision.
  (5) The verification-flooding anecdote (4,000 lines of test output causing
  task-confusion hallucination) as a concrete, named failure mode distinct from
  the generic "context window fills up" framing found elsewhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the "coding agent = model + harness"
  framing (Claim 1) as the chapter's opening definitional anchor, and the
  CLAUDE.md-first sequencing argument (Claim 2) as the recommended order of
  operations when a team is setting up harness configuration for the first
  time: CLAUDE.md/AGENTS.md → MCP servers → skills → sub-agents → hooks →
  back-pressure. This gives practitioners a concrete "start here" answer that
  the corpus currently lacks (existing sources describe what each surface
  should contain, not the order to configure them in).

- **Chapter 02 (Harness Engineering) — MCP decision rule**: Add the "is this
  tool well-represented in training data?" filter (Claim 4) as the explicit
  test for whether to build an MCP server vs. rely on CLI/shell access, with
  the Linear CLI wrapper as a worked example. This is more actionable than
  generic "avoid tool sprawl" guidance already in the corpus.

- **Chapter 02 (Harness Engineering) — Skills security**: Add the
  skills-as-dependencies warning (Claim 12) as a first-class caution in any
  section recommending Skill adoption. No prior corpus source treats Skills as
  a supply-chain risk; this should be added alongside — not subordinate to —
  the progressive-disclosure benefits of Skills.

- **Chapter 02 (Harness Engineering) — sub-agent guidance**: Add "context
  isolation, not role specialization" (Claim 6) as the recommended sub-agent
  design principle, with a note that Claude Code's Agent Teams feature
  (`blog-addyosmani-code-agent-orchestra.md` Claim 4) enables role-like
  coordination but has no independent verification of effectiveness — the guide
  should present isolation-for-noise-containment as the validated pattern and
  role-based specialization as unproven/contested.

- **Chapter 03 (Safety and Verification) or Chapter 02**: Add "back-pressure"
  (Claim 8) as a named harness surface: verification output (test results,
  lint output) must be filtered/summarized before re-entering context, not
  dumped raw. Cite the 4,000-line test-output flooding anecdote as the concrete
  failure mode this practice prevents.

- **Chapter 04 (Context Engineering)**: Add the context-engineering hierarchy
  (Claim 11: prompt engineering ⊂ context engineering ⊃ harness engineering) as
  the chapter's organizing frame, explicitly de-emphasizing prompt-wording
  advice relative to structural/tooling advice. Cross-reference the ETH Zurich
  reasoning-token findings (Claim 9, citing `paper-gloaguen-agentsmd-effectiveness.md`
  directly) as supporting evidence for why irrelevant context/tool descriptions
  cost real compute even when not directly used (Claim 5).

## Extraction Notes

- Fetched via WebFetch (URL content converted to markdown and processed by a
  fetch-time model, which by default resists returning full verbatim text due
  to copyright caution). All quotes in this note were obtained through multiple
  targeted fetches, each requesting specific short (<125 character) verbatim
  fragments for a named topic, cross-checked for consistency across fetches
  rather than relying on a single full-page summarization pass. No quote was
  reconstructed or paraphrased and presented as verbatim.
- The "dumb zone" / "smart zone" terminology is referenced via an external video
  link in the source article rather than defined inline; per MINER.md §2a, no
  quote was fabricated for a definition that doesn't exist in the article text
  — Claim 5's assessment flags this explicitly.
- Claim 10 (Terminal Bench 2.0 / Opus 4.6 ranking, attributed to "Viv") could
  not be corroborated against the specific numbered claims in
  `blog-langchain-better-harness-evals.md` — that note's extraction does not
  include a matching ranking claim. Rather than assert a false cross-reference,
  this is flagged as an unverified secondhand attribution in both Claim 10 and
  the Cross-References section, per MINER.md §4b.
- Checked for a contradiction between this post's sub-agent-specialization
  claim (Claim 6) and `blog-addyosmani-code-agent-orchestra.md` Claim 4 (Agent
  Teams feature description). Concluded this does not meet the bar for a filed
  contradiction under MINER.md §4a, because Osmani's own note already caveats
  that claim as an unverified vendor feature description rather than a
  practitioner finding — see Claim 6's "Our assessment" for the full reasoning.
  No contradiction issue was filed.
- This is the earlier of two related HumanLayer posts in the corpus; the later
  companion post (`blog-humanlayer-long-context-isnt-the-answer.md`, issue
  #1822) was mined first and already cross-links back to this one. Both notes
  now cross-reference each other.
- Confidence set to `emerging`: strong first-party production grounding for the
  configuration-surface taxonomy and sequencing claims, but several individual
  sub-claims are anecdotal (single-team CLAUDE.md line count, sub-agent
  specialization experiment) or unverified secondhand citations (Terminal Bench
  2.0 ranking, Chroma context-rot research not independently re-fetched).
