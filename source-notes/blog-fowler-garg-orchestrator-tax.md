---
source_url: https://martinfowler.com/articles/orchestrator-tax.html
source_type: blog-post
title: "The Orchestrator's Tax"
author: Rahul Garg (Principal Engineer, Thoughtworks)
date_published: 2026-07-28
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2293"
---

# The Orchestrator's Tax

> Garg's incident-driven argument that subagents are justified by what they
> keep out of the orchestrator's context, not by time saved or parallel
> execution — introducing "cognitive locality" (partition work by shared
> mental model, not by task) and four standing CLAUDE.md rules derived from
> a real four-subagent .NET refactor session, explicitly framed as
> exploratory rather than settled.

## Source Context

- **Type**: blog-post (martinfowler.com, published under Martin Fowler's
  "articles" section, dated 28 July 2026)
- **Author credibility**: Rahul Garg is a Principal Engineer at Thoughtworks,
  based in Gurgaon, India, per the article's own byline bio ("passionate
  about the craft of building maintainable software through DDD and Clean
  Architecture, and explores how AI can help teams achieve engineering
  excellence"). Published on martinfowler.com with Martin Fowler credited
  for "guidance and feedback throughout." This is first-person practitioner
  reflection on a single real incident, not a controlled study — the author
  repeatedly and explicitly flags his own claims as unmeasured (see Claim 3
  below) and frames the whole piece as "exploratory work... built from one
  real incident, and it ends with more open questions than settled answers"
  (article abstract).
- **Scope**: Covers one Claude Code session (four concurrent subagents on a
  .NET response-pipeline refactor) analyzed via the orchestrator critiquing
  its own delegation decisions, the resulting "cognitive locality" concept,
  four standing CLAUDE.md rules derived from the incident, and a second,
  separate incident about subagents not inheriting active skills. Does NOT
  cover: instrumented per-call token accounting (the author states this
  explicitly was not available), a benchmark or controlled comparison of
  delegation strategies, or guidance for any coding agent besides Claude
  Code (the CLAUDE.md thresholds are stated as calibrated specifically
  against "Claude Sonnet 5").

## Extracted Claims

### Claim 1: Subagents should be justified by what they keep out of the orchestrator's context, not by time saved or parallel execution
- **Evidence**: Stated as the article's central thesis in the abstract and
  restated in the body as the author's "working belief."
- **Confidence**: emerging
- **Quote**: "Every token in the orchestrator's context is competing for its attention, and the real value of a subagent is what it keeps out of that context, not how fast it runs."
- **Our assessment**: This is the organizing claim the rest of the piece
  builds toward. It reframes the standard "N agents in parallel = N-times
  speedup, minus duplication cost" mental model as measuring the wrong
  variable — throughput — when the scarcer resource is what the orchestrator
  carries forward in context. The author is careful to label this a
  "working belief," not a measurement (see Claim 1 restated later: "That's a
  belief, though, not a measurement. What I've actually measured is the
  other side of it, the cost of getting the isolation wrong.") — an
  important qualifier that should travel with this claim into the guide.

### Claim 2: The four-subagent session did produce a real wall-clock speedup from parallelism (~12 minutes vs. an estimated ~25 minutes serialized)
- **Evidence**: Author's own timing observation of the incident, offered
  before he pivots to arguing speed wasn't the interesting variable.
- **Confidence**: anecdotal
- **Quote**: "Three tasks ran concurrently, so wall-clock time was around twelve minutes instead of something closer to twenty-five if the work had been serialized."
- **Our assessment**: This is worth extracting on its own because it shows
  the author isn't denying parallelism has value — he explicitly concedes
  the speedup was real ("Parallelism still matters here, it's just not the
  main point... Running four agents concurrently is useful, but ordinary.")
  before arguing a different, larger cost was hiding underneath it. The
  guide should not overstate Claim 1 into "parallelism doesn't matter" —
  the author's own numbers show it does, just less than the context cost.

### Claim 3: The largest observed cost was the orchestrator itself importing a subagent's full raw transcript (tens of thousands of tokens) into the main thread when checking status — but the author explicitly flags this specific ranking as unmeasured, not a settled fact
- **Evidence**: First-person incident account plus an explicit
  self-correcting caveat paragraph immediately following the claim.
- **Confidence**: anecdotal (the author's own confidence label, stated
  directly in the source)
- **Quote**: "Instead of a lightweight summary, the tool it used pulled back the full raw transcript of a background agent: tens of thousands of tokens of JSONL, intermediate reasoning, and tool output, imported wholesale into the main thread." / "I didn't have real per-call token accounting, so treat that ranking as the orchestrator's account, not a measured fact. The trustworthy part is narrower: the transcript dumps were real, the wall-clock timings were real, and the status-check path clearly introduced a large, avoidable cost. Whether it was the single largest cost remains a hypothesis until the tooling can instrument it properly."
- **Our assessment**: This self-flagged epistemic caveat is itself worth
  extracting as a claim, not just a footnote — the "which cost was
  biggest" ranking came from asking the orchestrator to grade its own
  session, and the author explicitly refuses to treat that self-report as
  measured fact. Any guide text citing this incident should carry the same
  caveat: the *existence* of the transcript-dump cost is well-evidenced: the
  *ranking* of it as the single largest cost is not.

### Claim 4: Two of the four subagents were independently reconstructing the same mental model of the codebase because work had been partitioned by task rather than by the knowledge each task required — a distinction Garg names "cognitive locality"
- **Evidence**: Incident analysis plus an explicitly coined, defined term.
- **Confidence**: anecdotal
- **Quote**: "It was two agents independently reconstructing the same mental model of the codebase, because the work had been partitioned by task rather than by the knowledge each task required. I've started calling that distinction cognitive locality: Tasks that need the same mental model should usually stay together. Splitting them just forces multiple agents to rebuild the same understanding from scratch."
- **Our assessment**: This is the piece's most reusable named concept. It
  directly corroborates, under new terminology, `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 13's "Context-Centric Decomposition" principle ("Divide work by what
  context each agent needs rather than by what type of work it does") —
  two independent sources, one vendor-authoritative and one practitioner,
  converge on the same partitioning rule from different incidents. "Cognitive
  locality" is a more memorable label for the same underlying rule and is
  worth citing alongside Anthropic's framing rather than replacing it.

### Claim 5: One subagent ran repository-wide git operations (`git stash` / `git stash pop`) while sibling subagents were writing elsewhere in the same tree — nothing broke, but the risk was structural
- **Evidence**: Direct incident observation.
- **Confidence**: anecdotal
- **Quote**: "one agent ran git stash and git stash pop while sibling agents were writing elsewhere in the same tree. Nothing broke, but the risk was structural, because repository-wide operations are perfectly reasonable in a single-threaded session and become much harder to justify the moment multiple writers are active at once."
- **Our assessment**: A concrete, checkable near-miss rather than a
  measured failure — "nothing broke" is explicitly stated, so this should
  be cited as a structural-risk warning, not as an incident with an actual
  bad outcome. It is the direct source for standing rule 3 in Claim 9 below.

### Claim 6: Context pollution is a categorically different kind of cost from token spend — tokens are paid once, but polluted context is carried forward and taxes every subsequent turn
- **Evidence**: Author's own reframing of why the transcript-dump incident
  bothered him beyond its one-time token cost.
- **Confidence**: anecdotal
- **Quote**: "A token bill is one-time, you pay it and it's over. What happened here was different. The raw transcript stayed in the orchestrator's context after the tool call completed, and every turn after that carried it forward, whether or not it was still useful." / "Tokens are spent once. Context shapes every decision that follows."
- **Our assessment**: This is the piece's clearest general-purpose framing
  distinction and the one most transferable outside this specific incident.
  It gives practitioners a vocabulary for arguing that a "small" one-time
  context addition can be more expensive than its token count suggests, if
  it stays resident and irrelevant for the rest of a long session.

### Claim 7: A larger context window does not fix the attention-competition problem — more content sitting in context, regardless of how much room remains, makes it harder for the model to identify what currently matters
- **Evidence**: Author's stated generalization following the token-vs-context
  distinction (Claim 6).
- **Confidence**: anecdotal
- **Quote**: "The more that's sitting in context, competing for attention, the harder it gets for a model to pick out what matters right now, even with plenty of room still free. A bigger context window doesn't fix that. It just gives the noise more room to pile up before anyone notices."
- **Our assessment**: This corroborates `blog-humanlayer-long-context-isnt-the-answer.md`
  Claim 8 (context isolation beats context expansion for staying in the
  model's "smart zone") and Claim 9 (degradation observed even well within
  what would be considered a safe operating range for a smaller-window
  model) from an independent incident and independent vendor context —
  two practitioner sources now separately argue that window *size* and
  usable attention are different properties, though neither offers a
  quantified measurement of the effect.

### Claim 8: The orchestrator is the only part of a multi-agent system that accumulates understanding across a long session; subagents are meant to be disposable, and their noisy intermediate reasoning is supposed to stay in worker contexts rather than returning to the main thread
- **Evidence**: Author's stated architectural framing, following directly
  from Claims 6–7.
- **Confidence**: anecdotal
- **Quote**: "the orchestrator is the only part of the system that accumulates understanding across a long session. It remembers why a design decision was made, carries forward architectural constraints, and knows which trade-offs have already been discussed. The subagents don't, and that's by design. They are supposed to be disposable. Exploration, repeated file reads, failed approaches, and noisy intermediate reasoning are meant to stay in worker contexts and never make the trip back to the main thread."
- **Our assessment**: This directly corroborates `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 6's "context firewall" framing of subagents (isolation for noise
  containment, not role specialization) — two independent practitioner
  sources converge on subagents' primary value being containment of
  disposable reasoning, not division of labor by role.

### Claim 9: Four standing CLAUDE.md rules were derived from the incident, each testing whether a piece of information or work-split "earns a place" in the orchestrator's context
- **Evidence**: Author's own encoded rule list, explicitly framed as a
  compressed response to the specific failures observed (status polling,
  duplicated orientation, unsafe concurrent git operations).
- **Confidence**: anecdotal
- **Quote**: "Prefer two to four agents in one wave. If the orchestrator wants five or more, it should first ask whether tasks sharing files or conventions ought to be merged." / "Do not poll background agents for status when the answer can be given from what is already known. Do not fetch a full transcript to answer a lightweight question." / "Do not allow repository-wide git operations inside concurrent agent prompts." / "Treat overlapping file ownership as a consolidation signal, not a cue to spawn more agents."
- **Our assessment**: These are the article's single most directly
  adoptable artifact — see Concrete Artifacts below for the rules verbatim
  as a set. The author is explicit that these are calibrated to his own
  workflow and model ("calibrated against Claude Sonnet 5... I wouldn't
  present them as anything like universal constants"), so the guide should
  present the specific numeric thresholds (2–4 agents, 5 as a consolidation
  trigger) as one practitioner's calibration, not a general rule, while the
  four underlying *questions* (poll or not, split-or-merge, git-scope, file
  overlap) are more broadly transferable.

### Claim 10: A subagent does not automatically inherit skills active in the parent session — the orchestrator must explicitly pass them along
- **Evidence**: A second, separate incident described later in the article,
  distinct from the four-subagent refactor session.
- **Confidence**: anecdotal
- **Quote**: "I assumed that once a skill was active in the main thread, spawned subagents would follow it automatically. They don't. A subagent doesn't inherit skills active in the parent session unless the orchestrator passes them along explicitly."
- **Our assessment**: This is a concrete, checkable mechanical fact about
  subagent/skill propagation rather than a design opinion — it's the kind
  of "gotcha" that's easy to assume works and silently doesn't. Worth
  flagging directly in any guide section describing how to spawn subagents
  alongside active skills.

### Claim 11: The author rejected a "confirm-before-spawn" governance gate he initially designed, on the grounds that it solved the wrong problem — a missing fact should become a stated rule, not a checkpoint or approval ritual
- **Evidence**: Author's own account of designing, then discarding, a
  stricter governance mechanism, plus the resulting general heuristic he
  says he now uses more than the specific rule.
- **Confidence**: anecdotal
- **Quote**: "I didn't have evidence that bad spawn plans were slipping through for lack of a confirmation step. I'd discovered a missing fact about skill propagation, and that's a different kind of gap. A universal confirmation gate would have added a round-trip to every similar session, and before long I'd almost certainly have started approving those prompts on autopilot." / "Before adding a line to a standing instruction file, ask whether a reasonably competent orchestrator would make the right decision once it knew the one missing fact." / "If the fix starts specifying a decision procedure, such as approvals, checkpoints, mandatory steps, that's usually a sign I'm encoding process where a small clarification would have done the job."
- **Our assessment**: This is a distinct, transferable governance heuristic
  for standing-instruction-file design generally — not specific to
  multi-agent orchestration. It gives practitioners a test for over-
  engineering CLAUDE.md rules: does the fix add a fact, or does it add a
  ritual? The author explicitly flags this as untested against harder
  cases ("I don't know yet whether that heuristic survives harder cases").

### Claim 12: The author proposes, as a tentative and explicitly unsettled hypothesis, that the quality of the orchestrator's own working memory may be a third resource worth tracking in long-running agent workflows, after CPU/memory/throughput and token counts
- **Evidence**: Closing synthesis statement.
- **Confidence**: anecdotal (author's own stated confidence: "I don't think that's a settled law yet. It's a pattern that held up in the sessions I've looked at so far.")
- **Quote**: "For years we optimized software systems around CPU, memory, and throughput. The first wave of LLM tooling taught us to watch tokens. This session made me suspect there's a third thing worth watching in long-running agent workflows: the quality of the orchestrator's own working memory, the one resource that, once polluted, keeps charging rent for the rest of the session."
- **Our assessment**: This is the article's broadest, least-supported claim
  — a single-incident hypothesis explicitly not claimed as settled. It is a
  useful framing device for the guide but should be presented as a proposed
  lens, not an established metric category, consistent with the article's
  own hedge.

## Concrete Artifacts

### The four standing CLAUDE.md rules (verbatim, numbered list)
```
Source: martinfowler.com/articles/orchestrator-tax.html, "Turning a Session into Standing Rules"

1. Prefer two to four agents in one wave. If the orchestrator wants five or
   more, it should first ask whether tasks sharing files or conventions ought
   to be merged.
2. Do not poll background agents for status when the answer can be given
   from what is already known. Do not fetch a full transcript to answer a
   lightweight question.
3. Do not allow repository-wide git operations inside concurrent agent
   prompts.
4. Treat overlapping file ownership as a consolidation signal, not a cue to
   spawn more agents.
```

### Article section structure (headings, in order)
```
Source: martinfowler.com/articles/orchestrator-tax.html

1. (intro, unheaded)
2. The Incident Was Not Really About Parallelism
3. The Costs Were Not All the Same
4. The Scarce Resource Is the Orchestrator's Working Memory
5. Cognitive Locality Changes What Parallelism Is For
6. Turning a Session into Standing Rules
7. The Next Mistake Would Have Been More Governance
8. Where This Leaves Me
Appendix: Related Work; Acknowledgments
```

### The narrower skill-propagation fix that replaced the rejected confirm-gate (verbatim)
```
Source: martinfowler.com/articles/orchestrator-tax.html, "The Next Mistake Would Have Been More Governance"

"Before spawning, the orchestrator states which active skills are relevant
to each agent's task and points the subagent at the skill file to load,
rather than pasting the whole skill inline. Confirmation is only required
above the same batch-size threshold already in place, or when file
ownership is ambiguous."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 13
    (Context-Centric Decomposition: "Divide work by what context each agent
    needs rather than by what type of work it does") — this source's
    Claim 4 ("cognitive locality") independently arrives at the identical
    partitioning rule under different terminology, from a practitioner
    incident rather than vendor design guidance. Two independent sources,
    one authoritative/vendor and one practitioner, now converge on
    partition-by-context-need over partition-by-task-type.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 6 (sub-agents
    work as a "context firewall" for isolating noise, not role
    specialization) — this source's Claim 8 (subagents are "supposed to be
    disposable," their noisy reasoning meant to stay in worker contexts)
    independently corroborates the same containment-not-specialization
    framing of subagent value.
  - `blog-humanlayer-long-context-isnt-the-answer.md` Claim 8 (context
    isolation beats context expansion; sub-agents keep windows "in the
    smart zone") and Claim 9 (degradation observed well within what would
    be a safe range for a smaller window) — this source's Claim 7 (a bigger
    context window doesn't fix attention competition; it "just gives the
    noise more room to pile up") makes the same window-size-is-not-the-
    same-as-usable-attention argument from an independent incident.

- **Contradicts**: None identified. Checked against
  `blog-anthropic-multi-agent-coordination-patterns.md`,
  `blog-humanlayer-skill-issue-harness-engineering.md`,
  `blog-humanlayer-long-context-isnt-the-answer.md`,
  `blog-humanlayer-context-forking.md`, and
  `blog-cognition-multi-agents-working.md` — no existing note asserts that
  periodic full-transcript status polling of background subagents is
  beneficial or that context window size alone resolves attention
  competition, which would be the direct opposite of this source's central
  claims. No contradiction issue filed per MINER.md §4a.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3
    (orchestrator-subagent's named failure mode is an "information
    bottleneck" when subagents' cross-cutting findings can't be routed
    back efficiently) — this source names a different, additive failure
    mode of the same pattern: the orchestrator itself polluting its own
    context by over-fetching subagent status (Claim 3 here), which is a
    failure of the orchestrator's own behavior rather than lost inter-
    subagent findings.
  - `blog-humanlayer-context-forking.md` Claim 3 (context windows only
    permit push/pop from the newest end; no random access into the middle)
    — this source's transcript-dump incident (Claim 3/6 here) is a
    concrete illustration of the cost of *not* using a fork/rewind to
    discard a polluting addition once it's been pushed onto the stack; the
    two sources together suggest forking as a plausible mitigation this
    article's author does not himself mention.

- **Novel**:
  - **"Cognitive locality" as a named term** for partitioning subagent work
    by shared mental-model requirements — the underlying principle exists
    elsewhere (Anthropic's context-centric decomposition), but this specific
    coinage and its incident-grounded derivation are new to the corpus.
  - **Tokens-vs-context as two distinct cost categories** ("tokens are
    spent once, context shapes every decision that follows") — no prior
    corpus source draws this specific one-time-cost-vs-compounding-cost
    distinction this explicitly.
  - **Explicit epistemic self-correction of a vendor/practitioner's own
    incident ranking** (Claim 3) — the author naming his own "biggest cost"
    claim as the orchestrator's unverified self-report rather than a
    measured fact is a notably more disciplined evidentiary posture than
    most first-party incident write-ups in this corpus.
  - **The governance-restraint heuristic** (Claim 11: "would a reasonably
    competent orchestrator make the right call if it knew the one missing
    fact?") as a general test for whether a standing-instruction-file
    addition should be a stated fact or a procedural gate — not specific to
    multi-agent design and not previously named in this corpus.
  - **Subagent skill non-inheritance** (Claim 10) as a specific, checkable
    mechanical behavior — not previously documented in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Chapter 04 (Context Engineering)**:
  Add "cognitive locality" (Claim 4) as a named heuristic for subagent task
  decomposition, presented alongside `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 13's context-centric decomposition principle as two independently
  arrived-at statements of the same rule: partition subagent work by shared
  knowledge/mental-model requirements, not by superficial task category.

- **Chapter 02 (Harness Engineering)**: Add the four standing rules (Claim 9,
  Concrete Artifacts) as a practitioner-derived example rule set for
  orchestrator/subagent CLAUDE.md configuration — explicitly caveat the
  numeric thresholds (2–4 agents, 5 as a consolidation trigger) as one
  author's calibration against a specific model (Claude Sonnet 5) and
  workflow, not a universal constant, per the author's own explicit
  disclaimer.

- **Chapter 04 (Context Engineering)**: Add the tokens-vs-context
  distinction (Claim 6) and the "bigger window doesn't fix attention
  competition" claim (Claim 7) as a named framing, cross-referenced with
  HumanLayer's "instruction budget"/"smart zone" concept
  (`blog-humanlayer-long-context-isnt-the-answer.md`) as a second,
  independent source making a structurally similar argument.

- **Chapter 02 (Harness Engineering)**: Add subagent skill non-inheritance
  (Claim 10) as a checkable gotcha in any section describing subagent
  spawning alongside active skills — the orchestrator must explicitly pass
  along which skills are relevant and point the subagent at the skill file,
  rather than assuming automatic inheritance.

- **Chapter 00/01 (Principles) or wherever standing-instruction-file design
  guidance lives**: Add the governance-restraint heuristic (Claim 11) as a
  named test before adding a new CLAUDE.md rule: does the fix supply a
  missing fact, or does it specify a decision procedure (approvals,
  checkpoints, mandatory steps)? The latter is a signal of over-engineering
  a clarification into a ritual.

- **Any chapter citing this incident's specific cost ranking**: Explicitly
  carry the author's own caveat (Claim 3) that "status polling cost more
  than the duplication tax of four agents" is the orchestrator's
  self-report, not a measured fact — cite the existence of the
  transcript-dump cost, not its rank, as the evidenced part.

## Extraction Notes

- WebFetch's summarizing pass on this URL returned only a condensed,
  paraphrased ~250-word summary (consistent with the copyright-caution
  behavior already documented in this corpus's other source notes, e.g.
  `blog-cognition-multi-agents-working.md` and
  `blog-humanlayer-skill-issue-harness-engineering.md` Extraction Notes).
  The full article was instead fetched via `curl` with a browser
  user-agent, and all quotes above were taken directly from that raw HTML
  and cross-checked against the WebFetch summary for consistency — no
  discrepancy was found beyond the expected loss of direct quotes in the
  summary.
- The article's "Related Work" section links to Fowler's own "Context
  Anchoring" article (martinfowler.com/articles/reduce-friction-ai/context-anchoring.html)
  as covering context-as-scarce-resource "from a different angle," and the
  "Acknowledgments" section credits Birgitta Böckeler's "Harness
  Engineering" article (martinfowler.com/articles/harness-engineering.html)
  for naming the feedforward/feedback loop this piece's CLAUDE.md-updating
  practice follows. Neither was fetched as a separate source for this
  extraction (both are referenced only briefly, for framing/credit, not
  developed as claims within this article) — a grep of `source-notes/` for
  `harness-engineering.html` and for `Böckeler`/`Boeckeler` found no
  existing note for either (the one Böckeler match in this corpus,
  `blog-fowler-boeckeler-local-models-viability.md`, is a different article
  about local-model viability, not harness engineering). Both are flagged
  here as candidates for future separate source submissions.
- The author's linked CLAUDE.md gist (gist.github.com/techygarg/...) was
  not separately fetched: it is an external, mutable, unversioned document
  the article itself describes as "not a finished prescription... a sample,
  not a template," and its content beyond the four rules already quoted
  verbatim in the article body is out of scope for this extraction.
- No contradiction was identified against the existing corpus meeting the
  MINER.md §4a bar (see Cross-References → Contradicts); none filed.
- Confidence set to `emerging`: the article is explicitly self-described as
  "exploratory work... built from one real incident," with its most
  striking specific claim (context pollution costing more than duplication)
  explicitly flagged by the author as an unmeasured self-report. The
  conceptual contributions (cognitive locality, tokens-vs-context framing,
  the governance-restraint heuristic) are novel and corroborated in part by
  independent sources, but the evidentiary base is a single incident with
  no instrumentation, which keeps this below `settled`.
