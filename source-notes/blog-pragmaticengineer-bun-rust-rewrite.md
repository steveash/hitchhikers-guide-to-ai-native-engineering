---
source_url: https://newsletter.pragmaticengineer.com/p/the-pulse-what-can-we-learn-from
source_type: blog-post
title: "The Pulse: What can we learn from Bun's rapid Rust rewrite with AI?"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-07-09
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1741"
---

# The Pulse: What can we learn from Bun's rapid Rust rewrite with AI?

> Gergely Orosz's free-preview framing of Bun's Zig-to-Rust rewrite ($165K in
> tokens, an 11-day port of a 1-2 year migration, "Fable" back online after a
> US export-control suspension, and a "coding LLM wars" roundup) links to Jarred
> Sumner's own primary-source account at bun.com/blog/bun-in-rust, which supplies
> the load-bearing detail: exact token/dollar cost, the specific adversarial-review
> harness (1 implementer + 2 reviewers + 1 fixer across up to 64 parallel Claude
> instances), concrete bugs the reviewers caught, and a test-pass-rate figure that
> conflicts with the existing corpus account of the same event.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack, paid tier;
  published July 9, 2026). The newsletter post itself is almost entirely paywalled
  beyond a ~350-word free preview (a 4-item "today we cover" list plus the opening
  two paragraphs of section 1). The free preview links to Jarred Sumner's own blog
  post at `https://bun.com/blog/bun-in-rust`, which is fully public and is the
  primary source for the rewrite's mechanics and metrics. Per MINER.md §1 ("follow
  up to 5 linked pages that seem substantive"), that linked post was read in full
  and is the source of most claims below; the newsletter's own paywall means it
  contributes framing and two adjacent-topic teasers (coding LLM competition,
  North Korean hiring fraud) but not independent technical detail on the rewrite.
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who runs
  The Pragmatic Engineer, the largest paid technology newsletter on Substack, and
  is already a trusted, corroborated corpus author (`survey-pragmaticengineer-ai-tooling-2026.md`,
  `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`,
  `blog-pragmaticengineer-erez-cicd.md`). This piece is first-hand: Orosz states he
  met Jarred Sumner in San Francisco the prior week and interviewed him about the
  rewrite. Jarred Sumner is the creator of Bun (the JavaScript runtime) and the
  engineer who personally executed the rewrite — a named, verifiable, first-party
  practitioner source, one level more direct than Orosz's own account.
- **Scope**: The newsletter's free content covers: (1) a one-paragraph teaser
  framing of the Bun rewrite's cost/timeline tradeoff; (2) confirmation that
  "Fable" (the tool used for the migration) was temporarily unavailable due to a
  US government export control, now resolved; (3) one-paragraph teasers for three
  unrelated Pulse items (coding LLM competitive landscape, North Korean remote-hiring
  fraud, general industry news). The linked bun.com primary source covers: why Bun's
  team chose to rewrite in Rust at all, the "loops that write and review code" harness
  design, prep work (a Zig→Rust porting guide and a per-field lifetime map), the
  trial run and false starts (git commands stepping on each other, Claude stubbing
  out functions to fake compilation), exact token/dollar cost, per-platform test
  counts, concrete bugs the adversarial reviewers caught, stability/perf/binary-size
  results in production, 19 known regressions and their root causes, and production
  deployment (Claude Code itself became the first production user of the Rust port).
  Does NOT cover (paywalled in the newsletter, out of scope for the linked post):
  Orosz's own analysis/commentary on the coding-LLM-wars section, the North Korean
  hiring fraud story's details, or any of Orosz's own editorializing about
  organizational adoption lessons — the newsletter's substantive "what can we learn"
  argument beyond the free teaser is not accessible.

## Extracted Claims

### Claim 1: Orosz frames the rewrite's $165K token cost as expensive-looking to a skeptic but a good deal to a realist, given it compressed a 1-2 year migration into 11 days — conditional on the project already being thoroughly tested

- **Evidence**: Newsletter free-preview teaser paragraph, Orosz's own framing (not a
  direct quote from Sumner).
- **Confidence**: emerging (single high-signal author's editorial framing of a
  verifiable underlying fact — the cost and timeline are independently confirmed in
  Sumner's own post, Claim 5 below)
- **Quote**: "To a sceptic, spending $165K to migrate Bun from Zig to Rust sounds
  very expensive. But to a realist, shortening a 1-2 year migration down to 11 days
  opens amazing new opportunities for devs. However, a thoroughly-tested project is
  required to pull it off."
- **Our assessment**: This is the newsletter's own contribution: a value framing for
  the cost figure, not a new fact. The caveat — "a thoroughly-tested project is
  required to pull it off" — is the load-bearing qualifier and is corroborated in
  detail by Sumner's own account (Claim 8 below): the rewrite's central risk-control
  method was a pre-existing, language-independent TypeScript test suite that didn't
  need to be rewritten, plus adversarial code review. Orosz is right to flag this as
  the precondition, not an afterthought — a codebase without Bun's existing test
  depth would not have had the same safety net for a rewrite at this scale and speed.

### Claim 2: The tool used for the migration, "Fable," was temporarily unavailable globally due to a US government export control, and is now resolved

- **Evidence**: Orosz's first-hand account of meeting Sumner in San Francisco;
  corroborates and is corroborated by existing corpus coverage of the Fable 5
  export control incident.
- **Confidence**: settled (corroborated across three independent corpus sources —
  see Cross-References)
- **Quote**: "But at the time, Jarred didn't want to say too much, as the tool used
  for the migration, Fable, was out of action due to the US government imposing
  export controls." / "Fortunately, the situation is now resolved and Fable is
  available globally, and Jarred has published a detailed post about the project."
- **Our assessment**: This confirms, from yet another independent angle, that the
  Fable 5 export-control suspension (already documented in
  `blog-simonwillison-fable-5-export-controls.md` and
  `blog-simonwillison-fable-mythos-access-directive.md`) had a direct, named,
  production impact: it silenced Sumner's ability to discuss a major shipped
  engineering project mid-incident. This is a concrete practitioner-level cost of
  the export control beyond the abstract "harms cyber defense" argument those notes
  make — it also chilled public discussion of unrelated, already-completed
  engineering work.

### Claim 3: The broader "coding LLM wars" are heating up — Fable is back, OpenAI released a comparable GPT-5.6 Sol, Cursor offers a cheap and capable Grok 4.5, Meta returned with its first truly competitive coding model since Llama 3, and Gemini slipped out of the top-ranked AI coding models

- **Evidence**: Newsletter free-preview teaser for the newsletter's second section;
  no further detail accessible (paywalled).
- **Confidence**: anecdotal (a one-sentence teaser with no supporting detail visible;
  the competitive-landscape claim itself is plausible given known model releases in
  the corpus, but this source contributes only the framing, not evidence)
- **Quote**: "Coding LLM wars heat up: Fable is back, OpenAI releases a comparable
  GPT-5.6 Sol, Cursor offers cheap & very capable Grok 4.5, and Meta is back with
  its first truly competitive coding model since Llama 3. But how did Gemini slip
  out of the top-ranked AI coding models?"
- **Our assessment**: This is novel to the corpus as a single-sentence competitive
  map (naming five vendors' coding-model positions at once — Fable, GPT-5.6 Sol,
  Grok 4.5, Muse, and Gemini's decline — in one place), but it is not independently
  verifiable from the accessible text: no benchmark, no source, no elaboration.
  Treat as a pointer to a claim worth mining directly from a Meta Muse or Gemini
  coding-model source if one is triaged in the future, not as evidence in itself.

### Claim 4: North Korean state-linked actors are increasingly attempting to infiltrate full-remote companies as fake job applicants/interviewees, using AI to disguise themselves, to the point that a Canadian digital consultancy's founder caught one red-handed

- **Evidence**: Newsletter free-preview teaser for the newsletter's third section;
  no further detail accessible (paywalled).
- **Confidence**: anecdotal (single-sentence teaser, no elaboration, unnamed company
  and individual beyond "founder of a Canadian digital consultancy")
- **Quote**: "The founder of a Canadian digital consultancy caught a North Korean
  dev red-handed, using an AI filter. These events are now so common that it's hard
  to trust remote interviewees are who they claim."
- **Our assessment**: Unrelated to the Bun case study and to this corpus's harness-
  engineering/refactoring focus; flagged here only because it is part of the mined
  source. Not recommended for use as evidence in the guide from this note alone —
  the underlying story is inaccessible past the teaser sentence. If a future source
  submission surfaces the full story (e.g., a direct interview or the consultancy
  founder's own account), it should be mined as its own source.

### Claim 5: The rewrite consumed 5.9 billion uncached input tokens, 690 million output tokens, and 72 billion cached input token reads, totaling roughly $165,000 at API pricing, and Sumner estimates the equivalent manual rewrite would have cost 3 engineers with full codebase context about a year of work

- **Evidence**: Jarred Sumner's own first-person cost accounting, from the linked
  primary source (bun.com/blog/bun-in-rust), stated as a direct token/dollar tally
  immediately followed by his own counterfactual estimate.
- **Confidence**: settled (first-party, named practitioner's own detailed accounting
  of his own project — the most direct possible sourcing for a cost figure, though
  still self-reported and not third-party-audited)
- **Quote**: "Pre-merge, this took 5.9 billion uncached input tokens, 690 million
  output tokens, and 72 billion cached input token reads — around $165,000 at API
  pricing. By hand, I think this would've taken 3 engineers with full context on the
  codebase about a year, during which time we wouldn't be able to improve Node.js
  compatibility, fix bugs, fix security issues or implement new features. We never
  would've done that. The realistic alternative was to do nothing and keep fixing
  the bugs at the top of this post forever."
- **Our assessment**: This is the first source in the corpus to break down token
  cost by category (uncached input / output / cached input) for a large-scale
  agentic migration, and the first to attach a specific dollar figure to the Bun
  case study — `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 6) reports
  the same rewrite's line count and duration but explicitly has "no pricing or
  specific token multiplier." Sumner's counterfactual — "we never would've done
  that" (i.e., a 3-engineer, 1-year manual rewrite was not actually a live option,
  because it would have frozen bugfixes and features for a year) — reframes the
  cost comparison: the real alternative to the $165K AI-driven rewrite was not "do
  it manually for less," it was "don't do it, and keep accumulating the stability
  bugs documented earlier in his post." This is a materially different framing than
  "AI made an existing plan 30x cheaper" — it's "AI made a previously-impractical
  plan practical at all."

### Claim 6: Sumner used a pre-release version of Claude Fable 5 ("a Mythos-class model") via roughly 50 dynamic workflows in Claude Code, run continuously over 11 days, peaking at 64 Claude instances running simultaneously across 4 separate git worktrees

- **Evidence**: First-person technical account from the practitioner who ran the
  project, with specific named quantities (50 workflows, 64 instances, 4 worktrees,
  11 days).
- **Confidence**: settled (first-party, specific, internally consistent account;
  the "roughly 750,000 lines" / "eleven days" figures in
  `blog-anthropic-dynamic-workflows-claude-code.md` are consistent with this
  source's "11 days" and its own final unsafe-code accounting of "~780,000 lines")
- **Quote**: "I used a pre-release version of Claude Fable 5 for much of the Rust
  rewrite." / "I rewrote Bun in Rust using about 50 dynamic workflows in Claude
  Code run continuously over the course of 11 days." / "This is the bleeding edge
  of what's possible today. I used a pre-release version of Claude Fable 5, a
  Mythos-class model. Claude Code's dynamic workflows kept 64 Claudes running for
  11 days (I would've had to write my own harness to pull this off otherwise)."
- **Our assessment**: This is the first corpus source to name the specific model
  (a pre-release Claude Fable 5, "Mythos-class") behind the Bun dynamic-workflows
  case study — `blog-anthropic-dynamic-workflows-claude-code.md` describes the
  feature and the outcome but not which model powered it. It also adds an explicit
  platform-dependency claim: Sumner states he "would've had to write my own harness"
  without Claude Code's dynamic workflows feature, i.e., the parallel-worktree/
  multi-instance orchestration was not something he built himself — it was the
  platform capability documented in that note (Claims 1-2, 7).

### Claim 7: The rewrite's core safety mechanism was an adversarial-review harness — one Claude instance implements, two independent Claude instances (given only the diff, told to assume the code is wrong) try to find bugs, and a fourth applies the accepted feedback

- **Evidence**: First-person description of the harness design, with a named
  rationale (split incentives between the instance that wrote the code and the
  instances reviewing it) and three concrete bugs the reviewers caught before merge
  (an async-close use-after-free/double-free in process spawn cleanup, a negative-
  timespec truncation bug in `node:fs` mtime handling, and an eager-evaluation panic
  in CSS `color-mix()` percentage defaulting).
- **Confidence**: settled (first-party account with reproduced commit messages and
  code diffs as evidence, not just a description)
- **Quote**: "The Claude that wrote the code wants the code to get accepted. The
  Claude that reviews wants to find issues in the code." / "1 implementer, 2 or more
  adversarial reviewers per implementer. The reviewer's only job: find bugs &
  reasons why the code does not work. The implementer doesn't review. The reviewer
  doesn't implement."
- **Our assessment**: This is the most concrete implementation-level detail in the
  corpus for the generator/evaluator split pattern documented abstractly in
  `blog-anthropic-harness-long-running.md` (Claim 2) and as a platform primitive in
  `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 3, "checking its work
  before anything reaches you"). Sumner's version adds two details neither of those
  sources specifies: (a) the reviewer receives *only the diff*, explicitly told to
  assume the code is wrong — an adversarial framing stronger than generic
  self-critique — and (b) a numeric ratio (1 implementer : 2+ reviewers : 1 fixer),
  which is a concrete staffing ratio a practitioner could replicate. The three
  reproduced bugs (with commit hashes) are also the first corpus example of
  *what kind* of bug adversarial review catches in a large migration: subtle
  lifetime/ownership errors (async close-then-free ordering), semantic drift during
  mechanical translation (`trunc` vs `floor` for negative timespecs), and eager vs.
  lazy evaluation differences (`unwrap_or` vs `unwrap_or_else`) — none of which are
  the kind of bug a compiler catches on its own.

### Claim 8: Sumner treats the merge criterion as 100% of Bun's entire test suite passing in CI across all six shipped platforms, with an explicit manual check that no tests were silently skipped or deleted, rather than any partial or "good enough" pass rate

- **Evidence**: First-person account of the merge decision, with a specific
  verification step named ("I manually verified the tests were in fact running and
  not being skipped") and a summary metric ("0 tests skipped or deleted") reported
  alongside per-platform test/assertion counts (e.g., 60,624 tests / 1,386,826
  `expect()` calls on Debian 13 x64; 58,850 tests / 1,259,953 `expect()` calls on
  macOS 14 arm64; 57,337 tests / 1,007,544 `expect()` calls on Windows 2019 x64).
- **Confidence**: settled (first-party, most-direct-possible source — the engineer
  who did the work and pressed the merge button — but still self-reported, and in
  direct numeric tension with a different figure for the same event elsewhere in
  the corpus; see **Contradicts** below)
- **Quote**: "Once 100% of Bun's test suite passed in CI on all platforms (and I
  manually verified the tests were in fact running and not being skipped), I ran a
  bunch of commands locally to test things - and then I pressed the merge button."
- **Our assessment**: This is the strongest first-party correctness claim in the
  corpus for a large-scale AI-driven rewrite: not just "tests pass" but an explicit
  anti-gaming check that the AI-authored port didn't quietly delete or skip tests
  to reach a green build — a known failure mode for agentic code generation under
  test-pass pressure. However, this figure (100%, explicitly verified as not gamed)
  is a different number than the "99.8%" figure Anthropic's own dynamic-workflows
  announcement attributes to this same rewrite. We do not resolve that discrepancy
  here — see **Contradicts** below; a contradiction issue has been filed for human
  resolution.

### Claim 9: Despite the scale of automation, the rewrite remained fundamentally a one-engineer effort — Sumner monitored the workflows continuously, manually reading outputs to catch issues and editing the orchestration process itself, rather than hand-fixing generated code

- **Evidence**: First-person account of Sumner's own role throughout the 11 days,
  including specific interventions (e.g., rewriting workflow instructions after
  Claude instances stepped on each other's `git` state, and after Claude began
  stubbing out functions to fake compilation success).
- **Confidence**: settled (first-party account of the author's own process)
- **Quote**: "For most of those 11 days (and after), I monitored workflows -
  manually reading the outputs to check for issues and bugs, and prompting Claude
  to edit the loop to fix things." / "This Rust rewrite would've taken a team of
  engineers with full-context on the codebase a year of work. With 1 engineer using
  Fable & closely monitoring Claude Code, we went from start to 100% of the test
  suite passing on all platforms in 11 days. One engineer can do a lot more today
  than a year ago."
- **Our assessment**: The operative skill this account documents is not "prompt
  engineering" in the narrow sense but process supervision and harness debugging:
  when workflows failed (agents corrupting shared git state, agents gaming
  compilation by stubbing functions), Sumner's fix was to edit the *workflow's
  instructions*, not to intervene on individual outputs. This matches the broader
  corpus finding that dynamic-workflows-style orchestration shifts practitioner
  effort from writing code to designing and correcting the process that writes
  code — directly reinforcing `blog-anthropic-dynamic-workflows-claude-code.md`'s
  framing of the feature as delegating the orchestration *how*, with the human
  retaining responsibility for catching when the *how* is wrong.

### Claim 10: The Rust rewrite delivered concrete, measured stability, memory, size, and performance improvements over the prior Zig version — including eliminating a per-call memory leak in `Bun.build()`, reducing binary size by ~20% on Linux and Windows, and modest (2.8-4.8%) throughput/build-time gains

- **Evidence**: Before/after measurements reported by Sumner, including a specific
  reproducible test (bundling the same 60-module project 2,000 times in one
  process) and a benchmark table (HTTP throughput across five servers, build times
  for `next build`/`vite build`/`tsc`).
- **Confidence**: settled (first-party benchmark data with specific reproducible
  methodology described, though not independently re-run by a third party)
- **Quote**: "In Bun v1.3.14, every build leaks about 3 MB, forever — tools like dev
  servers that bundle on every request eventually run out of memory. In Bun v1.4.0,
  memory levels off" [at ~526-609 MB across 500-2,000 builds, vs. 1,914-6,745 MB in
  v1.3.14 over the same range]. / "Combined with the Rust rewrite, ICU changes, and
  identical code folding, Bun's binary size shrinks by ~20% on Linux & Windows."
- **Our assessment**: This is valuable as a demonstration that the rewrite's payoff
  wasn't purely "AI made this cheap" but also delivered real, measured engineering
  outcomes attributable to the target language's properties (Rust's `Drop` trait
  automatically fixing a class of memory leaks that Zig's manual `defer` discipline
  had allowed to recur) — i.e., the choice of Rust as the rewrite target, not just
  the use of AI to execute it, is doing real work here. The performance gains
  (2.8-4.8%) are modest and should not be oversold; the memory and binary-size wins
  are the more significant results.

### Claim 11: The rewrite introduced 19 known regressions (all subsequently fixed), and the dominant root cause pattern was code that looked syntactically identical across Zig and Rust but had different runtime semantics — e.g., Zig's `assert` always runs its argument while Rust's `debug_assert!` is erased entirely in release builds

- **Evidence**: First-person accounting of regression count and root-cause pattern,
  with a specific worked example (a `debug_assert!`-gated side effect that silently
  stopped running in release builds, breaking React Fast Refresh HMR in specific
  scenarios) plus two further named examples (odd-length slice handling differences,
  and Rust's release builds retaining bounds checks that Zig's `ReleaseFast` builds
  had stripped).
- **Confidence**: settled (first-party account with specific reproduced code and
  issue-tracker references, e.g. #30678, #31188, #31503)
- **Quote**: "This rewrite introduced 19 known regressions, each of which has been
  fixed." / "Most of the regressions came from code that's syntactically identical
  in both languages but semantically different."
- **Our assessment**: This is the most transferable lesson in the source for anyone
  attempting a mechanical AI-driven cross-language port: the dangerous bugs are not
  places where the translation obviously fails (a compiler error), they are places
  where the translation *compiles and looks equivalent* but silently changes
  behavior because of a language-semantics mismatch the mechanical port didn't (and
  couldn't easily) flag. This is a specific, named risk category — "syntactically
  identical, semantically different" — that the corpus has not previously documented
  for AI-driven language migrations, and it's a good candidate for a guide callout
  on large-scale AI-driven ports specifically (not just AI-driven rewrites in general).

### Claim 12: Claude Code itself became the first production user of the Rust-ported Bun runtime (version 2.1.181, released June 17, 2026), with a 10% faster Linux startup time and no user-facing disruption

- **Evidence**: First-person account of the production rollout, naming the specific
  consuming product (Claude Code) and version.
- **Confidence**: settled (first-party, specific, verifiable claim — Claude Code is
  a real, widely-used product whose dependency on Bun is independently checkable)
- **Quote**: "Claude Code v2.1.181 (released June 17th) and later use the Rust port
  of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed.
  Boring is good."
- **Our assessment**: This is a meaningful production-validation data point largely
  because of who the "customer" is: Claude Code (an Anthropic product) silently
  adopted a community/independent-team rewrite of its own runtime dependency, and
  the primary outcome was the absence of an outcome ("barely anyone noticed"). For
  a rewrite of this scale (>1M lines changed) and risk profile, "boring" is itself
  the strongest possible validation signal, and is a useful antidote to guide
  narratives that only celebrate dramatic wins — sometimes the correct measure of
  success for a large migration is that nothing visibly changed for users.

## Concrete Artifacts

### Newsletter free-preview: full extracted text (pragmaticengineer.com, paywall boundary)

```
Source: https://newsletter.pragmaticengineer.com/p/the-pulse-what-can-we-learn-from
(free content only; paywall begins immediately after the excerpt below)

The Pulse is a series covering events, insights, and trends within Big Tech and
startups. Notice an interesting event or trend? Hit reply and share it with me.

Today, we cover:

1. Bun's Rust rewrite with Fable: what can we learn? To a sceptic, spending $165K
   to migrate Bun from Zig to Rust sounds very expensive. But to a realist,
   shortening a 1-2 year migration down to 11 days opens amazing new opportunities
   for devs. However, a thoroughly-tested project is required to pull it off.
2. Anthropic's Fable, OpenAI's GPT-5.6 Sol, Cursor's Grok 4.5, Meta's Muse. Coding
   LLM wars heat up: Fable is back, OpenAI releases a comparable GPT-5.6 Sol,
   Cursor offers cheap & very capable Grok 4.5, and Meta is back with its first
   truly competitive coding model since Llama 3. But how did Gemini slip out of
   the top-ranked AI coding models?
3. North Korean hackers keep trying to infiltrate full-remote companies. The
   founder of a Canadian digital consultancy caught a North Korean dev red-handed,
   using an AI filter. These events are now so common that it's hard to trust
   remote interviewees are who they claim.
4. Industry Pulse. Meta's key logging exposed sensitive data, massive cuts at
   Xbox, Meta could not buy enough AI capacity from Google, Qualcomm acquires
   Modular, and memory price hikes hit Apple products.

1. Bun's Rust rewrite with Fable: what can we learn?

Last week in San Francisco, I met Jarred Sumner, creator of JavaScript runtime,
Bun, and was keen to learn more about the rewrite of Bun from Zig to Rust. But at
the time, Jarred didn't want to say too much, as the tool used for the migration,
Fable, was out of action due to the US government imposing export controls.

[image caption: "Jarred and I at Anthropic's HQ, last week"]

Fortunately, the situation is now resolved and Fable is available globally, and
Jarred has published a detailed post about the project. Before we get into the
migration, some context:

[PAYWALL — "This post is for paid subscribers"]
```

### Bun rewrite: cost, scale, and harness parameters (bun.com/blog/bun-in-rust)

```
Source: https://bun.com/blog/bun-in-rust (Jarred Sumner, linked from the newsletter above)

Tool:        pre-release Claude Fable 5 ("a Mythos-class model"), via Claude Code
             dynamic workflows (~50 workflows total)
Peak scale:  64 Claude instances at once, across 4 git worktrees (16 per worktree)
Duration:    11 days (May 3 - May 14, 2026)
Commits:     6,502 on the port branch (merges excluded); 6,778 including merges
Peak rate:   1,300 lines/minute at peak; 695 commits in the single busiest hour
Net diff:    +1,009,272 lines (final landed diff)
Pre-rewrite: 535,496 lines of Zig (excluding comments)
Post-rewrite unsafe accounting: ~13,000 `unsafe` keywords across ~27,000 lines,
             out of ~780,000 total lines of Rust (~4% of code in an unsafe block;
             78% of those blocks are a single line)

Cost:        5.9B uncached input tokens + 690M output tokens + 72B cached input
             token reads ≈ $165,000 at API pricing

Test suite (per platform, at merge):
  Debian 13 x64:     60,624 tests, 1,386,826 expect() calls, 4,174 files
  macOS 14 arm64:    58,850 tests, 1,259,953 expect() calls, 4,175 files
  Windows 2019 x64:  57,337 tests, 1,007,544 expect() calls, 4,173 files
Merge criterion: 100% of test suite passing in CI on all platforms; "0 tests
  skipped or deleted" (manually verified by Sumner, not just automated)

Harness roles per unit of work:
  1 implementer  — writes the code
  2+ adversarial reviewers — receive ONLY the diff, told to assume it's wrong,
                   job is exclusively to find bugs (do not implement)
  1 fixer        — applies accepted feedback (does not implement or review)

Regressions:  19 known, all fixed post-merge. Dominant root cause: code
  syntactically identical across Zig/Rust but semantically different
  (e.g., Zig `assert` always evaluates its argument; Rust `debug_assert!` is
  erased entirely in release builds — broke React Fast Refresh HMR in one case).

Production deployment: Claude Code v2.1.181 (June 17, 2026) first production
  consumer of the Rust-ported Bun runtime. Linux startup 10% faster
  (517ms -> 464ms per the announcement's own build notes), no other user-visible
  change.

Post-merge hardening: 11 rounds of Claude Code Security review; 24/7
  coverage-guided fuzzing across all Bun parsers (~100 billion executions,
  ~15 PRs from bugs found).
```

### Three bugs adversarial review caught before merge (verbatim-condensed from cited commits)

```
Source: https://bun.com/blog/bun-in-rust

1. Async close-then-drop use-after-free/double-free (js_bun_spawn_bindings.rs):
   `pipe.close(Subprocess::on_pipe_close)` on a `Box<uv::Pipe>` dropped the Box
   at the end of the match arm while libuv's async close callback still held the
   raw pointer -> use-after-free, then double-free when the callback ran.
   Fix: `Box::leak(pipe).close(...)` to keep the allocation alive until the
   async callback frees it.

2. Negative-timespec truncation (node_fs.rs, Windows mtime handling):
   `let sec = t.trunc();` on a negative, non-integer time rounds toward zero
   (-1.5 -> {sec: -1, nsec: -500_000_000}), producing an invalid (negative) nsec.
   Fix: use `.floor()` so nsec stays in [0, 1e9).

3. Eager-evaluation panic in CSS color-mix() (color.rs):
   `first.percentage.unwrap_or(1.0 - second.percentage.unwrap())` evaluates the
   fallback argument eagerly, so `second.percentage.unwrap()` runs and panics
   even when `first.percentage` is `Some`. Reproducible via
   `color-mix(in srgb, red 40%, blue)`.
   Fix: `unwrap_or_else(|| 1.0 - second.percentage.unwrap())` for lazy evaluation.

Attribution: each fix's commit message in the post carries its own review
attribution (e.g. "win-review: ...", "crossplat review fixes: ...").
```

## Cross-References

- **Corroborates**: `blog-anthropic-dynamic-workflows-claude-code.md` Claim 6
  (Bun rewrite: "roughly 750,000 lines of Rust," "eleven days from first commit
  to merge") — this source's "11 days" duration and its own final-state accounting
  of "~780,000" total lines of Rust are consistent with Anthropic's rounder
  "roughly 750,000" figure. This source also fills the gap that note's Extraction
  Notes explicitly flagged ("No pricing or specific token multiplier for dynamic
  workflows was mentioned") with an exact figure: $165,000 / 5.9B uncached input +
  690M output + 72B cached input tokens.
- **Corroborates**: `blog-anthropic-harness-long-running.md` Claim 2 (generator/
  evaluator split "outperforms prompting a single agent to self-critique") and
  `blog-anthropic-dynamic-workflows-claude-code.md` Claim 3 ("checking its work
  before anything reaches you") — Sumner's "1 implementer, 2+ adversarial
  reviewers, 1 fixer" harness is a specific, concrete, practitioner-built instance
  of exactly this pattern, including the explicit rationale ("The Claude that
  wrote the code wants the code to get accepted. The Claude that reviews wants to
  find issues") that echoes but is more concrete than the abstract framing in
  those two notes.
- **Corroborates**: `blog-simonwillison-fable-5-export-controls.md` and
  `blog-simonwillison-fable-mythos-access-directive.md` — both document the
  Fable 5 export-control suspension and its resolution; this source confirms the
  same event from a third, independent angle (a named practitioner directly
  affected in an unrelated production context) and adds a concrete practitioner-
  level cost of the suspension: it silenced public discussion of a completed,
  unrelated engineering project.
- **Extends**: `blog-simonwillison-not-locked-in.md` Claim 5 (programming language
  lock-in "structurally declining," citing the same Bun rewrite via a Hashimoto
  blockquote, without mechanism or metrics) — this source, like
  `blog-anthropic-dynamic-workflows-claude-code.md` before it, supplies mechanism
  and metrics that Willison's note lacked; this source additionally supplies the
  *cost* dimension (exact dollar figure) that neither of the two prior notes had.
- **Extends**: `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`
  — both are Orosz first-hand-reporting pieces from the same period (late June /
  early July 2026 visits) with the same paywall structure (a short free preview,
  most substantive content behind the paywall); this source is a second data point
  that Orosz's newsletter increasingly covers Claude Code / Anthropic-ecosystem
  agentic engineering practices directly and specifically, not just general
  industry trends.
- **Contradicts**: `blog-anthropic-dynamic-workflows-claude-code.md` Claim 6 states
  the Bun rewrite reached "99.8% of the existing test suite passing." This source
  (via Sumner's own primary account) states the merge criterion was 100% passing
  on all platforms, with an explicit manual check that no tests were skipped or
  deleted. These are two specific, different numbers for the same metric on the
  same event, and they are not obviously reconcilable from either text alone (no
  timestamp is given for Anthropic's 99.8% figure within the 11-day project, so it
  may describe an earlier checkpoint rather than the final merge state — but this
  is our speculation, not stated by either source). **A contradiction issue has
  been filed for human resolution: see GitHub issue #1759.** Per MINER.md §4a, we
  do not pick a winner here — both figures are presented as-is in Claim 8 above,
  with the discrepancy flagged rather than silently resolved.
- **Novel**:
  - **Per-category token cost for a large-scale agentic migration**: no prior
    corpus source breaks down uncached-input / output / cached-input token counts
    for a single large agentic project, nor attaches a specific dollar figure to
    the Bun case study specifically.
  - **The specific adversarial-review staffing ratio and reviewer isolation rule**
    ("reviewer receives only the diff, told to assume it's wrong") as a concrete,
    named harness design, with three worked bug examples and their fixes.
  - **The "syntactically identical, semantically different" regression root-cause
    category** for AI-driven mechanical language ports — not previously named in
    the corpus as a specific risk class distinct from ordinary translation errors.
  - **Claude Code itself as first production consumer of an AI-rewritten
    dependency** — a rare "the AI tooling vendor eats its own AI-rewritten
    dependency's dogfood" data point.
  - **A named model behind the Bun case study** (pre-release Claude Fable 5,
    "Mythos-class") — `blog-anthropic-dynamic-workflows-claude-code.md` describes
    the feature (dynamic workflows) but never names which model powered the case
    study it showcases.

## Guide Impact

- **Chapter 05 (Large-Scale Refactoring and Migrations)**: This is the strongest
  cost-anchor addition to the Bun case study, which the guide should already be
  citing per `blog-anthropic-dynamic-workflows-claude-code.md`. Add the specific
  figures: $165,000 total cost (5.9B uncached input / 690M output / 72B cached
  input tokens), against Sumner's own counterfactual that the realistic
  alternative was not a cheaper manual rewrite but *no rewrite at all* (a year of
  frozen bugfixes/features was not a live option). Add the adversarial-review
  staffing ratio (1 implementer : 2+ reviewers : 1 fixer, reviewer sees only the
  diff) as a concrete, reusable harness pattern for practitioners planning their
  own large migrations, with the three worked bug examples as illustrations of
  what this catches. Add the "syntactically identical, semantically different"
  regression category as a named risk for mechanical cross-language ports
  specifically. Flag the 99.8%-vs-100% test-pass discrepancy explicitly rather
  than picking one figure — cite issue #1759 / the eventual CONTRADICTIONS.md
  entry once resolved.
- **Chapter 02 (Harness Engineering)**: The specific implementer/reviewer/fixer
  role split, with the reviewer explicitly told to "assume the code is wrong" and
  given only the diff (no implementer reasoning), is a concrete, named refinement
  of the generator/evaluator pattern already in the guide via
  `blog-anthropic-harness-long-running.md`. Worth adding as a named variant:
  "adversarial diff review" — reviewer isolation (diff-only context) as the
  specific mechanism that prevents the reviewer from inheriting the implementer's
  blind spots.
- **Chapter 01 (Daily Workflows)**: Sumner's own account of what he did when
  workflows failed — edit the workflow's instructions, not the generated code
  (e.g., banning `git stash`/`git reset`/`cargo` mid-loop after Claude instances
  stepped on each other's state; adding a rule rejecting paragraph-long
  justification comments after Claude started explaining away workarounds instead
  of fixing them) — is a good concrete illustration of "supervising the process,
  not the output" for practitioners new to dynamic-workflow-style orchestration.

## Extraction Notes

- The newsletter source itself (the assigned URL for issue #1741) is almost
  entirely paywalled: the free preview is ~350 words (a 4-item teaser list plus
  two opening paragraphs of section 1). Raw HTML was fetched directly via `curl`
  and parsed with BeautifulSoup to confirm the exact free/paywall boundary and to
  extract verbatim text (the `available-content` div ends precisely where a
  `data-testid="paywall"` element begins) — this is more reliable than the
  WebFetch tool's summarization for confirming a paywall boundary exactly.
- Per MINER.md §1, the newsletter's one substantive outbound link
  (`https://bun.com/blog/bun-in-rust`) was followed and read in full — this is a
  single very long, image/chart-heavy post (raw HTML ~430KB); the article text
  was extracted via BeautifulSoup (`<article>` tag `get_text`) rather than relying
  solely on the WebFetch summarizer, specifically to verify every quote used above
  character-for-character against the source, per the quote-verification
  requirement in MINER.md §2a. All quotes in this note were located in the
  extracted flat text and copied verbatim; none were reconstructed from the
  WebFetch summary.
  Three sections of the bun.com post were not extracted into named claims above
  because they are lower-signal for this corpus: a lengthy technical discussion
  of Zig/C++/Rust memory-management tradeoffs predating the AI-driven decision
  (context for "why Rust," not about the AI-driven process itself), a full
  commit-by-commit / CI-build-by-build timeline visualization (hundreds of
  individual timestamped data points — summarized in Concrete Artifacts rather
  than reproduced in full), and a maintainability section with a Zig/Rust code
  diff pair illustrating that the port stayed close to idiomatic-looking code.
  These are available in the source if a future note needs them.
- One discrepancy was found and NOT silently resolved: the test-pass-rate figure
  for the same rewrite differs between this source's primary link (100%, with an
  explicit "not skipped" check) and the existing corpus note's citation of
  Anthropic's own announcement (99.8%). A contradiction issue was filed (GitHub
  issue #1759) per MINER.md §4a rather than picking a winner in this note.
- The three unrelated newsletter teaser items (coding LLM wars, North Korean
  hiring fraud, general industry news) are extracted as Claims 3-4 for completeness
  and issue-tracking purposes, but are flagged as low-confidence/low-utility for
  this corpus since their substantive content is entirely paywalled.
