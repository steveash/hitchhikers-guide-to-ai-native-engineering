---
source_url: https://simonwillison.net/2026/Jul/12/shot-scraper/
source_type: blog-post
title: "Release: shot-scraper 1.11"
author: Simon Willison
date_published: 2026-07-12
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: settled
issue: "#1915"
---

# Release: shot-scraper 1.11

> A one-sentence release "beat" — the same thin format as
> `blog-simonwillison-shot-scraper-1-10-release.md` — that frames shot-scraper
> 1.11 as minor command-option-consistency polish plus a fix to the `server:`
> startup delay used by `shot-scraper video` and `shot-scraper multi`. The
> beat itself says nothing about how the release was built, but the GitHub
> commit trail shows all three shipped fixes were authored by Claude Fable 5
> in a single Claude Code session, batch-closing one long-backlogged issue
> (filed September 2023) alongside two issues opened within the previous
> four months.

## Source Context

- **Type**: blog-post (release announcement — a "beat" in Simon Willison's
  format, matching the `class="beat"` structure already documented in
  `blog-simonwillison-shot-scraper-1-10-release.md`; one introductory
  sentence plus a four-item changelog, no companion essay).
- **Author credibility**: Simon Willison is the creator and maintainer of
  shot-scraper; this is first-party release documentation. The linked GitHub
  release (`simonw/shot-scraper` tag `1.11`) is the authoritative changelog,
  also authored by him, and its `body` field was fetched directly via the
  GitHub REST API rather than scraped from rendered HTML.
- **Scope**: Covers four changelog items (server startup polling, `--js-file`
  option, `js_file:` YAML key, `--timeout` consistency) and the four GitHub
  issues they close (#197, #192, #118, and #177 — the last not mentioned in
  the blog post or the release body at all, only visible in a commit
  message). Does not cover: adoption, usage in the wild, or anything beyond
  the changelog bullets, the closed issues, and the commits that closed them.
  Auto-discovered via the `simon-willison` trusted feed per the issue body.

## Extracted Claims

### Claim 1: `server:` processes used by `shot-scraper multi` and `shot-scraper video` now poll for up to 30 seconds for the target URL to accept TCP connections, replacing a fixed one-second `time.sleep(1)` delay
- **Evidence**: Blog post changelog bullet 1, matching the GitHub release
  body verbatim; cross-checked against the actual code diff in the fixing
  commit.
- **Confidence**: settled (shipped, first-party changelog text, independently
  confirmed against the merged code diff)
- **Quote**: "`server:` processes used by `shot-scraper multi` and `shot-scraper video` now wait up to 30 seconds for the target URL to accept connections, polling for port availability and replacing the previous fixed one-second delay. #197"
- **Our assessment**: This directly hardens the `server:` setup-step mechanism
  that `blog-simonwillison-shot-scraper-1-10-release.md` Claim 2 documents as
  part of the `shot-scraper video` storyboard vocabulary. A fixed one-second
  delay is exactly the kind of flaky timing assumption that makes an
  agent-invoked verification tool unreliable against real dev servers (e.g.
  Django, which can easily take longer than a second to boot) — this is a
  concrete reliability fix to the specific mechanism that note's Guide Impact
  section already flags as relevant to CI-integrated demo recording.

### Claim 2: The `server:` timeout fix (#197) was split from #194 — the same issue the 1.10 release notes credited for the original `shot-scraper video` command — and the underlying `ERR_CONNECTION_REFUSED` failure mode had already been reported by an external user (issue #177) a full year before 1.11 shipped
- **Evidence**: Issue #197's body ("Split from: #194"), fetched via the
  GitHub REST API; issue #177's body and `created_at` (2025-07-17),
  independently fetched; the fixing commit's trailer ("Closes #197, closes
  #177").
- **Confidence**: settled (directly queried via the GitHub API at extraction
  time — issue bodies, creation dates, and the closing commit's `Closes`
  trailer, not inferred from the blog post)
- **Quote** (issue #177, filed 2025-07-17): "My problem is I have a rather large Django project and the server has not finished starting by the time the first shot is processed. So I end up with `ERR_CONNECTION_REFUSED` errors from playright." (sic — "playright" is the reporter's typo for Playwright, preserved as filed)
- **Our assessment**: The blog post and even the GitHub release body only
  cite #197; neither mentions #177 at all. This means the changelog
  understates the fix's history — a concrete external bug report describing
  exactly this failure mode (Django + `ERR_CONNECTION_REFUSED`) sat open for
  a year before the internal video-feature team split off #197 and the fix
  landed in the same commit that also closed #177. The reporter's proposed
  fix (an explicit `wait: 5` YAML parameter) was not what shipped — the
  maintainer chose automatic TCP-connect polling instead, which fixes the
  problem without requiring every storyboard author to hand-tune a wait
  value.

### Claim 3: The `shot-scraper`, `pdf`, `html`, `accessibility`, and `har` commands gained a `--js-file` option for loading JavaScript from a local file, stdin, or `gh:username/script`, as an alternative to the existing `--javascript` string argument
- **Evidence**: Blog post changelog bullet 2, matching the GitHub release
  body verbatim.
- **Confidence**: settled (shipped, first-party changelog text)
- **Quote**: "The `shot-scraper`, `pdf`, `html`, `accessibility` and `har` commands now have a `--js-file` option for loading JavaScript from a local file, standard input or `gh:username/script`, as an alternative to `--javascript`which accepts the string of JavaScript directly as an argument. #192"
- **Our assessment**: A practical option, not a new capability — `--javascript`
  already accepted arbitrary JS, but only as an inline command-line string.

### Claim 4: The motivating use case for `--js-file` (issue #192) was hitting command-line length limits when passing large JavaScript payloads inline — specifically, a 4MB script assembled from cookie-banner/annoyance block lists
- **Evidence**: Issue #192's body, fetched directly via the GitHub REST API.
- **Confidence**: settled (first-party bug-report text from the person who
  filed the feature request, confirmed as the issue the shipped option
  closes)
- **Quote**: "There's already the --javascript option, but if you're adding a lot of JS, you run into command line lengths problem. My usecase is that I want to remove cookie banners and other annoyances, so I've converted various block lists to JS. This leads to 4MB of generated JS to run, so it's not practical to pass that in on the command line."
- **Our assessment**: This is not in the blog post or the release body at
  all — the changelog text describes the mechanism (`--js-file`) but not the
  concrete failure mode it fixes. It's a useful data point for anyone citing
  `--javascript`/`--js-file` in the guide: shell command-line length limits
  are a real, hit-in-practice constraint on inline-string tool arguments once
  payloads reach single-digit megabytes, independent of any LLM context-window
  concern.

### Claim 5: `shot-scraper multi` YAML storyboards gained an equivalent `js_file:` key alongside the existing `javascript:` key
- **Evidence**: Blog post changelog bullet 3, matching the GitHub release
  body verbatim; the fixing commit's message confirms the YAML key is
  literally named `javascript_file:`, not `js_file:` as the blog post prose
  states.
- **Confidence**: settled for the feature's existence; the exact key name is
  a discrepancy between two first-party sources (see Our assessment)
- **Quote** (blog post / release body): "`shot-scraper multi` supports the equivalent `js_file:` YAML key."
- **Quote** (fixing commit message): "shot-scraper multi YAML items can use a javascript_file: key for the same purpose. Using both javascript and javascript-file together is an error."
- **Our assessment**: The blog post and GitHub release body both say `js_file:`;
  the commit message that actually implements the feature says
  `javascript_file:`. We flag this as a documentation/commit-message naming
  discrepancy rather than resolving it ourselves — we did not fetch the
  merged `cli.py` source to check which string the parser actually accepts.
  Anyone citing this option in the guide should verify the flag name against
  the current `shot-scraper` docs rather than trusting either source here
  verbatim, since the two first-party texts disagree.

### Claim 6: The `shot-scraper javascript` and `shot-scraper html` commands gained a `--timeout` option, closing issue #118 — a consistency request originally filed on 2023-09-09, nearly three years before it was resolved
- **Evidence**: Blog post changelog bullet 4, matching the GitHub release
  body verbatim; issue #118's title and `created_at` (2023-09-09T00:54:37Z),
  fetched via the GitHub REST API.
- **Confidence**: settled (first-party changelog text plus directly-queried
  issue metadata)
- **Quote** (changelog): "The `shot-scraper javascript` and `shot-scraper html` commands now have a `--timeout` option for consistency with other commands. #118"
- **Quote** (issue #118 title): "Make --timeout option consistent across all commands (including javascript)"
- **Our assessment**: This mirrors the theme `blog-simonwillison-shot-scraper-video.md`
  Claim 11 already documents for the `shot-scraper video` feature itself
  (filed February 2024, shipped mid-2026, described by Willison as a feature
  he "almost certainly wouldn't have taken on without coding agent support")
  — a small, well-defined, long-open maintenance issue that sat for years
  before being cleared. Unlike Claim 11's case, this is not a feature but a
  minor consistency fix, and the blog post attaches no narrative to it at
  all; the multi-year gap is only visible by cross-referencing the issue's
  creation date against the release date.

### Claim 7: All three code changes in this release (the `server:` polling fix, `--js-file`, and `--timeout`) were authored by "Claude Fable 5" in a single Claude Code session — a fact stated nowhere in the blog post or the GitHub release notes, and visible only in the `Co-Authored-By` / `Claude-Session` trailers on the three closing commits
- **Evidence**: The three commits that close #197/#177, #192, and #118
  (`cb74ef2`, `9b181d4`, `6629e03` in `simonw/shot-scraper`), fetched
  directly via the GitHub REST API, each carry the trailer `Co-Authored-By:
  Claude Fable 5 <noreply@anthropic.com>` and an identical `Claude-Session:
  https://claude.ai/code/session_01XZuQTuwKQUpRgcJXTjwG1W` line.
- **Confidence**: settled (directly observed in the commit metadata at
  extraction time, not inferred or asserted by the author's prose)
- **Quote** (commit `cb74ef2`, closing #197 and #177): "Wait for server: to accept connections instead of sleeping one second\n\nReplace the fixed time.sleep(1) after starting a server: process in\nboth multi and video with _wait_for_server(), which polls the target\nURL's host:port until it accepts TCP connections (up to 30 seconds).\nServers that take longer than a second to start no longer cause\nERR_CONNECTION_REFUSED failures, and a server process that exits with\na non-zero code now produces a clear error message.\n\nCloses #197, closes #177\n\nCo-Authored-By: Claude Fable 5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01XZuQTuwKQUpRgcJXTjwG1W"
- **Our assessment**: This is a materially different disclosure pattern than
  the companion `shot-scraper video` essay
  (`blog-simonwillison-shot-scraper-video.md`), where Willison explicitly and
  prominently narrates that "GPT-5.5 xhigh running in Codex Desktop" wrote
  the storyboard YAML. For this release, the human-facing beat post makes no
  mention of agent authorship at all — the fact that Claude Fable 5 wrote
  100% of the shipped diff across three separate, previously-backlogged
  issues in one session is discoverable only by reading commit trailers via
  the GitHub API. This is a useful caution for the guide: this practitioner's
  degree of agent-authorship disclosure varies release-to-release, and a
  reader relying only on the prose of a release beat (rather than the commit
  history) would not know this release was agent-authored at all.

### Claim 8: The shipped `_wait_for_server()` implementation treats a server process exiting with a non-zero code during the wait as an immediate hard failure (raising `click.ClickException`), rather than continuing to poll until the 30-second timeout
- **Evidence**: The merged code diff for commit `cb74ef2`, fetched via the
  GitHub REST API diff endpoint.
- **Confidence**: settled (verified directly against the merged source diff,
  not the prose changelog, which does not describe this failure-mode
  behavior at all)
- **Quote**: "for process, details in server_processes:\n            returncode = process.poll()\n            if returncode:\n                raise click.ClickException(\n                    f\"server: process exited with code {returncode}: {details}\"\n                )"
- **Our assessment**: This is a second undocumented-in-prose improvement
  (like Claim 2/#177): the commit message itself says "a server process that
  exits with a non-zero code now produces a clear error message," but neither
  the blog post nor the GitHub release changelog bullet mentions this
  failure-mode handling at all — only the polling-timeout behavior is
  described publicly. A storyboard whose `server:` command crashes on
  startup (e.g. a syntax error in the app being demoed) now fails fast with
  an attributable error instead of burning the full 30-second timeout and
  then failing with a generic connection error from the subsequent
  navigation attempt.

## Concrete Artifacts

### Full GitHub release body for shot-scraper 1.11 (verbatim, via GitHub REST API)
```
- `server:` processes used by `shot-scraper multi` and `shot-scraper video` now wait up to 30 seconds for the target URL to accept connections, polling for port availability and replacing the previous fixed one-second delay. #197
- The `shot-scraper`, `pdf`, `html`, `accessibility` and `har` commands now have a `--js-file` option for loading JavaScript from a local file, standard input or `gh:username/script`, as an alternative to `--javascript`which accepts the string of JavaScript directly as an argument. #192
- `shot-scraper multi` supports the equivalent `js_file:` YAML key.
- The `shot-scraper javascript` and `shot-scraper html` commands now have a `--timeout` option for consistency with other commands. #118
```
(Source: `api.github.com/repos/simonw/shot-scraper/releases/tags/1.11`,
published 2026-07-12T23:46:52Z, linked from the beat post's "shot-scraper
1.11" text.)

### Complete prose content of the beat post (verbatim, via raw HTML)
```
Release
shot-scraper 1.11 — A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript
Some minor improvements, mainly around command option consistency and making the server: mechanism used by both shot-scraper video and shot-scraper multi work if the server takes longer than a second to start serving traffic.
```
(Source: raw HTML of `simonwillison.net/2026/Jul/12/shot-scraper/`, fetched
directly via `curl` and stripped of markup — the complete text of the post
apart from navigation/sidebar chrome and the changelog list already quoted
under Claim 1/3/5/6.)

### The `_wait_for_server()` implementation (merged diff, `shot_scraper/cli.py`)
```python
SERVER_READY_TIMEOUT = 30.0


def _wait_for_server(server_processes, url, timeout=SERVER_READY_TIMEOUT):
    """
    Wait until the host:port of url accepts TCP connections.

    Raises ClickException if a server process exits with a non-zero code
    while waiting. Returns after timeout seconds even if the port never
    opens, so that navigating to the URL can report its own error.
    """
    bits = urllib.parse.urlparse(url)
    if bits.scheme not in ("http", "https") or not bits.hostname:
        # Nothing to poll - fall back to the old fixed delay
        time.sleep(1)
        return
    port = bits.port or (443 if bits.scheme == "https" else 80)
    deadline = time.monotonic() + timeout
    while True:
        for process, details in server_processes:
            returncode = process.poll()
            if returncode:
                raise click.ClickException(
                    f"server: process exited with code {returncode}: {details}"
                )
        try:
            with socket.create_connection((bits.hostname, port), timeout=1):
                return
        except OSError:
            if time.monotonic() >= deadline:
                return
            time.sleep(0.05)
```
(Source: `api.github.com/repos/simonw/shot-scraper/commits/cb74ef20ec2fe03a74340f543ddfd57918544f9b`,
diff format, file `shot_scraper/cli.py`.)

### The three closing commits and their shared Claude Code session (verbatim trailers)
```
Commit cb74ef2 — "Wait for server: to accept connections instead of sleeping one second"
  Closes #197, closes #177
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01XZuQTuwKQUpRgcJXTjwG1W

Commit 9b181d4 — "Add --javascript-file option and javascript_file: YAML key"
  Closes #192
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01XZuQTuwKQUpRgcJXTjwG1W

Commit 6629e03 — "Add --timeout option to javascript and html commands"
  Closes #118
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01XZuQTuwKQUpRgcJXTjwG1W
```
(Source: `api.github.com/repos/simonw/shot-scraper/commits/{sha}` for each
of the three SHAs, full commit messages.)

## Cross-References

- **Extends**: `blog-simonwillison-shot-scraper-1-10-release.md` Claim 2
  (the full storyboard setup-step/scene-action vocabulary, including
  `server:` as a setup-step type) — Claim 1 above hardens that same
  mechanism's startup reliability. Also extends that note's Guide Impact
  recommendation (Chapter 02/07: "pipelines built against pre-1.10
  `shot-scraper multi`/`video` should not assume a failed setup command
  reliably fails the overall step") with a second, independent version
  floor: pipelines built against pre-1.11 shot-scraper should not assume
  `server:` setup reliably starts before the first navigation — 1.11 is the
  version floor for the 30-second polling behavior.
- **Extends**: `blog-simonwillison-shot-scraper-video.md` Claim 11 (issue
  #142, filed February 2024, described as a feature Willison "almost
  certainly wouldn't have taken on without coding agent support") — Claim 6
  above documents a second, independently-dated instance of the same pattern
  in the same tool: issue #118, filed September 2023 (five months earlier
  than #142), also sat unresolved for years before a coding-agent-assisted
  release cleared it. Together the two notes show at least two multi-year-old
  shot-scraper backlog items cleared within the same ~2-week release window
  (1.10 on 2026-06-30, 1.11 on 2026-07-12).
- **Contradicts**: None found against existing corpus source notes. Note,
  however, an internal discrepancy within this source's own first-party
  material: Claim 5 above documents that the blog post and GitHub release
  body both name the new YAML key `js_file:`, while the commit message that
  implements it names it `javascript_file:`. This is flagged in Claim 5's
  "Our assessment" rather than resolved, since we did not fetch the merged
  `cli.py` parser source to determine which string is actually accepted;
  per MINER.md §4a this is a same-source internal inconsistency rather than
  a claim-vs-claim disagreement between two source notes, so it does not
  rise to a contradiction-issue filing on its own, but the guide should not
  cite the flag name from this note without verifying against current docs.
- **Novel**: Claim 7 (three previously-backlogged issues batch-fixed by
  Claude Fable 5 in one Claude Code session, undisclosed in the human-facing
  release prose) is new to the corpus in this specific combination: prior
  Willison sources either explicitly narrate agent authorship in prose
  (`blog-simonwillison-shot-scraper-video.md`, `blog-simonwillison-sqlite-utils-40rc2.md`)
  or are release beats with no code-provenance claim either way
  (`blog-simonwillison-shot-scraper-1-10-release.md`). This is the first
  corpus example where prose-level silence on agent authorship is
  contradicted by commit-metadata evidence within the same release, from the
  same author who elsewhere discloses agent authorship prominently and by
  name. Also novel: issue #177's independent, external, year-old bug report
  of the exact `ERR_CONNECTION_REFUSED` failure mode (Claim 2), and the
  concrete 4MB-JS/command-line-length motivation for `--js-file` (Claim 4) —
  neither appears in the blog post or in any existing source note.

## Guide Impact

- **Chapter 04 (Development & Context Engineering / verification patterns)**:
  When citing `shot-scraper video`/`shot-scraper multi` (via
  `blog-simonwillison-shot-scraper-video.md` and
  `blog-simonwillison-shot-scraper-1-10-release.md`) as a CI-integrated
  verification pattern, add 1.11 as the version floor for reliable `server:`
  startup: prior to this release, a dev server that took more than one
  second to start would silently produce a broken/incomplete recording or a
  connection-refused failure, undermining "video proves the feature works."
  Cite Claim 1 (the fix) and Claim 8 (the additional non-zero-exit-code fast
  failure, undocumented in the release prose) together.

- **Chapter 07 (Tooling) — command-line argument size limits**: Add Claim 4
  (the concrete 4MB-JS-payload command-line-length failure that motivated
  `--js-file`) as a specific, real-world data point for a general pattern:
  tools that accept arbitrary content via an inline CLI string argument
  (`--javascript`, similar patterns elsewhere) need a file/stdin escape
  hatch once payloads reach single-digit megabytes, independent of any LLM
  context-window concern.

- **Chapter 02/09 (Agent-authored maintenance work / disclosure norms)**:
  Add Claim 7 as a concrete instance worth citing anywhere the guide
  discusses trusting a practitioner's self-reported degree of AI
  involvement: the same author who explicitly narrates agent authorship in
  one post (`blog-simonwillison-shot-scraper-video.md`) ships an entire
  release with zero prose disclosure in another, with the agent-authorship
  fact recoverable only from commit trailers. If the guide makes any claim
  about how transparently practitioners disclose AI-authored code, this
  source is evidence that disclosure is inconsistent even within one
  prolific, generally AI-transparent author's own body of work — readers
  should not assume "no mention of AI in the post" means "no AI was
  involved," and maintainers reviewing this kind of guide advice should
  consider checking commit trailers, not just release prose.

## Extraction Notes

- Fetched the raw HTML of the beat post directly via `curl` (not the
  summarizing WebFetch tool) to get the exact wording of the intro sentence
  and changelog bullets character-for-character; an initial WebFetch pass
  returned a close paraphrase (e.g. "wait up to 30 seconds" rendered
  correctly, but issue numbers and exact punctuation were reconstructed
  rather than verbatim) that was discarded in favor of the raw HTML per the
  precedent set in `blog-simonwillison-shot-scraper-video.md`'s Extraction
  Notes.
- Followed the linked GitHub release (`releases/tags/1.11`, via REST API for
  the verbatim body) and all three issues the release credits (#197, #192,
  #118), plus one issue (#177) discovered only by reading the fixing
  commit's `Closes` trailer rather than the public changelog — this is
  within the "follow up to 5 linked/discovered pages" budget. Also fetched
  the three closing commits' full messages and one full diff (`cb74ef2`,
  for the `_wait_for_server` implementation in Claim 8's Concrete Artifact).
  Did not fetch the diffs for the other two commits (`9b181d4`, `6629e03`)
  beyond their commit messages, since Claims 3–6 are adequately supported by
  the changelog text plus issue metadata and the messages already resolved
  the `js_file:`/`javascript_file:` naming discrepancy in Claim 5 without
  needing the diff.
- The issue body's auto-filed URL fragment (`#atom-everything`) does not
  correspond to a distinct section on the post itself — it is an anchor
  used on the feed-aggregation page the Prospector's scanner reads from, not
  a heading present in the beat post's own HTML. No content was missed by
  treating the URL as pointing to the whole post.
- No contradictions against other source notes were found (see
  Cross-References); the one inconsistency found (Claim 5, `js_file:` vs.
  `javascript_file:`) is internal to this source's own first-party
  materials (blog post + release body vs. commit message), not a
  disagreement with any existing corpus note, so no contradiction issue was
  filed per MINER.md §4a's "when NOT to file" guidance.
