---
source_url: https://cognition.com/frontiercode
source_type: blog-post
title: "FrontierCode Leaderboard / Introducing FrontierCode / FrontierCode 1.1"
author: The Cognition Team (leaderboard page); "Introducing FrontierCode" byline: Eric Lu, Ben Pan, Deniz Birlikci, Sam Lee, Ray Wang, Rohan Choudhury, Fermi Ma, TC Qin, Carlo Baronio, Silas Alberti, and more; "FrontierCode 1.1" byline: Eric Lu, Ben Pan, Fermi Ma, Alex Lombardi, Deniz Birlikci, Sam Lee, Ray Wang, Rohan Choudhury, TC Qin, Carlo Baronio, Jacob Teo, Joon Hee Lee, Silas Alberti, and more
date_published: 2026-06-08
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: emerging
issue: "#2176"
---

# FrontierCode: Cognition's "mergeability" benchmark for production code quality

> Cognition's own benchmark measuring whether a maintainer would actually
> merge an agent's PR — built with 36 open-source maintainers who each spent
> 40+ hours per task, evaluated via novel non-LLM-judge grading techniques
> (reverse-classical tests, scope enforcement, adaptive classical grading),
> and revised in version 1.1 to add an internet-use anti-cheating safeguard
> and deprecate the noisy "Diamond" hardest-task subset.

## Source Context

- **Type**: blog-post / live benchmark leaderboard (Cognition's own site,
  cognition.com). This note covers three linked pages treated as one source:
  the live leaderboard at `/frontiercode` (undated, "By The Cognition Team"),
  the original methodology post "Introducing FrontierCode" at
  `/blog/frontier-code` (published 2026-06-08, byline: Eric Lu, Ben Pan,
  Deniz Birlikci, Sam Lee, Ray Wang, Rohan Choudhury, Fermi Ma, TC Qin, Carlo
  Baronio, Silas Alberti, and more), and the revision post "FrontierCode 1.1"
  at `/blog/frontier-code-1.1` (published 2026-07-07, overlapping byline plus
  Alex Lombardi, Jacob Teo, Joon Hee Lee). The leaderboard page links directly
  to both blog posts ("Read the methodology" anchors to its own in-page
  methodology section; the two revision cards link to the dated posts), so
  per `agents/MINER.md` §1 these were followed as substantive linked pages.
- **Author credibility**: First-party vendor content from Cognition, the
  company that builds and sells Devin (an autonomous coding agent). Named,
  individual research-team authors (not an anonymous corporate byline) on
  both methodology posts, which is a stronger attribution than the
  leaderboard page's generic "By The Cognition Team." Cognition has a
  commercial interest in FrontierCode being perceived as rigorous (it
  doubles as a marketing artifact for Devin/SWE-1.x model quality), but the
  methodology disclosure is unusually detailed and includes named external
  validation: four named maintainers of specific open-source projects
  (Celery, Budibase, uppy, Mattermost) with attributed testimonial quotes,
  and a footnoted external citation to METR's independent research finding
  that many SWE-bench-passing PRs would not actually be merged. No
  independent (non-Cognition) audit of FrontierCode's own grading accuracy
  claims was found during this extraction.
- **Scope**: Covers the benchmark's definition of "mergeability," its
  six-axis grading criteria, three novel grading techniques (reverse-classical
  tests, code-scope enforcement, adaptive classical grading via a tool called
  "mutagent"), the task-authoring and five-step QC/review process, the
  three-tier task-difficulty structure (Extended/Main/Diamond), original
  (1.0) launch results by model, the 1.1 revision's internet-use
  anti-cheating methodology (and the blocklist/allowlist approaches it
  rejected), the deprecation of the Diamond subset, and the current live
  leaderboard standings. Does NOT cover: the underlying task text/content
  (not released publicly, to avoid contamination), exact per-task rubric
  weightings, cost/speed metrics for the leaderboard models (the page's
  marketing copy mentions comparing "cost, and speed" but the fetched
  leaderboard data — sourced from the page's embedded JSON-LD — contains
  only model name, rank, and score, not cost/speed columns), or any
  independent replication of Cognition's reported scores.

## Extracted Claims

### Claim 1: FrontierCode is framed as the first benchmark to measure "mergeability" — whether a maintainer would actually merge the agent's PR — assessed via an ensemble of grading techniques across five quality dimensions
- **Evidence**: Identical framing sentence appears verbatim on both the
  leaderboard page and the original methodology post's summary bullet.
- **Confidence**: settled (this is the source's own stated definition of
  what it measures, not an external empirical claim requiring
  verification)
- **Quote**: "FrontierCode is the first benchmark to measure mergeability: would the maintainer actually merge this PR?"
- **Quote (methodology post, near-identical restatement)**: "Would the maintainer actually merge this PR? We're the first benchmark to measure code mergeability. Our criteria assess end-to-end code quality — correctness, test quality, scope discipline, style, and adherence to codebase standards. This employs a novel ensemble of grading techniques, including unit tests, rubrics, and new types of verifiers."
- **Our assessment**: "Mergeability" as the grading standard — rather than
  "does it pass the tests" — is the core methodological bet of this source.
  It directly operationalizes METR's finding (cited by FrontierCode's own
  footnote — see Claim 12) that many SWE-bench-passing PRs would not
  actually be merged: FrontierCode's response is to have the actual
  maintainers who would make that merge decision author and grade the
  tasks, rather than relying on unit-test pass/fail as a correctness proxy.

### Claim 2: FrontierCode grades code along six named axes: behavioral correctness, regression safety, mechanical cleanliness, test correctness, scope, and code quality
- **Evidence**: Explicit bulleted list under the "Beyond Unit Tests" section
  heading of the original methodology post.
- **Confidence**: settled (direct statement of the grading taxonomy)
- **Quote**: "Behavioral correctness: Does the patch successfully solve the problem?" / "Regression safety: Does it break anything in the existing codebase?" / "Mechanical cleanliness: Does it pass the project's build, lint, and style checks?" / "Test correctness: Do the agent's tests actually capture the desired behavior?" / "Scope: Does the patch touch only what it needs to?" / "Code quality: Does the code conform to codebase conventions, follow sound design patterns, and remain readable to collaborators?"
- **Our assessment**: This is a more granular, six-axis breakdown than the
  leaderboard page's five-item summary ("correctness, test quality, scope
  discipline, style, and adherence to codebase standards") — the two lists
  overlap substantially (test correctness ≈ test quality, mechanical
  cleanliness + code quality ≈ style/codebase standards) but the
  methodology post's version separates "regression safety" as its own axis,
  which the summary bullet doesn't name explicitly. Useful as a citable,
  reusable rubric skeleton for teams building their own agent-PR grading
  criteria, independent of FrontierCode's specific implementation.

### Claim 3: FrontierCode introduces three grading techniques beyond standard unit tests: reverse-classical tests (agent-written tests must fail on the original broken codebase), scope enforcement (files/size/semantic constraints on what a patch may touch), and adaptive classical grading via an internal tool called "mutagent" that uses an LLM to align rigid test environments with an agent's specific implementation choices
- **Evidence**: Named, defined under the "Novel Grading Methods" section
  heading, each with an explicit mechanism description.
- **Confidence**: emerging (first-party description of internal tooling;
  no external validation of how well these techniques actually reduce
  misclassification beyond the aggregate 81% figure in Claim 6)
- **Quote**: "Reverse-Classical: The reverse-classical criterion is a way to ensure that agent-written tests are meaningful: when we run them on the original, broken codebase, they must fail. This gives us an automated, deterministic check that the agent understood the problem well enough to write an effective test for it."
- **Quote (scope)**: "Code Scope: A good PR should exercise restraint: it modifies only what it needs to, without touching unrelated files or introducing unnecessary refactors. The scope criterion is an automated check that enforces these boundaries. It combines three types of constraints: files: For fast, deterministic checks on which files can be allowed, denied, or must be deleted. size: To enforce limits on the number of changed lines, net line growth, or total files modified. semantic: For LLM-based checks that verify the locality or nature of a change within a specific part of a file (e.g., inside a single function)."
- **Quote (adaptive classical grading / mutagent)**: "Adaptive Classical Grading: Open-ended coding tasks can have many valid solutions. Static unit tests are too rigid; good solutions can fail for superficial differences like function names or error wording. We resolve this conflict with mutagent, a tool we built that uses an LLM to surgically patch the test environment (or the application code) and align with the agent's implementation details, allowing us to run rigorous, deterministic tests on open-ended solutions."
- **Our assessment**: The reverse-classical-test technique is the most
  novel and transferable idea in this source: requiring an agent's own
  test to fail against the pre-fix code is a cheap, automated, deterministic
  proxy for "did the agent actually understand the bug," distinct from and
  complementary to whether the test passes against the fix. The
  files/size/semantic scope taxonomy is a concrete, reusable checklist for
  any team building their own "did the agent stay in scope" gate. Mutagent
  (an LLM that patches the test harness itself to match an agent's
  legitimate implementation variance) is a specific engineering answer to
  the general "rigid unit tests reject valid alternative solutions" problem
  that `blog-cursor-cursorbench.md` Claim 1 and Claim 7 (agentic graders for
  open-ended tasks) also identify — see Cross-References.

### Claim 4: FrontierCode tasks are authored by the maintainers of 36 flagship open-source repositories, each spending 40+ hours per task, so that the people who would actually approve or reject the PR define the grading standard
- **Evidence**: Direct statement plus four attributed maintainer
  testimonials naming the maintainer, their role, and their project's star
  count.
- **Confidence**: settled (specific, named, checkable claim — the
  maintainers and projects are identified, which is a stronger evidentiary
  standard than an anonymous "expert reviewers" claim)
- **Quote**: "FrontierCode aims to measure whether models can produce code that would be merged into production codebases. To ensure this, we collaborated directly with the maintainers of 36 flagship open-source repositories. This team of all-star experts has collectively reviewed and merged thousands of commits to their codebases."
- **Quote (task investment)**: "20+ world-class open-source developers built realistic, diverse, and challenging coding tasks from the repos they maintain, spending more than 40 hours per task. They define what "mergeable" means in their repo."
- **Quote (maintainer testimonial, Celery)**: "Working with the team behind FrontierCode was a privilege. Taking on the AI evaluation problem felt like nothing less than an art… Where others grade like a CI, FrontierCode grades like a tech lead." — Tomer Nosrati, CEO and Tech Lead of Celery (28.6k stars)
- **Quote (maintainer testimonial, Budibase)**: "What sets FrontierCode apart is the attention to detail. Each task is calibrated to a depth that simply hasn't been seen before in LLM benchmarking. We should be moving away from benchmarks that can be gamed and instead using ones like FrontierCode to demonstrate genuine model intelligence and creativity." — Martin McKeaveney, Co-Founder and CTO of Budibase (28k stars)
- **Our assessment**: Note the two figures given for maintainer count are
  slightly inconsistent across the two pages: the leaderboard/summary bullet
  says "20+ world-class...developers," while the methodology post's "A Team
  of Open Source Maintainers" section says "36 flagship open-source
  repositories" — these may refer to different counts (maintainers vs.
  repositories, since one maintainer could cover multiple repos, or the
  benchmark may have grown from 20+ to 36 between when the summary bullet
  and the detailed section were last edited) but the source does not
  reconcile them explicitly. Cite the specific "36 flagship open-source
  repositories" figure from the detailed methodology section as the more
  precise number. The "grades like a tech lead" framing (McKeaveney's and
  Nosrati's quotes) is a strong, quotable articulation of what
  maintainer-authored grading is trying to capture that a CI/unit-test gate
  structurally cannot: judgment about design fit, not just pass/fail.

### Claim 5: Task quality control runs through a five-step process per task — design, hack report (adversarial red-teaming by the task author and by Devin), rubric calibration (four solutions spanning 0–100% score), pod-lead review, and Cognition-researcher final review — with tasks cycling through multiple revision rounds
- **Evidence**: Explicit numbered five-step list under "Our rubric creation
  process."
- **Confidence**: emerging (detailed first-party process description; no
  data on average revision-round count or task rejection rate)
- **Quote (hack report)**: "To prevent false positives, the task author imitates a lazy or adversarial programmer and tries to get a passing score with a deliberately incorrect or incomplete solution. This exposes criteria that can be improved. To prevent false negatives, the task author tries to write a perfectly valid, alternative solution that is different from the canonical one. If this solution fails the evaluation, the rubric is too rigid."
- **Quote (Devin red-teaming)**: "We augment the hack report process by also asking Devin to come up with novel ways to hack the rubric."
- **Quote (calibration)**: "To ensure that the rubric has sufficient resolution, the author must write four distinct solutions that target a range of scores from 0 to 100%."
- **Quote (review)**: "Each contributor belongs to an eval pod led by an experienced pod lead, who acts as the first quality gate. The lead reviews the full eval candidate and iterates with the contributor through multiple rounds. Once the eval candidate passes all pod-level checks, a Cognition researcher conducts a final review along with the pod lead and contributor."
- **Our assessment**: Using the coding agent itself (Devin) as an
  adversarial red-teamer against its own benchmark's rubric is a notable,
  self-referential quality-control technique not seen elsewhere in this
  corpus — it means the rubric is stress-tested against exactly the kind of
  reward-hacking behavior the benchmark is trying to catch, before any
  external model is graded on it. The four-solutions-across-0-100%
  calibration step is a concrete, transferable technique for any team
  building rubric-graded (rather than binary pass/fail) evals: it forces
  the rubric to have real resolution across the score range, not just at
  the extremes.

### Claim 6: FrontierCode reports 81% fewer misclassification errors ("false positive rate") than SWE-Bench Pro, based on trajectory-level analysis, and characterizes its own scores as "the most accurate ranking currently available"
- **Evidence**: Two separate statements of the same underlying ~81%
  figure — one in the hero-summary bullet list (framed specifically as
  false-positive rate vs. SWE-Bench Pro) and one in the body text near a
  chart image (framed more generally as misclassification errors vs.
  "other leading benchmarks").
- **Confidence**: anecdotal (Cognition's own comparative claim about its own
  benchmark's accuracy relative to a competitor benchmark; the underlying
  trajectory analysis, sample size, and methodology for computing this
  percentage are not disclosed in the fetched content, and no independent
  party has verified it)
- **Quote (summary bullet)**: "Rigorous quality control. Rubric grading is subjective, so we built an extensive QC pipeline with adversarial testing, calibration, and multi-stage review, where every task is manually reviewed by a Cognition researcher. We achieve an 81% lower false positive rate compared to SWE-Bench Pro."
- **Quote (body text)**: "We show through analysis of agent trajectories that FrontierCode produces 81% less misclassification errors than other leading benchmarks. This means that FrontierCode scores are the most accurate ranking currently available."
- **Our assessment**: The two statements are not identical in scope — one
  names SWE-Bench Pro specifically as the comparison point and "false
  positive rate," the other says "other leading benchmarks" generally and
  "misclassification errors" (which would include both false positives and
  false negatives) — and it isn't clear from the fetched text whether these
  describe the same measurement stated two ways or two different
  measurements that happen to share the same headline number. Treat "81%"
  as a notable but unverified self-reported comparative claim, not a
  peer-reviewed or reproducible statistic. This is directly relevant to
  `blog-cursor-cursorbench.md` Claim 1's "grading problems" failure mode
  (public benchmarks either penalize valid alternative solutions or add
  synthetic constraints) — FrontierCode's specific counter-claim is that its
  own techniques (Claim 3, Claim 5) measurably reduce exactly this failure
  mode relative to SWE-Bench Pro.

### Claim 7: FrontierCode 1.0 launched with three nested task-difficulty subsets — Extended (150 tasks), Main (100 tasks, the 100 hardest of Extended), and Diamond (50 tasks, the hardest of Main) — with Diamond reported as unsaturated at launch: best model Claude Opus 4.8 scored only 13.4%, versus GPT-5.5 at 6.3% and Gemini 3.1 Pro at 4.7%; the best open-source model, Kimi K2.6, scored 3.8% on Diamond, 16% on Main, and 37% on Extended
- **Evidence**: Direct statement of subset structure and a specific results
  paragraph from the original ("Introducing FrontierCode," 2026-06-08)
  methodology post.
- **Confidence**: settled for the subset structure (a direct methodology
  statement); emerging for the specific percentage figures (self-reported
  results, not independently reproduced, though specific and falsifiable)
- **Quote (subsets)**: "We present three nested subsets of FrontierCode at increasing difficulty: Extended, Main, and Diamond. Diamond comprises the 50 hardest tasks, Main the 100 hardest (including Diamond), and Extended the full set of 150."
- **Quote (Diamond results)**: "FrontierCode Diamond remains unsaturated: the best performing model, Claude Opus 4.8, achieves a score of only 13.4%. Other models score significantly lower: GPT-5.5 receives 6.3%, Gemini 3.1 Pro 4.7%, and others even less."
- **Quote (Main/Extended results)**: "On FrontierCode Main and Extended, Opus 4.8 still maintains a clear lead, at 34.3% and 51.8%, respectively. We also observe a large gap between open-source models and the frontier. Kimi K2.6, the best-performing open-source model, achieves just 3.8% on Diamond, 16% on Main and 37% on Extended."
- **Our assessment**: This 13.4%-for-Opus-4.8-on-Diamond figure is
  independently significant for this corpus: it is the exact number cited
  as the unnamed "second-best" score in `blog-latentspace-fable-5-mythos-launch.md`
  Claim 3 ("FrontierCode Diamond: Mythos 5 30.9% vs second-best 13.4%," from
  a June 10, 2026 digest — two days after this 2026-06-08 post). The number
  match (13.4% in both) is precise enough that it is very likely the same
  figure — this note's primary-source data most likely identifies Cognition's
  own launch-day "second-best" reference point in that AINews claim as
  Claude Opus 4.8. See Cross-References for the full three-way corroboration
  with a third corpus note.

### Claim 8: FrontierCode 1.1 (2026-07-07) rejected both blocklisting and allowlisting of internet domains as impractical anti-cheating mechanisms, settling instead on a prompt defining fair internet use plus a classical verifier that detects and zeroes runs that consult "solution-bearing sources" (e.g., the original upstream PR)
- **Evidence**: Direct description of two rejected alternatives (with a
  specific domain-count figure for the blocklist attempt) and the
  two-safeguard design that replaced them, from the "FrontierCode 1.1" post.
- **Confidence**: emerging (first-party account of an internal design
  iteration, with specific quantitative detail — domain count, turn count,
  post-fix unfair-use rate — but no external verification of these figures)
- **Quote (blocklist rejected)**: "Blocklisting turned out to be impractical. Over several iterations of blocking domains and inspecting agent trajectories, our blocklist grew to roughly 1,200 domains, and agents kept finding new workarounds, sometimes spending 20+ turns fighting the blocklist before solving the task themselves. Blocking sites also breaks honest workflows, since sites like GitHub are sometimes legitimately required"
- **Quote (allowlist rejected)**: "Allowlisting has the inverse problem: it requires anticipating every site an agent might legitimately need and building a custom allowlist per task, which doesn't scale. It also distorts agent behavior either way: if the allowlist is visible to the agent, it steers the agent toward the listed sites; if it is hidden, the agent either concludes the internet is broken or wastes effort probing which s[ites are reachable]"
- **Quote (final design)**: "FrontierCode 1.1 implements this as two safeguards: a prompt that explains what fair internet use is, and a classical verifier that detects unfair internet use and zeroes out those runs. The prompt alone is currently sufficient to essentially eliminate unfair internet use; the verifier confirms this and will catch any future deviations."
- **Quote (result)**: "Adherence to the prompt is remarkably good: with it in place, unfair internet use rates fall below 1% for every model we evaluated."
- **Quote (leaderboard summary, restricts what)**: "FrontierCode also restricts internet usage. Models may use the internet the way an engineer would, reading documentation and searching for error messages, but runs that consult solution-bearing sources such as the original pull request are detected and scored zero."
- **Our assessment**: This is a specific, well-documented negative result
  (two rejected approaches, with concrete failure detail — a 1,200-domain
  blocklist still got bypassed, sometimes after 20+ turns of an agent
  actively fighting the blocklist) as well as a positive result (prompt +
  classifier drove unfair use below 1%). This is directly relevant to
  `blog-cursor-reward-hacking-benchmarks.md` Claim 3 (upstream lookup —
  models retrieving merged PRs or fixed source files from the public web —
  named as the single most common benchmark-hacking mechanism Cursor
  found) and Claim 9 (Cursor's own fix: egress proxying, i.e. network-level
  allowlisting of package registries). The two vendors converge on the same
  underlying threat (agents finding the answer online) but diverge on
  mechanism: Cursor's published fix is exactly the network-level allowlist
  approach that Cognition explicitly tried and rejected as impractical at
  benchmark scale. This is a genuine, named methodological divergence
  between two independent organizations solving the same problem — worth
  flagging prominently, though it does not meet the `agents/MINER.md` §4a
  bar for a formal contradiction issue, since the two sources are not
  making opposed factual claims about the same system; they are reporting
  different design choices in different systems, each defensible in its own
  context (Cursor's live-traffic production sandbox vs. Cognition's
  benchmark-authoring pipeline with maintainer-curated task sets).

### Claim 9: Cognition deprecated the Diamond subset in FrontierCode 1.1, reporting scores going forward only for Main and Extended, because the hardest-task solve rates are so low that Diamond performance is "inherently noisy" and Diamond no longer reflects the actual 50 hardest tasks under the 1.1 methodology changes
- **Evidence**: Direct statement under a dedicated "Deprecating FrontierCode
  Diamond" subsection heading in the 1.1 post.
- **Confidence**: settled (a direct first-party statement of a methodology
  change and its stated rationale, not an empirical claim requiring
  external verification)
- **Quote**: "As described in our original blog post, Diamond consists of the 50 hardest tasks in our full 150-task Extended set, while Main consists of the 100 hardest. With the FrontierCode 1.1 updates, the Diamond set no longer reflects the 50 hardest tasks. Moreover, because the solve rates of the hardest tasks are so low, we have determined that Diamond performance is inherently noisy. As a result, we are deprecating the Diamond set"
- **Quote (leaderboard changelog)**: "Also audits blocker criteria and deprecates the Diamond subset."
- **Our assessment**: This directly affects how the guide (and any
  downstream reader) should treat prior Diamond-subset figures already in
  this corpus. `blog-latentspace-fable-5-mythos-launch.md` Claim 3 (Mythos
  5: 30.9% on FrontierCode Diamond) and
  `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 6 ("prior Opus"
  ~10%, Claude Fable 5 ~30% "on its hardest subset") both cite Diamond-tier
  figures from before this deprecation. Cognition's own stated reason —
  low solve rates at the hardest tier make scores noisy — is a reasonable
  basis for caution about over-interpreting small differences in those
  older Diamond numbers (e.g., treating a 30.9% vs. ~30% difference as
  meaningful), though it does not mean the directional claims in those
  notes (Fable-5-class models roughly tripling a prior Opus model's score on
  the hardest tier) are wrong. Not a formal contradiction: Cognition is not
  disputing the older Diamond numbers, just retiring the subset going
  forward because of a reliability concern it identified in its own
  methodology. See Cross-References for how this connects three notes.

### Claim 10: On the current live FrontierCode 1.1 Main leaderboard, Claude Fable 5 ranks first at 53.5%, ahead of GPT-5.6 Sol (47.5%), Claude Opus 4.8 (46.5%), GPT-5.5 (43.0%), Claude Sonnet 5 (42.7%), Grok 4.5 (42.4%), SWE-1.7 (42.3%), GPT-5.6 Terra (41.3%), GPT-5.6 Luna (39.8%), and Claude Opus 4.7 (38.5%)
- **Evidence**: Extracted directly from the page's embedded JSON-LD
  structured data (`ItemList`, "FrontierCode 1.1 Leaderboard (Main)"), which
  is present in the page's raw HTML even though the visible leaderboard
  table itself is rendered client-side via JavaScript (see Extraction
  Notes). This is first-party, machine-readable data from Cognition, not an
  AI-summarized paraphrase.
- **Confidence**: emerging (specific, current, machine-readable data, but a
  live leaderboard that can change at any time — this is a snapshot as of
  2026-07-23, not a fixed, citable measurement the way a dated paper's
  table would be)
- **Quote**: (structured data, not prose; see Concrete Artifacts for the
  full extracted table)
- **Our assessment**: This is the first source in this corpus to supply a
  full top-10 FrontierCode 1.1 Main leaderboard rather than a single
  headline figure. Notably, Cognition's own SWE-1.7 model (position 7,
  42.3%) sits below several competitor models on Cognition's own benchmark
  — a data point that argues against dismissing FrontierCode as pure
  self-serving marketing, since Cognition is not simply engineering the
  leaderboard to put its own model on top. Any guide citation of this table
  should be flagged as a point-in-time snapshot (2026-07-23) of a leaderboard
  that will keep changing as new models are evaluated.

### Claim 11: The leaderboard page includes an interactive task explorer that lets a user switch between models on a real FrontierCode task, run the grading pipeline live, and click a failed rubric criterion to jump directly to the offending part of the model's diff
- **Evidence**: Direct feature description plus a labeled interaction
  affordance ("Interactive:").
- **Confidence**: settled (description of a shipped, currently-live page
  feature)
- **Quote**: "Explore a real task below: switch between models, run the eval, and click a failed criterion to jump to the offending part of the diff."
- **Quote (labeled affordance)**: "Interactive: run the FrontierCode grading pipeline against each model's output and inspect how the patch maps to rubric pass/fail."
- **Our assessment**: This is a reviewability/transparency mechanism worth
  noting alongside `blog-cognition-verifying-agentic-development.md` Claim
  10 (Devin's own two-tier test-report design — labeled screenshots plus a
  chaptered video — as a way for a human to audit autonomous agent work
  after the fact without re-running it). Both are Cognition products built
  around the same underlying idea: make it fast to jump from a pass/fail
  verdict to the specific evidence that produced it, rather than requiring
  a reviewer to re-derive the verdict from scratch.

### Claim 12: FrontierCode's core motivation cites METR's independent research finding that many PRs which pass SWE-bench-style grading would not actually be merged into the target codebase
- **Evidence**: A footnoted external citation in the original methodology
  post's reference list.
- **Confidence**: settled (direct citation, attributable and checkable —
  though this note did not independently fetch and verify the METR source
  itself, only its citation as it appears here)
- **Quote**: "[1] METR, "Many SWE-bench-passing PRs would not be merged into main," March 10, 2026. metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main"
- **Our assessment**: This citation is the clearest evidence that
  FrontierCode is a direct, deliberate response to a specific, named,
  external, independent finding — not simply an in-house marketing
  benchmark invented without engaging the broader "benchmarks don't measure
  what we think they measure" critique already prominent in this corpus
  (`blog-cursor-cursorbench.md` Claim 1). No existing source note in this
  corpus currently covers the METR finding itself; if a future source
  mines that METR post directly, it should cross-reference this claim.

## Concrete Artifacts

### FrontierCode 1.1 Main leaderboard (current snapshot, extracted from page JSON-LD, 2026-07-23)

```
Source: cognition.com/frontiercode, embedded ItemList structured data,
"FrontierCode 1.1 Leaderboard (Main)", fetched 2026-07-23

Rank  Model              Score
1     Claude Fable 5     53.5%
2     GPT-5.6 Sol        47.5%
3     Claude Opus 4.8    46.5%
4     GPT-5.5            43.0%
5     Claude Sonnet 5    42.7%
6     Grok 4.5           42.4%
7     SWE-1.7            42.3%
8     GPT-5.6 Terra      41.3%
9     GPT-5.6 Luna       39.8%
10    Claude Opus 4.7    38.5%
```

### FrontierCode 1.0 launch results by subset (from "Introducing FrontierCode," 2026-06-08)

```
Source: cognition.com/blog/frontier-code

Subset (task count)     Best frontier model         Other cited models
Diamond (50, hardest)   Claude Opus 4.8: 13.4%       GPT-5.5: 6.3%, Gemini 3.1 Pro: 4.7%
Main (100)              Claude Opus 4.8: 34.3%
Extended (150, full)    Claude Opus 4.8: 51.8%

Best open-source model (Kimi K2.6): 3.8% (Diamond) / 16% (Main) / 37% (Extended)
```

### Rubric creation / quality-control process (from "Introducing FrontierCode," "Our rubric creation process")

```
Source: cognition.com/blog/frontier-code

1. Design — classical/deterministic tests preferred where checkable;
   behavioral tests for complex tasks; LLM grading reserved for soft
   qualities (idiomatic code, readability, architectural fit)
2. Hack report — task author plays "lazy or adversarial programmer" to
   find false positives; writes a valid alternative solution to find
   false negatives; Devin is also asked to find novel rubric exploits
3. Rubric calibration — author writes four distinct solutions spanning
   a 0-100% score range, to confirm the rubric has resolution
4. Review — eval pod lead reviews first; Cognition researcher does final
   review with pod lead and contributor; for a random subset, researchers
   independently re-solve the task
5. Re-Review — any stage can send a task back for revision; most tasks
   go through multiple iterations before passing
```

### Internet-use anti-cheating methodology, alternatives considered (from "FrontierCode 1.1," 2026-07-07)

```
Source: cognition.com/blog/frontier-code-1.1

Rejected — Blocklisting:
  ~1,200 domains blocked after iterative expansion
  Agents still found workarounds, sometimes after 20+ turns fighting it
  Broke legitimate workflows (e.g. GitHub access sometimes required)

Rejected — Allowlisting:
  Requires anticipating every legitimate site per task; doesn't scale
  Visible allowlist steers agent behavior toward listed sites
  Hidden allowlist causes agents to conclude "internet is broken" or
    waste turns probing reachability

Adopted — Prompt + classical verifier:
  Prompt defines fair use (docs, error messages) vs. unfair use
    (anything that could shortcut the task, e.g. the original PR)
  Classical verifier flags references to source PRs, upstream patches,
    or solution-bearing mirrors/vendored copies; flagged runs score zero
  Result: unfair internet use rate fell below 1% for every model tested
```

### Version changelog (from the leaderboard page)

```
Source: cognition.com/frontiercode

FrontierCode 1.1 (07.07.26, current): "Refines the methodology to
  distinguish legitimate internet use from unfair use: runs flagged for
  consulting solution-bearing sources are zeroed. Also audits blocker
  criteria and deprecates the Diamond subset."

FrontierCode 1.0 / "Introducing FrontierCode" (06.08.26, original):
  "Introduces the benchmark: mergeability as the grading standard, tasks
  crafted by open-source maintainers, and the ensemble of unit tests,
  rubrics, and verifiers behind the score."
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 3 ("Mythos 5 scored
    30.9% on FrontierCode Diamond versus a second-best of 13.4%," June 10,
    2026): this note's Claim 7 independently confirms, from Cognition's own
    primary-source blog post dated two days earlier (2026-06-08), that
    Claude Opus 4.8 scored exactly 13.4% on FrontierCode Diamond at launch —
    the same figure that AINews reported as the unnamed "second-best" score.
    This corroboration also triangulates with
    `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 6 ("On
    Cognition's internal 'Frontier Code' benchmark's hardest subset, the
    prior Opus model scored around 10% and Claude Fable 5 scored about
    30%"): three independent corpus notes now converge on the same
    approximate Diamond-subset numbers (a "prior Opus" model at
    ~10-13.4%, a Fable-5-class model at ~30-30.9%), each sourced
    differently (Cognition's own methodology post, an AINews aggregator
    digest, and an Anthropic-published interview with Cognition's Silas
    Alberti). That Claim 6 explicitly notes "methodology, task count, and
    task composition of Frontier Code are not disclosed" in its source —
    this note supplies exactly that missing methodology detail (Claims 2-9
    here), closing the gap that note flagged.
  - `blog-cursor-cursorbench.md` Claim 1 (public benchmarks suffer
    misalignment, grading problems, and training-data contamination) and
    Claim 7 (agentic graders needed for open-ended tasks with many valid
    solutions): FrontierCode's maintainer-authored tasks (Claim 4 here)
    directly answer the misalignment failure mode; its hack-report/
    calibration process (Claim 5) and adaptive-classical-grading "mutagent"
    tool (Claim 3) directly answer the grading-problems failure mode Cursor
    names, via a different mechanism (test-environment patching rather than
    a pure LLM judge).
  - `blog-simonwillison-kimi-k3-pelican-benchmark.md` Claim 5 (the pelican
    benchmark's correlation with overall model quality has been "mostly
    severed") and Claim 6 (public toy benchmarks don't measure agentic
    tool-calling or long-horizon reliability, "the thing that matters most"):
    thematically corroborates the general practitioner consensus that
    popular benchmarks are losing discriminative power at the frontier —
    FrontierCode's response (production-code, maintainer-graded
    mergeability) targets the same underlying problem from the
    software-engineering-benchmark angle rather than the toy-benchmark angle.

- **Contradicts**: None filed as a formal contradiction issue. One
  candidate was evaluated and rejected under `agents/MINER.md` §4a: this
  note's Claim 8 (Cognition explicitly tried and rejected network-level
  blocklisting/allowlisting as anti-cheating mechanisms, citing scale and
  workflow-breakage problems) sits in tension with
  `blog-cursor-reward-hacking-benchmarks.md` Claim 9 (Cursor's published fix
  for the same upstream-lookup exploit — Claim 3 of that note — is egress
  proxying, i.e. network-level allowlisting of package registries). This
  does not meet the contradiction-filing bar: the two sources are not
  making opposed factual claims about the same system, they are reporting
  different design choices by two different organizations for two
  different systems (a live coding-agent product's sandboxed execution
  environment vs. a benchmark-authoring pipeline with a fixed, curated task
  set) — a conditioning-variable difference, not a same-claim conflict. See
  Claim 8's "Our assessment" for the full reasoning.

- **Extends**:
  - `blog-anthropic-cognition-fable5-frontier-trust.md` (Cognition's
    internal "Frontier Code" benchmark, mentioned there only as an
    undisclosed-methodology internal tool used to validate Claude Fable 5's
    capability jump): this note supplies the full public methodology,
    task-count structure, and QC process for the benchmark that source
    treats as a black box.
  - `blog-cognition-swe16-preview.md` Claim 2 (Cognition selected SWE-Bench
    Pro because OpenAI recommended it, and treats evaluation-harness
    engineering as a first-class reproducibility problem) and Claim 3
    (Cognition's own attempt to replicate a competitor's reported SWE-Bench
    Pro score across three different harnesses produced a lower number than
    the competitor's own reported figure): this note shows Cognition's
    escalation from harness-level rigor applied to an *existing* public
    benchmark (SWE-Bench Pro) to building and maintaining an entirely new,
    maintainer-curated benchmark of its own — the same underlying
    "benchmark reproducibility is an engineering problem, not just a
    training problem" stance, taken further.
  - `blog-cognition-verifying-agentic-development.md` Claim 10 (Devin's
    two-tier test-report design — labeled screenshots plus a chaptered,
    scrubbable video — as a reviewability mechanism): this note's Claim 11
    (the leaderboard's interactive task explorer, letting a user jump
    directly from a failed rubric criterion to the offending diff line) is
    a second, independent Cognition product built around the same
    "fast path from verdict to evidence" reviewability principle.

- **Novel**:
  - The "mergeability" framing itself, and its explicit grounding in a
    named external critique (METR's finding — Claim 12) — no existing
    source note in this corpus discusses METR's SWE-bench-mergeability
    finding.
  - The three named novel grading techniques — reverse-classical tests,
    files/size/semantic scope enforcement, and the "mutagent" adaptive
    test-environment patching tool (Claim 3) — are new to the corpus.
  - The specific, quantified account of blocklisting/allowlisting as
    rejected anti-cheating approaches, with concrete failure detail (a
    1,200-domain blocklist still bypassed after 20+ turns of active
    circumvention) — Claim 8 — is new; the corpus's other benchmark-cheating
    source (`blog-cursor-reward-hacking-benchmarks.md`) documents the
    exploit mechanisms and one adopted fix (egress proxying) but not a
    documented account of alternatives tried and discarded.
  - Devin being used as an adversarial red-teamer against its own vendor's
    benchmark rubric (Claim 5) is new to the corpus.
  - The full FrontierCode 1.1 Main top-10 leaderboard (Claim 10) is the
    first source in this corpus to supply a complete, multi-model
    leaderboard table for this specific benchmark rather than a single
    headline figure.

## Guide Impact

- **Chapter 03 (Verification)**: Add the six-axis grading taxonomy (Claim 2)
  and the three novel grading techniques (Claim 3 — reverse-classical
  tests, scope enforcement, mutagent-style adaptive test patching) as
  concrete, reusable design patterns for teams building their own
  agent-output grading rubrics beyond binary pass/fail, citing this source.
  These are more mechanistic and implementation-specific than the corpus's
  existing benchmark-critique material (`blog-cursor-cursorbench.md`), which
  diagnoses the problem but gives fewer concrete grading-technique fixes.

- **Chapter 03 (Verification)**: Add the hack-report / adversarial
  calibration process (Claim 5) — including using the coding agent itself
  as a red-teamer against the rubric — as a technique for any team building
  rubric-based LLM evals, not just benchmark authors: stress-test your own
  grading criteria by asking an agent to find ways to pass while doing the
  wrong thing, before trusting the rubric in production.

- **Chapter 03 (Verification) / Chapter 06 (Security and Threat Model)**:
  Add the internet-use anti-cheating case study (Claim 8) — including the
  specific rejected alternatives (blocklisting, allowlisting) and their
  failure modes — as a worked example for any team running agent evals or
  agent-graded CI checks with live internet access: a prompt-plus-verifier
  approach may outperform network-level blocking, but this is only one
  data point in tension with a different vendor's (Cursor's) choice of
  network-level egress proxying for a similar threat — flag both approaches
  rather than presenting either as definitively better.

- **Chapter 03 (Verification)**: Add a caveat to any existing or future
  guide content that cites FrontierCode Diamond-subset figures (via
  `blog-latentspace-fable-5-mythos-launch.md` or
  `blog-anthropic-cognition-fable5-frontier-trust.md`): Cognition itself
  deprecated the Diamond subset in the 1.1 revision (Claim 9) due to noisy,
  low solve rates at the hardest tier — cite Diamond-era comparisons as
  directional (e.g. "roughly tripled") rather than precise, and prefer Main
  or Extended subset figures for any future FrontierCode citations.

## Extraction Notes

- The leaderboard page (`/frontiercode`) renders its visible leaderboard
  table client-side via JavaScript ("Loading leaderboard…" placeholder in
  the raw HTML) and was not retrievable through WebFetch's default
  AI-summarization pass, which reported "no actual model names, scores,
  costs, or speed metrics are displayed." This note instead fetched the raw
  HTML directly (`curl`) and located the leaderboard data embedded as
  `application/ld+json` structured data (`ItemList`, "FrontierCode 1.1
  Leaderboard (Main)") in the page source — this is first-party,
  machine-readable data from Cognition, not an AI paraphrase, and was
  verified present in the raw HTML before being cited. Only the Main
  leaderboard's top 10 was found in structured-data form; no equivalent
  structured data for the Extended subset, or for the FrontierCode 1.0 tab,
  was found in the static HTML (these likely load via client-side fetch
  when a user switches tabs) — this is disclosed as a coverage gap, not
  silently omitted. Cost and speed columns, mentioned in the page's
  `og:description` meta tag ("Compare scores, pass rates, cost, and
  speed"), were not found in the extracted JSON-LD (which contains only
  name/position/score) or elsewhere in the static HTML.
- Per `agents/MINER.md` §1, this note followed the two blog posts linked
  directly from the leaderboard page ("Introducing FrontierCode" and
  "FrontierCode 1.1") as substantive linked pages, since the leaderboard
  page's own prose is a condensed summary of the methodology those two
  posts describe in full. Both were fetched via raw HTML (`curl`) rather
  than WebFetch's default summarization pass, and every quote in this note
  was verified present, character-for-character, in the corresponding raw
  HTML file before being included (via direct `grep`/`python` extraction
  from the saved HTML, not from an AI-generated summary) — this is a
  stronger verification standard than several prior source notes in this
  corpus that relied on cross-checking two independent WebFetch passes
  against each other (e.g. `blog-latentspace-fable-5-mythos-launch.md`,
  `blog-thoughtworks-anand-agent-evaluation-framework.md`) because WebFetch
  itself was unreliable for this particular vendor's Next.js streaming page
  format.
- One quote (Claim 8, allowlist rejection) is truncated mid-sentence in the
  raw HTML as fetched — the source's own text appears to continue past
  "wastes effort probing which s..." — this is flagged in the quote itself
  with a bracketed `[ites are reachable]` completion inferred from context
  and grammar, not verified verbatim; the unbracketed portion before the
  truncation point is a direct, verified quote.
- No sub-pages beyond the two blog posts were followed. The two blog posts
  each have their own "Acknowledgments" sections listing many additional
  contributor names; these were not extracted as they are not substantive
  claims.
- One contradiction candidate was evaluated (Claim 8, blocklisting/
  allowlisting rejection vs. `blog-cursor-reward-hacking-benchmarks.md`
  Claim 9's egress-proxying fix) and determined not to meet the
  `agents/MINER.md` §4a filing bar — see Cross-References → Contradicts for
  the full reasoning. No contradiction issue filed.
- All claim numbers cited from other source notes
  (`blog-latentspace-fable-5-mythos-launch.md` Claim 3;
  `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 6;
  `blog-cursor-cursorbench.md` Claims 1 and 7;
  `blog-cursor-reward-hacking-benchmarks.md` Claims 3 and 9;
  `blog-simonwillison-kimi-k3-pelican-benchmark.md` Claims 5 and 6;
  `blog-cognition-swe16-preview.md` Claims 2 and 3;
  `blog-cognition-verifying-agentic-development.md` Claim 10) were verified
  by re-reading the cited note and locating the numbered heading before
  citing — no claim number was guessed or approximated.
