---
source_url: https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/
source_type: blog-post
title: "Rewriting Bun in Rust"
author: Simon Willison
date_published: 2026-07-08
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1811"
---

# Rewriting Bun in Rust

> Simon Willison's link-blog curation of Jarred Sumner's Bun Zig-to-Rust rewrite
> post, contributing an explicit callback to Joel Spolsky's "never rewrite"
> rule, a named "conformance suites" taxonomy for language-independent test
> suites used to validate cross-language ports, and two verbatim primary-source
> quotes not previously captured in the corpus — while the underlying case
> study facts (cost, scale, harness design) are already documented in more
> depth elsewhere.

## Source Context

- **Type**: blog-post (Simon Willison link-blog post / "blogmark," July 8, 2026,
  posted 11:57pm). A short curation piece: roughly 500 words of Willison's own
  commentary interleaved with five blockquoted excerpts from the primary
  source. Tagged `ai`, `rust`, `zig`, `generative-ai`, `llms`,
  `ai-assisted-programming`, `anthropic`, `bun`, `conformance-suites`,
  `agentic-engineering`, `claude-mythos-fable`.
- **Author credibility**: Simon Willison is the creator of Django and one of
  the highest-signal independent AI tooling commentators (see author-credibility
  discussion in `blog-simonwillison-not-locked-in.md` and dozens of other corpus
  notes). This post is explicitly secondary curation, not first-hand reporting:
  Willison did not do the rewrite or interview Sumner; he read and reacted to
  Sumner's own post at `bun.com/blog/bun-in-rust` (linked "via" Hacker News
  discussion `news.ycombinator.com/item?id=48837877`). His value-add here is
  editorial framing and cross-linking to his own long-running "conformance
  suites" tag taxonomy (11 posts), not new first-party facts about the rewrite.
- **Scope**: Covers Willison's own reaction and five blockquoted excerpts from
  Sumner's primary post: (1) the "programming language choice was a one-way
  decision" framing and why Rust was chosen for memory safety, (2) the
  TypeScript test suite acting as a conformance suite, (3) the "how do you
  review a PR with +1 million lines added" methodology summary, (4) the
  production deployment in Claude Code v2.1.181, (5) the $165,000 token cost.
  Does NOT cover: the harness staffing ratio (implementer/reviewer/fixer),
  the 19 regressions and their root cause, per-platform test counts, the trial
  runs and false starts, or any of the deeper mechanics — all of which are
  already extracted in `blog-pragmaticengineer-bun-rust-rewrite.md` directly
  from the same primary source.

## Extracted Claims

### Claim 1: Willison frames the Bun rewrite as evidence that coding agents have overturned the industry-standard "never do a full rewrite" rule articulated by Joel Spolsky in April 2000

- **Evidence**: Willison's own editorial framing, with a direct citation and
  link to Spolsky's specific 2000 essay by name.
- **Confidence**: emerging (single high-signal commentator's framing, backed by
  a verifiable, specific historical citation and one large concrete example)
- **Quote**: "Everyone knows you should never stop the world and rewrite a large piece of software from the ground up. Joel Spolsky highlighted that in Things You Should Never Do, Part I back in April 2000! Coding agents powered by today's frontier models change that equation."
- **Our assessment**: This is a genuinely new framing device for the corpus:
  no existing source note names Spolsky's essay as the specific conventional
  wisdom being challenged by AI-driven rewrites. It gives the guide a citable
  historical anchor point ("the rule everyone knows") to contrast against the
  growing pile of corpus rewrite case studies (Bun, the NAB Assembly migration
  in `blog-cursor-nab-legacy-migration.md`, the React Native rewrite in
  `blog-simonwillison-not-locked-in.md`). It is still a single commentator's
  framing, not a settled industry consensus — one large successful rewrite
  does not refute a 25-year-old heuristic on its own, and the guide should
  treat this as a "the exception may be swallowing the rule" observation
  rather than "the rule is dead."

### Claim 2: A crucial enabling factor for the rewrite was that Bun's TypeScript test suite was language-independent, letting it function as what Willison categorizes as a "conformance suite" — a recurring pattern he has tracked across 11 tagged posts

- **Evidence**: Willison's own tag taxonomy page (`simonwillison.net/tags/conformance-suites/`),
  which defines the term and lists 11 posts tagged with it as of this
  extraction, including this one, "Ladybird adopts Rust, with help from AI"
  (a distinct Willison post that is NOT yet mined in the corpus — do not
  confuse it with `blog-simonwillison-andreas-kling.md`, which is a
  *different* Kling post covering Ladybird's PR-acceptance governance
  policy, not the Rust/LibJS port referenced by this tag entry), "Scaling
  long-running autonomous coding," and "twitter-text-conformance."
- **Confidence**: emerging (a named, multi-instance pattern tracked by a
  high-signal author over time, but the taxonomy itself is Willison's own
  editorial category, not a third-party-validated engineering term)
- **Quote**: "A crucial enabling factor for the rewrite was that the Bun test suite was written in TypeScript, which meant it could act as a conformance suite."
- **Quote (tag definition, from the conformance-suites tag page)**: "Test suites that are designed to be run against different implementations of the same protocol or standard to help ensure they are compatible with each other."
- **Our assessment**: This is the most useful novel contribution of this
  source. It names a general pattern — a test suite written independently of
  the implementation language, that can validate a rewrite in a *different*
  language — as a recurring, trackable enabler across at least 11 cases
  Willison has documented (not just Bun). The existing corpus documents the
  Bun instance of this pattern in depth (`blog-pragmaticengineer-bun-rust-rewrite.md`
  Claim 8, "100% of Bun's test suite passed in CI on all platforms") but does
  not name it as a generalizable category with a track record beyond this one
  project. For the guide, this reframes "have a big test suite" as a specific,
  named precondition ("is your test suite implementation-independent?") worth
  checking before attempting an AI-driven cross-language rewrite.

### Claim 3: Sumner's own summary of how to review and merge a rewrite with over one million lines of LLM-authored code changed is: a language-independent test suite with a million assertions, adversarial code review, and fixing the generating process rather than hand-fixing bad output

- **Evidence**: Direct blockquote from the primary source (bun.com/blog/bun-in-rust),
  reproduced by Willison, that is not verbatim-quoted in
  `blog-pragmaticengineer-bun-rust-rewrite.md` (that note covers the same
  underlying facts — the adversarial review harness in its Claim 7, and
  process-fixing over hand-fixing in its Claim 9 — via different quoted
  passages from the same primary source).
- **Confidence**: settled (first-party practitioner's own summary of his
  methodology, corroborated in mechanism by the deeper extraction already in
  the corpus)
- **Quote**: "How do you review a PR with +1 million lines added? How do you start to build the confidence needed to responsibly merge large quantities of LLM-authored code? A language-independent test suite with a million assertions, adversarial code review and when something does go wrong, fixing the process that generates the code instead of hand-fixing the code."
- **Our assessment**: This is a tight, quotable three-part summary of the
  entire risk-mitigation methodology (test-suite validation, adversarial
  review, process-level fixes) in Sumner's own words. It's valuable to the
  guide precisely because it's a compact restatement — the corpus already has
  the underlying mechanics in far more granular detail via
  `blog-pragmaticengineer-bun-rust-rewrite.md` (Claims 7-9), but this
  three-clause formulation is a better pull-quote for a guide callout than
  reconstructing the same idea from the more detailed claims.

### Claim 4: Willison assesses the rewrite overall as "an extremely sophisticated piece of agentic engineering," explicitly naming dynamic workflows, trial runs, and adversarial review as its component techniques

- **Evidence**: Willison's own editorial assessment, stated as a direct verdict
  after reading the full primary source.
- **Confidence**: anecdotal (one commentator's qualitative judgment; not a
  metric or reproducible measurement)
- **Quote**: "Honestly, it was worth the wait. This is a detailed description of an extremely sophisticated piece of agentic engineering, featuring dynamic workflows, trial runs, adversarial review and all sorts of other interesting tricks."
- **Our assessment**: This is curatorial endorsement rather than new evidence
  — Willison is vouching for the primary source's substance to his readership,
  not adding a new fact. Useful only as corroborating authority that a
  high-signal, technically literate commentator considers the underlying
  Sumner post worth the attention the corpus has already given it via
  `blog-pragmaticengineer-bun-rust-rewrite.md` and
  `blog-anthropic-dynamic-workflows-claude-code.md`.

### Claim 5: Willison frames the entire episode as a case study in "taking on wildly ambitious projects with the help of coordinated parallel agents"

- **Evidence**: Willison's closing editorial line, summarizing the takeaway he
  wants readers to draw from the post.
- **Confidence**: anecdotal (single commentator's closing framing)
- **Quote**: "This whole thing is a fascinating case study in taking on wildly ambitious projects with the help of coordinated parallel agents."
- **Our assessment**: This is a generalization move — from "Bun did this one
  rewrite" to "this is a template for wildly ambitious projects in general."
  It is the kind of framing that risks overreach (one successful project is
  not proof the pattern generalizes to other ambitious projects with different
  risk profiles, e.g. ones lacking Bun's pre-existing million-assertion test
  suite), and the guide should pair this framing with the precondition named
  in Claim 2 (an implementation-independent conformance suite) rather than
  presenting "coordinated parallel agents" alone as sufficient for ambitious
  rewrites.

## Concrete Artifacts

### Full blogmark text (verbatim, simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/)

```
Source: https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/
Posted: 8th July 2026 at 11:57 pm
Tags: ai, rust, zig, generative-ai, llms, ai-assisted-programming, anthropic,
      bun, conformance-suites, agentic-engineering, claude-mythos-fable

Rewriting Bun in Rust (via) Jarred Sumner has been promising this blog post
(since May 9th) about his Zig to Rust rewrite of Bun for significantly longer
than it took him to finish the rewrite.

Honestly, it was worth the wait. This is a detailed description of an
extremely sophisticated piece of agentic engineering, featuring dynamic
workflows, trial runs, adversarial review and all sorts of other interesting
tricks.

Jarred spends the first half of the post praising Zig for getting Bun this
far. Then we get to a core idea in the piece, emphasis mine:

  Our bugfix list felt bad and I was tired of going to sleep worrying about
  crashes in Bun. I don't blame Zig for that - other users of Zig don't have
  the bugs we had, and mixing GC with manually-managed memory is an uncommon
  enough thing for software to need that no language really designs for it.
  We wouldn't have gotten this far if not for Zig, and I'll always be
  grateful. Until very recently, programming language choice was a one-way
  decision for a project like Bun. [emphasis Willison's]

Everyone knows you should never stop the world and rewrite a large piece of
software from the ground up. Joel Spolsky highlighted that in Things You
Should Never Do, Part I back in April 2000!

Coding agents powered by today's frontier models change that equation.

Why pick Rust? It all came down to those challenges with memory management:

  A large percentage of bugs from that list are use-after-free, double-free,
  and "forgot to free" in an error path. In safe Rust, these are compiler
  errors and RAII-like automatic cleanup with Drop.

A crucial enabling factor for the rewrite was that the Bun test suite was
written in TypeScript, which meant it could act as a conformance suite. This
allowed an agent harness to automate much of the initial port from Bun to
Rust, initially as an experiment to try out an earlier version of the model
we now have access to as Mythos/Fable.

  At first, I didn't expect it to work. A few days in, a high % of the test
  suite started passing and I saw how much the new Rust code matched up with
  the original Zig codebase. My opinion went from "this is worth trying" to
  "I'm going to merge this". [...]

  For most of those 11 days (and after), I monitored workflows - manually
  reading the outputs to check for issues and bugs, and prompting Claude to
  edit the loop to fix things.

  How do you review a PR with +1 million lines added? How do you start to
  build the confidence needed to responsibly merge large quantities of
  LLM-authored code?

  A language-independent test suite with a million assertions, adversarial
  code review and when something does go wrong, fixing the process that
  generates the code instead of hand-fixing the code.

The new implementation of Bun has been live in Claude Code for nearly a month
now:

  Claude Code v2.1.181 (released June 17th) and later use the Rust port of
  Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed.
  Boring is good.

A perk of working at Anthropic is that you don't have to pay for your tokens -
handy when the estimated cost is $165,000!

  Pre-merge, this took 5.9 billion uncached input tokens, 690 million output
  tokens, and 72 billion cached input token reads — around $165,000 at API
  pricing.

This whole thing is a fascinating case study in taking on wildly ambitious
projects with the help of coordinated parallel agents.
```

### conformance-suites tag definition (simonwillison.net/tags/conformance-suites/)

```
Source: https://simonwillison.net/tags/conformance-suites/ (fetched 2026-07-13)

Tag description: "Test suites that are designed to be run against different
implementations of the same protocol or standard to help ensure they are
compatible with each other."

11 posts tagged as of this extraction, including (most recent first):
  - Rewriting Bun in Rust (this source, 2026-07-08)
  - Ladybird adopts Rust, with help from AI
    (a distinct Willison post not yet mined in the corpus; NOT the same as
    corpus note blog-simonwillison-andreas-kling.md, which covers a different
    Kling piece about Ladybird's PR-acceptance governance policy, not the
    Rust/LibJS port referenced by this tag entry)
  - Scaling long-running autonomous coding
  - Open Responses
  - A Software Library with No Code
  - twitter-text-conformance
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7 (the adversarial-review
    harness: "1 implementer, 2 or more adversarial reviewers per implementer")
    and Claim 9 (Sumner monitoring workflows and editing the process rather than
    hand-fixing output) — this source's Claim 3 quote ("adversarial code review
    and when something does go wrong, fixing the process that generates the
    code instead of hand-fixing the code") states the same methodology as a
    compact three-part summary, using a different verbatim passage from the
    same primary source than either of those two claims cites.
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 5 ($165,000 total cost;
    5.9B uncached input tokens, 690M output tokens, 72B cached input token
    reads) and Claim 12 (Claude Code v2.1.181, June 17 2026, 10% faster Linux
    startup, "barely anyone noticed") — this source quotes the identical cost
    and production-deployment figures from the same primary source, with no
    numeric discrepancy.
  - `blog-anthropic-dynamic-workflows-claude-code.md` Claim 6 (documents that
    the Bun Zig-to-Rust rewrite was carried out using dynamic workflows) and
    Claim 4 (names "critical work requiring independent attempts and
    adversarial testing" as one of the three primary dynamic-workflows use
    cases) — this source's Claim 4 independently characterizes the same
    rewrite as "featuring dynamic workflows, trial runs, adversarial review,"
    from an external commentator's read of the primary source rather than
    Anthropic's own announcement. (Note: "trial runs" is Willison's own phrase
    from this PR, not a term used in the cited note; the overlap is on
    "dynamic workflows" and "adversarial testing/review.")
- **Extends**: `blog-simonwillison-not-locked-in.md` Claim 5 (Hashimoto:
  "Programming languages used to be LOCK IN, and they're increasingly not
  so," about this same Bun rewrite) — this source supplies the primary
  source's own, differently-worded version of the same lock-in claim, in
  Sumner's own voice rather than Hashimoto's: "Until very recently,
  programming language choice was a one-way decision for a project like
  Bun." This is a second, independent phrasing of the identical underlying
  claim (language choice is no longer effectively permanent), now sourced
  directly to the practitioner who did the rewrite rather than a third-party
  quoting him.
- **Contradicts**: None identified. This source's claims are consistent with
  the existing corpus's numeric account of the rewrite (cost, deployment,
  duration all match `blog-pragmaticengineer-bun-rust-rewrite.md`). It does
  not engage with the 99.8%-vs-100% test-pass-rate discrepancy already flagged
  in that note's Cross-References (issue #1759) — this source does not quote
  either specific test-pass percentage.
- **Novel**:
  - **The Joel Spolsky "Things You Should Never Do, Part I" citation** (Claim
    1) as the specific named conventional wisdom the Bun rewrite is offered as
    evidence against. No existing corpus note on the Bun rewrite, agentic
    rewrites generally, or lock-in cites Spolsky by name or links his essay.
  - **The "conformance suites" taxonomy** (Claim 2) as a named, multi-instance
    pattern Willison has tracked across at least 11 posts — reframing "a big
    test suite helped" from a one-off observation about Bun into a
    generalizable, checkable precondition ("is the test suite
    implementation-independent?") for attempting a similar AI-driven
    cross-language rewrite.
  - **The compact three-clause methodology quote** (Claim 3: test suite +
    adversarial review + fix-the-process) as a citable pull-quote distinct
    from the more granular claims already extracted from the same primary
    source elsewhere in the corpus.

## Guide Impact

- **Chapter 05 (Large-Scale Refactoring and Migrations)**: Add the Joel
  Spolsky "Things You Should Never Do, Part I" citation as the guide's
  explicit historical foil when discussing AI-driven full rewrites — framing
  the chapter's advice as "the 2000-era heuristic against full rewrites is
  being renegotiated by agentic engineering, evidenced by cases like Bun, not
  simply discarded." Add the "conformance suites" concept as a named
  precondition checklist item: before attempting an AI-driven cross-language
  port, check whether an implementation-independent test suite already exists
  (as Bun's TypeScript suite did) — this is a more specific, actionable framing
  than "have good test coverage." Cite this source's Claim 3 three-clause
  quote as a compact pull-quote alongside the deeper mechanics already sourced
  from `blog-pragmaticengineer-bun-rust-rewrite.md`.
- **Chapter 02 (Workflows)**: No new mechanism to add beyond what
  `blog-anthropic-dynamic-workflows-claude-code.md` and
  `blog-pragmaticengineer-bun-rust-rewrite.md` already document; this source
  is corroborating, not extending, on workflow mechanics.

## Extraction Notes

- This source is a short link-blog post (~500 words), read in full via raw
  HTML (`curl`) rather than the WebFetch summarizer, specifically so that
  every quoted passage above could be verified character-for-character
  against the live page (fetched 2026-07-13).
- One linked page was followed per MINER.md §1: the `conformance-suites` tag
  page (`simonwillison.net/tags/conformance-suites/`), which is directly
  cited inline in the source's own text as the definitional anchor for its
  central technical claim (test suite as conformance suite). This tag page
  was substantive enough to warrant its own Concrete Artifacts entry and
  Claim 2 above. The other two outbound links in the post — the Hacker News
  discussion (`news.ycombinator.com/item?id=48837877`) and Jarred Sumner's
  X/Twitter post announcing the upcoming write-up — were not followed: the HN
  discussion is a separate discussion-type source out of scope for this
  text-source extraction, and the X post predates the rewrite's completion
  and contains no technical content per Sumner's own May 9th teaser framing.
  The primary source itself (`bun.com/blog/bun-in-rust`) was not re-extracted
  in full here since it is already deeply mined in
  `blog-pragmaticengineer-bun-rust-rewrite.md` (issue #1741); this note
  focuses on what Willison's curation specifically adds beyond that existing
  extraction, per the Prospector's second triage comment on this issue.
- The Prospector filed two triage comments on this issue with different
  novelty assessments (first: "high," treating this as if it were the primary
  case study; second: "low-medium (incremental)," correctly identifying this
  as Willison's secondary curation of an already-mined primary source, since
  the URL is `simonwillison.net`, not `bun.com`). This note follows the
  second, more accurate assessment: the confidence_overall rating (emerging)
  and the modest guide-impact recommendations above reflect that most of the
  substantive case-study content is already in the corpus at greater depth,
  and this source's real contribution is Claims 1-3 (the Spolsky citation, the
  conformance-suites taxonomy, and the compact methodology quote).
