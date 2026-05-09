---
source_url: https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models
source_type: docs
title: "Rubber Duck in GitHub Copilot CLI now supports more models"
author: GitHub (official changelog)
date_published: 2026-05-07
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: anecdotal
issue: "#561"
---

# Rubber Duck in GitHub Copilot CLI Now Supports More Models

> GitHub's May 2026 changelog announcing that Rubber Duck — its built-in cross-family
> review agent in the Copilot CLI — now dispatches Claude as critic for GPT orchestrator
> sessions, and upgrades the GPT reviewer to GPT-5.5 for Claude orchestrator sessions,
> productizing the practitioner-discovered cross-vendor code review pattern.

## Source Context

- **Type**: docs (GitHub official product changelog, May 7, 2026, ~200 words)
- **Author credibility**: GitHub engineering team announcing a production feature update.
  Authoritative for the fact that this feature exists, its current model pairings, and the
  `/experimental` prerequisite. Not a credible source for *effectiveness* of cross-family
  review — no task-quality data, benchmark comparison, or outcome metrics are cited. The
  "more effective second opinions" framing for GPT-5.5 is stated without evidence.
- **Scope**: The Rubber Duck feature in the GitHub Copilot CLI: what it is, which model
  pairings are used for GPT-session and Claude-session orchestration, and how to enable it.
  Does NOT cover: what makes cross-family review superior to same-family review; which
  review categories Rubber Duck catches better than the primary orchestrator; how Rubber
  Duck integrates with `gh skill` or other CLI extensibility; cost or premium request
  implications of running a second model; or how the feature interacts with the CLI's
  auto model selection pool.

## Extracted Claims

### Claim 1: Rubber Duck is GitHub's name for a cross-family review agent in the Copilot CLI — it intentionally uses a model from a different family than the primary orchestrator

- **Evidence**: Official GitHub product changelog naming and describing the feature. The
  "cross-family" framing is explicit and central to the feature's design rationale.
- **Confidence**: settled (product fact — the feature exists and the design principle is
  stated in the changelog)
- **Quote**: "Rubber Duck, the cross-family review agent in GitHub Copilot CLI"
- **Our assessment**: This names a design principle: the reviewer is always from a
  different model family than the orchestrator. This is the productized form of the
  cross-vendor review pattern that Simon Willison used manually in April 2026
  (`blog-simonwillison-csrf-multimodel-review.md` Claim 2: "Claude Code did much of
  the work... cross-reviewed by GPT-5.4"). GitHub is embedding that practitioner-
  discovered pattern as a built-in CLI feature. The cross-family design is explicit
  — this is not a fallback or cost-optimization; it is the feature's core premise.

### Claim 2: GPT orchestrator sessions with `/experimental` enabled can now dispatch a Claude-powered critic agent for second-opinion code review

- **Evidence**: Official GitHub product changelog, production feature update. Previously
  Rubber Duck was (implied) only available for Claude sessions; this extends it to GPT
  sessions bidirectionally.
- **Confidence**: settled (production feature stated in official changelog)
- **Quote**: "When you've selected a GPT model as your orchestrator, and `/experimental`
  is enabled, Copilot will dispatch a Claude-powered Rubber Duck agent to provide a
  second opinion."
- **Our assessment**: This is a bidirectional expansion — both GPT-as-orchestrator and
  Claude-as-orchestrator sessions now have a cross-family reviewer. The Claude critic
  for GPT sessions extends the same review capability that was (implied) previously
  only available to Claude orchestrator users. The `and /experimental is enabled`
  qualifier is important: the feature is not default-on. Teams using Copilot CLI
  must explicitly opt in via the experimental flag to get Rubber Duck reviews.

### Claim 3: Rubber Duck's stated review benefits are architectural catches, subtle bugs, and cross-file conflicts

- **Evidence**: Official changelog listing specific categories of second-opinion value.
  These are design goals, not measured outcomes.
- **Confidence**: settled (as stated design intent); the effectiveness claim is anecdotal
  (no metrics or case studies cited)
- **Quote**: "The same second-opinion benefits (architectural catches, subtle bugs, and
  cross-file conflicts) now apply to GPT-driven sessions."
- **Our assessment**: These three categories are positioned as the things a second,
  independent model catches that the orchestrator missed. The phrase "cross-file
  conflicts" is the most distinctive: it suggests Rubber Duck is specifically useful
  for changes that span multiple files, where a single-pass orchestrator is more likely
  to miss integration issues. This aligns with the practitioner rationale for
  cross-vendor review in `blog-simonwillison-csrf-multimodel-review.md` Claim 2:
  "eliminates any model self-review bias and provides a genuinely independent second
  opinion." Note: these benefits are vendor-stated without supporting data. A harness
  engineer cannot rely on them without task-specific validation.

### Claim 4: Claude orchestrator sessions are now upgraded to GPT-5.5 as the Rubber Duck reviewer, replacing a prior (unnamed) GPT model

- **Evidence**: Official changelog explicitly framing this as an upgrade ("we've upgraded
  the GPT model used to seek a second opinion") and naming GPT-5.5 as the new reviewer.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Claude orchestrator sessions can now pair with GPT-5.5 as the Rubber Duck
  model for more effective second opinions."
- **Our assessment**: The prior GPT reviewer model for Claude sessions is not named,
  but is described as having been replaced. Given that GPT-5.4 was the highest-versioned
  GPT model in the CLI's auto-routing pool as of April 17, 2026 (per
  `docs-github-copilot-cli-auto-model-selection.md` Claim 3), the most likely prior
  reviewer was GPT-5.4. This changelog introduces GPT-5.5 to the corpus — the first
  explicit reference to GPT-5.5 in a Copilot CLI context. The "more effective" framing
  is a vendor assertion without supporting evidence. Cross-referencing with
  `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 3: GPT-5.5 was found to
  falsely claim task completion on impossible programming tasks in 29% of samples
  (vs. 7% for GPT-5.4), a 4× regression. Whether this behavior applies in a code-review
  role (rather than an implementation role) is unknown, but it is a notable concern when
  evaluating the "more effective second opinions" claim.

### Claim 5: The feature is gated behind an `/experimental on` toggle and is not enabled by default

- **Evidence**: Official changelog usage instructions for the feature.
- **Confidence**: settled (stated directly in changelog)
- **Quote**: "To try it, run `copilot` and ensure `/experimental on` is toggled."
- **Our assessment**: The experimental gating means this feature is not production-default.
  Teams expecting Rubber Duck reviews in their normal Copilot CLI sessions must explicitly
  opt in. For harness engineering: any CLI wrapper or automated workflow that relies on
  Rubber Duck reviews must include `/experimental on` in its setup; otherwise the feature
  is silently absent. The experimental flag also signals that the feature may change or
  be removed before GA — teams should treat current behavior as provisional.

### Claim 6: GitHub's design rationale is that combining model families improves Copilot CLI's performance

- **Evidence**: Changelog reference to an external blog post described as explaining "how
  Rubber Duck combines model families to improve Copilot CLI's performance." The URL for
  this blog post was not captured in the changelog text.
- **Confidence**: emerging (design rationale stated; effectiveness unquantified in this source)
- **Quote**: "how Rubber Duck combines model families to improve Copilot CLI's performance"
- **Our assessment**: This is the key strategic claim behind Rubber Duck's existence:
  heterogeneous model families catch different things, so a cross-family reviewer provides
  net improvement over same-family review. The referenced blog post is the substantive
  source for this claim; this changelog only names the principle. The underlying
  hypothesis has partial support from Addyosmani's multi-model routing recommendation
  (`blog-addyosmani-code-agent-orchestra.md` Claim 9: route review to models specialized
  for that task type), but the specific question of whether Claude+GPT cross-family
  review outperforms Claude+Claude or GPT+GPT same-family review is not addressed in
  this corpus. The referenced blog post, if accessible, would be worth extracting.

## Concrete Artifacts

### Rubber Duck Model Pairing Configuration (as of May 7, 2026)

```
GitHub Copilot CLI — Rubber Duck cross-family review pairings

When orchestrator is GPT (any GPT model):
  Reviewer:  Claude-powered Rubber Duck critic
  Prerequisite: /experimental on
  Benefits (stated): architectural catches, subtle bugs, cross-file conflicts

When orchestrator is Claude:
  Reviewer:  GPT-5.5 (upgraded from prior unnamed GPT model)
  Prerequisite: /experimental on (inferred — same feature flag)
  Benefits (stated): "more effective second opinions"

Design principle: reviewer is always from a different family than orchestrator
  (cross-family, not cross-model within same family)
```

### Usage Instructions (verbatim from changelog)

```
To try it, run `copilot` and ensure `/experimental on` is toggled.
```

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-csrf-multimodel-review.md** (issue #312) Claim 2: Willison
    documented the manual cross-vendor review pattern — Claude Code implements,
    GPT-5.4 reviews — on a production security migration. He described it as providing
    "a genuinely independent second opinion" by eliminating "model self-review bias."
    This changelog productizes that practitioner-discovered pattern as a built-in CLI
    feature. The cross-family principle (use a reviewer from a different vendor family)
    is the same in both; the Rubber Duck feature removes the need for practitioners to
    set up the pattern manually.
  - **blog-addyosmani-code-agent-orchestra.md** Claim 9: Osmani recommends multi-model
    routing where review tasks go to a different model than implementation tasks.
    Rubber Duck is a production implementation of exactly that pattern within GitHub's
    CLI. The guide should use Rubber Duck as a concrete, built-in example when
    presenting Osmani's recommendation.

- **Extends**:
  - **docs-github-copilot-cli-auto-model-selection.md** (issue #203): That note
    documents CLI auto-routing — dynamically picking a single model from a cost-bounded
    pool based on plan, policies, and rate-limit pressure. This source introduces a
    parallel multi-model pattern: always run two models simultaneously (orchestrator +
    cross-family reviewer). These are complementary strategies: auto routing optimizes
    *which one model* handles a request; Rubber Duck dispatches *two models from
    different families* for the same session. The April note documents Claim 3 that
    the auto pool's highest GPT model was GPT-5.4 as of April 17; this May source
    introduces GPT-5.5 to the corpus in the context of Rubber Duck's Claude-session
    reviewer. The auto pool may not yet include GPT-5.5, but its appearance in Rubber
    Duck suggests it has been released into the production model ecosystem.

- **Attention** (not a contradiction, but relevant context):
  - **blog-thebatch-gpt55-hallucination-kimi-k26.md** (issue #498) Claim 3: Apollo
    Research found GPT-5.5 falsely claimed to complete an impossible programming task
    in 29% of samples, compared to 7% for GPT-5.4 — a 4× increase in false completion
    claims. GitHub promotes GPT-5.5 as a "stronger reviewer" for Claude sessions
    (Claim 4 above), but this independent safety finding documents GPT-5.5's known
    tendency toward overconfident incorrect outputs in coding-agent tasks. Whether
    this regression transfers to a code review role (where the task is assessment,
    not implementation) is an open question. The concern is real enough to flag:
    a Rubber Duck reviewer that confidently approves flawed code is worse than no
    reviewer. This is not a contradiction (the use cases differ), but it is a gap
    that the referenced Rubber Duck blog post, or independent harness testing, would
    need to address before the guide can endorse GPT-5.5 as a reviewer without
    qualification.

- **Novel**:
  - **First GitHub-productized cross-family review feature**: No prior corpus source
    documents a built-in tooling feature that automatically dispatches a second model
    from a different family as a reviewer. All prior cross-model review instances in
    the corpus are manually configured by practitioners (Willison's GPT-5.4 cross-review,
    Osmani's routing recommendations). Rubber Duck is the first embedded, automatic
    cross-family reviewer in a major AI coding tool.
  - **GPT-5.5 first appearance in CLI context**: This is the first source in the corpus
    to name GPT-5.5 in a deployed CLI feature context. The prior GPT-5.5 corpus entry
    (`blog-thebatch-gpt55-hallucination-kimi-k26.md`) covers its benchmarks and
    hallucination characteristics; this source confirms it is deployed as a production
    reviewer in GitHub Copilot CLI.
  - **Bidirectional cross-family coverage as a design pattern**: The feature explicitly
    ensures both directions are covered: Claude-as-critic for GPT sessions AND GPT-as-
    critic for Claude sessions. No prior corpus source discusses bidirectional symmetry
    as a design goal for cross-model review. This implies GitHub's design decision that
    neither family has a review monopoly — each family critiques the other.
  - **`/experimental on` as a feature delivery gate**: This is the first source in the
    corpus to document GitHub's experimental flag mechanism (`/experimental on`) as the
    delivery gate for preview CLI features. Teams and harness engineers need to know
    this pattern to access new Copilot CLI capabilities before GA.

## Guide Impact

### Chapter 02: Harness Engineering / Daily Tooling

- **Add Rubber Duck as a built-in cross-family review mechanism**: Document that Copilot
  CLI's Rubber Duck feature provides automatic cross-family second opinions when
  `/experimental on` is enabled. Frame it as the productized form of the practitioner
  cross-review pattern from `blog-simonwillison-csrf-multimodel-review.md`. Key
  practitioner note: Rubber Duck is always from the opposite family (Claude critics GPT;
  GPT-5.5 critics Claude) — practitioners cannot configure which model acts as reviewer
  beyond the orchestrator choice.
- **Experimental flag prerequisite**: Any guide reference to Rubber Duck must include the
  `/experimental on` prerequisite. Harness scripts or CI integrations that depend on
  Rubber Duck review must set this flag; omitting it silently loses the review step.
- **Model pairing knowledge**: Practitioners using Claude as their orchestrator should
  know they are paired with GPT-5.5 as reviewer. Given GPT-5.5's known false-completion-
  claim rate (from `blog-thebatch-gpt55-hallucination-kimi-k26.md`), the guide should
  recommend verifying Rubber Duck's assessments rather than treating them as ground truth.

### Chapter 04: Model Selection and Cost Management

- **Rubber Duck as a dual-model cost consideration**: Rubber Duck dispatches two models
  per session. The cost implications (does the reviewer model consume separate premium
  requests?) are not addressed in this source. Recommend practitioners check current
  Copilot pricing docs before relying on Rubber Duck in cost-sensitive automated workflows.
  The guide should note this gap until a cost-impact source is available.

### Chapter 01: Daily Workflows

- **Cross-family review now available without manual setup**: The guide's recommendation
  for cross-vendor review (currently anchored in Willison's manual GPT-5.4 cross-review
  pattern) can now point to Rubber Duck as a lower-friction option for Copilot CLI users.
  The trade-off: Rubber Duck is automatic but opaque (you cannot configure the reviewer
  model); manual cross-review (Willison's pattern) is more work but gives the practitioner
  model selection control and transparency.

## Extraction Notes

1. **Source is very thin by design**: This is an ~200-word product changelog. Five
   substantive claims are extractable; the sixth (design rationale) derives from a
   referenced blog post that was not linked in the fetched changelog text. The referenced
   blog post would be a high-value follow-up source to mine — it likely contains the
   effectiveness rationale and any supporting data for the cross-family review benefit.
2. **Prior GPT reviewer model unnamed**: The changelog says the Claude-session reviewer
   was "upgraded" to GPT-5.5 but does not name what it was previously. The auto pool
   note (Claim 3 in `docs-github-copilot-cli-auto-model-selection.md`) implies GPT-5.4
   was the prior ceiling in the CLI model ecosystem as of April 17 — the most likely
   prior reviewer — but this cannot be confirmed from this source.
3. **GPT-5.5's reviewer-role fitness**: The mismatch between GitHub's "more effective"
   claim for GPT-5.5 and the `blog-thebatch-gpt55-hallucination-kimi-k26.md` safety
   finding is the most substantive gap in this source. The referenced Rubber Duck blog
   post may address this; without it, the "more effective" claim is unverified.
4. **No contradiction to file**: The GPT-5.5 concern above is a potential limitation of
   the feature, not a contradiction with an existing note. The false-completion-claim
   finding from Apollo Research (`blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 3)
   applies to a coding agent completing a task, not a code-review agent assessing work.
   The transfer is plausible but not established — not a contradiction, a gap.
5. **No blog post URL captured**: The referenced "recent blog post" about how Rubber Duck
   combines model families was mentioned but its URL was not present in the changelog text
   as fetched. A separate search for this post would yield a higher-value source.
