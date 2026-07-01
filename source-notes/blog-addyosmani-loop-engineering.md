---
source_url: https://addyosmani.com/blog/loop-engineering/
source_type: blog-post
title: "Loop Engineering"
author: Addy Osmani
date_published: 2026-06-07
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: emerging
issue: "#1388"
---

# Loop Engineering

> Osmani names "loop engineering" -- designing a system that prompts agents on
> your behalf instead of prompting them yourself -- and decomposes it into five
> shipped product primitives (automations, worktrees, skills, plugins/connectors,
> sub-agents) plus a sixth, external memory, mapping each one directly onto both
> the Codex app and Claude Code.

## Source Context

- **Type**: blog-post (personal blog, addyosmani.com; ~1,700 words; published
  June 7, 2026)
- **Author credibility**: Addy Osmani is a Google Chrome/Google Cloud AI
  engineering leader and O'Reilly author (`Beyond Vibe Coding`) already
  represented in this corpus by `blog-addyosmani-code-agent-orchestra.md`. He is
  a practitioner-synthesizer, not a primary researcher: his contribution here is
  aggregating and naming a pattern (citing Peter Steinberger and Boris Cherny as
  the originating voices) and mapping it concretely onto two competing shipped
  products. The post contains no original benchmarks, metrics, or controlled
  comparisons -- it is a structural/definitional piece.
- **Scope**: Covers the conceptual shift from manual per-turn prompting to
  designing an external system ("loop") that prompts the agent; a five-primitive
  taxonomy (automations, worktrees, skills, plugins/connectors, sub-agents) plus
  a sixth structural element (external memory/state); an explicit feature-parity
  table mapping each primitive onto the Codex app and Claude Code; one worked
  example of a composed loop; and a closing section on what loops do not solve
  (verification, comprehension, cognitive surrender). Does NOT cover
  implementation details (no code, no config snippets, no cost data), does not
  benchmark loop output quality against manual prompting, and does not address
  failure modes of any individual primitive in depth -- those are addressed in
  Osmani's own linked prior posts (see Linked Source Extractions).

## Extracted Claims

### Claim 1: Loop engineering is a name for replacing yourself as the person who prompts the agent by designing the system that prompts it instead
- **Evidence**: Author's definitional framing, opened with named attributions to
  two practitioners: Peter Steinberger and Boris Cherny (head of Claude Code at
  Anthropic).
- **Confidence**: emerging (a definitional claim backed by two named-authority
  quotes rather than data, but the authorities are specific and credible --
  Cherny in particular speaks with first-party authority on Claude Code)
- **Quote**: "Loop engineering is replacing yourself as the person who prompts
  the agent. You design the system that does it instead."
- **Additional quote (Steinberger)**: "You shouldn’t be prompting coding agents
  anymore. You should be designing loops that prompt your agents."
- **Additional quote (Cherny)**: "I don’t prompt Claude anymore. I have loops
  running that prompt Claude and figuring out what to do. My job is to write
  loops"
- **Our assessment**: The Cherny quote is independently corroborated: it appears
  verbatim in `blog-ronacher-the-coming-loop.md` (Concrete Artifacts -- "The
  Boris Cherny framing that opens the post"), where Ronacher opens his own
  June 23, 2026 post with the identical statement, sourced from a different
  link (Osmani links `x.com/rohanpaul_ai/status/2063289804708835412`; Ronacher's
  attribution is unlinked in that note). Two independent practitioner-authors
  citing the same Cherny statement within two weeks of each other as the
  defining articulation of this shift is a meaningful corroboration signal --
  this is very likely a real, widely-circulated remark rather than an isolated
  soundbite, even though it traces to a single ultimate source (Cherny).

### Claim 2: A loop requires five structural primitives plus a sixth element (external memory) to function as an autonomous system rather than a single run
- **Evidence**: Author's explicit taxonomy, presented as a numbered list, then
  mapped in a table (see Concrete Artifacts) onto Codex app and Claude Code
  features.
- **Confidence**: emerging (a structural taxonomy, not an empirical finding;
  its value is organizational clarity, verified against real product features
  rather than derived from a study)
- **Quote**: "A loop needs five things and then one place to remember stuff."
- **Additional quote**: "Then the sixth thing, the memory. A markdown file, or
  a Linear board, anything that lives outside the single conversation and holds
  what’s done and what is next."
- **Our assessment**: This taxonomy is the post's core contribution and is
  directly continuous with Osmani's own earlier `code-agent-orchestra` post,
  whose Claim 11 already named "five concrete patterns to adopt immediately --
  subagents for decomposition, agent teams for parallelism, git worktrees for
  isolation, quality gates for trust, AGENTS.md for compound learning." Loop
  Engineering renames and reorganizes nearly the same component set (sub-agents,
  worktrees, AGENTS.md/state) but adds automations and plugins/connectors as
  first-class primitives and explicitly maps every one onto shipped features in
  two competing products rather than presenting them as practitioner
  recommendations. The taxonomy is useful as an audit checklist for "is this
  actually a loop or just an agent session," but the ordering (automations
  listed first) is presentational, not evidence of which primitive matters most.

### Claim 3: Automations -- scheduled discovery and triage that runs without a person initiating it -- are the primitive that makes a system a loop rather than a single agent run
- **Evidence**: Author's structural claim, illustrated by the Codex app's
  Automations tab workflow (pick project, prompt, cadence, environment; results
  land in a Triage inbox; runs that find nothing self-archive) and the Claude
  Code equivalent (scheduled tasks, cron, `/loop`, hooks, GitHub Actions).
- **Confidence**: emerging (feature description with a concrete workflow, not
  a controlled test of automation effectiveness)
- **Quote**: "Automations are what make a loop an actual loop and not just one
  run you did once."
- **Additional quote**: "The runs that find something go to a Triage inbox, and
  the runs that find nothing just archive themselves wich is nice."
- **Our assessment**: This corroborates `blog-anthropic-claude-code-routines.md`
  (Claim 2: the three-axis scheduled/API-triggered/webhook-triggered taxonomy)
  almost exactly -- Osmani's "Automations" primitive and Anthropic's "Routines"
  feature are the same underlying capability described from two different
  vantage points (practitioner synthesis vs. first-party product announcement).
  The self-archiving-on-no-findings detail is new information not present in
  the Routines note, which focused on quotas and trigger types rather than the
  triage-inbox UX.

### Claim 4: `/goal` applies the maker/checker split to the stopping condition itself -- a separate small model judges whether the work is done, rather than the agent that produced it
- **Evidence**: Feature description of Claude Code's `/goal` (keeps working
  until a user-specified condition holds, verified after every turn by a
  separate model) and its Codex equivalent (also called `/goal`, with pause,
  resume, and clear).
- **Confidence**: emerging (feature description; the underlying mechanism --
  a distinct judge model -- is stated as fact but not independently verified
  by the author against production runs)
- **Quote**: "`/goal` keeps going until a condition you wrote is actually true,
  and after every turn a separate small model checks whether you are done, so
  the agent that wrote the code isnt the one grading it."
- **Additional quote**: "This is also basically what Claude Code’s `/goal` does
  under the hood, a fresh model decides if the loop is done instead of the one
  that did the work, the maker and checker split applied to the stop condition
  itself."
- **Our assessment**: This is the most concrete architectural claim in the
  post and it maps directly onto `blog-anthropic-harness-long-running.md`
  Claim 1 (models fail at self-evaluation, confidently praising mediocre work)
  and Claim 2 (the generator/evaluator split outperforms self-critique). Osmani
  is applying the identical generator/evaluator logic that Anthropic Labs
  documented for full harness architectures to a single CLI primitive (`/goal`)
  that any practitioner can invoke without building custom harness
  infrastructure. This is a genuinely useful compression: the same principle,
  productized as a slash command rather than requiring bespoke sprint-contract
  scaffolding.

### Claim 5: Git worktrees solve the mechanical collision problem of parallel agents, but human review bandwidth remains the actual ceiling on how many agents can run
- **Evidence**: Structural description of git worktree isolation (separate
  working directory on its own branch, sharing repo history) plus explicit
  cross-reference to the author's own prior post on the topic.
- **Confidence**: emerging (worktree mechanics are a standard, verifiable git
  feature; the review-bandwidth-as-ceiling claim is asserted, cross-referenced
  to a dedicated prior post, but not independently measured here)
- **Quote**: "A git worktree fixes it, its a separate working directory on its
  own branch sharing the same repo history, so one agent’s edits literally can
  not touch the other one’s checkout."
- **Additional quote**: "the worktrees take away the mechanical collision but
  YOU are still the ceiling, your review bandwith decides how many you can
  actually run, not the tool."
- **Our assessment**: This is fully consistent with -- and explicitly
  cross-referenced by the author to -- his own "orchestration tax" post (see
  Linked Source Extractions below), which makes the identical argument in much
  greater depth: human judgment is a single-threaded resource (the "GIL"
  metaphor) and Amdahl's Law caps the speedup from adding parallel agents at
  the fraction of work that stays serial (review). It also corroborates
  `blog-addyosmani-code-agent-orchestra.md` Claim 8 (WIP limits should be 3-5
  concurrent agents, bounded by review capacity, not tooling).

### Claim 6: Skills exist to stop an agent from re-deriving project context every session, functioning as externalized, one-time-written intent
- **Evidence**: Description of the shared `SKILL.md` folder format across Codex
  ("Agent Skills," invoked with `$` or matched implicitly) and Claude Code, plus
  a link to the author's dedicated "the intent debt" post as the underlying
  argument.
- **Confidence**: emerging (feature description plus a restated argument from a
  separate post, not new evidence generated here)
- **Quote**: "A skill is how you stop re-explaining the same project context
  every session like a goldfish."
- **Additional quote**: "Without skills the loop re-derives your whole project
  from zero every cycle, with skills it kind of compounds."
- **Our assessment**: This corroborates `blog-anthropic-claude-code-skills-lessons.md`
  Claim 1 (skills are one of the most-used extension points in Claude Code) and
  extends it with the loop-specific framing: skills matter more inside a loop
  than in an interactive session because there is no human present to
  re-supply missing context turn-by-turn. The claim that a skill is "the
  authoring format" and a plugin is "how you ship it" also matches the
  distribution model implied by that same note's Claim 4 (skills as folders
  with scripts/assets/data, distributable as bundles).

### Claim 7: Plugins and connectors (built on MCP) are what let a loop act inside real tools -- opening PRs, updating tickets, posting to chat -- rather than just reporting what it would do
- **Evidence**: Structural description of MCP-based connectors as the mechanism
  that gives a loop access to issue trackers, databases, staging APIs, and chat
  tools; both Codex and Claude Code are stated to "speak MCP."
- **Confidence**: emerging (architectural description; MCP interoperability
  between the two named products is stated as fact but not demonstrated with a
  worked cross-tool example)
- **Quote**: "A loop that can only see the filesystem is a tiny loop."
- **Additional quote**: "This is the difference between an agent that says
  “here is the fix” and a loop that opens the PR, links the Linear ticket and
  pings the channel once CI is green by itself."
- **Our assessment**: This is a clean, memorable articulation of why
  connector/plugin infrastructure matters specifically for unattended loops (as
  opposed to interactive sessions, where a human can manually open the PR after
  reading the agent's proposed diff). It does not introduce new mechanism
  beyond what is already documented in the corpus's MCP-focused notes, but the
  "report vs. act" framing is a useful one-line test for whether a given loop
  is actually autonomous or merely advisory.

### Claim 8: Splitting the agent that writes from the agent that checks is the single most useful structural element of a loop, because the loop runs unsupervised
- **Evidence**: Structural argument plus explicit cross-reference to two of the
  author's own prior posts making the same case ("the code agent orchestra" and
  "adversarial code review").
- **Confidence**: emerging (repeated assertion across three of the author's own
  posts, which increases internal consistency but does not constitute
  independent verification; the underlying mechanism -- self-grading bias --
  is corroborated by the first-party Anthropic post below)
- **Quote**: "The most useful structural thing in a loop, by far, is splitting
  the one who writes from the one who checks."
- **Additional quote**: "The reason it matters specifically inside a loop is
  the loop runs while you are not watching, so a verifier you actually trust is
  the only reason you can walk away."
- **Our assessment**: This is the strongest corroboration point in the note.
  `blog-anthropic-harness-long-running.md` Claim 1 documents the identical
  mechanism from a first-party, metrics-backed engineering retrospective:
  "agents tend to respond by confidently praising the work -- even when, to a
  human observer, the quality is obviously mediocre." Osmani's contribution is
  narrower but more actionable for most practitioners: he ties the same
  principle to a shipped, low-effort primitive (Claude Code subagents /
  `.claude/agents/`, Codex subagents as TOML in `.codex/agents/`) rather than
  requiring a custom Agent-SDK harness. The claim that subagents "burn more
  tokens since each one does its own model and tool work" is a real,
  underexamined cost the guide should note alongside the quality benefit.

### Claim 9: Loop primitives are no longer bespoke infrastructure a practitioner builds and maintains -- they now ship as first-class features inside both major coding-agent products
- **Evidence**: Author's direct before/after comparison: a year prior, a loop
  required a practitioner-maintained "pile of bash"; now the same five
  primitives are native features in both Codex and Claude Code.
- **Confidence**: emerging (a market-observation claim; verifiable in principle
  by checking each product's feature set, but not independently audited here
  beyond the author's own feature-parity table)
- **Quote**: "A year ago if you wanted a loop you wrote a pile of bash and you
  maintained that pile forever and it was yours and only yours. Now the pieces
  just ship inside the products."
- **Additional quote**: "Both products have all five now."
- **Our assessment**: This is a significant claim for the guide's shelf life:
  it argues that loop engineering has moved from a bespoke-scripting skill (the
  Ralph loop bash script documented in `blog-addyosmani-code-agent-orchestra.md`
  Concrete Artifacts) to a configuration skill (choosing and wiring together
  product-native primitives). If accurate, guide content that only teaches the
  bash-script Ralph loop pattern is increasingly incomplete -- practitioners
  should also be pointed at the native scheduling/worktree/subagent primitives
  in whichever tool they use. We rate this "emerging" rather than "settled"
  because it rests on one practitioner's feature audit of two products at one
  point in time (June 2026), and feature availability by plan tier is not
  addressed (contrast with `blog-anthropic-claude-code-routines.md` Claim 7,
  which documents that Routines specifically are gated by plan-tier daily
  quotas -- "ships inside the product" does not mean unlimited or free).

### Claim 10: A composed loop looks like a repeatable daily cycle -- an automation triggers a triage skill, isolated worktrees host sub-agent maker/checker pairs, connectors close the loop externally, and a state file carries context to the next run
- **Evidence**: A single worked narrative example combining all five primitives
  plus the state file.
- **Confidence**: anecdotal (illustrative example, not a documented production
  system with metrics; no cost, duration, or success-rate data provided, unlike
  the DAW/retro-game comparisons in `blog-anthropic-harness-long-running.md`)
- **Quote**: "An automation runs every morning on the repo. Its prompt calls a
  triage skill that reads yesterdays CI failures, the open issues, the recent
  commits, and writes the findings into a markdown file or a Linear board."
- **Additional quote**: "The state file is the spine of the whole thing, it
  remembers what got tried, what passed, what is still open, so tomorrow
  morning the run picks up where today stopped."
- **Our assessment**: This worked example is useful as a template but should
  not be over-weighted -- it is illustrative prose, not a documented deployment.
  Notably, this repository's own Miner/Prospector/Assayer/Smith pipeline
  (visible in this very extraction task) is a real, running instance of
  almost exactly this pattern: scheduled triage, skill-driven extraction,
  worktree-style isolation between agent roles, and issue/PR state as the
  external memory layer. That is a stronger existence proof of the pattern's
  viability than the blog post's own hypothetical example.

### Claim 11: Loops do not remove the need for human judgment -- three problems (verification, comprehension, complacency) get structurally harder, not easier, as the loop improves
- **Evidence**: Author's closing argument, cross-referencing three of his own
  prior posts (code review in the age of AI, comprehension debt, cognitive
  surrender) as the basis for each of the three named risks.
- **Confidence**: emerging (a normative/cautionary claim, consistent with and
  explicitly built on separately-argued prior posts rather than new evidence
  presented in this post)
- **Quote**: "The loop changes the work, it does not delete you from it. And
  three problems actually get sharper as the loop gets better, not easier."
- **Additional quote**: "Verification is still on you." / "Your understanding
  still rots if you allow it." / "the comfortable posture is the dangerous
  one."
- **Our assessment**: This closing caution is consistent with, and less
  detailed than, `blog-ronacher-the-coming-loop.md`, which makes a
  substantially more developed version of the same argument: Ronacher's
  Claim 12 describes the human role degrading to "messenger" inside a
  harness-operated loop, and Claim 5 describes loop iterations compounding
  defensive-code accumulation. The two posts are not in tension -- both treat
  unattended verification as the central open problem of loop-based systems --
  but Osmani's framing is more optimistic about retained agency ("Two people
  can build the exact same loop and get completely opposite results... The
  loop doesn't know the difference. You do") where Ronacher is more skeptical
  about whether the human is structurally still in a position to exercise that
  agency once the "done" signal is delegated to a machine judge. This is a
  difference in emphasis and confidence, not a factual disagreement -- both
  agree design and review discipline determine the outcome, they differ on how
  much residual control a well-designed loop actually leaves the human. Not
  filed as a contradiction per MINER.md 4a (conditioning/emphasis, not a claim
  that leads to opposite guide advice).

### Claim 12: The shift from prompt engineering to loop design increases the difficulty and stakes of the human's job rather than decreasing it -- the leverage point moved, it did not disappear
- **Evidence**: Author's closing synthesis, restating Cherny's framing from
  Claim 1.
- **Confidence**: anecdotal (rhetorical conclusion, not a measured or tested
  claim)
- **Quote**: "That’s what makes loop design harder than prompt engineering, not
  easier. Cherny’s point isn’t that the work got easier. It’s that the leverage
  point moved."
- **Our assessment**: This is a reasonable synthesis of the post's own evidence
  but should be read as the author's opinion, not a demonstrated result. It is
  directionally consistent with `blog-addyosmani-code-agent-orchestra.md`
  Claim 1 (the shift to multi-agent orchestration "fundamentally changes the
  required skill set") and with that note's assessment that the orchestra
  metaphor "risks grandiosity" while the underlying observation is sound. The
  same caveat applies here.

## Concrete Artifacts

### The five primitives plus memory (as listed in the post)

```
Source: Addy Osmani, "Loop Engineering," https://addyosmani.com/blog/loop-engineering/ (June 7, 2026)

1. Automations that go off on a schedule and do discovery and triage by
   themselves.
2. Worktrees so two agents working in paralell dont step on each other.
3. Skills to write down the project knowledge the agent would otherwise
   just guess.
4. Plugins and connectors to plug the agent into the tools you already use.
5. Sub-agents so one of them has the idea and a different one checks it.

Sixth element (not numbered in the list): the memory -- "A markdown file,
or a Linear board, anything that lives outside the single conversation and
holds what’s done and what is next."
```

### Primitive-to-product feature-parity table

```
Source: Addy Osmani, "Loop Engineering," https://addyosmani.com/blog/loop-engineering/ (June 7, 2026)

Primitive             | Job in the loop              | Codex app                                                                                          | Claude Code
-----------------------|-------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------
Automations           | discovery + triage on a       | Automations tab: pick project, prompt, cadence, environment; results land in a Triage inbox;         | Scheduled tasks and cron, /loop, /goal, hooks, GitHub Actions
                       | schedule                       | /goal for run-until-done                                                                              |
Worktrees             | isolate parallel features      | Built-in worktree per thread                                                                          | git worktree, --worktree, isolation: worktree on a subagent
Skills                | codify project knowledge       | Agent Skills (SKILL.md), invoked with $name or implicitly                                             | Agent Skills (SKILL.md)
Plugins / connectors  | connect your tools             | Connectors (MCP) plus plugins for distribution                                                        | MCP servers plus plugins
Sub-agents            | ideate and verify              | Subagents defined as TOML in .codex/agents/                                                            | Task subagents in .claude/agents/, agent teams
State                 | track what's done              | Markdown or Linear via a connector                                                                    | Markdown (AGENTS.md, progress files) or Linear via MCP
```

### Worked example: "what one loop looks like"

```
Source: Addy Osmani, "Loop Engineering," https://addyosmani.com/blog/loop-engineering/ (June 7, 2026)

"An automation runs every morning on the repo. Its prompt calls a triage
skill that reads yesterdays CI failures, the open issues, the recent
commits, and writes the findings into a markdown file or a Linear board.
For each finding that is worth doing the thread opens an isolated worktree
and sends a sub-agent to draft the fix, and a second sub-agent reviews that
draft against the project skills and the existing tests.

Connectors let the loop open the PR and update the ticket. Anything the
loop can not handle lands in the triage inbox for me. The state file is
the spine of the whole thing, it remembers what got tried, what passed,
what is still open, so tomorrow morning the run picks up where today
stopped."
```

## Cross-References

- **Corroborates**:
  - `blog-ronacher-the-coming-loop.md` (Concrete Artifacts -- "The Boris Cherny
    framing that opens the post"): independently quotes the identical Boris
    Cherny statement ("I don't prompt Claude anymore...") as the defining
    articulation of the shift from prompting to loop authorship -- two
    practitioner-authors converging on the same source within two weeks.
  - `blog-anthropic-harness-long-running.md` Claim 1 and Claim 2: the
    self-evaluation failure mode ("agents tend to respond by confidently
    praising the work -- even when, to a human observer, the quality is
    obviously mediocre") and the generator/evaluator architectural fix are the
    first-party, metrics-backed version of this post's Claim 4 and Claim 8
    (maker/checker split via `/goal` and sub-agents).
  - `blog-anthropic-claude-code-routines.md` Claim 2 and Claim 3: the
    scheduled/API-triggered/webhook-triggered taxonomy for Routines is the same
    underlying capability as this post's "Automations" primitive, described
    from the vendor side rather than the practitioner-synthesis side.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 1: "Skills have become
    one of the most used extension points in Claude Code" corroborates this
    post's claim that skills are now a standard loop primitive rather than a
    niche feature.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 8 (WIP limits bounded by
    review capacity, not tooling) and Claim 4 (Agent Teams shared task list):
    directly corroborated by this post's worktree and sub-agent sections,
    written by the same author roughly three months later.

- **Contradicts**: None filed. The closest tension is between this post's
  Claim 11 (the loop "doesn't know the difference" between disciplined and
  complacent use -- agency is retained if the practitioner exercises it) and
  `blog-ronacher-the-coming-loop.md` Claim 12 (in a harness-operated loop, "My
  role is reduced to that of a messenger" -- agency is structurally attenuated
  once the done-signal is delegated to a machine judge). Per MINER.md 4a, this
  is a difference in emphasis/confidence about the same underlying mechanism
  (both agree harness design and review discipline are what's actually at
  stake), not a claim that would drive opposite guide advice, so no
  contradiction issue was filed. The Assayer should double check this judgment.

- **Extends**:
  - `blog-addyosmani-code-agent-orchestra.md`: elevates that post's five
    "patterns to adopt" (Claim 11) from a practitioner recommendation list into
    a named paradigm ("loop engineering") with an explicit feature-parity
    mapping across two competing products, and adds automations and
    plugins/connectors as first-class primitives not enumerated in the earlier
    post's five.
  - `blog-anthropic-claude-code-routines.md` and
    `blog-anthropic-claude-code-skills-lessons.md`: this post is the
    connective tissue the guide currently lacks between individually-documented
    Claude Code features (Routines, Skills, subagents, worktrees) -- it
    explicitly argues these are not separate features but components of one
    coherent system when combined with external memory.
  - `blog-anthropic-harness-long-running.md`: compresses that post's
    Agent-SDK-level generator/evaluator/sprint-contract architecture into a
    CLI-native primitive (`/goal`) accessible without building custom harness
    infrastructure.

- **Novel**:
  - **"Loop engineering" as a named paradigm distinct from "harness
    engineering"**: the post explicitly frames loop engineering as "the cousin"
    of and "one floor above" harness engineering -- the harness is what one
    agent runs inside; the loop is what runs the harness on a timer and feeds
    it its own findings. No existing corpus note draws this specific
    floor-above relationship between the two concepts.
  - **Explicit five-primitive feature-parity table across Codex app and Claude
    Code**: no existing corpus source maps the same taxonomy onto both
    products side by side. `blog-ronacher-the-coming-loop.md` names the
    agent-loop/harness-loop architectural distinction but does not decompose
    the harness loop into discrete, product-mapped primitives.
  - **"Ships inside the product" framing for loop infrastructure**: the claim
    that loop primitives have moved from bespoke bash-script infrastructure to
    native product features (Claim 9) is a maturity-of-the-ecosystem claim not
    made explicitly in any prior corpus source.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a subsection distinguishing
  "harness" (what one agent runs inside, per `blog-anthropic-harness-long-running.md`
  and the author's own `agent-harness-engineering` post) from "loop" (the
  system that runs the harness repeatedly and feeds it its own findings, per
  this source and `blog-ronacher-the-coming-loop.md`'s agent-loop/harness-loop
  distinction). Currently the guide's harness content is agent-session-scoped;
  this source and its cross-references argue that scheduling/automation is an
  architecturally distinct layer above it, not a harness detail.

- **Chapter 01 (Daily Workflows)**: Add the five-primitive-plus-memory
  checklist (automations, worktrees, skills, plugins/connectors, sub-agents,
  state) as a practical audit tool: "if you're missing one of these six, you
  have an agent session, not a loop." Cross-reference the feature-parity table
  so practitioners can locate the equivalent primitive regardless of which
  tool (Claude Code or Codex) they use.

- **Chapter 02 (Harness Engineering) -- Verification**: Add `/goal`'s
  maker/checker stop-condition split (Claim 4) as a lightweight, CLI-native
  alternative to building a full generator/evaluator harness when the task
  does not warrant Agent-SDK-level custom infrastructure (per the
  `blog-anthropic-harness-long-running.md` cost-benefit principle already in
  the guide: the evaluator is worth its cost only when the task exceeds what
  the model does reliably solo).

- **Chapter 04 (Context Engineering, skeleton)**: The sixth-element framing
  ("the memory... the model forgets everything between runs so the memory has
  to be on disk and not in the context") reinforces the existing Ralph Loop /
  state-file guidance from `blog-addyosmani-code-agent-orchestra.md` with a
  cleaner one-line justification for why external state is structurally
  necessary, independent of any specific implementation pattern.

- **Chapter 05 (Team Adoption)**: Add Claim 9 (loop primitives now ship inside
  products rather than requiring bespoke infrastructure) as a framing point for
  teams deciding whether to build custom automation vs. adopt native tooling --
  paired with the caveat from `blog-anthropic-claude-code-routines.md` Claim 7
  that native scheduling features (e.g., Routines) are gated by plan-tier daily
  quotas, so "ships inside the product" does not mean unlimited.

## Linked Source Extractions

Three of the author's own linked posts were fetched and read in full because
they underpin claims made directly in this post (the harness/loop distinction,
the review-bandwidth ceiling, and the "memory must live outside the model"
argument). Two other linked posts already have dedicated corpus source notes
(`blog-anthropic-harness-long-running.md` for the Anthropic harness post;
`blog-ronacher-the-coming-loop.md` covers adjacent territory to the Karpathy
"mortally terrified of exceptions" link, though this post does not itself link
Karpathy). Several other self-referential links (agent-skills, intent-debt,
adversarial-code-review, code-review-ai, comprehension-debt, cognitive-surrender)
were not separately fetched -- they support single claims each (see the
Extracted Claims section above for their specific role) and did not appear to
add material beyond what their citing sentence already conveys.

### Linked Source 1: "Agent Harness Engineering" (2026-04-19)

**URL**: https://addyosmani.com/blog/agent-harness-engineering/

**Key findings**:
- Defines the harness via Viv Trivedy's formulation: "Agent = Model + Harness.
  If you're not the model, you're the harness."
- Names the "ratchet" practice: "Every line in a good `AGENTS.md` should be
  traceable back to a specific thing that went wrong" -- constraints are only
  added after an observed failure, never speculatively.
- States the Terminal Bench 2.0 data point (attributed to Viv Trivedy's team):
  moving a coding agent to a custom harness took it from Top 30 to Top 5 by
  changing only the harness, not the model.
- Names three context-rot mitigations used across harnesses: compaction,
  tool-call offloading, and skills with progressive disclosure -- and cites
  Anthropic's finding that "compaction alone wasn't sufficient" for long tasks.
- States the "harnesses don't shrink, they move" principle (attributed to the
  Anthropic harness post): "every component in a harness encodes an assumption
  about what the model can't do on its own."
- Names "Harness-as-a-Service" (Viv Trivedy's term): the shift from building on
  LLM completion APIs to building on harness runtime APIs (Claude Agent SDK,
  Codex SDK, OpenAI Agents SDK).

**Guide impact**: This is the direct conceptual precursor to Loop Engineering's
opening framing ("I wrote before about the cousin of this, agent harness
engineering... Loop engineering sits one floor above the harness"). It
provides the harness-side vocabulary (ratchet, context rot, HaaS) that
Chapter 02 should use alongside the loop-side vocabulary from the main post.
The Terminal Bench Top-30-to-Top-5 harness-only improvement is a concrete,
citable data point (secondhand, attributed to Viv Trivedy) worth flagging for
a follow-up extraction of the primary source.

### Linked Source 2: "The Orchestration Tax" (2026-05-24)

**URL**: https://addyosmani.com/blog/orchestration-tax/

**Key findings**:
- Central claim, attributed in part to a live exchange with Richard Seroter at
  a Google I/O panel: "running multiple agents does not mean there is more of
  you" -- human review judgment is a single-threaded resource.
- Uses the Python GIL as the operating metaphor: "You are the GIL of your AI
  agents... when any of their work needs genuine understanding of the
  architecture or resolving merge conflicts, that work has to acquire the
  lock. There is one lock. You hold it."
- Applies Amdahl's Law explicitly: "The speedup you get from paralellizing is
  capped by the fraction of work that stays serial... In agent development the
  serial fraction is the judgement."
- Five concrete practices: scale fleet size to review rate (not UI limits);
  sort work into delegatable vs. judgment-requiring piles; batch reviews to
  avoid repeated context-switch costs; spend the "lock" only on judgment (let
  the agent self-verify the mechanical 80%); protect serial (deep-focus) time.
- Distinguishes "busy" from "productive": running 20 agents can feel maximally
  productive while shipping little, because the dashboard tracks agent activity
  rather than reviewed/merged output.

**Guide impact**: This is the primary evidentiary source behind Loop
Engineering's Claim 5 ("YOU are still the ceiling"). It is far more developed
than the brief mention in the loop post and should anchor Chapter 05's
guidance on scaling agent fleets: the WIP-limit recommendation from
`blog-addyosmani-code-agent-orchestra.md` (3-5 agents) gets its mechanistic
justification here (Amdahl's Law / single-threaded review capacity), not just
an empirical rule of thumb.

### Linked Source 3: "Long-running Agents" (2026-04-28)

**URL**: https://addyosmani.com/blog/long-running-agents/

**Key findings**:
- Distinguishes three senses of "long-running": long-horizon reasoning (a
  model-quality property, tracked by METR's time-horizon metric, "doubling
  roughly every seven months since 2019"), long-running execution (a harness
  property), and persistent agency (a memory/identity property).
- Names "the three walls every long-running agent hits": finite context, no
  persistent state, and no self-verification -- framed via Anthropic's own
  analogy: "imagine a software project staffed by engineers working in shifts,
  where each new engineer arrives with no memory of what happened on the
  previous shift."
- Documents the Ralph loop reference implementation (attributed to Geoffrey
  Huntley and Ryan Carson) as a seven-step bash loop, and states plainly:
  "state lives outside the agent's context... The agent itself is amnesiac,
  but the filesystem isn't."
- Surveys three lab approaches converging on the same shape (explicit plan
  file, explicit progress file, separate generation from evaluation, a loop
  that refuses early stopping): Anthropic's initializer/coding-agent harness
  and brain/hands/session decoupling, and Cursor's planner/worker/judge
  architecture (with the finding that GPT outperformed Opus specifically for
  extended autonomous work because "Opus tended to stop early and take
  shortcuts").

**Guide impact**: This is the primary source behind Loop Engineering's
sixth-element claim ("the model forgets everything between runs so the memory
has to be on disk and not in the context"), and it is considerably more
detailed than the brief restatement in the loop post. The three-walls
framework (finite context / no persistent state / no self-verification) is a
cleaner organizing structure for Chapter 04's context-engineering content than
anything currently cited, and the Cursor model-role-matching finding (GPT for
extended autonomous work vs. Opus for other roles) is a novel, citable data
point not otherwise in the corpus and worth flagging for its own extraction if
the underlying Cursor post is added as a source.

## Extraction Notes

- Full article text for the main post and all three linked posts fetched via
  `curl` + `html2text` (not the WebFetch summarization tool) specifically so
  that every quote in this note could be copied character-for-character,
  including the source's own typos (e.g., "wich," "paralell," "isnt," "doesnt,"
  "bandwith") which are preserved verbatim in quotes per MINER.md 2a.
- Followed 3 of the post's ~8 self-referential links in depth (agent-harness-
  engineering, orchestration-tax, long-running-agents), chosen because they are
  the direct evidentiary basis for claims made in the main post itself (the
  harness/loop relationship, the review-bandwidth ceiling, and the
  external-memory argument). Two other linked topics already have dedicated
  corpus notes (`blog-anthropic-harness-long-running.md`,
  `blog-ronacher-the-coming-loop.md`) and were used for cross-referencing
  rather than re-fetched. The remaining self-referential links (agent-skills,
  intent-debt, adversarial-code-review, code-review-ai, comprehension-debt,
  cognitive-surrender) were not fetched; each supports exactly one claim in the
  main post and the citing sentence in the main post text was judged sufficient
  for this extraction's purposes. A future miner could extract these as
  standalone sources if they contain material not already covered by
  `blog-addyosmani-code-agent-orchestra.md`'s existing Linked Source
  Extractions (comprehension-debt and self-improving-agents are already
  covered there).
- Both external (non-Osmani) quotes attributed in the post -- Peter
  Steinberger's and Boris Cherny's -- are quoted from Osmani's own rendering of
  them (each links to an `x.com` status URL that was not independently
  fetched). The Cherny quote's independent appearance in
  `blog-ronacher-the-coming-loop.md`, sourced via a different link, gives
  reasonable confidence the quote is accurately transcribed by both authors.
  The Steinberger quote has no independent corroboration in this corpus; it is
  attributed to Osmani's paraphrase-as-quote of a tweet and should be treated
  with the same caution as any single-sourced attributed quote.
- No contradiction issue was filed. The one candidate tension identified
  (Claim 11 vs. `blog-ronacher-the-coming-loop.md` Claim 12, on how much
  agency a human retains inside a well-designed loop) was judged to be a
  difference in emphasis and confidence about the same underlying mechanism,
  not a factual disagreement that would drive opposite guide advice -- see the
  Cross-References section above for the full reasoning. The Assayer should
  independently check this judgment before treating it as settled.
- Cross-references to `blog-addyosmani-code-agent-orchestra.md`,
  `blog-anthropic-harness-long-running.md`,
  `blog-anthropic-claude-code-routines.md`,
  `blog-anthropic-claude-code-skills-lessons.md`, and
  `blog-ronacher-the-coming-loop.md` were all verified by reading the cited
  claim numbers in the actual source-note files before writing this note; no
  claim numbers were guessed.
