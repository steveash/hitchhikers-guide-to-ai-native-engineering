---
source_url: https://www.thoughtworks.com/insights/blog/architecture/designing-agentic-delivery-for-bounded-context-and-bounded-human-attention
source_type: blog-post
title: "Designing agentic delivery for bounded context and bounded human attention"
author: Jaya Simha Reddy Nandyala and Prabina Pani (Thoughtworks)
date_published: 2026-09-29
date_extracted: 2026-10-10
last_checked: 2026-10-10
status: current
confidence_overall: emerging
issue: "#4042"
---

# Designing agentic delivery for bounded context and bounded human attention

> Frames agentic delivery as protecting two scarce resources, the model's in-session attention and the reviewer's post-session attention, and offers concrete patterns (index-first loading, sub-agent context firewalls, fixed-shape PR summaries, plan-file steering) plus three named failure modes.

## Source Context

- **Type**: blog-post
- **Author credibility**: Two Thoughtworks practitioners, who also wrote the companion piece "Engineering the harness" (same date; see `blog-thoughtworks-nandyala-pani-engineering-the-harness.md`). The article carries a disclaimer that views are the authors' own. No measured results from their own work are reported.
- **Scope**: Covers context rot, progressive disclosure, sub-agents as firewalls, reviewer-attention limits, self-explaining changes (PR summary), and three failure modes. The fetched page also appends a Guides/Sensors/multi-repo-harness section that duplicates the companion article; it is not re-extracted here. Evidence is illustrative worked examples (cookie rule, `business-workflows.md`, PR #482, a 47-file diff), not measurements. External statistics are secondhand.

## Extracted Claims

### Claim 1: The bottleneck is moving from code generation to two constraints: usable model context and reviewer time
- **Evidence**: Assertion by the authors, with no data of their own.
- **Confidence**: emerging
- **Quote**: "Code generation is increasingly less likely to be the slow step."
- **Our assessment**: Plausible and consistent with other review-bottleneck sources in the corpus. The framing is useful, but it is asserted rather than shown.

### Claim 2: Context rot is a relevance problem, not a capacity problem; a larger window does not keep an early instruction salient
- **Evidence**: Hypothetical worked example: a "never store session tokens in localStorage; use httpOnly cookies" rule is buried by exploration output and then violated when a "remember me" feature is added.
- **Confidence**: emerging
- **Quote**: "Capacity and relevance are different problems."
- **Our assessment**: The example is constructed, not observed. The claim is independently supported by the HumanLayer note, which has measured-in-practice instruction-adherence degradation. Treat this note as an illustration of the mechanism, not proof.

### Claim 3: Context rot has two causes with distinct fixes: the "loading problem" and the "exploration problem"
- **Evidence**: Definitional framing by the authors; each cause gets its own worked example.
- **Confidence**: emerging
- **Quote**: "Loading problem: Reading an entire guide to answer one question."
- **Our assessment**: The loading/exploration split is a clean taxonomy and is new to the corpus. Other notes discuss progressive disclosure and sub-agents but do not pair them as answers to two different failure habits.

### Claim 4: Index-first loading ("map, then walk"): split a large knowledge doc into a short index plus nested docs and load only the path a question needs
- **Evidence**: Illustrative example: a 6,000-line `business-workflows.md` becomes `flows-index.md` plus nested flow docs. The SLA-exception question resolves via workspace-approval flow, escalation rules, SLA matrix, and exception policy.
- **Confidence**: emerging
- **Quote**: "Five files and a few hundred lines are enough."
- **Our assessment**: A concrete, copyable layout. The "few hundred lines" figure is illustrative, not measured. It also requires the index to stay accurate (see Claim 10).

### Claim 5: Sub-agents work as context firewalls when they have one job, an isolated window, and a condensed result
- **Evidence**: Same cookie-rule session replayed with exploration delegated; the sub-agent returns "httpOnly cookies are already implemented in session-manager.ts; reuse setAuthCookie()".
- **Confidence**: emerging
- **Quote**: "What makes the sub-agent useful is its boundary:"
- **Our assessment**: The three-part boundary (one job, isolated window, condensed result) is a handy design checklist. The article also says exploratory tool calls generally belong behind that boundary when the main session only needs their result. No evidence on cost or quality.

### Claim 6: Agents can produce changes faster than reviewers can read them, and passing tests and types do not make a large diff reviewable
- **Evidence**: Hypothetical 47-file, 3,140-line change. The article lists the costs: bugs hide in noise, approval becomes a stamp, comments arrive too late, and unrelated edits make revert all-or-nothing.
- **Confidence**: emerging
- **Quote**: "Tests and types can pass while the diff is still too large to judge with care."
- **Our assessment**: Consistent with the Addy Osmani and Pragmatic Engineer notes. The four-item cost list is a useful articulation.

### Claim 7: Reported statistics on PR scale and unreviewed agent PRs (secondhand)
- **Evidence**: Cited without links in the article: Salesforce Engineering for PR size/code volume, an unnamed "industry review" for the 61% figure, and Cortex 2026 for change-failure rates. Reported by the author, not verified by us.
- **Confidence**: anecdotal
- **Quote**: "One industry review found 61 percent of agent-authored pull requests had no recorded human review."
- **Our assessment**: Do not cite as measured. The unnamed source cannot be traced. Faros AI's figure in the Addy Osmani note (31.3% rise in PRs merging with zero review) is a more traceable data point for the same theme.

### Claim 8: Every change should carry a short, fixed-shape summary beside the diff (intent, coverage, how it was checked, risk), with code remaining the source of truth for behavior
- **Evidence**: PR #482 example: Context, Summary, Changes tied to requirements, an acceptance-criterion → test → result chain, Risk (with rollout and rollback), and a Reviewer checklist.
- **Confidence**: emerging
- **Quote**: "Same shape every time, so a reviewer learns where to look."
- **Our assessment**: The most actionable new contribution. It differs from Osmani's decision log (agent goal and rejected alternatives) by adding requirement → test → result traceability and an explicit risk/rollback line. Not validated by any measurement.

### Claim 9: Split mechanical checks from judgment: automation catches completeness gaps and bounces work back before review, while humans confirm only decisions with significant blast radius
- **Evidence**: Examples: a missing test for an acceptance criterion is caught by automation; a plan editing several repos at once needs human confirmation.
- **Confidence**: emerging
- **Quote**: "The person sees the decision that is costly to undo, and a summary small enough to read."
- **Our assessment**: Corroborates blast-radius tiering in the corpus. The specific "completeness gap" gate (every AC must map to a test) is a concrete, implementable check.

### Claim 10: Failure mode, long-horizon drift: after compaction an agent can report done against the original plan, so steering changes must be written into the plan file
- **Evidence**: Hypothetical example: "drop the invoice export; ship token rotation only" is said in chat and lost on compaction.
- **Confidence**: emerging
- **Quote**: "The agent can report done against the plan it started with."
- **Our assessment**: A plausible and practical risk, and the remedy is cheap. It supports the idea that handoff documents, not chat, are durable. The claim about compaction retaining early plans over later corrections is asserted, not demonstrated.

### Claim 11: Failure mode, stale specifications: when code and docs disagree, the code is the authority, and a confirmed human decision outranks an agent inference
- **Evidence**: Example: an agent reintroduces a deprecated `/v1/sessions` endpoint because an index still lists it. The article notes greenfield projects may differ.
- **Confidence**: emerging
- **Quote**: "When code and documentation disagree, the codebase is the authority (for greenfield projects this might differ)."
- **Our assessment**: A useful precedence rule, but it creates tension with index-first loading (Claim 4): indexes are another artifact that must be kept in sync. The article gives pruning advice but no mechanism.

### Claim 12: Failure mode, self-verification bias: an agent's "done" claim is a weak witness and must be backed by a test run, type check, or build result before a person is asked to trust it
- **Evidence**: Assertion with the example claim "AC-1 is covered; tests pass".
- **Confidence**: emerging
- **Quote**: "An agent that just wrote the change is a weak witness that the change is done."
- **Our assessment**: Corroborated by Cognition's finding that false "pass" reports fall when expected behavior is annotated before acting. Here it is a rule of thumb rather than an empirical result.

### Claim 13: "Bounded autonomy": give agents more autonomy inside deliberately set limits (scoped context, a short human artifact, mechanical checks first)
- **Evidence**: Summary framework; no data.
- **Confidence**: emerging
- **Quote**: "The goal is more autonomy, inside limits you set on purpose."
- **Our assessment**: A memorable synthesis, not an independent finding. It restates Claims 4, 5, 8 and 9 as three principles.

## Concrete Artifacts

Index-first walk (from the article's SLA example):

```
Question: "What is the SLA exception policy for a stuck approval?"
flows-index.md
  -> workspace-approval flow
  -> that flow's escalation rules
  -> SLA matrix
  -> exception policy
(Appeals, asset provisioning and vendor management stay unread.)
```

Fixed PR summary shape (from the article's "pull request #482" example):

```
Context.   PROJ-482, its blueprint and its readiness note.
Summary.   One paragraph of intent.
Changes, each tied to a requirement.
  AC-1: session tokens rotate on password change
  AC-2: invoice totals are recalculated on the server
  AC-3: the onboarding wizard resumes from the last completed step
Acceptance criterion, test and result.
  AC-1 -> "rotates session token on password change" -> passed
  (same chain for AC-2 and AC-3: requirement -> test -> result)
Risk.      Medium: session rotation could log people out mid-rollout.
           Ships behind a flag; rollback is turning the flag off. No data migration.
Reviewer checklist. Business logic matches the story. Architecture stays
           intact. Existing sessions stay as they are until rollout.
```

Sub-agent boundary (from the article): one job, an isolated window, a condensed result.

## Cross-References

- **Corroborates**:
  - `blog-humanlayer-long-context-isnt-the-answer.md` Claim 8 (context isolation via sub-agents and progressive disclosure beats context expansion), and Claim 7 (needle-in-a-haystack framing of instruction salience).
  - `blog-humanlayer-context-forking.md` Claim 10 (preserving context after a context-inefficient operation) is the same goal reached by a different mechanism.
  - `blog-anthropic-context-engineering-claude-5.md` Claim 7 and Claim 8 (progressive disclosure applied to CLAUDE.md and Skills).
  - `blog-thoughtworks-nandyala-pani-engineering-the-harness.md` Claim 4 (progressive disclosure), Claim 7 (confirmation gates only for blast radius) and Claim 8 (sensors over self-assessment) overlap with this article's Claims 4, 9 and 12; treat those as corroboration.
  - `blog-addyosmani-agentic-code-review.md` Claim 2 (PRs merging with zero review) and Claim 7 (review effort tiered by blast radius).
  - `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 6 (blast-radius risk tiering).
- **Contradicts**: None found. No contradiction issue was filed.
- **Extends**:
  - `blog-thoughtworks-nandyala-pani-engineering-the-harness.md` (companion article): adds the reviewer-attention half and the drift/staleness failure modes.
  - `blog-addyosmani-agentic-code-review.md` Claim 9 (decision log on the PR): this article adds a requirement → test → result chain and an explicit risk/rollback line to the PR summary.
  - `blog-cognition-verifying-agentic-development.md` Claim 6 (annotating expected behavior reduces false "pass" reports) is related to this article's self-verification bias claim.
  - `blog-thoughtworks-patole-context-real-bottleneck-ai-agents.md` Claim 2 (half-truths defeat human review) concerns the same reviewer-attention limit from the business-context side.
- **Novel**:
  - The loading-problem vs exploration-problem split as two distinct context-rot causes (Claim 3).
  - A concrete index-plus-nested-docs layout with a worked walk (Claim 4).
  - The fixed-shape PR summary with an AC → test → result chain and risk/rollback (Claim 8).
  - Writing steering changes into the plan file to survive compaction (Claim 10).
  - The precedence rule: code over docs, and a confirmed human decision over agent inference (Claim 11).

## Guide Impact

- **Chapter 00 ("Context Is a Budget, Not a Feature")**: add the relevance-vs-capacity distinction (Claim 2) alongside the existing budget framing. Cite the HumanLayer note for the measured evidence and this article only as illustration.
- **Chapter 02 (harness engineering)**: add the loading/exploration split as the rationale for progressive disclosure vs sub-agents, and the three-part sub-agent boundary (Claims 3 and 5). Add a short note on the code-over-docs precedence rule and index drift (Claim 11).
- **Chapter 03 (verification)**: add the rule that an agent's "done" must be backed by a test, type or build result, plus an automated AC-to-test completeness gate before human review (Claims 9 and 12).
- **Chapter 04 (context engineering)**: add the index-first layout and the plan-file steering rule for surviving compaction (Claims 4 and 10).
- **Chapter 01 (daily workflows)**: consider a PR-summary template based on the PR #482 shape (Claim 8), noting that it is unvalidated. Do not cite the 61% / 30% / Cortex figures as measured (Claim 7).

## Extraction Notes

- Fetched the page directly and read it in full. Nothing was paywalled. The page has no sub-pages worth following.
- The article has no named author affiliation beyond Thoughtworks. All examples are hypothetical; none are measured. Statistics in Claim 7 are secondhand and unlinked.
- The fetched page text continues past the "Bounded autonomy" section into a Guides/Sensors/multi-repo harness section that is a near-duplicate of the companion article. It was cross-checked against the existing harness note and not re-extracted as new claims.
- Cross-reference claim numbers were verified against the headings in each cited note.
