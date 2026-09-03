---
source_url: https://github.github.com/gh-aw/blog/2026-09-02-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 2, 2026: The Complexity Cop"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: emerging
issue: "#3191"
---

# Agent of the Day – September 2, 2026: The Complexity Cop

> Profiles Ponytail Reviewer, the first read-only, event-driven PR review
> agent in the "Agent of the Day" series: it applies the community-maintained
> `ponytail-review` skill to flag over-engineering in changed lines only,
> capped at 10 `COMMENT`-level review comments per run, and never blocks a
> merge. Fetching the live workflow source and the pinned `ponytail-review`
> skill file traced the skill to the same open-source `DietrichGebert/ponytail`
> project independently benchmarked in `blog-jetbrains-ponytail-token-savings-test.md`
> — this is gh-aw's production deployment of that project's review-time
> sibling skill, a link the blog post itself never mentions.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring convention
  documented across this series, e.g. `blog-ghaw-agent-of-the-day-2026-08-28.md`.
  One agent profiled per post.)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post cites three specific,
  independently-checkable GitHub Actions run IDs (33596102316, 33637292011,
  33635177913) and one specific PR number (#57860) — all fetched directly via
  `gh api` against `github/gh-aw` and corroborated in full (see Concrete
  Artifacts). This note additionally fetched the live workflow definition
  (`raw.githubusercontent.com/github/gh-aw/main/.github/workflows/ponytail-reviewer.md`)
  and the pinned `ponytail-review` `SKILL.md` from the external
  `DietrichGebert/ponytail` repository the workflow imports as a `skills:`
  dependency — neither is mentioned or linked in the blog post's own text.
- **Scope**: One short post (~450 words) describing the workflow's mission
  and three recent runs. Does NOT cover: the workflow's frontmatter
  configuration, the actual content of either safe-output item the three
  runs produced, the provenance of the `ponytail-review` skill it applies,
  or what a "genuine over-engineering" finding looks like in practice — all
  recovered (to the extent recoverable) by this note via the live workflow
  file, the pinned skill file, and direct inspection of PR #57860's review
  history, which did NOT surface an attributable Ponytail Reviewer comment
  (see Extraction Notes).

## Extracted Claims

### Claim 1: Ponytail Reviewer runs on every PR marked ready-for-review in `gh-aw`, plus on demand via a `/ponytail` slash command, applying the community-maintained `ponytail-review` skill, and only comments when it finds genuine over-engineering

- **Evidence**: Blog post opening paragraph, directly corroborated by the
  live workflow's `on:` frontmatter (`pull_request: types: [ready_for_review]`,
  `slash_command: name: ponytail, events: [pull_request_comment,
  pull_request_review_comment]`).
- **Confidence**: settled (blog narrative directly corroborated by the
  fetched live workflow source's trigger configuration)
- **Quote**: "It runs on every pull request marked ready for review in
  `gh-aw` (and on demand via a `/ponytail` slash command), applies the
  community-maintained `ponytail-review` skill, and only speaks up when it
  finds real over-engineering — no noise, no rubber-stamping."
- **Our assessment**: This is the first profiled agent in the "Agent of the
  Day" series that is both read-only (Architecture Guardian's posture,
  `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 6) and event-driven on a
  PR lifecycle trigger with an added on-demand slash-command path — a
  trigger combination distinct from Architecture Guardian's weekday
  schedule and ESLint Refiner's daily schedule
  (`blog-ghaw-agent-of-the-day-2026-08-28.md`). For Ch02: document
  "synchronous, on-demand-capable review agent" as a third trigger archetype
  alongside scheduled-audit and event-driven-action agents already in the
  corpus.

### Claim 2: The `ponytail-review` skill Ponytail Reviewer applies is pinned to a specific commit of the external, independently-maintained `DietrichGebert/ponytail` repository — the same open-source project whose flagship code-writing skill was independently A/B-benchmarked by JetBrains

- **Evidence**: Live workflow frontmatter: `skills: -
  DietrichGebert/ponytail/skills/ponytail-review@2ed6c52c9d7e5e56942508591085fd45dea277d3`.
  This note fetched that pinned skill file directly and separately fetched
  the parent repository's `README.md`, whose banner benchmark line reads
  "~54% less code (up to 94%) · ~20% cheaper · ~27% faster · 100% safe" —
  the identical four figures (54% code / 22% tokens / 20% cost / 27% time)
  quoted as the vendor's "Advertised" numbers in
  `blog-jetbrains-ponytail-token-savings-test.md` frontmatter summary and
  Claim 1.
- **Confidence**: settled (directly confirmed by fetching both the pinned
  skill file and the parent repo's README at the time of writing; not
  mentioned anywhere in the gh-aw blog post, which names neither the skill's
  external provenance nor the vendor project)
- **Quote**: (no direct quote from the gh-aw blog post — the skill's
  provenance is not mentioned in the blog text at all; sourced from the live
  workflow file's `skills:` frontmatter, cited by section name per MINER.md
  §4b: top-level frontmatter of `.github/workflows/ponytail-reviewer.md`,
  cross-checked against `DietrichGebert/ponytail`'s repository README)
- **Our assessment**: This is the most consequential finding in this note
  and is completely absent from the blog post's own framing. GitHub's own
  agentic-workflows platform team has put a specific version
  (`2ed6c52c9d7e5e56942508591085fd45dea277d3`) of a third-party, MIT-licensed
  community skill directly into a production PR-review path on its flagship
  `gh-aw` repository — the same skill family independently tested by
  JetBrains, which found the vendor's advertised code/token/cost/time
  figures collapse to roughly a third of their claimed size under paired
  measurement (`blog-jetbrains-ponytail-token-savings-test.md` Claim 1: −54%
  claimed vs. −15.4% measured code reduction). JetBrains benchmarked the
  *code-writing* skill (`ponytail`, injected via a Claude Code SessionStart
  hook, intervening at the point code is written); this workflow deploys the
  *review-time* sibling (`ponytail-review`, applied after code already
  exists, in a PR diff). No claim in either source establishes that the
  review-time skill's real-world hit rate matches the write-time skill's
  measured performance — they are different mechanisms in the same family,
  not the same tested artifact — but the fact that GitHub has adopted a
  pinned, specific version of the community project whose headline numbers
  the corpus has already found to be overstated is a useful data point for
  any guide passage citing vendor-adjacent skill adoption as implicit
  validation of vendor claims. For Ch02: extend "third-party skill
  dependency, pinned by commit SHA" (a supply-chain-adjacent pattern, see
  Claim 3) with the specific, dated instance of GitHub's own repository
  consuming a skill from a vendor project whose benchmark claims are already
  independently disputed elsewhere in the corpus.

### Claim 3: The `ponytail-review` skill defines a strict, single-purpose output contract — a one-line-per-finding format with five fixed tags (`delete`, `stdlib`, `native`, `yagni`, `shrink`), an explicit scope boundary excluding correctness/security/performance, a required closing net-line-count metric, and an exact stand-down phrase for clean diffs

- **Evidence**: The pinned `SKILL.md` file itself, fetched directly at the
  commit SHA pinned in the workflow.
- **Confidence**: settled (directly read from the first-party skill file;
  not described in the blog post, which only says the agent "only speaks up
  when it finds real over-engineering")
- **Quote**: "Review diffs for unnecessary complexity. One line per finding:
  location, what to cut, what replaces it. The diff's best outcome is
  getting shorter." / "Scope: over-engineering and complexity only.
  Correctness bugs, security holes, and performance are explicitly out of
  scope. Route them to a normal review pass, not this one." / "End with the
  only metric that matters: `net: -<N> lines possible.` If there is nothing
  to cut, say `Lean already. Ship.` and stop."
- **Our assessment**: This is a machine-checkable, narrowly-scoped output
  contract, not a loose "look for complexity" instruction — the five tags
  (`delete:`, `stdlib:`, `native:`, `yagni:`, `shrink:`) each require naming
  a concrete replacement (or "nothing" for `delete:`), which structurally
  prevents the vague "have you considered whether this is necessary?"
  hedging the skill's own worked examples explicitly reject (see Concrete
  Artifacts). The exact closing phrase "Lean already. Ship." is not
  paraphrased anywhere in the workflow's own prose — the workflow's
  process step 8 ("If nothing should be cut, call `noop` with `Lean
  already. Ship.` and stop") quotes the skill's stand-down phrase verbatim,
  confirming the workflow's `noop` path is wired directly to the skill's own
  language rather than a separately authored message. For Ch02: document
  "narrow, tag-based output contract with a fixed stand-down phrase" as a
  concrete technique for constraining a subjective-judgment review skill to
  auditable, comparable output — extends the `noop`-with-message
  auditability pattern already documented in
  `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4, here sourced verbatim
  from the imported skill rather than authored per-workflow.

### Claim 4: Across the three most recent runs (two successful 7-minute reviews, one 7-second fail-fast abort), the workflow produced zero errors and exactly two safe-output items total — evidence the agent discriminates between "comment warranted" and "PR is clean" rather than always producing output

- **Evidence**: Blog post "What the logs actually show" section; run
  metadata for all three run IDs independently fetched via `gh api
  repos/github/gh-aw/actions/runs/<id>`, which confirmed run
  33635177913's `conclusion: "failure"` (matching the blog's "failed fast"
  framing) and run 33596102316's `head_branch:
  copilot/sergo-fix-linters-silent-delete` against PR #57860 (matching the
  blog's stated branch and PR number exactly).
- **Confidence**: settled for the run metadata (independently verified via
  the GitHub Actions API); anecdotal for the "discriminates rather than
  always commenting" interpretation (a 3-run sample, and this note could not
  independently confirm which run(s) produced the two safe-output items —
  see Claim 5 and Extraction Notes)
- **Quote**: "Run #33596102316 — a 7-minute pass over PR #57860 (branch
  `copilot/sergo-fix-linters-silent-delete`), completed successfully with
  the Codex engine, burning 164K tokens across 8 model requests." / "Run
  #33635177913 — a quick 7-second run against a PR titled 'Fix
  daily-token-consumption-report: replace unsupported claude-sonnet-4.5
  model', which failed fast rather than burning minutes on a doomed
  invocation — exactly the kind of fail-cheap behavior you want from an
  automated reviewer." / "Across all three runs: zero errors, zero missing
  tools, and two safe-output items generated in total — meaning Ponytail
  Reviewer isn't just running, it's making judgment calls about when a
  comment is actually warranted versus when a PR is clean enough to leave
  alone."
- **Our assessment**: The "failed fast" run is real and independently
  confirmed (API `conclusion: "failure"`, 7-second window between
  `created_at` and `updated_at`), but the blog's framing of this as
  deliberate "fail-cheap behavior" is the author's interpretation, not a
  demonstrated design feature — a 7-second failure against a PR about
  replacing an "unsupported claude-sonnet-4.5 model" is at least as
  consistent with an invalid model-invocation error (an operational fault)
  as with intentional graceful degradation, and the post does not show the
  failure's actual error output. For Ch04 (Operations): a `conclusion:
  failure` run is a fault, not a feature, regardless of how quickly it
  fails — flag this distinction when citing "fail-fast" framing from a
  vendor/platform's own blog post; the API-level `conclusion` field is the
  authoritative signal, and it says failure, not a graceful skip
  (contrast with Architecture Guardian's explicit `safeoutputs.noop`,
  `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4, which is a *successful*
  run that chose not to act — a materially different signal from this run's
  outright failure).

### Claim 5: This note could not independently attribute either of the two reported safe-output items to a specific review comment on PR #57860, despite PR #57860 having one of the three profiled runs and eight visible reviews/comments from other bots

- **Evidence**: `gh api repos/github/gh-aw/pulls/57860/reviews` and `gh api
  repos/github/gh-aw/pulls/57860/comments`, fetched and read in full by this
  note.
- **Confidence**: settled (directly observed via the GitHub API; this is a
  gap this note surfaces, not a claim the blog post makes)
- **Quote**: (no direct quote — this is an independent verification finding,
  not a source-page claim; sourced from `gh api
  repos/github/gh-aw/pulls/57860/reviews` and `.../comments`, both fetched
  in full)
- **Our assessment**: PR #57860 carries four distinct reviews (from
  `copilot-pull-request-reviewer[bot]`, and three `github-actions[bot]`
  reviews with footers identifying them as "PR Code Quality Reviewer",
  "Impeccable Skills Reviewer", and "Matt Pocock Skills Reviewer" — three
  *different* named review workflows, none of which is Ponytail Reviewer)
  plus one inline review comment (attached to the "PR Code Quality
  Reviewer" review, not a standalone Ponytail comment). None carries a
  footer or signature identifying it as Ponytail Reviewer's own output,
  despite the blog post explicitly naming this PR as the target of a
  successful 164K-token, 8-model-request run. The most likely explanation
  is that this specific run's outcome was a `noop` ("Lean already. Ship.",
  per Claim 3) that produced no visible artifact — consistent with the
  blog's "two safe-output items... across all three runs" arithmetic (three
  runs, only two comment/review outputs, so at least one of the three
  necessarily produced nothing) — but this note could not confirm that from
  first-party evidence, and the blog post does not state which run(s)
  produced the two safe outputs. This also surfaces, incidentally, that
  `github/gh-aw` runs at least four independent AI code-review workflows on
  the same PRs (Ponytail Reviewer plus the three named above), a
  multi-reviewer-fleet composition pattern not previously quantified this
  concretely in the corpus. For Ch09 (Multi-Agent Coordination): note that
  a single PR in this repository can accumulate output from four-plus
  independent review agents, each with a narrow mandate (over-engineering,
  general code quality, "Impeccable" skills, "Matt Pocock" skills) — a
  concrete, high multi-reviewer density example worth citing if the guide
  discusses reviewer-fleet fatigue or comment-volume management.

### Claim 6: The workflow caps itself at 10 review comments and exactly one submitted review per run, restricted to `COMMENT`-level feedback — it can flag but cannot block a merge

- **Evidence**: Blog post "Built for restraint, not volume" section,
  directly corroborated by the live workflow's `safe-outputs` frontmatter:
  `create-pull-request-review-comment: {max: 10}`,
  `submit-pull-request-review: {max: 1, allowed-events: [COMMENT]}`.
- **Confidence**: settled (blog narrative directly corroborated by the
  fetched live workflow source's `safe-outputs` configuration)
- **Quote**: "It caps itself at 10 review comments and exactly one submitted
  review per run, scoped to `COMMENT`-level feedback only — it can flag
  concerns but can't block a merge outright."
- **Our assessment**: This is a harness-level (not prompt-level) restraint
  guarantee: `allowed-events: [COMMENT]` in `safe-outputs` structurally
  prevents the agent from ever submitting an `APPROVE` or
  `REQUEST_CHANGES` review, regardless of what the model decides — the same
  "capability removal over prompt discipline" pattern documented for ESLint
  Refiner's `edit: null` (`blog-ghaw-agent-of-the-day-2026-08-28.md` Claim
  7), here applied to review-authority scope rather than write access. This
  is a second, independent production instance of harness-enforced
  restraint constraining what an otherwise-capable review agent is allowed
  to do, distinct from ESLint Refiner's tool-removal mechanism. For Ch02:
  extend "capability removal over prompt discipline" with this second
  instance — `safe-outputs.submit-pull-request-review.allowed-events`
  restricts the *authority level* of an otherwise-unrestricted review
  action, complementing tool-level removal (`edit: null`,
  `bash:` allowlists) as a harness-level restraint mechanism.

### Claim 7: The workflow shares a `pr-review-base` import configured with `min-integrity: approved`, meaning it will not act on unverified or low-trust pull request content, and pre-fetches diff data through a shared caching layer keyed on the PR head commit SHA so repeated invocations on the same PR do not re-download context

- **Evidence**: Blog post "Built for restraint, not volume" section;
  corroborated by the live workflow's `imports: [{uses:
  shared/pr-review-base.md, with: {min-integrity: approved}}, shared/otlp.md,
  shared/pr-diff-data-fetch.md]` and `cache: {key:
  pr-prefetch-${{ github.event.pull_request.head.sha ||
  github.event.issue.number }}, path: /tmp/gh-aw/agent, restore-keys: [...]}`.
- **Confidence**: settled (blog narrative directly corroborated by the
  fetched live workflow source's `imports:` and `cache:` frontmatter; the
  two shared files themselves, `shared/pr-review-base.md` and
  `shared/pr-diff-data-fetch.md`, returned HTTP 404 when fetched directly
  from `raw.githubusercontent.com/github/gh-aw/main/`, so their own contents
  are not independently verified by this note — see Extraction Notes)
- **Quote**: "It also shares a `pr-review-base` import with `min-integrity:
  approved`, meaning it won't act on unverified or low-trust pull request
  content, and it pre-fetches diff data through a shared caching layer so
  repeated invocations on the same PR don't re-download the same context."
- **Our assessment**: This is a concrete, dated production instance of the
  `min-integrity: approved` trust-floor pattern already documented in
  `docs-ghaw-integrity-reference.md` and `docs-ghaw-mcp-gateway-reference.md`
  Claim 9, here applied via a shared, parameterized import
  (`with: {min-integrity: approved}`) rather than a workflow's own direct
  `tools.github.min-integrity` setting — the same parameterized-shared-import
  mechanism documented for ESLint Refiner's `shared/daily-audit-base.md`
  (`blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 8), now shown reused for
  a `min-integrity` policy rather than an `expires`/`title-prefix` pair. For
  Ch02: extend the "operational baseline import" pattern with a second
  parameter type (`min-integrity`) flowing through the same `with:`
  mechanism, corroborating that shared imports in this codebase are used to
  distribute security-relevant policy, not only cosmetic/expiry defaults.

### Claim 8: The workflow runs on the `codex` engine with the `copilot/mai-code-1-flash-picker` model, tuned for speed and low per-run cost (roughly 3–8 AIC in the profiled runs) rather than exhaustive analysis

- **Evidence**: Blog post "Built for restraint, not volume" section,
  directly corroborated by the live workflow's `engine: {id: codex}` and
  `model: copilot/mai-code-1-flash-picker` frontmatter fields.
- **Confidence**: settled (blog narrative directly corroborated by the
  fetched live workflow source's `engine`/`model` frontmatter)
- **Quote**: "Running on `codex` with the `copilot/mai-code-1-flash-picker`
  model, it's tuned to be fast and cheap per invocation (roughly 3–8 AIC in
  these samples) rather than exhaustive — a reviewer that shows up quickly,
  says its piece if there's something to say, and gets out of the way."
- **Our assessment**: This is a specific, named model-choice tradeoff for a
  narrow-scope review agent: a "flash"/fast-tier model rather than a
  frontier reasoning model, on the premise that detecting *obvious*
  over-engineering (per the skill's own worked examples — a 27-line email
  validator, a `moment.js` import for one format call) does not require
  the most capable available model. This is a concrete instance of matching
  model capability to task difficulty for a narrowly-scoped, high-frequency
  agent, a cost-engineering decision distinct from (and cheaper than) the
  general per-run cost profile of other profiled agents in this series
  (e.g., Architecture Guardian's 123k-token, 5.5-minute confirmation-only
  run, `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 5). For Ch04
  (Operations/Cost Management): add "narrow-scope, high-frequency review
  agents are a candidate for fast/cheap model tiers" as a concrete,
  named-model cost-tuning example.

## Concrete Artifacts

### Ponytail Reviewer: Full Workflow Frontmatter (live source)

```yaml
private: true
emoji: "✂️"
name: "Ponytail Reviewer"
description: Reviews pull requests for unnecessary complexity using Ponytail
on:
  pull_request:
    types: [ready_for_review]
    paths-ignore:
      - '*.md'
      - 'docs/**'
      - '.changeset/**'
  slash_command:
    strategy: centralized
    name: ponytail
    events: [pull_request_comment, pull_request_review_comment]
engine:
  id: codex
model: copilot/mai-code-1-flash-picker
permissions:
  contents: read
  pull-requests: read
  copilot-requests: write
tools:
  cli-proxy: true
  github:
    mode: gh-proxy
features:
  gh-aw-detection: true
imports:
  - uses: shared/pr-review-base.md
    with:
      min-integrity: approved
  - shared/otlp.md
  - shared/pr-diff-data-fetch.md
skills:
  - DietrichGebert/ponytail/skills/ponytail-review@2ed6c52c9d7e5e56942508591085fd45dea277d3
cache:
  key: pr-prefetch-${{ github.event.pull_request.head.sha || github.event.issue.number }}
  path: /tmp/gh-aw/agent
  restore-keys:
    - pr-prefetch-${{ github.event.pull_request.number || github.event.issue.number }}-
safe-outputs:
  create-pull-request-review-comment:
    max: 10
  submit-pull-request-review:
    max: 1
    allowed-events: [COMMENT]
timeout-minutes: 10
```

*Source: `.github/workflows/ponytail-reviewer.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-03. Note the
`features: {gh-aw-detection: true}` flag — this is the same shared
detection framework whose rollout across "30 more agentic workflows" is
recorded in `blog-ghaw-weekly-2026-08-17.md` Claim 9; Ponytail Reviewer is a
concrete, named consumer of that rollout not itemized in that weekly post.*

### Ponytail Reviewer: Prompt Body (live source, in full — 8 process steps)

```
# Ponytail Reviewer

Review the pull request exclusively for unnecessary complexity and
over-engineering by applying the installed `ponytail-review` skill.

## Context

- Repository: `${{ github.repository }}`
- Pull request: `#${{ github.event.issue.number || github.event.pull_request.number }}`

## Process

1. Verify that `/tmp/gh-aw/agent/pr-meta.json` and
   `/tmp/gh-aw/agent/pr-diff.patch` exist and are non-empty. If not, call
   `noop` with a brief explanation and stop.
2. Read the pre-fetched metadata, diff, and
   `/tmp/gh-aw/agent/pr-review-comments.json`. Do not fetch the pull
   request again.
3. Locate and read the installed `ponytail-review` skill's `SKILL.md`,
   then follow it exactly.
4. Review changed lines only. Skip generated files, lock files,
   correctness bugs, security issues, and performance issues.
5. Avoid duplicating existing review comments.
6. For each high-signal finding, add one inline
   `create-pull-request-review-comment` using Ponytail's one-line format.
   Limit the review to the 10 most impactful opportunities.
7. If findings exist, submit one `COMMENT` review whose body ends with the
   skill's required net-lines metric.
8. If nothing should be cut, call `noop` with `Lean already. Ship.` and
   stop.
```

*Source: `.github/workflows/ponytail-reviewer.md`, prose body, fetched
2026-09-03. Step 8's exact phrase matches the skill's own stand-down
instruction verbatim (see Claim 3).*

### `ponytail-review` SKILL.md (external dependency, pinned commit, fetched in full)

```markdown
---
name: ponytail-review
description: >
  Code review focused exclusively on over-engineering. Finds what to delete:
  reinvented standard library, unneeded dependencies, speculative abstractions,
  dead flexibility. One line per finding: location, what to cut, what replaces
  it. Use when the user says "review for over-engineering", "what can we
  delete", "is this over-engineered", "simplify review", or invokes
  /ponytail-review. Complements correctness-focused review, this one only
  hunts complexity.
---

Review diffs for unnecessary complexity. One line per finding: location, what
to cut, what replaces it. The diff's best outcome is getting shorter.

## Format

`L<line>: <tag> <what>. <replacement>.`, or `<file>:L<line>: ...` for
multi-file diffs.

Tags:

- `delete:` dead code, unused flexibility, speculative feature. Replacement: nothing.
- `stdlib:` hand-rolled thing the standard library ships. Name the function.
- `native:` dependency or code doing what the platform already does. Name the feature.
- `yagni:` abstraction with one implementation, config nobody sets, layer with one caller.
- `shrink:` same logic, fewer lines. Show the shorter form.

## Examples

❌ "This EmailValidator class might be more complex than necessary, have you
considered whether all these validation rules are needed at this stage?"

✅ `L12-38: stdlib: 27-line validator class. "@" in email, 1 line, real validation is the confirmation mail.`

✅ `L4: native: moment.js imported for one format call. Intl.DateTimeFormat, 0 deps.`

✅ `repo.py:L88: yagni: AbstractRepository with one implementation. Inline it until a second one exists.`

✅ `L52-71: delete: retry wrapper around an idempotent local call. Nothing replaces it.`

✅ `L30-44: shrink: manual loop builds dict. dict(zip(keys, values)), 1 line.`

## Scoring

End with the only metric that matters: `net: -<N> lines possible.`

If there is nothing to cut, say `Lean already. Ship.` and stop.

## Boundaries

Scope: over-engineering and complexity only. Correctness bugs, security holes,
and performance are explicitly out of scope. Route them to a normal review
pass, not this one. A single smoke test or `assert`-based
self-check is the ponytail minimum, not bloat, never flag it for deletion.
Does not apply the fixes, only lists them.
"stop ponytail-review" or "normal mode": revert to verbose review style.
```

*Source: `DietrichGebert/ponytail/skills/ponytail-review/SKILL.md`, fetched
via `curl` from `raw.githubusercontent.com/DietrichGebert/ponytail/` at the
exact commit SHA pinned in the workflow's `skills:` frontmatter
(`2ed6c52c9d7e5e56942508591085fd45dea277d3`), 2026-09-03.*

### Run and PR verification data (independently fetched via `gh api`, not from the blog post)

```
Run 33596102316: conclusion=success, event=pull_request,
  head_branch=copilot/sergo-fix-linters-silent-delete,
  created_at=2026-09-02T05:47:24Z, updated_at=2026-09-02T05:57:29Z
  (~10 min wall clock including queue time; blog's "7-minute pass" refers
  to execution time within the run)

Run 33637292011: conclusion=success, event=pull_request,
  head_branch=copilot/task-9919-1036865607-94dccca7-665c-4ddf-b9fb-33fbc86e24ed,
  created_at=2026-09-02T13:41:41Z, updated_at=2026-09-02T13:53:21Z

Run 33635177913: conclusion=failure, event=pull_request,
  head_branch=copilot/fix-daily-aic-consumption-report,
  created_at=2026-09-02T13:20:58Z, updated_at=2026-09-02T13:21:05Z
  (7 seconds wall clock — matches blog's "quick 7-second run" exactly)

PR #57860 ("Guard suggested fixes against comment loss in five linters"):
  state=closed, merged=true, changed_files=18, comments=8, review_comments=1
  Reviews present (fetched in full): copilot-pull-request-reviewer[bot]
  (APPROVED-recommended), "PR Code Quality Reviewer" (DISMISSED, run
  33596102221), "Impeccable Skills Reviewer" (COMMENTED, run 33596102308),
  "Matt Pocock Skills Reviewer" (APPROVED, run 33596102266) — none carries
  a Ponytail Reviewer signature footer (see Claim 5).
```

*Source: `gh api repos/github/gh-aw/actions/runs/<id>`, `gh api
repos/github/gh-aw/pulls/57860`, `gh api repos/github/gh-aw/pulls/57860/reviews`,
and `gh api repos/github/gh-aw/pulls/57860/comments`, all fetched directly,
2026-09-03.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 7 (ESLint Refiner's
    `edit: null` plus a four-command `bash:` allowlist as harness-enforced
    read-only posture): Claim 6 here (`allowed-events: [COMMENT]`) is a
    second, independent production instance of harness-level restraint
    constraining an agent's authority rather than relying on prompt
    discipline alone — this time restricting review *authority level*
    rather than write *capability*.
  - `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4 (`safeoutputs.noop`
    called with an explicit, human-readable message rather than silently):
    Claim 3 here shows the same auditable-noop pattern, but the message
    itself ("Lean already. Ship.") is sourced verbatim from the imported
    skill file rather than authored per-workflow — a variant of the same
    principle.
  - `docs-ghaw-integrity-reference.md` and `docs-ghaw-mcp-gateway-reference.md`
    Claim 9 (`min-integrity: approved` as the default trust floor for public
    repos): Claim 7 here is a concrete, dated production instance of that
    policy applied via a shared, parameterized import.

- **Contradicts**: None identified. Reviewed `CONTRADICTIONS.md` (no
  existing entries touching PR-review-agent scope, `ponytail`/complexity
  skills, or `min-integrity` policy) and the source notes cited throughout
  this note. No contradiction issue filed.

- **Extends**:
  - `blog-jetbrains-ponytail-token-savings-test.md` (independent A/B
    benchmark of `DietrichGebert/ponytail`'s code-writing skill, finding
    advertised −54% code / −22% tokens / −20% cost / −27% time collapses to
    measured −15.4% code / −10.3% cost / −11% time): Claim 2 here traces
    Ponytail Reviewer's `ponytail-review` skill to the exact same upstream
    project (confirmed via matching benchmark figures in that project's own
    README), establishing that gh-aw's production deployment and the
    corpus's existing benchmark study concern siblings within one tool
    family, not unrelated tools. Neither source measures the review-time
    skill's real-world accuracy, so this is a provenance link, not a
    performance corroboration — flagged explicitly in Claim 2's assessment.
  - `docs-ghaw-code-quality-monitoring.md` Claim 5 (quantitative code
    quality workflow using a crude ">500 lines" file-length threshold as a
    complexity proxy, alongside ESLint/flake8 error counts): Ponytail
    Reviewer targets the same general problem (excess complexity) via a
    qualitative, LLM-judgment mechanism instead of a line-count threshold —
    the corpus now has both a quantitative-proxy and a qualitative-judgment
    approach to complexity detection, profiled in enough detail to compare
    mechanisms directly.
  - `docs-ghaw-gallery-code-improvement.md` Claim 8 (a write-enabled,
    daily-scheduled "code-simplifier" workflow whose prompt explicitly warns
    against six named over-simplification failure modes): both workflows
    target complexity reduction but at opposite points in the SDLC and with
    opposite write postures — code-simplifier proactively opens draft PRs
    on a schedule across all recent changes; Ponytail Reviewer reactively
    comments on individual PRs at review time and never edits code itself.
    Together they document two structurally different approaches to the
    same underlying goal (less code) — proactive-write vs. reactive-review.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 9 (rollout of the shared
    `gh-aw-detection` feature "across 30 more agentic workflows"): the live
    workflow's `features: {gh-aw-detection: true}` (Concrete Artifacts) is
    a concrete, named consumer of that rollout not itemized by name in the
    weekly post.

- **Novel**:
  - **A named, verified link between a production GitHub Agentic Workflows
    deployment and an externally-benchmarked skill project already in the
    corpus** (Claim 2): the corpus has documented gh-aw's own agents and
    JetBrains' independent skill benchmarks as separate threads; this note
    is the first to trace a direct dependency edge between them (a pinned
    commit of `DietrichGebert/ponytail` consumed as a production `skills:`
    import), surfacing that GitHub's own production review pipeline uses a
    skill from the exact vendor project whose headline benchmark claims the
    corpus has already found to be overstated by roughly 3x on the sibling
    skill.
  - **`allowed-events` as an authority-scoping restraint mechanism distinct
    from tool/capability removal** (Claim 6): prior corpus restraint
    patterns removed *capabilities* (`edit: null`, `bash:` allowlists,
    `contents: read`); this is the first documented instance of restraint
    applied to the *authority level* of an action the agent otherwise fully
    retains (it can still submit a review, just never one that blocks).
  - **A pinned-commit-SHA dependency on an external, community-maintained
    skill repository as the mechanism for delivering a review agent's core
    judgment logic** (Claim 2/Concrete Artifacts): no prior corpus note
    documents a gh-aw workflow's primary analytical capability being
    supplied by an external `skills:` import (as opposed to prompt text
    authored directly in the workflow file) pinned to an exact commit — a
    supply-chain-adjacent pattern (external code determining agent
    judgment, version-pinned like a software dependency) not previously
    named in the corpus.
  - **Independent verification surfacing a negative result the source
    itself did not report**: this note could not attribute either of the
    two claimed safe-output items to a specific artifact on the one PR the
    blog names explicitly (Claim 5) — the first instance in this series
    where direct API verification of a blog's named example could not
    close the loop, despite finding four *other* attributable review
    workflows on the same PR.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "synchronous, on-demand-capable
  review agent" as a third trigger archetype (Claim 1), alongside
  scheduled-audit and event-driven-action agents already documented. Add
  "authority-scoping via `allowed-events`" as a restraint mechanism distinct
  from capability removal (Claim 6) — extend the "capability removal over
  prompt discipline" pattern with this second instance. Add "narrow,
  tag-based output contract with a fixed stand-down phrase, sourced from an
  imported skill rather than authored per-workflow" (Claim 3) as a technique
  for constraining subjective-judgment review skills to auditable output.
  Flag pinned-commit external `skills:` imports (Claim 2) as a
  supply-chain-adjacent dependency pattern worth naming explicitly,
  especially where — as here — the imported skill's vendor project has
  independently-benchmarked, overstated marketing claims elsewhere in the
  corpus; a version pin does not by itself validate the pinned code's
  claims.

- **Chapter 04 (Operations)**: Add "narrow-scope, high-frequency review
  agents as a candidate for fast/cheap model tiers" (Claim 8) as a
  named-model cost-tuning example (`copilot/mai-code-1-flash-picker`,
  3–8 AIC/run). Caution against citing a platform blog's own "fail-cheap"
  framing at face value (Claim 4) — the underlying signal was a
  `conclusion: failure`, not a graceful `noop`, and the two are materially
  different operational signals even when both complete quickly.

- **Chapter 09 (Multi-Agent Coordination)**: Note the concrete,
  independently-verified example of a single PR carrying output from at
  least four independent, narrowly-scoped review agents (Claim 5) — useful
  as a citable data point if the guide discusses reviewer-fleet density or
  comment-volume management on a real, busy first-party repository.

## Extraction Notes

1. **Blog post is short (~450 words); primary depth came from three fetched
   sub-pages**, within MINER.md §1's "up to 5" budget: the live workflow
   source (`ponytail-reviewer.md`), the pinned `ponytail-review` `SKILL.md`
   from the external `DietrichGebert/ponytail` repository, and that
   repository's own `README.md` (fetched to verify the benchmark-figure
   match underlying Claim 2). PR #57860 and all three cited run IDs were
   also independently queried via `gh api` for verification. Claims 2, 3,
   5, 6, 7, and 8, and all of Concrete Artifacts, rely on this sub-page and
   API material — none of it is present in the blog post's own text. The
   blog post's text alone would have supported Claims 1 and 4 (partially).

2. **Blog quotes obtained via direct HTML fetch, converted with a Python
   regex pass** (inline `<code>` tags to backticks) rather than WebFetch
   summarization, per MINER.md §2a. An initial WebFetch call against the
   blog URL returned text close to verbatim; this note independently
   re-fetched and parsed the raw HTML via `curl` to confirm character-level
   accuracy (including em-dashes and curly quotes) before quoting.

3. **Two shared imports could not be independently verified**:
   `shared/pr-review-base.md` and `shared/pr-diff-data-fetch.md` both
   returned HTTP 404 when fetched directly from
   `raw.githubusercontent.com/github/gh-aw/main/` (unlike `shared/otlp.md`,
   not attempted separately since it is not central to this note's claims,
   and unlike `shared/daily-audit-base.md`, which a prior note successfully
   fetched). This may reflect a different repository layout for these
   specific shared files (e.g. nested under a nonstandard path) rather than
   their absence; this note relies on the blog post's own description of
   their effect (Claim 7) rather than asserting their exact file contents.
   Flagged rather than silently worked around.

4. **PR #57860's actual Ponytail Reviewer output could not be located**
   (Claim 5): this is a genuine gap this note surfaces rather than resolves.
   All four reviews and one inline comment visible on the PR are
   attributable to other named review workflows via footer signatures;
   none matches Ponytail Reviewer. The most likely explanation (a `noop`
   outcome for this specific run) is stated as an inference, not a
   confirmed fact, in Claim 5's assessment.

5. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-05-20.md`,
   `blog-ghaw-agent-of-the-day-2026-08-28.md`,
   `blog-jetbrains-ponytail-token-savings-test.md`,
   `docs-ghaw-code-quality-monitoring.md`,
   `docs-ghaw-gallery-code-improvement.md`,
   `blog-ghaw-weekly-2026-08-17.md`,
   `docs-ghaw-integrity-reference.md`, `docs-ghaw-mcp-gateway-reference.md`,
   and `CONTRADICTIONS.md`, all read in full (not skimmed) before writing
   Cross-References. All `Claim N` citations above were checked against the
   actual numbered claims in those notes at the time of writing, per
   MINER.md §4b.

6. **No contradiction filed**: this note's findings extend and corroborate
   existing corpus claims (restraint mechanisms, `min-integrity` policy,
   the Ponytail benchmark series) rather than opposing any of them. The gap
   documented in Claim 5 is an extraction limitation, not a claims
   contradiction, and does not warrant a contradiction issue.

7. **Confidence rationale**: `confidence_overall` is set to "emerging"
   rather than "settled" because, while the workflow's configuration and
   the skill's own contract are directly verified from first-party sources
   (settled), the blog's efficacy narrative ("isn't just running, it's
   making judgment calls") rests on a 3-run sample where this note could
   not independently confirm the actual content of either reported
   safe-output item (Claim 5) — the evidentiary basis for "the agent is
   good at this" is thinner than the evidentiary basis for "this is how
   the agent is configured."
