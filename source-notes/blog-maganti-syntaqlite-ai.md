---
source_url: https://lalitm.com/post/building-syntaqlite-ai/
source_type: blog-post
title: "Eight years of wanting, three months of building with AI"
author: Lalit Maganti
date_published: 2026-04-05
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: emerging
issue: "#88"
---

# Lalit Maganti: Eight Years of Wanting, Three Months of Building with AI

> A long-form, first-person account of building syntaqlite — a production-grade
> SQLite parser/linter/formatter — that validates both the power and the hard
> limits of AI coding agents: AI demolished eight years of procrastination in
> three months, yet a fully vibe-coded first attempt had to be thrown away and
> rebuilt by hand because AI cannot make coherent architectural decisions on
> open-ended problems. Surfaces the implementation/design asymmetry as the
> core skill boundary of the AI age, and offers the "relativity" framework for
> knowing which zone you are in at any moment.

## Source Context

- **Type**: blog-post (long-form practitioner essay)
- **Author credibility**: Lalit Maganti is a software engineer at Google
  who maintains PerfettoSQL, a SQLite-based query language for performance
  traces used at approximately 100,000 lines of internal usage. He has
  prior open-source experience building developer tools as a teenager, deep
  C++ and Android performance expertise, and used Claude Code on the Max
  plan (£200/month) for three months of sustained, real-project work on
  syntaqlite — a linting, verification, parsing, and formatting library for
  SQLite intended for language servers and editor extensions. This is not a
  weekend toy or a one-off script. Simon Willison described it as "one of my
  favorite pieces of long-form writing" in his own link post.
- **Scope**: The full development arc of syntaqlite — from eight years of
  procrastination, through a discarded vibe-coded first attempt
  (January), to a deliberate human-led rewrite in Rust (February–March).
  Covers both where AI helped (breaking inertia, churning standard code,
  teaching unfamiliar domains, shipping the feature long-tail) and where AI
  hurt or failed (architectural dead ends, mental model erosion, design
  decision deferral, no institutional memory, tests as false comfort).
  Does NOT cover team adoption, MCP configuration, harness engineering, or
  multi-agent workflows.

## Extracted Claims

### Claim 1: AI breaks the procrastination loop by converting abstract design anxiety into concrete prototype problems
- **Evidence**: Author's direct account. Eight years of not starting; one
  month of AI-assisted prototyping produced a functional (if fragile)
  prototype.
- **Confidence**: anecdotal
- **Quote**: "AI let me put aside doubts by giving concrete problems to work
  on rather than endless abstract thinking. Instead of wrestling with 'I need
  to understand SQLite's parsing,' the immediate challenge became 'I need to
  get AI to suggest an approach so I can evaluate and improve it.'"
- **Our assessment**: Credible mechanism. The shift is from design
  anxiety (no concrete next step) to evaluation work (is this AI output
  good?). Evaluation is a different, lower-friction cognitive mode. This
  matches how other practitioners describe AI overcoming inertia, and it
  doesn't require the first prototype to survive — it just needs to start
  the momentum. High value for Ch01 (daily workflows): describe this as
  the "bootstrap" use of AI, not the production use.

### Claim 2: Vibe-coded first attempts can become architecturally unrepairable
- **Evidence**: Author's direct experience. The January prototype accumulated
  over 500 tests but had "complete spaghetti" architecture with "scattered
  functions, unclear organization, and multiple files reaching several
  thousand lines." The author discarded it entirely and rewrote from scratch.
- **Confidence**: anecdotal (single author), but corroborated by Miller
  et al. Claim 2 (41.6% persistent cognitive complexity increase after AI
  adoption) and by the practitioner-dadlerj-tin.md pattern contrast.
- **Quote**: "The codebase had become complete spaghetti with scattered
  functions, unclear organization, and multiple files reaching several
  thousand lines. While the approach proved viable and generated over 500
  tests, the fragile architecture couldn't support the author's larger
  vision."
- **Our assessment**: The 500 tests give a false sense of solidity. Tests
  prove function-level correctness, not architectural coherence. The Miller
  paper's 41.6% cognitive complexity increase is the population-level
  version of this individual story. The throw-away prototype is not a
  failure — it's an expensive lesson. The guide should frame this
  explicitly: vibe-coding is a prototyping tool, not an architectural one.

### Claim 3: AI excels at writing standard, obvious code and produces it faster and more completely than most humans
- **Evidence**: Author's comparison over three months of real use.
- **Confidence**: emerging (corroborated widely)
- **Quote**: "Given clear specifications like 'write a function with this
  behavior and parameters' or 'write a class matching this interface,' AI
  produced code faster than I would have, often in more intuitive styles.
  The AI-generated code included documentation I might skip, maintained
  consistency, and adhered to standard language conventions."
- **Our assessment**: This claim is well-supported across the corpus. The
  important nuance here is "standard code" — predictable, readable,
  unsurprising. This is the majority of any codebase.

### Claim 4: AI's normalization instinct actively hinders "edge" components where value comes from non-obvious approaches
- **Evidence**: Author's direct observation on the extraction pipeline and
  parser architecture of syntaqlite — the components requiring genuinely
  novel design.
- **Confidence**: anecdotal
- **Quote**: "Every project contains 'edge' pieces where value derives from
  non-obvious approaches. For syntaqlite, the extraction pipeline and parser
  architecture embodied this distinction. AI's normalization instinct
  actively hindered these components, requiring me to design them deeply or
  write them personally."
- **Our assessment**: This is the sharper half of Claim 3. AI's strength
  (standardization) is a weakness for the 5-20% of a codebase that
  genuinely needs unusual structure. Identifying which components are "edge"
  components requires the same taste and experience that makes designing
  them hard. This is a subtle but important claim for Ch01: the skill of
  AI-assisted engineering is knowing when to hand back the keyboard.

### Claim 5: AI as teaching assistant has the highest value-to-time ratio of any use
- **Evidence**: Author's cross-use-case comparison over three months.
- **Confidence**: anecdotal
- **Quote**: "Research showed the highest value-to-time-spent ratio among
  all AI applications. While I had worked with interpreters and parsers,
  Wadler-Lindig pretty-printing was entirely new. AI delivered focused,
  understandable lessons and pointed toward papers for deeper learning. This
  compressed potentially days of self-directed reading into efficient
  conversations."
- **Our assessment**: Developing the VS Code extension took "approximately
  one hour" with AI; the author estimates it would have taken "days of API
  learning" otherwise. This is plausible — learning unfamiliar but not
  novel domains is exactly where AI's broad training data provides leverage.
  The key condition: the fundamentals remain similar to what you know.
  Domain transition (C++ → Rust tooling, Python → VS Code APIs) is where
  this shines. Novel fundamentals (Wadler-Lindig) require human verification
  of the output.

### Claim 6: AI enabled shipping a much larger feature set than the author would have shipped alone
- **Evidence**: Concrete list of features attributed to AI making them
  "sufficiently inexpensive that skipping them felt wrong."
- **Confidence**: emerging
- **Quote**: "Without AI, the project would have shipped significantly
  smaller — probably without editor extensions or documentation sites. AI
  didn't merely accelerate the same project; it transformed what the project
  became."
- **Our assessment**: The feature long-tail claim is credible and consistent
  with the Shopify playbook's observation that AI lets engineers ship what
  they previously deprioritized. The author specifically lists: VS Code
  extension, Python bindings, WASM playground, documentation site, and
  multi-ecosystem packaging. These are exactly the tasks that have clear
  specs but high per-unit effort — precisely the "standard code" zone where
  AI is strongest (Claim 3).

### Claim 7: AI makes design-decision deferral feel consequence-free — but it isn't
- **Evidence**: Author's reflection on the vibe-coding month.
- **Confidence**: anecdotal
- **Quote**: "AI tempted me into procrastinating key design decisions.
  Because refactoring was cheap, deferring became easy, and
  industrial-scale AI refactoring made deferral feel consequence-free. But
  it wasn't: deferring corroded clear thinking because confusing codebases
  persisted meanwhile."
- **Our assessment**: This is the most important negative claim in the
  source and the one most counterintuitive. The usual argument for
  AI-assisted development is "refactoring is cheap, so defer decisions."
  Maganti directly contradicts this: the confused codebase is a tax on
  thinking, not just a technical debt. Even if you can refactor cheaply
  later, the time you spend navigating a poorly organized codebase is
  lost. For Ch01 and Ch02: refactoring ease does not eliminate the cost
  of architectural confusion during development.

### Claim 8: Tests give false comfort — they do not substitute for architectural clarity
- **Evidence**: Author's 500+ tests from the vibe-coded prototype that still
  required a full restart.
- **Confidence**: anecdotal
- **Quote**: "Over 500 tests felt reassuring, and AI facilitated generation
  of more. However, neither humans nor AI creatively foresee every future
  edge case encountered; during vibe-coding, discovering test cases revealed
  component designs requiring complete reworking."
- **Our assessment**: The vibe-coded prototype had a large test suite AND
  had to be discarded. This is the empirical proof that tests certify
  function-level behavior, not architectural soundness. The Miller paper
  Claim 3 (30.3% persistent increase in static analysis warnings) provides
  population-level corroboration that AI-generated test suites are not
  catching the structural problems. The guide should explicitly distinguish
  "test coverage" from "architectural confidence" when recommending
  AI-assisted testing practices.

### Claim 9: Mental model erosion causes communication breakdown with the agent
- **Evidence**: Author's multi-instance first-person observation.
- **Confidence**: anecdotal
- **Quote**: "Without mental threading through system operations, meaningful
  agent communication became impossible. Every exchange grew longer and more
  verbose. Instead of 'change FooClass to do X,' requests became 'change the
  thing which does Bar to do X,' requiring the agent to determine Bar, map
  it to FooClass, sometimes getting it wrong. This precisely parallels
  long-standing engineer complaints about managers who don't understand code
  requesting fanciful or impossible things — except now the author had become
  that manager."
- **Our assessment**: This is a concrete, vivid diagnosis of a failure mode
  that other sources gesture at but don't name. The "manager who doesn't
  understand code" framing is exactly right: when you lose your mental model,
  you lose the ability to scope your requests tightly, and scope creep in
  agent prompts produces worse output that generates more confusion. The fix
  the author found: "regularly reading recently-implemented code and actively
  engaging to ask 'how would I have done this differently?'" — deliberate
  re-ownership of the codebase as a practice, not as an exception.

### Claim 10: AI has no sense of time — it cannot carry institutional knowledge
- **Evidence**: Author's reflection on AI repeatedly re-encountering solved
  problems.
- **Confidence**: anecdotal
- **Quote**: "AI sees codebases in specific states but doesn't feel time
  like humans do. The natural problem involves repeating past mistakes,
  requiring relearning lessons, or falling into new traps successfully
  avoided before."
- **Our assessment**: This is the structural explanation for why the
  failure-decker-4hr-session-loss pattern exists: there is nothing inside
  the agent that accumulates institutional knowledge between sessions the
  way a human engineer does. Even within a session, as Claim 9 shows, the
  agent's knowledge is only as good as the prompt it receives. The author's
  proposed mitigation (updated specs and documentation) is the right
  direction but introduces its own cost: "capturing exhaustive implicit
  design decisions is expensive and time-consuming" and "AI can draft
  documentation, but without automatic verification accuracy, humans must
  still manually audit results."

### Claim 11: The AI slot machine loop creates unproductive late-night sessions
- **Evidence**: Author's introspective account.
- **Confidence**: anecdotal
- **Quote**: "Uncomfortable parallels exist between using AI coding tools and
  playing slot machines. Sending prompts, waiting, and receiving either
  excellent or useless results creates a feedback loop... When tired, prompts
  became vague, output degraded, and repetition increased fatigue. In these
  states, AI probably proved slower than self-implementation, but breaking
  the loop proved psychologically difficult."
- **Our assessment**: The tiredness loop is a real negative externality of
  AI-assisted coding that no other source in our corpus has named explicitly.
  The implication for Ch01: AI is a force multiplier on your current
  cognitive state. A sharp engineer gets sharper output; a tired engineer
  gets a vague-prompt → worse-output → more-iterations → more-fatigue spiral.
  This argues for stopping points, not just handoff points.

### Claim 12: The relativity framework — three distinct zones where AI performs differently
- **Evidence**: Author's synthesis from three months of practice, including
  the public API refactoring incident as a concrete example of the failure
  zone.
- **Confidence**: emerging (well-reasoned, corroborated by Claim 4 and
  Miller Claim 6)
- **Quote**: "When working on deeply understood territory, AI excelled...
  When working on describable-but-unknown territory, AI performed well with
  increased care requirements... When working on territory where even desired
  outcomes remained unclear, AI became unhelpful or harmful... Understanding
  where one sits on these axes at any moment represents, the author argues,
  the core skill of effective AI usage."
- **Our assessment**: This is the highest-value meta-claim in the source.
  The three-zone taxonomy (deeply known / describable-unknown / outcomes
  unclear) is the most precise conceptual framework for task delegation
  we have found. It explains why the same tool that can implement 400
  grammar rules in days cannot design a public API in weeks. The local vs.
  global frame (code level has right answers; architecture emerges from
  component interactions and can't be derived locally) is the physics
  analogy the author uses, and it is apt. Recommend this as the Ch00 or
  Ch01 organizing framework for "when to use AI for what."

### Claim 13: The implementation/design asymmetry is the core boundary of AI coding
- **Evidence**: Public API refactoring incident (several days of manual
  cleanup in early March). "No test or objective metric exists for 'is this
  API pleasant?' or 'will this help users solve problems they face?'"
- **Confidence**: emerging
- **Quote**: "Implementation has a right answer, at least at a local level:
  the code compiles, the tests pass. Design doesn't. Disputes about OOP
  continue decades after its introduction."
- **Our assessment**: This is the precise formulation of why AI excels at
  implementation and struggles with design. Objectively verifiable tasks
  are AI tasks; tasks without a checkable answer require human judgment.
  This is not new as an insight — the Miller paper's methodology implicitly
  assumes the same thing — but Maganti states it most clearly and grounds
  it in a specific, painful example (the public API mess). The guide should
  use this framing as the definitional boundary in Ch00 and return to it
  throughout.

## Concrete Artifacts

### The throw-away prototype → deliberate rebuild cycle

From the "How it happened" section (paraphrased from the source, with direct
quotes):

**January (vibe-coding month):**
- Stack: Python scripts extracting C parser from SQLite + formatter +
  PerfettoSQL extension support + web playground
- Approach: "maximalist approach using Claude Code on the Max plan
  (£200/month), essentially delegating design and implementation while
  acting as a semi-technical manager"
- Result: A functional prototype with 500+ tests, but "complete spaghetti"
  with "scattered functions, unclear organization, and multiple files
  reaching several thousand lines"
- Verdict: Discarded

**February–March (deliberate rewrite):**
- Stack: Rust (for validator and language server), C (for the parser
  extracted from SQLite)
- Approach: "taking complete ownership of decisions while using AI more
  carefully as 'autocomplete on steroids' within a structured process
  emphasizing careful design, thorough review, eager problem-fixing, and
  robust scaffolding"
- Result: A library "that can stand the test of time," shipped mid-March
  with VS Code extension, Python bindings, WASM playground, docs site,
  multi-ecosystem packaging

### The three-zone relativity framework

Direct from source:

```
Zone 1 — Deeply known territory:
  "AI excelled. Could instantly review output, catch mistakes before
  landing, and move at unprecedented pace."
  Example: Parser rule generation — 400 grammar rules, each reviewable
  in minutes.

Zone 2 — Describable-but-unknown territory:
  "AI performed well with increased care requirements. But disengagement
  wasn't possible; AI's suggestions required active evaluation."
  Example: Learning Wadler-Lindig pretty-printing — could articulate
  desired outcomes, evaluate directional correctness, learn from
  explanations.

Zone 3 — Outcomes unclear territory:
  "AI became unhelpful or harmful. Weeks following AI down dead ends
  exploring productive-feeling designs that collapsed under scrutiny."
  Example: Early architecture design — "In hindsight, I wonder if it
  would have been faster just thinking it through without AI."
```

### The mental model repair practice

```
Fix: "Regularly reading recently-implemented code and actively engaging
to ask 'how would I have done this differently?'"

All code can suffer from this issue when written months prior, but AI
accelerates this drift because original typing doesn't build the same
muscle memory.
```

## Cross-References

- **Corroborates**: paper-miller-speed-cost-quality Claim 2 (41.6%
  persistent cognitive complexity increase after AI adoption). Miller et al.
  provide the population-level empirical foundation for Maganti's
  individual experience of "complete spaghetti" after vibe-coding. Claim 7
  (design deferral) is the individual mechanism; the Miller paper is
  the aggregate outcome.

- **Corroborates**: paper-miller-speed-cost-quality Claim 4 (velocity gains
  decay to zero by month 3). The vibe-coded prototype was productive in
  month 1 and unsalvageable by month 3 — exactly the decay curve Miller
  measures at the OSS project level.

- **Corroborates**: paper-miller-speed-cost-quality Claim 6 (the mechanism
  is velocity → codebase size → technical debt, not AI introducing more
  bugs per line). Maganti's experience is the first-person version: AI
  let him produce code faster, and his existing project dynamics (no
  architectural discipline) played out at scale. The fix was process
  (deliberate design, eager refactoring), not less AI.

- **Corroborates**: failure-decker-4hr-session-loss (institutional knowledge
  is destroyed when context is lost). Maganti's Claim 10 (no sense of time)
  is the structural reason the decker failure is irreparable: even if you
  restore the session file, the agent has no memory of *why* decisions
  were made unless it was written somewhere durable.

- **Extends**: blog-osmani-good-spec.md — Osmani recommends writing specs
  before implementing. Maganti's failure during vibe-coding is the
  negative case: no spec, no architectural discipline, no protection from
  decision deferral debt. Claim 7 (deferral corrodes thinking) is the
  mechanism that makes Osmani's recommendation non-optional. Maganti also
  extends Osmani's Claim 5 (the "curse of instructions") — Maganti's Claim
  13 identifies the deeper reason: the problem isn't instructions per se,
  it's that design has no objectively verifiable answer for the model to
  optimize toward.

- **Extends**: blog-french-owen-coding-agents-feb-2026 Claim 3 (externalize
  state to the filesystem). Maganti's Claim 10 shows exactly what happens
  when you don't: the agent repeats past mistakes. The institutional
  knowledge that would prevent this can only be preserved if written down.
  French-Owen states the pattern; Maganti demonstrates the failure cost.

- **Complements (positive contrast)**: practitioner-dadlerj-tin.md (100%
  vibe-coded, all working). tin is a much narrower-scope tool (thread
  version control) with a single developer who appears to have strong
  domain knowledge of both the problem and the solution space. Maganti's
  experience suggests the key variable is Zone 1 coverage: if the entire
  project is in deeply-known territory, vibe-coding works. syntaqlite's
  parser architecture was Zone 3 for Maganti (SQLite internals, unknown
  territory) — that's where vibe-coding failed. Not a contradiction; a
  conditioning variable.

- **Novel**: The relativity framework (Zone 1 / 2 / 3 taxonomy for
  task-level AI delegation) is the clearest articulation in our corpus of
  *when* AI helps vs. hurts. No other note provides this level of
  task-level specificity.

- **Novel**: The mental model erosion → communication degradation chain
  (Claim 9) is named here for the first time. Other sources describe
  context loss from the tool side (compaction, session end); Maganti
  describes it from the human side.

- **Novel**: The throw-away prototype as a *feature*, not a failure — the
  first attempt broke inertia, validated the approach, and taught the
  author what architecture was needed. The guide should frame this as a
  deliberate strategy, not an accident.

## Guide Impact

- **Chapter 00 (Principles)**: Use the relativity framework (Claim 12) as
  the organizing principle for "when to use AI for what." Zone 1 = delegate
  freely; Zone 2 = delegate with active review; Zone 3 = think first, use
  AI for Zone 1/2 sub-tasks. Use the implementation/design asymmetry (Claim
  13) as the definitional boundary. These two claims should inform how Ch00
  frames the entire book.

- **Chapter 01 (Daily Workflows)**: Add the prototype-first pattern (Claim
  1) as a legitimate workflow entry point for large projects facing
  procrastination. Explicitly distinguish it from the production workflow:
  the prototype is for momentum and architecture discovery, not for shipping.
  Add the mental model repair practice (Claim 9 concrete fix) as a
  recommended daily or weekly habit for anyone using AI heavily.

- **Chapter 01 (Daily Workflows)**: Add the tiredness loop anti-pattern
  (Claim 11). Stopping points are not optional — they are part of the
  workflow. The signal: "prompts became vague and output degraded" means
  stop, not try harder.

- **Chapter 02 (Harness Engineering)**: Cite Claim 7 (design deferral
  creates real debt) as the counter-argument to "refactoring is cheap."
  Even if you can refactor, a confused codebase is expensive to *think in*.
  The harness should enforce architectural checkpoints (e.g., a required
  ADR or design review step before large features), not just lint/test/typecheck.

- **Chapter 02 (Harness Engineering)**: Cite Claim 4 (normalization
  instinct hinders "edge" components) as the rationale for keeping
  architecture design outside the agent's autonomous zone. The harness
  should have a "human-owns-design" gate for components the team identifies
  as architecturally critical.

- **Chapter 05 (Team Adoption)**: Lead the "quality vs. velocity" section
  with Maganti's two-attempt narrative. The vibe-coded first attempt is the
  cautionary case: velocity in month 1, complete restart by month 3. The
  second attempt is the model: AI as "autocomplete on steroids" inside a
  human-disciplined process. Cross-cite Miller et al. (Claim 4) for the
  empirical population-level version.

- **Chapter 05 (Team Adoption)**: Use Claim 6 (feature long-tail shipping)
  as the strongest positive framing for AI adoption ROI. The value isn't
  just faster core features — it's the VS Code extensions and docs sites
  that would otherwise never ship.

## Extraction Notes

- **Primary source is Lalit Maganti's full article** at
  `https://lalitm.com/post/building-syntaqlite-ai/`. Simon Willison's link
  post at `https://simonwillison.net/2026/Apr/5/building-with-ai/` is the
  discovery entry point (the issue URL) but contains only a brief summary.
  Both pages were fetched; all claims are extracted from Maganti's full text.
- **Syntaqlite is a real, shipped project** — not a prototype or a toy.
  The claims here are grounded in production-grade work (language servers,
  editor extensions, multi-ecosystem packaging) on a technically demanding
  problem (SQLite parser without a formal specification). Weight accordingly.
- **Single-author limitation**: All claims are one engineer's experience on
  one project. The Miller paper provides empirical corroboration for the
  structural claims (spaghetti architecture, velocity decay), but the
  taxonomy and the "relativity" framework are the author's own synthesis.
  Tag Zone 1/2/3 framework as "emerging" not "settled" until more
  practitioners validate it.
- **Month-1 vibe-coding cost**: The author estimates he lost an entire month
  to the discarded prototype. This is the most concrete cost estimate in the
  source for the "wrong use of AI" failure mode. It should be cited
  quantitatively in the guide where relevant.
- **The public API incident** (several days of manual refactoring in early
  March) is the best concrete example of the Zone 3 failure. No quote
  was available for the specific number of days, but the author says "several
  days of manual API refactoring, fixing total messes that experienced
  engineers would instinctively avoid but AI created."
