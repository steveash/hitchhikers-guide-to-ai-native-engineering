---
source_url: https://github.blog/changelog/2026-07-10-agentic-autofix-for-code-scanning-alerts-in-public-preview
source_type: docs
title: "Agentic autofix for code scanning alerts in public preview"
author: GitHub (official changelog)
date_published: 2026-07-10
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: settled
issue: "#1878"
---

# Agentic Autofix for Code Scanning Alerts in Public Preview

> GitHub's July 10, 2026 changelog announcing public preview of agentic autofix: assigning a
> code scanning alert to Copilot triggers a cloud-agent loop that explores the codebase,
> proposes a fix, validates it by rerunning CodeQL, and opens a draft PR — replacing the prior
> free, non-agentic "Generate Fix" option and requiring both a security license and Copilot
> cloud agent access.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words / "2 minute read", July 10, 2026)
- **Author credibility**: GitHub engineering team announcing a production feature in public
  preview. Authoritative for: the feature's existence, its trigger mechanism, the four-step
  agent loop, the licensing/billing requirements, and the admin-disable controls. Not a
  credible source for: fix acceptance rates, false-positive rates on generated fixes, how
  often the agent iterates before succeeding, or comparative performance against the classic
  (non-agentic) "Generate Fix" option it replaces.
- **Scope**: Covers what agentic autofix does, how it is triggered (four entry points), its
  requirements, and its billing model. Does NOT cover: fix quality/acceptance data, supported
  languages or alert types, behavior when CodeQL cannot confirm closure after iteration, or
  what happens to the classic "Generate Fix" option after the agentic version reaches GA.

## Extracted Claims

### Claim 1: Agentic autofix remediates code scanning alerts "by working across your codebase the way a developer would," and is scoped to organizations with both a Code Security/Advanced Security license and Copilot cloud agent enabled

- **Evidence**: Opening summary paragraph of the official changelog, stating the feature's
  mechanism and eligibility in a single passage.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Agentic autofix is now in public preview for code scanning alerts. It remediates
  alerts by working across your codebase the way a developer would: it explores relevant
  files, proposes a fix, and reruns CodeQL to confirm the fix closes the alert before opening
  a pull request for your review."
- **Our assessment**: The "the way a developer would" framing is doing real work here — it
  positions the agent as doing multi-file investigation rather than pattern-matching a
  single-line patch template (the likely mechanism of the classic, free "Generate Fix"
  option it replaces, per Claim 5). This is a proactive-remediation product, distinct from
  `docs-github-copilot-security-validation-third-party-agents.md`, which validates *newly
  generated* code as it's written. Agentic autofix instead targets a backlog of *pre-existing*
  alerts — closing the loop on findings that already exist in a repository's security
  inventory rather than preventing new ones.

### Claim 2: The agent loop is a fixed four-step sequence — explore relevant files, generate a proposed fix, validate by rerunning CodeQL, iterate if needed, then open a draft PR

- **Evidence**: Explicit numbered/bulleted breakdown of the "How it works" section.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "When you assign a code scanning alert to Copilot, it: Explores relevant files
  across your codebase. Generates a proposed fix. Validates the fix works by rerunning
  CodeQL. Iterates if needed, then opens a draft pull request ready for your review."
- **Our assessment**: The validation step is the most consequential design choice: GitHub
  uses the *same detector that raised the alert* as the pass/fail oracle for the fix,
  rather than a separate test suite or the agent's own self-assessment. This is a stronger
  and more specific instance of the "self-remediate before requesting human review" pattern
  in `docs-github-copilot-cca-validation-parallel.md` (Claim 3) — that source describes CCA's
  four validation tools (CodeQL, Advisory Database, secret scanning, Copilot code review)
  running generically against Copilot-written code; here, CodeQL rerun is not one of several
  generic checks but *the specific check that defines success* for this task, since the task
  is "close this exact alert." It also parallels Cursor's Anybump workflow
  (`blog-cursor-security-agents.md` Claim 6: reachability → trace → run tests → check
  breakage → open PR), which likewise gates PR creation on a concrete pass/fail signal rather
  than agent self-report.

### Claim 3: Fix generation typically takes 2–4 minutes, and the resulting pull request includes a fix summary, the reasoning for why it closes the alert, and the validation steps Copilot took

- **Evidence**: Timing statement and PR-content description immediately following the
  four-step loop description.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Fix generation typically takes 2–4 minutes." … "The pull request includes a
  summary of the fix, why it closes the alert, and the validation steps Copilot took to
  confirm that it works."
- **Our assessment**: A 2–4 minute turnaround for a full explore-generate-validate-iterate
  loop is fast enough to suggest most individual alerts have a narrow enough fix surface
  that the "explore relevant files" step doesn't require deep multi-file reasoning in the
  typical case (the changelog gives no data on the tail — alerts requiring several iteration
  rounds could take substantially longer). The PR-content requirement (summary + rationale +
  validation steps, not just a diff) matches the general pattern of coding-agent PRs
  including their own justification, which reduces reviewer verification cost by making the
  agent's reasoning inspectable rather than requiring the reviewer to reconstruct it.

### Claim 4: Reviewers can request further changes to the draft PR either via PR comments or by interacting with the session in the repository's Agents tab

- **Evidence**: Final sentence of the "How it works" section, describing the post-PR
  interaction model.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "When the pull request containing the fix is ready, you can instruct Copilot to
  make further changes to it by commenting on the pull request or interacting with the
  session in the Agents tab of your repository."
- **Our assessment**: Two distinct interfaces for the same iterative-refinement action (PR
  comment vs. Agents tab session) means the human-in-the-loop correction step doesn't force
  reviewers into a single workflow — someone doing PR review in the normal GitHub UI can
  correct the agent without leaving that context, while someone monitoring active agent
  sessions can intervene from the Agents tab instead. The changelog does not say whether
  these two paths converge on the same underlying session state or are independent.

### Claim 5: Agentic autofix replaces the free "Generate Fix" option with a paid "Assign to Copilot" button, because it now runs through the Copilot cloud agent and therefore draws down AI Credits

- **Evidence**: Opening sentence of the "How to use it" section, stated as a direct
  replacement and consequence.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Agentic autofix replaces the free "Generate Fix" option on individual code
  scanning alerts with an Assign to Copilot button. Because it uses the Copilot cloud agent,
  it draws down AI Credits."
- **Our assessment**: This is a concrete instance of a previously-free capability moving
  behind metered billing as it becomes agentic — worth flagging for cost-model guidance.
  Teams that budgeted "free" for code-scanning autofix (via the classic option) need to
  re-plan for AI Credit consumption once they adopt the agentic replacement, even though the
  entry point (a button on the alert) looks unchanged. The changelog does not state whether
  the classic "Generate Fix" option remains available as a free fallback during the preview,
  though Claim 8 implies "classic" and "agentic" autofix currently coexist as separate,
  independently controllable experiences.

### Claim 6: Agentic autofix can be triggered from four distinct entry points — individual alert assignment, multi-alert selection from the security alerts list, multi-alert selection within a security campaign, or the REST API by setting an alert's `assignees` to `["copilot-swe-agent[bot]"]`

- **Evidence**: Bulleted list in the "How to use it" section enumerating trigger surfaces.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Via the Update a Code Scanning Alert REST API by setting assignees to
  ["copilot-swe-agent[bot]"]."
- **Our assessment**: The REST API entry point means agentic autofix can be driven outside
  the GitHub UI — e.g., a scheduled workflow could enumerate open alerts matching some
  criteria and bulk-assign them to Copilot programmatically, similar in spirit to the
  `assign-to-agent` safe output documented in `docs-ghaw-assign-to-copilot.md` (Claim 1),
  though that reference targets generic issues/PRs while this REST parameter is scoped
  specifically to code scanning alerts. See Extraction Notes for a caveat on verifying the
  exact `assignees` parameter shape against the live REST reference.

### Claim 7: Access requires both an active GitHub Code Security or GitHub Advanced Security license and a Copilot license with Copilot cloud agent enabled

- **Evidence**: "Access" section, stated as a two-part requirement.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "The public preview of agentic autofix requires: An active GitHub Code Security
  or GitHub Advanced Security license. A Copilot license with Copilot cloud agent enabled."
- **Our assessment**: This dual-license gate — a security product license *and* a Copilot
  cloud agent entitlement — is a real adoption friction point: a team could have GitHub
  Advanced Security without Copilot cloud agent enabled (or vice versa) and be unable to use
  the feature until both are provisioned. This parallels the admin-enablement prerequisite
  for CCA's "Fix with Copilot" on failing Actions jobs (`docs-github-copilot-cca-fix-failing-
  actions.md` Claim 5: "Copilot cloud agent must be enabled by an organization administrator
  before users can access the workflow-fix feature") — Copilot cloud agent enablement is a
  recurring prerequisite gate across multiple GitHub agentic-remediation surfaces, not unique
  to this one.

### Claim 8: Org/repo admins can turn "Copilot Autofix" off in Settings, and enterprise admins can disable it by policy; disabling via policy turns off both the classic and agentic autofix experiences

- **Evidence**: Second sentence of the "Access" section, describing the disable controls and
  their scope.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "An organization or repository admin can turn Copilot Autofix off in Settings,
  and an enterprise admin can disable it by policy. When disabled via policy, both the
  classic and agentic autofix experiences are disabled."
- **Our assessment**: This confirms that "classic" (the prior free "Generate Fix") and
  "agentic" autofix currently coexist as two experiences under one feature umbrella, with a
  two-tier control structure: a settings-level toggle at org/repo scope, and a stricter,
  all-or-nothing policy toggle at enterprise scope that takes down both experiences together.
  Teams cannot use enterprise policy to disable only the paid/agentic path while keeping the
  free/classic path — that granularity, if it exists, would have to happen at the org/repo
  Settings level instead.

### Claim 9: During public preview, AI Credits are consumed only when a fix actually runs on an assigned alert, agentic autofix activity also consumes GitHub Actions minutes, and usage is not itemized separately from other Copilot activity

- **Evidence**: "Billing" section, describing the cost model and its current reporting
  limitation.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "During this public preview, agentic autofix draws down your organization's AI
  Credits. AI Credits are consumed only when a fix runs, on the alerts you assign to
  Copilot. Usage for agentic autofix isn't itemized separately from other Copilot activity
  during public preview." … "Activity performed by agentic autofix also consumes GitHub
  Actions minutes."
- **Our assessment**: Two separate cost dimensions apply — AI Credits (model inference) and
  Actions minutes (compute for running the exploration/fix/CodeQL-rerun loop, which
  presumably executes inside an Actions-backed environment). The explicit "isn't itemized
  separately" admission is an operational gap for cost governance during preview: an org
  admin cannot currently isolate "how much is agentic autofix costing us" from aggregate
  Copilot spend, which limits ROI evaluation before the feature reaches GA and pricing
  potentially changes.

## Concrete Artifacts

### Agentic Autofix Four-Step Loop

```
Source: GitHub changelog, "Agentic autofix for code scanning alerts in public preview"
(github.blog/changelog/2026-07-10-agentic-autofix-for-code-scanning-alerts-in-public-preview)

Trigger: alert assigned to Copilot (four entry points — see below)

1. Explore relevant files across the codebase
2. Generate a proposed fix
3. Validate the fix works by rerunning CodeQL
4. Iterate if needed → open a draft pull request ready for review

Typical fix-generation time: 2–4 minutes
PR contents: fix summary + rationale for alert closure + validation steps taken
Post-PR iteration: PR comments, or the repository's Agents tab session
```

### Trigger Entry Points

```
Source: same changelog, "How to use it" section

1. Individual code scanning alert → assign to Copilot (replaces free "Generate Fix")
2. Security alerts list → select one or more alerts for a single combined PR
3. Security campaign → select one or more alerts for a single combined PR
4. REST API → Update a Code Scanning Alert, assignees: ["copilot-swe-agent[bot]"]
```

### Requirements, Admin Controls, and Billing

```
Source: same changelog, "Access" and "Billing" sections

Requirements (both required):
  - Active GitHub Code Security or GitHub Advanced Security license
  - Copilot license with Copilot cloud agent enabled

Admin controls:
  - Org/repo admin: turn "Copilot Autofix" off in Settings
  - Enterprise admin: disable by policy
    -> policy-level disable turns off BOTH classic and agentic autofix experiences

Billing (public preview):
  - AI Credits consumed only when a fix runs on an assigned alert
  - GitHub Actions minutes also consumed by agentic autofix activity
  - Usage not itemized separately from other Copilot activity during preview
```

## Cross-References

- **Corroborates**: `blog-cursor-security-agents.md` Claim 6 (Cursor's Anybump: reachability
  analysis → trace code paths → run tests → check breakage → open PR → canary gate). Both
  sources describe an agentic remediation loop that gates PR creation on a concrete
  pass/fail validation step rather than agent self-report — GitHub uses "CodeQL rerun
  confirms the alert closes," Cursor uses "tests pass, no breakage detected." Different
  problem domains (static-analysis alerts vs. dependency vulnerabilities), same validate-
  before-PR architecture.

- **Corroborates**: `discussion-hn-autofix-hybrid-review.md` Claim 8 (DeepSource's 7-step
  hybrid pipeline: Codebase Indexing → Static Pass → AI Review → Remediation → Sanitization
  → Output → Caching). GitHub's four-step loop (Claim 2 above) is a production, narrower
  instantiation of the same "static findings anchor the AI, agent proposes a fix, fix is
  validated before output" architecture — GitHub's validation step (rerun CodeQL) plays the
  role of DeepSource's "Sanitization" step, but as a rerun of the original detector rather
  than a separate language-specific validator.

- **Corroborates**: `docs-github-copilot-cca-validation-parallel.md` Claim 3 ("The
  validation tools automatically scan Copilot-written code and attempt to self-remediate
  identified issues before requesting human review"). Both describe self-remediation before
  human review as the standard CCA behavior. The distinction: that source's validation tools
  (CodeQL, Advisory Database, secret scanning, Copilot code review) run generically against
  *newly written* Copilot code as a safety net; this source's CodeQL rerun is not a generic
  safety check but the specific, singular success criterion for a task whose entire purpose
  is closing one pre-existing alert.

- **Corroborates**: `docs-github-copilot-security-validation-third-party-agents.md` (whole
  note). Together with this source, GitHub is building two complementary ends of a security-
  agent pipeline: validation (Claims 1–2 of that note: CodeQL/Advisory Database/secret
  scanning checks on code as it's generated, including by third-party agents) prevents *new*
  issues, while agentic autofix (this source) remediates a backlog of *pre-existing* alerts.
  Neither source's note previously covered the other's half of this pipeline.

- **Corroborates**: `docs-github-copilot-cli-security-review.md` Claim 3 (Copilot CLI's
  `/security-review` five-category vulnerability taxonomy as a bounded, dedicated security
  surface) and `blog-cursor-security-agents.md` Claim 5 (dedicated, threat-model-tuned
  security agents outperform general-purpose review). This source is a further instance of
  GitHub building a dedicated, named agentic surface for a specific security workflow
  (backlog remediation) rather than routing it through general-purpose Copilot prompting,
  consistent with the specialization principle both of those sources argue for.

- **Extends**: `docs-github-copilot-cca-fix-failing-actions.md` (whole note — "Fix with
  Copilot" for failing GitHub Actions jobs). That source documents the same underlying
  pattern — assign a problem to Copilot cloud agent, it investigates and fixes it in an
  ephemeral environment, then opens a PR for review — applied to CI/test/linter failures.
  This source applies the identical assign→investigate→fix→validate→PR shape to code
  scanning alerts instead. Both require prior admin enablement of Copilot cloud agent
  (Claim 7 here; Claim 5 of that note), suggesting Copilot cloud agent enablement is a
  single organization-wide gate that unlocks multiple downstream agentic-remediation
  surfaces once granted.

- **Extends**: `docs-ghaw-assign-to-copilot.md` Claim 1 (`assign-to-agent` safe output for
  programmatically assigning Copilot to issues/PRs). This source's REST API trigger (Claim 6:
  setting an alert's `assignees` to `["copilot-swe-agent[bot]"]`) is a parallel,
  narrower assignment mechanism scoped specifically to code scanning alerts, using a
  distinct bot account identity from the generic `"copilot"` agent name used in the gh-aw
  safe output. See Claim 6 assessment and Extraction Notes for the verification caveat on
  this specific parameter.

- **Contradicts**: None identified. No existing source note makes a claim that materially
  opposes anything in this changelog. No contradiction issue filed.

- **Novel**: The four-step public-preview loop for code-scanning-alert remediation (explore
  → generate → validate via CodeQL rerun → iterate → draft PR) is new to the corpus in this
  specific trigger context (Claim 2). The distinct bot identity `copilot-swe-agent[bot]` used
  for this automation surface (Claim 6) is new — no prior corpus note documents this specific
  bot account string, as distinct from the generic `"copilot"` agent identifier used
  elsewhere. The explicit "classic vs. agentic autofix coexist, policy-disable takes down
  both" governance detail (Claim 8) is new. The dual AI-Credits-plus-Actions-minutes billing
  structure with no separate itemization during preview (Claim 9) is a new concrete cost-
  governance data point.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add "assign a code scanning alert to Copilot" as a
  concrete example of the delegate-and-review pattern for routine remediation work. The
  developer's role shifts to triage (which alerts to assign, individually or in batch) and
  review (accept, request changes via PR comment, or intervene in the Agents tab session on
  the resulting draft PR) rather than authoring the fix — citing Claims 1, 2, and 4.

- **Chapter 03 (Verification)**: Cite Claim 2 as a concrete example of "use the same tool
  that flagged the issue as the pass/fail oracle for the agent's fix" — rerunning CodeQL to
  confirm the exact alert closes is a stronger, narrower validation signal than an agent's
  self-assessment or a generic test suite. Present this alongside `docs-github-copilot-cca-
  validation-parallel.md`'s four-tool validation loop as evidence that GitHub is
  standardizing on "rerun the original detector" as the correctness check for security-
  related agent output, both for newly generated code (that source) and for fixes to
  pre-existing alerts (this source).

- **Chapter 05 (Tools and Frameworks / Cost and Economics)**: Cite Claims 5 and 9 to update
  cost-model guidance for GitHub Copilot: agentic autofix moves the previously-free
  "Generate Fix" option behind metered AI Credits, and the cost model spans two dimensions
  (AI Credits for inference, GitHub Actions minutes for the exploration/validation
  compute) rather than a single per-token cost. Flag the preview-period itemization gap
  (Claim 9) — org admins currently cannot isolate agentic-autofix spend from general Copilot
  activity, which limits per-feature ROI evaluation during rollout planning.

## Extraction Notes

1. **Verbatim quotes verified against raw HTML, not just WebFetch**: An initial WebFetch
   pass returned a paraphrased summary. To satisfy MINER.md §2a, the page's raw HTML was
   fetched directly via `curl` and stripped of markup to recover the literal text, and every
   quote in this note was copied character-for-character from that raw extraction (the
   source's own en dash in "2–4 minutes" was preserved). This avoids the quote-reliability
   caveats flagged in several sibling notes (e.g. `docs-ghaw-assign-to-copilot.md` Extraction
   Note 2) that had to rely on WebFetch-summarized quotes.

2. **REST API parameter not independently confirmed**: The changelog states the REST
   trigger sets `assignees` to `["copilot-swe-agent[bot]"]` on the Update a Code Scanning
   Alert endpoint. An attempt to independently verify this against the live GitHub REST API
   reference page for that endpoint returned an ambiguous WebFetch summary that described a
   generic `assignees` array of GitHub usernames and did not confirm a Copilot-specific
   value. This is treated as a limitation of that secondary fetch (REST reference pages are
   large and the summarizing pass may not have reached the relevant example), not as a
   contradiction of the changelog — the changelog is the primary, authoritative source for
   this claim and is quoted directly in Claim 6. Flagging for the Assayer in case independent
   verification against the live REST docs is warranted before this detail is used in the
   guide.

3. **Two linked pages followed**: In addition to the primary changelog, two linked
   documentation pages were fetched and read: the "Update a Code Scanning Alert" REST API
   reference (see Extraction Note 2 above) and the Copilot usage-based billing documentation
   page (confirms AI Credits as the general Copilot billing unit and that cloud agent usage
   is one of several AI-Credit-consuming surfaces, consistent with Claim 9, but provided no
   agentic-autofix-specific pricing detail). Neither linked page contributed a directly
   quotable, autofix-specific claim beyond what the changelog itself states.

4. **No contradictions found**: Checked this source's claims against all source notes
   returned by searching for "autofix," "copilot," "security," and "cursor" in
   `source-notes/`. No existing note makes a claim that materially opposes anything here. No
   contradiction issue filed.

5. **Source is short**: The changelog itself is a ~300-word, "2 minute read" announcement.
   All nine claims above are drawn from its full text — no paragraph was left unextracted.
   Depth in this note comes primarily from cross-referencing against the eight-plus existing
   corpus notes on adjacent GitHub Copilot cloud agent and security-agent surfaces, not from
   additional length in the primary source itself.
