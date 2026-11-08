---
source_url: https://github.github.com/gh-aw/blog/2026-11-07-ecosystem-spotlight/
source_type: blog-post
title: "Ecosystem Spotlight: witt3rd/review-council (GitHub Agentic Workflows)"
author: Copilot (GitHub Agentic Workflows blog byline)
date_published: 2026-11-07
date_extracted: 2026-11-08
last_checked: 2026-11-08
status: current
confidence_overall: anecdotal
issue: "#4591"
---

# Ecosystem Spotlight: witt3rd/review-council

> A short gh-aw blog spotlight on a third-party "council" of five narrowly scoped AI reviewers, each enforced as its own required commit status, with rules pinned to the PR base commit and releases gated on evals over golden PRs that include planted defects and a prompt injection.

## Source Context

- **Type**: blog-post (filed as "documentation", but it is a dated blog post)
- **Author credibility**: Byline "Copilot" on the GitHub-run gh-aw blog. It summarizes a community repo (`witt3rd/review-council`) and attributes several claims to that repo's `AGENTS.md` ("According to AGENTS.md", "AGENTS.md cites"). It does not independently measure anything.
- **Scope**: Design overview, defensive defaults, release process and four adoption steps. No eval scores, no catch-rate data, no comparison against a single general reviewer. I read only the blog post; I did not fetch the linked repo (AGENTS.md, changelog, eval setup), so the eval-score and cost claims remain unverified secondary reports.

## Extracted Claims

### Claim 1: Five narrowly scoped reviewers, one verdict each, beat a single catch-all reviewer
- **Evidence**: Design rationale only; no measurements. Reviewers: Steward (written law and PR claims), Architect (layers and contracts), Inspector (bugs), Warden (abuse), Editor (prose, for documents repos). Each workflow states what is *not* its job.
- **Confidence**: anecdotal
- **Quote**: "One AI reviewer that comments on everything tends to produce vague, overlapping feedback."
- **Our assessment**: Plausible and consistent with single-purpose-agent design, but asserted, not demonstrated. Cost multiplies with reviewer count, and no data shows five narrow reviewers outperform one well-prompted one.

### Claim 2: Each reviewer is enforced as its own required commit status on the PR head
- **Evidence**: Description of the caller file and the adoption step "Require each `<Reviewer> verdict` status in your branch ruleset." Verdict is set on `pull_request.head.sha`.
- **Confidence**: emerging
- **Quote**: "A repository calls the reviewers it wants from a short caller file and gets one required commit status per reviewer on the pull request head."
- **Our assessment**: Turns AI review from advisory comments into a merge gate, using the branch ruleset the team already has. This contrasts with the gh-aw starter, which limits review events to COMMENT (see Cross-References). Whether verdicts are reliable enough to block merges is not addressed.

### Claim 3: The "Warden" must name a concrete exploit path before raising a finding
- **Evidence**: Described rule: no defense-in-depth requests "just in case". No false-positive rate given.
- **Confidence**: anecdotal
- **Quote**: "requires every finding to name a concrete path: who sends what, and what they get that they should not."
- **Our assessment**: A reusable finding-quality rule (evidence-of-path requirement) that makes reviewer output auditable and cuts speculative noise. Worth citing as a prompt pattern; effect size unknown.

### Claim 4: Consumer rules are read from the PR base commit so a PR cannot rewrite its own review criteria
- **Evidence**: Attributed to the repo's AGENTS.md, not verified against code.
- **Confidence**: emerging
- **Quote**: "the council reads the repository's principles.md and AGENTS.md from the PR's base commit, so a PR cannot rewrite the rules it is judged by."
- **Our assessment**: A strong, simple trust-model point: judge criteria must come from a ref the author cannot modify in the same PR. Directly applicable to any AI review gate that reads in-repo instructions (AGENTS.md, CLAUDE.md, rules files).

### Claim 5: Defensive defaults: same-repo, non-draft PRs only; read-only permissions; bounded turns and time; newer push cancels older review
- **Evidence**: Config values given: `max-turns: 100`, `timeout-minutes: 40`; read-only contents and pull-requests.
- **Confidence**: emerging
- **Quote**: "Reviewers only run on non-draft, same-repo pull requests, because fork PRs get no secrets."
- **Our assessment**: Matches gh-aw's documented fork behavior. The tradeoff (fork/external contributors get no AI review) is not discussed.

### Claim 6: Releases are tagged only when an eval over golden PRs passes; fixtures include planted defects and a deliberate prompt injection
- **Evidence**: Process statement; changelog said to record scores and spend, but none are reproduced in the post.
- **Confidence**: anecdotal
- **Quote**: "Releases are tagged only when an eval run on golden pull requests passes. The fixtures carry planted defects and even a prompt injection on purpose."
- **Our assessment**: Notable practice: treating reviewer prompts as versioned artifacts with regression evals, including an adversarial fixture. Pass thresholds and results are unverified here.

### Claim 7: Cost datapoint of roughly $0.80 for five reviewers on a small PR
- **Evidence**: Self-reported, via AGENTS.md as cited by the blog; "small PR" undefined, model not named in the post (callers supply an `OPENROUTER_API_KEY`).
- **Confidence**: anecdotal
- **Quote**: "AGENTS.md cites roughly $0.80 for five reviewers on a small PR."
- **Our assessment**: Useful order-of-magnitude figure only. The post also warns "model spend bills to your repository", so cost lands on the adopter.

### Claim 8: Thin pinned callers: `uses:` pinned to a release SHA, with a `pins.yml` job reporting lagging callers
- **Evidence**: Description of `caller/review-council.yml` using YAML anchors to share permissions, inputs and secrets.
- **Confidence**: emerging
- **Quote**: "Each uses: is pinned to a release commit SHA with the tag as a comment, and a pins.yml workflow reports which callers lag behind the newest release."
- **Our assessment**: Standard supply-chain hygiene applied to shared agent workflows, with a drift-reporting mechanism that addresses the cost of pinning across many repos.

### Claim 9: Reusable agentic workflows across repos need `inlined-imports: true` and fixed reviewer names for status/concurrency IDs
- **Evidence**: Specific gh-aw gotchas described; CI recompiles locks and requires no diff.
- **Confidence**: emerging
- **Quote**: "because github.workflow is the caller's name inside a called workflow, status names and concurrency IDs use the reviewer's fixed name, and the verdict is set on pull_request.head.sha."
- **Our assessment**: Concrete, checkable operational knowledge. "CI recompiles the locks and requires no diff" is a good drift check for compiled agent workflows.

### Claim 10: The council holds no key and no consumer law; each caller supplies its own API key and principles
- **Evidence**: Adoption steps: copy caller, write `principles.md`, add `OPENROUTER_API_KEY` secret, require status checks.
- **Confidence**: emerging
- **Quote**: "The council holds no key and no consumer's law: each caller supplies its own OPENROUTER_API_KEY."
- **Our assessment**: Clean separation of shared reviewer logic from per-repo policy and billing. The post's caution to review prompts and locks as with any third-party workflow is the right adoption posture.

## Concrete Artifacts

Adoption steps (from the post, "Try it"; paraphrased list, not a verbatim block):
1. Copy `caller/review-council.yml` to `.github/workflows/review-council.yml`, keep wanted reviewers, pin to a release SHA.
2. Copy `caller/principles.md` to `.github/review-council/principles.md` and write own principles/checks.
3. Add the `OPENROUTER_API_KEY` repository secret.
4. Require each `<Reviewer> verdict` status in the branch ruleset.

Configuration values named in the post: `max-turns: 100`, `timeout-minutes: 40`, `inlined-imports: true`, trigger `on: workflow_call`, reviewer sources compiled to `.lock.yml`, shared contract in `.github/workflows/shared/`.

## Cross-References

- **Corroborates**: `docs-ghaw-fork-support.md` (agentic workflows skip fork contexts because forks lack secrets; the council's same-repo-only rule applies the same logic, cf. its Claim 3). `docs-ghaw-automated-pr-review.md` Claim 1 and Claim 4 (read-only contents/pull-requests permissions for the reviewing agent).
- **Contradicts:** none filed. Mild tension, not a contradiction: `docs-ghaw-automated-pr-review.md` Claim 6 restricts reviews to COMMENT events (advisory), while the council makes verdicts required status checks (blocking). These are different enforcement layers (review event vs commit status), so this is a conditioning difference.
- **Extends**: `docs-ghaw-automated-pr-review.md` (single reviewer, advisory) to multiple scoped reviewers with merge-gating; `docs-ghaw-guides-reusing-workflows.md` (reusable workflows) with a real-world pinned-caller and lock-drift practice; `blog-cursor-rollouts-security-reviewer.md` (security reviewer as a gate).
- **Related**: `blog-ghaw-ecosystem-spotlight-factory.md` (same blog series; also separates governance from the agent), `blog-cursor-bugbot-learning.md` (AI reviewer improvement via feedback, vs. eval-gated releases here), `blog-pragmaticengineer-orosz-code-review-approaches.md`.
- **Novel**: Base-commit pinning of review rules; multi-reviewer required-status council; eval-gated reviewer releases with a planted prompt-injection fixture; "no path, no finding" rule; `pins.yml` caller-drift reporting.

## Guide Impact

- **Chapter 03 (verification)**: Add the council as an example of enforcing AI review through per-reviewer required commit statuses, and of versioning reviewer prompts with golden-PR evals including planted defects. Label as author-reported, unmeasured.
- **Chapter 06 (security)**: Add the rule "read review criteria (AGENTS.md/principles) from the PR base commit, never the head" as a mitigation for PR-authored rule rewriting; add the prompt-injection eval fixture as a testing practice (Claims 4, 6).
- **Chapter 05 (adoption)**: Cite the thin pinned caller + drift report pattern for rolling one reviewer set across many repos (Claim 8); mention the spend-bills-to-repo caveat.
- **Chapter 02 (harness)**: Optional example of scoped reviewer roles with explicit "not my job" boundaries (Claims 1, 3).

## Extraction Notes

- Fetched the raw page HTML and read the full article (short; ~600 words). No sub-pages followed; the linked `witt3rd/review-council` repo and `github/gh-aw` were not read, so the Prospector's suggestion to verify eval scores and spend against the changelog was not done. All numbers are therefore secondhand.
- No headline metrics beyond the $0.80 figure; overall evidence is a description of design, hence `anecdotal`.
- No contradiction issue filed: no claim materially opposes an existing note.
