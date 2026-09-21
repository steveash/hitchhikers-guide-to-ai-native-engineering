---
source_url: https://simonwillison.net/2026/Sep/14/commit-rewriter/
source_type: blog-post
title: "commit-rewriter 0.1"
author: Simon Willison
date_published: 2026-09-14
date_extracted: 2026-09-21
last_checked: 2026-09-21
status: current
confidence_overall: anecdotal
issue: "#3589"
---

# commit-rewriter 0.1

> Simon Willison released `commit-rewriter`, a local web app for batch-editing
> git commit messages before publication, built specifically to sanitize
> commits from Datasette's security-release workflow that were "full of
> coding agent cruft and references to issue IDs from our private repository."

## Source Context

- **Type**: blog-post (Simon Willison "Release" link-blog entry, ~90 words of
  original text plus a one-line shell command; consistent with the format of
  other Willison tool-release posts already in this corpus, e.g.
  `blog-simonwillison-shot-scraper-1-11-release.md` and
  `blog-simonwillison-sqlite-utils-421.md`). The blog post itself is thin, so
  per MINER.md §1 the linked GitHub repository (release notes and README) and
  the linked Datasette security-release post were also fetched to establish
  the tool's full functionality and the concrete event that motivated it.
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  and `sqlite-utils`, and is a `trusted-feed` source already cited dozens of
  times in this corpus. This is a first-person tool-release report about
  software he wrote himself, for a problem he hit himself (cleaning up commits
  for the Datasette 1.0a39/0.65.4 security releases, documented in
  `blog-simonwillison-datasette-1-0a39.md`). No third-party or vendor framing.
- **Scope**: Covers what the tool does, how to run it, and the specific
  motivating problem (agent-generated commit messages unfit for a public
  repository). Does NOT cover: the tool's internal implementation (how commit
  rewriting is performed under the hood — likely `git filter-branch` /
  `git rebase` machinery, but the source never states this), how long it took
  to build, whether any commits ended up not being editable, or any usage
  data beyond the one motivating incident. The post does not name which
  coding agent(s) produced the "cruft" — it is described generically as
  "coding agent cruft."

## Extracted Claims

### Claim 1: The tool was built to solve a specific, named problem — commits from the Datasette security-release work were "full of coding agent cruft and references to issue IDs from our private repository" and therefore unfit for a public repo
- **Evidence**: First-party statement of motivation, tied to a verifiable prior event (the Datasette 1.0a39/0.65.4 security releases, already documented in `blog-simonwillison-datasette-1-0a39.md`, which describes Willison and Alex Garcia running a multi-model coding-agent security audit — Claude Fable 5.1, GPT-5.6 Sol, GPT-6 Astra — "working in a shared private repository").
- **Confidence**: anecdotal (single practitioner, single incident, but independently corroborated by the linked prior release's own documented private-repo workflow)
- **Quote**: "I built this little web app the other day to help edit the commit messages for the Datasette security releases. The initial commits were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication."
- **Our assessment**: This is a concrete, named instance of a failure mode distinct from what's elsewhere in this corpus: it's not that the agent-generated commit messages omitted intent (the Kenton Varda / intent-debt pattern), it's that they leaked *internal-only artifacts* — references to a private issue tracker — into text that was about to become part of a public, published repository. That is a specific publication-hygiene risk of doing agent-assisted work in a private staging repo before a public release, one this corpus had not previously documented (see Novel, below).

### Claim 2: The tool is a local web app, launched with a single `uvx` command against a target repo path (or the current directory)
- **Evidence**: Direct usage instructions in both the blog post and the GitHub README.
- **Confidence**: settled (directly verifiable — package published to PyPI and GitHub)
- **Quote**: "If you want to edit the commit messages for a repository you can run it like this: `uvx commit-rewriter path/to/repo` Omit the path if you are already in the directory for that repo."
- **Our assessment**: The `uvx` invocation (ephemeral, no persistent install required) matches the same zero-install-friction pattern Willison uses across his other small tools already in this corpus (`shot-scraper`, `sqlite-utils`) — consistent with a broader practitioner habit of shipping single-purpose utilities as instantly runnable CLIs/web apps rather than scripts you have to clone and configure.

### Claim 3: Before applying any edits, the tool creates a timestamped branch of the repository's current state specifically so changes can be reverted
- **Evidence**: Direct description of the tool's safety mechanism in the blog post, corroborated by the README's near-identical description.
- **Confidence**: settled
- **Quote**: "When you submit your edits the tool creates a timestamped branch of your current repo state - to allow you to revert if you need to - and then rewrites every commit from the first one you edited to the most recent."
- **Our assessment**: This is a minimal but concrete safety pattern for any tool that rewrites git history: snapshot-before-mutate via a disposable branch, rather than requiring the user to remember to do so manually first. It's the same underlying discipline as "always work on a branch," applied automatically by the tool rather than left to user diligence — a useful, generalizable detail for any guide content about tools that rewrite local git state.

### Claim 4: Editing even one historical commit message forces a rewrite of every commit from that point through the current HEAD, not just the commit(s) the user actually edited
- **Evidence**: Direct statement of the rewrite mechanism.
- **Confidence**: settled
- **Quote**: "rewrites every commit from the first one you edited to the most recent"
- **Our assessment**: This is an inherent consequence of git's hash-chaining (changing any commit's message changes its hash, which changes every descendant commit's hash), not a design choice the post frames as a caveat — but it is an important operational detail: this tool is for rewriting *local, not-yet-pushed* history before publication, not for editing messages on a branch others have already pulled. That matches the described use case exactly (cleaning up commits before they become public) and is worth stating explicitly for any guide content that recommends the tool, since applying it to already-shared history would break every collaborator's local clone.

### Claim 5: The web UI supports commit-level search/filtering and shows a live count of pending, unsaved edits before they are applied
- **Evidence**: README description and screenshot alt-text, both fetched directly from the GitHub repository.
- **Confidence**: settled
- **Quote**: "A toolbar shows a pending edits count with Discard drafts and Rewrite commit messages buttons, followed by a search box for message, author, or hash and an Edited only checkbox. A left sidebar titled Navigate commits lists recent commit messages with their short hashes. The main panel shows a card for each commit with its hash, author and timestamp, an editable text area containing the commit message, and a View full formatted diff toggle."
- **Our assessment**: This describes a genuinely batch-oriented editing workflow (search across many commits, filter to only the ones already touched, review a running edit count, then apply or discard as one unit) rather than a one-commit-at-a-time `git commit --amend` loop. For a maintainer cleaning up dozens of commits before a release — the Datasette security release scenario in Claim 1 — a batch UI with search-by-hash/author/message is a meaningfully different (and likely faster) workflow than editing history commit-by-commit on the command line.

### Claim 6: The tool is distributed as an installable, tested, open-source Python package (PyPI, Apache 2.0, CI test suite), not a one-off gist or snippet
- **Evidence**: README badges and Contributing section fetched from the GitHub repository.
- **Confidence**: settled
- **Quote**: "`pip install commit-rewriter` # or `uv tool install commit-rewriter`" and, under Contributing: "To run the tests: `uv run pytest`. To re-take the screenshot using shot-scraper: `shot-scraper multi shots.yml`"
- **Our assessment**: Willison ships this cleanup utility with the same production packaging conventions (PyPI release, license badge, CI test badge, a documented test command) as his other tools in this corpus, and even reuses his own `shot-scraper` tool (`blog-simonwillison-shot-scraper-1-11-release.md`) to keep the README screenshot current — a small but concrete example of one practitioner's tool ecosystem being self-reinforcing (a tool built to fix one workflow friction is itself maintained using another of his own tools).

### Claim 7: The server defaults to port 8000 and the port is configurable via a flag
- **Evidence**: GitHub release notes and README, independently corroborating the same default and flag.
- **Confidence**: settled
- **Quote**: "Defaults to port 8000, add -p 8033 to run on a different port." (GitHub release 0.1 notes) — the README states the same default with a different example flag value: "Defaults to running on `http://127.0.0.1:8000` - use `-p/--port 8002` to run on a different port."
- **Our assessment**: A minor operational detail included here mainly because the two sources (release notes vs. README) use different example port numbers for the same flag, confirming this is a real configurable flag rather than a fixed value, and that the two documents were written/updated somewhat independently of each other.

### Claim 8: Willison categorizes this release under his own `ai-assisted-programming` tag, alongside `git`, `projects`, and `python` — explicitly filing it as tooling built in response to an AI-assisted-development friction point, not a generic git utility
- **Evidence**: Post metadata (tag list) on the source page.
- **Confidence**: anecdotal (author's own self-categorization, not an independent judgment)
- **Quote**: (no direct quote; the tags "git", "projects", "python", "ai-assisted-programming" appear as a list of clickable tag links at the foot of the post, not as prose — see paraphrase above)
- **Our assessment**: This is a small but useful corroborating signal: Willison himself frames this specific tool, unprompted, as belonging to his `ai-assisted-programming` body of work rather than treating it as an unrelated git utility that happens to be useful for AI-generated commits. It reinforces that the "coding agent cruft" motivation in Claim 1 is the primary framing, not an incidental detail.

## Concrete Artifacts

### The full blog post (verbatim, from simonwillison.net/2026/Sep/14/commit-rewriter/, fetched via direct HTML retrieval)
```
commit-rewriter 0.1
— Python web app to help rewrite your commit messages

I built this little web app the other day to help edit the commit messages
for the Datasette security releases. The initial commits were full of
coding agent cruft and references to issue IDs from our private repository,
so they weren't fit for publication.

If you want to edit the commit messages for a repository you can run it
like this:

uvx commit-rewriter path/to/repo

Omit the path if you are already in the directory for that repo.

When you submit your edits the tool creates a timestamped branch of your
current repo state - to allow you to revert if you need to - and then
rewrites every commit from the first one you edited to the most recent.

Posted 14th September 2026 at 12:28 am
Tags: git, projects, python, ai-assisted-programming
```

### GitHub release 0.1 notes (verbatim, from github.com/simonw/commit-rewriter/releases/tag/0.1 page metadata)
```
Initial release.
Run uvx commit-rewriter path/to/repo to start a local web app for
rewriting commit messages in that repo.
Defaults to port 8000, add -p 8033 to run on a different port.
```

### README.md (verbatim excerpts, from raw.githubusercontent.com/simonw/commit-rewriter/main/README.md)
```
Local web app for editing local commit messages to a Git repository.

## Usage

uvx commit-rewriter /path/to/repository

Or omit the path if the repository is your current working directory.

Defaults to running on http://127.0.0.1:8000 - use -p/--port 8002 to run
on a different port.

Edit multiple commit messages using the web UI. When you apply them the
tool will first create a branch to back up the repository prior to
making the changes.

## Installation

pip install commit-rewriter
# or
uv tool install commit-rewriter

## Screenshot
[alt text] Screenshot of the commit-rewriter web interface. A heading reads
commit-rewriter above the repository path and current branch and commit
hash, with a short description of the tool. A toolbar shows a pending
edits count with Discard drafts and Rewrite commit messages buttons,
followed by a search box for message, author, or hash and an Edited only
checkbox. A left sidebar titled Navigate commits lists recent commit
messages with their short hashes. The main panel shows a card for each
commit with its hash, author and timestamp, an editable text area
containing the commit message, and a View full formatted diff toggle.

## Contributing

To run the tests:
uv run pytest

To re-take the screenshot using shot-scraper:
shot-scraper multi shots.yml
```
License badge on the README: Apache 2.0.

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-1-0a39.md` (Claim 5): that note documents
    Willison and Alex Garcia "working in a shared private repository" while
    running a multi-model coding-agent security audit (Claude Fable 5.1,
    GPT-5.6 Sol, GPT-6 Astra) ahead of the Datasette 1.0a39/0.65.4 public
    releases. This source's Claim 1 is the direct, dated sequel: three days
    after that release shipped (2026-09-11 → 2026-09-14), Willison built and
    released the tool needed to sanitize the "issue IDs from our private
    repository" that leaked into commit messages during that exact private
    audit-and-fix workflow. Read together, the two notes give a full
    before/after picture of one real security-release cycle: private-repo
    multi-model audit → publication-hygiene cleanup tooling.
  - `blog-simonwillison-kenton-varda-change-descriptions.md` (Claims 1–3):
    both sources document a named practitioner finding AI-generated
    change-documentation artifacts (commit messages, in both cases) unfit
    for use as originally produced. The two responses diverge instructively:
    Varda declared a team-wide moratorium banning AI-written commit
    messages, PR descriptions, and issue/ticket text outright. Willison, on
    the same artifact type (commit messages), kept AI-assisted commit
    authorship but built a dedicated tool to let a human batch-review and
    rewrite the messages before they become public — a cleanup gate rather
    than a ban. This is a useful contrast for the guide: "ban AI-authorship
    of an artifact type" and "keep AI-authorship but add a mandatory human
    sanitization step before publication" are two distinct, non-contradictory
    responses to the same underlying problem (AI-generated commit text isn't
    fit for its intended audience as-is), not competing claims about which is
    universally correct — Varda's failure mode was missing high-level framing,
    while Willison's was leaked internal references, which is itself a reason
    the two practitioners reached for different fixes.
  - `blog-simonwillison-shot-scraper-1-11-release.md`: `commit-rewriter`'s
    own README documents using `shot-scraper` (also built and maintained by
    Willison) to regenerate its interface screenshot — a small, concrete
    example of Willison's tool ecosystem being self-reinforcing.

- **Contradicts**: None filed. See the Varda corroboration above: this is a
  divergent remedy for a related problem, not an opposing claim about what
  practitioners should do — both responses are compatible with a broader
  guide recommendation of "don't publish AI-generated change text unreviewed,"
  they just differ on whether AI-authorship is banned or gated.

- **Extends**: `blog-simonwillison-datasette-1-0a39.md` — that note's
  Extraction Notes and Guide Impact sections cover the audit and disclosure
  process itself but do not mention any post-audit publication-hygiene step
  for the resulting commit history; this source fills that specific gap with
  a named, concrete tool and a stated reason for building it.

- **Novel**: The specific failure mode named in Claim 1 — agent-generated
  commit messages leaking references to a *private* issue tracker into text
  destined for a *public* repository — is new to this corpus. Existing
  agent-generated-commit-text coverage (Varda) is about missing high-level
  framing; this source is about leaked internal-only content, a distinct
  publication/confidentiality hygiene risk specific to teams that do
  agent-assisted work in a private staging repo before a public release.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a specific caution for any workflow
  where agent-assisted work happens in a private repository ahead of a public
  release (e.g., embargoed security fixes, as in
  `blog-simonwillison-datasette-1-0a39.md`): agent-generated commit messages
  may reference internal-only artifacts (private issue/ticket IDs) that must
  be scrubbed before the commit history becomes public. Cite this source's
  Claim 1 as a concrete, named instance and Claim 3–4 (timestamped backup
  branch, then rewrite from the first edited commit forward) as the
  mechanical pattern for doing the cleanup safely on local, not-yet-pushed
  history.
- **Chapter 02 (Harness Engineering)**: Add `commit-rewriter`'s batch-edit
  workflow (Claim 5: search by message/author/hash, filter to edited-only,
  review a pending-edit count before applying) as a concrete example of
  purpose-built tooling for a narrow agent-output-cleanup task, complementing
  the more general "cleanup layer for agent-generated code" pattern this
  chapter already covers. Distinguish it from the Kenton Varda moratorium
  pattern (ban AI-authorship outright): this is the "add a mandatory human
  sanitization gate, keep AI-authorship" alternative, and the guide should
  present both as legitimate options depending on whether the team's problem
  is missing intent (Varda) or leaked internal content (this source).

## Extraction Notes

- The blog post itself was fetched twice: once via WebFetch (AI-summarized,
  used only for orientation) and once via direct `curl` + tag-stripping, with
  every quote in this note checked against the raw-HTML-derived text, not the
  WebFetch summary.
- Two linked pages were additionally fetched per MINER.md §1's "follow up to
  5 linked pages" guidance: the GitHub release page
  (github.com/simonw/commit-rewriter/releases/tag/0.1, fetched via `curl` —
  the rendered HTML body did not expose plain release-note text directly, so
  the verbatim release notes were taken from the page's `og:description` /
  `twitter:description` meta tags, which GitHub populates from the same
  release-notes markdown) and the project's `README.md` (fetched directly via
  `raw.githubusercontent.com`, which returns plain Markdown rather than
  rendered HTML, avoiding any tag-stripping risk for that quote). The
  Datasette security-release post itself
  (datasette.io/blog/2026/september-security-releases/) was also re-fetched
  to confirm the "Datasette security releases" link target and cross-check
  it against the already-existing `blog-simonwillison-datasette-1-0a39.md`
  note rather than re-extracting it as new material.
- The tool's actual git-rewriting mechanism (e.g., whether it shells out to
  `git filter-branch`, `git rebase --exec`, or reconstructs history via
  `git commit-tree`) is not stated anywhere in the three fetched pages and is
  not claimed here — Claim 3 and Claim 4 describe only the externally
  observable behavior (branch backup, then full downstream rewrite), not the
  implementation.
- No contradiction with any existing corpus note was found (see
  Cross-References → Contradicts); the Kenton Varda comparison is a genuine
  divergence in practitioner remedy, not an opposing factual claim, so no
  contradiction issue was filed per MINER.md §4a.
- Cross-reference claim numbers were verified by re-reading
  `blog-simonwillison-datasette-1-0a39.md` in full and confirming Claim 5's
  content and numbering directly against its `### Claim 5:` heading before
  citing it here.
