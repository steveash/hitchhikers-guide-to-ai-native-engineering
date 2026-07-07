---
source_url: https://simonwillison.net/2026/Jul/3/judgement/
source_type: blog-post
title: "Fable's judgement"
author: Simon Willison
date_published: 2026-07-03
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: anecdotal
issue: "#1617"
---

# Fable's judgement

> Simon Willison relays a tip from the Claude Code team (via a fireside chat
> with Cat Wu and Thariq Shihipar) and from Jesse Vincent: tell Fable to use
> its own judgement — about when to test, and about which lower-power model
> to delegate coding subagents to — rather than dictating fixed rules; Fable
> then wrote a persistent project-local memory file at
> `~/.claude/projects/<project>/memory/` codifying the delegation policy.

## Source Context

- **Type**: blog-post (simonwillison.net, July 3, 2026 — a very short "note"
  post, roughly 350 words across seven paragraphs, with one inline code
  block for the prompt given to Claude Code and one blockquote reproducing
  the full memory file Claude wrote in response.)
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  and the `llm` Python CLI. He is a trusted-feed source in this corpus with
  prior notes on Claude Fable 5's capabilities
  (`blog-simonwillison-claude-fable-5.md`) and its autonomous behavior
  (`blog-simonwillison-fable-relentlessly-proactive.md`). This post is a
  same-day first-person account: Willison attended a fireside chat he hosted
  with Cat Wu and Thariq Shihipar (described as "from the Claude Code team")
  at the AI Engineer World's Fair, then applied a related tip from Jesse
  Vincent to his own Claude Code session that same day. No Anthropic
  affiliation.
- **Scope**: Covers exactly one practitioner workflow change — telling Fable
  (and, per Willison, "to a certain extent Opus") to use its own judgement
  about testing and about model selection for subagents — and the memory
  file artifact Claude Code produced in response to a single prompt. Does
  NOT cover: any measured before/after outcome (the post is same-day and
  explicitly preliminary — "so far it seems to be working well"), the
  content of the Fireside Chat beyond the one testing example, or any detail
  about how Claude Code selects which "lower power model" to use in a
  subagent.

## Extracted Claims

### Claim 1: The Claude Code team's advice, relayed from a fireside chat, is to let Fable (and Opus, to a lesser extent) use its own judgement rather than dictating how they should work

- **Evidence**: Willison's direct account of a tip from a fireside chat he
  hosted with Cat Wu and Thariq Shihipar, described as "from the Claude Code
  team," at the AI Engineer World's Fair.
- **Confidence**: anecdotal (single secondhand relay of a conference
  conversation; no transcript or recording cited)
- **Quote**: "One of the most interesting tips I got from the Fireside Chat I
  hosted with Cat Wu and Thariq Shihipar from the Claude Code team at AIE on
  Wednesday was to let Fable (and to a certain extent Opus) use their own
  judgement rather than dictating how they should work."
- **Our assessment**: This is the framing claim for the whole post — an
  authority-sourced (Claude Code team members, per Willison) general
  principle that autonomy-by-judgement outperforms rule-dictation. It is
  stated as advice, not as measured outcome data; the two concrete
  applications that follow (testing, model selection) are Willison's own
  attempt to operationalize it, not part of the fireside chat's own examples
  beyond testing.

### Claim 2: Prescribing a fixed rule for when to run automated tests is worse than telling Fable to use its own judgement about when to write tests

- **Evidence**: The specific example Willison attributes to the fireside
  chat speakers, contrasting a literal instruction against a judgement-based
  instruction.
- **Confidence**: anecdotal (single example from a secondhand conference
  relay; no comparative data on outcomes)
- **Quote**: "The example they gave was testing. You can tell Fable \"only
  use automated testing for larger features, don't update and run tests for
  small copy or design changes\" - but it's better to just tell Fable to use
  its own judgement when deciding to write tests instead."
- **Our assessment**: This is a concrete, falsifiable-sounding claim but the
  post offers no evidence for *why* judgement-based instruction outperforms
  the rule ("only use automated testing for larger features...") — no
  outcome comparison, no error-rate data, just the assertion that the team
  prefers it. Worth flagging: this specific example is about test-authoring
  *judgement calls*, not about safety boundaries; it should not be read as
  advice to loosen prohibitions or "never" rules.

### Claim 3: Jesse Vincent's related tip is to tell Fable to delegate smaller tasks to other models, using Fable's own judgement about which model to use, in order to conserve tokens before an imminent price increase

- **Evidence**: Willison's direct attribution to Jesse Vincent, given the
  same day, tied explicitly to an approaching Fable price increase.
- **Confidence**: anecdotal (single secondhand tip, applied once, same day)
- **Quote**: "Jesse Vincent just gave me a related tip to help avoid burning
  too many of those valuable Fable tokens in the few days we have left
  before the prices go up. Tell Fable to use other models for smaller
  tasks, applying its own judgement about which model to use."
- **Our assessment**: The token-budget urgency ("the few days we have left
  before the prices go up") is a strong contextual signal for *why*
  Willison tried this now, but the post does not name the price change,
  its size, or its effective date. This should be treated as a
  time-bounded motivation, not a durable pricing fact — see Extraction
  Notes for what could not be verified from this source alone.

### Claim 4: Willison operationalized the advice with the literal prompt "For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent," given to Claude Code

- **Evidence**: The exact prompt text, reproduced as a code block in the
  post.
- **Confidence**: anecdotal (single prompt, single session, same-day report)
- **Quote**: "For all coding tasks use your judgement to decide an
  appropriate lower power model and run that in a subagent"
- **Our assessment**: This is the most directly reusable artifact in the
  post — a short, literal instruction practitioners can paste into their
  own CLAUDE.md or type into a session. Note what it does *not* specify:
  it names no model tiers, no cost thresholds, and no task-size boundary;
  it delegates that judgement entirely to Fable, consistent with Claim 1's
  framing principle.

### Claim 5: In response to the prompt, Claude Code wrote a persistent memory file to `~/.claude/projects/<project>/memory/delegate-coding-to-subagents.md`, without being explicitly told to persist the instruction

- **Evidence**: Willison's direct observation, with the file path and full
  file contents reproduced verbatim in the post.
- **Confidence**: anecdotal (single observed instance)
- **Quote**: "Claude saved this memory file in
  `~/.claude/projects/name-of-project/memory/delegate-coding-to-subagents.md`:"
- **Our assessment**: The prompt (Claim 4) asked Fable to *act* on a
  judgement policy; it did not ask Fable to *persist* that policy to disk.
  Fable's choice to write a standing memory file is itself a form of
  judgement — treating a one-off instruction as a durable project
  preference worth surviving future sessions. This is the first
  documentation in this corpus of the specific `~/.claude/projects/<project
  hash-or-name>/memory/` path being populated by Claude Code's own
  initiative from a plain-language instruction, rather than via an explicit
  `/memory` command or user-authored file. See Concrete Artifacts for the
  full file and Guide Impact for why this extends the corpus's existing
  persistence-location documentation.

### Claim 6: The memory file Fable wrote states, as its own rationale, that "implementation work rarely needs the top-tier model" and that judgment, review, and synthesis should stay with the main loop

- **Evidence**: Verbatim reproduction of the memory file's "Why" field,
  which is Fable's own generated text, not Willison's paraphrase.
- **Confidence**: anecdotal (a single model-generated artifact; this is
  Fable's self-authored justification, not an externally validated
  cost/quality finding)
- **Quote**: "**Why:** cost/efficiency — implementation work rarely needs
  the top-tier model; judgment, review, and synthesis stay with the main
  loop."
- **Our assessment**: This sentence is Fable's own generated policy
  statement, elevated to a persistent memory entry — it is evidence of how
  the model *interpreted* the delegation instruction, not independent
  evidence that the policy is correct. It is directly relevant to the
  question of which role (orchestrator vs. subagent) should run the more
  capable model — see Cross-References → Contradicts.

### Claim 7: The memory file's "How to apply" guidance further specifies that only substantive/mechanical implementation should route to subagents (sonnet for substantive work, haiku for trivial/mechanical edits), while design, auditing, data synthesis, and judgment-heavy work stay in the main model

- **Evidence**: Verbatim reproduction of the memory file's "How to apply"
  field.
- **Confidence**: anecdotal (single model-generated artifact from one
  session)
- **Quote**: "**How to apply:** when a task in this project is primarily
  writing/editing code, spawn an Agent with a model override (sonnet for
  substantive implementation, haiku for trivial/mechanical edits) and a
  self-contained prompt; review the result in the main loop before
  committing. Design, auditing, data synthesis, and anything judgment-heavy
  stays in the main model."
- **Our assessment**: This is a concrete two-tier subagent routing scheme
  (sonnet vs. haiku by task substantiveness) generated autonomously by
  Fable from a one-line instruction — it is more specific than the prompt
  that produced it (Claim 4), which named no model tiers. Practitioners
  should treat this as an example of what Fable *will* infer when given
  latitude, not as a vetted routing policy; it was written and applied in
  the same session, with no outcome data yet.

### Claim 8: Willison reports the approach "seems to be working well" the same day, with more work getting done and his Fable token allowance depleting more slowly than before

- **Evidence**: Willison's own subjective, same-day assessment; no
  quantitative before/after comparison given.
- **Confidence**: anecdotal (single practitioner, single day, no
  quantitative outcome data)
- **Quote**: "So far it seems to be working well. I'm getting a _ton_ of
  work done and my Fable allowance is shrinking less quickly than before."
- **Our assessment**: This is the weakest-evidenced claim in the post —
  "seems to be working" and "a ton of work" are qualitative, same-day
  impressions with no baseline comparison, cost figures, or task count.
  It should not be cited in the guide as a validated cost-saving result;
  it is a preliminary practitioner impression worth flagging for
  a follow-up source if Willison publishes a later assessment.

## Concrete Artifacts

### The prompt given to Claude Code (verbatim from the article)

```
For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent
```

*Source: Simon Willison, simonwillison.net/2026/Jul/3/judgement/*

### The memory file Claude Code wrote in response (verbatim from the article)

```
Path: ~/.claude/projects/name-of-project/memory/delegate-coding-to-subagents.md

---
name: delegate-coding-to-subagents
description: Simon wants coding tasks delegated to subagents running an appropriately lower-power model
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 30068d78-43a9-4fb1-bb29-9799e18c526a
---

Stated by Simon on 2026-07-03: "For all coding tasks use your judgement to
decide an appropriate lower power model and run that in a subagent."

**Why:** cost/efficiency — implementation work rarely needs the top-tier
model; judgment, review, and synthesis stay with the main loop.

**How to apply:** when a task in this project is primarily writing/editing
code, spawn an Agent with a model override (sonnet for substantive
implementation, haiku for trivial/mechanical edits) and a self-contained
prompt; review the result in the main loop before committing. Design,
auditing, data synthesis, and anything judgment-heavy stays in the main
model. See also [[project-goals]].
```

*Source: Simon Willison, simonwillison.net/2026/Jul/3/judgement/*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 6 (multiagent
    orchestration lets a lead agent break work into pieces and delegate to
    specialists with their own model, prompt, and tools): This source is a
    Claude Code (not Managed Agents) instance of the same underlying
    pattern — an orchestrating loop delegating implementation to
    model-scoped subagents — applied via a plain-language instruction
    rather than a platform feature.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 9 (multi-model routing —
    route planning to cheaper models, implementation to capable models —
    improves cost and quality, citing a MODEL_ROUTING.md pattern): This
    source corroborates that practitioners are actively pursuing
    task-to-model routing for cost reasons, and adds a concrete instance
    where the routing policy is self-generated by the model into a memory
    file rather than hand-authored by the practitioner into a routing
    document.

- **Contradicts**: See filed contradiction
    [steveash/hitchhikers-guide-to-ai-native-engineering#1627](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1627).
    `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 8 states, and
    the guide (04-context-engineering.md, "Model mixing across
    orchestration tiers") currently repeats as an explicit "Rule," that an
    orchestrator/subagent split should run the *orchestrator* on the
    cheaper/faster model and the *subagents* on the more capable model
    ("not the reverse" — citing Spiral/Every: lead agent on Haiku, drafting
    subagents on Opus). Claim 6 and Claim 7 in this source describe the
    literal reverse: the orchestrating main loop keeps the top-tier model
    (Fable) for judgment/review/synthesis, while subagents get downgraded
    to a lower-power model for implementation. Both claims answer the same
    "which role gets the capable model" question with opposite general
    prescriptions. No verdict is picked here — see the contradiction issue
    for a possible reconciling conditioning variable (task complexity
    rather than orchestrator/subagent role).

- **Extends**:
  - `blog-simonwillison-claude-fable-5.md` and
    `blog-simonwillison-fable-relentlessly-proactive.md`: Both prior notes
    document what Fable *can* do (knowledge depth, autonomous multi-step
    tool use); this source documents a specific operational instruction
    practitioners can give Fable to shape *how* it delegates its own work,
    and shows Fable persisting that instruction unprompted.
  - `docs-ghaw-repo-memory-reference.md` / `docs-ghaw-memory-ops.md` and
    related memory-ops notes: those document GitHub Agentic Workflows'
    repo-level memory system; this source documents Claude Code's own
    project-local memory file convention (`~/.claude/projects/<project>/memory/`),
    a distinct mechanism from a different harness, populated here by the
    model's own initiative rather than a workflow step.

- **Novel**:
  - **First in-corpus documentation of Claude Code writing an unprompted
    persistent memory file from a plain-language delegation instruction**:
    no existing source note shows Claude Code choosing, on its own
    initiative, to persist a one-off instruction as a standing
    `~/.claude/projects/<project>/memory/*.md` file with structured
    frontmatter (`name`, `description`, `metadata.type: feedback`,
    `originSessionId`).
  - **A concrete, reusable model-delegation prompt**: "For all coding tasks
    use your judgement to decide an appropriate lower power model and run
    that in a subagent" is short enough to be directly actionable, and its
    downstream effect (a two-tier sonnet/haiku routing policy) is fully
    documented.
  - **A named example of the `~/.claude/projects/<project>/memory/` path**:
    this path is not documented in the guide's existing "Where Claude Code
    customization lives" table (04-context-engineering.md), which lists
    only `.claude/commands/`, `~/.claude/commands`, and
    `.claude/agents/<name>.md` — see Guide Impact.

## Guide Impact

- **Chapter 04 (Context Engineering) — "Where Claude Code customization
  lives" table**: The existing table
  (source: `blog-sankalp-claude-code-20.md` Claim 4) does not include
  `~/.claude/projects/<project>/memory/` as a persistence location. Add a
  row for this path, citing this source, with the caveat (per Claim 5) that
  it can be populated by the model's own initiative, not only by explicit
  user action — which has implications for auditing what ends up as
  "persistent policy" versus a one-off remark.

- **Chapter 04 (Context Engineering) — "Model mixing across orchestration
  tiers"**: Do not silently update the existing "Rule" to match this
  source. File and cite the contradiction
  (steveash/hitchhikers-guide-to-ai-native-engineering#1627): the current
  guide text states an unconditional "orchestrator = cheap, subagent =
  capable" rule sourced from a single production case; this source is a
  same-day anecdote showing the literal reverse. Until the contradiction is
  resolved, if this section is touched, flag both examples and note the
  possible task-complexity conditioning variable described in the
  contradiction issue rather than picking a side.

- **Chapter 01 (Daily Workflows) — "Multi-Model Cooperation" / delegation
  sections**: Add the exact prompt from Claim 4 as a copy-pasteable example
  of judgement-based (as opposed to rule-based) delegation instruction,
  alongside the caveat from Claim 2 that this pattern is about
  operational/test-authoring judgement calls, not a license to loosen
  safety prohibitions.

## Extraction Notes

- The source is a very short "note" post (~350 words, seven paragraphs).
  I read the entire post, including the reproduced memory file, and did not
  find sub-pages worth following: the only outbound link is to the AI
  Engineer World's Fair schedule page for the referenced Fireside Chat
  session (a conference schedule entry, not a substantive source in its own
  right).
- WebFetch's summarizing model refused full verbatim reproduction on first
  attempt (copyright policy) and returned only a paraphrase. I fetched the
  raw HTML directly via `curl` and extracted the article's `<div
  class="entry entryPage">` content by hand, which is the single source for
  every quote in this note — all quotes were verified against that raw HTML,
  not against WebFetch's paraphrased or "exact quote" responses, which
  differed in minor wording from the actual HTML in at least one case
  (WebFetch initially rendered the "Fireside Chat" quote with a
  fabricated present-tense framing not present in the source).
- Only 8 claims were extracted, below the template's suggested 5-15 range.
  This reflects the source's genuine length (~350 words) rather than
  shallow reading — every substantive sentence in the post is represented
  by a claim or a concrete artifact above; there is no further material to
  extract.
- The post gives no name, size, or effective date for "the prices go up"
  (Claim 3) beyond "the few days we have left" — I did not find or fetch a
  separate Anthropic pricing announcement to fill this gap, since none was
  linked from the source itself. A future source note on the actual Fable
  price change (if/when one is mined) should cross-reference this note.
- Cross-references verified:
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 8: confirmed
    at line 172 of that note ("Mixing models across orchestration levels is
    a concrete cost-optimization pattern — Spiral uses Haiku for the lead
    orchestrator agent and Opus for specialist drafting subagents").
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 6: confirmed
    at line 132 of that note (multiagent orchestration, lead agent
    delegates to specialists with their own model/prompt/tools).
  - `blog-addyosmani-code-agent-orchestra.md` Claim 9: confirmed at lines
    81-86 of that note (multi-model routing, MODEL_ROUTING.md pattern).
  - `guide/04-context-engineering.md` "Model mixing across orchestration
    tiers" section (lines 365-387): confirmed the guide currently states
    the cheap-orchestrator/capable-subagent rule as unconditional, sourced
    to `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 8.
  - `guide/04-context-engineering.md` "Where Claude Code customization
    lives" table (lines 441-461): confirmed it does not list
    `~/.claude/projects/<project>/memory/` among the documented persistence
    locations.
- Contradiction filed: steveash/hitchhikers-guide-to-ai-native-engineering#1627,
  before opening this PR, per MINER.md §4a. No verdict picked in this note.
