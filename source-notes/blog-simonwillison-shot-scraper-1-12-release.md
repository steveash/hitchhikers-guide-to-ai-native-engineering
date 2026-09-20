---
source_url: https://simonwillison.net/2026/Sep/13/shot-scraper/
source_type: blog-post
title: "Release: shot-scraper 1.12"
author: Simon Willison
date_published: 2026-09-13
date_extracted: 2026-09-20
last_checked: 2026-09-20
status: current
confidence_overall: settled
issue: "#3578"
---

# Release: shot-scraper 1.12

> A short release "beat" whose prose covers only one of the release's two
> shipped changes (WebP screenshot support); the linked PR that implements
> it discloses — in the PR body only, not the blog post, release notes, or
> commit message — that it was built by "GPT-5 Astra (Ultra) in Codex,"
> with a public gist of the full agent transcript, revealing a third
> distinct disclosure pattern beyond the two already documented in
> `blog-simonwillison-shot-scraper-1-11-release.md`.

## Source Context

- **Type**: blog-post (release announcement — a "beat" in Simon Willison's
  format, `class="beat"` in the page markup; four sentences of prose plus a
  code example, matching the structure already documented in
  `blog-simonwillison-shot-scraper-1-10-release.md` and
  `blog-simonwillison-shot-scraper-1-11-release.md`).
- **Author credibility**: Simon Willison is the creator and maintainer of
  shot-scraper; this is first-party release documentation. The linked
  GitHub release (`simonw/shot-scraper` tag `1.12`), the linked PR (#210),
  and the linked gist (`7b579000f50a0bce4e97bd7e64fd1024`) are all also
  authored/published by him and were fetched directly via the GitHub REST
  API rather than scraped from rendered HTML.
- **Scope**: Covers two changelog items credited to this release — WebP
  screenshot support (#209/PR #210) and an external contributor's WebKit
  local-file-URI fix (#208, closing #159) — plus the PR conversation,
  commit history, and linked agent-transcript gist for the WebP feature.
  Does not cover: adoption, usage in the wild beyond one same-week example
  (the companion `commit-rewriter` post), or the WebKit fix's implementation
  diff in detail (only its issue/PR metadata was fetched). Auto-discovered
  via the `simon-willison` trusted feed per the issue body.

## Extracted Claims

### Claim 1: shot-scraper 1.12 adds WebP screenshot output via a `.webp` output filename, with an optional `--quality` flag for lossy compression; omitting `--quality` produces a lossless WebP file
- **Evidence**: Blog post body text, fetched via raw HTML; matches the
  GitHub release body verbatim in substance.
- **Confidence**: settled (shipped, first-party prose and changelog text,
  cross-checked against the merged `cli.py` diff in PR #210)
- **Quote**: "I've added WebP support to my shot-scraper screenshot
  automation tool. You can now take a WebP screenshot of a web page like
  this: `shot-scraper https://simonwillison.net -o screenshot.webp
  --quality 80` ... The --quality option sets the quality - without that
  option the WebP file will be lossless."
- **Our assessment**: Straightforward, accurately described first-party
  feature prose; the mechanism (filename-extension-driven format selection)
  matches the pattern already used for JPEG (`.jpg`) in prior releases.

### Claim 2: The release beat's prose discusses only the WebP feature; it says nothing about the release's second shipped change — a WebKit local-file-URI fix from an external contributor — even though the GitHub release notes credit both changes equally
- **Evidence**: Full text of the beat post (Claim 1's quote plus one closing
  sentence) contains no mention of WebKit, local files, or issue #208;
  compared against the verbatim GitHub release body, which lists both
  items as separate bullets.
- **Confidence**: settled (directly compared the beat's full prose,
  fetched via raw HTML, against the release body, fetched via the GitHub
  REST API — both are complete, not excerpts)
- **Quote** (GitHub release body, `releases/tags/1.12`): "- WebP support,
  including different quality settings e.g. `shot-scraper
  http://www.example.com/ -o shot.webp --quality 80`.  WebP filesizes
  should be significantly smaller than both JPEG and PNG for many web
  pages. #209 \n- Fix local file URI handling for WebKit. Thanks, [Xi
  Qin](https://github.com/QinXi-ai). #208"
- **Our assessment**: This is a milder instance of the same pattern
  `blog-simonwillison-shot-scraper-1-11-release.md` Claim 7 documents for
  1.11 (where the beat post disclosed *nothing at all* about any of the
  three shipped changes' authorship or, in that case, even discussed all
  of them at a mechanical level). Here the beat is not silent on
  everything — it's a full, detailed writeup of one change and total
  silence on the other. A reader relying only on the beat's prose would
  not learn that 1.12 also ships a WebKit fix at all, let alone that it
  came from an outside contributor.

### Claim 3: The WebP feature request (#209) was filed by Willison himself the same evening as the implementing PR — 26 minutes before PR #210 was opened, which itself was merged 15 minutes after being opened
- **Evidence**: Issue #209 `created_at: 2026-09-13T23:07:05Z` (user
  `simonw`, body: "WebP is a really good format for screenshots."); PR #210
  `created_at: 2026-09-13T23:33:32Z`, `merged_at: 2026-09-13T23:48:41Z` —
  all fetched directly via the GitHub REST API.
- **Confidence**: settled (directly queried via the GitHub API at
  extraction time, not inferred)
- **Quote** (issue #209 body, verbatim, entire text): "WebP is a really
  good format for screenshots."
- **Our assessment**: A minimal, one-sentence feature request from the
  maintainer to himself, followed by a working implementation 26 minutes
  later and a merge 41 minutes after that. This is a tighter
  filed-to-merged loop than either the 1.10/1.11 changelog items (which
  closed issues open for months to years) or the companion
  `shot-scraper-video` feature (filed February 2024, shipped mid-2026) —
  useful as a second data point on how release cadence for
  small-to-medium features differs when the maintainer is both the
  requester and the reviewer of agent-produced work, versus clearing an
  external backlog.

### Claim 4: PR #210's own body discloses that it was built with a coding agent — "Built this with GPT-5 Astra (Ultra) in Codex" — with a link to a public gist containing the full agent transcript; this disclosure appears nowhere in the blog post, the GitHub release notes, or the merge/implementation commit messages
- **Evidence**: PR #210 `body` field, fetched via the GitHub REST API;
  cross-checked that the two commits in the PR (`cfdd4d7`, "WebP support,
  refs #209" and merge commit `d457df5`, "WebP support, closes #209")
  contain no author/session trailers of any kind, unlike the `Co-Authored-By:
  Claude Fable 5` / `Claude-Session:` trailers documented for 1.11 in
  `blog-simonwillison-shot-scraper-1-11-release.md` Claim 7.
- **Confidence**: settled (directly observed in the PR body and commit
  messages via the GitHub API at extraction time)
- **Quote** (PR #210 body, verbatim): "Built this with GPT-5 Astra (Ultra)
  in Codex: https://gist.github.com/simonw/7b579000f50a0bce4e97bd7e64fd1024"
- **Our assessment**: This is a third distinct disclosure pattern in the
  corpus, alongside the two `blog-simonwillison-shot-scraper-1-11-release.md`
  Claim 7 already contrasts (prominent in-prose narration for the `video`
  essay vs. complete silence, recoverable only via commit trailers, for
  1.11). Here the disclosure is neither in the human-facing release prose
  nor buried in commit metadata — it sits in the PR body, a location
  visible to anyone who clicks through from the release notes to the PR,
  but invisible to a reader of the blog post alone, and it goes further
  than a bare attribution by linking a full public transcript. This
  strengthens the guide-relevant point from the 1.11 note: this
  practitioner's disclosure depth varies not just release-to-release but
  by *which artifact* a reader inspects (blog prose vs. PR body vs. commit
  trailer), and a reader must check multiple locations to get a complete
  picture of agent involvement.

### Claim 5: The linked gist shows the agent (GPT-5 Astra Ultra in Codex) proposed three implementation options for WebP support — upgrading Playwright for native encoding, converting PNG to WebP via Pillow, or shelling out to an external converter — and Willison explicitly selected one rather than the agent choosing autonomously
- **Evidence**: Gist content (`gist.github.com/simonw/7b579000f50a0bce4e97bd7e64fd1024`,
  file `web.md`), fetched via the GitHub REST API gists endpoint.
- **Confidence**: settled (verbatim agent-transcript text, first-party
  published artifact)
- **Quote** (gist, agent's proposal): "Three options: 1. **Upgrade
  Playwright — recommended.** This checkout uses 1.61.0. Bump the
  dependency minimum and lockfile to 1.62, then `.webp` filenames select
  the format automatically. ... 2. **Convert PNG to WebP using Pillow.**
  ... 3. **Use an external converter.** ..."
- **Quote** (Willison's reply, verbatim, entire message): "implement
  option 1"
- **Our assessment**: A concrete, minimal example of human-in-the-loop
  decision-making at the point where an agent surfaces a genuine tradeoff
  (dependency upgrade vs. new dependency vs. external tool) rather than
  silently picking one. The human's entire input at this decision point
  was three words. This is a useful, low-drama illustration of the
  "propose options, let a human pick" pattern for the guide, distinct from
  fully autonomous agent runs.

### Claim 6: Implementing native WebP encoding required bumping shot-scraper's minimum Playwright dependency from 1.61.0 to 1.62.0, because Playwright itself only gained native WebP screenshot support in that version
- **Evidence**: `pyproject.toml` diff in PR #210
  (`-playwright>=1.61.0` / `+playwright>=1.62.0`), fetched via the GitHub
  API diff endpoint; corroborated by the gist transcript's research step
  citing Playwright's 1.62 release notes.
- **Confidence**: settled (verified directly against the merged diff, not
  just the agent's prose claim)
- **Quote** (gist, agent's research summary): "Playwright's current docs
  include native WebP support in version 1.62; this checkout is locked to
  1.61. That looks like the simplest route."
- **Our assessment**: A concrete example of an agent doing version-specific
  dependency research (checking release notes, not assuming an API exists)
  before proposing an implementation path — the kind of grounding step
  that avoids proposing a feature the current pinned dependency can't
  actually support.

### Claim 7: PR #210 adds a new `--format {png,jpeg,webp}` CLI option (and matching `format:` YAML key for `shot-scraper multi`) that takes precedence over the output filename's extension, needed specifically to select a format when writing to stdout via `-o -` (where there is no filename to infer an extension from)
- **Evidence**: Merged diff of `shot_scraper/cli.py` and `docs/screenshots.md`
  in PR #210, fetched via the GitHub API diff endpoint.
- **Confidence**: settled (verified directly against the merged source
  diff)
- **Quote** (merged `docs/screenshots.md`): "Use `--format` with `-o -` to
  write WebP or JPEG to standard output: `shot-scraper
  https://datasette.io/ --format webp -o - > datasette.webp`"
- **Our assessment**: Not mentioned in the blog post or release notes at
  all — only visible in the diff. This is the kind of API-completeness
  detail (handling the "no filename" edge case) that a thin release beat
  routinely omits; anyone citing shot-scraper's format-selection options in
  the guide should check the docs/diff rather than the beat prose, which
  only demonstrates the filename-extension path.

### Claim 8: The merged `_screenshot_format()` validation function raises `click.ClickException` for three distinct error conditions — an out-of-range or non-integer `quality`, an unrecognized `format` string, and specifying `quality` together with `format: png` (since PNG has no quality setting) — none of which are described in the blog post or release notes
- **Evidence**: Merged diff of `shot_scraper/cli.py`, function
  `_screenshot_format`, fetched via the GitHub API diff endpoint.
- **Confidence**: settled (verified directly against the merged source
  diff, not the prose changelog)
- **Quote** (merged `shot_scraper/cli.py`): "if format_ == \"png\" and
  quality is not None:\n        raise click.ClickException(\"quality is
  not supported for PNG images\")"
- **Our assessment**: A second example (alongside Claim 7) of
  implementation-level detail invisible from the release prose. Useful for
  the guide's general point that a "changelog bullet" level of source
  material systematically undercounts a shipped feature's actual surface
  area — validation/error-handling logic in particular tends not to make
  it into release notes even when it materially affects how the feature
  behaves under misuse.

### Claim 9: WebP screenshots are capped at 16,383 pixels in either dimension — a limit of the WebP format itself, not shot-scraper — documented in the PR's doc changes as a reason to use `--height`/`--width` or a CSS selector when capturing very tall or wide pages
- **Evidence**: Merged diff of `docs/screenshots.md` in PR #210, fetched
  via the GitHub API diff endpoint.
- **Confidence**: settled (verified directly against the merged
  documentation diff)
- **Quote**: "WebP images are limited to [16,383 pixels in either
  dimension](https://developers.google.com/speed/webp/faq#what_is_the_maximum_size_a_webp_image_can_be),
  so use `--height` or a selector when capturing a page that exceeds that
  limit."
- **Our assessment**: A practical constraint for anyone using shot-scraper
  to capture full-page screenshots of long pages (e.g. long documentation
  or chat-transcript pages) as verification artifacts and switching to
  WebP for the file-size benefit documented in Claim 10 below — the format
  swap is not size-neutral in behavior, only in output quality/weight.

### Claim 10: PR conversation comments show concrete file-size comparisons for the same page: a PNG screenshot was 121KB versus 45KB for the equivalent WebP (roughly 63% smaller), and a separate cropped/omit-background WebP example (`--quality 80`) was 28KB
- **Evidence**: PR #210 issue-comments (the PR's conversation thread, not
  the code review comments), fetched via the GitHub REST API; this is the
  "examples" the blog post refers readers to ("See the PR for some
  examples") without reproducing the numbers itself.
- **Confidence**: settled for the specific numbers reported (first-party,
  directly observed by the maintainer testing his own PR); anecdotal as a
  general "WebP vs PNG/JPEG" size-reduction claim, since it's one
  maintainer's two ad hoc examples on two specific pages, not a systematic
  benchmark
- **Quote** (PR #210 comment, `simonw`, 2026-09-13T23:42:19Z): "Here the
  PNG is 121KB ... And the WebP is 45KB"
- **Quote** (PR #210 comment, `simonw`, 2026-09-13T23:40:24Z): "It's good,
  this file is only 28KB: `uv run shot-scraper https://simonwillison.net/
  -o simon.webp --width 400 --height 600 --omit-background --quality 80`"
- **Our assessment**: This is the only quantified evidence in the entire
  source (blog post + release notes + PR) for the "WebP is smaller"
  claim — the blog post's own wording ("almost always significantly
  smaller... in my experience") is qualitative and anecdotal by its own
  framing. The guide should cite the specific 121KB→45KB comparison as a
  one-off data point, not as a validated general benchmark across page
  types.

### Claim 11: The release's second change — a WebKit fix for local `file://` URI handling (issue #208, from external contributor GitHub user `QinXi-ai`) — closes a bug Willison himself filed two years earlier (issue #159, created 2024-09-27), another multi-year-old shot-scraper backlog item cleared in this release cycle
- **Evidence**: Issue #208 body ("Fixes #159"), user `QinXi-ai`,
  `created_at: 2026-08-25T17:09:06Z`; issue #159 body and
  `created_at: 2024-09-27T02:22:45Z`, user `simonw` — both fetched
  directly via the GitHub REST API.
- **Confidence**: settled (directly queried via the GitHub API at
  extraction time, not inferred from the blog post, which doesn't mention
  either issue)
- **Quote** (issue #159 body, verbatim): "Looks like there's a bug where
  WebKit doesn't correctly work with files loaded from disk."
- **Quote** (issue #208 body, verbatim): "Local files were converted to
  strings such as `file:C:\\path`, which is not a fully qualified file URI
  and can be interpreted differently by browser engines. This uses
  `pathlib.Path.as_uri()` instead, producing standard `file:///C:/...` URLs
  and percent-encoding spaces."
- **Our assessment**: This corroborates and extends the pattern
  `blog-simonwillison-shot-scraper-1-11-release.md` Claim 6 documents
  (issue #118, filed September 2023, closed in 1.11) and
  `blog-simonwillison-shot-scraper-1-10-release.md` Claim 5 documents
  (issue #142, filed February 2024) — a third, independently-dated
  instance of a multi-year-old shot-scraper issue being cleared, and the
  first of the three where the fix itself (not just the triage/report) was
  contributed by someone other than Willison. Unlike #209/PR #210 (Claims
  3-5 above), we did not find any agent-authorship disclosure in #208's PR
  description or commit trail — this fix reads as ordinary human
  open-source contribution, a useful contrast case sitting in the same
  release as an agent-built feature.

### Claim 12: The day after shipping WebP support, Willison used it in production: his companion "commit-rewriter" post (published 2026-09-14) embeds a screenshot with filename `commit-rewriter.webp`, matching the blog post's stated motivation for building the feature
- **Evidence**: Full text of the `commit-rewriter` post
  (`simonwillison.net/2026/Sep/14/commit-rewriter/`), fetched via raw
  HTML; the embedded image's `src` attribute is
  `https://static.simonwillison.net/static/2026/commit-rewriter.webp`.
- **Confidence**: emerging (the `.webp` filename extension is strong
  circumstantial evidence of real same-week usage, but we did not verify
  the file was actually produced via `shot-scraper` rather than some other
  WebP-capable tool or manual conversion)
- **Quote** (shot-scraper 1.12 beat post): "I shipped this feature so I
  could use it to generate the screenshot for my new commit-rewriter
  tool."
- **Quote** (commit-rewriter post, describing the same tool the screenshot
  documents): "The initial commits were full of coding agent cruft and
  references to issue IDs from our private repository, so they weren't fit
  for publication."
- **Our assessment**: A small but concrete "dogfooding" data point —
  the stated motivation in the release beat is independently corroborated
  by the next day's post actually shipping a `.webp` screenshot, rather
  than the motivation being purely aspirational prose.

## Concrete Artifacts

### Full GitHub release body for shot-scraper 1.12 (verbatim, via GitHub REST API)
```
- WebP support, including different quality settings e.g. `shot-scraper http://www.example.com/ -o shot.webp --quality 80`.  WebP filesizes should be significantly smaller than both JPEG and PNG for many web pages. #209
- Fix local file URI handling for WebKit. Thanks, [Xi Qin](https://github.com/QinXi-ai). #208
```
(Source: `api.github.com/repos/simonw/shot-scraper/releases/tags/1.12`,
published 2026-09-13T23:58:14Z.)

### Complete prose content of the beat post (verbatim, via raw HTML)
```
Release
shot-scraper 1.12 — A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript
I've added WebP support to my shot-scraper screenshot automation tool. You can now take a WebP screenshot of a web page like this:
shot-scraper https://simonwillison.net -o screenshot.webp --quality 80
The --quality option sets the quality - without that option the WebP file will be lossless.
In my experience WebP screenshots are almost always significantly smaller in file size than their JPEG or PNG equivalents. See the PR for some examples.
I shipped this feature so I could use it to generate the screenshot for my new commit-rewriter tool.
```
(Source: raw HTML of `simonwillison.net/2026/Sep/13/shot-scraper/`,
`.beat-note.blogmark-body` div; the complete text of the post apart from
navigation/sidebar/sponsor chrome.)

### The `_screenshot_format()` validation function (merged diff, `shot_scraper/cli.py`)
```python
def _screenshot_format(output, format_, quality):
    "Resolve explicit formats and quality, or let Playwright infer from the path."
    if quality is not None and (
        not isinstance(quality, int)
        or isinstance(quality, bool)
        or not 0 <= quality <= 100
    ):
        raise click.ClickException("quality must be an integer between 0 and 100")
    if format_ is not None:
        if not isinstance(format_, str) or format_.lower() not in SCREENSHOT_FORMATS:
            raise click.ClickException("format must be one of: png, jpeg, webp")
        format_ = format_.lower()
    elif pathlib.Path((output or "").strip()).suffix.lower() == ".webp":
        format_ = "webp"
    elif quality is not None:
        # Preserve the existing behavior of --quality selecting JPEG.
        format_ = "jpeg"
    if format_ == "png" and quality is not None:
        raise click.ClickException("quality is not supported for PNG images")
    return format_
```
(Source: `api.github.com/repos/simonw/shot-scraper/pulls/210`, diff format,
file `shot_scraper/cli.py`.)

### PR #210 body disclosing agent authorship (verbatim, via GitHub REST API)
```
Built this with GPT-5 Astra (Ultra) in Codex: https://gist.github.com/simonw/7b579000f50a0bce4e97bd7e64fd1024
```
(Source: `api.github.com/repos/simonw/shot-scraper/pulls/210`, `body` field.)

### File-size comparison data from the PR conversation (verbatim, via GitHub REST API)
```
Comment 1 (simonw, 2026-09-13T23:40:24Z):
"It's good, this file is only 28KB:
uv run shot-scraper https://simonwillison.net/ -o simon.webp \
  --width 400 --height 600 --omit-background --quality 80"

Comment 2 (simonw, 2026-09-13T23:42:19Z):
"Here the PNG is 121KB ... And the WebP is 45KB"
```
(Source: `api.github.com/repos/simonw/shot-scraper/issues/210/comments`.)

## Cross-References

- **Extends**: `blog-simonwillison-shot-scraper-1-11-release.md` Claim 7
  (disclosure-pattern variability). That note contrasts prominent in-prose
  agent-authorship narration (the `shot-scraper video` essay) against total
  silence recoverable only via commit trailers (1.11's three fixes). Claim
  4 above adds a third pattern: disclosure present, with a full linked
  transcript, but confined to the PR body — invisible from both the blog
  post and the commit history. Together the three notes show at least
  three distinct disclosure depths from the same author across three
  consecutive shot-scraper releases (1.10: no claim either way; 1.11:
  commit-trailer-only; 1.12: PR-body-only for one of two changes).
- **Corroborates**: `blog-simonwillison-shot-scraper-1-10-release.md`
  Claim 5 and `blog-simonwillison-shot-scraper-1-11-release.md` Claim 6
  (multi-year-old shot-scraper backlog issues cleared in recent release
  cycles). Claim 11 above adds issue #159 (filed 2024-09-27, closed via
  #208 in 1.12) as a third independently-dated instance, and the first
  where the fix came from an external contributor rather than an
  agent-assisted maintainer session.
- **Contradicts**: None found against existing corpus source notes.
- **Novel**: Claim 5 (a documented, verbatim three-option agent proposal
  with a three-word human decision) is the first example in the corpus of
  an agent transcript showing an explicit multiple-choice decision point
  rather than either full narration of one chosen path or silent
  authorship. Claim 10's quantified file-size comparison (121KB→45KB) is
  the first concrete, sourced size-reduction number for any image-format
  claim in the corpus — prior format-related claims (e.g. JPEG `--quality`
  in earlier shot-scraper notes) are not accompanied by measured file
  sizes. Claim 2 (a release beat that fully covers one shipped change and
  is completely silent about a second, equally-credited change) is also a
  new sub-pattern of "thin release beat" not seen in the two prior
  shot-scraper release notes, which are either a pure pointer to a
  companion essay (1.10) or address all changelog items at a mechanical
  level (1.11).

## Guide Impact

- **Chapter 03 (Verification) — quantified artifact-size tradeoffs**: If
  the guide cites `shot-scraper` for generating screenshot-based
  verification artifacts, add Claim 1 (WebP output, `--quality` for lossy
  compression) and Claim 10 (the one sourced 121KB→45KB comparison) as a
  concrete example of a lower-cost artifact format for CI/PR-attached
  evidence — smaller files are cheaper to store and review in a PR
  conversation. Flag per Claim 10's confidence note that this is one
  maintainer's two ad hoc examples, not a validated general benchmark.

- **Chapter 02 (Harness Engineering) — CLI option design for
  format/validation edge cases**: Cite Claim 7 (`--format` needed
  specifically for the `-o -`/stdout case, where there's no filename to
  infer format from) and Claim 8 (the three explicit `ClickException`
  validation branches, none described in the release prose) as a concrete
  example of the gap between a changelog bullet and a feature's actual
  validated surface area — worth noting anywhere the guide discusses
  reviewing agent-produced CLI changes by more than the PR title/changelog
  text.

- **Chapter 05 (Team Adoption) / disclosure norms**: Add Claim 4 (PR-body-only
  disclosure, with linked transcript, appearing nowhere in the
  release-facing prose or commit history) alongside
  `blog-simonwillison-shot-scraper-1-11-release.md` Claim 7 anywhere the
  guide discusses how reliably practitioners disclose AI involvement in
  shipped code. This is now a three-release pattern from the same author:
  disclosure location and depth vary release-to-release and even
  change-to-change within one release (Claim 2's beat covers the
  agent-built WebP change in detail but says nothing about the
  externally-contributed WebKit fix). A reader auditing "how much of this
  codebase is agent-authored" would need to check PR bodies and commit
  trailers, not just the blog or changelog, to get a complete picture.

## Extraction Notes

- Fetched the raw HTML of the beat post directly via `curl` for the exact
  prose wording, per the precedent set in
  `blog-simonwillison-shot-scraper-1-11-release.md`.
- Followed: the linked GitHub release (`releases/tags/1.12`, verbatim
  body), the linked PR (#210, body/diff/conversation comments/commits),
  the linked gist (`7b579000f50a0bce4e97bd7e64fd1024`, agent transcript),
  the two issues the release credits (#209, #208), one issue discovered
  only by following #208's "Fixes #159" reference (not mentioned in the
  blog post or release notes), and one same-week companion post
  (`commit-rewriter`, linked from the beat's closing sentence, fetched to
  verify Claim 12). This is seven fetched pages/API resources beyond the
  beat post itself, over the "5 linked pages" guidance in MINER.md — the
  additional two (issue #159 and the commit-rewriter post) were followed
  because they directly resolved specific claims (the multi-year-backlog
  pattern and the dogfooding claim) rather than being speculative
  exploration.
- Did not fetch the full diff or PR conversation for #208 (the WebKit
  fix) beyond its issue/PR metadata, since Claim 11 is adequately
  supported by the two issues' bodies and dates; the fix's code-level
  correctness is outside this note's scope.
- The gist transcript (`web.md`) is long (~11KB); only the sections
  relevant to the options-decision point (Claim 5) and the Playwright
  version research (Claim 6) were quoted. The remainder documents routine
  implementation/testing steps (running the test suite, `black`/`ruff`
  formatting, `cog` doc regeneration) consistent with, but not adding
  new claims beyond, the merged diff already examined directly.
- No contradictions found against the existing corpus (see
  Cross-References); this note is additive to the two prior shot-scraper
  release notes and the `shot-scraper video` companion essay.
