---
source_url: https://addyosmani.com/blog/brownfield-agentic-engineering/
source_type: blog-post
title: "Brownfield Agentic Engineering"
author: Addy Osmani
date_published: 2026-09-14
date_extracted: 2026-09-22
last_checked: 2026-09-22
status: current
confidence_overall: emerging
issue: "#3611"
---

# Brownfield Agentic Engineering

> Osmani proposes a "zones" operating procedure (green/yellow/red, with three
> enforcement rules) for bounding agent autonomy in legacy codebases, argues
> that the harness should contain only what the code itself can't say, and
> threads together six external case studies (Bun, Asana, Shopify, Stripe,
> a VB6-to-C# controlled study, and a migration benchmark called SWE Refactor
> Bench) into a single claim: agents changed the *price* of attempting a
> migration, not the *evidence* required to trust its result.

## Source Context

- **Type**: blog-post (first-party personal engineering blog,
  addyosmani.com/blog, ~2,300 words, published September 14, 2026)
- **Author credibility**: Per the post's own byline, "Addy Osmani is an
  engineering and evangelism leader and a Member of Technical Staff at
  Anthropic, where he works on Claude Code. He spent over 14 years at Google
  leading developer experience across Chrome and, in recent years, AI
  (Gemini, coding agents, and agentic engineering), most recently as a
  Director at Google Cloud AI." Osmani is already a heavily corroborated,
  top-cited corpus author (`blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-intent-debt.md`, and others). This post is a
  practitioner-synthesis piece — it draws on the author's own career
  anecdotes (an AOL homepage incident, unspecified prior commerce-site work)
  plus six external case studies he did not run himself (Bun, Asana,
  Shopify, Stripe, Netflix, a VB6-to-C# study, and a benchmark called "SWE
  Refactor Bench"), none of which are linked or cited with a URL in the
  post itself. Treat the zones framework and harness/instructions/skills
  taxonomy as Osmani's own synthesis (emerging), and treat each external
  case-study figure as inheriting the confidence level of its own primary
  source where one exists in this corpus (see Cross-References).
- **Scope**: Covers a risk-zoning framework for legacy codebases, a
  distinction between what agents can infer from code versus what must be
  written down, a "durable research artifact" (comprehension memo) pattern,
  a taxonomy of instructions/skills/plugins/harness, characterization
  testing as the starting move for brownfield work, complete-unit migration
  as a requirement, six named external migration case studies used as
  evidence, a caution against parallelizing before verification is
  dependable, and a metrics list for judging migration progress. Does NOT
  provide: a worked example of the zones framework applied to a real
  codebase, the actual text of any comprehension memo, benchmark
  methodology or a citable source for "SWE Refactor Bench," a citation for
  the VB6-to-C# study, or first-hand verification of any of the six
  external case studies (all are described in third-party summary form,
  with several — Bun, Asana, Shopify, Stripe — already independently mined
  in this corpus from primary or closer-to-primary sources).

## Extracted Claims

### Claim 1: A "zones" model (green/yellow/red) should govern where agents may work in a legacy codebase, enforced by three rules — a human draws the map, zones only promote once earned, and each zone fixes what verbs are allowed
- **Evidence**: Author's own framework, illustrated with an unnamed
  commerce-site anecdote ("five or six departments all with their own
  microsites") and stated as three explicit enforcement rules.
- **Confidence**: emerging (practitioner framework, no controlled test of
  the zones model itself; the underlying rationale — trust should track
  test coverage/isolation, not code age — is plausible and consistent with
  standard legacy-system risk practice, but this specific three-rule
  formalization is Osmani's own synthesis)
- **Quote**: "Three rules make the zones an operating procedure instead of a
  metaphor. A person draws the map, not the agent; left to choose, the
  agent starts in the scariest file, because the scariest file has the
  most interesting names. Zones only move when it's earned: yellow becomes
  green once characterization tests exist and the module's owner has
  reviewed the agent's first changes. And the zone sets the verbs: green is
  a tight loop, yellow is tests first, red is a human pairing on every step
  or the work not happening."
- **Our assessment**: The specific, memorable detail here is the stated
  reason a human (not the agent) must draw the map: "left to choose, the
  agent starts in the scariest file, because the scariest file has the most
  interesting names" — an explicit claim about *why* unsupervised agents
  misjudge risk in legacy code (interesting-looking code attracts
  attention regardless of blast radius), not just an assertion that they
  do. The "zones only move when earned" rule (characterization tests +
  owner review, not agent confidence) is the load-bearing mechanism that
  keeps the framework from being self-defeating — without it, an agent
  could write its own characterization tests and promote its own zone.

### Claim 2: The harness should record only what the code cannot say — business/team-specific nuance, trade-offs, unenforced conventions, domain rules, and historical context — not general architecture the agent can already infer
- **Evidence**: Author's structural argument plus an itemized list of what
  counts as "what the code can't say."
- **Confidence**: emerging (practitioner synthesis; directionally
  consistent with the ETH Zurich AGENTS.md finding already in the corpus)
- **Quote**: "Write down what the code can't say, and nothing else."
- **Our assessment**: This restates, in a single imperative sentence, the
  "filter test" already documented from Osmani's own AGENTS.md post via
  `blog-addyosmani-code-agent-orchestra.md` (Linked Source 1: "Can the
  agent discover this by reading the code? Yes = delete it. No = keep it.")
  — applied specifically to brownfield/legacy context rather than to
  AGENTS.md content in general. The itemized list (business nuance,
  trade-offs, unenforced conventions, domain rules, external constraints,
  historical context) is a more concrete operationalization of that filter
  than the earlier post offered. The companion claim — "Autonomy should
  follow blast radius, observability, and recoverability. A model's
  confidence is a poor guide." — is the sharper, more citable half: it
  names three variables that should set agent autonomy and explicitly
  excludes a fourth (the model's own stated confidence) that practitioners
  might otherwise be tempted to use as a proxy.

### Claim 3: For yellow/red-zone work, a separate read-only research pass should produce a durable "comprehension memo" (entry points, owners, callers, tests, production signals, open questions, each citing a file/issue/dashboard) so later sessions don't repeat the same archaeology
- **Evidence**: Author's stated practice and its stated failure mode
  without the memo.
- **Confidence**: emerging (practitioner recommendation, no measurement of
  time saved or memo adherence)
- **Quote**: "I like a separate read-only pass that produces a short
  comprehension memo: entry points, owners, callers, existing abstractions,
  tests, production signals, relevant history, and open questions. Claims
  should cite a file, issue, ownership record, or dashboard." / "If your
  agent's exploration produces no durable artifact, the next agent pays for
  the same archaeology again."
- **Our assessment**: The "claims should cite a file, issue, ownership
  record, or dashboard" requirement is the specific, checkable part of this
  claim — it turns the memo from a free-text summary (which could itself
  hallucinate rationale) into a set of falsifiable, sourced assertions.
  This is a concrete implementation detail for the general "durable
  artifact" idea that the corpus already has in vaguer form (e.g., the
  Ralph Loop's four memory channels in `blog-addyosmani-code-agent-orchestra.md`
  Claim 6) — this source adds a citation requirement that those other
  memory-persistence patterns don't specify.

### Claim 4: Instructions, skills, plugins, and the harness serve different jobs — and every review comment an agent needs twice is a signal that something should move from prose into a mechanically enforced layer instead
- **Evidence**: Author's four-way taxonomy, plus a stated operational test.
- **Confidence**: emerging (practitioner framework/taxonomy)
- **Quote**: "Instructions record unusual facts about a repository. Skills
  package reusable procedures such as checking blast radius or verifying a
  schema change. Plugins can provide governed access to the ownership
  catalog, incident archive, or dashboards." / "Every repeated correction is
  a missing piece of the harness." / "If you quietly repair the diff, the
  next session can repeat it. When the same review comment appears again,
  move it into a lint rule, hook, type, test, or skill. Keep prose for
  constraints that cannot be enforced mechanically."
- **Our assessment**: The operational test — "does the same review comment
  appear twice?" — is the most directly actionable piece of this source for
  a guide checklist: it converts an abstract preference for mechanical
  enforcement over prose into a concrete trigger practitioners can watch
  for during code review, without requiring them to predict in advance
  which conventions deserve a lint rule versus a paragraph in CLAUDE.md.
  This complements, but does not duplicate, the "Enforcement Hierarchy"
  content already in `guide/02-harness-engineering.md` — that section
  covers *what* enforcement tiers exist; this source's contribution is a
  trigger for *when* to promote a rule between tiers.

### Claim 5: Characterization tests — pinning a legacy module's actual current behavior, ugly parts included, written or reviewed by a human before an agent works on the module — are the required starting move for brownfield refactoring, and Netflix's GraphQL cutover generalizes the same idea to homepage-scale surfaces with no honest unit suite
- **Evidence**: Author's own definition of characterization testing (set off
  as a blockquote in the source), a stated failure mode when an agent both
  writes and passes its own tests, and a named external case (Netflix
  GraphQL replay/shadow-traffic cutover) offered as the same technique
  applied where unit tests aren't viable.
- **Confidence**: emerging for the general recommendation (practitioner
  synthesis); the Netflix example is cited without a source link, so treat
  it as an unverified pointer, not independently confirmed by this note
- **Quote**: "Characterization tests are automated tests used to document a
  system's actual current behavior so you can safely refactor or change
  legacy code" / "When an agent is the one making them pass, don't let that
  same session be the only author of the tests. Pin the behavior first, in
  a separate pass or by a person; then let the agent work. Otherwise you
  get a green suite that encodes the implementation you just invented." /
  "Netflix used the same idea at production scale in its GraphQL cutover -
  replay and shadow traffic against the old and new paths, diff the
  payloads, promote only when they match. That is the promotion path when a
  homepage-class surface has no honest unit suite: don't guess; run both
  and compare."
- **Our assessment**: The specific failure mode named — an agent that
  writes and passes its own characterization tests produces "a green suite
  that encodes the implementation you just invented," not a pin of the
  *old* behavior — is a sharp, self-contained warning distinct from the
  more general "agents self-grade" concern already in
  `guide/03-verification.md` ("Green tests that never touch the risky
  code"). It specifically targets characterization testing, where the
  entire point of the test is to encode behavior the agent did not write,
  so agent-authored characterization tests are a more severe version of the
  self-grading problem than agent-authored unit tests for new code. The
  Netflix claim, by contrast, is presented with no link or further detail —
  it functions here as an analogy extending the shadow-traffic/parity-diff
  pattern (already documented with far more mechanism in
  `blog-anthropic-code-migration-playbook.md` Claim 5's "judge"
  construction) to a UI-facing surface, not as new verified evidence.

### Claim 6: A surface that only production traffic actually exercises is a red zone by definition, and the only trustworthy gate for changing it is user-testing or a synthetic stand-in for that traffic — illustrated by an AOL homepage outage the author was called in to fix on a day off
- **Evidence**: A first-person anecdote from the author's own career (an
  AOL.com homepage break, "dozens and dozens of departments" each owning
  components/scripts/A-B tests, insufficient unit-test coverage to isolate
  the cause) and an explicit generalization from it.
- **Confidence**: anecdotal (single, undated, unnamed-company-era personal
  story, offered as illustration rather than data)
- **Quote**: "In that case I was able to get it fixed, but we basically had
  to at least user-test the things that didn't have their own unit tests.
  How well were things working, without breaking for everybody?" / "That's
  still the job. Agents don't remove the dozens-of-departments problem;
  they make it cheaper to attempt a change against it. A surface that only
  production traffic really understands is a red zone by definition, and
  until you've built a stand-in for that traffic, the user-testing I did on
  my day off is still the gate."
- **Our assessment**: The generalizing sentence — "agents don't remove the
  dozens-of-departments problem; they make it cheaper to attempt a change
  against it" — is the most transferable idea in this claim and is a
  concrete instance of this source's overarching thesis (see Claim 14):
  agents lower the cost of *trying*, not the bar for what counts as
  evidence that a change is safe. The anecdote itself is decades-old,
  pre-dates agentic tooling entirely, and should be read as color
  establishing the author's personal stake in the "red zone" concept, not
  as evidence about agent behavior specifically.

### Claim 7: Half-finished migrations are especially confusing to agents because they create contradictory precedent — search returns the old pattern in some files and the new pattern in others — and a migration benchmark called "SWE Refactor Bench" names this failure mode "Blindness," with only 28 of 520 agent runs passing its full audit
- **Evidence**: A structural description of the contradictory-precedent
  problem plus a named benchmark and a specific pass-rate figure, cited
  without a link or further methodological detail.
- **Confidence**: anecdotal for the benchmark figure specifically (no
  citation, link, or methodology given for "SWE Refactor Bench" anywhere in
  the post — this note could not independently verify the benchmark exists
  or that the 28/520 figure is accurately represented); emerging for the
  underlying contradictory-precedent mechanism, which is a structural
  argument independent of the benchmark citation
- **Quote**: "Half-finished migrations are particularly confusing to
  agents. Search returns the old approach in forty files, the replacement
  in twelve, and a shim that presents both as current. The agent sees
  contradictory precedent." / "Tests can stay green while a replacement
  still calls the legacy implementation. SWE Refactor Bench calls this
  migration "Blindness." Across 520 agent runs, only 28 passed its
  migration audit, behavioral tests, and independent verification."
- **Our assessment**: This is the single most novel, specific claim in the
  source for the corpus — no other mined source names a migration-specific
  benchmark or a "Blindness" failure mode for agents working against
  half-migrated code. However, the complete absence of a link, publisher,
  or any other identifying detail for "SWE Refactor Bench" means this
  claim cannot be verified from the source alone and should not be cited
  in the guide as a settled statistic until an independent, linkable
  source for the benchmark is located and mined. The mechanism it
  illustrates (a shim or partial migration produces contradictory precedent
  an agent can't resolve, and a green suite can mask that a replacement
  still calls the legacy path underneath) is separately corroborated by
  this corpus's existing "complete-unit migration" material (see
  Cross-References).

### Claim 8: A migration unit is only complete once the new path works and the old dependency is demonstrably removed — deletion deferred to a "future cleanup ticket" means the unit was not actually finished, and Stripe's TypeScript migration is instructive specifically because it used no agents at all
- **Evidence**: Author's definition of migration completeness plus a named
  external example (Stripe) offered as a counterpoint precisely because it
  predates and excludes agentic tooling.
- **Confidence**: emerging for the completeness principle (practitioner
  synthesis); the Stripe figure is corroborated elsewhere in the corpus in
  more detail (see Cross-References)
- **Quote**: "I would rather finish one route end to end, including
  removing the old path, than convert thirty files and leave both patterns
  alive. If deletion is a future cleanup ticket, the migration unit is not
  complete." / "If a codemod can make the routine change, use the agent to
  help write and check it. Give agents the exception queue. Stripe's
  migration is useful here precisely because no agents were involved: the
  durable artifact was the migration machine."
- **Our assessment**: "Give agents the exception queue" is a specific,
  actionable division-of-labor rule: deterministic codemods handle the bulk
  mechanical change, and agents are reserved for the cases a codemod can't
  handle — the opposite allocation from simply pointing an agent at the
  whole migration. This is consistent with the corpus's existing
  "Deterministic tools for deterministic work" principle in
  `guide/00-principles.md`, applied here specifically to migrations rather
  than stated as a general rule.

### Claim 9: Two large agentic migrations (Bun's Zig-to-Rust port; Anthropic's own migration process) both front-loaded human preparation before any agent translation began — Bun with a porting guide mapping language idioms, Anthropic with a disposable mini-migration used to stress-test and discard a trial rulebook
- **Evidence**: A compressed summary of two migrations already covered in
  greater depth by other corpus sources.
- **Confidence**: settled for the Bun details (independently corroborated
  at far greater depth by `blog-pragmaticengineer-bun-rust-rewrite.md` and
  `blog-anthropic-code-migration-playbook.md`); emerging for the
  Anthropic-process generalization, which is stated here without the
  specific stress-test mechanics `blog-anthropic-code-migration-playbook.md`
  Claim 7 provides
- **Quote**: "Bun's Zig-to-Rust port ran about 50 workflows over 11 days
  from a 535,000-line codebase, with two adversarial reviewers on every
  generated unit and the entire pre-existing test suite as the merge gate;
  the part worth copying is that hours went into a porting guide mapping
  Zig idioms to Rust before any agent ran. Anthropic's own migration
  process stress-tests its rulebook on a disposable mini-migration and
  throws the trial output away before the broad run begins."
- **Our assessment**: This claim is a compressed restatement, not new
  evidence — every figure here (50 workflows, 11 days, 535,000 lines, two
  adversarial reviewers, full test suite as merge gate) matches figures
  already extracted in far greater depth and with primary-source
  verification in `blog-pragmaticengineer-bun-rust-rewrite.md` (Claims 5–8)
  and generalized into a named "stress-test" step in
  `blog-anthropic-code-migration-playbook.md` (Claim 7, Step 2 of the
  six-step process — "throw out any translated files. The goal is to
  refine the rules, not make incremental progress"). The value this source
  adds is framing both examples together as one instance of a single
  principle: prep work (a mapping/porting guide, a disposable stress test)
  happens *before* the main translation loop, not as an afterthought.

### Claim 10: A controlled VB6-to-C# study found 92% behavioral equivalence on simple features versus 47% on complex ones, establishing migration-unit size as "the lever"; the same size-dependency shows up pre-agent in Stripe's 3.7-million-line TypeScript codemod, Google's large-scale-changes practice, and now in Spotify's 650-plus monthly agent PRs on pre-existing Backstage rails
- **Evidence**: A named controlled study (no link, author, or publication
  given) plus three further external examples offered as the same
  principle recurring across eras and scales.
- **Confidence**: anecdotal for the VB6-to-C# figures specifically (no
  citation or methodology given — could not be independently verified from
  this source); the Stripe figure is corroborated with more detail
  elsewhere in this corpus (see Cross-References); the Spotify figure is
  cited here without further detail and is not independently corroborated
  elsewhere in this corpus
- **Quote**: "A controlled VB6-to-C# study measured 92% behavioral
  equivalence on simple features and 47% on complex ones: unit size is the
  lever. The shape predates agents entirely: Stripe moved 3.7 million lines
  to TypeScript in one PR through months of codemod work, with no agents
  involved, and Google's large-scale-changes chapter explains why atomic
  changes shrink as codebases grow. Spotify now reports 650-plus agent PRs
  merged monthly on rails Backstage built years earlier."
- **Our assessment**: "The shape predates agents entirely" is the load-
  bearing sentence for this source's larger thesis (see Claim 14): by
  reaching for a pre-agent VB6-to-C# study and Google's long-standing
  large-scale-change practice, Osmani argues migration-unit-size sensitivity
  is a property of migrations in general, not something agents introduced
  or something agents make obsolete. As with Claim 7's benchmark citation,
  the complete absence of a source, author, or publication name for the
  VB6-to-C# study means the specific 92%/47% figures should not be treated
  as verified data by the guide — they should be attributed explicitly to
  this source ("Osmani cites an uncredited controlled study...") if used at
  all, pending independent verification.

### Claim 11: Asana's roughly two-week, ~$12,000 removal of its unmaintained Enzyme testing framework is presented as transferring the same pattern as Bun's much larger port — narrow mechanical scope, a pre-existing test suite, and continuous human review of every change
- **Evidence**: A compressed restatement of the Asana case study, with an
  explicit caveat about the cost figure's evidentiary weight.
- **Confidence**: anecdotal (this figure is independently mined in far more
  depth, with the same caveat about the counterfactual, in
  `blog-openai-asana-codex-case-study.md`)
- **Quote**: "Asana cleared a multi-year Enzyme backlog in two calendar
  weeks for about $12,000 in model and infrastructure cost. That $12,000 is
  just a token bill but not a substitute for the five-year staffing
  estimate they had on the books; treat it as a vendor-reported cost of
  generation, not a controlled savings study. The transferable part is the
  same as Bun: a narrow mechanical migration, a pre-existing suite, humans
  still reviewing every change"
- **Our assessment**: Osmani's own hedge here — "treat it as a vendor-
  reported cost of generation, not a controlled savings study" — is
  notably more skeptical than the source case study itself
  (`blog-openai-asana-codex-case-study.md`, an OpenAI-published promotional
  piece); this is a useful example of a practitioner-synthesizer applying a
  more critical read to a vendor case study than the vendor's own framing,
  and the guide can cite Osmani's phrasing directly when discussing how to
  weigh vendor-reported migration cost figures in general, independent of
  the Asana specifics.

### Claim 12: Shopify's Shop consumer app was rebuilt from React Native to native Swift/Kotlin in twelve weeks using a small team and "agent-gated, screen-sized checkpoints," while the much larger merchant app remains an open brownfield problem on the same gates
- **Evidence**: A compressed restatement of the Shopify case study.
- **Confidence**: emerging (this figure and the underlying checkpoint
  mechanism are independently mined in far more depth, including the named
  "Helix" system, in `blog-shopify-back-to-native.md`)
- **Quote**: "Shopify rebuilt the Shop consumer app from React Native to
  native Swift and Kotlin in twelve weeks with a small team and
  agent-gated, screen-sized checkpoints. The much larger merchant app is
  still the brownfield problem: hundreds of screens, deep platform
  integration, same gates, longer clock."
- **Our assessment**: The explicit statement that the larger merchant app
  "is still the brownfield problem... same gates, longer clock" is a useful
  scoping discipline this source applies consistently: rather than
  generalizing the 12-week Shop-app figure to arbitrary app sizes, Osmani
  states directly that the same checkpoint discipline, not a shorter
  timeline, is what should be expected to transfer to the larger app —
  matching the explicit non-extrapolation caveat already flagged in
  `blog-shopify-back-to-native.md` Claim 7's "Our assessment."

### Claim 13: Software factories should parallelize only after one migration unit has a dependable automated judge, recovery path, and human-absorbable review format, because parallel agent output multiplies review bottleneck rather than relieving it, and git worktrees isolate changes but not the shared blast radius of credentials, local services, and network access
- **Evidence**: Author's stated ordering principle (verification before
  parallelism), a specific review-capacity argument, a prescription for how
  automated review should be structured, and a caveat about what worktree
  isolation does and does not provide.
- **Confidence**: emerging (practitioner synthesis; the review-bottleneck
  argument is a structural claim about human attention, not a measured
  study)
- **Quote**: "Parallelism multiplies the bottleneck you already have.
  Automated verification can handle five checked changes. One senior
  reading every line gets a queue, fragmented attention, and eventually
  ceremonial approval." / "I prefer automated review to lead with intent,
  changed invariants, test results, parity mismatches, and the rollback
  route. The complete diff remains available. Human attention goes first to
  the largest blast radius and weakest oracle." / "Worktrees isolate
  changes, not behavior. They may share Git metadata, credentials, local
  services, and network access. Trusted work may accept that tradeoff.
  Unattended agents consuming untrusted content need stronger sandboxes and
  scoped credentials."
- **Our assessment**: The worktrees caveat is the most concrete, actionable
  addition to the corpus's existing worktree coverage: `guide/02-harness-engineering.md`'s
  "Git Worktrees for Parallel Work" section documents worktrees as an
  isolation mechanism for *changes* (avoiding file-level collisions between
  concurrent agent sessions) but does not currently warn that worktrees
  share git metadata, credentials, local services, and network access — a
  distinct, security-relevant claim that worktree isolation is not sandbox
  isolation. This is a direct, specific addition the guide should make,
  not just a restatement. The "human attention goes first to the largest
  blast radius and weakest oracle" prioritization rule is a concrete,
  reusable triage heuristic for review queues under parallel-agent load,
  complementing rather than duplicating the WIP-limit guidance already
  sourced from `blog-addyosmani-code-agent-orchestra.md`.

### Claim 14: Agents changed the price of attempting a migration or trying multiple competing implementations, not the evidence required to choose one, and success should be tracked through process metrics (lead time, review minutes, interventions, escaped defects, rollbacks, oracle mismatches, suppressions, remaining old imports, traffic share on the new path) rather than lines generated
- **Evidence**: Author's closing thesis statement plus two itemized metrics
  lists (general agentic work, and migrations specifically).
- **Confidence**: emerging (practitioner synthesis/framing claim, not a
  measured study)
- **Quote**: "Agents have changed the price of trying several plausible
  implementations. They haven't changed the evidence required to choose
  one." / "Lines generated don't tell you whether the codebase improved. I
  would track lead time, review minutes, human interventions, escaped
  defects, rollbacks, oracle mismatches, and suppressions left behind." /
  "For a migration, track remaining old imports, traffic served by the new
  path, parity mismatches, and legacy dependencies removed. A green suite
  with all traffic still taking the old path is busywork."
- **Our assessment**: "A green suite with all traffic still taking the old
  path is busywork" is the single most quotable line in the source for a
  guide callout: it names a specific, checkable failure mode distinct from
  every other "tests can lie" warning already in the corpus (agent
  self-grading, characterization tests authored by the same session,
  mutation-testing gaps) — a migration can have a fully passing test suite
  while having made zero real progress, because the suite verifies
  correctness of the new path without verifying that the new path is
  actually being used. This is the organizing claim the rest of the post's
  case studies serve as evidence for, and it is the cleanest single
  sentence to cite if the guide adds only one idea from this source.

## Concrete Artifacts

### The zones framework (verbatim)

```
Source: addyosmani.com/blog/brownfield-agentic-engineering/, "Zones" section

Zone definitions:
  Green  = safe / good test coverage / isolated / modern conventions
  Yellow = mixed quality
  Red    = sensitive (auth, billing, permissions, payroll) / few people
           understand it / not for hasty or unsupervised changes

Three enforcement rules:
  1. A person draws the map, not the agent (agents default to the
     "scariest file" because it has the most interesting names)
  2. Zones only move when earned: yellow -> green requires
     characterization tests to exist AND the module owner to have
     reviewed the agent's first changes
  3. The zone sets the verbs:
       green = tight loop (agent works autonomously)
       yellow = tests first (characterization tests before agent changes)
       red = human pairing on every step, or the work does not happen
```

### Instructions / Skills / Plugins / Harness taxonomy (verbatim)

```
Source: addyosmani.com/blog/brownfield-agentic-engineering/,
"When instructions become a harness" section

Instructions — record unusual facts about a repository
Skills       — package reusable procedures (e.g. checking blast radius,
                verifying a schema change)
Plugins      — provide governed access to the ownership catalog, incident
                archive, or dashboards
Harness      — the working environment around the agent as a whole:
                context, tools, permissions, tests, logs, and recovery
Factory      — schedules many dependable loops, keeps durable state, hands
                novel cases back to people

Promotion trigger: "When the same review comment appears again, move it
into a lint rule, hook, type, test, or skill. Keep prose for constraints
that cannot be enforced mechanically."
```

### Migration metrics (verbatim, two lists)

```
Source: addyosmani.com/blog/brownfield-agentic-engineering/,
"Agents put a price on ambiguity" section

General agentic-work metrics:
  - lead time
  - review minutes
  - human interventions
  - escaped defects
  - rollbacks
  - oracle mismatches
  - suppressions left behind

Migration-specific metrics:
  - remaining old imports
  - traffic served by the new path
  - parity mismatches
  - legacy dependencies removed
```

### Six external case studies referenced (as compressed in this source; see
Cross-References for which are independently verified elsewhere in this
corpus)

```
Source: addyosmani.com/blog/brownfield-agentic-engineering/

1. Netflix GraphQL cutover — replay/shadow traffic diffed against old and
   new paths; promote only when payloads match. (No link given.)
2. SWE Refactor Bench — 28/520 agent runs passed a "migration audit,
   behavioral tests, and independent verification"; names the failure mode
   "Blindness." (No link, publisher, or methodology given.)
3. Bun Zig-to-Rust port — ~50 workflows, 11 days, 535,000-line codebase,
   two adversarial reviewers per unit, full pre-existing test suite as
   merge gate, porting guide written before any agent ran.
4. Anthropic's internal migration process — disposable mini-migration used
   to stress-test and discard a trial rulebook before the broad run.
5. VB6-to-C# controlled study — 92% behavioral equivalence on simple
   features, 47% on complex features. (No link, author, or publication
   given.)
6. Stripe — 3.7 million lines moved to TypeScript in one PR via months of
   codemod work, no agents involved.
7. Google's "large-scale-changes chapter" — cited as explaining why atomic
   changes shrink as codebases grow. (No link given.)
8. Spotify — 650+ agent PRs merged monthly on pre-existing Backstage rails.
   (No link or further detail given.)
9. Asana — Enzyme testing-framework removal, ~2 calendar weeks, ~$12,000
   model/infrastructure cost vs. a 5-year internal staffing estimate.
10. Shopify — Shop consumer app rebuilt React Native -> native Swift/Kotlin
    in 12 weeks, "agent-gated, screen-sized checkpoints"; merchant app
    migration still open/longer.
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-bun-rust-rewrite.md` (Claims 5–8, 10–11) and
    `blog-anthropic-code-migration-playbook.md` (Claims 2, 4, 7) — this
    source's Claim 9 (Bun porting guide, 50 workflows, 11 days, adversarial
    review, full test suite gate) restates figures already independently
    verified at primary-source depth in both notes; no new figures are
    introduced here for Bun.
  - `blog-anthropic-code-migration-playbook.md` Claim 7 (Step 2, "stress-test
    the rules": disposable mini-migration, "throw out any translated
    files... the goal is to refine the rules, not make incremental
    progress") directly corroborates this source's Claim 9 characterization
    of "Anthropic's own migration process stress-tests its rulebook on a
    disposable mini-migration and throws the trial output away."
  - `blog-openai-asana-codex-case-study.md` (Claims 1–2, 7) — this source's
    Claim 11 restates the ~2-week/$12,000-vs-5-year-estimate figures with an
    explicit "not a controlled savings study" hedge that is, notably, more
    skeptical than the OpenAI case study's own framing.
  - `blog-shopify-back-to-native.md` (Claims 6–9) — this source's Claim 12
    restates the 12-week Shop-app rebuild and "agent-gated... checkpoints"
    language, which corresponds to the much more detailed "Helix" checkpoint
    system (tests + visual review + two adversarial reviewers + human
    approval per checkpoint) documented in that note's Claim 9.
  - `blog-addyosmani-code-agent-orchestra.md` (Claim 5, "the bottleneck has
    shifted from code generation to verification"; Claim 11, git worktrees
    as a recommended isolation pattern) — this source's Claim 13 (worktrees
    isolate changes, not behavior; automated verification vs. human review
    capacity) is a direct extension of both claims into a specific caveat
    (worktrees are not a security/credential boundary) and a specific
    prioritization rule (blast radius + weakest oracle first) that the
    earlier, more general post does not state.
  - `blog-addyosmani-intent-debt.md` (Claim 2, agents fabricate plausible-
    sounding rationale rather than admitting uncertainty; Claim 8, AGENTS.md
    as an "intent ledger") — this source's Claim 2 ("write down what the
    code can't say, and nothing else") is the same underlying discipline
    (externalize only non-inferable rationale) applied specifically to
    brownfield/legacy constraints rather than to intent debt in general.

- **Contradicts**: None filed. This source's emphasis on characterization
  tests, complete-unit migrations, and human-drawn zone boundaries before
  any full rewrite is attempted is consistent with — not opposed to — the
  reconciling pattern already proposed (but not resolved) in
  `blog-simonwillison-rewrite-two-systems-trap.md` Cross-References →
  Extends (that full rewrites/migrations succeed specifically when a team
  retains deep familiarity with the system and uses a rigorous,
  pre-existing or purpose-built behavioral oracle, rather than a new team
  guessing at undocumented behavior). This source adds a fourth
  corroborating instance of that same pattern (characterization tests as
  the oracle, human review as the zone-promotion gate) rather than a fifth
  data point requiring its own contradiction issue — see issue #3370 for
  the underlying Willison-vs-Willison tension this pattern was proposed to
  reconcile, which this source does not itself engage with or cite.

- **Extends**:
  - `blog-addyosmani-code-agent-orchestra.md` Claim 7 / Linked Source 1
    (the AGENTS.md "filter test": "can the agent discover this by reading
    the code? Yes = delete it. No = keep it.") — this source's Claim 2
    restates the same filter as "write down what the code can't say, and
    nothing else," and Claim 4's "repeated review comment -> promote to a
    mechanical layer" trigger extends the filter into an ongoing
    maintenance discipline rather than a one-time authoring rule.
  - `guide/02-harness-engineering.md` "Git Worktrees for Parallel Work" —
    this source's Claim 13 adds a security-relevant caveat (shared git
    metadata, credentials, local services, network access) not currently
    present in that section, which documents worktrees primarily as a
    file-collision isolation mechanism.
  - `guide/03-verification.md` "Green tests that never touch the risky
    code" — this source's Claim 5 (agent-authored characterization tests
    encode the agent's own implementation rather than pinning prior
    behavior) and Claim 14 ("a green suite with all traffic still taking
    the old path is busywork") are both migration-specific variants of the
    same "passing tests aren't sufficient evidence" family already in that
    section, adding two new, specific instances of the pattern.

- **Novel**:
  - The three-rule zones enforcement procedure (human-drawn map, earn-to-
    promote, zone-sets-verbs) as a named, formalized framework — no
    existing corpus note proposes a comparable risk-zoning model for where
    agents may work in a legacy codebase.
  - "SWE Refactor Bench" and its "migration Blindness" failure mode (Claim
    7) — entirely new to the corpus, though unverifiable from this source
    alone (no link or citation given).
  - The VB6-to-C# controlled study and its 92%/47% behavioral-equivalence
    figures (Claim 10) — also new to the corpus and also unverifiable from
    this source alone.
  - The explicit claim that worktrees are not a credential/security
    boundary (Claim 13) — a specific, actionable caveat not previously
    stated in the corpus's existing worktree coverage.
  - The migration-specific metrics list (remaining old imports, traffic
    share on the new path, parity mismatches, legacy dependencies removed)
    as a named alternative to "lines generated" — new to the corpus in this
    specific, itemized form.

## Guide Impact

- **`guide/02-harness-engineering.md` — "Git Worktrees for Parallel Work"**:
  Add Claim 13's caveat verbatim-in-substance: worktrees isolate file-level
  changes, not behavior — they share git metadata, credentials, local
  services, and network access, so unattended agents consuming untrusted
  content need a stronger sandbox boundary than a worktree alone provides.
  This is a gap in the current section, which frames worktrees purely as a
  collision-avoidance mechanism for concurrent sessions.
- **`guide/03-verification.md` — "Green tests that never touch the risky
  code"**: Add Claim 5's specific warning that agent-authored
  characterization tests risk encoding the agent's own new implementation
  rather than pinning prior behavior — cite the source's own definition of
  characterization testing plus the "pin the behavior first, in a separate
  pass or by a person; then let the agent work" sequencing rule. Add Claim
  14's "a green suite with all traffic still taking the old path is
  busywork" as a named migration-specific instance of the passing-tests-
  aren't-sufficient-evidence pattern, alongside the migration-specific
  metrics list (Concrete Artifacts) as a concrete alternative to
  lines-of-code-generated as a success metric.
- **`guide/00-principles.md` — "Deterministic Tools for Deterministic
  Work"**: Add Claim 8's "give agents the exception queue" framing (routine
  mechanical migration steps go to a codemod; agents handle only what the
  codemod can't) as a migration-specific instance of the existing
  principle, citing Stripe's no-agents TypeScript migration as the source's
  own illustrative counterpoint.
- **`guide/01-daily-workflows.md`**: Add the zones framework (Claim 1) and
  the durable comprehension-memo pattern (Claim 3) as concrete brownfield-
  specific workflow additions — the "claims should cite a file, issue,
  ownership record, or dashboard" requirement for the memo is a specific,
  checkable rule not currently present anywhere in the guide's research/
  exploration-phase guidance.
- **`guide/05-team-adoption.md`**: Add Claim 13's review-bottleneck
  argument ("parallelism multiplies the bottleneck you already have") and
  its prescribed review-prioritization rule (lead with intent, invariants,
  test results, parity mismatches, and rollback route; human attention to
  the largest blast radius and weakest oracle) as a companion to the
  existing WIP-limit guidance sourced from
  `blog-addyosmani-code-agent-orchestra.md` — this source supplies the
  *ordering* principle ("copy the parallelism part only after one unit has
  a dependable judge, recovery path, and review format") that the WIP-limit
  number alone doesn't capture.
- **Do not cite** the SWE Refactor Bench "28/520... Blindness" figure
  (Claim 7) or the VB6-to-C# "92%/47%" figures (Claim 10) as verified
  statistics — both are given without a link, author, or publisher in the
  source, and neither could be independently located or verified during
  this extraction. If cited at all, attribute explicitly to Osmani's post
  rather than presenting as an independently confirmed study.

## Extraction Notes

- The source was fetched via `curl` directly (the live page, not an
  archive snapshot) and converted to plain text by stripping HTML tags
  programmatically, specifically so every `Quote` field above could be
  checked character-for-character against the raw extracted text rather
  than a WebFetch summarization pass, per MINER.md §2a. No paywall, dead
  link, or access issue was encountered.
- No linked sub-pages were followed. The post's "Related reading" footer
  links to three of the author's own prior posts (Agentic Skill Decay,
  Audit your Agent files, Human judgment doesn't leave the software
  factory) — all three are already mined in this corpus
  (`blog-addyosmani-agentic-skill-decay.md`,
  `blog-addyosmani-audit-agent-files.md`,
  `blog-addyosmani-human-judgment-relocates.md`) and were not re-fetched.
  A closing call-to-action links to the author's forthcoming O'Reilly book
  and newsletter signup — promotional, not substantive, not followed.
- None of the six external case studies this post references (Netflix,
  SWE Refactor Bench, the VB6-to-C# study, Stripe, Google's large-scale-
  changes practice, Spotify) are linked with a URL anywhere in the source
  page. Four of the six (Bun, Anthropic's internal process, Asana,
  Shopify) are independently corroborated at much greater depth by
  existing primary/closer-to-primary sources already in this corpus (see
  Cross-References). The other three (Netflix's GraphQL cutover, SWE
  Refactor Bench, the VB6-to-C# study, Google's large-scale-changes
  chapter, Spotify/Backstage) are novel to the corpus but entirely
  unverified beyond this one secondhand mention — flagged explicitly in
  each relevant claim's confidence rating and in Guide Impact's "do not
  cite" note. These are strong candidates for their own future source
  submissions if primary sources can be located (e.g., a Netflix
  engineering blog post on the GraphQL cutover, a paper or repo for "SWE
  Refactor Bench," Google's actual large-scale-changes documentation).
- The Prospector's two triage comments on issue #3611 both proposed
  chapter numbers (Ch02/03/05/07 in the first comment; Ch06/07/08/09 in the
  second) that only partially match the guide's actual structure. The
  live `guide/` directory contains six chapters, `00-principles.md` through
  `06-security-threat-model.md` — there is no Ch07, Ch08, or Ch09. Guide
  Impact above maps this source's content to the real chapters
  (`00-principles.md`, `01-daily-workflows.md`, `02-harness-engineering.md`,
  `03-verification.md`, `05-team-adoption.md`) verified against the actual
  file contents rather than the triage comments' chapter numbers.
- No contradiction with any existing corpus note was found that would
  warrant filing a new contradiction issue; see Cross-References →
  Contradicts for why this source is read as extending, rather than
  opposing, the reconciling pattern already proposed under issue #3370.
