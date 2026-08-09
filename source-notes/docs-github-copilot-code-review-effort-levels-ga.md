---
source_url: https://github.blog/changelog/2026-08-07-copilot-code-review-effort-levels-are-generally-available
source_type: docs
title: "Copilot code review effort levels are generally available"
author: GitHub (official changelog)
date_published: 2026-08-07
date_extracted: 2026-08-09
last_checked: 2026-08-09
status: current
confidence_overall: settled
issue: "#2585"
---

# Copilot Code Review Effort Levels Are Generally Available

> GitHub's August 7, 2026 changelog announcing that the Low/Medium review-depth
> tiers introduced in public preview on June 2, 2026 are now generally available
> under the renamed Lite/Balanced labels, and — the substantive new capability —
> that practitioners can now choose an effort level per individual review request,
> on top of the existing admin-controlled organization default and repository
> override. Cross-referenced against the linked "About GitHub Copilot code
> review" documentation page for the full effort-level, model-usage, and
> MCP/skills mechanics that the changelog itself only summarizes.

## Source Context

- **Type**: docs (GitHub official product changelog, August 7, 2026; ~230 words
  across five sections, plus the linked "About GitHub Copilot code review"
  documentation page at `https://docs.github.com/copilot/concepts/agents/code-review`,
  which was followed per the Miner's linked-page-following guidance and provides
  the substantive mechanics behind the changelog's summary claims).
- **Author credibility**: GitHub engineering team announcing a production status
  change (preview → GA) plus new capabilities. Authoritative for the fact that
  these features exist, their names, their configuration paths, and their
  availability. Not authoritative for whether Balanced reviews measurably
  improve defect-catch rates over Lite in a given team's codebase — no
  comparative metrics are given in either the changelog or the linked docs page.
- **Scope**: Covers the effort-level (formerly tier) feature specifically:
  naming migration, per-review selection, organization defaults, repository
  overrides, plan availability, and UI labeling. The linked docs page additionally
  covers model-usage policy (no user-facing model switching), MCP server and
  agent-skill invocation mechanics for code review, and a comparison table of
  `copilot-instructions.md` / path-specific instructions / `AGENTS.md` / skills.
  Neither source states quantified AI-Credit cost multipliers for Balanced vs.
  Lite, nor names the specific higher-reasoning model Balanced routes to.

## Extracted Claims

### Claim 1: Lite and Balanced effort levels for Copilot code review are now generally available, letting users match review depth to a pull request's complexity and risk

- **Evidence**: Opening sentence of the changelog, official GA status announcement.
- **Confidence**: settled (product status change — official changelog)
- **Quote**: "Lite and Balanced effort levels for GitHub Copilot code review are now generally available. They let you match the depth of a review to the complexity and risk of a pull request."
- **Our assessment**: This confirms the transition from public preview (announced
  June 2, 2026 in `docs-github-copilot-code-review-skills-mcp-tier.md`, Claims
  8–11) to GA. The rationale sentence — matching depth to complexity and risk —
  is identical in spirit to the June 2 framing ("Review depth should scale with
  the complexity of the change") but is now stated as a stable, supported
  product surface rather than a preview.

### Claim 2: The prior "Low" and "Medium" designations are renamed to "Lite" and "Balanced," with existing configurations carrying forward automatically under the new names

- **Evidence**: Dedicated changelog section titled "Lite and Balanced replace Low and Medium."
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "The Low and Medium effort levels introduced during public preview are now named Lite and Balanced. If you previously configured an effort level, your configuration automatically carries forward under the new name."
- **Our assessment**: Zero-migration-cost renaming, consistent with the pattern
  this corpus has already documented for other Copilot code review features
  (e.g., existing MCP/skills configurations carrying forward automatically per
  `docs-github-copilot-code-review-skills-mcp-tier.md` Claims 6–7). For any
  guide text that names the tiers "Low" and "Medium" (as the June 2 source note
  does throughout), the correct current names are Lite and Balanced —
  documentation and guide prose should be updated to avoid referencing a name
  GitHub no longer surfaces in the product UI.

### Claim 3: Practitioners can now choose Lite or Balanced for an individual review request, and that choice applies only to that one review, not to the repository or organization default

- **Evidence**: Dedicated changelog section titled "Choose an effort level for each review."
- **Confidence**: settled (new product capability — official changelog)
- **Quote**: "When you request a Copilot code review, choose Lite for routine changes or Balanced for larger, more complex, or sensitive changes. Your choice only applies to that review and doesn't change the repository or organization default."
- **Our assessment**: This is the most consequential new capability in this
  source, and it changes guide-relevant fact from the June 2 note. That note's
  Claim 14 stated: "The setting is admin-controlled per repository, not
  user-controlled per PR — the review depth is a policy decision, not a
  practitioner choice at review time." As of this August 7 GA announcement,
  that is no longer accurate: a practitioner requesting a review can now pick
  the effort level for that specific request, scoped only to that review. This
  is a genuine product capability added between June 2 (preview) and August 7
  (GA) — not two sources disagreeing about the same point in time — so it is
  handled here as an update/supersession under Cross-References rather than as
  a filed contradiction (see Cross-References below and MINER.md §4a's
  "conditioning variable" guidance, which this most closely resembles: the
  claims differ because the product changed, not because the sources disagree).
  For Ch01 (Daily Workflows): review-depth selection is now a practitioner-level
  interaction, not solely a repository-admin policy decision.

### Claim 4: Organization admins can set a default review effort level that applies across all repositories in the organization, via organization settings → Copilot → Copilot code review

- **Evidence**: Dedicated changelog section titled "⚙️ Organization-level defaults."
- **Confidence**: settled (new configuration surface — official changelog)
- **Quote**: "Organization admins can set a default review effort level that applies to all repositories in the organization. Repositories that haven't configured their own effort level inherit the organization default."
- **Quote**: "To configure the default, navigate to your organization settings → Copilot → Copilot code review."
- **Our assessment**: This adds a configuration layer above the repository-level
  setting the June 2 note documented (`repository settings → Copilot → Code
  review → Review effort level`, Claim 14 of that note). The org-level default
  is a fallback: repos without their own configured effort level inherit it,
  implying repo-level configuration (Claim 14's existing path) still exists and
  takes precedence when set. For Ch02 (Harness Engineering) and Ch05 (Team
  Adoption): organizations standardizing review depth across many repositories
  can now set one org-wide default instead of configuring each repository
  individually — relevant for platform teams managing fleets of repos.

### Claim 5: Repository administrators can override the organization's default effort level for a specific repository

- **Evidence**: "Review effort level" section of the linked documentation page,
  `https://docs.github.com/copilot/concepts/agents/code-review#review-effort-level`.
- **Confidence**: settled (stated directly in official GitHub documentation)
- **Quote**: "Organization owners can set a default review effort level for automatic code reviews in their organization. Repository administrators can override the organization default for a specific repository."
- **Our assessment**: This is the docs page confirming and completing the
  hierarchy the changelog only partially describes: org default (Claim 4) →
  repository-level override (this claim, same mechanism as the June 2 note's
  Claim 14 repo-settings path) → per-review practitioner choice (Claim 3). The
  changelog itself never states that repo-level settings continue to exist
  alongside the new org default; the docs page is necessary to confirm the
  three-tier hierarchy is additive rather than replacing repo-level control.
  For Ch02: document all three layers together as a single precedence chain —
  practitioner per-review choice is the most specific and wins for that review;
  absent a per-review choice, repo override applies; absent a repo override,
  the org default applies.

### Claim 6: Lite and Balanced are available on Copilot Pro, Pro+, Max, Business, and Enterprise plans

- **Evidence**: Standalone sentence in the changelog's opening section.
- **Confidence**: settled (plan-availability fact — official changelog)
- **Quote**: "Lite and Balanced are available with Copilot Pro, Pro+, Max, Business, and Enterprise plans."
- **Our assessment**: This list includes "Max," a plan tier absent from the June
  2 preview announcement's availability list ("Pro, Pro+, Business, and
  Enterprise" per that note's Concrete Artifacts section). Copilot Max did not
  exist, or was not yet included, in the June 2 preview's plan scope; by GA in
  August it is included. For Ch05 (Team Adoption / TCO): teams on Copilot Max
  now have effort-level control that was not confirmed available to them at
  preview time — worth flagging as a plan-scope change alongside the Low→Lite
  rename when updating any June-era guide text that lists plan availability.

### Claim 7: Copilot code review now labels which effort level ran, shown in both pull request timeline events and the pull request overview comment

- **Evidence**: Dedicated changelog section titled "See which effort level was used."
- **Confidence**: settled (new UI capability — official changelog)
- **Quote**: "Copilot code review now labels which effort level ran in both timeline events and the pull request overview comment. You can see at a glance whether a review ran at Balanced or Lite, making it easy to track review depth across your repositories."
- **Our assessment**: This closes a visibility gap: under the June 2 preview,
  effort level was a repository setting with no confirmed per-review UI
  indicator. Now that effort level can vary per review (Claim 3), surfacing
  which level actually ran becomes necessary for practitioners and reviewers
  to interpret review depth after the fact — without this labeling, a
  reviewer would have no way to know whether a light or thorough pass produced
  the comments they're looking at. This pairs with the severity-label and
  comment-grouping UX already documented in
  `docs-github-copilot-code-review-comment-ux.md`: that note reduced
  comment-level noise; this labeling adds review-run-level transparency.

### Claim 8: Lite is a "standard review" providing fast, targeted feedback on common issues (bugs, security vulnerabilities, style inconsistencies) and is the default; Balanced routes pull requests to a higher-reasoning model for longer analysis of complex logic, security-sensitive code, and cross-service changes, consuming more AI credits and GitHub Actions minutes than Lite

- **Evidence**: "Review effort level" section of the linked documentation page.
- **Confidence**: settled (product definitions stated in official documentation)
- **Quote**: "Lite: Standard review. Provides fast, targeted feedback on common issues such as bugs, security vulnerabilities, and style inconsistencies (default)."
- **Quote**: "Balanced: Routes pull requests to a higher-reasoning model for longer analysis of complex logic, security-sensitive code, and cross-service changes. Balanced reviews use more AI credits and GitHub Actions minutes than Lite reviews."
- **Quote**: "Use Balanced for security-sensitive code, multi-service pull requests, or repositories with strict quality standards. Use Lite for routine changes where fast feedback is more important than exhaustive analysis."
- **Our assessment**: This is materially more precise than the June 2 note's
  Low/Medium descriptions (which used near-identical complexity/risk language
  but did not explicitly name Lite as the default or state that Balanced costs
  more in both AI credits *and* Actions minutes — the June 2 note's Claim 11
  mentioned only AI Credits, not Actions minutes, for the cost delta). The docs
  page also newly recommends "configuring larger or self-hosted runners" for
  better Balanced-review performance, extending
  `docs-github-copilot-code-review-actions-billing.md`'s runner-configuration
  claims with a effort-level-specific performance recommendation.

### Claim 9: Copilot code review does not support user-selectable model switching; it uses a fixed, purpose-built mix of models, prompts, and system behaviors, and may use models not enabled on an organization's "Models" settings page

- **Evidence**: "Model usage" section of the linked documentation page.
- **Confidence**: settled (product constraint stated in official documentation)
- **Quote**: "Copilot code review is a purpose-built product that uses a carefully tuned mix of models, prompts, and system behaviors to deliver consistent, high-quality feedback across a wide range of codebases. Model switching is not supported, as changing the model is likely to compromise reliability, user experience, and the quality of review comments."
- **Quote**: "Copilot code review may use models that are not enabled on your organization's "Models" settings page. The "Models" settings page only controls Copilot Chat."
- **Our assessment**: This is new to the corpus and clarifies an open question
  the June 2 note flagged in its Extraction Notes ("Higher-reasoning model
  identity not stated... whether this is Claude claude-sonnet-4-6, Claude Opus
  4.8, or another model is not disclosed"). This source still does not name the
  model, but it does establish that effort-level selection (Lite/Balanced) is
  the *only* model-routing lever exposed to users — there is no separate model
  picker for code review the way there is for Copilot chat or Copilot cloud
  agent (see `docs-github-copilot-cca-reasoning-level.md` for CCA's distinct
  reasoning-level model-selection mechanism). For Ch04 (Agents): code review's
  model routing is a two-value effort-level abstraction, not an open model
  choice, distinguishing it architecturally from CCA.

### Claim 10: The GitHub MCP server and Playwright MCP server are enabled by default for Copilot code review, and repository MCP configuration is shared between Copilot cloud agent and code review, with a dedicated repository toggle to disable MCP for code review specifically

- **Evidence**: "MCP servers" subsection of the linked documentation page.
- **Confidence**: settled (product defaults and configuration mechanics stated in official documentation)
- **Quote**: "The GitHub MCP server and Playwright MCP server are enabled by default."
- **Quote**: "In repository settings, Allow Copilot to use MCP tools when reviewing pull requests is enabled by default. Disable this setting if you want MCP servers available only for Copilot cloud agent, and not for Copilot code review."
- **Our assessment**: This extends `docs-github-copilot-code-review-skills-mcp-tier.md`
  Claim 6 (existing CCA MCP configurations automatically apply to code review)
  with two new facts: (1) two specific MCP servers ship enabled by default
  rather than requiring any team configuration at all, and (2) teams that want
  MCP available to CCA but *not* code review now have an explicit toggle to
  achieve that — the June 2 note's "automatically apply" framing implied no
  opt-out; this source shows the opt-out exists. For Ch02: document this
  toggle alongside the shared-configuration claim so teams know MCP-for-CCA
  and MCP-for-code-review can be decoupled if desired.

### Claim 11: During a review, Copilot reads repository custom instructions, agent instructions, and agent skills from the pull request's head branch, not the base branch — allowing changes to those files to be tested within the same pull request before merging

- **Evidence**: "Agent skills" subsection of the linked documentation page.
- **Confidence**: settled (product behavior stated in official documentation)
- **Quote**: "When reviewing a pull request, Copilot reads repository custom instructions, agent instructions, and agent skills from the head branch (the branch with your changes), not the base branch. For example, when merging my-feature-branch into main, Copilot uses the instructions and skills in my-feature-branch, so you can test changes to them in the same pull request without merging them first."
- **Our assessment**: This is novel to the corpus and operationally important:
  no prior source note (including
  `docs-github-copilot-code-review-skills-mcp-tier.md` or
  `docs-github-copilot-code-review-agents-md-ui.md`) documents which branch
  Copilot code review reads its own configuration files from. Head-branch
  reading means a PR that edits `.github/skills/code-review/SKILL.md`,
  `AGENTS.md`, or `.github/copilot-instructions.md` will have that same PR
  reviewed using the *edited* version of those files, not the version on the
  base branch — a self-referential loop teams should be aware of when testing
  review-configuration changes. For Ch02: recommend this as the pattern for
  safely iterating on review configuration — open a PR that both changes the
  skill/instructions file and contains a test diff, and observe whether the
  review behavior changes as expected, before merging.

### Claim 12: Copilot code review can draw on four distinct customization surfaces — `copilot-instructions.md`, path-specific `*.instructions.md`, `AGENTS.md`, and skills — each with a different scope and activation mechanism

- **Evidence**: "Choosing between custom instructions, AGENTS.md, and skills" subsection and its comparison table, in the linked documentation page.
- **Confidence**: settled (product documentation directly comparing the four mechanisms)
- **Quote**: "Copilot code review can draw on several sources of customization, and each serves a different purpose. Use .github/copilot-instructions.md for repository-wide rules specific to Copilot, use path-specific *.instructions.md files under .github/instructions/ for rules that apply only to certain files or directories, use AGENTS.md for standing rules you want to share across AI tools and agents, and use skills for task-specific workflows that Copilot runs on demand."
- **Our assessment**: This is the first corpus source to present all four
  code-review customization surfaces side by side with an explicit decision
  rule for each, closing a gap `docs-github-copilot-code-review-skills-mcp-tier.md`
  left open ("Does NOT cover: how agent skills differ from AGENTS.md or
  CLAUDE.md for code review purposes") and complementing
  `docs-github-copilot-code-review-agents-md-ui.md` (which announced AGENTS.md
  support but did not compare it against the other three surfaces). The table's
  "Rule" row gives a one-line mental model for each: copilot-instructions.md =
  "Copilot, always know this for this repository"; path-specific
  instructions.md = "...when working in these paths"; AGENTS.md = "Any agent,
  always know this"; skills = "Do this when needed." For Ch02: use this table
  verbatim (see Concrete Artifacts) as the canonical customization-surface
  reference, superseding ad hoc surface-by-surface documentation scattered
  across earlier source notes.

## Concrete Artifacts

### Changelog Full Text (verbatim, August 7, 2026)

```
Title: Copilot code review effort levels are generally available
Published: 2026-08-07
Source: https://github.blog/changelog/2026-08-07-copilot-code-review-effort-levels-are-generally-available

Lite and Balanced effort levels for GitHub Copilot code review are now
generally available. They let you match the depth of a review to the
complexity and risk of a pull request.

Not every pull request needs the same scrutiny. Documentation updates and
small fixes may only need focused feedback, while complex logic,
security-sensitive code, and cross-service changes benefit from deeper
analysis. You can now:

  - Choose Lite for feedback on straightforward changes.
  - Choose Balanced when a change warrants deeper analysis from a
    higher-reasoning model.
  - Set an organization-wide default that repositories inherit while
    retaining control over individual reviews.

Lite and Balanced are available with Copilot Pro, Pro+, Max, Business, and
Enterprise plans.

--- SECTION: Lite and Balanced replace Low and Medium ---

The Low and Medium effort levels introduced during public preview are now
named Lite and Balanced. If you previously configured an effort level, your
configuration automatically carries forward under the new name.

--- SECTION: Choose an effort level for each review ---

When you request a Copilot code review, choose Lite for routine changes or
Balanced for larger, more complex, or sensitive changes. Your choice only
applies to that review and doesn't change the repository or organization
default.

--- SECTION: Organization-level defaults ---

Organization admins can set a default review effort level that applies to
all repositories in the organization. Repositories that haven't configured
their own effort level inherit the organization default.

To configure the default, navigate to your organization settings → Copilot
→ Copilot code review.

[Screenshot: "Organization default review effort level setting"]

--- SECTION: See which effort level was used ---

Copilot code review now labels which effort level ran in both timeline
events and the pull request overview comment. You can see at a glance
whether a review ran at Balanced or Lite, making it easy to track review
depth across your repositories.

[Screenshot: "A line of text from the timeline that includes the effort
level as part of the update"]

--- SECTION: Find out more and share your feedback ---

Learn how to tune review depth for your team in the Copilot code review
documentation, and share your feedback in the GitHub community.
```

### Linked Documentation Excerpt: Review Effort Level Section (verbatim)

```
Source: https://docs.github.com/copilot/concepts/agents/code-review#review-effort-level
(followed from the changelog's "Copilot code review documentation" link)

Copilot code review supports multiple review effort levels, so you can
choose the level of thoroughness that matches the criticality of your code.

  - Lite: Standard review. Provides fast, targeted feedback on common
    issues such as bugs, security vulnerabilities, and style
    inconsistencies (default).
  - Balanced: Routes pull requests to a higher-reasoning model for longer
    analysis of complex logic, security-sensitive code, and cross-service
    changes. Balanced reviews use more AI credits and GitHub Actions
    minutes than Lite reviews. For better performance with Balanced
    reviews, consider configuring larger or self-hosted runners.

Use Balanced for security-sensitive code, multi-service pull requests, or
repositories with strict quality standards. Use Lite for routine changes
where fast feedback is more important than exhaustive analysis.

Organization owners can set a default review effort level for automatic
code reviews in their organization. Repository administrators can override
the organization default for a specific repository.

After Copilot code review reviews a pull request, the pull request
overview comment shows the effort level used for each review run.
```

### Linked Documentation Excerpt: Customization Surface Comparison Table (verbatim)

```
Source: https://docs.github.com/copilot/concepts/agents/code-review
Section: "Choosing between custom instructions, AGENTS.md, and skills"

                copilot-instructions.md   Path-specific       AGENTS.md              Skills
                                          *.instructions.md
Best for        Repository-wide,          Always-on rules     Always-on rules        Task-specific
                always-on rules for       for specific        shared across          review
                Copilot                   paths, file types,  AI agents              workflows
                                          or directories
Stored in       .github/                  .github/            Repository root        .github/
                copilot-instructions.md   instructions/       (AGENTS.md)            skills/...
                                          **/*.instructions.md
Examples        Coding standards,         content/** writing  Shared repository      Reviews,
                architecture defaults,    rules, src/**       conventions that       releases,
                test expectations         coding conventions, should apply beyond    migrations,
                                          language-specific   Copilot                analysis
                                          guidance
Activation      Automatic                 Automatic when      Automatic (read        Automatic when
                                          changed files match  from repository        relevant (e.g.
                                          the instruction      root)                  review-focused
                                          scope                                       skills such as
                                                                                       code-review),
                                                                                       or on demand
Scope           Repository-wide and       Repository          Cross-tool /           Invoked per task
                Copilot-specific          sub-paths and        agent-agnostic
                                          Copilot-specific
Rule            "Copilot, always know     "Copilot, always     "Any agent,            "Do this when
                this for this             know this when       always know this"      needed"
                repository"               working in these
                                          paths"
```

### Linked Documentation Excerpt: Model Usage and MCP/Skills Mechanics (verbatim)

```
Source: https://docs.github.com/copilot/concepts/agents/code-review

--- Model usage ---
Copilot code review is a purpose-built product that uses a carefully tuned
mix of models, prompts, and system behaviors to deliver consistent,
high-quality feedback across a wide range of codebases. Model switching is
not supported, as changing the model is likely to compromise reliability,
user experience, and the quality of review comments.

Note: Copilot code review may use models that are not enabled on your
organization's "Models" settings page. The "Models" settings page only
controls Copilot Chat.

--- MCP servers and agent skills for code review ---
Copilot code review can use repository-level agent skills and MCP servers
when they are relevant to the review. Copilot code review is more likely to
use skills and MCP context when your repository or pull request gives clear
signals, including review-focused skill directory names, custom
instructions that reference MCP context, and pull request descriptions that
include identifiers referencing configured MCP servers such as issue keys
or incident IDs.

Agent skills:
"When reviewing a pull request, Copilot reads repository custom
instructions, agent instructions, and agent skills from the head branch
(the branch with your changes), not the base branch. For example, when
merging my-feature-branch into main, Copilot uses the instructions and
skills in my-feature-branch, so you can test changes to them in the same
pull request without merging them first."

MCP servers:
"The GitHub MCP server and Playwright MCP server are enabled by default."
"In repository settings, Allow Copilot to use MCP tools when reviewing
pull requests is enabled by default. Disable this setting if you want MCP
servers available only for Copilot cloud agent, and not for Copilot code
review."
```

### Effort-Level Configuration Hierarchy (compiled from changelog + docs page)

```
Precedence (most specific wins for a given review):

1. Per-review practitioner choice (NEW, GA Aug 7, 2026)
   → Selected when requesting the review; applies to that review only.

2. Repository-level override (existed since June 2, 2026 preview,
   repository settings → Copilot → Code review → Review effort level;
   explicitly confirmed still available as an override at GA per the
   docs page's "Repository administrators can override the organization
   default for a specific repository.")

3. Organization-level default (NEW, GA Aug 7, 2026,
   organization settings → Copilot → Copilot code review)
   → Applied when a repository has not configured its own effort level.

Renaming: Low → Lite, Medium → Balanced (automatic migration, no action
required).

Plan availability at GA: Copilot Pro, Pro+, Max, Business, Enterprise.
(June 2 preview list: Pro, Pro+, Business, Enterprise — no Max.)
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue #1052):
  - This source's Claims 1–2 confirm that the June 2 note's Low/Medium tier
    (Claims 8–11 of that note) has moved from public preview to GA and been
    renamed to Lite/Balanced. Any guide text drawn from that note's Low/Medium
    naming should be updated to Lite/Balanced.
  - This source's Claim 3 (per-review practitioner choice of effort level)
    **updates/supersedes** that note's Claim 14, which stated the setting was
    "admin-controlled per repository, not user-controlled per PR." That
    statement was accurate for the June 2, 2026 preview; it is no longer
    accurate as of this August 7, 2026 GA announcement, which explicitly adds
    per-review selection as a new capability. This is treated as a product
    evolution (Extends), not a filed contradiction: the two source notes are
    both GitHub's own official documentation describing the same feature at
    two different points in its lifecycle, and the newer source explicitly
    frames the change as new ("You can now..."), not as a disagreement about
    present-day behavior. No contradiction issue filed per MINER.md §4a's
    guidance that context/time-conditioned differences are not contradictions.
  - This source's Claim 4–5 (organization default + repository override
    hierarchy) adds a configuration layer above that note's Claim 14
    (repository-level `Review effort level` setting), which remains valid as
    the middle tier of the now three-tier hierarchy documented in the
    "Effort-Level Configuration Hierarchy" artifact above.
  - This source's Claim 10 (GitHub MCP and Playwright MCP servers enabled by
    default; explicit toggle to decouple MCP-for-CCA from MCP-for-code-review)
    extends that note's Claim 6 (existing CCA MCP configurations "automatically
    apply" to code review), which did not mention default-enabled servers or
    an opt-out toggle.
  - This source's Claim 11 (skills/instructions read from head branch, not
    base branch) is genuinely new information not present in that note's
    Claims 7 and 12 (which describe *where* skills are stored but not *which
    branch* they're read from during a review).

- **Extends** `docs-github-copilot-code-review-agents-md-ui.md` (issue #1236):
  - That source announced AGENTS.md support for code review but explicitly
    scoped out comparison against the other customization surfaces ("Does NOT
    cover: how AGENTS.md interacts with or takes precedence over
    `.github/copilot-instructions.md`, SKILL.md files, or MCP server context").
    This source's Claim 12 and the "Customization Surface Comparison Table"
    artifact directly fill that gap with GitHub's own side-by-side comparison
    of all four surfaces, including an explicit "Rule" framing for each.

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue #445):
  - That source established that Copilot code review's agentic architecture
    runs on GitHub Actions and that self-hosted/larger runners are supported.
    This source's Claim 8 adds an effort-level-specific instance of that
    guidance: "For better performance with Balanced reviews, consider
    configuring larger or self-hosted runners" — the first corpus source to
    tie runner sizing recommendations to a specific effort level rather than
    to code review generally.

- **Extends** `docs-github-copilot-cca-reasoning-level.md` (issue not
  re-verified in this note; cited by title only):
  - This source's Claim 9 (code review has no user-facing model switching,
    unlike the effort-level abstraction) is relevant to any guide discussion
    that compares CCA's model/reasoning-level selection against code review's
    effort levels — they are architecturally different controls (CCA:
    model/reasoning choice; code review: a fixed two-value effort abstraction
    with an internal, undisclosed model mapping). This note does not cite a
    specific numbered claim from that source, since verifying its exact claim
    numbering was out of scope for this extraction; the Assayer or Smith
    should confirm claim alignment before using this cross-reference in guide
    prose.

- **Contradicts**: None filed. The one apparent tension (per-review selection
  vs. the June 2 note's "not user-controlled per PR" statement) is a
  time-conditioned product change, not a disagreement between sources — see
  the "Extends" entry above for `docs-github-copilot-code-review-skills-mcp-tier.md`.
  No contradiction issue opened.

- **Novel**:
  - **Per-review, practitioner-level effort-level selection**: First corpus
    source to document that code review depth can be chosen at the moment of
    requesting an individual review, not only set as a standing repository or
    org policy.
  - **Three-tier effort-level precedence (org default → repo override →
    per-review choice)**: First corpus source to document all three layers
    together.
  - **Copilot Max plan inclusion**: First corpus source to list Copilot Max
    among the plans supporting code review effort levels.
  - **Model-switching policy statement**: First corpus source to state
    explicitly that Copilot code review does not support user-selectable model
    switching and may use models outside an organization's "Models" settings
    page scope.
  - **Default-enabled MCP servers (GitHub, Playwright) and the CCA/code-review
    MCP decoupling toggle**: First corpus source to name which MCP servers
    ship enabled by default and to document the toggle for disabling MCP in
    code review specifically while retaining it for CCA.
  - **Head-branch (not base-branch) reading of skills/instructions during
    review**: First corpus source to state which branch's configuration files
    Copilot code review actually reads.
  - **Four-surface customization comparison table**: First corpus source to
    present `copilot-instructions.md`, path-specific `*.instructions.md`,
    `AGENTS.md`, and skills side by side with a single decision framework.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Update the "code review configuration
  surface" material (built up across `docs-github-copilot-code-review-skills-mcp-tier.md`,
  `docs-github-copilot-code-review-config-controls.md`, and
  `docs-github-copilot-code-review-agents-md-ui.md`) with: (1) the Low→Lite,
  Medium→Balanced rename throughout; (2) the three-tier effort-level precedence
  hierarchy (org default → repo override → per-review choice) replacing the
  prior repo-admin-only framing; (3) the four-surface customization comparison
  table (Claim 12 / Concrete Artifacts) as the canonical reference for choosing
  between `copilot-instructions.md`, path-specific instructions, `AGENTS.md`,
  and skills; and (4) the head-branch-reads-configuration behavior (Claim 11)
  as the recommended pattern for safely testing review-configuration changes
  within the same PR that introduces them.
- **Chapter 04 (Agents)**: Add the model-usage policy (Claim 9) to any
  discussion contrasting Copilot code review's model routing with Copilot
  cloud agent's user-selectable reasoning levels — code review exposes only
  a two-value effort abstraction (Lite/Balanced) with no direct model choice,
  while CCA exposes explicit model/reasoning-level selection. This is a
  concrete example of two features from the same vendor taking different
  abstraction-vs-control tradeoffs for model routing.
- **Chapter 05 (Team Adoption)**: Update any code-review adoption checklist
  to note that (1) effort-level configuration is GA, not preview, removing
  preview-stability caveats; (2) Copilot Max plan users now have confirmed
  effort-level access; and (3) practitioners, not only admins, now have a
  review-depth lever available per review — teams rolling out Balanced/Lite
  guidance should train practitioners on when to choose Balanced manually
  (security-sensitive or multi-service changes) rather than relying solely on
  the repository/org default.
- **Chapter 01 (Daily Workflows)**: The practitioner-level interaction model
  changes: a practitioner requesting a Copilot code review can now pick
  Lite or Balanced for that specific request, and can see which effort level
  actually ran via the timeline event and PR overview comment labeling
  (Claim 7). Update any walkthrough of "requesting a Copilot review" to
  include this choice point.

## Extraction Notes

1. **WebFetch summarization avoided for quotes**: An initial WebFetch call
   against the changelog URL returned an AI-summarized version of the page
   (correct in substance but not verified verbatim). All quotes in this note
   were instead sourced from a direct `curl` fetch of the raw changelog HTML
   and the raw HTML of the linked documentation page, with tags stripped and
   HTML entities unescaped programmatically, then cross-checked against the
   page's Open Graph meta description and heading `id` attributes for
   consistency. This is a stronger verification path than the June 2 note's
   Extraction Notes describe (which relied on WebFetch's AI-summarized output).

2. **One linked page followed**: Per MINER.md's instruction to follow
   substantive linked pages, the changelog's link to
   `https://docs.github.com/copilot/concepts/agents/code-review#review-effort-level`
   was fetched and is the source of Claims 5, 8 (partially), 9, 10, 11, and 12.
   The changelog alone would have supported only Claims 1–4, 6, and 7. Other
   links in the changelog ("GitHub community" discussions link, several
   "read the docs" links embedded within the docs page itself such as
   "Configuring automatic code review by GitHub Copilot" and "Configure MCP
   servers for your repository") were not followed — they were assessed as
   procedural how-to pages unlikely to add claims beyond what the conceptual
   docs page already covers, and following all of them would exceed useful
   scope for this extraction.

3. **AI Credit multiplier for Balanced still not quantified**: Consistent with
   the June 2 note's Extraction Notes item 2, neither the changelog nor the
   linked docs page states a specific AI-Credit or Actions-minute multiplier
   for Balanced vs. Lite — only that Balanced "uses more" of both. Teams
   modeling TCO still cannot compute an expected cost delta from official
   sources alone.

4. **Cross-reference to `docs-github-copilot-cca-reasoning-level.md` not
   claim-verified**: This note references that source by title in the
   Cross-References section for architectural contrast (code review's
   effort-level abstraction vs. CCA's model/reasoning-level selection) but
   does not cite a specific numbered claim from it, since re-reading and
   verifying that note's claim numbering was not completed during this
   extraction. Flagged explicitly so the Assayer does not mistake this for a
   verified `Claim N` citation.

5. **No contradiction issue filed**: The one point of apparent tension with
   existing corpus content (per-review effort selection vs. the June 2 note's
   "not user-controlled per PR" statement) was assessed as a time-conditioned
   product change rather than a genuine contradiction between sources, per
   MINER.md §4a. See the Cross-References entry for
   `docs-github-copilot-code-review-skills-mcp-tier.md` for the full reasoning.
