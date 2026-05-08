---
source_url: https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models
source_type: docs
title: "Rubber Duck in GitHub Copilot CLI now supports more models"
author: GitHub (official changelog)
date_published: 2026-05-07
date_extracted: 2026-05-08
last_checked: 2026-05-08
status: current
confidence_overall: emerging
issue: "#561"
---

# Rubber Duck in GitHub Copilot CLI Now Supports More Models

> GitHub's official May 7, 2026 changelog announcing that Rubber Duck — the built-in
> cross-family reviewer for GitHub Copilot CLI — is now available for GPT orchestrator
> sessions (using a Claude-powered critic), and that Claude orchestrator sessions have
> been upgraded from GPT-5.4 to GPT-5.5 as the Rubber Duck model.

## Source Context

- **Type**: docs (GitHub official product changelog, ~100 words, May 7, 2026)
- **Author credibility**: GitHub engineering team. The linked blog post (April 6, 2026)
  is bylined by Nick McKenna (Applied Researcher III) and Bartek Perz (Principal Applied
  Science Manager). Authoritative for the product facts: that the feature exists, what
  models are used, and what the access requirements are. The linked blog post's SWE-Bench
  Pro benchmark is vendor-provided, not independently replicated.
- **Scope**: The changelog covers two model updates to Rubber Duck in Copilot CLI: (1)
  extending Rubber Duck to GPT orchestrator sessions (with Claude as critic), and (2)
  upgrading the Claude session reviewer from GPT-5.4 to GPT-5.5. One sub-page was
  followed: the linked blog post at
  `https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/`
  (April 6, 2026). That blog post provides benchmark results, activation checkpoint
  design, real-world catch examples, and architectural details not in the changelog.
  Claims from the blog post are explicitly attributed throughout.

## Extracted Claims

### Claim 1: Rubber Duck is GitHub's built-in cross-family review agent in Copilot CLI — it invokes a model from a different AI family to provide a second opinion on the primary agent's work

- **Evidence**: Official changelog names Rubber Duck "the cross-family review agent in
  GitHub Copilot CLI." The linked blog post (April 6, 2026) elaborates: "Rubber Duck is
  a focused review agent, powered by a model from a complementary family to your primary
  Copilot session."
- **Confidence**: settled (product fact — the feature name and cross-family design are
  stated in official materials)
- **Quote**: "Rubber Duck, the cross-family review agent in GitHub Copilot CLI"
- **Our assessment**: The name "cross-family" is definitional — Rubber Duck is specifically
  designed to use a model from a different vendor's family than the orchestrator. When
  Claude orchestrates, GPT reviews; when GPT orchestrates, Claude reviews. The April 6
  blog post explains the rationale: "a model reviewing its own work is still bounded by
  its own training biases: the same training data and techniques, the same blind spots."
  This automates what practitioners like Simon Willison have done manually (see
  `blog-simonwillison-csrf-multimodel-review.md` Claim 2). The design directly targets
  the self-review bias problem that is the primary failure mode of single-model verification.

### Claim 2: As of May 7, 2026, GPT orchestrator sessions can use a Claude-powered Rubber Duck critic when `/experimental` is enabled

- **Evidence**: Official changelog: "Rubber Duck for GPT sessions: When you've selected
  a GPT model as your orchestrator, and `/experimental` is enabled, Copilot will dispatch
  a Claude-powered Rubber Duck agent to provide a second opinion."
- **Confidence**: settled (product fact from official changelog)
- **Quote**: "Copilot will dispatch a Claude-powered Rubber Duck agent to provide a second
  opinion"
- **Our assessment**: This extends Rubber Duck from Claude-only orchestrators to GPT
  orchestrators. The April 6 blog post had said "For now, we are enabling Rubber Duck for
  all Claude family models (Opus, Sonnet, and Haiku) used as orchestrators in the model
  picker" and "We are already exploring other model families for the Rubber Duck to pair
  with GPT-5.4 as the orchestrator." The May 7 changelog delivers on that exploration.
  For practitioners using GPT models as their primary Copilot CLI orchestrator, Rubber
  Duck is now available with Claude as the independent reviewer.

### Claim 3: Claude orchestrator sessions have been upgraded from GPT-5.4 to GPT-5.5 as the Rubber Duck reviewer

- **Evidence**: Official changelog: "Stronger reviewer models for Claude sessions: Claude
  orchestrator sessions can now pair with GPT-5.5 as the Rubber Duck model for more
  effective second opinions." The prior state (GPT-5.4 as reviewer) is confirmed by the
  April 6 blog post: "When you've selected a Claude model from the model picker to use as
  your orchestrator, Rubber Duck will be GPT-5.4."
- **Confidence**: settled (product fact from official changelog)
- **Quote**: "Claude orchestrator sessions can now pair with GPT-5.5 as the Rubber Duck
  model for more effective second opinions"
- **Our assessment**: The upgrade from GPT-5.4 to GPT-5.5 applies silently to existing
  Claude-orchestrator users. The changelog provides no updated benchmark comparing the two
  reviewer models. GPT-5.5 is presumed to offer stronger review capabilities; practitioners
  should expect better Rubber Duck catches after this update without any configuration
  change. The May 7 benchmark data (Claim 7) is from the April 6 blog post using GPT-5.4 —
  the GPT-5.5 results are unpublished.

### Claim 4: Rubber Duck provides second-opinion benefits for both GPT and Claude orchestrator sessions: architectural catches, subtle bugs, and cross-file conflicts

- **Evidence**: Official changelog: "The same second-opinion benefits (architectural
  catches, subtle bugs, and cross-file conflicts) now apply to GPT-driven sessions." The
  linked blog post provides concrete examples for each category (see Concrete Artifacts).
- **Confidence**: settled (benefit categories stated in official materials; concrete
  examples from linked blog post)
- **Quote**: "The same second-opinion benefits (architectural catches, subtle bugs, and
  cross-file conflicts) now apply to GPT-driven sessions."
- **Our assessment**: The three benefit categories map to distinct failure modes that
  self-review tends to miss. Architectural failures require understanding the plan
  holistically; subtle bugs require noticing patterns the implementer is blind to; cross-
  file conflicts require integrating context across multiple files simultaneously. These
  are precisely the blind spots the blog post describes for single-model self-review:
  "same training data and techniques, the same blind spots." Cross-family design directly
  targets all three categories through independent perspective.

### Claim 5: Rubber Duck is in experimental mode and requires `/experimental on` to be toggled in Copilot CLI to access it

- **Evidence**: Official changelog: "To try it, run `copilot` and ensure `/experimental on`
  is toggled." The linked blog post confirms: "Use `/experimental` in Copilot CLI to access
  Rubber Duck alongside our other experimental features."
- **Confidence**: settled (access requirement stated in official materials)
- **Quote**: "To try it, run `copilot` and ensure `/experimental on` is toggled."
- **Our assessment**: The experimental flag gates features under active development. No
  timeline for Rubber Duck graduating to stable was given in either the April 6 post or
  the May 7 changelog. For harness engineering: experimental features are not suitable for
  automated CI/CD pipelines where behavior stability matters. Practitioners should treat
  Rubber Duck as a developer-assist feature for interactive sessions until it reaches
  stable status.

### Claim 6: Rubber Duck activates automatically at specific workflow checkpoints — after plan drafting, after complex implementation, after writing tests (before execution), and when the agent is stuck

- **Evidence**: Linked blog post (April 6, 2026): "For complex work, GitHub Copilot may
  seek a critique automatically at the checkpoints where feedback has the highest return:
  After drafting a plan [...] After a complex implementation [...] After writing tests,
  before executing them [...] The agent can also seek a critique reactively if it gets
  stuck in a loop or can't make progress."
- **Confidence**: settled (checkpoint list stated in official blog post; "may seek" is
  conditional, not guaranteed)
- **Quote**: "For complex work, GitHub Copilot may seek a critique automatically at the
  checkpoints where feedback has the highest return"
- **Our assessment**: The checkpoint design is principled. Plan-time is highest-leverage
  (early catch prevents compounding errors, as the blog post explains: "Assumptions and
  inefficiencies become dependencies, and by the time you notice, you may have to fix
  more than just the small mistake at the start"). Implementation review catches edge
  cases; pre-execution test review catches flawed assertions before they self-reinforce;
  loop-stuck reactive trigger adds a liveness benefit. The blog post notes that Rubber
  Duck is invoked "sparingly, targeting the moments where the signal is highest, without
  getting in the way" — not a reviewer of every step, but of structurally high-risk
  moments. Users can also trigger it explicitly at any point.

### Claim 7: SWE-Bench Pro evaluation shows Sonnet 4.6 + Rubber Duck (GPT-5.4) closes 74.7% of the Sonnet-to-Opus performance gap, with larger gains on difficult multi-file problems

- **Evidence**: Linked blog post (April 6, 2026): "Claude Sonnet 4.6 paired with Rubber
  Duck running GPT-5.4 achieved a resolution rate approaching Claude Opus 4.6 running
  alone, closing 74.7% of the performance gap between Sonnet and Opus." On difficult
  problems: "We noticed that Rubber Duck tends to help more with difficult problems, ones
  that span 3+ files and would normally take 70+ steps. On these problems, Sonnet + Rubber
  Duck scores 3.8% higher than the Sonnet baseline, and 4.8% higher on the hardest
  problems identified across three trials."
- **Confidence**: emerging (vendor-provided benchmark on SWE-Bench Pro; not independently
  replicated; methodology details limited; uses GPT-5.4 reviewer, not the GPT-5.5 used
  after the May 7 upgrade)
- **Quote**: "Claude Sonnet 4.6 paired with Rubber Duck running GPT-5.4 achieved a
  resolution rate approaching Claude Opus 4.6 running alone, closing 74.7% of the
  performance gap between Sonnet and Opus."
- **Our assessment**: This is the highest-value claim in the source for cost-vs-quality
  guide advice. The implication: Sonnet + Rubber Duck is a cost-effective alternative to
  Opus for practitioners trying to improve complex task quality without paying the Opus
  premium. At 74.7% gap closure, the tradeoff may be favorable for teams cost-constrained
  on Opus. However: the benchmark is vendor-provided (GitHub/Anthropic); the gap-closure
  metric is relative, not absolute (the absolute resolution rates are not published); the
  review model is GPT-5.4, not the upgraded GPT-5.5; and SWE-Bench Pro is a benchmark —
  practitioners should validate on their own task distribution before treating this as a
  universal claim.

### Claim 8: Rubber Duck is invoked through Copilot CLI's existing task tool — the same subagent infrastructure used for other subagents

- **Evidence**: Linked blog post (April 6, 2026): "For the technically curious: Rubber
  Duck is invoked through Copilot's existing task tool—the same infrastructure used for
  other subagents."
- **Confidence**: settled (architectural fact stated in official blog post)
- **Quote**: "Rubber Duck is invoked through Copilot's existing task tool—the same
  infrastructure used for other subagents."
- **Our assessment**: Architecturally significant: Rubber Duck is not a special-cased
  hard-coded feature but uses the standard subagent invocation mechanism. This makes the
  cross-family invocation pattern generalizable — the same infrastructure could support
  other cross-family subagent patterns. For the guide's multi-agent coordination chapters:
  Rubber Duck is a product realization of the generator-verifier pattern (see
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2) implemented as a built-in
  CLI subagent invocation.

## Concrete Artifacts

### Rubber Duck model configuration — changelog changes (May 7, 2026)

```
GitHub Copilot CLI — Rubber Duck Model State

BEFORE (April 6, 2026 launch):
  Orchestrator family:  Claude (Opus, Sonnet, Haiku)
  Rubber Duck model:    GPT-5.4
  GPT orchestrators:    NOT supported

AFTER (May 7, 2026 changelog):
  Claude orchestrators → Rubber Duck: GPT-5.5  (upgraded from GPT-5.4)
  GPT orchestrators   → Rubber Duck: Claude-powered critic  (NEW)

Access requirement for both: /experimental on
```

### Rubber Duck activation checkpoints (from linked blog post, April 6, 2026)

```
Proactive (automatic) — highest-signal moments:
  1. After drafting a plan
     Rationale: "catching a suboptimal decision early avoids compounding errors downstream"
  2. After a complex implementation
     Rationale: "second set of eyes on complex code can help catch edge cases"
  3. After writing tests, before executing them
     Rationale: "catch gaps in test coverage or flawed assertions, before
                 self-reinforcing that 'everything passes'"

Reactive:
  4. When agent gets stuck in a loop or can't make progress
     Rationale: "Consulting Rubber Duck can break the logjam"

User-triggered:
  5. Any time — ask Copilot to critique its work explicitly

Design principle: "the agent invokes Rubber Duck sparingly, targeting the moments
where the signal is highest, without getting in the way"
  — GitHub blog post, April 6, 2026
```

### SWE-Bench Pro benchmark results (from linked blog post, April 6, 2026)

```
Evaluation: SWE-Bench Pro (benchmark of large, difficult, real-world coding
            problems drawn from open-source repositories)

Comparison:
  Baseline:               Claude Sonnet 4.6 alone
  + Rubber Duck:          Claude Sonnet 4.6 + GPT-5.4 (Rubber Duck)
  Ceiling:                Claude Opus 4.6 alone

Results:
  Gap closed:             74.7% of Sonnet→Opus performance gap
  Multi-file problems (3+ files, 70+ steps):
    Sonnet + Rubber Duck:    +3.8% over Sonnet baseline
    Hardest problems (3 trials): +4.8% over Sonnet baseline

Note: benchmark used GPT-5.4 as reviewer. May 7, 2026 update upgrades
Claude sessions to GPT-5.5. No updated benchmark published as of extraction.
```

### Real-world catch examples (from linked blog post, April 6, 2026)

```
Architectural catch (OpenLibrary/async scheduler):
  Rubber Duck caught that the proposed scheduler would start and immediately exit,
  running zero jobs—and that even if fixed, one of the scheduled tasks was itself
  an infinite loop.

One-liner bug, big impact (OpenLibrary/Solr):
  Rubber Duck caught a loop that silently overwrote the same dict key on every
  iteration. Three of four Solr facet categories were being dropped from every
  search query, with no error thrown.

Cross-file conflict (NodeBB/email confirmation):
  Rubber Duck caught three files that all read from a Redis key which the new code
  stopped writing. The confirmation UI and cleanup paths would have been silently
  broken on deploy.
```

## Cross-References

- **Corroborates** `blog-simonwillison-csrf-multimodel-review.md` (#312) Claim 2:
  Willison documents a practitioner-driven cross-vendor review pattern (Claude Code
  implements, GPT-5.4 reviews) on a production security migration. Rubber Duck is a
  productized, automated form of the same pattern — cross-family review is now a built-in
  CLI feature, not just a practitioner technique. The SWE-Bench evidence (Claim 7)
  provides benchmarked support for the "cross-family catches different things" hypothesis
  that Willison's report supports anecdotally.

- **Corroborates** `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2
  (generator-verifier pattern): Anthropic's taxonomy names generator-verifier as a
  coordination pattern and notes it requires explicit acceptance criteria. Rubber Duck is
  a product implementation of generator-verifier at the CLI level: the primary agent
  generates; Rubber Duck verifies. The cross-family design adds a dimension that Claim 2
  does not specify — that the verifier's independence is structurally enhanced by different
  training data and family. This is among the first examples in the corpus of a
  vendor-shipping generator-verifier as a built-in product feature rather than an
  architecture practitioners must build themselves.

- **Extends** `docs-github-copilot-cli-auto-model-selection.md` (#203): That source
  documents CLI auto routing (cost- and rate-limit-driven, 0x–1x pool, no Opus). This
  source documents a complementary multi-model CLI feature that is capability-driven, not
  cost-driven. The two features are orthogonal: auto routing optimizes throughput and cost
  efficiency; Rubber Duck optimizes quality on complex tasks. A practitioner using GPT
  auto-mode can also have Claude reviewing via Rubber Duck simultaneously, once GPT
  orchestrator support is stable.

- **Extends** `docs-github-copilot-agent-model-selection.md` (#171): That source
  documents explicit model tier selection for Claude and Codex agents on github.com (user
  chooses Sonnet vs. Opus at task initiation). This source shows a complementary model
  pairing approach: Rubber Duck selects the reviewer model automatically based on the
  orchestrator family, not via user choice. Together they show GitHub offering both manual
  capability selection and automatic cross-family pairing, across different surfaces.

- **Novel**:
  - First corpus source documenting a built-in, checkpoint-triggered cross-family review
    mechanism as a shipping product feature. Prior corpus sources describe the cross-model
    review pattern as a practitioner technique (Willison CSRF), a theoretical taxonomy
    (Anthropic multi-agent patterns), or an advisory recommendation (Osmani orchestra);
    this is the first time it appears as a product feature with benchmark results.
  - First corpus source with vendor-benchmarked evidence (SWE-Bench Pro, 74.7% gap
    closure) that a Sonnet+cross-family-critic combination approaches Opus-level
    performance for complex multi-file tasks. This directly informs the cost-vs-quality
    tradeoff framework in Ch04 with a concrete data point.
  - First documentation in the corpus of automatic checkpoint-triggered second opinion
    (plan, implementation, tests, loop-stuck) as a designed agent workflow pattern with
    explicit architectural rationale.

## Guide Impact

### Chapter 02: Harness Engineering / Daily Tooling

- **Cross-family review as a new CLI capability**: Add a note that Copilot CLI's
  experimental Rubber Duck feature implements the generator-verifier pattern automatically,
  using a cross-family model for independent review. Recommend enabling `/experimental on`
  for complex tasks (multi-file refactors, architectural changes). Note the experimental
  qualifier: not suitable for automated pipelines until stable.
- **Checkpoint-driven review design**: The Rubber Duck checkpoint list (after plan, after
  implementation, after tests, when stuck) provides a practitioner-adoptable pattern for
  any tool. Engineers building their own harnesses can wire similar checkpoints into their
  workflows even without Rubber Duck, by manually invoking a second model at the same
  moments.

### Chapter 03: Safety and Verification

- **Cross-family review as verification pattern**: Update Ch03 to cite Rubber Duck as a
  product example of the cross-family review pattern alongside Willison's manual practice.
  The SWE-Bench Pro results (74.7% gap closure, specific catch types) provide the strongest
  benchmarked evidence in the corpus for why cross-family review works. The three real-
  world catch examples (async scheduler, Solr dict overwrite, NodeBB Redis conflict) are
  high-quality illustrations of the three catch categories.
- **Generator-verifier pattern instantiation**: Ch03 can now cite Rubber Duck as a
  specific, publicly accessible tool when explaining the generator-verifier pattern,
  alongside `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2.

### Chapter 04: Model Selection and Cost Management

- **Sonnet + cross-family critic as a cost-effective Opus alternative**: The SWE-Bench
  benchmark (74.7% gap closure) provides evidence that Sonnet + Rubber Duck is a viable
  middle path between Sonnet (lowest cost) and Opus (highest capability) for complex
  multi-file tasks. Add to the cost decision framework: "For tasks where Opus is
  cost-prohibitive but Sonnet alone is insufficient, Sonnet + Rubber Duck (experimental)
  may provide improved outcomes. Benchmark is vendor-provided; validate on your own task
  distribution."

## Extraction Notes

1. **One sub-page followed**: The changelog is ~100 words and links to a blog post
   (`https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/`,
   April 6, 2026) that provides the benchmark, architecture, activation design, and
   examples. That blog post was fetched in full. All claims citing it are explicitly
   attributed. That blog post may warrant its own source note — it is substantially richer
   than the changelog and documents the original Rubber Duck launch.
2. **Benchmark caveats**: The SWE-Bench Pro results (Claim 7) are vendor-provided, not
   independently replicated. The benchmark used GPT-5.4 as reviewer; the May 7 update
   upgrades Claude sessions to GPT-5.5. Updated benchmark results were not published.
3. **Experimental status**: No graduation timeline was given. All claims about Rubber
   Duck capabilities should be qualified as experimental until further notice.
4. **No contradictions found**: No existing corpus source claims cross-family review is
   ineffective or that the generator-verifier pattern doesn't apply to CLI tools. The
   vendor benchmark (Claim 7) is directionally consistent with the general evidence in the
   corpus for cross-model review. No contradiction issue filed.
