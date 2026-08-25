---
source_url: https://github.github.com/gh-aw/blog/2026-08-24-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – August 24, 2026: The Workflow Doctor"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-08-24
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: emerging
issue: "#2935"
---

# Agent of the Day – August 24, 2026: The Workflow Doctor

> Tenth entry in the "Agent of the Day" series — profiles Q ("The Workflow
> Doctor"), a slash-command-triggered `gh-aw` workflow that activates only on
> `/q` comments (issues, pull requests, discussions) to diagnose and propose
> fixes for *other* workflows in the repo. Introduces the corpus's first
> on-demand, comment-triggered write-enabled diagnostic agent, and gives the
> first documented example of a `create-pull-request` safe output configured
> with a multi-day expiry, a file-count patch cap, and a protected-file
> fallback-to-issue policy all in combination.

## Source Context

- **Type**: blog-post (tenth "Agent of the Day" entry from the official
  GitHub Agentic Workflows blog; bylined "Copilot" per the on-page author
  card, the same recurring gh-aw convention for AI-authored posts documented
  throughout this series, e.g. `blog-ghaw-agent-of-the-day-2026-08-21.md`.
  Each post profiles one production agent with concrete run data. This entry
  profiles a slash-command-triggered, write-enabled diagnostic agent —
  distinct from the daily-scheduled codemod agents (Dead Code Removal,
  Code Simplifier) and the daily-scheduled triage agent (Issue Arborist)
  documented elsewhere in the series, and from the read-only scheduled
  audits (Architecture Guardian, the Notary).)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post names three specific,
  independently identifiable GitHub Actions run IDs (32726221560, 32727642327,
  32726004596) and two specific source issues/discussions (`discussion
  #55296`, `issue #55389`, `discussion #55334`), plus a specific safe-outputs
  guardrail configuration (2-day PR expiry, 500-file patch cap,
  protected-file fallback). No run URL, issue URL, or discussion URL is
  rendered as a clickable link on the fetched page (unlike, e.g.,
  `blog-ghaw-agent-of-the-day-2026-08-21.md`, where run and PR numbers are
  hyperlinked) — the identifiers are named in prose only, so they are
  reported here as stated but were not independently followed. High
  credibility for first-party platform claims consistent with the rest of
  this series.
- **Scope**: Profiles three recent Q runs at a summary level (one request
  sentence, one outcome sentence each) plus the workflow's fixed technical
  specification (engine, permissions, self-edit restriction) and its
  safe-outputs guardrail configuration. Does NOT cover: the full YAML
  frontmatter or `q.md` workflow definition; the actual diff or PR content
  produced by any of the three runs; whether any of the three proposed PRs
  was merged; per-run token/turn/runtime metrics for runs 2 and 3 (only run 1
  states duration and token usage); or any run where Q's diagnosis was wrong
  or its proposed fix was rejected.

## Extracted Claims

### Claim 1: Q ("The Workflow Doctor") is a `gh-aw` workflow that activates only when summoned via a `/q` comment on an issue, pull request, or discussion — in explicit contrast to the timer-based schedule most `gh-aw` workflows in the series run on

- **Evidence**: Direct framing statement opening the post, contrasting Q with
  the (implicitly more common) scheduled-workflow pattern documented
  elsewhere in this series.
- **Confidence**: settled (explicit, first-party framing and mission
  description)
- **Quote**: "Most agentic workflows in gh-aw run on a timer, quietly doing their thing every day whether anyone's watching or not. Today's spotlight is different: it only shows up when you call it. Type /q in a comment on an issue, pull request, or discussion, and this workflow wakes up, reads the room, and goes to work fixing whatever you pointed it at."
- **Our assessment**: This is the series' first entry to name the trigger
  contrast explicitly as the organizing theme of the post (rather than
  describing the trigger only as a technical detail). It corroborates
  `docs-ghaw-chatops.md` Claim 1 ("no prior source note documents a human-
  initiated trigger for agentic workflows... human-pull rather than
  system-push"), giving that documented mechanism its first named production
  instance in the "Agent of the Day" series specifically. For Ch02 (Harness
  Engineering): "on-demand, comment-triggered diagnostic agent" is a fifth
  named agent archetype in this series' taxonomy, alongside event-driven
  moderation, scheduled read-only audit, scheduled write-enabled codemod, and
  scheduled triage — see Cross-References → Extends for the full taxonomy
  argument.

### Claim 2: Q's own frontmatter self-describes it as an "intelligent assistant that answers questions, analyzes repositories, and can create PRs for workflow optimizations," running on the Copilot engine with SDK mode enabled, with read-only access to issues, pull requests, and discussions, and a hard rule that it may never edit its own definition file (`q.md`)

- **Evidence**: Direct description under "Key Details About Q" naming the
  self-description, engine, access level, and the self-edit restriction.
- **Confidence**: settled (explicit technical specification, though sourced
  from the post's own paraphrase of the workflow's frontmatter rather than a
  directly fetched copy of `q.md` itself — see Extraction Notes)
- **Quote**: "We're calling this persona The Workflow Doctor, and it belongs to Q, a slash-command-triggered gh-aw workflow described in its own frontmatter as an \"intelligent assistant that answers questions, analyzes repositories, and can create PRs for workflow optimizations.\" Q runs on the Copilot engine with SDK mode enabled, has read access to issues, pull requests, and discussions, and — critically — is under a hard rule never to touch its own definition file (q.md)."
- **Our assessment**: "SDK mode enabled" on the Copilot engine corroborates
  `blog-ghaw-weekly-2026-06-01.md` Claim 3, which documents `engine:
  copilot-sdk` as an eighth engine option providing "direct access to the
  Copilot SDK runtime, opening up new integration patterns" beyond the
  standard Copilot CLI. Q is the first entry in this series to name
  `copilot-sdk` (or an SDK-mode variant of the Copilot engine) as the engine
  choice for a profiled agent. The self-edit restriction ("never to touch
  its own definition file") is a distinct, narrower restraint mechanism from
  any prior corpus entry: it is not a Safe Outputs protected-file policy
  applied generically (`docs-ghaw-threat-detection.md` Claim 10's protected
  categories are dependency manifests, CI/CD workflow files, and agent
  instruction files like `AGENTS.md`/`CLAUDE.md`) but a workflow-specific,
  presumably prompt-level or protected-files-`exclude`-configured rule
  singling out one exact file. For Ch03 (Safety and Verification): a
  write-enabled agent whose job is to *modify other workflows* is a
  self-referential risk case (it could, in principle, edit its own
  guardrails to loosen them); naming and enforcing "never edit your own
  definition file" as an explicit, separately-stated rule — distinct from
  the general protected-files policy — is a concrete mitigation worth
  documenting for any agent whose write scope overlaps its own configuration
  surface.

### Claim 3: In one documented run (32726221560, 11.5 minutes, 25.8k tokens, single turn), Q responded to a maintainer's `discussion #55296` request to add an MCP-remote-mode test job as an infrastructure canary, and concluded successfully with a proposed pull request queued up

- **Evidence**: Direct description of the run, its trigger, its stated
  purpose, and its outcome.
- **Confidence**: settled (specific run ID, specific token/turn/duration
  figures, specific discussion number, and specific verbatim request quoted)
- **Quote**: "Run 32726221560 fired from a comment on discussion #55296, where a maintainer asked Q to \"add a job that tests the github MCP in remote mode without using any agentic workflow feature\" as a canary test to rule out a runtime/compiler bug, plus a summary of the MCP handshake message. Q completed in 11.5 minutes across a single turn, burning 25.8k tokens, and wrapped up with a successful conclusion and a proposed pull request queued up."
- **Our assessment**: This is the only one of the three profiled runs with
  concrete performance figures (duration, token count, turn count) attached —
  runs 2 and 3 (Claims 4–5) are described only by request and outcome, with
  no timing or cost data. "Rule out a runtime/compiler bug" as the underlying
  motivation is notable: the request is not itself a workflow bug report but
  a request to build a *diagnostic instrument* (an MCP-remote-mode canary
  job) to help isolate a different, unconfirmed bug — Q is here building
  test infrastructure on request, not just fixing a known defect. For Ch02
  (Harness Engineering): "agent builds a diagnostic canary test on request,
  to help a human isolate an unrelated suspected bug" is a distinct request
  category from the fix-a-known-problem pattern more typical of codemod
  agents in this series (e.g., Dead Code Removal, Tidy-Upper).

### Claim 4: In a second run (32727642327), Q responded to a request on `issue #55389` to switch a workflow to a cheaper model to reduce cost, and turned it into a workflow-level model swap

- **Evidence**: Direct description of the run's trigger, request, and
  outcome.
- **Confidence**: settled (specific run ID, specific issue number, and
  specific verbatim request quoted; no duration/token/turn figures given for
  this run)
- **Quote**: "Run 32727642327 answered a comment on issue #55389 asking Q to \"use mai flash model to reduce cost\" — a straightforward cost-tuning request that Q turned into a workflow-level model swap."
- **Our assessment**: "Mai flash" as the target model name is stated exactly
  as quoted in the post (verbatim per MINER.md §2a; likely "MAI Flash" or a
  similarly-cased model identifier, but the source's own capitalization —
  lowercase "mai flash" inside the quoted maintainer request — is preserved
  here rather than normalized). No prior corpus note documents a model named
  "mai flash"; this may be a newly available model option not yet
  cross-referenced in `docs-ghaw-engines-reference.md` or model-inventory
  notes such as `blog-ghaw-weekly-2026-08-17.md` Claim 5 (which lists Gemini
  3.7 Flash and Grok 4.6 as the most recent additions as of that post,
  neither matching "mai flash"). For Ch04 (Operations): this run is a
  concrete example of "swap the model for a cheaper one" as a
  developer-requested, agent-executed cost-reduction action — a lighter-weight
  cost-governance mechanism than the token-budget guardrails documented
  elsewhere in the corpus (e.g. `blog-ghaw-weekly-2026-06-01.md` Claim 1's
  "token guardrails").

### Claim 5: In a third run (32726004596), Q responded to a request on `discussion #55334` to add persistent state via `repo-memory`, plumbing state into a workflow that had previously been stateless between runs

- **Evidence**: Direct description of the run's trigger, request, and
  outcome.
- **Confidence**: settled (specific run ID and discussion number, specific
  verbatim request quoted; no duration/token/turn figures given for this
  run)
- **Quote**: "Run 32726004596 came from discussion #55334, where the ask was to \"update to use repo-memory to store the mined loops\" — plumbing persistent state into a workflow that was previously stateless between runs."
- **Our assessment**: "Mined loops" as the specific state being persisted
  suggests the target workflow is itself a loop-mining or pattern-mining
  agent (plausibly related to this very guide-mining corpus's own domain of
  "loop engineering," c.f. `blog-addyosmani-loop-engineering.md` and
  `blog-addyosmani-practical-loop-engineering.md`, though those notes cover
  Addy Osmani's `/loop` feature in a different product, not a `gh-aw`
  workflow — no direct connection is claimed here, only a naming
  coincidence worth flagging). This is the series' first documented instance
  of an agent adding `repo-memory` to another workflow on request, rather
  than a workflow author configuring `repo-memory` for themselves — i.e., Q
  performing a specific category of workflow-authoring task (adding
  persistence) as a service to another workflow's maintainer. For Ch02: add
  "retrofit repo-memory into a previously stateless workflow" as one concrete
  request category Q (or a similar diagnostic/fix agent) can be asked to
  perform.

### Claim 6: Audit data classifies Q's behavior fingerprint as "directed" execution with "narrow" tool breadth and a "selective_write" actuation style — summarized in the post as "Q doesn't wander"

- **Evidence**: Direct statement following the three run examples,
  describing Q's classified behavior pattern and what it reads before acting.
- **Confidence**: settled (explicit classification terms quoted directly,
  though the classification methodology/system that produced these labels is
  not described — see Our assessment)
- **Quote**: "Audit data on the discussion-triggered run classifies its behavior fingerprint as directed execution with narrow tool breadth and a selective_write actuation style — in plain terms, Q doesn't wander. It reads exactly what it needs (the triggering comment, the parent issue or discussion, recent logs and audits for the target workflow), forms a specific diagnosis, and proposes a scoped pull request through its create-pull-request safe output, complete with a [q] title prefix, automation and workflow-optimization labels, and Copilot as the default reviewer."
- **Our assessment**: This is the first corpus source to name a formal
  three-part "behavior fingerprint" classification scheme (execution style /
  tool breadth / actuation style) for a `gh-aw` agent, with the specific
  labels "directed," "narrow," and "selective_write." No prior note in this
  series documents the existence of this classification system, what other
  label values it can take (e.g., is there an "exploratory" execution style
  or a "broad" tool-breadth counterpart?), or which underlying audit/
  monitoring component produces it — it reads as a pre-existing
  instrumentation feature referenced in passing rather than introduced here.
  For Ch04 (Operations): flag this three-axis behavior classification as a
  named `gh-aw` observability feature worth a dedicated follow-up source (the
  taxonomy of possible values for each axis is not given here and would
  need a docs-type source, e.g. an audit/observability reference page, to
  extract fully).

### Claim 7: Q's `create-pull-request` safe output is configured with three guardrails in combination: unmerged PRs expire after 2 days, patches are capped at 500 files, and edits to protected files automatically convert to a filed issue instead of failing silently

- **Evidence**: Direct statement of the safe-outputs guardrail configuration,
  immediately following the behavior-fingerprint description, framed as a
  deliberate design choice for a workflow with repo-wide write reach.
- **Confidence**: settled (explicit guardrail values stated directly, though
  sourced from the post's prose description rather than a directly fetched
  copy of the workflow's `safe-outputs:` YAML block — see Extraction Notes)
- **Quote**: "That safe-outputs configuration is worth calling out on its own: PRs expire after 2 days if unmerged, patches are capped at 500 files, and protected-file edits automatically fall back to filing an issue instead of silently failing. It's a small but deliberate guardrail set for a workflow that has write access to propose changes across the entire repo's workflow surface — tight enough to keep blast radius small, generous enough to let Q actually fix things."
- **Our assessment**: Each of the three guardrails individually corroborates
  a general mechanism already documented elsewhere in the corpus, but this
  is the first source to show all three applied together to a
  `create-pull-request` safe output specifically. (1) The 2-day PR expiry
  extends the `expires:` field pattern already documented on `create-issue`
  (`expires: 2d`) and `create-discussion` (`expires: 1d`) in the Issue
  Arborist workflow frontmatter (`blog-ghaw-weekly-2026-08-17.md` → Concrete
  Artifacts → "Issue Arborist workflow definition") — this is the first
  corpus example of `expires` applied to a pull-request-producing safe
  output rather than an issue or discussion. (2) A 500-file patch cap is a
  file-count limit distinct from the byte-size `max patch size` limits
  documented in `blog-ghaw-weekly-2026-06-15.md` Claim 5 (1 MB → 4 MB) and
  refined in `blog-ghaw-weekly-2026-04-27.md` Claim 6 (incremental-delta
  measurement) — no prior note documents a file-*count* cap specifically, as
  opposed to a diff-size-in-bytes cap, and this appears to be governed by
  the general all-or-nothing `max` semantics in
  `docs-ghaw-safe-outputs-specification.md` Claim 6 (SP3: exceeding a
  configured max rejects ALL operations of that type, not just the excess),
  though the post does not use the word "max" or confirm this is the same
  mechanism. (3) The protected-file fallback is a named production instance
  of the `fallback-to-issue` protection policy documented generically in
  `docs-ghaw-threat-detection.md` Claim 11 ("converts a hard-block into a
  human review workflow: instead of failing the safe output job with an
  error, the system creates a review issue"). For Ch03 (Safety and
  Verification): use Q's three-guardrail combination as the worked example
  when documenting `expires` + patch-size/file-count caps + `fallback-to-
  issue` as a composable guardrail set specifically appropriate for
  workflows whose write scope covers other workflows' own definitions (a
  higher-blast-radius case than a codemod agent scoped to application code).

### Claim 8: Q's proposed pull requests carry a `[q]` title prefix, `automation` and `workflow-optimization` labels, and Copilot set as the default reviewer

- **Evidence**: Direct statement of the PR metadata conventions, given in the
  same sentence as the guardrail description (Claim 7).
- **Confidence**: settled (explicit, specific metadata values stated
  directly)
- **Quote**: "it... proposes a scoped pull request through its create-pull-request safe output, complete with a [q] title prefix, automation and workflow-optimization labels, and Copilot as the default reviewer."
- **Our assessment**: The `[q]` title-prefix convention parallels the
  `title-prefix` field already documented on Issue Arborist's `create-issue`
  ("[Parent] ") and `create-discussion` ("[Issue Arborist] ") safe outputs in
  `blog-ghaw-weekly-2026-08-17.md` → Concrete Artifacts — this is the same
  configuration field applied to a `create-pull-request` safe output rather
  than `create-issue`/`create-discussion`. Setting Copilot itself as the
  *default reviewer* on an AI-authored PR is a specific, checkable detail
  not previously documented in this series for any of the write-enabled
  codemod agents (Dead Code Removal, Tidy-Upper); those notes describe human
  PR review as the authority gate (`blog-ghaw-agent-of-the-day-2026-05-28.md`
  Claim 7, "Engineers do the judgment call") without stating who is assigned
  as reviewer. Whether "Copilot as the default reviewer" means an AI-driven
  first-pass review before a human merges, or is simply a GitHub reviewer-
  assignment default with no bearing on who ultimately approves, is not
  clarified by the post. For Ch03: flag this as an open question worth
  resolving in a future source — does an AI-assigned-AI-reviewer pattern
  change the human-judgment guarantee documented for other codemod agents in
  this series, or is human merge approval still required regardless of who
  is listed as "reviewer"?

### Claim 9: The post frames Q's value proposition as the *range* of problems handled in one short window — an infrastructure canary, a cost tweak, and a state-persistence upgrade, each from a different person in a different part of the repo — rather than any single fix, summarized as "no scheduling, no queue, just /q and a clear ask"

- **Evidence**: Closing editorial framing of the post, explicitly stating
  what is "interesting" about the three-run sample.
- **Confidence**: anecdotal (author's interpretive framing of three
  hand-picked runs as representative of "the value proposition," not a
  measured claim about typical request diversity or volume)
- **Quote**: "The interesting part isn't any single fix — it's the range. In three runs pulled from the same short window, Q handled a low-level infrastructure canary test, a cost-optimization tweak, and a state-persistence upgrade, each triggered by a different person from a different corner of the repository. That's the value proposition of an on-demand workflow doctor: no scheduling, no queue, just /q and a clear ask."
- **Our assessment**: This framing is the clearest articulation in the
  corpus of what an on-demand, general-purpose diagnostic/fix agent offers
  that a fleet of narrowly-scoped scheduled agents (one agent per fixed task,
  as documented for Dead Code Removal, Tidy-Upper, Issue Arborist,
  Architecture Guardian) does not: it substitutes for having to build, name,
  and schedule a bespoke workflow for each new one-off request, at the cost
  of broader per-run scope (Q must be trusted to correctly interpret an
  arbitrary natural-language ask rather than execute one fixed, pre-vetted
  task). This is a real design tradeoff not previously named explicitly in
  this series: narrow-scheduled-agent-per-task (predictable, auditable,
  narrow blast radius per agent) versus one general on-demand agent (broader
  net utility, but each run's blast radius depends on correctly interpreting
  an open-ended request) — mitigated here specifically by the Claim 7
  guardrail set (expiry, file cap, protected-file fallback) plus Claim 6's
  "directed/narrow/selective_write" behavior classification. Also
  corroborates `docs-ghaw-chatops.md` Claim 1's framing of `slash_command` as
  "human-pull rather than system-push" automation — three separate humans
  each pulled Q into action for their own distinct need, rather than Q
  pushing unsolicited findings on a schedule. This bears on the already-
  resolved-but-`debated` corpus contradiction `C-004` (slash_command:
  recommended HITL mechanism vs. near-zero community success rate, per
  CONTRADICTIONS.md) — Q is a working, first-party-documented, multi-request
  production example of the `slash_command` trigger succeeding across three
  independent invocations, which is compatible with Side A of C-004 (the
  trigger is functional and intended for exactly this use) but does not by
  itself resolve the debate, since it says nothing about the community-wide
  success-rate data underlying Side B.

## Concrete Artifacts

### Q ("The Workflow Doctor"): Technical Specification

```
Persona:        The Workflow Doctor
Workflow name:  Q
Trigger:        /q comment on an issue, pull request, or discussion
                (slash_command trigger, per docs-ghaw-chatops.md)
Self-description (from Q's own frontmatter, per the post):
  "intelligent assistant that answers questions, analyzes repositories,
  and can create PRs for workflow optimizations"
Engine:         Copilot, with SDK mode enabled
Read access:    issues, pull requests, discussions
Hard restriction: never edits its own definition file (q.md)
Mission:        diagnose and improve OTHER workflows in the repository
                (not itself)
```
*Source: GitHub Agentic Workflows blog, "Agent of the Day – August 24, 2026"*

### Q: Three Profiled Runs

```
Run 32726221560
  Trigger:     comment on discussion #55296 (maintainer request)
  Request:     "add a job that tests the github MCP in remote mode without
               using any agentic workflow feature" — infrastructure canary
               test to rule out a runtime/compiler bug, plus an MCP
               handshake message summary
  Duration:    11.5 minutes
  Turns:       1 (single turn)
  Tokens:      25.8k
  Outcome:     successful conclusion; pull request proposal queued

Run 32727642327
  Trigger:     comment on issue #55389
  Request:     "use mai flash model to reduce cost" (verbatim as quoted
               in the post; model name/casing as given, not normalized)
  Outcome:     workflow-level model swap

Run 32726004596
  Trigger:     comment on discussion #55334
  Request:     "update to use repo-memory to store the mined loops" —
               adding persistent state to a previously stateless workflow
  Outcome:     repo-memory persistence added
```
*Source: GitHub Agentic Workflows blog, "Agent of the Day – August 24, 2026"*

### Q: Behavior Fingerprint and Safe-Outputs Guardrails

```
Behavior fingerprint (audit classification, discussion-triggered run):
  Execution style:   directed
  Tool breadth:      narrow
  Actuation style:   selective_write
  Reads before acting: triggering comment, parent issue/discussion,
                       recent logs and audits for the target workflow

create-pull-request safe output guardrails:
  PR expiry:           2 days if unmerged
  Patch cap:           500 files
  Protected-file edits: fall back to filing an issue (does not fail
                        silently)

PR metadata conventions:
  Title prefix:  "[q]"
  Labels:        automation, workflow-optimization
  Default reviewer: Copilot
```
*Source: GitHub Agentic Workflows blog, "Agent of the Day – August 24, 2026"*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-chatops.md` Claim 1 (`slash_command` is "human-pull rather
    than system-push" automation; "no prior source note documents a
    human-initiated trigger for agentic workflows"): Q is the first entry in
    the "Agent of the Day" series to profile a `slash_command`-triggered
    agent, giving that documented trigger mechanism its first named
    production instance in this specific sub-series (Claim 1 here).
  - `blog-ghaw-weekly-2026-06-01.md` Claim 3 (`engine: copilot-sdk` provides
    "direct access to the Copilot SDK runtime, opening up new integration
    patterns"): Q running "on the Copilot engine with SDK mode enabled"
    (Claim 2 here) is the first agent profiled in this series to use that
    engine option, giving it a first named production use case.
  - `docs-ghaw-threat-detection.md` Claim 11 (three protected-file policies,
    including `fallback-to-issue`: "converts a hard-block into a human
    review workflow... creates a review issue"): Q's protected-file
    guardrail (Claim 7 here) is a concrete, named production instance of
    exactly this policy, applied to a workflow whose write scope is other
    workflows' own definitions.
  - `blog-ghaw-weekly-2026-08-17.md` → Concrete Artifacts → Issue Arborist
    workflow definition (`expires: 2d` on `create-issue`, `expires: 1d` on
    `create-discussion`): Q's 2-day PR expiry (Claim 7 here) corroborates
    that `expires` is a recurring, deliberately-chosen guardrail value in
    the 1–2 day range across multiple `gh-aw` workflows and safe-output
    types, not a one-off configuration.

- **Contradicts**: None filed. Reviewed `CONTRADICTIONS.md` in full and the
  eight overlapping "Agent of the Day" / ChatOps / safe-outputs notes read
  for this extraction. `C-004` (slash_command: recommended mechanism vs.
  near-zero community success rate) is an already-resolved (`debated`)
  contradiction that this source bears on as corroborating evidence for Side
  A — see Claim 9's Our assessment — but Q's three successful runs do not
  materially oppose Side B's community failure-rate data (which concerns
  aggregate configuration outcomes across 204 sampled workflows, not
  whether any single well-configured workflow can succeed), so this does
  not meet the MINER.md §4a bar for filing a *new* contradiction. No new
  issue filed.

- **Extends**:
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` (Dead Code Removal Agent),
    `blog-ghaw-agent-of-the-day-2026-08-20.md` (Issue Arborist), and
    `blog-ghaw-agent-of-the-day-2026-08-21.md` (Code Simplifier / Tidy-Upper):
    together with the read-only scheduled audits (Architecture Guardian,
    the Notary) and the event-driven AI Moderator, this series now documents
    a fifth trigger/posture combination: **on-demand, comment-triggered,
    write-enabled diagnostic-and-fix agent** — distinct from event-reactive
    write-enabled (AI Moderator, reacts to PR/issue/comment *events*
    generally), scheduled write-enabled codemod (Dead Code Removal, Tidy-
    Upper, each with one fixed daily task), scheduled write-enabled triage
    (Issue Arborist), and scheduled read-only audit (Architecture Guardian,
    the Notary). Q is the first agent in the series triggered specifically
    by an explicit human command (`/q`) rather than any event or timer, and
    the first whose task is not fixed in advance (it answers whatever the
    triggering comment asks, within its diagnose-and-fix-other-workflows
    remit) rather than one narrowly pre-defined job.
  - `docs-ghaw-safe-outputs-specification.md` Claim 6 (SP3: all-or-nothing
    max-limit rejection) and Claim 8 (SP5: provenance metadata requirement):
    Q's 500-file patch cap (Claim 7 here) is a plausible but unconfirmed
    instance of SP3's all-or-nothing semantics applied to a file count
    rather than an operation count; the post does not use the word "max" or
    otherwise confirm the underlying mechanism, so this is flagged as a
    plausible extension, not a settled one. Q's `[q]` title prefix and
    Copilot-as-default-reviewer (Claim 8 here) are consistent with, but do
    not by themselves confirm, SP5-style provenance metadata (a footer
    identifying workflow source and run) — the post does not describe or
    quote a footer on Q's PRs.
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 7 ("The agent does the
    investigation and the grunt work. Engineers do the judgment call"): Q's
    PR-as-output pattern (Claim 6-7 here) is consistent with this authority-
    boundary framing, but Claim 8's "Copilot as the default reviewer" raises
    an unresolved question (not addressed in either note) about whether an
    AI-assigned-AI-reviewer step changes or supplements that human-judgment
    gate — see Claim 8's Our assessment.

- **Novel**:
  - **On-demand, comment-triggered, write-enabled diagnostic agent as a
    named fifth archetype** (Claim 1, Extends): no prior "Agent of the Day"
    entry profiles an agent triggered purely by an explicit human slash
    command with an open-ended (rather than fixed) task remit.
  - **A three-axis "behavior fingerprint" classification (execution style /
    tool breadth / actuation style)** (Claim 6): the specific labels
    "directed," "narrow," and "selective_write" are not documented in any
    prior corpus source, nor is the classification system that produces
    them.
  - **`expires` applied to `create-pull-request`, not just `create-issue`/
    `create-discussion`** (Claim 7): prior corpus examples of the `expires`
    guardrail field are on issue- and discussion-producing safe outputs; Q
    is the first documented case on a pull-request-producing safe output.
  - **A file-count patch cap (500 files) distinct from byte-size patch
    limits** (Claim 7): prior corpus patch-size guardrails
    (`blog-ghaw-weekly-2026-06-15.md`, `blog-ghaw-weekly-2026-04-27.md`) are
    all byte-size limits (1 MB → 4 MB, incremental-delta measured); no prior
    note documents a file-count limit.
  - **Copilot set as the default reviewer on an AI-authored PR** (Claim 8):
    no prior codemod-agent note in this series states who is assigned as
    reviewer on the agent's own PRs.
  - **A workflow-specific "never edit your own definition file" rule as a
    named restraint distinct from the general protected-files policy**
    (Claim 2): the general protected-files categories in
    `docs-ghaw-threat-detection.md` Claim 10 do not single out one specific
    file by name; Q's rule is scoped to exactly `q.md`.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "on-demand, comment-triggered,
  write-enabled diagnostic/fix agent" as a fifth named agent archetype
  (Claim 1, Extends), completing the trigger × posture taxonomy this series
  has been building: event-driven write-enabled, scheduled write-enabled
  codemod, scheduled write-enabled triage, scheduled read-only audit, and
  now on-demand write-enabled diagnostic. Document Q's request diversity
  (Claims 3–5, 9) as the concrete illustration of this archetype's value
  proposition — one agent substituting for several bespoke scheduled
  workflows, at the cost of needing to correctly interpret open-ended
  natural-language requests rather than executing one fixed task. Add
  "never edit your own definition file" (Claim 2) as a named restraint
  pattern specifically for agents whose write scope includes other
  workflows' configuration.

- **Chapter 03 (Safety and Verification)**: Document Q's three-part
  `create-pull-request` guardrail combination — 2-day expiry, 500-file patch
  cap, protected-file fallback-to-issue (Claim 7) — as a worked example of
  composing existing guardrail mechanisms (`expires`, a patch-size/count
  cap, `fallback-to-issue`) for a workflow whose blast radius spans the
  entire repo's workflow surface. Flag "Copilot as default reviewer on an
  AI-authored PR" (Claim 8) as an open question for the guide to resolve
  with a future source: does this change or supplement the human-merge-
  approval gate documented for other codemod agents in this series? Note
  this source as corroborating (not resolving) evidence for `C-004`'s Side A
  (slash_command as a working, intended HITL mechanism) — see Claim 9.

- **Chapter 06 (Maintenance)**: Add Q's three request categories (build a
  diagnostic canary test to isolate a suspected bug; swap a model for cost
  reduction; retrofit `repo-memory` into a stateless workflow) as concrete
  examples of "workflow maintenance requests a `/q`-style agent can field
  on demand" — useful as a starting checklist for scoping what such an
  agent should be trusted to handle.

## Extraction Notes

1. **Full post fetched via `curl` and read from raw HTML, not only WebFetch
   summary**: An initial WebFetch pass (asked for full verbatim text)
   returned a structured, paraphrased summary (e.g., "Description," "Technical
   Specifications" as bullet restatements rather than the source's own
   prose) — useful for orientation but not citable per MINER.md §2a. The
   page was independently re-fetched via `curl`, and the article body was
   located inside `<div class="sl-markdown-content">` (the second of two
   occurrences of that class name in the raw HTML — the first is inside an
   inline `<script>` block and is not the article). All quotes above are
   copied character-for-character from that raw-HTML extraction, not
   reconstructed from the WebFetch summary. The post is short (roughly 450
   words) and was captured in full in one fetch; no pagination or
   truncation was observed.

2. **No run/issue/discussion URLs followed**: Unlike several other entries
   in this series (e.g. `blog-ghaw-agent-of-the-day-2026-08-21.md`, where
   run and PR numbers are hyperlinked to their GitHub URLs), the fetched
   page renders the three run IDs (32726221560, 32727642327, 32726004596)
   and the issue/discussion numbers (#55296, #55389, #55334) as plain text,
   not links — the raw HTML for this article section contains no `<a href>`
   elements around these identifiers. They are therefore reported here
   exactly as stated in the post but were not independently fetched or
   verified against the underlying GitHub Actions runs, issues, or
   discussions. This is a weaker evidentiary basis than posts in this series
   where the numbers are directly hyperlinked, and is reflected in this
   note's `confidence_overall: emerging` rather than `settled`.

3. **`q.md` workflow definition not fetched separately**: Several prior
   notes in this series (e.g. `blog-ghaw-agent-of-the-day-2026-08-18.md`,
   `blog-ghaw-weekly-2026-08-17.md`) additionally fetched the profiled
   workflow's own YAML frontmatter directly from
   `raw.githubusercontent.com` to corroborate the blog post's claims
   independently. That was not done here: the post gives no repository path
   for `q.md` (unlike, e.g., the Notary post's explicit link to
   `.github/workflows/schema-consistency-checker.md`), so there was no
   specific file path to fetch. Claims 2 and 7 (engine, permissions,
   self-edit rule, and the safe-outputs guardrail configuration) are
   therefore sourced only from the blog post's own paraphrase of Q's
   frontmatter, not from a directly fetched copy of it — flagged
   accordingly in each claim's Confidence/Evidence field.

4. **Nine existing source notes reviewed in full or in relevant part before
   writing Cross-References**: `docs-ghaw-chatops.md`,
   `blog-ghaw-weekly-2026-06-01.md`,
   `docs-ghaw-threat-detection.md`,
   `blog-ghaw-weekly-2026-08-17.md`,
   `docs-ghaw-safe-outputs-specification.md`,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `blog-ghaw-agent-of-the-day-2026-08-20.md`,
   `blog-ghaw-agent-of-the-day-2026-08-21.md`, and
   `blog-ghaw-agent-of-the-day-2026-05-20.md`
   were read in full or in the relevant sections before citing any of them
   above. All `Claim N` citations were checked against the actual numbered
   claims in those notes at the time of writing; the Issue Arborist
   `expires` values are cited by section name ("Concrete Artifacts → Issue
   Arborist workflow definition"), not by an invented claim number, because
   they appear there as a reproduced YAML block rather than inside a
   numbered `### Claim` entry in that note.

5. **`CONTRADICTIONS.md` reviewed; no new contradiction filed, but relevant
   existing entry flagged**: `C-004` (slash_command: recommended HITL
   mechanism, per `docs-ghaw-chatops.md`, vs. near-zero community success
   rate, per `docs-ghaw-editors-reference.md`) is an already-resolved
   (`debated`) contradiction that this source provides corroborating —
   not contradicting, and not conclusively resolving — evidence for. See
   Claim 9's Our assessment and Cross-References → Contradicts for why this
   does not meet the MINER.md §4a bar for a new filing.

6. **Duplicate-triage note**: Three separate Prospector triage comments are
   present on issue #2935, apparently from repeated/parallel triage passes
   on the same auto-filed source. They differ somewhat in exact chapter
   emphasis (one adds Ch06; two focus on Ch02/Ch03/Ch05) and in exactly how
   they name the agent ("diagnostic on-demand workflows" vs. "the Workflow
   Doctor" vs. "workflow doctor responding to /q comments"), but agree on
   the core subject (Q, on-demand slash-command triggering, and the
   safe-outputs guardrail set) and on treating this as a novel, high-value
   entry in the series. This note follows the union of their guidance —
   covering the trigger-taxonomy angle (Ch02), the guardrail-composition
   angle (Ch03), and the maintenance-request-category angle (Ch06) — rather
   than picking one comment over the others.
