---
source_url: https://openai.com/index/cognition-devin-testing-with-astra
source_type: blog-post
title: "Cognition helps Devin test its own work with GPT‑6 Astra"
author: OpenAI
date_published: 2026-09-11
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: anecdotal
issue: "#3631"
---

# Cognition helps Devin test its own work with GPT‑6 Astra

> OpenAI's short partnership/customer-story post naming GPT‑6 Astra as the
> model behind Devin's self-testing: a two-artifact (recording + report)
> testing output pattern illustrated with a real customer app ("Otter Run,"
> an iPhone game), a screenshot-in/screenshot-out bug-fix workflow, and
> Cognition's stated bet that stronger self-verified testing will reduce how
> much code its engineers manually review over time — all sourced to a
> single named individual (Walden Yan, Cognition co-founder) with no
> benchmark data or architecture detail.

## Source Context

- **Type**: blog-post (OpenAI's `openai.com/index/` customer-story/product
  vertical, published 2026-09-11 per the source issue's RSS metadata — the
  page itself carries no visible byline or dateline beyond that feed
  timestamp). Structurally a short partnership testimonial piece: two named
  section headings ("Testing software and showing the results," "Working
  toward less manual code review"), two pull-quotes, no benchmark tables,
  no code samples, no named model comparison.
- **Author credibility**: House-authored OpenAI customer-story content, no
  individual OpenAI author credited. All substantive claims in the piece are
  attributed to a single named source: Walden Yan, identified as
  "Co-founder, Cognition" — i.e., this is OpenAI publishing its partner's
  own characterization of its own product, with an obvious mutual
  promotional interest (OpenAI showcasing a flagship customer's use of
  GPT‑6 Astra; Cognition getting a customer-facing endorsement from a
  frontier lab). No numbers, benchmark scores, or independently-verifiable
  claims appear anywhere in the piece.
- **Scope**: Covers, at a high level: why Cognition cares about
  Astra-powered testing (code review has become the bottleneck as
  engineering teams write more code), which Devin surfaces it has been
  applied to (the "core cloud agent," CLI, and desktop products), one
  concrete example (testing an iPhone game, "Otter Run," producing a
  simulator recording plus a pass/untested report), a screenshot-bug-report
  → screenshot-fix workflow, and Cognition's stated long-term goal (less
  manual code review, more shipped work). Does **not** cover: how Astra's
  testing capability differs mechanically from the computer-use testing
  architecture Cognition already documented in
  `blog-cognition-verifying-agentic-development.md` (test-plan generation,
  annotation, deterministic "skills," failure modes) — this post does not
  mention test plans, annotations, skills, or any of that architecture by
  name; any benchmark, cost, reliability, or accuracy figure for
  Astra-powered testing specifically; how Astra was selected over other
  models for the testing role, or whether Astra replaced a different model
  Devin previously used for testing; or any detail about Otter Run beyond
  its name and platform (iPhone game).

## Extracted Claims

### Claim 1: Cognition frames GPT‑6 Astra's central testing contribution as its ability to test its own work and prove — not just assert — that the result functions as expected
- **Evidence**: Direct pull-quote from Walden Yan, positioned as the post's
  lead claim immediately after the opening framing paragraph.
- **Confidence**: anecdotal (a single named executive's characterization,
  no supporting measurement of "prove" vs. a prior, weaker verification
  standard)
- **Quote**: "One of the big pieces that Astra improves on is its ability to test and prove that its work actually functions the way you expect."
- **Our assessment**: This is a direct, if unquantified, restatement of the
  same self-verification thesis `blog-cognition-verifying-agentic-development.md`
  documents in depth (that source's Claims 5-6: test plans and
  in-session annotation exist specifically to make Devin's "pass" claims
  trustworthy rather than self-reported and unverifiable). This post adds
  the model attribution (Astra) that source never named, but supplies no
  mechanism or evidence for *why* Astra specifically improves this over a
  prior model — "improves on" implies a before/after comparison that is
  asserted, not shown.

### Claim 2: Cognition is applying GPT‑6 Astra across its full product surface — not only Devin's cloud agent, but also its CLI and desktop products
- **Evidence**: Direct quote from Yan under "Testing software and showing
  the results."
- **Confidence**: settled (a specific, checkable product-rollout fact,
  low incentive to misstate which of the vendor's own products use a given
  model)
- **Quote**: "We've been using it to make improvements across our product, including the core cloud agent that is Devin, but also our CLI and desktop products," says Yan.
- **Our assessment**: This corroborates and dates forward the CLI/Desktop
  surfaces `blog-cognition-devin-local-fusion.md` documents (that source's
  Claim 10: Fusion, previously cloud-only, shipped to Devin CLI/Desktop on
  Sept 11, 2026 — the same publication date as this post) — together the
  two sources describe the same week's CLI/Desktop push touching both the
  Fusion lead/sidekick harness and Astra-powered testing. Neither source
  states whether Astra-powered testing on CLI/Desktop uses the Fusion
  architecture, or a separate testing-specific model-routing path like the
  one `blog-cognition-verifying-agentic-development.md` Claim 8 describes
  as "experimenting" — that source names no specific model for the testing
  role, so this post is the first in this corpus to attach a name (Astra)
  to Cognition's testing-phase model choice, without confirming it is the
  outcome of that named experiment.

### Claim 3: In one described example, Devin uses Astra to test an iPhone game ("Otter Run") and returns two artifacts: a recording of the game running in a simulator, and a report identifying which checks passed and which areas were left untested
- **Evidence**: Direct descriptive sentence from the post's "Testing
  software and showing the results" section, followed by an explanatory
  sentence on what each artifact is for.
- **Confidence**: anecdotal (a single named example with no detail on the
  underlying test scope, how "checks" were defined or generated, or
  whether this example is representative of typical Devin+Astra testing
  runs)
- **Quote**: "In one example, Devin uses Astra to test Otter Run, an iPhone game, and returns a recording of the game running in a simulator, alongside a report identifying checks that passed and areas left untested." … "The recording shows the application's behavior, while the report documents the scope of the testing. Engineers can use those outputs to inspect how the software works and understand what still needs attention."
- **Our assessment**: This two-artifact output pattern (a recording +
  a scope/pass-fail report) is structurally consistent with, though a
  compressed version of, the two-tier report design already documented in
  `blog-cognition-verifying-agentic-development.md` Claim 10 (labeled
  screenshots for a fast skim, plus a chaptered, scrubbable video with
  dead-time compression for deep review) — this post doesn't specify
  whether the Otter Run recording has the same chapter/compression
  features, so it should be read as corroborating the general shape of
  Devin's test-artifact output (a fast summary plus a deeper-inspection
  artifact) rather than as new detail about the recording format itself.
  The "areas left untested" framing is notable and not present in the
  earlier source: it implies the report explicitly scopes what was *not*
  covered, not just what passed or failed — a specific, useful transparency
  detail for any reviewer deciding whether to trust the test as
  sufficient, though this post gives no example of what an "untested area"
  disclosure actually looks like.

### Claim 4: Astra-powered Devin also speeds up customer bug-fix turnaround via a screenshot-in, screenshot-out workflow: a customer submits a screenshot of a bug, Devin (using Astra) fixes the issue, and returns a screenshot showing the fix
- **Evidence**: Direct quote/paraphrase from Yan under the same section.
- **Confidence**: anecdotal (a described workflow pattern with no data on
  frequency, success rate, or how "much quicker" is measured relative to a
  baseline)
- **Quote**: Astra is "helping Cognition get back to customers 'much quicker,' says Yan. When a customer sends a screenshot of a bug, the team can pass it to Devin using Astra, which fixes the issue and returns a screenshot showing the result."
- **Our assessment**: This is a distinct capability from Claim 3's
  proactive self-testing — it's a reactive, customer-triggered visual
  bug-report → visual-fix-confirmation loop, using the same underlying
  computer-use/screenshot capability but applied to support/triage rather
  than pre-merge verification. No source elsewhere in this corpus documents
  a screenshot-as-bug-report input format specifically (as distinct from a
  written bug description); this is a novel, concrete detail about how
  Devin accepts unstructured visual input for its self-testing/fix loop.

### Claim 5: Cognition's stated strategic bet is that stronger, evidenced self-testing will let engineers manually review less code over time while shipping more overall — framed by Yan as one of the things Cognition is "really excited about" regarding GPT‑6 generally, not Astra specifically
- **Evidence**: Direct closing pull-quote from Yan under "Working toward
  less manual code review," preceded by the post's own framing sentence.
- **Confidence**: anecdotal (a forward-looking expectation, not a measured
  outcome — "we expect over time" is explicitly speculative)
- **Quote**: "We expect over time that we have to manually look at less code and end up shipping more at the end of the day. This is one of the things we're really excited about when it comes to GPT-6."
- **Our assessment**: This is the post's thesis statement and directly
  corroborates the general "verification is the bottleneck" framing already
  in this corpus (`blog-addyosmani-code-agent-orchestra.md` Claim 5,
  restated as a 2026 case study in
  `blog-cognition-verifying-agentic-development.md` Claim 1) — but frames
  the *goal* as reducing human review volume specifically, which is a
  stronger and more specific claim than "verification is the bottleneck":
  it asserts that sufficiently trustworthy automated testing should let
  humans review less, not just review differently or faster. Worth noting
  precisely what's attributed to what: Yan's quote says "when it comes to
  GPT-6" (the model family generally), not "when it comes to Astra"
  specifically, even though the post's headline and preceding paragraphs
  are Astra-specific — a small but real scope gap between the post's frame
  and its own closing quote.

## Concrete Artifacts

```
Source: OpenAI, "Cognition helps Devin test its own work with GPT‑6 Astra,"
https://openai.com/index/cognition-devin-testing-with-astra (accessed via
r.jina.ai reader proxy 2026-09-23; direct fetch returned HTTP 403 with a
Cloudflare bot-challenge, and no Wayback Machine snapshot exists yet for
this specific URL — see Extraction Notes)

Section structure (in order):
1. Opening framing paragraph (code review bottleneck; Astra as one answer)
2. Pull-quote: Walden Yan, Co-founder, Cognition
3. "Testing software and showing the results"
   - product-surface breadth (cloud agent, CLI, desktop)
   - Otter Run example (recording + report)
   - screenshot bug-report -> screenshot fix-confirmation workflow
4. "Working toward less manual code review"
   - Cognition's stated less-review/more-shipping thesis
   - closing pull-quote: Walden Yan, Co-founder, Cognition

Named individual quoted: Walden Yan, Co-founder, Cognition (the only named
source in the piece; no other Cognition or OpenAI individual is quoted or
credited)

Named example application: "Otter Run" (described only as "an iPhone
game" — no further detail on genre, publisher, or codebase given)
```

## Cross-References

### Cross-reference verification notes
`blog-cognition-verifying-agentic-development.md`,
`blog-cognition-devin-local-fusion.md`, `blog-simonwillison-gpt6-astra-launch.md`,
and `blog-ronacher-astra-why.md` were each re-read in full before writing
this section, and every `Claim N` cited below was located and confirmed by
number and content against that note's own text before use, per
MINER.md §4b.

- **Corroborates**:
  - `blog-cognition-verifying-agentic-development.md` Claim 1 (the
    "verification is now the bottleneck" framing that motivated Devin's
    whole self-testing build-out) and Claim 10 (the two-tier
    screenshot-report + chaptered-video test artifact design): this post's
    Claim 5 restates the same bottleneck thesis with a sharper, more
    specific goal (reduce human review volume, not just make review
    faster), and Claim 3's recording+report output pattern is a
    compressed, less-detailed restatement of the same two-artifact design
    that earlier source documents at implementation depth.
  - `blog-cognition-devin-local-fusion.md` Claim 10 (Fusion shipped to
    Devin CLI/Desktop on 2026-09-11, the same publication date as this
    post): this post's Claim 2 (Astra applied across cloud agent, CLI, and
    desktop) independently confirms the same-week CLI/Desktop expansion
    from a different angle (testing capability, not the Fusion
    lead/sidekick harness) — two separate capabilities landing on Devin's
    local surfaces in the same release window.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar.
  One candidate tension was evaluated and rejected: this post's positive
  framing of Astra as reliably proving its own work "functions the way you
  expect" (Claim 1) sits alongside `blog-ronacher-astra-why.md`'s
  extensively documented account (that source's Claims 1-9) of Astra
  producing low-quality "slop" code and requiring more, not less, human
  review on a 35-hour unattended coding run. This does not meet the filing
  bar: the two sources describe different tasks under different conditions
  (this post describes Astra *testing* already-written code within Devin's
  reviewed harness workflow; Ronacher's report describes Astra *writing*
  code unsupervised for 35 hours with no analogous review loop) and neither
  makes a claim that would be falsified by the other under matched
  conditions. This is the same conditioning-variable reasoning
  `blog-cognition-devin-local-fusion.md`'s Cross-References already applied
  to a structurally identical Astra-trustworthiness tension — flagged here
  as a second instance of the same open question (does Astra's
  self-testing/self-review output hold up under Ronacher's specific
  "slop"-generation failure mode?) rather than filed as a new
  contradiction.

- **Extends**:
  - `blog-cognition-verifying-agentic-development.md`: this post is the
    first source in this corpus to name the specific model (GPT‑6 Astra)
    behind Devin's computer-use self-testing capability that earlier post
    described only in architectural terms with no model name attached —
    though see Claim 2's assessment for the gap between "Astra powers
    testing" here and "experimenting with routing the testing phase to
    different models" in that source's Claim 8: this post does not confirm
    whether Astra *is* the outcome of that named experiment or a separate,
    later model swap.
  - `blog-simonwillison-gpt6-astra-launch.md`: that source documents
    Astra's benchmark profile (pricing, Intelligence/Coding Agent Index
    scores, ARC-AGI-3, security benchmarks) with no mention of a
    testing-specific use case; this post supplies exactly the missing
    piece — a named, concrete testing/verification application of Astra —
    without any of the quantified benchmark detail that source provides.

- **Novel**:
  - The explicit naming of GPT‑6 Astra as the model behind Devin's
    self-testing capability — no prior source note in this corpus attaches
    a specific model name to that capability.
  - The screenshot-in/screenshot-out customer bug-fix workflow (Claim 4) —
    not documented in `blog-cognition-verifying-agentic-development.md` or
    any other Cognition source in this corpus.
  - The "areas left untested" disclosure framing in the test report
    (Claim 3) — a specific transparency detail (what was *not* covered, not
    just pass/fail) not previously documented for Devin's test-report
    format.

## Guide Impact

- **Chapter 03 (Verification)**: This post adds only a model attribution
  (Astra) and two small, unquantified workflow details (the "areas left
  untested" disclosure; the screenshot-bug-report intake path) to the
  self-verification architecture already sourced in depth from
  `blog-cognition-verifying-agentic-development.md`. Given the total
  absence of benchmark, accuracy, or comparative data in this post, it
  should be cited only as corroborating evidence that Cognition's
  production self-testing capability is model-attributed to GPT‑6 Astra as
  of September 2026, and as the source for the screenshot-in/screenshot-out
  bug-fix pattern (Claim 4) as a named, concrete instance of using
  computer-use/vision capability for reactive bug triage rather than
  proactive pre-merge testing — not as new evidence for the underlying
  testing architecture itself, which remains better sourced from the
  earlier, more detailed Cognition post.
- No chapter should cite this post's "much quicker" or "less manual code
  review over time" framing (Claims 4-5) as measured outcomes — both are
  explicit, unquantified vendor/partner expectations, not reported results.

## Extraction Notes

- **Live URL returned HTTP 403**: `https://openai.com/index/cognition-devin-testing-with-astra`
  returned an HTTP 403 with a Cloudflare bot-challenge (`cf-mitigated:
  challenge` header, confirmed via both `WebFetch` and a direct `curl` with
  a browser user-agent) — the same access pattern already documented for
  other `openai.com/index/` posts in this corpus (e.g.
  `blog-openai-chatgpt-work-ambitious-partner.md`,
  `blog-openai-gpt56-ga-announcement.md`).
- **No Wayback Machine snapshot available**: unlike the GPT‑5.6 GA
  announcement note, a direct query to the Internet Archive's availability
  API (`archive.org/wayback/available?url=openai.com/index/cognition-devin-testing-with-astra`)
  returned no archived snapshots as of this extraction (2026-09-23, twelve
  days after the post's 2026-09-11 publication) — this specific URL has
  apparently not yet been crawled.
- **Retrieved via r.jina.ai reader proxy**: the full article text (both
  section headings, both pull-quotes, and all body paragraphs) was
  successfully retrieved via `https://r.jina.ai/<source-url>` (a
  read-only HTML-to-markdown reader proxy), including a link-inventory pass
  confirming the article contains no in-body links to substantive related
  content — only site-navigation links and a footer "related posts" list
  (a GPT‑6 Sol/Luna announcement, a prompt-caching post, and a Parallel/AI
  customer story, all dated 2026-09-22 and unrelated to this post's
  Cognition/Astra testing topic). No sub-pages were followed, consistent
  with MINER.md §1's "linked pages that seem substantive" bar — none of the
  footer links are substantive extensions of this specific article.
- **Source is a short, single-source partnership post**: at roughly 300
  words with every substantive claim attributed to one named individual
  (Walden Yan) and no benchmark, metric, or independently-checkable figure
  anywhere in the text, this is one of the thinnest sources in this corpus.
  Five claims were extracted by treating each distinct assertion (testing
  capability, product-surface breadth, the Otter Run example, the bug-fix
  workflow, and the review-reduction thesis) as its own claim; all are
  rated `anecdotal` except Claim 2 (a checkable, low-incentive-to-misstate
  product-surface fact, rated `settled`). Overall confidence is rated
  `anecdotal`: this is vendor-partner testimonial content with no
  quantified or independently verifiable claim of any kind.
- **No contradiction meeting the MINER.md §4a filing bar was identified.**
  The one candidate tension (this post's positive Astra-testing framing vs.
  `blog-ronacher-astra-why.md`'s documented Astra code-quality failures) was
  evaluated and rejected as a conditioning-variable difference — see
  Cross-References → Contradicts for the full reasoning. No contradiction
  issue filed.
- All claim numbers cited from other source notes
  (`blog-cognition-verifying-agentic-development.md` Claims 1, 5, 6, 8, 10;
  `blog-cognition-devin-local-fusion.md` Claim 10;
  `blog-ronacher-astra-why.md` Claims 1-9;
  `blog-addyosmani-code-agent-orchestra.md` Claim 5) were verified by
  re-reading the cited note and locating the numbered heading before
  citing — no claim number was guessed or approximated.
