---
source_url: https://sourcegraph.com/blog/claude-code-file-picker-symbol-ranking
source_type: blog-post
title: "Filenames are the wrong index for Claude Code @ mentions"
author: Justin Dorfman (Sourcegraph)
date_published: 2026-08-20
date_extracted: 2026-08-22
last_checked: 2026-08-22
status: current
confidence_overall: emerging
issue: "#2860"
---

# Filenames are the wrong index for Claude Code @ mentions

> Sourcegraph engineering post diagnosing why Claude Code's `@` file-picker
> fails on symbol-name queries (fuzzy path character-matching, not filename
> matching), and shipping an open-source `fileSuggestion` hook that blends
> filename fuzzy-match, Sourcegraph symbol search, and git recency into one
> ranked score — with measured latency (p95 11.12ms), a documented index-
> staleness failure, and a fixed token-leak bug.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published August 20, 2026;
  auto-discovered via the `sourcegraph` trusted feed). Personal-voice
  engineering narrative: problem discovery (a third party's tweet), root-cause
  analysis, a three-signal scoring design, a worked before/after comparison,
  measured performance numbers, a documented failure the author hit while
  writing the post, and an install/uninstall walkthrough for the resulting
  tool.
- **Author credibility**: Byline is "Justin Dorfman," published on
  Sourcegraph's official company blog (same author as
  `blog-sourcegraph-dorfman-repo-security-posture.md`). The post is written in
  first person as the builder of the tool being described ("I started writing
  one at the gate," "I re-ran everything on August 20"), not as third-party
  reporting — this is first-party, hands-on engineering content, with
  Sourcegraph's commercial interest limited to the tool depending on
  Sourcegraph's `type:symbol` search product. A closing credit thanks
  "Stephanie Jarmak for her contributions to this blog post" (the author of
  `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`).
- **Scope**: Covers one narrow but concrete UX/tooling gap — Claude Code's
  `@` mention file picker — the `fileSuggestion` hook mechanism that lets a
  user override it, a three-signal ranking design and its measured weights,
  performance numbers against one real repository (Monty, 1,139 tracked
  files), a documented staleness failure and its root cause, two named
  limitations, and installation/configuration instructions including a fixed
  token-handling bug. Does NOT cover: Claude Code's own agentic search/grep
  behavior during task execution (a separate subsystem — see Cross-References
  for why this matters), any other `fileSuggestion`-style hook
  implementation, or evaluation of the tool against any repository other than
  Monty.

## Extracted Claims

### Claim 1: Claude Code's `@` file picker performs fuzzy path character-matching, not filename matching, so it returns paths whose characters happen to appear in order rather than paths whose name matches the query

- **Evidence**: Root-cause diagnosis of the problem Samuel Colvin reported (typing `@os.rs` in Monty returned fifteen irrelevant files, none of them named `os.rs`), explained mechanistically with a specific example path.
- **Confidence**: emerging (first-party technical diagnosis by the tool's author, not an Anthropic statement about the picker's internals, but directly demonstrated with a worked example)
- **Quote**: "Fuzzy path matching asks whether every character of your query appears somewhere in the path, in order. Walk `crates/monty/src/run.rs` against `os.rs` and you'll find the `o` in "monty", the `s` in "src", then `.`, `r`, `s` at the end. Valid match."
- **Our assessment**: This is a precise, falsifiable mechanistic explanation, not a vague complaint — it shows exactly why `run.rs`, `lib.rs`, and eleven other non-`os.rs` files all pass the picker's matching test. It reframes what looks like "the picker is broken" into "the picker is answering a different, more permissive question than the one users are asking," which is the article's load-bearing distinction and the reason a smarter ranking scheme (not a different match algorithm) is proposed as half the fix.

### Claim 2: When the query is a function or symbol name rather than a filename fragment, the picker returns zero results, because the name being searched for does not appear in any filename at all

- **Evidence**: A specific, named failure case (`@resolve_virtual_path` in Monty) contrasted explicitly with the "bad ordering" failure mode of Claim 1.
- **Confidence**: emerging (demonstrated with one named query against one real repository)
- **Quote**: "Type the name of a function and the filename index has nothing to offer at all, because the function name isn't in the filename. In Monty, `@resolve_virtual_path` returns **zero results**. Not a bad list. An empty one."
- **Our assessment**: This is the harder failure mode of the two, and the one that filename-only ranking improvements (Claim 4) cannot fix by construction — no amount of reordering an empty result set produces a match. It is the specific justification for adding a second signal (symbol search) rather than only tuning the first (filename fuzzy match).

### Claim 3: Claude Code exposes a `fileSuggestion` setting that lets a user replace the built-in `@` picker with an arbitrary external command, invoked once per keystroke with the query on stdin and ranked repo-relative paths expected on stdout

- **Evidence**: Mechanism description, attributed to a specific prior source (a tweet by Boris Cherny, Claude Code's creator, from April 2026) that the author says prompted the idea.
- **Confidence**: settled (a concrete, testable configuration mechanism the author then builds against and the note's Concrete Artifacts section reproduces verbatim)
- **Quote**: "You point it at a command. When you type `@`, Claude Code spawns that command once per keystroke, hands it `{"query": "..."}` on stdin, and shows whatever repo-relative paths it prints on stdout. Nothing in there tells you how to rank the list, which is the part I got excited about, so I started writing one at the gate."
- **Our assessment**: This is a first-party-verifiable extension-point fact about Claude Code (the `fileSuggestion` settings key exists and behaves this way), reported by a builder who then depends on it working exactly this way for a shipped tool — strong practical evidence even though it is not an Anthropic statement. Notably, the mechanism itself ships with no ranking logic at all ("nothing in there tells you how to rank the list"), meaning any ranking quality — good or bad — is entirely the responsibility of whatever command the user points it at, not something Claude Code adjudicates.

### Claim 4: A three-signal score (filename fuzzy match, Sourcegraph symbol search, git recency) is combined using logarithmically-tiered weights specifically designed so that no accumulation of weak signals can ever outrank a single strong one

- **Evidence**: The scoring table, with an explicit design rationale for the gap sizes between tiers.
- **Confidence**: emerging (a specific first-party design, with the exact weight values given as engineering choices, not derived from a formal optimization)
- **Quote**: "Every candidate gets one score, and the tiers sit far enough apart that no stack of weak signals ever outranks a strong one" — with the accompanying table: exact basename match 1,000,000; symbol name matches exactly 100,000; symbol name starts with the query 5,000; symbol name contains the query 800; definition rather than re-export +200; file touched in the last 25 commits +50.
- **Our assessment**: The design choice worth noting for harness engineers is the ordering-of-magnitude gap: a 6x jump between tiers means combinations of lower-tier signals (recency + substring match, for instance) can add at most a few hundred points, nowhere close to overtaking a 100,000-point exact symbol match. This is a deliberately conservative design against signal-stacking noise, at the cost of not letting several weak-but-consistent signals ever compound into a top rank — a tradeoff the post does not discuss explicitly but that follows directly from the stated weights.

### Claim 5: Filename-scoring improvements alone (nucleo fuzzy matching plus "exact basename wins") fully resolve the original reported bug — turning the symbol-search signal on or off makes no difference to the `@os.rs` result

- **Evidence**: A direct before/after comparison: running the hook with the symbol channel switched off, showing both real `os.rs` files land at ranks 1 and 2.
- **Confidence**: emerging (one worked example against one repository, but the comparison is a controlled on/off test of the specific signal in question)
- **Quote**: "`@os.rs` comes out right with the symbol channel switched off... Both real `os.rs` files, ranks 1 and 2, from filename scoring alone. Turning symbols on changes that list not at all. Sam's complaint was a path-scoring problem, and nucleo plus "exact basename wins" is the whole fix."
- **Our assessment**: This is the most important and most underappreciated finding in the post for anyone diagnosing similar picker complaints: the original, most publicized failure (Samuel Colvin's tweet) is fixable with better filename ranking alone — a much smaller change than standing up a symbol-search backend. Symbol search earns its place only on a narrower class of queries (Claim 2/Claim 6), not on the headline bug. A team facing "the `@` picker is bad" complaints should first check whether basename-exact-match precedence alone fixes it before reaching for a symbol index.

### Claim 6: Symbol search resolves queries that are function/type names absent from any filename — cases where nucleo's fuzzy filename match scores nothing on any candidate, because the query is not a subsequence of any candidate path

- **Evidence**: Two worked before/after query comparisons (`@resolve_virtual_path`, `@dropguard`) with filenames-only vs. with-symbols results shown side by side.
- **Confidence**: emerging (two worked examples against one repository)
- **Quote**: "@resolve_virtual_path / filenames only: (no results) / with symbols: crates/monty-fs/src/path_security.rs" and "@dropguard / filenames only: (no results) / with symbols: crates/monty/src/heap_traits.rs" ... "Neither query is a subsequence of the path it should return, so nucleo scores nothing on either one."
- **Our assessment**: This delineates exactly the boundary of what symbol search buys you: it does not improve already-working filename queries (Claim 5), it rescues queries that filename matching cannot answer in principle. This is a narrower, more defensible case for the added infrastructure cost of a symbol-search backend than "the picker is bad" would suggest.

### Claim 7: Warm-path latency is p50 9.32ms and p95 11.12ms over 200 real subprocess spawns against a 1,139-tracked-file repository, with ranking itself costing under a millisecond and the remainder attributable to process spawn and git; first invocation costs an extra 66ms for `git ls-files` and `git log`

- **Evidence**: Directly measured performance numbers, stated against an explicit self-imposed budget and with cost attribution across ranking vs. process/git overhead.
- **Confidence**: emerging (specific first-party measurement against one repository re-run "on August 20 against Monty at `70fe3f57`," not independently reproduced by this Miner or benchmarked against other repository sizes beyond the qualitative "19,000-file monorepo" extrapolation)
- **Quote**: "Warm p95 is 11.12ms over 200 real subprocess spawns, p50 9.32ms, against the 15ms bar I set for myself. The ranking itself is under a millisecond across Monty's 1,139 files, and the rest is process spawn plus `git`... First-ever invocation pays `git ls-files` and `git log` once, at 66ms."
- **Our assessment**: The self-imposed 15ms budget being cleared with room to spare (11.12ms p95) is a credible per-keystroke latency number for an interactive picker, and separating ranking cost (sub-millisecond, and the one component that scales with repo size) from process-spawn/git cost (fixed, does not scale) gives a useful mental model for extrapolating to larger repositories, though the post's own "several milliseconds on a 19,000-file monorepo" figure is stated qualitatively, not measured.

### Claim 8: Symbol-search results are cached to disk per four-character query prefix, so queries shorter than four characters never make a network call at all, and typing out a longer query character-by-character costs only one network fetch rather than one per keystroke

- **Evidence**: Direct description of the caching strategy and its effect on network call volume during interactive typing.
- **Confidence**: emerging (first-party design description; not independently benchmarked by this Miner)
- **Quote**: "Network never sits on the hot path: symbol results are cached to disk per four-character prefix, so typing `dropg`, `dropgu`, `dropgua`, `dropguard` costs one fetch instead of four. Anything shorter than four characters never goes over the wire at all. A cold prefix returns filename results immediately and spawns a detached fetch that fills the cache for the next keystroke."
- **Our assessment**: This is the specific engineering technique that keeps a network-backed ranking signal off the interactive hot path: the first keystroke of a new four-character prefix returns immediately using only the (local, fast) filename signal, while a detached background fetch populates the cache for the very next keystroke. It's a reasonable general pattern for any per-keystroke hook that wants to incorporate a network-backed signal without blocking on it — degrade gracefully to the local signal, backfill asynchronously.

### Claim 9: The symbol-search signal is only as fresh as Sourcegraph's own index, and a real production incident occurred where a renamed file (`heap.rs` → `heap/mod.rs`) caused a previously-working query to return zero results on both the filename and symbol channels until the index caught up

- **Evidence**: A specific, dated, self-reported incident the author says happened "while this post sat in review," including the before-state, the failure, the root cause, and the eventual resolution.
- **Confidence**: emerging (one specific, dated, first-party incident report — not a general staleness rate or SLA, but a concretely observed occurrence with a stated root cause)
- **Quote**: "`@collect_cycles` used to land `heap.rs` at rank 1, and on August 20 it returned nothing on both sides. Monty had refactored `heap.rs` into `heap/mod.rs`, sourcegraph.com's index still carried the old path, and the hook intersects symbol hits against `git ls-files` so you're never offered a file you don't have. Stale path, dropped, empty list... The symbol half is only as fresh as the index behind it, so when upstream moves a file you get the filename half until it catches up."
- **Our assessment**: This is the single most important caveat in the post, and the author reports it candidly rather than omitting it — a real, dated staleness failure in the author's own tool, discovered incidentally during the writing process rather than through deliberate testing. It is also a concrete illustration of the general index-staleness risk that `blog-anthropic-large-codebase-best-practices.md` argues against RAG-based retrieval for (see Cross-References): the failure mode described there — "by the time a developer queries the index, it reflects the codebase as it existed days, weeks, or even hours ago" — is exactly what happened here to a symbol index, in production, within the timeframe of writing one blog post. The hook's defensive design (intersecting symbol hits against live `git ls-files`) prevents suggesting a nonexistent path, but cannot prevent the stale index from silently omitting a file that does exist under a new name.

### Claim 10: The symbol index has two structural gaps that no amount of scoring-weight tuning can fix — `macro_rules!` macros never appear in the symbol index, and a trait method with many near-identical overrides has no single defining file for any signal to point to

- **Evidence**: Two named, specific limitations stated directly as known gaps in the "What it costs" section.
- **Confidence**: emerging (first-party statement of known limitations, not independently tested by this Miner against a Rust codebase with macros or heavily-overridden trait methods)
- **Quote**: "`macro_rules!` macros are absent from the symbol index, so `@defer_drop` will never resolve. And a trait method with thirty near-identical overrides has no single defining file, so no scoring signal can pick one for you."
- **Our assessment**: These are honestly disclosed structural boundaries rather than tuning problems — a macro genuinely may not have one canonical defining file in the way a function does, and a widely-implemented trait method genuinely may have thirty equally valid "definitions." Worth noting for readers evaluating whether a similar approach fits their own codebase: language features with many-to-one or no-canonical-location semantics (macros, trait/interface implementations, operator overloads in some languages) are a structural blind spot for this class of symbol-index-based ranking, independent of implementation quality.

### Claim 11: An earlier version of the hook attached the user's Sourcegraph access token to every outbound request regardless of destination, which leaked the author's own instance token to sourcegraph.com during testing and required rotating it; the fix sends the token only when the configured endpoint matches the endpoint actually being called

- **Evidence**: A first-person disclosed security bug in the tool's own development history, with the specific mechanism of the leak and the specific fix.
- **Confidence**: settled (a first-party, specific, named security defect and its specific fix, disclosed by the person who found and fixed it in their own code — not a hypothetical risk)
- **Quote**: "An earlier version of the hook attached `SRC_ACCESS_TOKEN` to every request, which sent one of my own instance tokens to sourcegraph.com during testing and meant rotating it. No build in the cookbook ever behaved that way, so there's nothing for you to rotate. Now the token goes out only when `SRC_ENDPOINT` matches the endpoint actually being called."
- **Our assessment**: This is a genuine token-leak-and-fix disclosure, not a generic "handle secrets carefully" caveat — the author names the exact bug (token attached unconditionally to all requests, including requests to a different, unintended endpoint), confirms it was caught before any public build shipped it ("no build in the cookbook ever behaved that way"), and states the specific fix (endpoint-matching gate before attaching the token). This is directly relevant to any harness-engineering guidance on writing custom Claude Code hooks that call out to authenticated third-party services: hooks that read credentials from the environment must scope which requests get the credential, not attach it unconditionally to every outbound call the hook makes.

### Claim 12: The tool requires no Sourcegraph account for public repositories (it queries sourcegraph.com anonymously by default) and degrades gracefully to filename-only ranking with no error when no indexed repository is available at all

- **Evidence**: Explicit statement of the no-account default and the no-index fallback behavior, in the installation/configuration section.
- **Confidence**: settled (a specific, verifiable default-configuration claim from the tool's author)
- **Quote**: "You don't need a Sourcegraph account for public code. The hook queries sourcegraph.com anonymously by default, so any indexed public repo works the moment you install it." ... "Without an indexed repo you get the filename half and nothing breaks."
- **Our assessment**: The graceful-degradation property (falls back to filename-only ranking rather than erroring) is an important adoption-risk detail — it means installing the hook is a strictly-additive, low-risk change even against a private or unindexed repository, since the worst case is simply "no symbol signal," not a broken picker. Combined with Claim 3's one-line uninstall, this makes the tool low-commitment to try.

## Concrete Artifacts

### Scoring weight table (verbatim, from "Three signals instead of one")
```
Source: https://sourcegraph.com/blog/claude-code-file-picker-symbol-ranking
Author: Justin Dorfman, Sourcegraph — published August 20, 2026

| Signal                              | Weight    |
| ------------------------------------ | --------- |
| Exact basename match                | 1,000,000 |
| Symbol name matches exactly         | 100,000   |
| Symbol name starts with the query   | 5,000     |
| Symbol name contains the query      | 800       |
| Definition rather than re-export    | +200      |
| File touched in the last 25 commits | +50       |
```

### Before/after query comparisons (verbatim, from "Half the fix is better ranking")
```
Source: https://sourcegraph.com/blog/claude-code-file-picker-symbol-ranking

@os.rs, symbol channel switched off:
1  crates/monty-types/src/os.rs
2  crates/monty/src/modules/os.rs
3  crates/monty-fs/src/overlay_state.rs

@resolve_virtual_path
  filenames only:  (no results)
  with symbols:    crates/monty-fs/src/path_security.rs

@dropguard
  filenames only:  (no results)
  with symbols:    crates/monty/src/heap_traits.rs
```

### Installation and configuration (verbatim, from "Run it")
```
Source: https://sourcegraph.com/blog/claude-code-file-picker-symbol-ranking

# Build and install the binary:
curl -sL https://github.com/sourcegraph-community/cookbook/archive/refs/heads/main.zip -o cookbook.zip && unzip -qo cookbook.zip 'cookbook-main/symbol-ranked-file-picker/*' 'cookbook-main/LICENSE' && (cd cookbook-main/symbol-ranked-file-picker && env -u RUSTUP_TOOLCHAIN cargo build --release && cp target/release/file-suggestion ~/.claude/file-suggestion)

# Add one top-level key to ~/.claude/settings.json:
{
  "fileSuggestion": { "type": "command", "command": "~/.claude/file-suggestion" }
}

# Private repos need your own Sourcegraph instance and a token
# (both endpoint variables, not one):
export CLAUDE_SG_ENDPOINT="https://sourcegraph.example.com"
export SRC_ENDPOINT="https://sourcegraph.example.com"
export SRC_ACCESS_TOKEN="sgp_..."
```

Source license/scope note, verbatim: "It's in the Sourcegraph Community
cookbook, Apache-2.0, about 1,200 lines of Rust."

## Cross-References

- **Extends**: `blog-anthropic-large-codebase-best-practices.md` Claim 2
  (Claude Code uses agentic search, not RAG-based retrieval, specifically
  because embedding/index-based retrieval goes stale — "By the time a
  developer queries the index, it reflects the codebase as it existed days,
  weeks, or even hours ago") and Claim 10 (LSP integrations give Claude
  IDE-level symbol navigation — following definitions, tracing cross-file
  references, disambiguating identically-named symbols). This source's Claim
  9 (the `heap.rs` → `heap/mod.rs` rename causing a stale, empty symbol-search
  result) is a concrete, dated, real-world instance of exactly the staleness
  failure mode Anthropic's post warns index-based retrieval is prone to —
  but happening in a different subsystem: Claude Code's own agentic search
  (grep, filesystem traversal) that Anthropic's post describes is Claude's
  mechanism for *exploring code during task execution*, whereas this source's
  `fileSuggestion` hook governs a narrower, separate UI surface — the
  interactive `@` mention picker a human uses to attach a file to a prompt,
  which never touches Claude's own grep-based exploration at all. This
  source's symbol-search signal is closer in spirit to Anthropic's Claim 10
  (LSP-style symbol resolution) than to Claim 2's agentic search, and it
  independently demonstrates the same index-staleness risk that motivated
  Claude Code's own core search to avoid indexes in the first place — just
  in a different, opt-in extension point that a user adds on top. **No
  contradiction filed**: these are different subsystems solving different
  problems (attach-a-file UX vs. task-execution code exploration), so the
  staleness finding here does not oppose Anthropic's architectural claim
  about Claude's own search — it corroborates the underlying staleness risk
  Anthropic's claim is built around, applied to a different, adjacent tool.
- **Corroborates**: `blog-anthropic-steering-claude-code-mechanisms.md`
  Claim 8 ("There are five types of hooks — command, HTTP, mcp_tool, prompt,
  and agent — where only the first three are truly deterministic," quoting
  "The first three execute deterministically while the latter two, prompt
  and agent, use Claude's judgment rather than a set of rules to determine
  the output"). The `fileSuggestion` hook documented in this source is a
  concrete, shipped, real-world example of exactly a `command`-type hook
  (`{"type": "command", "command": "~/.claude/file-suggestion"}` per this
  source's Concrete Artifacts) — a fully deterministic external binary
  invoked per keystroke. This is the first source in the corpus to document
  a complete, production, end-to-end `command` hook implementation
  (binary, scoring logic, caching, and measured latency) rather than
  describing the hook type in the abstract.
- **Corroborates**: `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`
  (same publisher, overlapping author credit — Stephanie Jarmak is
  acknowledged in this source's closing line, and is the byline author of
  that note). That source's Claim 5 argues retrieval difficulty should be
  weighted by dispersion (how spread out the answer is) rather than raw
  codebase size. This source's `@resolve_virtual_path` and `@dropguard`
  cases (Claim 6) are a narrower, UI-scoped instance of the same underlying
  point: a query that names a *symbol* rather than a *path fragment* is
  exactly the kind of dispersed, non-path-local query that plain fuzzy path
  matching cannot answer, regardless of codebase size — both sources
  independently arrive at "symbol/semantic signals matter separately from
  path-string signals," one for MCP-based code retrieval during task
  execution, this one for the interactive file-attachment picker.
- **Novel**: The `fileSuggestion` Claude Code settings key and its exact
  invocation contract (per-keystroke spawn, `{"query": "..."}` on stdin,
  ranked repo-relative paths on stdout) is not documented anywhere else in
  this corpus. The three-signal weighted-scoring design (filename fuzzy
  match, Sourcegraph symbol search, git recency) with its specific tiered
  weight table; the measured per-keystroke latency numbers (p50 9.32ms, p95
  11.12ms) and their cost attribution (ranking sub-millisecond, rest is
  process spawn + git); the four-character-prefix disk caching strategy for
  keeping a network-backed signal off the interactive hot path; the
  documented `heap.rs`/`heap/mod.rs` staleness incident; and the
  unconditional-token-attachment security bug and its endpoint-matching fix
  are all new to this corpus. No existing source documents a Claude Code
  extension point below the level of hooks/skills/MCP/CLAUDE.md — this is
  the first corpus source specifically about the `@` mention file-picker as
  a distinct, separately-configurable surface.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Extension Points / `fileSuggestion`
  hook**: `blog-anthropic-large-codebase-best-practices.md` already
  established a "seven extension points" taxonomy (CLAUDE.md, hooks, skills,
  plugins, MCP servers, LSP integrations, subagents) for Chapter 02, and
  `blog-anthropic-steering-claude-code-mechanisms.md` documents the five hook
  *types* (command, HTTP, mcp_tool, prompt, agent) in the abstract. Neither
  source names the `fileSuggestion` settings key or the `@` mention picker as
  a distinct, user-overridable surface. Recommend adding a concrete
  worked example under the "hooks" extension point specifically —
  "customizing the `@` file picker" — using this source's `command`-type
  `fileSuggestion` hook as the first fully-worked example of a `command`
  hook the guide has (binary, per-keystroke invocation contract, measured
  latency budget, one-line install/uninstall).
- **Chapter 02 (Harness Engineering) — large-codebase navigation**: The
  existing "Large Codebase Navigability" recommendations (from
  `blog-anthropic-large-codebase-best-practices.md`) cover CLAUDE.md
  layering, subdirectory initialization, test/lint scoping, codebase maps,
  and LSP integration, but say nothing about the `@` mention picker as a
  navigation surface a practitioner might need to fix separately. Recommend
  adding this source's core diagnostic — filename fuzzy-matching cannot find
  a file by the symbol it defines, only by characters in its path — as a
  named, distinct failure mode alongside the existing checklist, with the
  fix ordering this source demonstrates: try exact-basename-match ranking
  first (Claim 5, resolves the common case), add a symbol-search signal only
  for the narrower symbol-name-query case it doesn't cover (Claim 6).
- **Chapter 06 (Security & Threat Model) — hook credential scoping**: If
  the guide has or adds guidance on writing custom Claude Code hooks that
  call authenticated external services, this source's Claim 11 (an earlier
  build of the hook attached `SRC_ACCESS_TOKEN` to every outbound request
  regardless of destination, leaking the author's own token to
  sourcegraph.com) is a concrete, first-party example of the exact failure
  mode to guard against: hooks must scope credential attachment to the
  intended destination endpoint, not attach ambient credentials to every
  request the hook happens to make. Recommend citing this as a worked
  example distinct from the guide's existing MCP-supply-chain / rug-pull
  security content, since it is a hook-authoring mistake rather than an
  MCP-server or dependency-supply-chain risk.

## Extraction Notes

- **WebFetch summarized rather than reproduced verbatim on the first pass**,
  consistent with this Miner's experience on other Sourcegraph blog posts in
  this corpus (see Extraction Notes in
  `blog-sourcegraph-dorfman-repo-security-posture.md` and
  `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`). Per MINER.md §2a,
  this Miner did not rely on that summary for any `Quote` field. Instead,
  this Miner fetched the raw page HTML directly via `curl` and located the
  full article body embedded verbatim as a JSON string literal in the
  page's inline SvelteKit hydration `<script>` payload (`content:"..."`).
  Every `Quote` and code/table artifact in this note was copied
  character-for-character from that embedded source text, not from the
  WebFetch summary.
- **No sub-pages followed independently**: The post links to a tweet by
  Samuel Colvin (the reported bug), a tweet by Boris Cherny (the
  `fileSuggestion` mechanism's origin), the Monty GitHub repository, the
  `nucleo-matcher` crate docs, and the Sourcegraph Community cookbook page
  for the tool itself. None were fetched independently — the tweets are
  attributed and quoted only insofar as the blog post itself describes
  their content (this note does not claim independent verification of the
  tweets' exact wording), and the cookbook/Monty links are software
  repositories rather than additional substantive prose content within
  MINER.md's "follow up to 5 linked pages" guidance for text sources.
- **Confidence set to `emerging` overall**: The post's mechanism claims
  (the `fileSuggestion` settings contract, the hook type taxonomy overlap)
  are corroborated by an independent first-party Anthropic source and are
  graded closer to settled at the claim level. However, the performance
  numbers, the staleness incident, and the scoring-design rationale are all
  single-author, single-repository (Monty), non-independently-reproduced
  first-party engineering claims — real and specific, but not
  independently verified by this Miner or reproduced against a second
  codebase. No claim in this note is graded `settled` except the two
  claims (3, 11, 12) describing directly-observable, self-contained
  configuration facts and a disclosed-and-fixed bug rather than measured
  or extrapolated results.
- **No contradiction issue filed**: See Cross-References — Extends above
  for the reasoning. The apparent tension between this source's
  index-staleness incident and Anthropic's pro-agentic-search/anti-RAG
  architectural claim was considered and judged not to rise to a real
  contradiction, since the two claims describe different subsystems
  (interactive file-attachment UI vs. autonomous task-execution code
  search) rather than opposing positions on the same mechanism.
