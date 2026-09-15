---
source_url: https://sourcegraph.com/blog/introducing-agentic-batch-changes
source_type: blog-post
title: "Introducing Agentic Batch Changes: the frontier agent for code change at scale"
author: Lauren Preston (Sourcegraph)
date_published: 2026-09-14
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: emerging
issue: "#3452"
---

# Introducing Agentic Batch Changes: the frontier agent for code change at scale

> Sourcegraph product-launch post for "Agentic Batch Changes," a GA feature
> combining Batch Changes (cross-repo PR orchestration) with Deep Search and
> coding agents (Claude Code / Codex): the system decides per-plan-item
> whether to write a script or hand a repo to a full agent, adapts to
> repo-to-repo variation and CI failures, and bills per merged changeset
> rather than per token or seat — illustrated with two named customer cases
> (Mercari, Canva).

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published September 14,
  2026; auto-discovered via the `sourcegraph` trusted feed named in the
  triage issue). Short-form (~750 words) product-launch announcement: an
  opening problem-framing narrative, three section headings ("Describe the
  change once. The agent takes it from there.", "Agentic Batch Changes
  writes scripts more often than it deploys coding agents, which is what
  keeps it efficient at scale", "Success we saw from the Beta"), a pricing
  section ("Only pay for what merges"), and an availability/CTA close.
  Embeds a YouTube product demo (not transcribed for this note).
- **Author credibility**: Byline is Lauren Preston, published on
  Sourcegraph's official company blog (confirmed via the site's own embedded
  post metadata, which lists the same title, author, and 2026-09-14 publish
  date). This is vendor launch content: Sourcegraph sells both Batch Changes
  and the coding-agent orchestration layer the post describes. The two
  customer quotes (Mercari, Canva) are named, attributed to specific
  individuals and titles, and are the strongest evidence in the post; the
  aggregate numbers ("hundreds of thousands of changesets," "more than 2,200
  changesets from one change," "nearly a thousand changesets" in Beta) are
  first-party, self-reported, and not independently auditable by this Miner.
- **Scope**: Covers the product architecture (script-vs-agent decision per
  plan item, adaptation to repo variance, CI-failure handling, human review
  gate, centralized merge tracking), two named customer use cases, and a new
  outcome-based pricing model. Does NOT cover: how the "decides whether the
  change needs judgment" routing logic actually works technically, any
  named metric for time-to-completion or cost per changeset, the size or
  scope of the Beta cohort beyond "nearly a thousand changesets," or any
  failure case / repo the tool could not handle.

## Extracted Claims

### Claim 1: Sourcegraph's existing (non-agentic) Batch Changes engine has already been used at very large scale, with the largest single batch change merging more than 2,200 changesets
- **Evidence**: First-party claim about the pre-existing Batch Changes
  product (the substrate Agentic Batch Changes is built on), presented in
  the opening framing paragraph.
- **Confidence**: anecdotal (a superlative, self-reported figure — "the
  largest ... we have seen" — with no customer named and no independent
  verification)
- **Quote**: "The largest single Batch Change we have seen merged more than 2,200 changesets from one change."
- **Our assessment**: This establishes the baseline scale claim the new
  agentic layer is built on top of — useful context for why Sourcegraph
  frames cross-repo orchestration as a solved coordination problem before
  layering agent judgment on top of it, but it is an unaudited, unnamed
  customer superlative and should not be cited as a generalizable benchmark.

### Claim 2: Agentic Batch Changes is architecturally Batch Changes (cross-repo PR orchestration) plus Deep Search (codebase understanding) plus coding agents, forming a single harness that scales from thousands of repos to the largest monorepos
- **Evidence**: Author's own architectural description in "Describe the
  change once. The agent takes it from there."
- **Confidence**: emerging (a first-party architecture description for a
  shipped, GA product, but not independently verified by this Miner beyond
  the post's own text)
- **Quote**: "Agentic Batch Changes is built on Batch Changes and Deep Search, our agent for understanding complex codebases. Together they form an agent harness specialized for applying changes across codebases at any scale, from thousands of repositories to the largest monorepos."
- **Our assessment**: This is the load-bearing architectural claim of the
  post: it explicitly composes three previously-separate capabilities this
  corpus already has notes on individually (Batch Changes' PR orchestration,
  Deep Search's evaluator/aggregation layer) into one product. It is a
  composition claim, not a new primitive — see Cross-References.

### Claim 3: The workflow is: describe the change in plain language, the system scopes the work across the indexed codebase, builds a plan, trials the change in one repository, then rolls out and adapts where repos differ, reacting to CI failures until PRs are ready for human review
- **Evidence**: Author's own step-by-step workflow description, the post's
  most concrete technical claim about how the product operates.
- **Confidence**: emerging (a first-party, specific, multi-step workflow
  description for a GA feature; not independently observed by this Miner
  running the tool)
- **Quote**: "You tell it what needs to change, in plain language. It scopes the work across your indexed codebase, builds a plan, tries the change in one repository, then rolls it out. Where repositories differ, it adapts. A diff is not a shipped change, so when CI fails, it reacts. It keeps working until the pull requests are ready for a human to review and merge, and it tracks merge status the whole way so you can see the change land from one place."
- **Our assessment**: The "trial in one repo, then roll out" sequencing and
  the explicit CI-failure-reaction step are the two most specific,
  guide-relevant details here — they describe a scope → plan → single-repo
  validation → adaptive rollout pattern that is more concrete than a generic
  "AI agent applies changes" claim. No detail is given on how repo
  differences are detected or how many CI-failure-react cycles are typical
  before a PR is abandoned versus fixed.

### Claim 4: Agentic Batch Changes is positioned as extending a single coding agent's capability from one repository to an organization's entire repository set simultaneously
- **Evidence**: A pull-quote in the post, set apart typographically from the
  surrounding body text, functioning as the article's thesis statement.
- **Confidence**: anecdotal (a marketing framing/thesis statement, not an
  empirical claim)
- **Quote**: "Anything a single coding agent can do in one repository, Agentic Batch Changes can orchestrate across all of your repositories at the same time."
- **Our assessment**: This is a strong, unqualified equivalence claim
  ("anything... can do... it can orchestrate across all") that should be
  read as marketing framing rather than a technical guarantee — the post
  gives no example of a task type this fails to generalize to, and no
  discussion of scaling limits (e.g., very large monorepos with unusual
  build systems, or repos without CI).

### Claim 5: For each piece of a plan, the system decides whether the change needs judgment (handed to Claude Code or Codex with codebase context) or just needs doing (handled by a generated script), and it defaults to scripts because most large migrations are repetitive
- **Evidence**: Author's own architectural explanation, given as the
  section heading and body of "Agentic Batch Changes writes scripts more
  often than it deploys coding agents, which is what keeps it efficient at
  scale."
- **Confidence**: emerging (a specific, first-party routing-logic
  description tied to named downstream agents — Claude Code, Codex — for a
  shipped feature)
- **Quote**: "For each piece of a plan, Agentic Batch Changes decides whether the change needs judgment or just needs doing. When it needs judgment, it hands the repository to Claude Code or Codex with specific instructions and codebase context. Most of the time it writes a script, because a large migration is mostly the same change made over and over, and running a script is far more efficient than working out the same change a hundred times over."
- **Our assessment**: This is the single most reusable pattern in the post
  for guide purposes: an explicit script-vs-agent-judgment decision made
  per unit of work, with script generation as the default and full agent
  reasoning reserved for cases needing contextual judgment. This directly
  matches the Mercari customer's own framing of the same idea (Claim 9)
  and is a concrete instance of a "cheapest sufficient method" cost-control
  pattern applied to multi-repo change orchestration specifically.

### Claim 6: Human reviewers can see diffs as they are generated, intervene at any point, and the agent stops and asks when it needs a decision it can't make itself
- **Evidence**: Closing sentence of the script-vs-agent section, describing
  the human-in-the-loop control surface.
- **Confidence**: anecdotal (a feature description with no example given of
  what triggers a stop-and-ask, or how often it occurs in practice)
- **Quote**: "You see diffs as they are generated, you can step in at any point, and when the agent needs a decision, it stops and asks."
- **Our assessment**: This names a specific human-oversight mechanism
  (live diff visibility, ability to interrupt, agent-initiated
  escalation-on-uncertainty) rather than a generic "human in the loop"
  claim, but gives no detail on the escalation trigger's precision — a
  system that escalates too rarely would silently apply wrong changes,
  and too often would erode the claimed script-based efficiency; neither
  failure mode is addressed in the post.

### Claim 7: During the Beta, customers merged nearly a thousand changesets created by Agentic Batch Changes, spanning security remediation to library migrations
- **Evidence**: Author's own aggregate Beta-usage figure, opening the
  "Success we saw from the Beta" section.
- **Confidence**: anecdotal (a rounded, self-reported aggregate figure with
  no Beta cohort size, duration, or per-customer breakdown given)
- **Quote**: "During the Beta, customers merged nearly a thousand changesets created by Agentic Batch Changes, on work that ranged from security remediation to library migrations."
- **Our assessment**: "Nearly a thousand" is a vague quantifier compared to
  the specific "2,200 changesets" and "50+ pull requests" figures elsewhere
  in the same post — it reads as a rounded top-line marketing number rather
  than an audited count, and gives no indication of how many distinct
  customers or repos contributed to it.

### Claim 8: Mercari used Agentic Batch Changes to identify and patch a GitHub Actions environment-variable injection vulnerability across roughly 80 repositories, starting from a single prompt on two repos and extending it org-wide
- **Evidence**: Named customer quote, attributed to Patrick Klitzke, Team
  Lead at Mercari.
- **Confidence**: anecdotal (a single named customer's first-person account,
  not independently verified by this Miner, but attributed to a named
  individual and company rather than anonymous)
- **Quote**: "I looked at a GitHub injection issue where you have to set environment variables correctly. I was able to fix it with one prompt on both the Help Center frontend and backend, then extended this to all repos in Mercari. I found around 80 potential repos affected."
- **Our assessment**: This is the post's most concrete real-world case:
  a specific vulnerability class (GitHub Actions env-var injection), a
  specific starting point (one prompt, two repos), and a specific resulting
  scope (~80 repos). It corroborates the "trial in one repo, then roll out"
  workflow described abstractly in Claim 3 with an actual customer path.

### Claim 9: Mercari's team lead specifically credited the tool with handling repos that have similar-but-not-identical setups, contrasting this with a plain scripted text search-and-replace that lacks usage context
- **Evidence**: Second half of the same Mercari customer quote.
- **Confidence**: anecdotal (single named customer's own framing of why the
  tool succeeded where a plain script would not)
- **Quote**: "With the help of Agentic Batch Changes, you're able to handle repos that have similar, but not identical setups. A normal scripted change would most likely be a text search and replace operation without any context of how it's actually used."
- **Our assessment**: This is a practitioner's own articulation of exactly
  the script-vs-agent-judgment tradeoff Sourcegraph describes architecturally
  in Claim 5 — the customer is naming *why* contextual agent judgment beat a
  naive script for this specific vulnerability class (usage context matters,
  not just syntactic pattern-matching). This is a rare case in the post
  where the vendor's architectural claim and an independent customer's own
  explanation of their experience line up on the same specific mechanism.

### Claim 10: Canva used Agentic Batch Changes to raise and merge 50+ pull requests across repos for a library migration, tracked from a single view, as an alternative to oversized PRs or spreadsheet tracking
- **Evidence**: Named customer quote, attributed to William L., Senior
  Software Engineer at Canva.
- **Confidence**: anecdotal (a single named customer's account, company and
  role given but surname withheld to an initial)
- **Quote**: "We used Agentic Batch Changes to raise and merge 50+ pull requests across our repos as part of a library migration. The web UI made it easy to track each PR and its status. Without it, we would have been managing either huge PRs or spreadsheets; instead, Agentic Batch Changes made the process easier for both reviewers and me."
- **Our assessment**: The specific counterfactual named here — "either huge
  PRs or spreadsheets" — is a concrete articulation of the coordination
  problem this corpus's Tanner vulnerability-remediation note already
  describes abstractly as "ticket-per-team, PR-per-repo, status-by-spreadsheet"
  (see Cross-References). This is the second of only two named customer
  accounts in the post, and the only one describing a non-security use case
  (library migration rather than vulnerability remediation).

### Claim 11: Agentic Batch Changes uses outcome-based pricing — customers pay per changeset merged into their codebase, not per token, seat, or attempt, and unmerged PRs are free
- **Evidence**: Author's own pricing-model description in "Only pay for
  what merges," stated as a factual claim about the launched pricing
  structure.
- **Confidence**: settled (a verifiable, specific fact about how a shipped,
  GA commercial product is priced, not an evidentiary or effectiveness
  claim)
- **Quote**: "You pay per changeset merged into your codebase, not per token, seat, or attempt. If it opens a pull request and your team decides not to merge it, you don't pay for it."
- **Our assessment**: This is a genuinely novel cost model for this
  corpus — every other pricing reference in the corpus to date has been
  token-based, seat-based, or a flat platform fee. An outcome-based model
  (pay only for merged changesets) shifts the vendor's risk onto itself for
  low-quality or rejected changes, which is a meaningful signal of
  confidence in the underlying agent's success rate, though the post gives
  no actual per-changeset price or the underlying merge/PR ratio needed to
  judge whether this is cheaper or more expensive than a token-based
  alternative at scale.

### Claim 12: Sourcegraph frames security remediation and library migrations as two of several use cases, also naming dependency upgrades, deprecated API replacement, framework rollouts, CI pipeline modernization, and end-of-life deadlines as observed uses, explicitly calling these "starting points, not a fixed list"
- **Evidence**: Author's own closing enumeration in the "Success we saw
  from the Beta" section.
- **Confidence**: anecdotal (an illustrative list, not quantified per
  category — no breakdown of how many Beta changesets fell into each use
  case)
- **Quote**: "Security remediation and library migrations are two of the use cases. We've also seen dependency upgrades, deprecated API replacement, framework rollouts, CI pipeline modernization, and end-of-life deadlines. These are starting points, not a fixed list."
- **Our assessment**: Useful as a scope indicator for what kinds of
  cross-repo work this class of tool targets, but every item beyond the two
  named customer cases (security remediation, library migration) is
  asserted without a supporting example — a reader cannot tell from this
  post alone which of dependency upgrades, API replacement, framework
  rollouts, or CI modernization were actually demonstrated versus merely
  anticipated.

### Claim 13: Agentic Batch Changes is generally available today for Sourcegraph Cloud customers, enabled by default
- **Evidence**: Author's own availability statement in the closing section.
- **Confidence**: settled (a verifiable, unambiguous fact about product
  availability, stated directly by the vendor at launch)
- **Quote**: "Agentic Batch Changes is available today for Sourcegraph Cloud customers, on by default."
- **Our assessment**: This confirms the feature is GA (not a limited beta
  or waitlist), which matters for guide purposes when distinguishing
  "available production capability" from "vendor roadmap announcement" —
  this Miner did not independently verify default-on status by inspecting
  a live Sourcegraph Cloud tenant.

## Concrete Artifacts

### Pull-quote thesis statement (verbatim, set apart from body text in the original)
```
Source: https://sourcegraph.com/blog/introducing-agentic-batch-changes

"Anything a single coding agent can do in one repository, Agentic Batch
Changes can orchestrate across all of your repositories at the same time."
```

### Named customer quotes (verbatim)
```
Source: https://sourcegraph.com/blog/introducing-agentic-batch-changes

Patrick Klitzke, Team Lead at Mercari:
"I looked at a GitHub injection issue where you have to set environment
variables correctly. I was able to fix it with one prompt on both the Help
Center frontend and backend, then extended this to all repos in Mercari.
I found around 80 potential repos affected."

"With the help of Agentic Batch Changes, you're able to handle repos that
have similar, but not identical setups. A normal scripted change would
most likely be a text search and replace operation without any context of
how it's actually used."

William L., Senior Software Engineer, Canva:
"We used Agentic Batch Changes to raise and merge 50+ pull requests across
our repos as part of a library migration. The web UI made it easy to track
each PR and its status. Without it, we would have been managing either
huge PRs or spreadsheets; instead, Agentic Batch Changes made the process
easier for both reviewers and me."
```

### Use-case list (verbatim)
```
Source: https://sourcegraph.com/blog/introducing-agentic-batch-changes

"Security remediation and library migrations are two of the use cases.
We've also seen dependency upgrades, deprecated API replacement, framework
rollouts, CI pipeline modernization, and end-of-life deadlines. These are
starting points, not a fixed list."
```

## Cross-References

- **Extends**: `blog-sourcegraph-chan-migrations-less-context.md` — that
  note documents Deep Search's sandboxed "evaluator" mechanism (Claim 3/4:
  running scripts around search APIs so the LLM receives only aggregated
  findings, not raw intermediate results) as an already-shipped capability
  (Release 7.3). This post names Deep Search as one of the two components
  Agentic Batch Changes is built on (Claim 2 in this note) but does not
  itself describe the evaluator mechanism — a reader wanting the technical
  detail of *how* Deep Search understands a codebase before Agentic Batch
  Changes plans a rollout should read the Chan note alongside this one.
  Neither post cross-links to the other.
- **Extends**: `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`
  Claim 8 (no current remediation process scales past a few thousand repos;
  the bottleneck is coordination — "ticket-per-team, PR-per-repo,
  status-by-spreadsheet" — not technical difficulty) and Claim 12 (the
  proposed fix requires "coordinated change: the fix was generated, applied,
  and tracked as pull requests across every affected repository from one
  place"). This post's Canva quote (Claim 10 in this note: "we would have
  been managing either huge PRs or spreadsheets") independently restates
  the identical spreadsheet-tracking failure mode Tanner's post names in the
  abstract, and the Mercari case (Claim 8 in this note) is a concrete,
  named instance of exactly the "coordinated cross-repo pull-request
  remediation with centralized status tracking" capability Tanner's post
  argues enterprises need but usually lack. This post supplies the shipped
  product and two real customer instances; Tanner's post supplies the
  enterprise-scale motivating argument.
- **Extends**: `blog-sourcegraph-dorfman-repo-security-posture.md` Claim 8
  (teams with genuine codebase-wide visibility can "fix at the same scale
  they detect" and "see the blast radius before acting") — the Mercari case
  study (Claim 8 in this note: one prompt on two repos, extended to ~80
  affected repos) is a concrete demonstration of exactly this capability in
  production, closing the gap between Dorfman's normative checklist and an
  actual shipped, named-customer example.
- **Corroborates**: `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`
  — that note's overall lesson is to independently measure a Sourcegraph
  retrieval/agent claim (F1, recall, task completion, cost) rather than
  accept a vendor's aggregate framing at face value. This post's own
  aggregate figures (Claim 1's "2,200 changesets," Claim 7's "nearly a
  thousand changesets" in Beta) are exactly the kind of unquantified,
  unaudited vendor superlative the Jarmak note's methodology would subject
  to independent verification before a guide cites them as settled.
- **Contradicts**: None identified. No existing corpus source argues that
  script-based batch changes are sufficient without any agent-judgment
  fallback for heterogeneous repos, or that outcome-based/per-merge pricing
  is inferior to token-based pricing for this task class, so this source's
  central claims have no direct opposing claim in the corpus to flag as a
  contradiction.
- **Novel**: The explicit per-plan-item script-vs-agent-judgment routing
  decision with scripts as the efficiency default (Claim 5); the two named
  customer accounts of agent-based multi-repo remediation/migration at
  specific scale (Mercari ~80 repos, Canva 50+ PRs — Claims 8-10); the
  outcome-based "pay per changeset merged" pricing model (Claim 11), which
  is the first pay-per-outcome (as opposed to per-token or per-seat) pricing
  model in this corpus; and the explicit naming of Claude Code and Codex as
  the two downstream coding agents Agentic Batch Changes can delegate
  judgment-requiring repos to (Claim 5) are all new to this corpus.

## Guide Impact

- **Chapter 08 (Engineering for speed & scale)**: Add the per-plan-item
  script-vs-agent-judgment routing pattern (Claim 5: default to a generated
  script for repetitive changes, escalate to a full coding agent — Claude
  Code or Codex — only when a repo needs contextual judgment) as a named
  cost/efficiency pattern for multi-repo change orchestration, citing the
  Mercari quote (Claim 9) as independent practitioner corroboration of the
  same tradeoff. This is more specific than a generic "use scripts where
  possible" recommendation because it names the decision granularity
  (per plan item, not per project) and the concrete escalation targets.
- **Chapter 03 (Multi-step agentic patterns) / Chapter 04 (Tool
  orchestration & integration)**: Add the scope → plan → single-repo trial
  → adaptive rollout → CI-failure-reaction workflow (Claim 3) as a named
  pattern for agentic systems operating across many repositories, alongside
  the human-in-the-loop controls described in Claim 6 (live diff visibility,
  interrupt-at-any-point, agent-initiated stop-and-ask on uncertain
  decisions) as the review-gate mechanism that keeps the pattern safe to run
  unattended at scale.
- **Chapter 02 (Economics)**: If the guide adds a section comparing AI
  tooling pricing models, cite Claim 11 (outcome-based, pay-per-merged-
  changeset pricing) as a concrete alternative to the token- or seat-based
  models already documented elsewhere in the corpus, while flagging that no
  actual per-changeset price or underlying merge/reject ratio is disclosed
  in this source, so a cost comparison cannot yet be made quantitatively.

## Extraction Notes

- The blog post renders as an empty shell under a plain `curl` fetch (a
  SvelteKit client-hydrated app), and an initial WebFetch attempt against
  the URL returned HTTP 403. This Miner retried with `curl` using a
  browser User-Agent header, which returned HTTP 200, then located the
  full, unhydrated article text embedded verbatim as a JSON string literal
  inside the page's SvelteKit data-loading `<script>` payload (the `post.content`
  field). This string was extracted and JSON-decoded directly (not
  paraphrased by any summarization model), giving a verbatim copy of the
  complete ~750-word post used as the source for every quote in this note.
- The post embeds one YouTube video (`youtube.com/embed/kY0_rRtJ8BM`) as a
  product demo. This was not transcribed or watched as part of this
  extraction — if the guide later wants demo-specific detail (e.g., actual
  UI screenshots of the plan/rollout/tracking views), that would require a
  separate extraction pass against the video.
- No other sub-pages were linked from this post (unlike the sibling Chan
  migrations note, which linked out to two changelog pages) — this is a
  self-contained launch announcement with no changelog or documentation
  links to follow.
- `confidence_overall` is set to `emerging`: two claims are graded `settled`
  because they are unambiguous, verifiable facts about the shipped product
  (Claim 11, the pricing model; Claim 13, GA availability), and two named
  customer quotes (Claims 8-10) are stronger evidence than an anonymous
  assertion because they're attributed to specific named individuals and
  companies. However, the post's most load-bearing scale claims (Claim 1's
  2,200 changesets, Claim 7's "nearly a thousand" Beta changesets) are
  unaudited, rounded, self-reported vendor superlatives with no cohort size
  or methodology given, consistent with the `emerging` rating already
  applied to every other Sourcegraph blog post in this corpus.
- No contradiction issues filed; see Cross-References — Contradicts.
