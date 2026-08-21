---
source_url: https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/understanding-agents-their-five-controllers-and-one-graph
source_type: blog-post
title: "Understanding agents, their five controllers and one graph"
author: Zichuan Xiong
date_published: 2026-08-13
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2840"
---

# Understanding Agents, Their Five Controllers and One Graph

> Thoughtworks essay defining an agent as "a delegation of human judgment" and
> proposing a five-part taxonomy of structural mechanisms — Prompt,
> Instruction, Skill, Recipe, Loop — that encode human judgment into an
> agent's behavior, plus a sixth, non-controller element (the "graph") that
> grounds all five in shared, persistent institutional memory.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Machine learning and AI"
  category; published August 13, 2026; discovered via the trusted
  `thoughtworks` RSS feed). A conceptual/framework essay structured around
  eight sections in order: "The five controllers" (intro), "Prompts set the
  boundary," "Instructions direct the aim," "Skills replay experience,"
  "Recipes orchestrate and gate skills," "Loops correct against an external
  signal," "The graph grounds the controllers," and "Summary." The article
  includes one embedded diagram ("Figure 1. The five controllers and one
  graph") but no code, config, or metrics artifacts.
- **Author credibility**: Zichuan Xiong's Thoughtworks profile (verified in
  the prior source note `blog-thoughtworks-xiong-data-agents-context-resolution.md`)
  lists his title as **Global Head of AIOps, Thoughtworks Managed Services**,
  with 18 years of experience in "agentic AIOps and SRE modernization." This
  is his fourth source-note-worthy publication in this corpus within roughly
  a month, following two solo/co-authored pieces on ontology and data-agent
  context resolution (`blog-thoughtworks-xiong-ontology-llm-data-modernization.md`,
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`,
  `blog-thoughtworks-xiong-data-agents-context-resolution.md`). Those three
  pieces are narrowly scoped to data agents and semantic/ontology modeling;
  this piece is a broader, general-purpose agent-architecture essay — a
  different register from his prior data-focused work, though it reuses his
  recurring interest in persistent, structured knowledge (the "graph," here
  applied to agent control generally rather than data semantics
  specifically).
- **Scope**: Covers a five-part taxonomy of agent control mechanisms (Prompt,
  Instruction, Skill, Recipe, Loop), their individual definitions, failure
  modes, and one worked example (a repo-hygiene remediation skill/recipe
  pair) illustrating Skill and Recipe together. Also covers a sixth,
  explicitly non-controller element (the "graph") as persistent institutional
  memory, referencing an external DeepLearning.AI course
  ("Agentic Knowledge Graph Construction") without a URL. Does NOT cover:
  named case studies, named organizations that have implemented this
  taxonomy, metrics, code/config artifacts, or a worked example for the
  Prompt, Instruction, Loop, or graph concepts (only Skill and Recipe get the
  repo-hygiene walkthrough).

## Extracted Claims

### Claim 1: An agent is defined as a delegation of human judgment — authorizing the agent to decide something in a real-world case means handing over the judgment the task requires, not just the task itself
- **Evidence**: Author's opening definitional framing, presented as the premise the rest of the article's taxonomy is built to support.
- **Confidence**: emerging (a definitional/framing claim, not measured, but load-bearing for the article's entire argument)
- **Quote**: "An agent is a delegation of human judgment. You authorize it to decide something in a real-world case, what you hand over is not a task but the judgment the task requires."
- **Our assessment**: This is a compact, quotable framing that sharpens a distinction already present in this corpus in more diffuse form — that granting an agent capability is different from granting it decision-making authority. It converges conceptually with `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 8 ("delegation requires more than permission; it requires a model of competence, risk and consequence"), though the two articles are independent (different authors, same publisher, roughly a week apart) and use different vocabulary to reach a similar premise. Treat as framing vocabulary, not a measured finding.

### Claim 2: Delegating any judgment to an agent immediately creates a fidelity requirement — the agent must act faithfully to the judgment it was handed
- **Evidence**: Author's direct statement following the opening definition, presented as the reason the five controllers exist at all.
- **Confidence**: emerging (definitional, not measured)
- **Quote**: "The moment you delegate any judgment, one need follows immediately: the agent must act faithfully."
- **Our assessment**: This is the article's stated justification for the entire controller taxonomy — each of the five controllers is later framed as a distinct mechanism for encoding or enforcing this fidelity requirement. Useful as the "why" a guide section on agent control should open with before introducing the five mechanisms themselves.

### Claim 3: A Prompt declares an agent's boundaries (role, permissions, hard limits) but only declares — it cannot enforce, because a prompt the model can read is also a prompt the model can ignore
- **Evidence**: Author's definition and stated limitation under "Prompts set the boundary."
- **Confidence**: emerging (an architectural claim about LLM behavior, consistent with widely-documented prompt-injection and instruction-override failure modes elsewhere in AI-safety literature, but not independently measured in this article)
- **Quote**: "A Prompt declares an agent's boundaries, defining what it is and isn't: its role, its permissions, its hard limits."
- **Quote** (the limitation): "But a prompt the model can read is a prompt the model can ignore, so it declares without ever enforcing."
- **Our assessment**: This is a precise, quotable statement of a limitation this corpus already treats seriously in other terms (prompt-based guardrails are advisory, not enforced) but had not previously seen phrased this tightly. Directly relevant to any guide discussion of why system-prompt-level constraints are necessary but insufficient for safety — they need to be paired with mechanisms that actually enforce (tool permissions, sandboxing) rather than merely declare.

### Claim 4: An Instruction defines where to point and what good looks like (style, priorities, standing preferences) — it is deliberately open-ended because many valid paths can reach the same aim, but for that same reason it is the slowest layer, since static guidance cannot react in real time
- **Evidence**: Author's definition and stated trade-off under "Instructions direct the aim."
- **Confidence**: emerging
- **Quote**: "An Instruction defines where to point and what good looks like: style, priorities, standing preferences."
- **Quote** (the trade-off): "open-ended, because many valid paths reach the same aim" and "the slowest layer, and static guidance cannot react in real time"
- **Our assessment**: This maps closely onto the guide's existing "What to Put in CLAUDE.md" material (Chapter 02) — an Instruction, in this taxonomy, is essentially what a CLAUDE.md/AGENTS.md standing-preferences section encodes. The "slowest layer" framing is a useful addition: it names *why* instructions alone are insufficient for time-sensitive correction, motivating the need for the Loop controller (Claim 8 below) as a complementary, reactive mechanism.

### Claim 5: A Skill is packaged expertise for a single action, pre-committed and applied before anything goes wrong — what makes it a skill is not the tool it uses but the pre-committed procedure itself; it is fast and cheap because it does not deliberate, but for the same reason it is blind, acting on a fixed assumption
- **Evidence**: Author's definition and worked example under "Skills replay experience" — a repo-hygiene remediation skill.
- **Confidence**: emerging
- **Quote**: "A Skill is that packaged expertise for a single action, applied before anything goes wrong."
- **Quote** (what makes it a skill): "the tool is not what makes it a skill, the pre-committed procedure is."
- **Quote** (the trade-off): "Skill is fast and cheap because it does not deliberate. And for the same reason it is blind: it acts on a fixed assumption."
- **Our assessment**: This is a materially different definition of "skill" than the one this corpus already documents in `blog-anthropic-claude-code-skills-lessons.md` — that note describes Claude Code Skills as a specific product feature (folders with markdown, scripts, assets, a description field acting as a model-facing trigger). Xiong's "Skill" is a more abstract architectural category (any pre-committed, non-deliberative procedure for a single action) that Claude Code Skills would be one *implementation* of, not a synonym. Worth flagging in a guide section so the two uses of "skill" aren't conflated: one is a product feature, the other is a general control-mechanism category in an architectural taxonomy.

### Claim 6: A Recipe orchestrates skills, gating them across the branching scenarios of a more complex task — but it shares the Skill's blindness, handling only the situations its gates anticipated, and is specifically vulnerable to mis-routing when a gate aims the right skill at the wrong problem
- **Evidence**: Author's definition, worked example (repo-hygiene recipe with three conditional branches), and stated failure mode under "Recipes orchestrate and gate skills."
- **Confidence**: emerging
- **Quote**: "A Recipe is the orchestrator of skills, gating them for the branching scenarios of a more complex task."
- **Quote** (the limitation): "it shares the skill's blindness: it handles only the situations its gates anticipated" and the named failure mode, "mis-routing, when a gate aims the right skill at the wrong problem."
- **Our assessment**: The three-branch repo-hygiene recipe example (flagged dependency → remediation skill; failing lint rule → lint-fix skill; secret in git history → stop and escalate to a human) is a concrete, reusable illustration of the Recipe/Skill relationship, and specifically models a "know when to escalate rather than auto-remediate" pattern already valued elsewhere in this corpus's safety material (e.g., the escalation-threshold examples in `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`). The named "mis-routing" failure mode is a citable, specific risk for any guide discussion of gated/branching agent workflows.

### Claim 7: A Loop is the only one of the five controllers that corrects against an external signal — the others either don't validate at all (Prompt, Instruction) or validate against an internal hypothesis (Skill, Recipe) — and for a Loop to function as a Loop, it must close on an external authority (a test suite, a compiler, a human), not on the agent's own opinion of its work; a check the agent grades itself is not a Loop
- **Evidence**: Author's definition and explicit contrast against the other four controllers under "Loops correct against an external signal."
- **Confidence**: emerging (an architectural claim, internally consistent with widely-observed LLM self-assessment unreliability documented elsewhere, but not independently measured in this article)
- **Quote**: "A loop is the only controller that corrects against an external signal, as the rest either don't validate at all (prompts and instructions) or validate against an internal hypothesis (skills and recipes)."
- **Quote** (the requirement): "it must close on an external authority, a test suite, a compiler, a human, not on the agent's own opinion of its work."
- **Quote** (the disqualifier): "A check the agent grades itself is not a loop, because the agent can be wrong and satisfied at once."
- **Our assessment**: This is the article's sharpest and most guide-relevant claim: it gives a precise, falsifiable test for whether a given feedback mechanism qualifies as a genuine Loop ("does the validating signal originate outside the agent's own judgment?"). This directly corroborates and sharpens the existing self-grading-is-not-verification theme already present in this corpus (e.g., verification-loop material in `blog-anthropic-claude-code-verification-loops-skills.md` and the evaluation-layer material in `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 7, which frames production observability as an external safety net rather than agent self-report). Xiong's contribution is the compact litmus test itself, not new empirical evidence for it.

### Claim 8: An external validation signal can itself be weak or wrong, and if a Loop is pointed at such a signal it will converge just as confidently as if the signal were sound — which the author calls one of the most dangerous agent failure modes, because the output then carries the false authority of having been "validated"
- **Evidence**: Author's stated warning, extending the Loop definition (Claim 7) under "Loops correct against an external signal."
- **Confidence**: emerging (a plausible, well-articulated risk claim; not backed by a named incident or measured failure rate in this article)
- **Quote**: "Point it at a weak or wrong signal and it will converge just as confidently, and that is among the most dangerous agent failures, because the output now carries the false authority of having been validated."
- **Our assessment**: This is a distinct and important addition to this corpus's safety vocabulary: it is not enough for a Loop to validate against something external to the agent — the external signal itself must be trustworthy, or the Loop actively manufactures false confidence rather than merely failing to catch errors. This is a stronger, more specific claim than generic "tests aren't sufficient" framing already in the corpus (e.g., `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 3's "a coding agent might pass every automated test while introducing an architecture that becomes progressively harder to change") — that claim is about a valid-but-incomplete signal (tests that don't cover architecture quality); Xiong's claim is about an actively wrong or weak signal being trusted as if it were sound. Both are instances of a broader "external validation is necessary but not sufficient — the validator itself must be evaluated" theme, worth citing together in a guide section on verification design.

### Claim 9: The graph is explicitly not a sixth controller — the five controllers govern an agent's judgment, while the graph grounds them in shared, persistent knowledge described as "the institutional memory that outlives any run"
- **Evidence**: Author's direct statement under "The graph grounds the controllers," distinguishing the graph's role from the five controllers' role.
- **Confidence**: emerging (a definitional/architectural claim, illustrated by reference to an external course rather than a worked example in this article)
- **Quote**: "The graph is not a sixth controller. The five govern an agent's judgment; the graph grounds them in shared, persistent knowledge: the institutional memory that outlives any run."
- **Our assessment**: This draws a clean line between behavioral control (the five controllers, all scoped to a single agent run or decision) and persistent knowledge (the graph, scoped across runs). It is conceptually adjacent to, but distinct in scope from, this same author's other corpus contributions on structured knowledge for data agents (`blog-thoughtworks-xiong-data-agents-context-resolution.md`, `blog-thoughtworks-xiong-ontology-llm-data-modernization.md`) — those pieces apply persistent semantic structure specifically to cross-system data reconciliation, while this article applies the same instinct (durable, shared, structured knowledge) to general agent institutional memory. Worth citing together as one author's consistent through-line, not as independent corroboration.

### Claim 10: None of the five controllers answers what the system knows or where that knowledge persists — that is specifically the question the graph answers, illustrated by reference to Andrew Ng's DeepLearning.AI course on "Agentic Knowledge Graph Construction," where agents read from and write to a common, persistent structure
- **Evidence**: Author's argument plus an external reference (no URL given in the article) under "The graph grounds the controllers."
- **Confidence**: anecdotal (the graph's purpose is asserted via analogy to an external course rather than demonstrated with a worked example inside this article itself — unlike Skill/Recipe, which get the repo-hygiene walkthrough)
- **Quote**: "None answers a different question: what does the system know, and where does that knowledge persist?"
- **Our assessment**: Unlike the Skill/Recipe pairing, the graph concept in this article is asserted and referenced rather than demonstrated with a concrete worked example — no analogous "here is what the graph looks like for the repo-hygiene case" walkthrough is given. This is the weakest-evidenced claim in the article and should be flagged as such if cited; it is a plausible and useful framing (agents need persistent, shared memory distinct from their per-run control mechanisms) but the article itself does not ground it as concretely as the five controllers.

### Claim 11: The article's summary framework compresses the whole taxonomy into one sentence: the agent decides what to do, the prompt bounds, the instruction aims, the skill acts, the recipe sequences, the loop corrects, and the graph remembers
- **Evidence**: Author's closing summary sentence.
- **Confidence**: emerging (a compressed restatement of Claims 1-10, not new evidence)
- **Quote**: "the agent decides what to do, the prompt bounds, the instruction aims, the skill acts, the recipe sequences, the loop corrects and the graph remembers."
- **Our assessment**: This one-line mnemonic is the single most citable summary in the piece — a strong candidate for a guide callout box or section epigraph introducing the taxonomy, since it assigns each of the five controllers (plus the graph) a single verb, making the distinctions memorable without requiring the reader to hold all five full definitions at once.

## Concrete Artifacts

```
Source: Zichuan Xiong, "Understanding agents, their five controllers and one
graph," Thoughtworks Insights, published August 13, 2026.

Section structure (verbatim heading order):
  The five controllers (intro)
  Prompts set the boundary
  Instructions direct the aim
  Skills replay experience
  Recipes orchestrate and gate skills
  Loops correct against an external signal
  The graph grounds the controllers
  Summary

Embedded diagram: "Figure 1. The five controllers and one graph"
(referenced twice in the article; contents of the figure itself were not
reproducible via WebFetch — text-only extraction).

Worked example — repo-hygiene remediation (Skill, quoted in full):
  "For example, a repo-hygiene remediation skill encodes the exact sequence
  for a flagged dependency: read the report (this may or may not include
  tool-calling to browse an internal Confluence page), find the affected
  package, bump it to the nearest patched version, regenerate the lockfile,
  update the changelog, open a PR with a standard description."

Worked example — repo-hygiene recipe (Recipe, quoted in full):
  "If it's a flagged dependency, run the dependency-remediation skill;
  If it's a failing lint rule, run the lint-fix skill;
  If it's a secret in the git history, stop and escalate to a human rather
  than auto-remediate."

Five controllers, one-line definitions (author's own compressed summary):
  Prompt      -> bounds   (declares role/permissions/hard limits; cannot enforce)
  Instruction -> aims     (style/priorities/standing preferences; slowest layer)
  Skill       -> acts     (pre-committed procedure for a single action; blind)
  Recipe      -> sequences (gates skills across branching scenarios; blind to
                            unanticipated situations; risk: mis-routing)
  Loop        -> corrects (only controller validating against an external
                            signal; risk: a weak/wrong external signal still
                            converges confidently)
  Graph       -> remembers (not a controller; shared persistent institutional
                            memory the controllers draw on)
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-thoughtworks-kamelman-delegation-architecture.md`,
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
`blog-anthropic-claude-code-skills-lessons.md`,
`blog-thoughtworks-anand-agent-evaluation-framework.md`,
`blog-thoughtworks-xiong-data-agents-context-resolution.md`, and
`blog-thoughtworks-xiong-ontology-llm-data-modernization.md` were re-read
directly (MINER.md §4b) and claim numbers below were confirmed against those
notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 8
    (delegation "requires more than permission; it requires a model of
    competence, risk and consequence") and Claim 1 (bounded autonomy — what
    a system may decide, under what conditions, with what observability and
    accountability): this article's Claim 1 (an agent is "a delegation of
    human judgment," handing over "not a task but the judgment the task
    requires") independently reaches a closely related premise — that
    granting an agent capability is distinct from authorizing its judgment —
    from a different author, published about a week apart from the same
    Thoughtworks trusted feed. Independent convergence, not within-author
    restatement.
  - `blog-anthropic-claude-code-verification-loops-skills.md` and
    `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 7
    (operational observability as "the production safety net...that bridges
    the gap between pre-deployment testing and real user behavior"): this
    article's Claim 7 (a Loop must close on "an external authority... not on
    the agent's own opinion of its work") and Claim 8 (a weak/wrong external
    signal still produces false confidence) supply a precise, generalizable
    litmus test for why external, non-self-graded validation matters — Anand's
    note supplies the production-observability mechanism; this article
    supplies the underlying architectural principle for why that mechanism
    must be external to the agent.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5
    (the three-tier oversight structure — manual, semi-automated, automated —
    including semi-automated "dynamic escalation" routed to a human
    supervisor): this article's Recipe worked example ("If it's a secret in
    the git history, stop and escalate to a human rather than auto-remediate")
    is a concrete, small-scale instance of the same "know when to stop and
    hand off to a human rather than auto-act" pattern that Gordon/Kamelman
    document at enterprise scale.

- **Contradicts**: No contradiction issue filed. One terminology collision is
  worth flagging rather than escalating: this article's "Skill" (Claim 5 —
  an abstract architectural category, "the tool is not what makes it a
  skill, the pre-committed procedure is") uses the same word as, but is not
  the same concept as, "Skill" in `blog-anthropic-claude-code-skills-lessons.md`
  (a concrete Claude Code product feature — a folder containing markdown,
  scripts, and a model-facing description/trigger field). Neither article
  makes a claim that conflicts with the other; they are simply using
  "skill" at different levels of abstraction (Xiong: any pre-committed
  non-deliberative procedure, of which Claude Code Skills is one possible
  implementation; Anthropic: a specific product mechanism). Per MINER.md
  §4a, this is a term overload, not a material contradiction — flagging
  here so the Smith doesn't conflate the two if citing both in the same
  guide section.

- **Extends**:
  - `blog-thoughtworks-gall-supervisory-engineering.md` (three pillars:
    directing, evaluating, correcting, organized around an inner/middle/
    outer loop taxonomy): that article's "directing" pillar (breaking work
    into agent-sized chunks, codifying standards explicitly) maps loosely
    onto this article's Prompt/Instruction controllers (declaring bounds,
    aiming standing preferences), and "correcting" maps onto this article's
    Loop controller — but Xiong's taxonomy is finer-grained (five distinct
    mechanisms vs. three broad human activities) and mechanism-focused
    (what structures the agent's own behavior) rather than human-activity-
    focused (what the supervising engineer does). The two taxonomies
    describe adjacent but distinct layers: Gall's pillars describe human
    supervisory work in the middle loop; Xiong's controllers describe the
    structural mechanisms built into the agent/harness itself that the human
    supervisor is configuring and reacting to.
  - `blog-thoughtworks-xiong-data-agents-context-resolution.md` and
    `blog-thoughtworks-xiong-ontology-llm-data-modernization.md`: this
    article's graph concept (Claim 9/10 — persistent, shared institutional
    memory distinct from per-run control mechanisms) generalizes the same
    author's narrower, data-specific argument in those two pieces (persistent,
    version-controlled ontological context for cross-system data
    reconciliation) to agent architecture broadly. Read together, this looks
    like the same author's consistent thesis — durable structured knowledge
    beats ad hoc, per-run inference — applied first narrowly to data agents,
    then generalized to agents in general.

- **Novel**:
  - **The five-controller taxonomy itself** (Prompt/Instruction/Skill/
    Recipe/Loop): no existing corpus source names this specific five-part
    structural vocabulary for agent control mechanisms. The closest existing
    corpus taxonomies — Gall's three pillars (human supervisory activities)
    and Kamelman/Gordon's bounded-autonomy/tiered-oversight framework
    (organizational governance) — operate at different levels of
    abstraction (human activity, organizational policy) rather than naming
    discrete structural mechanisms built into the agent/harness itself.
  - **The Loop litmus test** (Claim 7: "A check the agent grades itself is
    not a loop, because the agent can be wrong and satisfied at once"): a
    precise, falsifiable test for distinguishing genuine external validation
    from self-assessment dressed up as validation — more specific than any
    existing corpus phrasing of the same underlying concern.
  - **The "false authority of having been validated" failure mode**
    (Claim 8): naming the specific danger that a Loop closing on a weak or
    wrong external signal doesn't just fail silently but actively manufactures
    false confidence in the output — distinct from and sharper than the
    "tests pass but architecture erodes" incompleteness concern already in
    the corpus (`blog-thoughtworks-kamelman-delegation-architecture.md`
    Claim 3).
  - **The graph as non-controller institutional memory** (Claim 9): framing
    persistent shared knowledge as explicitly separate from, rather than a
    sixth member of, a set of behavioral control mechanisms — a structural
    distinction (control vs. memory) not drawn this way elsewhere in the
    corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the five-controller taxonomy
  (Claims 3-7) as a structural vocabulary for describing what a harness
  configuration (CLAUDE.md/AGENTS.md, skill definitions, orchestration
  scripts, CI-gated verification) is actually doing — mapping Prompt to
  system-prompt/role declarations, Instruction to CLAUDE.md standing
  preferences, Skill to pre-committed single-action procedures, Recipe to
  gated multi-step workflows, and Loop to CI/test/human-review gates. This
  gives the guide's existing harness-configuration material (which already
  covers most of these mechanisms individually) a shared naming scheme to
  organize them under.
- **Chapter 03 (Verification)**: Add the Loop litmus test (Claim 7 — must
  close on an external authority, not the agent's own opinion) and the
  weak-signal danger (Claim 8 — a Loop pointed at a bad signal converges
  just as confidently, producing false authority) as core framing for any
  section distinguishing genuine automated verification from agent
  self-report. Pair with `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 7 for the production-observability mechanism that operationalizes
  this principle.
- **Chapter 06 (Security & Threat Model)**: Add the Prompt limitation (Claim
  3 — "a prompt the model can read is a prompt the model can ignore") as
  explicit framing for why prompt-level constraints must be paired with
  enforced mechanisms (tool permissions, sandboxing, human escalation) rather
  than relied on alone. Add the Recipe mis-routing failure mode (Claim 6) and
  the repo-hygiene "stop and escalate to a human" branch (Concrete Artifacts)
  as a small, concrete escalation-design example to complement the
  enterprise-scale escalation material already sourced from
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`.

## Extraction Notes

1. **WebFetch declined full verbatim reproduction; targeted quote extraction
   was used instead.** Consistent with this Miner's prior notes on other
   Thoughtworks pieces, a first WebFetch call returned a condensed synthesis
   rather than full body text, citing copyright caveats. This note was built
   from three separate, narrowly-scoped WebFetch calls: (1) a broad
   per-section extraction pass, (2) a targeted pass confirming section
   headings, the opening sentences, the author byline, the fidelity/judgment
   sentence, the weak-signal warning, and whether a diagram or course URL was
   present, and (3) a pass specifically requesting the full, untruncated
   repo-hygiene example sentences for Skill and Recipe (the first pass had
   returned these with an internal ellipsis, which was not trusted as a
   verbatim quote until re-fetched in full). All quotes used in the note
   above were returned verbatim, without ellipses, by at least one of these
   targeted calls. The Assayer should still spot-check quotes against the
   live URL.
2. **No sub-pages followed.** The article references an external
   DeepLearning.AI course ("Agentic Knowledge Graph Construction") but
   provides no URL for it in the piece itself, and no other inline links to
   further Thoughtworks documentation were surfaced in any extraction pass.
   Per MINER.md's "follow up to 5 linked pages," there was no substantive
   linked page to follow — the course reference is a named-but-unlinked
   citation, not a followable page.
3. **The embedded diagram ("Figure 1. The five controllers and one graph")
   could not be inspected.** WebFetch converts the page to markdown/text and
   does not reproduce image contents; the figure is noted as present in
   Concrete Artifacts, but its visual content (e.g., whether it depicts
   controllers as concentric rings, a pipeline, or a graph-and-satellites
   layout) is not captured in this note.
4. **Overall confidence rated "emerging."** The core taxonomy (five
   controllers) is precisely defined with one shared worked example (Skill
   and Recipe only) and internally consistent trade-off/failure-mode
   analysis for each controller, from a credible, repeat trusted-feed author
   with a verified relevant title (Global Head of AIOps). This is stronger
   than a pure opinion essay (no case studies or metrics are offered, so it
   does not reach "settled"), but the Prompt, Instruction, Loop, and
   especially graph concepts are asserted and defined without their own
   worked examples — only Skill/Recipe get concrete illustration. Claim 10
   (the graph, evidenced only by reference to an external, unlinked course)
   is individually weaker than the rest and is flagged as such above; it
   does not on its own justify downgrading the whole note below "emerging"
   given the strength of Claims 1-9.
5. **No contradiction issue filed.** See Cross-References → Contradicts
   above: the "Skill" terminology overlap with
   `blog-anthropic-claude-code-skills-lessons.md` is a term collision
   (different levels of abstraction), not a material contradiction between
   claims, per MINER.md §4a's "when NOT to file" guidance.
