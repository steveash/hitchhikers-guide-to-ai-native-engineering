---
source_url: https://addyosmani.com/blog/practical-loop-engineering/
source_type: blog-post
title: "Practical Loop Engineering"
author: Addy Osmani
date_published: 2026-08-14
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: emerging
issue: "#2913"
---

# Practical Loop Engineering

> A practitioner follow-up to Osmani's June "Loop Engineering" post that
> reframes loops around Anthropic's own four-type taxonomy (turn/goal/time/
> proactive), adds daily-driver tactics for delegation vs. supervision, a
> maker/checker near-miss anecdote, and operational fine print (spinning-loop
> detection, the 7-day recurring-loop expiry) drawn from running a PR-triage
> loop against an 80,000-star open source repo.

## Source Context

- **Type**: blog-post (personal blog, addyosmani.com; cross-posted from the
  author's Substack; published August 14, 2026)
- **Author credibility**: Addy Osmani is a Google Chrome/Google Cloud AI
  engineering leader and O'Reilly author (`Beyond Vibe Coding`), already
  represented in this corpus by `blog-addyosmani-loop-engineering.md` and
  `blog-addyosmani-code-agent-orchestra.md`. Unlike the June post, this
  article is framed in first person around the author's own daily workflow
  ("The way that I typically work...") and a named, verifiable project he
  maintains (the Agent Skills repository, "over 80,000 stars"). It also
  directly quotes and attributes a first-party framework to "the Claude Code
  team" rather than presenting the four-loop taxonomy as his own invention --
  the quoted material is reproduced from `blog-anthropic-getting-started-with-loops.md`
  (same four-type taxonomy, same worked examples, same `verify-frontend-change`
  skill), so this post's independent evidentiary value is the practitioner
  commentary and daily-workflow detail wrapped around that quoted framework,
  not the framework itself.
- **Scope**: Covers a redefinition of loop engineering around two Claude
  Code primitives (`/goal`, `/loop`); a verbatim reproduction of "the Claude
  Code team's" four-loop taxonomy (turn-based, goal-based, time-based,
  proactive) including their worked examples and the `verify-frontend-change`
  skill; the author's own delegation/supervision heuristics (5-10 agents
  daily, watch closely for security/auth/finance); a maker/checker anecdote
  where the author nearly merged AI-drafted competitive-gap PRs without
  reviewing the implementations closely; a real daily workflow (PR/issue
  triage on the Agent Skills repo) with worked `/loop` and combined
  `/loop`+`/goal` prompts; a "what loops don't buy you" section (vague goals,
  subjective/creative tasks); and closing operational fine print (spinning-
  loop detection heuristic, 7-day recurring-loop expiry, session-scoping
  with `--resume`/`--continue`). Does NOT cover: benchmarks, metrics, cost
  data, or any comparison of loop-assisted output quality against manual
  work -- this is a normative/anecdotal practitioner piece, like its June
  predecessor.

## Extracted Claims

### Claim 1: Osmani now frames loop engineering around two core Claude Code primitives -- `/goal` (drives a single bounded task to a measurable finish line) and `/loop` (reruns on a timer or fixed interval) -- a simplification from the five-primitive-plus-memory taxonomy in his June post
- **Evidence**: Author's direct reframing statement, contrasted implicitly
  with his own earlier taxonomy.
- **Confidence**: anecdotal (the author's own restated framing; not a new
  measured finding, and not reconciled explicitly against his June
  five-primitive taxonomy)
- **Quote**: "There are now basically two core primitives you can think
  about. In Claude Code you have a goal primitive, which can drive a single
  bounded task forward until you've got a particular goal, like a measurable
  finish line that's been met. And then loop reruns on a timer or a fixed
  interval, so you can use it to kind of schedule changes."
- **Our assessment**: This is a narrower frame than the June post's
  five-primitive-plus-memory taxonomy (`blog-addyosmani-loop-engineering.md`
  Claim 2: automations, worktrees, skills, plugins/connectors, sub-agents,
  plus memory). It is not a contradiction -- the two primitives named here
  (`/goal`, `/loop`) map onto that taxonomy's "automations" primitive and the
  goal-based/time-based rungs of Anthropic's own taxonomy -- but the note is
  worth flagging: this post narrows "loop engineering" from a five-part
  systems view down to two CLI commands the author reaches for daily. The
  guide should treat this as a simplified, task-level entry point rather
  than a replacement for the fuller structural taxonomy.

### Claim 2: Before loop primitives shipped as product features, loop engineering meant hand-rolling a bash loop, exemplified by the Ralph loop (Geoff Huntley), and was largely practiced on personal projects where failure had low cost
- **Evidence**: Author's own recollection of pre-primitive practice, naming
  a specific named pattern and its originator.
- **Confidence**: anecdotal (personal recollection, no dates or specific
  incident data)
- **Quote**: "I remember back before we had primitives baked into Claude
  Code and Codex, loop engineering was heavily about setting up your own
  bash loop, a hand-rolled thing. That's how I approached it. And you might
  remember earlier in the year, a number of us were playing around with the
  Ralph loop by Geoff Huntley."
- **Our assessment**: This directly corroborates
  `blog-addyosmani-loop-engineering.md` Claim 9 (loop primitives have moved
  from bespoke bash-script infrastructure to native product features) and
  its Linked Source 3 documentation of the Ralph loop reference
  implementation (attributed there to Geoffrey Huntley and Ryan Carson).
  This post adds a candid caveat not present in the June post: early
  experimentation was low-stakes because it happened "on some of our
  personal projects where, if we ran into a wall, it didn't really have a
  big cost to us." That caveat is directly relevant to the guide's framing
  of loop-adoption risk -- the author explicitly does not claim the same
  low-stakes tolerance applies to production or brownfield codebases (see
  Claim 3).

### Claim 3: Loop-engineering risk tolerance depends on codebase stakes -- an evergreen codebase without users or much historical complexity tolerates a loosely-supervised loop very differently than a brownfield codebase with real consequences (the author's example: a bank)
- **Evidence**: Direct qualifying statement following the bash-loop history,
  framed as a lesson learned from that lower-stakes experimentation period.
- **Confidence**: anecdotal (a single practitioner's stated heuristic, no
  incident data or comparative outcomes given)
- **Quote**: "you need to be very diligent, because loop engineering where
  you kind of leave it sitting alone, and you haven't really thought about
  whether the end goal or the constraints have been well defined, can leave
  you in a problematic state. This is why there's nuance when deciding to
  use it for an evergreen codebase without users or as much historical
  complexity vs. say a brownfield bank codebase."
- **Our assessment**: This is a specific, citable risk-conditioning
  heuristic not stated this explicitly in the June post or in
  `blog-anthropic-getting-started-with-loops.md` (whose closest equivalent,
  Claim 9, is the more generic "not all tasks require complex loops; start
  with the simplest solution"). The bank-vs-evergreen framing gives the
  guide a concrete axis (blast radius / historical complexity of the
  codebase) for deciding how much supervision a given loop warrants, beyond
  the task-type axis Anthropic's own post uses.

### Claim 4: Osmani reproduces the Claude Code team's own definition and four-type taxonomy of loops (turn-based/manual, goal-based, time-based, proactive) verbatim as the framework he now uses to think about loop design
- **Evidence**: Direct block-quoted reproduction of Anthropic's definitional
  statement and per-type descriptions, introduced with "Their write-up walks
  each rung."
- **Confidence**: settled (this is a verbatim reproduction of first-party
  Anthropic product guidance, already independently verified as settled in
  `blog-anthropic-getting-started-with-loops.md` Claim 1)
- **Quote**: "On the Claude Code team, we define loops as agents repeating
  cycles of work until a stop condition is met. We categorize a few
  different types of loops based on: how they are triggered, how they are
  stopped, what Claude Code primitive is used, what type of task is most
  appropriate for each. Not all tasks require complex loops; start with the
  simplest solution and use these patterns selectively."
- **Our assessment**: This is not new information to the corpus --
  `blog-anthropic-getting-started-with-loops.md` Claim 1 and Claim 9 already
  document this exact definition and caveat as first-party settled fact.
  Its value here is corroborative and adoption-signal: a second, independent
  high-signal practitioner is citing Anthropic's own taxonomy as his working
  model roughly six weeks after Anthropic published it, rather than
  proposing a competing framework. This strengthens confidence that the
  four-type taxonomy is becoming the standard vocabulary practitioners
  reach for, not just a vendor-side framing exercise.

### Claim 5: Osmani gives his own worked `/goal` example distinct from Anthropic's, adding an explicit no-regression constraint, a per-turn improvement requirement, and a stagnation-triggered abort condition in addition to a turn cap
- **Evidence**: A full worked `/goal` command the author presents as
  illustrative of how much more specific a goal prompt can be than
  Anthropic's simpler Lighthouse-score example.
- **Confidence**: anecdotal (a single illustrative example, not a
  documented production run with results)
- **Quote**: "/goal Refactor the data-fetching layer in Dashboard.tsx until
  Lighthouse performance score is >= 92 and LCP is under 1.8s as shown by
  the Lighthouse CLI output. Do not change the public API of any hooks.
  Each turn must improve at least one reported metric; abort if two
  consecutive turns show no improvement. Stop after 10 turns."
- **Our assessment**: This is a more sophisticated worked example than
  either Anthropic's own ("/goal get the homepage Lighthouse score to 90 or
  above, stop after 5 tries" -- `blog-anthropic-getting-started-with-loops.md`
  Concrete Artifacts) or Osmani's own June post, which did not include a
  worked `/goal` string. Three additions are worth extracting as a
  reusable pattern: (1) an explicit invariant ("do not change the public
  API"), (2) a monotonic-improvement requirement per turn, and (3) an
  early-abort condition on stagnation (two consecutive no-improvement
  turns) layered on top of a hard turn cap. This gives the guide a concrete
  template for writing goal prompts that guard against both runaway
  iteration and silent regressions, beyond the single-metric-threshold
  examples currently in the corpus.

### Claim 6: The evaluator model behind `/goal` does not judge whether the work is good -- it only checks the conversation transcript against the hard rules the user specified, so it is not a substitute for the human's own judgment of quality
- **Evidence**: Direct clarifying statement distinguishing the `/goal`
  evaluator from a human reviewer, made immediately after the worked
  `/goal` example.
- **Confidence**: emerging (a first-party-consistent mechanism claim, but
  stated by a practitioner rather than sourced to Anthropic directly in
  this post; it is consistent with, and sharpens, the mechanism Anthropic
  itself describes)
- **Quote**: "The evaluator sitting behind goal is not that checker, by the
  way. It doesn't look at the content to see if it's good or bad in any
  way, shape, or form. All it does is examine the conversation transcript
  to see if the hard rules you specified have been met."
- **Our assessment**: This is a sharper, more explicit statement of a
  distinction that `blog-anthropic-getting-started-with-loops.md` Claim 3
  implies but does not spell out this directly (Anthropic's own language is
  "an evaluator model checks your condition," without explicitly
  disclaiming that it does not assess quality). This is a genuinely useful
  clarification for the guide: practitioners should not treat a passing
  `/goal` run as equivalent to "a reviewer approved this" -- the evaluator
  enforces the letter of the stated rules, not the spirit or overall
  quality of the result. This directly motivates the maker/checker judgment
  anecdote in Claim 7.

### Claim 7: Osmani nearly merged AI-drafted competitive-gap PRs because he reviewed the agent's research closely but not the implementations, and on closer inspection found the changes would add complexity for users without much corresponding gain -- illustrating the difference between delegating a task and delegating judgment
- **Evidence**: First-person narrative anecdote describing a specific
  near-miss: tasking an agent to research competitor gaps and draft local,
  unpushed PRs, then almost pushing them based on reading the research but
  not the code.
- **Confidence**: anecdotal (single first-person incident, no counts or
  frequency data, self-reported after the fact)
- **Quote**: "I almost pushed some of those changes. But I didn't actually
  look at them closely enough. I read through its research, but I didn't
  look at the implementations closely enough. So I delegated the task, but
  I was close to delegating the judgment as well. Now, when I actually
  looked through the changes, what I realized is that it would introduce a
  lot of additional complexity for our users, for, I think personally, not
  all that much gain."
- **Our assessment**: This is the most concrete cautionary artifact in the
  post and a strong candidate for the guide's verification chapter -- it is
  a specific, self-reported failure-adjacent incident from a credible
  practitioner (not a hypothetical), and it names the precise failure
  mechanism: reading an agent's summary/research output feels like
  verification but is not the same as reviewing the actual generated
  artifact. It directly reinforces the maker/checker principle already
  well-corroborated in this corpus (`blog-addyosmani-loop-engineering.md`
  Claim 8, `blog-anthropic-getting-started-with-loops.md` Claim 6) but adds
  a distinct, narrower lesson those sources do not make explicit: even a
  practitioner who correctly uses a separate reviewing step can still
  under-verify if they only read the agent's narrative account of its own
  work rather than the artifact itself.

### Claim 8: Osmani runs 5-10 agents on a typical day but usually caps concurrent execution at about 5, and decides what to watch closely based on task sensitivity -- explicitly naming access to a system, authentication, and anything touching security or finance as triggers for closer supervision
- **Evidence**: Direct statement of daily practice and an explicit list of
  what raises supervision intensity.
- **Confidence**: anecdotal (self-reported personal workflow habits, not
  measured or comparative)
- **Quote**: "For me, I use probably between five and ten agents every day.
  Very typically I'll max out at about five concurrently." ... "If the task
  involves anything just a little bit sensitive, whether it is I've given
  this access to a system, or whether the feature happens to touch
  authentication, or something related to security or finance, I'll
  definitely be watching that closely."
- **Our assessment**: The "typically max out at about five concurrently"
  figure is consistent with, and slightly more specific than,
  `blog-addyosmani-code-agent-orchestra.md` Claim 8 ("WIP limits for agents
  should be 3-5 concurrent agents"), and with the review-bandwidth-ceiling
  argument in the June post's Linked Source 2 ("The Orchestration Tax" --
  human review capacity, not tooling, caps how many agents can run in
  parallel). The explicit named trigger list (system access, authentication,
  security, finance) for closer supervision is new, specific guidance not
  previously stated this concretely in the corpus -- it gives the guide a
  checklist rather than a vague "watch sensitive work more closely"
  instruction.

### Claim 9: Osmani's daily driver workflow is a scheduled PR/issue-triage loop on his Agent Skills open source repository (over 80,000 stars, previously up to 80-90 PRs/day to review), using `/loop every 1h` to summarize new issue urgency, and combining `/loop` with `/goal` to auto-fix labeled bugs and push branches
- **Evidence**: First-person description of a real, ongoing workflow with a
  specific project named and a specific historical review-volume figure,
  plus two worked prompt strings.
- **Confidence**: anecdotal (self-reported project and workflow; the "80 or
  90 pull requests... a day" figure is stated as a past historical peak,
  not necessarily the current volume, and no data on the triage loop's
  accuracy or false-positive rate is given)
- **Quote**: "I have a popular open source repository called Agent Skills.
  We've got over 80,000 stars, and up until recently we were getting
  anywhere up to like 80 or 90 pull requests that we had to review a day."
- **Additional quote (worked `/loop` example)**: "/loop every 1h \"Check the
  GitHub repository for any new open issues. Provide a bulleted summary of
  their urgency.\""
- **Additional quote (worked combined `/loop`+`/goal` example)**: "/loop
  every 24h \"Check GitHub for issues labeled 'bug'. If one exists, use
  /goal to implement a fix until all local tests pass and push the
  branch.\""
- **Our assessment**: This is a concrete, named, ongoing production use
  case -- a genuine existence proof for the "recurring streams of
  well-defined work: bug reports, issue triage, migrations, dependency
  upgrades" best-fit description that `blog-anthropic-getting-started-with-loops.md`'s
  proactive-loop row states abstractly. The two worked prompts are directly
  reusable templates for the guide's daily-workflows chapter, and the
  volume figure (80-90 PRs/day at peak) gives a concrete sense of the scale
  at which this pattern was adopted, not just a toy example.

### Claim 10: One concrete, reusable stopping condition Osmani uses for PR triage is closing PRs/issues that violate a specific, named contribution-guideline rule (the example given: the project does not accept translation contributions because the maintainers cannot verify all the languages)
- **Evidence**: Direct description of a real stopping condition used in
  production triage, with the underlying rationale for why the rule exists.
- **Confidence**: anecdotal (single named example from one project; no data
  on false-positive/false-negative rates for this specific rule)
- **Quote**: "we have a set of contribution guidelines, and our contribution
  guidelines include things like, hey, we currently don't accept
  translations." ... "if we tell it, close any issues or close any PRs
  which happen to touch that aspect of our contribution guidelines, that's
  something that can do really well when it's on that schedule."
- **Our assessment**: This is a good, concrete illustration of what
  "deterministic criteria" looks like for a judgment task (PR triage)
  rather than a metrics task (Lighthouse score, test pass count) --
  Anthropic's own examples of deterministic stopping conditions
  (`blog-anthropic-getting-started-with-loops.md` Claim 3) are all
  numeric/measurable; this example shows the same discipline applied to a
  categorical rule (does this PR touch a named, excluded contribution
  category) that a proactive loop can evaluate reliably because it maps to
  an explicit written policy, not a subjective judgment call.

### Claim 11: Loops are not a good fit for tasks without a clear, well-defined completion criterion -- vague goals ("keep going until this UI design is good") and tasks requiring human taste, subjective design judgment, or open-ended creative exploration are named as unsuitable
- **Evidence**: Direct statement under a dedicated "What loops don't buy
  you" section, with a specific counter-example of a vague goal.
- **Confidence**: settled (a clear-eyed limitation statement, consistent
  across every corpus source that discusses loop applicability -- treated
  as settled because it is corroborated independently by multiple
  first-party and practitioner sources, not because it is empirically
  measured)
- **Quote**: "Generally speaking if you don't have a clear idea of what the
  end-state/done/good means for your completion, it may not be the right
  pattern for your work. For example, a vague goal would be \"keep going
  until this UI design is good\". What does that mean? Good to who? How is
  it being evaluated? Tasks that require human taste, subjective design, or
  open-ended creative exploration aren't a good fit."
- **Our assessment**: This directly corroborates
  `blog-anthropic-getting-started-with-loops.md` Claim 9 ("not all tasks
  require complex loops; start with the simplest solution") and is
  consistent with `blog-addyosmani-loop-engineering.md` Claim 11 (loops do
  not remove the need for human judgment; verification, comprehension, and
  complacency get structurally harder, not easier). This post's specific
  contribution is the concrete "good to who?" framing for identifying a
  vague goal before writing it, which is a more actionable litmus test than
  the general caution in either prior source.

### Claim 12: A reliable heuristic for detecting a stuck/spinning loop is watching for the same command being retried with no change in result -- Osmani's rule of thumb is to stop after the third identical, unproductive retry
- **Evidence**: Direct statement of a practical detection heuristic under
  "The fine print."
- **Confidence**: anecdotal (a personal rule of thumb, no data on false
  positive rate or how often loops actually reach a third identical retry
  before self-terminating)
- **Quote**: "One classic sign that you've got a loop spinning in place is
  the same command being tried over and over without any change in the
  result. Give the same command a third time with no change from the
  second and it's probably time to stop."
- **Our assessment**: This corroborates and sharpens
  `blog-addyosmani-code-agent-orchestra.md` Claim 12 ("Kill stuck agents
  after 3+ iterations on the same error") -- both sources converge on
  roughly the same threshold (three unproductive repeats) as the trigger
  for manual intervention, from the same author across two different posts
  three months apart, applied here specifically to loop/goal stagnation
  rather than to general agent iteration. This is a reusable, low-cost
  detection rule the guide can state as a specific number rather than a
  vague "watch for it going in circles."

### Claim 13: Recurring loops expire seven days after creation (not three, which Osmani states he had previously been telling people), loops are session-scoped and stop when a new conversation starts, resuming a session with `--resume` or `--continue` restores any recurring task still inside its seven-day window, and anything that must outlive a session needs `/schedule` to run in the cloud
- **Evidence**: Direct, corrected statement of operational limits under
  "The fine print," including an explicit self-correction of a figure the
  author says he had previously stated publicly.
- **Confidence**: settled (a specific, falsifiable product-behavior claim
  presented as a correction of the author's own prior misstatement --
  self-correcting toward a more precise figure increases rather than
  decreases credibility here, though it is not independently confirmed
  against Anthropic's own documentation in this extraction)
- **Quote**: "One bit of fine print worth knowing. Recurring loops expire
  seven days after creation. I'd been telling people this was three days.
  It's seven. And loops are session-scoped, so they stop when you start a
  new conversation - though resuming that session with –resume or
  –continue brings back any recurring task still inside its seven-day
  window. If you need something that outlives your session, /schedule runs
  it in the cloud."
- **Our assessment**: This is a specific, operationally important detail
  not previously documented in this corpus at this level of precision --
  neither `blog-addyosmani-loop-engineering.md` nor
  `blog-anthropic-getting-started-with-loops.md` states a numeric
  expiration window for recurring `/loop` tasks, and neither documents the
  `--resume`/`--continue` interaction with an in-window recurring task.
  The self-correction ("I'd been telling people this was three days")
  is a data point about how easy it is for even a well-connected
  practitioner to circulate an inaccurate operational detail about these
  primitives -- worth a light caveat in the guide (verify current
  expiration windows against Anthropic's own docs before citing a specific
  number, since even practitioners close to the product have gotten this
  wrong once already). This is not a contradiction under MINER.md §4a: no
  other corpus source states a three-day (or any) figure for the guide to
  conflict with, and the "three days" claim was never published in this
  corpus -- it is the author correcting an unpublished, previously-spoken
  claim of his own within the same post, not two claims in tension in the
  source text itself.

## Concrete Artifacts

### The `verify-frontend-change` skill, reproduced verbatim from Anthropic's post

```
Source: Addy Osmani, "Practical Loop Engineering," quoting "the Claude Code
team" (originally from Anthropic's "Getting started with loops," already
documented in blog-anthropic-getting-started-with-loops.md, Concrete
Artifacts -- reproduced here character-for-character as it appears in this
post)

---
name: verify-frontend-change
description: Verify any UI change end-to-end before declaring it done.
---
# Verifying frontend changes
Never report a UI change as complete based on a successful edit alone.
Verify it the way a human reviewer would:
1. Start the dev server and open the edited page in the browser.
2. Interact with the change directly. For a new control (button, input,
   toggle): click it, confirm the expected state change, and screenshot
   before/after.
3. Check the browser console: zero new errors or warnings.
4. Use the Chrome Devtools MCP, run a performance trace and audit
   Core Web Vitals.
If any step fails, fix the issue and rerun from step 1 - do not hand
back partially verified work.
```

### The composed proactive-loop example, reproduced verbatim from Anthropic's post

```
Source: Addy Osmani, "Practical Loop Engineering," quoting "the Claude Code
team" (also documented in blog-anthropic-getting-started-with-loops.md,
Claim 5 / Concrete Artifacts)

The primitives above, along with other Claude Code features like auto mode
and dynamic workflows (research preview) can be composed into a loop for
long-running work. For example, to handle incoming feedback, you can use:
/schedule (research preview) to run a routine that checks for new reports,
/goal to define what done looks like, and skills to document how to verify
it. Dynamic workflows to orchestrate agents that triage each report, fix
it, and review the fix. Auto mode so the routine runs without stopping to
ask for permission.

Putting it together, a prompt could look like this: /schedule every hour:
check the project-feedback channel for bug reports. /goal: don't stop
until every report found this run is triaged, actioned, and responded to.
When fixing a bug, use a workflow to explore three solutions in parallel
worktrees and have a judge adversarially review them.
```

### Osmani's own worked prompts (original to this post)

```
Source: Addy Osmani, "Practical Loop Engineering," https://addyosmani.com/blog/practical-loop-engineering/

Specific /goal example with invariant + stagnation abort + turn cap:
/goal Refactor the data-fetching layer in Dashboard.tsx until Lighthouse
performance score is >= 92 and LCP is under 1.8s as shown by the
Lighthouse CLI output. Do not change the public API of any hooks. Each
turn must improve at least one reported metric; abort if two consecutive
turns show no improvement. Stop after 10 turns.

Hourly issue-triage /loop:
/loop every 1h "Check the GitHub repository for any new open issues.
Provide a bulleted summary of their urgency."

Combined /loop + /goal for bug-labeled issues:
/loop every 24h "Check GitHub for issues labeled 'bug'. If one exists,
use /goal to implement a fix until all local tests pass and push the
branch."
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-loop-engineering.md` Claim 9 (loop primitives shipped
    as native product features, replacing bespoke bash infrastructure) and
    its Linked Source 3 (Ralph loop, Geoffrey Huntley) -- this post's Claim
    2 independently restates the same bash-loop-to-native-primitive history
    and names the same originator, from the same author two months later.
  - `blog-addyosmani-loop-engineering.md` Claim 8 (splitting the writer
    from the checker is the most useful structural element of a loop) and
    `blog-anthropic-getting-started-with-loops.md` Claim 6 (a second
    reviewing agent with fresh context is less biased) -- this post's
    Claim 7 (the near-miss competitive-gap PR anecdote) and its framing
    ("not letting the agent that did the work decide the work is good...
    One sub-agent drafts the change. A separate one verifies it") restate
    the same maker/checker principle, with a specific first-person
    incident illustrating what happens when that discipline is only
    partially applied.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 8 (WIP limits should be
    3-5 concurrent agents) -- this post's Claim 8 ("Very typically I'll max
    out at about five concurrently") independently restates a nearly
    identical figure from the same author roughly five months later.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 12 (kill stuck agents
    after 3+ iterations on the same error) -- this post's Claim 12 (stop
    after the third identical, unproductive command retry) restates the
    same three-repeat threshold, applied specifically to loop/goal
    stagnation.
  - `blog-anthropic-getting-started-with-loops.md` Claim 1 (loops defined
    as agents repeating cycles of work until a stop condition is met) and
    Claim 9 (not all tasks require complex loops) -- this post's Claim 4
    quotes the same definition verbatim, and Claim 11 restates the same
    "not a good fit for vague/subjective goals" caution with a sharper
    "good to who?" litmus test.

- **Contradicts**: None filed. The one candidate considered was Claim 13's
  self-correction ("I'd been telling people this was three days. It's
  seven.") against MINER.md §4a's "a source disagrees with itself" trigger.
  This was evaluated and rejected: the "three days" figure was never
  published in this corpus or, as far as this extraction can determine, in
  any prior written source -- it is the author correcting an unpublished,
  previously-spoken claim of his own, not two claims in tension within the
  source text itself, and no existing corpus source states a conflicting
  expiration figure for `/loop` to genuinely contradict. No contradiction
  issue filed.

- **Extends**:
  - `blog-anthropic-getting-started-with-loops.md`: that post documents the
    four-loop taxonomy, its worked examples, and the verification-skill
    template as first-party product guidance; this post is a second,
    independent practitioner adopting that exact taxonomy as his working
    model six weeks later and wrapping it in daily-workflow detail
    (concrete supervision heuristics, a named production use case, an
    operational correction on the 7-day expiry) that the original
    announcement-style post does not and could not contain.
  - `blog-addyosmani-loop-engineering.md`: extends the June post's
    five-primitive taxonomy with a narrower two-primitive (`/goal`/`/loop`)
    daily-practice frame (Claim 1), a codebase-risk-tolerance axis not
    present in June (Claim 3), and a named, ongoing production loop (Claim
    9) where the June post's worked example was hypothetical/illustrative
    prose rather than a named, running system.
  - `blog-addyosmani-code-agent-orchestra.md`: extends Claim 8 (WIP limits)
    and Claim 12 (kill stuck agents after 3+ iterations) with restated,
    loop-specific versions of the same numeric thresholds five months
    later, suggesting these are stable heuristics for this author rather
    than one-off figures.

- **Novel**:
  - **The codebase-risk-tolerance axis (Claim 3)**: evergreen/no-users
    codebases vs. brownfield/high-consequence codebases (the author's named
    example: a bank) as a distinct dimension for deciding how much
    supervision a loop warrants -- not stated this explicitly in any prior
    corpus source on loop applicability.
  - **The evaluator-does-not-judge-quality clarification (Claim 6)**: the
    explicit statement that `/goal`'s evaluator checks only stated hard
    rules against the transcript, not content quality -- sharper than the
    mechanism description in `blog-anthropic-getting-started-with-loops.md`
    Claim 3.
  - **The near-miss maker/checker anecdote (Claim 7)**: a specific,
    first-person, self-reported incident of under-verification (reading
    research but not implementations) is new to the corpus -- prior
    maker/checker claims are structural/architectural, not incident-based.
  - **Named supervision triggers (Claim 8)**: system access, authentication,
    security, and finance as an explicit checklist for when to watch an
    agent more closely, rather than a general "watch sensitive work"
    instruction.
  - **A named, running production PR/issue-triage loop with real prompts
    and a historical volume figure (Claim 9, Claim 10)**: the Agent Skills
    repository (80,000+ stars, up to 80-90 PRs/day at peak) is the first
    named, ongoing (not hypothetical) production loop deployment in this
    corpus with worked prompt strings attached.
  - **The 7-day recurring-loop expiration window and the
    `--resume`/`--continue` interaction with in-window recurring tasks
    (Claim 13)**: a specific operational limit not previously documented at
    this precision anywhere in the corpus, including a candid
    self-correction of a previously-circulated wrong figure.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add Claim 9's two worked prompts
  (hourly issue-triage `/loop`, combined `/loop`+`/goal` bug-fix-and-push)
  as concrete, reusable templates for a scheduled triage workflow, citing
  the named production use case (Agent Skills repo) as an existence proof
  rather than a hypothetical. Pair with Claim 10's categorical-rule
  stopping-condition example (contribution-guideline violations) to show
  deterministic stopping conditions are not limited to numeric metrics.

- **Chapter 02 (Harness Engineering)**: Add Claim 5's worked `/goal`
  example as a template showing three composable guard patterns in one
  prompt (an explicit invariant, a per-turn monotonic-improvement
  requirement, and a stagnation-triggered early abort layered under a hard
  turn cap) -- more sophisticated than the single-threshold `/goal`
  examples currently sourced from `blog-anthropic-getting-started-with-loops.md`.
  Add Claim 12's "stop after the third identical, unproductive retry"
  heuristic as a specific, numeric spinning-loop detection rule.

- **Chapter 03 (Verification)**: Add Claim 6 (the `/goal` evaluator checks
  only stated hard rules, not content quality) as an explicit caution
  against treating a passing goal-run as equivalent to human review. Add
  Claim 7 (the near-miss competitive-gap PR anecdote) as a first-person
  cautionary case study for the maker/checker section: reading an agent's
  research/summary output is not the same as reviewing the artifact it
  produced, even when a nominal review step occurred.

- **Chapter 05 (Team Adoption)**: Add Claim 8's named supervision-trigger
  checklist (system access, authentication, security, finance) as concrete
  guidance for teams setting delegation policy, alongside the existing
  3-5-concurrent-agent WIP-limit guidance from
  `blog-addyosmani-code-agent-orchestra.md`. Add Claim 3's codebase-risk
  axis (evergreen vs. brownfield/high-consequence) as a second dimension
  for scoping which repositories or workstreams are appropriate for
  loosely-supervised loop adoption.

- **Chapter 02 (Harness Engineering) -- operational limits**: Add Claim
  13's 7-day recurring-loop expiration and session-scoping/`--resume`
  interaction as a specific operational detail practitioners should know
  before relying on `/loop` for anything long-running, with the explicit
  caveat (per this source's own self-correction) that this figure should
  be re-verified against Anthropic's current documentation before being
  stated as settled fact in the guide.

## Extraction Notes

- Full article text was fetched and returned verbatim (title through the
  closing author bio and copyright line), not summarized -- every `Quote`
  field above was copied character-for-character from that fetched text.
  The article's Substack cross-post notice, book-promotion callout, and
  author bio were excluded from claim extraction as non-substantive
  content, consistent with the pattern in prior notes for this author.
- No sub-pages were followed. Unlike Osmani's June post, this article does
  not contain further self-referential links to other Osmani posts beyond
  a mention of his June "Loop Engineering" post (already a dedicated corpus
  source, `blog-addyosmani-loop-engineering.md`) and his O'Reilly book
  promotion (not a substantive technical link).
- This post reproduces substantial verbatim material from Anthropic's
  "Getting started with loops" post (the four-loop taxonomy, the
  `verify-frontend-change` skill, and the composed proactive-loop example)
  under the framing "the Claude Code team's take." Those reproduced
  passages are treated in this note as corroboration of the already-settled
  `blog-anthropic-getting-started-with-loops.md` claims (see Claim 4 and
  Concrete Artifacts), not as new evidence -- the guide should continue to
  cite the original Anthropic post as the primary source for that
  taxonomy and reserve citations to this post for the practitioner-specific
  material (Claims 1-3, 5-13).
- All claim numbers cited from other source notes
  (`blog-addyosmani-loop-engineering.md` Claims 2, 8, 9, 11;
  `blog-addyosmani-code-agent-orchestra.md` Claims 8, 12;
  `blog-anthropic-getting-started-with-loops.md` Claims 1, 3, 6, 9) were
  verified by re-reading the cited note and locating the numbered heading
  before citing -- no claim number was guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified. The
  one candidate (Claim 13's self-correction of a previously-stated,
  unpublished 3-day figure) was evaluated and rejected because no existing
  corpus source states a conflicting figure, and the "disagreement" is
  between an unpublished spoken claim and this post's own corrected text,
  not between two claims present in citable source material. See
  Cross-References -> Contradicts above for the full reasoning.
