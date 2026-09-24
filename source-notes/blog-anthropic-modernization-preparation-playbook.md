---
source_url: https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects
source_type: blog-post
title: "How to prepare for AI-driven code modernization projects"
author: Jonah Ezekiel and Lexie Tonelli (Anthropic forward deployed engineers, "Notes from the Field" series)
date_published: 2026-09-23
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: emerging
issue: "#3658"
---

# How to prepare for AI-driven code modernization projects

> First-party Anthropic "Notes from the Field" playbook arguing that once
> agents accelerate code production, the bottleneck in enterprise
> modernization shifts from writing changes to mobilizing the organization
> around them — and laying out six pre-work steps (define the target,
> write the certificate, set the promotion policy, stage prerequisites,
> build the agentic workflow, pilot then scale) that regulated enterprises
> should complete before a modernization run starts.

## Source Context

- **Type**: blog-post (official claude.com/blog, "Notes from the Field"
  series; published September 23, 2026; stated 5-minute reading time;
  byline "Author(s): Jonah Ezekiel, Lexie Tonelli," introduced as "Anthropic
  forward deployed engineers" who "share best practices inspired by real
  customer deployments.")
- **Author credibility**: First-party Anthropic publication, written by named
  forward-deployed engineers whose stated role is working directly with
  enterprise customers on production modernization engagements ("Our forward
  deployed engineers work through these steps with customers on their most
  critical systems"). No individual customer, company, or outcome metric is
  named anywhere in the article — unlike `blog-anthropic-code-migration-playbook.md`,
  which names Jarred Sumner and Mike Krieger and gives specific token/cost/
  regression figures for two real migrations, this piece is a generalized
  process framework with no worked case study, no token-cost figures, and no
  named customer. Treat it as prescriptive first-party methodology, not an
  outcomes report.
- **Scope**: Covers the organizational pre-work for a modernization project —
  defining the target (uplift/transform/reimagine), building a certificate of
  correctness, setting a tiered promotion/review policy, staging environment
  and compliance prerequisites, building the agentic workflow, and piloting
  before scaling — plus a closing section on cost/token estimation. Does NOT
  cover: the technical translation mechanics once the workflow is running
  (contrast `blog-anthropic-code-migration-playbook.md`'s six-step
  rulebook→stress-test→translate→compile→run→match-behavior process, which
  this article explicitly treats as a downstream, separate concern — "Build
  and refine the agentic workflow" is one bullet here), any named case study,
  specific dollar or token figures, or model version names beyond generic
  references to "Sonnet" and "more intelligent models."

## Extracted Claims

### Claim 1: Once agents accelerate the production of changes, the organizational bottleneck shifts from producing changes to mobilizing the organization around them, because existing change-management processes were built on the assumption that a human wrote and a human reviewed each diff
- **Evidence**: Stated as the article's opening thesis, following directly
  from an example about mandatory change management on critical banking
  systems.
- **Confidence**: emerging (a first-party framing thesis, asserted as
  reasoning from an example rather than measured in this article)
- **Quote**: "Those processes are what make critical systems trustworthy, and they were built on the assumption that a human wrote each change and a human would review each diff. Once agents accelerate writing the changes, the bottleneck shifts from producing changes to mobilizing the organization around them."
- **Our assessment**: This is the same bottleneck-relocation thesis already
  well-represented in the corpus (see Cross-References → Corroborates), but
  applied specifically to regulated-industry code *modernization* rather than
  the SDLC broadly. It is a direct, concrete instance of the general
  "controls stop matching reality" claim already sourced from
  `blog-anthropic-ai-native-sdlc-playbook.md` Claim 1, narrowed to the
  specific case of change-management processes designed around per-diff
  human authorship.

### Claim 2: Three modernization types are defined by desired end state — uplift (same-stack version bump, e.g. C++11→C++20), transform (cross-stack rewrite with behavior held fixed, e.g. COBOL→Java), and reimagine (greenfield rebuild with modified behavior) — and which type an organization should pursue is often internally contested between risk-averse production stakeholders and stakeholders who want to pay down tech debt or add new requirements
- **Evidence**: A named three-row comparison table (Type / What it is / Choose
  when / The target is) followed by an explicit description of the internal
  disagreement pattern.
- **Confidence**: emerging (a first-party taxonomy and an organizational
  observation, not empirically tested against modernizations that skipped
  this step)
- **Quote**: "In our experience, the people closest to production want the stack swapped with behavior held constant to contain risk (transform modernization). On the other side are often the engineers who have lived with the codebase and want the modernization to pay down tech debt, plus other business stakeholders who want to take the opportunity to name new requirements (reimagine modernization)."
- **Quote**: "Both positions are reasonable, but if the question is left unresolved it resurfaces later as an argument over whether a given change is \"correct.\""
- **Our assessment**: This three-way taxonomy (uplift/transform/reimagine) is
  new, named vocabulary for the corpus's modernization coverage — prior
  sources (`blog-anthropic-code-migration-playbook.md`,
  `blog-thoughtworks-mishra-ai-assisted-migration.md`) describe specific
  migrations without naming a general typology for *what kind* of end state
  is being targeted. The observation that unresolved type-disagreement
  resurfaces later as a dispute over "correctness" is a specific, useful
  early-warning pattern: it argues the certificate (Step 2) cannot be written
  correctly until this disagreement is resolved, since "correct" is defined
  relative to the chosen target type.

### Claim 3: Claude's code modernization plugin can mine business rules with source citations via its assess, map, and extract-rules commands, but discovery from the code alone may not capture how a legacy system fully behaves — interviews with business users and developers, and internal documentation, are needed to fill the gaps
- **Evidence**: Direct product-capability description paired with an explicit
  limitation and named mitigation (human interviews, documentation review).
- **Confidence**: emerging (a first-party product claim about the plugin's
  mining capability, immediately self-qualified with a stated limitation)
- **Quote**: "Claude can do much of that discovery by mapping dependencies and documenting workflows that nobody remembers building. The code modernization plugin's assess, map, and extract-rules commands mine business rules with source citations that engineers can then review."
- **Quote**: "However, Claude's discovery alone may not capture how a legacy system fully behaves. Interviews with business users and developers, and internal documentation, can fill those gaps."
- **Our assessment**: The "source citations that engineers can then review" framing is the same anti-hallucination pattern already documented in the corpus as file:line source traceability
  (`blog-thoughtworks-mishra-ai-assisted-migration.md` Claim 2, which calls
  traceability "the real anti-hallucination mechanism" for legacy-code
  comprehension). This article corroborates that traceable extraction is now
  a named, first-party Anthropic plugin feature (not just a bespoke pattern
  one vendor built), while also explicitly conceding that automated
  discovery is necessarily incomplete for legacy systems — a hedge in the
  same spirit as `blog-thoughtworks-harrison-insurance-legacy-modernization.md`
  Claim 7's "not a push-button exercise."

### Claim 4: Risk reduction, not cost reduction, is described as the most important driver of modernization projects in the authors' experience, and the main challenge in initiating these projects is usually building internal consensus and commitment among the teams that own and depend on the system
- **Evidence**: Direct first-party claim contrasting stated motivations,
  followed by a description of what actually blocks project initiation.
- **Confidence**: emerging (an experience-based generalization from forward
  deployed engineers across customer engagements, not a surveyed or
  quantified finding)
- **Quote**: "Modernizing legacy systems can reduce ongoing maintenance and operational costs, however, in our experience, cost reduction has not been the driving goal of most modernization projects. Risk reduction is often the most important modernization benefit."
- **Quote**: "The main challenge in initiating these projects is usually building the internal consensus and commitment from the teams that own the system, and the teams that depend on it."
- **Our assessment**: This reframes the business case for modernization away
  from a pure ROI/cost-savings pitch and toward risk framing (unpatched
  vulnerabilities, shrinking pool of engineers who understand the system) —
  consistent with, but more specific than,
  `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 2's
  "legacy is increasingly a brake on change" framing, which does not
  explicitly rank risk above cost as the primary driver.

### Claim 5: The certificate is the set of checkable-without-a-human conditions every modernization change must meet, typically drawing from eleven possible sources of evidence including test-suite results, performance benchmarks, adversarial Claude reviews in fresh context windows, computer-use UI regression checks, input/output parity between current and target versions, staging soak time, and static/security scan results
- **Evidence**: A named, itemized list of eleven certificate-condition
  candidates, framed as a menu the workflow can iterate against
  autonomously.
- **Confidence**: emerging (a first-party prescriptive checklist; internally
  coherent but not benchmarked against a certificate missing one or more of
  these conditions)
- **Quote**: "Each condition should be checkable without a human in the loop, so the agentic workflow can iterate on a change until it meets the certificate or flag it for human review if it can't."
- **Quote**: "Independent adversarial reviews by Claude, each in a fresh context window, find no blocking issues"
- **Our assessment**: This is architecturally the same "judge" concept
  already documented in `blog-anthropic-code-migration-playbook.md` Claim 5
  (a judge built once, expensively, then run cheaply and repeatedly), but
  reframed here as a fixed menu of eleven concrete evidence types rather than
  a three-step construction process. It also names "computer-use... finds no
  regressions" as a certificate condition for UI parity, which is new,
  specific detail not present in the prior migration-playbook note's judge
  description.

### Claim 6: A good check on a finished certificate is whether the people who will review and promote changes would be comfortable merging on the certificate's evidence alone — if they see their own bar reflected in it, the promotion policy set in the next step can be lighter
- **Evidence**: Direct prescriptive claim, stated as the validation test for
  the certificate-writing step, tying certificate quality to reviewers'
  eventual review burden.
- **Confidence**: emerging (a specific, actionable heuristic; not tested
  against a certificate that failed this check)
- **Quote**: "A good check on the finished certificate is whether they would be comfortable merging on the certificate's evidence alone. If they see their own bar in it, the promotion policy in Step 3 can be lighter."
- **Our assessment**: This explicitly links certificate quality (Step 2) to
  promotion-policy leniency (Step 3) as a causal, incentive-aligned chain —
  a concrete instance of the "front-load SME hours to earn lighter review
  later" pattern that Claim 8 below states as a general promotion-policy
  rule. It gives teams a specific self-test rather than an abstract quality
  bar.

### Claim 7: What the certificate checks against depends on modernization type — an uplift and a transform both check parity against the original codebase (though a transform relies on traffic replay and differential testing rather than the original test suite), while a reimagine's certificate is anchored in the behavioral spec instead of an existing system, making it the hardest case because model judgment plays a larger role and produces more variable outcomes
- **Evidence**: Direct per-type breakdown of what "correct" means for the
  certificate under each of the three modernization types named in Claim 2.
- **Confidence**: emerging (a first-party taxonomy-to-verification mapping;
  internally consistent, not independently validated against real
  reimagine-type certificates)
- **Quote**: "For a reimagine modernization, the certificate is anchored in the behavioral spec. This is the hardest case. A spec is less objective than an existing system to diff against, so a larger degree of model judgement is involved, which can lead to more variable outcomes."
- **Quote**: "Expect to revise the certificate as the spec is clarified: gaps in the spec show up here first."
- **Our assessment**: This directly extends
  `blog-thoughtworks-mishra-ai-assisted-migration.md` Claim 7's spec-mediated
  generation pattern (code generated from a reviewed spec rather than
  code-to-code translation) by naming the specific risk that pattern
  introduces: a spec is "less objective... to diff against" than an existing
  system, so verification against it is inherently more judgment-dependent
  and variable. The two sources describe complementary halves of the same
  tradeoff — Mishra's note argues spec-mediation surfaces undocumented
  behavior better; this source names the corresponding cost (harder, more
  variable certification).

### Claim 8: The promotion policy is a tiered review path that must be agreed in advance and should tier changes by blast radius and agent confidence, fix recurring review flags at the source (in the workflow or certificate) rather than patching each instance, design the review output format together with reviewers, and allocate scarce SME time to the highest-risk tiers and flagged decisions rather than full diffs
- **Evidence**: Four named rules stated as holding "everywhere" regardless of
  organization-specific risk tolerance, presented as the core of Step 3.
- **Confidence**: emerging (prescriptive rules asserted as universal; not
  tested against an organization that violated one of the four)
- **Quote**: "Fix recurring flags at the source. Group and analyze the flagged changes over time. When the same kind of flag keeps recurring, fix the cause in the agentic workflow or the certificate rather than reviewing each one."
- **Quote**: "Allocate SME time effectively. SMEs won't read every final diff, but their judgment is still the scarce input. Make it easy for them to go straight to the changes in the highest-risk tiers, and to the flagged agent decisions within each one, without wading through large diffs."
- **Our assessment**: The "fix recurring flags at the source" rule is
  architecturally identical to the "fix a recurring mistake once in the
  rulebook, don't patch per-file" pattern already documented in
  `blog-anthropic-code-migration-playbook.md` Claim 9, now applied to human
  review flags at the promotion-policy stage rather than to reviewer
  disagreement during translation — the same "fix the process, not the
  instance" principle recurring at a different pipeline stage.

### Claim 9: The directive for the promotion policy should come from the top of the organization and be agreed before work starts, so that responsibility for a bug reaching production is shared rather than pinned on whoever approved the individual change — because individual approvers otherwise hesitate to sign off on lighter review paths while leadership bears the larger risk of an aging system
- **Evidence**: Direct first-party claim about where promotion-policy
  authority should sit, with an explicit incentive-mismatch rationale.
- **Confidence**: emerging (an organizational-design recommendation stated as
  learned practice, not independently validated against a promotion policy
  set by individual approvers instead)
- **Quote**: "In a regulated environment, taking a lighter human review path for any change can cause real discomfort. Individual approvers hesitate to sign off because they carry the risk of a bad change, while leadership carries the larger risk of an aging system."
- **Quote**: "In our experience, it is best to have the directive for the promotion policy come from the top of the organization. It is also better to agree on it beforehand so responsibility for a bug that reaches production is shared, not pinned on whoever approved the change."
- **Our assessment**: This is a specific governance mechanism for solving a
  named principal-agent problem (individual reviewer risk-aversion vs.
  organizational risk of inaction) — distinct from, but complementary to,
  the "separation of duties" governance principle already sourced from
  `blog-anthropic-ai-native-sdlc-playbook.md` Claim 13 (agents cannot approve
  their own work); this article's concern is about *where accountability for
  the review-depth decision itself* sits, not about who is permitted to
  approve a given diff.

### Claim 10: The promotion policy should reflect where a modernization sits on a speed/review-depth spectrum — a deadline-driven modernization (e.g., a runtime losing support) needs a faster policy with lighter review and an explicit agreement to accept more risk per change, while a modernization on a longer timeline can afford deeper review and a slower cutover
- **Evidence**: Direct first-party claim naming a spectrum and two concrete
  example anchor points.
- **Confidence**: emerging (a framing claim illustrated by one example each
  for the two spectrum ends, not a measured tradeoff curve)
- **Quote**: "A modernization racing to a hard deadline, such as a runtime losing support, needs a faster policy with lighter human review and an explicit agreement to accept more risk per change."
- **Quote**: "A modernization on a longer timeline can afford deeper human review and a slower cutover. Stakeholders will land on different points of this spectrum depending on their risk appetite and constraints so it is worth locking in before the work starts."
- **Our assessment**: This is a concrete decision variable (deadline
  pressure) the guide can use to help teams calibrate promotion-policy
  strictness, complementing Claim 9's "lock it in from the top beforehand"
  governance mechanism — together the two claims argue promotion policy is
  a deliberate, pre-committed organizational decision along two axes
  (authority level, and speed-vs-depth position) rather than something
  negotiated ad hoc per change.

### Claim 11: An uplift modernization done "in place" on a live codebase should be executed by splitting the codebase into logical partitions from the leaves inward, freezing and modernizing one partition at a time, and gating CI/CD so new commits cannot undo a partition once it has been modernized
- **Evidence**: A specific, named execution technique for the case where a
  system cannot be taken down or is changing too fast to keep a separate
  modernized copy in sync, presented in Step 6.
- **Confidence**: emerging (a specific first-party technique described as
  "what we have seen work," implying observed practice across engagements
  but no named case or measured outcome given)
- **Quote**: "What we have seen work in this case is splitting the codebase into logical partitions from the leaves inward; freezing and modernizing one partition at a time; and gating CI/CD so new commits cannot undo a partition once it has been modernized."
- **Our assessment**: This is a specific, actionable technique for the
  "modernizing a live, actively-developed codebase" scenario — a distinct
  concern from `blog-anthropic-code-migration-playbook.md`'s six-step
  process, which describes translating a codebase but does not address how
  to modernize a system that cannot be frozen wholesale during the run.
  "Leaves inward" (i.e., starting with dependency leaves that nothing else
  depends on) is a specific ordering rule worth preserving verbatim.

### Claim 12: The main cost drivers for a modernization are how much of the codebase must be read versus changed, how involved the certificate is (with verification, not writing the change, usually the larger token share in a regulated environment), how much test writing/repair the certificate demands, and how much reconciliation work comes from other teams merging in parallel with the run
- **Evidence**: A named four-item list of cost drivers presented in the
  article's closing "A note on cost" section.
- **Confidence**: emerging (a first-party cost-driver taxonomy without
  supporting token or dollar figures for any specific engagement)
- **Quote**: "How involved the certificate is (verification, not writing the change, is usually the larger share in a regulated environment);"
- **Our assessment**: The claim that verification cost dominates writing cost
  specifically "in a regulated environment" is a notable, checkable
  qualifier — it implies the cost profile would look different for a
  lower-stakes modernization, where writing cost might dominate instead.
  This contrasts with `blog-anthropic-code-migration-playbook.md` Claim 4's
  Bun figures (5.9B input / 690M output tokens for a structure-preserving
  Zig→Rust port with no certificate-heavy regulated-industry constraint),
  though the two sources are not in tension — they describe different cost
  regimes (unregulated structure-preserving port vs. regulated-enterprise
  modernization with a heavy certificate) rather than disagreeing about the
  same regime.

### Claim 13: Cost estimation should come from measuring token usage on a small pilot partition and extrapolating, treating anything the pilot could not observe (such as reconciliation work on a live codebase) as an unknown, which yields a cost floor rather than a full estimate; the same pilot data also shows where to optimize the workflow, and Claude itself can help analyze it
- **Evidence**: Direct prescriptive methodology for cost estimation, closing
  the "A note on cost" section.
- **Confidence**: emerging (a specific, actionable methodology; not
  demonstrated with worked numbers in this article)
- **Quote**: "When completing the modernization on a small part of the codebase, measure token-usage and use that to extrapolate for the rest of the run. Treat anything the pilot couldn't see, such as reconciliation on a live codebase, as an unknown. This way you can get an estimate for the cost floor for the full modernization."
- **Quote**: "If you give Claude access to both the workflow and the pilot data, it can do much of this analysis with you."
- **Our assessment**: "Cost floor, not full estimate" is a useful hedge that
  distinguishes this guidance from a promise of accurate budgeting — it
  explicitly tells readers the pilot-based extrapolation will undercount,
  not overcount, true cost, because it cannot see risks (like live-codebase
  reconciliation) that only appear at scale.

### Claim 14: Teams should avoid using the largest model for every step of the workflow — models like Sonnet suit the mechanical, high-volume work the certificate fully checks, while more intelligent models should be reserved for hard transformations and adversarial reviews that verify correctness; escalating to a more expensive model on certificate failure is reasonable, but retry rates should be analyzed carefully since several cheap attempts can cost more than one expensive one
- **Evidence**: Direct prescriptive model-tiering guidance, with an explicit
  caution about a specific cost trap (cheap-model retry storms).
- **Confidence**: emerging (a first-party cost-optimization heuristic, not
  backed by a comparative cost analysis within this article)
- **Quote**: "Consider using models like Sonnet that balance cost and capability for the mechanical, high-volume work the certificate fully checks. Keep more intelligent models for hard transformations and the adversarial reviews that verify correctness."
- **Quote**: "You can also escalate to a more expensive model when a less expensive one fails to meet the certificate, but analyze retry rates carefully while piloting, since several cheap attempts can cost more than one expensive one."
- **Our assessment**: This corroborates the model-tier rule already sourced
  from `blog-anthropic-code-migration-playbook.md` Claim 11 (smaller models
  for high-volume implementation fan-out, largest model reserved for
  reviewers and rule-authors), applied here specifically to
  certificate-driven modernization, and adds a new, concrete caution not
  present in that prior note: the retry-storm cost trap, where escalation
  policy itself needs cost analysis, not just a fixed cheap-then-expensive
  fallback rule.

### Claim 15: The modernized codebase is only one output of a modernization project — the others are the agentic workflow itself, the written certificate, the promotion policy now accepted into the organization's change-management process, and a full evidence trail for every change, and these should be codified as a reusable playbook asset for the next modernization
- **Evidence**: Direct closing claim in the "Beyond the modernization"
  section, naming four durable artifacts beyond the code itself.
- **Confidence**: emerging (a first-party closing framing claim, not
  independently measured)
- **Quote**: "The modernized codebase is one output. The others are the workflow that produced it, a written certificate for what counts as correct, a promotion policy your change-management process has already accepted, and an evidence trail for every change that landed. Codify the playbook as a reusable asset, so the pattern is already in place for the next upgrade or rewrite."
- **Our assessment**: This reframes a single modernization project as an
  investment in reusable organizational infrastructure (certificate template,
  promotion-policy precedent, workflow) rather than a one-off deliverable —
  directly consistent with
  `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 2's
  "modernization is a continuous balancing act... not a one-time fix"
  framing, now applied specifically to what a single modernization *project*
  should leave behind for the next one, rather than to an organization's
  overall modernization posture.

## Concrete Artifacts

### Six-step process (as named and ordered in source)

```
Source: https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects

- Define the target: the tech stack and behavior the modernized code must have.
- Create the certificate: the conditions that the changes must meet to be considered correct in the target state.
- Set the promotion policy: the path by which certified changes get into production at the rate they're produced.
- Put the prerequisites in place: environment, CI/CD, review capacity, and approvals.
- Build and refine the agentic workflow: the custom Claude Code dynamic workflow that distributes the modernization across many smaller parallel subagent workstreams that produce the changes. This is built around the target, certificate, and promotion policy.
- Run the modernization: prove the workflow end to end on a small partition of the codebase, then scale.
```

### Modernization type table (verbatim structure)

```
Source: same article, "Determine the modernization type"

Uplift    | Same-stack version bump (e.g., C++11 -> C++20) | Choose when: the stack is fine but the version has fallen behind (EOL runtimes, unpatched security issues, dependencies you can't upgrade) | Target: a runtime version and package set
Transform | Cross-stack rewrite that keeps behavior fixed (e.g., COBOL -> Java) | Choose when: the stack is the problem to resolve and the behavior is trusted | Target: everything an uplift needs, plus the language, frameworks, and architectural conventions the new code must follow
Reimagine | Greenfield rebuild on a new architecture with modified behavior | Choose when: the behavior needs to be changed alongside the code | Target: everything a transform needs, plus a written behavioral spec for the new system
```

### Certificate conditions (verbatim list)

```
Source: same article, Step 2

- The original test suite passes
- Claude-authored tests written during the modernization all pass
- Test coverage meets an agreed threshold
- Performance benchmarks stay within an agreed bound
- Independent adversarial reviews by Claude, each in a fresh context window, find no blocking issues
- For user interfaces, Claude-driven computer use finds no regressions
- Current and target versions produce the same output from the same input, which can be live, recorded, or Claude-generated
- Persisted state and wire formats round-trip between current and target versions
- Changes run in staging for an agreed period with no regressions in error rates, latency, or alerts
- Static analysis and security scans show no new findings
- For compiled targets, the build is clean and type checks pass
```

### Promotion policy rules (verbatim list)

```
Source: same article, Step 3

- Tier changes by blast radius and agent confidence. Use your organization's own change or risk classification if it has one. Keep full human review for critical paths.
- Fix recurring flags at the source. Group and analyze the flagged changes over time. When the same kind of flag keeps recurring, fix the cause in the agentic workflow or the certificate rather than reviewing each one.
- Design the output format with the reviewers. Agree on what information and format make review the fastest, and what signals give more confidence than others. Have them review early sample outputs in Step 5.
- Allocate SME time effectively. SMEs won't read every final diff, but their judgment is still the scarce input. Make it easy for them to go straight to the changes in the highest-risk tiers, and to the flagged agent decisions within each one, without wading through large diffs. A small number of expert hours then covers the changes that carry the most risk.
```

### Prerequisites checklist (verbatim, by category)

```
Source: same article, Step 4

Environment:
- A dedicated remote host for running the workflow with the codebase and other relevant sources reachable by Claude
- Test capacity as required by the certificate
- Anything that strengthens the certificate: production telemetry, a prod-parallel setup, or production data for replay

Codebase and CI/CD:
- A dependency map of the codebase, grounded in build and compile logs; import analysis; or runtime traces
- Planned treatment of any dependencies or packages, as part of the target definition
- A compatibility check ready to add to CI/CD, if needed
- An agreed code-freeze policy, if you are modernizing in place
- A communication plan for active developers covering any code freezes and new compatibility requirements

Teams and review:
- Agreement from other teams that depend on the codebase on how they take part, like signing off on the certificate or reviewing under the promotion policy, with reviewer time set aside

Security and compliance:
- A model access path for Claude Code approved for source code
- Least-privilege access for the agentic workflow: write only to modernization branches and no production credentials
- Secrets and PII scrubbed or masked from the modernization branch
- Every change traceable and PR linked to an agent transcript and certificate evidence
- License and vulnerability checks on new dependencies
```

### Cost drivers and mitigation (verbatim)

```
Source: same article, "A note on cost"

Main cost drivers:
- How much of the codebase has to be read versus changed
- How involved the certificate is (verification, not writing the change, is usually the larger share in a regulated environment)
- How much new test writing and test repair the certificate demands
- How much reconciliation work comes from other teams merging around you while the run is in progress

Mitigation: measure token usage on a small pilot, extrapolate for a cost
floor, treat unobserved risks (e.g. live-codebase reconciliation) as
unknown; use pilot data to find and optimize the most token-heavy workflow
steps; move compute-heavy verification signals behind cheaper gates; use
Sonnet-class models for mechanical high-volume work, reserve larger models
for hard transformations and adversarial review; escalate model tier on
certificate failure but watch retry rates.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-ai-native-sdlc-playbook.md` Claim 1 (once code stops
    being the bottleneck, the constraint moves to the human-speed stages
    around it — plan, review/test, deploy — and "controls stop matching
    reality" because per-line review can't keep pace with agent-authored
    diffs): this source's Claim 1 restates the identical bottleneck-shift
    thesis, narrowed specifically to regulated code-modernization change
    management, giving a concrete domain instance (mandatory review on
    critical banking systems) of the same abstract mechanism.
  - `blog-anthropic-code-migration-playbook.md` Claim 5 (a "judge" must be
    built and validated once, expensively, then run cheaply and repeatedly)
    and Claim 9 (a rulebook "keeps growing" so a recurring mistake is fixed
    once and inherited by all future batches, not patched per-file): this
    source's Claim 5 (the eleven-item certificate menu) is architecturally
    the same judge concept, and Claim 8's "fix recurring flags at the
    source... rather than reviewing each one" restates the identical
    fix-the-process-not-the-instance principle, now applied to human review
    flags at the promotion-policy stage.
  - `blog-anthropic-code-migration-playbook.md` Claim 11 (don't use the
    largest model for everything; smaller models handle high-volume
    implementation fan-out, largest model reserved for reviewers and
    rule-authors): this source's Claim 14 restates the same model-tiering
    rule for certificate-driven modernization work, and adds a specific new
    caution (analyze retry rates, since cheap-model retry storms can cost
    more than one expensive-model attempt) not present in that prior note.
  - `blog-thoughtworks-mishra-ai-assisted-migration.md` Claim 2 (file:line
    source traceability is "the real anti-hallucination mechanism" for
    legacy-code comprehension) and Claim 1 (green/amber/red confidence
    markers formalized to prevent AI from inventing things about ambiguous
    legacy code): this source's Claim 3 describes a first-party Anthropic
    product feature (the code modernization plugin's assess/map/extract-rules
    commands) that mines business rules "with source citations that
    engineers can then review" — the same traceability-as-guardrail pattern,
    now confirmed as a shipped Anthropic tool rather than a bespoke
    vendor-built mechanism.
  - `blog-thoughtworks-harrison-insurance-legacy-modernization.md` Claim 7
    (AI reduces the cost of understanding a legacy estate, "not by removing
    the hard work, and not by turning modernization into a push-button
    exercise"): this source's Claim 3 makes the same hedge in miniature —
    Claude's automated discovery "may not capture how a legacy system fully
    behaves," requiring human interviews and documentation to fill gaps.
  - `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 2
    ("modernization is a continuous balancing act between efficiency,
    control and agility," not a one-time fix): this source's Claim 15
    (codify the workflow, certificate, promotion policy, and evidence trail
    as a reusable playbook asset for the next modernization) applies the
    same "not a one-time fix" framing at the level of a single project's
    durable outputs, rather than an organization's overall modernization
    posture.

- **Contradicts**: None identified. This source's claim that certificate
  verification is "usually the larger share" of token cost "in a regulated
  environment" (Claim 12) sits in a different cost regime than
  `blog-anthropic-code-migration-playbook.md`'s Bun figures (Claim 4: 5.9B
  input / 690M output tokens dominated by translation across ~1,448 files,
  with no regulated-industry certificate described) — the two sources
  describe different kinds of engagements (unregulated structure-preserving
  port vs. regulated-enterprise modernization with a heavy certificate)
  rather than disagreeing about where token cost concentrates within the
  same kind of engagement. Not filed as a contradiction per MINER.md §4a.

- **Extends**:
  - `blog-anthropic-code-migration-playbook.md`: that source's six-step
    process (rulebook/dependency-map/gap-inventory → stress-test → translate
    → compile → run → match-behavior) describes the technical translation
    loop itself; this source is the layer above it — the organizational
    pre-work (target definition, certificate, promotion policy, prerequisites)
    that must exist before that translation loop is built. This source
    explicitly treats "build and refine the agentic workflow" (its Step 5)
    as a single downstream step, presupposing the more detailed six-step
    translation methodology the companion note documents.
  - `blog-thoughtworks-mishra-ai-assisted-migration.md` Claim 7 (code
    generated directly from a reviewed spec, not from code-to-code
    translation, for a "reimagine"-style migration): this source's Claim 7
    names the specific cost of that pattern — a spec-anchored certificate is
    "the hardest case" because "a spec is less objective... to diff against"
    than an existing system, making outcomes more variable. Read together,
    the two sources describe the benefit (surfaces undocumented behavior)
    and the corresponding certification cost (harder, more variable
    verification) of the same architectural choice.
  - `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 4
    (public agencies must optimize simultaneously for speed, trust,
    transparency, auditability, resilience, accessibility, compliance, and
    fairness, unlike private companies which can prioritize speed alone):
    this source's promotion-policy speed/review-depth spectrum (Claim 10)
    and its "directive from the top, agreed beforehand" governance mechanism
    (Claim 9) give a concrete operational answer, specific to code
    modernization, for how a regulated organization actually navigates that
    multi-objective tradeoff rather than just naming that the tradeoff
    exists.

- **Novel**:
  - **The uplift/transform/reimagine modernization-type taxonomy** (Claim 2),
    with its explicit mapping of each type to what the certificate must
    check against (Claim 7) — no prior corpus source names a general
    three-way typology for modernization end states.
  - **The certificate-as-eleven-item-menu** (Claim 5) and the
    "would reviewers be comfortable merging on this evidence alone"
    self-test (Claim 6) as a specific validation heuristic for a finished
    certificate.
  - **The "directive for the promotion policy should come from the top,
    agreed beforehand, so blame for a production bug is shared" governance
    mechanism** (Claim 9) — a specific principal-agent-problem framing for
    why promotion-policy authority should sit with leadership rather than
    individual approvers, not present elsewhere in the corpus's governance
    coverage.
  - **The leaves-inward, partition-freeze-and-gate technique for modernizing
    a live, actively-developed codebase in place** (Claim 11) — a concrete
    execution pattern for the specific case where a system cannot be taken
    down or copied for a separate modernized build.
  - **The retry-rate cost trap for model-tier escalation** (Claim 14) —
    "several cheap attempts can cost more than one expensive one" is a
    specific, named caution not present in the corpus's existing model-tiering
    guidance.
  - **Named token-cost drivers specific to a regulated-enterprise
    modernization** (Claim 12), particularly the claim that certificate
    verification cost usually exceeds change-writing cost in that context —
    a specific regime distinct from the corpus's existing Bun/Krieger
    migration cost figures, which come from unregulated, structure-preserving
    or redesign-style ports.

## Guide Impact

- **Chapter 05 (Large-Scale Refactoring and Modernization)**: Add the
  uplift/transform/reimagine typology (Claim 2) as a named vocabulary for
  scoping a modernization's target before any technical work starts, with
  the explicit warning that leaving the type undecided resurfaces later as
  a "correctness" dispute. Pair with Claim 7's per-type certificate mapping
  (parity against the original codebase for uplift/transform; anchored in a
  written behavioral spec, with higher variability, for reimagine) so the
  guide's existing six-step migration process
  (`blog-anthropic-code-migration-playbook.md`) is framed as what happens
  *after* this target-definition step, not as a self-contained starting
  point. Add the eleven-item certificate menu (Claim 5) as a concrete
  checklist alongside the existing "judge" construction guidance.
- **Chapter 05**: Add the four promotion-policy rules (Claim 8) and the
  "directive comes from the top, agreed beforehand" governance mechanism
  (Claim 9) as specific, actionable guidance for regulated-industry
  modernization review design, together with the speed/review-depth
  spectrum (Claim 10) as a way to calibrate policy strictness against
  deadline pressure.
- **Chapter 05**: Add the leaves-inward partition/freeze/gate technique
  (Claim 11) as a concrete pattern for modernizing a live codebase in place
  when a separate modernized copy isn't feasible.
- **Chapter 02 (Harness Engineering) / Chapter 05**: Add the cost-estimation
  methodology (Claim 13: pilot-measure, extrapolate to a cost floor, treat
  unobserved risk as unknown) and the model-tiering-with-retry-rate-caution
  guidance (Claim 14) as budgeting guidance specific to agentic modernization
  projects, alongside the existing Bun/Krieger token-cost data points from
  `blog-anthropic-code-migration-playbook.md` — note explicitly that
  regulated-enterprise certificate-verification cost (this source) and
  unregulated structure-preserving translation cost (Bun) are different cost
  regimes, not comparable figures.
- **Chapter 05**: Add Claim 15's "the codebase is one output; the workflow,
  certificate, promotion policy, and evidence trail are the others" framing
  as guidance for treating a modernization project as reusable organizational
  infrastructure, not a one-off deliverable.

## Extraction Notes

- **Access method**: WebFetch against the source URL returned only a
  condensed AI-generated summary (six bullet points and a short "critical
  insights" paragraph), not verbatim source text, consistent with the same
  limitation documented in several existing notes'
  (`blog-anthropic-code-migration-playbook.md`,
  `blog-anthropic-ai-native-sdlc-playbook.md`) Extraction Notes. To satisfy
  MINER.md §2a, the raw HTML was fetched directly via `curl` with a browser
  user agent (200 response, ~561KB, confirmed server-rendered), converted to
  plain text with a Python `html.parser`-based script that preserved
  paragraph/heading/list-item boundaries, and every quote in this note was
  copied character-for-character from that raw-text extraction.
- **Full article read**: The entire article body was read in full via the
  raw-text extraction, from the opening "Notes from the Field" framing
  through all six numbered steps, the "A note on cost" section, and the
  closing "Beyond the modernization" section and "Additional resources"
  list. No sub-pages were followed: the "Additional resources" section links
  to "The public codemod plugin for Claude Code," "The AI-Native SDLC
  playbook" (already mined as `blog-anthropic-ai-native-sdlc-playbook.md`),
  "Code modernization playbook," and "COBOL Modernization with AI: Breaking
  the Cost Barrier" — the latter two are candidate leads for future source
  notes but were not fetched here, as they are separate, substantial
  articles rather than supporting detail for this one.
- **No contradiction issue filed**: evaluated the certificate-verification-
  dominates-cost claim (Claim 12) against
  `blog-anthropic-code-migration-playbook.md`'s Bun token figures and judged
  it a difference in engagement type (regulated vs. unregulated, certificate-
  heavy vs. translation-heavy), not a claim-level disagreement — see
  Cross-References → Contradicts.
- **Confidence calibration**: rated `emerging` overall. The article is
  first-party Anthropic guidance from named forward-deployed engineers with
  a specific, detailed prescriptive framework, but contains no named
  customer case study, no token/dollar figures, and no measured before/after
  outcome anywhere in the piece — every claim is framed as "in our
  experience" or "what we have seen work" rather than a reported metric.
  This is a materially thinner evidentiary basis than
  `blog-anthropic-code-migration-playbook.md`, which names two practitioners
  and gives specific, cross-corroborated token and outcome figures for two
  real migrations.
