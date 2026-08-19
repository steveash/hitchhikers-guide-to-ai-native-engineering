---
source_url: https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype/
source_type: blog-post
title: "SQLite compressed text-history prototypes"
author: Simon Willison
date_published: 2026-08-09
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: emerging
issue: "#2772"
---

# SQLite compressed text-history prototypes

> Simon Willison prototypes (via an AI coding agent) two SQLite strategies for
> storing the *complete* edit history of a text value as compressed blobs
> instead of one row per revision, showing that Zstandard compression of a
> JSON array of snapshots acts as an implicit delta encoder — 1,000 simulated
> revisions (20.4 MB raw) compress to 80.3 KB — but that the naive
> single-blob version of the idea has quadratic write cost, which a chunked
> variant fixes at a small compression penalty.

## Source Context

- **Type**: blog-post (first-party experiment write-up on Willison's personal
  blog, linking out to a companion GitHub repository
  `simonw/research/tree/main/sqlite-text-history-prototype` that contains the
  actual code, `README.md`, and a `REPORT.md` with benchmark tables). The
  blog post itself is short; the substantive quantitative content — the
  benchmark table comparing monolithic vs. chunked storage, the codec
  comparison, and the sensitivity analysis — lives in `REPORT.md` in the
  linked repo. Both the blog post and the two repo files (`README.md`,
  `REPORT.md`) were fetched and used as primary sources for this note, since
  the blog post explicitly presents the repo as the artifact and summarizes
  only a subset of its findings.
- **Author credibility**: Simon Willison is the creator of `llm`,
  `sqlite-utils`, and Datasette, and writes extensively and credibly about
  SQLite internals and AI-assisted engineering experiments (see the many
  other `blog-simonwillison-*` notes in this corpus). This is not a
  production system he ships — it is explicitly framed as an exploratory
  prototype, one of his regular "I had an idea, I got an AI to build it,
  here's what happened" posts.
- **Scope**: Covers a narrow, specific problem — storing many prior text
  versions of a single mutable value (e.g., an autosaved document, a
  frequently-edited record) inside SQLite without one row per revision. It
  does not cover multi-writer conflict resolution beyond a single
  `BEGIN IMMEDIATE` locking note, does not cover non-text (binary) history,
  and the code is explicitly unaudited, AI-generated exploratory code, not a
  production library.

## Extracted Claims

### Claim 1: Storing a JSON array of full text snapshots and compressing the whole array with Zstandard achieves near-total size reduction because the compressor acts as an implicit delta encoder across near-duplicate snapshots
- **Evidence**: Concrete benchmark: 1,000 simulated revisions to a document produced 20.4 MB of raw revision text, compressed to 80.3 KB. This exact figure appears in the blog post and is elaborated in `REPORT.md`'s core-finding framing.
- **Confidence**: emerging (single-author benchmark on synthetic simulated edits, not a production workload; the mechanism — compressors exploiting redundancy between near-identical adjacent snapshots — is well-understood compression theory, but the specific ratio is workload-dependent)
- **Quote**: "1,000 simulated revisions to a document resulted in 20.4 MB of raw revision text that compressed to 80.3 KB as Zstandard-compressed JSON array."
- **Our assessment**: This is the headline number and it is real (0.39% of raw size), but it is a synthetic benchmark on simulated edits of unspecified realism — the compression ratio depends heavily on how similar consecutive revisions are (see Claim 6, the sensitivity finding, which shows this benefit disappears for high-entropy/unrelated edits). Treat the 80.3 KB figure as an upper bound on achievable compression for typical small-edit-per-revision workloads (autosave, incremental document editing), not a universal constant.

### Claim 2: The naive "one big compressed blob, rewritten in full on every edit" design has quadratic CPU growth and severe write amplification as revision count grows
- **Evidence**: `REPORT.md`'s benchmark table at 1,000 edits: the single Zstandard-blob strategy took 26.80 s total write time with a 136.7 MB WAL file and a 49.904 ms median edit latency for the last 25 edits (i.e., edit latency grows as history grows, since every edit decompresses and recompresses the entire history).
- **Confidence**: emerging (one benchmark run, three trials, on one machine/workload — but the mechanism, decompress-append-recompress on every write, is a straightforward and predictable cause of the measured quadratic behavior)
- **Quote**: (no direct quote; see the benchmark table reproduced in Concrete Artifacts, sourced from `REPORT.md`)
- **Our assessment**: This is the central engineering tradeoff the whole prototype set exists to expose. A single-blob-per-document design is attractive for its simplicity (Claim 1's compression ratio) but is not viable for any workload with more than a "few hundred" edits per document, per the author's own recommendation (Claim 5). This is a useful concrete cautionary data point for anyone tempted to implement "just store the whole history as one compressed JSON blob" without benchmarking write cost at scale.

### Claim 3: Sealing revision history into immutable chunks of ~64-128 revisions (or ~2-3 MB uncompressed) fixes the write-amplification problem at a small compression-ratio cost
- **Evidence**: `REPORT.md` benchmark table at 1,000 edits: chunked storage with 128-revision chunks compressed to 109.9 KB (vs. 80.3 KB monolithic — about 30 KB larger) but cut total write time from 26.80 s to 1.528 s and last-25-edit median latency from 49.904 ms to 2.196 ms. A 64-revision chunk size compressed slightly worse (154.9 KB) but wrote even faster (0.926 s total, 0.957 ms median edit).
- **Confidence**: emerging (same single-benchmark caveat as Claim 2)
- **Quote**: "Chunks of 128 achieved 'only about 30 KB larger' compression than the monolithic approach while reducing total execution time from 26.8 seconds to 1.53 seconds." — *(this exact wording is the summarizing tool's paraphrase of REPORT.md, not confirmed as REPORT.md's literal text; treat the underlying numbers, independently verified in the reproduced benchmark table, as the reliable part of this claim rather than the phrasing)*
- **Our assessment**: The core tradeoff is legible and generalizable beyond this specific prototype: bounding how much compressed data must be rewritten per edit (by sealing older history into fixed-size immutable chunks and only rewriting the "active" chunk) trades a small, bounded compression penalty for an order-of-magnitude write-latency and WAL-size improvement. This is a standard append/seal pattern (similar in spirit to log-structured storage or write-ahead segment rotation) applied specifically to compressed JSON history blobs — useful prior art for anyone building session/document history storage in SQLite.

### Claim 4: Zstandard substantially outperforms zlib for this workload
- **Evidence**: `REPORT.md` codec comparison at 1,000 revisions, monolithic design: Zstandard compressed to 80.3 KB vs. zlib's 176.4 KB — roughly 2.2x larger with zlib.
- **Confidence**: emerging (one workload, one document type — general text with incremental edits; not necessarily representative of all text-history workloads)
- **Quote**: (no direct quote; see benchmark figures in Concrete Artifacts)
- **Our assessment**: Consistent with Zstandard's known advantages over zlib for both ratio and speed on general text, and the repo's own compression-order-of-preference in `README.md` (prefer `compression.zstd`/`zstandard` over `zlib`) reflects this. Not a surprising result, but useful as a concrete, measured data point rather than a general assertion.

### Claim 5: The author's own recommendation is workload-conditioned — monolithic single-blob storage for infrequent edits and modest history length, chunked storage for high-frequency autosave or unbounded revision counts
- **Evidence**: `REPORT.md`'s recommendations section, contrasting "a few hundred revisions" (monolithic) against "high-frequency autosave scenarios, thousands of versions, or when memory and write amplification need a hard bound" (chunked).
- **Confidence**: emerging (author's own judgment call synthesizing the benchmark data, not independently validated against a real production system)
- **Quote**: (no direct quote; the summarizing tool's rendering of this passage was inconsistent across repeated fetches — see Extraction Notes — so this claim is paraphrased from REPORT.md's recommendations section rather than quoted directly)
- **Our assessment**: This is a conditioning variable, not a contradiction between the two designs — the two prototypes are explicitly presented as a spectrum with a workload-dependent crossover point (Claim 3's benchmark table is the evidence for where that crossover sits), not competing claims about which design is "correct."

### Claim 6: The compression benefit collapses when successive revisions are unrelated (high edit entropy) — the scheme only helps when edits are small relative to document size
- **Evidence**: A separate sensitivity analysis (`sensitivity.py` in the repo, results summarized in `REPORT.md`) varying the percentage of a document changed per edit; storage growth scales "roughly with the amount of new information introduced by edits," approaching the full uncompressed size (~16 MB for the tested workload) when consecutive snapshots share little content.
- **Confidence**: emerging (one synthetic sensitivity sweep)
- **Quote**: (no direct quote; see paraphrase above — sourced from a summarized reading of `REPORT.md`'s sensitivity section)
- **Our assessment**: This is the important caveat that qualifies Claim 1's headline number. The 99.6% compression ratio is specific to workloads where each revision is a small incremental edit of the last (autosave, live document editing, iterative refinement) — the exact shape of most AI-agent-driven document/session editing. For workloads where each "revision" is a substantially different document (e.g., independently-generated candidate outputs, not edits of one lineage), this technique offers little to no benefit over storing snapshots uncompressed.

### Claim 7: The prototype's design and code were produced end-to-end by an AI coding agent from a voice-conversation-originated idea, not hand-written by the author
- **Evidence**: The post describes discussing the idea in GPT-Live voice mode in the ChatGPT iPhone app, then handing a written prompt to a coding agent (referred to as "Sol" / GPT-5.6 Sol Pro in the post) which built the prototypes; the linked repo's `README.md` states the report and code were LLM-generated.
- **Confidence**: anecdotal (methodology/process description, not a technical claim about the storage design itself)
- **Quote**: "The new GPT‑Live voice mode in the ChatGPT iPhone app has got really good, so I discussed the prototype with that."
- **Our assessment**: Note that the Prospector's triage comments on this issue describe the builder inconsistently — one comment says "built by Claude Opus (GPT-5.6 Sol Pro in the article's terminology)," which conflates two different things. Our reading of the post and repo indicates the builder was GPT-5.6 Sol Pro (OpenAI), not Claude Opus; there is no Claude/Anthropic involvement mentioned anywhere in the source. This is itself a useful data point for the guide's coverage of AI-assisted research workflows: idea origination in a voice conversation, a written brief handed to an agentic coding model, and an explicitly-labeled "AI-generated research report" as the output — a full voice-to-prototype-to-writeup pipeline authored by one practitioner in what the post describes as a short session.

### Claim 8: The design keeps the current/live value as an ordinary uncompressed SQLite `TEXT` column, storing only prior versions in the compressed history blob, and uses `BEGIN IMMEDIATE` to serialize writers against concurrent-edit revision loss
- **Evidence**: `README.md`'s stated design principles: current version is not duplicated in history; replacement atomically appends the old current value to history before installing the new value; `BEGIN IMMEDIATE` serializes writers.
- **Confidence**: emerging (design principle stated in repo documentation, not independently load-tested for concurrent-writer correctness beyond the author's own testing)
- **Quote**: "BEGIN IMMEDIATE serializes writers to prevent revision loss" — *(from README.md's design-principles list; reproduced here based on the fetched summary of that section, not a page-source diff against the raw file)*
- **Our assessment**: This is a small but important correctness detail often missed in naive "just append to history" implementations: without a write lock coarse enough to serialize the read-modify-write of the history blob, two concurrent editors could each read the same prior history, append their own edit, and one write would silently clobber the other's contribution to history (not just the current value). Worth flagging for the guide's SQLite/local-storage patterns as a specific pitfall to check for in any agent or harness code doing similar blob-append history tracking.

## Concrete Artifacts

Benchmark table at 1,000 simulated edits, reproduced from `REPORT.md` in
`simonw/research/tree/main/sqlite-text-history-prototype` (via a summarized
fetch of that file — see Extraction Notes for the verification caveat):

```
Strategy                        | Compressed History | Total Write Time | Last-25 Median Edit | WAL Size
One JSON + Zstandard blob       | 80.3 KB             | 26.80 s           | 49.904 ms            | 136.7 MB
JSON chunks (64 revisions)      | 154.9 KB            | 0.926 s           | 0.957 ms             | 57.2 MB
JSON chunks (128 revisions)     | 109.9 KB            | 1.528 s           | 2.196 ms             | 58.4 MB
```

Codec comparison at 1,000 revisions, monolithic design (from `REPORT.md`):

```
Zstandard: 80.3 KB
zlib:      176.4 KB
```

Two implementation classes named in the repo (`text_history.py`), per the
blog post's own summary description:

```
WholeBlobHistoryStore  — rewrites one compressed historical blob per edit
ChunkedHistoryStore    — seals compressed chunks to improve scaling, default
                          chunk_size=128 in the shown usage example
```

Basic usage example, reproduced from `README.md`:

```python
from text_history import WholeBlobHistoryStore

with WholeBlobHistoryStore("documents.db") as history:
    document_id = history.create_document(
        "First draft",
        timestamp=1_800_000_000,
        codec="zstd",
        format_name="json",
    )

    history.replace(document_id, "Second draft", timestamp=1_800_000_060)
    history.replace(document_id, "Final draft", timestamp=1_800_000_120)

    for version in history.versions(document_id):
        print(version.revision, version.timestamp, version.text)
```

```python
from text_history import ChunkedHistoryStore

with ChunkedHistoryStore("documents.db", chunk_size=128) as history:
    document_id = history.create_document(
        "First draft",
        timestamp=1_800_000_000,
        codec="zstd",
        format_name="json",
    )
    history.replace(document_id, "Second draft", timestamp=1_800_000_060)
```

Repository resources referenced by the post:
- Code and prototypes: `https://github.com/simonw/research/tree/main/sqlite-text-history-prototype`
- Findings write-up: `REPORT.md` in the same repo
- A gist referenced from the post: `https://gist.github.com/simonw/4e255c53aebdb610553d02cdce17ac30`

## Cross-References

- **Corroborates**: `research-wasnotwas-context-compaction.md` Claim 6
  (OpenHands maintains a persistent, append-only event store where "nothing
  is ever deleted from the persistent store" and compaction is fully
  reversible). Willison's prototype is the same underlying philosophy —
  preserve everything, pay a storage/compute cost to keep it recoverable —
  applied to a different domain (single-document text revisions vs. agent
  session event logs) and with concrete compression-ratio and write-cost
  numbers that the wasnotwas note does not provide. Together they show the
  "preserve full history, don't discard" approach is technically viable in
  at least two different storage substrates (event-store rows in the
  wasnotwas case, compressed JSON blobs here), with this note adding the
  quantitative cost data the other note lacks.
- **Extends**: `blog-simonwillison-llm032.md` Claim 10 (the `llm` 0.32
  release ships a Git-modeled, content-addressed SQLite message store,
  specifically to avoid re-logging duplicate JSON on every turn of a
  growing conversation, motivated by "the pattern where the message
  sequence is appended to on every request"). That claim solved conversation
  history deduplication via content-addressing/dedup (never storing the same
  message content twice); this prototype solves a related-but-distinct
  problem — compressing near-duplicate *document* snapshots that are NOT
  byte-identical (each revision differs slightly from the last) — via
  whole-array compression rather than content-addressed dedup. The two are
  complementary techniques for the same underlying "conversation/document
  history grows unboundedly" problem: content-addressing wins when messages
  repeat verbatim; snapshot-array compression wins when each version is a
  small edit of the last, since a dedup store gains nothing from
  near-but-not-exact duplicates.
- **Contradicts**: None identified. No existing source note makes a
  competing claim about text-history storage design that this source
  disagrees with.
- **Novel**: The specific quantitative benchmark data (compression ratios,
  write-time/WAL-size tradeoffs between monolithic and chunked blob
  storage, zstd vs. zlib comparison, and the edit-entropy sensitivity
  finding) is new to this corpus. No existing source note has measured
  numbers for "store full revision history as compressed blobs in SQLite."

## Guide Impact

- **Chapter 02 (Harness engineering)**: If the guide has or adds guidance on
  session/document persistence patterns for agent harnesses (e.g., storing
  full edit history of an artifact an agent iteratively revises, or
  autosave-style checkpointing), this source provides a concrete, benchmarked
  design pattern: don't do one-row-per-revision, and don't do a single
  ever-growing compressed blob past a few hundred revisions — use sealed,
  size/count-bounded chunks (this source's `ChunkedHistoryStore` at ~128
  revisions or ~2-3 MB uncompressed) to bound write cost while keeping
  compression close to optimal. This is a specific, actionable elaboration
  the guide currently lacks (per the Prospector's triage: "Existing notes
  that overlap: None").
- **Chapter 04 (Context engineering)**: The edit-entropy sensitivity finding
  (Claim 6) is a useful caveat to attach to any recommendation involving
  compressed history storage for agent-generated content: the technique's
  effectiveness is conditional on high similarity between consecutive
  revisions (true for incremental document edits, not necessarily true for
  independently-regenerated candidate outputs), and the guide should not
  present the 80.3 KB/20.4 MB headline ratio as a universal constant without
  that qualifier.

## Extraction Notes

- The blog post itself (the URL filed in the issue) is short and light on
  quantitative detail; the substantive numbers live in `REPORT.md` in the
  linked GitHub repository (`simonw/research/tree/main/sqlite-text-history-prototype`).
  I fetched the blog post, `README.md`, and `REPORT.md` separately and cross-checked
  figures that appeared in more than one fetch (the "1,000 simulated
  revisions... 20.4 MB... 80.3 KB" sentence appeared identically across three
  independent fetches with different prompts, which is why it is treated as
  a reliable direct quote).
- Important caveat on verbatim quotes: my access to these pages is through a
  fetch-and-summarize tool that renders content through a secondary
  model rather than returning raw page source, and in repeated fetches it
  visibly paraphrased the same underlying sentence differently across calls
  (e.g., the "dog walk" origin-idea sentence and the REPORT.md
  recommendations sentence came back with different wording each time I
  asked). Where I could not get an identically-reproduced sentence across
  independent fetches, I have either marked the quote as unconfirmed inline
  or used paraphrase in "Our assessment"/prose instead of a `Quote` field,
  per MINER.md §2a. The benchmark table numbers (Concrete Artifacts) were
  also consistent across repeated fetches, which is why they are presented
  with higher confidence than the prose quotes.
- I did not find a REPORT.md-hosted disclaimer sentence distinguishing
  "settled/audited" from "exploratory" — the repo's own framing ("This is an
  AI-generated research report. All text and code in this report was
  created by an LLM") is itself the closest thing to a confidence
  disclaimer, which is why `confidence_overall` for this note is set to
  `emerging` rather than `settled`: single-author, single-benchmark-run,
  AI-generated exploratory code, not a peer-reviewed or production-validated
  system.
- I did not follow the linked gist (`gist.github.com/simonw/4e255c53aebdb610553d02cdce17ac30`)
  or the OpenAI GPT-Live announcement link beyond confirming they are
  referenced by the post — neither appeared to contain content beyond what
  the primary post and repo already cover for this note's purposes.
