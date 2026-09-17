---
source_url: https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/quantifying-ai-adoption-from-initial-challenges-to-doubling-speed
source_type: blog-post
title: "Quantifying AI adoption: From initial challenges to doubling speed"
author: Nik Malykhin (Thoughtworks)
date_published: 2026-09-16
date_extracted: 2026-09-17
last_checked: 2026-09-17
status: current
confidence_overall: emerging
issue: "#3509"
---

# Quantifying AI Adoption: From Initial Challenges to Doubling Speed

> A first-person, 8-month team-level case study (6 developers) reporting
> story-throughput gains from ~15 to ~27 user stories/iteration after
> rejecting two intermediate architectures (a heavy spec-kit-style
> specification framework, then local execution-state files) in favor of a
> minimal workflow of read-only documentation links, strict skill
> definitions, and multi-stage chat refinement. The short Thoughtworks post
> links out to two of the author's own deeper Substack write-ups containing
> quantified, artifact-level experiments (PR file counts, word counts, story
> point re-estimation, a concrete "hidden context modification" incident,
> and a public GitHub reference implementation) that substantially
> strengthen — and in one respect complicate — the headline claim.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "AI and ML" / "Technology
  strategy" categories; published September 16, 2026; ~700 words; discovered
  via the trusted `thoughtworks` RSS feed). Short on its own, but three
  inline links point to substantive follow-on material: two long-form
  Substack posts by the same author (`nikmalykhin.com`, "Designing AI-Driven
  Development Workflows," 2026-06-30, and "Assessing file-stored state in AI
  development workflows," 2026-07-21) and a public GitHub repository
  (`nikmalykhin/lightweight-jira-story-workflow`) implementing the workflow
  described. Per MINER.md's "follow up to 5 linked pages that seem
  substantive," all three were fetched and read in full; they are treated
  here as part of the same source (same author, directly linked from the
  primary article as the evidentiary basis for its claims) rather than as
  independent corpus entries.
- **Author credibility**: Nik Malykhin, identified in the Thoughtworks
  byline as "By Nik Malykhin," self-described in the piece as "the AI
  ​​champion for a team of six developers" over the 8-month period covered.
  This is the same author (Nik Malykhin, "an Israeli software developer and
  Thoughtworker" per his martinfowler.com bio) who wrote
  `blog-fowler-malykhin-archaeologist-copilot.md`, a solo legacy-modernization
  case study published two months earlier (2026-07-16). That piece carries
  no team-productivity claims (explicitly about method, not speed); this
  piece is his first corpus contribution with a quantified team-level
  productivity claim, though the Substack posts linked from it show he was
  independently running smaller, more controlled experiments (single-story,
  before/after tool comparisons) throughout the same window the Thoughtworks
  post summarizes. The Thoughtworks article carries a disclaimer: "The
  statements and opinions expressed in this article are those of the
  author(s) and do not necessarily reflect the positions of Thoughtworks." As
  the team's self-identified "champion" for the adoption effort he is now
  measuring, the author is not a disinterested party for the headline metric
  — a structural bias worth flagging for Claim 1 specifically, though it
  applies less to the more mechanical, artifact-level Substack findings
  (PR file counts, word counts), which are closer to raw observation than
  self-assessment.
- **Scope**: Covers one team's 8-month AI-adoption rollout (foundations →
  Scrum-sprint experimentation → default AI-assisted development), one
  headline productivity metric (user stories per iteration), an
  architectural narrative of context/state-management experiments (spec-kit
  → local execution-state files → minimal read-only-links workflow), and,
  via the linked Substack posts, two more granular single-story experiments
  quantifying PR structure, documentation volume, and story-point impact.
  Does NOT cover: organization-wide or multi-team rollout, independent
  verification of the story-count figures, a definition of "user story"
  size/complexity consistency across the three measured adoption stages, or
  named production incidents beyond the one described "hidden context
  modification" example (see Claim 10 below).

## Extracted Claims

### Claim 1: Team-level story throughput dropped from a baseline of ~15 to ~12 user stories per iteration during early AI-adoption workflow experimentation, then rose to ~27 per iteration after the team settled on a refined workflow, over an 8-month period
- **Evidence**: The author's own tracked metric, self-described as an
  attempt to "move beyond sentiment to measurable task-completion metrics,"
  covering a team of 6 developers over 8 months as the team's "AI champion."
- **Confidence**: anecdotal (single team of 6, one internally tracked count
  metric, no independent audit, no stated definition of story-sizing
  consistency across the three stages, self-reported by the person who
  championed the adoption)
- **Quote**: "Before implementing AI in our software development cycle, the
  team established a productivity baseline of approximately 15 user stories
  per iteration. During the early stages of implementation and workflow
  experimentation, productivity dropped to 12 user stories per iteration as
  engineers adapted to new interaction patterns and workflows. After we
  selected and refined a simpler workflow, the metric reached 27 user
  stories per iteration."
- **Our assessment**: This is a striking number (~80% above baseline, ~125%
  above the mid-adoption trough) that directly stresses the guide's existing
  "realistic ceiling is much lower than the vendor pitch" synthesis in
  `guide/05-team-adoption.md` (10-30% range). We filed this as a
  contradiction rather than resolving it here (see Cross-References). One
  specific reason for skepticism, beyond the general vanity-metric and
  champion-bias concerns: the same author's own more controlled, single-story
  experiment described in the linked Substack post (Claim 6 below) found
  that AI assistance removed "approximately one story point from
  medium-sized requirements" — e.g. a 3-point story re-estimated at 2
  points, roughly a one-third reduction in estimated complexity — with
  explicitly *diminishing* returns on larger, more complex stories. A
  one-third-per-story complexity reduction, generalized naively across a
  sprint, would not on its own predict an 80% throughput increase; something
  beyond per-story effort reduction (e.g. reduced blocking/rework time,
  the read-only-links and skill-definition workflow improvements, or story
  splitting/re-sizing between the baseline and post-adoption measurement
  periods) would have to account for the rest of the gap. The article does
  not reconcile the two numbers, and neither can this note — but the
  discrepancy between the author's own granular measurement and headline
  team-level claim is itself worth surfacing.

### Claim 2: Performance gains from AI integration were nonlinear — an initial productivity hit preceded, and was a precondition for, the technical foundation required for sustained acceleration
- **Evidence**: Author's direct interpretive framing of the pattern in Claim
  1, presented as the article's thesis statement.
- **Confidence**: anecdotal (single-team interpretation of a single-team data
  set)
- **Quote**: "In our experience, performance gains from AI integration were
  nonlinear; an initial performance hit preceded the technical foundation
  required for sustained acceleration of adoption."
- **Our assessment**: This "dip before climb" shape is directionally
  consistent with, but a different phenomenon from, the pattern in
  `paper-miller-speed-cost-quality.md` Claim 1 (a 281% velocity *spike* in
  month 1 that decays to zero by month 3 in OSS Cursor adoption). Miller et
  al. document an early spike that fades; Malykhin documents an early dip
  that later exceeds baseline. The two are not directly comparable (different
  metrics — LOC velocity vs. story count; different populations — OSS
  repositories vs. one internal team), but a guide section citing both should
  not imply they describe the same adoption curve shape.

### Claim 3: The main obstacle at the initial adoption stage was psychological — engineers needed to shift from trusting AI output to trusting compiled code — which required developing solid technical understanding of context-window limitations, prompt-template construction, and rigorous automated verification
- **Evidence**: Author's description of "Stage 1: Foundations and trust in
  the code," in the primary Thoughtworks article.
- **Confidence**: anecdotal
- **Quote**: "The main obstacle at this initial stage was psychological.
  Engineers needed to transition from trusting AI output to trusting in
  compiled code. This required developing a solid technical understanding of
  the limitations of the context window, the construction of prompt
  templates and rigorous automated verification."
- **Our assessment**: This corroborates `failure-noemit-early-agentic-adoption.md`
  Lesson 1 (early agentic coding required extremely granular prompting to
  produce usable output) and its Root Cause discussion of context-window and
  prompt-literacy prerequisites — though noemit's account is an individual,
  necessity-driven adopter working with 2024-era tools, while this is a
  supported team rollout roughly two years later. Both sources independently
  land on "compiled/verified code, not AI output, is the actual trust
  anchor" as the resolution to the psychological obstacle.

### Claim 4: The team adopted AI gradually via weekly two-hour hands-on workshops with engineering-leadership support, plus unstructured exploration within standard two-week Scrum sprints, rather than a top-down mandate
- **Evidence**: Author's description of "Stage 2: Iterative experimentation
  in Scrum sprints," primary Thoughtworks article.
- **Confidence**: anecdotal
- **Quote**: "We introduced weekly two-hour hands-on workshops with the
  support of engineering leadership. These regular sessions provided a
  controlled environment for estimating tasks, analyzing error modes and
  reviewing generated pull requests. Beyond these structured hours, engineers
  were free to explore AI tools within our standard two-week Scrum sprints
  without explicit daily guidance."
- **Our assessment**: A concrete, reusable adoption-scheduling pattern
  (structured weekly workshop time + unstructured sprint-embedded
  exploration, with no daily mandate). The explicit "not a sudden mandate"
  framing ("Transitioning the engineering team from manual development to
  stable production delivery using AI assistants required a gradual
  implementation, not a sudden mandate") corroborates a bottom-up-with-
  leadership-support adoption model.

### Claim 5: Heavy specification frameworks like spec-kit established clear design constraints but their administrative overhead (too many mandatory steps, unused documentation) slowed the workflow enough that the team abandoned them for day-to-day use
- **Evidence**: Author's summary account in the primary Thoughtworks article
  under "Architectural evolution of context and control."
- **Confidence**: anecdotal in the summary article, but backed by a
  quantified single-story comparison in the linked Substack post (see
  Claims 6-9 below)
- **Quote**: "Early on in the initiative, we evaluated heavy specification
  frameworks like spec-kit, to ensure clear design constraints. While this
  methodology established boundaries, the administrative overhead
  (specifically, too many mandatory steps and unused documentation) slowed
  the workflow."
- **Our assessment**: This is the first source in the corpus to name and
  evaluate `spec-kit` specifically (a grep across `source-notes/` for
  "spec-kit" before this note returned no results). It is a concrete
  instance of the more general tension already present in
  `blog-thoughtworks-lopezfernandez-asymmetric-dialogue.md` Claim 10 (the
  micro-batch/asymmetric-dialogue loop as "a middle path between unstructured
  mega-prompting and heavyweight upfront specification"). Note the summary
  article's "abandoned" framing is more absolute than the linked Substack
  post's actual conclusion (Claim 9 below), which recommends customizing
  spec-kit rather than discarding it outright — a nuance lost in the
  shorter, more polished Thoughtworks summary.

### Claim 6: In a controlled single-story comparison (a medium-sized SendGrid template-rendering user story implemented two ways), the custom read-only-links/skill-based workflow produced six small, functional-code-only pull requests (median 3-4 files, max 5), while spec-kit's vertical-slicing approach produced four pull requests that were individually much larger (average 7-8 files, max 13)
- **Evidence**: A named, described experiment on the author's Substack
  ("Designing AI-Driven Development Workflows," 2026-06-30), comparing
  GPT-5.3-Codex-driven implementation of the same user story (SendGrid
  template rendering/storage in an email notification use case) under the
  two workflows.
- **Confidence**: anecdotal (n=1 user story, one model, one author/reviewer,
  no replication) but with a much higher level of quantified, checkable
  detail than the parent Thoughtworks post alone provides
- **Quote**: "This approach generated six discrete pull requests. The median
  size of these code updates remained between three and four files, with the
  most extensive single update containing five files." ... "In contrast, the
  spec-kit framework approached the user story through vertical slicing,
  attempting to package complete functional business capabilities into each
  cycle. This strategy yielded four pull requests, but the internal volume of
  these updates was substantially larger, averaging seven to eight files per
  pull request. The most expansive update within this set encompassed
  thirteen distinct files."
- **Our assessment**: This is a concrete, reviewable-cost argument against
  spec-kit's default vertical-slicing PR structure, independent of any
  productivity-metric dispute: "Reviewing a thirteen-file modification
  requires deep contextual immersion and can easily exhaust a multi-hour
  block of defensive engineering time. Conversely, integrating five to seven
  highly compact pull requests throughout a standard working day introduces
  negligible cognitive friction." The author also notes both workflows
  independently introduced the *same* SendGrid-template rendering bug,
  requiring an identical corrective commit in both cases — "this suggests
  that the structural layout of the pull requests, rather than initial code
  accuracy, serves as the primary differentiator in developer friction." That
  is a specific, useful isolation of variables: the two workflows produced
  comparable code-correctness outcomes, and the measured difference is
  entirely in review ergonomics from PR shape.

### Claim 7: Interactive chat-based planning (four to five clarification/planning iterations, ~30 minutes of reading-equivalent dialogue) produced roughly the same total word volume as spec-kit's eight generated specification documents, but the spec-kit documentation took roughly 50 minutes of solitary technical reading to review versus 30 minutes of collaborative dialogue
- **Evidence**: Word counts and reading-time estimates from the same
  Substack experiment, using stated reading-rate assumptions (150 wpm
  conversational, 75 wpm for dense technical documentation).
- **Confidence**: anecdotal (a single author's estimated reading rates
  applied to one experiment's output; the 150/75 wpm assumptions are the
  author's own choices, not independently validated)
- **Quote**: "Cumulatively, this chat dialogue generated 16 pages of
  standard layout text, or 4,651 words. Assuming an average conversational
  rate of 150 words per minute, this preparatory phase equates to a
  thirty-minute collaborative pair-programming session." ... "The
  documentation total matches the 16-page volume of the conversational
  workflow but contains 3,832 words of highly dense technical material. When
  applying an analytical reading standard of 75 words per minute for complex
  documentation, reviewing this output demands roughly 50 minutes of
  solitary, rigorous technical analysis." ... "Insight: Engaging in a
  collaborative, bidirectional technical dialogue yields lower cognitive
  fatigue than parsing dense, machine-generated analytical documentation
  independently."
- **Our assessment**: The headline insight (interactive dialogue beats
  solitary document review at a similar word count) rests on an assumed,
  not measured, reading-speed differential (150 vs. 75 wpm) — the total text
  volume was nearly identical (4,651 vs. 3,832 words) so the entire claimed
  time advantage comes from that assumption plus the qualitative "cognitive
  fatigue" judgment, not from an independently observed time difference.
  Treat the specific "30 min vs 50 min" figure as an estimate built on the
  author's own assumptions, not a measured outcome — but the underlying
  observation (both workflows produce a comparable volume of "preparation
  text," they just differ in *format*: dialogue vs. static docs) is a solid,
  specific data point independent of the reading-speed assumption.

### Claim 8: AI assistance reduced the estimated complexity of a medium-sized (3-story-point) user story by approximately one point (to 2 points), a pattern the author reports as consistent "over a multi-month period," but this effect diminishes on larger, more complex stories
- **Evidence**: Author's story-point re-estimation observation from the
  same Substack experiment.
- **Confidence**: anecdotal (subjective story-point estimation, one team's
  planning-poker-style convention, not an objective effort measure)
- **Quote**: "By utilizing either AI-driven development environment, the
  effective complexity of the implementation dropped significantly, allowing
  the story to be re-estimated at two points. This finding aligns with
  observations gathered over a multi-month period: the strategic application
  of generative models consistently removes approximately one story point
  from medium-sized requirements." ... "However, this efficiency gain
  exhibits a clear non-linear trend when applied to larger tasks. A
  single-point reduction on a highly complex, five-point user story does not
  alter the fundamental delivery architecture or allow the task to be
  decomposed more effectively."
- **Our assessment**: This is the single most directly comparable
  productivity figure to Claim 1's headline metric, and it tells a much more
  modest story: a roughly one-third complexity reduction per medium story,
  with explicitly diminishing returns on complex stories — not a wholesale
  doubling of throughput. See Claim 1's "Our assessment" for the tension
  this creates with the parent article's 15→27 stories/iteration headline
  number.

### Claim 9: Adopting spec-kit "out of the box" (unmodified) is not recommended for long-term repository health because its documentation-generation habit produces a large volume of non-service files over a year at team scale; the recommended path is a hybrid architecture customizing spec-kit to inherit the smaller-PR structural discipline of the custom workflow, not abandoning it outright
- **Evidence**: Author's projected-scale calculation and final recommendation
  in the Substack post, extrapolating from the single-story experiment to an
  annual team-level volume.
- **Confidence**: anecdotal (a linear extrapolation from one story's
  documentation output to a hypothetical department's annual volume; no
  actual year-long deployment of unmodified spec-kit is reported)
- **Quote**: "Consider a baseline engineering department consisting of three
  to four development pairs. If these pairs collectively deliver
  approximately three completed user stories per development iteration
  across 26 annual iterations, the repository configuration changes
  dramatically over time. Under the unmodified spec-kit framework, this
  delivery velocity results in the accumulation of roughly 600 non-service
  Markdown and YAML files every year." ... "The ideal path forward requires a
  hybrid architecture. By customizing spec-kit to inherit the structural
  instructions of the custom workflow, we can merge the systematic rigor of
  automated planning with the clean, highly isolated pull request structure
  required by hexagonal architectures."
- **Our assessment**: This is a materially more nuanced verdict than the
  parent Thoughtworks article's "administrative overhead... slowed the
  workflow" framing (Claim 5) suggests — the Substack source's actual
  recommendation is "customize spec-kit," explicitly framed as unfinished
  future work ("Future efforts will focus on implementing custom skills
  within the agent configuration to restrict the generation of non-service
  files"), not "replace spec-kit with a from-scratch minimal workflow." The
  600-files/year figure is a specific, quotable number for a guide
  discussion of specification-framework documentation overhead, but it rests
  on a linear extrapolation from a single story to a full year, which the
  author does not validate against an actual longer deployment.

### Claim 10: Storing agent execution state in local repository files does not by itself prevent infinite loops or reduce redundant clarifying-question cycles — the storage medium is orthogonal to the model's decision-making behavior; only explicit constraints written into the skill/request configuration itself stop uncontrolled looping
- **Evidence**: A named experiment on the author's second Substack post
  ("Assessing file-stored state in AI development workflows," 2026-07-21)
  using a custom Codex skill (`ec-kick-off`) that fetched Jira issue context
  and staged it through a three-file local pipeline
  (`agents_utils/raw_tickets/<KEY>.json` →
  `agents_utils/raw_tickets/<KEY>.md` →
  `agents_utils/hardened_tickets/<KEY>.md`).
- **Confidence**: anecdotal (one skill, one workflow, one author's
  implementation)
- **Quote**: "Results showed that the storage medium does not affect the
  model's behavior when providing prompts. Passing context through files,
  rather than through prompt strings, does not alter the model's underlying
  decision-making logic." ... "File storage serves solely as a persistent
  storage layer. Preventing infinite loops requires explicit constraints
  built into the skill request configuration, rather than changes to the way
  context is provided."
- **Our assessment**: This is the artifact-level experiment underlying the
  parent Thoughtworks article's more compressed Claim (local repository
  files "serves as a storage layer, it does not prevent infinite loops").
  It is conceptually adjacent to
  `blog-thoughtworks-xiong-five-controllers-one-graph.md` Claim 7 (a Loop
  must close on an external authority, not the agent's own opinion of its
  work) and Claim 9 (the graph — persistent shared knowledge — is explicitly
  not a controller): Xiong's taxonomy would classify local execution-state
  files as graph-like persistent memory, and this experiment independently
  confirms, at implementation level, Xiong's abstract claim that persistent
  memory and behavioral control are categorically separate concerns.

### Claim 11: Isolating each workflow step in a fresh context window does not eliminate hallucinations — it resets the "hallucination space" rather than reducing it, because a model with no conversation history must fully reconstruct its understanding of the problem from scratch on every pass, at the same baseline error rate
- **Evidence**: The same `ec-kick-off` experiment, described as refuting the
  author's own working hypothesis going in.
- **Confidence**: anecdotal (one experiment, framed explicitly by the author
  as testing and refuting their own prior hypothesis)
- **Quote**: "The second hypothesis was that creating a new context window
  for each iteration would eliminate hallucinations and noise in the output.
  Isolated execution was also expected to prevent contamination of the
  generation space by accumulated conversation history. The experiment
  refuted this assumption. When the model reads state from a local file in a
  completely new context window, it must completely reconstruct its
  conceptual understanding of the problem domain. Since the model has no
  history of previous conversations, its baseline probability of generating
  hallucinations remains unchanged on each pass. The new context windows
  don't eliminate the hallucination space; they reset it."
- **Our assessment**: This is a precise, falsifiable, and self-critical
  finding (the author names and then reports refuting their own hypothesis,
  which is a stronger evidentiary posture than simply reporting a success).
  It directly supports Claim 12 below (multi-stage chat outperforms isolated
  single-pass execution) by explaining *why*: accumulated conversation
  context is doing real error-reduction work that a fresh, isolated context
  cannot replicate merely by being "clean."

### Claim 12: Multi-stage refinement within a single, continuous chat context consistently produced better implementation results than isolated, single-pass executions in fresh context windows, because the accumulating context buffer strengthens over successive iterations
- **Evidence**: Direct comparison stated in the same Substack post,
  following the "Fallacy of Stateless Context Isolation" finding (Claim 11).
- **Confidence**: anecdotal
- **Quote**: "Multi-stage refinement in chat allows the context buffer to
  strengthen over successive iterations, resulting in higher-quality
  technical characteristics. In practice, multi-step dialogue within a
  single context flow consistently yielded better results than isolated
  single-pass executions."
- **Our assessment**: This corroborates
  `blog-thoughtworks-lopezfernandez-asymmetric-dialogue.md` Claim 6 (a
  three-step intentional dialogue loop: expose a micro-blueprint, gather
  surgical human feedback, then micro-execute) and Claim 10 (a middle path
  between mega-prompting and heavyweight specification) — both sources
  independently converge on iterative, multi-turn refinement outperforming
  either a single large request or heavily front-loaded specification. This
  source adds the specific mechanistic reason (Claim 11): isolation doesn't
  reduce error rate, it just resets it, so accumulated context is the actual
  source of the quality improvement.

### Claim 13: A model given write access to generate a local Markdown copy of a source-of-truth Confluence page silently altered a specific policy statement (expanding the stated scope of end-to-end test coverage), which was not caught until a manual re-review of the generated file — demonstrating that model-writable local documentation copies risk silent policy drift even when the copy is not needed for any generative purpose beyond static reference
- **Evidence**: A single, concretely described incident in the same Substack
  post: Codex was given a central Confluence page as a "local rules file"
  reference; a later manual review of the generated local Markdown copy
  found the original policy text ("end-to-end tests were limited to testing
  only the primary success scenarios") had been altered to also include
  "critical business processes," which had, in the interim, caused the model
  to generate unwanted extensive negative-path end-to-end tests that
  conflicted with the team's actual testing strategy.
- **Confidence**: anecdotal (one incident, one document, one author's
  after-the-fact review). Note the source's sequencing: it first reports
  that on inspection the local file's contents "were found to be identical
  to the source code," and only in the following paragraph describes
  discovering the altered sentence. Read in order, the first statement is
  the *initial* review's (mistaken) conclusion — the author says as much
  later ("this addition was overlooked during the initial review") — not a
  second, contradictory finding. **Smith caution**: do not quote "were
  found to be identical to the source code" as this source's verdict on
  whether model-generated local copies stay faithful; in context it is the
  failure being narrated, and quoting it standalone inverts the source's
  actual finding.
- **Quote**: "While reviewing the local Markdown file generated by Codex, I
  discovered a minor change. The original Confluence code stated that
  end-to-end tests were limited to testing only the primary success
  scenarios. In the model-generated copy, this statement had been changed,
  and now, in addition to the primary success scenarios, critical business
  processes were included." ... "This minor wording change expanded the
  scope of our testing and altered our engineering strategy. While this
  addition was overlooked during the initial review, it revealed a key
  risk: whenever a model generates local copies of reference documentation,
  it retains the ability to be modified."
- **Our assessment**: This is the concrete worked example that the parent
  Thoughtworks article's "hidden context changes" claim lacks on its own —
  a specific policy sentence, a specific before/after wording delta, and a
  specific downstream consequence (unwanted negative-path E2E test
  generation). This is a strong, citable, and previously-missing-from-the-
  corpus illustration of "read-only access to reference material is a
  safety property, not a convenience preference" — the risk is not
  hypothetical drift, it is a documented instance of a model's local copy
  silently disagreeing with its own source of truth on a specific
  scope-defining sentence, and that disagreement propagating into generated
  test code before being caught.

### Claim 14: The team's final, durable workflow combined direct links to read-only documentation, strict skill definitions, and multi-stage chat refinement integrated with Jira — and this pattern is embodied in a public reference implementation (a central "control" repository running Codex against multiple target repositories via named workflow skills with two mandatory human-approval gates)
- **Evidence**: The primary Thoughtworks article's stated conclusion,
  corroborated by a public GitHub repository
  (`nikmalykhin/lightweight-jira-story-workflow`) linked from the article as
  the "lightweight workflow" referenced in Stage 3.
- **Confidence**: anecdotal for the productivity implications, but the
  repository's existence, structure, and skill names are directly
  verifiable (settled, as a description of what the repository contains)
- **Quote**: "Ultimately, we abandoned local state storage in favor of a
  minimal workflow combining direct links to read-only documentation, strict
  skill definitions and multi-stage chat refinement integrated with Jira."
- **Our assessment**: The repository README describes a named,
  reproducible skill sequence: `wf-story-kick-off` → `wf-story-plan` →
  `wf-task-plan-create` → `wf-task-plan-verify`, then, in a fresh context
  per task, `wf-task-implement` → `wf-task-verify` → `wf-task-commit`, with
  the explicit rule "Implementation has two approval gates; Codex must stop
  and wait at each gate" and "Start `$wf-task-implement` in a fresh Codex
  context for cleaner task focus." This is a rare case in this corpus of a
  narrative adoption case study backed by an actual public, inspectable
  configuration repository rather than only prose description — the
  specific gate-and-fresh-context pattern is a concrete, reusable structure
  for a guide section on multi-repository agent orchestration.

### Claim 15: Task-AI-delegation decisions were made dynamically by pairs of developers rather than governed by a formal algorithm — low-complexity tasks were often done manually when AI context-gathering overhead exceeded the task's value, while complex tasks defaulted to AI use, which yielded the largest gains specifically in coding and test-creation stages
- **Evidence**: Author's description under "Pragmatic problem solving in
  everyday engineering practice," primary Thoughtworks article.
- **Confidence**: anecdotal
- **Quote**: "For low-complexity tasks, such as small fixes or individual
  user stories, developers opted for manual implementation if gathering
  context and generating hints created unnecessary overhead... Conversely,
  for complex user stories requiring design analysis, creating new features
  or fixing bugs in production, teams relied on AI by default. Using model
  generation for complex tasks yielded significant results during the coding
  and test creation stages."
- **Our assessment**: This is a specific counterpoint to the common framing
  (present elsewhere in the corpus) that AI is most valuable for small,
  well-scoped tasks — this team reports the opposite allocation. Worth
  flagging alongside the guide's existing "well-scoped tasks work best with
  AI" guidance rather than silently favoring one framing; the discrepancy
  may reflect a conflation of task *size* and task *complexity* across
  sources rather than a genuine disagreement.

## Concrete Artifacts

```
Source: "Quantifying AI adoption: From initial challenges to doubling
speed," Nik Malykhin, Thoughtworks Insights, published September 16, 2026.

Productivity metric: user stories completed per iteration (team of 6 developers)

  Pre-AI baseline:                  ~15 stories/iteration
  Early adoption/experimentation:   ~12 stories/iteration  (-20% vs. baseline)
  Post-workflow-refinement:         ~27 stories/iteration  (+80% vs. baseline,
                                                             +125% vs. trough)

Timeline: 8 months total, three named stages:
  Stage 1: Foundations and trust in the code
  Stage 2: Iterative experimentation in Scrum sprints
    - Weekly 2-hour hands-on workshops (with engineering-leadership support)
    - Unstructured exploration within standard 2-week Scrum sprints,
      no daily mandate
  Stage 3: Moving to AI-assisted development by default
    - Gradual (not immediate) transition to production use
    - Consensus reached on adopting a "lightweight workflow" (see repo below)

Architectural evolution (context/control), in rejection order:
  1. EVALUATED, NOT ADOPTED FOR DAILY USE: Heavy specification frameworks
     (e.g., spec-kit) -- established design constraints but too much
     administrative overhead (mandatory steps, unused documentation)
  2. REJECTED: Local repository files storing agent execution state --
     enabled auditing, but a storage layer does not prevent infinite loops
  3. ALSO REJECTED: Local intermediate copies of static documentation --
     model-generated local copies caused hidden context changes
  4. ADOPTED (final, durable workflow): direct links to read-only
     documentation + strict skill definitions + multi-stage chat
     refinement + Jira integration
```
*Source: Thoughtworks article, 2026-09-16.*

```
Source: Nik Malykhin, "Designing AI-Driven Development Workflows"
(nikmalykhin.com/p/designing-ai-driven-development-workflows), 2026-06-30.
Experiment: same SendGrid-template-rendering user story implemented via
two workflows, GPT-5.3-Codex.

PR/file-count comparison:
  Custom workflow (chat kick-off -> AGENT.md + skills -> Codex tasks):
    6 pull requests; median 3-4 files; largest PR = 5 files
    All files: functional implementation code only (no doc/spec artifacts)
  spec-kit (vertical-slicing, out-of-the-box):
    4 pull requests; average 7-8 files; largest PR = 13 files
  Both workflows introduced the identical SendGrid-Handlebars rendering bug,
  each requiring one corrective commit -- code correctness was comparable;
  the measured difference was entirely in PR/review ergonomics.

Preparation-phase volume comparison:
  Custom workflow (interactive chat, 5 iterations across clarification +
  planning): 4,651 words / 16 pages -> ~30 min at 150 wpm (conversational)
  spec-kit (8 generated documents: requirements checklist 149w, OpenAPI
  contract 102w, data model 211w, implementation plan 409w, quickstart
  140w, research summary 260w, technical spec 1,021w, task breakdown
  1,540w): 3,832 words / 16 pages -> ~50 min at 75 wpm (dense technical
  reading)

Story-point re-estimation:
  Baseline empirical estimate for the target story: 3 points
  Re-estimated after AI-assisted implementation: 2 points
    ("the strategic application of generative models consistently removes
    approximately one story point from medium-sized requirements")
  Diminishing returns on complex stories: a 1-point reduction on a 5-point
    story "does not alter the fundamental delivery architecture"

Annual documentation-bloat projection (unmodified spec-kit, extrapolated):
  Baseline dept: 3-4 dev pairs, ~3 completed stories/iteration, 26
  iterations/year -> ~600 non-service Markdown/YAML files generated/year

Final recommendation: hybrid architecture -- customize spec-kit to inherit
the custom workflow's small-PR structural discipline, rather than discard
spec-kit outright. Explicitly framed as future work, not yet implemented.
```

```
Source: Nik Malykhin, "Assessing file-stored state in AI development
workflows" (nikmalykhin.com/p/assessing-file-stored-state-in-ai), 2026-07-21.

Experiment: custom Codex skill "ec-kick-off" (Codex + GPT-5.4-medium +
Atlassian Rovo Jira integration). Runs in a subagent's isolated environment.
  Pipeline:
    1. Fetch issue summary/description/status via Rovo Jira plugin
    2. Store raw JSON: agents_utils/raw_tickets/<KEY>.json
    3. Normalize to Markdown: agents_utils/raw_tickets/<KEY>.md
    4. Merge with prior draft context, write hardened ticket:
       agents_utils/hardened_tickets/<KEY>.md
  Observed implementation detail: Codex generated temporary scripts creating
  intermediate prompt files (e.g. /tmp/<KEY>_kickoff_prompt_v2.txt) before
  writing final output -- a self-generated scratch-file pattern for managing
  state transitions across isolated execution boundaries.

Finding 1 (question-loop control): file-based state storage does not by
  itself change model prompting/looping behavior. Explicit anti-loop
  constraints must live in the skill's own request configuration (e.g.,
  "if requirements are incomplete, apply minimal reasonable assumptions,
  record uncertainties, terminate without further prompting").

Finding 2 ("Fallacy of Stateless Context Isolation"): fresh, isolated
  context windows do not reduce hallucination rate -- they reset it. Model
  must fully reconstruct problem understanding each pass at the same
  baseline error rate. Multi-stage chat (accumulating context) outperformed
  isolated single-pass execution in practice.

Finding 3 ("hidden context modification" incident): Codex was given a
  central Confluence page as a read-source for a "local rules file." A
  model-generated local Markdown copy of that page was later found to have
  altered one policy sentence -- original: end-to-end tests limited to
  "primary success scenarios"; model-generated copy: expanded to also
  include "critical business processes." This silently changed the team's
  actual E2E test-scope policy and caused unwanted negative-path E2E test
  generation before being caught in manual review.
  Fix: read documentation directly from the source of truth via read-only
  tools; do not let the model generate or hold a local editable copy of
  policy/reference documentation.
```

```
Source: github.com/nikmalykhin/lightweight-jira-story-workflow (public repo,
linked from the Thoughtworks article as the "lightweight workflow").

Description: "Central Codex control center for lightweight Jira story work
across multiple target repositories."

Skill/workflow sequence (verbatim from README):
  Planning:  $wf-story-kick-off <jira-story>
               -> $wf-story-plan
               -> $wf-task-plan-create <story-key>
               -> $wf-task-plan-verify <story-key>
  Per-task (fresh context each time):
             $wf-task-implement <story-key> <task-id>
               -> $wf-task-verify <task-id>
               -> $wf-task-commit <task-id>

Rules (verbatim):
  "Implementation has two approval gates; Codex must stop and wait at each
  gate."
  "Start $wf-task-implement in a fresh Codex context for cleaner task
  focus."
  "Every implementation task must declare exactly one Repository: <repo-id>.
  Multi-repo stories must be split into separate per-repo tasks."
  "Target repository commits must not include central .temp updates."

File layout:
  AGENTS.md              -- workflow orchestration and global rules
  repos.md                -- shared target-repository list/canonical IDs
  .agents/skills/wf-*      -- user-invoked workflow steps
  .agents/skills/helper-*  -- reusable workflow helpers
  .temp/<story-key>/       -- generated story artifacts (story-context.md,
                              <story-key>-task-plan.md, <repo-id>/repo-context.md)
```

## Cross-References

### Cross-reference verification notes
`blog-fowler-malykhin-archaeologist-copilot.md`,
`blog-thoughtworks-anand-agent-evaluation-framework.md`,
`blog-thoughtworks-xiong-five-controllers-one-graph.md`,
`blog-thoughtworks-lopezfernandez-asymmetric-dialogue.md`,
`failure-noemit-early-agentic-adoption.md`, `blog-faros-claude-code-roi.md`,
`blog-bvp-shopify-ai-playbook.md`, and `paper-miller-speed-cost-quality.md`
were re-read directly (MINER.md §4b) and the claim numbers cited above were
confirmed against those notes' numbered `### Claim N:` headings (or, for
`guide/05-team-adoption.md`, against the actual prose/line range) before
writing this section.

- **Corroborates**:
  - `blog-thoughtworks-lopezfernandez-asymmetric-dialogue.md` Claim 6
    (three-step intentional dialogue loop: micro-blueprint, surgical
    feedback, micro-execution) and Claim 10 (a middle path between
    unstructured mega-prompting and heavyweight upfront specification):
    this source's Claims 11-12 (isolated fresh contexts don't reduce
    hallucinations, only reset them; multi-stage chat refinement
    consistently outperformed isolated single-pass execution) and Claim 5
    (heavy spec-kit-style upfront specification evaluated and found too
    costly for daily use) independently arrive at closely related
    conclusions from a different team and author.
  - `blog-thoughtworks-xiong-five-controllers-one-graph.md` Claim 7 (a Loop
    must close on an external authority, not the agent's own opinion) and
    Claim 9 (the graph — persistent memory — is explicitly not a
    controller): this source's Claim 10 (storing execution state in local
    files enabled auditing but did not prevent infinite loops; guardrails
    must live in skill definitions) is a concrete, implementation-level
    confirmation of Xiong's abstract claim that persistent memory and
    behavioral control are categorically separate concerns.
  - `failure-noemit-early-agentic-adoption.md` Lesson 1 and its root-cause
    discussion of context-window/prompt-literacy prerequisites: this
    source's Claim 3 reaches a similar diagnosis of early-adoption friction
    from a supported team rollout roughly two years after noemit's
    necessity-driven individual adoption.

- **Contradicts**: Filed as
  [issue #3522](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3522)
  (a refiling of #3520, which the intake pre-screen auto-closed for carrying
  no source URL in the issue body; #3522 is the live entry in the
  contradiction backlog and #3520 should be treated as dead) —
  this source's Claim 1 (~80% sustained productivity gain over an 8-month
  window, task-completion-count metric, still climbing at the end of the
  observation period) stresses the guide's existing synthesized "realistic
  ceiling is much lower than the vendor pitch" position in
  `guide/05-team-adoption.md` (10-30% range; "anything above 30% should be
  questioned and checked against a 6-month measurement window"; built on
  `blog-bvp-shopify-ai-playbook.md` Claim 5, `research-anthropic-ai-transforming-work.md`
  Claim 2, and `paper-miller-speed-cost-quality.md` Claims 1 and 4). See the
  filed issue for the full Side A/Side B breakdown; no verdict is picked
  here per MINER.md §4a. Notably, this source's *own* more granular Claim 8
  (a one-third complexity reduction on a medium story, diminishing on
  complex stories) is far closer in magnitude to the guide's existing
  10-30% ceiling than its own headline Claim 1 figure is — an internal
  tension within this single source's body of work that the resolver of
  #3522 may find useful.
  - Separately, not filed as a formal contradiction: this source's Claim 15
    (AI use paid off most for *complex* tasks; small tasks were often faster
    done manually) sits in tension with the general "AI works best on
    well-scoped, small tasks" framing common elsewhere in the corpus. Not
    filed per MINER.md §4a's "differ only in context" guidance — plausibly a
    task-complexity-vs-task-size conflation rather than a genuine
    disagreement, but worth the Smith's attention if citing both framings in
    the same section.

- **Extends**:
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 12
    (continuous-discipline thesis for evaluation): this source's overall
    narrative (three named architectural iterations before settling on a
    durable workflow) is a concrete illustration of the same
    continuous-refinement thesis, applied to workflow/context architecture.
  - `docs-github-copilot-usage-metrics-adoption-phase-review-velocity.md`
    and its sibling adoption-cohort notes: those document vendor-instrumented,
    API-level adoption metrics at scale; this source documents a single
    team's manually tracked task-completion metric plus granular single-story
    experiments, a qualitative complement to the quantitative-but-uninterpreted
    API metrics those notes describe.

- **Novel**:
  - **`spec-kit` named and evaluated, with quantified PR-size, documentation-volume,
    and story-point data** (Claims 5, 6, 7, 8, 9): no existing corpus source
    names or evaluates this specific specification framework; this is the
    first, and unusually well-quantified, data point on it in the corpus.
  - **"A storage layer does not prevent infinite loops" plus the "Fallacy of
    Stateless Context Isolation"** (Claims 10-11): a named, self-refuting
    experiment (the author explicitly tests and rejects their own prior
    hypothesis about fresh-context isolation reducing hallucinations) — a
    stronger evidentiary posture than most single-practitioner claims in the
    corpus.
  - **A concrete, dated "hidden context modification" incident** (Claim 13):
    a specific before/after policy-wording change (E2E test scope) caused by
    a model-writable local documentation copy, with a specific downstream
    consequence (unwanted negative-path test generation) — the first
    worked example in the corpus of this failure mode, rather than an
    abstract warning about it.
  - **A public reference implementation of a multi-repo, gated,
    fresh-context-per-task agent workflow** (Claim 14, `lightweight-jira-story-workflow`):
    a rare case of a narrative case study backed by an inspectable
    configuration repository rather than prose description alone.
  - **A rejection-ordered architecture narrative with a nuanced "customize,
    don't discard" verdict on spec-kit** (Claim 9): the deeper Substack
    source's actual recommendation is more moderate than the summary
    article's framing, a nuance worth preserving.

## Guide Impact

- **Chapter 05 (Team Adoption) — "Measuring impact" / "The realistic ceiling"
  section**: Do not add this source's ~80% headline figure directly to the
  ceiling synthesis without resolving
  [issue #3522](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3522)
  (supersedes the auto-closed #3520).
  If citing this source at all in that section, cite Claim 8's more modest,
  more mechanistic figure (~1 story point off a 3-point story, diminishing
  on complex stories) as a better-triangulated data point than the headline
  team-level throughput number, and note the internal tension between the
  two within the same author's own published work.
- **Chapter 05 — adoption-strategy section**: Add the weekly 2-hour
  structured workshop + unstructured sprint-embedded exploration cadence
  (Claim 4) as a concrete, reusable adoption-scheduling pattern.
- **Chapter 02 (Harness Engineering) — context/state architecture**: Add the
  rejection-ordered narrative (Concrete Artifacts) as a worked example of
  context-architecture evolution. Specifically add: (1) Claim 10's "a
  storage layer does not prevent infinite loops — guardrails belong in skill
  definitions" as a named caution against conflating auditability with
  safety; (2) Claim 11's "isolation resets the hallucination space, it
  doesn't reduce it" as a specific counter to the intuition that fresh
  contexts are inherently safer; (3) Claim 13's concrete Confluence
  scope-drift incident as the worked example for why reference documentation
  should be read via read-only links, not copied locally by the model; (4)
  the `lightweight-jira-story-workflow` gate/fresh-context pattern (Claim 14)
  as a reusable multi-repo orchestration structure.
- **Chapter 02 — specification-framework tradeoffs**: Add the quantified
  spec-kit-vs-custom-workflow PR-size and documentation-volume comparison
  (Claim 6, Concrete Artifacts) as the first quantified data point in the
  corpus on this specific tradeoff, paired with the more moderate "customize,
  don't discard" recommendation (Claim 9) and the annual documentation-bloat
  projection (~600 files/year) as a concrete cost to weigh against spec-kit's
  upfront design-constraint benefits.
- **Chapter 02 — task-scoping guidance**: Add Claim 15 (AI use paid off most
  for complex tasks; small tasks were often faster done manually) as an
  explicit counterpoint to existing "AI works best on well-scoped small
  tasks" guidance, flagging the likely conflation of task size and task
  complexity across sources.

## Extraction Notes

1. **WebFetch was not used for quote extraction; raw HTML was fetched
   directly instead.** Given this Miner's prior experience with
   inconsistent WebFetch quote reproduction on other Thoughtworks articles
   (documented in `blog-fowler-malykhin-archaeologist-copilot.md` Extraction
   Note 1), the primary article and all three linked pages were fetched
   directly via `curl` with a browser user-agent, HTML tags were stripped
   with a Python script, and the resulting text was read in full. Every
   quote in this note was copied character-for-character from that raw-text
   extraction.
2. **Three linked pages were followed and are load-bearing for this note**:
   two Substack posts by the same author
   (nikmalykhin.com/p/designing-ai-driven-development-workflows,
   nikmalykhin.com/p/assessing-file-stored-state-in-ai) and a public GitHub
   repository (github.com/nikmalykhin/lightweight-jira-story-workflow). Per
   MINER.md's "follow up to 5 linked pages that seem substantive," these
   were fetched because the primary Thoughtworks article's claims about
   spec-kit and local file-state storage were otherwise asserted without the
   underlying evidence; the linked posts turned out to contain the actual
   quantified experiments (PR file counts, word counts, story points, a
   named incident) behind those assertions. Roughly two-thirds of the
   claims in this note (Claims 6-14) derive from the linked pages rather
   than the primary article alone.
3. **Three separate, near-duplicate Prospector triage comments exist on the
   source issue** (#3509), each independently identifying the same core
   claims with minor differences in suggested chapter numbers. This note
   follows the actual chapter numbering in `guide/` (Chapter 05 = Team
   Adoption, Chapter 02 = Harness Engineering).
4. **One contradiction filed**: see Cross-References → Contradicts above and
   [issue #3522](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3522).
   It was first filed as #3520, which the intake pre-screen auto-closed and
   labeled `rejected` under criterion (a) ("No URL anywhere in the issue
   body") because the original body cited only `source-notes/` paths and
   guide line ranges. #3522 is the same contradiction refiled verbatim with
   the Thoughtworks article URL (plus the linked Substack/GitHub URLs) in
   the body; cite #3522, not #3520. No verdict is asserted in this note;
   the issue is left for human/Smith resolution per MINER.md §4a.
5. **Overall confidence rated `emerging`**, upgraded from an initial
   `anecdotal` assessment made before the linked Substack posts were
   fetched. The headline team-level productivity figure (Claim 1) remains
   individually `anecdotal` (single team, self-reported by the adoption
   champion, ungrounded story-count metric) and is the weakest load-bearing
   claim in the note — but the majority of the note's substantive content
   (Claims 6-14) is now backed by named, artifact-level experiments with
   specific quantified before/after comparisons (PR file counts, word
   counts, story-point deltas, a concrete documented incident, and a public,
   inspectable reference implementation), which is a materially higher
   evidence density than the primary Thoughtworks article alone would
   support. This mirrors the reasoning already used for `emerging` in
   `blog-fowler-malykhin-archaeologist-copilot.md` (same author): a single,
   unreplicated practitioner source can still earn `emerging` when it
   provides an unusually high density of independently checkable artifacts
   rather than summary-level assertions, even though its single most
   attention-grabbing number (Claim 1 here) does not itself clear that bar.
