---
source_url: https://simonwillison.net/2026/Sep/2/llm/
source_type: blog-post
title: "llm 0.34"
author: Simon Willison
date_published: 2026-09-02
date_extracted: 2026-09-08
last_checked: 2026-09-08
status: current
confidence_overall: settled
issue: "#3300"
---

# llm 0.34

> A three-sentence Willison "beat" release note for `llm` 0.34 (response-duration tracking in `llm logs`) that, once its linked GitHub release notes, issues, and PRs are followed, reveals a concrete cross-repo performance-regression-and-fix story: `llm-openrouter` 0.7's switch to the Responses API made `llm.get_models()` 43x slower against a 417-model registry (0.908s → 18.9s) by rebuilding a fresh Pydantic options class per model on every call, and a coordinated pair of caching fixes (`llm` PR #1651 + `llm-openrouter` PR/issue #59, both credited to external contributor waveplate) brought the same call down to 0.027s — faster than before the regression.

## Source Context

- **Type**: blog-post (Willison "beat" format — a three-sentence link-blog release note, ~55 words, with no code examples of its own). The beat post itself contains only the headline feature and a one-line pointer to "several contributed bug fixes" and a "significant performance improvement," crediting external contributor waveplate and linking to a same-day companion release, `llm-openrouter` 0.7.1. Per MINER.md §1, this note follows the substantive linked/referenced pages: the GitHub release notes for `llm` 0.34 (full changelog text, not summarized in the blog post), the GitHub issue the headline feature closes (#1653), the GitHub issue the performance fix closes (#1654), the PR implementing the performance fix (#1651, which contains a reproducible timing table), the companion `llm-openrouter` issue/PR describing the other half of the same fix (#59, with its own, more detailed timing table and root-cause writeup), and the same-day `llm-openrouter` 0.7.1 release notes.
- **Author credibility**: Simon Willison is the creator and maintainer of `llm` and (per prior notes in this corpus, e.g. `blog-simonwillison-llm-openrouter-07.md`) also maintains the `llm-openrouter` plugin. This is first-party release documentation from the person who merged the changes; the timing tables and root-cause analysis in the linked PRs, however, are written by the external contributor (waveplate) who diagnosed and fixed the regression, not by Willison himself.
- **Scope**: Covers the `llm` 0.34 release (duration tracking, `llm logs` performance fix, options-class caching, four smaller contributed bug fixes) and the same-day `llm-openrouter` 0.7.1 release insofar as it is the other half of the same coordinated performance fix explicitly cross-linked in the blog post ("see also llm-openrouter 0.7.1"). Does NOT independently benchmark `llm` 0.34 beyond the timing figures the contributor already reported in the linked PRs, and does not cover any `llm` 0.33 core release (no source note for `llm` 0.33 core exists in this corpus — the version history in `source-notes/` jumps from `blog-simonwillison-llm032.md` to plugin-specific 0.33/0.34 releases like `blog-simonwillison-llm-gemini-034.md`).

## Extracted Claims

### Claim 1: `llm logs --usage` Markdown output now shows response duration in both milliseconds and human-readable form, and `llm logs --short` gains a new `duration_ms` field
- **Evidence**: Identical wording in the blog post and the GitHub release notes; the feature closes issue #1653.
- **Confidence**: settled (first-party changelog; feature is shipped, not proposed)
- **Quote**: "llm logs --usage Markdown output now includes the response duration in milliseconds and as a human-readable duration. llm logs --short includes a new duration_ms field."
- **Our assessment**: A small but concrete observability addition — before this release, `duration_ms` existed in the underlying data but (per Claim 2) was only exposed via `--json`, meaning anyone reading the default human-facing log formats had no visibility into per-call latency at all. This directly supports the Prospector's triage question about what observability improvements llm 0.34 adds: the answer is narrow and specific — response duration surfaced in two existing log-viewing modes, not a new metrics system.

### Claim 2: The duration-tracking feature exists because `duration_ms` was previously computed and stored but only reachable through `llm logs --json`, not through the more commonly read Markdown/short log formats
- **Evidence**: The GitHub issue (#1653) that this release closes.
- **Confidence**: settled (first-party issue text, directly resolved by Claim 1's shipped feature)
- **Quote**: "The `duration_ms` is currently only available via `llm logs --json`."
- **Our assessment**: This confirms the fix is a display/surfacing change, not new instrumentation — `llm` was already recording per-call duration internally; the gap was that the two more human-readable log views (`--usage` Markdown, `--short`) didn't expose it. Worth citing if the guide discusses the general pattern of instrumentation existing in a tool's data model long before it's surfaced in the interfaces people actually read day to day.

### Claim 3: A separate fix "significantly improved the performance of `llm logs` for long conversations" by caching repeated message and model lookups, motivated by agent tool sessions producing very slow log reads
- **Evidence**: GitHub release notes bullet, closing issue #1654, whose own issue body names agent tool sessions specifically as the trigger.
- **Confidence**: settled (first-party changelog and issue; no independent benchmark of this specific fix's before/after numbers was published, unlike the options-class caching fix in Claim 4)
- **Quote**: "Significantly improved the performance of llm logs for long conversations by caching repeated message and model lookups." — release notes. Issue #1654: "llm logs can be VERY slow for conversations with a lot of messages in them, e.g. agent tool sessions."
- **Our assessment**: The explicit mention of "agent tool sessions" as the slow case is notable — long-running agentic loops (many tool calls, many logged messages per conversation) are exactly the workload this corpus's other `llm`-adjacent notes document (e.g. the ~99-tool-call session in `blog-simonwillison-llm-gemini-034.md` Claim 7). A CLI-logging tool that was not originally built for that message volume needed a targeted caching fix once agent-style usage became common — a reasonable pattern to flag for any harness engineer building or choosing tooling to inspect long agent transcripts.

### Claim 4: A related, more severe performance fix (PR #1651) caches dynamically-generated Pydantic "options classes" so identical model capability combinations reuse an already-built class instead of rebuilding one per model instance
- **Evidence**: PR #1651's own problem/change description and its reported timing table, run against `llm-openrouter`'s then-current 417-model list.
- **Confidence**: settled (first-party PR description with a reproducible-looking timing table; not independently re-run by this note, but internally consistent with the companion `llm-openrouter` issue #59's table, see Claim 5)
- **Quote**: "`Responses` and `AsyncResponses` currently call `build_options_class()` for every model instance. this creates a new pydantic model class each time, even when another model has exactly the same capabilities. this becomes expensive when a plugin registers a large number of models, since the same options classes are rebuilt whenever `llm.get_models()` or `llm.get_model()` is called."
- **Our assessment**: The general shape of this bug — an O(number of models) amount of redundant class-construction work happening on every registry read — is a pattern worth flagging generically for anyone building a plugin system where one plugin can register hundreds of homogeneous items: without capability-based deduplication, per-item setup cost that looked negligible at small N becomes a real latency problem once a plugin author (here, `llm-openrouter`) registers hundreds of near-identical entries.

### Claim 5: The performance regression this fix addresses was itself caused by `llm-openrouter` 0.7's switch to the Responses API, which made `llm.get_models()` 43x slower (0.908s → 18.9s) against a 417-model list; the coordinated fix (`llm` #1651 + `llm-openrouter` #59) brought the same call down to 0.027s, faster than the pre-regression baseline
- **Evidence**: The companion `llm-openrouter` issue/PR #59 (referenced from the `llm` 0.34 blog post via "see also llm-openrouter 0.7.1"), which states the root cause directly and provides a five-row timing table spanning the pre-regression baseline, the regression, and two stages of fix.
- **Confidence**: settled (first-party root-cause analysis and timing table from the contributor who fixed it; numbers are self-reported, not independently reproduced by this note, but the two related PRs' tables are mutually consistent)
- **Quote**: "`llm-openrouter==0.7` switched its registered models to the responses API. consequently, with the current openrouter model list, this creates synchronous and asynchronous instances for 417 models whenever `llm` rebuilds its model registry"
- **Our assessment**: This is the single most concrete and citable artifact in this source — a full regression-to-fix arc with real numbers, not just a changelog line. It also directly connects to an existing note in this corpus: `blog-simonwillison-llm-openrouter-07.md` Claim 2 documents the `llm-openrouter` 0.7 change that caused this ("Models use OpenRouter's Responses API by default"), confirmed there via the plugin's own README. That note's "Our assessment" for Claim 2 already flagged this as a "default-behavior change with real migration implications" — this source shows one of those implications was an unintended and severe latency regression for any workflow that repeatedly rebuilds the model registry (e.g., calling `llm models` or constructing model instances frequently in a script), not just a response-shape compatibility concern. See Concrete Artifacts for the full timing table.

### Claim 6: Invalid schema DSL passed to `llm prompt --schema` now produces a clean command-line error instead of a Python traceback
- **Evidence**: GitHub release notes bullet, credited to contributor ikatyal2110, closing PR #1647.
- **Confidence**: settled (first-party changelog with named contributor and linked PR)
- **Quote**: "Invalid schema DSL passed to llm prompt --schema now produces a clean command-line error instead of a Python traceback."
- **Our assessment**: A minor UX/error-handling fix rather than a feature; worth noting only as one of several small community-contributed fixes in this release, not independently significant enough to warrant guide coverage on its own.

### Claim 7: `llm --extract` now recognizes fenced code blocks in responses that use CRLF line endings
- **Evidence**: GitHub release notes bullet, credited to contributor mameikagou, closing PR #1644.
- **Confidence**: settled (first-party changelog with named contributor and linked PR)
- **Quote**: "llm --extract now recognizes fenced code blocks in responses that use CRLF line endings."
- **Our assessment**: A narrow parsing bug fix — models or pipelines that emit CRLF-terminated output (common on Windows-originated text) previously broke `--extract`'s code-block detection. Minor but a real cross-platform correctness gap that would silently fail rather than error loudly.

### Claim 8: `monotonic_ulid()` now remains monotonic if the system clock moves backwards or concurrent calls observe timestamps out of order
- **Evidence**: GitHub release notes bullet, credited to contributor Dylan Pulver, closing PR #1641.
- **Confidence**: settled (first-party changelog with named contributor and linked PR)
- **Quote**: "monotonic_ulid() now remains monotonic if the system clock moves backwards or concurrent calls observe timestamps out of order."
- **Our assessment**: A correctness fix for `llm`'s internal ID-generation utility (used for log/message ordering); relevant only insofar as it underlines that the SQLite logging layer's ordering guarantees depend on this function, but not independently significant for guide purposes.

### Claim 9: `typing-extensions` was declared as a direct dependency, with new tests added to protect against accidental missing dependencies
- **Evidence**: GitHub release notes bullet, credited to contributor Vansh Taneja, closing PR #1622.
- **Confidence**: settled (first-party changelog with named contributor and linked PR)
- **Quote**: "Declared the typing-extensions package as a direct dependency, and added tests to protect against accidental missing dependencies."
- **Our assessment**: A packaging-hygiene fix (previously relying on `typing-extensions` being pulled in transitively by another dependency) rather than user-facing behavior change; not independently significant for guide purposes.

### Claim 10: The same-day companion release, `llm-openrouter` 0.7.1, credits the same external contributor (waveplate) for "a performance fix for loading OpenRouter models," explicitly cross-linked from the `llm` 0.34 blog post
- **Evidence**: `llm-openrouter` 0.7.1 GitHub release notes (published 2026-09-02T20:23:26Z, one hour after `llm` 0.34's own release), and the `llm` 0.34 blog post's closing sentence naming both the contributor and the companion release.
- **Confidence**: settled (first-party changelog plus explicit cross-linking from the primary source)
- **Quote**: "Performance fix for loading OpenRouter models. Thanks, waveplate. #59" (llm-openrouter 0.7.1 release notes). From the `llm` 0.34 blog post: "Plus several contributed bug fixes, and a significant performance improvement to llm logs thanks to waveplate on GitHub, see also llm-openrouter 0.7.1."
- **Our assessment**: This confirms the fix in Claim 5 was genuinely coordinated across two separately-versioned repositories by one external contributor in a single day, rather than being two independent, coincidentally-related changes — the `llm-openrouter` release notes reference the same GitHub handle and the same underlying issue thread (#59) as the `llm`-side PR #1651.

## Concrete Artifacts

### GitHub release notes (verbatim, github.com/simonw/llm, tag 0.34, published 2026-09-02)
```
New features:

- `llm logs --usage` Markdown output now includes the response duration
  in milliseconds and as a human-readable duration. `llm logs --short`
  includes a new `duration_ms` field. #1653

Bug fixes:

- Significantly improved the performance of `llm logs` for long
  conversations by caching repeated message and model lookups. #1654
- Dynamically generated OpenAI options classes are now cached, avoiding
  repeated Pydantic class construction by plugins such as
  `llm-openrouter`. Thanks, waveplate. #1651
- Invalid schema DSL passed to `llm prompt --schema` now produces a
  clean command-line error instead of a Python traceback. Thanks,
  ikatyal2110. #1647
- `llm --extract` now recognizes fenced code blocks in responses that
  use CRLF line endings. Thanks, mameikagou. #1644
- `monotonic_ulid()` now remains monotonic if the system clock moves
  backwards or concurrent calls observe timestamps out of order.
  Thanks, Dylan Pulver. #1641
- Declared the `typing-extensions` package as a direct dependency, and
  added tests to protect against accidental missing dependencies.
  Thanks, Vansh Taneja. #1622
```
*Source: GitHub API, github.com/simonw/llm/releases/tags/0.34*

### PR #1651 timing table (verbatim, github.com/simonw/llm/pull/1651)
```
| llm version | llm-openrouter version | repeated `llm.get_models()` |
|---|---|---:|
| llm==0.31.1 | llm-openrouter==0.6.0 | 0.435 seconds |
| llm==0.33 | llm-openrouter==0.6.0 | 0.908 seconds |
| llm==0.33 | llm-openrouter==0.7 | 18.9 seconds |
| llm==0.33 with this change | llm-openrouter==0.7 | 5.531 seconds |
| llm==0.33 with this change | llm-openrouter==0.7 with its corresponding cache | 0.027 seconds |
```
*Source: GitHub API, github.com/simonw/llm/pulls/1651 (tests reported: "1,106 tests passed", plus black/ruff/mypy/documentation checks)*

### llm-openrouter issue/PR #59 root-cause and timing table (verbatim, github.com/simonw/llm-openrouter)
```
## problem

`llm-openrouter==0.7` switched its registered models to the responses
API. consequently, with the current openrouter model list, this
creates synchronous and asynchronous instances for 417 models whenever
`llm` rebuilds its model registry

each instance dynamically creates an openrouter-specific pydantic
options subclass, which means hundreds of mostly identical classes are
rebuilt on every call to `llm.get_models()` or `llm.get_model()`

## change

this caches the generated openrouter options subclasses by their base
options class. combined with simonw/llm#1651, identical capability
combinations reuse the classes that have already been built

## timings

| llm version | llm-openrouter version | repeated `llm.get_models()` |
|---|---|---:|
| llm==0.31.1 | llm-openrouter==0.6.0 | 0.435 seconds |
| llm==0.33 | llm-openrouter==0.6.0 | 0.908 seconds |
| llm==0.33 | llm-openrouter==0.7 | 18.9 seconds |
| llm==0.33 with simonw/llm#1651 | llm-openrouter==0.7 | 5.531 seconds |
| llm==0.33 with simonw/llm#1651 | llm-openrouter==0.7 with this change | 0.027 seconds |

## tests

- 27 tests passed against the core change
```
*Source: GitHub API, github.com/simonw/llm-openrouter/issues/59*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-openrouter-07.md` Claim 2 ("Models use OpenRouter's Responses API by default. You can temporarily use the older Chat Completions API for a prompt with `-o chat_completions 1`.") — this source's Claim 5 confirms the concrete cost of that default switch: a 43x `llm.get_models()` slowdown (0.908s → 18.9s) against `llm-openrouter`'s 417-model list, not previously quantified in that note.

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-llm-openrouter-07.md` Claim 2's "real migration implications" assessment — that note flagged the Responses-API-default switch as having migration implications for response-shape compatibility; this source shows a second, independent implication (severe registry-rebuild latency) that required a follow-up cross-repo fix (`llm-openrouter` 0.7.1, four days after this note's Claim 8's dated gap pattern would predict — actually twelve days after `llm-openrouter` 0.7's August 21, 2026 release per that note's frontmatter).
  - `blog-simonwillison-llm-gemini-034.md` Claim 3's observation that `llm logs` performance work is motivated by "agent tool sessions" producing many logged messages — this source's Claim 3 is the shipped fix for exactly that workload, and Claim 7 of that same note (the ~99-tool-call session) is a concrete example of the kind of conversation `llm logs` needed to handle efficiently.
  - `blog-simonwillison-llm032.md` — continues the same `llm` core-library version history (0.32 → ... → 0.34) documented there, though no source note for the intervening `llm` 0.33 core release exists in this corpus to bridge the two directly.

- **Novel**:
  - First in-corpus documentation of a concrete, quantified performance regression in the `llm` plugin ecosystem (43x slowdown from a Responses-API migration in `llm-openrouter` 0.7) and its full diagnosis-and-fix arc across two separately versioned repositories, coordinated by a single external contributor in one day.
  - First in-corpus mention of `llm logs --usage`/`--short` duration-tracking fields (`duration_ms`).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the `llm`/`llm-openrouter` options-class-caching regression (Claims 4–5) as a concrete case study of a plugin-architecture performance trap: when a plugin registers many (here, 417) near-identical items and each triggers per-item dynamic class construction on every registry read, cost that's invisible at small N becomes a 43x latency regression at real-world scale. Recommend citing the specific before/after numbers (0.908s → 18.9s → 0.027s) as a concrete illustration for any chapter discussing plugin/tool-registry design in a harness.
- **Chapter 01 (Daily Workflows)**: If the guide documents `llm logs` usage, note the new `duration_ms` field in `--short` output and duration display in `--usage` Markdown output (Claim 1) as a way to spot slow individual calls directly from the CLI log views, without needing `--json`.

## Extraction Notes

- **Six sources fetched and read in full beyond the blog post itself**: the GitHub release notes for `llm` 0.34 (via GitHub API), issue #1653 (via GitHub API), issue #1654 (via GitHub API), PR #1651 (via GitHub API, including its timing table and test summary), the companion `llm-openrouter` issue/PR #59 (via GitHub API, including its root-cause writeup and second timing table), and the `llm-openrouter` 0.7.1 release notes (via GitHub API). This is within MINER.md §1's "up to 5 linked pages" guidance, counting the closely related pair (issue #1654's fix and PR #1651/#59's fix) as the substantive extraction targets rather than treating every linked issue number as a separate "page." The four minor bug-fix bullets (#1647, #1644, #1641, #1622) were extracted directly from the already-fetched release notes text rather than fetched as separate pages, since their full detail is contained in the one-line changelog entries themselves.
- **Blog post confirmed thin as flagged by all three Prospector triage comments**: the blog post itself is three sentences; essentially all of the extractable substance in this note comes from following the GitHub release notes and the two linked issues/PRs, particularly the `llm-openrouter` regression story (Claim 5), which the blog post does not mention in any detail beyond "a significant performance improvement to llm logs thanks to waveplate on GitHub, see also llm-openrouter 0.7.1."
- **No contradictions found requiring MINER.md §4a filing.**
- **Cross-reference verification performed**: `blog-simonwillison-llm-openrouter-07.md` Claim 2 confirmed at lines 32–36 of that note (Responses-API-default statement and the `-o chat_completions 1` fallback). `blog-simonwillison-llm-gemini-034.md` Claim 3 and Claim 7 confirmed at lines 38–42 and 62–66 of that note (the ~13-minute, 99-tool-call session and its relevance to `llm logs` load). All claim numbers verified by document-order count in each cited note before writing this note's cross-references.
