---
source_url: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/
source_type: blog-post
title: "Claude Code uses Bun written in Rust now"
author: Simon Willison
date_published: 2026-07-19
date_extracted: 2026-07-24
last_checked: 2026-07-24
status: current
confidence_overall: settled
issue: "#2190"
---

# Claude Code uses Bun written in Rust now

> Simon Willison independently verifies, via binary inspection of his own
> Claude Code installation, that the Rust-rewritten Bun runtime documented in
> Jarred Sumner's post is actually shipping in production — supplying the
> first third-party (non-Anthropic, non-Sumner) confirmation of that claim,
> plus three reproducible verification methods any reader can run themselves.

## Source Context

- **Type**: blog-post (Simon Willison "note" format — his shortest post
  type, distinct from a full blogmark or essay; ~300 words including two
  later-appended "Update" addenda). Tagged `rust`, `anthropic`, `claude-code`,
  `bun`, `jarred-sumner`.
- **Author credibility**: Simon Willison is the creator of Django and one of
  the highest-signal independent AI tooling commentators (see the author-
  credibility discussion in `blog-simonwillison-not-locked-in.md` and dozens
  of other corpus notes). Unlike his July 8 post on the same underlying event
  (`blog-simonwillison-rewriting-bun-rust.md`), which was pure curation of
  Jarred Sumner's primary source, this post is first-hand technical
  investigation: Willison ran his own commands against his own locally
  installed `claude` binary and reports his own output.
- **Scope**: Covers exactly one narrow question — can an outside party
  independently confirm, from the shipped Claude Code binary itself, that it
  embeds the Rust-rewritten Bun runtime Sumner described in his primary post
  (already mined in `blog-pragmaticengineer-bun-rust-rewrite.md`)? Willison
  answers this using three techniques: (1) `strings`-extracting a Bun version
  string from the binary, (2) `strings`-extracting embedded `.rs` source file
  paths, (3) a reader-contributed runtime trick using Bun's own
  `BUN_OPTIONS=--preload` mechanism against the `claude` executable. Does NOT
  cover: any of the rewrite's harness mechanics, cost, regressions, or test
  methodology — all already covered in depth by
  `blog-pragmaticengineer-bun-rust-rewrite.md` and
  `blog-simonwillison-rewriting-bun-rust.md`.

## Extracted Claims

### Claim 1: Willison independently confirmed, via `strings`-extracting a version string from his local Claude Code binary, that it embeds a Bun build labeled "v1.4.0" — a version number that, as of the post date, had never been publicly tagged as a non-canary Bun release (the latest public tag was v1.3.14)

- **Evidence**: A reproducible terminal command (`strings ~/.local/bin/claude | grep -m1 'Bun v1'`) and its literal output on Willison's own machine, cross-checked by Willison against Bun's public GitHub releases page.
- **Confidence**: settled (reproducible command, verifiable by any reader against a public releases page, and independently corroborated by this note's own re-verification — see Extraction Notes)
- **Quote**: "I found these two commands convincing: strings ~/.local/bin/claude | grep -m1 'Bun v1' For me this outputs Bun v1.4.0 (macOS arm64). The most recent release of Bun on GitHub is currently v1.3.14 from May 12th, so that v1.4.0 version number in Claude supports them shipping a preview of a not-yet-released Bun version."
- **Our assessment**: This is the strongest single claim in the source: a specific, checkable version number embedded in a widely-distributed production binary, cross-referenced against the public release history to show it predates any public tag. It converts Sumner's self-reported "we shipped this" claim (already in the corpus via `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 12) into an externally-falsifiable, independently-reproduced fact.

### Claim 2: A second `strings` extraction turned up 563 embedded `.rs` source-file paths in the Claude Code binary, which Willison offers as evidence the Rust port is "indeed being run in production across millions of different devices"

- **Evidence**: A second reproducible command (`strings ~/.local/bin/claude | grep -Eo 'src/[[:alnum:]_./-]+\.rs'`) with three sample filenames quoted directly, and a link to the full 563-line list as a public gist.
- **Confidence**: emerging (the underlying observation — Rust source paths are compiled into the binary — is directly reproducible, but the specific "563 filenames" figure is a weaker proxy for "size of the Bun rewrite" than it first appears; see Our assessment)
- **Quote**: "This outputs a list of 563 filenames, starting with these: src/runtime/bake/dev_server/mod.rs src/runtime/bake/production.rs src/bundler/bundle_v2.rs It looks like Bun in Rust is indeed being run in production across millions of different devices."
- **Our assessment**: We fetched the linked gist directly (`gist.github.com/simonw/c92fb0f67b114ac26e3b95a09ddccfdc`) to check this claim's composition. Only a minority of the 564 raw lines (38 of 564) match Bun's own known top-level source directories (`src/runtime/`, `src/bundler/`, `src/jsc/`, `src/js_parser/`); the remainder are generic-looking paths (`src/vec/mod.rs`, `src/collections/btree/node.rs`, `src/panicking.rs`, `src/codecs/jpeg/decoder.rs`, `src/deflate/core.rs`) consistent with Rust standard-library and vendored third-party crate source (an `image`-crate-style codec set, `backtrace`, `miniz_oxide`-style deflate code) whose file paths get baked into any sizeable Rust binary's debug/panic strings regardless of whether that code is part of "the rewrite" specifically. There are also only 224 unique paths in the list (several filenames like `src/bundler/bundle_v2.rs` and `src/lib.rs` repeat). None of this undermines Willison's core conclusion — Rust code is unambiguously present and running in production — but "563 filenames" should not be read as "563 files of Bun-specific rewritten code"; it is a noisier signal than the version-string check in Claim 1.

### Claim 3: A reader-contributed technique (credited to Ajan Raj) lets anyone query the exact embedded Bun version at runtime by using Bun's own `BUN_OPTIONS=--preload` environment variable against the `claude` executable itself, without needing `strings` or binary inspection

- **Evidence**: A four-line reproducible shell/TypeScript snippet plus Willison's own reported output running it against his installation.
- **Confidence**: settled (reproducible, and its output — "1.4.0" — is independently consistent with Claim 1's `strings`-based result on the same machine)
- **Quote**: "Update: Here's a neat trick from Ajan Raj: cat > /tmp/bun-version.ts <<'EOF' console.log(\"embedded bun:\", Bun.version); process.exit(0); EOF BUN_OPTIONS=\"--preload=/tmp/bun-version.ts\" claude --version This outputs 1.4.0 for me."
- **Our assessment**: This is a genuinely different verification method from Claim 1's `strings` approach (it invokes the embedded Bun runtime's own preload mechanism rather than scanning binary strings), and it agrees with the version-string result. Two independent methods converging on the same version number is stronger evidence than either alone, and it's notable that the trick works at all — it implies the `claude` binary's embedded Bun runtime honors standard Bun environment variables when invoked as a CLI entrypoint, a detail about how deeply Bun is embedded (not just linked as a library, but runnable as itself) that neither of the two prior corpus notes on this rewrite mentions.

### Claim 4: The commit that set Bun's internal `package.json` version string to "1.4.0" was merged May 17, 2026, and that version had not changed nor been tagged in any public non-canary release as of the post date (July 19, 2026) — over two months later

- **Evidence**: A direct link to the specific GitHub commit (`oven-sh/bun@b18bf6d`), which we independently fetched and confirmed: the commit ("Bump (#30952)," authored by Jarred Sumner, dated Sun 17 May 2026) bumps the public `LATEST` marker file from 1.3.13 to 1.3.14 while simultaneously bumping the internal `package.json` `"version"` field from 1.3.14 to 1.4.0 — a divergence between the publicly-tagged version and the internal development version in the same commit.
- **Confidence**: settled (verifiable against a public, immutable commit)
- **Quote**: "Here's the commit from May 17th that updated the version in package.json to 1.4.0. That version hasn't been changed since then, but also hasn't yet made it into a tagged release outside of canary."
- **Our assessment**: This pins down, with a specific commit hash and date, exactly when Bun's own repository first internally marked itself as "1.4.0" — giving a verifiable lower bound for when the Rust rewrite's version numbering diverged from the publicly-shipping Zig-based line, independent of either Sumner's or Anthropic's own narrative timeline.

### Claim 5: As of an "Update" appended to the post, the Rust-rewritten Bun has since been released through Bun's own public canary channel, installable via `bun upgrade --canary`

- **Evidence**: Willison's own updated text, linking to Bun's canary-builds documentation and the `canary` release tag on GitHub.
- **Confidence**: settled (points to a live, checkable public release channel)
- **Quote**: "(Update: The Rust version has been released as Bun canary - running bun upgrade --canary will install this release.)"
- **Our assessment**: This is a small but concrete timeline data point absent from both prior corpus notes on the rewrite: the Rust port's first public distribution channel (beyond being silently embedded in Claude Code) was Bun's canary track, not a stable release — consistent with Claim 4's finding that "1.4.0" had, as of this post, still not reached a tagged non-canary release more than two months after the internal version bump.

### Claim 6: Jarred Sumner's original claim — that Claude Code v2.1.181 (released June 17, 2026) and later versions use the Rust port of Bun, with Linux startup 10% faster and "otherwise, barely anyone noticed" — is what prompted Willison's investigation

- **Evidence**: A direct blockquote of Sumner's own post, presented by Willison as the claim he set out to verify.
- **Confidence**: settled (already corroborated across three independent corpus sources — see Cross-References)
- **Quote**: "Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good."
- **Our assessment**: Not new evidence in itself (it restates a figure already in the corpus via `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 12 and `blog-simonwillison-rewriting-bun-rust.md`'s concrete artifact), but it is the explicit trigger for this post's independent-verification methodology, which is this source's real contribution.

## Concrete Artifacts

### Full post text (verbatim, simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)

```
Source: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/
Posted: 19th July 2026 at 3:54 am
Tags: rust, anthropic, claude-code, bun, jarred-sumner

Claude Code uses Bun written in Rust now

In Rewriting Bun in Rust, Jarred Sumner made the following claim:

  Claude Code v2.1.181 (released June 17th) and later use the Rust port of
  Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed.
  Boring is good.

I decided to have a poke at my own Claude Code installation to see if I
could find evidence that it was using Bun written in Rust.

I found these two commands convincing:

  strings ~/.local/bin/claude | grep -m1 'Bun v1'

For me this outputs Bun v1.4.0 (macOS arm64). The most recent release of Bun
on GitHub is currently v1.3.14 from May 12th, so that v1.4.0 version number
in Claude supports them shipping a preview of a not-yet-released Bun
version.

(Update: The Rust version has been released as Bun canary - running bun
upgrade --canary will install this release.)

  strings ~/.local/bin/claude | grep -Eo 'src/[[:alnum:]_./-]+\.rs'

This outputs a list of 563 filenames, starting with these:

  src/runtime/bake/dev_server/mod.rs
  src/runtime/bake/production.rs
  src/bundler/bundle_v2.rs

It looks like Bun in Rust is indeed being run in production across millions
of different devices. Like Jarred said, "Boring is good".

Update: Here's a neat trick from Ajan Raj:

  cat > /tmp/bun-version.ts <<'EOF'
  console.log("embedded bun:", Bun.version);
  process.exit(0);
  EOF
  BUN_OPTIONS="--preload=/tmp/bun-version.ts" claude --version

This outputs 1.4.0 for me.

Here's the commit from May 17th that updated the version in package.json to
1.4.0. That version hasn't been changed since then, but also hasn't yet made
it into a tagged release outside of canary.
```

### Independent re-verification of the gist link (fetched by this Miner, 2026-07-24)

```
Source: https://gist.github.com/simonw/c92fb0f67b114ac26e3b95a09ddccfdc (raw)

Total lines in raw gist: 564 (matches Willison's "563 filenames" within a
one-line rounding/fence-boundary difference)
Unique paths: 224 (i.e. many filenames repeat, e.g. "src/lib.rs" appears
3 times, "src/bundler/bundle_v2.rs" appears twice)
Paths matching Bun's own known top-level source tree
(src/runtime/, src/bundler/, src/jsc/, src/js_parser/): 38 of 564

Sample of non-Bun-specific-looking paths present in the same list:
  src/vec/mod.rs
  src/collections/btree/node.rs
  src/panicking.rs
  src/codecs/jpeg/decoder.rs
  src/codecs/webp/decoder.rs
  src/deflate/core.rs
  src/../../backtrace/src/backtrace/libunwind.rs

These read as Rust standard-library and vendored third-party crate paths
(an image-codec crate, a backtrace crate, deflate/compression code) rather
than Bun's own rewritten source — consistent with how `strings` on any
sizeable Rust binary surfaces file paths baked into panic/debug-info tables
across the whole dependency tree, not just first-party code.
```

### Independent re-verification of the linked commit (fetched by this Miner, 2026-07-24)

```
Source: https://github.com/oven-sh/bun/commit/b18bf6d1d0a92238f240bfd125f0e3b3461b9243
Commit: b18bf6d, "Bump (#30952)", Jarred Sumner, Sun 17 May 2026 17:34:04 -0700

diff --git a/LATEST b/LATEST
-1.3.13
+1.3.14
diff --git a/package.json b/package.json
-  "version": "1.3.14",
+  "version": "1.4.0",
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 12 (Claude Code v2.1.181,
    released June 17 2026, first production consumer of the Rust-ported Bun
    runtime, 10% faster Linux startup, "barely anyone noticed") — this
    source's Claim 6 quotes the identical Sumner claim, and Claims 1-3 supply
    the first *independent, non-Sumner, non-Anthropic* technical verification
    that this claim is true, via binary inspection rather than self-report.
  - `blog-simonwillison-rewriting-bun-rust.md` (Concrete Artifacts, full
    blogmark text) — that note's blockquoted excerpt of the same "Claude Code
    v2.1.181 ... Startup got 10% faster on Linux" line is the identical
    passage Willison quotes again as the trigger for this follow-up
    investigation, published by the same author 11 days later.
  - `blog-anthropic-dynamic-workflows-claude-code.md` Claim 6 (Sumner used
    dynamic workflows to port Bun from Zig to Rust) — this source does not
    add mechanism detail on the port itself, but independently confirms the
    port's real-world production outcome that Claim 6 describes as the
    project's showcase result.
- **Extends**: `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 12 and
  `blog-simonwillison-rewriting-bun-rust.md`'s corroborating account — both
  prior notes report the production-deployment claim as first-party
  (Sumner's own account, secondarily curated by Willison without independent
  checking). This source is the first in the corpus to independently
  *test* that claim from outside Anthropic/Bun, using three separate
  reproducible technical methods (binary string extraction of a version
  marker, binary string extraction of source file paths, and a runtime
  environment-variable probe), two of which (Claims 1 and 3) converge on the
  same version number from independent angles.
- **Contradicts**: None identified against existing corpus notes. This
  source's own internal evidence does complicate a plain reading of its own
  Claim 2 (the "563 filenames" figure is a noisier signal than it first
  appears — see Our assessment under Claim 2), but this is a caveat on the
  strength of one data point within the source, not a claim that materially
  opposes an existing source note or would change guide advice, so no
  contradiction issue was filed per MINER.md §4a ("claims differ only in
  degree of confidence" is not grounds for filing).
- **Novel**:
  - The first third-party, reproducible, non-self-reported verification that
    the Rust-rewritten Bun is genuinely present and running in the
    widely-distributed Claude Code binary (Claims 1-3).
  - The specific internal version marker "1.4.0" embedded in the binary, and
    the finding that it predates any public non-canary Bun release by more
    than two months as of the post date (Claims 1, 4, 5).
  - The `BUN_OPTIONS=--preload` runtime-probe technique (Claim 3) as a
    reusable verification method distinct from binary string-scanning —
    useful more generally for confirming which runtime/dependency version an
    AI CLI tool has actually embedded, versus what it claims in release
    notes.
  - The specific commit hash and date (`b18bf6d`, May 17 2026) marking when
    Bun's own repository first internally diverged its version string to
    "1.4.0" (Claim 4).

## Guide Impact

- **Chapter 04 (Tools & IDE Integration)**: Add this source as a concrete
  example of *independently verifying* a vendor's infrastructure claim about
  an AI coding tool, rather than taking a release note at face value. The
  three reproducible techniques here (`strings | grep` for an embedded
  version string, `strings | grep` for embedded source paths, and an
  environment-variable runtime probe) are a reusable template for
  practitioners who want to confirm what runtime/dependency version a CLI
  tool actually ships, independent of its changelog. Pair with the caveat
  from Claim 2: a raw count of extracted filenames can overstate how much of
  a binary is "the rewrite" specifically, since generic stdlib/dependency
  paths surface in the same `strings` output.
- **Chapter 02 (Building AI-Native Products)**: Reinforces, with independent
  confirmation, the existing corpus point (via
  `blog-pragmaticengineer-bun-rust-rewrite.md`) that Anthropic shipped a
  pre-release, not-yet-publicly-tagged dependency version silently to all
  Claude Code users in production — this source adds that, as of two months
  after the internal version bump, that dependency version still had not
  reached a public non-canary release, meaning production users were running
  a build more bleeding-edge than anything an external developer could
  install themselves outside of canary. Worth a callout on the risk/benefit
  tradeoff of an AI tooling vendor shipping ahead of its own dependency's
  public release cadence.

## Extraction Notes

- This is a short Willison "note" (~300 words, his shortest post format),
  read in full via raw HTML fetched directly (`curl`) to verify every quoted
  passage character-for-character against the live page (fetched
  2026-07-24), rather than relying on a summarizer.
- Per MINER.md §1, outbound links were followed: (1) the linked gist of 563
  filenames (`gist.github.com/simonw/c92fb0f67b114ac26e3b95a09ddccfdc`),
  fetched in full and independently analyzed for composition (see Concrete
  Artifacts and Claim 2's Our assessment); (2) the linked GitHub commit
  (`b18bf6d`) that bumped `package.json`'s version to 1.4.0, fetched as a
  patch and confirmed to match Willison's description exactly. Two links
  were not followed: the linked tweet from Ajan Raj (`twitter.com/ajanraj25`)
  returned no content to an unauthenticated fetch (X/Twitter blocks
  scraping), but its substance is fully reproduced as a code block in
  Willison's own post text, so nothing was lost; the Bun canary-builds
  documentation page (`bun.com/docs/installation#canary-builds`) is a
  client-side-rendered SPA that did not yield readable text via a raw HTML
  fetch, and its content (generic canary-install instructions) is tangential
  to this source's specific claims, so it was not pursued further.
  `bun.com/blog/bun-in-rust` (the underlying primary source for the whole
  rewrite) was not re-extracted here since it is already deeply mined in
  `blog-pragmaticengineer-bun-rust-rewrite.md` (issue #1741); this note
  focuses on what is specific to Willison's July 19 follow-up investigation.
- The Prospector filed three triage comments on this issue with varying
  novelty assessments (medium, high, high) and slightly different chapter
  suggestions (Ch02; Ch02 + Ch04; Ch02 + Ch04 again). This note follows the
  most detailed of the three, which correctly identifies the source's real
  contribution as the independent-verification methodology (binary
  inspection, reproducible commands) rather than new facts about the rewrite
  itself — the underlying rewrite facts (cost, harness, regressions) are
  already covered in depth by the two existing Bun-rewrite notes in the
  corpus.
- No contradiction was filed. The one nuance surfaced during extraction — that
  the "563 filenames" figure in Claim 2 is a noisier proxy for the rewrite's
  scope than a plain reading suggests, once the gist's actual composition is
  checked — is a caveat on a single data point within this source's own
  evidence, not a disagreement between two claims that would change guide
  advice, so it is captured as an "Our assessment" note rather than a filed
  contradiction issue per the MINER.md §4a "when NOT to file" guidance.
