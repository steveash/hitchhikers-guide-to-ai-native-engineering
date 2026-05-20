---
source_url: https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent
source_type: docs
title: "One-click fixes for failing Actions with Copilot cloud agent"
author: GitHub (official changelog)
date_published: 2026-05-18
date_extracted: 2026-05-20
last_checked: 2026-05-20
status: current
confidence_overall: settled
issue: "#819"
---

# One-Click Fixes for Failing Actions with Copilot Cloud Agent

> GitHub's May 18, 2026 changelog announcing that Copilot Business and Enterprise
> subscribers can trigger Copilot cloud agent to diagnose and fix failing GitHub
> Actions jobs directly from workflow run logs — introducing a new UI entry point
> for CCA invocation that is failure-specific and pull-request-branch-scoped,
> targeting routine failures like test and linter errors, and requiring prior admin
> enablement of Copilot cloud agent.

## Source Context

- **Type**: docs (GitHub official product changelog, ~100 words, May 18, 2026; three
  linked documentation pages also examined: "Starting GitHub Copilot sessions,"
  "Enabling Copilot cloud agent," and "About Copilot cloud agent")
- **Author credibility**: GitHub engineering team announcing a production feature.
  Authoritative for the feature's existence, the invocation mechanism, the subscription
  tier requirements, the admin enablement prerequisite, and the stated use cases
  (test fixes, linter corrections). Not a credible source for: which specific failure
  types CCA can reliably fix, success rates, failure modes, or how CCA behaves on
  custom or complex Actions workflows. The source is deliberately brief; linked
  documentation provides the step-by-step procedure and a limited constraint list.
- **Scope**: The announcement covers: the existence of the "Fix with Copilot" button,
  where it appears (workflow run logs page), what CCA does when clicked (investigate,
  push a fix, tag for review), the intended task scope (simple, time-consuming work),
  and the admin prerequisite. Does NOT cover: which failure types CCA can handle vs.
  those it will decline, success rates, whether CCA leaves comments on failures it
  cannot fix, billing implications of using CCA for workflow fixes, interaction with
  branch protection rules in the context of push-to-branch, or behavior on scheduled
  or non-PR-branch workflow runs.

## Extracted Claims

### Claim 1: Copilot Business and Enterprise subscribers can now ask Copilot cloud agent to fix a failing GitHub Actions job in one click from the workflow run logs page

- **Evidence**: Official GitHub product changelog announcing the feature as shipped
  (not preview). The "now" and present-tense framing indicate this is a GA release,
  not a public preview. Copilot Business and Enterprise access restriction is stated
  explicitly.
- **Confidence**: settled (feature announced as live in official product changelog)
- **Quote**: "When a GitHub Actions job fails, Copilot Business and Copilot Enterprise
  subscribers can now ask Copilot cloud agent to fix it in one click."
- **Our assessment**: This is the core announcement. The invocation mechanism — a
  button on the workflow run logs page — is a new CCA trigger distinct from all
  previously documented paths (issue assignment, Agents tab, @copilot in PR, REST
  API). The one-click framing positions this as a developer ergonomics feature, not
  just a technical capability expansion. For Ch02 (Harness Engineering): document
  this as a fifth CCA invocation path, conditioned on a workflow failure event rather
  than a human-initiated task. Cross-reference: `docs-github-copilot-cca-startup-custom-images.md`
  Claim 4 enumerates three UI-based invocation paths (issue assign, Agents tab, @copilot
  in PR); `docs-github-copilot-cca-rest-api-tasks.md` adds the REST API as a fourth path.
  The "Fix with Copilot" button is a fifth, event-triggered UI path not covered in any
  prior source note.

### Claim 2: Clicking "Fix with Copilot" causes CCA to investigate the failure, push a fix to the branch, and tag the user for review — all from its cloud-based development environment

- **Evidence**: Feature behavior described verbatim in the changelog. This is the
  complete stated behavior of the feature — investigate, fix, notify.
- **Confidence**: settled (first-party description of intended feature behavior)
- **Quote**: "Click the Fix with Copilot button on the workflow run logs page, and
  Copilot will investigate the failure, push a fix to your branch, and tag you for
  review when it's done. It does all this from its own cloud-based development
  environment."
- **Our assessment**: The three-step behavior (investigate → fix → tag for review) is
  consistent with CCA's general asynchronous execution model: the agent works in the
  background and surfaces a result for human review rather than requiring synchronous
  human involvement. The explicit "tag you for review" step means CCA does not merge
  its own fix — human review remains in the loop. The "cloud-based development
  environment" framing is consistent with the general CCA execution model documented
  in `docs-github-copilot-cca-rest-api-tasks.md` Claim 2. For Ch03 (Safety and
  Verification): the mandatory human review step is a structural safety gate —
  CCA cannot auto-merge its own workflow fixes without human approval.

### Claim 3: The feature is explicitly scoped to "simple but time-consuming" failures, with fixing tests and correcting linter failures given as the canonical examples

- **Evidence**: The changelog provides two explicit examples and uses the phrase "simple
  but time-consuming work" to characterize the intended use case.
- **Confidence**: settled (the scope characterization and examples are stated explicitly
  in the official announcement)
- **Quote**: "This means you can hand off simple but time-consuming work to Copilot
  (e.g., fixing tests or correcting linter failures) and stay focused on what you
  actually want to build."
- **Our assessment**: "Simple but time-consuming" is the vendor's self-characterization
  of the feature's sweet spot. The phrase is significant: GitHub is not claiming CCA
  can fix any failing Actions job, only those in the "simple" category. The two examples
  (test failures, linter failures) share a key property: they are deterministic and
  verifiable — a fixed test either passes or it doesn't; a linter either succeeds or
  it doesn't. Complex failures (logic errors, infrastructure failures, dependency
  conflicts, flaky tests) are conspicuously absent from the examples. For Ch02: when
  recommending this feature, practitioners should set expectations accordingly — it
  is most reliable for mechanical failures (formatting, type errors, straightforward
  test assertions) and less reliable for semantic or infrastructural failures. The
  changelog provides no data on what fraction of real-world Actions failures fall into
  the "simple" category.

### Claim 4: The feature triggers specifically on workflow run failures on pull request branches, accessed from the workflow run job page

- **Evidence**: The linked "Starting GitHub Copilot sessions" documentation specifies
  the trigger condition and entry point for this feature. This is more precise than
  the changelog itself, which says "when a GitHub Actions job fails" without specifying
  branch scope.
- **Confidence**: settled (linked product documentation page, accessed May 20, 2026)
- **Quote**: "When an GitHub Actions workflow run fails on a pull request branch"
  (from the linked "Starting GitHub Copilot sessions" documentation)
- **Our assessment**: The "pull request branch" qualifier is important — it means this
  feature is scoped to branch-based workflow failures associated with open pull requests,
  not all Actions workflow failures (e.g., scheduled workflows, main-branch push
  workflows). This is architecturally consistent: CCA needs a branch to push a fix to,
  and a PR to tag for review. A scheduled workflow that fails on the default branch
  would have no PR context and no clear branch to fix on. For Ch02: when documenting
  this feature, practitioners should specify the PR-branch constraint — teams expecting
  to use it for scheduled or post-merge workflow failures will be disappointed.

### Claim 5: Copilot cloud agent must be enabled by an organization administrator before users can access the workflow-fix feature

- **Evidence**: Explicit prerequisite stated in the changelog and in the linked enterprise
  enablement documentation. The enterprise docs confirm CCA is disabled by default.
- **Confidence**: settled (stated in both the changelog and the linked official docs)
- **Quote (changelog)**: "If your organization hasn't enabled Copilot cloud agent yet,
  an administrator will need to turn it on before you can start delegating to Copilot."
- **Quote (enterprise enablement docs)**: "Copilot cloud agent and use of third-party
  MCP servers are disabled by default."
- **Our assessment**: The admin-enablement gate means this feature is not self-service
  for individual developers. A Copilot Business or Enterprise subscriber who sees a
  failing Actions job cannot use "Fix with Copilot" unless their organization admin
  has already enabled CCA. For enterprise teams: this creates a clear prerequisite
  sequence — (1) enterprise admin enables CCA for the organization, (2) developers
  can access the "Fix with Copilot" button. The enterprise docs also establish that
  admins can enable CCA selectively per organization and that org owners can further
  disable it per repository — so the enablement state is multilevel. Cross-reference:
  `docs-github-copilot-cca-custom-properties.md` documents the enterprise admin control
  surface for CCA enablement in more detail.

### Claim 6: The linked documentation specifies a two-step user procedure for the feature

- **Evidence**: The linked "Starting GitHub Copilot sessions" documentation describes
  the end-user flow concisely.
- **Confidence**: settled (linked product documentation, accessed May 20, 2026)
- **Quote**: Step 1: "On GitHub, navigate to the failing workflow run job page."
  Step 2: "Click the Fix with Copilot button."
- **Our assessment**: The simplicity of the two-step procedure is consistent with the
  "one click" framing in the changelog headline and body. The user's role is minimal:
  navigate to the failure, click the button. Everything else is delegated to CCA.
  This is operationally important for setting expectations: the feature provides no
  UI affordance for specifying the fix approach, constraining the scope of changes,
  or excluding files — CCA acts on the full repository context with the failure as
  its only input.

### Claim 7: CCA operates in an ephemeral cloud development environment powered by GitHub Actions, where it can explore code, make changes, and execute tests and linters

- **Evidence**: The linked "About Copilot cloud agent" documentation describes the
  execution environment for all CCA tasks.
- **Confidence**: settled (product documentation describing the execution model)
- **Quote**: "its own ephemeral development environment, powered by GitHub Actions,
  where it can explore your code, make changes, execute automated tests and linters"
  (from the linked "About Copilot cloud agent" documentation)
- **Our assessment**: The ephemeral execution environment model applies to the workflow-fix
  feature just as it applies to other CCA task types. Critically, CCA can run the failing
  tests and linters itself as part of its fix cycle — it does not merely apply a static
  fix and hope. The "execute automated tests and linters" capability means CCA can
  verify its own fix before pushing it to the branch, completing an internal fix →
  verify → push loop. For Ch03: this self-verification capability is architecturally
  significant — CCA is not just generating a fix and pushing it blindly; it can run
  the same tests/linters that originally failed to confirm the fix works before tagging
  the developer for review.

### Claim 8: CCA has structural constraints that apply to workflow-fix tasks: one branch at a time, one pull request per task, and GitHub-only repositories

- **Evidence**: The linked "About Copilot cloud agent" documentation explicitly enumerates
  these constraints. They apply to all CCA task types, including the new workflow-fix
  feature.
- **Confidence**: settled (product documentation explicitly listing constraints)
- **Quote**: "Copilot can only work on one branch at a time and can open exactly one
  pull request" (from the linked "About Copilot cloud agent" documentation)
- **Our assessment**: These constraints are relevant context for teams designing workflows
  around the "Fix with Copilot" feature. In particular: if two developers each click
  "Fix with Copilot" on different failures in the same PR, it is unclear whether CCA
  would run them as sequential tasks or whether one would block the other — the
  changelog provides no guidance on concurrent CCA invocations for the same branch.
  The GitHub-only constraint means teams using self-hosted Git platforms (GitLab,
  Bitbucket) cannot use this feature regardless of their Copilot subscription status.
  For Ch02: document these as non-negotiable constraints, not design choices.

### Claim 9: The value proposition is developer attention reallocation — delegating routine CI-repair work to CCA so developers can focus on feature development

- **Evidence**: Explicit framing in the changelog announcement.
- **Confidence**: settled (stated intent/framing in official announcement; no usage data
  on whether developers actually change their behavior)
- **Quote**: "stay focused on what you actually want to build"
- **Our assessment**: The framing is aspirational: the feature is positioned as a
  developer attention tool, not just a CI tool. The implicit claim is that failing
  Actions on pull request branches consume developer attention that could otherwise
  go toward building. Whether developers actually achieve this reallocation depends on
  the feature's reliability — if CCA's fix introduces new failures or requires
  significant review effort, the attention savings evaporate. The changelog provides
  no evidence on how often CCA successfully resolves failures with minimal review
  burden. For Ch01 (Daily Workflows): present this as a pattern for routine CI
  failures, not a universal CI-repair tool. The pattern value is highest when CCA's
  fix is correct and the review is trivial (green CI, clear diff, straightforward
  change) — practitioners should set this expectation explicitly rather than treating
  it as a fully autonomous repair loop.

## Concrete Artifacts

### Verbatim Text of Source Changelog (May 18, 2026)

```
Title: One-click fixes for failing Actions with Copilot cloud agent

When a GitHub Actions job fails, Copilot Business and Copilot Enterprise subscribers
can now ask Copilot cloud agent to fix it in one click.

Click the Fix with Copilot button on the workflow run logs page, and Copilot will
investigate the failure, push a fix to your branch, and tag you for review when it's
done. It does all this from its own cloud-based development environment.

This means you can hand off simple but time-consuming work to Copilot (e.g., fixing
tests or correcting linter failures) and stay focused on what you actually want to
build.

If your organization hasn't enabled Copilot cloud agent yet, an administrator will
need to turn it on before you can start delegating to Copilot. To learn more, see
our documentation about enabling cloud agent.

To learn more, see 'Starting GitHub Copilot sessions' in the GitHub docs.
```

Source: https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent
Retrieved: 2026-05-20 via WebFetch (two independent fetches; content consistent)

### Feature Summary: "Fix with Copilot" for Failing Actions

```
Feature: One-click Fix for Failing GitHub Actions
Published: 2026-05-18

Access eligibility:
  ✅  Copilot Business subscribers
  ✅  Copilot Enterprise subscribers
  ❌  Copilot Pro / Pro+ (not mentioned)
  ❌  GitHub Actions alone (subscription required)

Admin prerequisite:
  Organization admin must enable Copilot cloud agent (disabled by default)
  Enterprise: AI controls → Agents → Copilot Cloud Agent → select policy
  Can be scoped per org, with per-repo overrides by org owners

Trigger condition:
  GitHub Actions workflow run fails on a pull request branch

Entry point:
  Workflow run logs page → "Fix with Copilot" button

User steps:
  1. Navigate to failing workflow run job page
  2. Click "Fix with Copilot"

CCA behavior after click:
  1. Starts new session in cloud development environment (ephemeral, GitHub Actions-powered)
  2. Investigates cause of failure
  3. Explores code, executes tests and linters
  4. Pushes fix to branch
  5. Tags user for review

Stated use-case scope: "simple but time-consuming work"
Canonical examples: fixing tests, correcting linter failures

CCA structural constraints (apply to all CCA tasks):
  - Only works with GitHub-hosted repositories
  - One branch at a time, one pull request per task
  - Branch protection rules may be incompatible
  - Does not account for content exclusions
  - Cannot access context outside the target repository

Human review: Required (CCA cannot merge its own fix)
```

### CCA Invocation Path Taxonomy (updated, May 2026)

```
CCA Task Invocation Paths (as of 2026-05-20)

Path 1 — UI / Manual (human-initiated)
  Trigger:   Assign issue to Copilot, start from Agents tab, @copilot in PR
  Source:    docs-github-copilot-cca-startup-custom-images.md Claim 4

Path 2 — GitHub Actions workflow (event-driven automation)
  Trigger:   Workflow event via assign-to-agent Safe Output (gh-aw platform)
  Source:    docs-ghaw-assign-to-copilot.md

Path 3 — REST API (direct programmatic)
  Trigger:   Any HTTP client (script, cron, portal, CI system)
  Source:    docs-github-copilot-cca-rest-api-tasks.md

Path 4 — Workflow failure UI (failure-event-triggered)
  Trigger:   GitHub Actions job fails on a pull request branch
  Mechanism: "Fix with Copilot" button on workflow run logs page
  Source:    THIS NOTE (docs-github-copilot-cca-fix-failing-actions.md)
  Scope:     PR-branch failures only; "simple" failures (tests, linters)
  Result:    CCA investigates → pushes fix → tags developer for review

Common output across all paths:
  Agent works in isolated ephemeral cloud environment → opens or updates a PR
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-code-w-claude-2026.md` Claim 9 ("CI auto-fix provides
    automatic fixes against PRs in CI/CD pipelines"): That claim documents the same
    CI auto-fix pattern for Claude Code Routines — when a PR triggers a CI failure,
    the routine analyzes the failure and attempts to fix it. The Copilot CCA feature
    here is the same pattern applied to a different agent (Copilot cloud agent vs.
    Claude Code Routines) in a different invocation style (UI button vs. webhook-triggered
    routine). Both corroborate that automatic CI failure remediation is an emerging
    standard pattern across AI coding agent platforms, not vendor-specific. The two
    implementations differ: Claude Code Routines are webhook-triggered automated pipelines;
    Copilot CCA "Fix with Copilot" is a human-initiated, one-click UI action.
  - `docs-github-copilot-cca-validation-parallel.md` Claim 3 ("The validation tools
    automatically scan Copilot-written code and attempt to self-remediate identified
    issues before requesting human review"): Both sources document a CCA
    investigate → fix → request-human-review loop. The validation parallel note documents
    this loop for CCA-written code (scan its own output); this source documents the same
    loop for externally-failing Actions jobs (investigate the failure, fix it, tag for
    review). Together they establish that the human-in-the-loop-at-review-only pattern
    is a consistent architectural choice for CCA across its use cases.

- **Extends**:
  - `docs-github-copilot-cca-rest-api-tasks.md` Claim 2 ("CCA executes in an isolated
    cloud development environment, making and validating code changes before opening a
    pull request"): This source adds a fourth invocation path to the CCA taxonomy
    documented in that note's Concrete Artifacts section. The REST API note documented
    Path 1 (UI), Path 2 (Actions workflow Safe Outputs), and Path 3 (REST API). The
    "Fix with Copilot" button adds Path 4 (workflow failure UI), which is event-triggered
    from a CI failure context rather than initiated directly by a human task intent.
  - `docs-github-copilot-cca-startup-custom-images.md` Claim 4 ("Three distinct
    interaction modes trigger CCA startup: assigning an issue to Copilot, starting a task
    from the Agents tab, and mentioning @copilot in a pull request"): That source
    enumerated the three pre-existing UI invocation modes. This source adds a fourth UI
    mode — clicking "Fix with Copilot" on workflow run logs — that is not covered by
    that enumeration. The new mode is triggered by a workflow failure event, not by a
    human-initiated intent like the other three.
  - `docs-github-copilot-cca-validation-parallel.md` Claim 4 ("Users can configure
    which of the four validation tools run via repository settings"): That source
    documents CCA's post-generation validation toolchain. This source adds a pre-push
    self-verification loop where CCA can execute the failing tests/linters before
    pushing the fix. These two verification layers are complementary: the validation
    toolchain scans CCA-generated code for security/quality issues; the test/linter
    execution in the fix cycle confirms the fix resolves the original failure.

- **Contradicts**: None identified. The feature's scope ("simple but time-consuming
  failures"), access tier (Business/Enterprise), and execution model (ephemeral cloud
  environment, human review required) are all consistent with existing CCA documentation.
  No contradiction issue filed.

- **Novel**:
  - **Fourth CCA invocation path (workflow-failure-triggered UI)**: No prior corpus
    source documents "Fix with Copilot" on workflow run logs as a CCA invocation
    mechanism. The prior paths (issue assign, Agents tab, @copilot in PR, REST API)
    are all initiated by human intent; this path is triggered by a failure event.
    The pattern shift — from intent-initiated to failure-event-initiated — is
    architecturally significant.
  - **Pull-request-branch scoping as a CCA constraint**: No prior corpus source
    establishes that CCA's workflow-fix capability is limited to PR-branch failures
    specifically. This is the first corpus entry to document a CCA feature that is
    explicitly conditioned on the workflow running on a pull request branch.
  - **Developer attention reallocation as explicit CCA value framing**: While the
    async development pattern has been documented (blog-simonwillison-code-w-claude-2026.md
    Claim 10), this is the first source to use the phrase "stay focused on what you
    actually want to build" as the explicit CCA value proposition for CI repair work
    specifically.
  - **CCA's ability to execute tests and linters in its fix cycle**: While previous
    notes document that CCA can run tests (docs-github-copilot-cca-validation-parallel.md),
    this is the first source to make explicit that CCA executes tests and linters as
    part of a diagnosis → fix → verify loop for externally-failing workflows, not just
    for its own generated code.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Update the CCA invocation taxonomy to include Path 4: the "Fix with Copilot" button
    on workflow run logs, triggered by a workflow failure on a PR branch. Specify the
    entry point (workflow run logs page), the trigger condition (PR-branch failure), and
    the scope constraint (simple failures: tests, linters). Document the PR-branch scoping
    as a hard constraint — this path does not apply to scheduled or main-branch workflow
    failures.
  - Add a "CI failure remediation" harness pattern: when a PR triggers a CI failure on
    a GitHub Actions workflow, developers can delegate the repair to CCA via one click,
    treating routine CI failures as CCA tasks rather than manual repair work. Set the
    expectation that this is reliable for deterministic mechanical failures (formatting,
    lint, type errors, straightforward assertions) and unreliable for logic failures,
    infrastructure failures, or flaky tests.
  - Add the admin enablement prerequisite as a deployment dependency: "Fix with Copilot"
    requires Copilot cloud agent to be enabled by an organization admin. Teams adopting
    this pattern must ensure CCA is enabled at the org level before expecting the button
    to appear.

- **Chapter 03 (Safety and Verification)**:
  - Add the workflow-fix invocation path as a concrete example of the CCA
    investigate → fix → self-verify → human-review-required loop. Distinguish this from
    the post-generation validation toolchain (docs-github-copilot-cca-validation-parallel.md):
    the validation layer scans for security/quality issues in CCA-written code; the
    workflow-fix self-verification executes the originally-failing tests/linters to confirm
    the fix resolves the failure before pushing. Both include a mandatory human review
    step.
  - Note that "Fix with Copilot" does not auto-merge: CCA pushes the fix to the branch
    and tags for review, but merging is a human decision. This maintains the human-in-the-loop
    requirement for all CCA workflow fixes.

- **Chapter 01 (Daily Workflows)**:
  - Add "Fix with Copilot" as a daily workflow pattern for pull request development:
    when a PR triggers a CI failure for a mechanical reason (lint, formatting, test assertion),
    clicking "Fix with Copilot" delegates the repair rather than switching context to debug
    it manually. Frame this as an attention conservation technique for routine failures,
    not a universal CI-repair strategy. The workflow: notice failure → click Fix with Copilot
    → return to building → review CCA's fix when notified.

- **Chapter 05 (Team Adoption)**:
  - Add the admin-enablement gate as a team rollout consideration: enabling "Fix with
    Copilot" for an organization requires an admin action (CCA must be on). Teams
    wanting to adopt this pattern should include CCA enablement in their Copilot
    onboarding checklist alongside model selection and usage metrics. Cross-reference
    the pilot-first pattern from docs-github-copilot-cca-custom-properties.md for
    progressive rollout guidance.

## Extraction Notes

1. **Brief source (~100 words)**: The changelog entry is among the shorter entries in
   the corpus. All substantive claims in the changelog itself are exhausted in three
   items. The linked documentation (three pages) substantially expands the extractable
   claims with constraint details, prerequisites, and procedural steps. Following the
   linked docs per MINER.md §1 was essential for producing a complete picture.

2. **WebFetch limitation on verbatim content**: Two fetches of the main changelog URL
   returned consistent content. The full verbatim text (5 paragraphs) is reproduced in
   the Concrete Artifacts section. Quotes are verified against this text. The linked
   documentation pages were fetched once each; those quotes are marked with the source
   page in the claim text.

3. **Quote reliability for linked docs**: The "Starting GitHub Copilot sessions"
   documentation WebFetch returned some paraphrasing rather than verbatim text for
   certain passages. Claims 4 and 6 use quotes from that page that the WebFetch model
   presented as direct quotes; the Assayer should spot-check these specific quotes
   against the live documentation URL. Claims derived from the "About cloud agent" page
   (Claim 7 and Claim 8) are presented as-fetched.

4. **No contradictions filed**: All claims are consistent with existing corpus notes.
   The feature extends the CCA invocation taxonomy (Claim 1) and the known CCA execution
   model (Claim 7) without contradicting any prior note. The CI auto-fix corroboration
   (Cross-References) is a pattern-level similarity, not an identity claim — the two
   implementations differ in agent, invocation mechanism, and scope.

5. **Failure type scope not specified**: The changelog lists "fixing tests or correcting
   linter failures" as examples but does not enumerate failure types CCA cannot handle,
   nor does it specify what CCA does when it cannot fix a failure (leave a comment?
   silently do nothing? create a PR explaining why it cannot fix?). This is a meaningful
   gap for practitioners deciding when to rely on "Fix with Copilot" — the linked
   documentation was also silent on CCA's behavior on unfixable failures.

6. **No billing implications documented**: The changelog and linked docs do not address
   whether "Fix with Copilot" consumes GitHub Actions minutes in addition to AI Credits
   (as Copilot code review does per docs-github-copilot-code-review-actions-billing.md
   Claim 2). Given that CCA operates in "an ephemeral development environment, powered
   by GitHub Actions," Actions minute consumption seems likely but is not confirmed by
   this source.
