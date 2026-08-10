---
source_url: https://github.github.com/gh-aw/blog/2026-08-10-weekly-update/
source_type: blog-post
title: "Weekly Update – August 10, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-08-10
date_extracted: 2026-08-10
last_checked: 2026-08-10
status: current
confidence_overall: emerging
issue: "#2604"
---

# Weekly Update – August 10, 2026 (GitHub Agentic Workflows)

> Two releases landed this week: v0.86.1 (August 7) shipped guided `gh aw fix`
> diagnostics, expanded engine support (Pydantic AI, plus definition-based
> `aider`/`cursor`/`kiro` example workflows), and the new "PureLock" daily
> pure-function test-coverage workflow; v0.86.0 (same day) was a security
> hardening pass enforcing secrets redaction across step summaries,
> patch/bundle artifacts, and MCP gateway diagnostic logs, plus URL-logging
> hardening and a tightened `upload_artifact` safe-output. The Agent of the
> Week spotlight profiles PureLock's first week of runs.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; two dated "Release" sections — v0.86.1 with a
  "What's New" bullet list, and v0.86.0 with a "Security & Redaction" bullet
  list — followed by a "Notable Pull Requests" section of five bullets not
  tied to either release, an "Agent of the Week: PureLock" spotlight, and a
  short "Try It Out" closer)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The page's `schema.org/BlogPosting`
  JSON-LD and on-page byline both name the author as "Copilot" — the same
  non-human byline pattern documented in `blog-ghaw-weekly-2026-08-03.md` and
  prior weekly notes. Verified against the raw page HTML fetched via `curl`
  and parsed with BeautifulSoup (`div.sl-markdown-content`), not a WebFetch
  summary alone (see Extraction Notes).
- **Scope**: Two dated release sections (v0.86.1: four "What's New" bullets;
  v0.86.0: three "Security & Redaction" bullets), one undated "Notable Pull
  Requests" section (five bullets), and one "Agent of the Week" spotlight
  (PureLock, a new agent debuting in this corpus). Does NOT cover: the
  mechanics of how `resolve_pull_request_review_thread` detects a stale node
  ID; what specifically made the prior `DefaultFirewallVersion` digest-pin
  logic lose pins on bumps; the full list of engines gaining "shared engine
  definitions" beyond Pydantic AI; or any workflow YAML/frontmatter syntax
  for the new `*TemplatableBool` config typing.

## Extracted Claims

### Claim 1: v0.86.1 added guided `gh aw fix` diagnostics for restricted `tools.bash` allow-listing and for known external engines missing their import statement (PRs #51102, #51088)

- **Evidence**: "What's New" section, first bullet, naming the tool (`gh aw
  fix`), the two diagnosed scenarios (`tools.bash` allow-listing on engines
  that ignore it; known external engines like `opencode` and `crush` missing
  their import), and two linked PRs.
- **Confidence**: settled (specific PRs, specific tool, specific named
  engines, first-party changelog)
- **Quote**: "The tool now offers a guided fix for restricted `tools.bash`
  allow-listing on engines that ignore it (#51102), plus tips for known
  external engines like opencode and crush missing their import (#51088)."
- **Our assessment**: This extends `docs-ghaw-troubleshooting-debugging.md`
  Claim 13, which documents `gh aw fix --write` as an auto-remediation path
  for *compilation* errors only (diagnosed via `gh aw compile --verbose`).
  This post describes `gh aw fix` diagnosing a different class of problem —
  configuration/engine-compatibility issues (a `tools.bash` allowlist that a
  given engine silently ignores, or a missing import statement for an
  external engine) — rather than compile-time syntax errors. `opencode` and
  `crush` are two of the three "experimental" engines named in
  `docs-ghaw-engines-reference.md` Claim 1 (alongside Pi); that note's Claim
  3 already flags Crush and OpenCode as bypassing the `tools:` allowlist
  entirely (a safety-relevant exclusion), which makes this guided-fix
  scenario ("restricted `tools.bash` allow-listing on engines that ignore
  it") read as `gh aw fix` now surfacing that known allowlist-bypass
  footgun as an actionable diagnostic rather than a silent gap. For Ch02
  (Harness Engineering): document `gh aw fix`'s expanded diagnostic scope
  (compile errors per Claim 13 of the troubleshooting note, now also
  `tools.bash` allowlist mismatches and external-engine import gaps) as a
  reason to run `gh aw fix` proactively, not just after a compile failure.

### Claim 2: v0.86.1 expanded engine support with shared engine definitions and smoke tests for Pydantic AI, plus new example workflows for the definition-based `aider`, `cursor`, and `kiro` engines (PRs #51161, #51166)

- **Evidence**: "What's New" section, second bullet, naming Pydantic AI (with
  "shared engine definitions and smoke tests") and three additional engines
  ("aider, cursor, and kiro definition-based engines") with example
  workflows, linked to two PRs.
- **Confidence**: settled (specific PRs, specific engine names, first-party
  changelog); emerging on what "definition-based engine" means mechanically
  (no elaboration beyond the label)
- **Quote**: "Added shared engine definitions and smoke tests for Pydantic
  AI (#51161), plus new example workflows for the aider, cursor, and kiro
  definition-based engines (#51166)."
- **Our assessment**: None of Pydantic AI, aider, cursor, or kiro appear in
  `docs-ghaw-engines-reference.md` Claim 1's enumeration of the platform's
  seven supported engines (Copilot CLI, Claude, Codex, Gemini, Crush,
  OpenCode, Pi) — all four are novel to this corpus. The phrase
  "definition-based engines" (applied here to aider/cursor/kiro, and
  implicitly to Pydantic AI via "shared engine definitions") suggests a
  distinct integration mechanism from the seven natively-coded engines in
  that reference — possibly a declarative/config-driven engine adapter
  rather than a first-class Go implementation, though this post gives no
  detail on the distinction. For Ch02 (Harness Engineering): flag "engine
  definitions" as a new gh-aw engine-integration mechanism worth a dedicated
  reference-doc mining pass, since it is unclear whether definition-based
  engines have the same feature-parity constraints (max-turns, tools
  allowlist enforcement, etc.) documented for the seven engines in
  `docs-ghaw-engines-reference.md` Claim 3.

### Claim 3: v0.86.1 introduced the "PureLock initiative" — a daily pure-function maximum-coverage test workflow that is progressively locking down core compiler functions with dedicated test suites (PRs #51107, #51167, #51119)

- **Evidence**: "What's New" section, third bullet, naming the initiative,
  its cadence (daily), its target (pure-function maximum coverage), and its
  scope (core compiler functions), linked to three PRs.
- **Confidence**: settled (specific PRs, specific named initiative,
  first-party changelog, corroborated in detail by the Agent of the Week
  section — see Claim 8)
- **Quote**: "Introduced a daily pure-function maximum-coverage test
  workflow (#51107) that is progressively locking down core compiler
  functions with dedicated test suites (#51167, #51119)."
- **Our assessment**: PureLock is architecturally similar to the Dead Code
  Removal Agent profiled in `blog-ghaw-agent-of-the-day-2026-05-28.md` — both
  are daily-scheduled, write-enabled codemod agents targeting the gh-aw Go
  codebase itself, and both fit that note's Claim 2 automation-fitness
  criterion of a "mechanical feedback loop" (build/vet/test pass or fail,
  no ambiguity), here applied to test-writing against measurable coverage
  gaps rather than to code deletion against a "no callers" check. Unlike the
  Dead Code Removal Agent, PureLock's target is explicitly scoped to "core
  compiler functions," a narrower and higher-stakes surface than
  general dead-code cleanup. For Ch02/Ch06: add PureLock as a second named
  example (alongside the Dead Code Removal Agent) of a daily-scheduled,
  narrowly-scoped write-enabled codemod agent applied to a project's own
  codebase — both exemplify "verification-first codemod" automation
  suitable for mechanical, binary-outcome tasks.

### Claim 4: v0.86.1 fixed `add_labels` failing on pull requests in issue-intent paths, and replaced loosely-typed bool-or-expression config fields with `*TemplatableBool` for safer config typing (PRs #51168, #51097)

- **Evidence**: "What's New" section, fourth bullet, naming the safe-output
  function (`add_labels`), the failure scenario ("issue-intent paths"), and
  the typing change (`*TemplatableBool` replacing "loosely-typed
  bool-or-expression fields"), linked to two PRs.
- **Confidence**: settled (specific PRs, specific function and type names,
  first-party changelog); emerging on what "issue-intent paths" means
  mechanically (no further detail given)
- **Quote**: "Fixed `add_labels` failing on pull requests in issue-intent
  paths (#51168) and replaced loosely-typed bool-or-expression fields with
  *TemplatableBool for safer config typing (#51097)."
- **Our assessment**: This is the first corpus mention of an
  `add_labels`-specific bug and of `*TemplatableBool` as a named gh-aw
  config type. "Issue-intent paths" likely refers to a code path where a
  safe-output originally scoped for issues is applied against a PR (PRs and
  issues share numbering/some API surface on GitHub), causing `add_labels`
  to fail when the safe-output's target turns out to be a PR rather than an
  issue — but this is inference, not stated in the post. For Ch02: note
  `*TemplatableBool` as the gh-aw team's fix for bool-or-expression
  frontmatter fields that previously admitted ambiguous types; flag
  "issue-intent paths" as a specific `add_labels` failure mode worth a
  dedicated reference-doc mining pass to confirm the mechanism.

### Claim 5: v0.86.0 enforced secrets redaction in step summaries, patch/bundle artifacts, and MCP gateway diagnostic logs — closing three previously-unredacted leak surfaces (PRs #50777, #50778, #50961)

- **Evidence**: "Security & Redaction" section, first bullet, naming three
  distinct output surfaces (step summaries, patch/bundle artifacts, MCP
  gateway diagnostic logs) and stating secrets could previously leak through
  them, linked to three PRs.
- **Confidence**: settled (three specific PRs, three specific named output
  surfaces, first-party changelog, framed as a fix implying prior absence of
  redaction on these surfaces)
- **Quote**: "Secrets can no longer leak through logs or artifacts.
  Redaction is now enforced in step summaries (#50777), patch/bundle
  artifacts (#50778), and MCP gateway diagnostic logs (#50961)."
- **Our assessment**: No existing source note documents secrets redaction on
  any of these three specific surfaces. `docs-ghaw-network-reference.md`
  Claim 11 documents a *different* redaction mechanism — non-allowlisted
  domain URLs replaced with `(redacted)` in workflow outputs, a
  data-exfiltration defense at the network-egress layer. This post's
  redaction is secrets-in-output redaction (step summaries, artifacts, MCP
  gateway logs), a distinct defense against credential leakage rather than
  URL/domain exfiltration — the two are complementary, not overlapping,
  redaction mechanisms. `docs-ghaw-artifacts-reference.md` documents the
  `agent` artifact (containing execution logs) and does not mention secrets
  redaction being applied to its contents prior to this post. For Ch04
  (Safety and Constraints): add secrets redaction across step summaries,
  patch/bundle artifacts, and MCP gateway diagnostic logs as three
  concrete, dated (v0.86.0, August 7 2026) hardening fixes; note this is a
  distinct redaction layer from the URL-based content sanitization
  documented in `docs-ghaw-network-reference.md` Claim 11 — the guide
  should not conflate "redaction" as a single mechanism when citing gh-aw's
  defenses.

### Claim 6: v0.86.0 hardened URL handling by stripping userinfo from logged URLs and no longer logging rejected URLs in full (PR #50776)

- **Evidence**: "Security & Redaction" section, second bullet, naming both
  the mechanism (userinfo stripping) and the behavior change (rejected URLs
  no longer logged in full), linked to one PR.
- **Confidence**: settled (specific PR, specific before/after logging
  behavior, first-party changelog)
- **Quote**: "URL handling hardened: userinfo is now stripped from logged
  URLs and rejected URLs are no longer logged in full (#50776)."
- **Our assessment**: "Userinfo" in a URL (the `user:password@host` portion)
  is a classic credential-leak vector when URLs are logged verbatim — this
  is a secrets-adjacent fix distinct from Claim 5's artifact/summary
  redaction, targeting gh-aw's own URL-handling/logging code rather than
  step-summary or artifact output. No existing source note documents
  userinfo-stripping from gh-aw logs specifically; `docs-ghaw-network-reference.md`
  Claim 11's `(redacted)` domain substitution is a workflow-output-facing
  behavior for non-allowlisted domains, not a URL-credential-stripping fix
  in gh-aw's internal logging. For Ch04: add userinfo-stripping and
  truncated rejected-URL logging as a fourth named URL/secrets-hardening fix
  in this release, distinct from but thematically aligned with Claim 5's
  artifact/summary redaction — both address credential/sensitive-data
  exposure through gh-aw's own logging surfaces.

### Claim 7: v0.86.0 restricted the `upload_artifact` safe-output to canonical allowed roots and now rejects sensitive paths (PR #50779)

- **Evidence**: "Security & Redaction" section, third bullet, naming the
  safe-output (`upload_artifact`) and the new restriction (canonical
  allowed roots; sensitive-path rejection), linked to one PR.
- **Confidence**: settled (specific PR, specific safe-output name, specific
  restriction described, first-party changelog); emerging on what counts as
  a "sensitive path" (no examples given)
- **Quote**: "`upload_artifact` safe-output now restricts uploads to
  canonical allowed roots and rejects sensitive paths (#50779)."
- **Our assessment**: This is the first corpus mention of `upload_artifact`
  as a named safe-output type with path-scoping restrictions.
  `docs-ghaw-artifacts-reference.md` documents the platform's 9-artifact
  taxonomy (what gh-aw produces) but does not document `upload_artifact` as
  a workflow-author-facing safe-output for uploading arbitrary content — this
  is new detail on a write-path capability, not the read-path taxonomy that
  note covers. The framing ("restricts... rejects sensitive paths") implies
  the pre-fix behavior allowed uploads from a broader path set, which is a
  path-traversal/data-exfiltration-adjacent risk for a safe-output that lets
  agent-selected file content leave the sandbox as a downloadable artifact.
  For Ch04 (Safety and Constraints): add `upload_artifact`'s canonical-root
  restriction and sensitive-path rejection as a concrete safe-output
  hardening example, and flag `upload_artifact` itself as a write-capable
  safe-output worth a dedicated reference-doc mining pass — no existing note
  documents its full behavior or what "sensitive paths" excludes.

### Claim 8: The Agent of the Week spotlight introduces PureLock — during its first profiled week it ran three times (once scheduled, twice via manual dispatch), took 15–22 minutes per run, used roughly 60,000 tokens total, stayed read-only until each run's final PR, and its August 1st run (PR #51586) locked down three named pure functions (`sameExpr`, `addAllowedToNetwork`, `rpcEntryToTimelineEvent`) with test suites

- **Evidence**: "Agent of the Week: PureLock" section, describing the
  agent's function, the three-run week with specific timing/token metrics,
  the read-only-until-final-PR behavior, and the specific PR and function
  names from its most notable run.
- **Confidence**: settled for the specific run-data figures (three runs,
  15–22 minutes each, ~60K tokens total, PR #51586 naming three functions)
  — first-party, specific, verifiable against the linked PR; emerging for
  the "quiet... unglamorous, repetitive work" editorial framing, which is
  narrative characterization rather than a measured claim
- **Quote**: "PureLock is the daily workflow that quietly locks down up to
  three uncovered pure Go functions per run, writing dedicated test suites
  so core compiler logic doesn't regress unnoticed." Run data: "This week
  PureLock ran three times — once from its daily schedule and twice via
  manual dispatch — clocking in at 15 to 22 minutes per run and burning
  through roughly 60,000 tokens total. All three runs completed successfully
  and stayed strictly read-only until their final PR, methodically chipping
  away at coverage gaps. Its handiwork showed up directly in this week's
  release notes, with #51586 locking down sameExpr, addAllowedToNetwork, and
  rpcEntryToTimelineEvent with pure-function test suites." Usage tip: "Pair
  a coverage-locking workflow like this with your CI's coverage gate so
  newly written tests actually prevent regressions instead of just padding a
  report."
- **Our assessment**: This is the first appearance of PureLock in this
  corpus and the first Agent of the Week/Day spotlight to profile an agent
  in the same post that announces its initiative launch (Claim 3), rather
  than spotlighting a previously-shipped agent — unlike the "repeat
  spotlight" pattern `blog-ghaw-weekly-2026-08-03.md` Claim 11 documents for
  the Dead Code Removal Agent (a prior agent revisited with new data), this
  is a same-week launch-and-profile. "Strictly read-only until their final
  PR" echoes the read-only-until-output posture
  `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 3 documents for the Dead
  Code Removal Agent (a PR-as-output, human-reviewed write pattern), giving
  a second concrete instance of that posture for a different write-enabled
  codemod agent. The usage tip — pairing coverage-locking agents with a CI
  coverage gate — is new prescriptive guidance not present for the Dead
  Code Removal Agent's usage tip in either prior note. For Ch02/Ch06: add
  PureLock's first-week metrics (3 runs, 15–22 min/run, ~60K tokens total,
  read-only until final PR) as a second concrete token/time budget data
  point for a daily-scheduled Go-codebase codemod agent, alongside the Dead
  Code Removal Agent's ~43K-tokens/three-run figure from
  `blog-ghaw-weekly-2026-08-03.md` Claim 11; add the CI-coverage-gate
  pairing usage tip as a named best practice for coverage-locking agent
  workflows.

### Claim 9: `resolve_pull_request_review_thread` was made more resilient to stale GraphQL node IDs by skipping them instead of failing the safe-output (PR #51630)

- **Evidence**: "Notable Pull Requests" section, first bullet, giving the PR
  title verbatim ("Skip stale review-thread node IDs instead of failing
  safe_outputs") plus an explanatory clause.
- **Confidence**: settled (specific PR, specific function name, specific
  before/after failure behavior stated, first-party changelog)
- **Quote**: "Skip stale review-thread node IDs instead of failing
  safe_outputs — makes resolve_pull_request_review_thread more resilient to
  stale GraphQL node IDs."
- **Our assessment**: This is the first corpus mention of
  `resolve_pull_request_review_thread` as a named gh-aw safe-output
  function. The fix pattern (skip-and-continue rather than fail-the-whole-run
  on a single stale reference) is a reliability posture distinct from the
  redaction/hardening fixes in Claims 5–7, addressing a resilience gap
  rather than a security exposure. For Ch06 (Agentic Operations): note
  `resolve_pull_request_review_thread` as a named safe-output function whose
  reliability was improved this release — relevant to any workflow that
  programmatically resolves PR review threads and previously risked a
  full-run failure from one stale GraphQL reference.

### Claim 10: Sandboxed agentic engines were granted read/write access to `/tmp/gh-aw` in the AWF sandbox, addressing engines that need scratch space during sandboxed runs (PR #51608)

- **Evidence**: "Notable Pull Requests" section, second bullet, naming the
  path (`/tmp/gh-aw`), the access level (read/write), and the context
  (AWF sandbox), plus an explanatory clause about scratch-space needs.
- **Confidence**: settled (specific PR, specific path and access level
  named, first-party changelog)
- **Quote**: "Grant agentic engines read/write access to /tmp/gh-aw in AWF
  sandbox — smooths out sandboxed engine runs that need scratch space."
- **Our assessment**: This is the first corpus mention of `/tmp/gh-aw` as a
  named, dedicated scratch-space path within the AWF (Agentic Workflow
  Firewall) sandbox. It implies sandboxed engines previously lacked a
  writable scratch directory, which would have broken or complicated any
  engine/tool behavior expecting standard temp-file write access. For Ch04
  (Safety and Constraints) or Ch02: note `/tmp/gh-aw` as the sandbox's
  designated writable scratch path — relevant when debugging sandboxed
  engine runs that fail on temp-file writes, and worth flagging that this
  path (not arbitrary `/tmp` locations) is the sanctioned scratch area.

### Claim 11: A recurring bug caused `gh-aw-firewall` to lose its digest pin whenever `DefaultFirewallVersion` was bumped; this was fixed to keep firewall image pins from silently drifting on version bumps (PR #51423)

- **Evidence**: "Notable Pull Requests" section, third bullet, naming the
  component (`gh-aw-firewall`), the trigger (`DefaultFirewallVersion`
  bumps), and the failure mode (digest-pin loss), plus an explanatory
  clause calling out silent drift.
- **Confidence**: settled (specific PR, specific component and trigger
  named, "recurring" framing implies this had happened more than once,
  first-party changelog)
- **Quote**: "Fix recurring gh-aw-firewall digest-pin loss on
  DefaultFirewallVersion bumps — keeps firewall image pins from silently
  drifting on version bumps."
- **Our assessment**: Digest pinning (pinning a container image to an
  immutable content hash rather than a mutable tag) is a supply-chain
  integrity control; losing the pin on a version bump means the firewall
  container could silently resolve to an unpinned/mutable reference,
  undermining that control exactly when the version changes. The
  "recurring" framing is notable — it implies this class of bug was not
  fully fixed on a prior occurrence, though this post gives no reference to
  an earlier fix attempt. No existing source note documents
  `DefaultFirewallVersion` or digest-pin loss for `gh-aw-firewall`
  specifically. For Ch04: add this as a concrete example of a supply-chain
  integrity control (digest pinning) that had a recurring implementation
  bug in gh-aw's own release-bump tooling — worth noting as a caution that
  "we pin by digest" claims should be periodically re-verified rather than
  assumed durable across version bumps.

### Claim 12: An explicit end-marker syntax was added for inline skills and sub-agents to clarify where inline skill/sub-agent content ends within workflow markdown (PR #51446)

- **Evidence**: "Notable Pull Requests" section, fourth bullet, naming the
  feature (explicit end marker syntax) and its purpose (clarifying content
  boundaries for inline skills and sub-agents in workflow markdown).
- **Confidence**: emerging (specific PR and feature named, first-party
  changelog, but no example of the marker syntax itself is given)
- **Quote**: "Add explicit end marker syntax for inline skills and
  sub-agents — clarifies where inline skill and sub-agent content ends in
  workflow markdown."
- **Our assessment**: This implies gh-aw's workflow-markdown format allows
  authoring inline skills and sub-agents directly within a workflow file
  (rather than only referencing external files), and that the boundary
  between such inline content and the rest of the workflow markdown was
  previously ambiguous enough to need an explicit end marker.
  `docs-ghaw-inline-sub-agents.md` documents inline sub-agents as a concept;
  this post's fix is a syntax-parsing detail for that feature not
  necessarily captured there (not independently verified against that
  note's claim numbers in this pass). For Ch02: flag explicit end-marker
  syntax as a recent parsing change for inline skills/sub-agents in workflow
  markdown, worth cross-checking against `docs-ghaw-inline-sub-agents.md`
  for whether that note's examples predate this syntax change.

### Claim 13: Copilot engine path handling was fixed for portability across different CI runner platforms (PR #51275)

- **Evidence**: "Notable Pull Requests" section, fifth bullet: "Fix Copilot
  path portability across runners — irons out cross-platform path handling
  for the Copilot engine."
- **Confidence**: emerging (specific PR and engine named, first-party
  changelog, but no detail on which runner platforms or what path handling
  broke)
- **Quote**: "Fix Copilot path portability across runners — irons out
  cross-platform path handling for the Copilot engine."
- **Our assessment**: This is a narrow, low-detail bug-fix bullet — likely a
  Windows/Linux/macOS runner path-separator or absolute-path issue specific
  to the Copilot engine, but the post gives no specifics. For Ch02: note
  only as a minor reliability fix; not detailed enough to add concrete
  guidance beyond "Copilot engine cross-runner path handling was buggy
  before v0.86.0/v0.86.1 and has since been fixed."

## Concrete Artifacts

### Release Summary: v0.86.0 and v0.86.1 (August 7, 2026)

```
Opening framing: "It's been another busy week in github/gh-aw, with two
notable releases and dozens of merged pull requests touching everything from
compiler safety to CI stability. Here's what shipped."

Release: v0.86.1 — August 7
  "landed on August 7th with a broad set of compiler safety fixes, new gh aw
  fix diagnostics, and expanded engine support."
  What's New:
    Guided `gh aw fix` diagnostics: restricted tools.bash allow-listing on
      engines that ignore it (#51102); tips for known external engines
      (opencode, crush) missing their import (#51088)
    Expanded engine support: shared engine definitions + smoke tests for
      Pydantic AI (#51161); example workflows for aider/cursor/kiro
      definition-based engines (#51166)
    PureLock initiative: daily pure-function maximum-coverage test workflow
      (#51107), progressively locking down core compiler functions (#51167,
      #51119)
    Safe-outputs improvements: fixed add_labels failing on PRs in
      issue-intent paths (#51168); replaced bool-or-expression fields with
      *TemplatableBool (#51097)

Release: v0.86.0 — August 7 (same day)
  "shipped earlier the same day as a heavy security and reliability
  hardening pass across secret redaction, MCP gateway logging, and
  threat-detection resilience."
  Security & Redaction:
    Secrets redaction enforced: step summaries (#50777), patch/bundle
      artifacts (#50778), MCP gateway diagnostic logs (#50961)
    URL handling hardened: userinfo stripped from logged URLs; rejected
      URLs no longer logged in full (#50776)
    upload_artifact safe-output restricted to canonical allowed roots;
      rejects sensitive paths (#50779)

Notable Pull Requests (not tied to either dated release):
  Skip stale review-thread node IDs instead of failing safe_outputs —
    resolve_pull_request_review_thread resilience (#51630)
  Grant agentic engines read/write access to /tmp/gh-aw in AWF sandbox
    (#51608)
  Fix recurring gh-aw-firewall digest-pin loss on DefaultFirewallVersion
    bumps (#51423)
  Add explicit end marker syntax for inline skills and sub-agents (#51446)
  Fix Copilot path portability across runners (#51275)
```

*Source: this week's blog post, "Release: v0.86.1", "Release: v0.86.0", and
"Notable Pull Requests" sections, raw HTML fetched via `curl` and parsed
with BeautifulSoup, 2026-08-10*

### Agent of the Week: PureLock — launch week profile

```
Agent:            PureLock (new; first profiled this post)
Function:         Daily workflow; locks down up to three uncovered pure Go
                  functions per run with dedicated test suites
Window:           First profiled week (as of 2026-08-10 post)
Run count:        3 (1 scheduled, 2 manual dispatch)
Duration:         15-22 minutes per run
Tokens:           ~60,000 total (across the three-run window)
Status:           All 3 runs completed successfully; strictly read-only
                  until each run's final PR
Notable run:      August 1 (PR #51586) — locked down sameExpr,
                  addAllowedToNetwork, and rpcEntryToTimelineEvent with
                  pure-function test suites

Usage tip (from source):
  Pair a coverage-locking workflow like this with your CI's coverage gate
  so newly written tests actually prevent regressions instead of just
  padding a report.

Workflow definition:
  https://github.com/github/gh-aw/blob/main/.github/workflows/purelock.md
```

*Source: this week's blog post, "Agent of the Week: PureLock" section, raw
HTML fetched via `curl`, 2026-08-10*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 3 (Dead Code Removal
    Agent stays read-only, investigating, until it has a complete fix,
    then submits a single PR — PR-as-output, human-reviewed write pattern):
    Claim 8 here ("strictly read-only until their final PR" for PureLock)
    is a second, independent instance of the same read-only-until-output
    posture for a different daily-scheduled write-enabled codemod agent.
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 2 (dead code removal
    is automation-suitable because its verification feedback loop is
    entirely mechanical — build/vet/test pass or fail): Claim 3 here
    (PureLock targets pure functions specifically, verified by test-suite
    pass/fail against a coverage target) corroborates the same
    mechanical-feedback-loop automation-fitness criterion applied to a
    different codemod task.

- **Contradicts**: None filed at the MINER.md §4a threshold. No claim in
  this post materially opposes any existing source note's claim on the
  same object; see Extraction Notes for a naming/scope note (not a
  contradiction) on `gh aw fix`'s diagnostic scope.

- **Extends**:
  - `docs-ghaw-troubleshooting-debugging.md` Claim 13 (`gh aw fix --write`
    auto-remediates compilation errors diagnosed via `gh aw compile
    --verbose`): Claim 1 here extends `gh aw fix`'s documented diagnostic
    scope beyond compile errors to `tools.bash` allow-listing mismatches
    and external-engine import gaps.
  - `docs-ghaw-engines-reference.md` Claim 1 (seven supported engines:
    Copilot, Claude, Codex, Gemini, Crush, OpenCode, Pi) and Claim 3
    (Crush/OpenCode bypass the `tools:` allowlist): Claim 2 here adds four
    engines (Pydantic AI, aider, cursor, kiro) not in that reference's
    enumeration, under a new "definition-based engine" label; Claim 1
    here's guided-fix scenario for `tools.bash` allow-listing plausibly
    relates to the allowlist-bypass gap that reference's Claim 3 documents
    for Crush/OpenCode specifically.
  - `docs-ghaw-network-reference.md` Claim 11 (non-allowlisted domain URLs
    replaced with `(redacted)` in workflow outputs — a data-exfiltration
    defense at the network-egress layer): Claims 5 and 6 here document a
    distinct redaction layer (secrets-in-output redaction across step
    summaries/artifacts/MCP logs; URL-userinfo stripping in gh-aw's own
    logging) — related in theme (both are gh-aw redaction mechanisms) but
    operating on different data (credentials/secrets vs. non-allowlisted
    domain URLs) and different surfaces (internal logs/artifacts vs.
    workflow-visible output).
  - `docs-ghaw-artifacts-reference.md` (9-artifact taxonomy for what gh-aw
    produces, including the `agent` artifact containing execution logs):
    Claim 5 here adds that secrets redaction is now enforced on
    patch/bundle artifact contents and on MCP gateway diagnostic logs,
    detail not present in that reference's taxonomy.
  - `blog-ghaw-weekly-2026-08-03.md` Claim 11 (Dead Code Removal Agent
    three-run window: ~43K tokens total, 0 errors/0 warnings): Claim 8 here
    gives a second daily-codemod-agent token/time budget data point
    (PureLock: ~60K tokens, 15-22 min/run, 3 runs) for comparison across
    different gh-aw self-maintenance agents.

- **Novel**:
  - **PureLock** (Claims 3, 8): a new daily-scheduled, write-enabled
    codemod agent debuting in this post, targeting pure-function test
    coverage in gh-aw's own Go compiler code — the first corpus mention of
    this agent.
  - **"Definition-based engines" as an engine-integration category**
    (Claim 2): Pydantic AI, aider, cursor, and kiro are all new to the
    corpus's engine roster, introduced under a label not used for any of
    the seven engines in `docs-ghaw-engines-reference.md`.
  - **Secrets redaction across step summaries, patch/bundle artifacts, and
    MCP gateway diagnostic logs** (Claim 5): the first corpus documentation
    of secrets-redaction enforcement on these three specific output
    surfaces.
  - **`/tmp/gh-aw` as the AWF sandbox's designated scratch path**
    (Claim 10): the first corpus mention of this specific sandbox
    filesystem convention.
  - **`upload_artifact` as a named, path-restricted safe-output**
    (Claim 7): the first corpus mention of this safe-output function and
    its canonical-root/sensitive-path restrictions.
  - **Digest-pin loss on `gh-aw-firewall` version bumps** (Claim 11): the
    first corpus mention of `DefaultFirewallVersion` and a recurring
    digest-pinning bug in gh-aw's own firewall-image release tooling.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Document `gh aw fix`'s expanded diagnostic scope (Claim 1) — compile
    errors (per `docs-ghaw-troubleshooting-debugging.md` Claim 13) plus now
    `tools.bash` allowlist mismatches and external-engine import gaps — as
    a reason to run `gh aw fix` proactively.
  - Flag "definition-based engines" (Claim 2: Pydantic AI, aider, cursor,
    kiro) as a new gh-aw engine-integration mechanism distinct from the
    seven engines in `docs-ghaw-engines-reference.md`, worth a dedicated
    reference-doc mining pass to determine feature-parity implications.
  - Add PureLock (Claims 3, 8) as a second concrete example of a
    daily-scheduled, narrowly-scoped write-enabled codemod agent, with
    first-week metrics (3 runs, 15-22 min/run, ~60K tokens) for comparison
    against the Dead Code Removal Agent's ~43K-tokens/three-run figure.
  - Note `*TemplatableBool` (Claim 4) as the fix for previously
    loosely-typed bool-or-expression frontmatter fields.
  - Flag explicit end-marker syntax for inline skills/sub-agents (Claim 12)
    as worth cross-checking against `docs-ghaw-inline-sub-agents.md`.

- **Chapter 04 (Safety and Constraints)**:
  - Add secrets redaction across step summaries, patch/bundle artifacts,
    and MCP gateway diagnostic logs (Claim 5) as three concrete, dated
    hardening fixes, explicitly distinct from the URL/domain redaction
    mechanism in `docs-ghaw-network-reference.md` Claim 11 — the guide
    should describe gh-aw as having multiple, distinct redaction layers,
    not a single unified one.
  - Add URL userinfo-stripping and truncated rejected-URL logging
    (Claim 6) as a fourth named credential/secrets-hardening fix in this
    release.
  - Add `upload_artifact`'s canonical-root restriction and sensitive-path
    rejection (Claim 7) as a concrete safe-output hardening example, and
    flag `upload_artifact` as a write-capable safe-output needing a
    dedicated reference pass.
  - Note `/tmp/gh-aw` (Claim 10) as the AWF sandbox's sanctioned writable
    scratch path.
  - Add the recurring `gh-aw-firewall` digest-pin loss on version bumps
    (Claim 11) as a caution that digest-pinning supply-chain controls
    should be periodically re-verified, not assumed durable across a
    project's own version-bump tooling.

- **Chapter 06 (Agentic Operations)**:
  - Add PureLock's first-week run data (Claim 8) alongside the Dead Code
    Removal Agent's run data as a second data point for daily-codemod-agent
    token/time budgeting; add the CI-coverage-gate pairing usage tip as
    named best practice for coverage-locking agent workflows.
  - Note `resolve_pull_request_review_thread`'s skip-stale-node-ID fix
    (Claim 9) as a named safe-output reliability improvement.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with BeautifulSoup**, following
   the practice established in prior weekly notes (see
   `blog-ghaw-weekly-2026-08-03.md` Extraction Note 1) after that note found
   WebFetch summaries lossy (renamed items, dropped PR numbers). For this
   post, an initial WebFetch pass similarly compressed distinct items (e.g.,
   merging the "Notable Pull Requests" bullets into unlisted prose and
   omitting several PR numbers and the exact `*TemplatableBool`/
   `upload_artifact`/`/tmp/gh-aw` terms). All quotes and PR numbers in this
   note come from the `curl`-fetched HTML, parsed via
   `BeautifulSoup(...).select_one('div.sl-markdown-content')` and read as
   per-tag text (`h2`/`h3`/`p`/`li`/`code`), cross-checked against the raw
   `<a href>` targets for each `#NNNNN` PR reference to confirm PR numbers
   resolve to `github.com/github/gh-aw/pull/<N>`.
2. **No sub-pages followed beyond link verification.** This is a single
   blog post page. It links out to two release tags (v0.86.0, v0.86.1),
   thirteen PR pages (#51102, #51088, #51161, #51166, #51107, #51167,
   #51119, #51168, #51097, #50777, #50778, #50961, #50776, #50779, #51630,
   #51608, #51423, #51446, #51275, #51586 — twenty distinct PRs total
   across both releases, Notable PRs, and the PureLock spotlight), and the
   `purelock.md` workflow definition file. PR/href targets were checked to
   confirm the linked issue numbers, but individual PR pages were not
   independently fetched or read for additional detail beyond the blog
   post's own bullet text.
3. **`gh aw fix`'s diagnostic-scope extension (Claim 1) is a scope
   observation, not a contradiction.** `docs-ghaw-troubleshooting-debugging.md`
   Claim 13 describes `gh aw fix --write` narrowly as compile-error
   auto-remediation; this post describes `gh aw fix` (without the
   `--write` flag mentioned) offering "guided fixes" for allowlist and
   import-statement issues. Both could be true of the same evolving tool at
   different points in time — no direct conflict, just an expanded feature
   set consistent with ongoing tool development. Noted under Extends, not
   filed as a contradiction.
4. **Cross-reference verification.** Reviewed
   `docs-ghaw-troubleshooting-debugging.md`,
   `docs-ghaw-engines-reference.md`, `docs-ghaw-network-reference.md`,
   `docs-ghaw-artifacts-reference.md`, `docs-ghaw-mcp-gateway-reference.md`,
   `docs-ghaw-inline-sub-agents.md` (existence/topic only — claim numbers
   not individually re-verified for the Claim 12 cross-check, flagged
   above as a follow-up), `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `blog-ghaw-weekly-2026-08-03.md`, and `docs-ghaw-frontmatter-full-reference.md`
   (grepped for `TemplatableBool` — no match, confirming Claim 4's typing
   change is not previously documented), plus `CONTRADICTIONS.md` for
   existing open contradiction entries potentially relevant to this post's
   claims (none found). All `Claim N` citations above were checked against
   the cited note's actual numbered claims before writing.
