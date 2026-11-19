---
source_url: https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
source_type: blog-post
title: "How the Claude Code team thinks about verification"
author: Addy Osmani
date_published: 2026-11-16
date_extracted: 2026-11-19
last_checked: 2026-11-19
status: current
confidence_overall: emerging
issue: "#4824"
---

# How the Claude Code team thinks about verification

> A first-party account of the verification layer behind a ~90%-Claude-written codebase: three test types (E2E, property, differential), a `verify` skill, a diff-triggered reliability checklist, check-immutability (rules read from the base branch), an off/observe/enforce commit gate with verification stamps, and a rule-promotion pipeline for turning misses into rules.

## Source Context

- **Type**: blog-post (first-party, Anthropic Claude Code team, claude.dev Engineering blog; 10 min read; published 2026-11-16)
- **Author credibility**: Addy Osmani writing about the Claude Code team's own practice. Primary-source practice, but the only quantitative claim is an internal, unbaselined vendor figure, and no raw data is published.
- **Scope**: Covers test-type selection, running the app end to end, escalation, code-owner-written checks, a reliability checklist, reviewer design, gate integrity, commit gating, reviewer evaluation, and rule promotion/pruning. It does not publish the checklist itself, gate false-positive rates, or any metrics on the commit gate. It is a companion to the Oct 2026 code-review post (see `blog-claude-dev-claude-code-team-code-review.md`).

## Extracted Claims

### Claim 1: Verification loops are what let one person run many agents in parallel
- **Evidence**: Authority/practice: ~90% of the team's code is written and reviewed by Claude. No measurement of the parallelism claim.
- **Confidence**: anecdotal
- **Quote**: "Without them, you can really only run one or two Claudes at a time, because you have to check everything yourself. With them, you can run dozens or hundreds in parallel."
- **Our assessment**: A useful framing for Ch03: verification is the throughput limiter, not generation. "Dozens or hundreds" is asserted, not evidenced.

### Claim 2: A separate rubric grader improved structured-file task success by up to 10 points (vendor claim)
- **Evidence**: "Internal testing around structured file generation"; no task set, sample size, or baseline detail.
- **Confidence**: anecdotal
- **Quote**: "having a separate grader check Claude's work against a rubric improved task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems."
- **Our assessment**: Vendor-reported internal result, narrow domain (structured file generation). "Up to" is a best case. Cite only with attribution; do not generalize to code.

### Claim 3: Flaky tests train agents to re-run instead of fix, and slow tests cause fewer test runs that make failures harder to pinpoint
- **Evidence**: Reasoned argument, no data.
- **Confidence**: anecdotal
- **Quote**: "If your tests are flaky you'll train the agent to run them again rather than fixing the failing code."
- **Our assessment**: Plausible and consistent with how agents optimize for green. The same post then gives the harsher flaky-test policy in Claim 14.

### Claim 4: If you pick only one test type, pick E2E; give the agent "hands and eyes" via a skill, with a feature map as the grading rubric
- **Evidence**: Argument (E2E tests are hard to fool, have definitive done criteria, and return screenshots rather than a bare timeout). Tools named: CDP, simulators, API harnesses.
- **Confidence**: emerging
- **Quote**: "If you have to focus on one test type, pick end-to-end."
- **Our assessment**: Specific and actionable. The "feature map" (features from the user's view with paths, shortcuts, selectors, expected results) doubling as a rubric is a concrete artifact idea. The claim that unit tests can pass while the feature is broken because "both the agent and the test don't understand the full task" is a good statement of the unit-test-circularity problem.

### Claim 5: Property tests counter agent bias because their edge cases are not generated with the same bias as the code under test
- **Evidence**: Argument plus four named property families (round-trip, invariant, idempotency, equivalence) and libraries (fast-check, Hypothesis, proptest). No data.
- **Confidence**: emerging
- **Quote**: "Property libraries are a great way to keep agents honest by using edge cases that aren't created with the same bias as the agent that created the original code."
- **Our assessment**: Corroborates the "unit/property/acceptance tests" gate list in `blog-addyosmani-agentic-code-quality.md` (Claim 2) but adds the concrete property taxonomy and the independence rationale. Property tests are also pitched for rewrites where the spec has drifted from production.

### Claim 6: Differential tests use the old system as the oracle for migrations, with random or sampled production inputs, normalization, and an approved-changes list
- **Evidence**: Procedure description; no case study.
- **Confidence**: emerging
- **Quote**: "You'll also want to normalize irrelevant factors like whitespace and keep a list of approved changes for situations where the new environment should differ from the old."
- **Our assessment**: Novel to the corpus as a named pattern. The approved-changes list is the key operational detail, since it turns "diff found" into a reviewable decision.

### Claim 7: Verification means running the change; a `verify` skill codifies how to boot and drive the app and is the team's smoke harness
- **Evidence**: Practice description: place it in `.claude/skills/`, near the relevant code, as many as needed; Claude knows to use it before committing; iterate and stress-test it.
- **Confidence**: emerging
- **Quote**: "To codify how to start the simulator or run your app, create a skill called verify."
- **Our assessment**: Overlaps `blog-anthropic-claude-code-verification-loops-skills.md` (Claim 2 lists `/verify`; Claim 8 covers chaining it). New here: place verify skills near the code, and treat the skill itself as a thing to stress-test ("rock solid"). The statement "This is how we test nearly all changes at Anthropic" is unquantified.

### Claim 8: Failing checks are an escalation signal: after three rounds Claude stops and brings in a human
- **Evidence**: Team practice, stated without data.
- **Confidence**: anecdotal
- **Quote**: "If a check is still failing after three rounds, Claude stops and brings in a human."
- **Our assessment**: Same three-round number as the reviewer round cap in `blog-claude-dev-claude-code-team-code-review.md` (Claim 10), which had before/after convergence data. Here it is applied to any check, not just review. Together they suggest a consistent "three-round" convention, though neither source explains why three.

### Claim 9: Code owners write the checks for their own code, and a check that pulls in a reviewer should say why
- **Evidence**: Practice statement.
- **Confidence**: anecdotal
- **Quote**: "The people who own the code write the checks for it, and refine them until they flag what the owner would flag."
- **Our assessment**: Matches REVIEW.md ownership in the code-review note (Claim 4). The "say why" rule is a small, copyable design requirement for any check that routes to a human.

### Claim 10: A diff-triggered reliability checklist (39 items) lets the agent check only matching items, usually 3 to 10
- **Evidence**: Description of structure (trigger readable from a diff, a check, the incidents or PRs behind it); one example item (`--resume` loads old transcripts). The list itself is not published.
- **Confidence**: emerging
- **Quote**: "Claude reads the diff and checks only the items whose trigger matches–usually 3 to 10–so nobody has to memorize past outages."
- **Our assessment**: Novel. It is incident memory encoded as conditional checks, which avoids loading all 39 items into context every time. The three-part entry (trigger / check / provenance) is directly reusable. Limitation: no data on hit rate or how triggers are kept accurate.

### Claim 11: Tune one reviewer with REVIEW.md rather than stacking reviewers, and make later rounds build on earlier context
- **Evidence**: Assertion only.
- **Confidence**: anecdotal
- **Quote**: "Adding a second, more expensive, reviewer on top of the primary one is often a worse approach than tuning the primary."
- **Our assessment**: Interesting counterpoint to multi-agent review stacks, but with no comparison data. It sits in mild tension with the parallel-finders-plus-voters architecture described in the code-review note (Claim 5), although that is one pipeline rather than stacked independent reviewers, so we do not treat it as a contradiction.

### Claim 12: Changes must not be able to modify the checks that judge them: review rules are read from the base branch, and reviews are pinned to commits
- **Evidence**: Design principle plus a concrete mechanism (Code Review reads REVIEW.md from the base or default branch). Also: cheap local checks (tests, build, linter) before opening a PR, enforceable by a hook or a `/goal`.
- **Confidence**: emerging
- **Quote**: "If a change can modify the check that judges it, the check is broken."
- **Our assessment**: High-value, novel gate-integrity rule that is not in the code-review note. Applies equally to CI configs, hooks, and permission files. The related statement "A passing review on an out-of-date commit means nothing" echoes the commit-bound approvals in the code-review note (Claim 8).

### Claim 13: Roll out a commit gate in off, observe, and enforce modes, stamping every commit with how it was verified (including "none"), with an escape hatch after two blocks
- **Evidence**: Practice description; no false-positive or block-rate numbers.
- **Confidence**: anecdotal
- **Quote**: "If commits have been blocked twice in the session, the next one will be allowed through so Claude doesn't get stuck – Claude Code isn't perfect."
- **Our assessment**: Novel and practical: the gate blocks a commit unless the session contained `/code-review` or `/verify`, observe mode logs would-be blocks to find false positives, and the stamp makes unverified commits queryable. Note the escape hatch means enforce is bounded, not absolute; a stuck agent can still commit unverified (and the stamp records it).

### Claim 14: Flaky tests: Claude may not skip, add sleeps, or retry; if it cannot find the root cause it deletes the test and records why
- **Evidence**: Policy statement; no outcome data.
- **Confidence**: anecdotal
- **Quote**: "If it can't find the root cause, it deletes the test and writes down why."
- **Our assessment**: Novel and risky. It closes off the three common agent escapes, but deleting reduces coverage. It is defensible only with the recorded reason and human visibility. Treat as a team policy to adapt cautiously, not a default recommendation.

### Claim 15: Reviewers should be evaluated against real incidents with separate recall at raw, post-verification, and final stages, and tuned only up to the point of overfitting
- **Evidence**: Description of the eval (repo recreated at review time, one-sentence answer key, merged-and-stable control, tuning set split from a fixed test set); tracked reverts, maintainer rejections, and a size-matched clean subset.
- **Confidence**: emerging
- **Quote**: "Any evaluation that treats all these as one end-to-end score won't capture this nuance."
- **Our assessment**: Extends the incidents-as-evals loop in the code-review note (Claim 11) with the stage-separated recall idea, which is the new detail: it detects a pipeline that loses bugs it already found. Also restates the Important / Nit / Pre-existing tags.

### Claim 16: Misses become rules via two pipelines: pattern mining (at least two PRs, diff-identifiable, three agents try to disprove, human approves in a PR) and replaying three bug finders on known-incident PRs (two or more hits means detectable)
- **Evidence**: Process description; no counts of rules produced or rejected.
- **Confidence**: emerging
- **Quote**: "Three agents will try to disprove them, and they will be reviewed and approved by a human in a PR."
- **Our assessment**: Novel and concrete governance for rule growth: an evidence threshold, adversarial disproof, then human approval. The replay test separates "reviewer can't see it" from "rule missing", and a miss on a small diff is flagged as a gap to turn into a REVIEW.md rule. Related to hook/rule feedback in Claim 1 context ("create a hook or a more explicit rule in your CLAUDE.md").

### Claim 17: Rules, tests, and .md files only grow unless pruned on a routine
- **Evidence**: Assertion; no routine described.
- **Confidence**: anecdotal
- **Quote**: "Test suites, verification steps and .md files only grow if you let them, so we tidy them up on a routine."
- **Our assessment**: Short but important counterweight to the rule-promotion pipeline. The post gives no pruning criteria, which is a gap.

## Concrete Artifacts

Reliability checklist entry shape (source: "Reliability checks trigger on the diff"; the source describes the structure and one example, not a file format):

```
Item structure: trigger (readable from a diff) + check + incidents/PRs behind it
Example item (quoted from source): "--resume loads old transcripts"
Trigger described: session storage or message types change
Check described: does a new field load safely, since older transcripts won't have it
Runtime behavior: Claude reads the diff and runs only matching items (usually 3 to 10 of 39)
```

Commit gate modes (source: "Start a new gate in observe mode", paraphrased structure):

```
off      -> no gate
observe  -> log what would have been blocked; review false positives
enforce  -> block commit if session did not contain /code-review or /verify
            (commit message may carry an explanation; after two blocks in a
             session the next commit is allowed through)
Every commit is stamped with how it was verified, including "none".
```

Property families named in the source: round-trip encoding, invariants, idempotency, equivalence (optimized vs naive). Libraries named: fast-check (JS/TS), Hypothesis (Python), proptest (Rust).

## Cross-References

- **Corroborates**: `blog-claude-dev-claude-code-team-code-review.md` (Claim 4 REVIEW.md owned by code owners; Claim 5 Important/Nit/Pre-existing tags; Claim 11 incidents as eval cases; Claim 10 three-round cap); `blog-anthropic-claude-code-verification-loops-skills.md` (Claim 2 `/verify` skill; Claim 8 chaining `/code-review`, `/simplify`, `/verify`); `blog-addyosmani-agentic-code-quality.md` (Claim 2 property/acceptance tests as gates).
- **Contradicts**: None filed. The "one tuned reviewer, not stacked reviewers" advice (Claim 11) is in mild tension with the multi-agent finder-plus-voter design in the code-review note (Claim 5), but the difference is stacking independent reviewers versus one pipeline, so no contradiction issue was filed.
- **Extends**: The code-review note's incidents-as-evals loop (adds stage-separated recall: raw, post-verification, final) and its REVIEW.md material (adds the base-branch rule). The verification-loops note (adds verify-skill placement and stress-testing).
- **Novel**: Diff-triggered 39-item reliability checklist; "changes can't modify their own checks" with base-branch rule reads; off/observe/enforce commit gate with verification stamps and two-block escape hatch; flaky-test deletion policy; two-pipeline miss-to-rule promotion with adversarial disproof; differential-test pattern with an approved-changes list; feature map as E2E grading rubric.

## Guide Impact

- **Chapter 03**: Add the three-test taxonomy (E2E first, then property, then differential) with the property families and the unit-test-circularity rationale. Add the "separate grader" result only with a vendor-claim caveat (Claim 2). Add stage-separated recall for evaluating review systems (Claim 15).
- **Chapter 02**: Add the commit gate as a harness mechanism: off/observe/enforce rollout, verification stamps, and a bounded escape hatch (Claim 13). Add the diff-triggered checklist as a way to keep incident memory out of always-on context (Claim 10). Add gate integrity: gating rules live on a branch the change cannot modify (Claim 12).
- **Chapter 05**: Add code-owner-authored checks that explain why they flag (Claim 9), the rule-promotion pipeline with human approval (Claim 16), and routine pruning (Claim 17). Flag the flaky-test deletion policy (Claim 14) as a cautionary, team-specific practice.

## Extraction Notes

- Fetched the full page directly and read it end to end (about 14k characters of text); all quotes were copied from that text. Related-post links were not followed because the triage identified the two overlapping notes, which were read for cross-references.
- All cross-referenced claim numbers were verified against the numbered headings in the cited notes.
- The only quantitative figure is the up-to-10-points grader result, which is vendor-reported. The post contains no numbers for the commit gate, the checklist, or rule promotion.
- No contradiction issue was filed; see Cross-References.
