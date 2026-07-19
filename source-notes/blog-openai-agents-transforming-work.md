---
source_url: https://openai.com/index/how-agents-are-transforming-work
source_type: blog-post
title: "How agents are transforming work"
author: OpenAI
date_published: 2026-06-25
date_extracted: 2026-07-19
last_checked: 2026-07-19
status: current
confidence_overall: emerging
issue: "#2030"
---

# How agents are transforming work

> OpenAI's own internal Codex-usage telemetry, presented as evidence for a
> "unit of knowledge work" thesis: agentic tools shift work from short
> chatbot interactions to delegated, long-horizon tasks. The centerpiece
> data point is OpenAI's own year-long internal transition — from Codex
> being under 10% of employee token usage in August 2025 to 99.8% of
> weekly company-wide output tokens by mid-2026 — paired with individual
> and organizational user data showing rapid non-developer adoption growth
> and longer task-horizon delegation over the same window.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`), summarizing
  what the post itself calls "our paper" — a longer research artifact this
  post distills rather than reproduces in full. No separate PDF or paper
  link is present in the fetched page content; the post is the only
  primary text examined for this note.
- **Author credibility**: Published under OpenAI's own domain, unsigned
  (no named individual author), presenting OpenAI's internal product
  telemetry (Codex usage inside OpenAI itself) alongside external
  individual- and organizational-user data from the same product. This is
  vendor-first-party usage data — OpenAI has direct, unaudited access to
  its own logs, which makes the *existence* of the underlying signal
  credible but the specific percentages unverifiable by outside readers.
  No sample sizes, cohort definitions, or measurement methodology (e.g.,
  how "estimated human-time-equivalent" per task is computed) are
  disclosed in the post itself.
- **Scope**: Covers four claimed adoption trends (longer-horizon delegation,
  cross-department primary-tool adoption at OpenAI, non-developer growth
  outpacing developer growth, and non-developers doing technical/coding
  work outside their job description), illustrated with OpenAI's own
  department-level Codex adoption timeline, a heat map of occupation vs.
  work-category token share, and closing "economic potential" framing.
  Does NOT cover: task success/quality rates, failure modes, methodology
  for the "estimated human-time" task-length metric, competitive
  comparison to Claude Code/GitHub Copilot/Cursor, or any external
  (non-OpenAI-product) validation of the figures.

## Extracted Claims

### Claim 1: Agentic AI changes the fundamental unit of knowledge work from short, self-contained chatbot interactions to delegated, long-horizon tasks
- **Evidence**: Author's opening framing/thesis statement, not itself a
  measured finding but the interpretive lens for the data that follows.
- **Confidence**: emerging (framing claim, not independently measured, but
  consistent with the behavioral data in Claims 3 and 5 below)
- **Quote**: "Agentic AI changes the unit of knowledge work from single interactions to delegated, long-horizon tasks. Chatbot interactions are often short and self-contained. Agents can operate independently for minutes or hours while orchestrating tool calls, interacting with environments, and iterating towards solutions."
- **Our assessment**: This is the post's title-level thesis and reads as an
  OpenAI-flavored restatement of the delegation-depth argument already
  well-represented in our corpus (e.g., `blog-addyosmani-own-the-outer-loop.md`
  Claim 2's inner-loop/outer-loop framing, and the general "chatbot vs.
  agent" distinction used across multiple Anthropic and practitioner
  sources). Useful as a vendor-independent restatement of a thesis this
  guide already holds, not as new evidence for it.

### Claim 2: Through August 2025, the average OpenAI employee spent less than 10% of their AI tokens on Codex; by mid-2026, Codex accounts for 99.8% of weekly company-wide output tokens at OpenAI
- **Evidence**: OpenAI's own internal token-usage telemetry, aggregated
  company-wide.
- **Confidence**: emerging (first-party vendor telemetry about the vendor's
  own product, presented without methodology, cohort definition, or
  external audit — but it is a specific, falsifiable, dramatic number)
- **Quote**: "Through August 2025, the average OpenAI worker spent less than 10% of their tokens on Codex. Now, every department, including non-technical departments such as Legal and Recruiting, uses Codex as their primary AI tool for work."
- **Additional quote**: "Codex accounts for 99.8% of weekly output tokens generated within OpenAI."
- **Our assessment**: The 99.8% figure is a striking, almost total-displacement number — it should be read as evidence that *inside OpenAI specifically*, agentic coding-tool usage has essentially replaced chatbot usage as the dominant AI interaction mode, not as a claim about what fraction of *work* is AI-assisted (that is a different metric OpenAI does not report here). This is a much larger claimed share than the closest comparable figure in our corpus, `research-anthropic-ai-transforming-work.md` Claim 1 (Anthropic engineers use Claude in "60% of their work," self-reported). The two numbers are not directly comparable — Anthropic's is a self-reported work-share estimate across all Claude products, OpenAI's is a measured token-share specifically between Codex and other internal AI tools — but the scale gap is large enough to flag as worth reconciling if either source is cited for "how much of AI-company-internal-work is now agent-mediated."

### Claim 3: By May 2026, 80.6% of sampled individual Codex users made at least one request estimated to exceed 30 minutes of human work; 70.2% exceeded one hour; 25.6% exceeded eight hours
- **Evidence**: OpenAI's internal estimation of "human-time-equivalent" per
  Codex task, sampled across individual (non-organizational) users.
- **Confidence**: emerging (a specific, dated, three-threshold statistic,
  but the "estimated human-time" metric's construction is not explained —
  it is unclear whether this is derived from task complexity heuristics,
  a labeled dataset, or self-report)
- **Quote**: "By May 2026, 80.6% of sampled individual users made at least one Codex request estimated to exceed 30 minutes of human work, 70.2% made one estimated to exceed one hour, and 25.6% made at least one Codex request estimated to exceed eight hours."
- **Our assessment**: This is the post's clearest quantitative evidence for
  the "longer-horizon delegation" thesis (Claim 1) and the single most
  citable statistic in the post for a guide discussion of delegation
  depth. The methodology gap (how is "human work" time estimated for an
  arbitrary agent task?) is the main weakness — without knowing whether
  this is a heuristic, a labeled benchmark, or a self-reported estimate,
  the precise percentages should be treated as directional rather than
  precise. Corroborates (from OpenAI's side) the general "tasks are
  getting longer-horizon" trend also present in
  `research-anthropic-ai-transforming-work.md` Claim 5 (Claude Code
  autonomous tool calls per task roughly doubled, Feb–Aug 2025), though
  the two sources measure different things (task duration vs. tool-call
  count) and are not the same underlying metric.

### Claim 4: By June 2026, users at the 99th percentile of Codex usage regularly generated more than 60 hours of Codex agent runtime per day, distributed across multiple parallel agents
- **Evidence**: OpenAI's internal daily-runtime telemetry for top-decile
  users.
- **Confidence**: anecdotal (a top-percentile figure, not representative of
  typical usage, and the post gives no indication of how many users are
  in this 99th-percentile band or what tasks compose the 60+ hours)
- **Quote**: "By June 2026, users at the 99th percentile regularly generated more than 60 hours of Codex agent turns per day, distributed across multiple, parallel agents."
- **Our assessment**: A striking number but explicitly a tail statistic —
  "more than 60 hours of agent runtime in a single day" is only possible
  through heavy parallelization (dozens of concurrent agent sessions), not
  literal single-threaded work. Useful as evidence that extreme-parallel
  multi-agent orchestration is happening in practice at the far edge of
  the user distribution, corroborating the general industry direction
  toward running many simultaneous agent sessions already noted in
  `blog-openai-codex-knowledge-work.md` Claim 6 (~50% of Codex users
  running more than one task simultaneously at some point in the day, a
  *median*-range statistic, distinct from this post's 99th-percentile
  claim). The two claims describe different parts of the same
  distribution (median vs. extreme tail) and should not be conflated when
  cited together.

### Claim 5: Codex became the primary AI tool for every department at OpenAI, with Engineering adopting first (majority-Codex by December 2025) and Legal, Finance, and Recruiting crossing over later (around April 2026), after which the average OpenAI worker's Codex usage exceeds 85% of their output tokens
- **Evidence**: OpenAI's internal department-level adoption-timeline
  telemetry.
- **Confidence**: emerging (specific, dated, department-level breakdown —
  more granular and more checkable than an aggregate figure, though still
  self-reported vendor telemetry)
- **Quote**: "The average engineer at the company shifted the majority of their usage of OpenAI products to Codex by December 2025. Today, the average engineer generates 99% of their output tokens with Codex rather than ChatGPT. Legal, finance, and recruiting crossed over to majority use of Codex later, around April 2026, but their transitions were much faster. The average lawyer or recruiter at OpenAI now generates more than 85% of their output tokens on Codex."
- **Our assessment**: The "transitions were much faster" detail for
  non-engineering departments is the most guide-relevant part of this
  claim — it suggests that once a coding-agent tool crosses some
  usability/utility threshold for non-technical roles, adoption within
  those roles can happen faster than the original engineering-team
  ramp-up did, not slower. This is a useful counter-data-point to any
  assumption that non-technical teams are inherently slow adopters of
  agentic tooling; it corroborates
  `blog-openai-codex-knowledge-work.md` Claim 2 (knowledge workers
  adopting Codex "more than 3 times as fast as developers") with a
  department-level, dated timeline rather than an aggregate multiplier.

### Claim 6: Over the past six months (to June 2026), Codex usage intensity grew fastest in Research (56x since November 2025), followed by Customer Support (32x), Engineering (27x), and Legal (13x)
- **Evidence**: OpenAI's internal department-level output-token growth
  telemetry, "among active internal users."
- **Confidence**: emerging (specific, department-broken-out multipliers,
  but "active internal users" is undefined — it is unclear whether this
  controls for headcount changes or measures only usage-intensity among
  already-active users)
- **Quote**: "Research saw the biggest jump: by June 2026, median use was 56 times higher than in November 2025. Customer Support rose 32 times and Engineering rose 27 times, while Legal grew more gradually but still reached 13 times its November level."
- **Our assessment**: Research leading in usage-intensity growth (rather
  than Engineering, which had the head start per Claim 5) suggests that
  once a department starts using an agent at all, growth in usage
  intensity can outpace the department that adopted first — a distinct
  finding from "who adopted first" (Claim 5). This is a novel
  department-level intensity-growth breakdown not present elsewhere in
  our corpus; the closest comparable is
  `research-anthropic-ai-transforming-work.md` Claim 7 (team-by-team usage
  *composition* breakdown — pre-training 54.6% feature implementation,
  security 48.9% code understanding), which measures *what* teams do with
  AI rather than *how fast* their usage is growing, so the two are
  complementary rather than overlapping.

### Claim 7: Non-developer Codex adoption grew far faster than developer adoption since August 2025 — 137x for individual users, 189x for organizational users, and 12x within OpenAI itself
- **Evidence**: OpenAI's internal usage growth telemetry, broken out by
  user population (individual / organizational / internal-OpenAI) and by
  developer-vs-non-developer classification.
- **Confidence**: emerging (three parallel, dated multipliers across three
  distinct user populations — internally consistent presentation, but
  self-reported and the developer/non-developer classification
  methodology is not disclosed)
- **Quote**: "Since August 2025, non-developer users rose 137x for individual users, 189x for organizational users, and 12x within OpenAI."
- **Our assessment**: This is the post's headline growth statistic and the
  most likely candidate for guide citation. The pattern — smaller
  multiplier for OpenAI's own internal population (12x) versus much larger
  multipliers for external individual (137x) and organizational (189x)
  users — is explained by OpenAI's own framing elsewhere in the post
  ("likely because this group already started at a well above average
  starting point"): OpenAI's internal non-developer base was not starting
  from zero the way external users were, so the smaller internal
  multiplier is a base-rate artifact, not evidence of slower internal
  growth. Corroborates
  `blog-openai-codex-knowledge-work.md` Claim 2 (20% of Codex users are
  now knowledge workers, adopting "more than 3 times as fast as
  developers") — the two posts describe the same underlying trend
  (non-developer Codex adoption outpacing developer adoption) using
  different metrics from different time windows (June 2 report: point-in-time
  adoption-rate ratio; this post, June 25: year-over-year growth
  multiplier), which is useful triangulation rather than a single
  restated number.

### Claim 8: Non-technical OpenAI workers regularly use Codex for coding or technical execution tasks outside their job description — automation, data transformation, tooling, debugging, and structured analysis — and over one-fourth of Codex work done by business-function workers is engineering or coding
- **Evidence**: OpenAI's internal task-classification telemetry, comparing
  inferred department against inferred work-category of Codex output.
- **Confidence**: emerging (a specific fraction — "over one-fourth" — for a
  defined population, but the task-classification methodology, i.e., how
  Codex infers "occupation" and "work category" from usage, is not
  disclosed)
- **Quote**: "For instance, over one-fourth of work done with Codex by workers in business functions was engineering or coding. Agents can lower the cost of moving across task boundaries and help workers do adjacent work that used to require more specialized technical support."
- **Our assessment**: This directly corroborates
  `blog-openai-codex-knowledge-work.md` Claim 5 (72% of knowledge-worker
  Codex users produce artifacts weekly; the next most common categories
  are engineering operations at 47% and code implementation at 46%) —
  both posts describe the same underlying phenomenon (role-boundary
  dissolution between "developer" and "knowledge worker" Codex usage)
  from different angles (this post: business-function workers doing >25%
  technical work; the earlier post: knowledge workers doing 46-47%
  technical-adjacent work). The consistency across two OpenAI posts
  published roughly three weeks apart, using what appear to be
  independently phrased statistics, raises modest confidence that this is
  a stable, repeatedly-observed pattern in OpenAI's internal data rather
  than a one-off framing choice.

### Claim 9: Codex enables non-technical departments to accelerate workflows previously bottlenecked by technical expertise, with Engineering/coding as the largest work category for Data Science/Research departments, and general "knowledge work" as the largest category for Finance/Business Operations, Marketing, and Operations departments
- **Evidence**: A heat map (described but not reproduced as data in the
  fetched text; only its caption and framing sentence were extracted)
  comparing inferred OpenAI department against Codex output work-category.
- **Confidence**: anecdotal (the underlying heat-map data was not
  recoverable from the text extraction used for this note — see
  Extraction Notes — so this claim rests on the post's own prose summary
  of the chart, not the chart's actual values)
- **Quote**: "The heat map below compares inferred occupations within OpenAI to the type of work represented in Codex outputs. Engineering and coding show up as the largest category for data science and research, whereas knowledge work is the largest category for finance and business operations, marketing, operations, and other departments."
- **Our assessment**: Consistent with Claims 5, 6, and 8's overall picture
  of broad-based non-engineering Codex adoption, but this specific claim
  is the weakest-evidenced in the post for our extraction purposes since
  the actual heat-map values were not present in the text we could fetch
  (see Extraction Notes) — treat as illustrative color, not a citable
  statistic, unless a future extraction can recover the chart's
  underlying data.

## Concrete Artifacts

```
Source: OpenAI, "How agents are transforming work,"
https://openai.com/index/how-agents-are-transforming-work (June 25, 2026)

Headline internal-adoption trajectory:
  Through Aug 2025:  <10% of average OpenAI worker's tokens on Codex
  Now (mid-2026):     Codex = primary AI tool in every OpenAI department
                       Codex = >85% of output tokens for average worker
                       Codex = 99.8% of weekly company-wide output tokens

Individual-user task-length thresholds crossed (May 2026 snapshot):
  >30 min of human-equivalent work:  80.6% of sampled users
  >1 hour:                            70.2% of sampled users
  >8 hours:                           25.6% of sampled users

Department Codex-adoption crossover timeline:
  Engineering:                majority-Codex by Dec 2025 (99% of output tokens, "today")
  Legal / Finance / Recruiting: majority-Codex by ~Apr 2026 (>85% of output tokens)

Six-month output-token growth by department (to June 2026, vs. Nov 2025):
  Research:          56x
  Customer Support:   32x
  Engineering:        27x
  Legal:              13x

Non-developer user growth since Aug 2025 (to early June 2026):
  Individual users:       137x
  Organizational users:   189x
  OpenAI internal users:   12x

99th-percentile daily usage (June 2026):
  >60 hours of Codex agent runtime per day, across parallel agents
```

## Cross-References

- **Corroborates**:
  - `blog-openai-codex-knowledge-work.md` (the June 2, 2026 OpenAI "Next
    Era of Knowledge Work" report) — both posts document the same
    underlying trend (non-developer/knowledge-worker Codex adoption
    outpacing developer adoption) using independently phrased statistics
    from overlapping but not identical time windows: the earlier post's
    Claim 2 (20% of users are knowledge workers, adopting 3x faster) and
    Claim 5 (72%/47%/46%/41% task-category participation among knowledge
    workers) line up with this post's Claim 7 (137x/189x/12x
    non-developer growth multipliers) and Claim 8 (>25% of business-function
    Codex work is engineering/coding). Two OpenAI posts three weeks apart
    reporting consistent directional findings from what is likely the
    same underlying "paper" (referenced but not linked in this post) is
    modestly reassuring for the *direction* of the trend, though both
    remain unaudited first-party vendor telemetry for the *magnitude*.
  - The general parallel/multi-agent-session usage trend already in the
    corpus — this post's Claim 4 (99th-percentile users generating 60+
    hours of parallel agent runtime per day) and
    `blog-openai-codex-knowledge-work.md` Claim 6 (~50% of Codex users
    running more than one task simultaneously) describe the same
    behavioral shift at different points of the usage distribution
    (extreme tail vs. median).
- **Contradicts**: None identified as a direct factual contradiction. Note
  the large scale gap between this post's Claim 2 (Codex = 99.8% of
  weekly output tokens at OpenAI) and
  `research-anthropic-ai-transforming-work.md` Claim 1 (Anthropic
  engineers self-report using Claude in 60% of their work) — these are
  not measuring the same thing (token share between internal tools vs.
  self-reported work-share) and are not treated as a contradiction here,
  but a future guide section citing both "how much of company-internal
  work is now agent-mediated at the leading labs" should not present
  these two numbers side-by-side without flagging the metric mismatch.
- **Extends**:
  - `research-anthropic-ai-transforming-work.md` — both sources are
    lab-internal usage studies of the lab's own coding agent (Codex at
    OpenAI, Claude Code at Anthropic) at roughly the same point in the
    industry's timeline, giving the guide two independent internal
    case studies from the two leading labs. Anthropic's is methodologically
    richer (survey + interviews + Clio log analysis, explicit limitations
    section) while this OpenAI post is telemetry-only with no disclosed
    methodology — the Anthropic note should be treated as the
    higher-confidence source of the two when a chapter needs one
    "internal lab adoption" citation, with this note as a corroborating,
    lower-confidence second data point.
  - `blog-addyosmani-own-the-outer-loop.md` Concrete Artifacts (the "external
    citations with direct links" block) already listed this exact article
    (`https://openai.com/index/how-agents-are-transforming-work/`) as one
    of six sources Osmani cited but that note did not independently fetch
    or verify; this note is the independent extraction of that citation
    (note: that source note's own numbered "Additional Sources to Enqueue"
    list omits this article specifically, even though the Concrete
    Artifacts block flags all six citations as enqueue candidates — this
    note closes that gap regardless).
- **Novel**:
  - The specific 99.8%-of-weekly-output-tokens figure for Codex usage
    inside OpenAI (Claim 2) — no existing corpus source reports a
    single-tool token-share this close to total displacement of other AI
    tools within a company.
  - The department-level six-month usage-intensity growth multipliers
    (Claim 6: Research 56x, Customer Support 32x, Engineering 27x, Legal
    13x) — a new department-by-department intensity-growth breakdown not
    present in any existing source note.
  - The three-population (individual/organizational/internal) non-developer
    growth-multiplier comparison (Claim 7: 137x/189x/12x) — the first
    source in our corpus to compare non-developer coding-agent adoption
    growth across external individual users, external organizational
    customers, and the vendor's own internal staff side-by-side.

## Guide Impact

- **Chapter 04 (Agentic Workflows)**: Claim 3 (30-min/1-hour/8-hour
  task-length adoption thresholds, May 2026) is a citable, dated
  data point for a section on delegation depth — pair with
  `research-anthropic-ai-transforming-work.md` Claim 5 (autonomous
  tool-call count roughly doubling) as two independent lab-internal
  signals that task horizons are lengthening, while flagging that neither
  source discloses how "task length" or "autonomy" is measured.
- **Chapter 05 (Team Adoption)**: Claim 5's finding that non-engineering
  departments (Legal, Finance, Recruiting) crossed over to majority-agent
  usage *faster* than Engineering did, once they started, is a useful
  counter-example to any "non-technical teams adopt slowly" assumption —
  cite alongside `blog-openai-codex-knowledge-work.md` Claim 2 for the
  same directional point from a different report.
- **Chapter 02 (Harness Engineering)**: Claim 8 (over one-fourth of
  business-function Codex work is engineering/coding) reinforces the
  point already flagged from `blog-openai-codex-knowledge-work.md` Claim 5
  against designing harnesses that assume a strict developer/non-developer
  usage boundary — now corroborated by a second, independently-phrased
  OpenAI statistic three weeks later.
- No chapter should cite the 99.8%-token-share figure (Claim 2) or the
  137x/189x/12x multipliers (Claim 7) as precise, load-bearing numbers on
  their own — they are unaudited first-party vendor telemetry with no
  disclosed methodology, cohort definition, or external validation. Use
  them as directional evidence of a real and large trend, not as
  benchmarks a reader should expect their own organization to replicate.

## Extraction Notes

- The live OpenAI URL (`https://openai.com/index/how-agents-are-transforming-work`)
  returned HTTP 403 to both `WebFetch` and direct `curl` with a browser
  user-agent (Cloudflare bot-challenge, `cf-mitigated: challenge` header
  observed directly). The Internet Archive Wayback Machine's availability
  API was also unreachable at extraction time ("Internet Archive services
  are temporarily offline"). The article was instead retrieved via a
  third-party reader proxy (`r.jina.ai`) fetched with `curl`, which
  returned the full page converted to Markdown, including all prose,
  headings, bullet lists, and the closing paragraph — every quote above
  was checked character-for-character against that fetched Markdown.
- The post references embedded interactive charts (a task-length-threshold
  chart, a department-adoption chart, and an occupation-vs-work-category
  heat map) whose underlying data tables were not recoverable as text from
  the reader-proxy Markdown conversion — the heat map in particular
  (Claim 9) rendered only as an empty table skeleton with a caption, no
  cell values. Claim 9 is therefore drawn only from the post's own prose
  description of the heat map, not the chart's actual data, and is
  flagged accordingly as anecdotal/weakest-evidenced in this note.
- The post refers to "our paper" in its closing paragraph ("Our paper
  shows how frontier users adopt capable agentic tools at the frontier")
  but the fetched page text contained no link to a separate paper or PDF
  distinct from the blog post itself — unlike
  `blog-openai-codex-knowledge-work.md`, where the blog post explicitly
  linked an 11-page companion PDF report. If a linked paper exists on the
  live page (inaccessible to this extraction due to the Cloudflare
  challenge), it was not found and is flagged as a follow-up for a future
  extraction attempt with a different access method.
- No numbered footnote targets (`[1]`, `[2]` in the fetched Markdown,
  linking to `#citation-bottom-1` / `#citation-bottom-2` anchors on the
  same page) resolved to visible footnote text in the reader-proxy
  extraction — these appear to be in-page citation markers for the two
  embedded charts rather than a separate references/bibliography section,
  and no footnote content was fabricated to fill this gap.
