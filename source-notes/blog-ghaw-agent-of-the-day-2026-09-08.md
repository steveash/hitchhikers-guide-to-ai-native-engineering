---
source_url: https://github.github.com/gh-aw/blog/2026-09-08-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 8, 2026: CLI Version Checker"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-08
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3322"
---

# Agent of the Day – September 8, 2026: CLI Version Checker

> A profile of CLI Version Checker, a daily dependency-drift monitor for
> eight agentic CLI tools and eight Docker images, whose "opens a pull
> request" framing turns out — on independently fetching the live workflow
> source, its compiled Actions run history, and one traced issue — to
> simplify a more interesting real mechanism: the agent only ever creates a
> `cookie`-labeled, 2-day-expiring issue, which the already-documented Issue
> Monster workflow then picks up and tries to hand to the Copilot coding
> agent. The one issue this note traced through that pipeline (#56841)
> expired and auto-closed with no PR ever appearing. Independent verification
> via the GitHub Actions API also shows the blog's "two runs failed" framing
> understates an actual seven-run losing streak (Aug 30–Sep 5), and that the
> engine actually executing on Sep 8 (Codex CLI, confirmed from job step
> names) does not match the `pi`/`copilot/gpt-5.4` engine declared in the
> workflow source as fetched today.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  AI-authored-post convention documented throughout this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-09-07.md`). This is the first corpus entry
  to profile CLI Version Checker.
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team, profiling a workflow that runs in
  the team's own `github/gh-aw` repository. This note independently fetched
  the live workflow source (`.github/workflows/cli-version-checker.md`, 322
  lines, via `curl` against `raw.githubusercontent.com`), the workflow's
  Actions run history (20 most recent runs, via `gh api
  repos/github/gh-aw/actions/workflows/195931538/runs`), job/step-level detail
  for four specific runs (via `gh api .../actions/runs/<id>/jobs`), and one
  concrete produced issue (#56841, via `gh api
  repos/github/gh-aw/issues/56841` plus its comments) — none of this was
  taken from the blog post's own text. All of it either confirms or
  meaningfully qualifies the blog's claims; see Claims 2, 3, and 4 below.
- **Scope**: Covers the workflow's stated mission, a five-run recent history
  snapshot, its operational discipline (caching, `npm view` preference,
  parallel fetching), its change-handling pipeline (release notes, PR-ref
  URL conversion, change categorization), one audit-trail finding (a blocked
  firewall domain), and a closing "not every agent needs to be flashy"
  framing. Does NOT cover: the Docker-image-specific 3-day release cooldown,
  the exact `create-issue` safe-output configuration (labels, expiry), the
  actual engine/model configured, or the cross-agent issue-to-PR handoff
  mechanism — all of which this note recovered only by fetching the live
  workflow source and the Actions API directly.

## Extracted Claims

### Claim 1: CLI Version Checker runs on a daily schedule and has one job — watch eight named CLI/MCP tools and eight named Docker images for version or digest changes, staying silent when nothing changed
- **Evidence**: Direct first-party description in the post's second
  paragraph, corroborated near-verbatim by the live workflow source's own
  frontmatter `description:` field and body opening line.
- **Confidence**: settled (identical tool/image lists given independently by
  the blog post and the live workflow source)
- **Quote**: "This workflow runs on a daily schedule and has one job: watch
  eight different tools — Claude Code, GitHub Copilot CLI, OpenAI Codex,
  GitHub MCP Server, Playwright CLI, MCP Gateway, Pi, and threat-detect —
  plus a stack of Docker images (actionlint, syft, grype, grant, zizmor,
  poutine, runner-guard, yamllint) for version or digest changes. When it
  finds one, it opens a pull request. When it doesn't, it says nothing and
  exits — no busywork issues, no noise."
- **Our assessment**: The tool and image lists match exactly between the
  blog post and the live workflow's frontmatter `description:` field
  ("Monitors and updates agentic CLI tools (Claude Code, GitHub Copilot CLI,
  OpenAI Codex, GitHub MCP Server, Playwright CLI, MCP Gateway, Pi,
  threat-detect) and Docker images (actionlint, syft, grype, grant, zizmor,
  poutine, runner-guard, yamllint) for new versions"). That is eight tools
  and eight Docker images by direct count of both lists — one of the three
  Prospector triage comments on this issue claimed "nine Docker images" while
  quoting the identical eight-item list, an internal miscount in the triage
  comment itself, not a discrepancy in the source. The "opens a pull request"
  half of this claim, however, does not survive a check against the live
  source's actual `safe-outputs:` configuration — see Claim 2, which
  qualifies this claim rather than contradicting it outright.

### Claim 2: The workflow does not open a pull request itself — its only configured safe output is `create-issue` with a `cookie` label and a 2-day expiry, and this note traced one such issue (#56841) through the "cookie"-label handoff to Issue Monster without a PR ever resulting
- **Evidence**: The live workflow source's `safe-outputs:` frontmatter block
  contains only `create-issue` (with `expires: 2d`, `title-prefix: "[ca] "`,
  `labels: [automation, dependencies, cookie]`, `close-older-issues: true`) —
  no `create-pull-request` key is present anywhere in the file. Independently,
  `gh api repos/github/gh-aw/issues/56841` (a real `[ca]`-titled,
  `cookie`-labeled issue this workflow produced on 2026-08-29, titled "CLI
  version updates: Claude Code 2.1.247→2.1.251, Copilot CLI 1.0.80→1.0.81,
  Pi 0.84.3→0.84.4") shows a comment from Issue Monster — byte-for-byte the
  same "🍪 **Issue Monster selected this for Copilot** ... Om nom nom! 🍪"
  template documented in `blog-ghaw-agent-of-the-day-2026-08-25.md` Concrete
  Artifacts and `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 5 —
  followed two days later by an automatic "closed because it expired" comment
  with no assignee ever recorded on the issue and no PR found via `gh api
  "search/issues?q=repo:github/gh-aw+56841+is:pr"` (0 results).
- **Confidence**: settled for the mechanism (the `safe-outputs:` block is
  read directly from the live source, not inferred; the issue trace is a
  direct `gh api` read, not a paraphrase); anecdotal for how often the
  Issue-Monster handoff actually completes with a PR before the 2-day expiry
  (n=1 traced case, and that one case did not complete)
- **Quote**: (no direct quote from the blog post — the blog post states only
  "it opens a pull request," never mentioning an issue, a label, or a
  second agent; sourced from the live workflow file's `safe-outputs:` block
  and from issue #56841's own comment thread, cited by content per MINER.md
  §4b, not by a fabricated claim number)
- **Our assessment**: This is the same category of gap already established
  twice in this series — a blog post's own prose claim not surviving a check
  against its own subject's live artifact (`blog-ghaw-agent-of-the-day-2026-08-25.md`
  Claim 5 for permissions, `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 1
  for cadence) — so per that precedent this does not meet the MINER.md §4a
  contradiction-filing bar; it is this source's own text being unverifiable
  against its own subject, not two independently-argued sources disagreeing.
  What is new here is more consequential than a cadence or permissions
  imprecision: "opens a pull request" describes a two-stage, cross-agent,
  time-boxed pipeline (this workflow creates a `cookie`-labeled issue → Issue
  Monster's daily scan picks it up from that exact label queue documented in
  `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7 → Issue Monster requests
  Copilot-coding-agent assignment) that can and — in the one instance this
  note could independently trace — did fail to produce a PR before the
  issue's 2-day expiry silently closed it. For Ch04 (Operations): document
  the actual create-issue → label-queue → second-agent → PR chain rather than
  a single-hop "agent opens a PR" model, and flag the expiry race as a
  concrete operational risk: a real dependency update can be silently dropped
  if the downstream agent doesn't complete within the `expires` window, with
  no distinct failure signal raised anywhere in the chain.

### Claim 3: The blog's "last five scheduled runs" snapshot for Sep 4–8 is independently confirmed by the GitHub Actions API, but the two-run failure window it names understates a longer, seven-run losing streak from Aug 30 through Sep 5
- **Evidence**: `gh api repos/github/gh-aw/actions/workflows/195931538/runs`
  (workflow ID resolved via `gh api repos/github/gh-aw/actions/workflows`,
  matching path `.github/workflows/cli-version-checker.lock.yml`) returns,
  for runs #543–#552 in run-number order: failure, failure, failure, failure,
  failure, failure, failure, success, success, success — i.e., runs
  #543–#549 (2026-08-30 through 2026-09-05) all failed, and only #550–#552
  (2026-09-06 through 2026-09-08) succeeded. Run #552's wall-clock duration,
  computed from `run_started_at` to `updated_at` via the same API, is exactly
  7.6 minutes.
- **Confidence**: settled (the run-number/date/conclusion triples and the
  7.6-minute duration are read directly from the GitHub Actions API, not
  paraphrased from the blog); the blog's own "last five" framing is not
  false, just narrower than the full picture the API shows
- **Quote**: "Run #552 (Sep 8) — completed in 7.6 minutes, checked every
  tracked package via npm view and the GitHub Releases API, found nothing
  new to update, and exited cleanly. Run from Sep 7 and Sep 6 — same story:
  full version sweep, no drift detected, quiet success. Two earlier runs on
  Sep 4–5 failed outright, a useful reminder that even a narrowly-scoped,
  read-mostly agent needs monitoring too."
- **Our assessment**: Every specific figure the blog states for the
  five-run window (#552's success and 7.6-minute duration; #550 and #551's
  success; #548 and #549's failure) checks out exactly against the Actions
  API. What the "last five" framing omits — without stating anything false —
  is that the failure window was not two isolated runs but a seven-run
  consecutive streak (#543–#549, 2026-08-30 through 2026-09-05); runs
  #534–#542 (2026-08-21 through 2026-08-29) were themselves a mix of one
  failure and eight successes. A five-run window happened to end right at the
  recovery point, making "two failed runs" read as a minor blip rather than
  a week-long outage of a daily dependency-drift monitor. This is a
  materially different reliability picture than the blog's own framing
  ("a useful reminder that even a narrowly-scoped, read-mostly agent needs
  monitoring too") suggests, though it does not make that framing false — it
  makes it incomplete. For Ch04 (Operations): when citing this or any other
  gh-aw agent's "last N runs" reliability framing from a blog post, pull the
  full recent run-conclusion history via `gh api
  .../actions/workflows/<id>/runs` before repeating the stated window as
  representative; a short window sampled at a recovery point can materially
  understate an outage's real duration.

### Claim 4: The engine that actually executed run #552 on Sep 8 was Codex CLI (confirmed from job step names), which does not match the `engine: id: pi` / `model: copilot/gpt-5.4` configuration present in the workflow source as fetched from `main` on Sep 9
- **Evidence**: `gh api repos/github/gh-aw/actions/runs/34190826308/jobs`
  (run #552) lists step names including "Install Codex CLI," "Install Codex
  CLI in docker-sbx path," and "Execute Codex CLI" in the `agent` job — no
  Copilot-CLI or `pi`-engine step names appear. The live workflow source
  fetched the same day via `curl` from
  `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/cli-version-checker.md`
  declares `engine: {id: pi, model-provider: github}` and `model:
  copilot/gpt-5.4` in its frontmatter. A second failed run's job list (#543,
  2026-08-30) shows the same "Execute Codex CLI" failing step.
- **Confidence**: settled (both the executed-engine evidence and the
  currently-declared engine config are read directly from first-party
  artifacts — Actions job step names and the raw workflow source — not
  inferred or paraphrased)
- **Quote**: (no direct quote; sourced from `gh api
  repos/github/gh-aw/actions/runs/34190826308/jobs` step-name list and the
  live workflow source's frontmatter, per MINER.md §4b — cited by artifact,
  not by a fabricated claim number)
- **Our assessment**: This is a third instance in the corpus of a
  source-vs-live-artifact precision gap for this general category of claim
  (cadence in `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 1, permissions
  in `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 5, and now
  engine/model configuration here) — except this time the gap is not between
  the blog post and its subject, but between the workflow source as it reads
  today and the workflow source as it must have read when it actually
  compiled and ran on 2026-09-08 (the compiled artifact is
  `cli-version-checker.lock.yml`; this note did not fetch the historical
  `.lock.yml` content at that commit, only today's `.md` source and the
  run's own job step names). The practical lesson is sharper than the prior
  two instances: for any gh-aw workflow whose source is actively maintained,
  the current `.md`/frontmatter on `main` is not a reliable descriptor of
  which engine or model produced a specific historical run. For Ch02
  (Harness Engineering): when auditing what engine/model executed a past
  run, use the run's own job step names or the `gh-aw-agentic-workflow` HTML
  comment metadata on any output it produced (as `blog-ghaw-agent-of-the-day-2026-09-07.md`
  Claim 5 did for PR #58996), not the current state of the workflow's source
  file.

### Claim 5: The agent is instructed to check a local cache before any network call, prefer `npm view` over web-fetch for package metadata, and fetch every tool's version in parallel rather than serially
- **Evidence**: Direct first-party description in the post, corroborated
  word-for-word by the live workflow source's "Guidelines" section
  ("**USE NPM COMMANDS**: Use `npm view` instead of web-fetch for package
  metadata queries," "**CHECK CACHE FIRST**," "**PARALLEL FETCHING**: Fetch
  all versions in parallel using multiple npm/WebFetch calls in one turn").
- **Confidence**: settled (blog claim independently corroborated by the live
  source's own imperative guidelines, not just consistent in spirit)
- **Quote**: "The agent is instructed to check a local cache before doing any
  network calls, to prefer npm view over web-fetch for package metadata
  (cheaper and faster), and to fetch every tool's version in parallel rather
  than serially grinding through eight lookups one at a time."
- **Our assessment**: The live source is more specific than the blog about
  *where* the cache lives (`/tmp/gh-aw/cache-memory/`, gh-aw's `cache-memory`
  tool, also documented in `docs-ghaw-cache-memory-reference.md`) and about
  what "prefer npm view" actually means operationally — the source lists the
  exact `npm view <package> version` invocation for each of the five
  npm-distributed tools (Claude Code, Copilot CLI, Codex, Playwright CLI,
  Pi), with the remaining three (GitHub MCP Server, MCP Gateway,
  threat-detect) resolved via `api.github.com` release endpoints instead,
  since they are not npm packages at all. The blog's "prefer npm view over
  web-fetch" framing is accurate for five of eight tools but silently omits
  that three of eight never had a web-fetch-vs-npm-view choice to begin with.
  Separately, `blog-ghaw-weekly-2026-03-30.md` Claim 3 documents a shipped
  security fix (v0.64.3, PR #23374) for an argument-injection vulnerability
  in exactly this class of operation — package/image names passed
  unvalidated into `npm view`/`pip`/`docker` subprocess calls elsewhere in
  gh-aw's own `--validate-packages` tooling. This workflow's `npm view
  <package> version` calls use hardcoded package names (not externally
  supplied strings), so this is not a live instance of that vulnerability
  class — but it is the same technique family, and the Docker-image digest
  fetches (Claim 6) do interpolate a version tag sourced from an external
  GitHub Releases API response into a shell command. For Ch03 (Safety and
  Verification): flag "npm view"/"docker manifest inspect" invocations that
  interpolate externally-fetched version strings as within the same
  technique family as the argument-injection class already fixed once in
  this codebase, even when the immediate package/image name itself is a
  fixed constant.

### Claim 6: When it does detect a real version change, the agent pulls GitHub release notes, converts every `#1234` PR reference into a full external URL, categorizes changes as Breaking/Features/Fixes/Security/Performance, and only then runs `make recompile` before opening a PR
- **Evidence**: Direct first-party description, corroborated and extended by
  the live workflow source's "Research & Analysis" and "Update Process"
  sections, which additionally specify per-tool release-note URLs (e.g.
  Codex's `.../releases/tag/rust-v{VERSION}`) and mark PR-reference-to-URL
  conversion as **CRITICAL** for four of the five tools with public
  repositories.
- **Confidence**: settled (blog claim independently corroborated by the
  live source's explicit, repeated "CRITICAL: Convert PR/issue references...
  to full URLs" instructions for Codex, GitHub MCP Server, Copilot CLI,
  Playwright CLI, and MCP Gateway)
- **Quote**: "When it does detect a real change, it doesn't just bump a
  constant — it pulls GitHub release notes, converts every #1234 PR
  reference into a full external URL, categorizes changes as
  Breaking/Features/Fixes/Security/Performance, and only then runs make
  recompile before opening the PR."
- **Our assessment**: Per Claim 2, "opening the PR" is not literally what
  this workflow's safe output does — it opens the `cookie`-labeled issue
  containing this analysis, and a PR (if any) comes from the downstream
  Issue-Monster/Copilot-coding-agent handoff. The PR-reference-to-URL
  conversion rule matters for exactly the reason `docs-ghaw-network-reference.md`
  Claim 11 documents: URLs to domains not in the workflow's `network.allowed`
  list are redacted to `(redacted)` in output. Converting a bare `#1234`
  into `https://github.com/openai/codex/pull/1234` before that URL reaches
  the issue body sidesteps any ambiguity about whether the domain
  (`github.com`) is allowlisted — and it is, since this workflow's
  `network: allowed: [defaults, node, go, "api.github.com", containers]`
  list (read directly from the live frontmatter) includes GitHub's own
  domains implicitly via `defaults`/`api.github.com`. For Ch04 (Operations):
  document "convert bare PR/issue references to full external URLs before
  including them in generated output" as a reusable pattern for any
  release-note-summarizing agent, independent of whether the target domain
  happens to be allowlisted.

### Claim 7: The agent additionally tracks eight named Docker images by registry digest — not just version tag — applying a 3-day cooldown before adopting a newly-published release, a mechanism the blog post never mentions
- **Evidence**: Live workflow source's "Docker Image Version Checking"
  section: a table of eight images (`ActionlintImage` through
  `YamllintImage`) each with a GitHub Releases API URL, plus a dedicated
  "3-Day Cooldown" subsection and Docker-registry-specific digest-fetching
  instructions (Docker Hub anonymous token flow for five images, `docker
  manifest inspect` or GHCR anonymous token flow for three GHCR-hosted
  images).
- **Confidence**: settled (read directly from the live workflow source; not
  present in the blog post at all, so no blog-vs-source comparison applies —
  this is purely novel-to-the-corpus information the blog omitted entirely)
- **Quote**: "Before considering any Docker image version update, check that
  the release is **at least 3 days old**... This avoids picking up immature
  or quickly-retracted releases. Digest-only updates for an already-pinned
  version are not subject to the release cooldown."
- **Our assessment**: This is a materially more sophisticated supply-chain
  monitoring design than "watch eight Docker images for version changes,"
  the framing the blog post uses. Two distinct signals are tracked
  independently: the release *version* (subject to the 3-day cooldown, to
  avoid chasing a tag that gets pulled or re-tagged shortly after
  publication) and the registry *digest* for whatever tag is currently
  pinned (checked on every run, with no cooldown, because "mutable or
  republished tags" can silently change the bytes behind an unchanged
  version string). This digest-drift concern is a real, previously
  undocumented-in-this-corpus supply-chain risk: a Docker image reference
  pinned as `tag@sha256:<digest>` is normally considered immutable, but if
  the *tag* is later re-pushed by the upstream maintainer with different
  content, only a digest re-check (not a version-string comparison) catches
  it. For Ch03 (Safety and Verification) / Ch04 (Operations): document
  "re-check the registry digest for an already-pinned tag on every run, not
  just when the version string changes" as a distinct supply-chain hardening
  practice, and the 3-day post-release cooldown as a way to avoid updating to
  a release that gets retracted within days of publication.

### Claim 8: The audit trail surfaced a firewalled domain, `ab.chatgpt.com:443`, blocked on every recent run (roughly 1 request out of 50), which this note found is not unique to this workflow — the identical domain was blocked in a different workflow's (Issue Monster's) run around the same period
- **Evidence**: Blog post's direct statement, plus this note's independent
  discovery that issue #56841's Issue-Monster comment (2026-08-30) contains
  the identical GitHub-generated firewall warning: `> [!WARNING]
  <details><summary>Firewall blocked 1 domain</summary>... `ab.chatgpt.com`
  ...`.
- **Confidence**: settled for the blocked-domain fact itself (confirmed by
  two independent workflows' audit output, not just the blog's paraphrase);
  anecdotal for whether the domain is contacted by every gh-aw workflow using
  a particular engine/model or is coincidental to these two specific
  workflows
- **Quote**: "The audit trail also surfaced something small but real: every
  recent run hit a firewalled domain, ab.chatgpt.com:443, and got blocked —
  1 request out of roughly 50 per run. Harmless in this case (the agent's
  actual work sails through on api.openai.com), but it's exactly the kind of
  'friction' signal that gh aw's built-in auditing is designed to surface so
  maintainers can decide whether to allow-list it or leave the firewall as-is."
- **Our assessment**: Finding the same blocked domain independently in Issue
  Monster's audit output (a workflow with a completely different mission,
  schedule, and — per its own frontmatter documented in
  `blog-ghaw-agent-of-the-day-2026-08-25.md` — different tool/model
  configuration) suggests `ab.chatgpt.com` is contacted at a layer common to
  multiple gh-aw workflows (plausibly an engine-level telemetry or health-check
  call made by the `codex` engine runtime itself, given both traced instances
  ran on `engine: codex`-family configurations), not something specific to
  CLI Version Checker's own version-checking logic. This reframes the
  blog's "friction signal" framing: it is evidence of a platform/engine-level
  firewall interaction pattern worth investigating once, not eight (or more)
  separate per-workflow anomalies each needing individual triage. This is
  the same underlying mechanism (`network.allowed` domain redaction/blocking)
  documented generically in `docs-ghaw-network-reference.md` Claims 1–3 and
  11; this pair of traced instances is a concrete production example of that
  mechanism firing identically across unrelated workflows. For Ch04
  (Operations): when an audit trail surfaces a blocked domain, check whether
  the same domain appears in other unrelated workflows' audit output before
  concluding it is specific to the workflow under investigation — a
  platform/engine-level cause has a very different remediation (fix once,
  upstream) than a per-workflow cause (allowlist or fix per workflow).

### Claim 9: The post's closing framing positions restraint and low visibility as a virtue — "not every agent needs to be flashy to be valuable" — the same design principle already established for other gh-aw daily agents
- **Evidence**: Direct closing statement of the post.
- **Confidence**: settled (explicit, first-party statement, consistent with
  the same framing already documented for other agents in this series)
- **Quote**: "There's a quieter lesson here too: not every agent needs to be
  flashy to be valuable. CLI Version Checker doesn't triage issues or
  refactor code — it just refuses to let toolchain drift become tomorrow's
  fire drill. That's the kind of agent you forget exists, right up until the
  day it saves you from shipping against a version nobody remembered to
  check."
- **Our assessment**: This is the same "restraint/low-visibility-as-a-virtue"
  framing already documented for the Dead Code Removal Agent
  (`blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4, restated in
  `blog-ghaw-agent-of-the-day-2026-09-07.md` Claim 8) and for Issue Monster
  (`blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 8's "no fanfare, no
  dashboard to babysit"), now applied to a third, structurally different
  agent (a monitoring/maintenance agent rather than a code-transformation or
  curation agent). Unlike the Dead Code Removal Agent's restraint claim,
  which is backed by a concrete, named "declines to act" behavior (skipping
  ambiguous static-analysis findings), and Issue Monster's, which is backed
  by its narrow three-safe-output action surface, this post's restraint
  framing is not backed by any equivalently concrete "what it declines to do"
  example in either the blog text or the live source — it is closer to a
  house-style rhetorical convention of this blog series than a claim about
  this specific agent's design. For Ch02 (Harness Engineering): when citing
  the "quiet, unflashy agents are valuable" theme across this corpus, note
  that its evidentiary strength varies per agent — some instances (Dead Code
  Removal Agent, Issue Monster) are backed by concrete behavioral
  restraint; this one is closer to editorial framing.

## Concrete Artifacts

### CLI Version Checker: live workflow frontmatter (abridged, fetched via `curl` from `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/cli-version-checker.md`, 2026-09-09)

```yaml
private: true
emoji: "🔢"
description: Monitors and updates agentic CLI tools (Claude Code, GitHub Copilot CLI, OpenAI Codex, GitHub MCP Server, Playwright CLI, MCP Gateway, Pi, threat-detect) and Docker images (actionlint, syft, grype, grant, zizmor, poutine, runner-guard, yamllint) for new versions
on:
  schedule: daily
  workflow_dispatch:
max-daily-ai-credits: 10000
permissions:
  contents: read
  pull-requests: read
  issues: read
  copilot-requests: write
model: copilot/gpt-5.4
strict: false
engine:
  id: pi
  model-provider: github
network:
   allowed: [defaults, node, go, "api.github.com", containers]
tools:
  cli-proxy: true
  web-fetch:
  cache-memory: true
  bash:
    - "*"
  edit:
safe-outputs:
  create-issue:
    expires: 2d
    title-prefix: "[ca] "
    labels: [automation, dependencies, cookie]
    close-older-issues: true
timeout-minutes: 45
```
*Note: this frontmatter, as fetched 2026-09-09, declares `engine: pi` /
`model: copilot/gpt-5.4`; Claim 4 shows the run that actually executed on
2026-09-08 (run #552) used Codex CLI instead, per its own job step names —
so this snapshot should not be read as "what ran on Sep 8," only as "what
the source currently declares."*

### CLI Version Checker: Docker image tracking table (from the live source's "Docker Image Sources" section)

```
Constant           | Current image (example)                                | Releases URL
--------------------|--------------------------------------------------------|---------------------------------------------------------------
ActionlintImage     | rhysd/actionlint:<version>@sha256:<digest>              | api.github.com/repos/rhysd/actionlint/releases/latest
SyftImage           | anchore/syft:<version>@sha256:<digest>                  | api.github.com/repos/anchore/syft/releases/latest
GrypeImage          | anchore/grype:<version>@sha256:<digest>                 | api.github.com/repos/anchore/grype/releases/latest
GrantImage          | anchore/grant:<version>@sha256:<digest>                 | api.github.com/repos/anchore/grant/releases/latest
ZizmorImage         | ghcr.io/zizmorcore/zizmor:<version>@sha256:<digest>      | api.github.com/repos/zizmorcore/zizmor/releases/latest
PoutineImage        | ghcr.io/boostsecurityio/poutine:<version>@sha256:<digest>| api.github.com/repos/boostsecurityio/poutine/releases/latest
RunnerGuardImage    | ghcr.io/vigilant-llc/runner-guard:<version>@sha256:<digest>| api.github.com/repos/vigilant-llc/runner-guard/releases/latest
YamllintImage       | pipelinecomponents/yamllint:<version>@sha256:<digest>   | api.github.com/repos/PipelineComponents/yamllint/releases/latest

3-day cooldown applies to version updates only; digest re-checks for an
already-pinned version run on every execution, cooldown-free.
```
*Source: `.github/workflows/cli-version-checker.md`, "Docker Image Sources"
and "3-Day Cooldown" sections, fetched 2026-09-09.*

### CLI Version Checker: recent Actions run history (independently fetched, `gh api repos/github/gh-aw/actions/workflows/195931538/runs`, 2026-09-09)

```
Run #  Date (2026)   Conclusion
553    Sep 9         success
552    Sep 8         success   (7.6 min, per run_started_at→updated_at)
551    Sep 7         success
550    Sep 6         success
549    Sep 5         failure
548    Sep 4         failure
547    Sep 3         failure
546    Sep 2         failure
545    Sep 1         failure
544    Aug 31        failure
543    Aug 30        failure   ← failure streak starts here, not Sep 4
542    Aug 29        success
541    Aug 28        success
540    Aug 27        success
539    Aug 26        success
538    Aug 25        success
537    Aug 24        success
536    Aug 23        success
535    Aug 22        success
534    Aug 21        failure
```
*Source: GitHub Actions API, `repos/github/gh-aw/actions/workflows/195931538/runs`,
fetched 2026-09-09. Runs #543 and #549 (both failures) show an identical
failed step, "Execute Codex CLI," per `gh api .../actions/runs/<id>/jobs`.*

### CLI Version Checker → Issue Monster: one traced full pipeline instance (issue #56841, fetched via `gh api repos/github/gh-aw/issues/56841` and `.../comments`, 2026-09-09)

```
2026-08-29 05:38 — CLI Version Checker opens issue #56841:
  "[ca] CLI version updates: Claude Code 2.1.247→2.1.251,
   Copilot CLI 1.0.80→1.0.81, Pi 0.84.3→0.84.4"
  labels: automation, dependencies, cookie
  body states: version_constants.go bumped, `make recompile` verified
  (297/297 workflows compiled), no Docker image changes this run.

2026-08-30 11:43 — Issue Monster comments:
  "🍪 Issue Monster selected this for Copilot
   I've identified this issue as a good candidate for automated
   resolution and requested assignment to the Copilot coding agent...
   Om nom nom! 🍪"
  + a firewall warning: "Firewall blocked 1 domain: ab.chatgpt.com"
  (same domain named in this post's Claim 8, now confirmed appearing
  in a second, unrelated workflow's own audit output)

2026-08-31 07:01 — GitHub Actions bot closes the issue:
  "This issue was automatically closed because it expired on
   2026-08-31T05:38:20.692Z."

No assignee was ever recorded on the issue (assignees: []), and
`gh api "search/issues?q=repo:github/gh-aw+56841+is:pr"` returns
0 results — no PR traceable to this issue was found.
```
*Source: `gh api repos/github/gh-aw/issues/56841` and
`repos/github/gh-aw/issues/56841/comments`, fetched 2026-09-09, quoted in
full for the Issue Monster comment and abridged for the issue body.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7 (Issue Monster's
    candidate pool is pre-filtered to only issues carrying a `cookie`
    label) and `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 5 (the exact
    "🍪 Issue Monster selected this for Copilot ... Om nom nom! 🍪" comment
    template): Claim 2 here independently traces a real, concrete instance
    of both — CLI Version Checker's `create-issue` config applies the
    `cookie` label directly, and issue #56841's Issue Monster comment
    matches that template byte-for-byte.
  - `docs-ghaw-network-reference.md` Claims 1–3 and 11 (the `network:`
    field's domain allowlisting and blocked-URL handling): Claim 8 here is a
    second, cross-workflow production confirmation of the same
    blocked-domain mechanism, and Claim 6 here shows why the "convert
    `#1234` to a full URL" instruction matters given Claim 11's redaction
    behavior for non-allowlisted domains.
  - `docs-ghaw-cache-memory-reference.md` (the `cache-memory` tool's
    `/tmp/gh-aw/cache-memory/` storage location and purpose): Claim 5 here
    confirms a concrete production consumer of that mechanism for
    version-check result caching, distinct from the ExpertOps/DailyOps
    consumers already documented there.

- **Contradicts**: No contradiction meeting the MINER.md §4a bar was filed.
  Claim 2's "opens a pull request" vs. the live source's issue-only safe
  output, and Claim 4's engine/model mismatch, both follow the established
  precedent from `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 5 and
  `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 1: a first-party source's
  own prose being unverifiable (or, here, actively contradicted) by its own
  subject's live artifact, not two independently-argued sources disagreeing
  with each other. `CONTRADICTIONS.md` and open `contradiction`-labeled
  issues were checked; no existing entry covers this workflow.

- **Extends**:
  - `docs-ghaw-dependabot.md` (the `gh aw compile --dependabot` mechanism for
    monitoring npm/pip/Go *runtime tool invocations detected inside workflow
    source files*): this source documents a structurally distinct, second
    dependency-drift mechanism in the gh-aw ecosystem — a dedicated daily
    agent that directly checks fixed, hardcoded CLI/Docker targets via `npm
    view`/GitHub Releases/registry digest APIs and self-reports via a
    labeled issue, rather than the compiler scanning workflow source and
    generating standard manifests for Dependabot to monitor. Neither
    mechanism supersedes the other; they cover different dependency
    surfaces (workflow-invoked runtime tools vs. the CLI/container toolchain
    the `gh-aw` project itself ships and depends on).
  - `blog-ghaw-agent-of-the-day-2026-08-25.md` and
    `blog-ghaw-agent-of-the-day-2026-09-03.md` (Issue Monster's `cookie`-label
    dispatch mechanism, previously shown only from Issue Monster's own
    side): this is a third, independently-traced production instance of an
    agent feeding Issue Monster's queue, and the first to be traced all the
    way through to a non-outcome (issue expired, no PR), adding a concrete
    failure case to a pattern previously documented only as a working
    handoff.
  - `blog-ghaw-agent-of-the-day-2026-09-07.md` Claim 5 (PR Sous Chef nudging
    a PR another agent already opened) and Claim 2's Issue-Monster handoff
    here: together these are now two distinct, both independently verified,
    cross-agent composition patterns in the corpus — one where a second
    agent acts on a PR the first agent already created, and one where a
    second agent must first successfully convert an issue into a PR before
    any such nudging could even apply, with no guarantee that conversion
    happens before the issue expires.

- **Novel**:
  - **The `cookie`-labeled, 2-day-expiring `create-issue` safe output as this
    workflow's actual (not PR-direct) mechanism** (Claim 2) — not stated
    anywhere in the blog post.
  - **Docker image registry-digest re-checking with a 3-day version-release
    cooldown** (Claim 7) — an entirely new supply-chain monitoring technique
    to the corpus, distinguishing tag-level version drift from digest-level
    content drift on an unchanged tag.
  - **A concretely traced instance of the `cookie`-label handoff to Issue
    Monster failing to complete before issue expiry** (Claim 2, Concrete
    Artifacts) — the first evidence in the corpus that this handoff pattern
    has a real, unmitigated failure mode, not just a working example.
  - **A cross-workflow-corroborated blocked firewall domain**
    (`ab.chatgpt.com`) appearing identically in two unrelated workflows'
    audit output (Claim 8) — reframes a single-workflow "friction signal"
    as a possible platform/engine-level pattern.
  - **A source-vs-actual-executed-engine mismatch** confirmed via job step
    names rather than blog-vs-source prose (Claim 4) — a new sub-category of
    the precision-gap pattern already established twice in this series for
    cadence and permissions claims.

## Guide Impact

- **Chapter 04 (Operations)**: When documenting agents that appear to "open
  a PR" as their terminal action, verify against the actual `safe-outputs:`
  configuration before repeating that framing — this agent's real mechanism
  is a labeled, time-boxed issue consumed by a second, independently
  scheduled agent (Claim 2). Add the expiry-race failure mode as a named
  operational risk for any multi-hop, label-queue-based agent handoff: if the
  downstream agent doesn't complete before the upstream issue's `expires`
  window, the finding is silently dropped with no distinct alert. Recommend
  either a longer `expires` window for update-tracking issues specifically,
  or a follow-up check that re-opens/re-flags an issue that expired without
  a linked PR.

- **Chapter 04 / Chapter 03 (Supply-Chain Security)**: Add "re-check the
  registry digest for an already-pinned image tag on every run, independent
  of whether the version string changed" (Claim 7) as a named supply-chain
  hardening technique — mutable or republished tags can change content
  without a version bump, and only a digest comparison catches it. Pair with
  the 3-day post-release cooldown as a way to avoid chasing releases that get
  retracted shortly after publication.

- **Chapter 02 (Harness Engineering)**: When auditing which engine/model
  executed a specific historical run, use the run's own job step names or
  embedded `gh-aw-agentic-workflow` metadata (Claim 4), not the workflow
  source's current state on `main` — actively-maintained workflow sources
  can and do drift out of sync with what a past run actually executed.

- **Chapter 04 (Operations)**: When an audit trail flags a blocked domain,
  check whether the same domain appears in other, unrelated workflows'
  audit output before treating it as workflow-specific (Claim 8) — a
  platform/engine-level cause warrants a different fix than a per-workflow
  allowlist change.

## Extraction Notes

1. **Raw HTML fetched via `curl` for the blog post itself, not just
   WebFetch**: an initial WebFetch pass returned a paraphrased summary
   (restructured "Overview"/"Key Details"/"Performance Metrics" headings not
   present in the source's own prose) that, on comparison, was largely
   accurate in substance but not safe to quote from directly per MINER.md
   §2a. The post was re-fetched via `curl` against the live URL and the
   article body extracted from the rendered HTML with a Python
   tag-stripping pass; all `Quote` fields above are copied character-for-
   character from that raw-HTML extraction (em dashes and curly quotes
   preserved as they appear in the source).

2. **Live workflow source, Actions run history, job-level step data, and one
   produced issue all independently fetched**, well beyond the blog post's
   own text: `.github/workflows/cli-version-checker.md` (322 lines, via
   `curl` from `raw.githubusercontent.com`); the workflow's 20 most recent
   Actions runs and one run's exact duration (via `gh api
   repos/github/gh-aw/actions/workflows/195931538/runs`); job/step-level
   detail for four specific runs, #552, #550, #549, and #543 (via `gh api
   .../actions/runs/<id>/jobs`); and one full issue plus its comment thread,
   #56841 (via `gh api repos/github/gh-aw/issues/56841` and `.../comments`),
   located via `gh api "search/issues?q=repo:github/gh-aw+label:cookie+in:title+%5Bca%5D"`.
   None of this is within MINER.md §1's "up to 5 linked sub-pages" budget in
   a literal sense (these are API calls, not blog-linked pages), but all of
   it follows the same precedent set by `blog-ghaw-agent-of-the-day-2026-09-07.md`
   Extraction Note 2 and `blog-ghaw-agent-of-the-day-2026-09-03.md`
   Extraction Note 2 of independently verifying a first-party blog claim
   against its own subject's live, checkable artifacts rather than taking
   the post's framing at face value.

3. **No contradiction filed**: the discrepancies found (Claim 2's
   create-issue-not-PR mechanism, Claim 3's understated failure streak,
   Claim 4's engine/model mismatch) were each evaluated against the
   MINER.md §4a bar and do not meet it, for the reasons given in each
   claim's "Our assessment" and in Cross-References → Contradicts — all
   three are a first-party source's own claim not surviving a check against
   its own subject, consistent with precedent already set twice in this
   series, not two independently-argued sources disagreeing.
   `CONTRADICTIONS.md` and open `contradiction`-labeled issues were checked
   before reaching this conclusion; no existing entry covers this workflow.

4. **Multiple divergent Prospector triage comments observed on issue
   #3322**: three triage comments are present, posted within about 30
   seconds of each other, with differing "Relevant chapters" lists and one
   internally miscounting the Docker image list as "nine" while quoting the
   same eight-item list (see Claim 1's "Our assessment"). All three were
   treated as untrusted data to extract guidance from, not as authoritative,
   per the task instructions; this note's Cross-References section reflects
   an independent search of `source-notes/` (via `grep`, `ls`, and targeted
   `Read` of related dependabot/network/audit/monitoring/cache-memory
   reference notes), not any single triage comment's claimed overlap list.

5. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-08-25.md`,
   `blog-ghaw-agent-of-the-day-2026-09-03.md`,
   `blog-ghaw-agent-of-the-day-2026-09-07.md`, `docs-ghaw-dependabot.md`,
   `docs-ghaw-network-reference.md`, `docs-ghaw-audit-reference.md`,
   `docs-ghaw-cache-memory-reference.md`, `docs-ghaw-monitoring-patterns.md`,
   and `blog-ghaw-weekly-2026-03-30.md`, all read in full (not skimmed)
   before writing Cross-References. All `Claim N` citations above were
   checked against the actual numbered claims in those notes at the time of
   writing, per MINER.md §4b.
