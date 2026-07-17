---
source_url: https://claude.com/blog/ai-code-migration
source_type: blog-post
title: "How Anthropic runs large-scale code migrations with Claude Code"
author: Anthropic (Claude team, no individual byline; features named practitioners Jarred Sumner and Mike Krieger)
date_published: 2026-07-16
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1954"
---

# How Anthropic runs large-scale code migrations with Claude Code

> Anthropic's first-party generalized methodology for AI-driven code migrations
> — a six-step process (rulebook/dependency-map/gap-inventory, stress-test,
> translate, compile, run, match-behavior) distilled from two case studies:
> Jarred Sumner's Bun Zig-to-Rust rewrite (already deeply mined in the corpus)
> and a previously undocumented second case, Mike Krieger's 165,000-line
> Python-to-TypeScript port completed in a weekend.

## Source Context

- **Type**: blog-post (official Anthropic blog, claude.com/blog, published
  July 16, 2026; ~2,300 words with two code-comparison graphics, a process
  diagram, and a "Related" section linking to a migration starter kit and a
  code-modernization plugin)
- **Author credibility**: First-party Anthropic publication, editorial "we"
  voice throughout ("In this article we'll cover two examples along with best
  practices from these projects," "Below is the six-step process we now use").
  No individual Anthropic author byline is given. The post's evidentiary weight
  comes from two named, verifiable practitioners it quotes and draws
  methodology from: Jarred Sumner ("co-founder of Bun and Member of Technical
  Staff at Anthropic") and Mike Krieger ("co-lead of Anthropic Labs" — Krieger
  is Instagram's co-founder and Anthropic's Chief Product Officer, though the
  post itself only credits him as "co-lead of Anthropic Labs"). Both are
  first-party, named, and hold Anthropic staff positions, which raises
  authority but also means neither is an independent third party validating
  Anthropic's own product claims.
- **Scope**: Covers the business case for migrations ("why and when to
  migrate"), why AI changes the economics (five structural properties of
  migration work), a six-step generalized process with a "prerequisites"
  section on building a verification "judge," two concrete code-gap examples
  (Zig→Rust manual memory management, Python→TypeScript interface contracts),
  a best-practices list, and outcome metrics for both the Bun and Krieger
  migrations. Does NOT cover: the specific model versions beyond "Claude Fable
  5" and "Claude Opus 4.8" named generically (no mention of the "pre-release
  Mythos-class" designation Sumner uses in his own post), the adversarial-review
  reviewer-isolation mechanics at Sumner's level of detail (only "two
  adversarial reviewers... disagreement... goes to a third agent" is stated,
  without the "reviewer receives only the diff" detail from Sumner's own
  account), per-platform test counts, or any discussion of the 99.8%-vs-100%
  test-pass-rate discrepancy already flagged in the corpus (see Cross-References
  → Contradicts).

## Extracted Claims

### Claim 1: Anthropic's central thesis is that migration quality comes from fixing the process that generates code, not from fixing the code's output directly
- **Evidence**: Stated as the article's named "core insight," positioned
  immediately after the two case-study summaries and before the six-step
  process is introduced; reinforced later in the best-practices section
  ("Review loop results, not code").
- **Confidence**: emerging (a first-party methodological framing claim,
  asserted rather than benchmarked against an alternative "fix the code
  directly" approach, but consistent with and corroborated by independent
  practitioner accounts of the same underlying case study — see
  Cross-References → Corroborates)
- **Quote**: "The core insight is that you don’t fix the code. You fix the process (loop) that produced the code."
- **Our assessment**: This is the organizing principle for the entire post and
  is consistent with Sumner's own words in his primary source, already
  extracted verbatim in `blog-pragmaticengineer-bun-rust-rewrite.md` (Claim 9):
  when workflows failed, "I monitored workflows... and prompting Claude to
  edit the loop to fix things," not hand-fixing generated code. This source's
  contribution is generalizing that single practitioner's habit into a named,
  repeatable principle intended for any migration, not just Bun's.

### Claim 2: Jarred Sumner's Bun Zig-to-Rust migration produced roughly a million lines of code in under two weeks, with 100% of Bun's existing test suite passing in CI before merge, and 19 post-merge regressions that have since all been fixed
- **Evidence**: First-party summary attributed by name and title to Sumner
  ("co-founder of Bun and Member of Technical Staff at Anthropic"), with a
  specific timeline, test-pass figure, and regression count.
- **Confidence**: settled (this specific figure set — 100% test pass, 19
  regressions — is independently corroborated by Sumner's own primary-source
  post as extracted in `blog-pragmaticengineer-bun-rust-rewrite.md` Claims 8
  and 11)
- **Quote**: "A million lines of code were produced in less than two weeks,
  with 100% of Bun's existing test suite passing in CI before merge. Nineteen
  regressions surfaced after merge and have all been fixed. The Rust port was
  shipped inside Claude Code in June."
- **Our assessment**: This figure set matches Sumner's own account (100%
  test-pass, "0 tests skipped or deleted," 19 known regressions) rather than
  Anthropic's own earlier "99.8%" figure from
  `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 6) — see
  Cross-References → Contradicts. That an Anthropic-published source now
  restates Sumner's 100% figure, six weeks after Anthropic's own 99.8% claim,
  is itself evidence relevant to resolving issue #1759, though we do not pick
  a winner here per MINER.md §4a.

### Claim 3: Mike Krieger, co-lead of Anthropic Labs, migrated a Python codebase to 165,000 lines of TypeScript over a weekend, using hundreds of agents, eight phase gates, three adversarial review rounds, and a final parity check diffing every command's output against the Python original
- **Evidence**: First-party account naming a specific Anthropic executive, a
  specific line count, timeframe, and four distinct process mechanisms (agent
  count, phase gates, review rounds, parity-check method).
- **Confidence**: emerging (named, senior first-party practitioner; a
  previously undocumented case study in this corpus with no independent
  third-party corroboration yet — unlike the Bun case, no separate first-hand
  blog post from Krieger has been mined)
- **Quote**: "Mike Krieger, co-lead of Anthropic Labs, migrated a Python
  codebase to 165,000 lines of TypeScript over a weekend. This included
  hundreds of agents, eight phase gates, three adversarial review rounds, and
  a final parity check that diffed every command's output against the Python
  original."
- **Our assessment**: This is the single most novel contribution of this
  source to the corpus: a second, independent large-scale migration case
  study, run by a different named Anthropic practitioner using a different
  language pair (Python→TypeScript, a redesign-style port, vs. Bun's
  structure-preserving Zig→Rust port) and a different verification method
  (a hand-built parity harness of real-world scenarios rather than an
  inherited implementation-independent test suite). It provides a second data
  point that the "one engineer + AI agents can complete a large migration in
  a weekend/two-weeks" pattern is not unique to the Bun case.

### Claim 4: The Bun migration consumed 5.9 billion uncached input tokens and 690 million output tokens (~$165,000 at API pricing); the main portion of Krieger's port consumed 27 million tokens
- **Evidence**: First-party token/cost accounting for both case studies,
  stated together in the same paragraph as a cost-justification discussion.
- **Confidence**: settled (the Bun figure is independently corroborated,
  token-for-token, by Sumner's own primary-source accounting in
  `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 5: "5.9 billion uncached
  input tokens, 690 million output tokens, and 72 billion cached input token
  reads — around $165,000." The Krieger figure — 27 million tokens for "the
  main portion" — is new to the corpus and unverified by any second source.)
- **Quote**: "The Bun migration, for example, consumed 5.9 billion uncached
  input tokens and 690 million output tokens — around $165,000 at API
  pricing. The main portion of Mike’s port was 27 million tokens."
- **Our assessment**: The token-cost gap between the two case studies (5.9B+690M
  vs. 27M) is dramatic — roughly two orders of magnitude — and is explained by
  scale (a million-line structure-preserving port across 1,448 files vs. a
  165,000-line redesign-style port) rather than methodology. The qualifier
  "main portion" for Krieger's figure signals the 27M number is incomplete
  (it excludes some unspecified portion of the work), which the guide should
  preserve rather than treat as a total project cost.

### Claim 5: A prerequisite for any migration is a "judge" capable of evaluating original and target code on equal terms, built by categorizing existing tests into portable/non-portable, rewriting the portable ones as target-agnostic assertions, and validating the judge catches both correct code and deliberately broken code
- **Evidence**: A named three-step sub-process ("Categorize existing tests,"
  "Rewrite for portability," "Validate the judge") presented as the
  prerequisite stage before the six numbered steps begin.
- **Confidence**: emerging (a first-party prescriptive methodology, backed by
  two practitioners' actual practice — Sumner's inherited TypeScript
  conformance suite and Krieger's hand-built seven-scenario parity harness —
  but not independently tested by a third party against migrations that lack
  either option)
- **Quote**: "The judge must be able to evaluate both the original code and
  the target code on equal terms. Test suites written in the original
  language will often depend on internal functions that won't exist in the
  target code." / "Validate the judge. Run it against the original code to
  confirm it passes. Then run it against deliberately broken code to confirm
  it fails — a judge that doesn't catch breakage isn't a judge."
- **Our assessment**: The "validate against deliberately broken code" step is
  the most transferable, concrete piece of advice here: it is a check most
  practitioners building an ad hoc verification harness would skip, and it
  directly guards against the known agentic failure mode of a verification
  harness that always reports success. This generalizes and makes explicit
  what Willison's note (`blog-simonwillison-rewriting-bun-rust.md` Claim 2)
  named more abstractly as a "conformance suite" precondition — this source
  adds the missing step of testing the judge itself, not just confirming a
  conformance suite exists.

### Claim 6: The order of the first step's three artifacts matters — the rulebook must be created before the gap inventory, because the gap inventory is defined by what the rulebook's defaults don't cover, and the two are validated together in a joint audit
- **Evidence**: Explicit sequencing rule stated as a standalone sentence
  within Step 1's description.
- **Confidence**: emerging (a first-party procedural claim with an internal
  logical justification given, not independently tested against a migration
  that built the gap inventory first)
- **Quote**: "The order matters: the rulebook must come before the gap
  inventory. The gap inventory is defined by what the rulebook's defaults
  won't cover, and the two are tested together in a joint audit."
- **Our assessment**: This is a specific, checkable procedural claim absent
  from the corpus's existing Bun-focused notes, which document that "Jarred
  inventoried these gaps up front" but do not state this ordering rule as a
  general principle. Notably, the source itself immediately complicates the
  rule: "Mike chose to translate first and then create the gap inventory by
  auditing afterwards. You may need to do both" — so this is presented as a
  default sequencing preference, not an absolute rule, for redesign-style
  migrations.

### Claim 7: The stress-test step (a disposable mini-migration on a handful of files, comparing multiple translation approaches) caught two critical issues for Sumner that would otherwise have propagated across all 1,448 files in the full migration
- **Evidence**: A specific, named example: Sumner used one agent to translate
  three files via the rulebook, one agent to translate three files "like a
  senior Rust engineer," and one agent to diff the two and generate new rules
  — catching two critical issues before they could fan out.
- **Confidence**: settled (specific numeric outcome — "two critical issues,"
  "1,448 files" — attributed to a named practitioner's actual run, though
  self-reported)
- **Quote**: "In this step, Jarred used one agent to translate three files
  using the rulebook, one agent to translate three files “like a senior Rust
  engineer,” and one agent to use the diff to create new translation rules. At
  this stage he caught two critical issues that would have created numerous
  issues if fanned out across all 1,448 files." / "Regardless, throw out any
  translated files. The goal is to refine the rules, not make incremental
  progress."
- **Our assessment**: The instruction to discard the stress-test's translated
  output entirely — "throw out any translated files" — is a specific,
  actionable, and somewhat counterintuitive piece of guidance: practitioners
  under schedule pressure would be tempted to keep working code from the
  stress test rather than deleting it. The rationale (the goal is rule
  quality, not incremental progress) is a direct instance of Claim 1's "fix
  the process" thesis applied concretely.

### Claim 8: Step 3 ("translate everything") runs a mechanical, disk-state-based work queue — a batch script determines completion by checking whether the translated file exists on disk, making the migration resumable by construction because the queue rebuilds from disk every time
- **Evidence**: First-party description of the work-queue mechanism, stated as
  a specific implementation detail rather than a general principle, and
  repeated as a best practice ("Make the work queue mechanical and resumable.
  Done should mean 'the output file exists on disk.'")
- **Confidence**: emerging (a first-party architectural claim; plausible and
  internally consistent with the same source's Step 6 description of the
  "build daemon" that similarly serializes state via a queue, but not
  independently verified against a real failure/resume scenario in this
  source)
- **Quote**: "The work queue should be mechanical. A batch script decides
  what’s done by checking whether the translated file exists on disk, then
  slices the pending files into batches for the implementer agents. Because
  the queue is rebuilt from disk every time, the migration is resumable by
  construction."
- **Our assessment**: This directly extends the corpus's existing coverage of
  dynamic-workflows resumability (`blog-anthropic-dynamic-workflows-claude-code.md`
  Claim 7: "Progress in dynamic workflows saves automatically... no mechanism
  described in the announcement") by supplying the actual mechanism that
  Claim 7 noted was missing: resumability here is not a platform feature but
  a design choice — deriving "done" from filesystem state rather than from an
  in-memory or database-tracked job list. This is a reusable pattern
  independent of any specific Anthropic product feature.

### Claim 9: Two adversarial reviewers evaluate implementer output using separate contexts; disagreement between the two reviewers is escalated to a third agent, and a recurring mistake across files is fixed once in the rulebook rather than patched per-file
- **Evidence**: First-party description of the Step 3 review mechanism,
  including the escalation path for reviewer disagreement and the rule-vs-patch
  distinction for recurring errors.
- **Confidence**: emerging (first-party architectural description without a
  concrete worked example of the escalation path being triggered, unlike
  Sumner's own post which supplies three specific bugs the reviewers caught)
- **Quote**: "Two adversarial reviewers evaluate the work of the implementers
  using separate contexts and disagreement between reviewers goes to a third
  agent. When a reviewer keeps catching the same mistake across files, the fix
  isn't per-file. You add one sentence to the rulebook and regenerate the
  affected batch. The rulebook keeps growing through this step; the code
  never gets hand-patched against it."
- **Our assessment**: This adds a specific mechanism — third-agent escalation
  on reviewer disagreement — not present in `blog-pragmaticengineer-bun-rust-rewrite.md`
  Claim 7's more detailed "1 implementer, 2+ adversarial reviewers, 1 fixer"
  ratio, which describes reviewer isolation ("only the diff, told to assume
  it's wrong") but not what happens when two reviewers disagree with each
  other. Whether "goes to a third agent" describes Sumner's own harness or is
  a generalized recommendation distilled across both case studies is not
  stated; the source presents it as the generic Step 3 process for any
  migration.

### Claim 10: Where the compiler sits in the loop is a deliberate, migration-specific design choice — Mike ran the TypeScript compiler inside every implementation loop because it checks a unit in seconds, while Jarred excluded the Rust compiler from the loop entirely and deferred it to a separate step because `cargo` takes minutes
- **Evidence**: A direct contrast between the two named practitioners' choices
  for the same architectural decision, with the stated rationale (compile
  speed) for each.
- **Confidence**: settled (specific, named, and internally consistent
  practitioner-level design choice, framed as a deliberate tradeoff rather
  than a universal rule)
- **Quote**: "One important design decision to note in this step is where the
  compiler sits. Mike ran the TypeScript compiler inside every loop, because
  it checks a unit in seconds. Jarred banned the compiler from the loop
  entirely and deferred it to the next step, because cargo takes minutes."
- **Our assessment**: This is a concrete, generalizable engineering heuristic
  for anyone designing a similar loop: compiler feedback belongs inside the
  per-file implementation loop only if it is fast enough not to bottleneck
  parallel agents; if it is slow (minutes, as with `cargo` across a whole
  workspace), it belongs in a separate, later, batched step. This is a
  concrete elaboration of Claim 1's "fix the process" thesis: identical
  problem (validate a translation), opposite architectural answer, driven
  entirely by one measurable variable (compiler latency).

### Claim 11: The best-practices list explicitly warns against using the largest model for every step — smaller models should handle high-volume implementation fan-out, with the largest model reserved for reviewers and for anything that writes rules other agents will follow
- **Evidence**: A named best practice, generalized from the observation that
  "Mike used Claude Sonnet when he fanned out 12 subagents for the main
  migration" (Step 3) and that "both Mike and Jarred used Fable for key
  steps... particularly in an advisory pattern that used multiple model
  classes to optimize token consumption."
- **Confidence**: emerging (a first-party prescriptive recommendation
  supported by two named practitioners' actual model choices, but without a
  controlled comparison against an all-largest-model baseline)
- **Quote**: "Don't use the largest model for everything. Token spend
  concentrates in your loops, so design them deliberately. Smaller models
  handle the high-volume implementation fan-out well; save your largest model
  for reviewers and for anything that writes rules other agents will follow."
- **Our assessment**: This is a specific, actionable token-economics rule
  that ties model tier directly to a role in the harness (implementer vs.
  reviewer vs. rule-author) rather than to task difficulty in the abstract.
  It corroborates the general "use smaller/cheaper models for
  high-volume/low-judgment work, larger models for judgment-heavy work"
  pattern already established elsewhere in the corpus's harness-engineering
  coverage, with a specific migration-context instance: 12 Sonnet subagents
  for Krieger's implementation fan-out.

### Claim 12: The Rust-ported Bun delivered measured production improvements — one benchmark's memory footprint dropped from 6,745 MB to 609 MB, the binary is 19% smaller on Linux and Windows, and HTTP serving/build-task performance improved 2-5%, while about 4% of the Rust code sits inside "unsafe" blocks (mostly single-line pointer operations at C/C++ boundaries)
- **Evidence**: First-party outcome metrics, presented in the post's closing
  "Review loop results, not code" section, alongside an explicit
  acknowledgment of the tradeoff (unsafe-block percentage).
- **Confidence**: settled (specific benchmark figures corroborated in
  substance, though not identical in framing, by
  `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 10, which reports the
  same memory-leak benchmark as "1,914–6,745 MB in v1.3.14" dropping to
  "~526–609 MB" in v1.4.0, and Claim 6's "~13,000 unsafe keywords... ~4% of
  code in an unsafe block; 78% of those blocks are a single line")
- **Quote**: "But the new codebase is measurably better. Every memory leak the
  team's tooling can detect has been fixed: one benchmark of 2,000 repeated
  builds dropped from 6,745 MB of memory to 609. The binary is 19% smaller on
  Linux and Windows. And cross-language optimization made it 2–5% faster
  across HTTP serving and real-world workloads like next build and tsc." /
  "For example, about 4% of the Rust code sits inside \"unsafe\" blocks,
  mostly single-line pointer operations at C/C++ boundaries."
- **Our assessment**: This closely matches (down to the same 6,745 MB and ~4%
  unsafe-block figures) the independently-mined `blog-pragmaticengineer-bun-rust-rewrite.md`
  account of the same benchmark, which strengthens confidence in both sources
  for this specific set of numbers — a rare case in this corpus of two
  distinct first-party/practitioner accounts converging on identical
  benchmark figures for the same event.

## Concrete Artifacts

### Gap-inventory code examples (verbatim from source, both language pairs)

```
Source: https://claude.com/blog/ai-code-migration — "Gap inventory and skeptic reviewers"

Zig (manual memory management gap):
fn readConfig(allocator: std.mem.Allocator) ![]u8 {
  const buf = try allocator.alloc(u8, 1024);
  // ...fill buf...
  return buf; // caller must free this — but only the comment says so
}
// A caller that forgets 'defer allocator.free(buf)' still compiles — the leak only surfaces at runtime.

Rust (equivalent, ownership-checked):
fn read_config() -> Vec<u8> {
  let buf = vec![0u8; 1024];
  // ...fill buf...
  buf // ownership moves to the caller; memory is freed automatically
}
// Use it after it's moved? Free it twice? Neither compiles.
// Forget to free it? There's no free call to forget — drop is automatic.

Python (missing-contract gap):
def register(handler):
  handler.setup()
  return handler.run({"retries": 3})
# Any object with .setup() and .run() works here. Which objects actually get passed in? Read the whole codebase to find out.

TypeScript (equivalent, contract-checked):
interface RunResult { ok: boolean }
interface Handler {
  setup(): void;
  run(opts: { retries: number }): Promise<RunResult>;
}
function register(handler: Handler): Promise<RunResult> {
  handler.setup();
  return handler.run({ retries: 3 });
}
// The contract must be written down before this compiles
```

### Six-step process (as named and ordered in source)

```
Source: https://claude.com/blog/ai-code-migration

Prerequisites: build and validate a "judge" (categorize tests → rewrite for
  portability → validate against both working and deliberately broken code)

Step 1 — Create the rulebook, dependency map, and gap inventory
  (rulebook before gap inventory; the two are tested together in a joint audit)
Step 2 — Stress-test the rules
  (disposable mini-migration; discard the translated output; refine rules, not progress)
Step 3 — Translate everything
  (implement → review → fix loop; mechanical disk-state work queue; smaller
  models implement, larger models review; unresolved cases flagged
  "// TODO(port): <reason>")
Steps 4, 5, 6 — Compile, run, and match behavior
  (the source covers these three under a single combined header, not as three
  separately-ordered steps; its stated rationale, quoted verbatim: "These
  three steps share the same loop architecture and need progressively less
  human judgment, so we cover them together." The source also notes step 4 may
  "often dissolve into step 3 depending on the language and size of the
  migration.")
  - Compile (agents may not run this at all depending on size/difficulty;
    Jarred used an orchestrator script invoking the compiler once across the
    whole workspace, with "fixer agents" burning down the error list in
    parallel with adversarial review)
  - Run (smoke tests)
  - Match behavior (full test suite / parity check; "build daemon" serializes
    rebuilds so only one process ever triggers a rebuild)
```

### Why AI changes migration economics (five properties, verbatim bullet list)

```
Source: https://claude.com/blog/ai-code-migration — "Why AI changes the code migration math"

- The work is parallel. Work can be executed across thousands of independent
  units such as files and crates, so agents can work at the same time rather
  than have one waiting on the other.
- Context is clear and comprehensive. The old code serves as a great spec for
  the model. It also serves as a core reference to help build the guide for
  translation agents to follow.
- There is a built-in referee. Many large codebases will include a test suite
  that agents can use to verify their work. Agents perform their best when
  verification is objective, because the model can grind against a ground
  truth for days without a human arbitrating quality.
- The queue writes itself. When a compiler or test run fails, that becomes
  the next item for an agent to fix.
- They require consistency and edge case handling: The process is built so
  drift has nowhere to hide: reviewers cite the rule behind every finding, so
  a violation becomes a queue item instead of a quiet divergence. And when an
  agent does hit an edge case, the fix becomes a rule every subsequent agent
  follows.
```

### Best practices (verbatim bullet list)

```
Source: https://claude.com/blog/ai-code-migration — "Code migrations best practices"

- Don't follow this guide blindly. Each migration is different. Treat this
  as a starting point, and plan your specific migration with Claude before
  committing to it.
- Don’t focus on individual failures. Individual failures are the loop's job.
  Fixer agents burn those down. Your attention belongs on the patterns.
- Make review adversarial and verification mechanical. Adversarial review
  allows for longer running tasks and is often worth the token consumption.
  Let scripts — a compiler, a diff, a test suite — be the referee.
- Don't use the largest model for everything. Token spend concentrates in
  your loops, so design them deliberately. Smaller models handle the
  high-volume implementation fan-out well; save your largest model for
  reviewers and for anything that writes rules other agents will follow.
- Front-load the human hours. The rulebook and the stress test are the most
  time-consuming. Everything after is mostly queues burning down.
- Make the work queue mechanical and resumable. Done should mean "the output
  file exists on disk."
```

### Krieger's compile-step business case (verbatim)

```
Source: https://claude.com/blog/ai-code-migration

"The compile step was the impetus for Mike's project. The internal tool his
team works on ships to users as a single binary. Producing that binary with
the Python toolchain took roughly eight minutes per platform, totaling a
30-minute wait across the build matrix on every release. After the port, the
same compile now takes about two seconds, the binary starts 6x faster, and
the team was able to retire a separate deployment pipeline."
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 5 ($165,000 total cost;
    5.9B uncached input tokens, 690M output tokens) — this source's Claim 4
    restates the identical Bun cost figures, with no numeric discrepancy, six
    weeks after Sumner's own primary-source post was mined.
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 8 (Sumner's own
    100%-passing, "0 tests skipped or deleted" merge criterion) — this
    source's Claim 2 restates "100% of Bun's existing test suite passing in
    CI before merge," matching Sumner's figure rather than Anthropic's own
    earlier 99.8% figure (see **Contradicts** below).
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 11 (19 known
    regressions, dominant root cause "syntactically identical... semantically
    different") — this source's Claim 2 restates the same "19 regressions...
    have all been fixed" figure.
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 10 (memory benchmark
    6,745 MB dropping to ~609 MB; binary ~20% smaller on Linux/Windows;
    ~4% of code in unsafe blocks) — this source's Claim 12 restates the same
    figures (6,745 MB, 609 MB, 19% smaller, ~4% unsafe) from the same
    underlying benchmark, now with the specific "2,000 repeated builds"
    methodology detail matching that note's "bundling the same 60-module
    project 2,000 times" description.
  - `blog-simonwillison-rewriting-bun-rust.md` Claim 3 (Sumner's own compact
    methodology quote: "a language-independent test suite with a million
    assertions, adversarial code review and when something does go wrong,
    fixing the process that generates the code instead of hand-fixing the
    code") — this source's Claim 1 ("you don't fix the code, you fix the
    process") is Anthropic's own generalized restatement of the identical
    principle Sumner stated in his own primary source.
  - `blog-addyosmani-loop-engineering.md` Claim 1 ("Loop engineering is
    replacing yourself as the person who prompts the agent. You design the
    system that does it instead.") — this source's central thesis (Claim 1,
    "you fix the process (loop) that produced the code") is a direct
    domain-specific instance of the same "loop engineering" framing, applied
    specifically to migrations, independently arrived at in a first-party
    Anthropic post rather than Osmani's practitioner-synthesis piece.
  - `blog-anthropic-dynamic-workflows-claude-code.md` Claim 3 (verification-
    before-return: "checking its work before anything reaches you") and
    Claim 2 (Claude "dynamically writes orchestration scripts") — this
    source's Step 3 implement/review/fix loop and Step 6 build-daemon
    describe concrete mechanisms consistent with that announcement's
    higher-level architectural claims, though this source never names
    "dynamic workflows" explicitly as the underlying feature for either case
    study (see Extraction Notes).

- **Contradicts**: `blog-anthropic-dynamic-workflows-claude-code.md` Claim 6
  states the Bun rewrite reached "99.8% of the existing test suite passing."
  This source's Claim 2 states "100% of Bun's existing test suite passing in
  CI before merge," matching Sumner's own primary-source figure rather than
  Anthropic's earlier announcement. **This is the same contradiction already
  filed as GitHub issue #1759** ("Bun Zig→Rust rewrite: test pass rate at
  merge — 99.8% vs. 100%," open, `needs-resolution`) — per MINER.md §4a
  ("check open contradiction-labeled issues... before filing"), no new issue
  is filed here. This source is additional evidence relevant to that issue's
  resolution: it is now the *second* first-party Anthropic publication to
  state the Bun figure, and the second one uses 100%, not 99.8% — worth
  noting for whoever resolves #1759, though we do not pick a winner in this
  note.

- **Extends**:
  - `blog-google-io-2026-developer-keynote.md` Claim 7 (Google's Migration
    Agent preview: "migrates your app code to a native Kotlin Android app,
    regardless of whether your source is React Native, a web framework, or
    iOS") — both sources address AI-driven code migration as a major 2026
    product/methodology theme, but represent opposite approaches: Google's
    Migration Agent is a packaged, single-button product feature; this
    source's methodology is an explicit, human-designed six-step process
    requiring a human to build a rulebook, dependency map, and gap inventory
    before any agent translation begins. The guide should treat these as two
    different points on a spectrum (turnkey product vs. supervised process)
    rather than directly comparable capabilities, since neither source
    benchmarks the other.
  - `blog-cursor-nab-legacy-migration.md` Claim 6 (NAB's Assembly mainframe
    migration, quoting Harjot Singh: "Before Cursor, we couldn't even think
    about moving away from Assembly. We just didn't have the expertise or
    time to tackle an enormous project like this manually.") — that note
    documents AI unblocking a migration that was categorically impossible
    due to expertise scarcity;
    this source's two case studies (Bun, Krieger's port) are migrations that
    were technically possible but previously too slow/expensive/risky to
    justify — a distinct "was blocked by cost/risk, not by expertise" framing
    that this source makes explicit in its own "why and when to migrate"
    section ("Migrating languages can deliver smaller, faster, and safer
    systems, but no one wants to pay for them").
  - `blog-anthropic-dynamic-workflows-claude-code.md` Claim 7 (dynamic
    workflows "progress... saves automatically... no mechanism described")
    — this source's Claim 8 supplies the actual mechanism this earlier
    note's Extraction Notes flagged as missing: resumability derived from
    checking whether a translated file exists on disk, not from any
    described platform-level checkpointing feature.

- **Novel**:
  - **Mike Krieger's Python-to-TypeScript migration case study**: a
    previously undocumented second large-scale migration in the corpus, run
    by a different named Anthropic executive, with different scale (165,000
    lines vs. Bun's ~1M), timeframe (a weekend vs. 11 days), and
    verification method (a hand-built seven-scenario parity harness vs. an
    inherited implementation-independent test suite).
  - **The generalized six-step process itself**, with the prerequisite
    "judge" construction sub-process (categorize → rewrite for portability →
    validate against broken code) and the "rulebook before gap inventory"
    ordering rule — no prior corpus source presents a named, numbered,
    reusable migration methodology; prior sources (the two Bun-focused notes)
    document one specific project's mechanics without generalizing them into
    a process other practitioners could follow step-by-step for a different
    migration.
  - **The compiler-placement design tradeoff** (compiler inside the loop if
    fast, deferred to a separate step if slow) as an explicit, named,
    contrasted decision between the two case studies.
  - **The disk-state-based mechanical work queue** as the specific mechanism
    underlying migration resumability — a concrete answer to a gap
    (`blog-anthropic-dynamic-workflows-claude-code.md` Claim 7) previously
    flagged as undocumented in the corpus.
  - **A specific token multiplier for a second, much smaller migration** (27M
    tokens for "the main portion" of Krieger's 165,000-line port) — the first
    corpus data point for token cost of a *smaller*-scale agentic migration,
    letting the guide contrast against Bun's 5.9B+690M-token, ~$165K figure.

## Guide Impact

- **Chapter 05 (Large-Scale Refactoring and Migrations)**: This source
  provides the strongest candidate for a named, reusable migration process in
  the guide — the six-step framework (rulebook/dependency-map/gap-inventory →
  stress-test → translate → compile → run → match-behavior), with the
  prerequisite "judge" construction as an explicit pre-Step-1 stage. Add the
  "rulebook before gap inventory" ordering rule and the "validate the judge
  against deliberately broken code" step as specific, checkable guidance
  items — both are concrete enough for a checklist, and neither is documented
  in the existing Bun-only corpus notes. Add Krieger's Python-to-TypeScript
  case study as a second worked example alongside Bun, specifically to
  illustrate the "redesign" migration type (vs. Bun's "structure-preserving"
  type) and its different judge-construction approach (hand-built parity
  harness vs. inherited conformance suite). Add the compiler-placement
  tradeoff (in-loop if fast, deferred if slow) as a specific harness-design
  decision point.
- **Chapter 02 (Harness Engineering)**: Add the disk-state-based mechanical
  work queue ("done" = file exists on disk, queue rebuilt from disk every
  time) as a concrete, reusable resumability pattern, and the "reviewer
  disagreement escalates to a third agent" mechanism as a refinement of the
  adversarial-review pattern already sourced from
  `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7. Add the model-tier
  rule (smaller models for high-volume implementation fan-out, largest model
  reserved for reviewers and rule-authors) as a specific token-economics
  heuristic, with the two case studies' concrete instances (12 Sonnet
  subagents for Krieger's implementation fan-out) as illustration.
- **Chapter 01 (Daily Workflows)**: The "worst case scenario is you delete
  the branch and try again" framing (from the "why and when to migrate"
  section) is a useful, quotable reduction of migration risk that the guide
  could use to explain why AI-driven migrations lower the career/organizational
  risk bar for attempting them, complementing the existing NAB case study's
  "categorically impossible" framing.

## Extraction Notes

- The WebFetch tool's summarized output (used for an initial pass) both
  omitted material present in the raw page and, on a follow-up "verbatim
  quotes" request, produced text that closely matched but was not confirmed
  identical to the live page. To satisfy MINER.md §2a's verbatim-quote
  requirement, the full page was re-fetched directly via `curl`, HTML tags
  were stripped programmatically, and every quote in this note was copied
  from that raw-text extraction, not from either WebFetch summary. The raw
  extraction captured the complete article body (from the headline through
  the "Related" section) plus substantial site-navigation boilerplate, which
  was excluded from this note.
- No sub-pages were followed. The article's "Related" section links to a
  "Migration starter kit," a "Code-modernization plugin," and "Dynamic
  workflows in Claude Code" — the last of these is already deeply mined as
  `blog-anthropic-dynamic-workflows-claude-code.md` (issue #988); the other
  two (starter kit, code-modernization plugin) were not followed because they
  are product/tooling pages rather than additional narrative or claims, and
  the article explicitly caveats the starter kit twice as "a generalized
  template of the process... it's not what these specific ports ran on" —
  i.e., the article itself flags that following that link would not yield
  additional facts about the two case studies covered here.
- This source never explicitly names "dynamic workflows" as the underlying
  Claude Code feature for either the Bun or Krieger case study, despite both
  being consistent with that feature's architecture (per Cross-References
  above) and despite Sumner's own separate post explicitly crediting "Claude
  Code's dynamic workflows" (per `blog-pragmaticengineer-bun-rust-rewrite.md`
  Claim 6). This is a notable omission worth flagging: readers of this post
  alone would not learn which specific Claude Code capability powered either
  migration.
- The source names Mike Krieger only as "co-lead of Anthropic Labs." His
  additional, more widely known role (Instagram co-founder; Anthropic's Chief
  Product Officer) is not stated in this source and is not included in any
  quote above — the "co-lead of Anthropic Labs" title is used verbatim
  per MINER.md §2a, and the additional biographical context noted in Source
  Context above is this note's own annotation, not a quote from the source.
