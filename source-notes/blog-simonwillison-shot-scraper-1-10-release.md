---
source_url: https://simonwillison.net/2026/Jun/30/shot-scraper/
source_type: blog-post
title: "Release: shot-scraper 1.10"
author: Simon Willison
date_published: 2026-06-30
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: settled
issue: "#1539"
---

# Release: shot-scraper 1.10

> A one-sentence release "beat" that defers all substantive discussion of
> shot-scraper 1.10 to a companion essay (already mined as
> `blog-simonwillison-shot-scraper-video.md`); the actual technical content
> of this release lives in the linked GitHub release notes, which document
> two changes the companion essay does not cover — a storyboard action
> vocabulary (including arbitrary `sh:`/`python:` execution steps) and a
> non-zero-exit-code fix for failed storyboard setup commands.

## Source Context

- **Type**: blog-post (release announcement — a "beat" in Simon Willison's
  format, per `class="beat"` in the page markup; one sentence of prose plus
  a link to the GitHub release tag)
- **Author credibility**: Simon Willison is the creator and maintainer of
  shot-scraper; this is first-party release documentation, and the linked
  GitHub release (`simonw/shot-scraper` tag `1.10`) is the authoritative
  changelog for the version, also authored by him.
- **Scope**: The beat post itself contains no independent technical content
  beyond a pointer to the companion essay and the release tag. The
  substantive material extracted here comes from the linked GitHub release
  notes (`github.com/simonw/shot-scraper/releases/tag/1.10`), which this
  note treats as a directly-linked sub-page per the Miner's "follow
  substantive linked pages" rule, since the beat post explicitly identifies
  it as where "the big new feature" is documented. Does not cover: adoption,
  usage in the wild, or anything beyond the three changelog bullets and the
  companion essay (already mined separately).

## Extracted Claims

### Claim 1: The entire prose content of this release beat is one sentence pointing readers to a separate companion essay for the substantive discussion of the release's main feature
- **Evidence**: Full HTML body of the beat post, fetched directly via curl.
- **Confidence**: settled (verified against the raw page source; this is the
  complete `beat-note` div content, nothing was truncated)
- **Quote**: "The big new feature is shot-scraper video storyboard.yml, described in detail in Have your agent record video demos of its work with shot-scraper video."
- **Our assessment**: This confirms Willison's practice of separating a
  short, dated "beat" (release/changelog announcement) from a longer,
  undated-in-the-beat companion essay for any release with a feature worth
  explaining. This is a different sub-pattern of "thin release beat" than
  `blog-simonwillison-datasette-llm-limits.md`, where the beat *was* the
  entire substantive content (two sentences plus a YAML example, no
  companion essay existed). Here the beat is a pure pointer; nearly all
  the technical substance readers need lives in the essay already captured
  by `blog-simonwillison-shot-scraper-video.md`.

### Claim 2: The GitHub release notes for shot-scraper 1.10 document the `shot-scraper video` command's full setup-step and scene-action vocabulary: setup via `sh:`, `python:`, and `server:`, and scene actions including `click`, `type`, `fill`, `press`, `scroll`, `pause`, `wait_for`, `wait_for_url`, `open`, `screenshot`, `sh`, `python`, and `javascript`/`js`
- **Evidence**: Verbatim release-notes body, retrieved via the GitHub REST
  API (`api.github.com/repos/simonw/shot-scraper/releases/tags/1.10`),
  first changelog bullet.
- **Confidence**: settled (first-party changelog text from the tool's
  author/maintainer, describing shipped, tagged software)
- **Quote**: "New shot-scraper video command for recording WebM videos from YAML storyboards. Storyboards can define setup steps with sh:, python: and server:, set the viewport, show a cursor and click rings, run startup waits and JavaScript, and then record scenes made from actions including click, type, fill, press, scroll, pause, wait_for, wait_for_url, open, screenshot, sh, python and javascript/js. Use -o/--output to override the WebM filename and --mp4 to also convert the recording to MP4 using ffmpeg. #142, #194"
- **Our assessment**: This is a materially fuller inventory than the single
  demo storyboard reproduced in `blog-simonwillison-shot-scraper-video.md`
  (Concrete Artifacts), which only exercises `pause`, `click`, `wait_for`,
  `fill`, and `wait_for_url` as scene actions and only `server:` as a setup
  step — it never demonstrates `type`, `press`, `scroll`, `screenshot`,
  `sh`, or `python` as scene actions, nor `sh:`/`python:` as setup steps.
  The vocabulary matters for the "video as verification artifact" framing
  in that note: because storyboards can run arbitrary `sh:`/`python:`
  commands both as setup and mid-scene, a storyboard-driven recording is
  not purely a record of organic UI interaction — it can also execute
  arbitrary shell or Python code as part of producing what ends up on
  screen. That note's Claim 7 already flags that agents can "cheat" by
  editing a Markdown demo transcript directly instead of generating it
  through the tool; this changelog shows that even a legitimately-generated
  *video* artifact has its own, narrower fabrication surface if the
  storyboard author (human or agent) inserts `sh:`/`python:` steps that
  stage on-screen state rather than only exercising the real UI.

### Claim 3: `shot-scraper multi` and `shot-scraper video` now both fail with a non-zero exit code if a storyboard's `sh:` or `python:` commands fail
- **Evidence**: Verbatim release-notes body, second changelog bullet.
- **Confidence**: settled (first-party changelog describing shipped
  behavior)
- **Quote**: "shot-scraper multi and the new shot-scraper video both now fail with a non-zero exit code if sh: or python: commands fail."
- **Our assessment**: The "now...fail" phrasing implies this is a behavior
  change from prior versions (at minimum for `shot-scraper multi`, which
  predates 1.10) — we treat that implication as an inference rather than
  a directly confirmed prior-version bug, since the changelog does not
  spell out the pre-1.10 behavior explicitly. Taken at face value, this is
  the detail that makes `shot-scraper video` usable as a CI gate: before
  this fix, a broken setup command inside a storyboard could plausibly
  produce a recording (of a broken or incomplete state) while the overall
  invocation still reported success, silently defeating the "video proves
  the feature works" framing that `blog-simonwillison-shot-scraper-video.md`
  builds its verification-artifact argument on.

### Claim 4: `shot-scraper javascript` gained `--width` and `--height` options for setting the browser viewport before executing JavaScript
- **Evidence**: Verbatim release-notes body, third changelog bullet.
- **Confidence**: settled (first-party changelog describing shipped
  behavior)
- **Quote**: "shot-scraper javascript now has --width and --height options for setting the browser viewport before executing JavaScript. #195"
- **Our assessment**: A minor, independent change bundled into the same
  release rather than a new capability tied to the video feature. It shares
  the release's broader viewport-control theme — the storyboard YAML format
  documented in the companion essay also sets `viewport: {width, height}`
  — but this option applies to the older, non-video `javascript` subcommand
  and is not otherwise connected to the video-recording work.

### Claim 5: The `shot-scraper video` feature (issue #142, opened 2024-02-06) and its immediate follow-up (#194) are the GitHub issues this release's changelog credits for the new command, and #142's creation date independently confirms the companion essay's claim that Willison filed the original request in February 2024
- **Evidence**: The changelog cites "#142, #194" against the `shot-scraper
  video` bullet; the GitHub REST API for issue #142
  (`api.github.com/repos/simonw/shot-scraper/issues/142`) returns
  `created_at: 2024-02-06T05:59:10Z` and the title "shot-scraper video
  command".
- **Confidence**: settled (directly queried via the GitHub API at
  extraction time, not inferred)
- **Quote**: (no direct prose quote from the beat or changelog identifying
  the date; the 2024-02-06 creation date comes from the GitHub API
  response for issue #142, not from prose in either post)
- **Our assessment**: This independently corroborates
  `blog-simonwillison-shot-scraper-video.md` Claim 11 ("filed the original
  issue in February 2024") with the specific issue number and exact date,
  which that note did not itself capture numerically. It also confirms the
  two posts describe the same underlying feature request rather than two
  separately-tracked efforts.

## Concrete Artifacts

### Full changelog body for shot-scraper 1.10 (verbatim, via GitHub REST API)
```
- New `shot-scraper video` command for recording WebM videos from YAML storyboards. Storyboards can define setup steps with `sh:`, `python:` and `server:`, set the viewport, show a cursor and click rings, run startup waits and JavaScript, and then record scenes made from actions including `click`, `type`, `fill`, `press`, `scroll`, `pause`, `wait_for`, `wait_for_url`, `open`, `screenshot`, `sh`, `python` and `javascript`/`js`. Use `-o/--output` to override the WebM filename and `--mp4` to also convert the recording to MP4 using `ffmpeg`. #142, #194
- `shot-scraper multi` and the new `shot-scraper video` both now fail with a non-zero exit code if `sh:` or `python:` commands fail.
- `shot-scraper javascript` now has `--width` and `--height` options for setting the browser viewport before executing JavaScript. #195
```
(Source: `api.github.com/repos/simonw/shot-scraper/releases/tags/1.10`,
published 2026-06-30T15:10:14Z, linked directly from the beat post as
"shot-scraper 1.10".)

### Complete prose content of the beat post (verbatim)
```
Release
shot-scraper 1.10 — A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript
The big new feature is shot-scraper video storyboard.yml, described in detail in Have your agent record video demos of its work with shot-scraper video.
```
(Source: raw HTML of `simonwillison.net/2026/Jun/30/shot-scraper/`, the
`.beat-content` div; this is the complete text of the post apart from
navigation/sidebar chrome.)

## Cross-References

- **Extends**: `blog-simonwillison-shot-scraper-video.md` Claim 11 (Claim 5
  above independently confirms the "filed the original issue in February
  2024" claim with the specific issue number, #142, and its exact creation
  date). Also extends that note's Concrete Artifacts: the storyboard action
  vocabulary in Claim 2 above (13 named actions plus 3 setup-step types) is
  broader than what that note's single reproduced YAML storyboard
  demonstrates (5 distinct actions, 1 setup-step type).

- **Corroborates**: `blog-simonwillison-datasette-llm-limits.md`
  (Extraction Notes: "the blog post is a 'beat' in Simon Willison's
  format"). Both sources are Willison release "beats" retrieved from the
  same trusted feed; together they confirm this thin, dated-announcement
  format recurs across this author's releases, though the two beats differ
  in whether the beat is self-contained (datasette-llm-limits: yes) or a
  pure pointer to a separate essay (shot-scraper 1.10: yes, per Claim 1
  above).

- **Contradicts**: None found. No existing source note makes a claim about
  shot-scraper's exit-code behavior, its storyboard action vocabulary, or
  its release-beat/companion-essay publishing structure that this source
  disagrees with.

- **Novel**: The `sh:`/`python:` setup-step and in-scene action types for
  `shot-scraper video` storyboards, and the non-zero-exit-code fix for
  failed storyboard commands, are not present in
  `blog-simonwillison-shot-scraper-video.md` and are new to the corpus —
  that note's example storyboard never exercises arbitrary shell/Python
  execution as part of a recording. The corpus previously had no source
  documenting that a video-recording tool's own scripting surface could be
  a fabrication vector distinct from the "agent edits the transcript
  directly" cheating pattern already noted there.

## Guide Impact

- **Chapter 04 (Development & Context Engineering / verification patterns)**:
  When citing `shot-scraper video` (via `blog-simonwillison-shot-scraper-video.md`)
  as a verification/demo artifact that is harder to fabricate than an
  agent-editable Markdown transcript, add the caveat surfaced by Claim 2
  here: because storyboards support `sh:`/`python:` setup and scene steps,
  a storyboard-authoring agent can execute arbitrary code to stage on-screen
  state, not only drive the real UI. The guide should present video as
  "harder to hand-edit after the fact" rather than "cannot be fabricated" —
  the fabrication risk moves from the artifact itself to the storyboard
  script that produced it, so review of agent-authored storyboards (not just
  the resulting video) remains part of trusting the artifact.

- **Chapter 02/07 (Tooling / CI use of demo artifacts)**: If the guide
  recommends `shot-scraper video` as a CI-integrated verification step
  (recording a demo as part of a pipeline), cite Claim 3's non-zero
  exit-code behavior (shipped in 1.10) as the version floor — pipelines
  built against pre-1.10 `shot-scraper multi`/`video` should not assume a
  failed setup command reliably fails the overall step.

## Extraction Notes

- The beat post itself (the nominal subject of issue #1539) is one sentence
  of prose. Per the Miner's "follow substantive linked pages" guidance, the
  GitHub release notes it points to as "the big new feature" were fetched
  and treated as the primary extractable content, since the beat text alone
  would not clear the "5-15 claims" quality bar. The release notes were
  retrieved via the GitHub REST API (`releases/tags/1.10`) rather than
  scraping the rendered HTML release page, to get the exact verbatim
  Markdown changelog text rather than a rendered/reflowed copy.
- The companion essay linked from this beat (`.../shot-scraper-video/`) was
  not re-mined here — it is already covered in depth by
  `blog-simonwillison-shot-scraper-video.md` (issue #1540). This note
  focuses on what that note does not cover: the full changelog text, the
  complete storyboard action/setup vocabulary, the exit-code fix, and the
  unrelated `shot-scraper javascript --width/--height` change.
- Verified issue numbers #142, #194, and #195 directly via the GitHub REST
  API (`issues/142`, `issues/194`, `issues/195`) rather than assuming their
  content from the changelog text alone; #142's `created_at` date
  (2024-02-06) is the source for Claim 5's cross-reference to the companion
  essay's "filed... in February 2024" claim.
- No contradictions found against the existing corpus; this note is
  additive to the already-mined companion essay.
