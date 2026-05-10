---
source_url: https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models
source_type: docs
title: "Rubber Duck in GitHub Copilot CLI now supports more models"
author: GitHub (official changelog)
date_published: 2026-05-07
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#561"
---

# Rubber Duck in GitHub Copilot CLI Now Supports More Models

> GitHub's May 2026 changelog announcing that Rubber Duck — a cross-AI-family review
> agent that pairs two models from different providers to overcome shared training
> blind spots — now supports GPT-orchestrated sessions with Claude as reviewer and
> upgrades Claude-orchestrated sessions to GPT-5.5; the linked April 2026 blog post
> provides benchmark evidence that this cross-family pairing closes 74.7% of the
> Sonnet/Opus performance gap on SWE-Bench Pro.

## Source Context

- **Type**: docs (GitHub official product changelog, May 7, 2026; linked blog post by
  Nick McKenna & Bartek Perz, April 6, 2026, also read per MINER.md §1)
- **Author credibility**: GitHub engineering team announcing a production feature
  change. The linked blog post (by Nick McKenna & Bartek Perz, GitHub) provides
  technical depth, the cross-family rationale, and the benchmark evaluation. Both are
  first-party GitHub sources. The performance metrics are self-reported by GitHub
  on SWE-Bench Pro — credible as directional evidence but not independently replicated.
- **Scope**: The Rubber Duck feature in GitHub Copilot CLI: what it is, how it works
  technically, when it activates, the cross-family pairing rationale, the benchmark
  results from the April launch, and the May 7 expansion (adding GPT-orchestrated
  sessions and upgrading Claude sessions to GPT-5.5). Does NOT cover: cost impact
  of running dual-model sessions; whether Rubber Duck is available outside of
  experimental mode; how Rubber Duck interacts with skills or CLAUDE.md context;
  latency implications; or whether the SWE-Bench Pro improvements generalize beyond
  coding tasks.

## Extracted Claims

### Claim 1: Rubber Duck is a cross-AI-family review agent that uses a second model from a different AI provider to provide an independent second opinion during agentic sessions

- **Evidence**: Blog post (April 6, 2026) by GitHub engineers Nick McKenna & Bartek Perz,
  providing the design rationale and technical description. The changelog (May 7, 2026)
  names it "the cross-family review agent."
- **Confidence**: settled (product fact — the feature exists and is described in detail)
- **Quote**: "Rubber Duck leverages a second model from a different AI family to act as an
  independent reviewer, assessing the agent's plans and work at the moments where feedback
  matters most."
- **Our assessment**: This is the defining claim. Rubber Duck is not self-review or
  reflection — it's a deliberate architectural choice to route evaluation through a
  different AI provider's model. The "different AI family" framing is central to the
  design rationale (see Claim 2). For practitioners: Rubber Duck is the CLI's automated
  equivalent of "get a second opinion from a different expert." Its value depends entirely
  on whether cross-family models genuinely have meaningfully different blind spots — which
  the training-bias claim (Claim 2) asserts and the benchmark data (Claim 6) supports.

### Claim 2: Cross-family review specifically targets the limitation that same-model self-review cannot escape its own training biases and blind spots

- **Evidence**: Blog post, providing the technical rationale for the design choice. The
  design explicitly contrasts with self-reflection approaches.
- **Confidence**: emerging (the training-bias rationale is logical and commonly accepted
  in ML, but empirically demonstrating that cross-family review outperforms same-model
  self-review in practice requires controlled comparison, which the benchmark partially
  provides)
- **Quote**: "However, a model reviewing its own work is still bounded by its own training
  biases: the same training data and techniques, the same blind spots."
- **Our assessment**: The blog post acknowledges that self-reflection is "a proven technique"
  but argues it has a ceiling. The cross-family design is the proposed ceiling-breaker.
  For guide advice: the training-bias argument is strong in principle and the benchmark
  provides supporting evidence, but practitioners should treat the 74.7% gap-closure
  (Claim 6) as directional, not definitive — it is measured on one benchmark
  (SWE-Bench Pro) by the feature's own developers. The claim that GPT-5.5 and Claude
  have meaningfully different blind spots on real-world coding problems is plausible
  but not independently verified.

### Claim 3: Rubber Duck activates automatically at four key moments in a session, plus on user demand

- **Evidence**: Blog post lists the activation triggers explicitly.
- **Confidence**: settled (product behavior described in official blog post)
- **Quote**: Activation points are "After drafting a plan," "After a complex
  implementation," "After writing tests, before executing them," and "reactively if it
  gets stuck in a loop or can't make progress."
- **Our assessment**: The trigger design is thoughtful — Rubber Duck activates at natural
  quality-gate moments in the agentic workflow, not on every step (which would be
  expensive) or only at the end (when changes are hard to incorporate). The "stuck in
  a loop" trigger is particularly interesting: it uses cross-family review as a recovery
  mechanism, not just a quality check. For Ch02: these four triggers represent a concrete
  pattern for when to invoke an external reviewer in any multi-agent harness — they could
  be adapted for custom pipelines that need automated quality gates.

### Claim 4: Users can also request Rubber Duck critique on demand at any point during a session

- **Evidence**: Blog post describes explicit user-invocation.
- **Confidence**: settled (product behavior described in official blog post)
- **Quote**: "On demand, whenever you ask. Just tell Copilot to critique its work, and it
  will invoke Rubber Duck, incorporate the feedback, and show you exactly what changed."
- **Our assessment**: The on-demand capability makes Rubber Duck useful as a deliberate
  practice, not just an automatic safeguard. Practitioners who want cross-family review
  at specific decision points (e.g., before merging a significant change) can explicitly
  trigger it. The "show you exactly what changed" output is a transparency affordance
  similar to the model-disclosure in the CLI auto routing (see Cross-References).

### Claim 5: Rubber Duck is invoked through Copilot's existing task tool infrastructure — the same mechanism used for other subagents

- **Evidence**: Blog post provides the technical implementation detail explicitly.
- **Confidence**: settled (technical fact from official blog post)
- **Quote**: "For the technically curious: Rubber Duck is invoked through Copilot's
  existing task tool—the same infrastructure used for other subagents."
- **Our assessment**: This is a significant architectural signal: Rubber Duck is not
  a special-cased feature but a use of the general subagent infrastructure. For Ch02:
  this implies the subagent task-tool pattern is extensible — teams building custom
  Copilot harnesses may be able to invoke cross-family review as a subagent step in
  their own workflows. It also means Rubber Duck's availability is tied to subagent
  infrastructure limits (rate limits, context windows, etc.).

### Claim 6: Claude Sonnet 4.6 paired with Rubber Duck (GPT-5.4 reviewer) closes 74.7% of the performance gap between Sonnet and Opus on SWE-Bench Pro

- **Evidence**: Blog post benchmark results from GitHub evaluation. Methodology: tested
  on SWE-Bench Pro, "a benchmark of large, difficult, real-world coding problems drawn
  from open-source repositories." The specific subset is problems spanning 3+ files and
  70+ steps.
- **Confidence**: emerging (self-reported benchmark by feature developers; single benchmark
  run; not independently replicated)
- **Quote**: "Claude Sonnet 4.6 paired with Rubber Duck running GPT-5.4 achieved a
  resolution rate approaching Claude Opus 4.6 running alone, closing 74.7% of the
  performance gap between Sonnet and Opus."
- **Our assessment**: This is the most consequential claim in the source. If it holds
  beyond SWE-Bench Pro, it means Rubber Duck fundamentally changes the Sonnet/Opus
  cost-capability tradeoff: instead of paying Opus prices for Opus quality, practitioners
  can pay Sonnet prices + Rubber Duck overhead to approach Opus quality. For Ch04
  (Model Selection and Cost Management): this should be cited as a concrete data point
  when advising the Sonnet-vs-Opus decision for CLI agentic workflows — but with the
  caveat that the measurement is on a specific benchmark, by the feature's own developers,
  and on problems that specifically favor Rubber Duck (3+ files, 70+ steps). Simpler
  tasks may not see the same improvement.

### Claim 7: Rubber Duck's benefit concentrates on difficult multi-file problems (3+ files, 70+ steps) with increasing gains at the hardest difficulty tier

- **Evidence**: Blog post performance data: on the difficult subset, 3.8% improvement
  over Sonnet baseline; on the hardest problems, 4.8% improvement.
- **Confidence**: emerging (same single benchmark caveat as Claim 6)
- **Quote**: "We noticed that Rubber Duck tends to help more with difficult problems, ones
  that span 3+ files and would normally take 70+ steps." And: "On these problems, Sonnet
  + Rubber Duck scores 3.8% higher than the Sonnet baseline, and 4.8% higher on the
  hardest problems."
- **Our assessment**: The difficulty-dependent improvement is a crucial conditioning
  variable. Rubber Duck is not a flat improvement for all tasks — it adds disproportionate
  value for complex, multi-file, multi-step tasks. For guide advice: practitioners doing
  simple, single-file tasks may see minimal benefit from Rubber Duck while incurring the
  latency cost of a second model call. Teams should consider enabling `/experimental`
  primarily for sessions where they expect complex, cross-file work.

### Claim 8: The May 7, 2026 changelog extends Rubber Duck to GPT-orchestrated sessions, with Claude serving as the cross-family reviewer

- **Evidence**: Official GitHub changelog, May 7, 2026. First explicit mention of
  Claude-as-reviewer (reverse of the original April configuration where Claude was
  orchestrator and GPT-5.4 was reviewer).
- **Confidence**: settled (product fact from official changelog)
- **Quote**: "Rubber Duck, the cross-family review agent in GitHub Copilot CLI, is now
  available using a Claude-powered critic agent when your session is using a GPT model."
  And: "When you've selected a GPT model as your orchestrator, and `/experimental` is
  enabled, Copilot will dispatch a Claude-powered Rubber Duck agent to provide a second
  opinion."
- **Our assessment**: The May update completes the bidirectional model-family pairing:
  originally only Claude-orchestrated sessions could use Rubber Duck (with GPT-5.4
  reviewing); now GPT-orchestrated sessions can use it too (with Claude reviewing). This
  symmetry is architecturally important — the feature is genuinely cross-family, not
  just "Claude + a GPT reviewer." For practitioners who prefer GPT-5.x as their primary
  orchestrator, Rubber Duck is now also available. The specific Claude reviewer model for
  GPT sessions is not named in the changelog.

### Claim 9: The May 7, 2026 changelog upgrades Claude-orchestrated sessions from GPT-5.4 to GPT-5.5 as the Rubber Duck reviewer

- **Evidence**: Official GitHub changelog, May 7, 2026, stating the reviewer model
  upgrade for Claude sessions. The blog post (April 6) confirms GPT-5.4 was the original
  reviewer for Claude sessions.
- **Confidence**: settled (product fact from official changelog)
- **Quote**: "Claude orchestrator sessions can now pair with GPT-5.5 as the Rubber Duck
  model for more effective second opinions."
- **Our assessment**: GPT-5.5 is a new model not previously mentioned in the Copilot
  CLI corpus — it does not appear in the auto-model-selection pool documented in
  `docs-github-copilot-cli-auto-model-selection.md` (which lists GPT-5.4, GPT-5.3-Codex,
  Sonnet 4.6, Haiku 4.5 as of April 17, 2026). GPT-5.5 appears to have been added to
  Copilot's model roster between April 17 and May 7. The upgrade from GPT-5.4 to
  GPT-5.5 is framed as quality improvement ("more effective second opinions") but no
  new benchmark data for the GPT-5.5 pairing is provided in the changelog.

### Claim 10: The feature requires enabling `/experimental` mode via the CLI command `copilot`

- **Evidence**: Both the changelog and blog post state this access requirement.
- **Confidence**: settled (stated in both official sources)
- **Quote**: "To try it, run `copilot` and ensure `/experimental on` is toggled."
- **Our assessment**: The experimental gate signals that Rubber Duck is not yet a
  default-on production feature — it requires opt-in and may have stability caveats.
  For Ch02: document the experimental flag as a prerequisite when referencing the
  feature. The "experimental" label also implies behavior may change or the feature
  could be removed before general availability, so guide advice should be appropriately
  hedged. Teams incorporating Rubber Duck into automated harnesses should monitor for
  graduation to production status.

### Claim 11: Rubber Duck's second-opinion benefits for GPT sessions include catching architectural issues, subtle bugs, and cross-file conflicts

- **Evidence**: Official changelog, describing the capability scope for GPT-orchestrated
  sessions.
- **Confidence**: settled (product claim in official changelog)
- **Quote**: "The same second-opinion benefits (architectural catches, subtle bugs, and
  cross-file conflicts) now apply to GPT-driven sessions."
- **Our assessment**: The problem categories targeted — architectural issues, subtle
  bugs, cross-file conflicts — are precisely the problem types where single-model
  agentic coding is most likely to fail on difficult tasks. These are the categories
  that motivated the 3+ files / 70+ steps difficulty definition in the benchmark.
  The feature's design is aligned with where multi-file, long-horizon tasks typically
  go wrong.

## Concrete Artifacts

### Rubber Duck Activation Triggers (from blog post, April 6, 2026)

```
Rubber Duck activates automatically at:
  1. After drafting a plan
  2. After a complex implementation
  3. After writing tests, before executing them
  4. Reactively if it gets stuck in a loop or can't make progress

On demand:
  - User tells Copilot to critique its work
  - Copilot invokes Rubber Duck, incorporates feedback, shows what changed
```

### Model Pairing Matrix (as of May 7, 2026)

```
GitHub Copilot CLI — Rubber Duck Cross-Family Pairings

Original (April 6, 2026):
  Orchestrator: Claude (Opus, Sonnet, or Haiku)
  Reviewer:     GPT-5.4
  Access:       /experimental on

Updated (May 7, 2026):
  Orchestrator: Claude (Opus, Sonnet, or Haiku)
  Reviewer:     GPT-5.5   ← upgraded from GPT-5.4
  Access:       /experimental on

  Orchestrator: GPT model (specific version not stated)
  Reviewer:     Claude-powered critic (specific model not stated)
  Access:       /experimental on

Note: GPT-5.5 is not listed in the Copilot CLI auto-model-selection
pool as of April 17, 2026 — appears to be a new model added to
Copilot's roster between April 17 and May 7, 2026.
```

### SWE-Bench Pro Results (from blog post, April 6, 2026)

```
Benchmark: SWE-Bench Pro (real-world open-source coding problems)
Focus subset: problems spanning 3+ files, normally requiring 70+ steps

Results for Claude Sonnet 4.6 + Rubber Duck (GPT-5.4 reviewer):
  vs. Claude Sonnet 4.6 alone:
    All difficult problems:  +3.8% resolution rate
    Hardest problems:        +4.8% resolution rate

  vs. Claude Opus 4.6 alone:
    Gap closed:              74.7%
    ("resolution rate approaching Claude Opus 4.6 running alone")

Self-reported by GitHub engineering team (Nick McKenna & Bartek Perz).
Not independently replicated.
```

### CLI Access

```bash
# Enable experimental mode (required for Rubber Duck)
copilot
/experimental on

# On-demand critique
# Tell Copilot directly: "critique your work" or similar natural language
```

### Technical Architecture Note

```
Rubber Duck implementation:
  - Invoked via Copilot's existing task tool
  - Same infrastructure used for other subagents
  - Not a special-cased feature — uses the general subagent mechanism
```

## Cross-References

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` (issue #203),
  specifically Claim 5 (CLI surfaces which model was used for transparency) and
  Claim 8 (users can switch between modes): both features add transparency and user
  control to multi-model CLI behavior. Auto routing routes to the most efficient model;
  Rubber Duck adds a second-model quality layer. They serve distinct purposes —
  auto is for cost/availability optimization; Rubber Duck is for quality improvement
  through cross-family review. The GPT-5.4 that appears in the auto pool (Claim 3 of
  that note) was the original Rubber Duck reviewer for Claude sessions; the May 7
  update introduces GPT-5.5 as the reviewer, a model NOT currently in the auto pool.
  This signals GitHub's model roster is expanding beyond what was documented in
  the April 17 auto-selection announcement.

- **Extends** `docs-github-copilot-agent-model-selection.md` (issue #171), Claim 7
  (the changelog implies model tier matters but provides no guidance): Rubber Duck
  directly addresses the Sonnet/Opus capability gap without requiring the user to
  explicitly select Opus. The 74.7% gap-closure result (Claim 6 here) is the empirical
  answer to Claim 7's open question — practitioners can approximate Opus quality
  for difficult multi-file problems by pairing Sonnet + Rubber Duck rather than
  selecting Opus explicitly. This should be referenced when building the guide's
  Sonnet-vs-Opus decision framework.

- **Complements** `docs-github-copilot-agent-skills-cli.md` (issue #189), Claim 1
  (skills as a package manager for agent capabilities): Rubber Duck "is invoked through
  Copilot's existing task tool—the same infrastructure used for other subagents,"
  connecting it to the same subagent infrastructure that the `gh skill` package manager
  distributes capabilities into. Both sources reveal GitHub treating the CLI subagent
  infrastructure as the primary surface for new agentic capabilities.

- **Novel**:
  - First source in the corpus to document **cross-AI-family review** as a deliberate
    architectural pattern with a named rationale: that same-family self-review cannot
    escape shared training biases. Prior multi-agent sources discuss orchestrator/
    sub-agent patterns but not the specific motivation of using a different AI provider
    to overcome provider-specific blind spots.
  - First source to provide **empirical benchmark data** (SWE-Bench Pro) showing
    a specific magnitude of improvement from cross-family pairing (74.7% gap closure,
    3.8–4.8% absolute improvement on difficult problems). No prior source in the corpus
    quantifies the quality benefit of cross-family vs. same-model review.
  - First documented evidence of **GPT-5.5** in the GitHub Copilot model roster.
    Not present in the April 17 auto-selection pool (`docs-github-copilot-cli-auto-model-selection.md`).
  - The **automatic quality-gate trigger pattern** (plan, implementation, tests,
    stuck-in-loop) is novel: prior corpus sources describe multi-agent orchestration
    in terms of task delegation, not automated quality-gate checkpoints embedded in
    the agentic workflow.

## Guide Impact

### Chapter 02: Harness Engineering / Daily Tooling

- **Cross-family review as a new CLI capability**: Add a note that Rubber Duck is now
  available for both Claude and GPT-orchestrated sessions in the Copilot CLI. Document
  the `/experimental on` prerequisite. For teams building CLI harnesses that wrap
  Copilot: Rubber Duck activates automatically at four workflow moments (plan, complex
  implementation, test-writing, loop-detection), which means harness scripts that
  drive Copilot CLI may see unexpected additional model invocations. Factor in the
  latency and potential rate-limit implications of the second model call.
- **Quality-gate trigger pattern**: The four Rubber Duck activation moments (Claim 3)
  are a reusable design pattern for any multi-agent harness that wants automated
  quality checkpoints. Document this pattern explicitly: invoke a cross-provider
  reviewer after planning, after major implementation, after test generation, and
  as a loop-breaking mechanism.
- **Subagent infrastructure connection**: Rubber Duck uses the same task-tool
  infrastructure as other Copilot subagents (Claim 5). This is relevant for teams
  evaluating the Copilot CLI subagent ecosystem — Rubber Duck demonstrates that
  the task tool can be used for quality-assurance subagents, not just capability
  subagents.

### Chapter 04: Model Selection and Cost Management

- **Rubber Duck as a Sonnet/Opus cost alternative**: The 74.7% gap-closure result
  (Claim 6) means Sonnet + Rubber Duck is a viable alternative to Opus for difficult
  multi-file coding tasks in the Copilot CLI. Add as a concrete cost optimization
  pattern: use Sonnet (lower cost) with `/experimental on` for complex agentic
  sessions rather than defaulting to Opus. Caveat: the benefit concentrates on
  3+ file, 70+ step problems; simpler tasks may not justify the extra latency.
- **GPT-5.5 now in Copilot roster**: The May 7 changelog introduces GPT-5.5 as
  a Rubber Duck reviewer. The auto-model-selection pool (issue #203) should be
  checked for whether GPT-5.5 has been added to that pool as well — the current
  note (April 17) does not include it.

### Chapter 01: Daily Workflows

- **When to enable experimental mode**: Add practical guidance on when a practitioner
  should toggle `/experimental on`: for complex, multi-file agentic sessions where
  catching architectural issues or cross-file conflicts early is worth the additional
  latency. For routine, single-file, or well-understood tasks, the overhead may not
  be justified.
- **On-demand critique as a practice**: Document "tell Copilot to critique its work"
  as a deliberate workflow step before merging or finalizing significant AI-generated
  changes (Claim 4). This gives practitioners a human-controlled quality gate in
  addition to the automatic triggers.

## Extraction Notes

1. **Two sources read**: The primary source is the GitHub changelog (May 7, 2026,
   ~6 sentences). The linked blog post (April 6, 2026, ~5 min read) was followed
   per MINER.md §1 as a substantive linked page. The blog post provides the technical
   depth, rationale, and benchmark data that the changelog only briefly references.
   Both sources are first-party GitHub engineering content.
2. **Blog post predates changelog**: The blog post (April 6) announced the initial
   Rubber Duck launch for Claude-orchestrated sessions with GPT-5.4 reviewer. The
   changelog (May 7) is an update expanding to GPT-orchestrated sessions and upgrading
   to GPT-5.5 for Claude sessions. The source note covers both.
3. **Benchmark caveats**: The 74.7% gap-closure metric is self-reported by GitHub
   developers in the launch blog post, measured on SWE-Bench Pro. The result should
   be treated as directional evidence, not a definitive claim. The original pairing
   (Sonnet + GPT-5.4) is what was benchmarked; the upgraded pairing (Sonnet + GPT-5.5)
   has no published benchmark results as of May 7, 2026.
4. **Reviewer model unspecified for GPT sessions**: The changelog does not name which
   Claude model serves as the Rubber Duck reviewer for GPT-orchestrated sessions.
   This is a gap — the model selection matters for understanding capability and cost.
5. **No contradictions to file**: No existing source note claims that cross-family
   review is ineffective, or that same-model self-reflection is sufficient for complex
   agentic tasks. The gap-closure metric (74.7%) does not contradict the auto-model-
   selection note — those cover different features. No contradiction issue required.
6. **GPT-5.5 novelty**: GPT-5.5 appears here for the first time in the corpus.
   Its presence as a Rubber Duck reviewer (May 7) suggests it was added to Copilot's
   model roster between April 17 and May 7, 2026. This is a corpus-level factual update
   that may affect the accuracy of `docs-github-copilot-cli-auto-model-selection.md`'s
   model pool enumeration — that note should be re-checked.
