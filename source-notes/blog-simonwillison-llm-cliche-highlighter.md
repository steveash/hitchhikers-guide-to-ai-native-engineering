---
source_url: https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/
source_type: blog-post
title: "LLM cliché highlighter"
author: Simon Willison
date_published: 2026-07-17
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: anecdotal
issue: "#2159"
---

# LLM cliché highlighter (Simon Willison)

> A one-paragraph "beat" post in which Willison announces a vibe-coded, deterministic
> regex-based web tool for highlighting clichéd phrasing that recurs in LLM-generated
> writing (e.g. "no X, no Y" chains, "sit with that," "you already know"). The post
> itself is ~90 words; the substantive content is the tool's shipped source, which
> implements twelve named pattern detectors — not ten, as the post's prose claims —
> each with explicit false-positive exclusions and a self-test suite.

## Source Context

- **Type**: blog-post (Simon Willison's link-blog "beat" format — a very short post
  announcing a tool, distinct from his longer essay-style posts). Posted 17th July
  2026 at 12:11 pm. Tagged `tools`, `ai`, `generative-ai`, `llms`.
- **Author credibility**: Simon Willison is the creator of Django and one of the
  highest-signal independent AI tooling commentators in this corpus (see dozens of
  prior notes, e.g. `blog-simonwillison-rewriting-bun-rust.md`,
  `blog-simonwillison-rss-vibe-coded-apps.md`). Here he is both source and subject —
  he built the tool himself and is announcing his own work, not curating a third
  party's. His credibility bears on the tool's execution quality, not on any external
  claim (the post makes none beyond "I built this because clichés annoyed me").
- **Scope**: Covers only the tool announcement and the tool's own shipped code
  (`tools.simonwillison.net/llm-cliche-highlighter`, fetched and read directly for
  this note — see Extraction Notes). Does NOT cover: any broader theory of why LLMs
  produce these phrasings, any measurement of how common these clichés are across a
  corpus of real LLM output, or any guidance on what to do once a cliché is detected
  (the tool highlights; it does not rewrite or fix).

## Extracted Claims

### Claim 1: Willison built the tool out of frustration with recurring clichéd phrasing in LLM-generated writing, citing "no fluff, no filler, no jargon" as a representative example
- **Evidence**: Willison's own stated motivation, in the post's opening sentence.
- **Confidence**: anecdotal (single author's stated motivation for a personal tool; no data on how widespread the annoyance is among readers generally)
- **Quote**: "I got frustrated reading yet another article that was crammed with the clichés of LLM-generated writing - \"no fluff, no filler, no jargon\" type stuff"
- **Our assessment**: This is a credible, specific first-hand irritant (not a general claim about LLM output quality), and it matches a pattern already visible elsewhere in this corpus of practitioners treating certain LLM phrasings as a readability/trust signal (see Cross-References). It's evidence that at least one high-signal reader finds these patterns common enough to be worth building tooling against — not evidence of prevalence or severity at scale.

### Claim 2: The tool was built by having Fable 5 "vibe code" the app, per Willison's own account
- **Evidence**: Willison's direct statement of how the tool was produced.
- **Confidence**: settled (first-party statement about the author's own process, consistent with this corpus's extensive prior documentation of Willison's vibe-coding practice)
- **Quote**: "so I had Fable 5 vibe code up this app for highlighting ten common patterns that show up in that sort of writing"
- **Our assessment**: Consistent with the broader pattern already well-documented in this corpus (`blog-simonwillison-rss-vibe-coded-apps.md` Claim 1: vibe-coding accelerates app development to blog-post-like release cadence). This is another data point of that same practice — a small, single-purpose, publicly shipped browser tool produced and announced same-day as a throwaway "beat" post, with no separate engineering writeup.

### Claim 3: The post's prose says the tool highlights "ten common patterns," but the shipped tool's source code implements twelve distinct named pattern detectors
- **Evidence**: Direct comparison of the post's text ("ten common patterns") against the `patterns` array in the tool's own JavaScript source, fetched and read directly from `tools.simonwillison.net/llm-cliche-highlighter`.
- **Confidence**: settled (verified by reading the shipped source code, not inferred)
- **Quote**: "so I had Fable 5 vibe code up this app for highlighting ten common patterns that show up in that sort of writing"
- **Our assessment**: This is a minor but concrete internal inconsistency worth flagging for guide purposes: the number in the announcement prose does not match the number of pattern objects actually shipped in the code (twelve: `no-chain`, `whole`, `did-not-chain`, `dont-verb-it`, `sit-with`, `already-know`, `is-the-entire`, `the-entire-is`, `is-real`, `punchline`, `worth-naming`, `not-nothing` — full list in Concrete Artifacts). This does not rise to a corpus-level contradiction (no other source note makes a competing claim about pattern count) and doesn't affect any guide recommendation, so no contradiction issue was filed per MINER.md §4a — it's noted here only as a caution against citing "ten patterns" as a fact without checking the source, and as a small illustration that even a single-author vibe-coded tool's own description can drift from what it actually ships.

### Claim 4: Three named cliché patterns are given as the post's own representative examples: "no X, no Y" chains, "sit with that," and "you already know"
- **Evidence**: Direct quote from the post's dek/summary line (the description shown under the "Tool" post-type heading).
- **Confidence**: settled (direct quote of the author's own summary)
- **Quote**: "identify patterns like \"no X, no Y\" chains, \"sit with that,\" \"you already know,\" and other LLM-generated expressions"
- **Our assessment**: These three are Willison's own chosen headline examples out of the twelve implemented; the tool's actual pattern list (Concrete Artifacts) also includes less-famous entries like "The punchline is," "That's not nothing," and "Is real … and / not." A guide callout quoting "cliché examples" should draw from the full twelve, not just these three, to avoid under-representing what the tool actually detects.

### Claim 5: Each pattern is implemented as a deterministic hand-written regular expression (or a small regex-chain-counting function), not as an LLM-based classifier
- **Evidence**: Direct reading of the tool's JavaScript source — every entry in the `patterns` array has a `find` function built from either `makeRegexFinder(regex)` or `makeChainFinder(...)`, both of which operate purely on `String.raw` regex literals with no model API calls in the detection path.
- **Confidence**: settled (verified directly from source code, not inferred from the blog post's prose, which does not mention the implementation approach at all)
- **Quote**: (no direct quote from the post; verified in the tool's own source — see Concrete Artifacts for the `makeChainFinder`/`makeRegexFinder` code)
- **Our assessment**: This is the most guide-relevant technical fact in the source and is absent from the blog post's own text — the post frames this as an LLM-adjacent tool ("vibe coded," "LLM-generated writing") but the actual cliché-detection mechanism is old-fashioned regex pattern matching, with the LLM's role confined to having written that regex code during development. This is a useful concrete example of a broader pattern worth naming for the guide: an LLM (Fable 5) was used to *build* a deterministic, auditable, non-LLM detector, rather than to *be* the detector at runtime — trading generality for reproducibility, zero runtime cost, and an inspectable rule set.

### Claim 6: The regex patterns include explicit hand-tuned exclusions to suppress specific known false positives
- **Evidence**: Direct reading of the tool's source code — e.g. the `is-real` pattern's regex explicitly excludes matches followed by "estate," "time," "life," "world," or "quick" (to avoid flagging "real estate," "real time," etc.), and the `worth-naming` pattern excludes "naming names."
- **Confidence**: settled (verified directly from source code)
- **Quote**: (no direct quote from the post; verified in source — see Concrete Artifacts)
- **Our assessment**: This is a concrete, reusable design lesson for anyone building similar lexical-pattern detectors: naive phrase matching produces false positives on common non-clichéd usage, and the fix demonstrated here is a short explicit denylist embedded directly in the regex rather than a separate filtering pass. Small and mundane, but exactly the kind of detail that's invisible from the announcement post and only recoverable by reading the shipped code.

### Claim 7: The tool can analyze arbitrary external URLs (not just pasted text) by fetching the page through the Jina Reader proxy (`r.jina.ai`), with a direct fetch racing in parallel as a fallback
- **Evidence**: Direct reading of the tool's source code and its UI copy.
- **Confidence**: settled (verified directly from source code and the visible input placeholder text)
- **Quote**: "https://example.com/article — fetched via r.jina.ai" (input placeholder text, tool UI)
- **Our assessment**: This is a practical, reusable integration pattern already implicitly present elsewhere in this corpus's discussion of the Jina Reader proxy as a way to get plain-text content from arbitrary URLs without a scraping pipeline, applied here specifically to make the highlighter usable directly against any published article, not just text the user manually copies in.

### Claim 8: The tool ships with an embedded self-test suite (assertions over expected pattern hits/misses on hand-written sample sentences), runnable headlessly via a documented Node.js one-liner
- **Evidence**: Direct reading of the tool's HTML/JS source — a `<footer class="test-footer">` section with a documented `node -e '...'` command that extracts and evaluates the code between marker comments, plus dozens of `test(...)` calls with `expectEqual` assertions against a `patternCases` array of example sentences and expected match counts.
- **Confidence**: settled (verified directly from source code)
- **Quote**: "Run these headlessly with Node: the one-liner below reads this file on stdin, extracts the code between the "impl" and "tests" start/end marker comments in the script, eval()s it, and prints a pass/fail tally."
- **Our assessment**: For a single-file, no-build-step vibe-coded tool, embedding both the implementation and its test suite in one static HTML file — with a documented one-liner to run the tests outside the browser — is a lightweight but genuine testing discipline. This is a concrete, small-scale counterexample to any guide narrative that vibe-coded single-session tools necessarily ship untested; here testing was included as part of the same build, not bolted on afterward.

### Claim 9: The tool's built-in "Load example" text is deliberately constructed so that every one of the twelve patterns fires exactly once (with the sole exception of two clichés sharing a single flagged sentence)
- **Evidence**: Direct reading of the tool's source code — the `EXAMPLE` constant (a short multi-paragraph passage packed with instances of each cliché) and a self-test named "example text trips every pattern exactly once" that asserts this property against the live pattern list.
- **Confidence**: settled (verified directly from source code, including the self-test that mechanically enforces this property)
- **Quote**: (no direct quote from the blog post; the `EXAMPLE` text and its self-test are verified directly from source — see Concrete Artifacts)
- **Our assessment**: This is a nice small piece of craftsmanship — the demo text doubles as a regression check (if a future pattern edit stops firing on the example, or an unrelated pattern starts double-firing, the self-test catches it), meaning the "click here for an example" convenience feature is simultaneously part of the test suite rather than a separate, driftable artifact.

## Concrete Artifacts

### Full post text (verbatim, simonwillison.net/2026/Jul/17/llm-cliche-highlighter/)

```
Tool

LLM cliché highlighter

Detect and highlight common clichéd phrases in text that frequently appear
in language model outputs. Paste text into the analyzer to identify
patterns like "no X, no Y" chains, "sit with that," "you already know,"
and other LLM-generated expressions, with toggleable pattern detection
and context-aware sentence highlighting.

I got frustrated reading yet another article that was crammed with the
clichés of LLM-generated writing - "no fluff, no filler, no jargon" type
stuff - so I had Fable 5 vibe code up this app for highlighting ten
common patterns that show up in that sort of writing.

Posted 17th July 2026 at 12:11 pm
Tags: tools, ai, generative-ai, llms
```

### The twelve shipped pattern detectors (verbatim `name`/`description` fields, from the tool's own source at tools.simonwillison.net/llm-cliche-highlighter, fetched 2026-07-23)

```
id: no-chain          name: "No X, no Y" chains
  desc: Two or more "no …" items in a row, e.g. "No fluff, no filler, no
  jargon." The badge counts the "no" items.

id: whole              name: "That's the whole …"
  desc: "That / this is the whole point, game, thing …"

id: did-not-chain      name: "Did not X, did not Y" chains
  desc: Two or more "did not …" or "didn't …" items in a row. The badge
  counts the items.

id: dont-verb-it       name: "Don't VERB it … VERB it"
  desc: "Don't call it X. Call it Y." — a negated verb + "it", then the
  same verb + "it" again.

id: sit-with           name: "Sit with that"
  desc: The reflective "sit with that / this / it (for a moment)", plus
  "sit with the discomfort" and friends.

id: already-know       name: "You already know"
  desc: "You already know" — the answer, what to do, or standing alone
  before a full stop.

id: is-the-entire      name: "Is the entire …"
  desc: "X is the entire point / game / business model."

id: the-entire-is      name: "The entire … is"
  desc: "The entire point / game / business model is …" — the flipped
  twin of "is the entire".

id: is-real            name: "Is real … and / not"
  desc: "The X is real, and / not …", including "is the real … and it".
  Skips "real estate", "real time", and similar.

id: punchline          name: "The punchline is"
  desc: "The punchline is …", "the punchline:", or "the punchline?".

id: worth-naming       name: "Worth naming"
  desc: The therapist-voiced "that loss is real and it's worth naming",
  "it's worth naming that …", or a "Worth naming:" opener. Skips
  "naming names".

id: not-nothing        name: "That's not nothing"
  desc: "That is not nothing" / "that's not nothing", plus the
  "this / it / which is not nothing" variants.
```

### Implementation approach (verbatim comment + finder signature, from source)

```
// Each pattern: { id, name, description, find(text) -> [{ start, end, badge?, badgeTitle?, count? }] }
// Add new patterns to this array and they get a checkbox, per-pattern count,
// and highlighting for free.
// makeChainFinder builds a detector for "HEAD X, HEAD Y, ..." lists and counts
// the items; makeRegexFinder wraps a plain regex (must use the g flag).
```

### The self-tripping example text (verbatim `EXAMPLE` constant, from source)

```
We rebuilt the editor from the ground up. No sign-ups, no downloads, no
hassle — just paste your text and start writing. Everything runs locally
in your browser.

The reviewer read the draft twice. Did not flinch, did not blink, did not
reach for the red pen. That's the whole review, honestly.

Don't call it a rewrite — call it a rescue. The improvement is real, and
it's not subtle. That loss is worth naming. Sit with that for a moment.
The gains were modest, but that's not nothing.

You already know the answer, of course. Consistency is the entire game,
and the punchline is that nobody wants to hear it. The entire pitch is
one sentence long.

This closing paragraph is deliberately ordinary, with no list patterns at
all, so nothing here should light up.
```

### Self-test runner (verbatim, from source)

```
node -e 's=require("fs").readFileSync(0,"utf8");cut=n=>s.split(`// ==== ${n} start ====`)[1].split(`// ==== ${n} end ====`)[0];eval(cut("impl")+cut("tests")+`let f=0;for(const t of selfTests){try{t.fn()}catch(e){f++;console.log("FAIL "+t.name+": "+e.message)}}console.log((selfTests.length-f)+" passed, "+f+" failed");process.exitCode=f?1:0`)' < llm-cliche-highlighter.html
```

## Cross-References

- **Corroborates**: `blog-simonwillison-rss-vibe-coded-apps.md` Claim 1 (vibe-coding
  accelerates release cadence to blog-post-like speed) — this tool is another
  instance of the same practice: built, shipped, and announced in a single ~90-word
  post the same day, with no separate development writeup.
- **Corroborates**: `blog-simonwillison-claude-fable-5.md` (multiple claims document
  Willison using Fable 5 for real development work, e.g. Claim 6's autonomous
  MicroPython-to-CPython-WASM upgrade and Claim 7's LLM 0.32a3 pause/resume
  implementation). This source adds a smaller, single-session example of the same
  author/model pairing being used for a disposable single-purpose tool rather than a
  larger project.
- **Contradicts**: None identified.
- **Extends**: None directly — this corpus has no prior note on LLM-writing-cliché
  detection to extend.
- **Novel**: This is the first source in this corpus that addresses detection of
  clichéd/formulaic phrasing in LLM-generated text as a concrete, working artifact
  (checked via grep across all existing `source-notes/*.md` for cliché-adjacent
  terminology — no prior note covers this). Specifically novel: (1) the twelve named
  pattern categories and their regexes as a reusable "known LLM tells" reference list;
  (2) the design choice to detect clichés with deterministic regex rather than a
  second LLM call; (3) the false-positive-suppression technique (explicit exclusion
  lists embedded in the regex, e.g. "real estate" skipped by the `is-real` pattern);
  (4) the embedded, headlessly-runnable self-test suite as a lightweight testing
  pattern for single-file vibe-coded tools.

## Guide Impact

- **Chapter 03 (Verification)**: Add the twelve named cliché patterns (Concrete
  Artifacts) as a concrete "known LLM writing tells" checklist for human reviewers
  skimming LLM-generated prose (documentation, PR descriptions, blog content) for
  low-effort or unedited output — citing Claim 4's headline three plus the full
  twelve-pattern list, with the caveat from Claim 3 that the author's own "ten
  patterns" framing undercounts what's actually implemented.
- **Chapter 01 (Daily Workflows) or Chapter 03 (Verification)**: Cite Claim 5 (regex
  detection, not a second LLM call) and Claim 6 (hand-tuned false-positive
  exclusions) as a specific, reusable example of the "use an LLM to build a
  deterministic checker, then run the checker for free" pattern — relevant to any
  guide discussion of when to reach for a classifier LLM call versus a cheap
  rule-based check for a well-defined, enumerable text pattern.
- **Chapter 04 (Context Engineering) or wherever vibe-coding practice is discussed**:
  Add Claim 8 (embedded, headlessly-runnable self-test suite in a single-file
  vibe-coded tool) as a small concrete counterexample to a narrative that
  single-session vibe-coded tools are necessarily untested — pair with
  `blog-simonwillison-rss-vibe-coded-apps.md`'s existing coverage of the vibe-coding
  release-cadence pattern.

## Extraction Notes

- The post itself is very short (~90 words) — the Prospector's triage comments
  (three separate passes, with novelty ratings ranging from "low" to "high") flagged
  this tension explicitly: thin as a written essay, but backed by a working,
  inspectable artifact. This note follows the third and most specific triage comment's
  guidance to extract the tool's concrete pattern list as the primary payload, while
  also independently reading the tool's actual source code (not just the blog post)
  to verify claims rather than relying on the post's prose descriptions.
- WebFetch's summarizer declined to reproduce the blog post's full text verbatim
  (citing copyright policy on lengthy reproduction), consistent with the pattern
  already noted in other corpus extractions of this and other blogs. Per MINER.md
  §2a, no paraphrased WebFetch output was used for quotes. The full post text was
  instead retrieved via a direct `curl` fetch of the live HTML, with tags stripped and
  entities decoded, and re-verified as plain text (fetched 2026-07-23).
- The tool itself (`tools.simonwillison.net/llm-cliche-highlighter`) was also fetched
  directly via `curl` and read in full — this is a single self-contained HTML file
  with inline `<script type="module">` JavaScript, not a separate repo, so "following
  a linked page" here meant reading the tool's own shipped source rather than a
  separate documentation page. This is the source for Claims 3, 5, 6, 7, 8, and 9 and
  for all of the Concrete Artifacts except the post text itself; none of it is
  described in the blog post's prose, which only names three of the twelve patterns
  and gives no implementation detail.
- No GitHub repository or separate source-code link was found for the tool; it
  appears to be a single static HTML file hosted directly under
  `tools.simonwillison.net`, consistent with Willison's `tools.simonwillison.net`
  subdomain pattern for hosting individual vibe-coded utilities (seen elsewhere in
  this corpus, e.g. via `blog-simonwillison-rss-vibe-coded-apps.md`).
- Cross-reference claims verified by direct re-reading of
  `blog-simonwillison-rss-vibe-coded-apps.md` (Claim 1) and
  `blog-simonwillison-claude-fable-5.md` (Claims 6-7) before citing them, and by
  grepping all existing `source-notes/*.md` files for cliché/writing-tell-adjacent
  terminology to confirm no prior note covers this topic (see Novel, above).
- Confidence rated "anecdotal" overall: the tool's own contents (pattern list,
  implementation approach, self-tests) are settled/verified facts about a piece of
  software, but the source's only claim of general interest — that these patterns are
  common and annoying in LLM-generated writing — is a single author's stated
  motivation, not a measured or corroborated finding. No claim in this note rises
  above anecdotal on the "are these clichés actually prevalent/harmful" question; the
  settled-confidence claims here are settled only in the narrow sense of "this is
  what the shipped code does," not "this is true of LLM output generally."
