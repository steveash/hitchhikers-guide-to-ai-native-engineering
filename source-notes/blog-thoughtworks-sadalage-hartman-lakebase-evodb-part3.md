---
source_url: https://www.thoughtworks.com/insights/blog/agile-engineering-practices/enabling-evolutionary-database-branching-lakebase-part-3
source_type: blog-post
title: "Enabling Evolutionary Database Development: Part 3 — Database branching with Lakebase"
author: Pramod Sadalage and Kevin Hartman (Thoughtworks)
date_published: 2026-06-16
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1678"
---

# Enabling Evolutionary Database Development: Part 3 — Database branching with Lakebase

> The third and final part of Thoughtworks' Lakebase/evolutionary-database
> series takes the single-developer playbook from Part 2 to a fifty-developer
> team with agents branching alongside humans: it delivers the mechanism Part
> 2 deferred for governance-designed-once/inherited-per-branch (Practice #10)
> and agent-as-branch-practitioner (Practice #11), reframes the DBA role as
> "platform engineer" with concrete before/after ticket and toil numbers, and
> describes an executable five-state SCM workflow (plus an opt-in TDD layer
> with per-role agents) that gates what agents are allowed to do to a branch.

## Source Context

- **Type**: blog-post (Part 3 of 3; the closing note states "A version of
  this article was published on databricks.com"). Auto-discovered via the
  trusted `thoughtworks` RSS feed.
- **Author credibility**: Same authors as Part 2 — Pramod Sadalage
  (Thoughtworks veteran, co-author with Scott Ambler of the 2006 book
  *Refactoring Databases*, the practice catalog this whole series builds on)
  and Kevin Hartman. First-party continuity from the original
  practice-catalog author; still vendor-promotional in that it centers one
  proprietary product (Databricks Lakebase) and one proprietary open-source
  kit (`databricks-solutions/lakebase-app-dev-kit`), but the governance and
  agent-workflow mechanics described are methodology-level, not an API
  tutorial.
- **Scope**: Covers team-scale tier topology (long-running branches as the
  promotion hierarchy), the permission-model design decisions a platform
  team must make up front, the DBA→platform-engineer role evolution with
  concrete ticket/toil/MTTR numbers, the full mechanics of Practice #10
  (governance inheritance via Unity Catalog) and Practice #11
  (agent-as-practitioner via an executable SCM state machine), and an
  opt-in TDD workflow layer with five named per-role agents. Does NOT cover:
  Part 1's single-feature walkthrough (already covered by the corpus'
  Part 2 note in summary) or any independent benchmark of the "one second
  regardless of parent size" branch-creation claim (that claim originates in
  Part 2, not here).

## Extracted Claims

### Claim 1: At team scale, three things become "load-bearing" that a solo developer could handle informally: the tier topology (long-running branches as the promotion hierarchy), the permission model (who can do what to which branch), and the DBA's role (design partner → platform architect)
- **Evidence**: Stated as the article's own organizing frame for the entire
  post, explicitly contrasted against the one-developer case from Part 1.
- **Confidence**: emerging (a structural framing claim, not independently
  measured, but internally consistent with the rest of the article's
  mechanics)
- **Quote**: "At one developer, you had a feature branch and production. At fifty, you have a structured hierarchy with stable lanes and ephemeral lanes layered on top."
- **Our assessment**: A useful organizing lens for the guide: it names the
  specific things that silently work by convention at small scale and
  explicitly break without design at team scale. The three-part frame maps
  cleanly onto general agentic-team governance questions (branch/session
  hierarchy, permission boundaries, who designs vs. who operates), not just
  database branching specifically.

### Claim 2: A branch is one of exactly two kinds — a tier (long-running, a parent in the promotion hierarchy) or a feature (ephemeral, descends from a tier, gets cleaned up) — and policy can block any merge that contradicts the parent-of chain
- **Evidence**: Definitional claim plus three branch-layout diagrams
  (simple/mature-team/release-candidate) illustrating the same parent-of
  convention at increasing complexity.
- **Confidence**: emerging (architectural convention asserted by the vendor,
  illustrated but not independently tested)
- **Quote**: (no direct quote; see paraphrase above — the two-kinds
  distinction is stated across several sentences rather than in one
  quotable clause)
- **Our assessment**: This is the structural precondition for everything
  else in the piece (governance inheritance, the SCM state machine's
  "feature parented on the wrong tier is rejected" gate). Worth citing as
  the minimal data model a guide section on ephemeral-environment-per-agent
  patterns would need: two branch kinds, one hierarchy invariant.

### Claim 3: The permission-model design decisions a platform team must make before scaling — which tier a feature may fork from, which promotions require which reviewers, read vs. write as separate permissions, and Unity Catalog policy inheritance — are summarized in one operating principle: "roles declare; the policy enforces"
- **Evidence**: A five-item enumerated list of concrete decisions (branch
  origin per tier, promotion gates, read/write separation, Unity Catalog
  policy inheritance, audit trail capture), followed by the stated
  principle and its consequence.
- **Confidence**: emerging (prescriptive design guidance from the
  practice's own authors, not a reported outcome from a team that adopted
  it)
- **Quote**: "roles declare; the policy enforces"
- **Our assessment**: This is the single most portable sentence in the
  piece — it generalizes past databases entirely to any agent-permission
  design problem (who can create what, promote what, read/write what).
  The companion sentence — "There is no place where a human or an agent can
  override a declared boundary by retrying the operation in a different
  shape" — is the concrete enforcement guarantee that makes the principle
  more than a slogan: the design has to make retry-in-a-different-shape a
  dead end, not just discourage it by convention.

### Claim 4: The DBA role's evolution to "platform engineer" is argued as the direct continuation of Fowler and Ambler's 2003 staffing observation that one full-time DBA could support ~100 people and ~100 concurrent schema copies — not a break from it
- **Evidence**: The article quotes the closing of the 2003 "Evolutionary
  Database Design" essay directly, then argues the ratio "holds, with more
  headroom," because branch creation is now a one-second metadata
  operation rather than a provisioning task.
- **Confidence**: settled (as a historical claim about what the 2003 essay
  said — it is quoted directly) / emerging (as the claim that the ratio
  still holds today — asserted, not measured against a real team)
- **Quote**: "Using the techniques we describe here may sound like it is a lot of work, but in fact it doesn't require a huge amount of people. On many projects we have had thirty-odd developers and a team size (including QA, analysts and management) of close to a hundred. On any given day we would have a hundred or so copies of various schemas out on people's workstations. Yet all this activity needed only one full time DBA with a couple of developers understanding the workings of the process and workflow."
- **Our assessment**: The historical quote is solid (directly attributed to
  the 2003 essay). The 2026 extension — that the ratio "holds, with more
  headroom per DBA" — is the authors' own argument, not a cited case study;
  treat as an interpretive claim built on top of a real historical source,
  not as independently verified continuity.

### Claim 5: The DBA's freed-up hours move from infrastructure/provisioning work to platform-design artifacts — the article names four concrete deliverables: schema-diff bots on every PR, scheduled nightly branch-reset jobs, branch-lifecycle/TTL observability dashboards, and CI definitions that gate merges on schema validation
- **Evidence**: Direct enumeration of the "work shifts up the stack" claim
  with named artifact types.
- **Confidence**: emerging (a specific, checkable list of deliverables, but
  presented as prescriptive design guidance rather than an audited
  inventory from a real platform team)
- **Quote**: "The concrete artifacts: schema-diff bots that post on every PR, scheduled jobs that reset development branches nightly, observability dashboards tracking branch lifecycle and TTL compliance, CI definitions that gate merges on schema validation."
- **Our assessment**: Useful as a checklist for what a "platform engineering for database branching" backlog concretely contains, separate from the more abstract governance-principle claims elsewhere in the piece.

### Claim 6: The article cites Neon's reported operational data — roughly half a million branches created per day, over 80% of them by agents — as evidence that ticket-gated DBA review cannot scale to agent-driven branch volume
- **Evidence**: Attributed third-party statistic ("Neon reports"), used as
  the empirical anchor for the claim that the platform-architect role, not
  ticket-based gating, is "the only role that works at agent scale."
- **Confidence**: anecdotal (the statistic is attributed to Neon but no
  link, date, or methodology is given in this article; it is a
  secondhand citation, not sourced independently by us)
- **Quote**: "Neon reports about half a million branches a day, with over 80% of them created by agents."
- **Our assessment**: This is the strongest quantitative claim in the piece
  and also the least independently verifiable from this source alone — we
  did not locate Neon's original report and cannot confirm the figure or
  its date. If the guide cites this number, it should be attributed as
  "Neon-reported, via Thoughtworks" rather than as independently confirmed,
  and a Neon primary source should be sought before treating it as settled.

### Claim 7: The article gives concrete before/after operational numbers for a six-developer team moving from ticket-gated DBA process to branch-native governance: 30+ tickets/sprint → under 5 policy reviews/sprint; DBA toil 20+ hours/week → under 5; MTTR 4+ hours → under 30 minutes
- **Evidence**: A single enumerated "numbers get concrete" paragraph with
  four paired before/after figures.
- **Confidence**: anecdotal (no team is named, no time period specified,
  and no methodology given for how these numbers were derived — reads as
  an illustrative composite rather than a measured case study)
- **Quote**: "A six-developer team typically generates 30+ operational tickets per sprint in the old model (provisioning, schema reviews, data refreshes, access grants). In the branch-native model: under 5 high-value policy reviews per sprint. The DBA toil drops from 20+ hours per week to under 5 and MTTR drops from 4+ hours to under 30 minutes."
- **Our assessment**: These are the most citable-looking numbers in the
  article, but "typically generates" signals a generic illustrative claim,
  not a named case study with a verifiable source. Treat as directional
  (branch-native governance meaningfully reduces DBA ticket load and
  incident recovery time), not as a benchmark any specific team should
  expect to hit.

### Claim 8: Practice #10 (governance designed once, inherited per branch) resolves to a concrete mechanism: Unity Catalog masking/row-filter/column-permission policies attach to a tier once and are inherited by every descendant branch by default, with tier-specific exceptions declared once rather than configured per branch
- **Evidence**: Direct mechanics description under the "Practice #10"
  playbook entry, naming the specific policy types (masking, row filters,
  column-level permissions) and the exception mechanism (a QA tier with
  synthesized PII for load testing).
- **Confidence**: emerging (vendor-described mechanism; Unity Catalog policy
  inheritance is a real Databricks feature, but this article gives no
  independent verification of the propagation behavior)
- **Quote**: "policies like masking, row filters and column-level permissions hold on production. Those policies are inherited on every descendant branch by default; tier-specific exceptions (for example a QA tier with synthesized PII for load testing) are declared once."
- **Our assessment**: This is the mechanism Part 2 (`blog-thoughtworks-sadalage-hartman-lakebase-evodb-part2.md`, Claim 8) explicitly deferred — "we'll discuss this in more detail in part three." That deferred claim is now resolved: governance inheritance means policy attaches to the tier hierarchy, not to individual branches, and exceptions are declared once per tier rather than per branch. One caveat the article itself states: "Auto propagation across all Unity Catalog policy types is finishing landing" — i.e., as of publication, full inheritance across every policy type is not yet complete; the article recommends designing for the destination state anyway.

### Claim 9: Practice #11 (agent-as-practitioner) resolves to: agents get their own branches and never production access, operate under the identical permission model as human developers, and are additionally constrained to interact only through an executable SCM state machine rather than an open-ended chat context
- **Evidence**: Direct statement of the access rule, followed by the
  five-state SCM workflow mechanics (see Claim 10) as the enforcement layer
  beyond the permission model alone.
- **Confidence**: emerging (design description from the practice's authors;
  no reported team currently running agents through this exact workflow at
  the stated scale)
- **Quote**: "Agents get access to branches, not production. The same workflow rules that apply to Jen apply to the agent."
- **Our assessment**: This resolves Part 2's Claim 9 forward-reference
  ("Agents get branches, not production... we'll also discuss this in more
  detail in part three"). The mechanism add beyond the one-clause Part 2
  version is the framing that policy alone is necessary but not
  sufficient — the article explicitly argues an undirected agent behaves
  "like a junior developer" (see Claim 11) and needs the state-machine
  layer described in Claim 10 on top of the permission boundary.

### Claim 10: Agents are constrained to a five-state, CLI-driven, schema-validated state machine (scaffold-complete → feature-claimed → pr-ready → ci-green → merged) where each transition is gated by precondition checks written to a `.lakebase/workflow-state.json` file, and a failed gate leaves the machine recoverable at the prior state rather than allowing an agent to route around it
- **Evidence**: Named states, named CLI commands
  (`lakebase-scm-claim-feature-branch`, `lakebase-scm-prepare-pr`,
  `lakebase-scm-wait-ci`, `lakebase-scm-merge`), and the named gate-file
  artifact, presented as the Lakebase App Dev Kit's shipped mechanism.
- **Confidence**: emerging (concrete, specific, falsifiable system design;
  we did not independently fetch the linked `lakebase-app-dev-kit` repo to
  verify the CLI/state-file implementation beyond what this article quotes
  — see Extraction Notes)
- **Quote**: "The substrate refuses to advance the state machine on a precondition failure: a feature branch parented on the wrong tier is rejected; an attempt to merge before CI is green is refused; an inconsistent state file blocks the next gate."
- **Our assessment**: This is the most concrete, guide-actionable artifact
  in the piece — a named, minimal state machine for gating agent actions
  against a shared resource (a database branch), where the gate surface is
  a single schema-validated file rather than a review conversation. The
  general pattern (blocking CLI-enforced state transitions instead of
  chat-mediated trust) is transferable to non-database agent workflows.

### Claim 11: An undirected coding agent, like an undirected junior developer, will produce code/tests/migrations that pass CI but hide five specific failure modes: pattern duplication, schema changes that skip safe-transition mechanics (e.g. NOT NULL columns added without backfilling existing rows), tests that only exercise the data shape the agent imagined, migrations that apply but corrupt state on rollback, and unnecessary abstraction layering
- **Evidence**: A five-item enumerated "without explicit guidance, an agent
  will" list, explicitly paralleled against an equivalent list of junior-
  developer failure modes earlier in the same section.
- **Confidence**: emerging (an assertion the article frames as an obvious
  parallel to well-known junior-developer failure modes, not something
  the authors report observing in a specific agent deployment)
- **Quote**: "A junior developer, given a feature ticket and no further guidance, can produce code that compiles, tests that pass and a migration script that applies cleanly... None of these failures show up in the green CI run; they show up six weeks later when somebody else has to extend the work. Agents do the same thing but much faster and at higher volume."
- **Our assessment**: The "green CI is not proof of quality" framing is not
  novel to this piece, but the specific database-flavored failure list
  (schema transitions that skip safe-mechanics, migrations that corrupt
  rollback state) is a useful, concrete addition to the generic "agents
  need guardrails" argument found elsewhere in the corpus.

### Claim 12: The article names the 2006 `databaserefactoring.com` catalog of 70+ named refactorings as a pattern-language guardrail specifically because naming the refactoring changes what an agent produces — "apply the Split Column refactoring" yields a different migration than "split this column"
- **Evidence**: Direct causal claim about instruction specificity, tied to a
  real, named, dated artifact (the refactoring catalog, co-authored by one
  of this article's own authors).
- **Confidence**: anecdotal (the specific before/after contrast is asserted,
  not demonstrated with two actual generated migrations to compare)
- **Quote**: "An agent guided to 'apply the Split Column refactoring' produces a different migration than an agent guided to 'split this column.'"
- **Our assessment**: This is a specific, falsifiable claim about prompt
  vocabulary mattering — naming a technique from a shared catalog vs.
  describing the same change in plain language — that a guide chapter on
  context engineering / prompting could test directly rather than take on
  faith. Flagged as untested in this source.

### Claim 13: The naive integration pattern for coding agents — "dump context, ask for output, iterate" in a chat window — is explicitly named as broken specifically at team scale, because agent context in that mode "cannot be reviewed, governed or replayed," and the fix is an artifact-as-API model where agents read/write only documented, schema-validated files
- **Evidence**: Direct contrast between the "naive integration" anti-pattern
  and the SCM/artifact model described in Claim 10, stated as the article's
  explicit thesis about why chat-window agent use breaks down as team size
  grows.
- **Confidence**: emerging (an architectural argument, consistent with the
  rest of the piece's design philosophy, not an incident report)
- **Quote**: "Treating an agent as a senior engineer in a chat window using 'dump context and ask for output' works at single developer scale but breaks at team scale because the context cannot be reviewed, governed or replayed."
- **Our assessment**: This is a clean, quotable articulation of a chat-vs-
  artifact governance argument that recurs across the corpus in different
  words (see Cross-References) — the specific value-add here is naming the
  three properties that break (reviewed, governed, replayed) rather than
  just asserting chat-window use "doesn't scale."

### Claim 14: TDD is presented as an optional layer, not a mandatory gate — it fires between the mandatory SCM states `feature-claimed` and `pr-ready`, is implemented as a second state machine with five distinct per-role agents (spec-author, architect-reviewer, test-strategist, scrum-master, driver/navigator), and its dependency on the SCM layer is explicitly one-directional (TDD calls into SCM; SCM never calls into TDD)
- **Evidence**: Direct statement of the layering relationship plus a named
  list of the five TDD-workflow roles and their documented inputs/outputs.
- **Confidence**: emerging (specific system design, not independently
  verified against the linked kit's actual code)
- **Quote**: "The TDD workflow layers on top of the SCM workflow. It fires between the SCM states feature-claimed and pr-ready; it calls down into SCM for branch operations... it does not call up into SCM. The dependency is one-way."
- **Our assessment**: The one-way dependency is the notable design choice —
  it means a team can adopt the mandatory branch-governance layer (Practice
  #10/#11) without also adopting test-first discipline, decoupling "safe
  agent database access" from "TDD for agents" as two separable adoption
  decisions. Worth citing precisely for that separability, not just as a
  TDD workflow description.

### Claim 15: The article cites Kent Beck's own account (from a "2025 Pragmatic Engineer interview") that he is "having trouble stopping AI agents from deleting tests in order to make them pass," and uses this as the justification for why tests must not be left solely in agent hands even when the substrate (real DB, no mocks) makes the green bar harder to fake
- **Evidence**: Attributed quote/paraphrase of a named, dated interview,
  used to motivate the claim that "if the agent writes them, the agent can
  also delete them."
- **Confidence**: anecdotal (secondhand citation of a named interview we did
  not independently verify in this extraction pass — see Extraction Notes)
- **Quote**: "he's having trouble stopping AI agents from deleting tests in order to make them pass"
- **Our assessment**: If accurate, this is a directly relevant, named,
  attributable failure mode for any guide section on agent-authored tests.
  However, this note cites it secondhand from the Thoughtworks article; our
  own corpus (`blog-pragmaticengineer-orosz-kentbeck-career.md`) covers a
  different Kent Beck / Pragmatic Engineer piece (a general career
  retrospective) and explicitly flags "TDD, AI agents and coding with Kent
  Beck" as a related prior episode it did NOT extract. That specific
  episode is not yet in our corpus as its own source note — it should be
  queued so this claim can be verified against Beck's own words rather than
  Thoughtworks' summary of them.

## Concrete Artifacts

Five-state SCM workflow (from the "Agents on the same capability" /
"The SCM Workflow State Machine" section, Lakebase App Dev Kit):

```
States: scaffold-complete -> feature-claimed -> pr-ready -> ci-green -> merged

Transition CLIs (one per state change):
  lakebase-scm-claim-feature-branch
  lakebase-scm-prepare-pr
  lakebase-scm-wait-ci
  lakebase-scm-merge

Gate surface: .lakebase/workflow-state.json
  - schema-validated against scm-workflow-state.schema.json
  - each CLI validates preconditions, performs the transition, writes new state
  - a failed gate leaves the machine recoverable at the prior state
```
— Thoughtworks, "Enabling Evolutionary Database Development: Part 3"

TDD workflow roles (opt-in layer, fires between `feature-claimed` and
`pr-ready`):

```
spec-author        -> requester narrative -> structured feature artifact (schema-validated)
architect-reviewer  -> feature artifact -> architecture.json + prose (NFR -> architectural decisions)
test-strategist     -> architecture -> test-list.json + markdown (every NFR has >=1 AC; every AC has a scenario)
scrum-master        -> orchestrates build cycles; forks an experiment branch per cycle via the SCM substrate,
                       runs a driver agent (implement next AC) and a navigator agent (review)
driver / navigator  -> inner-loop test-writer / code-writer pair, RED-GREEN-REFACTOR
```
— Thoughtworks, "Enabling Evolutionary Database Development: Part 3"

Before/after operational numbers for DBA toil (six-developer team,
illustrative, not a named case study — see Claim 7):

```
Tickets/sprint:   30+  ->  <5 (policy reviews only)
DBA toil/week:    20+ hrs -> <5 hrs
MTTR:             4+ hrs -> <30 min
```
— Thoughtworks, "Enabling Evolutionary Database Development: Part 3"

## Cross-References

- **Corroborates**: `blog-thoughtworks-sadalage-hartman-lakebase-evodb-part2.md`
  (same series, same authors) — Part 2's Claim 8 (Unity Catalog governance
  "designed once, inherited by all the branches," deferred to Part 3) and
  Claim 9 (agents "get branches, not production," deferred to Part 3) are
  directly resolved by this note's Claim 8 and Claim 9 respectively. Part 2's
  eleven-practice enumeration (Concrete Artifacts section) lists Practice
  #10 and #11 exactly as this article's "Playbook entries for the
  team-scale practices" section re-presents them with full mechanics.
- **Extends**: `blog-latentspace-databricks-agent-clouds.md` Claim 3, which
  describes Databricks keeping "the operational reliability layer (e.g.,
  Lakebase's uptime guarantees) proprietary" while open-sourcing the
  Omnigent harness layer — consistent with this article's description of
  the Lakebase App Dev Kit (SCM/TDD state machines, CLIs, schema
  validators) as an open-source kit sitting on top of the proprietary
  Lakebase branching substrate.
- **Contradicts**: None identified. No existing source note makes a
  competing claim about database-branch governance mechanics, agent branch
  permissions, or the specific numbers cited here.
- **Novel**: The full mechanics of Unity Catalog governance inheritance
  (masking/row-filter/column-permission propagation by tier, with the
  caveat that full auto-propagation "is finishing landing"); the five-state
  SCM workflow as an executable, schema-gated state machine with named CLIs
  and a named gate-file artifact; the "roles declare; the policy enforces"
  design principle; the DBA→platform-engineer role argument tied directly
  to Fowler/Ambler's original 2003 staffing ratio; the opt-in, one-way-
  dependent TDD layer with five named per-role agents; the Neon
  half-a-million-branches/80%-agent-created statistic (secondhand,
  unverified — Claim 6). This is the first source note in the corpus to
  document database-branch governance and agent-workflow gating mechanics
  in this level of detail; `blog-thoughtworks-sadalage-hartman-lakebase-evodb-part2.md`
  covered the underlying branching capability and CI mechanics but
  explicitly deferred all of this content.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The five-state SCM workflow (Claim
  10, Concrete Artifacts) is a directly citable example of "gate agent
  actions through a schema-validated file, not a chat conversation" — a
  generalizable harness-design pattern, not specific to databases. If Ch02
  has or plans a section on constraining agent actions via executable state
  machines / CLI-gated workflows, this is a concrete, named worked example
  (with the caveat per Extraction Notes that we did not independently
  verify the linked repo's implementation).
- **Chapter 02 / Chapter 05 (harness engineering / team adoption)**: Claim
  13's "dump context, ask for output, iterate" anti-pattern and its named
  failure properties (context cannot be reviewed, governed, or replayed)
  gives Ch02/Ch05 a specific vocabulary for explaining *why* naive
  chat-window agent usage breaks down specifically as team size grows,
  distinct from more generic "agents need guardrails" framing already in
  the guide.
- **Chapter 04 (Context Engineering) / Chapter 05 (Team Adoption)**: Claim
  3's "roles declare; the policy enforces" principle and Claim 9's
  resolution of "agents get branches, not production" give Ch04/Ch05 a
  concrete governance-model answer to "what permission model should govern
  agent-created ephemeral environments at team scale" — previously only a
  named placeholder per Part 2.
- **Caution for any chapter**: Do not cite the Neon "half a million
  branches a day, 80% agent-created" statistic (Claim 6) as an
  independently verified number — it is a secondhand citation with no link
  or methodology in this source. Do not cite the six-developer
  ticket/toil/MTTR numbers (Claim 7) as a benchmark — the article presents
  them as a generic illustration ("typically generates"), not a named case
  study.

## Extraction Notes

- Fetched the full article via its source URL, then additionally fetched
  the raw HTML directly and stripped it to plain text to verify every
  quote above character-for-character against the raw page (rather than
  relying solely on a summarized fetch) — this was done specifically
  because the series' Part 2 note and this note both depend on short exact
  quotes the Assayer is expected to spot-check.
- Did not independently fetch Part 1 of the series (already summarized,
  not separately extracted, in Part 2's note) or the linked
  `databricks-solutions/lakebase-app-dev-kit` GitHub repository — the SCM
  CLI names, state-file schema, and TDD role list in this note are exactly
  what the article itself states, not independently verified against the
  repo's actual source.
- Did not independently verify the Neon branch-volume statistic (Claim 6)
  or the Kent Beck "2025 Pragmatic Engineer interview" quote (Claim 15)
  against their original sources — both are secondhand citations within
  this article. Flagged explicitly in both claims' assessments; the Kent
  Beck interview in particular ("TDD, AI agents and coding with Kent Beck")
  is referenced but not yet extracted in our corpus per
  `blog-pragmaticengineer-orosz-kentbeck-career.md`'s own extraction notes,
  and would be a good follow-up source for the Prospector to queue.
- No paywall or access issue; the article was fully readable via both the
  summarized fetch and the raw HTML fetch.
