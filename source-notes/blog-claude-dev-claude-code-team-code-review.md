---
source_url: https://claude.dev/blog/solving-code-review-at-anthropic/
source_type: blog-post
title: "How the Claude Code team does code review"
author: Addy Osmani, Morgan Westlee Lunt, Qing Wang
date_published: 2026-10-15
date_extracted: 2026-10-17
last_checked: 2026-10-17
status: current
confidence_overall: emerging
issue: "#4176"
---

# How the Claude Code team does code review

> A first-party account of a layered, mostly automated review pipeline (fresh-context verification, verifier-voted AI review, blocking security review, classifier-set risk-tiered human approval, merge queue/flags/rollback) with reviewer-convergence data and an incidents-as-evals loop.

## Source Context

- **Type**: blog-post (first-party, Anthropic Claude Code team, claude.dev Engineering blog; 14 min read)
- **Author credibility**: Written by members of the Claude Code team describing their own repos (CLI, desktop/web, mobile). Primary-source practice, but all metrics are internal and vendor-reported with no external baseline or raw data.
- **Scope**: Covers the pipeline from pre-PR verification to rollback, how the reviewer is improved and made to converge, where humans stay involved, context sharing, ownership norms, and an adoption checklist. It does not publish absolute revert/incident rates, classifier details, or the eval-set size.

## Extracted Claims

### Claim 1: The team optimizes for minimum human review time, with reverts and incidents as the guardrail
- **Evidence**: Stated goal plus named measures: human approvals per PR (median and 95th percentile), human comments, wait time on a person. Outcome claim: merged PRs more than doubled June–September while the reverted share fell by more than 40%. No absolute numbers.
- **Confidence**: emerging
- **Quote**: "Revert and incident rates are the guardrail: if they rise, we haven't saved human time, we've only moved it."
- **Our assessment**: Strong framing: human time includes the time spent fixing what bad code breaks. The headline result is self-reported and unbaselined, and "share reverted" fell while volume doubled, so treat as directional.

### Claim 2: "Did a human read the code?" is an imprecise proxy; review becomes continuous rather than an end-of-road gate
- **Evidence**: Argument from volume: monorepo changes/day went from about 2,500 in May to more than 30,000 in September (monorepo, not the Claude Code repo, which is separate).
- **Confidence**: emerging
- **Quote**: "Now, review runs continuously, more like spellcheck while you write."
- **Our assessment**: Reframing is useful for Ch03/Ch05. The 2,500→30,000 figure is for Anthropic's monorepo, not the team's own repo; do not conflate.

### Claim 3: Most review happens before the PR: runnable checks plus a fresh-context subagent review
- **Evidence**: Practice description; Boris Cherny's estimate that verification makes results two to three times better. Internal skills (bug hunt, simplify diff, end-to-end check) are run before opening a PR.
- **Confidence**: emerging
- **Quote**: "Then a subagent reviews the diff with fresh context."
- **Our assessment**: Consistent with prior Anthropic material. The 2–3x figure is an estimate attributed to one person, not a measurement.

### Claim 4: REVIEW.md, written by code owners, configures the reviewer per code area, and adherence to it is checked separately
- **Evidence**: Description of what good REVIEW.md files contain (failure definition per repo type, nit cap, skip paths, file-and-line evidence, count-first summary).
- **Confidence**: anecdotal
- **Quote**: "They say what failure looks like in that repo (for docs it's \"it lies,\" for config it's \"it misroutes\"), cap the nits, list paths to skip, and ask for a file and line as evidence instead of a guess from a name."
- **Our assessment**: Concrete, copyable guidance for Ch02. Repeated reviewer complaints are fixed "at the source" (skill, lint rule, CLAUDE.md/REVIEW.md) rather than per PR.

### Claim 5: AI review uses parallel bug-hunting agents plus a separate voting group; only agreed findings are posted
- **Evidence**: Mechanism description; style/diagnostic/cleanup findings dropped, filters A/B tested on internal PRs (results not given); findings tagged Important, Nit, or Pre-existing. Launch effect: share of internal PRs with substantive review comments went from 16% to 54%.
- **Confidence**: emerging
- **Quote**: "Then a separate group votes on each finding, and it only gets posted if enough of them agree it's real."
- **Our assessment**: Verifier-voting is a precision mechanism worth capturing. The 16%→54% measures comment coverage, not bug-catch accuracy. The Pre-existing tag is a small but notable design detail.

### Claim 6: Open findings from either the bug review or the security review block merge; every finding must be answered
- **Evidence**: Process description; findings clear automatically if a later commit fixes them; false positives are cleared by closing the thread with a reason.
- **Confidence**: anecdotal
- **Quote**: "A PR can't merge while any finding from the bug review or the security review is still open."
- **Our assessment**: Contrasts with read-only/COMMENT-only reviewer designs; here the AI review is a merge blocker (though not an approver, see Claim 8).

### Claim 7: Human approval tier is set by a classifier from the change, not the author; low risk needs no person, medium one, high two
- **Evidence**: Risk table (Low: docs, copy, internal-only, additive-behind-flag; Medium: ordinary product plus caching/auto-updater/system prompts; High: highest-risk code plus a small set of always-two paths). A second classifier asks whether a change needs another person even when its tier says otherwise. Only trusted-list authors get lighter paths.
- **Confidence**: emerging
- **Quote**: "The change sets the tier, not the author."
- **Our assessment**: Operationalizes blast-radius tiering. Caveat: the "only trusted authors get the lighter paths" rule means the author does matter for eligibility, so the headline is slightly stronger than the practice.

### Claim 8: Governance rules: agent approvals never count as a person's; whoever prompted the change is a required reviewer; approvals bind to a specific commit
- **Evidence**: Policy statements; re-approval required if commits land that the system can't vouch for (agent push, hand-resolved merge).
- **Confidence**: emerging
- **Quote**: "An agent's approval never counts as a person's, either."
- **Our assessment**: Clear, adoptable rules. Related "dismiss approvals on new commits" appears in the adoption checklist.

### Claim 9: Agent-author/agent-reviewer loops fail to converge by default; 59% of repeated flags were on code present at the first pass
- **Evidence**: One CLI PR went through more than fifty review/fix rounds overnight; git blame on repeated flags showed about 59% was code present since the first pass.
- **Confidence**: emerging
- **Quote**: "The reviewer was rarely finding new bugs, it was finding a few more old ones each round."
- **Our assessment**: A valuable failure-mode datapoint (single example plus one blame analysis). The team concedes they made it worse by defaulting to several rounds.

### Claim 10: Four convergence controls (round cap of three, diff-only re-review, flag the bug class, no repeats) improved convergence
- **Evidence**: FIG D, internal PRs before→after: pass after one review-and-fix round 65%→78%; need five or more rounds 8.9%→1.5%; mean reviews to pass 2.08→1.32. Team now tracks rounds-to-pass alongside recall. No sample size or time window given.
- **Confidence**: emerging
- **Quote**: "After three rounds, the reviewer asks the author to step back and reconsider the approach."
- **Our assessment**: Specific and actionable; numbers are first-party before/after without confounder control. Note that recall impact of diff-only re-review is not reported.

### Claim 11: Every incident/revert becomes an expert-confirmed eval case; each reviewer change is scored daily and kept only if the score rises
- **Evidence**: FIG C loop description. Eval size and score values are not given.
- **Confidence**: emerging
- **Quote**: "Any incidents are now an eval."
- **Our assessment**: Corroborates the incidents-as-regression-cases idea from the SDLC playbook, here applied to the reviewer itself rather than CLAUDE.md/skills/hooks.

### Claim 12: Reviewer noise is measured by author response category and by runs on known-clean PRs; priority is bugs first, fewer rounds second
- **Evidence**: Comments sorted into fixed / wrong / intentional / doesn't matter; known-clean PRs used to count harmful-change suggestions.
- **Confidence**: anecdotal
- **Quote**: "Our priority, written down, is catching real bugs first and cutting review rounds second."
- **Our assessment**: Compare with Cursor Bugbot's resolution-rate approach; this adds the known-clean control set. Notes that noise costs more when the author is an agent because every nit triggers another commit and round.

### Claim 13: Humans retain five decisions: whether to build, risky code, architecture, reading evidence, owning the outcome
- **Evidence**: Practice list (FIG E); examples: billing, auto-updater, CI workflows. Includes "If you can't say what the checks would miss, ask for a real review rather than a quick approval."
- **Confidence**: emerging
- **Quote**: "A person is accountable for every change that ships, whoever typed it."
- **Our assessment**: Consistent with other Anthropic org accounts; adds the specific "reading the evidence" duty.

### Claim 14: Fast rollback is the last layer, and the team admits it lacks circuit breakers that tighten approval when revert/incident metrics move
- **Evidence**: Flags off without deploy, weekly on-call, incident reviews asking which layer should have caught the issue. The authors say engineers want circuit breakers before more code moves to zero-human merges.
- **Confidence**: anecdotal
- **Quote**: "We don't yet have circuit breakers that tighten approval when those numbers move; engineers here want them before more code moves to zero-human merges."
- **Our assessment**: Honest limitation: the zero-human tier currently lacks an automated safety valve. Relevant counterweight to the headline metrics.

### Claim 15: Review's second job (shared understanding) is replaced by on-demand Claude-written explainers, with no formal process
- **Evidence**: Team practice only; no measurement of whether understanding is preserved.
- **Confidence**: anecdotal
- **Quote**: "When someone wants to understand a part of the codebase, they ask Claude to write an explainer for exactly that slice."
- **Our assessment**: Plausible but untested; the weakest-evidenced claim and the one most worth watching for failure reports.

## Concrete Artifacts

Risk-tier table (source: "5. Human approval, scaled by risk"):

```
Risk    Examples                                                              Human approvals
Low     Docs, copy, internal-only features, additive changes behind a flag    None required once automated review and security checks are green
Medium  Ordinary product changes, and changes to sensitive areas such as      One person
        caching, the auto-updater, or system prompts
High    The highest-risk code, plus a small set of paths that always need two Two people
        people
```

Convergence results (source: FIG D, internal PRs, before → after convergence work):

```
Pass after one review and fix round   65%  -> 78%
Need five or more rounds              8.9% -> 1.5%
Mean reviews to pass                  2.08 -> 1.32
```

Other metrics (source text): internal PRs with substantive review comments 16% → 54% after research-preview launch; monorepo changes/day ~2,500 (May) → 30,000+ (Sept); Claude Code merged PRs more than doubled June–Sept with revert share down >40%; ~59% of repeat reviewer flags were on code present at first pass; one CLI PR ran 50+ rounds overnight.

Pipeline layers (source: FIG A/B): verification → required CI → Claude code review → security review → risk-based approval → merge queue (+ flags, staged release `latest` then `stable`) → watch/fix-forward/rollback.

Adoption checklist (source: "How you can adopt this process"), abridged: short CLAUDE.md with runnable checks plus formatter/linter hooks; `/code-review` and `/security-review` locally; add REVIEW.md; require CI and add "Testing", "Risk" and "How to revert" to the PR template; pilot an AI reviewer on one repo and tune REVIEW.md for a few weeks; require all review threads resolved; cap rounds and re-review only the new diff; write risk tiers (start strict, loosen with evidence); CODEOWNERS and branch protection for auth, billing, CI/release workflows, installers; dismiss approvals on new commits; merge queue, flags, staged releases, one-step rollback; turn incidents into an eval set; measure human time with revert/incident rates as guardrail.

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-agentic-code-review.md` Claim 7 (tier review by blast radius, not by authorship) and Claim 11 (humans on the loop rather than in it): this note supplies a concrete implementation (classifier-set tiers, trusted-author lists).
  - `blog-anthropic-ai-native-sdlc-playbook.md` Claim 13 (agent findings never approve; human code owner required) and Claim 12 (every production incident becomes a permanent regression case).
  - `blog-anthropic-ai-native-engineering-org.md` Claim 6 (code review bifurcated: Claude handles bug-catching, humans retain domain expertise) and Claim 1 (review and verification became the bottleneck).
  - `blog-anthropic-claude-code-verification-loops-skills.md` Claim 8 (chaining `/code-review`, `/simplify`, `/verify` before PR) and Claim 11 (verification as team infrastructure on every PR).
- **Contradicts**: None filed. Tension to note, not a contradiction: `blog-addyosmani-agentic-code-review.md` Claim 10 proposes a predictive circuit breaker, while this source says the team does not yet have one and wants it before expanding zero-human merges (Claim 14 above). Also `docs-ghaw-automated-pr-review.md` Claim 6 restricts the agent to COMMENT-type reviews; here the AI review/security review block merging but still never approve, a compatible but stronger gate.
- **Extends**: `blog-cursor-bugbot-learning.md` (Claim 4 on resolution-rate as quality signal): adds known-clean-PR runs and incident-derived eval sets. `blog-anthropic-ai-native-sdlc-playbook.md` Claim 13 (REVIEW.md as policy): adds REVIEW.md authoring guidance and the nit cap.
- **Novel**: Reviewer convergence data and controls (round cap, diff-only re-review, class-level flagging, no repeats; 59% pre-existing blame analysis; 50+ round PR); verifier voting with Important/Nit/Pre-existing tags; classifier-set approval tiers with a second "needs another person anyway" classifier; commit-bound approvals; "prompter is a required reviewer"; incidents-as-reviewer-eval with daily scoring.

## Guide Impact

- **Chapter 03**: Add a "reviewer convergence" subsection: agent-author plus agent-reviewer loops need a round cap (3), diff-only re-review, bug-class flagging and no-repeat findings, citing the 2.08→1.32 mean-reviews and 8.9%→1.5% five-plus-rounds figures (labelled vendor-reported). Add the incidents-as-reviewer-eval loop and known-clean-PR noise check alongside existing verification-loop material.
- **Chapter 05**: Add the risk-tier approval model (classifier sets tier from the change; trusted-author lists; commit-bound approvals; prompter counts as required reviewer; agent approval never counts) as a worked example of the blast-radius rule, with the human-time metric set (approvals/PR median and p95, wait time) and revert/incident guardrails. Note the missing circuit breakers as an open risk.
- **Chapter 06**: Cite security review as a separate merge-blocking pass whose open findings block merge, with CODEOWNERS/branch protection for auth, billing, CI and release workflows.
- **Chapter 02**: Add REVIEW.md authoring guidance (failure definition, nit cap, skip paths, evidence requirement, count-first summary) next to CLAUDE.md guidance, and the practice of fixing repeated reviewer complaints at the source.

## Extraction Notes

- Full article read from the fetched page text (including all figure labels and the adoption checklist); no sub-pages followed (linked best-practices, CI-scaling, and Code Review announcement posts were not read).
- All metrics are first-party and unbaselined; confidence capped at emerging per triage guidance. Sample sizes, time windows, and absolute revert rates are not given.
- Co-author Addy Osmani also wrote `blog-addyosmani-agentic-code-review.md`; the two are not independent sources on tiering/human-on-the-loop.
- Figure content (FIG A–E) was captured from the page's text labels; the PNG images themselves were not viewed.
