---
source_url: https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust/
source_type: blog-post
title: "parse_number() as a SQLite extension: C vs Rust"
author: Simon Willison
date_published: 2026-11-08
date_extracted: 2026-11-09
last_checked: 2026-11-09
status: current
confidence_overall: anecdotal
issue: "#4603"
---

# parse_number() as a SQLite extension: C vs Rust

> A short worked example of "give the model a measured baseline and ask it to beat or match it", with the result checked by a benchmark table and a cross-implementation fuzz comparison, then packaged as a research report by a follow-up prompt.

## Source Context

- **Type**: blog-post (short "Research" entry that links to a report in simonw/research)
- **Author credibility**: Simon Willison, creator of Datasette and sqlite-utils, and a prolific public documenter of LLM workflows. Here he reports his own single-session experiment.
- **Scope**: Covers three prompts in a Claude chat session (Opus 5.5), one benchmark table, and a one-line summary of 8 million fuzz checks. It does NOT show the fuzz harness, the benchmark code, or the generated C. Those are in the linked research report, which I did not fetch. The post is short, so the fuzz and correctness claims rest on the author's summary.

## Extracted Claims

### Claim 1: A single exploratory prompt produced a working comparison of C vs Rust implementations, including size figures
- **Evidence**: The author reports artifact sizes from the model's output: Rust 321 KB (Rusqlite), 298 KB (sqlite-loadable-rs), C 14 KB.
- **Confidence**: anecdotal
- **Quote**: "the Rust extension was 321 KB (using Rusqlite) and 298 KB (using sqlite-loadable-rs), while the C extension was 14 KB."
- **Our assessment**: Plausible and cheap to check. The prompt asked for comparisons of performance, code complexity and file size at once, which is a good example of an open-ended "explore the trade-off" prompt. The sizes are unverified by us.

### Claim 2: The model's first C version lost to Rust, and the author's follow-up named the baseline explicitly as the target
- **Evidence**: The author's second prompt, quoted below, targets the Rust numbers. He attributes the gap to strtod, saying the Rust equivalent is "twice as fast".
- **Confidence**: anecdotal
- **Quote**: "Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation"
- **Our assessment**: The pattern is to turn a surprising measurement into a concrete "match or beat X" goal. The model chose Clinger's fast path itself, according to the post. The "twice as fast" diagnosis is the model's or the author's claim, not demonstrated in the post.

### Claim 3: The optimized C version beat both Rust versions, with the largest gain on decimal data
- **Evidence**: Table of net ns/row over 2 million rows, reproduced under Concrete Artifacts. Decimals only: first C 106 ns, new C 18 ns, rusqlite 55 ns, sqlite-loadable 47 ns.
- **Confidence**: anecdotal
- **Quote**: "The optimized C implementation was fastest at 16–19 ns per row, about twice as fast as the Rust versions and far faster than SQL `replace()`."
- **Our assessment**: The result is a single-machine microbenchmark with no variance reported in the post. Do not generalize "C beats Rust". The transferable part is that the benchmark was split by data shape (mixed / integer-only / decimal-only), which exposed where the first C version was weak (decimals, 106 ns).

### Claim 4: Equivalence of all four implementations was checked by a large fuzz comparison
- **Evidence**: A one-line statement in the summary; the harness itself is not shown in the post. Tests are also said to cover type preservation, parsing rules and floating-point accuracy.
- **Confidence**: anecdotal
- **Quote**: "all versions matched across 8 million fuzz checks."
- **Our assessment**: This is the verification pattern most relevant to the guide: when the model replaces a standard-library routine (strtod) with a hand-rolled one, differential testing against the other implementations is the right oracle. It is only a summary claim here, so cite the pattern, not the harness detail, unless the linked report is mined.

### Claim 5: The finished investigation was turned into a repository-style report with one more prompt
- **Evidence**: The prompt is quoted in the post and the resulting report is linked.
- **Confidence**: anecdotal
- **Quote**: "Clone simonw/research from GitHub and turn your above investigation into a research report as seen in that repository - you can give me a zip file to download that contains your new folder"
- **Our assessment**: Using an existing repo as the format exemplar is a lightweight way to get consistent write-ups. Note the work happened in chat, not an agent harness, and the author asked for a zip download.

### Claim 6: The experiment cost little attention
- **Evidence**: The author's framing of how it started.
- **Confidence**: anecdotal
- **Quote**: "I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension"
- **Our assessment**: Anecdote about low-friction, mobile-friendly experimentation. Supports Ch01 themes on idle-time work but is not evidence of quality.

## Concrete Artifacts

Prompt 1 (Simon Willison, Claude chat, Opus 5.5):

```
I'm thinking about a SQLite custom function 'parse_number(value)' that strips ',', '$', '£' and '%', handles a leading '-', and returns 'NULL' for anything it can’t parse
Explore the difference between building this as a SQLite extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting.so(or whatever) file
```

Prompt 2:

```
Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation
```

Prompt 3:

```
Clone simonw/research from GitHub and turn your above investigation into a research report as seen in that repository - you can give me a zip file to download that contains your new folder
```

Benchmark table (net cost per row over 2 million rows, lower is better):

| Data | first C | new C | rusqlite | sqlite-loadable |
|---|---|---|---|---|
| Mixed data | 67 ns | 19 ns | 46 ns | 41 ns |
| Integers only | 25 ns | 16 ns | 36 ns | 32 ns |
| Decimals only | 106 ns | 18 ns | 55 ns | 47 ns |

## Cross-References

- **Corroborates**: `blog-simonwillison-sqlite-utils-40rc2.md` shows the same author building trust in model output through independent checks (see its Claims 7 and 8 on cross-model review); this post uses an executable oracle (fuzz comparison) instead of a second model.
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-claude-code-bun-in-rust.md` covers a language-level Rust rewrite with performance framing (see its Claim 6, the "10% faster" startup claim); this post is a small-scale, model-driven performance comparison.
- **Novel**: No existing note covers prompting a model to beat a measured baseline with a per-data-shape benchmark, or differential fuzzing of multiple implementations as the correctness oracle for model-written code.

## Guide Impact

- **Chapter 03 (verification)**: Candidate short example: for model-written performance code that replaces a trusted routine, require (a) a benchmark split by input shape and (b) a differential fuzz against existing implementations. Cite as anecdotal and single-author; harness details would need the linked report.
- **Chapter 01 (daily workflows)**: Candidate example of converting a measured shortfall into an explicit "catch up to or beat the baseline" follow-up prompt, then asking for a write-up in the format of an existing repo.
- No change recommended to existing claims; the C-vs-Rust numbers should not be generalized.

## Extraction Notes

- Read the full post (short). Did not follow the linked simonw/research report; the fuzz harness and code details may be extractable from it in a follow-up.
- The 8 million fuzz figure and the "tests cover type preservation, parsing rules, and floating-point accuracy" statement appear only in the post's summary paragraph, not in the body. The triage comment's wording about "beat or match" is a paraphrase; the actual prompt is quoted above.
- Cross-reference claim numbers were verified against the headings of the cited notes.
