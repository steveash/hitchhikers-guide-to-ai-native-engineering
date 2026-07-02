---
source_url: https://claude.com/blog/getting-started-with-loops
source_type: blog-post
title: "Getting started with loops"
author: Delba de Oliveira and Michael Segner
date_published: 2026-06-30
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: emerging
issue: "#1433"
---

# Getting started with loops

> Official Claude Code team guidance defining a four-loop progression model —
> turn-based, goal-based (`/goal`), time-based (`/loop`/`/schedule`), and
> proactive — mapping each type to trigger, stop condition, and best-fit task,
> with practical code-quality and token-management guidance for composing them.

## Source Context

- **Type**: blog-post (official claude.com/blog product/practice guidance,
  published June 30, 2026; ~5 minute read)
- **Author credibility**: Written by Delba de Oliveira and Michael Segner,
  published under Category "Claude Code" / Product "Claude Code" on
  Anthropic's own blog. This is first-party guidance from the team that
  builds the product being described — maximum authority for what the
  primitives (`/goal`, `/loop`, `/schedule`, dynamic workflows, auto mode) do
  and how they compose, but it is prescriptive practice guidance rather than
  a benchmarked study: no metrics, no controlled comparisons, no named
  customer case study are included.
- **Scope**: Covers a definitional framing of "loop" (agents repeating cycles
  of work until a stop condition is met), a four-type taxonomy classified by
  trigger/stop/primitive/best-fit-task, one worked example per loop type, a
  worked composed-loop example combining all four primitives, a
  "maintaining code quality" section (five practices), a "managing token
  usage" section (six practices including the `/usage` and `/workflows`
  commands), and a closing summary table plus a getting-started checklist.
  Does NOT cover: implementation internals of `/goal`'s evaluator model,
  pricing or quota details for `/schedule`, or metrics/case studies
  demonstrating the progression model's effectiveness in practice.

## Extracted Claims

### Claim 1: The Claude Code team defines a loop as agents repeating cycles of work until a stop condition is met, and classifies loop types along four axes
- **Evidence**: Author's opening definitional framing, presented as the
  organizing principle for the rest of the post.
- **Confidence**: settled (first-party definitional statement from the team
  that builds the product; not a measured claim, but authoritative framing)
- **Quote**: "On the Claude Code team, we define loops as agents repeating cycles of work until a stop condition is met. We categorize a few different types of loops based on:"
- **Our assessment**: This defines "loop" independently of the specific CLI
  primitives that implement it, which is useful groundwork — it separates
  the abstract concept (cyclical work with a stop condition) from any one
  implementation (`/loop`, `/schedule`, dynamic workflows). The four
  classification axes named directly after this quote are: how triggered,
  how stopped, what Claude Code primitive is used, and what task type fits.
  This four-axis framing is the organizing structure the rest of the
  article's taxonomy claims (2-5 below) instantiate.

### Claim 2: Turn-based loops are the default manual loop — user-triggered, self-judged stop condition, best for shorter non-recurring tasks, improved by encoding verification as skills
- **Evidence**: Structured feature description (Triggered by / Stop criteria
  / Best used for / Managed usage by) plus a worked example (asking Claude to
  create a like button) and a full `SKILL.md` example for self-verification.
- **Confidence**: settled (describes the baseline behavior of every Claude
  Code interactive session, not a new or unverified feature)
- **Quote**: "Every prompt you send starts a manual loop with you directing each turn. Claude gathers context, takes action, checks its work, repeats if needed, and responds. We call this the agentic loop."
- **Our assessment**: This is the least novel of the four loop types (it
  describes ordinary interactive use) but it is the article's baseline for
  the stated progression: "Move from turn-based to goal-based to time-based
  to proactive" is the framing the Prospector's triage flagged as the
  distinctive contribution of this source. The recommendation to encode
  manual verification steps as a `SKILL.md` so Claude can "check more of its
  own work, end-to-end" directly extends
  `blog-anthropic-claude-code-skills-lessons.md` Claim 10 (skill
  descriptions function as trigger specifications) with a loop-specific use
  case: skills as the self-verification layer for the simplest loop type,
  not just a context-loading mechanism.

### Claim 3: Goal-based loops (`/goal`) extend iteration by having a separate evaluator model check a user-defined success condition after every turn, rather than letting the generating agent decide when it is done
- **Evidence**: Structured feature description plus a worked example prompt.
- **Confidence**: settled (first-party mechanism description of a shipped
  CLI command)
- **Quote**: "When you define the success criteria, Claude doesn't have to make a determination on what is "good enough" and end the loop early. Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work until the goal is met or a number of turns you define is reached."
- **Additional quote (worked example)**: "/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries."
- **Our assessment**: This is a direct, first-party confirmation of the
  generator/evaluator split already documented in the corpus as an
  architectural pattern. `blog-anthropic-harness-long-running.md` Claim 2
  states the generator/evaluator split "outperforms prompting a single agent
  to self-critique," and `blog-addyosmani-loop-engineering.md` Claim 4
  (quoting Osmani) independently described `/goal` the same way ("a fresh
  model decides if the loop is done instead of the one that did the work").
  This source is the first in the corpus to state the mechanism as an
  official product description rather than a practitioner's inference about
  what `/goal` does "under the hood" — it corroborates and confirms, at
  first-party authority, what was previously only practitioner-observed.

### Claim 4: Time-based loops trigger on an interval via `/loop` (local) and `/schedule` (cloud), and are best suited to recurring work or monitoring external systems that change independently of the agent
- **Evidence**: Structured feature description plus two worked examples (a
  recurring interval prompt and the local-to-cloud migration path).
- **Confidence**: settled (first-party mechanism description of shipped CLI
  commands)
- **Quote**: "For these, you can trigger when Claude runs with `/loop` which re-runs a prompt on an interval. For example: /loop 5m check my PR, address review comments, and fix failing CI `/loop` runs on your computer, so if you turn it off, it stops. You can move the loop to the cloud by creating a routine with `/schedule`."
- **Our assessment**: The `/loop`-runs-locally / `/schedule`-runs-in-the-cloud
  distinction directly corroborates `blog-anthropic-claude-code-routines.md`
  Claim 6 ("The CLI `/schedule` command now creates scheduled routines on
  Anthropic's cloud infrastructure"), confirming from a second, more recent
  (June 30, 2026 vs. April 14, 2026) first-party source that `/schedule` is
  the graduation path from a local, session-bound `/loop` to a persistent
  cloud routine. No new mechanism is introduced beyond what the Routines
  note already documents (quotas, three-axis trigger taxonomy), but this
  source frames the relationship the other way around: not "routines are a
  new product surface" but "`/schedule` is what `/loop` becomes when you
  need it to survive you turning your laptop off."

### Claim 5: Proactive loops compose `/schedule`, `/goal`, dynamic workflows, and auto mode into a single unattended pipeline for recurring, well-defined work streams like bug triage and dependency upgrades
- **Evidence**: Structured feature description plus a single worked composed
  example prompt combining all four primitives.
- **Confidence**: emerging (a compositional recommendation combining four
  separately-shipped features; the article states this as intended usage
  but provides no case study or metrics demonstrating it in production)
- **Quote**: "The primitives above, along with other Claude Code features like auto mode and dynamic workflows (research preview) can be composed into a loop for long-running work."
- **Additional quote (composed example)**: "/schedule every hour: check #project-feedback for bug reports. /goal: don't stop until every report found this run is triaged, actioned, and responded to. When fixing a bug, use a workflow to explore three solutions in parallel worktrees and have a judge adversarially review them."
- **Our assessment**: This is the most concrete artifact in the source and
  the clearest evidence for the Prospector's "progression model" framing —
  it is the only place in the article where all four loop types collapse
  into one composed primitive stack. It directly names dynamic workflows as
  "(research preview)," consistent with
  `blog-anthropic-dynamic-workflows-claude-code.md`'s own status label, and
  the "have a judge adversarially review them" phrase maps onto that same
  note's Claim 3 (built-in verification-before-return) and
  `blog-anthropic-harness-long-running.md`'s generator/evaluator
  architecture generally. This is a template worth extracting into the
  guide directly (see Concrete Artifacts and Guide Impact below) — it is
  the single densest example of composing loop primitives currently in the
  corpus.

### Claim 6: Maintaining loop output quality depends on five system-level practices: a clean codebase, self-verification skills, reachable docs, a second reviewing agent, and encoding individual failures into system-wide fixes
- **Evidence**: First-party bulleted practice list under "Maintaining code
  quality," including a named tool reference (`/code-review` skill or "Code
  Review for Github").
- **Confidence**: emerging (a practice recommendation from the product team,
  not independently measured, though internally consistent with other
  first-party guidance in the corpus)
- **Quote**: "Use a second agent for code reviews: A reviewer with fresh context is less biased and not influenced by the main agent's reasoning. You can use the built-in `/code-review` skill or Code Review for Github."
- **Additional quote**: "When an individual result doesn't meet the standard, don't stop at fixing the individual issue, try to encode it to improve the system for all future iterations."
- **Our assessment**: The "second agent, fresh context, unbiased by the
  first agent's reasoning" framing for code review is the same
  generator/evaluator principle stated yet a third way (after `/goal`'s
  evaluator model and dynamic workflows' adversarial judge). The
  "encode individual failures into the system" recommendation is a distinct
  claim not reducible to the generator/evaluator pattern — it argues that
  *loop maintenance itself* should be a feedback loop (fix the specific bug,
  then update the skill/CLAUDE.md/hook so the same failure class doesn't
  recur), which is directly the "ratchet" practice attributed to Addy
  Osmani's linked-source material in
  `blog-addyosmani-loop-engineering.md` ("Every line in a good `AGENTS.md`
  should be traceable back to a specific thing that went wrong" — cited
  there as Linked Source 1, not a numbered claim in that note itself, so
  cited by section name per MINER.md 4b). This source restates the same
  discipline applied to loops generally, not just `AGENTS.md` authorship.

### Claim 7: Managing token usage in loops requires six practices: right-sized primitive/model choice, explicit success criteria, piloting before large runs, scripts over reasoning for deterministic work, interval-matching, and active usage review via `/usage` and `/workflows`
- **Evidence**: First-party bulleted practice list under "Managing token
  usage," naming two specific CLI commands (`/usage`, `/workflows`) and
  their specific reporting granularity.
- **Confidence**: settled (the two named commands and what they report are
  factual, verifiable product behavior, not a subjective recommendation)
- **Quote**: "Pilot before a large run: Dynamic workflows can spawn hundreds of agents. Gauge usage on a smaller slice of the work first."
- **Additional quote**: "Review usage: The `/usage` command breaks down recent usage by skills, subagents, and MCPs, `/goal` with no arguments shows number of turns and token usage so far, `/workflows` shows each agent's token usage and you can stop an agent at any time."
- **Our assessment**: The "Dynamic workflows can spawn hundreds of agents"
  line directly corroborates
  `blog-anthropic-dynamic-workflows-claude-code.md` Claim 1's "tens to
  hundreds of parallel subagents" language and Claim 8's token-cost
  warning ("Dynamic workflows can consume substantially more tokens than a
  typical Claude Code session") — this source adds the concrete mitigation
  ("pilot on a smaller slice first") that the dynamic-workflows
  announcement itself only gestured at ("start with scoped tasks"). The
  `/usage` and `/workflows` commands as named, callable usage-inspection
  tools are new to the corpus — no existing source note documents these
  specific commands or their reporting granularity (skills/subagents/MCPs
  breakdown for `/usage`; per-agent token usage plus a stop-any-agent
  control for `/workflows`).

### Claim 8: The four loop types form an explicit progression from turn-based (hand off the check) through goal-based (hand off the stop condition) and time-based (hand off the trigger) to proactive (hand off the prompt itself)
- **Evidence**: A summary table at the end of the article ("To summarize")
  with four columns (Loop / You hand off / Use it when / Reach for) and one
  row per loop type, followed by a getting-started checklist.
- **Confidence**: emerging (a synthesis/summary framing constructed by the
  authors to close the piece; useful as an organizing device but not itself
  a new mechanism or measured finding)
- **Quote**: "To summarize: Loop / You hand off / Use it when / Reach for / Turn-based / The check / You're exploring or deciding / Custom verification skills / Goal-based / The stop condition / You know what done looks like / /goal / Time-based / The trigger / The work happens outside your project on a schedule / /loop, /schedule / Proactive / The prompt / The work is recurring and well-defined / All of the above, and dynamic workflows"
- **Our assessment**: This table is the clearest statement of the
  "progression model" the Prospector's triage asked to have extracted. Each
  row names a specific thing being delegated to the loop (the check, the
  stop condition, the trigger, the prompt itself) rather than framing
  progression as merely "more automation" — this is a more precise
  organizing axis than existing corpus taxonomies. It complements rather
  than duplicates `blog-addyosmani-loop-engineering.md`'s five-primitive
  taxonomy (automations, worktrees, skills, plugins/connectors, sub-agents):
  Osmani's taxonomy answers "what structural pieces does a loop need,"
  while this table answers "which piece of judgment am I delegating, and in
  what order should I learn to delegate it." Both are complementary
  organizing frames for the same underlying primitives, not competing
  claims.

### Claim 9: Not all tasks require complex loops — practitioners should start with the simplest loop type and adopt more complex ones selectively, not by default
- **Evidence**: A direct qualifying statement placed immediately after the
  article's opening definitional framing, before any of the four loop types
  are introduced.
- **Confidence**: settled (an explicit editorial caution from the authors,
  not a claim requiring external verification)
- **Quote**: "Not all tasks require complex loops; start with the simplest solution and use these patterns selectively."
- **Our assessment**: This caution positions the whole article as a
  progression *menu*, not a maturity ladder practitioners are expected to
  climb to the top of. It tempers the "move from turn-based to goal-based to
  time-based to proactive" framing the Prospector highlighted: the article
  does not argue proactive loops are strictly better, only that they suit a
  narrower, more specific task profile (recurring, well-defined work). This
  is a useful corrective for the guide to preserve — pairing the progression
  table (Claim 8) with this caution prevents the guide from reading as "more
  autonomous is always the goal."

### Claim 10: Recommended self-verification skills should be as quantitative as possible, giving Claude tools or connectors to see, measure, or interact with the result rather than relying on static code review alone
- **Evidence**: A worked `SKILL.md` example (`verify-frontend-change`) with a
  four-step verification procedure including browser interaction,
  screenshotting, console-error checking, and a Core Web Vitals audit via
  Chrome DevTools MCP.
- **Confidence**: emerging (a specific worked example illustrating a general
  principle, not a benchmarked comparison of quantitative vs. qualitative
  verification skills)
- **Quote**: "The more quantitative the checks are, the easier it is for Claude to self-verify."
- **Our assessment**: This principle, plus its worked example, is the most
  concrete, reusable artifact in the article (see Concrete Artifacts below
  for the full `SKILL.md` text). It operationalizes
  `blog-anthropic-claude-code-skills-lessons.md`'s general skills guidance
  with a loop-specific instance: a skill written explicitly to let Claude
  self-judge whether a UI change is actually done, closing the same
  self-evaluation gap that `blog-anthropic-harness-long-running.md` Claim 1
  documents as a general model failure mode ("agents tend to respond by
  confidently praising the work — even when, to a human observer, the
  quality is obviously mediocre"). The instruction "If any step fails, fix
  the issue and rerun from step 1 — do not hand back partially verified
  work" is a concrete anti-pattern guard worth citing directly in the
  guide's verification chapter.

## Concrete Artifacts

### Four-loop taxonomy (Triggered by / Stop criteria / Best used for / Managed usage by)

```
Source: "Getting started with loops," claude.com/blog, June 30, 2026

TURN-BASED
  Triggered by:     A user prompt.
  Stop criteria:    Claude judges it has completed the task or needs
                     additional context.
  Best used for:    Shorter tasks that are not part of a regular process
                     or schedule.
  Managed usage by: Write specific prompts and improve verification using
                     skills to reduce the number of turns.

GOAL-BASED (/goal)
  Triggered by:     A manual prompt in real-time.
  Stop criteria:    Goal achieved OR maximum number of turns reached.
  Best used for:    Tasks that have verifiable exit criteria.
  Managed usage by: Setting a specific completion criteria and explicit
                     turn caps, "stop after 5 tries."

TIME-BASED (/loop and /schedule)
  Triggered by:     A specified time interval.
  Stop criteria:    You cancel it, or the work completes (the PR merges,
                     the queue is empty).
  Best used for:    For recurring work, or interfacing with external
                     environments / systems.
  Managed usage by: Set longer intervals or react based on events rather
                     than time.

PROACTIVE
  Triggered by:     An event or schedule, with no human in real time.
  Stop criteria:    Each task exits when its goal is met. The routine
                     itself runs until you turn it off.
  Best used for:    Recurring streams of well-defined work: bug reports,
                     issue triage, migrations, dependency upgrades, etc.
  Managed usage by: Routing routines to smaller, faster models and using
                     the most capable model for judgment calls.
```

### Worked example prompts (one per loop type, verbatim)

```
Source: "Getting started with loops," claude.com/blog, June 30, 2026

Goal-based:
  /goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.

Time-based:
  /loop 5m check my PR, address review comments, and fix failing CI

Proactive (composed):
  /schedule every hour: check #project-feedback for bug reports. /goal:
  don't stop until every report found this run is triaged, actioned, and
  responded to. When fixing a bug, use a workflow to explore three
  solutions in parallel worktrees and have a judge adversarially review
  them.
```

### `verify-frontend-change` SKILL.md (verbatim)

```
Source: "Getting started with loops," claude.com/blog, June 30, 2026
(worked example under "Turn-based loops")

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
4. Use the Chrome Devtools MCP, run a performance trace and audit Core Web
   Vitals.
If any step fails, fix the issue and rerun from step 1 — do not hand back
partially verified work.
```

### Closing summary table

```
Source: "Getting started with loops," claude.com/blog, June 30, 2026

Loop         | You hand off      | Use it when                                          | Reach for
-------------|--------------------|-------------------------------------------------------|------------------------------
Turn-based   | The check          | You're exploring or deciding                           | Custom verification skills
Goal-based   | The stop condition | You know what done looks like                          | /goal
Time-based   | The trigger        | The work happens outside your project on a schedule    | /loop, /schedule
Proactive    | The prompt         | The work is recurring and well-defined                 | All of the above, and dynamic workflows
```

### Token-usage inspection commands (verbatim description)

```
Source: "Getting started with loops," claude.com/blog, June 30, 2026

"The /usage command breaks down recent usage by skills, subagents, and
MCPs, /goal with no arguments shows number of turns and token usage so
far, /workflows shows each agent's token usage and you can stop an agent
at any time."
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-loop-engineering.md` Claim 4 ("`/goal` keeps going
    until a condition you wrote is actually true, and after every turn a
    separate small model checks whether you are done, so the agent that
    wrote the code isnt the one grading it"): this source's Claim 3 states
    the identical mechanism ("an evaluator model checks your condition")
    from first-party authority, upgrading it from practitioner inference to
    official product description.
  - `blog-anthropic-claude-code-routines.md` Claim 6 (the CLI `/schedule`
    command creates cloud-hosted routines): this source's Claim 4
    independently confirms the same local-`/loop`-to-cloud-`/schedule`
    relationship from a second, more recent first-party post.
  - `blog-anthropic-dynamic-workflows-claude-code.md` Claim 1 ("tens to
    hundreds of parallel subagents") and Claim 8 (substantially higher
    token cost, "start with scoped tasks"): this source's Claim 7
    ("Dynamic workflows can spawn hundreds of agents. Gauge usage on a
    smaller slice of the work first") restates both the scale and the
    mitigation using near-identical language, and Claim 5's composed
    example explicitly labels dynamic workflows "(research preview),"
    matching that note's own status designation.
  - `blog-anthropic-harness-long-running.md` Claim 1 (models "confidently
    praise mediocre work" when self-evaluating) and Claim 2 (generator/
    evaluator split outperforms self-critique): this source's Claim 3
    (`/goal`'s separate evaluator model) and Claim 6 ("a reviewer with
    fresh context is less biased and not influenced by the main agent's
    reasoning") restate the same architectural principle as shipped,
    user-facing primitives rather than custom harness components.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 10 (the skill
    description field is a trigger specification): this source's Claim 2
    extends that note's general skills guidance with a loop-specific
    application — encoding manual verification steps as a `SKILL.md` so
    the turn-based loop can self-verify without a human present for every
    check.

- **Extends**:
  - `blog-addyosmani-loop-engineering.md`: that note's five-primitive
    taxonomy (automations, worktrees, skills, plugins/connectors,
    sub-agents, plus memory) answers "what structural pieces does a loop
    need"; this source's four-type progression table (Claim 8) answers a
    different, complementary question — "which piece of judgment (the
    check, the stop condition, the trigger, the prompt) does a
    practitioner hand off next, and in what order should they learn to."
    Neither taxonomy supersedes the other; the guide should present both
    as different cuts through the same primitive set.
  - `blog-anthropic-claude-code-routines.md`: that note documents Routines
    as a standalone scheduling/trigger product surface (three-axis
    taxonomy, plan-tier quotas); this source recontextualizes `/schedule`
    as one step in a four-step practitioner progression rather than a
    freestanding feature announcement, adding the missing "why would I
    reach for this, and what comes before/after it" framing that a pure
    feature announcement does not provide.
  - Osmani's "the ratchet" practice, cited via `blog-addyosmani-loop-engineering.md`
    Linked Source 1 section (not a numbered claim in that note — "Every
    line in a good `AGENTS.md` should be traceable back to a specific
    thing that went wrong"): this source's Claim 6 ("try to encode it to
    improve the system for all future iterations") restates the same
    ratchet discipline as a general loop-maintenance practice, not
    specifically tied to `AGENTS.md` authorship.

- **Contradicts**: None found. No claim in this source opposes an existing
  corpus claim on the same topic; where this source overlaps with
  `blog-addyosmani-loop-engineering.md` and
  `blog-anthropic-claude-code-routines.md`, it corroborates or extends
  rather than conflicts (see above).

- **Novel**:
  - **The explicit four-type progression table** (Claim 8: turn-based →
    goal-based → time-based → proactive, each defined by what judgment is
    handed off) is new to the corpus. No existing source frames loop
    adoption as a staged progression with a named thing delegated at each
    stage.
  - **`/usage` and `/workflows` as named, callable token-inspection
    commands** (Claim 7) with specific reporting granularity (skills/
    subagents/MCPs breakdown; per-agent token usage with a stop control)
    are not documented in any existing corpus source.
  - **The `verify-frontend-change` `SKILL.md` worked example** (Claim 10)
    is a complete, concrete, reusable skill template not present elsewhere
    in the corpus — most existing skill-related sources describe skills
    structurally (`blog-anthropic-claude-code-skills-lessons.md`) rather
    than providing a full worked verification skill.
  - **The single composed proactive-loop prompt** (Claim 5) combining
    `/schedule`, `/goal`, dynamic workflows, and adversarial review in one
    string is the densest example in the corpus of stacking multiple loop
    primitives into one instruction.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the four-type progression table
  (Claim 8) as a decision aid for practitioners choosing a loop type,
  paired with Claim 9's caution ("not all tasks require complex loops")
  so it reads as a menu of fit-for-purpose options rather than a maturity
  ladder to climb by default. Cross-reference
  `blog-addyosmani-loop-engineering.md`'s five-primitive taxonomy as the
  complementary "what structural pieces" answer to this table's "what
  judgment am I delegating" answer.

- **Chapter 02 (Harness Engineering)**: Add the `verify-frontend-change`
  `SKILL.md` (Claim 10, full text in Concrete Artifacts) as a concrete,
  citable template for encoding self-verification into turn-based loops,
  and add the explicit principle "the more quantitative the checks are,
  the easier it is for Claude to self-verify" as guidance for writing new
  verification skills. Cross-reference the "if any step fails... do not
  hand back partially verified work" instruction as a concrete
  anti-shortcut guard practitioners can copy directly.

- **Chapter 02 (Harness Engineering) — token/cost management**: Add the
  six token-management practices from Claim 7, specifically naming `/usage`
  and `/workflows` as concrete commands for auditing loop cost — this is
  more actionable than the existing corpus's qualitative "substantially
  more tokens" warning from `blog-anthropic-dynamic-workflows-claude-code.md`,
  since it gives practitioners a specific command to run rather than only a
  caution to heed.

- **Chapter 03 (Verification)**: Add Claim 3's first-party confirmation of
  `/goal`'s evaluator-model mechanism as the settled (not merely
  practitioner-inferred) version of the generator/evaluator claim already
  in the guide via `blog-anthropic-harness-long-running.md`. Update any
  existing citation of the Osmani-sourced `/goal` description to note it
  is now independently confirmed by Anthropic's own guidance.

- **Chapter 05 (Team Adoption)**: Add Claim 6's "second agent for code
  review... built-in `/code-review` skill or Code Review for Github" and
  the "encode individual failures into system-wide fixes" ratchet practice
  as concrete team-level recommendations for maintaining loop output
  quality as adoption scales past a single practitioner's manual review
  capacity.

## Extraction Notes

- WebFetch's summarization pass returned only a lossy paraphrase of this
  article (headings and rough claim gist, no verbatim text usable for
  quoting). The full article was instead retrieved via `curl` against the
  live page, stripped of scripts/styles, and converted to plain text with a
  Python regex-based tag-stripper, preserving the article's exact wording
  including its own quotation marks and dashes. Every `Quote` field above
  was copied character-for-character from that extracted plain text, not
  reconstructed from the WebFetch summary.
- The full body was read end-to-end, from the opening framing through the
  closing "Getting started" checklist and FAQ. The "Related posts" section
  (unrelated post teasers) and the surrounding site chrome (nav, cookie
  banner, "Get Claude Code" install instructions) were excluded as
  non-article content.
- No sub-pages were followed. The article's closing line references
  "the loop, schedule, goal, and dynamic workflows pages" in the Claude
  Code docs as further reading, but does not link them inline as
  hypertext in the fetched HTML in a way that resolved to distinct URLs
  worth an independent fetch within this extraction's scope; a follow-up
  extraction of the dedicated `/goal`, `/loop`, and `/schedule` docs pages
  (if they exist as separate, citable sources) would add implementation
  detail this announcement-style post does not cover.
- No contradiction with existing corpus notes was found; see
  Cross-References above. `confidence_overall` is set to `emerging` rather
  than `settled` because, while the individual command mechanics
  (`/goal`, `/loop`, `/schedule`, `/usage`, `/workflows`) are settled
  first-party feature facts, the article's central contribution — the
  four-stage progression model itself (Claim 8) — is prescriptive practice
  guidance from the vendor, not a measured or independently validated
  claim about how practitioners actually progress through these stages.
- Cross-references to `blog-addyosmani-loop-engineering.md`,
  `blog-anthropic-claude-code-routines.md`,
  `blog-anthropic-dynamic-workflows-claude-code.md`,
  `blog-anthropic-harness-long-running.md`, and
  `blog-anthropic-claude-code-skills-lessons.md` were all verified by
  reading the cited claim numbers in the actual source-note files before
  writing this note; the one non-numbered citation (Osmani's "ratchet"
  practice) is cited by its "Linked Source 1" section name per MINER.md
  4b, not as a fabricated claim number.
