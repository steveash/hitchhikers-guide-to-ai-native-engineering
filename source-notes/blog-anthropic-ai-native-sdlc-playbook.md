---
source_url: https://claude.com/blog/the-ai-native-sdlc-playbook
source_type: blog-post
title: "The AI-Native SDLC playbook"
author: Louis Claxton (Anthropic Applied AI team)
date_published: 2026-08-21
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: emerging
issue: "#2933"
---

# The AI-Native SDLC playbook

> First-party Anthropic Applied AI team playbook that restructures the
> traditional six-stage SDLC (Plan, Design, Build, Test, Deploy, Maintain)
> into a version-controlled artifact chain (`intent.md` → `spec.md` →
> `plan.md` → diff/tests → PR/review → incident record), with a named "play"
> per stage — each giving prerequisites, concrete execution steps, a
> governance mechanism, and leading/lagging metrics — and worked code
> examples for hooks, managed settings, skills, subagents, CI evals, and a
> deterministic production-monitoring loop that closes back into `intent.md`.

## Source Context

- **Type**: blog-post (official claude.com blog, published August 21, 2026;
  stated 5-minute reading time; byline "Author(s): Louis Claxton," with a
  closing acknowledgment "Thanks to Jim Blackhurst, Will Steuk, and Jamal
  Arif for their contributions to this guide, which was inspired by and
  built on much of their previous work.")
- **Author credibility**: Published under Anthropic's own claude.com/blog
  domain, framed throughout as "our Applied AI team's best practices for
  integrating Claude internally across each stage of the SDLC... inspired by
  working with our customers." This is first-party vendor guidance
  synthesizing patterns observed across Anthropic's own customer base, not a
  single company's internal case study (contrast with
  `blog-anthropic-secure-ai-native-sdlc.md`, which is Anthropic's Deputy
  CISO describing Anthropic's *own* internal SDLC specifically). No
  independent metrics or named customer outcomes are cited anywhere in this
  piece — every "How to measure it" section names a metric to track, not a
  result Anthropic or a customer has already measured.
- **Scope**: Covers a six-stage AI-native SDLC restructuring (Plan, Design,
  Build, Test, Deploy, Maintain) as a set of 15 named "plays," each with
  Prerequisites, Infrastructure, "How to execute it," a worked example
  artifact, Governance considerations, and How to measure it (leading +
  lagging indicators). Does not cover: specific pricing, a step-by-step
  admin rollout sequence beyond the closing "Resources" documentation links,
  any first-party metrics or named-customer case studies, or a security
  threat model (contrast with `blog-anthropic-secure-ai-native-sdlc.md` and
  `blog-anthropic-ciso-guide-agentic-ai.md`, which this piece does not cite
  or cross-reference).

## Extracted Claims

### Claim 1: When code generation stops being the bottleneck, the constraint moves to the human-speed stages around it (plan, review/test, deploy), controls stop matching reality because per-line human review can't keep pace with agent-authored diffs, and governance costs rise because exceptions still route through periodic meetings
- **Evidence**: Stated as the article's opening thesis, a three-part
  consequence list following directly from the premise that build now runs
  faster than the rest of the SDLC.
- **Confidence**: emerging (a first-party framing thesis, presented as
  self-evident reasoning rather than backed by a measurement in this
  article)
- **Quote**: "When code is no longer the bottleneck and the build phase runs
  faster than the traditional SDLC allows for, three things become true:"
- **Quote**: "The bottleneck moves to the steps to the left and right of the
  build phase. This is mainly plan, review/test, and deploy, which still run
  at human speed."
- **Quote**: "The controls stop matching reality and become intractable.
  Reviewing each line by hand made sense when a person had written it, but
  it can't keep up once agents write most of the diff."
- **Quote**: "Governance costs increase because exceptions still route
  through meetings and committees that meet weekly or monthly."
- **Quote**: "Build is no longer the constraint — the human-speed steps
  around it are. Human-speed stages keep their length while build collapses
  to hours."
- **Our assessment**: This is the same bottleneck-relocation thesis already
  well-represented in the corpus (see Cross-References → Corroborates), but
  it is the first source to decompose the *consequences* of the shift into
  three named mechanisms (controls become intractable at per-line
  granularity; governance costs rise because exception-handling stays
  meeting-paced) rather than just asserting "the bottleneck moved." The
  security-queue framing ("either the review queue builds or code ships
  under-reviewed") is a concrete, testable prediction worth citing alongside
  the more abstract bottleneck-shift claims already in the guide.

### Claim 2: The AI-native SDLC replaces a linear flow with a loop where each stage commits a version-controlled artifact that the next stage reads, and an accepted artifact automatically fires the next stage's gate
- **Evidence**: Stated as the structural definition of "AI-native SDLC" and
  restated as the organizing principle of the "Plays" section.
- **Confidence**: emerging (an architectural framework asserted by the
  source, illustrated with a single domain example — claims status
  self-service — rather than validated against multiple real
  implementations in this article)
- **Quote**: "The AI-native SDLC is a reimagined process that combines the
  old control objectives with new enforcement. Instead of a linear flow, the
  process becomes a loop, and AI is embedded at each point."
- **Quote**: "The thread running through the right-hand column is the
  committed artifact. Each stage ends by writing one to version control
  (including intent.md, spec.md, plan.md, the diff and its tests, the PR
  with its review findings, and the incident record) and the next stage
  begins by reading it."
- **Quote**: "A stage ends by committing an artifact with the commit
  initiating the next stage. An accepted intent.md triggers the requirements
  and design pass, an approved spec.md triggers plan mode, a merged PR
  triggers the pipeline, and a breached control band in production writes
  the next intent.md and so the loop continues."
- **Our assessment**: This is the article's central organizing device and
  its most guide-actionable structural claim: it names six concrete
  artifact types and states explicitly that "the chain of commits is also
  the audit trail: who asked for what, what the agent produced, and who
  approved it." This reframes governance as an emergent property of the
  artifact chain rather than a separately bolted-on control layer — a
  useful, specific mechanism for any guide section on how to keep human
  oversight legible as agent throughput increases.

### Claim 3: Plan-stage intent capture replaces committee-based requirements gathering with a single Claude-assisted brainstorming session that produces a version-controlled, machine-actionable `intent.md`, with the product owner reviewing and correcting the agent-written draft rather than authoring it
- **Evidence**: Described as Stage 1 (Plan), with a "Traditional vs.
  AI-native" comparison and a full worked `intent.md` example (see Concrete
  Artifacts).
- **Confidence**: emerging (a prescriptive workflow with a worked example,
  not a measured outcome — the "How to measure it" section names an
  expectation, "fall from a multi-week elicitation and refinement cycle to
  hours," but does not report an observed before/after result)
- **Quote**: "The originator brainstorms with Claude and writes the result
  down as intent.md, a proto-spec in the originator's own terms. The
  artifact contains what is wanted, why, and under which constraints."
- **Quote**: "Regardless of whether the intent originates from an event
  trigger or an agent, the same steps apply: the product owner reviews and
  corrects the agent-written intent.md before it is committed."
- **Our assessment**: The specific governance mechanism — a human always
  reviews and corrects the agent-drafted artifact before it becomes the
  audit-trail record — is stated identically at every stage of this
  playbook (Plan, Design, Build) and is the closest thing the article has to
  a single unifying control. Worth extracting as a named pattern in its own
  right: "the agent drafts, a named human corrects and commits" rather than
  "the agent drafts and a human approves," which shifts the human's role
  from gatekeeper to co-author of the artifact of record.

### Claim 4: Requirements and design, traditionally separate phases run by separate teams (analysts, then designers), collapse into a single prompted Claude session constrained by the organization's skills for brand, security, compliance, and UX
- **Evidence**: Described as Stage 2 (Design), with a "Traditional vs.
  AI-native" comparison and a worked prompt example.
- **Confidence**: emerging (prescriptive workflow, worked prompt example
  given, no measured before/after cycle-time result reported in this
  article)
- **Quote**: "Both phases happen in a single prompted session. Claude takes
  intent.md and produces a requirements and design spec, constrained by the
  organization's skills, with areas of concern flagged."
- **Quote**: "Instead of being discovered in a review weeks later, the live
  policy is read and applied while the spec is written."
- **Our assessment**: This is a specific instance of "shift policy
  enforcement left" applied to requirements/design rather than code — the
  same structural move as the CLAUDE.md-as-security-control pattern already
  documented in `blog-anthropic-secure-ai-native-sdlc.md` Claim 4, but
  applied one stage earlier in the lifecycle (at spec-writing time rather
  than code-generation time). The measurement design is notable and
  reusable on its own: "Elapsed time between the intent.md commit and the
  spec.md commit for the same change (two git timestamps)" is a concrete,
  low-effort leading indicator derivable from git log alone, without any new
  tooling.

### Claim 5: Claude Code's plan mode is positioned as the default starting point for build-stage work — the engineer gives Claude the approved spec.md and lets it interview them, iterating on a written plan before any code is written, with the accepted plan committed as `plan.md` for later stages (PR review) to check the eventual diff against
- **Evidence**: Described as Stage 3 (Build)'s primary play, with a
  Traditional/AI-native comparison, a worked `plan.md` example (see
  Concrete Artifacts), and an explicit governance mechanism (plan mode
  itself enforces the gate).
- **Confidence**: emerging (a prescriptive workflow claim; the governance
  mechanism described — "Claude cannot edit files until the engineer
  accepts the plan" — is a product-behavior claim about Claude Code, not
  independently verified in this note)
- **Quote**: "Work starts with a written plan that Claude produces in plan
  mode, where it can read the codebase without changing anything. The
  engineer corrects the plan before code is written, and the approved
  version is committed as plan.md for later stages to check against."
- **Quote**: "Design review happens before any code is generated, when
  changing course is still a matter of editing a document. Plan mode
  enforces this itself, since Claude cannot edit files until the engineer
  accepts the plan."
- **Quote**: "When implementation departs from the plan, update plan.md in
  the same commit. Consider using a hook to enforce synchronization between
  the two."
- **Our assessment**: The "consider a hook to enforce plan.md/diff
  synchronization" line is a specific, actionable idea not seen elsewhere in
  the corpus: rather than treating plan.md as a one-time artifact that goes
  stale, the article suggests using the same hook mechanism (Claim 8 below)
  to keep the committed plan and the actual diff from drifting apart. The
  lagging indicator proposed — "how often the merged diff still matches the
  committed plan.md" — gives a concrete way to measure plan/execution
  fidelity that the guide could recommend as a review-time check.

### Claim 6: A working rule for maintaining CLAUDE.md is that when Claude makes the same mistake twice, the correction goes into the file — keeping it under a page because Claude reads all of it every session and stale content wastes context for no benefit
- **Evidence**: Stated as a specific maintenance heuristic within the
  CLAUDE.md play, with a worked example file (see Concrete Artifacts)
  containing a "Things Claude gets wrong" section.
- **Confidence**: settled (a specific, low-ambiguity operational rule stated
  as prescriptive guidance, consistent with — not novel relative to — how
  CLAUDE.md is already treated elsewhere in the corpus)
- **Quote**: "A working rule helps here. When Claude makes a mistake twice,
  the correction goes into CLAUDE.md."
- **Quote**: "Keep it under a page, because Claude reads all of it at the
  start of a session and anything stale is taking up context for no
  benefit."
- **Our assessment**: This corroborates and sharpens the "closing the loop"
  pattern for CLAUDE.md maintenance already implicit in
  `blog-anthropic-secure-ai-native-sdlc.md` Claim 4 (update CLAUDE.md
  whenever a vulnerability class is discovered) by generalizing it beyond
  security: any repeated mistake, not just a security-relevant one, earns a
  CLAUDE.md entry. The explicit "under a page" size constraint is a concrete
  operational number not previously quantified this specifically in the
  corpus.

### Claim 7: The rule of thumb for deciding what becomes a skill versus what belongs in CLAUDE.md or a prompt is: write a skill for institutional knowledge that must be applied consistently, and a skill is only an advisory control — a deterministic hook is needed behind any policy that must hold without exception
- **Evidence**: Stated as the explicit decision rule in the "Skills as
  institutional knowledge" play, paired with a governance caveat about
  skills' limits.
- **Confidence**: settled (a clear, first-party decision rule stated as
  unambiguous prescriptive guidance)
- **Quote**: "The rule of thumb: write a skill for institutional knowledge
  that must be applied consistently; don't write a skill for components that
  belong in CLAUDE.md or a prompt."
- **Quote**: "A skill is a control, though an advisory one. It makes Claude
  likely to apply the policy while the code is written, and nothing forces a
  session to comply with it. A policy that must always hold needs something
  deterministic behind the skill, such as a hook that blocks the action or a
  review pass that re-checks the policy at the PR. The skill makes
  violations rare and the hook makes them close to impossible."
- **Our assessment**: The "skill = advisory, hook = deterministic enforcement
  layer behind it" distinction is a clean, reusable taxonomy for a harness-
  engineering chapter — it gives a specific test ("does this policy need to
  always hold, or just usually hold?") for choosing between the two
  mechanisms, rather than treating skills and hooks as interchangeable
  "configuration." This is consistent with, and adds a decision rule on top
  of, the nine-category skill taxonomy already in the corpus via
  `blog-anthropic-claude-code-skills-lessons.md`, which does not frame the
  skill/hook boundary in advisory-vs-deterministic terms.

### Claim 8: Build-phase hooks should be fast, scoped to the file that changed, and used to block edits to protected paths, run formatters/linters after edits, and keep credentials out of the diff — while a hook that asks a human for approval belongs at the deploy gate, not the build phase, because an approval prompt mid-build blocks every session running in parallel
- **Evidence**: Stated as the explicit scoping rule for the "Hooks as
  build-time guardrails" play, distinguishing it from the "Hooks as approval
  gates" play in Stage 5.
- **Confidence**: settled (a specific, first-party design rule for where a
  given hook type belongs in the pipeline)
- **Quote**: "A hook that asks a human for approval belongs with the gates
  in Stage 5: Deploy, because an approval prompt during the build puts a
  person back on the critical path of all the sessions running in
  parallel."
- **Quote**: "A hook runs on each action that matches it, so build-phase
  hooks should be fast and scoped to the file that changed. Heavier checks
  such as the full test suite belong at the commit or the PR."
- **Our assessment**: This is a specific, actionable placement rule for
  hooks that the corpus does not currently state this precisely: it
  distinguishes hooks by *when in the pipeline they should block* rather
  than just what they check, with an explicit rationale (parallel sessions
  break if a build-time hook pauses for human input). This directly informs
  how the "hooks as build guardrails" vs. "hooks as approval gates" plays
  later in the same article (Claim 9 below) divide responsibility.

### Claim 9: Approval gates should be implemented as hooks that can allow, ask, or block — team-level hooks live in git-tracked `.claude/settings.json`, non-negotiable organization-wide hooks live in managed settings that individual engineers cannot override, and a block should explain itself (the reason and the approval route) in Claude's output
- **Evidence**: Stated as the "Hooks as approval gates" play, with two full
  worked code artifacts: a `.claude/settings.json` PreToolUse hook
  registration and the corresponding `production-gate.sh` script (see
  Concrete Artifacts).
- **Confidence**: settled (a specific, prescriptive mechanism with a
  complete worked implementation, consistent with the hooks documentation
  referenced in the article's closing Resources list)
- **Quote**: "Team hooks go in .claude/settings.json in git, and
  non-negotiable hooks go in managed settings owned by the platform or IT
  admin, where individual engineers cannot switch them off."
- **Quote**: "A block should explain itself, so when a hook stops an action
  the reason and the route to approval appear in Claude's output."
- **Our assessment**: The team-hooks-vs-managed-hooks split (git-tracked and
  engineer-editable vs. platform-owned and non-overridable) is a specific,
  two-tier governance model worth citing directly alongside the
  `allowManagedHooksOnly` managed-settings key documented in the same
  article's worked "Managed settings for a regulated enterprise" example
  (Concrete Artifacts) — the two plays are explicitly designed to compose:
  managed settings is what makes the "non-negotiable" half of this claim
  actually non-negotiable, since `allowManagedHooksOnly` is stated to mean
  "the approval gates from this play are the only hooks that run; nothing
  local can add to or replace them."

### Claim 10: One engineer can run several independent Claude Code sessions in parallel, each in its own git worktree with no knowledge of the others, while a subagent is a distinct mechanism — a scoped helper inside a single session with its own context window and tool limits, suited to jobs that recur within one task
- **Evidence**: Described as the "Parallel sessions and subagents" play,
  with worked examples of both a `claude --worktree` invocation pattern and
  a full `.claude/agents/verifier.md` subagent definition (see Concrete
  Artifacts).
- **Confidence**: emerging (a clear conceptual distinction and worked
  examples, but the practical ceiling given — "two or three sessions is a
  sensible starting point" — is presented as author guidance, not a
  measured optimum)
- **Quote**: "A parallel session is another full Claude Code instance,
  working a separate task in its own git worktree. Each independent session
  knows nothing about the others, and the engineer steering them is the only
  thing they share."
- **Quote**: "A subagent runs inside a single session as a scoped helper
  with its own context window and tool limits and suits jobs that recur in
  multiple tasks such as verifying the app runs as expected."
- **Quote**: "Two or three sessions is a sensible starting point. The
  practical ceiling is how many streams one person can review properly, so
  add sessions only while review is keeping up."
- **Our assessment**: This is a clean terminological distinction (parallel
  session = separate worktree/instance/task; subagent = in-session scoped
  helper) that the guide can use to disambiguate two mechanisms that are
  sometimes conflated. The stated ceiling — driven by review capacity, not
  compute or tooling — reinforces Claim 1's framing that review, not
  generation, is the binding constraint even at the level of a single
  engineer's individual workflow.

### Claim 11: A feedback loop (Claude checking and fixing its own work via tests, a build, or a screenshot diff, run through the whole task as many times as needed) is a distinct mechanism from a verifier subagent (a single fresh-context check run once the session believes it is done), and the loop itself must be protected by a hook that blocks edits to test files during a fix task
- **Evidence**: Stated as the "Give Claude a feedback loop" play's core
  distinction and closing safeguard, in Stage 4 (Test).
- **Confidence**: settled (a specific mechanism definition plus a concrete,
  low-ambiguity enforcement recommendation)
- **Quote**: "The feedback loop should not be confused with a verifier
  subagent (Stage 3: Build). The feedback loop runs through the whole task
  as many times as the work. The verifier subagent, on the other hand, is
  one way to package the final check by running a fresh context window once
  the session believes the work is done. This way the verdict is not
  colored by the assumptions that produced the code."
- **Quote**: "The loop itself needs protecting, because an agent fixing code
  must not be able to weaken the check on that code. A hook that blocks
  edits to test files during a fix task does this. The alternative is to
  check the diff in review and reject any change that touches a test."
- **Our assessment**: The self-undermining-verification risk this names —
  an agent asked to make a failing test pass could edit the test instead of
  the code — is a specific, concrete failure mode worth flagging in a
  verification chapter, along with its stated mitigation (hook-block test
  files during fix tasks, or reject any review diff that touches a test).
  This complements the verification-loop taxonomy already in the corpus via
  `blog-anthropic-claude-code-verification-loops-skills.md` Claim 1, which
  defines a verification loop similarly ("Claude checks its own work and
  attempts to fix it") but does not name this specific test-file-tampering
  risk or its hook-based mitigation.

### Claim 12: Continuous evals are the AI-native equivalent of stage-gate QA — a 20-to-50-task suite built from real recent work, run in CI on every change to CLAUDE.md, skills, or hooks (not just on a schedule), gating configuration changes on the pass rate, with every production incident added as a permanent regression case
- **Evidence**: Described as the "Continuous evals in CI" play, with a
  worked GitHub Actions workflow (see Concrete Artifacts) and an explicit
  execution trigger.
- **Confidence**: emerging (a prescriptive workflow with a worked CI
  example; no measured pass-rate or incident-reduction outcome reported in
  this article)
- **Quote**: "The suite runs non-interactively in CI on a schedule and on
  any change to CLAUDE.md, skills or hooks, since that configuration steers
  the agent and deserves the regression testing that code gets."
- **Quote**: "Each production incident gets an eval, written by the team
  that owned the incident, and stays in the suite as a regression test."
- **Our assessment**: "Configuration steers the agent and deserves the
  regression testing that code gets" is a specific, quotable framing: it
  argues CLAUDE.md/skills/hooks changes should go through the same CI gate
  as code changes, not be treated as prose edits exempt from testing. The
  incident-to-eval-case pipeline directly parallels the same pattern already
  described for the Maintain stage (Claim 14 below), making it a
  through-line across the whole article rather than a single-stage idea.

### Claim 13: Claude both reviews incoming PRs against a written policy (`REVIEW.md`, naming passes, severity thresholds, and a nit cap) and addresses review comments on its own PRs when tagged, but findings never approve or block a PR on their own — branch protection still requires a human code owner's approval, preserving separation of duties because the agent that wrote the code cannot approve it
- **Evidence**: Described as the "AI in the PR review loop" play, with a
  full worked `REVIEW.md` example (see Concrete Artifacts) and an explicit
  governance statement.
- **Confidence**: settled (a specific, unambiguous governance rule directly
  stated, consistent with separation-of-duties framing already present
  elsewhere in the corpus)
- **Quote**: "The tech lead sets the human threshold. Findings do not
  approve or block a PR on their own, and branch protection still requires
  approval from a code owner."
- **Quote**: "Separation of duties is preserved, because the agent that
  wrote the code has no way to approve it."
- **Quote**: "Reserve Important for findings that would break behavior, leak
  data or breach a policy. Style and naming are nits."
- **Our assessment**: This directly corroborates the separation-of-duties
  principle already documented as one of this article's own five governance
  principles and echoes `blog-anthropic-secure-ai-native-sdlc.md` Claim 6
  ("multiple specialized review agents... to avoid the shared blind spots of
  a single reviewer") — but adds a specific artifact (`REVIEW.md`, with
  named passes: bugs, security, compliance-against-spec-and-plan) and a
  specific tuning mechanism ("once a month the tech lead tunes the setup by
  rating findings so the reviewer improves and by capping Nit volume") not
  present in that companion piece.

### Claim 14: In the Maintain stage, a deterministic (non-model) monitoring script watches a production metric against a rolling baseline with statistical process-control rules, and response is tiered by how far the metric has drifted — 1σ only logs, 2σ invokes Claude read-only to diagnose, 3σ lets Claude act only by opening a PR into the existing review gate or triggering a pre-approved runbook — with the diagnosis written back as a new `intent.md` that re-enters Stage 1
- **Evidence**: Described as the "Maintenance and closing the loop" play,
  with a worked `bands.yaml` config example (see Concrete Artifacts) and
  three named example trigger scenarios.
- **Confidence**: emerging (a prescriptive architecture with a worked
  config example and named example scenarios, not a reported production
  outcome — the article gives illustrative examples, e.g. "when the CI test
  failure rate breaches 3σ, the agent quarantines the flaky test or opens a
  revert PR," rather than a case study of this actually happening)
- **Quote**: "A deterministic script watches production and invokes Claude
  when a control band is breached."
- **Quote**: "They write the detection script, typically mean and standard
  deviation over a rolling window with rules (Western Electric or similar)
  so the bands catch slow drift as well as spikes. The script is version
  controlled and unit tested, and detection stays entirely deterministic,
  with no model involved."
- **Quote**: "At 1σ the script only logs, at 2σ it invokes Claude read-only
  to diagnose, and at 3σ Claude may act, though only by opening a PR into
  the review gate or triggering a pre-approved runbook."
- **Quote**: "Detection stays deterministic. Claude is invoked once a band
  is breached, and the tier sets what it may do."
- **Our assessment**: The Western-Electric-rules-based tiered response (log
  → diagnose read-only → act-through-a-gate-only) is a specific, reusable
  control architecture for "how much autonomy should a monitoring-triggered
  agent get" — a concrete answer that scales the model's authority to the
  severity of the detected drift rather than granting it a fixed
  permission level. This is new to the corpus in this specific
  statistical-process-control form (no existing note names Western Electric
  rules or a σ-tiered response ladder for agent autonomy).

## Concrete Artifacts

```
Source: "The AI-Native SDLC playbook," claude.com/blog, August 21, 2026

Stage 1 (Plan) worked example — intent.md:

# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.
## Problem
Customers phone the contact center to ask where their claim is.
Handlers spend roughly a third of call time on status-only queries.
## Proposed outcome
Customers see claim status, next step and expected date in the portal.
## Affected users and systems
Claims handlers, portal team, claims-core API.
## Constraints
No new PII in the portal session. Existing authentication only.
## Open questions
Do third-party loss adjusters need access too?
```

```
Source: same article

Stage 3 (Build) worked example — plan.md:

# Plan: claims status self-service (from intent.md 2026-06-02)
## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py,
claims-api/tests/test_status.py
## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.
## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.
## Proof
test_status.py covers the four claim states; screenshot matches the
approved mock.
```

```
Source: same article

CLAUDE.md worked example (Build stage):

# Payments service
## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)
## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
- Every endpoint needs an integration test in src/itest.
## Architecture
- api/ holds REST controllers, core/ holds domain logic,
adapters/ talks to external systems.
- Kafka events are defined in schemas/; never edit generated classes.
## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
- The legacy v1/ package is frozen; changes go in v2/.
```

```
Source: same article

Skill worked example (.claude/skills/secure-api-review/SKILL.md):

---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
modifying an external-facing endpoint, reviewing API code, or
generating an OpenAPI spec.
---
# Secure API review
When you create or change an API endpoint:
1. Authentication: every endpoint requires the gateway JWT;
no anonymous routes outside /health.
2. Input validation: validate request bodies against the OpenAPI
schema and reject unknown fields.
3. Audit: every state-changing endpoint emits an audit event with
actor, action, entity and timestamp.
4. Data classification: fields tagged pii in the schema must never
appear in logs or error messages.
Run scripts/check-endpoints.sh and include its output in your summary.
```

```
Source: same article

Subagent worked example (.claude/agents/verifier.md), from the
"Parallel sessions and subagents" play:

---
name: verifier
description: Runs the app and checks the change works before the session
reports done
tools: Bash, Read
---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

```
Source: same article

Approval-gate hook pair (Stage 5: Deploy), .claude/settings.json:

{
"hooks": {
"PreToolUse": [
{
"matcher": "Bash",
"hooks": [
{ "type": "command",
"command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh" }
]
}
]
}
}

...and the gate script itself (.claude/hooks/production-gate.sh):

#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
if [ -z "$RELEASE_APPROVAL" ]; then
echo "Production deploys need a release authorization." >&2
exit 2 # exit 2 blocks the action; the message goes to Claude
fi
fi
exit 0
```

```
Source: same article

"Managed settings for a regulated enterprise" worked example (deployed by
the platform team via MDM/admin console; engineers cannot edit or override):

{
"permissions": {
"deny": [
"Read(.env*)", "Read(./secrets/**)",
"WebFetch", "Bash(curl *)", "Bash(wget *)"
],
"allow": [
"Bash(git *)", "Bash(make build)",
"Bash(make test)", "Bash(make lint)"
],
"disableBypassPermissionsMode": "disable"
},
"allowManagedPermissionRulesOnly": true,
"sandbox": {
"enabled": true,
"failIfUnavailable": true,
"allowUnsandboxedCommands": false,
"network": { "allowedDomains": ["git.internal.example.com",
"registry.npmjs.org"] },
"credentials": {
"files": [
{ "path": "~/.ssh", "mode": "deny" },
{ "path": "~/.aws/credentials", "mode": "deny" }
],
"envVars": [ { "name": "GITHUB_TOKEN", "mode": "deny" } ]
}
},
"allowManagedHooksOnly": true,
"disableSideloadFlags": true,
"allowManagedMcpServersOnly": true,
"strictKnownMarketplaces": [
{ "source": "github", "repo": "example-corp/approved-plugins" }
],
"requiredMinimumVersion": "2.1.193"
}
```

```
Source: same article

CI evals workflow (Stage 4: Test), .github/workflows/agent-evals.yml:

name: Agent evals
on:
pull_request:
paths: ['CLAUDE.md', '.claude/**']
schedule:
- cron: '0 2 * * *'
jobs:
evals:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- run: npm install -g @anthropic-ai/claude-code
- name: Run eval suite
env:
ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
run: |
for eval in evals/*.json; do
claude -p "$(jq -r '.prompt' $eval)" \
--allowedTools "Read,Edit,Bash(make test)" \
--output-format json > result.json
./evals/check.sh "$eval" result.json
done
```

```
Source: same article

PR review policy worked example (Stage 5: Deploy), REVIEW.md:

# Review instructions
## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles
## What Important means here
Reserve Important for findings that would break behavior, leak data
or breach a policy. Style and naming are nits.
## Cap the nits
Report at most five nits per review; summarize the rest as a count.
## Do not report
Generated files under src/gen/ and anything CI already enforces.
```

```
Source: same article

CI/CD pipeline step worked example (Stage 5: Deploy), non-interactive
triage:

- name: Triage failed build
if: failure()
run: >
claude -p "Read the build log at out/build.log. Identify the most
likely cause, say whether the failure looks flaky or real, and write a
three-line summary for the PR thread." >> triage.md
```

```
Source: same article

Production monitoring config worked example (Stage 6: Maintain),
bands.yaml:

metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
1sigma: { action: log }
2sigma: { action: diagnose,
tools: "Read,Grep,Bash(gh run view *)" }
3sigma: { action: propose,
routes: [pull_request, runbook:rollback-deploy] }
```

```
Source: same article

"The shifts" comparison table (Traditional SDLC vs. AI-native SDLC,
reproduced from the article's table):

Plan     | Traditional: Requirements gathered by committee, distilled
           through workshops and sign-offs, written up by hand
         | AI-native: Claude synthesizes pain points straight from the
           sources and captures them within intent.md which is human
           readable and machine actionable
Design   | Traditional: Spec written by analysts, parsed by designers
         | AI-native: Requirements and design compressed into one working
           session with an agent, guided by standards encoded as skills,
           versioned in git
Build    | Traditional: Tests and code are handwritten and documentation
           is written after the main development happens
         | AI-native: Tests and code are generated by AI and institutional
           knowledge is maintained as versioned machine-readable CLAUDE.md
           files and skills
Test     | Traditional: QA gates at stage boundaries
         | AI-native: Continuous evals woven through implementation
Deploy   | Traditional: Humans review every line of code and governance
           occurs in review cycles, often inconsistently
         | AI-native: Layers of agentic review with human review reserved
           for regulated and critical code. Governance is enforced as the
           AI acts, with hooks as approval gates
Maintain | Traditional: Humans watch production for bugs
         | AI-native: Agents monitor live deployments. Any breached
           control band is diagnosed and written back into the loop as a
           new intent.md
```

```
Source: same article

Five stated governance principles (from the article's "Governance
Principles" summary, reproduced as a list):

1. Humans remain accountable for decisions requiring judgment
2. Controls are version-controlled so policy changes are auditable
3. Everything is logged in git history and audit trails
4. Separation of duties preserved -- agents cannot approve their own work
5. Managed settings allow platform teams to enforce non-negotiable controls
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-secure-ai-native-sdlc.md` Claim 6 (multiple specialized
    review agents, each scoped to a narrow focus, review every PR to avoid
    a single reviewer's blind spots): this article's PR review loop (Claim
    13 here) is architecturally consistent, adding the specific `REVIEW.md`
    artifact and named passes (bugs/security/compliance) that the companion
    piece does not detail.
  - `blog-anthropic-secure-ai-native-sdlc.md` Claim 4 (CLAUDE.md as a
    security-guideline enforcement surface, closing the loop by updating it
    when a vulnerability class is discovered): this article's Claim 6
    generalizes the same "close the loop via CLAUDE.md" mechanism beyond
    security to any repeated mistake.
  - `blog-anthropic-secure-ai-native-sdlc.md`'s "insider threat" / SIEM
    governance framing and its five governance principles are consistent
    with — though not identical in wording to — this article's own five
    stated Governance Principles (Concrete Artifacts), particularly
    "separation of duties preserved" appearing near-verbatim in both
    (compare this article's principle 4 to the companion piece's Claim 9
    framing of agents as insider threats requiring separation of duties).
  - `blog-addyosmani-new-software-lifecycle.md` Claim 7 (AI compresses the
    SDLC unevenly — implementation collapses while requirements,
    architecture, and verification stay slow because they are judgment
    work, relocating rather than removing the bottleneck): this is the same
    underlying thesis as Claim 1 here, from a different first-party/
    practitioner-synthesis source. Osmani's piece frames the unevenness as
    a *phase-compression* argument; this article frames the same shift as a
    *consequence* argument (controls become intractable, governance costs
    rise) — complementary framings of one thesis rather than duplicates.
  - `blog-anthropic-claude-code-verification-loops-skills.md` Claim 1
    (a verification loop is Claude checking its own work and attempting to
    fix it, distinct from the broader agentic loop): directly corroborated
    by this article's Claim 11 definition of a "feedback loop," though this
    article adds a risk (test-file tampering during a fix) and mitigation
    (hook-block test file edits) not present in that note.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 3 (verification
    skills have had the most measurable impact on Claude's output quality
    internally at Anthropic): consistent with, though not directly
    restating, this article's emphasis on feedback loops and continuous
    evals (Claims 11-12 here) as central to the Test stage.

- **Contradicts**: No formal contradiction issue filed. One point of
  friction worth flagging for editorial awareness: this article never cites
  or cross-references `blog-anthropic-secure-ai-native-sdlc.md` or
  `blog-anthropic-ciso-guide-agentic-ai.md` despite covering substantially
  overlapping territory (both describe a six-stage SDLC framework with a
  governance layer, published by the same company one month apart — this
  article August 21, 2026; the security piece July 21, 2026). The two
  six-stage breakdowns use different stage names (this article: Plan,
  Design, Build, Test, Deploy, Maintain; the security piece: Plan, Code,
  Test/CI, Deploy/CD, Monitor, Governance) and organize the material by
  workflow-transformation vs. security-control respectively, so this is not
  a factual disagreement — the two pieces answer different questions about
  the same underlying six-stage shape. Not filed as a contradiction issue
  per MINER.md 4a because no claim in either piece opposes a claim in the
  other; flagged here only so the guide does not present two
  differently-named "the six SDLC stages" frameworks as if they were one
  without noting the terminology mismatch.

- **Extends**: `blog-anthropic-secure-ai-native-sdlc.md`: that article
  organizes six stages (Plan, Code, Test/CI, Deploy/CD, Monitor, Governance)
  around security controls specifically, with one control and one "enduring
  principle" per stage. This article covers a similarly-shaped six-stage
  breakdown (Plan, Design, Build, Test, Deploy, Maintain) organized around
  general workflow transformation rather than security, and adds
  substantial new stage-specific mechanism detail not in the security
  piece: the artifact-chain structure itself (Claim 2), intent.md capture
  (Claim 3), the design-and-requirements-compression play (Claim 4), plan
  mode as the default build-stage entry point with a plan.md/diff
  synchronization hook (Claim 5), the skill-vs-hook advisory/deterministic
  decision rule (Claim 7), the build-vs-deploy hook placement rule (Claim
  8), the parallel-sessions/subagent distinction (Claim 10), the
  feedback-loop/verifier-subagent distinction and test-file-tampering risk
  (Claim 11), and the σ-tiered deterministic monitoring architecture (Claim
  14) — none of which appear in the companion piece.

- **Novel**:
  - **The full artifact-chain structure** (Claim 2): naming intent.md,
    spec.md, plan.md, diff+tests, PR+review, and incident record as a single
    connected chain, each stage's output becoming the next stage's input, is
    new to the corpus as an explicit, named end-to-end structure.
  - **The skill-is-advisory / hook-is-deterministic decision rule** (Claim
    7): no prior corpus source states this specific test for choosing
    between a skill and a hook.
  - **The build-hook-vs-deploy-hook placement rule** (Claim 8): the
    rationale that approval-asking hooks belong at deploy because they
    would block parallel build sessions is new and specific.
  - **The σ-tiered (Western Electric rules) deterministic monitoring
    architecture** (Claim 14): no existing corpus source names Western
    Electric rules or a three-tier (log/diagnose/propose) autonomy ladder
    keyed to statistical drift magnitude.
  - **The plan.md/diff synchronization hook suggestion** (Claim 5): using a
    hook to keep a committed plan artifact from drifting silently out of
    sync with the actual implementation is a new, specific idea.
  - **The parallel-session vs. subagent terminological distinction** (Claim
    10), stated this precisely with worked examples of both, is new to the
    corpus as a side-by-side comparison (prior sources discuss subagents and
    worktrees separately, not paired and distinguished in one place).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the skill-is-advisory /
  hook-is-deterministic decision rule (Claim 7) and the build-hook-vs-
  deploy-hook placement rule (Claim 8) as concrete guidance for a section on
  choosing enforcement mechanisms — currently the guide's coverage of
  skills and hooks (via `blog-anthropic-claude-code-skills-lessons.md` and
  `failure-hooks-enforcement-2k.md`) does not state this specific two-axis
  decision framework (what kind of control, and at what pipeline stage).

- **Chapter 02 (Harness Engineering)**: Add the parallel-session/subagent
  distinction (Claim 10) with its two worked examples
  (`claude --worktree`, `.claude/agents/verifier.md`) as a concrete,
  citable clarification for any section covering multi-session or
  multi-agent workflows, including the explicit ceiling rationale ("add
  sessions only while review is keeping up").

- **Chapter 03 (Verification)**: Add the feedback-loop/verifier-subagent
  distinction and the test-file-tampering risk with its hook-based
  mitigation (Claim 11) as a specific failure mode and fix for any section
  on self-verifying agent workflows — this is a concrete risk
  (`blog-anthropic-claude-code-verification-loops-skills.md` does not name
  this specific risk) with a named mitigation.

- **Chapter 03 (Verification)**: Add the continuous-evals-in-CI pattern
  (Claim 12), specifically the framing that CLAUDE.md/skills/hooks changes
  should trigger the same regression suite as code changes and that every
  production incident should become a permanent eval case — this
  reinforces and gives a concrete CI trigger mechanism (path-based GitHub
  Actions trigger on `CLAUDE.md`, `.claude/**`) to the general
  "evals-as-regression-tests" idea already present via
  `blog-anthropic-claude-code-verification-loops-skills.md`.

- **Chapter 05 (Team Adoption)**: Use the six-stage artifact-chain structure
  (Claim 2) and the intent.md → spec.md → plan.md progression (Claims 3-5)
  as a candidate organizing skeleton for a section on rolling out AI-native
  process changes stage-by-stage — the article's own explicit permission to
  "begin with any 'clay play' (prerequisite-free) stage" and adopt plays
  independently is a useful, low-risk incremental-adoption framing distinct
  from a big-bang SDLC rewrite.

- **Chapter 06 (Security and Threat Model)**: Add the σ-tiered deterministic
  monitoring architecture (Claim 14, with the worked `bands.yaml` example)
  as a concrete pattern for scaling an agent's production-response
  authority to the severity of a detected anomaly, alongside the existing
  six-stage security framework from `blog-anthropic-secure-ai-native-sdlc.md`
  — note in the text that the two articles use different stage names for
  what is otherwise a similar six-stage shape (see Cross-References →
  Contradicts) so the guide should pick one naming convention rather than
  presenting both as if unrelated.

## Extraction Notes

- **Access method**: An initial WebFetch request returned a condensed,
  AI-generated summary rather than verbatim source text (consistent with
  the same limitation noted in `blog-anthropic-secure-ai-native-sdlc.md`'s
  Extraction Notes). Rather than extract quotes from that summary, the raw
  HTML was downloaded directly via `curl` with a browser user agent
  (200 response, ~642KB, confirmed server-rendered — not a JS-only SPA
  shell) and converted to plain text by stripping tags while preserving
  paragraph/heading/table-cell boundaries. All quotes in this note were
  taken from that raw-HTML text extraction and checked against the
  extracted text directly, following the same curl-based method already
  validated in `blog-addyosmani-new-software-lifecycle.md` and
  `blog-addyosmani-loop-engineering.md`.
- **Full article read**: The entire article was read in full via the raw
  text extraction, from the opening "Code is no longer the bottleneck"
  section through all six stage plays (Plan, Design, Build, Test, Deploy,
  Maintain), the two Build-stage sidebars (Legacy systems / source of
  truth; CLAUDE.md; Skills; Hooks; Parallel sessions), the "Managed
  settings for a regulated enterprise" worked example, and the closing
  "Closing thoughts" and "Resources and acknowledgments" sections. No
  linked sub-pages were followed — the article's own "Resources and
  acknowledgments" section links to platform documentation pages
  (admin-setup, settings reference, sandboxing, hooks, skills, plugin
  marketplaces, managed MCP, monitoring, compliance API, security model)
  rather than substantive prose sources; these are reference documentation,
  not additional narrative content, so they were not separately fetched for
  this extraction but are noted here in case a future Miner wants to mine
  the platform docs directly.
  - **One minor artifact in the raw-text extraction**: the sentence "Build
  is no longer the constraint — the human-speed steps around it are.
  Human-speed stages keep their length while build collapses to hours."
  appears to be a pull-quote/callout rendered inline with the surrounding
  paragraph in the tag-stripped text (it interrupts a paragraph about the
  security-team example mid-sentence in the raw HTML). It was extracted as
  its own quote in Claim 1 rather than spliced into the surrounding
  sentence, consistent with MINER.md 2a's instruction not to splice
  non-adjacent text into a single quoted passage.
- **All cross-reference claim numbers** cited above (from
  `blog-anthropic-secure-ai-native-sdlc.md`,
  `blog-addyosmani-new-software-lifecycle.md`,
  `blog-anthropic-claude-code-verification-loops-skills.md`, and
  `blog-anthropic-claude-code-skills-lessons.md`) were verified by
  re-reading each cited note's actual numbered claims before writing this
  note; none were guessed.
- **No contradiction issue filed**: evaluated the stage-naming mismatch with
  `blog-anthropic-secure-ai-native-sdlc.md` against the MINER.md 4a bar (see
  Cross-References → Contradicts) and judged it a terminology difference
  between two complementary framings, not a claim-level disagreement that
  would drive opposite guide advice.
- **Confidence calibration**: rated `emerging` overall. The article is
  first-party Anthropic guidance with extensive, specific worked code
  examples (settled-level artifacts — the JSON/YAML/shell examples are
  concrete and internally consistent), but nearly every prescriptive claim
  is presented as recommended practice with a "how to measure it" section
  naming a metric to *start* tracking, not a reported outcome already
  observed — unlike `blog-anthropic-secure-ai-native-sdlc.md`, which reports
  specific first-party metrics (e.g., 16%→54% substantive-review growth).
  This article should be read as a prescriptive playbook, not an
  outcomes report.
