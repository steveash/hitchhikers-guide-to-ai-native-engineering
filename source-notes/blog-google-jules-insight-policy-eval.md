---
source_url: https://developers.googleblog.com/measuring-what-matters-with-jules/
source_type: blog-post
title: "Measuring What Matters with Jules"
author: Nghi Bui, Georgios Evangelopoulos, Zack Elliott (Google — Jules/Google Labs research team)
date_published: 2026-06-22
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1676"
---

# Measuring What Matters with Jules

> Google's first-party account of an evaluation methodology for proactive (not
> just reactive) coding agents: grading an agent's "insight policy" against
> ground truth mined from real bug-fix history, with preliminary results
> (705 bugs, 1,178 CLs) showing exploration budget — not just the underlying
> model — drives diagnostic accuracy (Hit@5 jumps from 33% to 57% going from
> two to three exploration rounds).

## Source Context

- **Type**: blog-post (official Google Developers Blog, ~450 words, published
  June 22, 2026)
- **Author credibility**: Three named Google authors — Nghi Bui and Georgios
  Evangelopoulos, both credited as "Research Scientist," and Zack Elliott,
  credited as "Software Engineer." This is the research/engineering team
  behind Jules (Google's coding agent) writing about their own evaluation
  methodology and citing their own peer-reviewed-style paper, "Agentic Coding
  Needs Proactivity, Not Just Autonomy" (arxiv.org/abs/2605.06717). First-party
  and technically specific (named heuristics, a stated sample size, a stated
  scoring scale), but the results are explicitly preliminary and unaudited by
  anyone outside Google.
- **Scope**: Covers the conceptual shift from task-oriented to goal-oriented
  agent evaluation, the "insight policy" framing, the bug-clustering
  methodology for deriving evaluation ground truth, the preliminary
  eval-set construction (705 bugs / 1,178 CLs, internal Google codebases,
  up to 3 exploration rounds, LLM-judge scoring), and two headline results
  (single-round insight relevance; multi-round Hit@5 improvement). Does NOT
  cover: Jules' product features or UI, the underlying model architecture
  the agent runs on, the full statistical methodology of the LLM-judge
  scoring, or any evaluation on public (non-Google-internal) repositories —
  the post explicitly frames the public-GitHub extension as future work, not
  something already done.

## Extracted Claims

### Claim 1: Coding agents are shifting from reactive, task-completing assistants to proactive engines that must discover relevant information and surface insights before being asked
- **Evidence**: Opening framing statement of the post, presented as the
  authors' own characterization of where the field (and their own agent,
  Jules) is heading.
- **Confidence**: emerging (a framing/positioning claim from the team that
  builds Jules, not an externally validated industry trend measurement)
- **Quote**: "AI coding agents are rapidly shifting from reactive assistants
  that complete tasks when prompted to proactive engines that continuously
  absorb context, spot emerging risks, and surface diagnostic insights before
  developers have to ask."
- **Our assessment**: This is a vendor's own framing of its product direction,
  so it should be read as a positioning claim, not a measured fact about the
  industry. It is nonetheless a specific and falsifiable articulation of the
  reactive→proactive shift already gestured at elsewhere in the corpus (e.g.
  `blog-addyosmani-new-software-lifecycle.md` Claim 15's conductor/orchestrator
  distinction, and the async "orchestrator" agents named in that note's Linked
  Source B). What's new here is that Google explicitly ties this shift to a
  *measurement* problem: if agents are meant to work at the goal level, task-
  completion benchmarks cannot certify them as good at it.

### Claim 2: Public agent benchmarks (e.g. SWE-Bench) test task completion; no public benchmark exists for evaluating goal-oriented, proactive agent behavior
- **Evidence**: Direct statement contrasting SWE-Bench-style benchmarks with
  the "goals" framing the authors introduce.
- **Confidence**: emerging (an assertion about the state of public
  benchmarking, not independently audited against the full benchmark
  landscape, but directionally consistent with what SWE-Bench is designed to
  measure)
- **Quote**: "Public benchmarks like SWE-Bench test an agent's ability to
  complete tasks, like fixing a narrowly defined bug, but no benchmarks
  currently exist for goals."
- **Our assessment**: This is the load-bearing gap claim that motivates the
  rest of the post. It is a reasonable characterization of SWE-Bench (which
  is explicitly a bounded bug-fix/PR-resolution benchmark), and no source
  note currently in our corpus documents a public benchmark for proactive,
  goal-level agent behavior — so the claim holds as accurate relative to our
  corpus's existing knowledge, though we have not exhaustively surveyed every
  public benchmark to confirm the "no benchmarks currently exist" claim in
  full generality.

### Claim 3: Proactive agents should be graded on their "insight policy" — the ability to decide what matters, what evidence supports it, and whether to interrupt the developer or stay silent
- **Evidence**: The post's central conceptual contribution, attributed to the
  authors' own paper.
- **Confidence**: emerging (a named evaluation construct proposed by the
  authors; not yet an adopted industry standard)
- **Quote**: "In our most recent paper, Agentic Coding Needs Proactivity, Not
  Just Autonomy, we argue that proactive agents must be graded on their
  insight policy—the ability to decide what matters, what evidence supports
  it, and whether to interrupt the developer or stay silent."
- **Our assessment**: "Insight policy" is a genuinely new evaluation
  vocabulary term for our corpus — no existing source note names this
  construct. It decomposes agent judgment into three separable sub-skills
  (relevance detection, evidence-grounding, interruption timing), which is
  more actionable for a verification chapter than a single "is this a good
  agent" score. The "stay silent" option is notable: it explicitly treats
  under-interruption (missing something) and over-interruption (crying wolf)
  as symmetric failure modes, which most task-completion benchmarks have no
  mechanism to penalize at all.

### Claim 4: A companion architecture diagram frames the agent as continuously ingesting context and emitting one of four insight types — notify, question, draft, or stay silent — then learning from the developer's response
- **Evidence**: Figure caption accompanying the post's "overview-abstract"
  diagram.
- **Confidence**: emerging (architecture description via a figure caption,
  not elaborated in the article's prose)
- **Quote**: (no direct quote of body prose; this is the image caption text
  as rendered on the page: "The Figure above shows the design of a proactive
  agentic coding engine. Context streams into an engine that maintains
  development state and a developer model, emits insights (notify, question,
  draft, stay silent), and learns from response.")
- **Our assessment**: This is the concrete action taxonomy underlying the
  abstract "insight policy" concept in Claim 3 — it names four discrete
  output types an insight-policy evaluation would need to score, rather than
  a single interrupt/don't-interrupt binary. "Learns from response" also
  implies the architecture is meant to close the loop (developer reactions
  feed back into the agent's model of the developer), which the rest of the
  post's evaluation methodology does not directly measure — the described
  eval (Claim 6) grades insight quality against ground truth, not the
  learning-from-feedback loop itself.

### Claim 5: Ground truth for insight-policy evaluation can be built by clustering a team's real bug-fixing history using two heuristics — temporal proximity and semantic similarity
- **Evidence**: Named methodology, with a stated underlying hypothesis.
- **Confidence**: emerging (a proposed methodology backed by the preliminary
  results in Claim 7-8, but not yet validated at scale or on external data)
- **Quote**: "One way to build this 'ground truth' is to analyze a team's
  real bug-fixing history along two heuristics we term temporal proximity and
  semantic similarity. Our hypothesis is simple: when engineers file and fix
  several related bugs within a short time period, those bugs are often
  symptoms of a single underlying engineering effort."
- **Our assessment**: This is the most transferable methodological idea in
  the post, independent of Jules or Google's internal codebase — any team
  with bug-tracker history could in principle apply the same clustering
  heuristic to derive higher-level "aspirational goals" from a backlog of
  individually-filed bugs. It is a concrete answer to a real practical
  problem: how do you get labeled ground truth for "did the agent identify
  the right underlying problem" without hand-authoring goal statements for
  every historical bug.

### Claim 6: A worked example shows how the clustering method surfaces a higher-level goal from three individually narrow bugs
- **Evidence**: Concrete illustrative example given immediately after the
  methodology statement.
- **Confidence**: emerging (illustrative example, not a real case from the
  705-bug eval set — presented as explanatory, not as one of the measured
  data points)
- **Quote**: "A cluster of bugs around \"sandbox timeout errors,\" \"broker
  config failures,\" and \"network isolation flaky tests\" all point toward a
  common aspirational goal like \"Strengthen sandbox execution reliability.\"
  Individually, each bug is too task-specific to serve as a goal. Together,
  they reveal the higher-level objective."
- **Our assessment**: This example makes Claim 5's methodology concrete and
  checkable: it shows what a "cluster → goal" mapping looks like in practice.
  It is worth flagging to readers that this specific example is illustrative
  prose, not a reproduced data point from the 705-bug preliminary study
  described next — the Assayer or a future reader should not treat "Strengthen
  sandbox execution reliability" as one of the measured ground-truth targets.

### Claim 7: The preliminary eval set used 705 bugs (1,178 CLs) from internal Google codebases, with agents investigating a reverted pre-fix codebase for up to three rounds before being graded by an LLM judge on a 1-5 scale against ground-truth goals
- **Evidence**: Step-by-step methodology description in the post.
- **Confidence**: emerging (a specific, stated sample size and procedure —
  the strongest kind of evidence in this post — but the LLM-judge scoring
  methodology itself is not further detailed, e.g. no inter-rater reliability
  or judge-model identification is given)
- **Quote**: "To build our preliminary benchmark and test our hypothesis, we
  used 705 bugs (1,178 CLs) from internal Google codebases to: Cluster
  related historical bugs to reveal the higher-level \"aspirational goals\"
  ... Set the individual bugs within each cluster as our \"ground truth\"
  targets and reverted the codebase to its exact pre-fix state so the agent
  began where the human engineer did. Allow the agent to investigate the
  codebase for up to three rounds (its \"exploration budget,\" or N) before
  generating its final insights. Use an LLM to judge the agent's predicted
  insights from 1 (irrelevant) to 5 (exact match) against our \"ground truth\"
  targets. Measure success by tracking the agent's average top score and how
  often it successfully produced a highly accurate match (Hit@K)."
- **Our assessment**: This is the concrete evaluation protocol a practitioner
  could adapt: revert-to-pre-fix-state + capped exploration rounds + LLM-judge
  scoring + Hit@K reporting. The naming of "exploration budget (N)" as an
  explicit, controllable variable is the key methodological move — it turns
  "how much should the agent investigate before answering" into a tunable
  parameter with a measurable accuracy/cost tradeoff (see Claim 9), rather
  than an implicit agent behavior.

### Claim 8: On straightforward problems, a single exploration round was enough for the agent to identify a highly relevant insight, averaging 4.5 out of 5
- **Evidence**: Stated headline result for the single-round condition.
- **Confidence**: emerging (a specific, stated average score from the
  preliminary 705-bug study; not independently reproduced outside Google)
- **Quote**: "The core diagnostic logic works: Given a single exploration
  round, the agent consistently identified a highly relevant insight
  (averaging 4.5 out of 5). It successfully captured the primary signal for
  straightforward engineering problems."
- **Our assessment**: This establishes a ceiling case (easy problems, minimal
  exploration) before the post moves to the harder case in Claim 9. Taken
  alone it is a strong result, but "straightforward" is not independently
  defined in the post — we do not know what fraction of the 705-bug set was
  classified as straightforward versus complex, so this figure should not be
  read as the average performance across the whole eval set.

### Claim 9: Increasing the exploration budget from two rounds to three rounds raised Hit@5 accuracy on complex, multi-faceted problems from 33% to 57%
- **Evidence**: Stated headline result for the multi-round condition, with
  Hit@5 explicitly defined.
- **Confidence**: emerging (a specific, stated before/after percentage from
  the preliminary study — the single most citable quantitative claim in the
  post — but a two-point comparison from one internal study, not a
  systematically varied ablation across N=1..5+ or multiple codebases)
- **Quote**: "Complex, multi-faceted problems are naturally harder, but giving
  the agent more resources to investigate pays off. By increasing the
  exploration budget from two rounds to three, the agent's Hit@5 accuracy
  (defined as the rate at which a correct diagnostic insight appears within
  its top 5 recommendations) rebounded significantly from 33% to 57%. This
  proves that extra passes directly help the agent uncover secondary signals
  it initially missed."
- **Our assessment**: This is the headline quantitative result of the post
  and the clearest evidence for a specific, actionable claim: for proactive/
  diagnostic agent tasks, exploration budget is a first-order lever on
  quality, distinct from model choice. The word "rebounded" implies Hit@5 was
  presumably lower still at N=1 for complex problems (not stated), and the
  post does not report results beyond N=3, so we don't know whether the
  33%→57% trend continues, plateaus, or reverses with further rounds. The
  authors' own causal language ("This proves...") is stronger than a
  two-point before/after comparison actually supports — we'd downgrade
  "proves" to "is consistent with" until a fuller ablation is published.

### Claim 10: Google plans to expand this evaluation methodology to public GitHub data and to richer context sources (issue trackers, conversations, design documents) beyond the codebase alone
- **Evidence**: Stated future-work section.
- **Confidence**: anecdotal (a stated intention, not a committed roadmap with
  dates)
- **Quote**: "These are preliminary results on an initial sample, and we are
  actively expanding coverage on multiple fronts. To start, we are expanding
  this evaluation to public GitHub data (issues and resolving PRs) to make
  this methodology broadly applicable to the wider AI community. We are also
  exploring how to ingest richer context streams like issue trackers,
  conversations, and design documents beyond just the codebase."
- **Our assessment**: This signals that the 705-bug/1,178-CL study is
  explicitly not the final form of this benchmark — practitioners should
  expect a public, GitHub-sourced version of this eval to appear later, which
  would be independently reproducible in a way the internal-codebase study
  is not. Worth flagging for future source-scanning: watch for a follow-up
  Google post or paper revision that reports results on public data.

## Concrete Artifacts

```
Source: developers.googleblog.com/measuring-what-matters-with-jules/ (June 22, 2026)

Preliminary Insight-Policy Eval Protocol (Google / Jules team)

Sample:        705 bugs (1,178 CLs), internal Google codebases
Ground truth:  Clusters of related bugs (temporal proximity + semantic
               similarity heuristics) → inferred "aspirational goal" per
               cluster
Setup:         Codebase reverted to exact pre-fix state per bug/cluster
Exploration:   Agent allowed up to 3 investigation rounds ("exploration
               budget," N) before producing final insights
Scoring:       LLM judge, 1 (irrelevant) to 5 (exact match), predicted
               insight vs. ground-truth goal
Metrics:       Average top score; Hit@K (rate of a highly accurate match
               appearing in top-K predictions)

Headline Results:
  Single exploration round, straightforward problems:  avg. 4.5 / 5
  Complex problems, N=2 rounds:                          Hit@5 = 33%
  Complex problems, N=3 rounds:                          Hit@5 = 57%
```

```
Source: same post — figure caption for "overview-abstract" diagram

Proactive agentic coding engine architecture (as captioned):
  Context streams in → engine maintains development state + a developer
  model → engine emits one of: {notify, question, draft, stay silent} →
  engine learns from the developer's response.
```

```
Source: same post — paper reference

Paper: "Agentic Coding Needs Proactivity, Not Just Autonomy"
Authors: Google Labs / Jules research team (paper cited, not separately
         fetched for this note)
URL: https://arxiv.org/abs/2605.06717  (PDF: https://arxiv.org/pdf/2605.06717)
Follow-up: http://labs.google/code
```

## Cross-References

- **Corroborates**: `blog-cursor-real-time-rl.md` Claim 1 and Claim 7 — that
  note documents Cursor's argument that production/real-user signal is
  qualitatively different from synthetic evaluation signal ("the user cannot
  be faithfully simulated"), and that longer-horizon agentic tasks will need
  "less frequent but crisper" feedback evaluated on complete outcomes rather
  than individual edits. This source's ground-truth methodology (mining real
  bug-fix history rather than hand-authoring synthetic goals) is a concrete,
  independently-arrived-at instance of the same principle: grounding
  evaluation in real historical developer work product rather than
  synthetic benchmarks. Neither post cites the other; the convergence is
  independent.
- **Extends**: `blog-addyosmani-new-software-lifecycle.md` Claim 6 (the
  output-eval/trajectory-eval decomposition of "evals," attributed to
  Osmani's co-authored Google whitepaper) — that claim splits verification
  into "did the agent get the right answer" (output) versus "was the path
  it took sound" (trajectory). This source's "insight policy" grading is a
  third, more specific axis for a particular class of agent (proactive/
  diagnostic, not task-executing): not just "was the final insight correct"
  but "did the agent decide correctly whether to say anything at all." The
  guide should treat insight-policy grading as a specialization of output
  evaluation for proactive agents, not a wholesale alternative to the
  output/trajectory split.
- **Extends**: `blog-google-io-2026-developer-keynote.md` Claim 6 (Android
  Bench, a domain-specific LLM leaderboard for Android development tasks) —
  that note documents Google building task-domain-aligned evaluation as an
  alternative to general coding benchmarks. This source is a second,
  independent instance of the same institutional pattern (Google building
  bespoke evaluation infrastructure rather than relying on SWE-Bench-style
  general benchmarks), but for a different axis: domain specificity (Android
  Bench) versus behavioral-mode specificity (task-oriented vs. goal-oriented,
  this source). Neither note documents Jules elsewhere — per that note's
  Extraction Notes, "Jules coding agent... appears in triage comments as a
  potential extraction target" but was not found in the I/O keynote article;
  this source is the first in the corpus to substantively cover Jules.
- **Novel**: This is the first source note in the corpus to document: (1) the
  "insight policy" evaluation construct for proactive coding agents; (2) a
  concrete methodology for deriving agent-evaluation ground truth from a
  team's real bug-fixing history via temporal-proximity + semantic-similarity
  clustering; (3) "exploration budget" (capped investigation rounds before
  final output) as an explicit, measured lever on agent output quality,
  distinct from model capability; and (4) Hit@K as an agent-evaluation metric
  in our corpus (previously used only in retrieval/ranking contexts
  elsewhere, not agent diagnostic evaluation).

## Guide Impact

- **Chapter 03 (Verification)**: Add "insight policy" as a named evaluation
  construct for proactive/diagnostic agents, distinct from task-completion
  benchmarks (SWE-Bench-style) and from the output-eval/trajectory-eval split
  already documented via `blog-addyosmani-new-software-lifecycle.md` Claim 6.
  Specific recommendation: for any agent designed to work proactively (surface
  issues, flag risks, suggest goals) rather than execute a well-defined task,
  task-completion metrics alone will not certify quality — the guide should
  recommend evaluating relevance (does the insight matter), evidence-grounding
  (is it backed by real signal), and interruption timing (notify vs. stay
  silent) as three separable sub-dimensions, per this source's framing.

- **Chapter 03 (Verification) — ground truth methodology**: Add the
  temporal-proximity + semantic-similarity bug-clustering technique (Claim 5,
  Claim 6) as a concrete, replicable recipe for teams that want to build their
  own goal-oriented agent eval without hand-authoring ground truth: mine your
  own bug tracker for temporally- and semantically-clustered bug groups, treat
  the cluster's common thread as the "goal," and revert the codebase to
  pre-fix state as the agent's starting point.

- **Chapter 02 (Harness Engineering)**: Add "exploration budget" (Claim 7,
  Claim 9) as a named, tunable harness parameter with a measured
  accuracy/cost tradeoff, alongside existing harness-engineering content on
  context and tool configuration. Specific recommendation: when a proactive
  or diagnostic agent underperforms, exploration-round budget is a lever to
  test before concluding the model or prompt is at fault — this source's
  33%→57% Hit@5 jump (two to three rounds) is a concrete illustration that
  more investigation, not a different model, closed most of the gap on
  complex problems.

- **Chapter 01 (Daily Workflows)**: Note Jules' explicit framing (Claim 1,
  Claim 4) of proactive-agent output as one of four discrete actions —
  notify, question, draft, stay silent — as a useful vocabulary for
  describing what a "background" or "async" agent should be allowed to do
  short of an outright code change, complementing the conductor/orchestrator
  mode distinction already in the guide via `blog-addyosmani-new-software-lifecycle.md`.

## Extraction Notes

- Initial fetch via the WebFetch tool returned a summarized version of the
  article (including two author-title fabrications not present in the actual
  byline text, e.g. implying titles were quoted from prose when they were
  actually rendered as separate byline `<span>` elements). Per MINER.md §2a,
  this summarized version was not used as a quote source. Instead the full
  page was fetched with `curl` (browser user-agent) and the article body was
  located and extracted directly from the raw HTML (`<div class="inner-block-
  content rich-content">` blocks), which is the complete article text — the
  post is short (~450 words) and every paragraph was read and checked
  character-for-character against the HTML before quoting.
- The post is short and single-page; no internal links to substantive
  sub-pages were present other than the cited arXiv paper (not separately
  fetched for this note — flagged as a natural follow-up source, since it
  would contain the full statistical methodology, e.g. inter-rater
  reliability of the LLM judge, that this blog-post digest omits) and the
  `labs.google/code` follow-along link (a landing page, not a substantive
  standalone source).
- No contradictions identified against existing source notes. This source
  introduces a new evaluation construct (insight policy) that sits alongside,
  rather than opposes, the output/trajectory eval split already in the corpus
  via `blog-addyosmani-new-software-lifecycle.md` — see Cross-References →
  Extends for how the two relate.
- All cross-referenced claim numbers (from `blog-cursor-real-time-rl.md`,
  `blog-addyosmani-new-software-lifecycle.md`, and
  `blog-google-io-2026-developer-keynote.md`) were verified by re-reading each
  cited note's actual numbered claims before writing this note.
