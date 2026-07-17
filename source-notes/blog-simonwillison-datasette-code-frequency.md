---
source_url: https://simonwillison.net/2026/Jul/13/datasette-code-frequency/
source_type: blog-post
title: "datasette code-frequency chart on GitHub"
author: Simon Willison
date_published: 2026-07-13
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: anecdotal
issue: "#1951"
---

# datasette code-frequency chart on GitHub

> Simon Willison points to GitHub's code-frequency chart for his Datasette project as
> the "best I've found so far" illustration of coding agents' impact on his personal
> output, noting the largest weekly spike in the project's eight-year history (37,022
> additions / -9,528 deletions) lands in 2026 and coincides with the availability of
> Opus 4.8, GPT-5.5, Fable 5, and GPT-5.6 Sol — while explicitly hedging that this is
> the best proxy he's found, not a rigorous one.

## Source Context

- **Type**: blog-post (a "link post" / "beat" in Simon Willison's format — a linked
  GitHub URL, one image, and two sentences of framing prose. This is one of the
  shortest post formats on his blog, distinct from his longer analytical posts.)
- **Author credibility**: Simon Willison is the creator and lead maintainer of
  Datasette (the project the chart describes) and of the `llm` CLI tool. As the
  repository owner, he has first-party knowledge of what drove the commits behind
  the chart, though the post itself offers no commit-level detail — it is a
  observation about an aggregate chart, not a walkthrough of specific PRs or
  sessions.
- **Scope**: Covers only one signal — GitHub's "Code frequency" graph (weekly
  addition/deletion line counts) for one repository (`simonw/datasette`) over
  2018–2026. Does not cover: which specific commits or PRs drove the 2026 spike,
  how much of the added/deleted code was agent-authored versus hand-written,
  review overhead, defect rates, or any other project's chart. Does not distinguish
  net feature progress from refactors, reverts, or generated boilerplate — additions
  and deletions are raw line counts, not judged by intent or durability.

## Extracted Claims

### Claim 1: Willison set out specifically to find a measurable illustration of coding agents' impact on his own coding output, and settled on GitHub's per-repo code-frequency chart as the best one he found
- **Evidence**: First-person statement of intent and method from the repository owner.
- **Confidence**: anecdotal
- **Quote**: "Out of curiosity I decided to see if I could find a useful illustration of the impact of coding agents and Opus 4.5 class models on my own output. The best I've found so far is this GitHub chart of frequency of code changes to my Datasette open source project"
- **Our assessment**: The "best I've found so far" phrasing is an explicit hedge, not a claim of rigor — Willison is not asserting that raw weekly line-change counts are a good productivity metric, only that it's the most legible one he's located. That hedge should travel with any citation of the numbers below; the guide should not upgrade this into a validated measurement methodology.

### Claim 2: The single largest weekly code-change event in Datasette's eight-year GitHub history (2018–2026) is 37,022 additions paired with 9,528 deletions, and it falls in 2026
- **Evidence**: Description of the chart's data points, given in the image's alt text on the published post (machine-readable accessibility description of the screenshotted GitHub chart, not raw API data).
- **Confidence**: anecdotal
- **Quote**: "the largest spike is 37,022 additions with -9,528 deletions in 2026"
- **Our assessment**: This is a real, attributable number from a specific, linkable, and in-principle independently verifiable source (GitHub's `/graphs/code-frequency` page for `simonw/datasette`), which is stronger footing than a purely narrative anecdote. But it is a single week's line-count spike on a single repository — it says nothing about defect rates, review burden, or whether the 37,022 added lines represent durable feature work versus vendored dependencies, generated boilerplate, or agent-driven churn that gets reverted later. See Claim 5 below and `paper-miller-speed-cost-quality.md` for why raw addition spikes specifically should not be read as sustained productivity gains without a multi-month window.

### Claim 3: A second-largest activity spike of 14,638 additions and 6,584 deletions occurred in late 2025, distinct from and smaller than the 2026 peak
- **Evidence**: Same chart alt-text description.
- **Confidence**: anecdotal
- **Quote**: "followed by 14,638 additions with -6,584 deletions in late 2025"
- **Our assessment**: The existence of a second, smaller but still substantial spike roughly 6-12 months before the largest one suggests a step-function pattern of escalating peak activity across 2025-2026 rather than one isolated event. Consistent with a period of successive more-capable model releases each producing a further jump in the ceiling of what Willison could push through the repo in a single week, though the post does not name which models drove the late-2025 spike.

### Claim 4: Willison attributes the 2026 activity spike specifically to the concurrent availability of four named models — Opus 4.8, GPT-5.5, Fable 5, and GPT-5.6 Sol
- **Evidence**: Direct first-person causal attribution from the repository owner, timed to when he observed the spike.
- **Confidence**: anecdotal
- **Quote**: "The big spike in activity at the end aligns with Opus 4.8, GPT-5.5, Fable 5 and GPT-5.6 Sol."
- **Our assessment**: "Aligns with" is a correlation claim, not a causal proof — there is no isolation of which model(s) actually drove which fraction of the additions, and no counterfactual (would the spike have happened with only one of the four models available?). Still, naming four specific, dateable model releases as concurrent with a measurable repo-activity spike is a more falsifiable claim than a vague "AI made me faster" statement, and it is useful as a timestamped data point for correlating model releases with observed practitioner throughput.

### Claim 5: Weekly deletion spikes on the order of thousands of lines occur independent of the current generation of coding agents — a comparable deletion spike (-10,658) occurred in mid-2020, years before agentic coding tools existed
- **Evidence**: Chart alt-text description of the full 2018-2026 history, which includes a large deletion event unconnected to any AI-model release.
- **Confidence**: anecdotal
- **Quote**: "a standout deletion spike of -10,658 in mid-2020"
- **Our assessment**: This is the built-in caution the source itself supplies against over-attributing volume spikes to AI tooling: large refactors and cleanups produced spikes of comparable magnitude to the "AI era" numbers well before any coding agent existed. It weakens (without refuting) Claim 4 — it shows the chart alone cannot distinguish an AI-driven spike from an ordinary large-refactor spike; the "alignment" in Claim 4 is suggestive but not something the chart format could ever prove on its own.

### Claim 6: The 2026 addition spike (37,022) is roughly 2.3x the size of the largest pre-2025 spike shown on the chart (15,998 additions, early 2018)
- **Evidence**: Derived by comparing the two addition figures given in the chart alt-text (37,022 vs. 15,998); this comparison is our own arithmetic, not asserted by the source.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see Claims 2 and the early-2018 figure "15,998 additions" in the chart alt text — this is our synthesis comparing the two)
- **Our assessment**: If accurate, this indicates the 2026 spike is not merely a new instance of the kind of burst the repo has always had periodically — it is meaningfully larger than any pre-agentic-era burst captured in the same chart. That said, this is a single before/after data point on a single project from a single maintainer, extracted via an image's alt text rather than raw commit data — treat as illustrative, not as measured evidence of a general productivity multiplier.

## Concrete Artifacts

### Full prose content of the post (verbatim)

> "datasette code-frequency chart on GitHub. Out of curiosity I decided to see if I could
> find a useful illustration of the impact of coding agents and Opus 4.5 class models on
> my own output. The best I've found so far is this GitHub chart of frequency of code
> changes to my Datasette open source project:
>
> [chart image]
>
> The big spike in activity at the end aligns with Opus 4.8, GPT-5.5, Fable 5 and
> GPT-5.6 Sol."

*Source: Simon Willison, simonwillison.net/2026/Jul/13/datasette-code-frequency/,
13th July 2026. This is the complete prose content of the post — a "link post" in
Willison's format.*

### Chart image alt text (verbatim)

> "Screenshot of a GitHub "Code frequency" bar chart, subtitled "Additions and deletions
> per week", showing green addition bars and red deletion bars per week from 2018 through
> 2026, with a y-axis labeled Frequency ranging from -20k to 30k. Activity comes in
> sporadic bursts: the largest spike is 37,022 additions with -9,528 deletions in 2026,
> followed by 14,638 additions with -6,584 deletions in late 2025, 15,998 additions in
> early 2018, and a standout deletion spike of -10,658 in mid-2020, with quieter periods
> of smaller weekly changes in between."

*Source: alt attribute of the chart screenshot embedded in the post, same URL. This
alt text is the only source for the specific numeric figures cited in Claims 2, 3, 5,
and 6 — see Extraction Notes for verification caveats.*

### Linked primary source

- GitHub code-frequency graph: https://github.com/simonw/datasette/graphs/code-frequency
  (the live, interactive version of the chart described above — in principle independently
  verifiable, though it requires GitHub to have finished computing repository statistics,
  which is an asynchronous background job; see Extraction Notes)

## Cross-References

- **Extends** `blog-simonwillison-vibe-coding-agentic-engineering.md` (Claim 7: "The SDLC
  was designed for ~200 LOC/day and does not scale to 2,000 LOC/day — every downstream
  process breaks"): that note documents Willison's qualitative claim about a roughly
  10x jump in personal LOC-per-day throughput from agentic tooling. This source supplies
  a concrete, dated, per-repository number in the same spirit — a single week hitting
  37,022 additions on one project — that is consistent with (though not a direct
  confirmation of) that order-of-magnitude claim. Both come from the same author, so this
  is one practitioner's pattern reinforcing itself across two posts, not independent
  corroboration.
- **Extends** `blog-simonwillison-code-w-claude-2026.md` (17x YoY growth in Anthropic API
  volume, reported at Anthropic's May 2026 developer event): that note documents
  platform-level usage growth; this source supplies an individual practitioner-level
  output metric from the same rough period. Both point in the same direction — usage and
  output scaling up sharply through 2025-2026 — at different levels of aggregation.
- **Corroborates (with an important caveat)** `paper-miller-speed-cost-quality.md`
  (Claim 1: Cursor adoption produces a 281.3% increase in lines added in month 1, decaying
  to zero by month 3, in a controlled difference-in-differences study of 806 adopting
  open-source projects vs. 1,380 matched controls): both sources document large addition
  spikes coincident with AI coding tool adoption/availability. But Miller et al.'s
  controlled study is the load-bearing caution here — their central finding is that raw
  addition-count spikes of exactly this kind are *transient* and revert to baseline within
  a few months unless something else changes. This source is a single non-longitudinal
  snapshot (one chart, one point in time, no before/after window reported) and cannot by
  itself distinguish "durable new baseline" from "another instance of the same transient
  spike-then-decay pattern" that Miller et al. document at scale. Any guide passage citing
  this source's numbers as evidence of sustained productivity gain should pair it with
  Miller et al.'s decay finding.
- **Corroborates** `blog-simonwillison-charity-majors-code-economics.md` (code shifted from
  an expensive, curated asset to a free, disposable, instantly-regenerable one in 2025):
  a 37,022-line addition/9,528-line deletion week is a concrete instance of code being
  produced and discarded at a volume consistent with Majors's "code is now disposable"
  framing — high churn (large deletions alongside large additions) rather than pure
  accretion.
- **Novel**: First corpus source to supply a specific, named-model-attributed, per-repository
  GitHub code-frequency data point (weekly addition/deletion line counts) as a practitioner's
  self-selected illustration of coding-agent impact on personal output. Prior corpus sources
  on this author's own productivity (`blog-simonwillison-vibe-coding-agentic-engineering.md`)
  are qualitative/narrative; this is the first quantitative (if informally sourced) figure
  from Willison himself.

## Guide Impact

- **Chapter 05 (Developer productivity with agents / measuring impact)**: This source is
  useful as a vivid, dated anecdote ("even Simon Willison, who is careful about hedging his
  claims, calls this the best productivity illustration he could find, and it's a screenshot
  of a GitHub chart") but should NOT be cited as measured evidence of a productivity
  multiplier. If used, it should be paired explicitly with `paper-miller-speed-cost-quality.md`
  to make the point that raw line-change-volume spikes are a weak, easily-transient signal —
  the guide's "measuring impact" guidance should recommend against using single-repo,
  single-snapshot code-frequency charts as a KPI, using this post as the cautionary example
  of a credible practitioner reaching for exactly that metric because nothing better was
  available to him.
- **Chapter 05 (Developer productivity with agents)**: Claim 4's named-model list (Opus 4.8,
  GPT-5.5, Fable 5, GPT-5.6 Sol) is useful as a timeline anchor — it corroborates
  `blog-simonwillison-vibe-coding-agentic-engineering.md`'s claim about a step-change in
  personal coding throughput being associated with this specific generation of models
  (mid-2026), independent of whether the code-frequency chart itself is good evidence.

## Extraction Notes

- **Very thin source, confirmed verbatim**: This is one of Willison's shortest post formats
  (a "link post" — a linked URL, one image, two sentences). Full page text was extracted via
  curl + raw HTML (not via a summarizing fetch) specifically so the two prose sentences and
  the image alt text could be quoted verbatim rather than paraphrased. The `og:description`
  meta tag independently confirms the opening sentence, ruling out a truncated or mangled
  fetch.
- **Numeric figures come from image alt text, not raw GitHub data**: The specific numbers in
  Claims 2, 3, 5, and 6 are drawn from the alt-text description of the embedded chart
  screenshot, not from GitHub's underlying stats API. I attempted to independently verify
  these figures against `https://api.github.com/repos/simonw/datasette/stats/code_frequency`,
  which returns raw weekly addition/deletion arrays for the repository — but GitHub computes
  this asynchronously per-repository and the endpoint returned HTTP 202 (computation
  in progress, empty body) on three attempts at extraction time, so I could not cross-check
  the alt-text numbers against the primary API data. The Assayer or a future reviewer should
  re-query that endpoint (it is public and unauthenticated) to confirm the four figures if
  precision matters for how the guide cites them. I have not treated the alt-text numbers as
  independently verified — they are reported as "what the post says," not as facts I confirmed
  against GitHub's raw statistics.
- **No linked sub-pages followed beyond the primary GitHub chart**: The post links only to
  the GitHub code-frequency graph (attempted, see above) and to `datasette.io` (the project's
  marketing homepage, which contains no additional relevant claims about this chart or the
  author's productivity — not a substantive sub-page for this extraction).
- **No contradictions filed**: Nothing here directly opposes an existing source note's claim
  in a way that would change guide advice — `paper-miller-speed-cost-quality.md` is a
  methodological caution about the same *kind* of metric (raw line-change spikes), not a
  factual dispute with anything Willison asserts. He does not claim the spike is durable; the
  caution is about how a reader might be tempted to over-read the number, which the
  Cross-References and Guide Impact sections above address directly rather than via a
  contradiction issue.
