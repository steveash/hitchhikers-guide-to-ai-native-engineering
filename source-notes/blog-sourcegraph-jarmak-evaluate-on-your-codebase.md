---
source_url: https://sourcegraph.com/blog/how-to-evaluate-sourcegraph-on-your-own-codebase
source_type: blog-post
title: "How to evaluate Sourcegraph on your own codebase"
author: Stephanie Jarmak (Sourcegraph)
date_published: 2026-07-31
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: emerging
issue: "#2384"
---

# How to evaluate Sourcegraph on your own codebase

> Sourcegraph vendor blog post that decouples "does structured code
> retrieval help?" into three independently-moving measurements —
> retrieval quality, task completion, and cost — backed by a 288-task
> experiment where F1/recall improved substantially while aggregate task
> completion stayed flat, and closes with a nine-control evaluation
> checklist and a CLI tool (CodeProbe) for running the same comparison on
> a reader's own repositories.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published July 31, 2026;
  auto-discovered via the `sourcegraph` trusted feed). Long-form
  methodology post: intro framing, an "Aggregate result" walkthrough, a
  "search difficulty" section with a difficulty-weighting scheme, a
  nine-control checklist, a nine-row result-interpretation table, a
  full CLI walkthrough for a tool called CodeProbe, and a closing section
  on the limits of the evaluation itself (sample-size guidance).
- **Author credibility**: Byline is "Stephanie Jarmak," contactable at
  stephanie.jarmak@sourcegraph.com, published on Sourcegraph's official
  company blog. This is vendor content — Sourcegraph sells the MCP
  server/code-search product being evaluated — but the post is unusual
  among vendor content in that its headline result is *not* flattering to
  the product on the metric most readers would care about first
  (aggregate task completion "effectively unchanged"). The author links
  to a companion piece, "Rethinking coding agent benchmarks" (a January
  2026 Medium post), and to CodeProbe's own longer methodology post
  (`sourcegraph.com/blog/codescalebench-testing-coding-agents-on-large-codebases-and-multi-repo-software-engineering-tasks`),
  which is the primary source of the 288-task dataset this post reports
  numbers from — this Miner did not independently fetch or extract that
  companion post as part of this note (see Extraction Notes), so the
  underlying experimental design (task mining, verifier construction) is
  not independently verified here, only the summary numbers and
  methodology recommendations presented in this post.
- **Scope**: Covers how to evaluate whether the Sourcegraph MCP server
  improves a coding agent's task completion, retrieval quality, or cost
  on a reader's own codebase — including a difficulty-classification
  scheme, nine evaluation controls, a result-interpretation table, and a
  CLI-driven experiment walkthrough (CodeProbe, described as alpha
  software). Does NOT cover: the internals of the Sourcegraph MCP server
  itself, a description of CodeProbe's task-mining or verification
  internals beyond the CLI surface, or independent reproduction of the
  288-task result — all numbers are first-party and self-reported.

## Extracted Claims

### Claim 1: Retrieval quality, task completion, and cost are three independently-moving measurements of an agent system, and measuring only one of them can produce a technically correct result that still leads to the wrong rollout decision
- **Evidence**: Stated as the article's central methodological thesis,
  immediately following the report of the 288-task result (Claim 2).
- **Confidence**: emerging (a first-party framing claim, illustrated by
  the article's own experimental result, but not independently tested
  against a second dataset in this post)
- **Quote**: "Those results are not contradictory. Retrieval quality, task completion, and cost measure different parts of the system. Measuring only one can produce a technically correct result that still leads to the wrong rollout decision."
- **Our assessment**: This is the load-bearing claim the rest of the post
  operationalizes. It is a direct, generalizable warning against the
  common practice of citing a single aggregate metric (e.g., "F1
  improved 2.6x") as if it settles whether a retrieval tool is worth
  deploying. The claim is strengthened by the fact that Sourcegraph is
  reporting a result where its own product's headline retrieval metric
  improved sharply while the metric most buyers actually care about
  (task completion) did not move — a vendor has little incentive to
  publish a result this unflattering unless the underlying pattern is
  real and they expect readers to independently reproduce it.

### Claim 2: Across 288 tasks with full information parity, Sourcegraph's structured retrieval raised file-level F1 from 0.091 to 0.240 and recall from 0.120 to 0.272, while aggregate task-completion reward was effectively unchanged
- **Evidence**: The core experimental result, reported twice (intro and
  "One evaluation, three different answers" section) with the same
  numbers both times, described as measured "under full information
  parity: both arms could reach the same code at the same revisions."
- **Confidence**: emerging (specific, repeated first-party numbers from a
  288-task experiment; not independently reproduced by this Miner or, as
  far as this note can establish, by any third party)
- **Quote**: "Sourcegraph improved retrieval, raising file-level F1 from 0.091 to 0.240 and recall from 0.120 to 0.272. Aggregate task-completion reward was effectively unchanged."
- **Our assessment**: A roughly 2.6x F1 improvement and 2.3x recall
  improvement is a large retrieval-quality gain by any normal standard,
  which makes the flat completion result the more surprising and more
  useful half of the finding. Taken alone, either half of this claim
  would mislead: "F1 improved 2.6x" implies the tool clearly helps;
  "completion was unchanged" implies it doesn't matter. Reported
  together, the claim is that retrieval quality and task completion are
  not the same measurement and do not have to move together — this is
  the concrete evidence for Claim 1.

### Claim 3: The cost effect of structured retrieval depended on how much the baseline agent already had to search — it saved 15% to 51% when the baseline searched broadly, but cost an average of $0.15 more when the baseline localized the work in seven searches or fewer
- **Evidence**: Reported as the third, independently-moving measurement
  in the same 288-task result, in the "One evaluation, three different
  answers" section.
- **Confidence**: emerging (specific first-party cost figures tied to a
  stated baseline-search-count threshold)
- **Quote**: "Structured retrieval saved 15% to 51% where the baseline agent searched broadly, but cost an average of $0.15 more when the baseline localized the work in seven searches or fewer."
- **Our assessment**: This is the practical payoff of decoupling the
  three metrics: a team that only measured aggregate cost across all 288
  tasks would see a muddled, possibly net-negative number, obscuring
  that the tool has a real and substantial cost benefit on a specific,
  identifiable subset of tasks (those where the baseline searches
  broadly) and a real cost penalty on another subset (tasks the baseline
  already localizes cheaply). The seven-searches threshold is a
  concrete, actionable segmentation boundary for readers running their
  own evaluation, though the post elsewhere (Claim 6) gives a higher
  20-search threshold as part of a four-signal bundle, so this
  seven-search figure should be read as a rough single-variable proxy,
  not the full predictor.

### Claim 4: A post-hoc census of the 288-task corpus found that roughly 74% of tasks were solvable with grep alone, and only about a quarter combined a behavioral instruction with an answer dispersed across the codebase — meaning most tasks in the corpus left little room for better retrieval to change the completion outcome
- **Evidence**: Presented as the explanation for why the flat aggregate
  completion result (Claim 2) is "easy to misread," in the "One
  evaluation, three different answers" section.
- **Confidence**: emerging (a specific, quantified corpus composition
  statistic, self-reported and not independently audited by this Miner)
- **Quote**: "A later census found that roughly 74% of the corpus was solvable with grep alone. Thirty-eight percent of prompts named a path, symbol, or directory outright, while only about a quarter combined a behavioral instruction with an answer dispersed across the codebase."
- **Our assessment**: This is the diagnostic explanation behind Claim 2's
  flat aggregate result — it is not that structured retrieval fails to
  help, but that most of the 288 tasks did not require the kind of help
  it provides. This has a direct methodological implication beyond
  Sourcegraph's own product: any aggregate benchmark result for a
  retrieval tool is only as informative as the task mix's dispersion
  profile, and a corpus dominated by grep-solvable tasks will
  systematically understate a structured-retrieval tool's value on the
  minority of tasks it actually targets.

### Claim 5: Retrieval difficulty should be weighted by repository span and directory dispersion rather than raw codebase size — a 40-million-line monorepo can behave like a small repository if the relevant code sits in one directory, while a 2-million-line codebase can be the harder retrieval problem if the answer is scattered across four services
- **Evidence**: Presented as the article's retrieval-difficulty weighting
  scheme, stated to have been "defined before we examined outcomes" (a
  pre-registration claim), in the "Search difficulty matters more than
  codebase size" section.
- **Confidence**: emerging (a stated pre-registered weighting scheme with
  an illustrative example; the pre-registration claim itself is asserted
  by the author, not independently verifiable by this Miner)
- **Quote**: "Our retrieval-difficulty weighting, defined before we examined outcomes, assigns more weight to repository span and directory dispersion than to total lines of code. A 40-million-line monorepo behaves like a small repository when the relevant code sits in one directory. A two-million-line estate becomes the harder retrieval problem when the answer is scattered across four services."
- **Our assessment**: This directly reframes "does codebase size matter for
  agent tooling?" — a question the corpus has treated in absolute terms
  elsewhere (see Cross-References) — into a claim that dispersion, not
  raw size, is the operative variable. A team evaluating retrieval tools
  by codebase line count alone (a common proxy) would be measuring the
  wrong axis by this account; the right proxy is how many
  services/directories/ownership boundaries a task's answer spans.

### Claim 6: Observed baseline search burden — roughly 20+ searches, 15+ file reads, 30+ turns, and 75,000+ payload tokens together — is a better predictor of where structured retrieval helps than the task's assigned difficulty category, illustrated by a task (`domain-160`) labeled difficult that the baseline localized in only two searches, where retrieval cost more instead of less
- **Evidence**: Presented in the "Search difficulty matters more than
  codebase size" section as the practical alternative to a taxonomy-based
  difficulty label, following the correlation finding in Claim 7.
- **Confidence**: emerging (a specific four-threshold bundle described as
  "reference points from one corpus, not universal cutoffs," plus one
  named counter-example task)
- **Quote**: "`domain-160` shows why observed search burden matters more than a task label. We classified it as difficult because the instruction was behavioral and the answer was dispersed, but the baseline localized it in only two searches. Structured retrieval therefore cost more. The more useful predictor was not the category we assigned, but how much searching the baseline agent actually had to do."
- **Our assessment**: This is the single most actionable methodological
  claim in the post for a team running its own evaluation without a
  labeled difficulty taxonomy: instrument the baseline agent's own
  trajectory (search count, file reads, turns, token consumption) before
  deciding whether a task is a good candidate for retrieval improvement,
  rather than trusting a manually-assigned category. The author's own
  admission that the taxonomy mis-predicted `domain-160` is a credible
  self-correction — a vendor post that only reported cases where its
  own classification worked would be less trustworthy.

### Claim 7: Across 113 paired tasks, the correlation between Sourcegraph's cost advantage and baseline search breadth was r = -0.57 — the more the baseline agent searched, the more likely structured retrieval reduced cost
- **Evidence**: Stated directly as a Pearson-style correlation coefficient
  over a named subset (113 of the 288 tasks) in the "Search difficulty
  matters more than codebase size" section, immediately preceding a
  scatterplot figure of seven illustrative task pairs.
- **Confidence**: emerging (a specific correlation coefficient over a
  named sample size; the underlying task-level data is not published in
  the post, so this Miner cannot independently verify the coefficient)
- **Quote**: "Across 113 paired tasks, the correlation between Sourcegraph's cost advantage and baseline search breadth was (r = -0.57): the more the baseline agent searched, the more likely structured retrieval was to reduce cost."
- **Our assessment**: An r of -0.57 is a moderate-to-strong negative
  correlation for a real-world engineering dataset (not a perfect
  predictor, but far from noise) and is the quantitative backbone for
  Claim 6's search-burden-over-category recommendation. This is the most
  citable single statistic in the post for a guide passage arguing that
  cost savings from a retrieval tool are conditional on baseline search
  behavior rather than a fixed percentage.

### Claim 8: Repository and revision parity between the two evaluation arms is a critical, previously-unaudited confound — tasks where the baseline arm was missing repositories showed a +0.091 reward delta, compared with -0.007 under full parity, meaning the unaudited comparison partly measured access to code rather than the ability to find it
- **Evidence**: Presented as control #3 ("Pin the code") of the
  nine-control checklist, with a specific before/after audit result.
- **Confidence**: emerging (a specific, named audit finding with numeric
  deltas; first-party and not independently reproduced)
- **Quote**: "Both arms must reach the same repositories at the same revisions. When we audited this, tasks where the baseline was missing repositories showed a +0.091 reward delta, compared with −0.007 under full parity. The former measures having code rather than finding it."
- **Our assessment**: This is a striking self-reported methodological
  bug the authors found and fixed in their own prior evaluation
  practice: a +0.091 reward delta (favoring the retrieval-tool arm)
  collapses to essentially zero (-0.007) once both arms have equal
  repository access. Any team comparing a retrieval-augmented agent
  against a local-search baseline should treat unequal repository access
  as a near-certain source of an inflated apparent effect, not a minor
  configuration detail — the magnitude here (+0.091 vs. -0.007) suggests
  this single confound alone can account for essentially the entire
  measured effect in an unaudited setup.

### Claim 9: Single-trial evaluation designs overstate effect deltas by 40% to 60% relative to averaging at least three repeated trials per task, because within-task variance routinely exceeds the effect being estimated
- **Evidence**: Presented as control #6 ("Repeat each task at least three
  times") of the nine-control checklist.
- **Confidence**: emerging (a specific percentage-overstatement range
  presented without the underlying trial-by-trial data or a cited
  external study; appears to be a first-party empirical finding from the
  authors' own evaluation practice)
- **Quote**: "Repeat each task at least three times. Average runs within each task before comparing arms. Single-trial designs overstate deltas by 40% to 60%, and within-task variance routinely exceeds the effect being estimated."
- **Our assessment**: A 40-60% overstatement range is large enough to
  flip a marginal result from "significant" to "noise" in a single-trial
  design, which makes this one of the most concrete, quotable numbers in
  the post for arguing against single-run agent benchmarking generally
  (not specific to retrieval-tool evaluation). No comparison methodology
  or confidence interval is given for how the 40-60% range itself was
  computed, so this figure should be treated as a directional,
  first-party finding rather than a settled statistical constant.

### Claim 10: OpenAI's audit of SWE-Bench Pro estimated that roughly 30% of its tasks were broken — most often because prompts and tests disagreed, tests enforced an unstated implementation, or incomplete solutions could pass — meaning mining real historical work does not automatically produce valid evaluation tasks
- **Evidence**: Cited as supporting evidence for control #1 ("Choose real
  work") of the nine-control checklist, with a link to OpenAI's
  published audit ("Separating signal from noise: coding evaluations").
- **Confidence**: emerging (a specific, named third-party statistic
  attributed to OpenAI, linked in the source but not independently
  fetched or verified by this Miner against OpenAI's own report)
- **Quote**: "OpenAI's audit of SWE-Bench Pro estimated that roughly 30% of its tasks were broken, most often because prompts and tests disagreed, tests enforced an unstated implementation, or incomplete solutions could pass."
- **Our assessment**: This is a genuinely novel citation to the corpus
  (see Cross-References — Novel): it names a different SWE-Bench Pro
  validity problem than the one already documented from Cursor's own
  audit (reward hacking / answer retrieval during evaluation). OpenAI's
  ~30% figure is about test/task construction validity — the task itself
  is malformed — which is a distinct failure mode from a model gaming an
  otherwise-valid task. Both point to the same underlying lesson (don't
  trust a coding-agent benchmark score without auditing the benchmark's
  own construction), but from opposite ends: OpenAI's finding says the
  tasks themselves are often wrong; Cursor's finding (already in the
  corpus) says even valid-looking passing runs can reflect answer
  retrieval rather than derivation.

### Claim 11: A pilot of 40 tasks is useful only for exposing integration failures and directional differences; roughly 80 paired tasks is the statistical floor for a stable effect estimate, 200 provides a more defensible basis for a deployment claim, and closer to 100 is recommended specifically when retrieval quality (rather than completion or cost) is the primary endpoint being measured
- **Evidence**: Stated in the closing "What this evaluation cannot tell
  you yet" section as explicit sample-size guidance, following the
  CodeProbe walkthrough's default of 40 tasks.
- **Confidence**: emerging (specific sample-size recommendations
  attributed to the authors' "power analysis," without the power
  analysis itself being published in the post)
- **Quote**: "In our analysis, roughly 80 paired tasks was the statistical floor, while 200 provided a more defensible basis for a deployment claim." ... "Expand to at least 80 paired tasks before treating the measured effect as stable, and closer to 100 when retrieval quality is the primary endpoint, since that was the hardest effect to estimate precisely in our power analysis."
- **Our assessment**: This is concrete, actionable guardrail guidance
  against a common evaluation mistake: running a cheap, small pilot (the
  post's own CodeProbe default is 40 tasks) and treating its result as a
  stable effect estimate. The specific numbers (80 floor, 100 for
  retrieval-quality endpoints, 200 for deployment-grade claims) give
  readers a concrete target rather than a vague "run more trials"
  recommendation, though — consistent with the rest of this note's
  confidence grading — the underlying power analysis is not shown, so
  the exact thresholds should be treated as this corpus's directional
  guidance rather than a universally derived statistical requirement.

### Claim 12: Removing trivial tasks — prompts that name the answer's file, directory, or symbol outright — materially changes what an evaluation can measure, because cost win rate for structured retrieval fell monotonically as prompts revealed more about the answer's location
- **Evidence**: Presented as control #2 ("Remove trivial tasks") of the
  nine-control checklist, illustrated by a figure showing win rate by
  "instruction-leak bucket" (0% win rate for exact-path prompts, rising
  to 32% for behavioral-plus-dispersed prompts).
- **Confidence**: emerging (a stated monotonic relationship, illustrated
  by a bucketed win-rate figure with four categories; the underlying
  per-bucket sample sizes are not given in the accessible text)
- **Quote**: "Reject prompts that name the answer's file, directory, or symbol. In our corpus, cost win rate fell monotonically as prompts revealed more about the answer, so this filter materially changes what the evaluation can measure."
- **Our assessment**: This is a specific, falsifiable filtering rule
  (reject prompts naming the file/directory/symbol) rather than a vague
  "avoid easy tasks" instruction, and it is directly load-bearing for
  Claim 4's census finding (38% of the corpus named the path/symbol/
  directory outright) — those are exactly the tasks this control would
  strip out. A team that skips this filter risks diluting their own
  evaluation the same way the unfiltered 288-task corpus diluted this
  post's aggregate completion result.

## Concrete Artifacts

### The nine-control evaluation checklist (verbatim, numbered list from "Nine controls your evaluation needs")
```
Source: https://sourcegraph.com/blog/how-to-evaluate-sourcegraph-on-your-own-codebase

1. Choose real work. Mine merged pull requests, incidents, migrations,
   compliance investigations, and cross-service changes. Tasks mined from
   private repository history substantially reduce the risk that the model
   has already seen the task or its solution, but a real change is not
   automatically a valid evaluation task. [...] Check that each prompt
   states what the verifier enforces, that the tests accept functionally
   valid alternatives, and that the reference change is not the only
   solution that can pass.
2. Remove trivial tasks. Reject prompts that name the answer's file,
   directory, or symbol. In our corpus, cost win rate fell monotonically
   as prompts revealed more about the answer, so this filter materially
   changes what the evaluation can measure.
3. Pin the code. Both arms must reach the same repositories at the same
   revisions. When we audited this, tasks where the baseline was missing
   repositories showed a +0.091 reward delta, compared with -0.007 under
   full parity. The former measures having code rather than finding it.
4. Hold the agent constant. Use the same model, verifier, budgets,
   runtime, and task text in both arms. Keep the task instruction
   byte-identical. Any Sourcegraph-specific preamble or tool description
   is part of the treatment and should be recorded and published with the
   result.
5. Compare access methods. Compare baseline local search with
   Sourcegraph-assisted retrieval. For a substitution test, remove local
   source access rather than asking the agent to prefer Sourcegraph,
   because an agent can fall back under pressure and turn the experiment
   into a test of instruction-following. This isolation condition is for
   attribution, not necessarily the configuration you would use in
   production.
6. Repeat each task at least three times. Average runs within each task
   before comparing arms. Single-trial designs overstate deltas by 40% to
   60%, and within-task variance routinely exceeds the effect being
   estimated.
7. Measure the whole system. Record completion, retrieval, wall time,
   total tokens, total cost, search calls, and the amount of code entering
   context. Define the token-accounting boundary before the experiment and
   apply it identically to both arms. For implementation tasks, assign
   zero reward when the agent produces no required diff, so doing nothing
   cannot score the same as attempting the task and failing.
8. Segment before aggregating. Report easily localized tasks separately
   from dispersed and search-heavy ones. Pooling them can produce a number
   that answers neither deployment question.
9. Audit actual tool use. Configuration does not prove that the tool was
   available or adopted. Verify connectivity with observed tool calls,
   report zero-call trials as adoption or configuration failures, and
   separate them from analyses of retrieval capability.
```

### Result-interpretation table (verbatim, from "How to interpret the result")
```
Source: https://sourcegraph.com/blog/how-to-evaluate-sourcegraph-on-your-own-codebase

Result                                                    | What it likely means                                                                                   | What to do next
-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------
Better completion and lower cost                          | Strong evidence that Sourcegraph improves both capability and efficiency                               | Expand the evaluation and prioritize rollout
Equivalent completion with lower cost or latency          | Sourcegraph provides an efficiency advantage without reducing task quality                             | Deploy first to workflows with the largest savings
Better completion at higher cost                          | Sourcegraph enables work the baseline misses, but the added capability has a price                     | Decide whether the completion gain justifies the cost for that workflow
Better retrieval, equivalent completion, higher cost      | The agent finds more relevant code, but that improvement is not reaching the final outcome efficiently | Examine the invocation surface, result shaping, and task population
Gains concentrated in dispersed or search-heavy tasks     | The aggregate is hiding a workflow-specific advantage                                                  | Target Sourcegraph to those tasks rather than requiring a universal win
No gain and little baseline search activity               | The selected work may not require indexed retrieval                                                    | Add tasks with behavioral prompts, repository span, or important history
Large gains when the baseline lacks required repositories | The experiment measures access to information rather than retrieval quality                            | Restore repository and revision parity before interpreting the result
Lower cost with worse completion                          | The agent is doing less work, not necessarily working more efficiently                                 | Treat completion as the binding constraint and investigate the failure mode
Many zero-tool-call trials                                | The tools may be unavailable, poorly described, or not adopted by the agent                            | Diagnose connectivity and adoption before estimating retrieval capability
```

### CodeProbe CLI walkthrough (verbatim code block, from "Your first experiment, start to finish")
```
Source: https://sourcegraph.com/blog/how-to-evaluate-sourcegraph-on-your-own-codebase
Tool: CodeProbe (Sourcegraph, described as "still in alpha and is
currently being tested internally and with partners")

# 1. Can this repository produce valid tasks at all?
codeprobe assess /path/to/repo

# 2. Build 40 tasks from merged pull requests. Ground truth comes from two
#    independent backends; --no-llm keeps mining inside your boundary.
codeprobe mine /path/to/repo --org-scale --count 40 \
    --consensus-backends ast,grep --no-llm

# 3. Define the comparison and its two arms.
codeprobe experiment init /path/to/repo --name sourcegraph-eval

codeprobe experiment add-config <exp> \
    --label local-baseline --agent <agent> --model <model>   # arm 1: local search

codeprobe experiment add-config <exp> \
    --label sourcegraph --agent <agent> --model <model> \
    --mcp-config '<sourcegraph-config>' \
    --mcp-mode strict --hide-local-source scaffold           # arm 2: retrieval only

# 4. Price it before you run it, then run it.
codeprobe run <exp> --dry-run                   # projected cost, launches no agents
codeprobe run <exp> --repeats 3 --parallel 5    # 240 runs: 40 tasks x 2 arms x 3 repeats

# 5. Paired per-task deltas, plus the validity gate described below.
codeprobe interpret <exp> --format html
```

Two flag definitions given directly after the walkthrough, verbatim:
```
Source: https://sourcegraph.com/blog/how-to-evaluate-sourcegraph-on-your-own-codebase

"--mcp-mode strict preserves the configured retrieval tools and write
access while blocking local reads, grep, glob, and shell commands. This
is an experimental condition, not a recommended production configuration.
[...] strict mode also removes shell capabilities unrelated to retrieval.
Its result therefore measures the complete isolated tool surface, not the
retrieval backend alone."

"--hide-local-source scaffold replaces source files with zero-byte
placeholders at their original paths, then overlays the agent's edits
onto the real code before verification. The agent cannot inspect the
local implementation, but the verifier still evaluates a real
repository. Use hide instead when the required output is a text artifact
rather than a code change."
```

## Cross-References

- **Corroborates**: `blog-cursor-reward-hacking-benchmarks.md` Claim 6 and
  Claim 11 — that source independently found that harness configuration
  (history isolation, egress proxying) changes published SWE-bench Pro
  scores by 14-21 points for frontier models, and frames the goal of eval
  design as construct validity ("the benchmark measures what it claims to
  measure") rather than raw score correctness. This source's Claim 1
  (retrieval quality, completion, and cost are independently-moving
  measurements that must be reported separately) is the same underlying
  argument — a single aggregate number can be "real" in a narrow sense
  while not measuring what a reader assumes it measures — applied to
  retrieval-tool evaluation rather than benchmark-gaming detection. Both
  sources converge on "measure the harness, not just the score" as the
  operative discipline.
- **Corroborates**: `blog-cursor-reward-hacking-benchmarks.md` Claim 10 —
  that source's recommendation to "audit transcripts and constrain the
  eval environment" and "make the setup clear when they report results"
  is the same posture as this source's control #9 ("Audit actual tool
  use... report zero-call trials as adoption or configuration failures")
  and control #4 ("Any Sourcegraph-specific preamble or tool description
  is part of the treatment and should be recorded and published with the
  result"). Both sources treat harness transparency as a precondition for
  a trustworthy score, not an optional disclosure.
- **Corroborates**: `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 4 — that source states, as a general taxonomy, that "RAG systems
  are typically evaluated on: Retrieval relevance, Context coverage,
  Faithfulness, Hallucination rates" as a metric set distinct from
  task-completion metrics. This source is a concrete, quantified worked
  example of exactly that separation for a code-retrieval tool
  specifically (F1/recall as the retrieval-quality metrics, reward/pass
  rate as the completion metric, dollars as the cost metric), and adds
  the finding the Thoughtworks taxonomy does not: that these separately-
  tracked metrics can move in different directions on the same task set,
  which is the reason to keep them separate rather than just a
  classification convenience.
- **Extends**: `blog-anthropic-large-codebase-best-practices.md` Claim 2
  — that source argues Claude Code's own built-in navigation (agentic
  search: filesystem traversal, grep) is architecturally preferable to
  RAG-based embedding retrieval because embeddings go stale ("By the time
  a developer queries the index, it reflects the codebase as it existed
  days, weeks, or even hours ago"). This source is not in tension with
  that claim: it evaluates a different question — whether adding an
  external retrieval tool (the Sourcegraph MCP server) *on top of* an
  agent's baseline search behavior changes task completion or cost — not
  whether an agent's own built-in navigation mechanism should be
  agentic-search-based versus embedding-based. Read together, the two
  sources suggest a two-layer view: an agent's default navigation
  mechanism is a harness-architecture decision (Anthropic's claim), while
  whether a supplementary retrieval tool is worth deploying on top of
  that baseline is a separate, task-mix-dependent evaluation question
  (this source's claim) — the guide should not conflate "agentic search
  beats RAG for an agent's default navigation" with "structured retrieval
  tools never help," since this source's own data shows retrieval
  quality improved substantially even though completion did not move in
  aggregate.
- **Extends**: `blog-cursor-fast-regex-search.md` Claim 1 and Claim 12 —
  that source documents that grep/regex search latency is a first-order
  UX problem in large monorepos ("We routinely see rg invocations that
  take more than 15 seconds") and that the bottleneck is worst during
  investigation-type tasks specifically. This source's search-burden
  predictor (Claim 6: 20+ searches, 15+ file reads, 30+ turns, 75,000+
  tokens as the signal that a task will benefit from retrieval) gives a
  concrete, measurable definition of exactly the "investigation" task
  class that source names qualitatively — incident response, compliance
  investigations, migrations, and cross-repository tracing, per this
  source's own text. The two sources together suggest that fast local
  indexing (Cursor's fix) and structured cross-repo retrieval (this
  source's evaluation target) may be solving overlapping but not
  identical problems: Cursor's post is about making grep itself fast;
  this source is about whether an entirely different retrieval mechanism
  changes outcomes once grep is no longer the bottleneck.
- **Novel**: The specific 288-task F1/recall/completion/cost result
  (Claim 2, Claim 3); the retrieval-difficulty weighting scheme based on
  repository span and directory dispersion rather than line count (Claim
  5); the observed-search-burden predictor with the `domain-160`
  counter-example (Claim 6); the r = -0.57 cost-correlation finding
  (Claim 7); the repository-parity confound audit with the +0.091 vs.
  -0.007 delta (Claim 8); the 40-60% single-trial overstatement finding
  (Claim 9); OpenAI's ~30%-broken-tasks SWE-Bench Pro audit citation
  (Claim 10) — this is a distinct third-party validity finding from
  Cursor's own reward-hacking audit already in the corpus (see
  Corroborates above), naming task-construction validity rather than
  runtime answer-retrieval as a separate failure mode; the specific
  sample-size guidance (80 floor, ~100 for retrieval-endpoint precision,
  200 for deployment claims, Claim 11); and the CodeProbe CLI tool
  itself (Concrete Artifacts) are all new to this corpus. No existing
  source note provides a nine-control checklist or a result-
  interpretation table for evaluating a code-retrieval tool specifically.

## Guide Impact

- **Chapter 03 (Verification) — extend "Benchmark Scores Can Measure
  Retrieval, Not Coding"**: That section currently covers benchmark
  *gaming* (Cursor's reward-hacking audit: models retrieving known fixes
  during eval). This source adds a complementary, non-adversarial failure
  mode for the same underlying discipline: even an honest, non-gamed
  evaluation of a retrieval *tool* can mislead if it reports only one of
  retrieval quality, task completion, or cost. Recommend adding a new
  subsection — "A retrieval tool's own metrics can mislead" — citing
  this source's Claim 1 and Claim 2 (F1 2.6x up, completion flat) as the
  concrete illustration, and Claim 10 (OpenAI's ~30% SWE-Bench Pro
  task-validity audit) alongside the existing Cursor citation, since the
  two findings name distinct failure modes (broken tasks vs. gamed valid
  tasks) that the guide currently only covers one of.
- **Chapter 03 (Verification) — extend "Vendor Token Savings Claims Are
  Marketing Until You A/B Them"**: That section currently uses JetBrains'
  Caveman skill (65% claimed vs. 8.5% measured) as the worked example of
  why vendor efficiency claims require independent measurement. This
  source is a rare case of a vendor publishing its *own* rigorous
  methodology for A/B-testing its own product, including a checklist a
  reader can run against Sourcegraph itself. Recommend citing the
  nine-control checklist (Concrete Artifacts) as a template readers can
  apply to any vendor's retrieval/tooling claim, not just Sourcegraph's —
  the checklist's generality (pin the code, hold the agent constant,
  repeat 3x, segment before aggregating) is reusable independent of which
  vendor's tool is under test.
- **Chapter 03 (Verification) — new content on sample-size guidance for
  agent evaluations**: The guide does not currently have any concrete
  sample-size recommendation for internal agent A/B tests. Add Claim 9
  (single-trial designs overstate deltas 40-60%) and Claim 11 (80-task
  statistical floor, 200 for deployment claims) as concrete numeric
  guardrails, paired with a caveat that these are one vendor's directional
  findings from one corpus, not a derived statistical law.
- **Chapter 02 (Harness Engineering) — MCP tool selection**: If the guide
  adds guidance on evaluating whether to add an MCP server (code search,
  retrieval, or otherwise) to a team's harness, this source's Claim 6
  (instrument the baseline agent's own search burden — search count, file
  reads, turns, token consumption — before assuming a task needs a
  retrieval tool) is a concrete, generalizable diagnostic that applies
  beyond Sourcegraph specifically: any team deciding whether an MCP tool
  is worth its complexity should first measure how much their baseline
  agent already struggles, rather than assuming the tool helps uniformly.

## Extraction Notes

- **WebFetch summarization avoided for all quotes**: An initial WebFetch
  pass against this URL returned what appeared to be a full-text
  extraction, but per MINER.md §2a this Miner did not trust it for
  `Quote` fields. Instead, this Miner downloaded the raw page HTML via
  `curl` and located the article's embedded JSON `content` field (a
  server-rendered React page ships the full Markdown article body as a
  JSON string literal in the page source), extracted it, and decoded it
  with `json.loads` to correctly resolve JS string escapes while
  preserving UTF-8 characters (an initial naive `str.encode('utf-8').
  decode('unicode_escape')` pass corrupted a non-ASCII minus sign in one
  quote — re-done correctly with `json.loads`). Every `Quote` field in
  this note was copied character-for-character from that decoded,
  verbatim article text, not from the WebFetch summary. The two figure
  captions and the two `alt` texts describing the cost-scatterplot and
  instruction-leak charts were also recovered this way and are quoted
  directly where used.
- **One linked source not independently extracted**: The article's
  numbers derive from a companion, longer methodology post
  (`sourcegraph.com/blog/codescalebench-testing-coding-agents-on-large-codebases-and-multi-repo-software-engineering-tasks`,
  referred to in this post as "evaluating the Sourcegraph MCP server").
  This Miner confirmed the linked page loads and contains substantial,
  distinct content (a ~32,000-character methodology article describing
  CodeProbe's task-mining and benchmark-design rationale, including a
  named "git treachery" gaming incident the author encountered while
  building the benchmark) but did not extract it as part of this note,
  since it is a separate, independently substantial source that would
  need its own source-submission issue rather than being folded into
  this one. **Recommend filing a new source-submission issue for
  `sourcegraph.com/blog/codescalebench-testing-coding-agents-on-large-codebases-and-multi-repo-software-engineering-tasks`**
  — it appears to be the primary methodology source behind the 288-task
  numbers cited throughout this note and likely contains additional
  extractable claims (e.g., the "git treachery" agent-gaming incident is
  not covered anywhere in this note or, as far as this Miner can tell,
  elsewhere in the corpus).
- **No other sub-pages followed**: The post also links to a January 2026
  Medium post ("Rethinking coding agent benchmarks") by the same author
  and to OpenAI's SWE-Bench Pro audit ("Separating signal from noise:
  coding evaluations"). Neither was independently fetched for this note;
  the OpenAI citation (Claim 10) is graded `emerging` rather than
  `settled` in part because of this.
- **Confidence set to `emerging` overall**: Every quantitative claim in
  this note is first-party and self-reported by Sourcegraph, with no
  independent reproduction found by this Miner. The post is unusually
  candid for vendor content — its headline result does not favor the
  product on the metric most readers care about most (task completion)
  — which raises confidence relative to typical vendor marketing, but
  does not substitute for independent verification. No claim in this
  note is graded `settled`.
- **No contradiction filed**: This Miner considered whether this source's
  emphasis on "structured retrieval" conflicts with
  `blog-anthropic-large-codebase-best-practices.md`'s claim that agentic
  search (not RAG/embedding retrieval) is the right default for large
  codebases, and concluded it does not rise to a genuine contradiction —
  the two sources answer different questions (an agent's default
  navigation mechanism vs. whether a supplementary retrieval tool changes
  outcomes on top of that baseline), and this source never claims to be
  RAG/embedding-based. See Cross-References — Extends for the full
  reasoning. No contradiction issue was filed.
