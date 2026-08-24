---
source_url: https://github.github.com/gh-aw/blog/2026-08-23-from-conformance-failure-to-eslint-rule/
source_type: blog-post
title: "One Small Error Message, One Big Feedback Loop"
author: GitHub Agentic Workflows team (bylined "Copilot" and "Peli de Halleux")
date_published: 2026-08-23
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: emerging
issue: "#2908"
---

# One Small Error Message, One Big Feedback Loop

> Traces a single production incident in `github/gh-aw` — a daily Safe Outputs
> conformance check flags an `[object Object]` error message, the investigation
> uncovers a real MCP error-serialization edge case, a targeted PR fixes it, and
> a scheduled "ESLint Miner" workflow turns the fix into a preventative lint
> rule — as a concrete illustration of detect → repair → prevent as reusable
> maintenance infrastructure, not a one-off bug fix.

## Source Context

- **Type**: blog-post (GitHub Agentic Workflows blog, `blog/2026-08-23-from-conformance-failure-to-eslint-rule/`)
- **Author credibility**: First-party account from the gh-aw team, bylined to
  "Copilot" and "Peli de Halleux" (per the page's JSON-LD author metadata; Peli
  de Halleux runs GitHub Next / Microsoft Research and authors the "Agent
  Factory" series covered elsewhere in this corpus). The post cites specific,
  traceable artifacts from the `github/gh-aw` repository itself: issue #55014,
  PR #55042, PR #55052, run `#32621246743`, and named files
  (`mcp_server_core.cjs`, `error_helpers.cjs`, `dispatch_workflow.cjs`,
  `route_slash_command.cjs`, `log_parser_shared.cjs`, `safeoutputs_cli.cjs`).
  High credibility for the described mechanics — this is a first-party report
  of the team's own production incident, not a third-party analysis.
- **Scope**: Covers one incident end-to-end: the daily conformance checker that
  found the bug, the specific bug and its fix, and the scheduled miner workflow
  that generalized the fix into a lint rule. Does NOT cover: the full list of
  conformance checks the Daily Safe Outputs Conformance Checker runs (only
  MCE-006 is discussed), the ESLint Miner's workflow YAML or trigger
  configuration, the full contents of PR #55042 or PR #55052 beyond the
  summarized diff intent, or how many prior MCE-006-style checks exist in the
  Safe Outputs conformance suite.

## Extracted Claims

### Claim 1: The post's central thesis is that the value of this incident is the loop connecting the artifacts (issue, repair PR, lint-rule PR), not any single artifact
- **Evidence**: Stated explicitly in the second paragraph and restated as the
  closing section's title and argument.
- **Confidence**: settled (explicit authorial thesis, stated twice)
- **Quote**: "One check became issue #55014, a focused repair in PR #55042, and a preventative lint rule proposed in PR #55052. The interesting part is not any one of those artifacts. It is the loop between them."
- **Our assessment**: This framing is the organizing claim of the whole post —
  everything else (the specific bug, the specific fix, the specific rule) is
  presented as an instance of a general maintenance-loop shape. It is worth
  treating skeptically as a single-incident narrative (see Claim 9), but the
  shape itself — detect via automated check, investigate past the surface
  symptom, repair, then generalize the repair into a preventative check — is a
  concrete, reproducible pattern independent of whether this specific bug was
  significant.

### Claim 2: The Daily Safe Outputs Conformance Checker runs a fixed script daily against the Safe Outputs implementation, groups results by severity and check ID, and converts high-severity failures into short-lived issues that get replaced rather than accumulated
- **Evidence**: Described in the "A tiny signal worth following" section as the
  checker's operating mechanics.
- **Confidence**: settled (first-party description of a named, currently-running script)
- **Quote**: "Every day, the checker runs scripts/check-safe-outputs-conformance.sh against the Safe Outputs implementation. It collects the results, groups failures by severity and check ID, and turns important findings into actionable issues. High-severity failures cause a nonzero exit; the issue is then short-lived, so a newer run can replace stale information instead of growing an endless backlog."
- **Our assessment**: The "short-lived issue, replaced by a newer run" design
  is the notable operational detail here: it avoids the common failure mode of
  scheduled-check workflows where every run files a new issue and the tracker
  fills with duplicates or stale reports. A newer conformance run superseding
  the previous run's issue (rather than filing alongside it) is a concrete
  anti-noise mechanism distinct from the per-category/instance-threshold
  aggregation documented elsewhere in this corpus (see Cross-References).

### Claim 3: The specific defect (check MCE-006) was that `getErrorMessage()` in `error_helpers.cjs` could fall back to whole-object stringification when a thrown object had a non-string `message` property, producing the unhelpful string `[object Object]`
- **Evidence**: Described in the "A tiny signal worth following" section with a
  concrete example input.
- **Confidence**: settled (specific code-level root cause with a reproducing example)
- **Quote**: "If code threw a plain object with a non-string message, the helper could fall back to String(error). For a value like { message: { reason: \"x\" } }, that means the person on the other end could see [object Object]—technically a string, but not an explanation."
- **Our assessment**: This is a narrow but realistic JavaScript error-handling
  footgun: `String(error)` on a plain object with no custom `toString` always
  produces `[object Object]`, which is syntactically a string (so type checks
  pass) but conveys nothing to a human or downstream consumer. The bug is
  interesting specifically because it would not be caught by type-level checks
  — only by a check that inspects the actual runtime content of the message.

### Claim 4: The checker's initial signal looked like a plausible false positive — it detected direct `String(e.message)` calls in `mcp_server_core.cjs`, even though that file actually delegates to a shared helper — but the investigation followed the helper instead of dismissing the finding, and that is what surfaced the real bug
- **Evidence**: Described sequentially: first the surface-level detection
  method, then the explicit statement that this could have ended the
  investigation, then the pivot to following the helper.
- **Confidence**: anecdotal (a single incident's investigative narrative; no
  broader claim about how often surface-level conformance signals are
  false-positive vs. real)
- **Quote**: "At first glance, it looked like the checker had simply missed an abstraction: it searched mcp_server_core.cjs for direct calls such as String(e.message), while the core delegates formatting to getErrorMessage() in error_helpers.cjs." / "That could have been the end of the investigation: another false positive to tune away. Instead, the generated issue followed the helper."
- **Our assessment**: This is the most transferable operational lesson in the
  post: a conformance check that appears to be flagging an abstraction it
  doesn't understand (i.e., "the code doesn't literally match the pattern I'm
  looking for, because it correctly delegates to a helper") is not
  automatically a false positive to silence — it can be a prompt to inspect
  the delegated implementation itself. Tuning away signals that look like
  false positives without inspecting what they point to risks losing genuine
  bugs, as happened here.

### Claim 5: The fix (PR #55042) made the fallback logic explicit — preserve or coerce a string `message` when a non-`Error` object has one, and reserve whole-object stringification for objects that have no `message` property at all — backed by new tests for numeric and non-primitive message values
- **Evidence**: Described in the "Fix the bug—and improve the question" section.
- **Confidence**: settled (specific description of the shipped fix's logic and test coverage)
- **Quote**: "PR #55042 makes the intent explicit: when a non-Error object has a message property, preserve a string message or coerce that message value. Only objects without a message use the whole-object fallback. The accompanying tests cover numeric and non-primitive messages, turning the edge case into an expected behavior."
- **Our assessment**: The phrase "turning the edge case into an expected
  behavior" describes the standard verification discipline for a bug fix: the
  previously-unhandled input (a non-string `message`) is now covered by an
  explicit test, so a future regression would be caught mechanically rather
  than rediscovered by another conformance run months later.

### Claim 6: The conformance check itself (MCE-006) was revised alongside the fix so that it validates a property (does the implementation produce a readable message?) rather than a specific implementation shape (does the code call a particular function?) — stated as a general principle for writing durable conformance checks
- **Evidence**: Described in the "Fix the bug—and improve the question"
  section as the second half of PR #55042's improvement.
- **Confidence**: emerging (a general design principle asserted from a single
  instance of applying it — the post does not cite other conformance checks
  that were redesigned this way)
- **Quote**: "The repair also improves MCE-006 itself. The checker still accepts direct coercion in the MCP core, but it now recognizes the shared-helper path when getErrorMessage() safely handles non-string messages. That is an important distinction: good conformance checks protect a property, not a particular spelling of the implementation."
- **Our assessment**: This is a specific, actionable principle for anyone
  writing static/conformance checks in an agentic-workflow codebase: a check
  written against one literal code shape (e.g., "must call
  `String(x.message)` directly") will produce false positives against any
  correct refactor (e.g., delegating to a shared helper) unless the check is
  redefined against the underlying property the code must satisfy. This
  generalizes beyond MCE-006 to any conformance or lint rule that risks
  coupling to implementation detail rather than behavior.

### Claim 7: A separate scheduled "ESLint Miner" workflow — which mines recent issues and discussions, scans a fixed target directory, selects a single low-false-positive rule candidate, validates it, and opens at most one draft PR per run — used MCE-006 as its seed input to ask whether the same failure pattern exists elsewhere in the codebase
- **Evidence**: Described in the "Then ask: where else does this pattern
  live?" section, with the specific run dated August 23.
- **Confidence**: settled (first-party description of the workflow's operating
  constraints and its specific August 23 run, though only one run is described)
- **Quote**: "The scheduled ESLint Miner mines recent issues and discussions, scans actions/setup/js, selects one low-false-positive rule, validates it, and opens at most one draft PR. Its August 23 run used MCE-006 as the seed for a broader question: is this pattern hiding elsewhere?"
- **Our assessment**: The self-limiting constraints (one rule, one directory
  per run, at most one draft PR) mirror a restraint-by-design pattern seen
  elsewhere in the gh-aw corpus for write-enabled agents (see
  Cross-References): rather than proposing many rules or rewriting broadly,
  the miner narrows its output to a single reviewable proposal per run. Using
  a just-fixed bug as a seed query — "does this exact failure shape recur
  elsewhere?" — is a concrete technique for converting one bug fix into a
  systematic sweep, rather than treating each occurrence as an independent
  discovery.

### Claim 8: The proposed rule (`no-string-fallback-for-non-string-message`, PR #55052) is deliberately a warning rather than an automatic rewrite, because choosing a readable fallback message requires local judgment; the miner found four live occurrences of the pattern in `actions/setup/js`
- **Evidence**: Described in the "Then ask: where else does this pattern
  live?" section, including the explicit rule name, its detection shape, and
  the four named files where it recurred.
- **Confidence**: settled (specific rule name, detection logic description, and enumerated file list)
- **Quote**: "The result is the proposed no-string-fallback-for-non-string-message rule in PR #55052. It looks for a narrow shape: code confirms that x.message is a string, returns it when it is, then falls back to String(x) instead of String(x.message). The rule is a warning, not an automatic rewrite, because a readable fallback still needs local judgment."
- **Our assessment**: This is a concrete design decision worth generalizing:
  not every lint rule discovered from a bug fix should auto-rewrite. When the
  "correct" fix depends on what a good fallback message should say for that
  specific call site (local judgment), a warning that surfaces the pattern —
  without silently rewriting code — is the safer default. The four
  occurrences found (`dispatch_workflow.cjs`, `route_slash_command.cjs`,
  `log_parser_shared.cjs`, `safeoutputs_cli.cjs`) are each left as separate,
  human-reviewed fix decisions rather than being auto-patched in bulk.

### Claim 9: The post explicitly frames the overall system as a "maintenance system that keeps learning" and argues this kind of automation does not replace engineering judgment but creates more opportunities to apply it
- **Evidence**: Stated in the closing section, "The real product is the
  feedback loop," as the post's summarizing argument.
- **Confidence**: emerging (an editorial/thesis-level claim about the value of
  the pattern, illustrated by — but not measured beyond — this one incident)
- **Quote**: "It is a maintenance system that keeps learning: a specification defines the promise, a daily check tests it, an issue investigates the signal, a small repair closes the gap, and a lint rule helps prevent the pattern from returning." / "That is the kind of automation worth building. It does not replace engineering judgment; it creates more opportunities to apply it where it matters most."
- **Our assessment**: The five-stage chain named here (specification →
  daily check → issue investigation → repair → lint rule) is a slightly more
  granular restatement of Claim 1's detect→repair→prevent loop, with the
  specification made an explicit first stage. Read skeptically: this is a
  single incident being used to justify a general architectural claim about
  automation's relationship to engineering judgment — a reasonable one given
  the corroborating evidence elsewhere in the corpus (see Cross-References),
  but the post itself supplies exactly one worked example.

## Concrete Artifacts

### The five-stage loop, as named in the closing section

```
specification (defines the promise)
  -> daily check (scripts/check-safe-outputs-conformance.sh; tests it)
  -> issue (investigates the signal)          [issue #55014]
  -> repair (closes the gap)                  [PR #55042]
  -> lint rule (prevents the pattern returning) [PR #55052, no-string-fallback-for-non-string-message]

Source: "One Small Error Message, One Big Feedback Loop" (gh-aw blog,
2026-08-23), "The real product is the feedback loop" section.
```

### Incident artifact trail (traceable IDs from the source)

```
Daily Safe Outputs Conformance Checker run: #32621246743
Check ID:                                    MCE-006 (readable serialized error messages)
Generated issue:                             #55014
Fix PR:                                      #55042
Lint-rule PR (draft, ESLint Miner):          #55052
Proposed rule name:                          no-string-fallback-for-non-string-message

Files affected in mcp_server_core.cjs / error_helpers.cjs (the bug):
  mcp_server_core.cjs   - MCP core; delegates to getErrorMessage()
  error_helpers.cjs     - defines getErrorMessage(), the shared formatting helper

Files where the ESLint Miner found the same pattern recur in actions/setup/js:
  dispatch_workflow.cjs
  route_slash_command.cjs
  log_parser_shared.cjs
  safeoutputs_cli.cjs

Source: "One Small Error Message, One Big Feedback Loop" (gh-aw blog, 2026-08-23)
```

### The bug, in the terms the post uses

```
Trigger:  code throws a plain object with a non-string `message` property,
          e.g. { message: { reason: "x" } }
Buggy path: getErrorMessage() falls back to String(error)
Observed output: "[object Object]"  -- syntactically a string, not an explanation

Fix intent (PR #55042): when a non-Error object HAS a message property,
  preserve a string message or coerce that message value; only objects
  WITHOUT a message property use the whole-object fallback. Tests added for
  numeric and non-primitive message values.

Source: "One Small Error Message, One Big Feedback Loop" (gh-aw blog, 2026-08-23),
"A tiny signal worth following" and "Fix the bug—and improve the question" sections.
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 2 ("Dead code removal is
    automation-suitable because the verification feedback loop is entirely
    mechanical — build and test results provide definitive answers with no
    ambiguity"): the Daily Safe Outputs Conformance Checker's nonzero-exit-on-
    high-severity-failure design (Claim 2 here) is another instance of the
    same "mechanical feedback loop" criterion — a script with an objective
    pass/fail signal driving automated maintenance — applied to conformance
    checking rather than dead-code detection. Together the two notes show the
    mechanical-feedback-loop criterion recurring across at least two distinct
    gh-aw maintenance systems (Go dead-code removal, Safe Outputs conformance).

- **Contradicts**: None identified. No claim here materially opposes an
  existing source note.

- **Extends**:
  - `docs-ghaw-safe-outputs-specification.md` Claim 11 ("Two conformance
    classes exist — C1 (full conformance, all normative requirements) and C2
    (partial conformance, security-critical requirements only)"): that note
    documents conformance as a formal, normative classification in the Safe
    Outputs specification. This post shows the *operational* instantiation of
    conformance testing against that specification — a daily script that
    checks the live implementation and turns a violation into an issue, a
    fix, and a preventative rule. The spec defines what conformance means;
    this post is the first corpus evidence of a live, running check that
    enforces it and the concrete repair loop it triggers on failure.
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 2 ("Linter Miner
    systematically mines discussions, issues, and source code patterns to
    propose new analyzers, producing PRs with ADR documentation"): the
    "ESLint Miner" described here (Claim 7) is a structurally parallel mining
    workflow, but for JavaScript/TypeScript (`actions/setup/js`) rather than
    Go, and seeded by a specific just-fixed bug rather than open-ended
    pattern mining. This extends the "Miner" archetype documented for Go
    analyzers to a second language and a second discovery trigger (bug-fix-
    as-seed rather than freeform issue/discussion mining).
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 6 ("The
    three-workflow partition — invent, challenge, apply — enables durability
    through separation of concerns that are typically conflated in
    traditional linting"): this post's loop (conformance checker detects →
    issue/PR repairs → ESLint Miner invents a preventative rule) is a
    smaller, two-actor variant of the same separation-of-concerns idea:
    detection is decoupled from repair, and repair is decoupled from
    generalization/prevention. It corroborates that gh-aw's own team
    repeatedly builds multi-stage detect/fix/prevent maintenance loops as
    infrastructure, rather than one-off scripts, across at least two
    different domains (Go static analysis; MCP error-handling conformance).

- **Novel**:
  - **The Daily Safe Outputs Conformance Checker and
    `scripts/check-safe-outputs-conformance.sh`** (Claim 2): first corpus
    documentation of this specific script and its short-lived-issue,
    replace-not-accumulate design for avoiding tracker noise from a daily
    scheduled check.
  - **The `getErrorMessage()` / `error_helpers.cjs` MCP error-serialization
    bug and its `[object Object]` failure mode** (Claim 3): first corpus
    documentation of this specific root cause and symptom.
  - **"Good conformance checks protect a property, not a particular spelling
    of the implementation"** (Claim 6): a specific, actionable design
    principle for writing conformance/lint checks that survive correct
    refactors, not previously stated in the corpus.
  - **The "ESLint Miner" workflow and its per-run constraints** (mines
    issues/discussions, scans one target directory, selects one
    low-false-positive rule, opens at most one draft PR) (Claim 7): a named
    workflow not previously documented in the corpus, structurally related to
    but distinct from the Go-focused "Linter Miner."
  - **Warning-only (non-autofix) lint rule as a deliberate design choice tied
    to "local judgment"** (Claim 8): the explicit rationale for choosing
    warn-not-rewrite — that the correct fix (a readable fallback message)
    varies per call site — is new to the corpus's discussion of lint rule
    design.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the detect → repair → prevent loop
  demonstrated here (conformance checker finds a violation → issue/PR repairs
  it → a miner workflow generalizes the fix into a lint rule, seeded by the
  specific bug) as a named maintenance-automation shape, alongside the
  existing three-workflow loop (`blog-ghaw-custom-linters-three-workflow-loop.md`).
  Note that this instance generalizes the pattern beyond Go static analysis to
  MCP error-handling conformance and to a second "Miner"-style workflow
  (ESLint Miner) operating on JS/TS.

- **Chapter 03 (Safety and Verification)**: Add "good conformance checks
  protect a property, not a particular spelling of the implementation"
  (Claim 6) as concrete guidance for writing conformance and lint checks that
  won't false-positive on correct refactors. Pair with
  `docs-ghaw-safe-outputs-specification.md` Claim 11's formal C1/C2
  conformance classes: the spec defines the normative target; this principle
  is how to write a check that verifies the target without overfitting to one
  implementation shape. Also add Claim 4's investigative discipline — a signal
  that looks like a false positive against a surface pattern is worth
  following into any delegated implementation before being tuned away.

- **Chapter 04 (Operations)**: Add the miner's self-limiting operating
  constraints — one target directory, one selected rule, at most one draft PR
  per run (Claim 7) — as a concrete rate-limiting pattern for agentic
  code-mining workflows, alongside the existing restraint-by-design pattern
  documented for the Dead Code Removal Agent
  (`blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4). Add the "warning, not
  autofix" lint-rule design criterion (Claim 8) — when the correct fix
  requires local judgment per call site, prefer a flagging rule over an
  automatic rewrite.

## Extraction Notes

1. **Verbatim text obtained via direct HTML fetch, not just WebFetch
   summarization**: WebFetch was used for an initial pass, but all quotes in
   this note were verified character-for-character against a raw `curl` fetch
   of the page HTML with tags stripped, to satisfy MINER.md §2a. The full
   article body (all five sections) was captured this way and is short enough
   (~600 words) that the entire source was read, not sampled.

2. **Author byline**: The page's JSON-LD metadata lists two authors —
   "Copilot" and "Peli de Halleux" — and the rendered byline under the title
   shows both names. Recorded both in frontmatter/Source Context per the
   page's own attribution; this is consistent with the "By Copilot" AI-authored
   convention noted in `blog-ghaw-agent-of-the-day-2026-05-28.md`, here
   apparently co-attributed to a named team member as well.

3. **Single-incident source**: The entire post is one worked example (one
   conformance-check run, one bug, one fix PR, one lint-rule PR). Confidence
   levels reflect this: the described mechanics (script names, issue/PR
   numbers, file names) are settled first-party facts, but the higher-level
   thesis claims (Claims 1, 6, 9) generalize from this single instance and are
   marked emerging or anecdotal accordingly.

4. **No sub-pages followed**: The post links to `github/gh-aw` (the
   repository generally) and to the three specific issue/PR numbers
   (#55014, #55042, #55052), but does not link to any documentation sub-pages.
   The issue/PR numbers were not independently fetched from GitHub — they are
   cited as they appear in the source post, consistent with how PR/issue
   numbers are handled in `blog-ghaw-custom-linters-three-workflow-loop.md`
   (Extraction Note 2 there).

5. **`docs-ghaw-staged-mode-reference.md` checked, not cited**: The Prospector's
   triage comment flagged this note as a possible overlap ("Safe Outputs mode
   configuration"). On inspection, that note documents the `staged: true`
   preview/dry-run feature for workflow-author-facing safe outputs, which is a
   different concern from this post's topic (internal conformance testing of
   the Safe Outputs MCP Gateway's own error-handling code). No genuine overlap
   was found, so it is not cited above.

6. **No contradictions filed**: Reviewed `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `blog-ghaw-custom-linters-three-workflow-loop.md`,
   `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-staged-mode-reference.md`,
   `docs-ghaw-code-quality-monitoring.md`, `docs-ghaw-troubleshooting-errors.md`,
   and `CONTRADICTIONS.md`. No claim in this source materially opposes an
   existing source note. No contradiction issue filed.
