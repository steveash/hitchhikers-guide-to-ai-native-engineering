---
source_url: https://www.latent.space/p/wayfinder-skill
source_type: blog-post
title: "The /wayfinder Skill: Navigating the \"Fog of War\" of Planning"
author: Richard MacManus (Latent Space), interviewing Matt Pocock (AI Hero / "AI Skills for Real Engineers")
date_published: 2026-08-20
date_extracted: 2026-09-06
last_checked: 2026-09-06
status: current
confidence_overall: anecdotal
issue: "#3274"
---

# The /wayfinder Skill: Navigating the "Fog of War" of Planning

> A Latent Space interview with Matt Pocock introducing `/wayfinder`, an
> installable Claude Code/agent skill for planning greenfield or
> uncertain-outcome projects, built around three named entities — map
> (accumulated decisions), ticket (a bounded unit of work, typed as grilling,
> prototype, research, or task), and session (the execution context a ticket
> runs in) — orchestrated by a layer that decides what to plan next instead
> of the human manually managing planning-session context.

## Source Context

- **Type**: blog-post (narrative interview/Q&A format, first-party skill
  announcement from the tool's creator, published on a trusted feed)
- **Author credibility**: Richard MacManus is a Latent Space contributor
  (already represented in this corpus via `blog-latentspace-macmanus-glean-model-routing.md`,
  another narrative interview piece). The interview subject, Matt Pocock, is
  an independently-established voice in this specific subfield — creator of
  the "AI Skills for Real Engineers" project (220,000+ GitHub stars per the
  Prospector's triage) and host of a 347,000-subscriber YouTube channel
  focused on AI coding workflows. Pocock is also independently corroborated
  elsewhere in this corpus as an active skill-builder: `blog-humanlayer-show-me-skill.md`
  names him (Source Context) among practitioners who built on or reacted to
  HumanLayer's `show-me` skill. This is a first-party creator interview, not
  an independent evaluation — all claims about wayfinder's effectiveness
  originate from the person who built and is promoting it.
- **Scope**: Covers the motivating problem (context-management overhead
  during planning for uncertain-outcome projects), the three-entity model
  (map/ticket/session), four ticket subtypes (grilling/prototype/research/task),
  a decision rule for choosing wayfinder over Pocock's earlier "grill me"
  skill, his terminology/"ubiquitous language" philosophy, and one worked
  example (a personal-website rearchitecture project, shown via screenshots).
  Does NOT cover: the skill's underlying prompt/instruction text verbatim,
  install instructions or a package name comparable to `npx skills add ...`,
  any usage metrics, failure modes, or independent verification that the
  pattern reduces planning overhead in practice — the entire case is made by
  the creator's own description and one self-selected example.

## Extracted Claims

### Claim 1: The core problem wayfinder addresses is "fog of war" — situations where a project's full decision set cannot be determined at the start
- **Evidence**: Pocock's own framing of the concept, given directly in
  response to a question about wayfinder's use cases.
- **Confidence**: anecdotal
- **Quote**: "One really key idea in wayfinder is the 'fog of war'. So this is the concept of, you can't quite decide everything right at the start."
- **Our assessment**: This is a naming/framing claim, not an empirical one —
  it labels a real and recognizable problem (planning under incomplete
  information) rather than demonstrating that wayfinder solves it better
  than alternatives. The value for the guide is the vocabulary itself: "fog
  of war" is a compact, memorable term for a planning condition the corpus
  already touches via looser framing (see Cross-References).

### Claim 2: Wayfinder structures planning around three entities — a map (accumulated decisions), a ticket (the specific task), and a session (the execution context)
- **Evidence**: Pocock's description of the design process, naming each
  entity in turn.
- **Confidence**: anecdotal
- **Quote**: "You've got the map, and you've got the ticket, and you've got the session."
- **Our assessment**: This three-way split is the skill's structural core.
  It maps loosely onto patterns already in the corpus under different names:
  the "map" resembles an externalized state/decision record (see
  `blog-addyosmani-loop-engineering.md` Claim 2's "sixth element," and
  `blog-addyosmani-code-agent-orchestra.md` Claim 6's Ralph Loop memory
  channels), and the "ticket" resembles a bounded unit of work analogous to
  a task pulled from a task-state file. What's new here is naming and
  formalizing the pairing specifically for the *planning* phase, rather than
  for execution loops generally — see Guide Impact.

### Claim 3: A child planning session needs two things: a vague overview of everything else happening, and its own specific task
- **Evidence**: Pocock's explanation of what gets passed into a spawned
  planning session.
- **Confidence**: anecdotal
- **Quote**: "the child probably needs to understand a vague overview of what else is happening, and they need their specific task."
- **Our assessment**: This is the map/ticket split operationalized — the
  "map" supplies the vague overview, the "ticket" supplies the specific task.
  It's a plausible minimal-context-injection design (avoid re-deriving the
  whole project per child session) but is asserted, not measured; no
  comparison is offered against giving a child session either more or less
  context.

### Claim 4: An orchestrator layer decides what to plan next, removing the need for the human to manually manage planning-session sequencing
- **Evidence**: Pocock's stated design goal.
- **Confidence**: anecdotal
- **Quote**: "I wanted an orchestrator layer that would basically say, okay, whatever you want to plan, I'm going to handle the planning sessions for you."
- **Our assessment**: This reframes wayfinder as an orchestration layer
  specifically for the *planning* phase — distinct from execution-phase
  orchestration (subagents, agent teams) already documented in the corpus.
  No detail is given on how the orchestrator actually decides sequencing
  (a scheduling algorithm? a fixed order of ticket types? human-in-the-loop
  confirmation at each step?), so this is a stated intent rather than a
  described mechanism.

### Claim 5: Wayfinder defines four ticket types — grilling, prototype, research, and task — each serving a distinct planning function
- **Evidence**: Pocock's enumeration of ticket types in response to a
  use-cases question.
- **Confidence**: anecdotal
- **Quote**: "So you've got grilling tickets, which are just a grilling session."
- **Our assessment**: The interview names all four types together (grilling,
  prototype, research, and task tickets — the last covering "anything the
  human needs to do that the agent can't do," per Pocock's fuller answer),
  but only the first is quotable here as a short, self-contained fragment
  without splicing per MINER.md §2a; the fuller enumeration is paraphrased
  rather than quoted for that reason. As a taxonomy it's a reasonable
  decomposition of planning work into what needs alignment (grilling), what
  needs building to learn (prototype), what needs external information
  (research), and what's outside the agent's own capability (task) — but no
  criteria are given for how an agent (or human) decides which type a given
  piece of planning work falls into.

### Claim 6: Use "grill me" when the whole task can be planned in a single session; use wayfinder specifically for work where the path ahead is unknown
- **Evidence**: Pocock's direct answer to when to use each of his two skills.
- **Confidence**: anecdotal
- **Quote**: "Use 'grill me' in cases where you feel like you can plan the whole thing in a single session, and you need to align before you go."
- **Our assessment**: This is the most actionable, decision-rule-shaped
  claim in the source: a binary choice conditioned on whether the project's
  scope is knowable up front. It is a conditioning variable, not a
  contradiction, between the two skills — consistent with MINER.md §4a's
  guidance not to file a contradiction issue for "use X here, use Y there"
  distinctions. Both skills are Pocock's own, so the comparison is
  self-consistent rather than an adjudicated head-to-head.

### Claim 7: Precise, consistent terminology between human and agent reduces confused agent behavior
- **Evidence**: Pocock's stated rationale for being deliberate about naming
  (map/ticket/session, ticket subtypes) rather than using looser or
  overlapping terms.
- **Confidence**: anecdotal
- **Quote**: "because if you just call everything a ticket, or if you just refer to it in different ways in different places, then it's going to be really confused and you're going to get strange behavior."
- **Our assessment**: This is a specific, checkable-in-principle claim
  (inconsistent terminology → "strange behavior") but no example of the
  strange behavior is given, nor a before/after comparison. It supports a
  broader, plausible harness-engineering principle — that a skill's internal
  vocabulary should be fixed and non-overlapping — but as stated here it's
  an assertion from the skill's own author about his own skill's design
  choice.

### Claim 8: Pocock is developing a broader "ubiquitous language" / AI coding dictionary to keep terminology consistent across all of his skills, not just wayfinder
- **Evidence**: Pocock's own statement in response to a question about time
  spent teaching the model terminology.
- **Confidence**: anecdotal
- **Quote**: "I realized that I needed a ubiquitous language between me and the agent."
- **Our assessment**: This generalizes Claim 7 from a single skill's
  internal naming to a cross-skill vocabulary standard. It's a personal
  practice described by one practitioner, not a tested framework — useful as
  a named concept ("ubiquitous language," borrowed from domain-driven design
  terminology) but with no artifact (e.g., a published dictionary) linked in
  this article to inspect directly.

### Claim 9: Wayfinder has been applied to non-engineering domains, including course planning
- **Evidence**: Pocock's own statement about his usage of the skill.
- **Confidence**: anecdotal
- **Quote**: "I've been using it for engineering, for non-engineering stuff, for course planning, all sorts."
- **Our assessment**: A single-practitioner, self-reported claim of
  cross-domain applicability with no worked non-engineering example shown in
  the article (only the website-rearchitecture example is illustrated with
  screenshots). Treat as a plausibility signal, not evidence that the
  map/ticket/session model transfers cleanly outside software projects.

### Claim 10: Pocock tested wayfinder by using it to plan a rearchitecture of his own personal website
- **Evidence**: Pocock's description of his dogfooding process, illustrated
  with screenshots in the article.
- **Confidence**: anecdotal
- **Quote**: "I decided to test /wayfinder on a project to rearchitect my personal website. Here's the initial project set-up, in this case using Claude Code."
- **Our assessment**: This is the article's only concrete worked example,
  and it is a single first-party dogfooding case rather than an independent
  or third-party deployment. It establishes that the skill was used on a
  real (if small, personal-scale) project, but provides no outcome data
  (time saved, decisions avoided, planning-session count before/after).

## Concrete Artifacts

```
Source: https://www.latent.space/p/wayfinder-skill (Richard MacManus
interviewing Matt Pocock, published 2026-08-20)

Three-entity model (as named in the interview):
  - map     — accumulated project decisions ("all of the rest of the stuff,
              all the decisions that have already been made")
  - ticket  — the specific bounded task
  - session — the execution context a ticket runs in

Four ticket types (as enumerated by Pocock):
  - grilling  — a grilling/alignment session
  - prototype — for creating prototypes
  - research  — for conducting research
  - task      — broad catch-all, "anything the human needs to do that the
                agent can't do"

Decision rule (Pocock, when asked "when do we directly use the grill-me
skill, versus wayfinder?"):
  - grill me  — "in cases where you feel like you can plan the whole thing
                in a single session, and you need to align before you go"
  - wayfinder — "for stuff where you don't know the path ahead, for stuff
                where you can feel the fog of war in front of you"
```

## Cross-References

- **Corroborates**: `blog-humanlayer-show-me-skill.md` (Source Context) —
  that note independently names Matt Pocock as one of several practitioners
  who "built on or reacted to" HumanLayer's `show-me` skill, corroborating
  this note's framing of him as an active, cross-pollinating skill-builder
  in the same practitioner ecosystem rather than an isolated author.
- **Extends**: `blog-addyosmani-loop-engineering.md` Claim 2 (a loop needs
  five primitives plus a sixth element, external memory — "A markdown file,
  or a Linear board, anything that lives outside the single conversation
  and holds what's done and what is next") and Claim 6 (skills exist "to
  stop an agent from re-deriving project context every session"). Wayfinder's
  "map" is a planning-phase-specific instance of that same externalized-memory
  primitive, and its "ticket" is a planning-phase-specific instance of a
  bounded unit of work; this source formalizes both specifically for the
  *planning* stage rather than for general execution loops.
- **Extends**: `blog-addyosmani-code-agent-orchestra.md` Claim 6 (the Ralph
  Loop's five-step cycle and its memory channels — "git commit history,
  progress logs, task state file, and AGENTS.md") — wayfinder's map/ticket
  split is a narrower, planning-specific analog of the same
  externalized-state-plus-bounded-task pattern, applied before
  implementation begins rather than during it.
- **Extends**: `blog-simonwillison-liteparse-browser.md` Claim 5 (the
  notes.md → plan.md context handoff, where prior research is pasted into a
  file and Claude Code is asked to read it before writing a plan). Willison's
  pattern is an ad hoc, single-project instance of what wayfinder tries to
  formalize and name as a reusable skill: an externalized decision record
  (map ≈ notes.md) feeding a bounded planning task (ticket ≈ the plan.md
  request). Wayfinder adds an orchestrator layer and typed ticket subtypes
  that Willison's manual workflow does not have.
- **Contradicts**: None identified. No existing source note makes a claim
  about planning-phase context management that this source's claims
  materially oppose.
- **Novel**: (1) The "fog of war" framing as a named condition for planning
  under incomplete information — no prior corpus source uses this specific
  term. (2) The map/ticket/session three-entity model as an explicit,
  named structure for the planning phase specifically (as opposed to
  execution-loop memory/task patterns already in the corpus). (3) The
  four-way ticket typology (grilling/prototype/research/task) — no prior
  source decomposes planning work into these categories. (4) The
  "ubiquitous language" cross-skill terminology-consistency practice as an
  explicit, named harness-design concern distinct from any single skill's
  content.

## Guide Impact

- **Chapter 01 (Daily Workflows) or Chapter 02 (Harness Engineering)**: Add
  the "fog of war" framing and the grill-me/wayfinder decision rule (Claim 6)
  as a concrete heuristic for choosing a planning approach: if the project's
  scope is knowable up front, a single-session alignment conversation
  suffices; if it isn't, a skill that maintains a persistent map across
  multiple bounded planning tickets is a better fit. This is a specific,
  actionable addition — the guide currently lacks a named decision rule for
  "how much planning structure does this project need."
- **Chapter 04 (Context Engineering, skeleton)**: Cite the map/ticket/session
  model alongside the existing loop-engineering "external memory" and Ralph
  Loop "task state file" content (see Cross-References) as a
  planning-phase-specific instance of the same principle: decisions and
  overview information belong in a persistent, externally-readable record,
  and each child session should receive that overview plus its own narrow
  task rather than the whole project's history. Note explicitly that this
  source provides no outcome data — it is a design pattern proposal from the
  skill's creator, not a verified improvement.
- **Chapter 02 (Harness Engineering — Skill Terminology)**: Add Claim 7/8
  (precise, non-overlapping, cross-skill-consistent terminology as a
  deliberate design choice) as a lightweight addition to the guide's
  existing skill-design coverage — distinct from what a skill's instructions
  say, this is about the vocabulary a skill introduces and whether that
  vocabulary stays consistent across a practitioner's whole skill set.

## Extraction Notes

- Fetched via WebFetch (URL content converted to markdown and processed by a
  fetch-time model). As with prior notes extracted the same way (e.g.
  `blog-humanlayer-show-me-skill.md`, `blog-simonwillison-liteparse-browser.md`),
  the first fetch returned a paraphrased summary rather than verbatim text.
  All quotes in this note were obtained through multiple follow-up targeted
  fetches, each requesting one short, specific, contiguous passage; quotes
  that came back with internal ellipses or spliced fragments (e.g. an
  initial attempt at the full four-ticket-type list, and an initial attempt
  at a "map" definition) were discarded or trimmed to their shortest
  quotable contiguous fragment rather than used as-is, per MINER.md §2a.
  No quote was reconstructed, tightened, or paraphrased and presented as
  verbatim.
- One requested passage — a single self-contained sentence defining what a
  "session" is in isolation — could not be obtained as a clean contiguous
  quote; Claim 3 uses the closest available contiguous quote (about what a
  *child session* needs) instead, and the "session" concept is otherwise
  covered via paraphrase in Claim 2's assessment, not fabricated as a quote.
- The article's four-ticket-type sentence is longer and more embedded than
  ideal for verbatim quoting in full; per MINER.md §2a Claim 5 quotes only
  the first, self-contained clause ("grilling tickets, which are just a
  grilling session") and paraphrases the remaining three types rather than
  quoting a reconstructed or spliced version of the full sentence.
- Metadata not independently verified beyond what WebFetch reported from the
  page itself: author byline (Richard MacManus), publication date
  (2026-08-20, consistent with the issue's auto-filed "Published: Thu, 20
  Aug 2026" field), and linked resources (aihero.dev/skills,
  github.com/mattpocock/skills, @mattpocockuk). These were not independently
  fetched/verified as live URLs and are reported here only as what the
  article itself states or links to.
- No contradiction with any existing source note was found; no contradiction
  issue was filed per MINER.md §4a.
- Confidence set to `anecdotal`: every claim in this source originates from
  the skill's own creator describing his own design choices and a single
  self-selected dogfooding example, with no independent verification,
  usage metrics, or outcome data of any kind.
